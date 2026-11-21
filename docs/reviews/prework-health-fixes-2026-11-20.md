# Health pre-work: stage 1 fix pass, 2026-11-20

Read: the second-model read (docs/reviews/prework-health-gemini-2026-11-20.md, findings 1 to 9 and its three
questions, the main list); the real-page findings of the two calibration reads (docs/reviews/calibration-health-2026-11-20.md,
expert #6 to #22 as listed there, and docs/reviews/calibration-health-gemini-2026-11-20.md, Gemini #5, #7, #8, #13 to
#15, whose wording was read in the Gemini report it names); the health parts of data/plans/later.csv L96; and the first
read (docs/reviews/prework-health-read-2026-11-19.md) only to see what was already handled. Settled calls read first:
DESK-ANSWERS entries for q-later-arts-health-pe, q-prework-health-pe-1 and -2, q-prework-open-1 and -2. Every map cell
was recomputed from the Serves tags in data/progressions/health.csv and checked against the 81 outcomes in
data/standards/hecat-topics.txt; every owner-row claim was checked against our words in data/standards/nhes-2024.txt.
`python -X utf8 scripts/progression.py check health`: 0 failures after the fixes.

| # | Source | What | Decision | Where |
|---|---|---|---|---|
| 1 | gemini #1, gemini cal #8, expert cal #7, L96 | Map cites PHW 13, FN 13, PA 8, S 9, T 6, which do not exist | Fixed: 9 to 12 cells now PHW 9 to 12, FN 10, 11, PA 5 to 7, S 1 to 6, 8, T 3 to 5; 6 to 8 PA 1, 2, 5, 7 (all match the csv) | STANDARD.md section 4 table |
| 2 | gemini #1, gemini cal #8, L96 | Key says care-seeking PHW 10 and 11 start in K to 2; the K to 2 cell and csv have only 11 | Fixed: key says PHW 11 starts in K to 2 (NHES.S1.2.7), PHW 10 in grade 5 | STANDARD.md section 4 key |
| 3 | gemini #1 | PHW 12 tagged on g5-fn-claims-that-hurt but the 3 to 5 cell says 1 to 11 | Fixed the map, not the row: the progression read (2026-11-19) tagged PHW 12 there on purpose; 3 to 5 cell now "All", key says PHW 12 is first met in grade 5 and judged in grade 7. Gemini's question 3c answered this way | STANDARD.md section 4 |
| 4 | gemini #1 | MEH 3 in the 3 to 5 cell, no 3 to 5 row serves it | Fixed: HECAT.MEH.HBO3 added to g5-v-conflict-steps (conflict with others, as g2 and g8 conflict rows already tag); question 3b | health.csv |
| 5 | gemini #1 | FN 12 in the 9 to 12 cell, grade 9 does not teach it | Fixed: FN 12 listed "met in 6 to 8" (g8-fn-advocacy-audience), as the settled rule says the cell lists what the semester carries (q-prework-health-pe-2); question 3a needs no Desk card | STANDARD.md section 4 |
| 6 | gemini #2, gemini cal #15 | Approach page sends items to the wrong plan fields (family note under section field 9; teacher views and disclosure under supports; rehearsal rule under supports; unit check and marking under daily evidence; "field 8" unnamed) | Fixed: every heading now names its unit or section field by UNIT-PLAN.md number; family note to unit field 9, unit check to unit field 5, marking to unit field 7, tools to unit field 8, figure sources to unit field 10, teacher views and disclosure to section field 1, daily evidence to section field 3, sensitive rehearsal to section field 7; one line says fields not named add nothing for health | APPROACH.md |
| 7 | gemini #2 | Eleven fields "dropped" | Not a fault: an approach page fills subject slots only; the shared fields stand as UNIT-PLAN.md says, now stated in one line. Gemini's added rules (group cap of four, extra time, scenario-only readiness) are new policy and were not added | APPROACH.md opening |
| 8 | gemini #2 | Check accommodations missing from section field 9 | Fixed: the existing access rule now names exit and check items too | APPROACH.md, supports |
| 9 | gemini #2 | Health needs the UNIT-PLAN.md rule 15 exception (no quoting SHAPE America verbs) | Follow-up (shared file); unit field 2 now points to STANDARD.md sections 1 and 2 | APPROACH.md unit field 2 |
| 10 | gemini #3 | Kindergarten touches no standard 8, against "each year touches all eight" | Fixed: k-s-trusted-helpers carries ~NHES.S8.2.1 (prepares asking others for help, owned in g1-meh-tell-a-helper) | health.csv |
| 11 | gemini #4.1 | No sensitivity-read trigger on the pre-work pages | Fixed: rule 8 points to the sensitivity agent (FOUNDATION.md section 7, the sensitivity-read brief) for each sensitive unit. Gemini's extension to non-sensitive units on bodies, food or family is new policy: not added | STANDARD.md section 5 |
| 12 | gemini #4.2, gemini cal #5 | 17 sensitive rows lack leave-out, family note, still-meets or disclosure pointers | Fixed: each now opens with one pointer to STANDARD.md section 5 and the approach page's disclosure steps (the rule stays stated once), and names the non-sensitive rows that still meet its ~ skills where it did not | health.csv, 17 rows |
| 13 | gemini #4.3 | g7-s-ride-gear-places has students role-play a ride refusal with no safeguard | Fixed: written scripts, a card plays the driver, no student plays an impaired driver (as g4-t-saying-no and g7-aod-turn-down-requests) | health.csv |
| 14 | gemini #5 | g7-fn-influences-on-eating drops environment, results, fair health, and says three levels | Fixed: all five levels, results and fairness in health | health.csv |
| 15 | gemini #5 | g9-t-decision-views-process drops "why" | Fixed: "when and why" | health.csv |
| 16 | gemini #5 | g7-phw-credible-sources checks information only, not products and services | Fixed: adds a credible place for a product and a service | health.csv |
| 17 | gemini #5 | g4-fn-food-claims-source-check has no service example; g9-v-advocacy-adjust has no environment example | Fixed: a flyer for a health service; an ask for cleaner air or more shade | health.csv |
| 18 | gemini #6, expert cal #15 | One k-12 health row in data/courses.csv against four band courses | Question for Cory (catalogue rows) | below |
| 19 | gemini #7 | No short path stated | Fixed as a pointer: each band's scope and sequence names its short path (bar C2 puts it there). What a short path drops is the frame's call, so Gemini's question 2 needs no Desk card now | APPROACH.md, pacing |
| 20 | gemini #7 | Default sessions say "about" | Not a fault: the defaults are ours and untested, and each band frame sets its exact count with a reason | none |
| 21 | gemini #8, expert cal #9 | Science lean claims puberty, germs and nutrition lean on science; the csv has health state those facts itself | Fixed: science bullet names MS-LS1-1 and MS-LS1-3 and says health states germ, vaccine, puberty and body-name facts itself; one line points to the csv column for every lean's code (codes not copied a second time) | STANDARD.md section 8 |
| 22 | gemini #8 | MS-LS1-1 and 6.SP.B.5 sit late in grade 6 | Not a fault at pre-work: placement within the year is the grade 6 frame's; the 6.SP.B.5 lean already says "after the grade 6 statistics unit" | none |
| 23 | gemini #9, gemini cal #13 | Stale lines: STANDARD "APPROACH.md (draft)", "ids only" in STANDARD section 1 and the nhes-2024.txt reuse note | Fixed | STANDARD.md lines 3 to 7 and 22; nhes-2024.txt header line 11 |
| 24 | gemini #9 | Stale "(draft)" in the lens and "approach page's yes" owed in ADOPTION-BAR-SUBJECTS.md | Follow-up (files not mine) | below |
| 25 | gemini #9 | g6-phw-prevent-illness-injury says the idea is not taught in between, yet g5-s-choose-safe-option carries ~S1.5.3 | Fixed: says grade 5 carries only the injury side; illness prevention has no grade 5 row | health.csv |
| 26 | gemini cal #7 | Grade 4 to 6 jumps and the source-check chain | Not a fault on the real page: g5-phw-health-information assumes g4-fn-food-claims-source-check; g4-phw-prevent-illness-injury and g4-meh-calm-stress both hand on to grade 5 rows | none |
| 27 | gemini cal #14 | K to 2 cell names V 8, rule 1 says V 8, 9 for K to 5 | Fixed: rule 1 says V 8 from K, V 9 from grade 3 (matches the map and csv) | STANDARD.md section 5 rule 1 |
| 28 | expert cal #6 | General help-seeking (MEH 6) sits only in sensitive units | Not a fault: MEH 6 in sensitive units was placed by the 2026-11-19 fix; getting help is taught in non-sensitive units every band (rule 3: g4-meh-help-with-feelings, g7-meh-seek-and-give-support, g9-meh-help-and-concern) | none |
| 29 | expert cal #8 | "At least in alternate years" against "Topics return each year" | Fixed: the second line now points to the first | STANDARD.md section 4 |
| 30 | expert cal #13 | No national use survey exists for grades 3 to 5, yet g3-t-tobacco-facts and g5-aod-refuse-alcohol-drugs ask for one | Fixed: the approach page's understanding day says what a unit below grade 6 does (the norm in plain words, the nearest figure named for its age); the two rows point to it. That national youth use surveys begin at grade 6 is from memory, marked so | APPROACH.md, kinds of day; health.csv |
| 31 | expert cal #12 | A child calling 911 (judgment) | Not a fault at pre-work: the reader's wording was not seen; g4-s-get-help-emergency already teaches what an emergency is and giving a name and place; who places the call is a unit-plan wording for the section 6 read against current guidance | none |
| 32 | expert cal #17 | "Bottom" in the body-names row | Not a fault: Cory's word (2026-11-21, q-prework-open-1) | none |
| 33 | expert cal #18 to #22 | Minor real-page findings | Follow-up, not seen: the calibration report lists them by number only and the reader's report sits in the calibration folder this pass may not open | follow-up |

## Questions for Cory

1. Catalogue rows (item 18): split the single k-12 health row in data/courses.csv into four band rows (health-k-2,
   health-3-5, health-6-8, health-9-12, the last one semester in grade 9), as was done for SEL and ELD on 2026-11-21.

## Follow-ups for the lead

- docs/courses/UNIT-PLAN.md rule 15: add Health beside Arts and Computer Science (cite the NHES id and give its
  action in our own words; the indicator's wording is never quoted).
- docs/agents/lenses/health.md line 7: "docs/courses/health/APPROACH.md (draft)" is stale (approved 2026-11-21).
- docs/ADOPTION-BAR-SUBJECTS.md health row (line 564): "the approach page's yes (Desk q-prework-open-1)" is still
  listed as owed; it was given 2026-11-21.
- Expert calibration minor real-page findings #18 to #22 (docs/reviews/calibration-health-2026-11-20.md): their text
  is not in the repository; read them from the calibration report and send any that stand to the next health fix.
- No PE change is needed from this pass: the health map still names PA 3, 4 and 6 in grades 6 to 8 as taught in PE.

## Follow-ups done 2026-11-21

- Expert calibration minors #18 to #22: not done. Their text is only in the reader's report in the calibration folder, which this pass may not open; the calibration review lists them by number only. No health page or progression row changed.
