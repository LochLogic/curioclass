# Bus Stop: Play lens (round 1)

Played twice: once as a kindergartner alone at home, Sound on, reading nothing, and once as a teacher projecting
Drive with a class calling out the stories. All three roads, both forks, Split mode from 2 to 10, three Express rides,
Tell first, Other road, Motion off, 1366x768, 760x900 and 680x425. I drove the tool with drive.py (real held clicks,
a jittered drag from the cup to a seat, keys), on Chrome port 9862.
Frames: `S:/CurioClass-codex-scratch/bus-stop/play/f/` (p01 to p23), `f2/` (q01 to q09), `f3/` (r1, r2), plus the
zooms `z18.png` and `zmap.png` in `play/`. Shared audit: `S:/CurioClass-codex-scratch/bus-stop/audit-r1/`.
No console errors or exceptions in any of my 34 shots.

What works: the first screen names the action ("Tap a road sign...") and the picture signs need no reading; every
step's hint names its control; wrong cards act themselves out instead of buzzing; the bus never leaves on a wrong
card; Done only passes with exactly k counters (I tried 0, 1, 3, and the cup does stop at 10); Other road brings back
the fork with the chart and tickets as they were (p23: tickets "3 + 2 = 5", "5 - 1 = 4", 4 riders); the end screen
with ten waving kids and the ticket row lands (p11). A kid would replay a road to see the other fork. The short
test passes for Drive; the findings below are about moments that teach the wrong thing or show the answer.

## Blocker

1. **Drive, miscount card on a take-away stop counts the wrong seats** (src.html:1323-1327). "Let's count" numbers
   seats 0 to c-1 in order, whatever counters the child removed. Focus lands on seat 0 at an off stop (src.html:1188),
   so the usual move is to tap seat 0 to send it off. Then the dashed empty ring gets "1", the rider still sitting in
   seat 4 is never counted, and Ms. Rosa says "Four riders": the tool models skipping a rider and counting an empty
   seat at the exact moment it says "Let's count." Seen: `f/p03-off-miscount.png` (Duck Pond, 5 - 1 = 5 card),
   DOM after the count: `gone counting:1, solid counting:2, solid counting:3, solid counting:4, solid:` (seat 4
   uncounted). Fix: count the seats still holding a rider (solid or new), in seat order. **general**

## Should fix

2. **Express shows the answer on the take-away strip** (src.html:1538-1541). Before any answer, "Five riders. Three
   get off" draws 2 solid counters and 3 dashed leaving rings, so the answer is just the solid counters: no
   subtracting, no fluency (K.OA.A.5). Add facts are softer (count the counters, then the kids) but are still counting
   all. Seen: `f/p14-express-minus.png`. This is how the spec describes it ("b counters wear the leaving ring"), so it
   goes to the spec's open questions: for example show a counters plain and the b leavers standing at the open door,
   and mark the leaving rings only on the reveal. POLISH, Games and quizzes. **general**

3. **Express, the riders walk twice and contradict the strip** (src.html:1569 then 1572/1551). finishExpress starts the
   walk; 1.5 s later renderExpress re-renders the riders with the walk class again, so the kids jump back to the curb
   and start over while the strip already shows the result and "2 + 3 = 5". They also walk on into a closed door
   (showWorld open is `!e.locked`, src.html:1532). Seen: `f2/q08-express-wrong.png` at 2.0 s: five seats full, the
   sentence shown, three kids still on the curb, door shut. Anything shown twice must match (POLISH). **general**

4. **Ten stop and School cards are solved by the total alone.** At every Ten stop the right card is the only one that
   ends in 10 ("8 + 0 = 8", "8 + 2 = 10", "8 + 1 = 9"), and at School the only one ending in 0. After one trip a child
   picks "the 10" without asking what goes with 8 to make ten, which is the K.OA.A.4 question. Seen:
   `f/p09-ten-cards.png`, `f/p20-ten-680.png`. Better: wrong cards that also say 10 ("8 + 1 = 10", "8 + 3 = 10"), so the
   child matches the blue counters to the second number. Card content is in the spec, so this goes to its open
   questions. **general**

5. **No next action once every way is found.** Split mode: after "You found every way to make two. Three ways!" the
   hint stays "Tap a counter across. Then tap Keep it." although nothing is left to keep; More, Fewer and the places
   are never named. Drive's Split stop: "Find more ways, or tap Drive on." stays when there are no more ways (the spec
   says that line goes stale when all ways are found). Seen: `f/p16-split-allways.png`, `f/p17-split-10.png`
   (hint text in the run log). Say how to act. **general**

6. **Split counters under 60 px below 1340 px wide.** With 10 riders the counters are 47 to 48 px at 1000x625 (the
   `repeat(5)` rule only applies at 1340 px and up). At 1366x768 they are 62x70 (measured, `f3/r1`). Seen: audit
   `state-split-ten-1000x625.png`. K targets are 60 px. **general**

7. **Way list at 680x425 is cramped and crossed by lines.** With 7 to 11 slots in two columns, each slot's "↔" mark
   sits on the last digit ("10 = 9 + 1↔" reads "10 = 9 + 1."), and the turn-around curves run down the gap and over the
   slots of the second column. At 1366x768 the "↔" also touches the last digit, a lighter version. Seen: `play/z18.png`
   (zoom of `f/p18-split-10-680.png`), `f/p17-split-10.png`. In the preview, drop the curves (keep the ↔ in its own
   space) or give the mark room. **general**

## Polish

8. **Tell first leaves the cup and Done live before Go** (canEdit includes 'hold', src.html:1206). With Tell first on,
   two cup taps added two counters before the story played; Done is lit gold beside Go. Seen: `f2/q03` (changed = 2 in
   hold), `f/p19-tellfirst-hold.png`. Better: only Go is live and lit while the class tells the story. **general**

9. **Express scene cannot tell on from off.** The same three kids (ids 0, 1, 2: Express never moves the kid cursor)
   stand on the curb for every fact; for "get off" they stand exactly where "get on" kids wait, though the spec puts
   leavers at the door. A child who misses the words can't read the story from the picture. Seen: `f/p14` vs
   `f2/q07`. Better: leavers at the open door facing out, a fresh set of kids per fact. **general**

10. **Express ride end is flat.** After the fifth fact the tiles disappear and leave a large empty board with one
   strip, and Ms. Rosa keeps her talking face. Drive's end (tickets in a big row, the kids waving) lands; Express could
   do the same with its five tickets and the cheer face. Seen: `f/p15-express-done.png`. **general**

11. **Stop name floats over a blank painted sign.** The name box sits above and beside the painted stop sign, whose
   face stays empty at every stop (the spec puts the name on the sign). Seen: `f/p02-park-walk.png`,
   `f2/q01-school-after.png`. Better: set the name on the sign face, or crop the blank sign out. **general**

12. **Seat chart faces the other way from the bus.** The painted bus faces right (door and driver on the right); the
   chart's driver mark ◉ is on the left, so the front of the chart is the back of the bus. Seen: `f/p02`. Put the
   driver mark on the right. **general**

13. **Crowded curb.** Seven to ten kids are packed into the right 40 percent of the scene and overlap each other and
   the sign post, most at 680x425. Seen: `f/p20-ten-680.png`, `f2/q01`, `f2/q02`. POLISH: no figure covers another;
   stand larger groups in two rows in perspective. **general**

14. **Split mode has no riders in it.** The counters are plain yellow discs on the swings and slide; the ten kid
   cutouts drawn for the tool never appear, and "Tap a counter across" ("across" is a hard word for K) is the only
   instruction. A rider face on each counter, or kids standing beside each play area, would make 7 = 4 + 3 a story the
   way Drive is. Seen: `f/p16`, `f/p17`. **general**

15. **Split equation steps up and down.** The addends (number over dots) sit higher than "n =", so "10 = 0 + 10"
   looks staggered. Seen: `f/p16`, `f/p17`. Align the numerals on one baseline with the dots below. **general**

16. **Trip map forks in the wrong place.** The chosen fork stop is drawn on the trunk as "?", and the line splits after
   it, at the Park, Library or Farm stop, which sits on the upper branch while the lower branch has no stop. The
   picture of "two roads" doesn't match the choice the child made. Seen: `play/zmap.png` (crop of `f/p03`). **general**

## Nit

17. The Drive split ticket records the counters as they stand when Drive on is tapped, not a kept way: I kept 7 = 7 + 0
   and 7 = 6 + 1, moved two more and got the ticket "7 = 4 + 3" (`f2/q09`). **general**
18. Every Express ride is 2 add and 3 take-away facts (src.html:1517); a ride is never 3 adds. **general**
19. The Ten stop right line starts lower case after "Yes!" ("Yes! seven plus three equals ten.", src.html:1347 and
   lines.json). Spoken only today; it would show in a caption. **general**
20. "Tell first" uses a telephone glyph ☏; a child alone has no way to know what it does. A speech-bubble icon (as the
   spec says) would read better. **general**

Not reported: the welcome cut by a first tap on a road sign or Express (BASELINE 16; the premise is in the hint and
Read). Voice counts are Craft's; in my muted run the vlog marked every line `silent`, so I could not judge timing by
ear.

## Audit pilot

- **Leads confirmed:** split counters below 60 px with 10 riders (confirmed at 1000x625, finding 6). The 44 px controls
  at 680x425 are real but the spec allows 44 px in the preview, so not reported.
- **Leads wrong:** "line drawn across text '?'" on the trip map: the road runs under the "?" circle, not across the
  glyph (`play/zmap.png`). "split-counter 47x44 at every size": at 1366x768 the counters measure 62x70 (`f3/r1`, `r2`).
  "Welcome not heard" after Express and road first taps: allowed by BASELINE 16.
- **Missed:** the miscount count landing on the empty seat (blocker 1), the Express double walk (3), the answer on the
  Express strip (2), the Ten and School cards solved by the total (4), the stale hint after all ways (5), the cramped
  680 way list (7), the live cup during Tell first (8), and everything about feel. Its clean rows on sizes, Motion
  off, resize and the 2 s tap pace held where I looked.
