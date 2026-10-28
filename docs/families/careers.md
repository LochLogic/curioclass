# Family: careers

Career tools share one engine, `kit/careers.js`, inlined with `<script src="kit:careers"></script>` after
`kit:curio`. It gives one global, `Careers`: the career sheet (one career up close) and the formatting helpers.
career-match-quiz (grades 6-8) drew the sheet first, inside its own page; career-cluster-explorer (grades 6-8) moved
it here. path-planner and hospital-shift (9-12) will use it too.

career-match-quiz still carries its own copy of the sheet (2026-10-28). Move it onto the engine when it is next
reworked: the engine's defaults draw the same sheet (below, "The quiz's sheet").

## Data

Each tool bundles a `careers.json` with a `"json:careers"` token:

```js
{year: '2025', clusters: {mfg: 'Advanced Manufacturing', ...14},
 handbook: {edition: '2025-35', name, by, url},   // present when the Handbook fields are
 careers: [{
  id, name, onet, cluster, emoji,        // O*NET-SOC code; cluster is a key of clusters
  does, path, try,                       // written for grades 6-8 (scripts/careers_data.py)
  uses, riasec: [6], zone, ctx,          // O*NET 30.2: strengths, interest profile (R I A S E C), Job Zone, work context
  pay, hourly, jobs,                     // BLS OEWS May <year>, national: yearly median (null when BLS has only hourly), jobs
  // the Handbook fields (BLS Occupational Outlook Handbook, 2025-35), optional:
  edu,       // typical entry-level education, the Handbook's exact Quick Facts wording
  eduNote,   // where edu is "See How to Become One": the Handbook's own sentence for this job, quoted
  level,     // the ladder column 0-4 (below); set from eduNote where edu does not say
  outlook,   // "-2% (Decline)": the Handbook's percent and word, 2025-35
  ooh, oohTitle,   // the profile URL and its title (a career can sit inside a larger profile)
  oohJobs,   // the profile's "Number of jobs, 2025" (counts the self-employed; covers the whole profile)
  oohPay,    // the profile's 2025 median pay, yearly (oohHourly instead where the page gives only hourly)
}]}
```

The careers come from `scripts/careers_data.py`, which writes the Handbook fields too (its `HANDBOOK` and
`EDU_NOTE` tables, each value copied from the live page, since bls.gov blocks scripts):

```
python scripts/careers_data.py [<O*NET folder>] [--out <careers.json>] [--more]
```

The default `--out` is career-match-quiz's file, with the 83 careers. `--more` adds `C_MORE`, ten careers
career-cluster-explorer added so its clusters have ways in at more levels (2026-10-28); their O*NET interests are
read from O*NET OnLine (`ONET_MORE`), with no Job Zone (`zone: null`) or work context (`ctx: {}`), so a tool that
shows Training or work style should not use `--more` until those are filled from the O*NET files. Without an O*NET
folder the builder reuses the O*NET fields already in the output file (or the quiz's). career-match-quiz's own
`careers.json` was last built before the 2026-10-28 fixes (Hairstylist in Healthcare and Human Services, Real Estate
Agent in Financial Services, the psychologist's path, gender-neutral emoji); they reach it when it is rebuilt or
moves onto this engine. Every profile URL is in career-cluster-explorer's `sources.md`.

Never guess a Handbook value. A career with no profile has no `ooh`; the sheet then says "Not in the Handbook".

## Pure helpers

```js
Careers.money(n)          // "$62,960"
Careers.payText(c)        // {big, small}: yearly median and about-hourly, or the hourly median ("much of the work is part-time")
Careers.jobsText(n)       // "1.2 million", "416,000", always US separators
Careers.ZONE, Careers.ZONE_SHORT   // O*NET Job Zone names, 1-5
Careers.LEVELS            // the five ladder columns: [{key, name, short, means}]
Careers.EDU_LEVEL         // Handbook wording -> column
Careers.level(c)          // c.level, else from c.edu; null when not in the Handbook
Careers.EDU_PLAIN, Careers.eduPlain(c)   // the Handbook's wording in plain grade 6-8 words ("A certificate after high school")
Careers.groupPay(c)       // the Handbook profile's median as text when it differs from this job's, else null
Careers.outlook(c)        // {pct, word, dir: up|flat|down, arrow: ▲ ▶ ▼, text} or null
Careers.inHandbook(c)
Careers.corr(a, b)        // Pearson correlation of two interest profiles
Careers.similar(c, list, n = 4)   // closest interest profiles, +0.15 for the same cluster
Careers.esc(s)            // HTML-escape
```

The five columns merge the Handbook's eight categories: No degree needed (no formal educational credential, or a
high school diploma), Certificate or some college (postsecondary nondegree award, or some college, no degree),
Associate's, Bachelor's, and Master's, doctoral or professional.

## The sheet

```js
const sheet = Careers.sheet({
  data,                         // the careers.json object
  facts: ['pay', 'training', 'jobs'],   // the facts row, in order (default); keys of Careers.FACTS or
                                //   functions (c, data, opts) => {key, label, big, small, bigSmall, raw} | null
  payLabel: 'Typical pay',      // the pay box's label (default); career-cluster-explorer: 'Median pay, 2025'
  factCols: 3,                  // columns in the facts row (default: the number of facts, at most 3)
  blocks: {afterDoes, afterFacts, beforeSimilar, end},   // (c, ctx) => html: the sibling's own parts
  source: (c, data) => html,    // the line at the bottom (default: the quiz's)
  similarCount: 4,              // 0 hides Similar careers
  closeLabel: 'Close',          // text beside the ✕ (default: the ✕ alone, labeled Close)
  theme: 'night',               // a class on the overlay, for the tool's colors (CSS variables below)
  onOpen(c, ctx), onClose(c), afterDraw(box, c, ctx),
  root: document.body,
});
sheet.open(id, ctx)   // ctx is passed to the blocks and hooks; Similar careers reopen with {from: 'similar'}
sheet.close(); sheet.isOpen(); sheet.current; sheet.el; sheet.box
```

Facts: `pay` (when the data has `oohPay` and it differs, the small line adds "The Handbook page covers a larger
group, <oohTitle>: $X a year."), `training` (Job Zone and path), `jobs` (with `oohJobs`: the Handbook's count,
"counting people who work for themselves. Handbook count for all <oohTitle>"; without it, the OEWS wage and salary
count as the quiz shows it), `edu` (plain words in big type, then `Handbook: "<exact wording>"`, then the eduNote
quoted), `outlook` ("Job outlook, 2025-35", an arrow and the percent, the Handbook's word under it). The arrow is
never alone: the percent and word are always there. Under 640 px wide the facts go to one column.

Order on the sheet: header (emoji, name, cluster), what they do, `afterDoes`, facts, `afterFacts`, Try it now,
`beforeSimilar`, Similar careers, `end`, the source line.

Built in: Esc and the backdrop close it. Keys are read on `document` in the capture phase while the sheet is open,
so Esc works even after a click on the sheet's text moved focus to the page, and Esc does not reach the page's own
handlers. Tab stays inside (buttons, links, inputs, selects, textareas and `tabindex` elements; Tab from outside the
sheet goes to its first control); focus goes to the close button on open and back to what had it on close, all with
`preventScroll`. The sheet uses the fixed ids `cr-title` and `cr-close`, so a page has one sheet; a 260 ms rise on open,
none with Motion off; under 560 px wide it is a bottom sheet; under 520 px tall it tightens. The header keeps
116 px clear on the right, so a long name wraps instead of running under a labeled close button ("✕ Close").

Colors are CSS variables on the overlay (set them under the theme class): `--cr-backdrop --cr-bg --cr-ink --cr-muted
--cr-line --cr-fact --cr-try --cr-try-line --cr-chip --cr-link`, and `--cr-target` for the Similar buttons' height
(default 40 px; use 44 px in new tools). Defaults are the quiz's light look.

## The quiz's sheet (parity)

`Careers.sheet({data})` with no other options draws career-match-quiz's sheet: Typical pay, Training, People doing
it, Try it now, Similar careers and "Pay and job counts: BLS, May 2025, national. Interests and work style: O*NET
<code>." The quiz's own parts go in blocks: its match "why" in `afterDoes`, the interest bars, work style and
strengths in `afterFacts`.

## career-cluster-explorer

Facts `['pay', 'edu', 'outlook', 'jobs']` in two columns, payLabel `Median pay for this job, 2025`; `afterDoes` says
whether the lantern lit (only careers opened at the festival light one), `afterFacts` the path, `beforeSimilar` a See
it at the festival button; the source line links the Handbook profile. Built with `--more`: 93 careers
(`sources.md` lists each URL); `onClose` replays the lantern pop the sheet covered.
