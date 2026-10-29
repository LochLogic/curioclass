# Family: network

Four tools, grade 3 to 12 (computer science), share one network engine: `kit/network.js`, inlined with
`<script src="kit:network"></script>` after `kit:curio`. It defines one global, `Net`. internet-journey built it;
the full description is in tools/internet-journey/spec.md ("Family engine").

## What the engine does (shared)

A graph of devices and links, the routes packets take through it, the packets themselves, and an SVG map with
code-drawn icons and tokens that glide along the links. The pure part (no DOM) is one marked block at the top of the
file; tools expose it as `__tool.net` for tests.

```js
// Graph (pure). Design units 1000 x 600.
const g = Net.graph({nodes: [{id, kind, label, x, y, up: true}], links: [{a, b, medium: 'wire'|'wifi'|'fiber', ms, mbps, lenM, up: true, via: [[x, y]]}]});
g.node(id), g.link(a, b), g.byId, g.byKey, g.adj, g.index
Net.addNode(g, n), Net.addLink(g, l)      // one link per pair: a second addLink replaces it
Net.removeNode(g, id), Net.removeLink(g, a, b), Net.key(a, b)
Net.KINDS   // laptop tablet phone desktop printer camera tv | wifi-router access-point switch core-switch router
            // firewall modem isp server cloud   (Net.DEVICES = the first seven)

// Routes (pure)
Net.path(g, from, to, {by: 'ms'|'hops', skip(link), avoid(node)})  // ids or null; ties: fewer hops, then lower node index
Net.cost(g, ids, by), Net.reach(g, from, opts) -> Set
Net.flows(g, [{from, to, mbps}], {by}) -> {routes, load{key}, util{key}, nodeLoad{id}, unrouted}
Net.around(g, id)                         // neighbors clockwise from straight up

// Packets and forwarding (pure)
Net.split(text, n, {src, dst, ttl}) -> [{seq, of, src, dst, data, ttl}]     // by words
Net.join(list) -> {text, missing}                                         // gaps read "___"
Net.step(g, table, pkt) -> {at, next, dropped: 'ttl'|'down'|null, arrived, waiting}   // table[node] = neighbor

// Map (DOM)
const view = Net.draw(svg, g, skin)   // design units -> skin.box at real pixel size; icons and labels keep their px
view.pos(id), view.linkPoints(l, from), view.nodeEl(id), view.linkEl(a, b), view.update()
view.badge(id, {text, icon: 'lock'|'open'|'check'|'x', fill, ink, line, side: 'right'|'left'}), view.badge(id, null)
   // an unchanged badge is not redrawn; a redrawn node keeps its place in the tab order and keeps keyboard focus
view.ring(ids, {color, width})            // default color: colors.ring, else gold
view.setPickable(on), view.focus(id), view.layers {back, links, marks, nodes, under, tokens, over}   // rings sit under the tiles, so badges stay readable
view.labelBox(id) -> {x, y, width, height} in svg px, or null   // to keep overlays off a node's name
Net.icon(kind, size, color) -> '<svg ...>'   // for cards and panels

// Tokens and movement (DOM)
const t = Net.token(view, 'envelope'|'numbered'|'ping', label, {fill, ink, line, aria, onPick(t)}); Net.place(t, x, y)
   // onPick: the token gets a 48 px hit circle, a tab stop and role button; it picks on pointerdown (so a moving
   // token is easy to catch) and on Enter or Space
await Net.send(view, g, pkt, hops, {speed, token, keep, onHop, onDown: 'bounce', onBounce, delay})
   // -> 'arrived' | 'dropped' | 'bounced' | 'stopped'; each link takes its ms / speed; bounce = 2 x ms + 400
Net.stop(view)                            // stops movers, removes tokens not marked keep (send's keep: true marks one)
```

Skin options: `box, units, icon, tile ('round'|'circle'|'none'), label ('below'|'above'|'right'|'none'|{dx, dy, anchor}|fn(node) returning one of those),
labelSize, labelWidth, labelLines, labelGap, labelHaloWidth (default 4), font, colors {tile, tileLine, ink, label,
labelHalo, wire, fiber, fiberCore, wifi, down, downTile, downLabel (a down node's name; default: down), bad, badText,
linkLabel, linkHalo, ring}, pickable, onPick(node), canPick(node),
linkStyle(link) (optional, up links only: {color, width, dash}, each optional; down links keep colors.down),
onPickLink(link), linkFocus, linkAria, linkLabel(link), linkLabelSize, linkHit, nodeAria(node), drawIcon`. Per node:
`hidden` (its links hide too), `faint`, `fill`.

Fixed by the engine: the icon set (one drawn icon per kind), wire 3 px, fiber 5 px with a light core, Wi-Fi dashed
with three arcs at the radio end, a down link dashed with a break mark, a down node grey with an X badge, node
buttons that are focusable and fire `onPick`, tokens carried over when the map is redrawn (resize), and motion off:
tokens jump hop to hop with the same timing (Curio.reduce).

## Rules for siblings

- Graphs, routes, packets and the map come from the engine. A sibling brings its own scene and its own question.
- Draw at real pixel size: pass `skin.box` in px, keep labels 12 px or more at the 680x425 preview.
- Node tab order follows the order of `nodes`; give it the order a reader would follow.
- Made-up names, addresses and numbers only (phone numbers 555-0100 to 555-0199). No real brands on devices.
- New engine features go into the engine and this file in the same change, keeping existing calls working. Re-check
  internet-journey after any change to `draw` or `send`.

## Recipes

- **Guest network** (network-help-desk): mark the router's guest links `guest: true` in the tool's own graph data.
  The engine has no guest concept; for a home-device target pass `skip: l => l.guest` to `Net.path` and `Net.reach`
  (guest-to-cloud routes stay open). Style guest links with the skin's `linkStyle(link)` option (added for this tool),
  not by writing on the engine's link paths, and give down links a look of their own (`colors.down`) so a broken link never reads as Guest.

## What each tool brings (its own)

| Tool | Grade | Its one idea (not shared) | Engine parts |
|---|---|---|---|
| internet-journey | 3 | a party invite travels in 8 numbered pieces; one choice per stop; the board of where copies live | graph, draw, send (envelopes, bounce), split, join, path (Trip map) |
| network-help-desk | 4 | a home network appears only as you ask the right questions; sort the kind, then the cause | graph, draw, path, reach (guest skip), token and send ('ping'), stop, down nodes and links, badges |
| packet-race | 6-8 | you are the routing table: aim each router's arrow, re-aim when routers fail | graph, draw, step, send ('numbered'), split, join |
| network-architect | 9-12 | wire a high school, then run the tests a network team would | graph, draw, path, reach, flows (load, util) |
