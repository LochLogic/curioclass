// Curio Class kit: what every tool does the same way (motion, sound, read aloud, timing).
// Inlined by scripts/bundle_tool.py from a kit:curio script tag, before the tool's own script.
// One fix here reaches every tool on its next bundle. Docs: docs/KIT.md
const Curio = (() => {
  const $ = id => document.getElementById(id);
  const wait = ms => new Promise(r => setTimeout(r, ms));

  // ---------- motion: the Motion button, the OS reduced-motion setting, remembered across tools ----------
  let reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  try { const m = localStorage.getItem('curio-motion'); if (m) reduce = m === 'calm'; } catch {}
  const motionFns = [];
  function showMotion() {
    document.body.classList.toggle('calm', reduce);
    const b = $('motion');
    if (b) { b.setAttribute('aria-pressed', !reduce); b.textContent = reduce ? '⏸ Motion' : '✨ Motion'; }
    motionFns.forEach(f => f(reduce));
  }

  // ---------- sound: the Sound button turns off chimes and narration (Read still speaks) ----------
  let sound = true;
  const soundFns = [];

  // ---------- speech: recorded clips first, then the best browser voice ----------
  function bestVoice() {
    const voices = speechSynthesis.getVoices().filter(v => /^en(-|_|$)/i.test(v.lang));
    const score = v => (/natural|neural/i.test(v.name) ? 50 : 0) + (/premium|enhanced/i.test(v.name) ? 40 : 0) +
      (/google/i.test(v.name) ? 30 : 0) + (/aria|jenny|ava|samantha|libby|sonia/i.test(v.name) ? 10 : 0) +
      (/en-US/i.test(v.lang) ? 5 : 0) + (v.default ? 1 : 0) - (/david|mark|zira|desktop/i.test(v.name) ? 20 : 0);
    return voices.sort((a, b) => score(b) - score(a))[0] || null;
  }
  if ('speechSynthesis' in window) {
    // Chrome fills its voice list late, so an early line waits for it; cancel() also drops a line still waiting,
    // or it would start after the next one and the tool would talk over itself
    const speak = speechSynthesis.speak.bind(speechSynthesis), cancel = speechSynthesis.cancel.bind(speechSynthesis), held = new Set();
    speechSynthesis.speak = u => {
      if (speechSynthesis.getVoices().length) return speak(u);
      held.add(u);
      const go = () => { if (!held.delete(u)) return; const v = bestVoice(); if (v) { u.voice = v; u.lang = v.lang; } speak(u); };
      speechSynthesis.addEventListener('voiceschanged', go, {once: true});
      setTimeout(go, 1500);
    };
    speechSynthesis.cancel = () => { held.forEach(u => u.onend && u.onend()); held.clear(); cancel(); };
    speechSynthesis.getVoices();
  }
  let clips = {}, rate = .9, talk = 0, clip = null, last = [], heard = false;
  // nothing speaks until the first tap or key: browsers block sound before that, and a tool shouldn't talk on load
  for (const ev of ['pointerdown', 'keydown']) addEventListener(ev, () => { heard = true; }, {once: true, capture: true});
  function stop() { talk++; if (clip) { clip.pause(); clip = null; } if ('speechSynthesis' in window) speechSynthesis.cancel(); }
  function speakOne(text) {
    return new Promise(done => {
      if (clips[text]) { clip = new Audio(clips[text]); clip.onended = clip.onerror = () => done(); clip.play().catch(() => done()); return; }
      if (!('speechSynthesis' in window)) return done();
      const u = new SpeechSynthesisUtterance(text);
      const v = bestVoice(); if (v) { u.voice = v; u.lang = v.lang; }
      u.rate = rate; u.pitch = 1; u.onend = u.onerror = () => done();
      speechSynthesis.speak(u);
    });
  }
  // say one line or several in a row; resolves when the last one ends (or at once when sound is off).
  // force: speak even with Sound off or before the first tap (the Read button)
  async function say(parts, force) {
    if (!heard && !force) return;
    if (!sound && !force) return;
    stop();
    const me = talk;
    last = [].concat(parts);
    for (const p of last) { if (me !== talk) return; await speakOne(p); await wait(150); }
  }

  // ---------- narration: one queue for a tool's lines (Curio.voice, docs/KIT.md "Voice") ----------
  // Two kinds of line: how-to and teaching lines ('how') are spoken the first time, then only shown in the hint;
  // event lines ('event': praise, results, failures) are spoken every time. Every line is checked when its turn comes
  // (scope, valid, needs, maxAge) and dropped, unmarked, when its moment has passed. Welcomes: one per mode, once.
  let voiceOne = null;
  const say0 = say;
  function voice(opts = {}) {
    if (voiceOne) return voiceOne;
    const now = () => Math.round(performance.now());
    const lines = opts.lines || {}, isKey = k => typeof k === 'string' && Object.prototype.hasOwnProperty.call(lines, k) && typeof lines[k] === 'string';
    const said = new Set(), heardSet = new Set(), q = [], log = [];
    let tapped = heard, gen = 0, busy = false, cur = null, readP = Promise.resolve(), readCut = null, nQ = 0, nS = 0, chainN = 0, later = false;
    const est = opts.est || (s => 600 + 62 * s.length);    // pacing when a line is not spoken (Sound off)
    const cap = s => 2500 + 80 * s.length;                   // longest a line may hold the queue (a clip that never ends)
    const scope = () => opts.scope ? opts.scope() : 0;
    // the hint: an element id (default 'hint'), a function, or false (the tool owns it; lines never write it)
    const hintEl = () => $(typeof opts.hint === 'string' ? opts.hint : 'hint');
    const setHint = t => {
      if (opts.hint === false) return;
      if (typeof opts.hint === 'function') return opts.hint(t);
      const h = hintEl(); if (h && h.textContent !== t) h.textContent = t;
    };
    if ((opts.hint === false || typeof opts.hint === 'function') && !opts.read)
      console.warn('Curio.voice: the tool owns the hint, so pass read: () => text (Read falls back to #hint)');
    // the log: repeats of the same silent or dropped line in a row fold into one entry with a count n
    function note(it, as, why) {
      const e = log[log.length - 1];
      if (e && (as === 'silent' || as === 'dropped') && e.as === as && e.why === why && e.key === it.key && e.kind === it.kind) {
        e.n = (e.n || 1) + 1; e.t2 = now(); return;
      }
      log.push({t: now(), key: it.key, kind: it.kind, text: it.text, as, why});
    }
    // a control a line names must be there, enabled and visible: on screen, or in a scroll panel that is on screen
    const inView = r => r.width > 0 && r.height > 0 && r.bottom > 0 && r.right > 0 && r.top < innerHeight && r.left < innerWidth;
    function panel(e) {
      for (let p = e.parentElement; p && p !== document.body && p !== document.documentElement; p = p.parentElement) {
        const s = getComputedStyle(p);
        if (/auto|scroll/.test(s.overflowY + ' ' + s.overflowX) && (p.scrollHeight > p.clientHeight || p.scrollWidth > p.clientWidth)) return p;
      }
      return null;
    }
    const on = s => {
      const e = document.querySelector(s);
      if (!e || e.disabled || e.getAttribute('aria-disabled') === 'true' || !e.getClientRects().length || getComputedStyle(e).visibility === 'hidden') return false;
      if (inView(e.getBoundingClientRect())) return true;
      const p = panel(e); return !!p && inView(p.getBoundingClientRect());
    };
    const ok = it => it.scope === scope() && (!it.valid || it.valid()) && it.needs.every(on) && (!it.maxAge || performance.now() - it.at <= it.maxAge);
    const end = (it, as, why) => { if (it.res) { const r = it.res; it.res = null; r(it.detail ? {as, why} : as); } };
    // one line: a text or a key of opts.lines, or [line, options] for one part of a sequence
    function item(p, o, chain, link) {
      const [line, po = {}] = Array.isArray(p) ? p : [p];
      const text = isKey(line) ? lines[line] : line, kind = po.kind || o.kind;
      const v1 = o.valid, v2 = po.valid;
      return {text, kind: kind === 'how' || kind === 'welcome' ? kind : 'event', key: po.key || (chain ? null : o.key) || (isKey(line) ? line : text),
        valid: v1 && v2 ? () => v1() && v2() : v1 || v2, needs: [].concat(o.needs || [], po.needs || []), maxAge: po.maxAge || o.maxAge, hold: po.hold || o.hold || 0,
        hint: 'hint' in po ? po.hint : 'hint' in o ? o.hint : true, at: performance.now(), scope: scope(), chain, link, detail: o.wait === 'detail'};
    }
    // say(line or [line, line, ...], {kind, key, valid, needs, maxAge, hold, hint, wait, now}). hold: ms a long clip may
    // hold the queue, past the cap (it never shortens it). A list is one sequence: its
    // lines play in order, a newer how-to never splits it, and when one of its lines is dropped the rest go too.
    // Returns true when queued, or with wait a promise: 'spoken', 'silent' or 'dropped' ({as, why} with wait: 'detail')
    function say(x, o = {}) {
      const parts = Array.isArray(x) ? x : [x];
      const chain = parts.length > 1 ? ++chainN : 0;
      const its = parts.map((p, i) => item(p, o, chain, i)), last = its[its.length - 1];
      const p = new Promise(r => { last.res = r; });
      if (!tapped || !sound) {                                // before the first tap, or Sound off: the hint, no voice
        let ms = 0, as = 'silent', why = tapped ? 'off' : 'early';
        for (const it of its) {
          if (as === 'dropped') { note(it, 'dropped', 'chain'); why = 'chain'; continue; }
          if (!ok(it)) { note(it, 'dropped', 'stale'); as = 'dropped'; why = 'stale'; continue; }
          if (it.hint) setHint(it.hint === true ? it.text : it.hint);
          note(it, 'silent', why); ms += est(it.text);
        }
        if (o.wait && ms) wait(ms).then(() => end(last, as, why)); else end(last, as, why);
        return o.wait ? p : false;
      }
      // a newer copy of a line replaces a queued one; a newer how-to replaces older queued how-tos (one step at a time)
      const keys = new Set(its.map(i => i.key)), how = its.some(i => i.kind === 'how');
      dropQueued(x => keys.has(x.key) || (how && x.kind === 'how'), 'newer');
      if (o.now) { dropQueued(null, 'newer'); if (cur) { mark(cur, 'now'); cur.cut(); stop(); } }   // speak now: cut in (Read still wins)
      for (const it of its) { nQ++; q.push(it); }
      pump();
      return o.wait ? p : true;
    }
    async function pump() {
      if (busy) return;
      busy = true;
      const g = gen;
      try {
        for (;;) {
          if (!q.length && later) { later = false; welcome(); }   // a welcome the first tap put off, after the tap's own line
          if (!q.length) break;
          await readP;                                        // Read wins: lines wait for it, never cut it off
          if (g !== gen) return;
          const it = q.shift();
          if (!it) continue;
          if (!ok(it)) { note(it, 'dropped', 'stale'); end(it, 'dropped', 'stale'); dropRest(it); continue; }   // checked when it starts
          if (it.hint) setHint(it.hint === true ? it.text : it.hint);
          if (it.kind === 'how' && said.has(it.key)) { note(it, 'silent', 'heard'); end(it, 'silent', 'heard'); continue; }
          if (it.kind !== 'event') said.add(it.key);          // marked when it plays, never when queued
          heardSet.add(it.key); heardSet.add(it.text);
          nS++; note(it, 'spoken'); it.entry = log[log.length - 1]; cur = it;
          await Promise.race([say0(it.text), wait(Math.max(cap(it.text), it.hold)), new Promise(r => { it.cut = r; })]);
          if (cur === it) cur = null;
          end(it, 'spoken');
          if (g !== gen) return;
        }
      } finally { if (g === gen) busy = false; }
    }
    // the rest of a dropped line's sequence goes with it
    function dropRest(it) { if (it.chain) dropQueued(x => x.chain === it.chain && x.link > it.link, 'chain'); }
    // drop lines that have not started (all, or only those f(line) picks); they stay unmarked so their trigger can
    // queue them again. The line in progress plays on. A dropped line takes the rest of its sequence with it.
    function dropQueued(f, why = 'newer') {
      const keep = [], gone = [], cutAt = new Map();
      for (const x of q) {
        if (x.chain && cutAt.has(x.chain) && x.link > cutAt.get(x.chain)) gone.push([x, 'chain']);
        else if (!f || f(x)) { gone.push([x, why]); if (x.chain && !cutAt.has(x.chain)) cutAt.set(x.chain, x.link); }
        else keep.push(x);
      }
      q.length = 0; q.push(...keep);
      for (const [x, w] of gone) { note(x, 'dropped', w); end(x, 'dropped', w); }
    }
    // stop everything: the queue, the line in progress and Read (mode changes, resets, Sound off)
    // a line cut off while it was playing: its spoken log entry gets cut = why (hush, read, sound, now), for tests
    const mark = (it, why) => { if (it.entry) it.entry.cut = typeof why === 'string' ? why : 'hush'; };
    function hush(why = 'hush') {
      gen++; later = false;
      dropQueued(null, 'hush');
      if (cur) { mark(cur, why); cur.cut(); cur = null; }
      if (readCut) { readCut(); readCut = null; }             // a stopped Read clip never ends: nothing may wait on it
      busy = false; readP = Promise.resolve(); stop();
    }
    // Read: stop the queue, then speak opts.read() (a line or a list), else the hint, even with Sound off
    function read() {
      hush('read');
      const parts = [].concat(opts.read ? opts.read() : (hintEl() || {}).textContent || ''), h = parts.join(' ');
      log.push({t: now(), key: 'read', kind: 'read', text: h, as: 'read'});
      let cut; const c = new Promise(r => { cut = r; }); readCut = cut;
      readP = Promise.race([say0(parts, true), wait(cap(h)), c]).catch(() => {}).then(() => { if (readCut === cut) readCut = null; });
    }
    // the mode's welcome. opts.welcome() gives one entry or a list of them, or null when none fits now. An entry is a
    // key of opts.lines, [key, text] or [key, text or nothing, {valid, needs, hint}]. Each key is said once.
    const entry = e => typeof e === 'string' ? [e, lines[e], {}] : typeof e[1] === 'string' ? [e[0], e[1], e[2] || {}] : [e[0], lines[e[0]], e[1] || {}];
    const wl = () => { const w = opts.welcome && opts.welcome(); return !w ? [] : typeof w === 'string' || typeof w[0] === 'string' ? [entry(w)] : w.map(entry); };
    function welcome() {
      later = false;
      if (!tapped || !sound) return false;
      let any = false;
      for (const [key, text, wo] of wl()) {
        if (said.has(key) || q.some(x => x.key === key)) continue;
        const it = item([text, {...wo, kind: 'welcome', key}], {}, 0, 0), v = it.valid;
        it.valid = () => wl().some(w => w[0] === key) && (!v || v());
        nQ++; q.push(it); any = true;
      }
      if (any) pump();
      return any;
    }
    // the very first tap or key: decide after that tap's own handler has run. Read, Sound, a control that speaks for
    // itself later (opts.speaks), or a tap that queued or started a line skip the welcome, unmarked. With
    // opts.welcomeAfter the skipped welcome comes once the tap's own line has finished (Read and Sound still skip it).
    for (const ev of ['pointerdown', 'keydown']) addEventListener(ev, e => {
      if (tapped) return;
      tapped = true;
      const b = e.target && e.target.closest ? e.target.closest('button') : null, q0 = nQ, s0 = nS;
      let done = false;
      const decide = () => {
        if (done) return; done = true;
        if (b && (b.id === 'read' || b.id === 'sound')) return;
        const speaks = !!(b && opts.speaks && b.matches(opts.speaks) && !b.disabled);
        if (!speaks && nQ === q0 && nS === s0) return welcome();
        if (!opts.welcomeAfter) return;
        later = true;
        if (busy || q.length) return;                         // the tap's line is queued or playing: pump brings the welcome after it
        if (!speaks) return welcome();                        // its line has already had its turn
        setTimeout(() => { if (later && !busy && !q.length) welcome(); }, 4000);   // a line that never came
      };
      const endEv = ev === 'pointerdown' ? 'click' : 'keyup';
      const after = () => { removeEventListener(endEv, after, true); clearTimeout(fb); setTimeout(decide, 0); };
      addEventListener(endEv, after, true);
      const fb = setTimeout(after, 1500);
    }, true);
    soundFns.push(s => { if (!s) hush('sound'); else welcome(); });   // Sound back on: the welcome, if it was never said
    const r = $('read'); if (r) r.onclick = read;
    // every string in opts.lines (nested objects and lists too), once each: for allLines() and voice/lines.json
    const allLines = () => {
      const out = new Set(), walk = v => { if (typeof v === 'string') out.add(v); else if (v && typeof v === 'object') Object.values(v).forEach(walk); };
      walk(lines); return [...out];
    };
    voiceOne = {
      say, how: (x, o) => say(x, {...o, kind: 'how'}), welcome, dropQueued, hush, read, log, said, allLines,
      heard: k => heardSet.has(k) || (isKey(k) && heardSet.has(lines[k])),
      get queue() { return q.map(x => ({key: x.key, kind: x.kind, text: x.text})); },
      get playing() { return cur ? cur.text : null; }, get tapped() { return tapped; },
    };
    return voiceOne;
  }

  // ---------- chimes: a soft sine tone, through one shared audio context ----------
  let ctx = null;
  const audio = () => ctx || (ctx = new (window.AudioContext || window.webkitAudioContext)());
  // nothing sounds before the first tap or key (browsers block it, and a context made before then stays suspended)
  function tone(freq, dur = .3, vol = .05, type = 'sine') {
    if (!sound || !heard) return;
    try {
      const a = audio(), t = a.currentTime, o = a.createOscillator(), g = a.createGain();
      o.type = type; o.frequency.value = freq;
      g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(vol, t + .02); g.gain.exponentialRampToValueAtTime(.0001, t + dur);
      o.connect(g).connect(a.destination); o.start(t); o.stop(t + dur + .05);
    } catch {}
  }
  const yes = () => [523, 659, 784].forEach((f, i) => setTimeout(() => tone(f, .35, .05), i * 110));

  // set everything up once the page is there: {clips: "voice:*", rate: .9, readFallback: () => text}
  function init(opts = {}) {
    clips = opts.clips || {}; if (opts.rate) rate = opts.rate;
    const m = $('motion');
    if (m) m.onclick = () => { reduce = !reduce; try { localStorage.setItem('curio-motion', reduce ? 'calm' : 'on'); } catch {} showMotion(); };
    const s = $('sound');
    if (s) s.onclick = () => {
      sound = !sound;
      s.setAttribute('aria-pressed', sound); s.textContent = sound ? '🔔 Sound' : '🔇 Sound';
      if (!sound) stop();
      soundFns.forEach(f => f(sound));
    };
    const r = $('read');
    if (r) r.onclick = () => voiceOne ? voiceOne.read() : say(last.length ? last : [opts.readFallback ? opts.readFallback() : ($('hint') || {}).textContent || ''], true);
    showMotion();
  }
  // a stage of fixed design size, scaled to fit its box: fit('stage', 'scene', 1000, 620)
  function fit(stageId, sceneId, w = 1000, h = 620) {
    const go = () => { const r = $(stageId).getBoundingClientRect(); $(sceneId).style.setProperty('--s', Math.min(r.width / w, r.height / h)); };
    new ResizeObserver(go).observe($(stageId)); go();
  }

  return {
    init, say, stop, wait, tone, yes, audio, fit, bestVoice, voice,
    get reduce() { return reduce; }, get sound() { return sound; }, get last() { return last; },
    onMotion: f => motionFns.push(f), onSound: f => soundFns.push(f),
  };
})();
