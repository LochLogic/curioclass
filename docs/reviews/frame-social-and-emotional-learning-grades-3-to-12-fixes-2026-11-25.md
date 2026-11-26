# Frame fixes: Social and emotional learning, grades 3 to 5, 6 to 8 and 9 to 12 (2026-11-25)

The one fix pass of COURSE-RUN stage 3 for the three SEL frames after K to 2, after the fresh expert read
(docs/reviews/frame-social-and-emotional-learning-grades-3-to-12-2026-11-25.md) and the three second-model reads
(docs/reviews/frame-social-and-emotional-learning-grades-{3-to-5,6-to-8,9-to-12}-codex-2026-11-25.md). Run beside the
health 3 to 12 fix pass (docs/reviews/frame-health-grades-3-to-12-fixes-2026-11-25.md), so health now quotes SEL's
cards word for word.

Files changed: docs/courses/social-and-emotional-learning-grades-3-to-5/frame.md, docs/courses/social-and-emotional-learning-grades-6-to-8/frame.md,
docs/courses/social-and-emotional-learning-grades-9-to-12/frame.md, data/progressions/sel.csv (27 notes cells: 7 in
grades 3 to 5, 16 in 6 to 8, 4 in 9 to 12; no row id moved or renumbered, no hands_on or assumes cell touched), and
data/plans/frames.csv, data/plans/calendar.csv and docs/courses/CALENDAR.md through `frame.py sync`. Short-path check
weeks moved in 3 to 5 (below); no full-path check week moved.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 117 courses; calendar.csv 2119 rows |
| `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-3-to-5` | 0 failures; 18 units, 192 days (180 in units, 12 for checks and respond days) |
| `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-6-to-8` | 0 failures; 18 units, 192 days (180 in units, 12 for checks and respond days) |
| `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-9-to-12` | 0 failures; 24 units, 256 days (240 in units, 16 for checks and respond days) |
| `python -X utf8 scripts/progression.py check sel` | 520 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |
| Other frames' SEL unit citations (scripted, every docs/courses/*/frame.md) | Career 6 to 8 and 9 to 12, PE 3 to 5 and PE K to 2 agree with the SEL tables; PE 9 to 12 lines 317 and 334 do not (Left for the lead 3) |

## Findings

38 findings: 31 applied, 7 kept or sent on with a reason (J1, J2, J3, m2, and the ownership-check half of each read's
library finding, which is the validator's).

| Read | # | Finding | Applied or kept | What changed, or why not |
|---|---|---|---|---|
| Expert | S1 | 9 to 12 I-statement reworded, not grown | Applied | Shared steps, Models carried and unit 4: "I feel ___ when ___ because ___. I need ___. Does that work for you?" ("I need" is the request; the check-back is the fifth part). Leave-out says "five-part". Row g9-rel-friendships matches. Health 9 to 12 quotes the same card |
| Expert | S2 | Brown carries SO6 four times, twice in 6 to 8 | Applied | 6 to 8: grade 7 unit 9 takes the Nineteenth Amendment (1920), grade 8 unit 16 Section 504 (1973) or the ADA (1990), each from a National Archives page (named from memory, browser check if it blocks) plus a community account named at the unit plan; rows g7-soc-fair-rules and g8-soc-fair-rules match with teacher notes. Brown stays in 3 to 5 grade 5 and 9 to 12 grade 10 unit 9, which now says it is a deliberate return at new depth |
| Expert | M1 | SEL unit numbers differ from neighbors | Applied | The SEL frames already number through the band; health 3 to 5, 6 to 8 and 9 to 12 SEL tables now use band numbers with year and weeks. sel.csv notes keep year numbers, as the read advised. The one-line note in SEL STANDARD section 3 is the lead's |
| Expert | M2 | Widened Check over-full; item counts disagree | Applied | 3 to 5 and 6 to 8 Course-level checks: "at most two sampled items, written only; sampled steps are never a second rehearsal"; each check cell trimmed to two written samples; five items at most on the page. 6 to 8 adds individual look-fors, a probe-set cap on unfinished pairs and a short-path minute budget (5, 12, 8, 5); 9 to 12 adds the same cap and its budget (5, 15, 13, 7) |
| Expert | M3 | 6 to 8 loses the 3 to 5 card lineage | Applied | 3 to 5 Models carried adds refusal steps, upstander plan, care steps and focus plan with their units; 6 to 8 Models carried moves refusal, fairness questions, who-is-affected map and upstander plan into rows saying what grade 6 adds; the "New in this band" paragraph is replaced. Rows g6-rel-stand-up and g6-rel-ask-offer-help get the read's step-up clauses |
| Expert | M4 | Health and SEL claim the I-statement in different words | Applied | Health 3 to 5 now uses "I need ___"; SEL 3 to 5's shared-steps line says health uses the same cards |
| Expert | m1 | Stale "not written" and "being written" notes | Applied | 3 to 5 lines 124 and 169, For the lead 5 and the CS row (g5-team-project in unit 3 of Computer Science, Grade 5, weeks 11 to 17); 6 to 8 For the lead 8; 9 to 12 CS table (grade 11 unit 5, weeks 25 to 28; grade 12 unit 3, weeks 13 to 23; grade 12 unit 5, weeks 29 to 32) and For the lead 8 and 12 |
| Expert | m2 | "judgement" did not land | Kept (lead) | None of the six frames holds it; it is in docs/courses/sel/STANDARD.md lines 100, 132, 154, 157, 216 and the SEL lens line 37, which are shared docs |
| Expert | m3 | Calm-down step changes its word | Applied | 6 to 8 Models carried, unit 3 and carry-out, 9 to 12 Picked up and Models carried: "stop, breathe, name it, choose, go on"; row g6-sm-calm-down matches. PE 6 to 8's two cue lines are the lead's |
| Expert | m4 | "Every unit sampled twice" untrue | Applied | 9 to 12 Course-level checks take the read's sentence: units 1, 2, 4 and 5 are sampled once more; units 3 and 6 return in the next year's retrieval openings |
| Expert | m5 | Partner customs named by kind only | Applied | 3 to 5 and 9 to 12 Base text: the unit plan names the one custom's source and the sensitivity read checks it; 3 to 5 names what to avoid now that PE and K to 2 are written (PE's jianzi and Pilolo, PE grade 4 unit 16; K to 2's Ampe and acchi muite hoi) |
| Expert | J1 | 3 to 12 fold course checks into Check sessions; K to 2 does not | Kept | No frame change, as the read says; the K to 2 For Cory card should mention that 3 to 12 kept 11 and 10 by folding (Left for the lead 6) |
| Expert | J2 | Grade 6 depth is "a choice among options" in most rows | Kept | Rows left, the read's pick; the rows already hold the pressure. The grade 6 scope writer names the pressure in each Application (a scope-stage note, Left for the lead 7) |
| Expert | J3 | 3 to 5 grades 4 and 5 run three two-group units before mid-year | Kept | Accepted, the read's pick: allowed by STANDARD section 2 and no two-group unit holds more than six rows |
| Codex 3-5 | 1 | Complete placement masks partial treatment of two standards | Applied | SA5 values in units 1, 10 and 13 with evidence; SA2 in unit 18 (an invented character's cultural or linguistic strength). Rows g3, g4, g5-sa-feel-think-link and g5-sa-my-strengths match |
| Codex 3-5 | 2 | Leave-out misses a dependency and carried models | Applied | Leave-out adds care steps (unit 3 to 10, 16), refusal and upstander (unit 5 to 11, 16, 17), focus plan (unit 6 to 8, 14) and the working agreement (unit 7 to unit 8 bridge); the blanket grade 4 and 5 assurance becomes a check; a bridge never restores the claim |
| Codex 3-5 | 3 | Short path puts two checks in core check weeks | Applied | Short-path unit sizes: grade 3 5, 6, 5, 6, 5, 5 (checks weeks 11 and 27); grade 4 5, 5, 5, 6, 5, 6 (weeks 15 and 26); grade 5 5, 5, 5, 6, 6, 5 (weeks 15 and 27); every short-path check clear of core checks |
| Codex 3-5 | 4 | Widened checks exceed their sampling limit | Applied | As expert M2; unit 8's retrieval gets the grade 3 if-then item and unit 15's the grade 4 source-check item, so the trimmed samples return |
| Codex 3-5 | 5 | Library transfers outside the ownership record | Applied (path); kept (validator) | Path corrected to data/progressions/library-excluded.csv. The ownership check for the three AASL codes is the Pending marker already in the Standard bullet: validator support is the lead's |
| Codex 3-5 | 6 | Health seam specifies competing cards | Applied | Health seam intro and rows rebuilt: one card set, SEL's words, health units and weeks |
| Codex 3-5 | 7 | Friendship rehearsals contradict the role rule | Applied | Units 4, 11 and 16: the teacher or a scene card supplies the unkind or pushing words and the partner coaches; rows g3, g4, g5-rel-friendships match |
| Codex 3-5 | 8 | Stale status notes and a file pointer | Applied | As expert m1, plus the library path |
| Codex 6-8 | 1 | Hallway rehearsal assigns a prohibited role | Applied | Unit 3: the hallway scene is replaced by the teacher modeling a plan falling apart before a class display; row g6-sm-big-feelings matches |
| Codex 6-8 | 2 | Complete placement masks partial treatment | Applied | SA5 values in units 2, 10 and 13; SA2 in unit 14 with its evidence point; RS3 ways of working with cited sources in units 6 and 7 and a Deaf and hearing team in unit 16 (Deaf-Hearing Communication Centre tips, https://www.dhcc.org/resources/communication-tips; no simulation of hearing loss); rows match |
| Codex 6-8 | 3 | Leaving out unit 2 breaks unit 3 | Applied | Leave-out adds unit 3's bridge for the feelings scale and the think-feel-do chain (unit 2 to 10, 13) |
| Codex 6-8 | 4 | Widened checks lack a bounded workload and evidence placement | Applied | As expert M2; units 14 and 18 place each owned skill in Application or Check (unit 18: SM4, SM6, SM7, RS7, RD3 in Application; RS9, RS4, RD6 in Check); the Evidence bullet says every grade 8 owner unit plan names its split, unit 18 the model |
| Codex 6-8 | 5 | Library transfers outside ownership checking | Applied (path); kept (validator) | As Codex 3-5 finding 5 |
| Codex 6-8 | 6 | Model register misstates inheritance and changes shared wording | Applied | As expert M3 and m3 |
| Codex 6-8 | 7 | Historical pack lacks the community's own voice | Applied in part | Each settled case now names an archive page plus a community account at the unit plan, and the sensitivity read checks both. Codex's wish to keep Brown in grade 7 was not taken: the expert read settled no case twice in a band (For the lead 11 records the reason) |
| Codex 6-8 | 8 | Living notes describe done work as pending | Applied | For the lead 4, 5, 6, 7 and 8 rewritten as done or as lead items; SM5 materials system added to unit 15 (row g8-sm-plan-and-tidy) |
| Codex 9-12 | 1 | High school I-statement replaces the shared wording | Applied | As expert S1 |
| Codex 9-12 | 2 | Leave-out bridges teach the wrong depth and miss a receiver | Applied | A bridge teaches the card's one-step form in the first ten minutes; unit 2 is named as the first receiver of unit 1's look-back step, with its bridge; the 6 to 8 cards name their first 9 to 12 users (units 4, 5, 5, 6). Days: a Given: item is used only where a class did not meet the earlier form; it is the readiness evidence, kept apart from the reteach |
| Codex 9-12 | 3 | Annual teaching narrows a sub-skill before its owner year | Applied | SM5 materials and records in units 1, 11 and 14; RS3 in unit 3 (one member's way of disagreeing from a cited source, each preference asked) and unit 16 (a Deaf and hearing team, the DHCC tips, no simulation) |
| Codex 9-12 | 4 | Evidence plan does not secure several owner-year checks | Applied | Unit 20 places SA8, SM3 and SM5 in Application and SA3, SM2 and SM1 in the Check; the Evidence bullet asks every grade 12 owner unit to name its split, gives each student their own look-for in pair work, and allows writing or a card |
| Codex 9-12 | 5 | Library transfers outside ownership checking | Applied (path); kept (validator) | As Codex 3-5 finding 5 |
| Codex 9-12 | 6 | Preparation sources deferred | Applied | Base text names each case's sources and community: Mendez (U.S. Courts account with Sylvia Mendez's words), Brown (National Archives and the Brown Foundation, ruling told apart from carrying it out), Morgan (Library of Virginia; a community account needed before any personal cost is taught), Heart of Atlanta (Library of Congress exhibition; unit 22 now says "covered public accommodations"). Oyez pages are browser check. Safety names Colorado's field-trip school nurse checklist |
| Codex 9-12 | 7 | Living notes describe completed work as absent | Applied | CS table and For the lead 4, 5, 8, 11, 12 and 13 rewritten; calendar paths now data/plans/calendar.csv; health seam weeks corrected from the health frame (unit 8 week 6; unit 21 week 16) |
| Codex 9-12 | 8 | "Every unit sampled twice" overstates | Applied | As expert m4 |

Where the reads disagreed: Codex 6-8 finding 7 would keep Brown in grade 7 with stronger sources; the expert read
settled that no case repeats in a band. This pass took the expert's pick and kept Codex's source rule for the new
cases.

### Calendar clashes

Not moved, per the lead's instruction. The full list is in SEL 3 to 5 For the lead 9 and the expert read's "Clashes for
the lead's calendar pass".

## Pattern notes

- A card's wording lives in SEL STANDARD section 7; every frame and every health or PE line quotes it word for word.
- A partner never plays an unkind, pushing or abusive part: the teacher or a scene card supplies the words and the
  partner coaches.
- "Owned in full" means every clause of the code has a teaching place and an evidence point, named in the unit.
- A settled case carries its community's own account, not only an archive page, and no case repeats in a band.

## Left for the lead

1. SEL STANDARD: section 7 forms for 6 to 8 and 9 to 12 as the frames now quote them; section 3 one line saying
   sel.csv notes number units by year and frames by band (M1); "judgement" to "judgment" at lines 100, 132, 154, 157
   and 216, and the SEL lens line 37 (m2).
2. Validator support for the three AASL codes placed in SEL (all three bands' Pending markers).
3. PE 6 to 8 cue lines 288 and 305: "pick a tool" to "choose". PE 9 to 12 line 317: "SEL 9 to 12 unit 2's goal steps"
   should be unit 6 (or unit 1); line 334: "unit 22's balanced week" should be grade 9 unit 5's balanced week or unit
   20's changed-month plan; its docs/plans/calendar.csv path.
4. Career exploration 6 to 8: its obsolete Pending paragraph on SEL.
5. The adoption-bar SEL status row and the DESK-ANSWERS lines for the settled choices.
6. The K to 2 For Cory card: say 3 to 12 kept 11 and 10 by folding the checks (J1).
7. A grade 6 scope-writer note: name the pressure in each Application (J2).
8. Browser checks: the Oyez Morgan and Heart of Atlanta pages, and the National Archives Nineteenth Amendment and
   504 or ADA pages, opened in Claude in Chrome.
9. The calendar clashes above, and a Spanish translation brief for the family notes.

## For Cory

1. **Grading or credit for SEL 9 to 12 (scope).** Pick: Curio Class makes no credit claim; credit is the school's
   choice.
2. **Supply ceiling (money).** About $55 to $60 a year printing, plus up to $20 a pilot in 9 to 12. Pick: set none
   until the unit plans price the quantities.
3. **Unit sizes across bands (scope).** 3 to 12 keep 11 and 10 by folding the checks; K to 2 uses 11 and 8. Pick:
   accept both shapes.
4. **Annual check placement (scope, Codex 3-5 For Cory 1).** Each year-end check comes before a full last unit, with
   that unit sampled the next year. Pick: accept.
