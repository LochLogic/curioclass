import { clamp, dist } from '../core/music';
import { Vec2, nowS, pushHistory, stageSize, state } from '../core/state';
import { initAudio, setFx } from '../audio/engine';
import {
  addString, chooseMenuItem, closeMenu, endHold, forgetPointer, hitMenuItem,
  moveHold, nearestBadge, nearestBody, nearestEndpoint, openMenu, projectOnString,
  pullString, releasePull, startHold, sweepPointer, updateStringOrient,
} from './strings';

export function moveFx(from: Vec2, to: Vec2): void {
  const dx = to.x - from.x;
  const dy = to.y - from.y;
  const R = 190;
  const dark = clamp(dy / R, 0, 1);
  const thin = clamp(-dy / R, 0, 1);
  const echo = clamp(Math.abs(dx) / R, 0, 1);
  state.fx = { from, to, dark, thin, echo };
  setFx(dark, thin, echo);
}

export function endFx(): void {
  if (!state.fx) return;
  state.fx = null;
  setFx(0, 0, 0);
}

function snapEndpoint(a: Vec2, b: Vec2): Vec2 {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const L = Math.hypot(dx, dy);
  const ang = Math.atan2(dy, dx);
  const snapped = Math.round(ang / (Math.PI / 4)) * (Math.PI / 4);
  return { x: a.x + Math.cos(snapped) * L, y: a.y + Math.sin(snapped) * L };
}

export function initPointer(canvas: HTMLCanvasElement, toast: (msg: string) => void): void {
  const m = state.mouse;

  const toStage = (e: PointerEvent | WheelEvent): Vec2 => {
    const r = canvas.getBoundingClientRect();
    return {
      x: ((e.clientX - r.left) * stageSize.w) / Math.max(1, r.width),
      y: ((e.clientY - r.top) * stageSize.h) / Math.max(1, r.height),
    };
  };

  canvas.addEventListener('contextmenu', e => e.preventDefault());

  canvas.addEventListener('pointerdown', e => {
    initAudio();
    const p = toStage(e);
    m.x = m.px = p.x;
    m.y = m.py = p.y;
    m.inside = true;
    forgetPointer('mouse');

    try { canvas.setPointerCapture(e.pointerId); } catch { /* ignore */ }

    // Menu interaction
    if (state.menu) {
      const hit = hitMenuItem(p);
      if (hit) {
        chooseMenuItem(hit);
      } else {
        closeMenu();
      }
      m.drag = null;
      return;
    }

    // Middle button or Shift + Left button on empty space -> Acoustic XY Air Pad
    if (e.button === 1 || (e.button === 0 && e.shiftKey)) {
      m.down = true;
      m.drag = { type: 'fx', from: p };
      moveFx(p, p);
      return;
    }

    // Right-click -> Sustain / Bow / Roll on string, or open menu on badge
    if (e.button === 2) {
      m.rightDown = true;
      const badge = nearestBadge(p, 20);
      if (badge) {
        openMenu(badge, 'hub');
        return;
      }
      const body = nearestBody(p, 20);
      if (body) {
        m.drag = { type: 'bow', s: body.s };
        state.selectedId = body.s.id;
        startHold(body.s, 'mouse-bow', body.u);
      }
      return;
    }

    if (e.button !== 0) return;
    m.down = true;

    // 1. Endpoint drag (resize / rotate)
    const ep = nearestEndpoint(p, 16);
    if (ep) {
      pushHistory();
      state.selectedId = ep.s.id;
      m.drag = { type: 'end', s: ep.s, end: ep.end };
      return;
    }

    // 2. Center badge -> click to open menu, drag to move entire string
    const badge = nearestBadge(p, 18);
    if (badge) {
      state.selectedId = badge.id;
      m.drag = {
        type: 'dot',
        s: badge,
        from: p,
        origA: { ...badge.a },
        origB: { ...badge.b },
      };
      return;
    }

    // 3. String body -> pull & pitch-bend
    const body = nearestBody(p, 10);
    if (body && state.settings.strumMode === 'hover') {
      state.selectedId = body.s.id;
      m.drag = { type: 'grab', s: body.s, u: body.u };
      pullString(body.s, body.u, p);
      return;
    }

    // 4. Click-strum mode: if clicking near strings with no modifier, allow strumming if dragging across,
    // or stretching a new string when dragging in open space.
    if (state.settings.strumMode === 'click' && !e.altKey) {
      if (body) {
        state.selectedId = body.s.id;
        m.drag = { type: 'grab', s: body.s, u: body.u };
        pullString(body.s, body.u, p);
        return;
      }
      m.drag = { type: 'strum', from: p };
      return;
    }

    // 5. Stretch a new string
    m.drag = { type: 'new', from: p };
  });

  let lastMoveT = nowS();
  canvas.addEventListener('pointermove', e => {
    const p = toStage(e);
    const t = nowS();
    const dt = Math.max(0.004, t - lastMoveT);
    lastMoveT = t;
    m.speed = Math.hypot(p.x - m.x, p.y - m.y) / dt;
    m.px = m.x;
    m.py = m.y;
    m.x = p.x;
    m.y = p.y;
    m.inside = true;

    if (state.menu) {
      const hit = hitMenuItem(p);
      state.menu.hover = hit ? hit.id : null;
      return;
    }

    if (m.drag) {
      const d = m.drag;
      if (d.type === 'new' && d.from && dist(p, d.from) > 12) {
        const b = e.altKey ? snapEndpoint(d.from, p) : p;
        state.preview = { a: d.from, b, snapped: e.altKey };
      } else if (d.type === 'end' && d.s && d.end) {
        const other = d.end === 'a' ? d.s.b : d.s.a;
        const target = e.altKey ? snapEndpoint(other, p) : p;
        d.s[d.end] = { ...target };
        d.s.touched = t;
      } else if (d.type === 'dot' && d.s && d.from && d.origA && d.origB) {
        if (dist(p, d.from) > 9) {
          pushHistory();
          d.type = 'move';
        }
      } else if (d.type === 'move' && d.s && d.from && d.origA && d.origB) {
        const dx = p.x - d.from.x;
        const dy = p.y - d.from.y;
        d.s.a = { x: d.origA.x + dx, y: d.origA.y + dy };
        d.s.b = { x: d.origB.x + dx, y: d.origB.y + dy };
        d.s.touched = t;
      } else if (d.type === 'grab' && d.s && d.u != null) {
        pullString(d.s, d.u, p);
      } else if (d.type === 'fx' && d.from) {
        moveFx(d.from, p);
      } else if (d.type === 'bow' && d.s) {
        const pr = projectOnString(p, d.s);
        moveHold(d.s, 'mouse-bow', clamp(pr.u, 0.02, 0.98));
      } else if (d.type === 'strum') {
        sweepPointer('mouse', p, t);
      }
      return;
    }

    // Free cursor movement: hover-strum (unless Ctrl is held or pointer is over HUD)
    if (state.settings.strumMode === 'hover' && !e.ctrlKey && !m.overHud) {
      sweepPointer('mouse', p, t);
    } else {
      // Still update proximity highlight cleanly without plucking
      for (const s of state.strings) {
        const pr = projectOnString(p, s);
        s.near = pr.dist < 32 && pr.u >= -0.05 && pr.u <= 1.05;
      }
      forgetPointer('mouse');
    }
  });

  const handleUp = (e: PointerEvent) => {
    const p = toStage(e);
    const d = m.drag;
    if (e.button === 2) {
      m.rightDown = false;
      if (d?.type === 'bow' && d.s) {
        endHold(d.s, 'mouse-bow');
        m.drag = null;
      }
      return;
    }

    if (!m.down) return;
    m.down = false;
    m.drag = null;
    if (!d) return;

    if (d.type === 'new') {
      const pv = state.preview;
      state.preview = null;
      if (pv && dist(pv.a, pv.b) >= 60) {
        addString(pv.a, pv.b);
      }
    } else if (d.type === 'end' && d.s) {
      updateStringOrient(d.s);
    } else if (d.type === 'grab' && d.s) {
      releasePull(d.s);
    } else if (d.type === 'fx') {
      endFx();
    } else if (d.type === 'dot' && d.s && d.from && dist(p, d.from) <= 10) {
      openMenu(d.s, 'hub');
    } else if (d.type === 'strum' && d.from) {
      // In Click-Strum mode, dragging without hitting strings creates a string if Alt was held
      forgetPointer('mouse');
    }
  };

  canvas.addEventListener('pointerup', handleUp);
  canvas.addEventListener('pointercancel', handleUp);
  canvas.addEventListener('pointerleave', () => {
    if (!m.down && !m.rightDown) {
      m.inside = false;
      forgetPointer('mouse');
    }
  });

  // Mouse wheel over string -> quick Octave shift (Shift+Wheel -> string gain)
  canvas.addEventListener('wheel', e => {
    if (state.menu) return;
    const p = toStage(e);
    const hit = nearestBody(p, 26) || (() => {
      const b = nearestBadge(p, 26);
      return b ? { s: b, u: 0.5 } : null;
    })();
    if (!hit) return;
    e.preventDefault();
    const dir = e.deltaY < 0 ? 1 : -1;
    if (e.shiftKey) {
      hit.s.gain = clamp(hit.s.gain + dir * 0.1, 0.25, 1.4);
      toast(`String volume: ${Math.round(hit.s.gain * 100)}%`);
    } else {
      hit.s.oct = clamp(hit.s.oct + dir, -2, 2);
      hit.s.touched = nowS();
      toast(`Octave: ${hit.s.oct > 0 ? '+' : ''}${hit.s.oct}`);
    }
  }, { passive: false });
}
