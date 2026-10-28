# Family: security

Three tools, grade 5 to 12 (computer science), share one engine: `kit/security.js`, inlined with
`<script src="kit:security"></script>` after `kit:curio`. It gives one global, `Sec`. Data Defenders built it first;
phishing-spotter and capture-the-flag use it as is.

## The rule that binds every sibling

Security tools teach **defense**, with **made-up systems inside the page only**.

- Every web address and email domain is a reserved name: `example.com`, `example.org`, `example.net` (and their
  subdomains), or a name ending `.example`, `.test` or `.invalid` (RFC 2606, RFC 6761). The renderers check every
  address they draw and log one console error for any other, so a real site shows up as a failed console check.
- No real brands, logos or company names. Logos are drawn shapes with made-up names (`logo: {shape, color, name}`).
- No attack steps. Students spot, check and fix things; they never get a recipe for breaking in. Ciphers and
  encodings are shown as "not a lock", never as a way into someone else's account.
- Links never navigate. A click shows "In real life, this would open: ..." and the address.
- Nothing is sent or stored. Students never type a real password: password fields in `login` artifacts do not take
  typing, and password strength is checked only on the tool's own made-up candidates.

## What the engine does (shared)

### Pure checks (no DOM): `Sec.pure`, also spread onto `Sec`

```js
Sec.hostOf(u)              // host of a URL or email address ("Name <a@b.example>", "https://x.test/p", "a@b.test")
Sec.safeDomain(u)          // true only for reserved names; never logs. A real top-level label just before the
                           //   reserved suffix fails too ('brand.com.example', 'x.org.test'), so a real brand
                           //   cannot hide inside a reserved name
Sec.COMMON                 // the 20 most-used passwords (UK NCSC 2019 list)
Sec.POOLS                  // {lower: 26, upper: 26, digit: 10, symbol: 33}
Sec.strength(pw, names)    // {length, pools, poolSize, bits, words, wordBits, used, onList, hasName}
                           //   names: words a guesser would try first (school, mascot, person)
Sec.band(r, names = [])    // 'Weak' (on the list, has a name, or under 8) | 'OK' (8 to 14) | 'Strong' (15 or more)
                           //   r: a strength() result, or a password string (then names are passed to strength,
                           //   so band('Cedar2026', ['cedar']) is Weak; with no names it is OK)
Sec.reasons(r, names = []) // short plain-language reasons for the band; r as in band
Sec.guessSeconds(bits, rate = 1e10)
Sec.seal(nums)             // the checksum the tools teach: the plain sum
Sec.caesar(text, k)        // letters only, case kept
Sec.vigenere(text, key, dir)   // dir 1 / 'enc' or -1 / 'dec'; the key advances on letters only
Sec.b64(text, dir)         // UTF-8 safe; returns null on a bad decode
Sec.lock({check, normalize})   // {try(answer) -> {open, misses}, open, misses, reset(), force()}
                               //   default normalize: trim and lowercase strings
Sec.clock({mode: 'down' | 'up', ms, onEnd, onTick, tick})
                           // {start, pause, reset(ms), elapsed, left, total, running, ended}
Sec.mmss(ms, up)           // "4:05"
```

Checked values (scratch Node test): the four Data Defenders passwords band Weak, Weak, Weak, Strong; capture-the-flag
bits 59.1, 37.6, 105.9 / 38.8 and 205.9 / 77.5; `b64('flag{not_a_lock}')` is `ZmxhZ3tub3RfYV9sb2NrfQ==`; the spec
strings for `caesar(7)` and `vigenere('LANTERN')` match; Data Defenders seals sum to 70, 67, 79, 65.

### With the DOM

```js
Sec.guard(u, where)        // safeDomain, plus one console.error per non-reserved name
Sec.world(org)             // org: {name, domains, people: [{id, name, role}], accounts, files}
                           //   checks every domain and every email or URL string in people, accounts and files;
                           //   returns {org, ok, person(id)}
Sec.h(tag, attrs, ...kids) // tiny DOM builder
Sec.artifact(kind, data, opts)  // the things people read; returns a handle (below)
```

Artifact kinds and their data:

| kind | data |
|---|---|
| `email` | `fromName, from, replyTo, to, subject, time, body` (paragraphs: a string, `{text, spot}` or `{parts: [...]}`), `links: [{text, href, spot}]`, `attachments` |
| `sms` | `sender, number, bubbles, links` |
| `login` | `address, addressSpot, logo: {shape, color, name}, heading, fields` (never take typing), `button` |
| `log` | `columns: [{key, label, mono, nowrap}]`, `rows` (each may carry `spot`, `details`, `label`), `sort`, `filter` |
| `file` | `title, fields, seal: {label, value, icon, spot}, files: [{name, body, spot}], text`; `layout: 'row'` gives a one-line card: `name`, chip fields (tappable), a seal chip (with its `icon`) and `handle.slot` for the tool's own buttons |
| `call` | `lines: [{speaker, text, spot}]`, `numbered` |
| `note` | `lines` (strings or `{text, spot}`) or `text`; `style: 'text'` gives a plain card, any other value a yellow sticky |

`opts`: `{onSpot(id, el, tell, e), onLink(href), linkNote, dark, status, statusText, title, maxHeight, className, fieldNote}`.
A spot is `spot: 'id'` or `spot: {id, tell}`; `tell` reaches `onSpot` as given. `opts.title` wins over `data.title`.
`dark: true` gives the terminal look (capture-the-flag).

Handle: `{el, kind, slot, spot(id), spots(), tell(id), mark(id, 'marked' | 'right' | 'wrong' | 'dim' | null),
marked(), clearMarks(), tag(id, text, cls), status(text)}`. Marks survive a log re-sort.

Spots are tappable with `role=button` (Enter and Space work; real buttons are not double-fired). Tap targets are at
least 44 px (chips, inputs, fake buttons, sort buttons, the tools select, spot rows in a log), and the keyboard focus
ring is drawn after the marked, right and wrong looks, so focus stays visible on a marked spot. Hover, focus or a
long press on a link shows its address in the status bar, the habit phishing-spotter teaches.

Fixed by the engine: the look of every artifact (one stylesheet, colored from `--sec-*` variables a tool may set:
`--sec-card, --sec-ink, --sec-muted, --sec-line, --sec-link, --sec-status, --sec-glow, --sec-ok, --sec-bad,
--sec-mono`, and `--sec-term*` for the dark look), spot marking, link handling, the domain guard, the password
bands and the lock and clock behavior.

## What each tool brings (its own)

| Tool | Grade | Its one idea (not shared) | Engine parts it leans on |
|---|---|---|---|
| data-defenders | 5 | an escape room: three rooms for C, I and A (two, two and three fix-it puzzles; the Server Closet's network puzzle uses the network engine's map), then sort six problems | `world`, `strength`/`band`, `seal`, `artifact('file', layout 'row')`, `artifact('log')`, `lock`, `clock` |
| phishing-spotter | 6-8 | fast keep-or-report rounds; a report scores fully only when the tell is tapped | `artifact('email' / 'sms' / 'login' / 'call')`, `hostOf`, spots, marks, link status bar |
| capture-the-flag | 9-12 | a twelve-tile board in a made-up freight company: find each flag by careful reading, then patch the hole it came from | `artifact('log' / 'file' / 'note' / 'call', dark)`, `caesar`, `vigenere`, `b64`, `strength`, `guessSeconds`, `lock` |

## Rules for siblings

- Artifacts, checks, locks and the clock come from the engine. A sibling brings its own scene and its own story.
- Call `Sec.world(org)` with every made-up domain the tool uses, so the guard checks them on load.
- A spec test should include `Sec.safeDomain('evil.com') === false` and a clean console.
- New engine features go into the engine and this file in the same change, keeping existing calls working.
