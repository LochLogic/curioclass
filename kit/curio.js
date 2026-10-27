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
  // (valid, needs, maxAge) and dropped, unmarked, when its moment has passed. Welcomes: one per mode, once.
  let voiceOne = null;
  const say0 = say;
  function voice(opts = {}) {
    if (voiceOne) return voiceOne;
    const now = () => Math.round(performance.now());
    const said = new Set(), q = [], log = [];
    let tapped = heard, gen = 0, busy = false, cur = null, readP = Promise.resolve(), readCut = null, nQ = 0, nS = 0;
    const est = opts.est || (s => 600 + 62 * s.length);    // pacing when a line is not spoken (Sound off)
    const cap = s => 2500 + 80 * s.length;                   // longest a line may hold the queue (a clip that never ends)
    const hintEl = () => $(typeof opts.hint === 'string' ? opts.hint : 'hint');
    const setHint = t => { if (typeof opts.hint === 'function') return opts.hint(t); const h = hintEl(); if (h && h.textContent !== t) h.textContent = t; };
    const note = (it, as, why) => log.push({t: now(), key: it.key, kind: it.kind, text: it.text, as, why});
    // a control a line names must be there, shown and enabled
    const on = s => { const e = document.querySelector(s); return !!e && !e.disabled && e.getAttribute('aria-disabled') !== 'true' && e.getClientRects().length > 0; };
    const ok = it => (!it.valid || it.valid()) && [].concat(it.needs || []).every(on) && (!it.maxAge || performance.now() - it.at <= it.maxAge);
    const end = (it, as) => { if (it.res) { it.res(as); it.res = null; } };
    function push(it) {
      nQ++;
      q.push(it);
      pump();
    }
    // say(text, {kind, key, valid, needs, maxAge, hint, wait, now}); returns true when queued, or with wait a promise
    // that resolves 'spoken', 'silent' or 'dropped' once the line has had its turn
    function say(text, o = {}) {
      const kind = o.kind === 'how' ? 'how' : 'event';
      const it = {text, kind, key: o.key || text, valid: o.valid, needs: o.needs, maxAge: o.maxAge, hint: o.hint !== false, at: performance.now()};
      const p = new Promise(r => { it.res = r; });
      if (!tapped || !sound) {                                // before the first tap, or Sound off: the hint, no voice
        if (ok(it)) { if (it.hint) setHint(text); note(it, 'silent', tapped ? 'off' : 'early'); }
        else { note(it, 'dropped', 'stale'); end(it, 'dropped'); return o.wait ? p : false; }
        if (o.wait) wait(est(text)).then(() => end(it, 'silent')); else end(it, 'silent');
        return o.wait ? p : false;
      }
      // a newer copy of a line replaces a queued one; a newer how-to replaces older queued how-tos (one step at a time)
      dropQueued(x => x.key === it.key || (kind === 'how' && x.kind === 'how'), 'newer');
      if (o.now) { dropQueued(null, 'newer'); if (cur) { cur.cut(); stop(); } }   // speak now: cut in (Read still wins)
      push(it);
      return o.wait ? p : true;
    }
    async function pump() {
      if (busy) return;
      busy = true;
      const g = gen;
      try {
        while (q.length) {
          await readP;                                        // Read wins: lines wait for it, never cut it off
          if (g !== gen) return;
          const it = q.shift();
          if (!it) continue;
          if (!ok(it)) { note(it, 'dropped', 'stale'); end(it, 'dropped'); continue; }   // checked when it starts
          if (it.hint) setHint(it.text);
          if (it.kind === 'how' && said.has(it.key)) { note(it, 'silent', 'heard'); end(it, 'silent'); continue; }
          if (it.kind !== 'event') said.add(it.key);          // marked when it plays, never when queued
          nS++; note(it, 'spoken'); cur = it;
          await Promise.race([say0(it.text), wait(cap(it.text)), new Promise(r => { it.cut = r; })]);
          if (cur === it) cur = null;
          end(it, 'spoken');
          if (g !== gen) return;
        }
      } finally { if (g === gen) busy = false; }
    }
    // drop lines that have not started (all, or only those f(line) picks); they stay unmarked so their trigger can
    // queue them again. The line in progress plays on.
    function dropQueued(f, why = 'newer') {
      for (let i = q.length - 1; i >= 0; i--) if (!f || f(q[i])) { const [it] = q.splice(i, 1); note(it, 'dropped', why); end(it, 'dropped'); }
    }
    // stop everything: the queue, the line in progress and Read (mode changes, resets, Sound off)
    function hush() {
      gen++;
      dropQueued(null, 'hush');
      if (cur) { cur.cut(); cur = null; }
      if (readCut) { readCut(); readCut = null; }             // a stopped Read clip never ends: nothing may wait on it
      busy = false; readP = Promise.resolve(); stop();
    }
    // Read: stop the queue, then speak the current hint, even with Sound off
    function read() {
      hush();
      const h = opts.read ? opts.read() : (hintEl() || {}).textContent || '';
      log.push({t: now(), key: 'read', kind: 'read', text: h, as: 'read'});
      let cut; const c = new Promise(r => { cut = r; }); readCut = cut;
      readP = Promise.race([say0([h], true), wait(cap(h)), c]).catch(() => {}).then(() => { if (readCut === cut) readCut = null; });
    }
    // the mode's welcome (opts.welcome() gives [key, text], a list of them, or null when it does not fit now);
    // each key is said once; returns true when something was queued
    const wl = () => { const w = opts.welcome && opts.welcome(); return !w ? [] : typeof w[0] === 'string' ? [w] : w; };
    function welcome() {
      if (!tapped || !sound) return false;
      let any = false;
      for (const [key, text] of wl()) {
        if (said.has(key) || q.some(x => x.key === key)) continue;
        push({text, kind: 'welcome', key, hint: true, at: performance.now(), valid: () => wl().some(w => w[0] === key)});
        any = true;
      }
      return any;
    }
    // the very first tap or key: decide after that tap's own handler has run. Read, Sound, a control that speaks for
    // itself later (opts.speaks), or a tap that queued or started a line skip the welcome, unmarked.
    for (const ev of ['pointerdown', 'keydown']) addEventListener(ev, e => {
      if (tapped) return;
      tapped = true;
      const b = e.target && e.target.closest ? e.target.closest('button') : null, q0 = nQ, s0 = nS;
      let done = false;
      const decide = () => {
        if (done) return; done = true;
        if (b && (b.id === 'read' || b.id === 'sound')) return;
        if (b && opts.speaks && b.matches(opts.speaks) && !b.disabled) return;
        if (nQ !== q0 || nS !== s0) return;
        welcome();
      };
      const endEv = ev === 'pointerdown' ? 'click' : 'keyup';
      const after = () => { removeEventListener(endEv, after, true); clearTimeout(fb); setTimeout(decide, 0); };
      addEventListener(endEv, after, true);
      const fb = setTimeout(after, 1500);
    }, true);
    soundFns.push(s => { if (!s) hush(); else welcome(); });   // Sound back on: the welcome, if it was never said
    const r = $('read'); if (r) r.onclick = read;
    voiceOne = {
      say, how: (text, o) => say(text, {...o, kind: 'how'}), welcome, dropQueued, hush, read, log, said,
      get queue() { return q.map(x => ({key: x.key, kind: x.kind, text: x.text})); },
      get playing() { return cur ? cur.text : null; }, get tapped() { return tapped; },
    };
    return voiceOne;
  }

  // ---------- chimes: a soft sine tone, through one shared audio context ----------
  let ctx = null;
  const audio = () => ctx || (ctx = new (window.AudioContext || window.webkitAudioContext)());
  function tone(freq, dur = .3, vol = .05, type = 'sine') {
    if (!sound) return;
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
