// Curio Class family engine: robot. A program of cards, the card strip that edits it, and the runner that walks it
// (once in order, or as rules checked every tick), with a trace of what each card did. Inlined by
// scripts/bundle_tool.py from a kit:robot script tag, after kit:curio. Spec and API: docs/families/robot.md (full
// description in tools/snowy-mail-route/spec.md, "Family engine"). Lifted from robot-dance's card strip and step
// runner. New features go here and into that doc in the same change, keeping existing calls working.
// Sound, voice, art and the world stay in the tool.
const Robot = (() => {
  'use strict';
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const calm = () => typeof Curio !== 'undefined' && Curio.reduce;
  let uid = 1;

  // ==================================================================================================================
  // 1. Program model: prog.list = [{id, op, args}]. Every edit fires the listeners and bumps prog.gen.
  // ==================================================================================================================
  function program(opts = {}) {
    const fns = [];
    const card = (x) => {
      const o = typeof x === 'string' ? {op: x} : x;
      return {id: uid++, op: o.op, args: o.args ? {...o.args} : {}};
    };
    const p = {
      list: [], gen: 0, max: opts.max || Infinity,
      get length() { return p.list.length; },
      get full() { return p.list.length >= p.max; },
      ops: () => p.list.map(c => c.op),
      card: i => p.list[i],
      indexOf: id => p.list.findIndex(c => c.id === id),
      on(fn) { fns.push(fn); return p; },
      // add(op, at = end, args): null when full
      add(op, at, args) {
        if (p.full) return null;
        const c = card({op, args});
        at = at == null ? p.list.length : clamp(at, 0, p.list.length);
        p.list.splice(at, 0, c);
        fire({kind: 'add', i: at, card: c});
        return c;
      },
      replace(i, op, args) {
        const old = p.list[i]; if (!old) return null;
        const c = {id: old.id, op, args: args ? {...args} : {}};
        p.list[i] = c;
        fire({kind: 'replace', i, card: c, was: old});
        return c;
      },
      // move(i, d): swap card i with its neighbor d steps away (d = -1 or 1); returns the new index or -1
      move(i, d) {
        const j = i + d;
        if (!p.list[i] || j < 0 || j >= p.list.length) return -1;
        const c = p.list.splice(i, 1)[0];
        p.list.splice(j, 0, c);
        fire({kind: 'move', from: i, to: j, card: c});
        return j;
      },
      remove(i) {
        const c = p.list[i]; if (!c) return null;
        p.list.splice(i, 1);
        fire({kind: 'remove', i, card: c});
        return c;
      },
      clear() { p.list = []; fire({kind: 'clear'}); },
      // load(list): ops ('up') or {op, args}; new ids
      load(list) { p.list = (list || []).slice(0, p.max).map(card); fire({kind: 'load'}); },
    };
    function fire(info) {
      p.gen++;
      for (const f of fns) f(info, p);
      if (opts.onEdit) opts.onEdit(info, p);
    }
    return p;
  }

  // ==================================================================================================================
  // 3. Runner. Robot.run(prog, opts) -> a runner, ready; r.go(), r.step(), r.stop().
  //    style 'sequence': each card once, in order; exec(card, i, r) -> {ok: true} or {stop: reason}, plus snap.
  //      With target (a list of ops or cards): robot-dance's results, ok, wrong, ranout (no card i), extra (target done).
  //    style 'rules': every tick the cards are checked top to bottom with when(card, world, r); the first that holds
  //      runs exec(card, i, world, r); at most one fires per tick. Then tick(n, world, r) moves the world; return false
  //      from it to end the run. Runs until then, opts.ticks, a {stop} or Stop.
  // ==================================================================================================================
  let last = null;
  function run(prog, o = {}) {
    const style = o.style || 'sequence';
    const list = () => Array.isArray(prog) ? prog : prog.list;
    const pgen = () => Array.isArray(prog) ? 0 : prog.gen;
    const beatMs = () => typeof o.beat === 'function' ? o.beat() : (o.beat || 1000);
    const g0 = pgen();
    let gen = 0, busy = false, want = null;
    const r = {
      style, status: 'ready', next: 0, tick: 0, trace: [], result: null,
      get busy() { return busy; },
      get gen() { return gen; },
      alive: g => g === undefined ? (r.status === 'running' || r.status === 'paused' || r.status === 'ready') : g === gen && r.status !== 'stopped' && r.status !== 'ended',
      traceFor: i => r.trace.filter(e => e.i === i),
      go() { if (r.status === 'ended' || r.status === 'stopped') return false; want = 'go'; if (!busy) loop(); return true; },
      step() { if (busy || r.status === 'ended' || r.status === 'stopped') return false; want = 'step'; loop(); return true; },
      stop() {
        if (r.status === 'ended' || r.status === 'stopped') return false;
        gen++; busy = false; want = null;
        finish({result: 'stopped', step: style === 'rules' ? r.tick : r.next});
        return true;
      },
    };
    last = r;
    function finish(res) {
      r.result = res;
      r.status = res.result === 'stopped' ? 'stopped' : 'ended';
      want = null; busy = false;                              // onEnd sees a settled runner
      if (o.onEnd) o.onEnd(res, r);
    }
    const same = o.same || ((c, t) => c.op === (t && typeof t === 'object' ? t.op : t));
    // one beat; true when the run goes on
    async function beat(g) {
      if (pgen() !== g0) { finish({result: 'edited', step: r.next}); return false; }
      const L = list();
      if (style === 'rules') {
        const world = o.world, n = r.tick;
        let i = -1, out = {ok: true};
        for (let k = 0; k < L.length; k++) if (!o.when || o.when(L[k], world, r)) { i = k; break; }
        if (i >= 0) out = (await (o.exec ? o.exec(L[i], i, world, r) : null)) || {ok: true};
        if (g !== gen) return false;
        const result = out.stop ? 'stop' : i < 0 ? 'none' : 'ok';
        const snap = 'snap' in out ? out.snap : o.snap ? o.snap(world) : undefined;
        if (i >= 0 || o.traceIdle) r.trace.push({t: n, i, op: i >= 0 ? L[i].op : null, result, reason: out.stop || null, snap});
        const ms = beatMs();
        if (o.onStep) o.onStep(i, i >= 0 ? L[i] : null, {result, reason: out.stop || null, snap, tick: n}, ms, r);
        const more = out.stop ? true : o.tick ? o.tick(n, world, r) !== false : true;
        await wait(ms);
        if (g !== gen) return false;
        r.tick = n + 1;
        if (out.stop) { finish({result: 'stop', step: n, i, reason: out.stop}); return false; }
        if (!more || (o.ticks && r.tick >= o.ticks)) { finish({result: 'done', step: r.tick}); return false; }
        return true;
      }
      const tgt = o.target, i = r.next;
      const n = tgt ? Math.max(L.length, tgt.length) : L.length;
      if (i >= n) { finish({result: 'done', step: i}); return false; }
      const card = L[i], wanted = tgt ? tgt[i] : undefined;
      let result = 'ok';
      if (tgt) result = !card ? 'ranout' : wanted === undefined ? 'extra' : !same(card, wanted) ? 'wrong' : 'ok';
      let out = {ok: true};
      if (card && o.exec) out = (await o.exec(card, i, r, result)) || {ok: true};
      if (g !== gen) return false;
      if (out.stop) result = 'stop';
      const snap = 'snap' in out ? out.snap : o.snap ? o.snap() : undefined;
      r.trace.push({t: i, i, op: card ? card.op : null, result, reason: out.stop || null, snap});
      const ms = beatMs();
      if (o.onStep) o.onStep(i, card || null, {result, reason: out.stop || null, snap, want: wanted}, ms, r);
      await wait(result === 'ok' ? ms : ms + (o.pause || 0));
      if (g !== gen) return false;
      if (result !== 'ok') { finish({result, step: i, reason: out.stop || null}); return false; }
      r.next = i + 1;
      if (r.next >= n) { finish({result: 'done', step: r.next}); return false; }
      return true;
    }
    async function loop() {
      busy = true;
      r.status = 'running';
      const g = gen;
      for (;;) {
        const more = await beat(g);
        if (g !== gen) return;                                // stopped: late beats are ignored
        if (!more) break;
        if (want === 'step') { r.status = 'paused'; busy = false; if (o.onPause) o.onPause(style === 'rules' ? r.tick : r.next, r); break; }
      }
    }
    return r;
  }

  // ==================================================================================================================
  // 2. Card strip: Robot.strip(el, {prog, max, layout, renderCard, onSelect, ...}). Numbered cards and dashed empty
  //    slots, one selection, the three card buttons, keys, card states (now, bug badge, pulse) and the run pointer.
  // ==================================================================================================================
  const ICON = {
    earlier: '<path d="M14.5 5 7.5 12l7 7" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 5.5v13" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".55"/>',
    later: '<path d="M9.5 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 5.5v13" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".55"/>',
    up: '<path d="M5 14.5 12 7.5l7 7" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.5 20h13" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".55"/>',
    down: '<path d="M5 9.5l7 7 7-7" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.5 4h13" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".55"/>',
    trash: '<path d="M3.5 6.5h17M9 6.5V3.8h6v2.7M5.8 6.5l1 14h10.4l1-14M10 10.2v6.8M14 10.2v6.8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
  };
  const svgI = d => `<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">${d}</svg>`;
  let cssDone = false;
  function css() {
    if (cssDone) return; cssDone = true;
    const s = document.createElement('style');
    s.id = 'robot-css';
    // first in <head>, so a tool's own styles win
    s.textContent = `
.rb-strip{position:relative;display:grid;grid-template-columns:repeat(var(--rb-cols,8),var(--rb-cw,90px));column-gap:var(--rb-gap,10px);row-gap:var(--rb-rgap,0px);justify-content:center;padding-top:var(--rb-pt,26px);border-radius:16px;transition:box-shadow .2s}
.rb-strip.rb-column{grid-template-columns:var(--rb-cw,260px);row-gap:var(--rb-gap,10px);padding:0 0 0 var(--rb-pl,34px)}
.rb-cell{position:relative;width:var(--rb-cw,90px);height:var(--rb-ch,96px);border-radius:var(--rb-r,14px)}
.rb-cell.empty{border:3px dashed var(--rb-empty,#8a97b8)}
.rb-slotn{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:800 calc(var(--rb-nd,28px)*.62)/1 'Trebuchet MS','Segoe UI',sans-serif;color:var(--rb-empty,#8a97b8)}
.rb-cell:not(.empty) .rb-slotn{display:none}
.rb-card{position:absolute;inset:0;width:100%;height:100%;margin:0;padding:0;border:3px solid var(--rb-line,#132036);border-radius:var(--rb-r,14px);background:var(--rb-card,#fff);color:var(--rb-ink,#1c2433);overflow:visible;transition:transform .15s ease,box-shadow .15s}
.rb-card[aria-pressed="true"]{transform:translateY(-10px);box-shadow:0 0 0 5px var(--rb-sel,#ffd23f),0 0 0 8px var(--rb-line,#132036)}
.rb-column .rb-card[aria-pressed="true"]{transform:translateX(10px)}
.rb-card.now{box-shadow:0 0 0 4px #fff,0 0 22px 8px var(--rb-glow,#ffd23f)}
.rb-card[aria-disabled="true"]{cursor:default}
.rb-face{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;pointer-events:none;border-radius:inherit;overflow:hidden}
.rb-num{position:absolute;left:-9px;top:-11px;width:var(--rb-nd,28px);height:var(--rb-nd,28px);border-radius:50%;background:#fff;border:3px solid var(--rb-line,#132036);font:800 calc(var(--rb-nd,28px)*.56)/1 'Trebuchet MS','Segoe UI',sans-serif;display:flex;align-items:center;justify-content:center;color:var(--rb-ink,#1c2433);z-index:1;pointer-events:none}
.rb-bug{display:none;position:absolute;left:50%;transform:translateX(-50%);top:calc(var(--rb-nd,28px)*-.65);min-width:var(--rb-nd,28px);height:var(--rb-nd,28px);border-radius:999px;background:var(--rb-bug,#d6203a);color:#fff;border:3px solid #fff;font:900 calc(var(--rb-nd,28px)*.66)/1 'Trebuchet MS',sans-serif;align-items:center;justify-content:center;z-index:2;box-shadow:0 2px 6px #0006;pointer-events:none}
.rb-cell.bug .rb-bug{display:flex}
.rb-cell.bug .rb-card{animation:rb-wob .32s ease-in-out 3}
@keyframes rb-wob{25%{rotate:-6deg}75%{rotate:6deg}}
.rb-cell.pulse .rb-card{animation:rb-pulse 1.1s ease-in-out infinite}
@keyframes rb-pulse{50%{box-shadow:0 0 0 6px var(--rb-pulse,#ffd23f),0 0 18px 6px var(--rb-pulse,#ffd23f)}}
.calm .rb-cell.pulse .rb-card{animation:none;box-shadow:0 0 0 6px var(--rb-pulse,#ffd23f)}
.calm .rb-cell.bug .rb-card{animation:none}
.rb-card.rb-flip{animation:rb-flip .36s ease-out}
@keyframes rb-flip{0%{scale:0 1}100%{scale:1 1}}
.rb-strip.rb-flash{box-shadow:0 0 0 5px var(--rb-glow,#ffd23f)}
.rb-ptr{position:absolute;left:0;top:0;width:var(--rb-pw,34px);height:var(--rb-ph,18px);pointer-events:none;transition:left .2s ease,top .2s ease;filter:drop-shadow(0 0 6px var(--rb-glow,#ffd23f));display:none;z-index:2}
.rb-ptr svg{width:100%;height:100%;display:block}
.rb-cbtns{position:relative;height:var(--rb-bh,72px)}
.rb-cbtns.rb-column{height:auto;width:var(--rb-bw,72px)}
.rb-cbtns .rb-in{position:absolute;top:var(--rb-bt,6px);left:0;display:flex;gap:var(--rb-bgap,16px);transition:left .25s ease,top .25s ease}
.rb-cbtns.rb-column .rb-in{flex-direction:column;left:var(--rb-bt,6px);top:0}
.rb-cbtns.off .rb-in{visibility:hidden}
.rb-cbtns button{width:var(--rb-bs,60px);height:var(--rb-bs,60px);border-radius:50%;background:#fff;border:3px solid var(--rb-line,#132036);padding:0;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 0 #0005;color:var(--rb-ink,#1c2433)}
.rb-cbtns button svg{width:52%;height:52%;display:block}
.rb-cbtns button[aria-disabled="true"]{opacity:.4;cursor:default}
.rb-cbtns .rb-del{color:var(--rb-bug,#c0182f)}`;
    document.head.insertBefore(s, document.head.firstChild);
  }

  function strip(el, o = {}) {
    css();
    const prog = o.prog, col = o.layout === 'column', max = o.max || prog.max;
    const keyPrev = col ? 'ArrowUp' : 'ArrowLeft', keyNext = col ? 'ArrowDown' : 'ArrowRight';
    el.classList.add('rb-strip', col ? 'rb-column' : 'rb-row');
    el.setAttribute('role', 'list');
    if (!el.hasAttribute('aria-label')) el.setAttribute('aria-label', o.label || 'Cards');
    const cells = [], cardEls = new Map();
    for (let i = 0; i < max; i++) {
      const c = document.createElement('div');
      c.className = 'rb-cell empty'; c.setAttribute('role', 'listitem');
      c.innerHTML = `<span class="rb-slotn" aria-hidden="true">${i + 1}</span><span class="rb-bug" aria-hidden="true">?</span>`;
      el.appendChild(c); cells.push(c);
    }
    const ptr = document.createElement('div');
    ptr.className = 'rb-ptr'; ptr.setAttribute('aria-hidden', 'true');
    ptr.innerHTML = col ? '<svg viewBox="0 0 18 34"><path d="M2 3v28L16 17z" fill="var(--rb-glow,#ffd23f)" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/></svg>'
      : '<svg viewBox="0 0 34 18"><path d="M3 2h28L17 16z" fill="var(--rb-glow,#ffd23f)" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/></svg>';
    el.appendChild(ptr);
    // the card buttons, under the strip (row) or beside it (column)
    let box = o.buttons;
    if (!box) { box = document.createElement('div'); el.after(box); }
    box.classList.add('rb-cbtns', 'off'); if (col) box.classList.add('rb-column');
    const N = Object.assign(col ? {earlier: 'Move up', later: 'Move down'} : {earlier: 'Move earlier', later: 'Move later'}, {remove: 'Take away'}, o.names || {});
    box.innerHTML = `<div class="rb-in" role="group" aria-label="${o.buttonsLabel || 'The picked card'}">` +
      `<button type="button" class="rb-prev" aria-label="${N.earlier}">${svgI(col ? ICON.up : ICON.earlier)}</button>` +
      `<button type="button" class="rb-del" aria-label="${N.remove}">${svgI(ICON.trash)}</button>` +
      `<button type="button" class="rb-next" aria-label="${N.later}">${svgI(col ? ICON.down : ICON.later)}</button></div>`;
    const inn = box.firstChild, bPrev = inn.children[0], bDel = inn.children[1], bNext = inn.children[2];

    const st = {sel: null, why: null, now: null, bug: null, bugText: '?', pulse: null, locked: false};
    const off = b => b.getAttribute('aria-disabled') === 'true';
    const cardOf = i => cells[i] && cells[i].querySelector('.rb-card');

    function make(c) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'rb-card'; b.dataset.rbid = c.id;
      b.innerHTML = '<span class="rb-num" aria-hidden="true"></span><span class="rb-face"></span>';
      cardEls.set(c.id, b);
      return b;
    }
    const rects = () => { const m = new Map(); for (const [id, b] of cardEls) if (b.isConnected) m.set(id, b.getBoundingClientRect()); return m; };
    function render(opt = {}) {
      const L = prog.list, act = document.activeElement;
      const actId = act && act.classList && act.classList.contains('rb-card') ? +act.dataset.rbid : null;
      for (const [id, b] of cardEls) if (!L.some(c => c.id === id)) { b.remove(); cardEls.delete(id); }
      cells.forEach((cell, i) => {
        const c = L[i], cur = cardOf(i);
        cell.classList.toggle('empty', !c);
        cell.classList.toggle('bug', st.bug === i && !!c);
        cell.classList.toggle('pulse', st.pulse === i && !!c);
        if (!c) { if (cur) cur.remove(); return; }
        const b = cardEls.get(c.id) || make(c);
        if (cur && cur !== b) cur.remove();
        if (b.parentNode !== cell) cell.appendChild(b);
        const sig = c.op + '|' + JSON.stringify(c.args) + '|' + i;
        if (b._sig !== sig) { b._sig = sig; if (o.renderCard) o.renderCard(c, i, b.querySelector('.rb-face'), b); }
        b.querySelector('.rb-num').textContent = i + 1;
        b.setAttribute('aria-label', o.cardLabel ? o.cardLabel(c, i) : `Card ${i + 1}: ${c.op}`);
        b.setAttribute('aria-pressed', st.sel === i);
        b.classList.toggle('now', st.now === i);
        b.setAttribute('aria-disabled', st.locked);
      });
      // a card that moved between cells keeps keyboard focus
      if (actId != null && document.activeElement !== act) { const b = cardEls.get(actId); if (b && b.isConnected) b.focus({preventScroll: true}); }
      if (opt.flip && !calm()) for (const [id, r0] of opt.flip) {
        const b = cardEls.get(id); if (!b || !b.isConnected) continue;
        const r1 = b.getBoundingClientRect(), dx = r0.left - r1.left, dy = r0.top - r1.top;
        if (!dx && !dy) continue;
        b.style.transition = 'none'; b.style.translate = `${dx}px ${dy}px`;
        b.getBoundingClientRect();
        b.style.transition = 'translate .3s ease, transform .15s ease, box-shadow .15s';
        b.style.translate = '0px 0px';
        setTimeout(() => { b.style.transition = ''; b.style.translate = ''; }, 340);
      }
      syncBtns(); placePtr();
    }
    function syncBtns() {
      const L = prog.list, on = st.sel != null && st.sel < L.length && !st.locked, fa = document.activeElement;
      const hadFocus = fa && box.contains(fa);
      box.classList.toggle('off', !on);
      bPrev.setAttribute('aria-disabled', !on || st.sel === 0);
      bNext.setAttribute('aria-disabled', !on || st.sel === L.length - 1);
      bDel.setAttribute('aria-disabled', !on);
      for (const b of inn.children) b.tabIndex = on ? 0 : -1;
      // the buttons went away while one had focus: focus goes to the picked card, else the nearest card, else away
      if (!on && hadFocus) rescue(st.sel != null ? st.sel : 0);
      if (!on) return;
      placeBtns();
    }
    function rescue(i) {
      const L = prog.list, k = Math.min(i, L.length - 1), b = k >= 0 && cardOf(k);
      const t = b || (o.emptyFocus && o.emptyFocus());
      if (t) t.focus({preventScroll: true});
    }
    function placeBtns() {
      if (st.sel == null) return;
      const cell = cells[st.sel]; if (!cell || !cell.offsetParent) return;
      const bound = (o.bounds ? (typeof o.bounds === 'function' ? o.bounds() : o.bounds) : box.parentElement).getBoundingClientRect();
      const cr = cell.getBoundingClientRect(), bx = box.getBoundingClientRect();
      if (col) {
        const h = inn.offsetHeight || 212;
        inn.style.top = Math.round(clamp(cr.top + cr.height / 2 - h / 2 - bx.top, bound.top - bx.top + 4, bound.bottom - bx.top - h - 4)) + 'px';
      } else {
        const w = inn.offsetWidth || 212;
        inn.style.left = Math.round(clamp(cr.left + cr.width / 2 - w / 2 - bx.left, bound.left - bx.left + 6, bound.right - bx.left - w - 6)) + 'px';
      }
    }
    function placePtr() {
      const i = st.now;
      if (i == null || i >= max || !cells[i].offsetParent || cells[i].classList.contains('empty')) { ptr.style.display = 'none'; return; }
      ptr.style.display = 'block';
      const c = cells[i];
      if (col) {
        ptr.style.left = Math.round(c.offsetLeft - ptr.offsetWidth - 4) + 'px';
        ptr.style.top = Math.round(c.offsetTop + c.offsetHeight / 2 - ptr.offsetHeight / 2) + 'px';
      } else {
        ptr.style.left = Math.round(c.offsetLeft + c.offsetWidth / 2 - ptr.offsetWidth / 2) + 'px';
        ptr.style.top = Math.round(c.offsetTop - ptr.offsetHeight - 4) + 'px';
      }
    }

    function select(i, why = 'tap') {
      if (i == null || !prog.list[i]) return deselect(why);
      st.sel = i; st.why = why; render();
      if (o.onSelect) o.onSelect(i, why);
    }
    function deselect(why = 'tap') {
      if (st.sel == null) return;
      st.sel = null; render();
      if (o.onSelect) o.onSelect(null, why);
    }
    const canEdit = () => !st.locked && (!o.canEdit || o.canEdit());
    el.addEventListener('click', e => {
      const b = e.target.closest('.rb-card'); if (!b || !canEdit()) return;
      const i = cells.indexOf(b.parentNode);
      // a tap on the card that something else picked (a footprint, the tool) keeps it picked; a second tap puts it down
      if (st.sel === i && st.why !== 'tap' && st.why !== 'key') { st.why = 'tap'; return; }
      if (st.sel === i) deselect('tap'); else select(i, 'tap');
    });
    el.addEventListener('keydown', e => {
      const b = e.target.closest && e.target.closest('.rb-card'); if (!b || e.altKey || e.ctrlKey || e.metaKey) return;
      const i = cells.indexOf(b.parentNode);
      if (st.sel === i && canEdit()) {
        if (e.key === keyPrev) { e.preventDefault(); moveSel(-1, true); }
        else if (e.key === keyNext) { e.preventDefault(); moveSel(1, true); }
        else if (e.key === 'Delete' || e.key === 'Backspace') { e.preventDefault(); removeSel(true); }
      } else if (e.key === keyPrev || e.key === keyNext) {
        const n = cardOf(i + (e.key === keyPrev ? -1 : 1));
        if (n) { e.preventDefault(); n.focus({preventScroll: true}); }
      }
    });
    addEventListener('keydown', e => {
      if (e.key !== 'Escape' || st.sel == null) return;
      const a = document.activeElement, c = cardOf(st.sel);
      deselect('key');
      if (a && box.contains(a) && c) c.focus({preventScroll: true});   // from the card buttons: back to the card
    });
    function moveSel(d, byKey) {
      const i = st.sel; if (i == null || !canEdit()) return false;
      const before = rects(), j = prog.move(i, d);
      if (j < 0) return false;
      render({flip: before});
      if (byKey) { const b = cardOf(j); if (b) b.focus({preventScroll: true}); }
      if (o.onMove) o.onMove(i, j);
      return true;
    }
    function removeSel(byKey) {
      const i = st.sel; if (i == null || !canEdit()) return false;
      const fa = document.activeElement, had = byKey || (fa && (box.contains(fa) || (fa.classList && fa.classList.contains('rb-card'))));
      const c = prog.remove(i);
      if (had) rescue(i);
      if (o.onRemove) o.onRemove(i, c);
      return true;
    }
    bPrev.onclick = () => { if (!off(bPrev)) moveSel(-1); };
    bNext.onclick = () => { if (!off(bNext)) moveSel(1); };
    bDel.onclick = () => { if (!off(bDel)) removeSel(); };

    // edits keep the selection on the same card; any edit clears the run marks (now, bug), since the run is old
    prog.on(info => {
      const s = st.sel;
      if (info.kind === 'move') { if (s === info.from) st.sel = info.to; else if (s === info.to) st.sel = info.from; }
      else if (info.kind === 'remove') { if (s === info.i) st.sel = null; else if (s != null && s > info.i) st.sel = s - 1; }
      else if (info.kind === 'add') { if (s != null && s >= info.i) st.sel = s + 1; }
      else if (info.kind === 'clear' || info.kind === 'load') st.sel = null;
      st.now = null; st.bug = null; st.pulse = null;
      render();
      if (s != null && st.sel == null && o.onSelect) o.onSelect(null, 'edit');
    });

    const api = {
      el, box, cells,
      get sel() { return st.sel; },
      get locked() { return st.locked; },
      render, select, deselect,
      // run marks: the pointer and glow, the bug badge, a pulsing card
      setNow(i) { st.now = i == null ? null : i; render(); },
      setBug(i, text = '?') { st.bug = i == null ? null : i; st.bugText = text; for (const c of cells) c.querySelector('.rb-bug').textContent = text; render(); },
      pulse(i) { st.pulse = i == null ? null : i; render(); },
      // edits off while running: cards and buttons stay focusable but aria-disabled
      lock(on) {
        on = !!on; if (on === st.locked) return;
        st.locked = on;
        if (on && st.sel != null) { const s = st.sel; st.sel = null; render(); if (o.onSelect) o.onSelect(null, 'lock'); const c = cardOf(s); if (c && box.contains(document.activeElement)) c.focus({preventScroll: true}); }
        else render();
      },
      flash(ms = 900) { el.classList.add('rb-flash'); setTimeout(() => el.classList.remove('rb-flash'), ms); },
      flip(i) {
        const b = cardOf(i); if (!b || calm()) return;
        b.classList.remove('rb-flip'); b.getBoundingClientRect(); b.classList.add('rb-flip');
        setTimeout(() => b.classList.remove('rb-flip'), 400);
      },
      // size({cw, ch, gap, rowGap, cols, nd, pad, ptrW, ptrH, btn, btnGap, btnH}) in px; null keeps a value
      size(z) {
        const set = (k, v, u = 'px') => { if (v != null) { el.style.setProperty(k, v + u); box.style.setProperty(k, v + u); } };
        set('--rb-cw', z.cw); set('--rb-ch', z.ch); set('--rb-gap', z.gap); set('--rb-rgap', z.rowGap); set('--rb-cols', z.cols, '');
        set('--rb-nd', z.nd); set(col ? '--rb-pl' : '--rb-pt', z.pad); set('--rb-pw', z.ptrW); set('--rb-ph', z.ptrH);
        set('--rb-bs', z.btn); set('--rb-bgap', z.btnGap); set(col ? '--rb-bw' : '--rb-bh', z.btnH); set('--rb-bt', z.btnTop);
        api.place();
      },
      place() { placePtr(); if (st.sel != null) placeBtns(); },
      card: cardOf, cell: i => cells[i],
    };
    render();
    return api;
  }

  return {
    version: 1, program, strip, run,
    get last() { return last; },
    get trace() { return last ? last.trace : []; },
    traceFor: i => last ? last.traceFor(i) : [],
  };
})();
