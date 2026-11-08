# Bus Stop: Teaching lens (round 1)

Cold lens, Claude, 2026-11-06. Read spec.md, src.html, notes.md, content.json, voice/lines.json, audit-states.json,
STANDARDS.md, BASELINE.md, REFINE.md and the shared audit (`S:/CurioClass-codex-scratch/bus-stop/audit-r1/audit.md`).
Own frames and logs: `S:/CurioClass-codex-scratch/bus-stop/teaching/frames/` (shots in `../shots.json`).

Checks run:
- Recomputed all 6 route paths from content.json in Python: park 3,5,4 then 7 or 8; library 4,6,7 then 6 or 5;
  farm 5,4,7 then 4 or 6. Every stop's start matches the previous result, Ten stop empties 2 to 6, all within 0 to 10,
  all match the spec's Content. 25 Express facts match the spec (10 add, 15 take-away, largest sum 5).
- CCSS K.OA.A.1 to A.5 wording in the spec matches the standards as published (A.3 asks "more than one way"; the tool's
  "every way" is above the minimum).
- Played Park road via Duck Bridge school to school (frames `ten-start`, `ten-cards`, `school-miscount`, `end`),
  a Farm off stop (`drive-offstop`), Ten stop miscount (`ten-miscount`) and an Express take-away fact with Read pressed
  (`express-minus`). Done passes only on exactly k (code `done()`, src.html:1253); the bus never leaves on a wrong card.

## Findings

1. **Express take-away facts show the answer before the child answers.** Where: Express, `renderExpress()`
   src.html:1538-1541. On "Five riders. Two get off. How many now?" the five-seat strip already shows 3 solid counters
   and 2 dashed rings with arrows, and the 2 leaving kids already stand on the curb. The answer is "count the yellow
   ones"; no subtraction and no fluency is needed. Add facts show a counters plus b kids, so they are count-all too.
   K.OA.A.5 asks for fluency, which this mode is the only home for. Better: before the answer show the a riders (all
   solid) and the b leavers still at the door, and only mark the gone rings at the reveal; or show the picture for a
   moment then cover the strip while the question is asked. How seen: `teaching/frames/express-minus.png`.
   **should fix**, general.

2. **Read in Express loses the question.** Where: Express hint `L.express` src.html:444, `expressQuestion()` 1520-1528.
   The hint is only "Say how many. Tap a number, or Show me."; the story ("Five riders. Two get off. How many now?")
   is spoken once and never shown. Pressing Read cuts the story and reads only the instruction (vlog: the express how
   line "cut: read", then read = "Say how many. Tap a number, or Show me."). A pre-reader alone at home who missed the
   question has no way to hear it again (rule 4). Better: put the fact's story in the hint (or have Read say it), as
   Drive's See again does for stops. How seen: `express-minus` shot log. **should fix**, general.

3. **The Ten stop never asks the make-ten question.** Where: Ten stop, `addCounter()` src.html:1207-1216 and
   `makeStop()` 1154. The cup stops by itself at the tenth seat and greys to "Full", so the child taps until it stops;
   then the only card whose total is 10 is the right one ("7 + 3 = 10", "7 + 2 = 9", "7 + 0 = 7"), with the bus
   visibly full. A child can drive on without ever knowing the 3. K.OA.A.4 is the number that makes 10. Better: a
   distractor that also says 10 with the wrong addend (`7 + 2 = 10`), so the child must count the blue counters; or
   ask "How many empty seats?" before the cup goes live. How seen: `teaching/frames/ten-cards.png`. **should fix**,
   family:bus-stop.

4. **K.OA.A.4 covers only 4 to 8.** Where: content.json routes; notes.md "Good to know" admits it. The standard says
   "for any number from 1 to 9"; 1, 2, 3 and 9 never come up in a Ten stop. Split mode at 10 does list all eleven ways
   to make ten, which helps, but it is a decomposition task, not "given 3, find the partner". Rule 2 wants the code
   taught well. Better: a short Ten round (Split-style or in Express, any start 1 to 9, fill the empties, pick
   `n + e = 10` against close distractors), or vary the Ten stop's start on Other road. **should fix**, family:bus-stop.

5. **Elimination drives the bus.** Where: Drive tell step, `pickCard()` src.html:1285-1338. With three cards and wrong
   cards greyed for the stop, two wrong taps leave one card; the ticket then records it like any other. No score, and
   each wrong card is acted out, so this is not a blocker, but a child can finish every stop by tapping in order. notes.md
   line 27 says so to the teacher. Better: after a wrong card, the remaining cards stay live only after the child
   re-counts or taps See again, or the ticket marks a first-try stop with a small star. **polish**, family:bus-stop.

6. **School miscount card counts nothing.** Where: School stop, card "10 − 9 = 1", src.html:1321-1332. Ms. Rosa says
   "Let's count." then nothing is counted (no counters) and "Zero riders. Try another card." The empty count shows no
   reason one rider can't be on. Better: point at the ten empty rings ("Every seat is empty. Nobody is still on."), or
   count the ten rings that left. How seen: `teaching/frames/school-miscount.png` and its log. **polish**, family:bus-stop.

7. **Way list dots don't sit under their numbers.** Where: Split, src.html:1442 and `.way-dots` 132. In a kept slot the
   two dot groups sit side by side under the middle of "2 = 2 + 0", so "2 = 1 + 1" shows two lone dots under the first
   1. Empty slots show "· · ·", which reads as three dots to a dot-counting child. Better: dots under each addend as in
   the live equation, and an empty slot with no dots (a dashed outline is enough). How seen:
   `audit-r1/state-split-small-1366x768.png`. **polish**, family:bus-stop.

8. **"Tap a counter across" is vague for K.** Where: `L.split`, `welcomeSplit` src.html:429, 436. The spec's "Tap a rider
   counter to send it to the other side" says where it goes; "across" does not. **polish**, general.

9. **Teacher notes carry build talk.** Where: notes.md:27 ("as the specification requires"), :48 ("Speech uses the
   kit's browser voice fallback in this Build. No voice recordings were made."), :53 ("25 positive-operand facts
   specified"). Teachers don't know the spec or the build; line 48 will be false once voice is recorded. Better:
   "Wrong cards stay grey for that stop", drop line 48, "25 facts within five, no zeros". Also :58 names the
   Progressions but links an achievethecore situation-types page; label it as what it is. **polish**, general.

10. **Express rides are always 2 add and 3 take-away.** Where: `newExpress()` src.html:1517. The spec says "at least 2
    of each"; the code fixes the split, so additions are always the minority. **nit**, family:bus-stop.

11. **Ten stop right line lower case.** Where: src.html:1347 "Yes! seven plus three equals ten." (also in lines.json).
    Harmless for speech; matters only if lines are shown or recorded as text. **nit**, general.

Language, grade fit and guardrails otherwise hold: every choice is a picture or numerals with dots and is spoken, no
score or timer, K teacher-led with a solo path. Done-when 2 to 7 hold on the path I played and in code. Nothing
cultural, Native or hard-history. The rider kids (hijab, hearing aid, leg brace, varied skin tones) go to the BASELINE
11 representation check, not judged here.

Counts: blocker 0, should fix 4, polish 5, nit 2.

## Audit pilot

- Leads confirmed: none touch teaching. The 44 px targets at 680x425 are the spec's allowed preview size. The Express
  welcome "not heard" after a first tap is allowed by BASELINE 16, and the Express how line still names the action.
- Leads wrong or not mine: "line drawn across text '?'" on the trip map is the fork's unknown stop; the circle is drawn
  over the path (not checked further, Play/Craft).
- Missed (it can't see these): the Express take-away strip giving the answer (1), Read dropping the Express question
  (2), the Ten stop solvable without the make-ten number (3), and the empty count on the School miscount card (6).
