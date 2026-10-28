// Curio Class family engine: music-studio (compose, arrange and hear music in the browser). Docs: docs/families/music-studio.md
// Inlined by scripts/bundle_tool.py from a kit:music-studio script tag, after kit:curio. Exposes MS.
// (Never write a closing script tag in this file, even in a comment: the inlined copy would end there.)
// Four tools share it: melody-maker (3-5), song-form-builder (3-5), chord-explorer (6-8), beat-lab (9-12).
// Written 2026-10-28 by song-form-builder, the first tool on it. The sound parts (ctx, INSTR, pluck, blow, freq, KEYS,
// SCALES, COL) are lifted unchanged in sound from melody-maker's src.html; MS.play is new: a lookahead scheduler on
// the audio clock (25 ms timer, 150 ms horizon, the pattern of beat-buddies' startClock).
// Everything sounds through one shared AudioContext, made on first use (after a tap: browsers block sound before it).
// Silent while the kit's Sound button is off (Curio.sound), but the clock and its callbacks still run (on the page
// clock), so a playhead still walks with Sound off.
const MS = (() => {
  // ---------- pitch ----------
  // Syllables carry their colors (the common classroom bell colors), always with the name on them.
  const COL = {do: '#d8392b', re: '#ef7d1a', mi: '#e9b500', fa: '#3c9a3c', sol: '#1f9bb5', la: '#3d5fc4', ti: '#8a4fbf'};
  // rows: [semitones above do, syllable, scale degree (0 = do)]
  const SCALES = {
    major: {name: 'Major', home: 'do', rows: [[0, 'do', 0], [2, 're', 1], [4, 'mi', 2], [5, 'fa', 3], [7, 'sol', 4], [9, 'la', 5], [11, 'ti', 6], [12, 'do', 7]]},
    penta: {name: 'Pentatonic', home: 'do', rows: [[0, 'do', 0], [2, 're', 1], [4, 'mi', 2], [7, 'sol', 4], [9, 'la', 5], [12, 'do', 7]]},
    minor: {name: 'Minor (la is home)', home: 'la', rows: [[-3, 'la', -2], [-1, 'ti', -1], [0, 'do', 0], [2, 're', 1], [4, 'mi', 2], [5, 'fa', 3], [7, 'sol', 4], [9, 'la', 5]]},
  };
  // key: do's pitch (semitones above middle C), letter of do (C = 0 ... B = 6), and the key signature
  const KEYS = {
    C: {semi: 0, letter: 0, sig: [], name: 'C'},
    D: {semi: 2, letter: 1, sig: ['F♯', 'C♯'], name: 'D'},
    F: {semi: 5, letter: 3, sig: ['B♭'], name: 'F'},
    G: {semi: 7, letter: 4, sig: ['F♯'], name: 'G'},
  };
  // frequency of a note `semi` semitones above do in `key` (do of C = middle C, 261.63 Hz)
  const freq = (key, semi) => 261.63 * Math.pow(2, ((KEYS[key] ? KEYS[key].semi : 0) + semi) / 12);
  // a scale row as semitones above do, and its syllable
  const rowSemi = (scale, row) => SCALES[scale].rows[row][0];
  const rowSyl = (scale, row) => SCALES[scale].rows[row][1];

  // note names to semitones above middle C: 'C' 0, 'E' 4, 'G3' -5, 'C5' 12, 'F#4' 6, 'Bb' 10 (octave 4 when left out)
  const LETTER = {C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11};
  function semi(name) {
    const m = /^([A-Ga-g])([#♯b♭]?)(-?\d)?$/.exec(String(name).trim());
    if (!m) throw new Error('MS.semi: not a note name: ' + name);
    const acc = m[2] === '#' || m[2] === '♯' ? 1 : m[2] === 'b' || m[2] === '♭' ? -1 : 0;
    return LETTER[m[1].toUpperCase()] + acc + 12 * ((m[3] === undefined ? 4 : +m[3]) - 4);
  }
  // durations in beats (a quarter note = 1 beat)
  const LEN = {s: .25, e: .5, de: .75, q: 1, dq: 1.5, h: 2, dh: 3, w: 4};
  // a melody written as text to events: "E D C:h | C:e C:e - D". A token is a note name or '-' (a rest), then
  // optionally ':' and a length (a LEN key or a number of beats; default 1). '|' (bar lines) are ignored.
  // opts.scale multiplies every length (for example 0.5 to write a 6/8 tune with eighth = 1).
  // Returns {events: [{beat, semi, dur}], beats} (rests leave a gap, no event).
  function parse(text, opts = {}) {
    const k = opts.scale || 1, events = [];
    let beat = 0;
    for (const tok of String(text).split(/\s+/)) {
      if (!tok || tok === '|') continue;
      const [n, l] = tok.split(':'), dur = (l === undefined ? 1 : l in LEN ? LEN[l] : +l) * k;
      if (!(dur > 0)) throw new Error('MS.parse: bad length in ' + tok);
      if (n !== '-') events.push({beat, semi: semi(n), dur});
      beat += dur;
    }
    return {events, beats: beat};
  }
  // scale-row numbers (null or '-' for a rest) to events, one row per beat: rows(notes, {scale, start, instr})
  // The list also carries .beats (start + notes.length), so MS.play gives trailing rests and an all-rest grid their time.
  function rows(notes, opts = {}) {
    const scale = opts.scale || 'penta', start = opts.start || 0, out = [];
    notes.forEach((r, i) => { if (r !== null && r !== undefined && r !== '-') out.push({beat: start + i, semi: rowSemi(scale, r), dur: 1, instr: opts.instr}); });
    out.beats = start + notes.length;
    return out;
  }

  // ---------- sound ----------
  let ac = null, master, room;
  const enabled = () => typeof Curio === 'undefined' || Curio.sound;
  // the shared context: master gain .8 to the speakers, plus the short room delay (130 ms, feedback .28, wet .22)
  function ctx() {
    if (!ac) {
      try { ac = new (window.AudioContext || window.webkitAudioContext)(); } catch { return null; }
      master = ac.createGain(); master.gain.value = .8; master.connect(ac.destination);
      const d = ac.createDelay(), fb = ac.createGain(), wet = ac.createGain(), lp = ac.createBiquadFilter();
      d.delayTime.value = .13; fb.gain.value = .28; wet.gain.value = .22; lp.type = 'lowpass'; lp.frequency.value = 2400;
      room = ac.createGain(); room.connect(d); d.connect(lp).connect(fb).connect(d); lp.connect(wet).connect(ac.destination);
    }
    if (ac.state === 'suspended') ac.resume();
    return ac;
  }
  // bus: where a voice goes, {m, r} (dry and room sends). Default the shared master and room; MS.play makes its own,
  // so Stop can silence notes already scheduled.
  const bus0 = () => ({m: master, r: room});
  // pluck, blow and tick make the context themselves and are silent with Sound off, like note and chime
  const ready = () => enabled() && !!ctx();
  const INSTR = {
    marimba: {name: '🪵 Marimba', play: (f, t, d, b) => pluck(f, t, Math.min(1.1, .5 + d), {gain: .32, partials: [[1, 1], [4, .18], [10, .04]]}, b)},
    flute: {name: '🪈 Flute', play: (f, t, d, b) => blow(f, t, d, b)},
    piano: {name: '🎹 Piano', play: (f, t, d, b) => pluck(f, t, 1.4, {gain: .22, partials: [[1, 1], [2, .45], [3, .2], [4, .1], [5, .05]], type: 'triangle', cutoff: f * 9}, b)},
    box: {name: '🎁 Music box', play: (f, t, d, b) => pluck(f * 2, t, 1.6, {gain: .16, partials: [[1, 1], [2.76, .25], [5.4, .08]]}, b)},
  };
  function pluck(f, t, decay, {gain = .2, partials = [[1, 1]], type = 'sine', cutoff = 0} = {}, b) {
    if (!ready()) return;
    b = b || bus0();
    const g = ac.createGain();
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(gain, t + .006); g.gain.exponentialRampToValueAtTime(.0001, t + decay);
    let out = g;
    if (cutoff) { const lp = ac.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.setValueAtTime(cutoff, t); lp.frequency.exponentialRampToValueAtTime(cutoff * .3, t + decay); g.connect(lp); out = lp; }
    out.connect(b.m); out.connect(b.r);
    for (const [r, l] of partials) {
      const o = ac.createOscillator(), pg = ac.createGain();
      o.type = type; o.frequency.setValueAtTime(f * r, t); pg.gain.value = l;
      o.connect(pg).connect(g); o.start(t); o.stop(t + decay + .05);
    }
  }
  function blow(f, t, d, b) {
    if (!ready()) return;
    b = b || bus0();
    const o = ac.createOscillator(), o2 = ac.createOscillator(), g = ac.createGain(), v = ac.createOscillator(), vg = ac.createGain();
    o.type = 'sine'; o.frequency.value = f; o2.type = 'triangle'; o2.frequency.value = f * 2;
    v.frequency.value = 5; vg.gain.value = f * .006; v.connect(vg).connect(o.frequency);
    const g2 = ac.createGain(); g2.gain.value = .12; o2.connect(g2).connect(g); o.connect(g);
    const len = Math.max(.25, d * .92);
    g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.24, t + .06); g.gain.setValueAtTime(.22, t + len - .06); g.gain.exponentialRampToValueAtTime(.0001, t + len + .12);
    g.connect(b.m); g.connect(b.r);
    [o, o2, v].forEach(x => { x.start(t); x.stop(t + len + .15); });
  }
  // one note now (or `at` seconds from now): note('marimba', 'C', 4, 0, .4). dur in seconds.
  function note(instr, key, s, at = 0, dur = .4) {
    if (!enabled()) return;
    const c = ctx(); if (!c) return;
    (INSTR[instr] || INSTR.marimba).play(freq(key, s), c.currentTime + at + .02, dur);
  }
  // the lead-in tick: a short wood click
  function tick(t, b, accent = false) {
    pluck(accent ? 1760 : 1320, t, .08, {gain: .14, partials: [[1, 1], [2.3, .3]]}, b);
  }
  // the melody-maker chime: a rising arpeggio for good, two falling notes for not yet
  function chime(good) {
    if (!enabled()) return;
    const c = ctx(); if (!c) return;
    (good ? [0, 4, 7, 12] : [5, 4]).forEach((s, i) => pluck(523.25 * Math.pow(2, s / 12), c.currentTime + i * .09, .6, {gain: .12, partials: [[1, 1], [2.76, .2]]}));
  }

  // ---------- the clock ----------
  // play(events, {bpm, lead, key, instr, beats, exclusive, onStep, onEnd}) -> player
  //   events: [{beat, semi, dur, instr}] (beat and dur in beats; beat may be fractional; instr defaults to opts.instr,
  //     then marimba), or the {events, beats} that MS.parse returns
  //   bpm: beats a minute (default 100); player.bpm = n changes it from now on, without a jump in the playhead
  //   lead: lead-in ticks before beat 0 (default 0)
  //   key: KEYS key for freq (default 'C'); semi is above do of the key
  //   beats: the length. Default: events.beats when the list has one (MS.rows and MS.parse give it), else the end of
  //     the last event. Pass it for a fixed-length grid, so trailing rests and an all-rest grid take their time
  //   exclusive: true (default) stops every other running player first; false plays alongside them
  //   onStep(i, info): once per whole beat, in step with the sound (i < 0 during the lead-in); info {beat, events}
  //     lists the events starting in that beat
  //   onEnd(why): 'end' after the last beat, or 'stop'
  // player: {stop(), done (a promise of 'end' or 'stop'), playing, bpm, beat (the current beat, fractional)}
  // Notes go through the player's own bus, so stop() also silences notes already scheduled.
  // The clock: the audio clock when Sound is on and the context is running at the start; otherwise the page clock,
  // silent for that whole play (so a suspended context never stalls a playhead).
  const live = new Set();
  function play(input, opts = {}) {
    const events = Array.isArray(input) ? input : (input && input.events) || [];
    if (opts.exclusive !== false) stop();
    const c0 = enabled() ? ctx() : null, c = c0 && c0.state === 'running' ? c0 : null;
    const now = () => c ? c.currentTime : performance.now() / 1000;
    const evs = events.slice().sort((a, b) => a.beat - b.beat);
    const last = evs.reduce((m, e) => Math.max(m, e.beat + (e.dur || 1)), 0);
    const given = opts.beats != null ? opts.beats : input && input.beats != null ? input.beats : null;
    const total = given != null ? given : last;
    const steps = Math.ceil(total - 1e-9), lead = opts.lead || 0, key = opts.key || 'C';
    let bpm = opts.bpm || 100, aB = -lead, aT = now() + .08;           // anchor: beat aB sounds at time aT
    const at = b => aT + (b - aB) * 60 / bpm;
    let next = -lead, ei = 0, timer = 0, on = true, finish;
    const outs = [];
    let b = null;
    if (c) {
      const m = c.createGain(), r = c.createGain(); m.connect(master); r.connect(room); b = {m, r};
    }
    const later = (t, f) => { const id = setTimeout(() => { outs.splice(outs.indexOf(id), 1); if (on) f(); }, Math.max(0, (t - now()) * 1000)); outs.push(id); };
    const done = new Promise(r => { finish = r; });
    function end(why) {
      if (!on) return;
      on = false; clearTimeout(timer); outs.splice(0).forEach(clearTimeout);
      if (b && why === 'stop') { const t = c.currentTime; for (const g of [b.m, b.r]) { g.gain.setValueAtTime(g.gain.value, t); g.gain.linearRampToValueAtTime(0, t + .05); } }
      if (b) setTimeout(() => { b.m.disconnect(); b.r.disconnect(); }, 4000);   // let the last notes ring out first
      live.delete(player);
      if (opts.onEnd) opts.onEnd(why);
      finish(why);
    }
    function pump() {
      if (!on) return;
      const horizon = now() + .15;
      while (next < steps && at(next) < horizon) {
        const i = next, t = at(i);
        if (i < 0 && b && enabled()) tick(t, b, i === -lead);
        const inBeat = evs.filter(e => e.beat >= i && e.beat < i + 1);
        if (opts.onStep) later(t, () => opts.onStep(i, {beat: i, events: inBeat}));
        next++;
      }
      while (ei < evs.length && at(evs[ei].beat) < horizon) {
        const e = evs[ei++];
        if (b && enabled() && e.beat < total) (INSTR[e.instr || opts.instr] || INSTR.marimba).play(freq(key, e.semi), at(e.beat), (e.dur || 1) * 60 / bpm, b);
      }
      if (next >= steps && ei >= evs.length) { later(at(total), () => end('end')); return; }
      timer = setTimeout(pump, 25);
    }
    const player = {
      stop: () => end('stop'), done,
      get playing() { return on; },
      get bpm() { return bpm; },
      set bpm(v) { const t = now(), cb = aB + (t - aT) * bpm / 60; aB = cb; aT = t; bpm = v; },
      get beat() { return aB + (now() - aT) * bpm / 60; },
    };
    live.add(player);
    pump();
    return player;
  }
  // stop every running player
  function stop() { for (const p of [...live]) p.stop(); }

  return {
    COL, SCALES, KEYS, LEN, INSTR, freq, rowSemi, rowSyl, semi, parse, rows,
    ctx, pluck, blow, note, tick, chime, play, stop,
    get playing() { return live.size > 0; }, version: '1.1',
  };
})();
