// Curio Class family engine: network. A graph of devices and links, the routes packets take through it, the packets
// themselves, and an SVG map with code-drawn icons and tokens that glide along the links. Inlined by
// scripts/bundle_tool.py from a kit:network script tag, after kit:curio. Spec and API: docs/families/network.md
// (full description in tools/internet-journey/spec.md, "Family engine"). New features go here and into that doc in
// the same change, keeping existing calls working.
const Net = (() => {
  // ==================================================================================================================
  // PURE PART: no DOM below this line until "DOM PART". Graph, path, reach, flows, packets, forward.
  // Everything here can run in Node or a test page (exposed as __tool.net).
  // ==================================================================================================================
  const EPS = 1e-9;
  const key = (a, b) => a < b ? a + '|' + b : b + '|' + a;
  const KINDS = ['laptop', 'tablet', 'phone', 'desktop', 'printer', 'camera', 'tv',
    'wifi-router', 'access-point', 'switch', 'core-switch', 'router', 'firewall', 'modem', 'isp', 'server', 'cloud'];
  const DEVICES = new Set(KINDS.slice(0, 7));

  // graph({nodes, links}): node {id, kind, label, x, y, up:true} in design units (1000 x 600 by default);
  // link {a, b, medium:'wire'|'wifi'|'fiber', ms, mbps, lenM, up:true, via:[[x,y],...]}. Extra fields are kept.
  // One link per pair of nodes (adding a second one replaces the first).
  function graph({nodes = [], links = []} = {}) {
    const g = {nodes: [], links: [], byId: new Map(), index: new Map(), adj: new Map(), byKey: new Map()};
    g.node = id => g.byId.get(id);
    g.link = (a, b) => g.byKey.get(key(a, b));
    for (const n of nodes) addNode(g, n);
    for (const l of links) addLink(g, l);
    return g;
  }
  function addNode(g, n) {
    const m = Object.assign({up: true, label: n.id}, n);
    if (g.byId.has(m.id)) removeNode(g, m.id);
    g.index.set(m.id, g.nodes.length); g.nodes.push(m); g.byId.set(m.id, m); g.adj.set(m.id, []);
    return m;
  }
  function addLink(g, l) {
    if (!g.byId.has(l.a) || !g.byId.has(l.b)) throw new Error(`Net: link ${l.a}-${l.b} names a missing node`);
    const k = key(l.a, l.b);
    if (g.byKey.has(k)) removeLink(g, l.a, l.b);
    const m = Object.assign({up: true, medium: 'wire', ms: 500}, l);
    g.links.push(m); g.byKey.set(k, m);
    g.adj.get(m.a).push(m); g.adj.get(m.b).push(m);
    return m;
  }
  function removeLink(g, a, b) {
    const l = g.byKey.get(key(a, b)); if (!l) return null;
    g.byKey.delete(key(a, b)); g.links.splice(g.links.indexOf(l), 1);
    for (const id of [l.a, l.b]) { const list = g.adj.get(id); list.splice(list.indexOf(l), 1); }
    return l;
  }
  function removeNode(g, id) {
    const n = g.byId.get(id); if (!n) return null;
    for (const l of [...g.adj.get(id)]) removeLink(g, l.a, l.b);
    g.nodes.splice(g.nodes.indexOf(n), 1); g.byId.delete(id); g.adj.delete(id);
    g.index.clear(); g.nodes.forEach((m, i) => g.index.set(m.id, i));
    return n;
  }
  const other = (l, id) => l.a === id ? l.b : l.a;
  const usable = (g, l, opts) => l.up && !(opts.skip && opts.skip(l));
  const nodeOk = (g, id, opts) => { const n = g.byId.get(id); return !!n && n.up && !(opts.avoid && opts.avoid(n)); };

  // path(g, from, to, {by:'ms'|'hops', skip: link => bool, avoid: node => bool}): Dijkstra over the nodes and links
  // that are up. Ties (equal cost) go to the path with fewer hops, then to the lower node index (the path whose node
  // indexes come first, read in order).
  // Returns a list of ids from `from` to `to`, or null when there is no road.
  function path(g, from, to, opts = {}) {
    const by = opts.by || 'ms';
    if (!nodeOk(g, from, {}) || !nodeOk(g, to, {})) return null;
    if (from === to) return [from];
    const dist = new Map([[from, 0]]), best = new Map([[from, [from]]]), done = new Set();
    const cmpPath = (p, q) => {
      if (p.length !== q.length) return p.length - q.length;   // equal cost: fewer hops first
      for (let i = 0; i < Math.min(p.length, q.length); i++) {
        const d = g.index.get(p[i]) - g.index.get(q[i]); if (d) return d;
      }
      return p.length - q.length;
    };
    for (;;) {
      let u = null;
      for (const [id, d] of dist) {
        if (done.has(id)) continue;
        if (u === null || d < dist.get(u) - EPS || (Math.abs(d - dist.get(u)) <= EPS && cmpPath(best.get(id), best.get(u)) < 0)) u = id;
      }
      if (u === null) return null;
      if (u === to) return best.get(u);
      done.add(u);
      for (const l of g.adj.get(u)) {
        if (!usable(g, l, opts)) continue;
        const v = other(l, u);
        if (done.has(v) || !nodeOk(g, v, v === to ? {} : opts)) continue;
        const w = by === 'hops' ? 1 : (+l.ms || 0), nd = dist.get(u) + w, np = [...best.get(u), v];
        if (!dist.has(v) || nd < dist.get(v) - EPS || (Math.abs(nd - dist.get(v)) <= EPS && cmpPath(np, best.get(v)) < 0)) {
          dist.set(v, nd); best.set(v, np);
        }
      }
    }
  }
  // cost(g, ids, by): the total ms (or hops) along a list of ids; Infinity if a link is missing
  function cost(g, ids, by = 'ms') {
    if (!ids) return Infinity;
    let t = 0;
    for (let i = 1; i < ids.length; i++) { const l = g.link(ids[i - 1], ids[i]); if (!l) return Infinity; t += by === 'hops' ? 1 : +l.ms || 0; }
    return t;
  }
  // reach(g, from, {skip, avoid}): the set of ids reachable from `from` over what is up (empty if `from` is down)
  function reach(g, from, opts = {}) {
    const seen = new Set();
    if (!nodeOk(g, from, {})) return seen;
    const stack = [from]; seen.add(from);
    while (stack.length) {
      const u = stack.pop();
      for (const l of g.adj.get(u)) {
        const v = other(l, u);
        if (seen.has(v) || !usable(g, l, opts) || !nodeOk(g, v, opts)) continue;
        seen.add(v); stack.push(v);
      }
    }
    return seen;
  }
  // flows(g, [{from, to, mbps}], {by:'hops', skip, avoid}): route each demand by path and add up the load.
  // Returns {routes: [ids|null], load: {key: mbps}, util: {key: load / link.mbps}, nodeLoad: {id: mbps}, unrouted: [i]}.
  // A link's key is net.key(a, b). nodeLoad counts traffic passing through a node (both ends included).
  function flows(g, demands, opts = {}) {
    const o = Object.assign({by: 'hops'}, opts), load = {}, util = {}, nodeLoad = {}, routes = [], unrouted = [];
    demands.forEach((d, i) => {
      const p = path(g, d.from, d.to, o); routes.push(p);
      if (!p) { unrouted.push(i); return; }
      for (const id of p) nodeLoad[id] = (nodeLoad[id] || 0) + (+d.mbps || 0);
      for (let j = 1; j < p.length; j++) { const k = key(p[j - 1], p[j]); load[k] = (load[k] || 0) + (+d.mbps || 0); }
    });
    for (const k in load) { const l = g.byKey.get(k); util[k] = l && l.mbps ? load[k] / l.mbps : null; }
    return {routes, load, util, nodeLoad, unrouted};
  }
  // around(g, id): neighbor ids ordered by the link's angle from the node, measured from straight up, clockwise
  // (design units, y down). Used to turn a router's arrow "to the next link clockwise".
  function around(g, id) {
    const n = g.byId.get(id);
    const ang = m => { const a = Math.atan2(m.x - n.x, -(m.y - n.y)); return a < -EPS ? a + 2 * Math.PI : Math.max(0, a); };
    return g.adj.get(id).map(l => g.byId.get(other(l, id))).sort((p, q) => ang(p) - ang(q) || g.index.get(p.id) - g.index.get(q.id)).map(m => m.id);
  }

  // split(text, n, {src, dst, ttl}): cut a message by words into n numbered pieces (fewer if it has fewer words);
  // earlier pieces take the extra words. Each piece is {seq, of, src, dst, data, ttl}.
  function split(text, n, opts = {}) {
    const words = String(text).trim().split(/\s+/).filter(Boolean);
    const k = Math.max(0, Math.min(n, words.length)), out = [];
    if (!k) return out;
    const base = Math.floor(words.length / k), extra = words.length % k;
    let i = 0;
    for (let s = 1; s <= k; s++) {
      const take = base + (s <= extra ? 1 : 0);
      out.push({seq: s, of: k, src: opts.src, dst: opts.dst, data: words.slice(i, i + take).join(' '), ttl: opts.ttl || 8});
      i += take;
    }
    return out;
  }
  // join(list): put pieces back in seq order. Returns {text, missing:[seq...]}; a gap reads "___".
  function join(list) {
    const by = new Map();
    let of = 0;
    for (const p of list || []) { if (!p) continue; by.set(p.seq, p); of = Math.max(of, p.of || 0, p.seq); }
    const parts = [], missing = [];
    for (let s = 1; s <= of; s++) { if (by.has(s)) parts.push(by.get(s).data); else { parts.push('___'); missing.push(s); } }
    return {text: parts.join(' '), missing};
  }
  // step(g, table, pkt): move a packet one hop by a forwarding table (table[node] = neighbor id). Takes one from
  // pkt.ttl (default 8) and updates pkt.at. Returns {at, dropped: 'ttl'|'down'|null, arrived, waiting, next}:
  // waiting when the table has no entry for this node (the packet stays), 'down' when the next node or link is down
  // or missing (the packet stays at `at`), 'ttl' when the count runs out before the destination.
  function step(g, table, pkt) {
    const at = pkt.at;
    if (at === pkt.dst) return {at, dropped: null, arrived: true};
    const next = table[at];
    if (next == null) return {at, dropped: null, waiting: true};
    const l = g.link(at, next), n = g.byId.get(next);
    if (!l || !l.up || !n || !n.up) return {at, dropped: 'down', next};
    pkt.ttl = (pkt.ttl == null ? 8 : pkt.ttl) - 1; pkt.at = next;
    if (pkt.ttl <= 0 && next !== pkt.dst) return {at: next, dropped: 'ttl', next};
    return {at: next, dropped: null, arrived: next === pkt.dst, next};
  }

  const pure = {KINDS, DEVICES, key, graph, addNode, addLink, removeNode, removeLink, path, cost, reach, flows, around, split, join, step};
  if (typeof document === 'undefined') return pure;   // Node or a worker: the pure part only

  // ==================================================================================================================
  // DOM PART: draw (the map), icons, tokens and the mover.
  // ==================================================================================================================
  const NS = 'http://www.w3.org/2000/svg';
  const mk = (tag, attrs = {}, parent) => {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  };
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const calm = () => typeof Curio !== 'undefined' ? Curio.reduce : matchMedia('(prefers-reduced-motion: reduce)').matches;
  let styled = false;
  function style() {
    if (styled) return; styled = true;
    const s = document.createElement('style');
    s.textContent = `
.net-node{outline:none}
.net-node.pick{cursor:pointer}
.net-node .net-focus{fill:none;stroke:transparent;stroke-width:4}
.net-node:focus-visible .net-focus{stroke:var(--focus,#c2410c)}
.net-node.pick:hover .net-tile{filter:brightness(1.06)}
.net-label{font-weight:600;pointer-events:none}
.net-token.pick{cursor:pointer;outline:none}
.net-token.pick:focus-visible .net-token-hit{fill:none;stroke:var(--focus,#c2410c);stroke-width:4}
.net-link-hit{stroke:transparent;fill:none;cursor:pointer}
.net-link-g{outline:none}
.net-link-g:focus-visible .net-link-hit{stroke:var(--focus,#c2410c);stroke-opacity:.6}
.net-token{cursor:pointer}
.net-token text{pointer-events:none}`;
    document.head.appendChild(s);
  }

  // icons: one per kind, drawn in a 48 x 48 box with an ink stroke (no fills that fight the tile)
  const IC = {
    laptop: '<rect x="11" y="11" width="26" height="18" rx="2"/><path d="M6 35h36l-3-5H9z"/>',
    tablet: '<rect x="13" y="7" width="22" height="34" rx="4"/><circle cx="24" cy="36" r="1.6" class="f"/><path d="M17 12h14v19H17z" stroke-width="1.6"/>',
    phone: '<rect x="16" y="6" width="16" height="36" rx="4"/><path d="M21 10h6" /><circle cx="24" cy="37" r="1.5" class="f"/>',
    desktop: '<rect x="7" y="9" width="34" height="22" rx="2"/><path d="M20 31l-2 7h12l-2-7M15 39h18"/>',
    printer: '<path d="M14 18V8h20v10"/><rect x="7" y="18" width="34" height="14" rx="3"/><path d="M14 28h20v12H14z"/><circle cx="35" cy="23" r="1.6" class="f"/>',
    camera: '<path d="M8 14l26-4 3 11-26 4z"/><path d="M37 15l5-1 1 6-5 1M20 24l2 9M14 35h14"/><circle cx="13" cy="17" r="1.6" class="f"/>',
    tv: '<rect x="5" y="9" width="38" height="25" rx="3"/><path d="M15 40l4-6M33 40l-4-6M12 40h24"/>',
    'wifi-router': '<rect x="7" y="27" width="34" height="11" rx="3"/><path d="M14 27V15M34 27V15"/><circle cx="14" cy="33" r="1.6" class="f"/><circle cx="20" cy="33" r="1.6" class="f"/><path d="M19 17a8 8 0 0 1 10 0M16 13a13 13 0 0 1 16 0" stroke-width="2"/>',
    'access-point': '<ellipse cx="24" cy="33" rx="16" ry="6"/><path d="M8 33v3c0 3 7 6 16 6s16-3 16-6v-3"/><path d="M18 22a9 9 0 0 1 12 0M14 17a15 15 0 0 1 20 0" stroke-width="2"/>',
    switch: '<rect x="5" y="16" width="38" height="16" rx="3"/><path d="M10 22h4v5h-4zM17 22h4v5h-4zM24 22h4v5h-4zM31 22h4v5h-4z" stroke-width="1.6"/>',
    'core-switch': '<rect x="5" y="9" width="38" height="13" rx="3"/><rect x="5" y="26" width="38" height="13" rx="3"/><path d="M10 14h4v4h-4zM17 14h4v4h-4zM24 14h4v4h-4zM10 31h4v4h-4zM17 31h4v4h-4zM24 31h4v4h-4z" stroke-width="1.4"/><path d="M34 15.5h4M34 32.5h4"/>',
    router: '<ellipse cx="24" cy="18" rx="17" ry="7"/><path d="M7 18v11c0 4 8 7 17 7s17-3 17-7V18"/><path d="M14 18h7m0 0l-3-2.5M21 18l-3 2.5M34 18h-7m0 0l3-2.5M27 18l3 2.5" stroke-width="1.8"/>',
    firewall: '<rect x="6" y="10" width="36" height="28" rx="2"/><path d="M6 19.3h36M6 28.6h36M18 10v9.3M30 10v9.3M12 19.3v9.3M24 19.3v9.3M36 19.3v9.3M18 28.6V38M30 28.6V38" stroke-width="1.8"/>',
    modem: '<path d="M7 30l4-14h26l4 14z"/><rect x="7" y="30" width="34" height="6" rx="2"/><circle cx="16" cy="24" r="1.6" class="f"/><circle cx="22" cy="24" r="1.6" class="f"/><circle cx="28" cy="24" r="1.6" class="f"/>',
    isp: '<path d="M10 42V18h18v24M28 42V26h11v16M6 42h37"/><path d="M14 23h3M21 23h3M14 29h3M21 29h3M14 35h3M21 35h3M32 31h3M32 36h3" stroke-width="2"/><path d="M19 18V8M14 10a7 7 0 0 1 10 0" stroke-width="2"/>',
    server: '<rect x="11" y="5" width="26" height="38" rx="3"/><path d="M11 17h26M11 29h26"/><circle cx="31" cy="11" r="1.6" class="f"/><circle cx="31" cy="23" r="1.6" class="f"/><circle cx="31" cy="35" r="1.6" class="f"/><path d="M16 11h8M16 23h8M16 35h8" stroke-width="2"/>',
    cloud: '<path d="M14 36h22a8 8 0 0 0 1-16 11 11 0 0 0-21-3 9 9 0 0 0-2 19z"/>',
  };
  // icon(kind, size, color): a standalone <svg> string, for panels and cards outside the map
  function icon(kind, size = 48, color = 'currentColor') {
    return `<svg viewBox="0 0 48 48" width="${size}" height="${size}" aria-hidden="true" fill="none" stroke="${color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><style>.f{fill:${color};stroke:none}</style>${IC[kind] || IC.cloud}</svg>`;
  }
  const iconInto = (parent, kind, size, color) => {
    const s = size / 48, gi = mk('g', {transform: `translate(${-size / 2},${-size / 2}) scale(${s})`, fill: 'none', stroke: color,
      'stroke-width': 2.6, 'stroke-linecap': 'round', 'stroke-linejoin': 'round'}, parent);
    gi.innerHTML = (IC[kind] || IC.cloud).replace(/class="f"/g, `fill="${color}" stroke="none"`);
    return gi;
  };

  const SKIN = {
    units: [1000, 600], icon: 48, tile: 'round', label: 'below', labelSize: 14, labelWidth: 110, labelLines: 3, labelGap: 4,
    font: "'Segoe UI',system-ui,sans-serif",
    colors: {tile: '#ffffff', tileLine: '#2b2b2b', ink: '#2b2b2b', label: '#2b2b2b', labelHalo: null, wire: '#8a8a8a',
      fiber: '#e0a400', fiberCore: '#fff6d6', wifi: '#8a8a8a', down: '#9b9b9b', downTile: '#d9d9d9', bad: '#b3261e',
      badText: '#ffffff', linkLabel: '#2b2b2b'},
    pickable: true, linkHit: 16,
  };

  // draw(svg, g, skin): draw the map into an <svg> (or a <g> inside one). Design units map into skin.box
  // ({x, y, w, h} in px; default the whole svg) separately in x and y, so spacing scales and icons and labels keep
  // their pixel size. Returns a view: {root, layers, pos(id), linkPoints(l), nodeEl(id), linkEl(a, b), update(),
  // badge(id, b), ring(ids, opts), setPickable(on), focus(id), labelBox(id)}.
  function draw(svg, g, skinIn = {}) {
    style();
    const skin = Object.assign({}, SKIN, skinIn, {colors: Object.assign({}, SKIN.colors, skinIn.colors || {})});
    const host = svg.ownerSVGElement || svg;
    const prev = svg.__net;   // the last view drawn here: tokens still moving are carried over to the new one
    if (prev && prev.root.parentNode) prev.root.remove();
    const C = skin.colors, [UW, UH] = skin.units;
    const box = skin.box || {x: 0, y: 0, w: +host.getAttribute('width') || host.clientWidth || UW, h: +host.getAttribute('height') || host.clientHeight || UH};
    const px = n => ({x: box.x + n.x / UW * box.w, y: box.y + n.y / UH * box.h});
    const root = mk('g', {class: 'net-map'}, svg);
    const layers = {};
    for (const k of ['back', 'links', 'marks', 'nodes', 'under', 'tokens', 'over']) layers[k] = mk('g', {class: 'net-' + k}, root);
    const nodeEls = new Map(), linkEls = new Map(), badgeEls = new Map();
    const S = skin.icon, R = S / 2 + 8;   // tile half size

    function linkPoints(l, from) {
      const a = g.node(l.a), b = g.node(l.b);
      const pts = [px(a), ...(l.via || []).map(([x, y]) => px({x, y})), px(b)].map(p => [p.x, p.y]);
      return from && from === l.b ? pts.reverse() : pts;
    }
    const d = pts => 'M' + pts.map(p => p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join('L');
    function drawLink(l) {
      const old = linkEls.get(key(l.a, l.b));
      const gEl = mk('g', {class: 'net-link-g', 'data-a': l.a, 'data-b': l.b});
      if (old && old.parentNode === layers.links) old.replaceWith(gEl); else { if (old) old.remove(); layers.links.appendChild(gEl); }
      if (g.node(l.a).hidden || g.node(l.b).hidden) gEl.style.display = 'none';   // a hidden node hides its links too
      const pts = linkPoints(l), path = d(pts), down = !l.up;
      const col = down ? C.down : l.medium === 'fiber' ? C.fiber : l.medium === 'wifi' ? C.wifi : C.wire;
      if (l.medium === 'fiber') {
        mk('path', {d: path, fill: 'none', stroke: col, 'stroke-width': 5, 'stroke-linecap': 'round', 'stroke-dasharray': down ? '10 7' : null}, gEl);
        if (!down) mk('path', {d: path, fill: 'none', stroke: C.fiberCore, 'stroke-width': 1.5, 'stroke-linecap': 'round'}, gEl);
      } else if (l.medium === 'wifi') {
        mk('path', {d: path, fill: 'none', stroke: col, 'stroke-width': 3, 'stroke-dasharray': down ? '3 9' : '7 7', 'stroke-linecap': 'round'}, gEl);
        // three arcs at the radio end, facing along the link
        const radio = /wifi-router|access-point/.test(g.node(l.b).kind) && !/wifi-router|access-point/.test(g.node(l.a).kind) ? l.b : l.a;
        const p = linkPoints(l, radio), [x0, y0] = p[0], [x1, y1] = p[1], len = Math.hypot(x1 - x0, y1 - y0) || 1;
        const ux = (x1 - x0) / len, uy = (y1 - y0) / len, ang = Math.atan2(uy, ux);
        for (let i = 0; i < 3; i++) {
          const r = R + 4 + i * 7, sp = .55;
          const ax = x0 + Math.cos(ang - sp) * r, ay = y0 + Math.sin(ang - sp) * r, bx = x0 + Math.cos(ang + sp) * r, by = y0 + Math.sin(ang + sp) * r;
          mk('path', {d: `M${ax.toFixed(1)} ${ay.toFixed(1)}A${r} ${r} 0 0 1 ${bx.toFixed(1)} ${by.toFixed(1)}`, fill: 'none', stroke: col, 'stroke-width': 2.5, 'stroke-linecap': 'round'}, gEl);
        }
      } else {
        mk('path', {d: path, fill: 'none', stroke: col, 'stroke-width': 3, 'stroke-linecap': 'round', 'stroke-dasharray': down ? '10 7' : null}, gEl);
      }
      if (down) {   // a break mark: two short slashes across the middle
        const m = mid(pts), a = m.ang + Math.PI / 2;
        for (const off of [-4, 4]) {
          const cx = m.x + Math.cos(m.ang) * off, cy = m.y + Math.sin(m.ang) * off;
          mk('path', {d: `M${(cx - Math.cos(a) * 9).toFixed(1)} ${(cy - Math.sin(a) * 9).toFixed(1)}L${(cx + Math.cos(a) * 9).toFixed(1)} ${(cy + Math.sin(a) * 9).toFixed(1)}`,
            stroke: C.bad, 'stroke-width': 3, 'stroke-linecap': 'round'}, gEl);
        }
      }
      const txt = skin.linkLabel && skin.linkLabel(l);
      if (txt) {
        const m = mid(pts);
        const t = mk('text', {x: m.x, y: m.y - 8, 'text-anchor': 'middle', 'font-size': skin.linkLabelSize || 12, 'font-family': skin.font,
          fill: C.linkLabel, 'font-weight': 600, 'paint-order': 'stroke', stroke: C.linkHalo || 'none', 'stroke-width': C.linkHalo ? 4 : 0}, gEl);
        t.textContent = txt;
      }
      if (skin.onPickLink) {
        const hit = mk('path', {d: path, class: 'net-link-hit', 'stroke-width': skin.linkHit}, gEl);
        hit.addEventListener('click', e => skin.onPickLink(l, e));
        if (skin.linkFocus) {
          gEl.setAttribute('tabindex', 0); gEl.setAttribute('role', 'button');
          gEl.setAttribute('aria-label', skin.linkAria ? skin.linkAria(l) : `Link ${g.node(l.a).label} to ${g.node(l.b).label}`);
          gEl.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); skin.onPickLink(l, e); } });
        }
      }
      linkEls.set(key(l.a, l.b), gEl);
    }
    function mid(pts) {   // the point halfway along a polyline, with the direction there
      let L = 0; const seg = [];
      for (let i = 1; i < pts.length; i++) { const s = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); seg.push(s); L += s; }
      let h = L / 2;
      for (let i = 0; i < seg.length; i++) {
        if (h <= seg[i] || i === seg.length - 1) {
          const t = seg[i] ? h / seg[i] : 0, [x0, y0] = pts[i], [x1, y1] = pts[i + 1];
          return {x: x0 + (x1 - x0) * t, y: y0 + (y1 - y0) * t, ang: Math.atan2(y1 - y0, x1 - x0)};
        }
        h -= seg[i];
      }
      return {x: pts[0][0], y: pts[0][1], ang: 0};
    }
    // labels wrap by words to skin.labelWidth (a number or node => px), at most skin.labelLines lines
    function wrapInto(t, text, maxW, x, lines) {
      const words = String(text).split(/\s+/), size = +t.getAttribute('font-size');
      const out = []; let cur = '';
      const tmp = mk('tspan', {}, t);
      const w = s => { tmp.textContent = s; return tmp.getComputedTextLength ? tmp.getComputedTextLength() : s.length * size * .55; };
      for (const word of words) {
        const tryS = cur ? cur + ' ' + word : word;
        if (!cur || w(tryS) <= maxW) cur = tryS; else { out.push(cur); cur = word; }
      }
      if (cur) out.push(cur);
      tmp.remove();
      while (out.length > lines) { out[lines - 1] += ' ' + out.pop(); }
      out.forEach((s, i) => { const sp = mk('tspan', {x, dy: i ? size * 1.15 : 0}, t); sp.textContent = s; });
      return out.length;
    }
    function drawNode(n) {
      const old = nodeEls.get(n.id);
      const p = px(n), down = !n.up, hadFocus = !!(old && old.contains(document.activeElement));
      // a redrawn node takes the old one's place, so the tab order stays the order of g.nodes
      const gEl = mk('g', {class: 'net-node', 'data-id': n.id, transform: `translate(${p.x.toFixed(1)},${p.y.toFixed(1)})`});
      if (old && old.parentNode === layers.nodes) old.replaceWith(gEl); else { if (old) old.remove(); layers.nodes.appendChild(gEl); }
      if (n.hidden) gEl.style.display = 'none';
      if (n.faint) gEl.setAttribute('opacity', .35);
      const tileFill = down ? C.downTile : (n.fill || C.tile), ink = down ? C.down : C.ink;
      if (skin.tile === 'circle') mk('circle', {class: 'net-tile', r: R, fill: tileFill, stroke: down ? C.down : C.tileLine, 'stroke-width': 2.5}, gEl);
      else if (skin.tile !== 'none') mk('rect', {class: 'net-tile', x: -R, y: -R, width: 2 * R, height: 2 * R, rx: 14, fill: tileFill, stroke: down ? C.down : C.tileLine, 'stroke-width': 2}, gEl);
      if (skin.drawIcon) skin.drawIcon(gEl, n, {size: S, ink, down}); else iconInto(gEl, n.kind, S, ink);
      mk(skin.tile === 'circle' ? 'circle' : 'rect', skin.tile === 'circle' ? {class: 'net-focus', r: R + 5} : {class: 'net-focus', x: -R - 5, y: -R - 5, width: 2 * R + 10, height: 2 * R + 10, rx: 18}, gEl);
      const lab = typeof skin.label === 'function' ? skin.label(n) : skin.label;
      if (lab && lab !== 'none' && n.label) {
        const pos = typeof lab === 'object' ? lab : lab === 'above' ? {dx: 0, dy: -R - 4 - skin.labelGap, anchor: 'middle', up: true} :
          lab === 'right' ? {dx: R + 8, dy: 5, anchor: 'start'} : {dx: 0, dy: R + skin.labelSize + skin.labelGap, anchor: 'middle'};
        const t = mk('text', {class: 'net-label', x: pos.dx, y: pos.dy, 'text-anchor': pos.anchor || 'middle', 'font-size': skin.labelSize,
          'font-family': skin.font, fill: down ? (C.downLabel || C.down) : C.label}, gEl);
        if (C.labelHalo) { t.setAttribute('paint-order', 'stroke'); t.setAttribute('stroke', C.labelHalo); t.setAttribute('stroke-width', skin.labelHaloWidth || 4); t.setAttribute('stroke-linejoin', 'round'); }
        const lw = typeof skin.labelWidth === 'function' ? skin.labelWidth(n) : skin.labelWidth;
        const nl = wrapInto(t, n.label, lw, pos.dx, skin.labelLines);
        if (pos.up && nl > 1) t.setAttribute('y', pos.dy - (nl - 1) * skin.labelSize * 1.15);
      }
      if (down) badgeOn(gEl, {icon: 'x', fill: C.bad, ink: C.badText});
      const b = badgeEls.get(n.id); if (b) badgeOn(gEl, b);
      gEl.setAttribute('aria-label', skin.nodeAria ? skin.nodeAria(n) : n.label + (down ? ', down' : ''));
      setPick(gEl, n);
      nodeEls.set(n.id, gEl);
      if (hadFocus && gEl.getAttribute('tabindex') !== null) gEl.focus({preventScroll: true});   // a redraw keeps keyboard focus
    }
    function setPick(gEl, n) {
      const on = !!(view.pickable && skin.onPick && (!skin.canPick || skin.canPick(n)));
      gEl.classList.toggle('pick', on);
      if (on) { gEl.setAttribute('tabindex', 0); gEl.setAttribute('role', 'button'); }
      else { gEl.removeAttribute('tabindex'); gEl.setAttribute('role', 'img'); }
    }
    function badgeOn(gEl, b) {
      const old = gEl.querySelector(b.icon === 'x' ? '.net-x' : '.net-badge'); if (old) old.remove();
      if (!b) return;
      const text = b.text || '';
      const w = text ? Math.max(24, 10 + text.length * 8 + (b.icon && b.icon !== 'x' ? 16 : 0)) : 24;
      // side 'left' puts the badge on the tile's top left (it grows leftward), clear of a link leaving up and right
      const tx = b.side === 'left' ? -R + 26 - w : R - 2;
      const bg = mk('g', {class: b.icon === 'x' ? 'net-x' : 'net-badge', transform: `translate(${tx},${-R + 2})`}, gEl);
      mk('rect', {x: -12, y: -12, width: w, height: 24, rx: 12, fill: b.fill || C.bad, stroke: b.line || '#fff', 'stroke-width': 2}, bg);
      if (b.icon === 'x') mk('path', {d: 'M-5 -5L5 5M5 -5L-5 5', stroke: b.ink || '#fff', 'stroke-width': 3, 'stroke-linecap': 'round'}, bg);
      else if (b.icon === 'lock' || b.icon === 'open') {
        mk('rect', {x: -6, y: -2, width: 12, height: 9, rx: 2, fill: b.ink || '#fff'}, bg);
        mk('path', {d: b.icon === 'lock' ? 'M-3.5 -2v-3a3.5 3.5 0 0 1 7 0v3' : 'M-3.5 -2v-3a3.5 3.5 0 0 1 7 0', fill: 'none', stroke: b.ink || '#fff', 'stroke-width': 2}, bg);
      } else if (b.icon === 'check') mk('path', {d: 'M-6 0l4 4 8-8', fill: 'none', stroke: b.ink || '#fff', 'stroke-width': 3, 'stroke-linecap': 'round', 'stroke-linejoin': 'round'}, bg);
      if (text) {
        const t = mk('text', {x: b.icon && b.icon !== 'x' ? 8 : -12 + w / 2, y: 5, 'text-anchor': b.icon && b.icon !== 'x' ? 'start' : 'middle',
          'font-size': 13, 'font-weight': 700, 'font-family': skin.font, fill: b.ink || '#fff'}, bg);
        t.textContent = text;
      }
    }
    const view = {
      svg, g, skin, root, layers, box, pickable: skin.pickable, R,
      pos: id => px(g.node(id)),
      linkPoints, nodeEl: id => nodeEls.get(id), linkEl: (a, b) => linkEls.get(key(a, b)),
      // redraw every node and link from the graph (after up, hidden, faint or label changes)
      update() { for (const l of g.links) drawLink(l); for (const [k, el] of linkEls) if (!g.byKey.has(k)) { el.remove(); linkEls.delete(k); }
        for (const n of g.nodes) drawNode(n); for (const [id, el] of nodeEls) if (!g.byId.has(id)) { el.remove(); nodeEls.delete(id); } },
      // badge(id, {text, icon:'lock'|'open'|'check'|'x', fill, ink, line, side:'right'|'left'}) on the tile's top
      // right (or left); null removes it
      // (an unchanged badge is not redrawn)
      badge(id, b) {
        const was = badgeEls.get(id); if (JSON.stringify(was || null) === JSON.stringify(b || null)) return;
        if (b) badgeEls.set(id, b); else badgeEls.delete(id); const n = g.node(id); if (n) drawNode(n);
      },
      // ring(ids, {color, width}): a ring around these tiles (the current stop); ring(null) clears
      ring(ids, o = {}) {
        layers.marks.textContent = '';
        const col = o.color || C.ring || '#f2c14e', w = o.width || 4;
        for (const id of [].concat(ids || [])) {
          const p = px(g.node(id));
          if (skin.tile === 'circle') mk('circle', {class: 'net-ring', cx: p.x, cy: p.y, r: R + 9, fill: 'none', stroke: col, 'stroke-width': w}, layers.marks);
          else mk('rect', {class: 'net-ring', x: p.x - R - 9, y: p.y - R - 9, width: 2 * R + 18, height: 2 * R + 18, rx: 22, fill: 'none', stroke: col, 'stroke-width': w}, layers.marks);
        }
      },
      setPickable(on) { view.pickable = on; for (const n of g.nodes) { const el = nodeEls.get(n.id); if (el) setPick(el, n); } },
      focus(id) { const el = nodeEls.get(id); if (el && el.focus) el.focus({preventScroll: true}); },
      // labelBox(id): the node's label box in svg px ({x, y, width, height}), or null when it has no label
      labelBox(id) {
        const el = nodeEls.get(id), t = el && el.querySelector('.net-label'); if (!t || !t.getBBox) return null;
        const b = t.getBBox(), p = px(g.node(id));
        return {x: p.x + b.x, y: p.y + b.y, width: b.width, height: b.height};
      },
    };
    root.addEventListener('click', e => {
      const el = e.target.closest && e.target.closest('.net-node.pick'); if (!el) return;
      skin.onPick(g.node(el.dataset.id), e);
    });
    root.addEventListener('keydown', e => {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      const el = e.target.closest && e.target.closest('.net-node.pick'); if (!el) return;
      e.preventDefault(); skin.onPick(g.node(el.dataset.id), e);
    });
    view.update();
    if (prev) { for (const t of [...prev.layers.tokens.childNodes]) layers.tokens.appendChild(t); prev.movers && prev.movers.forEach(m => m.view = view); }
    view.movers = prev && prev.movers || new Set();
    view.gen = prev ? prev.gen : 0;
    svg.__net = view;
    return view;
  }
  const viewOf = s => s && s.layers ? s : s && s.__net;

  // token(svgOrView, kind, label, opts): a token element in the tokens layer. Kinds: 'envelope' (cream, a number),
  // 'numbered' (a square with a number), 'ping' (a dot). opts: {fill, ink, line, aria, onPick}. Position it with
  // place(token, x, y) or let send() move it. With onPick(token, event) the token is a button: a 48 px hit circle
  // that picks on press (pointerdown, so a moving token is easy to catch), focusable, Enter or Space picks.
  function token(sv, kind = 'envelope', label = '', o = {}) {
    const view = viewOf(sv);
    const t = mk('g', {class: 'net-token net-token-' + kind}, view.layers.tokens);
    const fill = o.fill || '#fff8e1', ink = o.ink || '#241b33', line = o.line || ink;
    if (kind === 'ping') mk('circle', {r: 7, fill: o.fill || '#2f7de1', stroke: '#fff', 'stroke-width': 2.5}, t);
    else if (kind === 'numbered') {
      mk('rect', {x: -13, y: -13, width: 26, height: 26, rx: 5, fill, stroke: line, 'stroke-width': 2}, t);
      const x = mk('text', {y: 5, 'text-anchor': 'middle', 'font-size': 14, 'font-weight': 800, fill: ink, 'font-family': "'Segoe UI',system-ui,sans-serif"}, t); x.textContent = label;
    } else {
      mk('rect', {x: -17, y: -12, width: 34, height: 24, rx: 3, fill, stroke: line, 'stroke-width': 2}, t);
      mk('path', {d: 'M-17 -11L0 2L17 -11', fill: 'none', stroke: line, 'stroke-width': 1.6, 'stroke-linejoin': 'round'}, t);
      const x = mk('text', {y: 9, 'text-anchor': 'middle', 'font-size': 12, 'font-weight': 800, fill: ink, 'font-family': "'Segoe UI',system-ui,sans-serif"}, t); x.textContent = label;
    }
    if (o.aria) { t.setAttribute('role', 'img'); t.setAttribute('aria-label', o.aria); }
    if (o.onPick) {
      mk('circle', {class: 'net-token-hit', r: 24, fill: 'transparent'}, t);
      t.classList.add('pick'); t.setAttribute('tabindex', 0); t.setAttribute('role', 'button');
      t.addEventListener('pointerdown', e => { e.stopPropagation(); e.preventDefault(); o.onPick(t, e); });
      t.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); o.onPick(t, e); } });
    }
    return t;
  }
  const place = (t, x, y) => { t.setAttribute('transform', `translate(${x.toFixed(1)},${y.toFixed(1)})`); t.__xy = [x, y]; };

  // send(svgOrView, g, pkt, hops, {speed, token, keep, onHop, onDown, onBounce, delay}): glide a token along each
  // link of hops (a list of node ids) for that link's ms / speed (speed 1 = the link's own time; 0.5 = twice as
  // slow). Resolves 'arrived'; 'dropped' when the next node or link is down, or goes down under it; 'bounced' with
  // onDown:'bounce' (the token reaches the down node, shakes and comes back: 2 x ms + 400 ms); 'stopped' by stop().
  // pkt.at is the last node reached. token: a kind ('envelope', 'numbered', 'ping') or an element to move.
  // Motion off: the token jumps hop to hop with the same timing (and does not shake).
  async function send(sv, g, pkt, hops, o = {}) {
    let view = viewOf(sv);
    const speed = o.speed || 1, gen = view.gen;
    const tok = o.token && o.token.nodeType ? o.token : token(view, o.token || 'envelope', String(pkt.seq == null ? '' : pkt.seq), o);
    if (o.keep) tok.__keep = true;   // stop() leaves it on the map
    pkt.token = tok;
    const mover = {view}; view.movers.add(mover);
    const live = () => (view = mover.view, view.gen === gen);
    const finish = r => { view.movers.delete(mover); if ((!o.keep || r === 'stopped') && tok.parentNode) tok.remove(); return r; };
    const at = id => { const p = view.pos(id); place(tok, p.x, p.y); };
    if (o.delay) { await wait(o.delay); if (!live()) return finish('stopped'); }
    at(hops[0]); pkt.at = hops[0];
    for (let i = 1; i < hops.length; i++) {
      const a = hops[i - 1], b = hops[i], l = g.link(a, b), nb = g.node(b);
      const ms = (l ? +l.ms || 500 : 500) / speed;
      const blocked = () => !l || !l.up || !nb || !nb.up;
      if (blocked()) {
        if (o.onDown !== 'bounce') { tok.classList.add('net-dropped'); return finish('dropped'); }
        if (o.onBounce) o.onBounce(b, pkt);
        const r = await glide(view, tok, l, a, 2 * ms + 400, true, () => !live(), mover);
        if (r === 'stopped') return finish('stopped');
        at(a); return finish('bounced');
      }
      const r = await glide(view, tok, l, a, ms, false, () => !live() ? 'stopped' : blocked() ? 'down' : null, mover);
      if (r === 'stopped') return finish('stopped');
      if (r === 'down') { tok.classList.add('net-dropped'); return finish('dropped'); }
      pkt.at = b; at(b);
      if (o.onHop) o.onHop(b, pkt);
    }
    return finish('arrived');
  }
  // move a token along one link (or toward a down node and back when bounce), frame by frame
  function glide(view0, tok, l, from, ms, bounce, check, mover) {
    return new Promise(res => {
      const t0 = performance.now(), still = calm();
      const pts = () => { const v = mover.view, p = v.linkPoints(l, from); return {p, R: v.R}; };
      const posAt = (p, f) => {   // the point at fraction f of the polyline
        let L = 0; const seg = [];
        for (let i = 1; i < p.length; i++) { const s = Math.hypot(p[i][0] - p[i - 1][0], p[i][1] - p[i - 1][1]); seg.push(s); L += s; }
        let h = f * L;
        for (let i = 0; i < seg.length; i++) {
          if (h <= seg[i] || i === seg.length - 1) { const t = seg[i] ? Math.min(1, h / seg[i]) : 0; return [p[i][0] + (p[i + 1][0] - p[i][0]) * t, p[i][1] + (p[i + 1][1] - p[i][1]) * t, L]; }
          h -= seg[i];
        }
        return [p[0][0], p[0][1], L];
      };
      let tm = 0, over = false;
      const done = v => { if (over) return; over = true; clearInterval(tm); res(v); };
      const tick = () => {
        if (over) return;
        const c = check(); if (c) { done(c === true ? 'stopped' : c); return; }
        const f = Math.min(1, (performance.now() - t0) / ms);
        if (!still) {
          const {p, R} = pts();
          if (!bounce) { const [x, y] = posAt(p, f); place(tok, x, y); }
          else {
            const [, , L] = posAt(p, 0), stopF = L > 0 ? Math.max(0, (L - R - 16) / L) : 1, go = (ms - 400) / 2;
            const el = performance.now() - t0;
            let ff, shake = 0;
            if (el < go) ff = stopF * (el / go);
            else if (el < go + 400) { ff = stopF; shake = Math.sin((el - go) / 400 * Math.PI * 6) * 5; }
            else ff = stopF * Math.max(0, 1 - (el - go - 400) / go);
            const [x, y] = posAt(p, ff); place(tok, x + shake, y);
          }
        }
        if (f >= 1) { done(null); return; }
        requestAnimationFrame(tick);
      };
      // rAF stops in a hidden tab; a timer keeps the timing honest there
      tm = setInterval(() => { if (document.hidden) tick(); }, 100);
      tick();
    });
  }
  // stop(svgOrView): every token moving on this map resolves 'stopped' and is removed (mode changes, resets)
  function stop(sv) { const v = viewOf(sv); if (!v) return; v.gen++; v.layers.tokens.querySelectorAll('.net-token').forEach(t => { if (!t.__keep) t.remove(); }); }

  return Object.assign({}, pure, {draw, icon, token, place, send, stop, ICONS: IC});
})();
