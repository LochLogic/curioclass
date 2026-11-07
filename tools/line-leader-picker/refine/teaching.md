# Teaching lens: line-leader-picker (round 1)

Cold Teaching lens, 2026-11-06. Read spec.md, src.html, notes.md, BASELINE, REFINE and the shared audit
(S:/CurioClass-codex-scratch/line-leader-picker/audit-r1). My frames and logs:
S:/CurioClass-codex-scratch/line-leader-picker/teaching/frames (shots.json, shots2.json beside them).

Summary: no blockers. The core works: Run stays disabled until both steps are chosen, day 1 lights step 1 then
step 2, the Who overlay stamps "Made by our class", the stays-to-back change gives twenty 1s over Before outlines,
rule C shows Q1 yes and Q2 yes with the fSame line, Bee sick under B gives Bee 0 and Ant 2 (leaders 0,2,3,...,19,0,
confirmed in t-bee-sick-B-checks), verdicts are never marked. Recomputed: 20 x (19/20)^20 = 7.17. The problems are
in the Is It Fair? check flow and a few lines that say something false or misleading.

## Findings

1. **Is It Fair?, Our chart (src.html:1239, 1355-1370).** The summary records Q1, Q2 and Q3 at month end, before
   any check is answered, so opening Our chart right after a rule card shows "Yes / Yes / Yes" for that rule while
   all three thumbs are still untouched. Q1 (a rule-level fact the chart cannot show) is handed over outright.
   Seen: frames/t-summary-before-checks.png (checks [null,null,null], row C all Yes). Better: fill a cell only once
   that check is answered ("?" until then). Level: should fix. Tag: general.

2. **Is It Fair?, thumbs mean two things (src.html:854-855, 861-862).** The three checks use thumbs up for "yes" and
   thumbs down for "no", and the verdict uses thumbs up for Fair and thumbs down for Not fair. For rule A the
   matching check answers are down, up, up (yes, a friend was left out), then the class is asked for a thumbs
   verdict. A K-2 child reads thumbs up as "good"; "thumbs up, yes a friend was left out" fights that, and it blurs
   the line the tool wants kept between the chart's facts and the student's own fairness call. Seen:
   frames/t-bee-sick-B-checks.png (three thumbs-up checks beside a thumbs-up Fair button). Better: yes / no
   pictures for the checks (check mark and cross, or a nodding and a shaking head), thumbs only for the verdict.
   Level: should fix. Tag: general.

3. **Is It Fair?, Q1 mismatch says "Look at the chart again." (src.html:1340).** Every check answer that does not
   match gets that line. But Q1 is the rule's own fact (spec: "Q1 is the rule's own fact"); for rule C the chart
   shows 3 stickers beside 0, which supports the "no" a child just gave. Sending them back to the chart for Q1
   teaches the opposite of fSame. Seen in code: the agree/look choice is the same for checks 0 to 2. Better: for Q1
   a mismatch line about the rule ("Think about the rule, not this month's stickers."), then the q1 rule line.
   Level: should fix. Tag: general.

4. **Is It Fair?, feedback arrives after the next question (src.html:1334-1340).** Answering a check speaks the next
   question first (now:true), then "The chart agrees." plus the evidence line for the check just answered. Log with
   9 s gaps (t-check-order, shots2.json): after Q1 the order is "Was any friend left out? ..." then "The chart
   agrees. Only the friend at the front can lead...". After Q3 the verdict prompt plays before Q3's feedback
   (t-fair-C-all-thumbs). A pre-reader hears the answer to question 1 while looking at question 2. Better: feedback
   first, then the next question. Level: should fix. Tag: general.

5. **Change a Step, Which step: the old tile is called unchanged (src.html:1043-1047, L.chSame line 636).** After
   "Which step made the month change? Tap that step.", tapping "Stays at the front" (the Before step, in the
   changed slot) gets "That step stayed the same. Look for the step you changed." That is false: it is the very
   step that changed. Seen: t-which-old-tile log (tile-2 tap). Also, while the question is open every tile tap is
   captured as an answer, so a child cannot try another change until they find the pressed new tile. Better: judge
   by slot (any tile in a changed slot is right: "Yes, step 2 changed from stays at the front to goes to the
   back"), or give the old tile a line saying it was the Before step. Level: should fix. Tag: general.

6. **Is It Fair?, Bee's sick line implies a cause it did not have (src.html:1253-1256).** With Bee sick, tapping Bee
   at 0 always says "Bee was home sick on day two." then the left-out line, under every rule. Under rule A (Ant 20,
   everyone else 0) and often under rule C, Bee's 0 has nothing to do with the sick day. Seen: t-bee-sick-A log
   ("Bee. never led this month. Bee was home sick on day two. That friend waited all month..." with Ant 20).
   E2-ALG-IM-03 is about telling the rule's effect from the situation's effect, so the line should not blur them.
   Better: play beeSick only when the sick day changed Bee's count (rule B), or under A say Bee would not have led
   under this rule even at school. Level: should fix. Tag: general.

7. **Is It Fair?, New month erases the class's call (src.html:1034, 1239, 1355-1358); notes.md "Modes".** New month
   on a draw rule (and re-tapping any rule card) clears the verdict and overwrites the summary row, so Our chart
   loses the call the class already made. Seen: t-newmonth-wipes-call (summary C verdict false, then null after New
   month). notes.md says Our chart "records the outcomes and the class's own calls for this page load", which is
   not true after a New month. Better: keep the last verdict per rule (or show the old call beside "new month"),
   and make notes match. Level: should fix. Tag: general.

8. **Is It Fair?, the sick day is not visible on the chart (src.html:984; day strip hidden at 951).** Bee in bed
   shows only while exactly 2 days are done; the fair month runs at 75 ms a day, and in a finished month Bee's
   column looks like any left-out column. With the day strip hidden, a teacher cannot point at why Ant has 2 and
   Bee 0 (the turn passed on day 2, Ant led again on day 20). Seen: frames/t-bee-sick-B-checks.png (no bed mark, no
   day record). Better: a small bed mark on Bee's column in sick months and a one-line day readout ("Day 2: Bee
   away, Cat led. Day 20: Ant again."). Level: polish. Tag: general.

9. **Make a Rule, Who closed unanswered never returns (src.html:1227-1233, 1274).** Close (x) dismisses the only
   EK-ALG-IM-03 question for the whole page load (whoShown stays true). A teacher who closes it by accident loses
   the stamp moment. Better: offer it again after the next month until it is answered. Level: polish. Tag: general.

10. **Is It Fair?, Q2 evidence line is singular (src.html:1329, L.left).** The Q2 detail is always "That friend
    waited all month and never led...", even for rule A with 19 friends at 0. Seen: t-fair-C-all-thumbs log (rule
    A, Q2). Better: a Q2 line with the count ("Nineteen friends never led."), keeping "Being left out feels sad."
    Level: polish. Tag: general.

11. **Is It Fair?, rule B's Q1 line answers a different question (L.q1B, line 638).** Q1 asks "Same chance for
    every friend?" and rule B's line is "Everyone gets a turn, one after another." That is the turn-for-everyone
    idea the tool separates from same chance (fSame). Better: "Every friend's place comes to the front in turn, so
    everyone has the same chance." Level: polish. Tag: general.

12. **Our chart column "Extra / none?" (src.html:527).** Cryptic for grade 2 next to the spoken "Did someone lead
    more than once while a friend got none?". Better: the same star-star-bar-empty picture used on the check, or
    "Extra turns?". Level: nit. Tag: general.

Standards: EK (choose two steps, Who question, stamp), E1 (change a step, Before outlines, Which step) and E2 (three
checks, own verdict, Bee's sick day) are each exercised by something the student does and sees; no code is only
mentioned. Findings 1 to 7 weaken E1 and E2 delivery. Teacher notes: What it teaches, Key skills and Support at home
are true of this tool and doable tonight; nothing sensitive for rule 8. Nothing cultural, Native or hard history: no
sensitivity review needed.

## Audit pilot

- Leads confirmed: none in the Teaching lens's scope (its rows are layout and voice timing; Play and Craft own the
  375x812 count and face overlaps and the 0 px header text).
- Leads wrong or excused: "welcome not heard after a first tile or friend tap" is excused by BASELINE rule 16; the
  premise stays on the rule card's job line and returns in the Who line.
- What it missed: the summary giveaway before any check (1), the thumbs double meaning (2), Q1 "look at the chart"
  (3), feedback after the next question (4; its walk has no answer sequence), the false "stayed the same" line (5),
  Bee's sick line under rule A (6) and New month erasing the call (7). All are states or words it cannot judge.
