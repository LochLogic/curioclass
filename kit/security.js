// Curio Class family engine: security. Made-up organizations, the things people read in them (emails, texts,
// sign-in pages, logs, files, call transcripts, notes), spots to tap, password and cipher checks, locks and clocks.
// Inlined by scripts/bundle_tool.py from a kit:security script tag, after kit:curio. Spec and API:
// docs/families/security.md. New features go here and into that doc in the same change.
//
// Every security tool teaches defense with made-up systems inside the page only: every web address and email domain
// must be a reserved name (example.com, example.org, example.net, or ending .example, .test, .invalid; RFC 2606 and
// RFC 6761). The renderers check every address they draw and log a console error for any other, so no real site or
// brand can slip into a lesson. Links never navigate.
const Sec = (() => {

  // =====================================================================================================
  // PURE: no DOM in this block (checks, locks, clock). Exposed as Sec.pure, and spread onto Sec itself.
  // =====================================================================================================
  const pure = (() => {
    const RESERVED = ['example.com', 'example.org', 'example.net'], ENDS = ['.example', '.test', '.invalid'];
    // the host part of a web address or an email address ("Name <a@b.example>", "https://x.test/p?q", "a@b.test")
    function hostOf(u) {
      let s = String(u == null ? '' : u).trim().toLowerCase();
      const ang = s.match(/<([^>]+)>/); if (ang) s = ang[1];
      s = s.replace(/^[a-z][a-z0-9+.-]*:\/\//, '').replace(/^mailto:/, '');
      s = s.split(/[/?#\s]/)[0];
      if (s.includes('@')) s = s.slice(s.lastIndexOf('@') + 1);
      s = s.replace(/:\d+$/, '').replace(/\.$/, '');
      return s;
    }
    // real top-level domains: a name like "brand.com.example" hides a real site's name in front of a reserved suffix
    const REAL_TLDS = ['com', 'org', 'net', 'edu', 'gov', 'mil', 'int', 'io', 'co', 'uk', 'us', 'ca', 'au', 'de', 'fr', 'jp',
      'info', 'biz', 'app', 'dev', 'ai', 'me', 'tv', 'gg', 'ly', 'xyz', 'online', 'site', 'shop'];
    // true only for reserved names: example.com/.org/.net (and their subdomains) or a name ending .example/.test/.invalid,
    // and never a real-looking name parked in front of one ("brand.com.example" or "brand.com.example.com" is false)
    function safeDomain(u) {
      const h = hostOf(u);
      if (!h || !/^[a-z0-9.-]+$/.test(h) || h.includes('..')) return false;
      const end = RESERVED.find(d => h === d || h.endsWith('.' + d)) || ENDS.find(t => h.endsWith(t) && h.length > t.length);
      if (!end) return false;
      const rest = h === end ? [] : h.slice(0, h.length - end.length).replace(/^\.|\.$/g, '').split('.').filter(Boolean);
      return !(rest.length >= 2 && REAL_TLDS.includes(rest[rest.length - 1]));
    }

    // a short sample: 20 very common passwords, all on the UK NCSC list of the 100,000 most-used breached passwords (2019)
    const COMMON = ['123456', '123456789', 'qwerty', 'password', '1111111', '12345678', 'abc123', 'password1', 'iloveyou',
      'sunshine', 'princess', 'football', 'monkey', 'letmein', 'dragon', 'baseball', 'welcome', '123123', 'qwerty123', '000000'];
    const POOLS = {lower: 26, upper: 26, digit: 10, symbol: 33};   // symbol: the 32 printable ASCII symbols and space
    const WORD_LIST = 7776;                                         // a dice word list (EFF): log2(7776) = 12.92 bits per word
    // pattern(pw): how a guesser who tries patterns first would build pw, or null when pw shows no pattern.
    //   Guessers try words before random strings, and the usual dressing first: a capital, digits or a year at the
    //   end, a symbol at the end, a separator between words, letter swaps (4 for a, 0 for o) and keyboard and alphabet
    //   runs (qwerty, 12345, abcd; a stretch of runs back to back counts as each run). Parts: word (log2 7776 = 12.9 bits; a capital or all capitals adds 1), run (10), year
    //   (1900 to 2099: log2 200 = 7.6), digits (3.3 each), symbols (log2 33 = 5.0 each), separator (one kind of
    //   space - _ . between words: log2 5 = 2.3, once), letters (a 1 or 2 letter scrap: 5.7 each), plus 1 bit per
    //   swap. A word used again costs log2(the words so far) + 1. Letter runs split where a capital follows a small letter and before a Title-case word after a
    //   capital run (ILove = I + Love, NYKnicks = NY + Knicks), except that a capital run of 3+ with a vowel keeps
    //   its letters (LOLpassword = LOL + password). A letter run counts as a word when it has a vowel and no five
    //   consonants in a row; 10 or more letters in one run count as one word per 6 letters; a capital run of up to
    //   4 that is not word-like counts as letters. One character typed 3 or more times in a row is a repeat
    //   (log2 52 or log2 10, plus log2 of the count, plus 1). A whole password that is one unit typed 2 or more
    //   times (Ab1!Ab1!Ab1!, zzzz...) is rated as the unit (its pattern, or its characters at random) plus
    //   log2(times) + 1. There is no dictionary, so this is a model: it can still over-rate a pattern it doesn't
    //   know (a name, a phrase with odd capitals) and under-rate a random run that looks like a word. Applies only
    //   with a sign of a pattern (two or more words, a capital, a digit, a symbol, a swap, a run, a repeat, or one
    //   10+ letter run) and at least one word, run or repeat.
    //   Returns {parts: [{kind, text, bits, times?}], bits, words, caps, swaps}; kinds word, run, year, digits,
    //   symbols, separator, letters, repeat (text is the character, times the count), chars (a random unit) and
    //   times (a whole-password repeat: times is the count).
    const SWAPS = {'0': 'o', '1': 'i', '3': 'e', '4': 'a', '5': 's', '7': 't', '8': 'b', '@': 'a', '$': 's'};
    const RUNS = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', '1234567890', 'abcdefghijklmnopqrstuvwxyz'];
    const isRun = s => s.length >= 4 && RUNS.some(r => r.includes(s) || [...r].reverse().join('').includes(s));
    // a stretch made only of runs back to back (qwertyuiop + asdfghjkl, 1234567890 + 987654321), or null
    function runSplit(s) {
      const out = [];
      for (let i = 0; i < s.length;) {
        let n = s.length - i;
        while (n >= 4 && !isRun(s.slice(i, i + n))) n--;
        if (n < 4) return null;
        out.push(s.slice(i, i + n)); i += n;
      }
      return out.length > 1 ? out : null;
    }
    // letters split for pattern(): at small-to-capital, and before a Title-case word that follows a capital run
    function splitLetters(run) {
      const out = [];
      for (const seg of run.split(/(?<=[a-z])(?=[A-Z])/)) {
        const m = seg.match(/^([A-Z]{2,})([a-z][a-z]*)$/);
        if (!m) { out.push(seg); continue; }
        if (m[1].length >= 3 && /[AEIOU]/.test(m[1])) out.push(m[1], m[2]);
        else out.push(m[1].slice(0, -1), m[1].slice(-1) + m[2]);
      }
      return out;
    }
    const charBits = s => {
      const c = [...s], pool = Object.keys(POOLS).reduce((t, k) => t + ({lower: /[a-z]/, upper: /[A-Z]/, digit: /[0-9]/, symbol: /[^a-zA-Z0-9]/}[k].test(s) ? POOLS[k] : 0), 0);
      return c.length * Math.log2(pool || 1);
    };
    function pattern(pw) {
      pw = String(pw == null ? '' : pw);
      const ch = [...pw];
      if (ch.length < 3) return null;
      // one unit typed again and again: rate the unit, plus a small cost for the count
      for (let n = 1; n <= ch.length / 2; n++) {
        if (ch.length % n) continue;
        const unit = ch.slice(0, n).join(''), times = ch.length / n;
        if (unit.repeat(times) !== pw) continue;
        const pu = pattern(unit), ub = pu ? pu.bits : charBits(unit);
        const parts = (pu ? pu.parts : [{kind: 'chars', text: unit, bits: ub}]).concat({kind: 'times', text: unit, times, bits: Math.log2(times) + 1});
        return {parts, bits: ub + Math.log2(times) + 1, words: pu ? pu.words : 0, caps: pu ? pu.caps : 0, swaps: pu ? pu.swaps : 0};
      }
      // one unit typed again and again with a separator (dog dog dog, pass-pass-pass): the unit, the separator, the count
      for (const sep of [' ', '-', '_', '.']) {
        const us = pw.split(sep), unit = us[0], times = us.length;
        if (times < 2 || !unit || us.some(x => x !== unit)) continue;
        const pu = pattern(unit), isWord = !pu && /^[a-z]{3,}$/.test(unit);
        const ub = pu ? pu.bits : isWord ? Math.log2(WORD_LIST) : charBits(unit);
        const parts = (pu ? pu.parts : [{kind: isWord ? 'word' : 'chars', text: unit, bits: ub}]).concat(
          {kind: 'separator', text: sep, bits: Math.log2(5)}, {kind: 'times', text: unit, times, bits: Math.log2(times) + 1});
        return {parts, bits: ub + Math.log2(5) + Math.log2(times) + 1, words: pu ? pu.words : isWord ? 1 : 0, caps: pu ? pu.caps : 0, swaps: pu ? pu.swaps : 0};
      }
      const L = c => /[a-zA-Z]/.test(c || '');
      // undo swaps that sit between two letters (Gr4v1ty, m0nkeyB@rs; not the 0 in 2026)
      let swaps = 0;
      const u = ch.map((c, i) => SWAPS[c] && L(ch[i - 1]) && L(ch[i + 1]) ? (swaps++, SWAPS[c]) : c);
      // tokens: letter runs (split where a capital follows a small letter), digit runs, other runs
      const toks = [];
      for (const m of u.join('').matchAll(/[a-zA-Z]+|[0-9]+|[^a-zA-Z0-9]+/g)) {
        if (/^[a-zA-Z]/.test(m[0])) for (const w of splitLetters(m[0])) toks.push({t: 'L', s: w});
        else toks.push({t: /^[0-9]/.test(m[0]) ? 'D' : 'S', s: m[0]});
      }
      const SEP = /^[ \-_.]$/, parts = [], seen = [];
      let words = 0, caps = 0, sepKind = null, sepBad = false, signal = swaps > 0 || /[A-Z]/.test(pw), anchor = false;
      toks.forEach((k, i) => {
        if (k.t !== 'S' && k.s.length >= 3 && /^(.)\1+$/.test(k.s)) {
          parts.push({kind: 'repeat', text: k.s[0], times: k.s.length, bits: Math.log2(k.t === 'L' ? 52 : 10) + Math.log2(k.s.length) + 1});
          anchor = signal = true; return;
        }
        if (k.t === 'L') {
          const low = k.s.toLowerCase();
          if (isRun(low)) { parts.push({kind: 'run', text: k.s, bits: 10}); anchor = signal = true; return; }
          const rl = runSplit(low);
          if (rl) { rl.forEach(r => parts.push({kind: 'run', text: r, bits: 10})); anchor = signal = true; return; }
          const cased = k.s === low || k.s === k.s[0].toUpperCase() + low.slice(1) || k.s === k.s.toUpperCase();
          if (k.s.length >= 3 && cased && /[aeiouy]/.test(low) && !/[^aeiouy]{5}/.test(low)) {
            const n = k.s.length >= 10 ? Math.round(k.s.length / 6) : 1, cap = k.s !== low ? 1 : 0;
            if (n > 1) signal = true;
            if (seen.includes(low)) {   // a word used again: pick one of the words so far, + 1
              parts.push({kind: 'word', text: k.s, again: true, bits: Math.log2(seen.length) + 1 + cap});
              caps += cap; anchor = signal = true; return;
            }
            seen.push(low); words += n; caps += cap; anchor = true;
            parts.push({kind: 'word', text: k.s, bits: n * Math.log2(WORD_LIST) + cap});
          } else if (k.s.length <= 2 || (k.s.length <= 4 && k.s === k.s.toUpperCase())) parts.push({kind: 'letters', text: k.s, bits: k.s.length * Math.log2(52)});
          else { parts.push(null); }   // a letter run that is not word-like: no pattern
        } else if (k.t === 'D') {
          signal = true;
          const rd = isRun(k.s) ? [k.s] : runSplit(k.s);
          if (rd) { rd.forEach(r => parts.push({kind: 'run', text: r, bits: 10})); anchor = true; }
          else if (/^(19|20)\d\d$/.test(k.s)) parts.push({kind: 'year', text: k.s, bits: Math.log2(200)});
          else parts.push({kind: 'digits', text: k.s, bits: k.s.length * Math.log2(10)});
        } else {
          signal = true;
          const between = toks[i - 1] && toks[i + 1] && toks[i - 1].t !== 'S' && toks[i + 1].t !== 'S';
          if (between && SEP.test(k.s) && (sepKind == null || sepKind === k.s)) {
            parts.push({kind: 'separator', text: k.s, bits: sepKind == null ? Math.log2(5) : 0}); sepKind = k.s;
          } else { sepBad = sepBad || between; parts.push({kind: 'symbols', text: k.s, bits: [...k.s].length * Math.log2(POOLS.symbol)}); }
        }
      });
      if (parts.includes(null) || !anchor) return null;
      if (words >= 2) signal = true;
      if (!signal) return null;
      const bits = parts.reduce((s, p) => s + p.bits, 0) + swaps;
      return {parts, bits, words, caps, swaps};
    }
    // strength(pw, names): {length, pools, poolSize, bits, words, wordBits, pattern, patternBits, used, onList, hasName}
    //   bits = length x log2(pool total), which assumes every character was picked at random; wordBits only when pw
    //   is two or more different lowercase words split by single spaces (words x log2(7776)); otherwise pattern = pattern(pw)
    //   and patternBits its bits; used = the lowest of these; hasName: pw contains one of names (case-insensitive)
    function strength(pw, names = []) {
      pw = String(pw == null ? '' : pw);
      const chars = [...pw], length = chars.length;
      const pools = {lower: /[a-z]/.test(pw), upper: /[A-Z]/.test(pw), digit: /[0-9]/.test(pw), symbol: /[^a-zA-Z0-9]/.test(pw)};
      const poolSize = Object.keys(POOLS).reduce((s, k) => s + (pools[k] ? POOLS[k] : 0), 0);
      const bits = length && poolSize ? length * Math.log2(poolSize) : 0;
      const isWords = /^[a-z]+( [a-z]+)+$/.test(pw) && new Set(pw.split(' ')).size === pw.split(' ').length;
      const words = isWords ? pw.split(' ').length : 0;
      const wordBits = isWords ? words * Math.log2(WORD_LIST) : null;
      const pat = isWords ? null : pattern(pw);
      const patternBits = pat ? pat.bits : null;
      const low = pw.toLowerCase();
      return {length, pools, poolSize, bits, words, wordBits, pattern: pat, patternBits,
        used: Math.min(bits, wordBits == null ? Infinity : wordBits, patternBits == null ? Infinity : patternBits),
        onList: COMMON.includes(low), hasName: names.some(n => n && low.includes(String(n).toLowerCase()))};
    }
    // band(r, names) for grades 3 to 5: Weak if on the list, has a name, or under 8 characters; OK for 8 to 14; Strong
    // for 15+. r is a strength() result, or a password string checked against names (so band('Cedar2026', ['cedar'])
    // is Weak; without names a string is checked against none)
    function band(r, names = []) {
      if (typeof r === 'string') r = strength(r, names);
      if (r.onList || r.hasName || r.length < 8) return 'Weak';
      return r.length >= 15 ? 'Strong' : 'OK';
    }
    // the reasons behind a band, in plain words (the tool may write its own)
    function reasons(r, names = []) {
      if (typeof r === 'string') r = strength(r, names);
      const out = [];
      if (r.length < 8) out.push('too short');
      if (r.hasName) out.push("uses the school's name");
      if (r.onList) out.push('on the common passwords list');
      if (!out.length) out.push(r.length + ' characters');
      return out;
    }
    // seconds to try every possibility at a guess rate (default 10 billion a second): 2^bits / rate
    const guessSeconds = (bits, rate = 1e10) => Math.pow(2, bits) / rate;
    // a toy checksum: the sum of the numbers
    const seal = nums => nums.reduce((s, n) => s + Number(n), 0);

    // ciphers: letters only, case kept, everything else unchanged
    const shift = (c, k) => {
      const A = c >= 'a' && c <= 'z' ? 97 : c >= 'A' && c <= 'Z' ? 65 : 0;
      return A ? String.fromCharCode(A + ((c.charCodeAt(0) - A + k) % 26 + 26) % 26) : c;
    };
    const caesar = (text, k) => [...String(text)].map(c => shift(c, Math.round(k) || 0)).join('');
    // dir: 1 or 'enc' encodes, -1 or 'dec' decodes; the key moves on only at letters
    function vigenere(text, key, dir = 1) {
      const ks = String(key).toLowerCase().replace(/[^a-z]/g, '');
      if (!ks) return String(text);
      const d = dir === -1 || dir === 'dec' || dir === 'decode' ? -1 : 1;
      let i = 0;
      return [...String(text)].map(c => /[a-z]/i.test(c) ? shift(c, d * (ks.charCodeAt(i++ % ks.length) - 97)) : c).join('');
    }
    // Base64, UTF-8 safe. dir 1/'enc' encodes, -1/'dec' decodes; a decode that is not Base64 returns null
    function b64(text, dir = 1) {
      const d = dir === -1 || dir === 'dec' || dir === 'decode' ? -1 : 1;
      try {
        if (d === 1) { let s = ''; for (const b of new TextEncoder().encode(String(text))) s += String.fromCharCode(b); return btoa(s); }
        const bin = atob(String(text).replace(/\s+/g, ''));
        return new TextDecoder('utf-8', {fatal: true}).decode(Uint8Array.from(bin, c => c.charCodeAt(0)));
      } catch { return null; }
    }

    // a lock: lock({check, normalize}). normalize trims and lowercases strings by default (other answers pass through).
    // l.try(answer) -> {open, misses}; l.open, l.misses, l.reset(), l.force() (opens it, for tests and replays)
    function lock({check, normalize} = {}) {
      const norm = normalize || (v => typeof v === 'string' ? v.trim().toLowerCase() : v);
      const l = {open: false, misses: 0,
        try(answer) {
          if (l.open) return {open: true, misses: l.misses};
          const r = check(norm(answer));
          const ok = r === true || !!(r && r.open);
          if (ok) l.open = true; else l.misses++;
          return {...(r && typeof r === 'object' ? r : {}), open: ok, misses: l.misses};
        },
        reset() { l.open = false; l.misses = 0; },
        force() { l.open = true; },
      };
      return l;
    }

    // a clock: clock({mode: 'down' | 'up', ms, onEnd, onTick, tick}). Counting down ends at 0 and calls onEnd once.
    // c.start(), c.pause(), c.reset(ms), c.left, c.elapsed, c.running, c.ended. Timing is real time (never shortened).
    function clock({mode = 'down', ms = 60000, onEnd, onTick, tick = 250} = {}) {
      let total = ms, base = 0, t0 = 0, running = false, ended = false, timer = null;
      const now = () => performance.now();
      const elapsed = () => Math.min(mode === 'down' ? total : Infinity, base + (running ? now() - t0 : 0));
      function step() {
        if (onTick) onTick(c);
        if (mode === 'down' && elapsed() >= total && !ended) { ended = true; c.pause(); base = total; if (onTick) onTick(c); if (onEnd) onEnd(c); }
      }
      const c = {
        start() { if (running || ended) return c; running = true; t0 = now(); timer = setInterval(step, tick); step(); return c; },
        pause() { if (!running) return c; base = elapsed(); running = false; clearInterval(timer); timer = null; return c; },
        reset(m) { c.pause(); if (m != null) total = m; base = 0; ended = false; if (onTick) onTick(c); return c; },
        get elapsed() { return elapsed(); },
        get left() { return mode === 'down' ? Math.max(0, total - elapsed()) : Infinity; },
        get total() { return total; },
        get running() { return running; },
        get ended() { return ended; },
      };
      return c;
    }
    // 1234567 ms -> "20:34" (minutes and seconds, rounded up while counting down)
    const mmss = (ms, up) => { const s = Math.max(0, up ? Math.floor(ms / 1000) : Math.ceil(ms / 1000)); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); };

    return {hostOf, safeDomain, COMMON, POOLS, strength, pattern, band, reasons, guessSeconds, seal, caesar, vigenere, b64, lock, clock, mmss};
  })();
  // ========================================== END PURE ==========================================

  // ---------- the guard: every address a renderer draws, and every domain a world lists ----------
  const flagged = new Set();
  function guard(u, where) {
    if (u == null || u === '') return true;
    if (pure.safeDomain(u)) return true;
    const k = String(u);
    if (!flagged.has(k)) { flagged.add(k); console.error(`Sec: "${k}"${where ? ' (' + where + ')' : ''} is not a reserved domain. Use example.com/.org/.net or a name ending .example, .test or .invalid.`); }
    return false;
  }
  // a made-up organization: {name, people: [{id, name, role}], accounts, files, domains}. Checks every domain and
  // every email-looking or web-looking string in accounts, people and files. Returns {org, person(id), ok}.
  function world(org = {}) {
    let ok = true;
    for (const d of org.domains || []) ok = guard(d, org.name + ' domains') && ok;
    const look = v => {
      if (typeof v === 'string') { if (/@[a-z0-9-]+\.[a-z]/i.test(v) || /^[a-z]+:\/\//i.test(v)) ok = guard(v, org.name) && ok; }
      else if (v && typeof v === 'object') Object.values(v).forEach(look);
    };
    look(org.accounts); look(org.people); look(org.files);
    const people = new Map((org.people || []).map(p => [p.id, p]));
    return {org, ok, person: id => people.get(id) || null};
  }

  // ---------- the look: one stylesheet, colors from --sec-* variables a tool may set ----------
  let styled = false;
  function style() {
    if (styled) return; styled = true;
    const s = document.createElement('style');
    s.textContent = `
.sec-card{--c-bg:var(--sec-card,#fbfbf8);--c-ink:var(--sec-ink,#1c1f26);--c-muted:var(--sec-muted,#555c6b);--c-line:var(--sec-line,#d9dce3);
  --c-link:var(--sec-link,#1a56c4);--c-status:var(--sec-status,#e9ebef);--c-glow:var(--sec-glow,#ffd23f);--c-ok:var(--sec-ok,#1f7a46);--c-bad:var(--sec-bad,#b42318);
  --c-mono:var(--sec-mono,ui-monospace,'Cascadia Mono',Consolas,monospace);
  position:relative;background:var(--c-bg);color:var(--c-ink);border:1px solid var(--c-line);border-radius:12px;overflow:hidden;
  font:15px/1.45 'Segoe UI',system-ui,sans-serif;text-align:left;min-width:0}
.sec-card.sec-dark{--c-bg:var(--sec-term,#0a0f14);--c-ink:var(--sec-term-ink,#d6e2ee);--c-muted:var(--sec-term-muted,#a6b3c4);--c-line:var(--sec-term-line,#253140);
  --c-status:var(--sec-term-status,#16202b);--c-link:var(--sec-term-link,#8cc4ff);--c-ok:var(--sec-term-ok,#6fdca6);--c-bad:var(--sec-term-bad,#ff9c8f)}
.sec-body{padding:10px 12px}
.sec-scroll{overflow:auto}
.sec-scroll.sec-more{-webkit-mask-image:linear-gradient(to right,#000 calc(100% - 36px),rgba(0,0,0,.25));mask-image:linear-gradient(to right,#000 calc(100% - 36px),rgba(0,0,0,.25))}
.sec-detailbox{position:sticky;left:8px;box-sizing:border-box;white-space:normal;overflow-wrap:anywhere}
.sec-title{font-weight:700;font-size:15px;padding:8px 12px;border-bottom:1px solid var(--c-line);display:flex;gap:8px;align-items:center}
.sec-title small{font-weight:400;color:var(--c-muted)}
.sec-muted{color:var(--c-muted)}
.sec-mono{font-family:var(--c-mono)}
.sec-spot{cursor:pointer;border-radius:6px;outline:2px solid transparent;outline-offset:1px;transition:outline-color .2s,background .2s}
.sec-spot:hover{background:color-mix(in srgb,var(--c-glow) 18%,transparent)}
.sec-spot.sec-marked{outline:3px solid var(--c-glow);background:color-mix(in srgb,var(--c-glow) 22%,transparent)}
.sec-spot.sec-right{outline:3px solid var(--c-ok)}
.sec-spot.sec-wrong{outline:3px dashed var(--c-bad)}
.sec-spot:focus-visible,.sec-spot.sec-marked:focus-visible,.sec-spot.sec-right:focus-visible,.sec-spot.sec-wrong:focus-visible{outline:3px solid var(--focus,#1d4ed8);outline-offset:2px;box-shadow:0 0 0 2px #fff}
.sec-spot.sec-dim{opacity:.55}
.sec-tag{display:inline-block;margin-left:6px;padding:0 7px;border-radius:999px;font:700 12px/20px 'Segoe UI',system-ui,sans-serif;background:var(--c-glow);color:#1c1f26;vertical-align:middle}
.sec-tag.ok{background:var(--c-ok);color:#fff}
.sec-tag.bad{background:var(--c-bad);color:#fff}
.sec-link{color:var(--c-link);text-decoration:underline;cursor:pointer}
.sec-status{background:var(--c-status);color:var(--c-muted);font:13px/1.3 var(--c-mono);padding:5px 10px;min-height:26px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;border-top:1px solid var(--c-line)}
.sec-status:empty::before{content:'\\00a0'}
.sec-head{display:grid;grid-template-columns:auto 1fr;gap:1px 10px;font-size:14px;padding:10px 12px;border-bottom:1px solid var(--c-line)}
.sec-head dt{color:var(--c-muted)}
.sec-head dd{margin:0;min-width:0;overflow-wrap:anywhere}
.sec-subject{font-weight:700;font-size:17px}
.sec-body p{margin:0 0 8px}
.sec-att{display:inline-flex;gap:6px;align-items:center;border:1px solid var(--c-line);border-radius:8px;padding:4px 10px;margin:2px 6px 2px 0;font-size:14px}
.sec-phone{max-width:340px;margin:0 auto;border:8px solid var(--sec-phone,#2a2f3a);border-radius:26px;background:var(--c-bg)}
.sec-sender{text-align:center;font-weight:700;padding:8px;border-bottom:1px solid var(--c-line)}
.sec-sender small{display:block;font-weight:400;color:var(--c-muted)}
.sec-bubbles{display:flex;flex-direction:column;gap:6px;padding:10px}
.sec-bubble{align-self:flex-start;max-width:88%;background:var(--sec-bubble,#e9ebef);border-radius:16px 16px 16px 4px;padding:7px 11px}
.sec-bubble.me{align-self:flex-end;background:var(--sec-bubble-me,#d6e6ff);border-radius:16px 16px 4px 16px}
.sec-chrome{display:flex;gap:8px;align-items:center;background:var(--c-status);padding:6px 10px;border-bottom:1px solid var(--c-line)}
.sec-dots{display:flex;gap:4px}.sec-dots i{width:9px;height:9px;border-radius:50%;background:var(--c-line);display:block}
.sec-addr{flex:1;display:flex;gap:6px;align-items:center;background:var(--c-bg);border:1px solid var(--c-line);border-radius:999px;padding:3px 10px;font:14px var(--c-mono);min-width:0;overflow:hidden;white-space:nowrap}
.sec-page{padding:16px;display:flex;flex-direction:column;align-items:center;gap:10px}
.sec-logo{display:flex;gap:8px;align-items:center;font-weight:800;font-size:18px}
.sec-field{width:min(100%,280px);display:flex;flex-direction:column;gap:2px;font-size:13px;color:var(--c-muted)}
.sec-input{min-height:44px;border:1px solid var(--c-line);border-radius:8px;padding:8px 10px;color:var(--c-ink);background:var(--c-bg);font:15px var(--c-mono);cursor:not-allowed}
.sec-input:focus-visible{outline:3px solid var(--focus,#1d4ed8)}
.sec-fake-btn{width:min(100%,280px);min-height:44px;border-radius:8px;border:0;background:var(--sec-login-btn,#3b4252);color:#fff;font-weight:700;cursor:not-allowed}
.sec-lock-note{font-size:13px;color:var(--c-muted);min-height:18px;text-align:center}
.sec-table{width:100%;border-collapse:collapse;font-size:14px}
.sec-table th,.sec-table td{padding:6px 8px;border-bottom:1px solid var(--c-line);text-align:left;vertical-align:top}
.sec-table th{font-size:12.5px;color:var(--c-muted);font-weight:700;position:sticky;top:0;background:var(--c-bg);z-index:1}
.sec-table th button{all:unset;cursor:pointer;display:inline-flex;gap:4px;align-items:center;min-height:44px;min-width:44px}
.sec-table th button:focus-visible{outline:3px solid var(--focus,#1d4ed8)}
.sec-table td small{display:block;color:var(--c-muted);font-size:12px;white-space:nowrap}
.sec-table td.sec-nowrap{white-space:nowrap}
.sec-table tr.sec-spot{outline:none}
.sec-table tr.sec-spot td{height:44px;box-sizing:border-box}
.sec-table tr.sec-spot td:first-child{border-left:4px solid transparent}
.sec-table tr.sec-spot.sec-marked td{background:color-mix(in srgb,var(--c-glow) 28%,transparent)}
.sec-table tr.sec-spot.sec-marked td:first-child{border-left-color:var(--c-glow)}
.sec-table tr.sec-spot.sec-right td:first-child{border-left-color:var(--c-ok)}
.sec-table tr.sec-spot.sec-wrong td:first-child{border-left-color:var(--c-bad)}
.sec-table tr.sec-spot:focus-visible td{box-shadow:inset 0 3px 0 var(--focus,#1d4ed8),inset 0 -3px 0 var(--focus,#1d4ed8)}
.sec-table tr.sec-hasdetails{cursor:pointer;outline:none}
.sec-table tr.sec-hasdetails td{height:44px;box-sizing:border-box}
.sec-table tr.sec-hasdetails:hover td{background:color-mix(in srgb,var(--c-glow) 12%,transparent)}
.sec-table tr.sec-hasdetails:focus-visible td{box-shadow:inset 0 3px 0 var(--focus,#1d4ed8),inset 0 -3px 0 var(--focus,#1d4ed8)}
.sec-table tr.sec-hasdetails td:first-child::before{content:'▸';display:inline-block;width:1em;color:var(--c-muted)}
.sec-table tr.sec-hasdetails[aria-expanded="true"] td:first-child::before{content:'▾'}
.sec-table tr.sec-details td{background:var(--c-status);font-size:13.5px}
.sec-tools{display:flex;gap:6px;flex-wrap:wrap;align-items:center;padding:6px 10px;border-bottom:1px solid var(--c-line);font-size:13px}
.sec-tools select{min-height:44px;font:inherit}
.sec-fields{display:grid;grid-template-columns:auto 1fr;gap:4px 10px;align-items:baseline}
.sec-fields dt{color:var(--c-muted);font-size:13.5px}
.sec-fields dd{margin:0;font-family:var(--c-mono);font-size:16px}
.sec-seal{display:flex;gap:8px;align-items:center;margin-top:8px;padding-top:8px;border-top:1px dashed var(--c-line);font-weight:700}
.sec-rowbody{display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;padding:6px 10px}
.sec-rowname{font-weight:800;font-size:16px;min-width:2.6em}
.sec-chips{display:flex;gap:4px}
.sec-chip{all:unset;box-sizing:border-box;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;min-width:44px;min-height:44px;padding:1px 4px;border:1px solid var(--c-line);border-radius:8px;background:var(--c-bg);line-height:1.1}
button.sec-chip{cursor:pointer}
.sec-chip small{font-size:11px;color:var(--c-muted)}
.sec-chip b{font:700 17px var(--c-mono)}
.sec-sealchip{border:2px solid var(--sec-seal,#9a3412);background:color-mix(in srgb,var(--sec-seal,#9a3412) 8%,var(--c-bg))}
.sec-sealchip b{display:inline-flex;gap:3px;align-items:center}
.sec-chip.sec-marked{background:color-mix(in srgb,var(--c-glow) 45%,var(--c-bg));outline-offset:0}
.sec-slot{display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;margin-left:auto}
.sec-files{display:flex;flex-direction:column;gap:6px}
.sec-file{border:1px solid var(--c-line);border-radius:8px;padding:6px 10px}
.sec-file b{display:block;font-family:var(--c-mono);font-size:13.5px}
.sec-file pre{margin:4px 0 0;white-space:pre-wrap;font:14px/1.4 var(--c-mono)}
.sec-call{display:flex;flex-direction:column;gap:4px}
.sec-line{display:grid;grid-template-columns:4.5em 1fr;gap:8px;padding:4px 6px}
.sec-line b{color:var(--c-muted);font-size:13.5px}
.sec-note{font:15px/1.5 var(--c-mono);white-space:pre-wrap;padding:14px}
.sec-card.sec-sticky{background:var(--sec-sticky,#fff3a8);color:#2b2600;border-color:#e6d66a;box-shadow:2px 3px 0 #0002}
.calm .sec-spot{transition:none}
`;
    document.head.appendChild(s);
  }

  // ---------- DOM helpers ----------
  const NS = 'http://www.w3.org/2000/svg';
  function h(tag, attrs, ...kids) {
    const e = document.createElement(tag);
    for (const k in attrs || {}) {
      const v = attrs[k];
      if (v == null || v === false) continue;
      if (k === 'class') e.className = v; else if (k === 'text') e.textContent = v;
      else if (k.startsWith('on')) e.addEventListener(k.slice(2), v); else e.setAttribute(k, v === true ? '' : v);
    }
    for (const c of kids.flat(Infinity)) if (c != null && c !== false) e.append(c.nodeType ? c : document.createTextNode(String(c)));
    return e;
  }
  // an icon given as a Node, or as an SVG/HTML string (parsed), or nothing
  const iconNode = i => { if (!i) return null; if (i.nodeType) return i; const t = document.createElement('template'); t.innerHTML = String(i).trim(); return t.content.firstChild; };
  // a small padlock icon for address bars (closed)
  const padlock = () => { const s = document.createElementNS(NS, 'svg'); s.setAttribute('width', 12); s.setAttribute('height', 14); s.setAttribute('viewBox', '0 0 12 14'); s.setAttribute('aria-hidden', 'true');
    s.innerHTML = '<rect x="1" y="6" width="10" height="7.5" rx="1.5" fill="currentColor"/><path d="M3 6V4.2a3 3 0 0 1 6 0V6" fill="none" stroke="currentColor" stroke-width="1.6"/>'; return s; };
  // the made-up logo: a simple shape and the org's name
  const LOGO = {
    pebble: '<ellipse cx="12" cy="13" rx="9" ry="7"/>', tower: '<path d="M8 22V8l4-5 4 5v14z"/>', leaf: '<path d="M4 20C4 9 11 4 21 4c0 10-5 17-17 16z"/>',
    box: '<path d="M3 8l9-4 9 4v10l-9 4-9-4z"/>', book: '<path d="M3 5h8v15H3zM13 5h8v15h-8z"/>', wave: '<path d="M2 14c3-4 6-4 9 0s6 4 9 0v6H2z"/>',
    shield: '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z"/>', circle: '<circle cx="12" cy="12" r="9"/>', star: '<path d="M12 2l3 7 7 .6-5.3 4.6 1.7 7-6.4-4-6.4 4 1.7-7L2 9.6 9 9z"/>',
  };
  function logo(l) {
    if (!l) return null;
    const s = document.createElementNS(NS, 'svg'); s.setAttribute('width', 28); s.setAttribute('height', 28); s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('aria-hidden', 'true');
    s.innerHTML = `<g fill="${l.color || 'currentColor'}">${LOGO[l.shape] || LOGO.circle}</g>`;
    return h('div', {class: 'sec-logo'}, s, l.name || '');
  }

  // =====================================================================================================
  // ARTIFACTS: artifact(kind, data, opts) -> handle. Kinds: email, sms, login, log, file, call, note.
  // Any part may be a spot: give it spot: 'id' or spot: {id, tell}. Tapping, Enter or Space fires opts.onSpot(id, el, tell).
  // The tool decides if it is right, then marks it: handle.mark(id, 'marked' | 'right' | 'wrong' | 'dim' | null).
  // Links never navigate: hover, focus or long-press shows the real href in the status bar; a tap fires
  // opts.onLink(href, el) and shows opts.linkNote(href) (default "In real life, this would open: <href>").
  // opts: {onSpot, onLink, onDetails, linkNote, dark, status: true|false, statusText, title, maxHeight, className, fieldNote}
  // =====================================================================================================
  function artifact(kind, data = {}, opts = {}) {
    style();
    const spots = new Map();
    const card = h('div', {class: 'sec-card sec-' + kind + (opts.dark ? ' sec-dark' : '') + (opts.className ? ' ' + opts.className : '')});
    let statusEl = null, statusBase = '';
    const status = t => { if (statusEl) statusEl.textContent = t == null ? statusBase : t; };
    const spotOf = s => s == null ? null : typeof s === 'string' ? {id: s} : s;
    // make an element a spot (keyboard and pointer)
    function spot(el, s, label) {
      s = spotOf(s); if (!s) return el;
      el.classList.add('sec-spot'); el.dataset.spot = s.id;
      if (!el.matches('button,a,input')) { el.tabIndex = 0; el.setAttribute('role', 'button'); }
      el.setAttribute('aria-pressed', 'false');
      if (label) el.setAttribute('aria-label', label);
      const fire = e => { if (opts.onSpot) opts.onSpot(s.id, el, s.tell, e); };
      el.addEventListener('click', e => { e.preventDefault(); fire(e); });
      if (el.tagName !== 'BUTTON') el.addEventListener('keydown', e => { if ((e.key === 'Enter' || e.key === ' ') && e.target === el) { e.preventDefault(); fire(e); } });
      spots.set(s.id, {el, tell: s.tell});
      return el;
    }
    // a link: shows its real address, never navigates
    function link(l) {
      guard(l.href, kind + ' link');
      const a = h('span', {class: 'sec-link', tabindex: l.spot ? null : 0, role: l.spot ? null : 'link', 'data-href': l.href, text: l.text});
      const show = () => status(l.href), hide = () => status();
      a.addEventListener('pointerenter', show); a.addEventListener('pointerleave', hide);
      a.addEventListener('focus', show); a.addEventListener('blur', hide);
      let lp = null;
      a.addEventListener('touchstart', () => { lp = setTimeout(show, 450); }, {passive: true});
      a.addEventListener('touchend', () => clearTimeout(lp));
      a.addEventListener('click', e => { e.preventDefault(); status((opts.linkNote || (u => 'In real life, this would open: ' + u))(l.href)); if (opts.onLink) opts.onLink(l.href, a); });
      if (!l.spot) a.addEventListener('keydown', e => { if (e.key === 'Enter') a.click(); });
      return l.spot ? spot(a, l.spot, `${l.text} (link to ${l.href})`) : a;
    }
    // a paragraph: a string, {text, spot}, or {parts: [string | {text, href, spot}], spot}
    function para(p, tag = 'p', cls) {
      if (typeof p === 'string') return h(tag, {class: cls}, p);
      if (p.parts) return spot(h(tag, {class: cls}, p.parts.map(x => typeof x === 'string' ? x : x.href ? link(x) : x.spot ? spot(h('span', {}, x.text), x.spot) : x.text)), p.spot);
      if (p.href) return h(tag, {class: cls}, link(p));
      return spot(h(tag, {class: cls}, p.text), p.spot);
    }
    const title = t => t ? h('div', {class: 'sec-title'}, typeof t === 'string' ? t : [t.text, t.small ? h('small', {}, t.small) : null]) : null;
    let body;
    const tl = opts.title || data.title;

    if (kind === 'email') {
      const addr = v => typeof v === 'string' ? v : v.address;
      for (const k of ['from', 'replyTo', 'to']) if (data[k]) guard(addr(data[k]), 'email ' + k);
      const row = (label, v) => v == null ? [] : [h('dt', {}, label), h('dd', {}, typeof v === 'string' || !v.spot ? (typeof v === 'string' ? v : v.text || v.address) : spot(h('span', {}, v.text || v.address), v.spot))];
      const fromV = data.from == null ? null : {text: (data.fromName ? data.fromName + ' ' : '') + '<' + addr(data.from) + '>', spot: (data.from && data.from.spot) || data.fromSpot};
      body = h('div', {},
        h('div', {class: 'sec-head'},
          h('dt', {}, 'Subject'), h('dd', {}, data.subject ? spot(h('span', {class: 'sec-subject'}, typeof data.subject === 'string' ? data.subject : data.subject.text), data.subject.spot) : ''),
          ...row('From', fromV), ...row('Reply-to', data.replyTo), ...row('To', data.to), ...row('Sent', data.time)),
        h('div', {class: 'sec-body'},
          (data.body || []).map(p => para(p)),
          (data.links || []).length ? h('p', {}, data.links.map(l => [link(l), ' '])) : null,
          (data.attachments || []).length ? h('div', {}, data.attachments.map(a => spot(h('span', {class: 'sec-att'}, '📎 ', a.name), a.spot))) : null));
    } else if (kind === 'sms') {
      body = h('div', {class: 'sec-phone'},
        h('div', {class: 'sec-sender'}, spot(h('span', {}, data.sender || ''), data.senderSpot), data.number ? h('small', {}, data.number) : null),
        h('div', {class: 'sec-bubbles'}, (data.bubbles || []).map(b => para(b, 'div', 'sec-bubble' + (b && b.me ? ' me' : ''))),
          (data.links || []).map(l => h('div', {class: 'sec-bubble'}, link(l)))));
    } else if (kind === 'login') {
      guard(data.address, 'login address bar');
      const note = h('div', {class: 'sec-lock-note', 'aria-live': 'polite'});
      const field = f => {
        const shown = f.fill == null ? '' : f.type === 'password' ? '•'.repeat(String(f.fill).length || 8) : String(f.fill);
        const inp = h('div', {class: 'sec-input', role: 'textbox', 'aria-readonly': 'true', tabindex: 0, 'aria-label': f.label}, shown);
        inp.addEventListener('focus', () => { note.textContent = opts.fieldNote || 'Practice page: nothing you type goes anywhere.'; });
        inp.addEventListener('keydown', e => { if (e.key.length === 1) e.preventDefault(); });
        return h('label', {class: 'sec-field'}, f.label, inp);
      };
      body = h('div', {},
        h('div', {class: 'sec-chrome'}, h('div', {class: 'sec-dots', 'aria-hidden': 'true'}, h('i'), h('i'), h('i')),
          spot(h('div', {class: 'sec-addr', 'aria-label': 'Address bar: ' + data.address}, padlock(), data.address), data.addressSpot)),
        h('div', {class: 'sec-page'}, logo(data.logo), data.heading ? h('div', {style: 'font-weight:700;font-size:17px'}, data.heading) : null,
          (data.fields || [{label: 'User name'}, {label: 'Password', type: 'password'}]).map(field),
          h('button', {class: 'sec-fake-btn', type: 'button', 'aria-disabled': 'true', onclick: () => { note.textContent = opts.fieldNote || 'Practice page: nothing you type goes anywhere.'; }}, data.button || 'Sign in'), note));
    } else if (kind === 'log') {
      // {columns: [{key, label, mono, nowrap}], rows: [{key: value | {text, sub}, spot, details}], sort: true, filter: 'account'}
      const cols = data.columns || [];
      let rows = (data.rows || []).map((r, i) => ({...r, _i: i})), sortKey = null, sortDir = 1, filt = '';
      const tbody = h('tbody');
      const val = v => v == null ? '' : typeof v === 'object' ? v.text : v;
      const cell = (c, v) => h('td', {class: [c.mono ? 'sec-mono' : '', c.nowrap ? 'sec-nowrap' : ''].join(' ').trim() || null}, typeof v === 'object' && v ? [v.text, v.sub ? h('small', {}, v.sub) : null] : String(v == null ? '' : v));
      const open = new Set();
      // a row with details opens and closes in place (a toggle never rebuilds the row under the pointer), by tap,
      // Enter or Space; a row with details but no spot still gets a tab stop. opts.onDetails(row, isOpen) hears each
      // toggle. The details text sits in a box as wide as the visible part of the card (sticky at its left edge), so
      // it wraps in view even when the table scrolls sideways.
      const scroller = h('div', {class: 'sec-scroll'});
      const fitDetails = () => { const w = scroller.clientWidth; if (!w) return;
        for (const b of scroller.querySelectorAll('.sec-detailbox')) b.style.width = Math.max(120, w - 18) + 'px'; };
      // a fade at the right edge says the table scrolls sideways
      const more = () => scroller.classList.toggle('sec-more', scroller.scrollLeft + scroller.clientWidth < scroller.scrollWidth - 2);
      scroller.addEventListener('scroll', more, {passive: true});
      if (typeof ResizeObserver === 'function') new ResizeObserver(() => { fitDetails(); more(); }).observe(scroller);
      const detailRow = r => h('tr', {class: 'sec-details'}, h('td', {colspan: cols.length}, h('div', {class: 'sec-detailbox'}, r.details)));
      function toggle(r, tr) {
        const was = open.has(r._i);
        if (was) { open.delete(r._i); const n = tr.nextElementSibling; if (n && n.classList.contains('sec-details')) n.remove(); }
        else { open.add(r._i); tr.after(detailRow(r)); fitDetails(); }
        more();
        tr.setAttribute('aria-expanded', String(!was));
        if (opts.onDetails) opts.onDetails(r, !was);
      }
      // numbers sort as numbers only when the whole value is a number ("312", "1,400"); times like "07:41" sort as text
      const num = v => { const s = String(v).replace(/,/g, '').trim(); return /^-?\d*\.?\d+$/.test(s) ? parseFloat(s) : null; };
      const ths = [];
      function draw() {
        tbody.textContent = '';
        for (const k of [...spots.keys()]) if (String(k).startsWith('row:')) spots.delete(k);
        let list = rows.filter(r => !filt || String(val(r[data.filter])) === filt);
        if (sortKey) list = [...list].sort((a, b) => { const x = val(a[sortKey]), y = val(b[sortKey]), nx = num(x), ny = num(y);
          return sortDir * (nx != null && ny != null ? nx - ny : String(x).localeCompare(String(y))) || a._i - b._i; });
        for (const r of list) {
          const tr = h('tr', {}, cols.map(c => cell(c, r[c.key])));
          const id = r.spot ? spotOf(r.spot).id : null;
          if (r.spot) spot(tr, r.spot, (r.label || cols.map(c => c.label + ' ' + val(r[c.key])).join(', ')));
          if (r.details) {
            tr.classList.add('sec-hasdetails'); tr.setAttribute('aria-expanded', String(open.has(r._i)));
            if (!r.spot) { tr.tabIndex = 0; tr.setAttribute('role', 'button'); tr.setAttribute('aria-label', (r.label || cols.map(c => c.label + ' ' + val(r[c.key])).join(', ')) + '. Details'); }
            tr.addEventListener('click', () => toggle(r, tr));
            tr.addEventListener('keydown', e => { if ((e.key === 'Enter' || e.key === ' ') && e.target === tr) { e.preventDefault(); toggle(r, tr); } });
          }
          tbody.append(tr);
          if (r.details && open.has(r._i)) tbody.append(detailRow(r));
          if (id && marks.has(id)) applyMark(id, marks.get(id));
          if (id && tags.has(id)) applyTag(id, ...tags.get(id));
        }
        fitDetails(); more();
        if (data.sort) ths.forEach((th, i) => { const k = cols[i].key; th.setAttribute('aria-sort', sortKey === k ? (sortDir > 0 ? 'ascending' : 'descending') : 'none');
          const m = th.querySelector('.sec-sortmark'); if (m) m.textContent = sortKey === k ? (sortDir > 0 ? ' ▲' : ' ▼') : ' ↕'; });
      }
      const head = h('tr', {}, cols.map(c => { const th = h('th', {scope: 'col'}, data.sort ? h('button', {type: 'button', onclick: () => { sortDir = sortKey === c.key ? -sortDir : 1; sortKey = c.key; draw(); }}, c.label, h('span', {class: 'sec-sortmark', 'aria-hidden': 'true'}, ' ↕')) : c.label); ths.push(th); return th; }));
      const tools = data.filter ? h('div', {class: 'sec-tools'}, h('label', {}, 'Show ',
        h('select', {onchange: e => { filt = e.target.value; draw(); }}, h('option', {value: ''}, 'every ' + (cols.find(c => c.key === data.filter) || {label: ''}).label.toLowerCase()),
          [...new Set(rows.map(r => String(val(r[data.filter]))))].map(v => h('option', {value: v}, v))))) : null;
      scroller.append(h('table', {class: 'sec-table'}, h('thead', {}, head), tbody));
      body = h('div', {}, tools, scroller);
      card._draw = draw;
    } else if (kind === 'file' && data.layout === 'row') {
      // one line: name, the fields as small tappable chips, the seal, then handle.slot for the tool's own parts
      card.classList.add('sec-file-row');
      const name = h('div', {class: 'sec-rowname'}, data.name || '');
      const chips = (data.fields || []).map(f => {
        const c = h(f.spot ? 'button' : 'span', {class: 'sec-chip', type: f.spot ? 'button' : null}, h('small', {}, f.label), h('b', {}, String(f.value)));
        return f.spot ? spot(c, f.spot, f.label + ': ' + f.value) : c;
      });
      const seal = data.seal ? spot(h('div', {class: 'sec-chip sec-sealchip'}, h('small', {}, data.seal.label || 'Seal'), h('b', {}, iconNode(data.seal.icon), String(data.seal.value))), data.seal.spot) : null;
      card._slot = h('div', {class: 'sec-slot'});
      body = h('div', {class: 'sec-rowbody'}, name, h('div', {class: 'sec-chips'}, chips), seal, card._slot);
    } else if (kind === 'file') {
      // {title, fields: [{label, value, spot}], seal: {label, value, spot}, files: [{name, body, spot}], text}
      body = h('div', {class: 'sec-body'},
        (data.fields || []).length ? h('dl', {class: 'sec-fields'}, data.fields.map(f => [h('dt', {}, f.label), h('dd', {}, f.spot ? spot(h('span', {style: 'display:inline-block;min-width:44px;min-height:32px;padding:2px 8px;text-align:center'}, String(f.value)), f.spot, f.label + ': ' + f.value) : String(f.value))])) : null,
        data.seal ? spot(h('div', {class: 'sec-seal'}, iconNode(data.seal.icon), data.seal.label || 'Seal', ' ', h('span', {class: 'sec-mono'}, String(data.seal.value))), data.seal.spot) : null,
        (data.files || []).length ? h('div', {class: 'sec-files'}, data.files.map(f => spot(h('div', {class: 'sec-file'}, h('b', {}, f.name), f.body != null ? h('pre', {}, f.body) : null), f.spot))) : null,
        data.text ? h('pre', {class: 'sec-note', style: 'padding:0;margin:0'}, data.text) : null);
    } else if (kind === 'call') {
      body = h('div', {class: 'sec-body sec-call'}, (data.lines || []).map((l, i) => spot(h('div', {class: 'sec-line'}, h('b', {}, (data.numbered ? (i + 1) + ' ' : '') + l.speaker), h('span', {}, l.text)), l.spot, `${l.speaker}: ${l.text}`)));
    } else if (kind === 'note') {
      if (data.style !== 'text') card.classList.add('sec-sticky');
      body = h('div', {class: 'sec-note'}, (data.lines || [data.text || '']).map((l, i) => [i ? '\n' : '', typeof l === 'string' ? l : spot(h('span', {}, l.text), l.spot)]));
    } else {
      console.error('Sec.artifact: unknown kind ' + kind);
      body = h('div');
    }
    card.append(...[title(tl), body].filter(Boolean));
    if (data.status !== false && opts.status !== false && (kind === 'email' || kind === 'sms' || kind === 'login' || opts.status)) {
      statusEl = h('div', {class: 'sec-status', 'aria-live': 'polite'}); statusBase = opts.statusText || ''; status();
      card.append(statusEl);
    }
    if (opts.maxHeight) { card.style.maxHeight = opts.maxHeight + 'px'; card.style.overflow = 'auto'; }

    // marks and tags survive a log re-sort or filter
    const marks = new Map(), tags = new Map();
    function applyTag(id, text, cls) {
      const s = spots.get(id); if (!s) return;
      s.el.querySelectorAll(':scope > .sec-tag, :scope > td:last-child > .sec-tag').forEach(t => t.remove());
      if (text) (s.el.tagName === 'TR' ? s.el.lastElementChild : s.el).append(h('span', {class: 'sec-tag' + (cls ? ' ' + cls : '')}, text));
    }
    function applyMark(id, how) {
      const s = spots.get(id); if (!s) return;
      s.el.classList.remove('sec-marked', 'sec-right', 'sec-wrong', 'sec-dim');
      if (how) s.el.classList.add('sec-' + how);
      s.el.setAttribute('aria-pressed', how === 'marked' || how === 'right' ? 'true' : 'false');
    }
    if (card._draw) card._draw();
    return {
      el: card, kind, slot: card._slot || null,
      spot: id => (spots.get(id) || {}).el || null,
      spots: () => [...spots.keys()],
      tell: id => (spots.get(id) || {}).tell,
      mark(id, how) { if (how) marks.set(id, how); else marks.delete(id); applyMark(id, how); },
      marked: () => [...marks].filter(([, v]) => v === 'marked' || v === 'right').map(([k]) => k),
      clearMarks() { for (const id of [...marks.keys()]) { marks.delete(id); applyMark(id, null); } },
      tag(id, text, cls) { if (text) tags.set(id, [text, cls]); else tags.delete(id); applyTag(id, text, cls); },
      status,
    };
  }

  return {pure, ...pure, world, guard, artifact, h};
})();
