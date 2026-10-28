// Curio Class family engine: fact-check. A made-up web inside the page: sites with their own looks, a mock browser
// (tabs, back, a read-only address bar), the Wayfind search engine, Openpedia, image search, a site lookup, Trace
// (follow a citation to its source and see the passage), a notebook of findings and recorded calls with the seconds
// and tabs each pass took. Inlined by scripts/bundle_tool.py from a kit:fact-check script tag, after kit:curio.
// Spec and API: docs/families/fact-check.md. New features go here and into that doc in the same change.
//
// Every address must be a reserved name: ending .example, or example.org, example.com, example.net (and their
// subdomains) (RFC 2606, RFC 6761). The engine checks every address in the world on load and logs one console
// error for each other one, so no real site can slip into a lesson. Links never navigate the real window.
const FC = (() => {

  // =====================================================================================================
  // PURE: no DOM in this block. FC.pure (hostOf, isReserved, words, search, results, parseUrl) and, per
  // world, the lab state made by FC.create: search, imageSearch, lookup, resolve, locks, notebook, calls, timers.
  // =====================================================================================================
  const pure = (() => {
    const RESERVED = ['example.com', 'example.org', 'example.net'], ENDS = ['.example'];
    // the host part of a web address ("https://x.example/p?q" -> "x.example")
    function hostOf(u) {
      let s = String(u == null ? '' : u).trim().toLowerCase();
      s = s.replace(/^[a-z][a-z0-9+.-]*:\/\//, '');
      s = s.split(/[/?#\s]/)[0];
      if (s.includes('@')) s = s.slice(s.lastIndexOf('@') + 1);
      return s.replace(/:\d+$/, '').replace(/\.$/, '');
    }
    // a real top-level label just before the reserved ending ("brand.com.example") hides a real site's name
    const REAL_TLDS = ['com', 'org', 'net', 'edu', 'gov', 'mil', 'int', 'io', 'co', 'uk', 'us', 'ca', 'au', 'de', 'fr', 'jp',
      'info', 'biz', 'app', 'dev', 'ai', 'me', 'tv', 'gg', 'ly', 'xyz', 'online', 'site', 'shop', 'news'];
    function isReserved(u) {
      const h = hostOf(u);
      if (!h || !/^[a-z0-9.-]+$/.test(h) || h.includes('..')) return false;
      const end = RESERVED.find(d => h === d || h.endsWith('.' + d)) || ENDS.find(t => h.endsWith(t) && h.length > t.length);
      if (!end) return false;
      const rest = h === end ? [] : h.slice(0, h.length - end.length).replace(/^\.|\.$/g, '').split('.').filter(Boolean);
      return !(rest.length >= 2 && REAL_TLDS.includes(rest[rest.length - 1]));
    }
    // {host, path, query}: path starts with "/", query is an object of the ?a=b pairs
    function parseUrl(u) {
      const s = String(u || '').trim().replace(/^[a-z][a-z0-9+.-]*:\/\//i, '');
      const host = hostOf(u), rest = s.slice(s.indexOf('/') < 0 ? s.length : s.indexOf('/'));
      const [p, q = ''] = rest.split('?');
      const query = {};
      for (const kv of q.split('&').filter(Boolean)) { const [k, v = ''] = kv.split('='); query[decodeURIComponent(k)] = decodeURIComponent(v.replace(/\+/g, ' ')); }
      return {host, path: p || '/', query};
    }
    // search words: lowercase, a trailing 's dropped ("Park's" -> park) and other apostrophes removed, split on anything
    // not a letter or digit (so punctuation and hyphens split words), little words left out, then each word folded:
    // a number 0 to 12 becomes its word ("4" -> four), a plain plural becomes singular ("libraries" -> library,
    // "games" -> game; not after s, u or i: "class", "bus", "this" stay). Queries and index terms fold the same way,
    // so an index needs no plural twins.
    const LITTLE = new Set(['a', 'an', 'the', 'of', 'to', 'in', 'on', 'is', 'are', 'and', 'for']);
    const NUM = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'];
    const fold = w => /^\d+$/.test(w) ? (+w <= 12 ? NUM[+w] : w)
      : w.length > 4 && w.endsWith('ies') ? w.slice(0, -3) + 'y'
      : w.length > 3 && w.endsWith('s') && !/[sui]s$/.test(w) ? w.slice(0, -1) : w;
    const words = q => String(q == null ? '' : q).toLowerCase().replace(/['’]s\b/g, '').replace(/['’]/g, '').split(/[^a-z0-9]+/)
      .filter(w => w && !LITTLE.has(w)).map(fold);
    // index entries whose terms are all in the query, best overlap (most terms) first, then index order
    function search(index, q) {
      const ws = new Set(words(q));
      if (!ws.size) return [];
      return index.map((e, i) => ({e, i, t: e.terms.flatMap(words)})).filter(x => x.t.length && x.t.every(t => ws.has(t)))
        .sort((a, b) => b.t.length - a.t.length || a.i - b.i).map(x => x.e);
    }
    // the results of those entries in order, each address once
    function results(index, q) {
      const seen = new Set(), out = [];
      for (const e of search(index, q)) for (const r of e.results || []) if (!seen.has(r.url)) { seen.add(r.url); out.push(r); }
      return out;
    }

    // the lab for one world: everything a tool asks about it, and the student's notebook, calls and timers
    function lab(world, o = {}) {
      const W = {sites: [], people: [], posts: {}, images: {}, entries: [], index: [], ...world};
      const svc = {search: {name: 'Wayfind', domain: 'wayfind.example'}, wiki: {name: 'Openpedia', domain: 'openpedia.example'},
        lookup: {name: 'Site lookup', domain: 'sitelookup.example'}, ...(o.services || {})};
      const log = o.log || (() => {});
      // check(): every address in the world. Returns {bad, missing}: bad = not a reserved name (each also logged),
      // missing = a link or result that resolves to no page in the world
      function check() {
        const bad = new Set(), missing = new Set(), urls = [];
        const walk = (v, k) => {
          if (typeof v === 'string') { if (k === 'domain' || k === 'url' || k === 'href' || k === 'works' || /^https?:\/\//.test(v)) urls.push([v, k]); }
          else if (Array.isArray(v)) v.forEach(x => walk(x, k === 'works' ? 'works' : k));
          else if (v && typeof v === 'object') for (const [kk, vv] of Object.entries(v)) if (kk !== 'src') walk(vv, kk);
        };
        walk(W, ''); walk(svc, '');
        for (const [u, k] of urls) {
          if (!isReserved(u)) bad.add(u);
          else if (k !== 'domain' && !resolve(u)) missing.add(u);
        }
        for (const u of bad) log(u);
        return {bad: [...bad], missing: [...missing]};
      }
      const siteOf = host => W.sites.find(s => s.domain === host) || null;
      // resolve(url) -> {site, page, service} or null. Services: search (/, /search?q=, /images?id=), wiki (/wiki/<id>),
      // lookup (/?d=domain). A site page is found by its path ("/" is the first page when none says "/")
      function resolve(url) {
        const {host, path, query} = parseUrl(url);
        if (host === svc.search.domain) {
          if (path === '/images') return W.images[query.id] ? {service: 'imageSearch', id: query.id} : null;
          if (path === '/search') return {service: 'search', q: query.q || ''};
          return path === '/' ? {service: 'searchHome'} : null;
        }
        if (host === svc.wiki.domain) {
          const id = path.replace(/^\/wiki\//, '');
          const e = W.entries.find(x => x.id === id);
          return e ? {service: 'entry', entry: e} : null;
        }
        if (host === svc.lookup.domain) return {service: 'lookup', domain: query.d || ''};
        const site = siteOf(host);
        if (!site) return null;
        const page = (site.pages || []).find(p => p.path === path) || (path === '/' ? (site.pages || [])[0] : null);
        return page ? {site, page} : null;
      }
      const searchUrl = q => `https://${svc.search.domain}/search?q=${encodeURIComponent(q).replace(/%20/g, '+')}`;
      const imageUrl = id => `https://${svc.search.domain}/images?id=${encodeURIComponent(id)}`;
      const lookupUrl = d => `https://${svc.lookup.domain}/?d=${encodeURIComponent(hostOf(d))}`;
      const wikiUrl = id => `https://${svc.wiki.domain}/wiki/${id}`;
      // imageSearch(id): the image's copies, earliest first (as given); lookup(domain): {domain, registered, owner,
      // note} or null when the lab has no record
      const imageSearch = id => ((W.images[id] || {}).copies || []).slice();
      function lookup(d) {
        const s = siteOf(hostOf(d));
        return s && s.lookup ? {domain: s.domain, name: s.name, ...s.lookup} : null;
      }
      // title of the page at an address (for result lists and the tab strip)
      function titleOf(url) {
        const r = resolve(url); if (!r) return hostOf(url);
        if (r.page) return r.page.title || r.site.name;
        if (r.entry) return r.entry.title;
        return {search: svc.search.name, searchHome: svc.search.name, imageSearch: 'Image search', lookup: svc.lookup.name}[r.service] || hostOf(url);
      }

      // ---- locks: names the browser knows are newTab, search, image, lookup, leave (a link to another site) and
      // trace (a citation link, even one to the same site) ----
      const locks = new Set();
      const lock = names => { [].concat(names || []).forEach(n => locks.add(n)); };
      const unlock = names => { if (names == null) locks.clear(); else [].concat(names).forEach(n => locks.delete(n)); };
      const locked = n => locks.has(n);

      // ---- notebook: one card per finding (per group: a tool's specimen, ad or case) ----
      let group = null;
      const notes = [];
      function note(n) {
        if (!n || !n.id) return false;
        if (n.for && n.for !== group) return false;              // a finding that belongs to another specimen
        if (notes.some(x => x.id === n.id && x.group === group)) return false;
        notes.push({id: n.id, text: n.text, tag: n.tag || 'inside', from: n.from || null, group, at: Date.now()});
        return true;
      }
      const notesOf = (g = group) => notes.filter(x => x.group === g).reverse();   // newest first

      // ---- timers and tabs per (group, pass): visible time only ----
      const T = {};
      let cur = null, since = null, running = false, hidden = false;
      const now = () => (o.now ? o.now() : Date.now());
      const tk = (g, p) => g + '|' + p;
      const slot = k => T[k] || (T[k] = {ms: 0, tabs: 0});
      function settle() { if (cur && since != null) { slot(cur).ms += now() - since; } since = null; }
      function pause() { settle(); running = false; }
      function resume() { if (!cur) return; running = true; if (!hidden && since == null) since = now(); }
      function begin(g, pass) { pause(); group = g; cur = tk(g, pass); slot(cur); resume(); }
      function focus(g) { pause(); group = g; cur = null; }       // look at a group without timing it (a tested one)
      function setHidden(h) { if (h === hidden) return; if (h) { settle(); hidden = true; } else { hidden = false; if (running) since = now(); } }
      function countTab(n = 1) { if (cur) slot(cur).tabs += n; }
      function ms(g, p) { const k = tk(g, p); let m = (T[k] || {}).ms || 0; if (k === cur && since != null) m += now() - since; return m; }
      const seconds = (g, p) => Math.round(ms(g, p) / 1000);
      const tabs = (g, p) => (T[tk(g, p)] || {}).tabs || 0;

      // ---- calls ----
      const calls = [];
      function call(g, pass, verdict, extra = {}) {
        if (cur === tk(g, pass)) settle();
        const rec = {specimen: g, pass, verdict, seconds: seconds(g, pass), tabs: tabs(g, pass), at: Date.now(), ...extra};
        const i = calls.findIndex(c => c.specimen === g && c.pass === pass);
        if (i >= 0) calls[i] = rec; else calls.push(rec);
        if (cur === tk(g, pass) && running && !hidden) since = now();
        return rec;
      }
      const callOf = (g, pass) => calls.find(c => c.specimen === g && c.pass === pass) || null;
      // clear(g): that group's calls, notes and timers; clear(): everything
      function clear(g) {
        const hit = x => g == null || x === g;
        for (let i = calls.length; i--;) if (hit(calls[i].specimen)) calls.splice(i, 1);
        for (let i = notes.length; i--;) if (hit(notes[i].group)) notes.splice(i, 1);
        for (const k of Object.keys(T)) if (hit(k.split('|')[0])) { if (k === cur) since = running && !hidden ? now() : null; delete T[k]; }
      }
      const dump = () => { settle(); if (running && !hidden && cur) since = now(); return JSON.parse(JSON.stringify({calls, notes, T})); };
      function restore(d) {
        if (!d || typeof d !== 'object') return;
        calls.length = 0; notes.length = 0;
        (d.calls || []).forEach(c => c && c.specimen != null && calls.push(c));
        (d.notes || []).forEach(n => n && n.id && notes.push(n));
        for (const k of Object.keys(T)) delete T[k];
        Object.assign(T, d.T || {});
      }

      return {world: W, services: svc, check, resolve, siteOf, titleOf, searchUrl, imageUrl, lookupUrl, wikiUrl,
        search: q => search(W.index, q), results: q => results(W.index, q), imageSearch, lookup,
        lock, unlock, locked, get locks() { return [...locks]; },
        note, notes: notesOf, get allNotes() { return notes.slice(); }, get group() { return group; },
        begin, focus, pause, resume, setHidden, countTab, seconds, tabs, ms,
        call, callOf, get calls() { return calls.slice(); }, clear, dump, restore};
    }
    return {hostOf, isReserved, parseUrl, words, search, results, lab};
  })();
  // ================================ end of PURE ================================

  const h = (tag, attrs = {}, ...kids) => {
    const e = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (v == null || v === false) continue;
      if (k === 'class') e.className = v; else if (k === 'style' && typeof v === 'object') Object.assign(e.style, v);
      else if (k.startsWith('on') && typeof v === 'function') e.addEventListener(k.slice(2), v);
      else e.setAttribute(k, v === true ? '' : v);
    }
    const add = k => { if (k == null || k === false) return; if (Array.isArray(k)) k.forEach(add); else e.append(k.nodeType ? k : document.createTextNode(String(k))); };
    kids.forEach(add);
    return e;
  };
  const svg = (w, hgt, inner, cls) => { const s = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); s.setAttribute('viewBox', `0 0 ${w} ${hgt}`); s.setAttribute('width', w); s.setAttribute('height', hgt); s.setAttribute('aria-hidden', 'true'); if (cls) s.setAttribute('class', cls); s.innerHTML = inner; return s; };

  // ---- icons (drawn in code) ----
  const ICON = {
    lock: '<rect x="3" y="8" width="12" height="9" rx="2" fill="currentColor"/><path d="M6 8V6a3 3 0 0 1 6 0v2" fill="none" stroke="currentColor" stroke-width="2"/>',
    back: '<path d="M11 4 5 10l6 6" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
    search: '<circle cx="8" cy="8" r="5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="m12 12 5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
    who: '<circle cx="10" cy="6.5" r="3.6" fill="currentColor"/><path d="M3 18c.6-4 3.4-6 7-6s6.4 2 7 6z" fill="currentColor"/>',
    evidence: '<path d="M5 2h7l4 4v12H5z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 9h6M8 12.5h6M8 16h4" stroke="currentColor" stroke-width="1.8"/>',
    others: '<path d="M2 4h10v7H6l-3 3v-3H2z" fill="currentColor"/><path d="M9 9h9v7h-1v3l-3-3H9z" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    inside: '<rect x="2.5" y="3" width="15" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2.5 7h15" stroke="currentColor" stroke-width="2"/><circle cx="10" cy="12" r="2.2" fill="currentColor"/>',
    image: '<rect x="2" y="3" width="16" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="7" cy="8" r="1.8" fill="currentColor"/><path d="m3 15 5-4 3 2 3-3 4 4" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    close: '<path d="m5 5 8 8M13 5l-8 8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
  };
  function icon(name, size = 18) { const s = svg(20, 20, ICON[name] || '', 'fc-ico'); s.setAttribute('width', size); s.setAttribute('height', size); return s; }
  // a drawn logo: {shape: circle | square | shield | leaf | bubble | star | book | drop | bolt, color, text (initials)}
  function logo(l = {}, size = 34) {
    const c = l.color || '#555', t = (l.text || '').slice(0, 3);
    const shapes = {
      circle: `<circle cx="20" cy="20" r="18" fill="${c}"/>`,
      square: `<rect x="2" y="2" width="36" height="36" rx="7" fill="${c}"/>`,
      shield: `<path d="M20 2 36 8v12c0 9-7 15-16 18C11 35 4 29 4 20V8z" fill="${c}"/>`,
      leaf: `<path d="M4 34C4 14 16 4 36 4c0 20-10 32-32 30z" fill="${c}"/>`,
      bubble: `<path d="M4 6h32v22H16l-8 8v-8H4z" fill="${c}"/>`,
      star: `<path d="m20 2 5 12 13 1-10 8 3 13-11-7-11 7 3-13L2 15l13-1z" fill="${c}"/>`,
      book: `<path d="M3 7c6-3 11-3 17 1 6-4 11-4 17-1v26c-6-3-11-3-17 1-6-4-11-4-17-1z" fill="${c}"/>`,
      drop: `<path d="M20 2c8 11 14 18 14 25a14 14 0 0 1-28 0C6 20 12 13 20 2z" fill="${c}"/>`,
      bolt: `<rect x="2" y="2" width="36" height="36" rx="4" fill="${c}"/><path d="m23 5-12 17h8l-3 13 13-18h-8z" fill="#fff" opacity=".9"/>`,
    };
    const body = shapes[l.shape] || shapes.circle;
    const txt = t && l.shape !== 'bolt' ? `<text x="20" y="${l.shape === 'shield' ? 22 : 21}" text-anchor="middle" dominant-baseline="middle" font-family="Segoe UI,Arial,sans-serif" font-weight="800" font-size="${t.length > 2 ? 11 : 14}" fill="${l.ink || '#fff'}">${t.replace(/[<&]/g, '')}</text>` : '';
    const s = svg(40, 40, body + txt, 'fc-logo'); s.setAttribute('width', size); s.setAttribute('height', size); return s;
  }
  const avatar = (text, color, size = 40) => logo({shape: 'circle', color: color || '#64748b', text}, size);

  const FONTS = {
    sans: "'Segoe UI',system-ui,Arial,sans-serif", serif: "Georgia,'Times New Roman',serif", slab: "Rockwell,'Roboto Slab',Georgia,serif",
    comic: "'Comic Sans MS','Comic Neue','Segoe Print',cursive", mono: "ui-monospace,Consolas,monospace", round: "'Trebuchet MS','Segoe UI',sans-serif",
    condensed: "'Arial Narrow','Segoe UI',Arial,sans-serif", news: "'Times New Roman',Georgia,serif",
  };
  const fmt = n => typeof n === 'number' ? n.toLocaleString('en-US') : n;

  let cssDone = false;
  function css() {
    if (cssDone) return; cssDone = true;
    const s = document.createElement('style');
    s.textContent = `
.fc-browser{--fc-chrome:#e3e6ec;--fc-chrome2:#f4f5f8;--fc-cink:#1f2430;--fc-cmuted:#4b5263;--fc-cline:#c3c8d3;--fc-cfocus:var(--focus,#b45309);
  display:flex;flex-direction:column;min-height:0;height:100%;background:var(--fc-chrome);border:1px solid var(--fc-cline);border-radius:12px;overflow:hidden;color:var(--fc-cink);
  font-family:'Segoe UI',system-ui,Arial,sans-serif;box-shadow:0 6px 18px #0002}
.fc-browser button{font:inherit;color:inherit;cursor:pointer}
.fc-browser :focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:-3px}
.fc-ico{display:inline-block;vertical-align:-3px;flex:none}
.fc-tabs{display:flex;align-items:flex-end;gap:2px;padding:4px 6px 0;overflow-x:auto;overflow-y:hidden;scrollbar-width:thin;flex:none}
.fc-tab{display:flex;align-items:center;flex:0 1 190px;min-width:92px;height:44px;background:#d3d7df;border-radius:10px 10px 0 0;position:relative}
.fc-tab.on{background:var(--fc-chrome2)}
.fc-tab>.fc-tabb{all:unset;box-sizing:border-box;cursor:pointer;flex:1;min-width:0;height:44px;padding:0 6px 0 10px;display:flex;align-items:center;gap:6px;font-size:13.5px;font-weight:600;border-radius:10px 0 0 0}
.fc-tab>.fc-tabb span{overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
.fc-tab>.fc-tabb:focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:-3px}
.fc-tabx{all:unset;box-sizing:border-box;cursor:pointer;width:44px;min-width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:0 10px 0 0;color:var(--fc-cmuted)}
.fc-tabx:hover{color:var(--fc-cink);background:#0001}
.fc-tabx:focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:-3px}
.fc-tabn{display:inline-flex;align-items:center;justify-content:center;min-width:20px;height:20px;border-radius:5px;background:#6b7280;color:#fff;font-size:11.5px;font-weight:800;flex:none}
.fc-newtab{all:unset;box-sizing:border-box;cursor:pointer;flex:none;min-width:48px;height:44px;margin-left:2px;display:flex;align-items:center;justify-content:center;gap:4px;border-radius:10px 10px 0 0;font-size:24px;font-weight:600;line-height:1;padding:0 10px}
.fc-newtab:hover{background:#0000000f}
.fc-newtab:focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:-3px}
.fc-bar{display:flex;align-items:center;gap:6px;padding:6px 8px;background:var(--fc-chrome2);border-bottom:1px solid var(--fc-cline);flex:none;flex-wrap:wrap}
.fc-bar>button,.fc-imgbtn{border:1px solid var(--fc-cline);background:#fff;border-radius:999px;min-height:44px;min-width:44px;padding:0 12px;display:inline-flex;align-items:center;justify-content:center;gap:6px;font-size:14px;font-weight:600}
.fc-back{padding:0!important;width:44px}
.fc-back:disabled{opacity:.4;cursor:default}
.fc-addr{flex:1 1 160px;min-width:110px;min-height:40px;display:flex;align-items:center;gap:6px;background:#fff;border:1px solid var(--fc-cline);border-radius:999px;padding:0 14px;font:13.5px ui-monospace,Consolas,monospace;color:#2d3340;overflow:hidden;white-space:nowrap}
.fc-addr span{overflow:hidden;text-overflow:ellipsis}.fc-addr span.fc-host{flex:0 0 auto;max-width:100%;color:#11151f;font-weight:700}.fc-addr span.fc-path{flex:0 1 auto;min-width:0;margin-left:-6px;color:#5a6172}
.fc-sbox{flex:0 1 250px;min-width:200px;display:flex;align-items:center;gap:0;background:#fff;border:1px solid var(--fc-cline);border-radius:999px;padding-left:12px;min-height:46px;position:relative}
.fc-sbox input{all:unset;box-sizing:border-box;flex:1;min-width:0;height:44px;font-size:14px;padding:0 4px}
.fc-sbox button{all:unset;box-sizing:border-box;cursor:pointer;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:999px}
.fc-sbox:focus-within{outline:3px solid var(--fc-cfocus);outline-offset:1px}
.fc-sbox button:focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:-3px}
.fc-locked{position:relative;color:#5b6170!important;background:repeating-linear-gradient(135deg,#f1f2f5 0 6px,#e7e9ee 6px 12px)!important;border-style:dashed!important}
.fc-pad{display:inline-flex;align-items:center;gap:3px;font-size:11.5px;font-weight:800;background:#4b5263;color:#fff;border-radius:999px;padding:2px 7px 2px 5px;white-space:nowrap}
.fc-locked .fc-pad{margin-left:2px}
.fc-sbox.fc-locked input{color:#5b6170}
.fc-newtab.fc-locked{font-size:22px;border:2px dashed #9aa1af;border-bottom:0}
.fc-msg{background:#fff7d6;border-bottom:1px solid #e6d27c;color:#3d3200;padding:6px 12px;font-size:14px;flex:none}
.fc-page{flex:1;min-height:0;overflow:auto;background:#fff;position:relative;scroll-behavior:auto}
.fc-pg{--pg-bg:#fff;--pg-ink:#1d2330;--pg-muted:#5b6170;--pg-accent:#2456c5;--pg-band:#f3f4f6;--pg-band-ink:#1d2330;--pg-line:#e3e5ea;
  min-height:100%;background:var(--pg-bg);color:var(--pg-ink);font-size:16px;line-height:1.5}
.fc-pghead{display:flex;align-items:center;gap:10px;padding:10px 18px;background:var(--pg-band);color:var(--pg-band-ink);flex-wrap:wrap}
.fc-pghead b{font-size:19px;letter-spacing:.2px}
.fc-pghead small{display:block;font-size:12.5px;opacity:.85;font-weight:600}
.fc-nav{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
.fc-nav a{color:inherit}
.fc-body{max-width:760px;margin:0 auto;padding:14px 20px 28px}
.fc-pg a.fc-a{color:var(--pg-accent);text-decoration:underline;text-underline-offset:2px;cursor:pointer;border-radius:4px;padding:2px 2px;display:inline;min-height:auto}
.fc-nav a.fc-a{display:inline-flex;align-items:center;min-height:44px;padding:0 10px;text-decoration:none;font-weight:700;font-size:14.5px;color:inherit}
.fc-nav a.fc-a[aria-current="page"]{text-decoration:underline}
.fc-body a.fc-a{display:inline-block;box-sizing:border-box;min-height:44px;padding:10px 2px;margin:-10px 0}
.fc-pg a.fc-a:focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:1px}
.fc-pg a.fc-a.fc-locked{color:#5b6170;text-decoration-style:dashed;background:repeating-linear-gradient(135deg,#f1f2f5 0 6px,#e7e9ee 6px 12px)}
.fc-cite{font-size:.82em;vertical-align:1px;margin-left:2px}
.fc-browser .fc-pg h1{font:inherit;font-size:27px;font-weight:700;line-height:1.2;margin:6px 0 8px;white-space:normal;overflow:visible}
.fc-browser .fc-pg h2{font:inherit;font-size:20px;font-weight:700;line-height:1.25;margin:12px 0 6px;white-space:normal}
.fc-pg p{margin:8px 0}
.fc-byline{color:var(--pg-muted);font-size:14px;margin:4px 0 10px}
.fc-banner{display:inline-block;background:var(--pg-accent);color:#fff;font-weight:800;padding:3px 10px;border-radius:4px;font-size:13px;letter-spacing:.6px;text-transform:uppercase}
.fc-badge{display:inline-flex;align-items:center;gap:6px;border:2px solid var(--pg-accent);color:var(--pg-accent);border-radius:999px;padding:3px 12px;font-weight:800;font-size:14px}
.fc-ad{border:1px dashed var(--pg-muted);padding:8px 12px;margin:14px 0;font-size:14px;color:var(--pg-muted)}
.fc-ad b{display:block;color:var(--pg-ink);font-size:15px}
.fc-counter{display:inline-block;font:700 15px ui-monospace,Consolas,monospace;background:#111;color:#7CFC00;padding:2px 8px;border:2px inset #888;letter-spacing:2px}
.fc-quote{border-left:4px solid var(--pg-accent);padding:4px 12px;margin:10px 0;font-style:italic}
.fc-meta{font-size:13.5px;color:var(--pg-muted)}
.fc-fig{margin:10px 0;position:relative}
.fc-fig img{display:block;width:100%;max-width:520px;height:auto;aspect-ratio:4/3;object-fit:cover;border-radius:4px;background:#cfd5de}
.fc-fig.small img{max-width:300px}
.fc-fig figcaption{font-size:13px;color:var(--pg-muted);margin-top:4px}
.fc-imgwrap{position:relative;display:inline-block;max-width:520px;width:100%}
.fc-fig.small .fc-imgwrap{max-width:300px}
.fc-imgbtn{position:absolute;right:8px;top:8px;background:#fffffff0!important;color:#1f2430;box-shadow:0 2px 6px #0004;font-size:13.5px!important}
.fc-list{list-style:none;margin:8px 0;padding:0}
.fc-list li{padding:6px 0;border-bottom:1px solid var(--pg-line)}
.fc-list small{display:block;color:var(--pg-muted);font-size:13px}
.fc-table{border-collapse:collapse;margin:8px 0;font-size:14.5px}
.fc-table td,.fc-table th{border:1px solid var(--pg-line);padding:5px 10px;text-align:left;vertical-align:top}
.fc-card{border:1px solid var(--pg-line);border-radius:10px;padding:10px 14px;margin:10px 0;background:#ffffffc0}
.fc-tap{min-height:44px;box-sizing:border-box;cursor:pointer;border-radius:6px;outline:2px dotted transparent;outline-offset:2px;box-shadow:inset 0 -2px 0 color-mix(in srgb,var(--fc-note,var(--brand,#6d28d9)) 33%,transparent)}
.fc-tap.fc-tapi{display:inline-block;padding:10px 3px;margin:-6px 0;vertical-align:middle;line-height:1.5}
.fc-tap:hover{background:color-mix(in srgb,var(--fc-note,var(--brand,#6d28d9)) 7%,transparent)}
.fc-tap:focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:2px}
.fc-tap.fc-noted{box-shadow:inset 0 -2px 0 var(--fc-note,var(--brand,#6d28d9))}
.fc-noted-tag{display:inline-flex;align-items:center;gap:3px;margin-left:6px;font:700 11.5px 'Segoe UI',sans-serif;background:var(--fc-note,var(--brand,#6d28d9));color:#fff;border-radius:999px;padding:1px 7px;vertical-align:2px;font-style:normal;letter-spacing:0;text-transform:none}
.fc-pg mark{background:#fde68a;color:inherit;box-shadow:0 0 0 3px #fde68a;border-radius:2px}
.fc-notsay{background:#fee2e2;color:#7f1d1d;border:2px solid #b91c1c;border-radius:10px;padding:8px 12px;font-weight:700;margin:0 0 10px}
.fc-post{border:1px solid var(--pg-line);border-radius:14px;padding:12px 14px;background:#fff;margin:10px 0;max-width:560px}
.fc-post-h{display:flex;align-items:center;gap:10px}
.fc-post-h b{display:block}
.fc-post-h small{color:var(--pg-muted)}
.fc-post-t{font-size:17px;margin:8px 0}
.fc-post-f{display:flex;gap:16px;flex-wrap:wrap;color:var(--pg-muted);font-size:14px;margin-top:6px}
.fc-post.mini{padding:8px 12px}
.fc-post.mini .fc-post-t{font-size:15px;margin:4px 0}
/* services */
.fc-wf{--pg-accent:#1a5fb4;font-family:'Segoe UI',system-ui,sans-serif}
.fc-wf-logo{font:800 30px 'Trebuchet MS','Segoe UI',sans-serif;letter-spacing:-.5px;color:#1a5fb4}
.fc-wf-logo i{font-style:normal;color:#c2410c}
.fc-wf-form{display:flex;gap:6px;margin:10px 0;max-width:560px}
.fc-wf-form input{flex:1;min-width:0;min-height:46px;border:2px solid #9db4d6;border-radius:999px;padding:0 16px;font-size:16px}
.fc-wf-form input:focus-visible{outline:3px solid var(--fc-cfocus);outline-offset:1px}
.fc-wf-form button{min-height:46px;border:0;border-radius:999px;background:#1a5fb4;color:#fff;font-weight:700;padding:0 18px;font-size:15px}
.fc-chips{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0 12px}
.fc-chip{border:1px solid #9db4d6;background:#eef4fc;color:#123a6e;border-radius:999px;min-height:44px;padding:0 14px;font-size:14.5px;font-weight:600}
.fc-res{margin:0 0 14px}
.fc-res .fc-url{font:13px ui-monospace,Consolas,monospace;color:#2b6b2b}
.fc-res a.fc-a{font-size:18px;display:inline-block;padding:10px 0;margin:-6px 0;min-height:44px}
.fc-res p{margin:2px 0;color:#444}
.fc-none{background:#f4f6fa;border-radius:10px;padding:10px 14px}
.fc-copies{list-style:none;padding:0;margin:8px 0}
.fc-copies li{display:flex;gap:12px;align-items:center;border-bottom:1px solid #e5e7eb;padding:8px 0}
.fc-copies img{width:96px;height:72px;object-fit:cover;border-radius:4px;flex:none;background:#cfd5de}
.fc-copies b{display:block}
.fc-first{display:inline-block;background:#1a5fb4;color:#fff;font-size:12px;font-weight:800;border-radius:999px;padding:1px 8px;margin-right:6px}
.fc-lk{font-family:ui-monospace,Consolas,monospace}
.fc-lk table{border-collapse:collapse;margin:10px 0;font-size:15px}
.fc-lk td{border:1px solid #d1d5db;padding:6px 12px}
.fc-lk td:first-child{background:#f3f4f6;font-weight:700}
.fc-blank{display:flex;align-items:center;justify-content:center;height:100%;color:#5b6170;font-size:16px;padding:20px;text-align:center}
/* the notebook */
.fc-nb{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.fc-nb li{background:#fff;border:1px solid var(--line,#d9deea);border-left:5px solid var(--nb-c,var(--fc-note,var(--brand,#6d28d9)));border-radius:10px;padding:6px 10px;font-size:14px;line-height:1.35}
.fc-nb .fc-nbt{display:flex;align-items:center;gap:5px;font-weight:800;font-size:12.5px;color:var(--nb-c,var(--fc-note,var(--brand,#6d28d9)));margin-bottom:2px}
.fc-nb li.fc-new{animation:fcIn .5s ease-out 1}
@keyframes fcIn{from{background:#fef3c7}to{background:#fff}}
.fc-nb-empty{font-size:14px;color:var(--muted,#555);margin:0}
`;
    document.head.appendChild(s);
  }

  // the four notebook tags: what the word and icon say
  const TAGS = {
    inside: {word: 'Inside', icon: 'inside', color: 'var(--fc-note,var(--brand,#6d28d9))'},
    who: {word: "Who's behind it?", icon: 'who', color: '#1d4ed8'},
    evidence: {word: "What's the evidence?", icon: 'evidence', color: '#0f766e'},
    others: {word: 'What do other sources say?', icon: 'others', color: '#9a3412'},
  };

  // create(world, opts): the lab (pure state, above) plus the DOM parts: browser(el, opts) and notebook(el, opts)
  function create(world, opts = {}) {
    const fc = pure.lab(world, {...opts, log: u => console.error('fact-check: not a reserved address, left out of the lesson: ' + u)});
    const report = fc.check();
    fc.report = report;
    fc.safeDomain = u => { const ok = pure.isReserved(u); if (!ok) console.error('fact-check: not a reserved address: ' + u); return ok; };
    fc.isReserved = pure.isReserved;
    fc.hostOf = pure.hostOf;
    fc.words = pure.words;
    fc.tags = TAGS;
    if (typeof document !== 'undefined') document.addEventListener('visibilitychange', () => fc.setHidden(document.visibilityState === 'hidden'));

    // ---------------------------------------------------------------- browser
    fc.browser = function browser(root, bo = {}) {
      css();
      const maxTabs = bo.maxTabs || 8;
      const texts = {notSay: "This source doesn't say that.", noResults: 'No good results. Try other words.', tooMany: maxTabs + ' tabs is the most. Close a tab with its × first.',
        lookupBtn: 'Who runs this site?', imageBtn: 'Search this image', searchPh: 'Search ' + fc.services.search.name, blank: 'Nothing open yet.',
        notFound: 'This page is not part of the lab.', noLookup: 'No lookup record for this site in the lab. Search its name to see who is behind it.',
        noted: 'Noted', home: 'Search the made-up web', copies: 'Copies of this image, earliest first', first: 'Earliest', ...(bo.texts || {})};
      const art = bo.art || {};
      const lockLabel = bo.lockLabel || 'Locked';
      let S = {tabs: [], active: 0};
      let msgT = 0;
      const el = h('div', {class: 'fc-browser'});
      const tabsEl = h('div', {class: 'fc-tabs', role: 'tablist', 'aria-label': 'Browser tabs'});
      const plus = h('button', {class: 'fc-newtab', type: 'button', 'aria-label': 'New tab', title: 'New tab'}, '+');
      const backB = h('button', {class: 'fc-back', type: 'button', 'aria-label': 'Back', title: 'Back'}, icon('back', 20));
      const addr = h('div', {class: 'fc-addr', role: 'textbox', 'aria-readonly': 'true', 'aria-label': 'Address'}, h('span', {class: 'fc-host'}), h('span', {class: 'fc-path'}));
      const sIn = h('input', {type: 'search', 'aria-label': texts.searchPh, placeholder: texts.searchPh, autocomplete: 'off', enterkeyhint: 'search'});
      const sGo = h('button', {type: 'submit', 'aria-label': 'Search'}, icon('search', 18));
      const sForm = h('form', {class: 'fc-sbox', role: 'search'}, sIn, sGo);
      const lkB = h('button', {class: 'fc-lookup', type: 'button'}, icon('who', 16), h('span', {}, texts.lookupBtn));
      const bar = h('div', {class: 'fc-bar'}, backB, addr, sForm, lkB);
      const msg = h('div', {class: 'fc-msg', role: 'status', hidden: true});
      const pageEl = h('div', {class: 'fc-page', tabindex: '-1'});
      el.append(tabsEl, bar, msg, pageEl);
      root.append(el);

      const say = t => { msg.textContent = t; msg.hidden = false; clearTimeout(msgT); msgT = setTimeout(() => { msg.hidden = true; }, 6000); };
      const hideMsg = () => { msg.hidden = true; };
      const isLocked = n => fc.locked(n);
      function blocked(n, e) { if (!isLocked(n)) return false; if (e) e.preventDefault(); bo.onLocked && bo.onLocked(n); return true; }
      // a locked control stays visible, with a padlock and the label (for example "Pass 2")
      function paintLock(b, n) {
        const on = isLocked(n);
        b.classList.toggle('fc-locked', on);
        b.setAttribute('aria-disabled', on ? 'true' : 'false');
        const pad = b.querySelector(':scope > .fc-pad');
        if (on && !pad) b.append(h('span', {class: 'fc-pad'}, icon('lock', 11), lockLabel));
        if (!on && pad) pad.remove();
      }
      function paintLocks() {
        paintLock(plus, 'newTab'); paintLock(lkB, 'lookup'); paintLock(sForm, 'search');
        sIn.readOnly = isLocked('search');
        sIn.setAttribute('aria-disabled', isLocked('search') ? 'true' : 'false');
        sGo.setAttribute('aria-disabled', isLocked('search') ? 'true' : 'false');
        pageEl.querySelectorAll('.fc-imgbtn').forEach(b => paintLock(b, 'image'));
        pageEl.querySelectorAll('.fc-citea').forEach(b => paintLock(b, 'trace'));
      }

      const tab = () => S.tabs[S.active];
      const curUrl = () => { const t = tab(); return t ? t.hist[t.i].url : null; };
      // open(url, {newTab, hl, count}): in this tab (history grows) or a new one (counted for the timer's pass)
      function open(url, o = {}) {
        if (!fc.safeDomain(url)) return false;
        hideMsg();
        if (o.newTab || !S.tabs.length) {
          if (S.tabs.length >= maxTabs) { say(texts.tooMany); return false; }
          S.tabs.push({hist: [{url, hl: o.hl || null}], i: 0});
          S.active = S.tabs.length - 1;
          if (o.count !== false) fc.countTab();
        } else {
          const t = tab();
          t.hist = t.hist.slice(0, t.i + 1); t.hist.push({url, hl: o.hl || null}); t.i++;
        }
        render(true);
        return true;
      }
      function back() { const t = tab(); if (t && t.i > 0) { t.i--; hideMsg(); render(true); } }
      function close(i) {
        if (i <= 0 || i >= S.tabs.length) return;
        S.tabs.splice(i, 1);
        if (S.active >= i) S.active = Math.max(0, S.active - 1);
        hideMsg(); render(true, true);
      }
      function select(i) { if (i === S.active || !S.tabs[i]) return; S.active = i; hideMsg(); render(true, true); }
      function newTab(e) {
        if (blocked('newTab', e)) return;
        open(bo.home || `https://${fc.services.search.domain}/`, {newTab: true});
        const box = pageEl.querySelector('.fc-wf-form input'); if (box && bo.focusSearch !== false) box.focus({preventScroll: true});
      }
      function searchFor(q, sameTab) {
        q = String(q || '').trim(); if (!q) return;
        const u = fc.searchUrl(q), r = fc.resolve(curUrl() || '');
        if (sameTab || (r && (r.service === 'search' || r.service === 'searchHome'))) open(u); else open(u, {newTab: true});
      }
      plus.onclick = e => newTab(e);
      backB.onclick = () => back();
      sForm.onsubmit = e => { e.preventDefault(); if (blocked('search', e)) return; searchFor(sIn.value); sIn.value = ''; };
      sIn.addEventListener('pointerdown', e => { if (isLocked('search')) { e.preventDefault(); bo.onLocked && bo.onLocked('search'); } });
      sIn.addEventListener('keydown', e => { if (isLocked('search') && e.key.length === 1 || isLocked('search') && e.key === 'Enter') { e.preventDefault(); bo.onLocked && bo.onLocked('search'); } });
      sGo.addEventListener('click', e => { if (isLocked('search')) { e.preventDefault(); bo.onLocked && bo.onLocked('search'); } });
      lkB.onclick = e => { if (blocked('lookup', e)) return; const u = curUrl(); if (u) open(fc.lookupUrl(u), {newTab: true}); };

      // ---- tab strip: rebuilt, keeping focus on the same tab ----
      function drawTabs() {
        const f = document.activeElement, fi = f && f.dataset ? f.dataset.fcTab : null, fx = f && f.dataset ? f.dataset.fcX : null;
        tabsEl.replaceChildren();
        S.tabs.forEach((t, i) => {
          const title = fc.titleOf(t.hist[t.i].url);
          const b = h('button', {class: 'fc-tabb', type: 'button', role: 'tab', 'aria-selected': i === S.active ? 'true' : 'false', 'data-fc-tab': i, title},
            h('span', {class: 'fc-tabn'}, i + 1), h('span', {}, title));
          b.onclick = () => select(i);
          const wrap = h('div', {class: 'fc-tab' + (i === S.active ? ' on' : '')}, b);
          if (i > 0) { const x = h('button', {class: 'fc-tabx', type: 'button', 'aria-label': 'Close tab ' + (i + 1), title: 'Close tab', 'data-fc-x': i}, icon('close', 16)); x.onclick = () => close(i); wrap.append(x); }
          tabsEl.append(wrap);
        });
        tabsEl.append(plus);
        if (fi != null || fx != null) {
          const t = tabsEl.querySelector(fx != null ? `[data-fc-x="${fx}"]` : `[data-fc-tab="${fi}"]`) || tabsEl.querySelector(`[data-fc-tab="${S.active}"]`);
          if (t) t.focus({preventScroll: true});
        }
        const on = tabsEl.querySelector('.fc-tab.on'); if (on) { const r = on.offsetLeft - tabsEl.scrollLeft; if (r < 0 || r + on.offsetWidth > tabsEl.clientWidth) tabsEl.scrollLeft = on.offsetLeft - 8; }
      }

      // ---- one link: never a real href, so nothing can leave the page ----
      function link(text, href, o = {}) {
        const a = h('a', {class: 'fc-a', role: 'link', tabindex: '0', title: href, 'data-href': href}, text);
        if (o.cite) { a.classList.add('fc-citea'); a.append(h('span', {class: 'fc-cite', 'aria-hidden': 'true'}, '↗')); }
        const go = e => {
          e.preventDefault();
          const from = curUrl();
          if (o.cite && blocked('trace', null)) return;
          if (pure.hostOf(href) !== pure.hostOf(from) && blocked('leave', null)) return;
          if (o.newTab) open(href, {newTab: true, hl: o.cite || null}); else open(href, {hl: o.cite || null});
          bo.onLink && bo.onLink(href, o);
        };
        a.addEventListener('click', go);
        a.addEventListener('keydown', e => { if (e.key === 'Enter') go(e); });
        return a;
      }
      // a bit of text: a string, or parts [text, {link, href, cite}, {b: text}, {i: text}]
      function rich(x) {
        if (x == null) return '';
        if (typeof x === 'string') return x;
        if (Array.isArray(x)) return x.map(rich);
        if (x.link) return link(x.link, x.href, x);
        if (x.b) return h('b', {}, x.b);
        if (x.i) return h('i', {}, x.i);
        return String(x.text || '');
      }
      // a block or a part of one that carries a note: tap (or Enter) adds it when on: 'tap' (the default for inside
      // notes), otherwise it is added when the page is shown
      function noteOn(e, n, seen) {
        if (!n) return e;
        const tap = n.on ? n.on === 'tap' : (n.tag || 'inside') === 'inside';
        if (!tap) { seen.push(n); return e; }
        e.classList.add('fc-tap'); e.setAttribute('role', 'button'); e.setAttribute('tabindex', '0');
        if (/^(SPAN|SMALL|B|I|EM|STRONG)$/.test(e.tagName)) e.classList.add('fc-tapi');   // an inline part gets a 44 px box
        e.setAttribute('aria-label', (e.textContent || '').trim().slice(0, 120) + '. Add to notebook');
        const mark = () => { if (!e.classList.contains('fc-noted')) { e.classList.add('fc-noted'); e.append(h('span', {class: 'fc-noted-tag'}, '✓ ' + texts.noted)); } };
        if (fc.allNotes.some(x => x.id === n.id && x.group === fc.group)) mark();
        const act = ev => {
          if (ev.target.closest && ev.target.closest('a,button') && ev.target.closest('a,button') !== e) return;
          ev.preventDefault();
          const added = fc.note({...n, from: curUrl()});
          if (added || fc.allNotes.some(x => x.id === n.id && x.group === fc.group)) mark();
          bo.onNote && bo.onNote(n, added, true);
        };
        e.addEventListener('click', act);
        e.addEventListener('keydown', ev => { if (ev.key === 'Enter' || ev.key === ' ') act(ev); });
        return e;
      }
      function figure(b, seen) {
        const im = fc.world.images[b.image] || {};
        const src = art[b.image] || im.src || '';
        const img = h('img', {src, alt: b.alt || im.alt || '', loading: 'lazy'});
        const wrap = h('div', {class: 'fc-imgwrap'}, img);
        if (im.copies && b.search !== false) {
          const ib = h('button', {class: 'fc-imgbtn', type: 'button'}, icon('image', 16), h('span', {}, texts.imageBtn));
          ib.onclick = e => { if (blocked('image', e)) return; open(fc.imageUrl(b.image), {newTab: true}); };
          paintLock(ib, 'image');
          wrap.append(ib);
        }
        const f = h('figure', {class: 'fc-fig' + (b.small ? ' small' : '')}, wrap, b.caption ? h('figcaption', {}, b.caption) : null);
        return noteOn(f, b.note, seen);
      }
      function post(p, seen, mini) {
        const P = typeof p === 'string' ? fc.world.posts[p] : p;
        if (!P) return null;
        const n = P.notes || {};
        const part = (e, k) => noteOn(e, n[k], seen);
        return h('article', {class: 'fc-post' + (mini ? ' mini' : '')},
          h('div', {class: 'fc-post-h'}, avatar(P.initials || (P.handle || '?').replace(/^@/, '').slice(0, 2).toUpperCase(), P.color),
            h('div', {}, part(h('b', {}, P.name || P.handle), 'name'), part(h('small', {}, `${P.handle}${P.followers != null ? ' · ' + fmt(P.followers) + ' followers' : ''}`), 'followers'))),
          part(h('p', {class: 'fc-post-t'}, rich(P.text)), 'text'),
          P.image && !mini ? figure({image: P.image, note: n.image, alt: P.alt}, seen) : null,
          h('div', {class: 'fc-post-f'}, P.time ? h('span', {}, P.time) : null, P.shares != null ? part(h('span', {}, h('b', {}, fmt(P.shares)), ' shares'), 'shares') : null));
      }
      // one block of a page: {t, ...} with an optional note
      function block(b, seen) {
        const t = b.t || 'p';
        let e;
        if (t === 'h1') e = h('h1', {}, rich(b.text));
        else if (t === 'h2') e = h('h2', {}, rich(b.text));
        else if (t === 'p') e = h('p', {}, rich(b.text));
        else if (t === 'byline') e = h('p', {class: 'fc-byline'}, rich(b.text));
        else if (t === 'meta') e = h('p', {class: 'fc-meta'}, rich(b.text));
        else if (t === 'banner') e = h('p', {}, h('span', {class: 'fc-banner'}, b.text));
        else if (t === 'badge') e = h('p', {}, h('span', {class: 'fc-badge'}, b.icon === 'star' ? '★' : '✔', b.text));
        else if (t === 'ad') e = h('div', {class: 'fc-ad'}, h('small', {}, b.label || 'Advertisement'), h('b', {}, b.title || ''), b.text ? rich(b.text) : null);
        else if (t === 'counter') e = h('p', {}, b.label ? b.label + ' ' : '', h('span', {class: 'fc-counter'}, b.text));
        else if (t === 'quote') e = h('blockquote', {class: 'fc-quote'}, rich(b.text));
        else if (t === 'img') e = figure({...b, note: null}, seen);   // style, cls and the block's note are added below
        else if (t === 'post') { e = post(b.id, seen, b.mini); if (!e) return null; }
        else if (t === 'posts') e = h('div', {}, (b.ids || []).map(id => post(id, seen, true)));
        else if (t === 'profile') {
          e = h('div', {class: 'fc-post'}, h('div', {class: 'fc-post-h'}, avatar(b.initials || (b.handle || '?').replace(/^@/, '').slice(0, 2).toUpperCase(), b.color, 52),
            h('div', {}, h('b', {}, b.name || b.handle), h('small', {}, `${b.handle}${b.followers != null ? ' · ' + fmt(b.followers) + ' followers' : ''}`))),
          b.bio ? h('p', {}, rich(b.bio)) : null);
        }
        else if (t === 'list') e = h('ul', {class: 'fc-list'}, (b.items || []).map(it => h('li', {}, it.href ? link(it.text, it.href, it) : rich(it.text), it.sub ? h('small', {}, it.sub) : null)));
        else if (t === 'works') {
          const p = (fc.world.people || []).find(x => x.name === b.person);
          e = h('ul', {class: 'fc-list'}, ((p && p.works) || []).map(u => { const r = fc.resolve(u); return h('li', {}, link(fc.titleOf(u), u), r && r.page && r.page.date ? h('small', {}, r.page.date) : null); }));
        }
        else if (t === 'table') e = h('table', {class: 'fc-table'}, b.head ? h('tr', {}, b.head.map(c => h('th', {}, c))) : null, (b.rows || []).map(r => h('tr', {}, r.map(c => h('td', {}, rich(c))))));
        else if (t === 'card') e = h('div', {class: 'fc-card'}, b.title ? h('b', {}, b.title) : null, (b.lines || []).map(l => h('p', {}, rich(l))));
        else if (t === 'link') e = h('p', {}, link(b.text, b.href, b));
        else if (t === 'hr') e = h('hr', {style: 'border:0;border-top:1px solid var(--pg-line);margin:14px 0'});
        else { console.error('fact-check: unknown block ' + t); e = h('div'); }
        if (b.style) Object.assign(e.style, b.style);
        if (b.cls) e.classList.add(...b.cls.split(' '));
        return noteOn(e, b.note, seen);
      }
      function sitePage(site, page, seen) {
        const L = site.look || {};
        const pg = h('div', {class: 'fc-pg fc-k-' + (page.kind || 'article') + (L.cls ? ' ' + L.cls : '')});
        const set = (k, v) => v && pg.style.setProperty(k, v);
        set('--pg-bg', L.bg); set('--pg-ink', L.ink); set('--pg-muted', L.muted); set('--pg-accent', L.accent); set('--pg-band', L.band); set('--pg-band-ink', L.bandInk); set('--pg-line', L.line);
        pg.style.fontFamily = FONTS[L.font] || L.font || FONTS.sans;
        if (L.border) pg.style.border = L.border;
        const nav = (site.nav || []).map(n => { const a = link(n.text, `https://${site.domain}${n.path}`); if (n.path === page.path) a.setAttribute('aria-current', 'page'); return a; });
        pg.append(h('div', {class: 'fc-pghead', style: L.headStyle || null}, L.logo !== false ? logo(L.logo || {text: site.name.slice(0, 2)}, 36) : null,
          h('div', {}, h('b', {style: L.nameStyle || null}, site.name), L.tagline ? h('small', {}, L.tagline) : null), nav.length ? h('nav', {class: 'fc-nav', 'aria-label': site.name}, nav) : null));
        pg.append(h('div', {class: 'fc-body'}, (page.blocks || []).map(b => block(b, seen))));
        if (page.note) seen.push(page.note);
        return pg;
      }
      function chipsEl() {
        const list = bo.chips ? bo.chips() || [] : [];
        if (!list.length) return null;
        return h('div', {class: 'fc-chips', role: 'group', 'aria-label': 'Suggested searches'}, list.map(c => { const b = h('button', {class: 'fc-chip', type: 'button'}, c); b.onclick = () => searchFor(c, true); return b; }));
      }
      function wfForm(q) {
        const inp = h('input', {type: 'search', value: q || '', 'aria-label': texts.searchPh, placeholder: texts.searchPh, autocomplete: 'off'});
        const f = h('form', {class: 'fc-wf-form', role: 'search'}, inp, h('button', {type: 'submit'}, 'Search'));
        f.onsubmit = e => { e.preventDefault(); searchFor(inp.value, true); };
        return f;
      }
      const wfHead = () => h('div', {class: 'fc-wf-logo'}, fc.services.search.name.slice(0, -1), h('i', {}, fc.services.search.name.slice(-1)));
      function servicePage(r, seen) {
        const pg = h('div', {class: 'fc-pg fc-wf'}), body = h('div', {class: 'fc-body'});
        pg.append(body);
        if (r.service === 'searchHome') {
          body.append(wfHead(), h('p', {class: 'fc-meta'}, texts.home), wfForm(''), chipsEl());
        } else if (r.service === 'search') {
          const res = fc.results(r.q);
          body.append(wfHead(), wfForm(r.q), chipsEl());
          if (!res.length) body.append(h('p', {class: 'fc-none'}, bo.noResults || texts.noResults));
          else body.append(h('div', {}, res.map(x => h('div', {class: 'fc-res'}, h('div', {class: 'fc-url'}, pure.hostOf(x.url) + pure.parseUrl(x.url).path.replace(/\/$/, '')), link(x.title || fc.titleOf(x.url), x.url), x.snippet ? h('p', {}, x.snippet) : null))));
          for (const e of fc.search(r.q)) if (e.note) seen.push(e.note);
        } else if (r.service === 'imageSearch') {
          const im = fc.world.images[r.id], cps = fc.imageSearch(r.id);
          body.append(wfHead(), h('h2', {}, texts.copies),
            h('ul', {class: 'fc-copies'}, cps.map((c, i) => h('li', {}, h('img', {src: art[r.id] || im.src || '', alt: ''}),
              h('div', {}, h('b', {}, i === 0 ? h('span', {class: 'fc-first'}, texts.first) : null, c.label || fc.titleOf(c.url)), h('span', {class: 'fc-meta'}, c.date || ''), h('div', {}, link(pure.hostOf(c.url) + pure.parseUrl(c.url).path.replace(/\/$/, ''), c.url)))))));
          if (im.note) seen.push(im.note);
        } else if (r.service === 'lookup') {
          const L = fc.lookup(r.domain);
          pg.classList.add('fc-lk');
          body.append(h('h2', {}, fc.services.lookup.name), h('p', {class: 'fc-meta'}, 'Who registered a web address, and when.'));
          if (!L) body.append(h('p', {class: 'fc-none'}, r.domain + ': ' + texts.noLookup));
          else {
            body.append(h('table', {}, h('tr', {}, h('td', {}, 'Domain'), h('td', {}, L.domain)), h('tr', {}, h('td', {}, 'Registered'), h('td', {}, L.registered || 'unknown')),
              h('tr', {}, h('td', {}, 'Owner'), h('td', {}, L.owner === 'hidden' || !L.owner ? 'Hidden' : L.owner))));
            if (L.note) seen.push(L.note);
          }
        } else if (r.service === 'entry') {
          const e = r.entry;
          pg.classList.remove('fc-wf');
          pg.style.fontFamily = FONTS.serif;
          pg.style.setProperty('--pg-band', '#f6f6f6');
          pg.prepend(h('div', {class: 'fc-pghead', style: 'border-bottom:1px solid #ddd'}, logo({shape: 'book', color: '#4b5563', text: 'O'}, 34), h('div', {}, h('b', {}, fc.services.wiki.name), h('small', {}, 'The free made-up encyclopedia'))));
          body.append(h('h1', {style: 'font-weight:500;border-bottom:1px solid #ccc;padding-bottom:4px'}, e.title), ...[].concat(e.text).map(p => typeof p === 'object' && p.t ? block(p, seen) : h('p', {}, rich(p))));
          if (e.note) seen.push(e.note);
        }
        return pg;
      }
      // highlight the first place a passage appears; false when it isn't there
      function highlight(root, passage) {
        const want = String(passage).toLowerCase().replace(/\s+/g, ' ').trim();
        for (const b of root.querySelectorAll('p,li,h1,h2,td,blockquote,figcaption')) {
          const txt = (b.textContent || '').toLowerCase().replace(/\s+/g, ' ');
          const at = txt.indexOf(want);
          if (at < 0) continue;
          // walk the text nodes and wrap the range
          const tw = document.createTreeWalker(b, NodeFilter.SHOW_TEXT);
          let pos = 0, n, startN = null, startO = 0, endN = null, endO = 0;
          const raw = b.textContent, norm = []; // map normalized index -> raw index
          for (let i = 0, prevSp = false; i < raw.length; i++) { const sp = /\s/.test(raw[i]); if (sp && prevSp) continue; norm.push(i); prevSp = sp; }
          const rs = norm[at], re = norm[at + want.length - 1] + 1;
          while ((n = tw.nextNode())) {
            const len = n.nodeValue.length;
            if (startN == null && rs < pos + len) { startN = n; startO = rs - pos; }
            if (startN && re <= pos + len) { endN = n; endO = re - pos; break; }
            pos += len;
          }
          if (!startN || !endN) continue;
          const rg = document.createRange(); rg.setStart(startN, startO); rg.setEnd(endN, endO);
          const m = document.createElement('mark');
          try { m.append(rg.extractContents()); rg.insertNode(m); } catch { continue; }
          return m;
        }
        return null;
      }
      // render(nav, keepFocus): draw the active tab. A page's seen notes are added here, once each
      function render(nav, keepFocus) {
        drawTabs();
        const t = tab();
        const had = pageEl.contains(document.activeElement) && !keepFocus;
        pageEl.replaceChildren();
        if (!t) { addr.firstChild.textContent = ''; addr.lastChild.textContent = ''; backB.disabled = true; pageEl.append(h('div', {class: 'fc-blank'}, texts.blank)); paintLocks(); return; }
        const {url, hl} = t.hist[t.i];
        const u = pure.parseUrl(url);
        addr.firstChild.textContent = u.host; addr.lastChild.textContent = (u.path === '/' && !Object.keys(u.query).length ? '' : u.path) + (Object.keys(u.query).length ? '?' + Object.entries(u.query).map(([k, v]) => k + '=' + v).join('&') : '');
        addr.title = url;
        backB.disabled = t.i === 0;
        const r = fc.resolve(url), seen = [];
        let pg;
        if (!r) pg = h('div', {class: 'fc-blank'}, texts.notFound);
        else if (r.service) pg = servicePage(r, seen);
        else pg = sitePage(r.site, r.page, seen);
        pageEl.append(pg);
        if (hl) {
          const m = highlight(pg, hl);
          if (!m) { const body = pg.querySelector('.fc-body') || pg; body.prepend(h('p', {class: 'fc-notsay', role: 'status'}, texts.notSay)); }
          else requestAnimationFrame(() => { const pr = pageEl.getBoundingClientRect(), mr = m.getBoundingClientRect(); pageEl.scrollTop += mr.top - pr.top - 60; });
        }
        if (nav && !hl) pageEl.scrollTop = 0;
        const added = [];
        for (const n of seen) if (fc.note({...n, from: url})) added.push(n);
        paintLocks();
        if (had) pageEl.focus({preventScroll: true});
        bo.onOpen && bo.onOpen(url, r, added);
        if (added.length && bo.onNote) added.forEach(n => bo.onNote(n, true, false));
      }

      return {
        el, page: pageEl, open, back, close, select, newTab: () => newTab(null), search: q => searchFor(q),
        // use(session): show another session's tabs ({tabs, active}); the browser keeps working in that object
        use(s) { S = s || {tabs: [], active: 0}; S.tabs = S.tabs || []; S.active = S.active || 0; hideMsg(); render(false, true); return S; },
        get session() { return S; }, get url() { return curUrl(); }, get tabs() { return S.tabs.length; },
        render: () => render(false, true), paintLocks, message: say,
      };
    };

    // ---------------------------------------------------------------- notebook
    // notebook(el, {empty, group}): the cards of the current group, newest first; refresh() redraws, marking new ones
    fc.notebook = function notebook(root, no = {}) {
      css();
      const list = h('ul', {class: 'fc-nb', 'aria-live': 'polite'});
      const empty = h('p', {class: 'fc-nb-empty'}, no.empty || 'No notes yet.');
      root.append(empty, list);
      let shown = new Set();
      function refresh(fresh) {
        const ns = fc.notes(no.group ? no.group() : undefined);
        list.replaceChildren(...ns.map(n => {
          const T = TAGS[n.tag] || TAGS.inside, key = n.group + '|' + n.id;
          const li = h('li', {class: fresh !== false && !shown.has(key) && shown.size ? 'fc-new' : '', style: `--nb-c:${T.color}`},
            h('div', {class: 'fc-nbt'}, icon(T.icon, 15), T.word), h('div', {}, n.text));
          return li;
        }));
        empty.hidden = ns.length > 0;
        shown = new Set(fc.allNotes.map(n => n.group + '|' + n.id));
        return ns.length;
      }
      refresh(false);
      return {el: list, refresh, get count() { return fc.notes(no.group ? no.group() : undefined).length; }};
    };
    fc.icon = icon; fc.logo = logo; fc.h = h;
    return fc;
  }

  return {pure, create, TAGS, icon, logo, h, isReserved: pure.isReserved, hostOf: pure.hostOf};
})();
