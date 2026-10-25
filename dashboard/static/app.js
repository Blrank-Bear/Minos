/* Minos Miner Console — single-page app over the dashboard/server.py JSON API. */
"use strict";

const S = { live: null, rounds: null, replays: null, configs: null, jobs: null, logs: null, system: null, tune: null, params: {} };
const UI = {
  tab: "overview",
  roundsFilter: { chrom: "", status: "finalized", q: "" },
  replay: { primary: null, compare: "" },
  cfgSel: null, cfgDraft: null,
  jobSel: null,
  sort: {},
};
const REQUIRED_IMAGES = ["broadinstitute/gatk:4.5.0.0", "quay.io/biocontainers/samtools:1.20--h50ea8bc_0",
  "quay.io/biocontainers/bcftools:1.20--h8b25389_0", "genonet/hap-py"];
const VALIDATOR_TIMEOUT = 900;
const C = { s1: "var(--series-1)", s2: "var(--series-2)", s3: "var(--series-3)", s4: "var(--series-4)" };

/* ---------------- helpers ---------------- */
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const f4 = v => v == null || !isFinite(v) ? "—" : (+v).toFixed(4);
const f3 = v => v == null || !isFinite(v) ? "—" : (+v).toFixed(3);
const sgn = v => v == null ? "—" : (v >= 0 ? "+" : "") + (+v).toFixed(4);
const pct = v => v == null ? "—" : (100 * v).toFixed(1) + "%";
const secs = v => v == null ? "—" : v >= 60 ? `${Math.floor(v / 60)}m ${Math.round(v % 60)}s` : `${Math.round(v)}s`;
const dt = iso => { if (!iso) return "—"; const d = new Date(iso); return isNaN(d) ? iso : d.toLocaleString([], { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" }); };
const short = iso => { const d = new Date(iso); return isNaN(d) ? iso : `${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")} ${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`; };
const ago = iso => { const s = (Date.now() - new Date(iso)) / 1000; if (!isFinite(s)) return "—"; if (s < 60) return "just now"; if (s < 3600) return `${Math.floor(s / 60)}m ago`; if (s < 86400) return `${Math.floor(s / 3600)}h ago`; return `${Math.floor(s / 86400)}d ago`; };
const regionMb = r => { const m = /:(\d+)-(\d+)/.exec(r || ""); return m ? ((m[2] - m[1]) / 1e6) : null; };
const dirToIso = d => { const m = /^(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})Z$/.exec(d || ""); return m ? `${m[1]}-${m[2]}-${m[3]}T${m[4]}:${m[5]}:${m[6]}Z` : d; };
const rankEmoji = r => r == null ? "" : r === 1 ? "🥇" : r === 2 ? "🥈" : r === 3 ? "🥉" : r <= 20 ? "🎯" : "";

async function api(path, opts = {}) {
  const res = await fetch(`/api/${path}`, {
    method: opts.method || "GET",
    headers: opts.body ? { "Content-Type": "application/json" } : {},
    body: opts.body ? JSON.stringify(opts.body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw Object.assign(new Error(data.error || res.statusText), { data });
  return data;
}
function toast(msg, kind = "") {
  const t = document.createElement("div");
  t.className = `toast ${kind}`;
  t.innerHTML = msg;
  $("#toasts").appendChild(t);
  setTimeout(() => t.remove(), 4500);
}
const status = (kind, label) => `<span class="status ${kind}">${esc(label)}</span>`;
const empty = (emoji, text, extra = "") => `<div class="empty"><span class="big">${emoji}</span>${text}${extra}</div>`;

async function load(key, force = false) {
  if (S[key] && !force) return S[key];
  const path = { live: "live", rounds: "rounds", replays: "replays", configs: "configs", jobs: "jobs", logs: "logs", system: "system", tune: "tune" }[key];
  try { S[key] = await api(path); } catch (e) { S[key] = { error: e.message }; }
  return S[key];
}
async function params(tool) {
  if (!S.params[tool]) S.params[tool] = (await api(`params/${tool}`)).params;
  return S.params[tool];
}

/* derived data */
function summaries() { return (S.replays && S.replays.summary) || []; }
function bestSummary() {
  return summaries().filter(s => s.mean_gap != null).sort((a, b) => b.mean_gap - a.mean_gap)[0] || summaries()[0];
}
function resultsFor(label) {
  const latest = {};
  for (const r of (S.replays?.results || []).filter(r => r.label === label)) latest[r.round] = r;
  return latest;
}
function finalizedRounds() { return (S.rounds?.rounds || []).filter(r => r.finalized); }

/* ---------------- shell ---------------- */
function setTheme(t) {
  if (t) document.documentElement.setAttribute("data-theme", t); else document.documentElement.removeAttribute("data-theme");
  try { t ? localStorage.setItem("theme", t) : localStorage.removeItem("theme"); } catch (_) { /* storage unavailable */ }
}
function initTheme() {
  let t = null;
  try { t = localStorage.getItem("theme"); } catch (_) { /* ignore */ }
  if (t) setTheme(t);
  $("#theme-btn").addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme") ||
      (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    setTheme(cur === "dark" ? "light" : "dark");
    render();
  });
}
function updatePill() {
  const cur = S.live?.current;
  const pill = $("#live-pill");
  if (!cur || cur.error) { pill.innerHTML = "⚠️ live data unavailable"; return; }
  const phase = cur.status === "open" ? "🟢 open" : cur.status === "scoring" ? "🟡 scoring" : `⚪ ${esc(cur.status)}`;
  pill.innerHTML = `<span class="dot-live"></span>${esc(cur.chromosome || "")} · ${phase} · <span data-until="${esc(cur.submission_end_time)}">…</span>`;
}
function tickCountdowns() {
  for (const n of $$("[data-until]")) {
    const ms = new Date(n.dataset.until) - Date.now();
    if (!isFinite(ms)) { n.textContent = "—"; continue; }
    if (ms <= 0) { n.textContent = "closed"; continue; }
    const m = Math.floor(ms / 60000), s = Math.floor((ms % 60000) / 1000);
    n.textContent = `${m}:${String(s).padStart(2, "0")} left`;
  }
}
function updateJobsBadge() {
  const active = (S.jobs?.jobs || []).filter(j => j.status === "running" || j.status === "queued").length;
  const b = $("#jobs-badge");
  b.hidden = !active;
  b.textContent = active;
}
function openDrawer(html) {
  $("#drawer-body").innerHTML = html;
  $("#drawer").hidden = false;
}
function closeDrawer() { $("#drawer").hidden = true; }

/* ---------------- router ---------------- */
const VIEWS = { overview, live, rounds, replays, tune, configs, jobs, logs, system };
function route() {
  const tab = (location.hash.replace(/^#\//, "") || "overview").split("/")[0];
  UI.tab = VIEWS[tab] ? tab : "overview";
  $$("#nav a").forEach(a => a.classList.toggle("active", a.dataset.tab === UI.tab));
  render();
}
async function render() {
  const view = $("#view");
  try {
    await VIEWS[UI.tab](view);
  } catch (e) {
    console.error(e);
    view.innerHTML = `<div class="card">${empty("💥", `Something went wrong: ${esc(e.message)}`)}</div>`;
  }
  tickCountdowns();
}

/* ================= OVERVIEW ================= */
async function overview(view) {
  if (!S.rounds) view.innerHTML = `<div class="skeleton"></div>`;
  await Promise.all(["live", "rounds", "replays", "system", "jobs", "logs", "tune"].map(k => load(k)));
  const cur = S.live?.current || {};
  const lastFinal = finalizedRounds()[0];
  const best = bestSummary();
  const nRounds = S.rounds?.rounds?.length || 0;
  const sys = S.system || {};
  view.innerHTML = `
    <div class="view-head"><div><h1>👋 Mining overview</h1><p>Live round, our best config against the field, and what's left before going live.</p></div>
      <div class="row"><button id="ov-fetch">📥 Fetch new rounds</button><button class="primary" onclick="location.hash='#/jobs'">🏁 Run a replay</button></div></div>
    <div id="ov-work">${workBanner()}</div>
    <div class="grid g4">
      <div class="card tile"><span class="emoji">📡</span><span class="label">Current round</span>
        <span class="value">${esc(cur.chromosome || "—")}</span>
        <span class="sub">${esc(cur.region || "")}</span>
        <span class="sub">${cur.status === "open" ? "🟢 open · " : cur.status ? esc(cur.status) + " · " : ""}<span data-until="${esc(cur.submission_end_time)}"></span> · ${cur.submission_count ?? "—"} subs</span></div>
      <div class="card tile"><span class="emoji">🏆</span><span class="label">Latest winning score</span>
        <span class="value num">${f4(lastFinal?.top1)}</span>
        <span class="sub">${lastFinal ? `${esc(lastFinal.chromosome)} · ${dt(lastFinal.round_id)}` : "no finalized rounds yet"}</span>
        <span class="sub">top-5 spread ${f4(lastFinal?.spread_top5)}</span></div>
      <div class="card tile"><span class="emoji">🥇</span><span class="label">Our best config</span>
        <span class="value">${best ? esc(best.label) : "—"}</span>
        <span class="sub">${best ? `gap to #1 ${sgn(best.mean_gap)} · avg rank ${best.mean_rank ? best.mean_rank.toFixed(1) : "—"}` : "no replays yet"}</span>
        <span class="sub">${best ? `${best.ok}/${best.rounds} rounds · ${best.wins} 🥇 wins` : ""}</span></div>
      <div class="card tile"><span class="emoji">🗂️</span><span class="label">Replay data</span>
        <span class="value num">${nRounds}</span>
        <span class="sub">${finalizedRounds().length} finalized with leaderboards</span>
        <span class="sub">${sys.disk ? `${sys.disk.rounds_gb} GB · ${sys.disk.free_gb} GB free` : ""}</span></div>
    </div>
    <div class="grid g3" style="margin-top:16px">
      <div class="card span2"><div class="card-head"><h2>📈 ${best ? esc(best.label) : "Our config"} vs the field</h2>
        <span class="muted">projected from replays of past rounds</span></div><div id="ov-chart"></div></div>
      <div class="card"><div class="card-head"><h2>🚦 Mining readiness</h2></div>${readiness()}</div>
    </div>
    <div class="grid g2" style="margin-top:16px">
      <div class="card"><div class="card-head"><h2>🧪 Recent jobs</h2><a href="#/jobs">all jobs →</a></div>${jobsMini()}</div>
      <div class="card"><div class="card-head"><h2>📜 Latest changes</h2><a href="#/logs">all logs →</a></div>${commitsMini()}</div>
    </div>`;
  $("#ov-fetch").onclick = () => startJob("fetch_rounds", { last: 30 });
  scoreChart($("#ov-chart"), best?.label, "");
}
function readiness() {
  const sys = S.system || {};
  const imgs = (sys.docker?.images || []).map(i => i[0]);
  const imgOk = REQUIRED_IMAGES.every(r => imgs.some(i => i.startsWith(r)));
  const refs = sys.reference_chromosomes?.length || 0;
  const best = bestSummary();
  const items = [
    [imgOk, "🐳", "Docker + caller images", imgOk ? "GATK, samtools, bcftools, hap.py" : "run scripts/setup_miner.sh images"],
    [refs >= 22, "🧬", "Reference genome", `${refs}/22 chromosomes`],
    [finalizedRounds().length >= 10, "🗂️", "Past rounds for replay", `${finalizedRounds().length} finalized`],
    [summaries().length > 0, "🏁", "Replays run", `${(S.replays?.results || []).length} results`],
    [best && best.mean_rank != null && best.mean_rank <= 5, "🥇", "Config competitive (avg rank ≤ 5)", best?.mean_rank ? `best avg rank ${best.mean_rank.toFixed(1)}` : "no ranked replays"],
    [!!sys.wallet_present, "👛", "Wallet", sys.wallet_present ? "hotkey found in wallets/" : "not created — needs your go-ahead"],
    [false, "📝", "Registered on SN107", "needs wallet + ~0.99 TAO"],
    [(sys.miner_processes || []).length > 0, "⛏️", "Miner running", (sys.miner_processes || []).length ? "process found" : "not running"],
  ];
  return `<ul class="checklist">${items.map(([ok, e, t, s]) =>
    `<li><span class="ico">${ok ? "✅" : "⬜"}</span><div><b>${e} ${esc(t)}</b><small>${esc(s)}</small></div></li>`).join("")}</ul>`;
}
function jobsMini() {
  const js = (S.jobs?.jobs || []).slice(0, 5);
  if (!js.length) return empty("🫧", "No jobs yet.");
  return `<div class="table-wrap"><table><tbody>${js.map(j => `
    <tr class="click" onclick="UI.jobSel='${j.id}';location.hash='#/jobs'">
      <td>${jobEmoji(j.kind)} ${esc(jobTitle(j))}</td><td>${jobStatus(j)}</td><td class="muted">${ago(j.created)}</td></tr>`).join("")}</tbody></table></div>`;
}
function commitsMini() {
  const cs = (S.logs?.project || []).slice(0, 5);
  if (!cs.length) return empty("🌱", "No commits.");
  return cs.map(c => `<div class="commit"><div class="row"><code class="muted">${esc(c.short)}</code><b>${esc(c.subject)}</b><span class="spacer"></span><span class="muted">${ago(c.date)}</span></div></div>`).join("");
}

/* score-vs-field line chart (shared by overview + replays) */
function scoreChart(box, label, compare) {
  const rows = finalizedRounds().slice().reverse();
  if (!label || !rows.length) { box.innerHTML = empty("🏁", "Run a replay to see projected scores against each round's leaderboard."); return; }
  const a = resultsFor(label), b = compare ? resultsFor(compare) : {};
  const used = rows.filter(r => a[r.dir] || (compare && b[r.dir]));
  if (!used.length) { box.innerHTML = empty("🏁", `No replays of <b>${esc(label)}</b> on finalized rounds yet.`); return; }
  const series = [
    { name: label, color: C.s1, values: used.map(r => a[r.dir]?.score ?? null) },
    { name: "#1", color: C.s2, values: used.map(r => r.top1 ?? null) },
    { name: "median", color: C.s3, values: used.map(r => r.median ?? null) },
  ];
  if (compare) series.push({ name: compare, color: C.s4, values: used.map(r => b[r.dir]?.score ?? null) });
  Charts.line(box, {
    series, labels: used.map(r => short(r.round_id)), fmt: f3, height: 270, aria: "score per round",
    tipTitle: i => `${esc(used[i].chromosome)} · ${dt(used[i].round_id)}${a[used[i].dir]?.rank ? ` · ${rankEmoji(a[used[i].dir].rank)} rank ${a[used[i].dir].rank}` : ""}`,
    onClick: i => roundDrawer(used[i].dir),
  });
}

/* ================= LIVE ================= */
async function live(view) {
  view.innerHTML = `<div class="skeleton"></div>`;
  await Promise.all([load("live"), load("rounds")]);
  const L = S.live || {}, cur = L.current || {}, nc = L.network_config || {};
  const recent = L.recent?.rounds || [];
  const local = new Set((S.rounds?.rounds || []).map(r => r.round_id));
  const phase = cur.status;
  const step = (key, title, time, desc) => `<div class="step ${phase === key ? "on" : ""}"><b>${title}</b>${dt(time)}<br><span class="muted">${desc}</span></div>`;
  view.innerHTML = `
    <div class="view-head"><div><h1>📡 Live round</h1><p>Updated ${ago(L.fetched_at)} from the public Minos API & MCP. Polls every 30 s.</p></div>
      <div class="row">${L.health?.status === "healthy" ? status("good", "platform healthy") : status("critical", `platform ${L.health?.status || "unknown"}`)}</div></div>
    ${cur.error ? `<div class="card">${empty("⚠️", esc(cur.error))}</div>` : `
    <div class="grid g3">
      <div class="card span2">
        <div class="card-head"><h2>🧬 ${esc(cur.region || "—")}</h2><span class="pill">${phase === "open" ? "🟢 accepting submissions" : phase === "scoring" ? "🟡 validators scoring" : esc(phase || "")}</span></div>
        <div class="grid g3">
          <div class="tile"><span class="label">Submission window</span><span class="value"><span data-until="${esc(cur.submission_end_time)}"></span></span><span class="sub">closes ${dt(cur.submission_end_time)}</span></div>
          <div class="tile"><span class="label">Submissions</span><span class="value num">${cur.submission_count ?? "—"}</span><span class="sub">${cur.scored_submission_count ?? 0} scored</span></div>
          <div class="tile"><span class="label">Window size</span><span class="value num">${regionMb(cur.region)?.toFixed(1) ?? "—"} Mb</span><span class="sub">${esc(cur.chromosome || "")}</span></div>
        </div>
        <div class="timeline">
          ${step("open", "① Submit", cur.start_time, "miners send configs")}
          ${step("scoring", "② Score", cur.submission_end_time, "validators re-run configs")}
          ${step("completed", "③ Finalize", cur.scoring_end_time, "weights + reveal")}
        </div>
        <p class="muted" style="margin:10px 0 0">🆔 <code>${esc(cur.round_id)}</code>${cur.note ? ` · ${esc(cur.note)}` : ""}</p>
      </div>
      <div class="card"><div class="card-head"><h2>⚖️ Reward policy</h2><span class="chip">scoring ${esc(nc.scoring_version || "?")}</span></div>
        <dl class="kv">
          <dt>🏆 winner weight</dt><dd>${pct(nc.winner_weight)}</dd>
          <dt>🎯 dust ranks</dt><dd>2 – ${nc.dust_top_n ?? "?"} · decay ${nc.dust_decay ?? "?"}</dd>
          <dt>🔥 burn</dt><dd>${pct(nc.burn_rate)}</dd>
          <dt>✅ eligibility</dt><dd>${nc.min_participation_rounds ?? "?"} of ${nc.participation_window ?? "?"} rounds</dd>
          <dt>🔐 commitment</dt><dd>${nc.config_commitment_required ? "required" : nc.config_commitment_enabled ? "enabled" : "off"}</dd>
          <dt>💸 paid resubmit</dt><dd>${nc.resubmission_fee_enabled ? "on" : "off"}</dd>
          <dt>👥 1 reward / coldkey</dt><dd>${nc.reward_normalization ? "yes" : "no"}</dd>
        </dl>
        <h3 style="margin:14px 0 6px">Chromosome odds</h3>
        <div class="row">${(nc.chromosome_rotation?.weights || []).filter(w => w.weight > 0.03).map(w => `<span class="chip">chr${w.chromosome} ${pct(w.weight)}</span>`).join("")}
          <span class="chip muted">others ${pct((nc.chromosome_rotation?.weights || []).filter(w => w.weight <= 0.03).reduce((a, w) => a + w.weight, 0))}</span></div>
      </div>
    </div>`}
    <div class="card" style="margin-top:16px"><div class="card-head"><h2>🕒 Recent rounds</h2><button id="lv-fetch">📥 Download revealed rounds</button></div>
      <div class="table-wrap"><table><thead><tr><th>Round</th><th>Region</th><th class="num">Mb</th><th>Status</th><th class="num">Subs</th><th class="num">Scored</th><th>Local</th></tr></thead><tbody>
      ${recent.map(r => `<tr><td>${dt(r.round_id)}</td><td><code>${esc(r.region)}</code></td><td class="num">${regionMb(r.region)?.toFixed(1) ?? ""}</td>
        <td>${r.status === "open" ? status("good", "open") : r.status === "scoring" ? status("warning", "scoring") : r.is_finalized ? status("", "finalized") : esc(r.status)}</td>
        <td class="num">${r.submission_count ?? ""}</td><td class="num">${r.scored_submission_count ?? ""}</td>
        <td>${local.has(r.round_id) ? "💾" : "—"}</td></tr>`).join("")}</tbody></table></div></div>`;
  $("#lv-fetch").onclick = () => startJob("fetch_rounds", { last: 30 });
}

/* ================= ROUNDS ================= */
async function rounds(view) {
  view.innerHTML = `<div class="skeleton"></div>`;
  await Promise.all([load("rounds"), load("replays")]);
  const all = S.rounds?.rounds || [];
  const F = UI.roundsFilter;
  const chroms = [...new Set(all.map(r => r.chromosome).filter(Boolean))].sort((a, b) => parseInt(a.slice(3)) - parseInt(b.slice(3)));
  const best = bestSummary();
  const ours = best ? resultsFor(best.label) : {};
  let rows = all.filter(r => (!F.chrom || r.chromosome === F.chrom) && (F.status !== "finalized" || r.finalized) &&
    (!F.q || `${r.region} ${r.round_id} ${r.winner_hotkey}`.toLowerCase().includes(F.q.toLowerCase())));
  rows = sortRows("rounds", rows, {
    when: r => r.round_id, mb: r => regionMb(r.region), subs: r => r.submission_count, top1: r => r.top1,
    median: r => r.median, spread: r => r.spread_top5, ours: r => ours[r.dir]?.score, rank: r => ours[r.dir]?.rank,
  });
  const th = (k, t, num) => `<th class="sortable ${num ? "num" : ""}" data-sort="${k}">${t}${UI.sort.rounds?.k === k ? (UI.sort.rounds.dir > 0 ? " ▲" : " ▼") : ""}</th>`;
  view.innerHTML = `
    <div class="view-head"><div><h1>🧬 Round history</h1><p>${all.length} downloaded rounds · click a row for its leaderboard and our replays.</p></div>
      <div class="row"><button id="rd-meta">🔁 Refresh metadata</button><button id="rd-fetch" class="primary">📥 Fetch rounds</button></div></div>
    <div class="card">
      <div class="row" style="margin-bottom:12px">
        <select id="f-chrom"><option value="">🧬 all chromosomes</option>${chroms.map(c => `<option ${F.chrom === c ? "selected" : ""}>${c}</option>`).join("")}</select>
        <div class="seg" id="f-status"><button data-v="finalized" class="${F.status === "finalized" ? "on" : ""}">✅ finalized</button><button data-v="all" class="${F.status === "all" ? "on" : ""}">all</button></div>
        <input id="f-q" placeholder="🔎 search region, round, winner…" value="${esc(F.q)}" style="flex:1;min-width:180px">
        <span class="muted">${rows.length} shown${best ? ` · "ours" = ${esc(best.label)}` : ""}</span>
      </div>
      <div class="table-wrap"><table><thead><tr>${th("when", "Round")}<th>Chr</th><th>Region</th>${th("mb", "Mb", 1)}${th("subs", "Subs", 1)}${th("top1", "#1", 1)}${th("median", "Median", 1)}${th("spread", "Top-5 spread", 1)}${th("ours", "Ours", 1)}${th("rank", "Proj. rank", 1)}<th>Files</th></tr></thead>
      <tbody>${rows.map(r => {
        const o = ours[r.dir];
        return `<tr class="click" data-dir="${r.dir}"><td>${dt(r.round_id)}</td><td><span class="chip">${esc(r.chromosome || "?")}</span></td><td><code>${esc(r.region || "—")}</code></td>
          <td class="num">${regionMb(r.region)?.toFixed(1) ?? ""}</td><td class="num">${r.submission_count ?? ""}</td><td class="num">${f4(r.top1)}</td><td class="num">${f4(r.median)}</td>
          <td class="num">${f4(r.spread_top5)}</td><td class="num">${o ? f4(o.score) : "—"}</td><td class="num">${o?.rank ? `${rankEmoji(o.rank)} ${o.rank}/${o.field}` : "—"}</td>
          <td>${r.files_ok ? "💾" : "⚠️"}</td></tr>`;
      }).join("") || `<tr><td colspan="11">${empty("🔭", "No rounds match.")}</td></tr>`}</tbody></table></div></div>`;
  $("#f-chrom").onchange = e => { F.chrom = e.target.value; render(); };
  $$("#f-status button").forEach(b => b.onclick = () => { F.status = b.dataset.v; render(); });
  $("#f-q").oninput = debounce(e => { F.q = e.target.value; render().then(() => { const q = $("#f-q"); q.focus(); q.setSelectionRange(q.value.length, q.value.length); }); }, 300);
  $$("tr[data-dir]").forEach(tr => tr.onclick = () => roundDrawer(tr.dataset.dir));
  bindSort("rounds");
  $("#rd-fetch").onclick = () => startJob("fetch_rounds", { last: 30 });
  $("#rd-meta").onclick = () => startJob("fetch_meta", {});
}
async function roundDrawer(dir) {
  openDrawer(`<div class="skeleton"></div>`);
  const [d] = await Promise.all([api(`rounds/${dir}`), load("configs")]);
  const meta = d.meta || {}, board = meta.leaderboard || [];
  const latestBy = {};
  for (const r of d.replays) latestBy[r.label] = r;
  const mine = Object.values(latestBy).filter(r => r.ok).sort((a, b) => b.score - a.score);
  const colors = [C.s1, C.s2, C.s3];
  const cfgs = S.configs?.configs || [];
  openDrawer(`
    <h1 style="margin-right:40px">🧬 ${esc(meta.region || dir)}</h1>
    <p class="muted">${dt(meta.round_id)} · ${meta.submission_count ?? "?"} submissions · ${meta.scored_submission_count ?? "?"} scored · ${meta.finalized ? "✅ finalized" : "⏳ not finalized"}</p>
    <div class="card" style="margin:14px 0"><div class="card-head"><h2>📊 Score distribution</h2><span class="muted">grey = field · coloured = our replays</span></div>
      ${mine.length ? Charts.legend(mine.slice(0, 3).map((r, i) => ({ name: r.label, color: colors[i], dot: true }))).outerHTML : ""}
      <div id="dr-strip"></div></div>
    <div class="card" style="margin-bottom:14px"><div class="card-head"><h2>🏁 Replay this round</h2></div>
      <div class="row"><select id="dr-cfg">${cfgs.map(c => `<option>${esc(c.name)}</option>`).join("")}</select>
        <select id="dr-thr"><option>2</option><option>4</option><option>8</option></select><span class="muted">threads</span>
        <button class="primary" id="dr-go">▶️ Queue replay</button></div></div>
    ${mine.length ? `<div class="card" style="margin-bottom:14px"><div class="card-head"><h2>🧪 Our replays</h2></div>${resultsTable(mine, false)}</div>` : ""}
    <div class="card"><div class="card-head"><h2>🏆 Leaderboard</h2><span class="muted">${board.length} shown (API caps at 64)</span></div>
      <div class="table-wrap"><table><thead><tr><th class="num">#</th><th>UID</th><th>Hotkey</th><th class="num">Score</th><th class="num">SNP</th><th class="num">Indel</th><th class="num">Weight</th><th>Tool</th></tr></thead><tbody>
      ${board.map(e => `<tr><td class="num">${rankEmoji(e.rank)} ${e.rank}</td><td class="num">${e.uid ?? ""}</td><td><code title="${esc(e.hotkey)}">${esc((e.hotkey || "").slice(0, 10))}…</code></td>
        <td class="num">${f4(e.combined_final)}</td><td class="num">${f4(e.snp_final)}</td><td class="num">${f4(e.indel_final)}</td><td class="num">${e.weight != null ? pct(e.weight) : ""}</td><td>${esc(e.tool_name || "")}</td></tr>`).join("") || `<tr><td colspan="8">${empty("⏳", "Leaderboard not revealed yet.")}</td></tr>`}
      </tbody></table></div></div>`);
  if (board.length) {
    Charts.strip($("#dr-strip"), {
      field: board.map(e => ({ v: e.combined_final, label: `#${e.rank} · uid ${e.uid}` })),
      marks: mine.slice(0, 3).map((r, i) => ({ v: r.score, label: `${r.label} → rank ${r.rank}`, color: colors[i] })),
      height: 150,
    });
  } else $("#dr-strip").innerHTML = empty("⏳", "No leaderboard yet.");
  $("#dr-go").onclick = () => startJob("replay", { config: $("#dr-cfg").value, rounds: [dir], threads: +$("#dr-thr").value });
}

/* ================= REPLAYS ================= */
async function replays(view) {
  view.innerHTML = `<div class="skeleton"></div>`;
  await Promise.all([load("replays"), load("rounds")]);
  const sums = summaries();
  if (!UI.replay.primary || !sums.some(s => s.label === UI.replay.primary)) UI.replay.primary = bestSummary()?.label || null;
  const P = UI.replay.primary, X = UI.replay.compare;
  const rows = Object.values(resultsFor(P || "")).sort((a, b) => (b.round > a.round ? 1 : -1));
  view.innerHTML = `
    <div class="view-head"><div><h1>🏁 Replays & projected rankings</h1><p>Each replay re-runs a config on a past round exactly as a validator would, then places it on that round's real leaderboard.</p></div>
      <div class="row"><button id="rp-csv">⬇️ Export CSV</button><button class="primary" onclick="location.hash='#/jobs'">▶️ New replay</button></div></div>
    <div class="card"><div class="card-head"><h2>📋 Config league table</h2><span class="muted">latest result per round · sorted by mean gap to #1</span></div>
      ${sums.length ? `<div class="table-wrap"><table><thead><tr><th></th><th>Config</th><th class="num">Rounds</th><th class="num">Mean score</th><th class="num">Mean gap</th><th class="num">Avg rank</th><th class="num">Best</th><th class="num">🥇</th><th class="num">Top 5</th><th class="num">Max calling</th><th>Last run</th></tr></thead><tbody>
      ${sums.map((s, i) => `<tr class="click ${s.label === P ? "me" : ""}" data-label="${esc(s.label)}"><td>${i === 0 && s.mean_gap != null ? "👑" : ""}</td><td><b>${esc(s.label)}</b> <code class="muted">${esc(s.config_hash)}</code></td>
        <td class="num">${s.ok}/${s.rounds}${s.failed ? " ⚠️" : ""}</td><td class="num">${f4(s.mean_score)}</td><td class="num">${sgn(s.mean_gap)}</td><td class="num">${s.mean_rank ? s.mean_rank.toFixed(1) : "—"}</td>
        <td class="num">${s.best_rank ? `${rankEmoji(s.best_rank)} ${s.best_rank}` : "—"}</td><td class="num">${s.wins}</td><td class="num">${s.top5}</td>
        <td class="num">${runtimeCell(s.max_calling_seconds)}</td><td class="muted">${ago(s.last_run)}</td></tr>`).join("")}</tbody></table></div>` :
        empty("🏁", "No replays yet. Queue one from the Jobs tab.", `<br><br><button class="primary" onclick="location.hash='#/jobs'">▶️ Start first replay</button>`)}
    </div>
    ${P ? `
    <div class="card" style="margin-top:16px"><div class="card-head"><h2>📈 Score per round</h2>
      <div class="row"><label class="muted">config</label><select id="rp-p">${sums.map(s => `<option ${s.label === P ? "selected" : ""}>${esc(s.label)}</option>`).join("")}</select>
        <label class="muted">compare</label><select id="rp-x"><option value="">— none —</option>${sums.filter(s => s.label !== P).map(s => `<option ${s.label === X ? "selected" : ""}>${esc(s.label)}</option>`).join("")}</select></div></div>
      <div id="rp-line"></div></div>
    <div class="grid g2" style="margin-top:16px">
      <div class="card"><div class="card-head"><h2>📏 Gap to #1 per round</h2><span class="muted">${esc(P)} · 0 = tie with winner</span></div><div id="rp-gap"></div></div>
      <div class="card"><div class="card-head"><h2>⏱️ Calling time per round</h2><span class="muted">validators stop at ${VALIDATOR_TIMEOUT}s</span></div><div id="rp-time"></div></div>
    </div>
    <div class="card" style="margin-top:16px"><div class="card-head"><h2>🔬 Results · ${esc(P)}</h2><span class="muted">v2 = 100 × (0.70 core + 0.30 germline)</span></div>${resultsTable(rows, true)}</div>` : ""}`;
  $$("tr[data-label]").forEach(tr => tr.onclick = () => { UI.replay.primary = tr.dataset.label; if (UI.replay.compare === UI.replay.primary) UI.replay.compare = ""; render(); });
  $("#rp-csv").onclick = exportCsv;
  if (!P) return;
  $("#rp-p").onchange = e => { UI.replay.primary = e.target.value; render(); };
  $("#rp-x").onchange = e => { UI.replay.compare = e.target.value; render(); };
  scoreChart($("#rp-line"), P, X);
  const fin = finalizedRounds().slice().reverse();
  const res = resultsFor(P);
  const used = fin.filter(r => res[r.dir]?.ok && res[r.dir].gap != null);
  if (used.length) {
    Charts.bars($("#rp-gap"), {
      values: used.map(r => res[r.dir].gap), labels: used.map(r => short(r.round_id)), fmt: f4, valueName: "gap to #1",
      color: v => v >= 0 ? "var(--good)" : C.s1, tipTitle: i => `${used[i].chromosome} · rank ${res[used[i].dir].rank}/${res[used[i].dir].field}`,
      onClick: i => roundDrawer(used[i].dir),
    });
  } else $("#rp-gap").innerHTML = empty("📏", "No placed results yet.");
  const timed = Object.values(res).filter(r => r.calling_seconds).sort((a, b) => a.round > b.round ? 1 : -1);
  if (timed.length) {
    Charts.bars($("#rp-time"), {
      values: timed.map(r => r.calling_seconds), labels: timed.map(r => short(dirToIso(r.round))), fmt: v => `${Math.round(v)}s`, valueName: "calling time",
      color: v => v > VALIDATOR_TIMEOUT ? "var(--critical)" : v > VALIDATOR_TIMEOUT * 0.7 ? "var(--warning)" : C.s3,
      tipTitle: i => `${timed[i].chromosome} · ${timed[i].threads} threads · ${regionMb(timed[i].region)?.toFixed(1)} Mb`,
    });
  } else $("#rp-time").innerHTML = empty("⏱️", "No timings yet.");
}
function runtimeCell(s) {
  if (s == null) return "—";
  const flag = s > VALIDATOR_TIMEOUT ? " 🛑" : s > VALIDATOR_TIMEOUT * 0.7 ? " ⚠️" : "";
  return `${secs(s)}${flag}`;
}
function resultsTable(rows, withRound) {
  if (!rows.length) return empty("🧪", "No results.");
  return `<div class="table-wrap"><table><thead><tr>${withRound ? "<th>Round</th><th>Chr</th>" : "<th>Config</th>"}<th class="num">Score</th><th class="num">Rank</th><th class="num">Gap</th>
    <th class="num">Core</th><th class="num">Germline</th><th class="num">FP/target</th><th class="num">Indel F1</th><th class="num">SNP F1</th><th class="num">Calling</th><th class="num">Calls</th><th>When</th></tr></thead><tbody>
    ${rows.map(r => `<tr ${withRound ? `class="click" data-rd="${r.round}"` : ""}>${withRound ? `<td>${dt(dirToIso(r.round))}</td><td><span class="chip">${esc(r.chromosome)}</span></td>` : `<td><b>${esc(r.label)}</b></td>`}
      <td class="num">${r.ok ? f4(r.score) : status("critical", "failed")}</td><td class="num">${r.rank ? `${rankEmoji(r.rank)} ${r.rank}/${r.field}` : "—"}</td><td class="num">${sgn(r.gap)}</td>
      <td class="num">${f4(r.breakdown?.core)}</td><td class="num">${f4(r.breakdown?.germline)}</td><td class="num">${f3(r.metrics?.fp_per_target)}</td>
      <td class="num">${f4(r.metrics?.f1_indel)}</td><td class="num">${f4(r.metrics?.f1_snp)}</td><td class="num">${runtimeCell(r.calling_seconds)}</td>
      <td class="num">${r.variant_count ?? "—"}</td><td class="muted">${ago(r.ts)}</td></tr>`).join("")}</tbody></table></div>
    ${withRound ? "" : ""}`;
}
function exportCsv() {
  const rows = S.replays?.results || [];
  if (!rows.length) return toast("Nothing to export yet.");
  const cols = ["ts", "label", "config_hash", "round", "chromosome", "region", "threads", "score", "rank", "field", "top1", "median", "gap", "calling_seconds", "variant_count"];
  const csv = [cols.join(","), ...rows.map(r => cols.map(c => JSON.stringify(r[c] ?? "")).join(","))].join("\n");
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" }));
  a.download = "minos-replays.csv";
  a.click();
}

/* ================= TUNING (live work status) ================= */
const TUNE_STATUS = {
  running: ["warning", "🔄 tuning in progress"], starting: ["warning", "🚀 starting"], stopping: ["serious", "⏸️ stopping"],
  finished: ["good", "✅ finished"], stopped: ["", "⏹️ stopped"], error: ["critical", "💥 error"], dead: ["critical", "💀 process gone"],
};
const tuneStatus = st => { const [k, l] = TUNE_STATUS[st] || ["", st || "not started"]; return status(k, l); };
const roundLabel = dir => { const r = (S.rounds?.rounds || []).find(x => x.dir === dir); return r ? `${r.chromosome} · ${short(r.round_id)}` : dir; };
function fmtVal(v) { return typeof v === "number" ? (Math.abs(v) < 0.01 && v !== 0 ? v.toExponential(1) : String(+v.toFixed(6))) : String(v); }

function workBanner() {
  const T = S.tune || {}, st = T.state || {};
  const active = ["running", "starting", "stopping"].includes(st.status) && T.alive;
  const jobsActive = (S.jobs?.jobs || []).filter(j => j.status === "running");
  if (!active && !jobsActive.length) {
    if (!st.status) return "";
    return `<div class="card callout" style="margin-bottom:16px">🎛️ Tuner ${tuneStatus(st.status)} · best dev gap ${sgn(st.best?.mean_gap)} · avg rank ${st.best?.mean_rank?.toFixed(1) ?? "—"} · <a href="#/tune">details →</a></div>`;
  }
  const cur = st.current || {}, step = st.step || {};
  const pctDone = cur.rounds_total ? Math.round(100 * cur.rounds_done / cur.rounds_total) : 0;
  return `<div class="card" style="margin-bottom:16px;border-color:color-mix(in srgb,var(--accent) 40%,var(--border))">
    <div class="row"><span class="dot-live"></span><b>🛠️ Work in progress</b><span class="spacer"></span><a href="#/tune">open Tuning →</a></div>
    ${active && st.phase === "screen" ? (() => {
      const cs = st.screen?.candidates || [], fin = cs.filter(c => c.done === c.total).length;
      const top = cs.filter(c => c.delta != null).sort((a, b) => b.delta - a.delta)[0];
      return `<div class="row" style="margin-top:8px"><span>🔎 Screening single changes · ${fin}/${cs.length} done${top ? ` · leading: <code>${esc(top.param)}</code>=${esc(fmtVal(top.value))} (${sgn(top.delta)})` : ""}</span>
        <span class="spacer"></span><span class="muted">best gap ${sgn(st.best?.mean_gap)}</span></div>
        <div class="progress" style="margin-top:8px"><i style="width:${cs.length ? Math.round(100 * fin / cs.length) : 0}%"></i></div>`;
    })() : active ? `<div class="row" style="margin-top:8px"><span>🎛️ Step ${step.index ?? "–"}/${step.of ?? "–"} · <code>${esc(cur.param || step.param || "baseline")}</code>${cur.param ? ` ${esc(fmtVal(cur.from))} → <b>${esc(fmtVal(cur.value))}</b>` : ""}</span>
      <span class="spacer"></span><span class="muted">${cur.rounds_done ?? 0}/${cur.rounds_total ?? "?"} rounds · best gap ${sgn(st.best?.mean_gap)}</span></div>
      <div class="progress" style="margin-top:8px"><i style="width:${pctDone}%"></i></div>` : ""}
    ${jobsActive.map(j => `<div class="row" style="margin-top:8px">${jobEmoji(j.kind)} ${esc(jobTitle(j))}<span class="spacer"></span><span class="muted">${esc(j.summary || "")}</span></div>`).join("")}
  </div>`;
}

async function tune(view) {
  if (!S.tune) view.innerHTML = `<div class="skeleton"></div>`;
  await Promise.all([load("tune", true), load("rounds")]);
  const T = S.tune || {}, st = T.state || {};
  const best = st.best;
  const hist = st.history || [];
  const cur = st.current, step = st.step || {};
  const active = ["running", "starting", "stopping"].includes(st.status) && T.alive;
  const baseline = (T.events || []).find(e => e.kind === "baseline");
  const plan = st.plan_params || [];
  const done = new Set(st.completed_params || []);
  view.innerHTML = `
    <div class="view-head"><div><h1>🎛️ Tuning — one change at a time</h1>
      <p>Each step changes a single parameter, replays it on ${st.dev_rounds?.length ?? 8} past rounds exactly as validators score, and keeps it only if the mean gap to each round's #1 improves.</p></div>
      <div class="row">${tuneStatus(st.status)}${st.heartbeat ? `<span class="muted">♥ ${ago(st.heartbeat)}</span>` : ""}
        ${active ? `<button class="danger" id="tn-stop">⏹ Stop</button>` : `<button class="primary" id="tn-start">▶️ ${best ? "Resume" : "Start"} tuning</button>${best ? `<button id="tn-pass">🔁 New pass from best</button>` : ""}`}
        ${st.pass ? `<span class="chip">pass ${st.pass}</span>` : ""}</div></div>
    ${st.error ? `<div class="callout warn" style="margin-bottom:16px">💥 ${esc(st.error)}</div>` : ""}
    <div class="grid g4">
      <div class="card tile"><span class="emoji">🧭</span><span class="label">Step</span>
        <span class="value num">${step.index ?? "—"}<span class="muted" style="font-size:16px"> / ${step.of ?? (plan.length || "—")}</span></span>
        <span class="sub"><code>${esc(step.param || "—")}</code></span></div>
      <div class="card tile"><span class="emoji">🧪</span><span class="label">Testing now</span>
        <span class="value" style="font-size:18px">${cur?.param ? `${esc(fmtVal(cur.from))} → ${esc(fmtVal(cur.value))}` : st.phase === "screen" && active ? "🔎 screening" : active ? "baseline" : "—"}</span>
        <span class="sub">${cur ? `${cur.rounds_done ?? 0}/${cur.rounds_total ?? "?"} rounds replayed` : st.phase === "screen" && active ? `${st.screen?.candidates?.filter(c => c.done === c.total).length ?? 0}/${st.screen?.candidates?.length ?? 0} single changes screened` : "idle"}</span>
        ${cur ? `<div class="progress" style="margin-top:6px"><i style="width:${cur.rounds_total ? Math.round(100 * cur.rounds_done / cur.rounds_total) : 0}%"></i></div>` : ""}</div>
      <div class="card tile"><span class="emoji">🥇</span><span class="label">Best so far</span>
        <span class="value num">${sgn(best?.mean_gap)}</span>
        <span class="sub">avg rank ${best?.mean_rank?.toFixed(1) ?? "—"} · ${best?.wins ?? 0} wins · ${best?.top5 ?? 0} top-5</span></div>
      <div class="card tile"><span class="emoji">📈</span><span class="label">Gain vs stock</span>
        <span class="value num">${best && baseline ? sgn(best.mean_gap - baseline.mean_gap) : "—"}</span>
        <span class="sub">${hist.filter(h => h.accepted).length} accepted · ${hist.length} tried · ${st.runs ?? 0} replays</span></div>
    </div>
    <div class="grid g3" style="margin-top:16px">
      <div class="card span2"><div class="card-head"><h2>📈 Progress</h2><span class="muted">mean gap to #1 per candidate · higher is better · 0 = tie with winner</span></div><div id="tn-chart"></div></div>
      <div class="card"><div class="card-head"><h2>🗺️ Plan</h2><span class="muted">${done.size}/${plan.length} params done</span></div>
        <div class="stack" style="gap:6px;max-height:320px;overflow:auto">${plan.map((p, i) => {
          const accepted = hist.filter(h => h.param === p && h.accepted).pop();
          const icon = done.has(p) ? (accepted ? "✅" : "➖") : step.param === p ? "🔄" : "⏳";
          return `<div class="row"><span>${icon}</span><code style="flex:1">${i + 1}. ${esc(p)}</code>${accepted ? `<span class="chip">→ ${esc(fmtVal(accepted.value))}</span>` : ""}</div>`;
        }).join("") || empty("🗺️", "Plan appears when the tuner starts.")}</div></div>
    </div>
    ${validationCard(T.validation)}
    ${screenCard(st)}
    ${cur ? `<div class="card" style="margin-top:16px"><div class="card-head"><h2>🔬 Current candidate · live per round</h2><code class="muted">${esc(cur.label || "")}</code></div>
      <div class="table-wrap"><table><thead><tr><th>Round</th><th class="num">Score</th><th class="num">Gap to #1</th><th class="num">Rank</th><th class="num">Calling</th><th></th></tr></thead><tbody>
      ${(st.dev_rounds || []).map(rd => { const r = cur.per_round?.[rd]; return `<tr><td>${esc(roundLabel(rd))}</td>
        <td class="num">${r?.score != null ? f4(r.score) : r?.failed ? status("critical", "failed") : "<span class='muted'>⏳ running…</span>"}</td>
        <td class="num">${sgn(r?.gap)}</td><td class="num">${r?.rank ? `${rankEmoji(r.rank)} ${r.rank}` : "—"}</td>
        <td class="num">${runtimeCell(r?.calling_seconds)}</td><td>${r?.cached ? "<span class='muted'>cached</span>" : ""}</td></tr>`; }).join("")}
      </tbody></table></div></div>` : ""}
    <div class="grid g2" style="margin-top:16px">
      <div class="card"><div class="card-head"><h2>🧾 Step history</h2><span class="muted">newest first</span></div>
        ${hist.length ? `<div class="table-wrap"><table><thead><tr><th></th><th>Change</th><th class="num">Mean gap</th><th class="num">Rank</th><th class="num">🥇</th><th class="num">Max calling</th></tr></thead><tbody>
        ${hist.slice().reverse().map(h => `<tr title="${esc(h.reason)}"><td>${h.accepted ? "✅" : "❌"}</td><td><code>${esc(h.param)}</code><br><span class="muted">${esc(fmtVal(h.from))} → <b>${esc(fmtVal(h.value))}</b> · ${esc(h.reason)}</span></td>
          <td class="num">${sgn(h.mean_gap)}</td><td class="num">${h.mean_rank?.toFixed(1) ?? "—"}</td><td class="num">${h.wins ?? 0}</td><td class="num">${runtimeCell(h.max_calling_seconds)}</td></tr>`).join("")}
        </tbody></table></div>` : empty("🧾", "No candidates evaluated yet.")}</div>
      <div class="stack">
        <div class="card"><div class="card-head"><h2>🧬 Best config vs stock</h2><a href="#/configs">open in editor →</a></div>${configDiff(st)}</div>
        <div class="card"><div class="card-head"><h2>📦 Deliverables</h2></div>${deliverables(T)}</div>
        <div class="card"><div class="card-head"><h2>📡 Live activity</h2></div>${activityFeed(T)}</div>
      </div>
    </div>`;
  const s = $("#tn-start"), p = $("#tn-stop");
  if (s) s.onclick = async () => { try { await api("tune/start", { method: "POST", body: { resume: true } }); toast("🎛️ Tuner starting…"); setTimeout(pollTune, 1500); } catch (e) { toast(`⚠️ ${esc(e.message)}`); } };
  const np = $("#tn-pass");
  if (np) np.onclick = async () => { try { await api("tune/start", { method: "POST", body: { resume: true, new_pass: true } }); toast("🔁 New tuning pass starting…"); setTimeout(pollTune, 1500); } catch (e) { toast(`⚠️ ${esc(e.message)}`); } };
  if (p) p.onclick = async () => { if (!confirm("Stop the tuner after the replays in flight?")) return; await api("tune/stop", { method: "POST" }); toast("⏹ Stopping after current replays…"); };
  tuneChart($("#tn-chart"), T);
}
function validationCard(v) {
  if (!v || !v.configs) return "";
  const icon = { running: "🔄", finished: "✅", dead: "💀" }[v.status] || "⏸️";
  return `<div class="card" style="margin-top:16px"><div class="card-head"><h2>🧪 Held-out validation</h2>
      <span class="muted">${icon} ${esc(v.status)} · ${v.rounds?.length ?? 0} finalized rounds the tuner never saw${v.heartbeat ? ` · ♥ ${ago(v.heartbeat)}` : ""}</span></div>
    <div class="table-wrap"><table><thead><tr><th>Config</th><th class="num">Rounds</th><th class="num">Mean score</th><th class="num">Mean gap</th><th class="num">Avg rank</th>
      <th class="num">🥇 Wins</th><th class="num">Beats #1</th><th class="num">Top 5</th><th class="num">Max calling</th></tr></thead><tbody>
    ${v.configs.map(c => `<tr><td><b>${esc(c.name)}</b> <code class="muted">${esc(c.hash)}</code>
        ${c.done < c.total ? `<div class="progress" style="margin-top:6px;max-width:220px"><i style="width:${Math.round(100 * c.done / Math.max(1, c.total))}%"></i></div>` : ""}</td>
      <td class="num">${c.done}/${c.total}</td><td class="num">${f4(c.mean_score)}</td><td class="num">${sgn(c.mean_gap)}</td>
      <td class="num">${c.mean_rank ? c.mean_rank.toFixed(1) : "—"}</td><td class="num">${c.wins ?? 0}</td><td class="num">${c.beats_top1 ?? 0}</td>
      <td class="num">${c.top5 ?? 0}</td><td class="num">${runtimeCell(c.max_calling_seconds)}</td></tr>`).join("")}
    </tbody></table></div></div>`;
}
function screenCard(st) {
  const sc = st.screen;
  if (!sc) return "";
  const cands = sc.candidates || [];
  const finished = cands.filter(c => c.done === c.total).length;
  const rows = cands.slice().sort((a, b) => (b.delta ?? -9) - (a.delta ?? -9));
  const maxAbs = Math.max(0.001, ...cands.map(c => Math.abs(c.delta || 0)));
  const bar = d => d == null ? "" : `<span style="display:inline-block;height:8px;border-radius:4px;vertical-align:middle;margin-left:8px;width:${Math.round(60 * Math.abs(d) / maxAbs)}px;background:${d >= 0 ? "var(--good)" : "var(--critical)"}"></span>`;
  return `<div class="card" style="margin-top:16px"><div class="card-head"><h2>🔎 Phase 1 · screening single changes</h2>
      <span class="muted">${finished}/${cands.length} candidates · ${sc.rounds?.length} rounds each · paired Δ score vs current best${sc.status === "done" ? " · ✅ done" : ""}</span></div>
    <div class="progress" style="margin-bottom:12px"><i style="width:${cands.length ? Math.round(100 * finished / cands.length) : 0}%"></i></div>
    ${sc.plan ? `<div class="callout" style="margin-bottom:12px">🗺️ Descent order from screening: ${sc.plan.map(([p, v]) => `<code>${esc(p)}</code> (${v.map(fmtVal).join(", ")})`).join(" → ") || "no single change helped"}</div>` : ""}
    <div class="table-wrap" style="max-height:420px;overflow:auto"><table><thead><tr><th>Change</th><th class="num">Δ score</th><th class="num">Rounds</th><th class="num">Max calling</th></tr></thead><tbody>
    ${rows.map(c => `<tr><td><code>${esc(c.param)}</code> = <b>${esc(fmtVal(c.value))}</b></td>
      <td class="num">${c.delta == null ? "<span class='muted'>⏳</span>" : sgn(c.delta)}${bar(c.delta)}</td>
      <td class="num">${c.done}/${c.total}</td><td class="num">${runtimeCell(c.max_calling_seconds)}</td></tr>`).join("")}
    </tbody></table></div></div>`;
}
function tuneChart(box, T) {
  const ev = (T.events || []).slice().reverse().filter(e => e.kind === "baseline" || e.kind === "candidate");
  if (!ev.length) { box.innerHTML = empty("📈", "Progress appears after the baseline is scored."); return; }
  let bestSoFar = null;
  const bestLine = ev.map(e => { if (e.kind === "baseline" || e.accepted) bestSoFar = e.mean_gap; return bestSoFar; });
  Charts.line(box, {
    series: [{ name: "candidate", color: C.s1, values: ev.map(e => e.mean_gap ?? null) },
             { name: "best so far", color: C.s2, values: bestLine }],
    labels: ev.map((e, i) => e.kind === "baseline" ? "stock" : `#${i}`), fmt: v => v.toFixed(4), height: 260,
    tipTitle: i => ev[i].kind === "baseline" ? "stock baseline" : `${ev[i].param} = ${fmtVal(ev[i].value)} ${ev[i].accepted ? "✅ accepted" : "❌ rejected"}`,
  });
}
function configDiff(st) {
  const b = st.base?.options || {}, t = st.best?.options || {};
  const keys = Object.keys(t).filter(k => t[k] !== b[k]);
  if (!keys.length) return empty("⚖️", "No changes from stock yet.");
  return `<div class="table-wrap"><table><thead><tr><th>Parameter</th><th class="num">Stock</th><th class="num">Tuned</th></tr></thead><tbody>
    ${keys.map(k => `<tr><td><code>${esc(k)}</code></td><td class="num muted">${esc(fmtVal(b[k]))}</td><td class="num"><b>${esc(fmtVal(t[k]))}</b></td></tr>`).join("")}</tbody></table></div>`;
}
function deliverables(T) {
  return `<ul class="checklist">${(T.deliverables || []).map(d => `<li><span class="ico">${!d.exists ? "⏳" : d.uncommitted ? "✳️" : d.committed ? "✅" : "🆕"}</span>
    <div><b>${esc(d.name)}</b> <code class="muted">${esc(d.path)}</code><small>${d.exists ? `${esc(d.status)} · updated ${ago(d.modified)}${d.committed ? ` · last commit ${esc(d.committed)} “${esc(d.commit_subject)}”` : ""}` : "not created yet"}</small></div></li>`).join("")}</ul>`;
}
function activityFeed(T) {
  const items = [];
  for (const e of (T.events || []).slice(0, 40)) {
    const text = e.kind === "candidate" ? `${e.accepted ? "✅" : "❌"} ${e.param} = ${fmtVal(e.value)} · gap ${sgn(e.mean_gap)}`
      : e.kind === "accept" ? `🏆 new best: ${e.param} = ${fmtVal(e.value)}`
      : e.kind === "baseline" ? `📏 baseline scored · gap ${sgn(e.mean_gap)}`
      : e.kind === "start" ? `🚀 tuner started (${e.workers} workers)`
      : e.kind === "screen_start" ? `🔎 screening ${e.candidates} single changes (${e.runs} replays)`
      : e.kind === "screen_done" ? `🗺️ screening done · ${(e.plan || []).length} helpful parameters`
      : `🔔 ${e.kind}`;
    items.push({ ts: e.ts, text });
  }
  for (const j of (S.logs?.journal || []).slice(0, 15)) items.push({ ts: j.ts, text: `📓 ${j.text}` });
  for (const c of (S.logs?.project || []).slice(0, 10)) items.push({ ts: c.date, text: `🛠️ commit ${c.short}: ${c.subject}` });
  items.sort((a, b) => new Date(b.ts) - new Date(a.ts));
  if (!items.length) return empty("📡", "Nothing yet.");
  return `<div class="stack" style="gap:6px;max-height:360px;overflow:auto">${items.slice(0, 40).map(i => `<div class="row" style="align-items:flex-start"><span class="muted" style="min-width:64px">${ago(i.ts)}</span><span style="flex:1">${esc(i.text)}</span></div>`).join("")}</div>`;
}

/* ================= CONFIGS ================= */
async function configs(view) {
  view.innerHTML = `<div class="skeleton"></div>`;
  await Promise.all([load("configs"), load("replays")]);
  const cfgs = S.configs?.configs || [];
  if (!UI.cfgSel || !cfgs.some(c => c.name === UI.cfgSel)) { UI.cfgSel = cfgs[0]?.name || null; UI.cfgDraft = null; }
  const sel = cfgs.find(c => c.name === UI.cfgSel);
  const sums = Object.fromEntries(summaries().map(s => [s.config_hash, s]));
  view.innerHTML = `
    <div class="view-head"><div><h1>⚙️ Variant-caller configs</h1><p>Edit with the exact ranges validators enforce. One invalid value fails the whole round, so the editor checks every change.</p></div></div>
    <div class="grid g3">
      <div class="stack">${cfgs.map(c => {
        const s = sums[c.hash];
        return `<div class="card cfg-card ${c.name === UI.cfgSel ? "sel" : ""}" data-name="${esc(c.name)}">
          <div class="row"><b>${c.tool === "gatk" ? "🧬" : c.tool === "deepvariant" ? "🧠" : "🔧"} ${esc(c.name)}</b><span class="spacer"></span>${c.is_live ? `<span class="chip">🚀 live</span>` : ""}</div>
          <div class="row"><span class="chip">${esc(c.tool)}</span><code class="muted">${esc(c.hash)}</code>${c.validation.valid ? status("good", "valid") : status("critical", "invalid")}</div>
          <div class="muted">${s ? `🏁 ${s.ok} rounds · gap ${sgn(s.mean_gap)} · avg rank ${s.mean_rank ? s.mean_rank.toFixed(1) : "—"}` : "no replays yet"}</div></div>`;
      }).join("") || `<div class="card">${empty("📄", "No configs in configs/.")}</div>`}</div>
      <div class="card span2" id="cfg-editor">${sel ? "" : empty("👈", "Pick a config.")}</div>
    </div>`;
  $$(".cfg-card").forEach(c => c.onclick = () => { UI.cfgSel = c.dataset.name; UI.cfgDraft = null; render(); });
  if (sel) await configEditor($("#cfg-editor"), sel);
}
async function configEditor(box, cfg) {
  const defs = await params(cfg.tool);
  if (!UI.cfgDraft || UI.cfgDraft.base !== cfg.name) UI.cfgDraft = { base: cfg.name, options: { ...cfg.options } };
  const D = UI.cfgDraft.options;
  const changed = Object.keys(defs).filter(k => D[k] !== undefined && D[k] !== cfg.options[k]).length;
  const input = (k, d) => {
    const v = D[k] ?? d.default;
    if (d.type === "bool") return `<select data-k="${k}" data-t="bool"><option value="true" ${v === true ? "selected" : ""}>true</option><option value="false" ${v === false ? "selected" : ""}>false</option></select>`;
    if (d.allowed_values) {
      const opts = d.allowed_values;
      return `<select data-k="${k}" data-t="enum">${opts.map(o => `<option ${String(o) === String(v) ? "selected" : ""}>${esc(o)}</option>`).join("")}</select>`;
    }
    return `<input type="number" data-k="${k}" data-t="${d.type}" value="${esc(v)}" step="${d.type === "int" ? 1 : "any"}" ${d.min != null ? `min="${d.min}"` : ""} ${d.max != null ? `max="${d.max}"` : ""}>`;
  };
  box.innerHTML = `
    <div class="card-head"><h2>✏️ ${esc(cfg.name)}</h2><div class="row">
      <span id="cfg-valid">${status("good", "valid")}</span><span class="chip">${changed} unsaved change${changed === 1 ? "" : "s"}</span></div></div>
    <div class="param-grid">${Object.entries(defs).map(([k, d]) => {
      const v = D[k] ?? d.default, isDefault = v === d.default;
      const range = d.min != null ? `${d.min} – ${d.max}` : (d.allowed_values || ["true", "false"]).join(" · ");
      return `<div class="param ${D[k] !== cfg.options[k] ? "changed" : ""}" data-p="${k}"><span class="pname">${esc(k)}</span>${input(k, d)}
        <span class="phint">${esc(range)} · default ${esc(d.default)}${isDefault ? "" : " · ✳️ tuned"}</span></div>`;
    }).join("")}</div>
    <div id="cfg-errors" style="margin-top:10px"></div>
    <div class="row" style="margin-top:14px">
      <input id="cfg-name" placeholder="new config name, e.g. gatk-pcrnone-v1" style="flex:1;min-width:200px">
      <button id="cfg-save" class="primary">💾 Save as new</button>
      <button id="cfg-over">✍️ Overwrite</button>
      <button id="cfg-reset" class="ghost">↩️ Reset</button>
    </div>
    <div class="row" style="margin-top:10px">
      <button id="cfg-replay">🏁 Replay on all finalized rounds</button>
      <button id="cfg-deploy" class="danger">🚀 Deploy as live miner config</button>
    </div>
    <p class="muted" style="margin:10px 0 0">Deploy copies this file to <code>minos_subnet/configs/${esc(cfg.tool)}.conf</code> (the file the miner submits), backing up the old one in <code>state/config_backups/</code>.</p>`;
  const collect = () => {
    for (const n of $$("[data-k]", box)) {
      const k = n.dataset.k, t = n.dataset.t;
      const v = t === "bool" ? n.value === "true" : t === "int" ? parseInt(n.value, 10) : t === "float" ? parseFloat(n.value) : n.value;
      // Leave parameters the config never set alone while they sit at the default.
      if (!(k in cfg.options) && v === defs[k].default) delete D[k]; else D[k] = v;
    }
    return D;
  };
  const check = debounce(async () => {
    const v = await api("configs/validate", { method: "POST", body: { tool: cfg.tool, options: collect() } });
    $("#cfg-valid").innerHTML = v.valid ? status("good", "valid") : status("critical", "invalid");
    $("#cfg-errors").innerHTML = v.valid ? "" : `<div class="callout warn">⚠️ ${v.errors.map(esc).join("<br>")}</div>`;
    $$(".param", box).forEach(p => p.classList.toggle("bad", v.errors.some(e => e.includes(`'${p.dataset.p}'`))));
  }, 250);
  $$("[data-k]", box).forEach(n => n.addEventListener("input", () => {
    collect();
    n.closest(".param").classList.toggle("changed", D[n.dataset.k] !== cfg.options[n.dataset.k]);
    check();
  }));
  check();
  const save = async overwrite => {
    const name = overwrite ? cfg.name : $("#cfg-name").value.trim();
    if (!name) return toast("✏️ Give the new config a name.");
    try {
      await api("configs/save", { method: "POST", body: { name, tool: cfg.tool, options: collect(), overwrite } });
      toast(`💾 Saved <b>${esc(name)}</b>`);
      UI.cfgSel = name; UI.cfgDraft = null;
      await load("configs", true); render();
    } catch (e) { toast(`⚠️ ${esc(e.message)}`); }
  };
  $("#cfg-save").onclick = () => save(false);
  $("#cfg-over").onclick = () => { if (confirm(`Overwrite ${cfg.name}?`)) save(true); };
  $("#cfg-reset").onclick = () => { UI.cfgDraft = null; render(); };
  $("#cfg-replay").onclick = () => startJob("replay", { config: cfg.name, rounds: finalizedRounds().map(r => r.dir), threads: 2 });
  $("#cfg-deploy").onclick = async () => {
    if (!confirm(`Deploy "${cfg.name}" as the live ${cfg.tool} config? The running miner submits it from the next round.`)) return;
    try {
      const r = await api("configs/deploy", { method: "POST", body: { name: cfg.name } });
      toast(`🚀 Deployed <b>${esc(r.deployed)}</b> · backup ${esc(r.backup)}`);
      await load("configs", true); render();
    } catch (e) { toast(`⚠️ ${esc(e.message)}`); }
  };
}

/* ================= JOBS ================= */
const jobEmoji = k => ({ replay: "🏁", fetch_rounds: "📥", fetch_meta: "🔁", upstream_check: "🛰️" }[k] || "🧪");
function jobTitle(j) {
  const p = j.params || {};
  if (j.kind === "replay") return `Replay ${p.config} · ${p.rounds?.length || 0} rounds · ${p.threads}t`;
  if (j.kind === "fetch_rounds") return `Fetch last ${p.last} rounds`;
  if (j.kind === "fetch_meta") return "Refresh round metadata";
  if (j.kind === "upstream_check") return "Check upstream updates";
  return j.kind;
}
function jobStatus(j) {
  const map = { running: ["warning", "running"], queued: ["", "queued"], done: ["good", "done"], failed: ["critical", "failed"], cancelled: ["", "cancelled"], interrupted: ["serious", "interrupted"] };
  const [k, l] = map[j.status] || ["", j.status];
  return status(k, l);
}
async function startJob(kind, params) {
  try {
    const j = await api("jobs", { method: "POST", body: { kind, params } });
    toast(`${jobEmoji(kind)} Queued: <b>${esc(jobTitle(j))}</b>`);
    UI.jobSel = j.id;
    await load("jobs", true); updateJobsBadge();
    if (UI.tab === "jobs") render();
  } catch (e) { toast(`⚠️ ${esc(e.message)}`); }
}
async function jobs(view) {
  await Promise.all([load("jobs", true), load("configs"), load("rounds")]);
  const js = S.jobs?.jobs || [];
  const cfgs = S.configs?.configs || [];
  const fin = finalizedRounds();
  if (!UI.jobSel && js[0]) UI.jobSel = js[0].id;
  const pick = UI.pick || (UI.pick = new Set(fin.map(r => r.dir)));
  view.innerHTML = `
    <div class="view-head"><div><h1>🧪 Jobs</h1><p>Replays and downloads run one at a time in the background; state and logs survive restarts in <code>data/jobs/</code>.</p></div></div>
    <div class="grid g2">
      <div class="card"><div class="card-head"><h2>🏁 New replay</h2><span class="muted" id="pick-n">${pick.size} rounds</span></div>
        <div class="row" style="margin-bottom:10px">
          <label class="field" style="flex:1">Config<select id="jb-cfg">${cfgs.map(c => `<option>${esc(c.name)}</option>`).join("")}</select></label>
          <label class="field">Threads<select id="jb-thr"><option>2</option><option>4</option><option>8</option></select></label></div>
        <div class="row" style="margin-bottom:8px">
          <button data-q="all">✅ all finalized</button><button data-q="last10">🕒 last 10</button><button data-q="top">🎯 chr11–13</button><button data-q="none" class="ghost">✖ none</button></div>
        <div style="max-height:220px;overflow:auto;border:1px solid var(--border);border-radius:12px;padding:6px 10px">
          ${fin.map(r => `<label class="row" style="padding:3px 0"><input type="checkbox" data-rd="${r.dir}" ${pick.has(r.dir) ? "checked" : ""}>
            <span>${dt(r.round_id)}</span><span class="chip">${esc(r.chromosome)}</span><span class="muted">${regionMb(r.region)?.toFixed(1)} Mb · #1 ${f4(r.top1)}</span></label>`).join("") || empty("🗂️", "No finalized rounds downloaded.")}
        </div>
        <p class="muted" style="margin:8px 0">⏱️ Roughly 2–5 min per round at 2 threads. 2 threads mimics the smallest validators (900 s limit).</p>
        <button class="primary" id="jb-go">▶️ Queue replay</button></div>
      <div class="card"><div class="card-head"><h2>🗂️ Data & maintenance</h2></div>
        <div class="stack">
          <div class="row"><input id="jb-last" type="number" min="1" max="200" value="30" style="width:90px"><button id="jb-fetch">📥 Download last N rounds + metadata</button></div>
          <div class="row"><button id="jb-meta">🔁 Refresh leaderboards & regions</button><span class="muted">for rounds that finalized since</span></div>
          <div class="row"><button id="jb-up">🛰️ Check upstream (minos_subnet) updates</button></div>
          <div class="callout">💡 New rounds are revealed every 72 minutes; leaderboards appear about 2.5 h after a round opens.</div>
        </div></div>
    </div>
    <div class="grid g2" style="margin-top:16px">
      <div class="card"><div class="card-head"><h2>📋 Queue & history</h2></div>
        ${js.length ? `<div class="table-wrap"><table><tbody>${js.map(j => `
          <tr class="click ${j.id === UI.jobSel ? "me" : ""}" data-job="${j.id}"><td>${jobEmoji(j.kind)}</td><td><b>${esc(jobTitle(j))}</b><br><span class="muted">${esc(j.summary || "")}</span>
            ${j.status === "running" ? `<div class="progress" style="margin-top:6px"><i style="width:${Math.round(100 * j.progress / Math.max(1, j.total))}%"></i></div>` : ""}</td>
            <td>${jobStatus(j)}</td><td class="muted">${ago(j.created)}</td>
            <td>${j.status === "running" || j.status === "queued" ? `<button class="danger" data-cancel="${j.id}">⏹</button>` : ""}</td></tr>`).join("")}</tbody></table></div>` : empty("🫧", "No jobs yet.")}</div>
      <div class="card"><div class="card-head"><h2>🖨️ Log</h2><span class="muted">${UI.jobSel ? esc(UI.jobSel) : ""}</span></div><div class="log-box" id="jb-log">Select a job…</div></div>
    </div>`;
  $$("input[data-rd]").forEach(c => c.onchange = () => { c.checked ? pick.add(c.dataset.rd) : pick.delete(c.dataset.rd); $("#pick-n").textContent = `${pick.size} rounds`; });
  $$("button[data-q]").forEach(b => b.onclick = () => {
    pick.clear();
    const q = b.dataset.q;
    const src = q === "last10" ? fin.slice(0, 10) : q === "top" ? fin.filter(r => ["chr11", "chr12", "chr13"].includes(r.chromosome)) : q === "all" ? fin : [];
    src.forEach(r => pick.add(r.dir));
    render();
  });
  $("#jb-go").onclick = () => startJob("replay", { config: $("#jb-cfg").value, rounds: [...pick], threads: +$("#jb-thr").value });
  $("#jb-fetch").onclick = () => startJob("fetch_rounds", { last: +$("#jb-last").value || 30 });
  $("#jb-meta").onclick = () => startJob("fetch_meta", {});
  $("#jb-up").onclick = () => startJob("upstream_check", {});
  $$("tr[data-job]").forEach(tr => tr.onclick = e => { if (e.target.closest("[data-cancel]")) return; UI.jobSel = tr.dataset.job; render(); });
  $$("[data-cancel]").forEach(b => b.onclick = async () => { await api(`jobs/${b.dataset.cancel}/cancel`, { method: "POST" }); toast("⏹ Cancelling…"); await load("jobs", true); render(); });
  refreshLog();
}
async function refreshLog() {
  const box = $("#jb-log");
  if (!box || !UI.jobSel) return;
  const atBottom = box.scrollTop + box.clientHeight >= box.scrollHeight - 20;
  const { lines } = await api(`jobs/${UI.jobSel}/log?tail=600`);
  box.textContent = (lines || []).filter(l => !l.includes("screen size is bogus")).join("\n").replace(/\x1b\[[0-9;]*m/g, "") || "(no output yet)";
  if (atBottom) box.scrollTop = box.scrollHeight;
}

/* ================= LOGS ================= */
async function logs(view) {
  view.innerHTML = `<div class="skeleton"></div>`;
  await load("logs", true);
  const L = S.logs || {};
  const tags = [["🛠️", "dev"], ["🎛️", "tuning"], ["⛏️", "mining"], ["🐛", "issue"], ["💡", "idea"]];
  view.innerHTML = `
    <div class="view-head"><div><h1>📜 Development & update logs</h1><p>Our commits, upstream subnet changes, and a journal for decisions and observations.</p></div></div>
    <div class="grid g2">
      <div class="card"><div class="card-head"><h2>🛠️ Our commits</h2><span class="muted">${(L.project || []).length} commits${L.project_dirty?.length ? ` · ✳️ ${L.project_dirty.length} uncommitted` : " · clean"}</span></div>
        ${(L.project || []).map(commitHtml).join("") || empty("🌱", "No commits.")}</div>
      <div class="stack">
        <div class="card"><div class="card-head"><h2>📓 Journal</h2></div>
          <div class="row" style="margin-bottom:8px"><select id="jn-tag">${tags.map(([e, t]) => `<option value="${t}">${e} ${t}</option>`).join("")}</select></div>
          <textarea id="jn-text" placeholder="What changed, what you observed, what to try next…"></textarea>
          <div class="row" style="margin:8px 0 12px"><button class="primary" id="jn-add">➕ Add entry</button></div>
          <div class="stack" style="gap:8px">${(L.journal || []).map(e => `<div class="journal-entry"><div class="row"><b>${(tags.find(t => t[1] === e.tag) || ["📝"])[0]} ${esc(e.tag)}</b><span class="spacer"></span><span class="muted">${dt(e.ts)}</span></div><div style="white-space:pre-wrap">${esc(e.text)}</div></div>`).join("") || empty("📓", "No entries yet.")}</div></div>
        <div class="card"><div class="card-head"><h2>🛰️ Upstream minos_subnet</h2>
          <div class="row">${L.upstream_behind ? `<span class="chip">⬇️ ${L.upstream_behind} new</span>` : `<span class="chip">✅ up to date (last fetch)</span>`}<button id="lg-up">🔄 Check now</button></div></div>
          ${L.upstream_dirty?.length ? `<div class="callout warn" style="margin-bottom:10px">✳️ ${L.upstream_dirty.length} local change(s) in the clone (auto-update would skip): <code>${L.upstream_dirty.slice(0, 8).map(esc).join(", ")}${L.upstream_dirty.length > 8 ? ` … +${L.upstream_dirty.length - 8} more` : ""}</code></div>` : ""}
          ${(L.upstream || []).slice(0, 15).map(commitHtml).join("")}</div>
      </div>
    </div>`;
  $("#jn-add").onclick = async () => {
    const text = $("#jn-text").value.trim();
    if (!text) return toast("✏️ Write something first.");
    await api("journal", { method: "POST", body: { text, tag: $("#jn-tag").value } });
    toast("📓 Saved"); render();
  };
  $("#lg-up").onclick = () => startJob("upstream_check", {});
}
function commitHtml(c) {
  return `<details class="commit"><summary><code class="muted">${esc(c.short)}</code><b>${esc(c.subject)}</b><span class="spacer"></span><span class="muted">${esc(c.author)} · ${ago(c.date)}</span></summary>
    ${c.body ? `<pre>${esc(c.body.trim())}</pre>` : ""}</details>`;
}

/* ================= SYSTEM ================= */
async function system(view) {
  view.innerHTML = `<div class="skeleton"></div>`;
  await Promise.all([load("system", true), load("live")]);
  const s = S.system || {};
  const imgs = s.docker?.images || [];
  const env = s.env || {};
  view.innerHTML = `
    <div class="view-head"><div><h1>🖥️ System</h1><p>Local environment the miner and replays depend on. Checked ${ago(s.fetched_at)}.</p></div></div>
    <div class="grid g4">
      <div class="card tile"><span class="emoji">🐳</span><span class="label">Docker</span><span class="value">${s.docker?.ok ? "online" : "offline"}</span><span class="sub">${imgs.length} images</span></div>
      <div class="card tile"><span class="emoji">🧬</span><span class="label">Reference</span><span class="value num">${s.reference_chromosomes?.length || 0}/22</span><span class="sub">chromosomes</span></div>
      <div class="card tile"><span class="emoji">💽</span><span class="label">Disk free</span><span class="value num">${s.disk?.free_gb ?? "—"} GB</span><span class="sub">rounds use ${s.disk?.rounds_gb ?? "—"} GB</span></div>
      <div class="card tile"><span class="emoji">🐍</span><span class="label">bittensor</span><span class="value num">${esc(s.bittensor || "—")}</span><span class="sub">${s.cpus} CPUs</span></div>
    </div>
    <div class="grid g2" style="margin-top:16px">
      <div class="card"><div class="card-head"><h2>📦 Required images</h2></div>
        <ul class="checklist">${REQUIRED_IMAGES.map(r => { const hit = imgs.find(i => i[0].startsWith(r)); return `<li><span class="ico">${hit ? "✅" : "❌"}</span><div><b><code>${esc(r)}</code></b><small>${hit ? esc(hit[1]) : "missing — run scripts/setup_miner.sh images"}</small></div></li>`; }).join("")}</ul></div>
      <div class="card"><div class="card-head"><h2>⛏️ Miner</h2></div>
        <dl class="kv">
          <dt>process</dt><dd>${(s.miner_processes || []).length ? status("good", "running") : status("", "not running")}</dd>
          <dt>pm2</dt><dd>${s.pm2 ? "installed" : "not installed"}</dd>
          <dt>wallet</dt><dd>${s.wallet_present ? "found" : "none yet"}</dd>
          <dt>platform</dt><dd>${S.live?.health?.status === "healthy" ? status("good", "healthy") : status("critical", S.live?.health?.status || "unknown")}</dd>
          ${Object.entries(env).map(([k, v]) => `<dt><code>${esc(k)}</code></dt><dd>${v == null ? "<span class='muted'>unset</span>" : `<code>${esc(v)}</code>`}</dd>`).join("")}
        </dl></div>
    </div>
    <div class="card" style="margin-top:16px"><div class="card-head"><h2>🧬 Reference chromosomes</h2></div>
      <div class="row">${Array.from({ length: 22 }, (_, i) => `chr${i + 1}`).map(c => `<span class="chip">${(s.reference_chromosomes || []).includes(c) ? "✅" : "⬜"} ${c}</span>`).join("")}</div></div>`;
}

/* ---------------- sorting ---------------- */
function sortRows(key, rows, getters) {
  const st = UI.sort[key];
  if (!st || !getters[st.k]) return rows;
  const g = getters[st.k];
  return rows.slice().sort((a, b) => {
    const x = g(a), y = g(b);
    if (x == null && y == null) return 0;
    if (x == null) return 1;
    if (y == null) return -1;
    return (x > y ? 1 : x < y ? -1 : 0) * st.dir;
  });
}
function bindSort(key) {
  $$("th[data-sort]").forEach(th => th.onclick = () => {
    const k = th.dataset.sort, cur = UI.sort[key];
    UI.sort[key] = { k, dir: cur?.k === k ? -cur.dir : -1 };
    render();
  });
}
function debounce(fn, ms) { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; }

/* ---------------- polling ---------------- */
let lastJobState = "";
async function pollJobs() {
  await load("jobs", true);
  updateJobsBadge();
  const sig = (S.jobs?.jobs || []).map(j => `${j.id}:${j.status}:${j.progress}`).join("|");
  if (sig !== lastJobState) {
    const finished = lastJobState && (S.jobs?.jobs || []).some(j => (j.status === "done" || j.status === "failed") && !lastJobState.includes(`${j.id}:${j.status}`));
    lastJobState = sig;
    if (finished) {
      await Promise.all(["replays", "rounds", "configs", "logs"].map(k => load(k, true)));
      toast("✅ Job finished — data refreshed");
    }
    if (UI.tab === "jobs" || finished) render();
  }
  if (UI.tab === "jobs") refreshLog();
}
async function pollTune() {
  await Promise.all([load("tune", true), load("logs", true)]);
  const st = S.tune?.state || {};
  const live = ["running", "starting", "stopping"].includes(st.status) && S.tune?.alive;
  $("#tune-badge").hidden = !live;
  if (UI.tab === "tune") render();
  else if (UI.tab === "overview" && $("#ov-work")) $("#ov-work").innerHTML = workBanner();
}
async function pollLive() {
  await load("live", true);
  updatePill();
  if (UI.tab === "live") render();
  tickCountdowns();
}

/* ---------------- boot ---------------- */
document.addEventListener("click", e => { if (e.target.closest("[data-close]")) closeDrawer(); });
document.addEventListener("keydown", e => { if (e.key === "Escape") closeDrawer(); });
$("#refresh-btn").onclick = async () => {
  await api("refresh", { method: "POST" });
  for (const k of Object.keys(S)) if (k !== "params") S[k] = null;
  await pollLive(); render(); toast("🔄 Refreshed");
};
window.addEventListener("hashchange", route);
let resizeT;
window.addEventListener("resize", () => { clearTimeout(resizeT); resizeT = setTimeout(render, 250); });
initTheme();
route();
pollLive();
setInterval(tickCountdowns, 1000);
setInterval(pollLive, 30000);
setInterval(pollJobs, 4000);
pollTune();
setInterval(pollTune, 5000);
