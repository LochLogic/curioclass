# Fixes: scope and sequence of social-and-emotional-learning-grades-3-to-5, 2026-11-26

Fix pass after the Claude expert read (docs/reviews/sequence-social-and-emotional-learning-grades-3-to-5-2026-11-26.md),
per build/scope-writes/AFTERCORE-FIX.md. The Codex read waits for Codex's usage reset (after 2026-11-30) and gets its
own small fix pass then. The 2026-11-15 lead-call items are skipped as the fix brief says.

Counts: applied 6 of 6 expert findings (finding 6's five bullets each applied) and all 8 rows of the expert's Settled
table; lead calls 1, 4, 7 and 11 applied to frame wording; band items from the K to 2 read: none touch this course.
Not applied: 0.

## Applied

- **Expert 1** (days.csv): the missing skill added to the Application goal the Check note names, card withdrawn, on an
  unseen case, on days 36 (repair), 40 (leading steps), 48 (what, why, what if with a changed idea), 59 (focus plan
  against a planned distraction), 62 (welcome kit's first step checked against its plan), 100 (adapted care steps), 108
  (first meeting led with the three leading steps), 111 (repair talk, friend's side first, teacher supplying the words),
  123 (well-being choice for self and a friend), 146 (private purpose-and-cost decision, steps followed only), 152
  (unseen town system and its pressure), 161 (care steps with a follow-up, partner playing only the friend), 167 (asking
  the teacher for help with friends watching, partner playing the teacher), 172 (split choice of a first step led to a
  decision). Check notes repointed: day 52 (RD1 to day 48), 63 (SM3 to day 59; SM6 to day 62), 104 (SO3 to day 100),
  147 (SA9 to the private decision sheet, day 146), 180 (RS7 to day 172). Day 20 page item 1 now asks the honest
  action, its value, and what honesty cost and kept.
- **Expert 2** (days.csv notes, scope Shorter path): fold-ins moved to grade 3 days 14, 18, 34, 38 and grade 5 days
  131, 135, 141, 155; grade 4 unchanged. "Fold-in day" removed from days 35, 39, 61, 160, 186 and added to 18, 34, 38,
  135, 155. The Shorter path names the Applications that repeat each folded task. Still 12 sessions, 360 minutes.
- **Expert 3** (days.csv notes, scope Leave-out list): bridges on day 12 (stop-think-choose), 22 (strength scale and
  stop-think-choose), 43 (adds stop-think-choose), 75 (adds the goal steps card), 79 (focus plan and try-again step).
- **Expert 4** (days.csv): day 123 starts the one-week solution test (school days 307 to 312); day 126 checks it and
  decides what to keep; day 127's RD3 pointer reads "item 2 and the test checked on day 126". Scope unit 12 says so.
- **Expert 5** (days.csv day 153, scope unit 15 and Sources, frame Base text, Sensitivity reads and For the lead 10):
  the National Park Service five-cases and Briggs v. Elliott pages back the families' cost; the page names job loss and
  refused loans only, threats and violence stay off it; the Brown Foundation page is a secondary link only.
- **Expert 6** (days.csv, scope): day 12's ss3-biography note corrected; "sheets are is thrown away" fixed on days 21,
  53, 94, 116, 158, 181; shared-cards heading now says the frame grows STANDARD section 7's cards (section 7 gives a
  grades 3 to 5 form only for the I-statement); the school's grounds policy named as the pick-up guide on days 185 and
  187 and the CPSC handbook kept for the grounds check only (scope Sources reworded); grade 4 unit 8's project is now a
  class guide to our routines for a substitute teacher day (day 75, scope unit 8, frame unit 8 row).
- **Lead call 1** (frame.md): For the lead 9 retitled "settled by CALENDAR.md rule 1"; the scope had no matching item.
- **Lead calls 4, 7, 11** (frame.md): the Brown Foundation and unit 8 project wording fixed in the frame (above).
- **Lead call 6**: 12 defect rows logged with plan.py defect (made-at scope, status fixed).
- **Lead calls 8, 14**: checked; every teaching day has codes (only Respond days are empty), and no readiness check sits
  in a note with `assess` blank. Nothing to change.
- **Lead calls 2, 3, 9, 10, 12**: nothing in this course needed them (no source-map.csv; frame.py check 0 failures;
  the scope's For the lead 1, owned codes off the checks with reasons, stands as the read did not settle a year-end item).

## Not applied

None.

## Settled (for DIGEST)

| Judgment | Reason |
|---|---|
| A Check note's "seen on day N" must name an Application day whose goal runs that skill, card withdrawn, on an unseen case | the frame's evidence rule; Fluency and first-teaching days do not count |
| A short-year fold-in never removes the only rehearsal of an assessed skill; fold a second Fluency whose task the next Application repeats | keeps "no assessed part cut" true in practice |
| Grade 5 Brown v. Board cost: job loss and refused loans only, from the NPS pages; no threats or violence | age fit, sourced |
| Grade 4 unit 8 project: class guide to our routines for a substitute teacher day | no repeat of grade 3's welcome kit within the band |

## For the structure pass

- docs/agents/lenses/sel.md (lead call 13, UK spellings): line 11 "practise" to "practice"; line 83 "behaviour" to
  "behavior" (line 82's "meta-analyses" is a noun and stays).
- scripts/unit_skeleton.py SUBJECTS holds only social studies, math, ELA and science, so sequence.py prints no rule 2
  notes for SEL (the scope's For the lead 2): add SEL (and the other after-core subjects) if rule 2 counting should
  cover them.
- Scope For the lead 3 (once-a-week form for units 12 and 17 keeping the moved Application) stays open for the lead.
- The K to 2 read's progression items (g1-rel-say-no, g2-soc-fair-rules) belong to that course's pass; nothing here.

## For Cory

None.

## Gates

- `python -X utf8 scripts/sequence.py check social-and-emotional-learning-grades-3-to-5`: 0 failures.
- `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-3-to-5`: 0 failures (unit days 60 a
  year; 18 units, 192 days).
- `python -X utf8 scripts/frame.py calendar`: no break reported for this course; no unit, day count or check week moved.
