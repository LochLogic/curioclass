# fake-or-fact-lab: handoff (Refine round 1 fixes, draft)

## What it is

- `src.html` on the kit starter with `kit:curio` and `kit:fact-check` (the family engine; API in
  docs/families/fact-check.md). Brand `#6d28d9`; `--inside` violet and `--outside` amber tint the two passes.
- Two modes: **Lab** (opens first) and **Report**. The panel is first in the DOM (hint, pass badge, notebook,
  verdicts, Lock my call, or after the reveal Next specimen with a small Retest; the Report's Clear lab).
- Draft: art is the 4 webp files in `art/` (bundled through `art:` tokens); voice is the browser voice
  (`voice/lines.json` matches `allLines()`, 19 lines, not recorded). The art prompts for ff-shark-street (curved fin
  with a dark trailing edge) and ff-library-front (green trees, not autumn) changed in `art/prompts.json`; the webp
  files were not regenerated.

## Layout of src.html

1. CSS: palette, three layouts (`wide` w>=1000 and h>=650, `compact` w>=640 and w/h>=1.25, else `stack`) and the body
   classes `relayout()` sets: `c300` (panel 300 wide), `nbc` (notebook as a chip that opens `#nbPop`), `narrowb`
   (browser under 600: search box hidden, lookup icon-only, slim masthead), `tinyb` (under 390), `midb` (browser
   under 820: the locked lookup's label hides so the address fits), `tight` (short non-stack: jar drawings hide), `hx`
   (stack under 480: one-row header, emoji-only Motion, Sound, Read, small jars, two-line hint), `big` (wide and
   1600 or wider: larger page, jar and reveal type for projection). Narrow tables (under 560) turn into stacked rows.
2. HTML: header, `#panel`, `#stage` with `#lab` (`#tray` of jar buttons, `#madeup` line, `#bwrap` for the browser,
   `#reveal`) and `#report`.
3. Script: `D` (domains), `SPEC` (S1 to S6: kind, url, expert verdict, why, `key` deciding findings, chips), `WORLD`
   (sites, people, posts, images, Openpedia entries, the Wayfind index built with `ASK()`), `FIND` (note id to note),
   the line table `L`, then state, drawing, flow (`openSpec`, `pick`, `lockCall`, `retest`, `nextSpec`, `setMode`),
   report, keys, `relayout()`, and `window.__tool` (also `rowOf`, `FIND`).

## The tricky parts

- **Sessions per specimen.** One browser; `state.sessions[S]` holds each specimen's tabs, swapped in with
  `browser.use()`. Retest throws the session away. The specimen's own tab counts once (not again on reopen).
- **First try.** `state.first[S]` keeps a retested specimen's first calls `{c1, c2}`; it is saved inside
  `fofl-table` as `first`. `rowOf(S)` returns the first try (with `retested: true`) when there is one, so the table and
  counts always use the first try. Clear lab empties it.
- **Locks.** Pass 1 locks `newTab, search, image, lookup, leave, trace`; other same-site links work. A locked tap sets
  the `locked` hint and speaks the `locked` how line once.
- **Outside move.** `outsideDone(S)`: a tab opened in Pass 2, or a note that is not an inside note. Lock stays
  disabled in Pass 2 until then (`h2need` hint).
- **Timers.** `fc.begin(S, pass)` on open, `fc.pause()` on Report and after the second call; `visibilitychange`
  pauses too and saves.
- **Voice.** `hint: false` with `read`. Welcomes: `wLab` (only in Pass 1; `welcomeAfter: true`), `wReport` or
  `wReportMore` (untested specimens left). `coachOutside()` queues outside (only while `browser.tabs === 1`, needs
  `.fc-newtab`), tools (needs `.fc-lookup`), image (needs `.fc-imgbtn`, so S2 only); `onOpen` re-runs it so the outside
  item drops once + is pressed. The outside lock calls `V.dropQueued()` before `expert`, so a fast Next specimen
  can't push the expert line out. `expert` is valid only while that specimen is open and tested.
- **Reveal.** Absolute over the bottom of the browser, capped at 85% in stack; Hide/Show. Its deciding-findings list
  comes from `SPEC[S].key` through `FIND`, marked by `fc.notes`. The Fact-checker column hides in compact.

## Answer key (teacher copy; not in notes.md)

| Specimen | Fact-checker | Deciding findings |
|---|---|---|
| S1 Gloverly Study Institute (gloverlystudy.example.org) | Don't trust it | Openpedia: founded 2024 by Quillbop Apps (maker of Gradewhistle); Glimmerlake Tribune: funded by the app maker; Trace: the "survey" is 412 Gradewhistle customers (lookup: registered 2024 to Quillbop Apps, Inc.) |
| S2 @SquallnookAlerts on Tweedlebeak | Don't trust it | image search: "Street Shark" 2019 collage by Rhea Lind first; Truthlamp Fact Desk; the account names no source (Gazette flood story has no shark) |
| S3 Port Alder Gazette | Trust it | Marisol Vega's staff page (2020 to 2026); council minutes 4 to 1; Glimmerlake Tribune brief agrees (Openpedia: founded 1921) |
| S4 Zapline Now | Don't trust it | lookup 3 weeks ago, owner hidden; J. Carter has no other work; nobody else reports it |
| S5 Pixelpuddle Parent | Partly true, stretched | Trace: the Quellmont Journal study found a small link and says it cannot show cause; Glimmerlake Tribune says the same |
| S6 Ms. Park's Pond Notes | Trust it | Puddlewick Middle School staff page (science teacher, as her About me says); Brambleskip Nature Center; Openpedia wood frog |

## Name searches (blocker 1)

Every organization, outlet, school, app, handle and site name was web-searched before use. "No match" means no real
organization, product or outlet with that name or a close one turned up.

| Name searched | Result | Decision |
|---|---|---|
| Daily Ledger Now | The Daily Ledger is a real Canton, Illinois paper (teaching lens) | replaced by Zapline Now |
| BrightPath Apps | real BrightPath Kids (teaching lens) | replaced by Quillbop Apps |
| Willow Creek Middle School | real school name in three states (teaching lens) | replaced by Puddlewick Middle School |
| Center for Smart Study | a real "Smart Study" app exists | replaced by Gloverly Study Institute |
| Quillbop | no match | used (Quillbop Apps) |
| Gradewhistle | no match | used (the app) |
| Gloverly | no match | used (Gloverly Study Institute) |
| Zapline Daily, Zapline Now | no match | used (Zapline Now) |
| Puddlewick Middle School | no match | used |
| Squawkle | close to the real Squawki | rejected |
| Tweedlebeak; "Tweedlebeak" app | no match (Tweedle apps are distinct) | used (social site, replaces Chirp) |
| @StormWatchNow | handle not found, but StormWatch is a real app and brand | replaced |
| Gustwhopper | echoes Ghost Whopper | rejected |
| Squallnook | no match | used (@SquallnookAlerts, Squallnook Alerts) |
| Pixel Parent | real Pixel Parents podcast | replaced |
| StudyStar, Chirp | not searched: common real product words, replaced on sight | replaced (Gradewhistle, Tweedlebeak) |
| Pixelpuddle; "Pixelpuddle Parent" | no match (the Pixel Parenting podcast is distinct) | used |
| Journal of Child Learning | close to a real journal | replaced |
| Quellmont | no match | used (Quellmont Journal of Child Learning) |
| Fernhollow Nature Center | real Fern Hollow | rejected |
| Northwoods Nature Center | not searched: a common place-name pattern, replaced on sight | replaced |
| Brambleskip; "Brambleskip Nature Center" | no match | used |
| CheckPoint Desk | not searched: Check Point is a real security company, replaced on sight | replaced |
| Truthlamp; "Truthlamp" fact check | no match (TruthLens is distinct) | used (Truthlamp Fact Desk) |
| Dockfiddle | no match | used (Dockfiddle Hardware ad) |
| Lakeshore Tribune | echoes real papers | replaced |
| Glimmerlake | no match | used (Glimmerlake Tribune) |
| Port Alder, Port Alder Gazette | no match | kept |
| Openpedia | no match | kept |
| Wayfind | only Wayfinder products | kept |
| Rhea Lind | no match | kept |

Every address is reserved (`.example` or `example.org`); `fc.report` and `safeDomain` pass.

## Refine round 1: what changed, by item

1. Renamed every organization, outlet, school, app and handle (table above); the domains follow the names.
2. A line under the jars: "Every page in this lab is made up for practice. Your calls are saved on this device
   only." (second sentence hidden when narrow); the reveal footer says the same.
3. Each verdict button shows its one-line meaning. S2's why now says the post's news is the shark (so "Don't trust
   it" fits the definition); S5's says a fan blog cheering for games with a real study under it.
4. S6 has an "About me" card ("I teach science at Puddlewick Middle School"), checked by the school staff page; the
   why says so.
5. New engine lock `trace`: cite links (`.fc-citea`) are locked in Pass 1 even on the same site, with the padlock look.
6. Retest keeps the first try in the table and counts, tagged "retested"; Next specimen is the big button after the
   reveal, Retest a small one with "Your first try stays in the lab table."; Pass 2 can't lock before an outside move.
   spec.md Interactions updated.
7. Jar kinds: site, post, news story, news story, blog, blog ("news" when narrow): the Gazette and Zapline Now match.
8. `FC.pure.words` folds plurals ("-ies", final s), the numbers 0 to 12 and apostrophes; punctuation splits words.
   The index gained single-word name terms and plain routes (puzzle, spatial, game study, four day week, library
   Sunday, Ms Park teacher). A probe of plain grade 7 queries finds every key route.
9. 375 wide: one-row header (emoji-only Motion, Sound, Read, 44 px Lab/Report), smaller jars, two-line hint, short
   pass label, the page slot sized so verdicts and Lock are in view at 375x812.
10. Locked line and hint: "That's for the outside read. Pick a verdict, then press Lock my call."
11. Report with untested specimens: welcome and hint add "Press Lab to test the next specimen." (`wReportMore`).
12. Welcome: "Read this page. Tap lines to save them in your notebook. Then pick a verdict, and lock your call. Tap a
    jar for another specimen." (names no disabled control as the next step).
13. Focus: inside lock to `+`, outside lock to Next specimen, Retest to Trust it, Clear lab > Yes to Lab.
14. Enter locks only from the page body, Lock my call, or the verdict already picked.
15. Engine: inline tap notes get `fc-tapi` (inline-block, 44 px box); body links are 44 px inline-block boxes;
    result links 44 px.
16. Engine: `img` and `post` blocks take style, cls and note; tooMany uses `maxTabs`; the violet is `--fc-note`
    (default `--brand`); search button gets aria-disabled; hooks documented. Doc updated in the same change.
17. The outside line is queued only while just the specimen tab is open and is dropped once + is pressed.
18. The expert line survives a 2 s Next: queued how lines are dropped before it.
19. Reveal: "What decides it (your notebook has N of M)" with each key finding marked; the report adds a line that
    reacts to the student's own counts.
20. Wood frog: "In cold winters ... freezes solid. Its heart stops beating. In spring it thaws, and its heart starts
    beating again."
21. ff-shark-street prompt: a curved dorsal fin with a dark trailing edge (art not regenerated).
22. Report column "Tabs opened outside".
23. Each why names the source's purpose (to sell study apps, built to get shares, a fan blog, a paper that reports
    town news); notes.md has the `.org` question.
24. Match tags read "Matches" / "Doesn't match"; ✓ ~ ✗ belong to verdicts only.
25. Welcome no longer says "Pick a specimen" (see 12).
26. Pass 2 hint moves on once Wayfind is open (`h2b`: "Tap a suggestion or a result to read it. Then pick a
    verdict.").
27. Headline in view on arrival at 680x425 and 375x812 (slim masthead in narrow browsers).
28. `big` layout at 1600 and wider: larger page, jar, reveal and made-up line type.
29. Craft polish taken (student-visible only): reveal's Fact-checker column hidden in compact; "Inside" jar state;
   short "Notes: N" chip and "Pass 1: Inside" in compact; "Tested" pass label in compact; jar label line-height 1.3
   (no clipped descenders); the host label wins over the locked lookup label in narrow browsers; the table saves on
   specimen open, on hide and on pagehide; reopening a specimen does not recount its tab; a Clear lab confirm hint;
   the storage line in the Lab; the S3 caption "(file photo)".

## Checks run (this round)

- Flow test through `__tool` (scratch flow.js): every key finding by chip and by typed plain queries, tags, notes once,
  Pass 1 cite link locked (stays on the page, locked hint), Trace, image search order, lookups, `fc.report`
  `{bad: [], missing: []}`, `safeDomain`.
- Node test of `FC.pure.words` folding ("4-day week", "Ms Parks", "libraries", "class", "bus").
- Size sweep at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x1000 in four states (Pass 1 S1,
  Pass 2 S2 after a search, S4 reveal, report with a retest): main controls in view, no target under 44 px, no
  truncation, no horizontal scroll.
- 375x812 and 375x667 through `drive.py --host` in the same states: all clean (no small targets, no hscroll).
- Voice at a 2 s pace with held clicks: cite link (locked spoken), lock (outside spoken), + then lock and Next
  (tools and image dropped as newer or chain, expert spoken), Report with untested specimens (wReportMore spoken);
  a second run with silent first taps speaks wLab once.
- Focus and Enter check (results in item 13 and 14). Console clean apart from the host's favicon 404.

## Open

- At 375x667 the page slot is 110 px (verdicts and Lock in view; the headline needs a scroll). 375x812 is clean.
- The two changed art prompts need new images (the webp files still show the older fin and autumn trees).
- Voice is not recorded (draft).
