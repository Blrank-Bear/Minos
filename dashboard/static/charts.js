/* Minimal SVG charts with hover tooltips. Colors are CSS custom properties. */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const tip = () => document.getElementById("tooltip");

  function el(name, attrs = {}, parent) {
    const n = document.createElementNS(NS, name);
    for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
    if (parent) parent.appendChild(n);
    return n;
  }

  function niceTicks(min, max, count = 5) {
    if (!isFinite(min) || !isFinite(max)) return [0, 1];
    if (min === max) { const d = Math.abs(min) * 0.05 || 0.01; min -= d; max += d; }
    const span = max - min;
    const step0 = span / count;
    const mag = Math.pow(10, Math.floor(Math.log10(step0)));
    const norm = step0 / mag;
    const step = (norm < 1.5 ? 1 : norm < 3 ? 2 : norm < 7 ? 5 : 10) * mag;
    const lo = Math.floor(min / step) * step, hi = Math.ceil(max / step) * step;
    const out = [];
    for (let v = lo; v <= hi + step / 2; v += step) out.push(+v.toFixed(10));
    return out;
  }

  function showTip(evt, html) {
    const t = tip();
    t.innerHTML = html;
    t.hidden = false;
    const pad = 14, r = t.getBoundingClientRect();
    let x = evt.clientX + pad, y = evt.clientY + pad;
    if (x + r.width > innerWidth - 8) x = evt.clientX - r.width - pad;
    if (y + r.height > innerHeight - 8) y = evt.clientY - r.height - pad;
    t.style.left = x + "px";
    t.style.top = y + "px";
  }
  function hideTip() { tip().hidden = true; }

  function legend(items) {
    const d = document.createElement("div");
    d.className = "legend";
    d.innerHTML = items.map(i =>
      `<span><i class="${i.dot ? "dot" : ""}" style="background:${i.color}"></i>${i.name}</span>`).join("");
    return d;
  }

  /**
   * Line chart. opts: {series:[{name,color,values:[y|null]}], labels:[x label],
   * fmt:y=>str, height, yMin, yMax, tipTitle:i=>str}
   */
  function line(container, opts) {
    container.innerHTML = "";
    const series = opts.series.filter(s => s.values.some(v => v != null));
    if (series.length > 1) container.appendChild(legend(series));
    const W = Math.max(320, container.clientWidth || 640), H = opts.height || 260;
    const m = { l: 52, r: 74, t: 10, b: 30 };
    const all = series.flatMap(s => s.values).filter(v => v != null);
    const ticks = niceTicks(opts.yMin ?? Math.min(...all), opts.yMax ?? Math.max(...all));
    const y0 = ticks[0], y1 = ticks[ticks.length - 1];
    const n = opts.labels.length;
    const X = i => m.l + (n <= 1 ? (W - m.l - m.r) / 2 : (i * (W - m.l - m.r)) / (n - 1));
    const Y = v => m.t + (H - m.t - m.b) * (1 - (v - y0) / (y1 - y0 || 1));
    const fmt = opts.fmt || (v => v.toFixed(3));
    const wrap = document.createElement("div");
    wrap.className = "chart";
    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": opts.aria || "line chart" }, wrap);
    for (const t of ticks) {
      el("line", { x1: m.l, x2: W - m.r, y1: Y(t), y2: Y(t), class: "gridline" }, svg);
      el("text", { x: m.l - 8, y: Y(t) + 4, "text-anchor": "end", class: "tick" }, svg).textContent = fmt(t);
    }
    el("line", { x1: m.l, x2: W - m.r, y1: H - m.b, y2: H - m.b, class: "axis" }, svg);
    const every = Math.max(1, Math.ceil(n / Math.floor((W - m.l - m.r) / 70)));
    opts.labels.forEach((lab, i) => {
      if (i % every) return;
      el("text", { x: X(i), y: H - m.b + 18, "text-anchor": "middle", class: "tick" }, svg).textContent = lab;
    });
    for (const s of series) {
      let d = "", pen = false;
      s.values.forEach((v, i) => {
        if (v == null) { pen = false; return; }
        d += `${pen ? "L" : "M"}${X(i).toFixed(1)},${Y(v).toFixed(1)}`;
        pen = true;
      });
      el("path", { d, fill: "none", stroke: s.color, "stroke-width": 2, "stroke-linejoin": "round", "stroke-linecap": "round" }, svg);
      s.values.forEach((v, i) => {
        if (v == null) return;
        el("circle", { cx: X(i), cy: Y(v), r: n > 40 ? 2.5 : 4, fill: s.color, stroke: "var(--surface-solid)", "stroke-width": 2 }, svg);
      });
    }
    // Direct labels at each series' last point (selective: one per series),
    // nudged apart vertically so near-identical series don't collide.
    if (series.length <= 4) {
      const labs = series.map(s => {
        const li = s.values.map((v, i) => v == null ? -1 : i).filter(i => i >= 0).pop();
        return li == null ? null : { name: s.name, x: X(li) + 8, y: Y(s.values[li]) + 4 };
      }).filter(Boolean).sort((a, b) => a.y - b.y);
      for (let i = 1; i < labs.length; i++) labs[i].y = Math.max(labs[i].y, labs[i - 1].y + 13);
      for (const l of labs) el("text", { x: l.x, y: l.y, class: "lbl" }, svg).textContent = l.name;
    }
    const cross = el("line", { y1: m.t, y2: H - m.b, class: "axis", visibility: "hidden", "stroke-dasharray": "3 3" }, svg);
    const hit = el("rect", { x: m.l, y: m.t, width: W - m.l - m.r, height: H - m.t - m.b, class: "hit" }, svg);
    hit.addEventListener("mousemove", evt => {
      const box = svg.getBoundingClientRect();
      const px = ((evt.clientX - box.left) / box.width) * W;
      const i = Math.max(0, Math.min(n - 1, Math.round(((px - m.l) / (W - m.l - m.r)) * (n - 1))));
      cross.setAttribute("x1", X(i)); cross.setAttribute("x2", X(i)); cross.setAttribute("visibility", "visible");
      const rows = series.map(s => s.values[i] == null ? "" :
        `<div class="tt-row"><span><i style="background:${s.color}"></i>${s.name}</span><b class="num">${fmt(s.values[i])}</b></div>`).join("");
      showTip(evt, `<div class="tt-title">${opts.tipTitle ? opts.tipTitle(i) : opts.labels[i]}</div>${rows}`);
    });
    hit.addEventListener("mouseleave", () => { cross.setAttribute("visibility", "hidden"); hideTip(); });
    if (opts.onClick) hit.addEventListener("click", evt => {
      const box = svg.getBoundingClientRect();
      const px = ((evt.clientX - box.left) / box.width) * W;
      opts.onClick(Math.max(0, Math.min(n - 1, Math.round(((px - m.l) / (W - m.l - m.r)) * (n - 1)))));
    });
    container.appendChild(wrap);
  }

  /** Vertical bars from a zero baseline. opts: {values:[y|null], labels, color, fmt, tipTitle, height} */
  function bars(container, opts) {
    container.innerHTML = "";
    const W = Math.max(320, container.clientWidth || 640), H = opts.height || 220;
    const m = { l: 56, r: 12, t: 10, b: 30 };
    const vals = opts.values.filter(v => v != null);
    const ticks = niceTicks(Math.min(0, ...vals), Math.max(0, ...vals));
    const y0 = ticks[0], y1 = ticks[ticks.length - 1];
    const n = opts.labels.length;
    const band = (W - m.l - m.r) / Math.max(1, n);
    const bw = Math.max(3, Math.min(28, band - 2));
    const Y = v => m.t + (H - m.t - m.b) * (1 - (v - y0) / (y1 - y0 || 1));
    const fmt = opts.fmt || (v => v.toFixed(3));
    const wrap = document.createElement("div");
    wrap.className = "chart";
    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": opts.aria || "bar chart" }, wrap);
    for (const t of ticks) {
      el("line", { x1: m.l, x2: W - m.r, y1: Y(t), y2: Y(t), class: "gridline" }, svg);
      el("text", { x: m.l - 8, y: Y(t) + 4, "text-anchor": "end", class: "tick" }, svg).textContent = fmt(t);
    }
    el("line", { x1: m.l, x2: W - m.r, y1: Y(0), y2: Y(0), class: "axis" }, svg);
    const every = Math.max(1, Math.ceil(n / Math.floor((W - m.l - m.r) / 70)));
    opts.values.forEach((v, i) => {
      const cx = m.l + band * i + band / 2;
      if (!(i % every)) el("text", { x: cx, y: H - m.b + 18, "text-anchor": "middle", class: "tick" }, svg).textContent = opts.labels[i];
      if (v == null) return;
      const top = Math.min(Y(v), Y(0)), h = Math.max(1, Math.abs(Y(v) - Y(0)));
      const r = Math.min(4, bw / 2, h);
      // Rounded at the data end only, square on the baseline.
      const up = v >= 0, x = cx - bw / 2;
      const d = up
        ? `M${x},${top + h}V${top + r}Q${x},${top} ${x + r},${top}H${x + bw - r}Q${x + bw},${top} ${x + bw},${top + r}V${top + h}Z`
        : `M${x},${top}V${top + h - r}Q${x},${top + h} ${x + r},${top + h}H${x + bw - r}Q${x + bw},${top + h} ${x + bw},${top + h - r}V${top}Z`;
      const color = typeof opts.color === "function" ? opts.color(v, i) : opts.color;
      el("path", { d, fill: color }, svg);
      const hit = el("rect", { x: m.l + band * i, y: m.t, width: band, height: H - m.t - m.b, class: "hit" }, svg);
      hit.addEventListener("mousemove", evt => showTip(evt,
        `<div class="tt-title">${opts.tipTitle ? opts.tipTitle(i) : opts.labels[i]}</div>
         <div class="tt-row"><span>${opts.valueName || "value"}</span><b class="num">${fmt(v)}</b></div>`));
      hit.addEventListener("mouseleave", hideTip);
      if (opts.onClick) hit.addEventListener("click", () => opts.onClick(i));
    });
    container.appendChild(wrap);
  }

  /**
   * Horizontal strip of dots: the field, plus highlighted marks.
   * opts: {field:[{v,label}], marks:[{v,label,color}], fmt, height}
   */
  function strip(container, opts) {
    container.innerHTML = "";
    const W = Math.max(320, container.clientWidth || 640), H = opts.height || 120;
    const m = { l: 16, r: 16, t: 14, b: 28 };
    const vals = [...opts.field.map(f => f.v), ...(opts.marks || []).map(k => k.v)].filter(v => v != null);
    const ticks = niceTicks(Math.min(...vals), Math.max(...vals), 6);
    const x0 = ticks[0], x1 = ticks[ticks.length - 1];
    const X = v => m.l + (W - m.l - m.r) * (v - x0) / (x1 - x0 || 1);
    const fmt = opts.fmt || (v => v.toFixed(4));
    const wrap = document.createElement("div");
    wrap.className = "chart";
    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": "score distribution" }, wrap);
    const base = H - m.b;
    for (const t of ticks) {
      el("line", { x1: X(t), x2: X(t), y1: m.t, y2: base, class: "gridline" }, svg);
      el("text", { x: X(t), y: base + 18, "text-anchor": "middle", class: "tick" }, svg).textContent = fmt(t);
    }
    el("line", { x1: m.l, x2: W - m.r, y1: base, y2: base, class: "axis" }, svg);
    // Beeswarm-lite: stack dots that would overlap.
    const placed = [];
    const yFor = x => {
      let row = 0;
      while (placed.some(p => p.row === row && Math.abs(p.x - x) < 9)) row++;
      placed.push({ x, row });
      return base - 8 - row * 9;
    };
    const dot = (v, label, color, r) => {
      const x = X(v), y = yFor(x);
      const c = el("circle", { cx: x, cy: Math.max(m.t, y), r, fill: color, stroke: "var(--surface-solid)", "stroke-width": 2 }, svg);
      const hit = el("circle", { cx: x, cy: Math.max(m.t, y), r: r + 5, class: "hit" }, svg);
      hit.addEventListener("mousemove", evt => showTip(evt, `<div class="tt-title">${label}</div><div class="num">${fmt(v)}</div>`));
      hit.addEventListener("mouseleave", hideTip);
      return c;
    };
    opts.field.forEach(f => dot(f.v, f.label, "var(--field)", 4));
    (opts.marks || []).forEach(k => dot(k.v, k.label, k.color, 5.5));
    container.appendChild(wrap);
  }

  window.Charts = { line, bars, strip, legend };
})();
