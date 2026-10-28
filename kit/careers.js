// Curio Class family engine: careers. The career sheet (one career's what they do, pay, training, people doing it,
// Try it now, similar careers and sources) and the formatting helpers every careers tool shares. Inlined by
// scripts/bundle_tool.py from a kit:careers script tag, after kit:curio. Spec and API: docs/families/careers.md.
// New features go here and into that doc in the same change.
//
// Data: a tool's careers.json (built by scripts/careers_data.py): {year, clusters: {key: name}, careers: [...]}.
// Each career: id, name, onet, cluster, emoji, does, path, try, uses, riasec[6], zone, ctx, pay, hourly, jobs, and
// optionally the Handbook fields edu, eduNote, level, outlook, ooh, oohTitle, oohJobs, oohPay or oohHourly (BLS
// Occupational Outlook Handbook; oohJobs and oohPay are the Handbook page's own numbers, for its whole group).
// The defaults draw career-match-quiz's sheet as it is live (2026-10): a sibling adds its own blocks and facts.
const Careers = (() => {

  // =====================================================================================================
  // PURE: formatting and lookups, no DOM
  // =====================================================================================================
  const money = n => '$' + Math.round(n).toLocaleString('en-US');
  // pay: a yearly median when BLS has one, else the hourly median (musicians, actors: much of the work is part-time)
  function payText(c) {
    if (c.pay) return {big: money(c.pay), small: `a year, about ${money(c.pay / 2080)} an hour`};
    return {big: '$' + c.hourly.toFixed(2), small: 'an hour; much of the work is part-time, so yearly pay varies a lot'};
  }
  const jobsText = n => n >= 1e6 ? (n / 1e6).toFixed(1).replace(/\.0$/, '') + ' million' : n >= 1e4 ? Math.round(n / 1000).toLocaleString('en-US') + ',000' : n.toLocaleString('en-US');
  // O*NET Job Zones (training), as career-match-quiz shows them
  const ZONE = ['', 'Little or no training', 'High school plus some training', 'Training after high school', '4-year college degree', 'More than 4 years of college'];
  const ZONE_SHORT = ['', 'On the job', 'On the job', '1-2 years after high school', '4-year degree', 'Grad school'];
  // the Handbook's typical entry-level education, merged into five ladder columns (career.level is 0 to 4)
  const LEVELS = [
    {key: 'none', name: 'No degree needed', short: 'No degree', means: 'No formal educational credential, or a high school diploma'},
    {key: 'cert', name: 'Certificate or some college', short: 'Certificate', means: 'A postsecondary nondegree award, or some college'},
    {key: 'assoc', name: "Associate's", short: "Associate's", means: "An associate's degree (about 2 years of college)"},
    {key: 'bach', name: "Bachelor's", short: "Bachelor's", means: "A bachelor's degree (about 4 years of college)"},
    {key: 'grad', name: "Master's, doctoral or professional", short: 'Grad school', means: "A master's, doctoral or professional degree"},
  ];
  const EDU_LEVEL = {'No formal educational credential': 0, 'High school diploma or equivalent': 0, 'Postsecondary nondegree award': 1,
    'Some college, no degree': 1, "Associate's degree": 2, "Bachelor's degree": 3, "Master's degree": 4, 'Doctoral or professional degree': 4};
  // the ladder column: career.level when the data has it (set from eduNote where the Handbook says "See How to Become
  // One"), else from edu; null when the career is not in the Handbook
  const level = c => c.level ?? EDU_LEVEL[c.edu] ?? null;
  // "-2% (Decline)" -> {pct: -2, word: 'Decline', dir: 'down', arrow: '▼'}; null when not in the Handbook
  function outlook(c) {
    const m = /^(-?\d+)%\s*\((.+)\)$/.exec(c.outlook || '');
    if (!m) return null;
    const pct = +m[1], word = m[2], dir = /decline/i.test(word) ? 'down' : /little or no change/i.test(word) ? 'flat' : 'up';
    return {pct, word, dir, arrow: {up: '▲', flat: '▶', down: '▼'}[dir], text: c.outlook};
  }
  const inHandbook = c => !!c.ooh;
  // the Handbook's education wording in plain grade 6-8 words (the exact wording goes under it); "See How to Become
  // One" careers use their level
  const EDU_PLAIN = {'No formal educational credential': 'No diploma or degree needed', 'High school diploma or equivalent': 'A high school diploma',
    'Postsecondary nondegree award': 'A certificate after high school', 'Some college, no degree': 'Some college classes',
    "Associate's degree": "An associate's degree (about 2 years of college)", "Bachelor's degree": "A bachelor's degree (about 4 years of college)",
    "Master's degree": "A master's degree (college after a bachelor's)", 'Doctoral or professional degree': 'A doctoral or professional degree (many years of college)'};
  const LEVEL_PLAIN = ['A high school diploma or less', 'A certificate or some college', "An associate's degree (about 2 years of college)",
    "A bachelor's degree (about 4 years of college)", "A master's degree or more"];
  const eduPlain = c => EDU_PLAIN[c.edu] || LEVEL_PLAIN[level(c)] || c.edu;
  // the Handbook page's own median, when it differs from this job's (its group is larger than the one detailed job)
  function groupPay(c) {
    if (c.oohPay && c.pay && c.oohPay !== c.pay) return money(c.oohPay) + ' a year';
    if (c.oohHourly && !c.pay && c.hourly && c.oohHourly !== c.hourly) return '$' + c.oohHourly.toFixed(2) + ' an hour';
    return null;
  }
  // Pearson correlation of two interest profiles (career-match-quiz's similar careers)
  function corr(a, b) {
    const n = a.length, ma = a.reduce((s, x) => s + x, 0) / n, mb = b.reduce((s, x) => s + x, 0) / n;
    let t = 0, da = 0, db = 0;
    for (let i = 0; i < n; i++) { t += (a[i] - ma) * (b[i] - mb); da += (a[i] - ma) ** 2; db += (b[i] - mb) ** 2; }
    return da && db ? t / Math.sqrt(da * db) : 0;
  }
  // the n careers closest in interests, with a nudge toward the same cluster
  const similar = (c, list, n = 4) => list.filter(o => o !== c && o.id !== c.id)
    .map(o => ({o, r: corr(o.riasec, c.riasec) + (o.cluster === c.cluster ? .15 : 0)})).sort((a, b) => b.r - a.r).slice(0, n).map(x => x.o);
  const esc = s => String(s ?? '').replace(/[&<>"]/g, ch => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[ch]));

  // =====================================================================================================
  // FACTS: one box each in the facts row. A fact is (c, data) => {label, big, small} | null (left out).
  // =====================================================================================================
  const FACTS = {
    // career-match-quiz's label; a sibling can pass payLabel ('Median pay, 2025')
    // when the Handbook page covers a larger group with a different median, the small line says so
    pay: (c, d, o) => { const p = payText(c), g = groupPay(c);
      return {key: 'pay', label: o.payLabel || 'Typical pay', big: p.big, small: p.small + (g ? `. The Handbook page covers a larger group, ${c.oohTitle}: ${g}.` : '')}; },
    training: c => ({key: 'training', label: 'Training', big: ZONE[c.zone], bigSmall: true, small: c.path}),
    // the Handbook's count when the data has it (it includes the self-employed), else the OEWS wage and salary count
    jobs: c => c.oohJobs ? {key: 'jobs', label: 'People doing it', big: jobsText(c.oohJobs),
      small: `jobs in the US in 2025, counting people who work for themselves. Handbook count for all ${c.oohTitle}`}
      : {key: 'jobs', label: 'People doing it', big: c.jobs ? jobsText(c.jobs) : 'Not counted',
      small: c.jobs ? 'jobs in the US (wage and salary)' : 'mostly self-employed, so BLS does not count them'},
    // the Handbook's typical entry-level education, exact wording; where it says "See How to Become One", the
    // Handbook's own sentence for this job is quoted under it
    // plain words in big type; the Handbook's exact wording (and its own sentence where it says "See How to Become
    // One") underneath
    edu: c => inHandbook(c) ? {key: 'edu', label: 'Entry-level education', big: eduPlain(c), bigSmall: true,
      small: `Handbook: "${c.edu}"` + (c.eduNote ? `. For this job: "${c.eduNote}" (How to Become One)` : '')}
      : {key: 'edu', label: 'Entry-level education', big: 'Not in the Handbook', bigSmall: true, small: ''},
    outlook: c => { const o = outlook(c); return o ? {key: 'outlook', label: 'Job outlook, 2025-35', big: `<span class="cr-arrow" aria-hidden="true">${o.arrow}</span> ${o.pct}%`,
      small: `(${esc(o.word)}): projected change in jobs`, raw: true} : {key: 'outlook', label: 'Job outlook, 2025-35', big: 'Not in the Handbook', bigSmall: true, small: ''}; },
  };

  // =====================================================================================================
  // THE SHEET: a dialog over the page. Career-match-quiz's openDetail, shared.
  // =====================================================================================================
  // Careers.sheet({data, ...}) -> {open(id, ctx), close(), isOpen(), current, el}
  //   data         the careers.json object (year, clusters, careers)
  //   facts        fact keys in order (default ['pay', 'training', 'jobs']) or functions (c, data) => {label, big, small}
  //   payLabel     the pay box's label (default 'Typical pay')
  //   blocks       {afterDoes, afterFacts, beforeSimilar, end}: (c, ctx) => html, a sibling's own parts
  //   source       (c, data) => html, the line at the bottom (default: career-match-quiz's)
  //   similarCount how many similar careers (default 4; 0 hides them)
  //   closeLabel   text beside the ✕ (default none: the ✕ alone, labeled Close)
  //   onOpen(c, ctx), onClose(c), afterDraw(el, c, ctx)   hooks
  //   theme        a class added to the overlay, for a tool's own colors (CSS variables below)
  // Esc (anywhere on the page while open) and the backdrop close it; Tab stays inside; focus goes back to what had it.
  // The sheet uses the fixed ids cr-title and cr-close, so a page has one sheet.
  let cssDone = false;
  function css() {
    if (cssDone) return; cssDone = true;
    const s = document.createElement('style');
    s.textContent = `
.cr-sheet{position:fixed;inset:0;background:var(--cr-backdrop,#1d234066);display:flex;align-items:center;justify-content:center;z-index:40;padding:18px}
.cr-detail{background:var(--cr-bg,#fff);color:var(--cr-ink,#1d2340);border-radius:26px;max-width:760px;width:100%;max-height:calc(100vh - 36px);overflow:auto;box-shadow:0 30px 80px #0005;position:relative}
.cr-head{display:flex;gap:16px;align-items:center;padding:20px 116px 14px 22px;border-bottom:1px solid var(--cr-line,#e7ded3)}
.cr-head .cr-em{font-size:64px;line-height:1}
.cr-head h2{margin:0;font:800 30px/1.1 'Segoe UI',sans-serif}
.cr-head p{margin:4px 0 0;color:var(--cr-muted,#5b6178);font-weight:600}
.cr-close{position:absolute;top:12px;right:12px;min-width:46px;height:46px;border-radius:999px;border:1px solid var(--cr-line,#e7ded3);background:var(--cr-bg,#fff);color:inherit;font-size:20px;font-weight:700;padding:0 12px;display:inline-flex;align-items:center;gap:6px;justify-content:center}
.cr-close span{font-size:15px}
.cr-body{padding:16px 22px 22px;display:grid;gap:14px}
.cr-does{font-size:19px;line-height:1.45;margin:0}
.cr-facts{display:grid;grid-template-columns:repeat(var(--cr-cols,3),1fr);gap:10px}
.cr-fact{background:var(--cr-fact,#fbf6f0);border-radius:14px;padding:10px 12px}
.cr-fact>span{display:block;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--cr-muted,#5b6178)}
.cr-fact b{font-size:20px;font-variant-numeric:tabular-nums}
.cr-fact b.cr-bs{font-size:17px}
.cr-fact small{display:block;color:var(--cr-muted,#5b6178);font-size:12.5px;margin-top:2px;line-height:1.35}
.cr-body h3{margin:0 0 6px;font:800 13px/1 'Segoe UI',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--cr-muted,#5b6178)}
.cr-try{background:var(--cr-try,#fff6dc);border-left:5px solid var(--cr-try-line,#f5b82e);border-radius:10px;padding:10px 12px;font-size:15px;line-height:1.45}
.cr-sim{display:flex;flex-wrap:wrap;gap:8px}
.cr-sim button{border:1px solid var(--cr-line,#e7ded3);background:var(--cr-chip,#fff);color:inherit;border-radius:999px;min-height:var(--cr-target,40px);padding:0 14px;font-weight:700;font-size:14px}
.cr-note{margin:0;color:var(--cr-muted,#5b6178);font-size:13.5px;line-height:1.45}
.cr-note a{color:var(--cr-link,inherit);font-weight:700}
@media (max-width:640px){.cr-facts{grid-template-columns:1fr}}
@media (max-width:560px){.cr-sheet{align-items:flex-end;padding:0}.cr-detail{border-radius:20px 20px 0 0;max-height:92vh}
  .cr-head{padding:14px 64px 10px 14px;gap:10px}.cr-head .cr-em{font-size:44px}.cr-head h2{font-size:23px}.cr-body{padding:12px 14px 18px}.cr-does{font-size:17px}}
@media (max-height:520px){.cr-sheet{padding:8px}.cr-detail{max-height:calc(100vh - 16px);border-radius:18px}.cr-head{padding:10px 64px 8px 14px;gap:10px}.cr-head .cr-em{font-size:40px}.cr-head h2{font-size:22px}
  .cr-body{padding:10px 14px 14px;gap:10px}.cr-does{font-size:16px}.cr-fact{padding:7px 10px}.cr-fact b{font-size:17px}}
`;
    document.head.append(s);
  }

  function sheet(o = {}) {
    css();
    const data = o.data, list = data.careers, byId = Object.fromEntries(list.map(c => [c.id, c]));
    const facts = o.facts || ['pay', 'training', 'jobs'];
    const blocks = o.blocks || {};
    const source = o.source || (c => `Pay and job counts: BLS, May ${data.year}, national. Interests and work style: O*NET ${esc(c.onet)}.`);
    const ov = document.createElement('div');
    ov.className = 'cr-sheet' + (o.theme ? ' ' + o.theme : ''); ov.hidden = true;
    const box = document.createElement('div');
    box.className = 'cr-detail'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.setAttribute('aria-labelledby', 'cr-title');
    ov.append(box); (o.root || document.body).append(ov);
    let lastFocus = null, current = null, ctx0 = null;

    function factHTML(c) {
      const fs = facts.map(f => typeof f === 'function' ? f(c, data, o) : FACTS[f](c, data, o)).filter(Boolean);
      return `<div class="cr-facts" style="--cr-cols:${o.factCols || Math.min(fs.length, 3)}">${fs.map(f => `<div class="cr-fact cr-f-${f.key || 'x'}"><span>${esc(f.label)}</span><b class="${f.bigSmall ? 'cr-bs' : ''}">${f.raw ? f.big : esc(f.big)}</b>${f.small ? `<small>${f.raw ? f.small : esc(f.small)}</small>` : ''}</div>`).join('')}</div>`;
    }
    function open(id, ctx) {
      const c = byId[id]; if (!c) return;
      if (ov.hidden) lastFocus = document.activeElement;
      current = c; ctx0 = ctx || {};
      const b = (k) => blocks[k] ? blocks[k](c, ctx0) || '' : '';
      const sim = o.similarCount === 0 ? [] : similar(c, list, o.similarCount || 4);
      box.innerHTML = `<button class="cr-close" id="cr-close" type="button" aria-label="Close">✕${o.closeLabel ? `<span>${esc(o.closeLabel)}</span>` : ''}</button>
        <div class="cr-head"><span class="cr-em" aria-hidden="true">${c.emoji}</span><div><h2 id="cr-title">${esc(c.name)}</h2><p>${esc(data.clusters[c.cluster])}</p></div></div>
        <div class="cr-body">
          <p class="cr-does">${esc(c.does)}</p>
          ${b('afterDoes')}
          ${factHTML(c)}
          ${b('afterFacts')}
          <div class="cr-try"><b>Try it now:</b> ${esc(c.try)}</div>
          ${b('beforeSimilar')}
          ${sim.length ? `<div><h3>Similar careers</h3><div class="cr-sim">${sim.map(s => `<button type="button" data-id="${s.id}">${s.emoji} ${esc(s.name)}</button>`).join('')}</div></div>` : ''}
          ${b('end')}
          <p class="cr-note">${source(c, data)}</p>
        </div>`;
      ov.hidden = false;
      box.querySelector('#cr-close').onclick = () => close();
      box.querySelectorAll('.cr-sim button').forEach(btn => btn.onclick = () => open(btn.dataset.id, {from: 'similar'}));
      box.scrollTop = 0;
      if (o.afterDraw) o.afterDraw(box, c, ctx0);
      box.querySelector('#cr-close').focus({preventScroll: true});
      if (!(window.Curio && Curio.reduce) && box.animate) box.animate([{transform: 'translateY(30px) scale(.97)', opacity: 0}, {transform: 'none', opacity: 1}], {duration: 260, easing: 'ease-out'});
      if (o.onOpen) o.onOpen(c, ctx0);
    }
    function close() {
      if (ov.hidden) return;
      const c = current;
      ov.hidden = true; current = null;
      if (lastFocus && lastFocus.isConnected && lastFocus.focus) lastFocus.focus({preventScroll: true});
      if (o.onClose) o.onClose(c);
    }
    ov.addEventListener('click', e => { if (e.target === ov) close(); });
    // keys go through document (capture) while the sheet is open, so Esc works even after a click on its text moved
    // focus to the page; Tab stays inside the sheet
    const FOCUSABLE = 'button:not([disabled]), a[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';
    document.addEventListener('keydown', e => {
      if (ov.hidden) return;
      if (e.key === 'Escape') { e.preventDefault(); e.stopPropagation(); close(); return; }
      if (e.key !== 'Tab') return;
      const f = [...box.querySelectorAll(FOCUSABLE)]; if (!f.length) return;
      const a = document.activeElement;
      if (!box.contains(a)) { e.preventDefault(); f[e.shiftKey ? f.length - 1 : 0].focus({preventScroll: true}); }
      else if (e.shiftKey && a === f[0]) { e.preventDefault(); f[f.length - 1].focus({preventScroll: true}); }
      else if (!e.shiftKey && a === f[f.length - 1]) { e.preventDefault(); f[0].focus({preventScroll: true}); }
    }, true);
    return {open, close, isOpen: () => !ov.hidden, get current() { return current; }, el: ov, box};
  }

  return {money, payText, jobsText, ZONE, ZONE_SHORT, LEVELS, EDU_LEVEL, EDU_PLAIN, level, eduPlain, groupPay, outlook, inHandbook, corr, similar, esc, FACTS, sheet};
})();
