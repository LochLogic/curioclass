OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 9 (general 7, family 2), polish accepted 17
Traced to spec: blockers 1, should fix 4

# Refine: bus-stop

spec.md was updated in this merge (Refine round 1 notes in Content, Interactions, Voice, Done when 6, 7 and 13,
Sources checks, Open questions). Build to the updated spec. Lens files: `refine/teaching.md`, `play.md`, `craft.md`.
Shared audit: `S:/CurioClass-codex-scratch/bus-stop/audit-r1/`.

## Blocker
1. **Miscount card counts the wrong seats on a take-away stop.** src.html:1322-1332 (`pickCard`, miscount branch).
   The count numbers seats 0 to c-1 in order, whatever the child changed. Focus lands on seat 0 at an off stop
   (src.html:1188), so the usual move is to send seat 0 off; then the dashed empty ring is counted "1", the rider still
   in seat 4 is never counted, and Ms. Rosa says "Four riders": it models skipping a rider and counting an empty seat
   at the moment it says "Let's count." Seen: `play/f/p03-off-miscount.png` (Duck Pond, card 5 - 1 = 5), DOM after the
   count `gone counting:1 ... solid:` (Play 1). Integrator read the code: confirmed. Fixed: number only seats holding a
   rider (solid or new), in seat order (spec, Interactions, Miscount). (build) (general)
2. **Express shows the answer before the child answers.** src.html:1538-1541 (`renderExpress`). On "Five riders. Two
   get off. How many now?" the strip already shows 3 solid counters and 2 dashed leaving rings, so the answer is "count
   the yellow ones": no take-away, no fluency, and Express is the only home for K.OA.A.5. The scene also can't tell on
   from off: the same three kids (ids 0 to 2) stand at the curb for every fact. Seen: `teaching/frames/express-minus.png`,
   `play/f/p14-express-minus.png` vs `play/f2/q07` (Teaching 1, Play 2, Play 9). Integrator read the code: confirmed;
   the spec asked for the rings ("b counters wear the leaving ring"), now changed. Fixed (spec, Express facts): before
   the answer the strip holds a plain solid counters; "off" leavers stand at the open door facing out, "on" kids at the
   curb; no leaving ring until the reveal; a fresh set of kids per fact. (spec) (general)

## Should fix
1. **Ten stop and School cards are solved by the total alone.** src.html:1154-1155 (`makeStop`). Every Ten stop has one
   card ending in 10 ("8 + 0 = 8", "8 + 2 = 10", "8 + 1 = 9"), School one ending in 0, so a child picks "the 10"
   without the make-ten partner (K.OA.A.4); and the School wrong card says "Let's count." then counts nothing ("Zero
   riders"). Seen: `teaching/frames/ten-cards.png`, `play/f/p09-ten-cards.png`, `teaching/frames/school-miscount.png`,
   `craft/path-park.json` 97-99 (Teaching 3 and 6, Play 4, Craft 5). Fixed (spec, Content routes, Card kinds,
   Interactions): Ten stop cards `n + e = 10` | `n + (e-1) = 10` | `n + (e+1) = 10`, a wrong one counts the blue counters
   then "{e} kids got on. Try another card."; School cards `10 - 10 = 0` | `10 - 9 = 0` | `10 - 0 = 0`, a wrong one counts
   the dashed rings then "Ten kids got off. Try another card." Update lines.json and `allLines()`. (spec) (family:bus-stop)
2. **K.OA.A.4 covers starts 4 to 8 only.** content.json routes; notes.md admits it. The standard is "any number from 1
   to 9" (Teaching 4). Settled by BASELINE rule 2: new mode `Fill up` (spec, Screens and modes "Fill up", Voice "Fill up",
   Done when 13): five buses a ride, starts drawn without repeats so two rides use all of 1 to 9, each bus plays as the
   Ten stop with the new same-total cards, e + 1 kids waiting. Reuse the Ten stop code; add its lines to lines.json and
   `allLines()`; add `audit-states.json` entries for it. (spec) (family:bus-stop)
3. **Read in Express loses the question.** Hint `L.express` src.html:444, `expressQuestion()` 1520-1528. The fact's
   story is spoken once and never shown; Read cuts it and says only "Say how many. Tap a number, or Show me.", so a
   pre-reader alone who missed it can't hear it again (rule 4). Seen: `teaching` express-minus shot log (Teaching 2).
   Fixed: the fact's story is the first sentence of the Express hint, so Read repeats it (spec, Voice, Read line). (spec) (general)
4. **The first stop's story plays about 6 s after the kids boarded.** src.html:1144-1145 queue the road line and the
   start-counters line, then `beginStop` 1186-1187 queues the story behind them while the walk starts at once. Measured:
   tap 1.3 s, riders gone 3.9 s, "Maple Street! Two kids get on" at 10.3 s; a Done at 8.4 s drops the story unheard
   (`craft/c.json` intro-timing, `a.json` done5) (Craft 1). The spec listed three lines in a row and a walk with the story
   without saying how they fit. Fixed (spec, Interactions first bullet): on a road's first stop the walk starts when the
   story line starts. (spec) (general)
5. **Express riders walk twice and contradict the strip.** src.html:1569 then 1572/1551. `finishExpress` starts the walk;
   1.5 s later `renderExpress` re-renders the riders with the walk class, so they jump back and walk again while the
   strip and "2 + 3 = 5" already show the result, and they walk into a closed door (`showWorld` open is `!e.locked`,
   1532). Seen: `play/f2/q08-express-wrong.png` at 2.0 s (Play 3). Fixed: one walk per fact through an open door; after
   the reveal the riders stay at their end spots. (build) (general)
6. **No next action once every way is found.** Split mode: after "You found every way to make two. Three ways!" the hint
   stays "Tap a counter across. Then tap Keep it."; Drive's Split stop keeps "Find more ways, or tap Drive on." though
   the spec makes it stale when all ways are found. Seen: `play/f/p16-split-allways.png`, `p17-split-10.png` (Play 5).
   Fixed: Split mode hint after all ways names `More`, `Fewer` and the places ("Tap More or Fewer for a new number, or a
   place."); Drive's says "Tap Drive on." (build) (general)
7. **Split counters under 60 px below 1340 px wide.** src.html:161 (48 px discs) and the `auto-fit` grid at 120/182; with
   10 riders they are 47 to 48 px at 1000x625 and fall into rows of 4 at 680x425 (spec: 70 px counters in rows of 5).
   Seen: `audit-r1/state-split-ten-1000x625.png`, `state-split-ten-680x425.png` (Play 6, Craft 4; Craft's 62x60 at
   1000x625 was the button box with fewer riders, not the 10-rider disc). Fixed: 60 px or more at every size but the
   680x425 preview (44 px there), always 5 per row. (build) (general)
8. **Way list at 680x425 is cramped and crossed by lines.** Each slot's "↔" sits on the last digit ("10 = 9 + 1↔"), and
   turn-around curves run over the second column's slots; at 1366x768 the "↔" touches the digit too. Seen: `play/z18.png`,
   `play/f/p17-split-10.png` (Play 7). Fixed: the "↔" in its own space; at 680x425 drop the curves and keep the marks.
   (build) (general)
9. **Split mode says the same instruction twice in a row.** Entering Split speaks the welcome (src.html:429, 999) then
   `how('split')` (1003), back to back, nothing between (`craft/d.json` split-first, 1.3 s and 6.9 s) (Craft 2). The spec
   gives Split mode one how line (its welcome). Fixed: no second how line after the Split welcome. (build) (general)

## Polish accepted
1. **Tell first: only Go is live while riders wait.** src.html:1206 (`canEdit` includes 'hold'): cup taps added counters
   before the story and Done shows lit beside Go (`play/f2/q03`, `play/f/p19-tellfirst-hold.png`) (Play 8). Spec now says
   so. (general)
2. **Fold "say the answer out loud" into Express.** The Express welcome is always dropped by the first fact
   (`craft/d.json` express-later) (Craft 3). Remove it from lines.json and `allLines()`; the first fact's how line is
   "Listen, say the answer out loud, then tap the number or Show me." (spec, Voice Express). (general)
3. **Express ride end lands.** After the fifth fact a big empty board (`play/f/p15-express-done.png`). Show the five
   tickets in a big row and Ms. Rosa's cheer face, as Drive's end does (Play 10). (general)
4. **Stop name on the sign face.** `#stop-name` (src.html:44) floats top-right beside the blank painted sign
   (`play/f/p02-park-walk.png`, `audit-r1/state-sentence-cards-1366x768.png`) (Play 11, Craft 6). Set it over each scene's
   sign board, as the spec says. (general)
5. **Seat chart driver mark on the right.** The bus faces right but the chart's driver mark is on the left
   (`play/f/p02`) (Play 12). (general)
6. **Crowded curb.** Seven to ten kids overlap each other and the sign post, worst at 680x425 (`play/f/p20-ten-680.png`,
   `play/f2/q01`, `q02`). Larger groups stand in two rows in perspective, no figure covering another (Play 13). (general)
7. **Split wording.** "Tap a counter across" (src.html:429, 436) becomes the spec's "Tap a rider counter to send it to
   the other side." (Teaching 8, Play 14). (general)
8. **Split equation on one baseline.** Addends sit higher than "n =" (`play/f/p16`, `p17`) (Play 15). (general)
9. **Trip map fork.** The chosen fork stop is drawn on the trunk as "?" and the line splits after it (`play/zmap.png`)
   (Play 16). Split the line at the fork with each branch holding its own stop. (general)
10. **Way list dots.** src.html:132-133, 1442: kept-slot dots are 3 px and sit side by side under the middle; empty slots
    show "· · ·", which reads as three dots (`audit-r1/state-split-small-1366x768.png`, `craft/z2.png`) (Teaching 7,
    Craft 4). Each addend's dots under its numeral, at least 5 px; empty slots a dashed outline only. (family:bus-stop)
11. **Teacher notes without build talk.** notes.md:27 ("as the specification requires"), :48 (voice fallback, will be
    false), :53 ("specified"); :58 labels an achievethecore page as the Progressions (Teaching 9). Reword, drop :48, label
    the link as what it is; add Fill up to the notes. (general)
12. **Remove the `.idle-light` speck** (src.html:62, 297) or hide it while `#split-stage` shows (`craft/z1.png`) (Craft 8). (general)
13. **Ten stop right line capitalised:** "Yes! Seven plus three..." (src.html:1347, lines.json) (Teaching 11, Play 19,
    Craft 7). (general)
14. **Express mix at random,** 2 or 3 adds per ride (src.html:1517 always 2 adds) (Teaching 10, Play 18). (family:bus-stop)
15. **Tell first icon:** a speech bubble, not ☏ (Play 20, spec Screens). (general)
16. **Access labels:** `#cup` label says "Full" when full or disabled (src.html:310); the Split equation is announced
    when a counter moves (aria-live) (Craft 9). (general)
17. **Drive Split ticket records the last kept way,** not the counters as they stand at Drive on (`play/f2/q09`: kept
    7 = 6 + 1, ticket 7 = 4 + 3) (Play 17). (general)

## Settled calls
- Express giveaway and the same-total Ten and School cards: Play sent both to the spec's open questions because the spec
  wrote them; settled here by "a check must reward the right practice" and BASELINE rule 2, spec.md updated, so Codex
  builds them.
- K.OA.A.4 range: Teaching offered a short Ten round or varying the Ten stop; settled as the `Fill up` mode (rule 2, rule
  1: taught in full, not a thin add-on). Varying the Drive Ten stop alone can't reach 1 to 3 or 9 without breaking the
  route numbers.
- Split counter size: Play (47 to 48 px with 10 riders at 1000x625) and Craft (62x60) measured different states; the
  10-rider case and src.html:161 decide it, so it is a should fix.
- Keep: the cup stops by itself at 10 (Done when 6); welcomes cut by a first tap (BASELINE 16); 44 px controls at the
  680x425 preview (spec allows); wrong cards act out, never buzz; no score, no timer; the trip map "?" circle drawn over
  the road (all three lenses: no overlap on screen).

## To the spec's open questions
- None for Cory. Everything the lenses routed here was settled from BASELINE and the spec (Settled calls).

## Not taken
- Elimination drives the bus (Teaching 5): wrong cards are acted out and greyed; gating the rest or a first-try star
  would add friction or a score. Notes already tell the teacher.
- Rider faces on Split counters, kids beside the play areas (Play 14): the plain counter is the K.OA.A.1 object on purpose.
- Bundle 2.74 MB (Craft 10): over the 2 MB goal, under 6 MB, no `Size:` line needed (BASELINE 12).
