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
    if (r) r.onclick = () => say(last.length ? last : [opts.readFallback ? opts.readFallback() : ($('hint') || {}).textContent || ''], true);
    showMotion();
  }
  // a stage of fixed design size, scaled to fit its box: fit('stage', 'scene', 1000, 620)
  function fit(stageId, sceneId, w = 1000, h = 620) {
    const go = () => { const r = $(stageId).getBoundingClientRect(); $(sceneId).style.setProperty('--s', Math.min(r.width / w, r.height / h)); };
    new ResizeObserver(go).observe($(stageId)); go();
  }

  return {
    init, say, stop, wait, tone, yes, audio, fit, bestVoice,
    get reduce() { return reduce; }, get sound() { return sound; }, get last() { return last; },
    onMotion: f => motionFns.push(f), onSound: f => soundFns.push(f),
  };
})();
