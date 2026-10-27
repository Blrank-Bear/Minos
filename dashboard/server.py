#!/usr/bin/env python3
"""Minos SN107 mining dashboard: JSON API + static UI, standard library only.

Run inside WSL from the project root:
  .venv/bin/python dashboard/server.py [--port 8787] [--host 127.0.0.1]
then open http://localhost:8787 in the Windows browser.

Reads everything from this project folder (data/rounds, data/replays,
configs/, git history) plus the public Minos API/MCP for live round data.
Long work (replays, downloads, upstream checks) runs as queued jobs whose
state and logs persist under data/jobs/.
"""
import argparse
import hashlib
import json
import os
import queue
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import traceback
import urllib.request
import uuid
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT / "minos_subnet"
STATIC = Path(__file__).resolve().parent / "static"
DATA = ROOT / "data"
ROUNDS = DATA / "rounds"
RESULTS = DATA / "replays" / "results.jsonl"
JOBS_DIR = DATA / "jobs"
JOURNAL = DATA / "journal.jsonl"
TUNE = DATA / "tune"
TUNE_STATE = TUNE / "state.json"
TUNE_EVENTS = TUNE / "events.jsonl"
TUNED_CONF = ROOT / "configs" / "gatk-tuned.conf"
CONFIGS = ROOT / "configs"
STATE = ROOT / "state"
PY = ROOT / ".venv" / "bin" / "python"
API = "https://api.theminos.ai"
TOOLS = ("gatk", "deepvariant", "bcftools")

sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(REPO))


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return default


def read_jsonl(path: Path) -> list:
    out = []
    try:
        with path.open() as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        out.append(json.loads(line))
                    except ValueError:
                        pass
    except OSError:
        pass
    return out


def run(cmd, cwd=ROOT, timeout=30) -> str:
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout).stdout
    except (OSError, subprocess.SubprocessError):
        return ""


# --------------------------------------------------------------------------
# Cached external data
# --------------------------------------------------------------------------
class TTLCache:
    def __init__(self):
        self._lock = threading.Lock()
        self._data = {}

    def get(self, key, ttl, fn):
        with self._lock:
            hit = self._data.get(key)
            if hit and time.time() - hit[0] < ttl:
                return hit[1]
        try:
            value = fn()
        except Exception as e:  # noqa: BLE001 - external data is best-effort
            value = {"error": f"{type(e).__name__}: {e}"}
            if hit:  # serve stale rather than nothing
                value = {**hit[1], "stale": True} if isinstance(hit[1], dict) else hit[1]
        with self._lock:
            self._data[key] = (time.time(), value)
        return value


CACHE = TTLCache()


def http_json(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "minos-dashboard"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def mcp_call(tool, **kw):
    from minos_mcp import MinosMCP
    return MinosMCP(timeout=30).call(tool, **kw)


def live_data():
    def fetch():
        out = {"fetched_at": now_iso()}
        try:
            out["current"] = mcp_call("get_current_round")
        except Exception as e:  # noqa: BLE001
            out["current"] = {"error": str(e)}
        try:
            out["recent"] = mcp_call("list_recent_rounds", limit=20)
        except Exception as e:  # noqa: BLE001
            out["recent"] = {"error": str(e)}
        try:
            out["network_config"] = http_json(f"{API}/scoring/network-config")
        except Exception as e:  # noqa: BLE001
            out["network_config"] = {"error": str(e)}
        try:
            out["health"] = http_json(f"{API}/health", timeout=10)
        except Exception as e:  # noqa: BLE001
            out["health"] = {"status": "unreachable", "error": str(e)}
        return out
    return CACHE.get("live", 25, fetch)


# --------------------------------------------------------------------------
# Rounds and replays
# --------------------------------------------------------------------------
def dir_size(path: Path) -> int:
    total = 0
    for p in path.rglob("*"):
        try:
            if p.is_file():
                total += p.stat().st_size
        except OSError:
            pass
    return total


def leaderboard_stats(board):
    scores = sorted((e["combined_final"] for e in board if e.get("combined_final") is not None), reverse=True)
    if not scores:
        return {}
    pick = lambda q: scores[min(len(scores) - 1, int(q * len(scores)))]  # noqa: E731
    return {"top1": scores[0], "top5": scores[min(4, len(scores) - 1)], "median": pick(0.5),
            "p90": pick(0.9), "scored": len(scores), "spread_top5": scores[0] - scores[min(4, len(scores) - 1)]}


def local_rounds():
    out = []
    if not ROUNDS.exists():
        return out
    for rd in sorted(ROUNDS.iterdir(), reverse=True):
        rec = read_json(rd / "round.json")
        if not rec:
            continue
        meta = read_json(rd / "meta.json", {}) or {}
        board = meta.get("leaderboard") or []
        winner = board[0] if board else {}
        out.append({
            "dir": rd.name,
            "round_id": rec.get("round_id"),
            "region": meta.get("region"),
            "chromosome": meta.get("chromosome"),
            "finalized": bool(meta.get("finalized")),
            "submission_count": meta.get("submission_count"),
            "files_ok": all((rd / n).exists() for n in ("input.bam", "truth.vcf.gz", "mutations.vcf.gz")),
            "bam_mb": round((rd / "input.bam").stat().st_size / 1e6, 1) if (rd / "input.bam").exists() else None,
            "winner_uid": winner.get("uid"),
            "winner_hotkey": winner.get("hotkey"),
            "commitments": len(rec.get("commitments") or []) if isinstance(rec.get("commitments"), list) else None,
            **leaderboard_stats(board),
        })
    return out


def results():
    # Subregion (slice) replays are screening data, not comparable with the
    # round leaderboard; keep them out of the replay tables and summaries.
    return [r for r in read_jsonl(RESULTS) if not r.get("subregion")]


def replay_summary(rows):
    """Per config label: averages over its latest result per round."""
    latest = {}
    for r in rows:
        latest[(r.get("label"), r.get("config_hash"), r.get("round"))] = r
    groups = {}
    for (label, chash, _), r in latest.items():
        groups.setdefault((label, chash), []).append(r)
    out = []
    for (label, chash), rs in groups.items():
        ok = [r for r in rs if r.get("ok")]
        placed = [r for r in ok if r.get("rank")]
        mean = lambda xs: sum(xs) / len(xs) if xs else None  # noqa: E731
        out.append({
            "label": label, "config_hash": chash, "tool": rs[0].get("tool"),
            "rounds": len(rs), "ok": len(ok), "failed": len(rs) - len(ok),
            "mean_score": mean([r["score"] for r in ok]),
            "mean_gap": mean([r["gap"] for r in placed]),
            "mean_rank": mean([r["rank"] for r in placed]),
            "best_rank": min((r["rank"] for r in placed), default=None),
            "wins": sum(1 for r in placed if r["rank"] == 1),
            "top5": sum(1 for r in placed if r["rank"] <= 5),
            "max_calling_seconds": max((r.get("calling_seconds") or 0 for r in ok), default=None),
            "mean_calling_seconds": mean([r["calling_seconds"] for r in ok if r.get("calling_seconds")]),
            "last_run": max(r.get("ts") or "" for r in rs),
        })
    out.sort(key=lambda s: (s["mean_gap"] is None, -(s["mean_gap"] or -9)))
    return out


# --------------------------------------------------------------------------
# Configs
# --------------------------------------------------------------------------
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")


def param_defs(tool):
    from templates import tool_params as tp
    return {"gatk": tp.GATK_QUALITY_PARAMS, "deepvariant": tp.DEEPVARIANT_QUALITY_PARAMS,
            "bcftools": tp.BCFTOOLS_QUALITY_PARAMS}[tool]


def parse_conf(text):
    opts = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip()
        if v.lower() in ("true", "false"):
            opts[k] = v.lower() == "true"
            continue
        for conv in (int, float):
            try:
                opts[k] = conv(v)
                break
            except ValueError:
                pass
        else:
            opts[k] = v
    return opts


def conf_tool(name, opts):
    """Infer the tool of a config: name prefix first, then parameter overlap."""
    for t in TOOLS:
        if name.startswith(t) or f"-{t}" in name:
            return t
    best, overlap = "gatk", -1
    for t in TOOLS:
        n = len(set(opts) & set(param_defs(t)))
        if n > overlap:
            best, overlap = t, n
    return best


def opts_hash(opts):
    return hashlib.sha256(json.dumps(opts, sort_keys=True).encode()).hexdigest()[:12]


def validate(tool, opts):
    from templates.tool_params import validate_and_build_flags
    r = validate_and_build_flags(tool, opts)
    return {"valid": r["valid"], "errors": r.get("errors") or [], "flags": r.get("flags") or []}


def list_configs():
    live = {t: parse_conf((REPO / "configs" / f"{t}.conf").read_text())
            for t in TOOLS if (REPO / "configs" / f"{t}.conf").exists()}
    out = []
    for p in sorted(CONFIGS.glob("*.conf")):
        opts = parse_conf(p.read_text())
        tool = conf_tool(p.stem, opts)
        out.append({
            "name": p.stem, "tool": tool, "options": opts, "hash": opts_hash(opts),
            "is_live": live.get(tool) == opts, "modified": datetime.fromtimestamp(
                p.stat().st_mtime, timezone.utc).isoformat(timespec="seconds"),
            "validation": validate(tool, opts),
        })
    return {"configs": out, "live": {t: {"hash": opts_hash(o), "options": o} for t, o in live.items()}}


def write_conf(path: Path, tool, opts, note=""):
    defs = param_defs(tool)
    lines = [f"# {tool} config saved by the Minos dashboard {now_iso()}"]
    if note:
        lines += [f"# {l}" for l in note.splitlines()]
    for k in defs:
        if k in opts:
            v = opts[k]
            lines.append(f"{k}={'true' if v is True else 'false' if v is False else v}")
    for k, v in opts.items():  # unknown keys kept so validation can flag them
        if k not in defs:
            lines.append(f"{k}={v}")
    path.write_text("\n".join(lines) + "\n")


# --------------------------------------------------------------------------
# Jobs
# --------------------------------------------------------------------------
class Jobs:
    """Serial job queue; replays are CPU-heavy, so one runs at a time."""

    def __init__(self):
        JOBS_DIR.mkdir(parents=True, exist_ok=True)
        self.q = queue.Queue()
        self.lock = threading.Lock()
        self.proc = None
        self.jobs = {}
        for p in JOBS_DIR.glob("*.json"):
            j = read_json(p)
            if j:
                if j.get("status") in ("queued", "running"):
                    j["status"] = "interrupted"  # server restarted mid-job
                    self._save(j)
                self.jobs[j["id"]] = j
        threading.Thread(target=self._worker, daemon=True).start()

    def _save(self, job):
        (JOBS_DIR / f"{job['id']}.json").write_text(json.dumps(job, indent=2))

    def log_path(self, jid):
        return JOBS_DIR / f"{jid}.log"

    def submit(self, kind, params):
        jid = datetime.now().strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:4]
        job = {"id": jid, "kind": kind, "params": params, "status": "queued", "created": now_iso(),
               "started": None, "finished": None, "progress": 0, "total": 1, "summary": "", "cancel": False}
        with self.lock:
            self.jobs[jid] = job
            self._save(job)
        self.q.put(jid)
        return job

    def cancel(self, jid):
        with self.lock:
            job = self.jobs.get(jid)
            if not job or job["status"] not in ("queued", "running"):
                return False
            job["cancel"] = True
            if job["status"] == "queued":
                job["status"] = "cancelled"
                job["finished"] = now_iso()
            self._save(job)
            proc = self.proc if job["status"] == "running" else None
        if proc and proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
            except OSError:
                pass
        return True

    def list(self):
        with self.lock:
            return sorted(self.jobs.values(), key=lambda j: j["created"], reverse=True)

    def _sh(self, job, cmd, log):
        log.write(f"$ {' '.join(map(str, cmd))}\n")
        log.flush()
        proc = subprocess.Popen(list(map(str, cmd)), cwd=ROOT, stdout=log, stderr=subprocess.STDOUT,
                                text=True, start_new_session=True)
        with self.lock:
            self.proc = proc
        rc = proc.wait()
        with self.lock:
            self.proc = None
        return rc

    def _worker(self):
        while True:
            jid = self.q.get()
            job = self.jobs.get(jid)
            if not job or job["status"] != "queued":
                continue
            job.update(status="running", started=now_iso())
            self._save(job)
            try:
                with self.log_path(jid).open("a") as log:
                    getattr(self, f"_run_{job['kind']}")(job, log)
                if job["cancel"]:
                    job["status"] = "cancelled"
                elif job["status"] == "running":
                    job["status"] = "done"
            except Exception:  # noqa: BLE001
                job["status"] = "failed"
                with self.log_path(jid).open("a") as log:
                    log.write(traceback.format_exc())
            job["finished"] = now_iso()
            self._save(job)

    def _run_replay(self, job, log):
        p = job["params"]
        cfg = CONFIGS / f"{p['config']}.conf"
        rounds = p["rounds"]
        job["total"] = len(rounds)
        ok = 0
        for i, rd in enumerate(rounds):
            if job["cancel"]:
                break
            job["summary"] = f"round {i + 1}/{len(rounds)}: {rd}"
            self._save(job)
            log.write(f"\n=== [{i + 1}/{len(rounds)}] {rd} ===\n")
            rc = self._sh(job, [PY, "scripts/score_round.py", ROUNDS / rd, "--config", cfg,
                                "--tool", p.get("tool", "gatk"), "--threads", p.get("threads", 2),
                                "--memory-gb", p.get("memory_gb", 6),  # leave RAM for a concurrent tuner
                                "--label", p["config"], "--job", job["id"]], log)
            ok += rc == 0
            job["progress"] = i + 1
            self._save(job)
        job["summary"] = f"{ok}/{job['progress']} rounds scored"

    def _run_fetch_rounds(self, job, log):
        rc = self._sh(job, ["bash", "scripts/fetch_rounds.sh", "--last", int(job["params"].get("last", 20))], log)
        if rc == 0 and not job["cancel"]:
            rc = self._sh(job, [PY, "scripts/fetch_round_meta.py"], log)
        job["progress"] = 1
        job["summary"] = "rounds + metadata updated" if rc == 0 else f"exit code {rc}"
        if rc != 0:
            job["status"] = "failed"

    def _run_fetch_meta(self, job, log):
        rc = self._sh(job, [PY, "scripts/fetch_round_meta.py"], log)
        job["progress"] = 1
        job["summary"] = "metadata updated" if rc == 0 else f"exit code {rc}"
        if rc != 0:
            job["status"] = "failed"

    def _run_upstream_check(self, job, log):
        rc = self._sh(job, ["git", "-C", REPO, "fetch", "--quiet", "origin"], log)
        behind = run(["git", "-C", str(REPO), "rev-list", "--count", "HEAD..@{u}"]).strip()
        log.write(f"upstream commits not yet pulled: {behind or '?'}\n")
        log.write(run(["git", "-C", str(REPO), "log", "--oneline", "HEAD..@{u}"]))
        job["progress"] = 1
        job["summary"] = f"{behind or '?'} new upstream commit(s)" if rc == 0 else f"git fetch failed ({rc})"
        if rc != 0:
            job["status"] = "failed"


JOBS = None


# --------------------------------------------------------------------------
# Logs, journal and system
# --------------------------------------------------------------------------
def git_log(repo: Path, n=50):
    fmt = "%H%x1f%h%x1f%aI%x1f%an%x1f%s%x1f%b%x1e"
    raw = run(["git", "-C", str(repo), "log", f"-{n}", f"--pretty=format:{fmt}"])
    out = []
    for rec in raw.split("\x1e"):
        parts = rec.strip("\n").split("\x1f")
        if len(parts) == 6:
            out.append(dict(zip(("hash", "short", "date", "author", "subject", "body"), parts)))
    return out


def logs_data():
    behind = run(["git", "-C", str(REPO), "rev-list", "--count", "HEAD..@{u}"]).strip()
    return {
        "project": git_log(ROOT),
        "project_dirty": run(["git", "status", "--short"]).splitlines(),
        "upstream": git_log(REPO, 25),
        "upstream_behind": int(behind) if behind.isdigit() else None,
        "upstream_dirty": run(["git", "-C", str(REPO), "status", "--short"]).splitlines(),
        "journal": list(reversed(read_jsonl(JOURNAL))),
    }


def pid_alive(pid) -> bool:
    try:
        os.kill(int(pid), 0)
    except (OSError, TypeError, ValueError):
        return False
    try:  # a finished child we never reaped still answers kill(0): check for zombie
        return Path(f"/proc/{int(pid)}/stat").read_text().split(")")[-1].split()[0] != "Z"
    except OSError:
        return True


def deliverable(path: Path, label: str):
    rel = str(path.relative_to(ROOT))
    if not path.exists():
        return {"name": label, "path": rel, "exists": False, "status": "not created yet"}
    last = run(["git", "log", "-1", "--pretty=format:%h%x1f%aI%x1f%s", "--", rel]).split("\x1f")
    dirty = bool(run(["git", "status", "--short", "--", rel]).strip())
    return {
        "name": label, "path": rel, "exists": True,
        "modified": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(timespec="seconds"),
        "committed": last[0] or None, "commit_date": last[1] if len(last) > 1 else None,
        "commit_subject": last[2] if len(last) > 2 else None,
        "uncommitted": dirty, "status": "uncommitted changes" if dirty else ("committed" if last[0] else "untracked"),
    }


def tune_data():
    state = read_json(TUNE_STATE, {}) or {}
    alive = pid_alive(state.get("pid")) if state else False
    if state.get("status") in ("running", "starting", "stopping") and not alive:
        state["status"] = "dead"  # process gone without writing a final status
    events = read_jsonl(TUNE_EVENTS)[-300:]
    autopilot = read_json(TUNE / "autopilot.json", {}) or {}
    autopilot["alive"] = pid_alive(autopilot.get("pid")) if autopilot else False
    autopilot["log"] = list(reversed(read_jsonl(TUNE / "autopilot_log.jsonl")[-120:]))
    if autopilot.get("status") in ("running", "starting", "stopping") and not autopilot["alive"]:
        autopilot["status"] = "dead"
    validation = read_json(TUNE / "validation.json", {}) or {}
    if validation.get("status") == "running" and not pid_alive(validation.get("pid")):
        validation["status"] = "dead"
    return {
        "state": state, "alive": alive, "events": list(reversed(events)), "validation": validation,
        "autopilot": autopilot,
        "deliverables": [
            deliverable(TUNED_CONF, "Tuned GATK config"),
            deliverable(ROOT / "scripts" / "tune.py", "Tuner"),
            deliverable(ROOT / "dashboard" / "static" / "app.js", "Dashboard UI"),
            deliverable(ROOT / "scripts" / "score_round.py", "Replay scorer"),
        ],
        "live_config": parse_conf((REPO / "configs" / "gatk.conf").read_text()) if (REPO / "configs" / "gatk.conf").exists() else {},
    }


def tune_start(body):
    state = read_json(TUNE_STATE, {}) or {}
    if state and pid_alive(state.get("pid")) and state.get("status") in ("running", "starting", "stopping"):
        return {"error": "tuner already running"}, 409
    cmd = [str(PY), "scripts/tune.py", "--workers", "1", "--deploy"]  # one test at a time (user rule)
    if body.get("resume", True) and state.get("best"):
        cmd.append("--resume")
        if body.get("new_pass"):
            cmd.append("--new-pass")
    TUNE.mkdir(parents=True, exist_ok=True)
    log = (TUNE / "tuner.log").open("a")
    proc = subprocess.Popen(cmd, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    threading.Thread(target=proc.wait, daemon=True).start()  # reap it when it exits
    return {"started": " ".join(cmd[1:])}, 200


def autopilot_start(body):
    ap = read_json(TUNE / "autopilot.json", {}) or {}
    if ap and pid_alive(ap.get("pid")) and ap.get("status") in ("running", "starting", "stopping"):
        return {"error": "autopilot already running"}, 409
    cmd = [str(PY), "scripts/autopilot.py", "--workers", "1"]  # one test at a time (user rule)
    if body.get("start"):
        cmd += ["--start", *[str(Path(s)) for s in body["start"]]]
    if body.get("reset"):
        cmd.append("--reset")
    if body.get("focus_round"):
        cmd += ["--focus-round", Path(str(body["focus_round"])).name]
        if body.get("focus_slice"):
            cmd.append("--focus-slice")
    if body.get("mode") in ("single", "global"):
        cmd += ["--mode", body["mode"]]
    if body.get("batch"):
        cmd += ["--batch", str(int(body["batch"]))]
    TUNE.mkdir(parents=True, exist_ok=True)
    log = (TUNE / "autopilot.log").open("a")
    proc = subprocess.Popen(cmd, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    threading.Thread(target=proc.wait, daemon=True).start()
    return {"started": " ".join(cmd[1:])}, 200


def autopilot_stop():
    ap = read_json(TUNE / "autopilot.json", {}) or {}
    if not pid_alive(ap.get("pid")):
        return {"error": "autopilot not running"}, 409
    os.kill(int(ap["pid"]), signal.SIGTERM)
    return {"stopping": ap["pid"]}, 200


def tune_stop():
    state = read_json(TUNE_STATE, {}) or {}
    pid = state.get("pid")
    if not pid_alive(pid):
        return {"error": "tuner not running"}, 409
    os.kill(int(pid), signal.SIGTERM)  # tuner finishes the round batch in flight, then stops
    return {"stopping": pid}, 200


def env_settings():
    env = {}
    p = REPO / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip()
    keep = ("NETUID", "WALLET_NAME", "WALLET_HOTKEY", "MINER_TEMPLATE", "MINOS_SUBMIT_ONLY", "MINER_DEMO",
            "PLATFORM_URL", "STORAGE_PRIMARY_BACKEND", "MINER_PAY_FOR_RESUBMISSIONS")
    return {k: env.get(k) for k in keep}


def system_data():
    def fetch():
        images = [l.split("\t") for l in run(["docker", "image", "ls", "--format",
                                              "{{.Repository}}:{{.Tag}}\t{{.Size}}"]).splitlines() if l]
        refs = sorted((p.name for p in (REPO / "datasets" / "reference").glob("chr*")
                       if (p / f"{p.name}.fa").exists()), key=lambda c: int(c[3:]) if c[3:].isdigit() else 99)
        du = shutil.disk_usage(ROOT)
        miner = run(["pgrep", "-af", "neurons.miner|neurons/miner.py"]).strip().splitlines()
        pm2 = shutil.which("pm2") is not None
        bt_ver = run([str(PY), "-c", "import importlib.metadata as m; print(m.version('bittensor'))"]).strip()
        return {
            "fetched_at": now_iso(),
            "docker": {"ok": bool(images), "images": images},
            "reference_chromosomes": refs,
            "disk": {"free_gb": round(du.free / 1e9, 1), "total_gb": round(du.total / 1e9, 1),
                     "rounds_gb": round(dir_size(ROUNDS) / 1e9, 2) if ROUNDS.exists() else 0},
            "miner_processes": [m for m in miner if "pgrep" not in m],
            "pm2": pm2,
            "bittensor": bt_ver or None,
            "env": env_settings(),
            "wallet_present": any((ROOT / "wallets").glob("*/hotkeys/*")) if (ROOT / "wallets").exists() else False,
            "cpus": os.cpu_count(),
        }
    return CACHE.get("system", 60, fetch)


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(STATIC), **kw)

    def end_headers(self):
        # Static files: revalidate every load so UI edits show up immediately.
        if not self.path.startswith("/api/"):
            self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):  # quieter console
        if not self.path.startswith("/api/"):
            return
        sys.stderr.write("%s %s\n" % (self.command, self.path))

    def _json(self, obj, status=200):
        body = json.dumps(obj, default=str).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}") if n else {}

    def do_GET(self):
        u = urlparse(self.path)
        if not u.path.startswith("/api/"):
            return super().do_GET()
        try:
            parts = u.path.strip("/").split("/")[1:]
            qs = parse_qs(u.query)
            if parts == ["live"]:
                return self._json(live_data())
            if parts == ["rounds"]:
                return self._json({"rounds": local_rounds()})
            if len(parts) == 2 and parts[0] == "rounds":
                rd = ROUNDS / Path(parts[1]).name
                meta = read_json(rd / "meta.json", {}) or {}
                return self._json({"dir": rd.name, "round": read_json(rd / "round.json", {}), "meta": meta,
                                   "replays": [r for r in results() if r.get("round") == rd.name]})
            if parts == ["replays"]:
                rows = results()
                return self._json({"results": rows, "summary": replay_summary(rows)})
            if parts == ["configs"]:
                return self._json(list_configs())
            if len(parts) == 2 and parts[0] == "params" and parts[1] in TOOLS:
                return self._json({"tool": parts[1], "params": param_defs(parts[1])})
            if parts == ["jobs"]:
                return self._json({"jobs": JOBS.list()})
            if len(parts) == 3 and parts[0] == "jobs" and parts[2] == "log":
                p = JOBS.log_path(Path(parts[1]).name)
                tail = int((qs.get("tail") or ["400"])[0])
                lines = p.read_text(errors="replace").splitlines()[-tail:] if p.exists() else []
                return self._json({"lines": lines})
            if parts == ["logs"]:
                return self._json(logs_data())
            if parts == ["system"]:
                return self._json(system_data())
            if parts == ["tune"]:
                return self._json(tune_data())
            return self._json({"error": "not found"}, 404)
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            return self._json({"error": f"{type(e).__name__}: {e}"}, 500)

    def do_POST(self):
        u = urlparse(self.path)
        try:
            parts = u.path.strip("/").split("/")[1:]
            body = self._body()
            if parts == ["configs", "validate"]:
                tool = body.get("tool", "gatk")
                return self._json(validate(tool, body.get("options") or {}))
            if parts == ["configs", "save"]:
                name, tool, opts = body.get("name", ""), body.get("tool", "gatk"), body.get("options") or {}
                if not NAME_RE.match(name) or tool not in TOOLS:
                    return self._json({"error": "invalid name or tool"}, 400)
                v = validate(tool, opts)
                if not v["valid"]:
                    return self._json({"error": "config is not valid", **v}, 400)
                path = CONFIGS / f"{name}.conf"
                if path.exists() and not body.get("overwrite"):
                    return self._json({"error": f"{name} exists"}, 409)
                CONFIGS.mkdir(exist_ok=True)
                write_conf(path, tool, opts, body.get("note", ""))
                return self._json({"saved": name, "hash": opts_hash(opts)})
            if parts == ["configs", "deploy"]:
                name = Path(body.get("name", "")).name
                src = CONFIGS / f"{name}.conf"
                if not src.exists():
                    return self._json({"error": "unknown config"}, 404)
                opts = parse_conf(src.read_text())
                tool = conf_tool(name, opts)
                v = validate(tool, opts)
                if not v["valid"]:
                    return self._json({"error": "config is not valid", **v}, 400)
                dst = REPO / "configs" / f"{tool}.conf"
                backup = STATE / "config_backups" / f"{tool}-{datetime.now():%Y%m%d-%H%M%S}.conf"
                backup.parent.mkdir(parents=True, exist_ok=True)
                if dst.exists():
                    shutil.copy2(dst, backup)
                shutil.copy2(src, dst)
                return self._json({"deployed": name, "tool": tool, "backup": str(backup.relative_to(ROOT))})
            if parts == ["jobs"]:
                kind = body.get("kind")
                params = body.get("params") or {}
                if kind == "replay":
                    if not (CONFIGS / f"{Path(params.get('config', '')).name}.conf").exists():
                        return self._json({"error": "unknown config"}, 400)
                    params["rounds"] = [Path(r).name for r in params.get("rounds") or [] if (ROUNDS / Path(r).name).is_dir()]
                    if not params["rounds"]:
                        return self._json({"error": "no rounds selected"}, 400)
                    params["threads"] = max(1, min(int(params.get("threads", 2)), os.cpu_count() or 2))
                elif kind not in ("fetch_rounds", "fetch_meta", "upstream_check"):
                    return self._json({"error": "unknown job kind"}, 400)
                return self._json(JOBS.submit(kind, params))
            if len(parts) == 3 and parts[0] == "jobs" and parts[2] == "cancel":
                return self._json({"cancelled": JOBS.cancel(Path(parts[1]).name)})
            if parts == ["journal"]:
                text = (body.get("text") or "").strip()
                if not text:
                    return self._json({"error": "empty note"}, 400)
                entry = {"ts": now_iso(), "tag": (body.get("tag") or "note")[:24], "text": text[:4000]}
                JOURNAL.parent.mkdir(parents=True, exist_ok=True)
                with JOURNAL.open("a") as fh:
                    fh.write(json.dumps(entry) + "\n")
                return self._json(entry)
            if parts == ["tune", "start"]:
                out, code = tune_start(body)
                return self._json(out, code)
            if parts == ["autopilot", "start"]:
                out, code = autopilot_start(body)
                return self._json(out, code)
            if parts == ["autopilot", "stop"]:
                out, code = autopilot_stop()
                return self._json(out, code)
            if parts == ["tune", "stop"]:
                out, code = tune_stop()
                return self._json(out, code)
            if parts == ["refresh"]:
                CACHE._data.clear()
                return self._json({"ok": True})
            return self._json({"error": "not found"}, 404)
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            return self._json({"error": f"{type(e).__name__}: {e}"}, 500)


def main():
    global JOBS
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8787)
    args = ap.parse_args()
    JOBS = Jobs()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Minos dashboard on http://localhost:{args.port}  (Ctrl+C to stop)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
