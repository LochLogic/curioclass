# Family: fact-check

Three tools share one engine, `kit/fact-check.js`, inlined with `<script src="kit:fact-check"></script>` after
`kit:curio`. It gives one global, `FC`. fake-or-fact-lab (grades 6-8) built it first; fact-check-desk (ELA 8) and
ad-agency (grade 12) feed it their own worlds.

The engine is a made-up web inside the page: sites with their own looks, a mock browser (tabs, back, a read-only
address bar), the Wayfind search engine, Openpedia, image search, a site lookup, Trace (follow a citation to its
source and see the passage), a notebook of findings, and recorded calls with the seconds and tabs each pass took.

## The rule that binds every sibling

- **Every address is a reserved name**: a host ending `.example`, or `example.com`, `example.org`, `example.net`
  and their subdomains (RFC 2606, RFC 6761). A real top-level label just before the reserved ending
  (`brand.com.example`) fails too, so a real brand cannot hide inside a reserved name. `FC.create` checks every
  address in the world on load and logs one console error for each bad one, so a real site shows up as a failed
  console check. Every spec test includes `fc.safeDomain('evil.com') === false` and a clean console.
- **Links never navigate the real window.** Links are `<a role="link" data-href>` with no real `href`.
- **Everything is invented**: sites, people, studies, posts and photos. No real brands, no real living private
  people, nothing partisan. Logos are drawn shapes with made-up initials.
- **Web-search every display name before use**: each organization, outlet, school, app, handle and site name. Use it
  only when the search finds no real one and nothing that sounds close (a real "Fern Hollow" rules out "Fernhollow";
  a real app called "Smart Study" rules out a "Center for Smart Study"). Plainly invented compounds work best
  (Gloverly, Tweedlebeak, Glimmerlake). List the searches and their results in the tool's handoff.md.
- Nothing is sent anywhere. The search engine, lookup and encyclopedia are lookups into the tool's own world.

## Pure parts (no DOM): `FC.pure`

```js
FC.pure.hostOf(u)          // "https://x.example/p?q" -> "x.example" (also takes "a@b.example")
FC.pure.isReserved(u)      // true only for reserved names (above); never logs
FC.pure.parseUrl(u)        // {host, path ("/" when none), query: {k: v}}
FC.pure.words(q)           // search words: lowercase, a trailing 's dropped ("Park's" -> park), other apostrophes
                           //   removed, split on anything not a letter or digit (punctuation and hyphens split),
                           //   little words left out (a an the of to in on is are and for), then each word folded:
                           //   0 to 12 become words ("4" -> four), "-ies" -> "-y" ("libraries" -> library), a plain
                           //   final s dropped ("games" -> game; not after s, u, i: class, bus, this stay)
FC.pure.search(index, q)   // index entries whose terms are ALL in the query, most terms first, then index order.
                           //   Terms fold the same way as queries, so an index needs no plural or number twins
FC.pure.results(index, q)  // the results of those entries in order, each address once
FC.pure.lab(world, o)      // the lab state for one world, without the DOM (what FC.create builds on)
FC.isReserved, FC.hostOf   // the same two, at the top
```

## The world

A tool passes one object to `FC.create(world, opts)`:

```js
{
  sites: [{
    domain: 'zaplinenow.example', name: 'Zapline Now',
    look: {...},                         // below
    nav: [{text: 'Top stories', path: '/'}, {text: 'Authors', path: '/authors'}],
    pages: [{path: '/four-day-week', kind: 'article', title: 'Four-day week next fall', date: 'May 2, 2026',
             blocks: [...], note}],     // "/" falls back to the first page when no page says "/"
    lookup: {registered: '3 weeks ago', owner: 'hidden', note},   // owner: a name, or 'hidden'
  }],
  people: [{name: 'Marisol Vega', works: ['https://glimmerlaketribune.example/...']}],
  posts: {storm1: {handle: '@SquallnookAlerts', name, initials, color, followers: 12400, text, image: 'ff-shark-street',
                   alt, shares: 8900, time: '2h', notes: {name, followers, text, image, shares}}},
  images: {'ff-shark-street': {src, alt, copies: [{url, date, label}], note}},     // copies earliest first
  entries: [{id: 'Glimmerlake_Tribune', title, text: [string | rich parts | a block], note}],   // Openpedia
  index: [{terms: ['squallnook'], results: [{title, url, snippet}], note}],                // Wayfind
}
```

- **Site look** `look`: `{font, bg, ink, muted, accent, band, bandInk, line, border, logo, tagline, headStyle,
  nameStyle, cls}`. `font` is `sans`, `serif`, `slab`, `comic`, `mono`, `round`, `condensed`, `news` or any CSS
  font list. `logo` is `{shape, color, text, ink}` with shape `circle`, `square`, `shield`, `leaf`, `bubble`, `star`,
  `book`, `drop` or `bolt`, or `false` for none. `headStyle` and `nameStyle` are inline CSS for the site header and
  its name. `cls` adds classes to the page, for a tool's own page styles (ad-agency's billboard). Give siblings in one
  tool different looks, so pages differ from each other and from the tool's chrome.
- **Page kind** `kind` (`article`, `about`, `post`, `profile`, `entry`, `document`, or any word) becomes the class
  `fc-k-<kind>`. It changes nothing else; it is for a tool's CSS.
- **Blocks** `{t, ...}` (each may carry `note`, `style` (inline CSS object) and `cls`; `img` and `post` take all
  three too):

| t | fields |
|---|---|
| `h1`, `h2`, `p` | `text` (rich) |
| `byline`, `meta` | `text` (rich), smaller and muted |
| `banner` | `text`: a bold strip such as "BREAKING" |
| `badge` | `text`, `icon: 'star'` (else a check): a trust badge the site gives itself |
| `ad` | `label` ("Advertisement"), `title`, `text` (rich) |
| `counter` | `label`, `text`: a big number ("8,900 shares") |
| `quote` | `text` (rich) |
| `img` | `image` (an images key), `caption`, `alt`, `small`, `search: false` (no Search this image button) |
| `post` | `id` (a posts key), `mini` (no photo) |
| `posts` | `ids`: a feed of mini posts |
| `profile` | `handle, name, initials, color, followers, bio` (rich) |
| `list` | `items: [{text, href, sub, cite, newTab}]` |
| `works` | `person`: that person's `works` as links, with each page's `date` |
| `table` | `head`, `rows` (cells rich) |
| `card` | `title`, `lines` (rich) |
| `link` | `text, href, cite, newTab` |
| `hr` | none |

- **Rich text** is a string or a list of parts: a string, `{link, href, cite, newTab}`, `{b}`, `{i}`.
  A `cite` is the passage to find at `href`: the link gets a small ↗ and opens with the passage in `<mark>`
  (scrolled into view), or with the banner "This source doesn't say that." when the passage is not there (Trace).
- **Notes** `{id, text, tag, for, on}`: `tag` is `inside` (default), `who`, `evidence` or `others`. `for` ties the
  finding to one group (a specimen, ad or case), so it is only added while that group is current. `on: 'tap'` makes
  the block a tap target (`role=button`, Enter and Space, a dotted underline, "✓ Noted" once taken; an inline part
  such as a `span`, `b` or `small` gets the class `fc-tapi` and a 44 px tall box); inside notes are
  tap notes unless `on` says otherwise; every other note is added when its page, entry, image search, lookup or
  search result list is shown. Pages, entries, images, lookups and index entries all take `note`; posts take
  `notes` per part (`name`, `followers`, `text`, `image`, `shares`).

## `FC.create(world, opts)` -> `fc`

`opts`: `{services, now}`. `services` overrides the three made-up services, each `{name, domain}`:
`{search: Wayfind wayfind.example, wiki: Openpedia openpedia.example, lookup: Site lookup sitelookup.example}`.
`now` replaces `Date.now` for the timers (tests).

```js
fc.world, fc.services
fc.report                  // {bad, missing} from the load check: bad = not reserved (each logged), missing = a link,
                           //   result or work that resolves to no page in the world (not logged; test it)
fc.check()                 // run that check again (after a tool adds pages to the world, such as ad-agency's ads)
fc.safeDomain(u)           // isReserved, plus a console.error when it fails
fc.isReserved, fc.hostOf, fc.words, fc.tags (the TAGS table), fc.icon(name, size), fc.logo(look.logo, size), fc.h

// addresses
fc.resolve(url)            // {site, page} | {service: 'search', q} | {service: 'searchHome'} | {service: 'imageSearch', id}
                           //   | {service: 'entry', entry} | {service: 'lookup', domain} | null
fc.siteOf(host), fc.titleOf(url)
fc.searchUrl(q), fc.imageUrl(id), fc.lookupUrl(urlOrDomain), fc.wikiUrl(id)
fc.search(q), fc.results(q)          // over world.index (pure search above)
fc.imageSearch(id)                   // the copies, earliest first
fc.lookup(urlOrDomain)               // {domain, name, registered, owner, note} or null (no record)

// locks: newTab, search, image, lookup, leave (a link to another site), trace (a cite link, even on the same site)
fc.lock(names), fc.unlock(names?)    // unlock() with no names clears all
fc.locked(name), fc.locks

// notebook: one card per finding per group
fc.note({id, text, tag, from, for}) // true when added; false when already there or for another group
fc.notes(group?)                     // newest first; the current group by default
fc.allNotes, fc.group

// timers and tabs per (group, pass): visible time only (document hidden pauses it)
fc.begin(group, pass)                // the current group; starts timing that pass
fc.focus(group)                      // the current group, not timed (a finished one)
fc.pause(), fc.resume(), fc.setHidden(bool)   // setHidden is wired to visibilitychange already
fc.countTab(n = 1)                   // the browser calls it for each new tab
fc.seconds(group, pass), fc.tabs(group, pass), fc.ms(group, pass)

// calls
fc.call(group, pass, verdict, extra) // {specimen, pass, verdict, seconds, tabs, at, ...extra}; replaces an earlier
                                     //   call for the same group and pass. extra carries a tool's own fields
                                     //   (ad-agency: {rules: ['R2']})
fc.callOf(group, pass), fc.calls
fc.clear(group?)                     // that group's calls, notes and timers; no argument clears everything
fc.dump(), fc.restore(d)             // JSON for localStorage: {calls, notes, T}
```

"Group" is the engine's word for whatever a tool compares: fake-or-fact-lab's specimens, fact-check-desk's cases,
ad-agency's ads. The call record still names it `specimen`.

### `fc.browser(el, opts)` -> handle

`opts`:

| option | what it does |
|---|---|
| `art` | `{imageKey: src}`: the bundled `art:` images, by images key (else `images[key].src`) |
| `chips()` | suggestion chips on Wayfind's home and results; return a list of query strings (or none) |
| `noResults` | the no-results line (default "No good results. Try other words.") |
| `maxTabs` | default 8; one more shows "8 tabs is the most..." (the number is `maxTabs`) in the browser's status line |
| `lockLabel` | the padlock pill's word on a locked control (default "Locked"; fake-or-fact-lab: "Pass 2") |
| `texts` | override any of: `notSay, noResults, tooMany, lookupBtn, imageBtn, searchPh, blank, notFound, noLookup, noted, home, copies, first` |
| `onLocked(name)` | a locked control was used (the control stays visible; nothing happens) |
| `onNote(note, added, tapped)` | a note was taken; `added` false when it was already in the notebook |
| `onOpen(url, resolved, addedNotes)` | after every render |
| `onLink(href, linkOpts)` | after a page link was followed |
| `home` | the new tab's address (default Wayfind's home) |
| `focusSearch` | default true: a new tab puts focus in Wayfind's box |

Handle: `{el, page, open(url, {newTab, hl, count}), back(), close(i), select(i), newTab(), search(q), use(session),
session, url, tabs, render(), paintLocks(), message(text)}`.

- `open` checks `safeDomain` first. `newTab` opens a tab (counted for the timer unless `count: false`); `hl` is a
  passage to highlight.
- `use(session)` shows another `{tabs, active}` object and keeps working in it, so a tool keeps one browser and one
  session per group (fake-or-fact-lab keeps each specimen's tabs).
- Chrome: numbered tabs (tab 1 cannot be closed), `+`, back, a read-only address bar (host bold, path muted and
  clipped first), a search box (Wayfind), "Who runs this site?" (opens a lookup of the current site in a new tab).
  Each photo with `copies` gets a "Search this image" corner button. Locked controls keep their place with a padlock
  pill (and `aria-disabled="true"` on the search box and its button). A link to another site fires
  `onLocked('leave')` while `leave` is locked; a cite link (class `fc-citea`) fires `onLocked('trace')` while `trace`
  is locked, on any site; other same-site links always work. Links in a page body are 44 px tall boxes.
- Stable hooks a tool may style or focus: `.fc-newtab` (the `+`), `.fc-lookup` ("Who runs this site?"), `.fc-imgbtn`
  (Search this image), `.fc-sbox` (the search box), `.fc-citea` (a cite link), `.fc-tap` and `.fc-tapi` (tap notes).
- The tab strip is rebuilt keeping focus on the same tab or close button. Every target is at least 44 px.
- Page `h1`/`h2` take the site's font, not the tool's.

### `fc.notebook(el, {empty, group})` -> `{el, refresh(fresh), count}`

The cards of `group()` (default the current group), newest first, each with its tag's icon and word (Inside, Who's
behind it?, What's the evidence?, What do other sources say?). `refresh()` redraws and gives new cards a one-shot
highlight (no loop). Call it from `onNote`.

## Styling

The engine injects one stylesheet the first time a browser or notebook is made. The browser chrome uses
`--fc-chrome, --fc-chrome2, --fc-cink, --fc-cmuted, --fc-cline, --fc-cfocus` (set them on `.fc-browser` to recolor);
pages use the site's look. Tap notes, Noted tags, Inside notebook cards and the Inside tag colour use `--fc-note`
(default the tool's `--brand`, then #6d28d9). A tool may hide `.fc-sbox` on a narrow browser (fake-or-fact-lab does under 600 px), since
`+` reaches Wayfind too. No animation runs forever.

## What each tool brings (its own)

| Tool | Grade | Its one idea | Engine parts it uses |
|---|---|---|---|
| fake-or-fact-lab | 6-8 | six specimens read twice: Pass 1 inside only (all six locks), Pass 2 outside; a lab table compares both calls with the experts | everything; locks in Pass 1; Trace on S1, S5; image search on S2; lookups on S1, S4 |
| fact-check-desk | ELA 8 | two sources disagree on one fact | world, browser, Trace, notebook, calls |
| ad-agency | 12 | build ads, then judge rival ads against rule cards | world (adds the student's own ads as pages, then `fc.check()`), browser fully unlocked, notebook, calls with `extra: {rules}`; no locks |

## Rules for siblings

- World, browser, search, lookup, image search, Trace, notebook, locks, timers and calls come from the engine. A
  sibling brings its own scene, its story and its verdict scale (the engine stores any verdict string).
- Give every finding a note with a stable `id` and the right tag; use `for` when one page holds findings for
  several groups.
- Test: `fc.report` is `{bad: [], missing: []}`, `fc.safeDomain('evil.com') === false`, a clean console.
- New engine features go into the engine and this file in the same change, keeping existing calls working.
