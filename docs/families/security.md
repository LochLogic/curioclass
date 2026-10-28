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
Sec.COMMON                 // a short sample: 20 very common passwords, all on the UK NCSC 2019 list of the
                           //   100,000 most-used breached passwords (not that list's top 20). Say "a list of 20
                           //   very common passwords" on screen, so "no" never reads as "safe"
Sec.POOLS                  // {lower: 26, upper: 26, digit: 10, symbol: 33}  (symbol: 32 printable symbols and space)
Sec.strength(pw, names)    // {length, pools, poolSize, bits, words, wordBits, pattern, patternBits, used, onList, hasName}
                           //   names: words a guesser would try first (school, mascot, person)
                           //   bits = length x log2(pool): assumes every character was picked at random
                           //   wordBits: two or more different lowercase words split by single spaces (words x 12.9)
                           //   pattern / patternBits: otherwise, Sec.pattern(pw) (null when pw shows no pattern)
                           //   used = the lowest of bits, wordBits and patternBits
Sec.pattern(pw)            // null, or {parts: [{kind, text, bits}], bits, words, caps, swaps}: how a guesser who
                           //   tries patterns first would build pw. Kinds: word (12.9, +1 with a capital), run
                           //   (keyboard, digit or alphabet run of 4+, 10 each; a stretch of runs back to back counts as
                           //   each run: qwertyuiopasdfghjkl 20.0), year (1900 to 2099, 7.6), digits (3.3 each),
                           //   symbols (5.0 each), separator (one kind of space - _ . between words, 2.3 once),
                           //   letters (a 1 or 2 letter scrap, or a capital run of up to 4 that is not word-like,
                           //   5.7 each), repeat (one character 3+ times in a row: log2 52 or log2 10, + log2 of the
                           //   count + 1), chars and times (a whole password that is one unit typed 2+ times: the
                           //   unit's pattern, or its characters at random, + log2(times) + 1; Ab1!Ab1!Ab1! 28.9,
                           //   twenty z's 10.0; with a separator, as in dog dog dog, the unit (a lowercase unit counts
                           //   as one word) + 2.3 + log2(times) + 1: six "password"s 18.8); a word used again costs log2(the words so far) + 1
                           //   (kettle orbit maple twice 48.9); +1 per letter swap undone (4 for a, 0 for o, @ for a, between two
                           //   letters). Letter runs split at small-to-capital and before a Title-case word after a
                           //   capital run (ILove = I + Love, NYKnicks = NY + Knicks); a capital run of 3+ with a
                           //   vowel keeps its letters (LOLpassword = LOL + password). No dictionary: a letter run
                           //   is a word when it has a vowel and no five consonants in a row (10+ letters: one word
                           //   per 6). It is a model, not a guesser: it can under-rate a random run that looks like
                           //   a word and can still over-rate a pattern it does not know (names, phrases, odd
                           //   capitals), so a tool says "no pattern this meter knows", never "no pattern". Needs a
                           //   sign of a pattern (two or more words, a capital, a digit, a symbol, a swap, a run, a
                           //   repeat, or one 10+ letter run) and at least one word, run or repeat; a run of 3+
                           //   letters that is not word-like means no pattern. Part kinds: word, run, year, digits,
                           //   symbols, separator, letters, repeat ({text: the character, times}), chars, times
                           //   ({times}). A tool showing bits must say on screen what they assume (STANDARDS)
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
bits 59.1, 37.6, 105.9 / 38.8 and 205.9 / 77.5; patterns: Winter2026! 26.6 (by characters 72.3), Gr4v1ty#7 24.3,
Tidepool-Lantern-88 36.8, m0nkeyB@rs 28.8, Kettle Orbit Maple 44.1, xK9#mQ2$vL no pattern (65.7),
ILoveMyDog2008! 57.6 (by characters 98.5), IHateMath1! 41.9, NYKnicks2026 33.0, ILoveYou123 43.5, LOLpassword 26.8,
twenty z's 10.0 (94.0), Ab1!Ab1!Ab1! 28.9 (78.8), six "password"s 18.8 (was 77.5 by words), abcdefghijklmnop 10.0,
qwertyuiopasdfghjkl 20.0, 1234567890987654321 20.0, kettle orbit maple twice 48.9 (integrator fix, BR2 exit round 2); `b64('flag{not_a_lock}')` is `ZmxhZ3tub3RfYV9sb2NrfQ==`; the spec
strings for `caesar(7)` and `vigenere('LANTERN')` match; Data Defenders seals sum to 70, 67, 79, 65.

### With the DOM

```js
Sec.guard(u, where)        // safeDomain, plus one console.error per non-reserved name
Sec.world(org)             // org: {name, domains, people: [{id, name, role}], accounts, files}
                           //   checks every domain and every email or URL string in people, accounts and files;
                           //   returns {org, ok, person(id)}
Sec.h(tag, attrs, ...kids) // tiny DOM builder (kids may be nested lists)
Sec.artifact(kind, data, opts)  // the things people read; returns a handle (below)
```

Artifact kinds and their data:

| kind | data |
|---|---|
| `email` | `fromName, from, replyTo, to, subject, time, body` (paragraphs: a string, `{text, spot}` or `{parts: [...]}`), `links: [{text, href, spot}]`, `attachments` |
| `sms` | `sender, number, bubbles, links` |
| `login` | `address, addressSpot, logo: {shape, color, name}, heading, fields` (never take typing), `button` |
| `log` | `columns: [{key, label, mono, nowrap}]`, `rows` (each may carry `spot`, `details`, `label`), `sort`, `filter`. A row with `details` opens and closes in place under itself (tap, Enter or Space; it gets a tab stop and `aria-expanded` even without a spot; a toggle never rebuilds the row, while a sort or filter redraws the rows and keeps open details open). The details text sits in a box as wide as the visible part of the card, held at its left edge, so it wraps in view when the table scrolls sideways. A table wider than its card gets a fade at the right edge until it is scrolled to the end. On a row with both a `spot` and `details`, a tap, Enter or Space fires `onSpot` and also toggles the details. `sort` puts a button in each header with a mark (both ways, up, down) and `aria-sort`; values compare as numbers only when both are plain numbers such as 312 or 1,400 (times like 07:41 sort as text), and ties keep their first order |
| `file` | `title, fields, seal: {label, value, icon, spot}, files: [{name, body, spot}], text`; `layout: 'row'` gives a one-line card: `name`, chip fields (tappable), a seal chip (with its `icon`) and `handle.slot` for the tool's own buttons |
| `call` | `lines: [{speaker, text, spot}]`, `numbered` |
| `note` | `lines` (strings or `{text, spot}`) or `text`; `style: 'text'` gives a plain card, any other value a yellow sticky |

`opts`: `{onSpot(id, el, tell, e), onLink(href), onDetails(row, isOpen), linkNote, dark, status, statusText, title, maxHeight, className, fieldNote}`.
`onDetails` hears each log row's details opening or closing.
A log's column names stick to the top of its `.sec-scroll` box; they stay in view only when that box is the one that scrolls, so a tool that shows a long log in a scrolling stage caps `.sec-scroll`'s height (capture-the-flag sets it from the space left in the stage).
A spot is `spot: 'id'` or `spot: {id, tell}`; `tell` reaches `onSpot` as given. `opts.title` wins over `data.title`.
`dark: true` gives the terminal look (capture-the-flag).

Handle: `{el, kind, slot, spot(id), spots(), tell(id), mark(id, 'marked' | 'right' | 'wrong' | 'dim' | null),
marked(), clearMarks(), tag(id, text, cls), status(text)}`. Marks and tags survive a log re-sort or filter.

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
