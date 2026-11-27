# Scope group fixes: health, 2026-11-26

Fix pass on docs/reviews/scope-group-health-2026-11-26.md, per build/scope-writes/GROUP-FIX.md, with the settled calls in
build/scope-writes/AFTERCORE-FIX.md. Courses: health-grades-k-to-2, health-grades-3-to-5, health-grades-6-to-8,
health-grades-9-to-12. No unit moved, and no day count or owned row changed. No SEL or PE file was edited. Days CSVs were
edited with the csv module, keeping their quoting and line endings (CRLF for K to 2, 3 to 5 and 9 to 12; LF for 6 to 8).

## Applied

2. **Boundary steps (scope).**
   - Health 3 to 5 day 20, health 6 to 8 days 33 and 67, and the 6 to 8 scope's card list now use SEL's refusal card
     words: "say it, say it again, move away, tell". The 3 to 5 and 6 to 8 frame card tables use the same words.
   - The progression row g3-v-my-limits-and-yours (data/progressions/health.csv) had the same "repeat it, leave" words.
     That was plain wording, so I fixed it and spliced only that row back.
   - Health K to 2 keeps "say it, say stop again, move away, tell". Day 71's note, the K to 2 frame table and the
     scope's shared-cards line now name it as the young form, which grows into "say it again" in grade 3.
3. **New to Curio Class health at band entry (scope).**
   - Health 6 to 8: the 3 to 5 sentence ("a student new to Curio Class health shows any gap here and the teacher
     reteaches that step on the card the same day") is now on every grade 6 day that retrieves a grade 4 or 5 row
     (days 1, 6, 8, 10, 11, 16 to 19, 21, 23, 27, 29, 32, 35, 37 to 39), and on day 12. That covers all five days the
     read named, and more. I went wider so the band entry is handled the same way on every such day.
   - Health 9 to 12: the same sentence is on every non-sensitive day that retrieves a grade 8 row (days 3, 5, 9, 12, 16,
     19, 23, 27, 31, 37, 39, 41, 45, 46, 49, 52, 55, 59, 61, 65). Day 1 has its own line: the one-page reminder card and
     a one-minute self-rating stand in for a grade 8 log.
   - Both scopes' readiness sections gain a band-entry sentence. The sensitive units keep their leave-out bridge
     (6 to 8) and their one-page fallback (9 to 12).
   - Partly wrong in the read: 9 to 12 day 1 already ran its retrieval "on a one-page reminder card, never on students'
     own grade 8 logs". It did not assume the logs. The self-rating was the only thing added.
4. **NYTS edition (scope).**
   - The FDA results page, opened 2026-11-26 (content current as of 2026-06-23), gives 2025 middle school current
     e-cigarette use as 2.6%. It reports no "ever tried" figure.
   - Health 6 to 8 day 17 now gives 2025, 2.6% and "about 97 in 100". It notes that the CDC page still showed 2024. The
     scope's day 17 arc line, its Sources section and the frame's norms bullet match.
   - Health 3 to 5 days 8 and 51 give 2.6% for 2025. The 12.9% ever-tried figure stays, marked as the 2024 edition, the
     latest edition that reports it. The scope's unit 2 line and source list match.
5. **Speak-up plan growth (scope).**
   - Health 6 to 8 day 85 names the grade 7 step added before notice: "spot the chance" (for a person, a family or a
     community). The frame table and the scope card list match.
   - Health 9 to 12 day 21 shows the card first in its grade 8 form (6 to 8 day 130).
   - Health 9 to 12 day 61 says how each step grew from the grade 8 card. Issue comes from spot the chance and notice,
     and audience from who. Evidence is new, grown from grade 8's one sourced fact. Deliver comes from say, and judge
     the result is the grade 8 look-back. The 9 to 12 frame table names the growth.
6. **Help, decision and conflict steps (scope).**
   - Health 9 to 12 day 12 and its frame table restore "pick the right one" in the help steps.
   - Day 42 says that priorities and plan are this course's additions to the grade 8 decision card.
   - Day 39 now quotes the conflict card in the grown form the 9 to 12 frame already gives. It names the growth from the
     grade 8 card. See "Conflict card wording" below.
7. **Codes on sensitive days (scope).**
   - Health 9 to 12 days 69 and 71 to 78 add "The codes listed are practiced, not scored: this sensitive unit owns
     none." (Day 70 lists no codes.)
   - Health 6 to 8 keeps its `~` codes, as the read allows.
   - The K to 2 part is rejected (below).
8. **Sensitivity flags (scope).**
   - Health 6 to 8: every "Sensitivity (area):" or "Sensitivity:" note now reads "Sensitivity flag: <area>" with the
     private route: "cases are characters'; any student may take another case, and a student who wants help talks
     privately with the nurse or counselor".
   - Where no area was named, I named one (day 2 home and sleep, day 21 vaccines and family choices, day 32 safety and
     harm, day 56 safety and loss, day 69 body and ongoing conditions).
   - New flags in 6 to 8: safety and harm on days 66 to 68, and body on days 123 to 129. The scope's sensitivity
     paragraph states the form.
   - Health 3 to 5: flags with the grade-fit route ("talks to the teacher or the counselor") on days 6 and 80 (food), 8
     and 51 (substances), 19 (bullying, safety and harm), 36 (body and ongoing conditions) and 70 (alcohol and other
     drugs). A new "Sensitivity flags" bullet in the scope lists them.
   - "Sensitivity read" notes stay as they are. They name the sources for the sensitivity reader, not a classroom flag.
9. **6 to 8 frame seam sentence (frame).** Now reads "two grade 4 rows last used in grade 5 (retrieval)".
10. **Asthma repeat (scope).**
   - Health 6 to 8 day 69's main case is now type 1 diabetes at school, with a food allergy as the second case. Asthma
     keeps only day 70's one-line school plan.
   - Day 97 says why asthma returns: grade 8 looks at surroundings and community factors (air quality, a smoke or heat
     day, a school's plan), not the person's routine.

## Rejected

- **7, K to 2 part.** The K to 2 scope already says it (How the band runs, owned-standards paragraph): "The sensitive
  units own no id; their days leave `codes` empty except day 25's begun `~NHES.S4.2.3`, and their notes name what they
  practice." No change was needed.

## Conflict card wording (for the lead, to carry to PE)

The conflict card's words did not change anywhere:

- **Health 3 to 5 and 6 to 8:** still "stop, calm down, each says their side, find a fair way, or walk away and get
  help".
- **Health K to 2:** no change.
- **Health 9 to 12 frame:** still "calm, say what happened, listen, negotiate, walk away, get help".
- **Health 9 to 12 day 39 (the only new text):** this note now quotes the 9 to 12 frame form and adds that it grows
  from the grade 8 card. Negotiate grows from "find a fair way", and staying out of places where violence is likely is
  new.

## For the structure pass

- None from this read. Every scope finding was a wording or day-note change.

## For Cory

**1. Family-structure content and opt-outs.** Not applied.

The facts:

- Health K to 2 unit 11 (days 53 and 54) and health 3 to 5 unit 7 (days 27 and 28) treat the content on families of
  many structures as sensitive and removable, with a family note and a leave-out bridge.
- SEL K to 2 and 3 to 5 teach the same content as ordinary model content: kindergarten unit 1, grade 1 unit 11 in the
  same weeks, and the 3 to 5 model webs.
- So an opt-out of health unit 11 does not keep the content away, and the family note's promise does not hold.

The read's options:

- (a) Keep health's units sensitive, and have the family note say plainly that SEL's models show families of every kind
  all year and are not removable.
- (b) Make health's family-respect days ordinary, matching SEL, and keep the leave-out only for any body or
  relationship-history content.
- (c) SEL removes family structures from its models.

The read's pick is (b), with (a) as the honest fallback. It advises against (c), since that would cut content from a
course that has already passed its own read.

## Check results

- `python -X utf8 scripts/sequence.py check <course>`: 0 failures for all four courses.
- `python -X utf8 scripts/frame.py check <course>`: 0 failures for all four courses.
- Standing notes only: unit day counts by year, and "standard None is on no day" (call 12, left as is). There was also
  the 3 to 5 unit 20 begun-code note, which was there before this pass.
- 15 defect rows were logged with `plan.py defect --made-at=scope` (14 fixed, 1 rejected).

## Sources

- https://www.fda.gov/tobacco-products/youth-and-tobacco/results-annual-national-youth-tobacco-survey-nyts, opened
  2026-11-26 (2025: 2.6% current e-cigarette use and 4.1% current use of any tobacco product, middle school; no
  ever-tried figure).
