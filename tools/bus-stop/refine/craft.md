# Bus Stop: Craft lens (round 1)

Cold Craft lens on the built bundle `tools/bus-stop/bus-stop.html` (not re-bundled). My own runs:
`S:/CurioClass-codex-scratch/bus-stop/craft/` (a.json to e.json, outputs in `out/`, logs in the *.json files).
Shared audit: `S:/CurioClass-codex-scratch/bus-stop/audit-r1/`.

## Findings

### Should fix

1. **The first stop's story line plays long after the kids have boarded.** `src.html:1144-1145` queues two intro
   lines on a road pick ("The park road! Off we go." and "Three riders are on the bus. I can't see the back seats, so
   the seat chart shows me."), then `beginStop` (`src.html:1186-1187`) queues the stop story and its how line behind
   them. The riders' walk starts at once and is over in about 2.5 s. Measured (c.json `intro-timing`, real voice, no
   other taps): tap at 1.3 s, riders gone by 3.9 s, "Maple Street! Two kids get on the bus. Tap the cup..." starts at
   10.3 s. So "two kids get on" is spoken about 6 s after they got on, and a child who waits 7 s still hasn't heard
   the stop story (a.json `done5`: Done tapped at 8.4 s dropped the story and how line unheard). The spec's watch step
   has the story line play while the riders walk. Fix: hold the first walk until the story line starts, or shorten
   the intro to one line. Same thing happens on every road. Tag: general.
2. **Split mode says the same instruction twice in a row.** Entering Split queues the welcome
   ("Tap a counter across, then Keep it. Show every way to split the riders.", `src.html:429`, `999`) and then
   `how('split')` (`src.html:1003`), "Tap a counter across. Then tap Keep it." Both are spoken back to back
   (d.json `split-first`: 1.3 s and 6.9 s, nothing else between). That breaks "don't nag". Fix: make the how line
   silent when the welcome just said it (or fold the welcome into the how line). Tag: general.

### Polish

3. **The Express welcome is never spoken.** `setMode` calls `V.welcome()` and then `expressQuestion()` with
   `now:true` (`src.html:999`, `1004`, `1526`), which drops the queued welcome every time (d.json `express-later`:
   welcome `dropped, newer`; audit row 2 likewise). Its line ("Listen, say the answer out loud...") is in
   lines.json and would be recorded for nothing, and "say the answer out loud", the class part of Express, is never
   heard. Better: drop the Express welcome and put "Say the answer out loud" into `L.express`. Tag: general.
4. **Split counters and way dots lose the five structure at small sizes.** At 680x425 the counters sit in rows of
   4 (frame `audit-r1/state-split-ten-680x425.png`: 4, 4, 2), not the spec's rows of 5 (the `auto-fit` grid at
   `src.html:120` and `182`). In the way list the dot pictures are 3 px and sit side by side in the middle of the
   slot, not under their numbers (`src.html:133`, `1442`; zoom `craft/z2.png` of
   `state-drive-split-1366x768.png`: the dots for "6 + 1" are both under "= 6"). Better: a fixed 5-column group,
   and each addend's dots under its numeral, at least 5 px. Tag: general.
5. **At School, a wrong card says "Let's count." and then counts nothing.** For the two School wrong cards the
   miscount branch (`src.html:1321-1331`) loops `d.stop.c` = 0 times, so the child hears "Let's count." then
   "Zero riders. Try another card." with nothing lit (path logs, `craft/path-park.json` lines 97 and 99). Better:
   for 10 - 9 = 1 point at one ring and say "one rider still on? Look, every seat is empty"; for 10 - 0 = 10 use the
   ghost act-out. Tag: general.
6. **The stop name floats beside the blank painted sign, not on it.** `#stop-name` is pinned top-right
   (`src.html:44`), so a code label hangs next to an empty painted sign (`state-sentence-cards-1366x768.png`,
   `-760x900.png`, `-375x812.png`). The spec puts the name on the blank sign. Better: place the label over the sign
   board in each scene, or crop the sign out. Tag: general.

### Nit

7. Ten stop right lines start lower case after "Yes!": "Yes! seven plus three equals ten..." (`src.html:1347`, five
   lines in `voice/lines.json`). Use `cap(num(s.a))`. Tag: general.
8. `.idle-light` (`src.html:62`, `297`), an 8 px glinting dot with z-index 8, shows over the Split stop in Drive at
   the left edge (zoom `craft/z1.png` of `state-drive-split-1366x768.png`) and reads as a speck elsewhere. Remove it
   or hide it when `#split-stage` shows. Tag: general.
9. Access: `#cup` keeps the label "Counter cup: add one rider" when full or disabled (`src.html:310`); the Split
   equation (`#split-equation`) is not announced when a counter moves, so a screen reader user hears only "Move
   rider to Slide". Tag: general.
10. Bundle is 2.74 MB (59 webp images, 1.9 MB of art), over the 2 MB goal and under 6 MB, so no `Size:` line is
    required. Tag: general.

## Checks that came out clean

- **Contract:** one file; no resource requests after load (`performance` resource list empty, a.json `contract`);
  no `http` URLs in the bundle; no console errors or exceptions in any of my 17 shots or the audit; nothing stored
  except the kit Motion setting; kit used (Curio.voice, kit header, kit focus ring).
- **Lines:** `allLines()` = 542 lines = `voice/lines.json` 542 lines, word for word, both directions. All 6 paths
  (each road, both forks via Other road) played with too-few and too-many Done, both wrong cards, Ten-stop over-taps,
  Split stop, then Split mode n = 2 to 10 every way, places, and two Express rides: 282 distinct spoken texts, every
  one in lines.json. Tickets right on every path; the bus never left on a wrong card.
- **Access:** Tab order is header, then panel (Tell first, New road), then road signs (c.json `tab-order`); after a
  right Done focus moves to the first card, then its speaker (`cards-key`); kit `:focus-visible` 4 px ring; new,
  gone and aboard counters differ by mark and ring, not color alone; wrong cards grey and disable. Targets: 60 px or
  more at every size except the 680x425 preview, where the spec allows 44 px. Split counters measured 62x70 at
  1366x768, 70x70 at 1280x720, 62x60 at 1000x625 (e.json).
- **Motion:** frame times during the boarding walk at 1366x768: p50 16.7 ms, p95 16.8 ms, max 16.8 ms (d.json; a
  desktop headless Chrome, not a slow laptop). Motion off: audit clean.
- **Art:** 59 `art:` tokens, 59 prompts.json entries, no extras; all 23 people images (10 kids x 2, Ms. Rosa x 3)
  are `people: true`, drawn by gpt-image (not a local model); the cast covers the spec's hijab, glasses, hearing aid
  and leg brace.
- **Words:** no em dashes in src, notes, spec, content or lines; "Curio Class" never shortened; nothing
  classroom-unsafe.

## Standard voice check (Sound on, Motion on, held clicks)

| line | kind | expected | spoken |
|---|---|---|---|
| "Two kids got on, and you added zero..." (Done too few, 5 taps 7 s apart) | event | 5 | 5 |
| "Maple Street! ... Tap the cup for each new rider..." (first on stop) | how | 1 | 1 when left alone (at 10.3 s, finding 1); dropped unheard when Done comes first |
| Split welcome, then "Tap a counter across. Then tap Keep it." | welcome + how | 1 | 2 (finding 2) |
| Express welcome | welcome | 1 | 0 (finding 3) |
| "How many riders now? ..." after switching back to Drive | how | fits the cards on screen | 1, correct |

- **Stale lines:** road, cup, cup, Done, Split, Drive at 0.2 s gaps: the card sequence was hushed by the mode
  switch, the Split welcome cut by Drive, and only the line for the cards on screen played after. Clean.
- **First tap:** stage tap and a first Tab key both give the welcome within 0.3 s; road sign gives only its own line;
  Read speaks the hint only; Sound says nothing (audit table). Clean.
- **Read:** Read during "The park road!" cut it and spoke the hint; with Sound off Read still spoke. Clean.
- **Order:** spoken lines follow the actions in every log. Clean.

## Audit pilot

- **Leads confirmed:** first tap on Express or a road sign skips the welcome (true, and fine under BASELINE 16 for
  the roads; for Express it hides a bigger problem, finding 3: the Express welcome never plays at all). 44 px targets
  at 680x425 are real but allowed by the spec.
- **Leads wrong:** "button.split-counter 47x44 [every size]" is wrong: I measured 62x70, 70x70 and 62x60 at
  1366x768, 1280x720 and 1000x625. "Line drawn across text ?" is the trip map road running under the "?" fork circle,
  which is drawn on top (`src.html:1378-1387`, frame `state-seat-work-1366x768.png`): no overlap on screen.
- **Missed:** the late first-stop story line (finding 1, it needs timing against the walk), the back-to-back Split
  instructions (finding 2), the dead Express welcome as a whole-tool fact, rows of 4 and misplaced way dots
  (finding 4), the empty School count (finding 5), the stray idle-light dot (finding 8).
- Nothing cultural, Native or hard-history here; the people art goes to the contact sheet and the fresh
  representation check the spec already names.
