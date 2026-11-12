# Handoff: the one current-state page

**This is the single page that says where the work stands and what to do next. Last updated 2026-11-12, after
unit 11.1 was built (all but its tool). Everything here is pushed to `spec/sara` and `main`.**

[ROADMAP.md](ROADMAP.md) holds the order of work only. Its history is in `docs/archive/`. If another page
disagrees with this one, the other page is stale: check the date, fix it, and say so.

## Start here: the next action

The pilot unit comes first (grade 4 math unit 11.1, [courses/math-4/s11.md](courses/math-4/s11.md)). In order:

1. **Done 2026-11-12: cold expert read of `s11.md`**, revised once
   ([reviews/unit-plan-s11-2026-11-12.md](reviews/unit-plan-s11-2026-11-12.md)): 15 findings, none for Cory,
   verdict "the build can start". `scripts/plan.py check` passes (18 items, 31 wrong answers). Sara's own read
   as a teacher is still owed at the top of that report; it does not hold up step 2.
2. **Written, read, revised: [courses/LESSON-DAY.md](courses/LESSON-DAY.md), draft 2 (2026-11-12). Approved by Cory
   2026-11-12** (Desk card `q-lesson-day`; DESK-ANSWERS). What one teaching day ships as, with sizes, written against day 90
   ([courses/math-4/u11-1/d090.md](../courses/math-4/u11-1/d090.md)). `scripts/lesson.py check` and `build --pdf`
   gate and print it. The expert's cold read
   ([reviews/lesson-day-2026-11-12.md](reviews/lesson-day-2026-11-12.md)) had 13 findings: 1 to 7 were made
   before asking Cory (display carries figures and steps from data; the tool's exit items are rows with
   `path`; `leans_on` and "not ready"; the credit rule refuses ND and puts `source` on rows; the student count
   includes the questions; "What changes by subject"; a foot line with version and licence). 8, 9, 12 wait for
   the taught run (defects.csv, status open). Day 90 is "draft 2, not ready": the tool, the unit opener, the
   facts check sheet and the record sheet do not exist yet.
3. **Keys as data: built for stretch 11** (`data/plans/`, `scripts/plan.py`; see "Plan weight"). The lesson
   days' own items go in as rows while the pilot is written.
4. **Unit 11.1 built 2026-11-12, all but its tool.** In `courses/math-4/u11-1/`: days 89 to 93, the opener, the
   readiness check, the record sheet, the family note (English and Spanish), `sheet-d091.md`; the two facts-check
   sheets are in `u01-1/`. Every day passes `lesson.py check` (two sides each) and `plan.py check` (70 items, 79 wrong
   answers, 0 failures). Days 89, 91 and 92 build "ready"; day 90 waits on Community Plot Planner; day 93 leans on
   stretch 12's readiness check, which is frozen with the rest of planning. New this round:
   - `lesson.py` builds "pieces" (opener, record, check, facts, family, sheet) and check days (answers display,
     look-fors in the key from the `steps` cell of judged end items).
   - The generator sheet is the measure-shapes skill `formulas` (preset math-4 #40 in
     `data/closet/worksheets/generated.csv`). `plan.py reserve math-4 11` writes the unit's number sets into the
     generator so it never repeats them, and `plan.py check` fails when that list is stale: run it after any
     items.csv change in stretch 11.
   - Shelf: anchor chart `data/closet/charts/math-4-area-and-perimeter-formulas.md`; family game
     `data/closet/games/fence-or-floor.md`.
   - Community Plot Planner is the first build in the Codex queue (`codex_queue.py` PILOT), with a note sending the
     builder to d090.md and the TOOL-ASKS asks. Codex needs main merged into `codex/queue` first.
   - Costs: [pilots/COST.md](pilots/COST.md). One agent per day cost 128,000 to 137,000 tokens.
   - **Done 2026-11-12: expert cold reads of days 89, 91, 92, 93** (docs/reviews/day-0NN-2026-11-12.md): 50 findings,
     none for Cory, 35 in the process; settled fixes applied and logged in defects.csv. Each read cost about 170,500
     tokens (COST.md). How often to read from here: [pilots/REVIEW-CADENCE.md](pilots/REVIEW-CADENCE.md).
   - **Decided 2026-11-12, card 111 `q-plan-after-11-1`** (DESK-ANSWERS): one more full expert read on every day of
     the next unit, then spot checks; grade 4 math is the main thread, with the ELA and science pilots alongside once
     11.1 has its teacher read and no other math course before them; tools held until the frame is built, except
     Community Plot Planner and Codex's non-course queue until 2026-11-30.
   - **Now: stretch 10 (days 79 to 88, units 10.1 to 10.3)**, the next unit. Its prose plan goes into data first
     (`plan.py check`), then one agent per day as for 11.1, then a full expert read on every day (REVIEW-CADENCE.md
     step 2). Costs go in COST.md.
   - Still owed: the Spanish family note needs a qualified reader; the module has no Word Wall cards of its own
     (area, perimeter, square unit, formula, length, width exist under other modules), which is the Word Wall
     owner's to add; the plan should say where day 90's two "On your own" items go when day 91's warm-up is the facts
     check (day 91 agent); day 92's written task has no slot for feedback on day 93, so the teacher page hands it back
     at the door (day 92 agent); figure cells cannot label mixed numbers yet (day 91 used 6¾).
5. **People.** Cory is arranging a grade 3 to 5 teacher, one taught run and three timed students
   ([pilots/README.md](pilots/README.md)). Their notes change the templates.
6. **After the pilot is read:** fix the templates, then the first ELA pilot (grade 6, stretch 2, five days) and
   the first science pilot. ELA is nearly ready to plan: its rubric page, approach page and rights list exist
   (see "Where things stand"). Science has none of the three yet (Sara's piece 3).

**Waiting on Cory (all on the Desk and asked in chat on 2026-11-12):**

- (Answered 2026-11-12: card `q-ela-piece-2`, see "Decided 2026-11-12" below.)
- Whether the four untracked files in `S:\CurioClass` belong in the repository (see "The folders").
- Move the other five planned stretches (1, 2, 3, 9, 10) into data now, or when each is next opened? The
  standing answer is "when next opened" (UNIT-PLAN.md) and the assistant's advice is to wait for the pilot:
  the row shapes will change once a lesson day exists.
- In or not-now for the six extra pieces of a finished course (ROADMAP, "What a finished course holds",
  items 10 to 15).
- (Answered 2026-11-12, card `q-course-texts`: K-8 anchors on newer texts, mostly our own; 9-12 may anchor on
  Reading Room texts; the grade 6 ELA pilot gets a new hero story as anchor and a retold myth as its pair, and its
  rights list is redone. See DESK-ANSWERS.)
- (Answered 2026-11-12: shelves, the feedback note, no slides, build unit 11.1 now. See DESK-ANSWERS.) His read
  of the approach pages, and his final yes on the science and ELA spines, are still owed from before.

**Frozen until the pilot is read:** new spines, stretch sheets, unit plans and specs. One exception: the grade 4
start-of-year check and stretch 4's readiness items (Sara's piece 4).

## Decided 2026-11-12: card q-ela-piece-2 (ELA)

> 1, yes. 2, I agree with you. 3, i agree with you. 4, lets do our own research and find our own preferred
> document. 5, i agree with you but if it doesnt work later, we find a new story. 6, use your suggestion but add
> a note to upgrade to a free source later.

1. **Grades 3 to 5 ELA teach foundational skills.** The rubric's first gateway applies in full and each of
   those spines starts from a taught sequence (`RUBRIC-ELA.md`, `APPROACH-ELA.md`).
2. **`APPROACH.md` principle 3** takes the expert's wording on modelling in reading and writing.
3. **ELA text records, question sets and word lists are rows in `data/plans/`**, shown as generated tables
   outside the word cap. The row files are named in `UNIT-PLAN.md`; they are built with the first ELA pilot plan.
4. **The fallback second hero:** we do our own research and pick our own preferred document. The verse
   Ramayana on file is not used. Report: `docs/reviews/fallback-hero-ela-6-2026-11-12.md`. Cory, the same day:
   "The Ogre of Rashomon sounds fine to me, lets go with that". It is row 5 of the rights list: Yei Theodora
   Ozaki, Japanese Fairy Tales, the tale whole, 2,244 words; found, not yet second-read; a sensitivity read is
   owed.
5. **The Monkey King:** teach the 2,000-word cut now; write a labeled Curio Class retelling before stretch 2 is
   called finished; if that does not work, a new story takes its place. An outside reader from the culture still
   needs Cory's separate yes.
6. **Background text two:** a short labeled Curio Class explainer (500 to 700 words), with a standing note to
   replace it when a suitable free source is found. Not written yet; it is part of the ELA pilot build.

## The folders (cleaned up 2026-11-12, on Cory's yes)

The truth is the GitHub repository, branch `main`. Each folder is a working copy of it.

| Folder | Branch | Who works there |
|---|---|---|
| `S:\CurioClass` | `main` | **The main session, from now on.** Brought level with GitHub on 2026-11-12 |
| `S:\CurioClass-spec2` | `spec/sara` | Sara's sessions only |
| `S:\CurioClass-codex` | `codex/queue` | Codex. Merged into `main` on 2026-11-12 (Cory: "Review, then merge"); the folder stays for Codex to work in |
| `S:\CurioClass-archive` | none | Not a working copy. Holds what the clean-up set aside (below) |

What was done, with nothing deleted that was not first saved:

- **Word Wall work** that sat uncommitted in `S:\CurioClass` (215 word pictures, 13 word lists, the media
  manifest) was checked (`scripts/check_words.py`, 0 problems), committed and pushed to `main`.
- **Left untracked in `S:\CurioClass` on purpose** (this is a public repository, and these may be private):
  `docs/Curio-Class-Plan.pdf`, `docs/US Curriculum Design Blueprint.pdf`, `docs/Return/`,
  `docs/agents/audit/wordwall-movement-cards.jpg`. Cory says whether any belongs in the repository.
- **Antigravity** (Cory: "no longer needed"): its working copy was removed. Its 5 commits stay on GitHub as
  branch `agy/build`. Its 8,846 files that git ignored (scratch work, prompts, raw art) were copied to
  `S:\CurioClass-archivegy-2026-11-12` and compared byte for byte first.
- **`S:\CurioClass-codex-scratch`** was moved, whole, to `S:\CurioClass-archive\codex-scratch-2026-11-12`.
- **The Codex branch was reviewed and merged** (2026-11-12): 141 new files and 5 changed, all under `tools/`
  (builds of globe-theatre-stage, equation-balancer, mole-bakery, star-life-story, rigid-motion-twins,
  thesis-workshop and smaller pieces). No conflict with `main`, no tool went live (live count still 83), and
  `check_tools`, `check_safety`, `check_games` and `check_words` pass. These tools are still in the frozen bin
  (BASELINE rule 26): merging saved the work, it did not restart it. Found in passing, not caused by the merge:
  `scripts/check_concepts.py` reports an unknown module `social-studies-3-5-road-trip-atlas` at
  `social-studies.txt` line 135.
- **For Cory to delete by hand** (a safety check stops the assistant removing top-level folders): the two empty
  folders `S:\CurioClass-audit` and `S:\CurioClass-agy`. The archive folder can go whenever he is sure.

## How to work here

- **The main session works in `S:\CurioClass`, branch `main`** (since 2026-11-12): `git pull -q --rebase origin
  main`, then `git push -q origin HEAD:main`. Sara's sessions work in `S:\CurioClass-spec2`, branch `spec/sara`,
  and push to both (`git push -q origin HEAD:spec/sara`, `git push -q origin HEAD:main`). Do not edit in the
  other session's folder. Pull before starting: the other session pushes to `main` too. "Bypassed rule violations" on main is normal. Commit only your own files.
- No em dashes anywhere. Always "Curio Class" in full. Never say Curio Class was reviewed by, meets or is
  endorsed by anyone. Public copy names no companies. Outside rubrics are linked and put in our own words.
- Do not touch the Word Wall files (`data/closet`, `closet/words`, `data/media-manifest.txt`).
- A background agent that is editing files blocks `pull --rebase`. Commit and push after it finishes.
- The working pattern: a writer agent drafts; commit; the curriculum expert reads it cold (a fresh agent told to
  read [agents/EXPERT.md](agents/EXPERT.md) first; report goes to `docs/reviews/<what>-<date>.md`); revise once;
  anything that changes what a course teaches or a decided rule goes to Cory on the Review Desk **and** in chat.
- Records to update after every decision: this page, and one dated entry in
  [agents/decisions/DESK-ANSWERS.md](agents/decisions/DESK-ANSWERS.md) with Cory's words. ROADMAP changes only
  when the order of work changes. A rule goes in BASELINE. The assistant's memory notes point here.
- What goes to Cory is narrower since 2026-11-11: scope, audience, money, outside people, and anything that moves
  a standard between units. Item-level choices are settled by the expert and go in a weekly digest
  ([reviews/DIGEST.md](reviews/DIGEST.md), started 2026-11-12: copy each report's "Settled by the expert" table
  into it).
- The Review Desk is https://claude.ai/artifact/SVXBzgyS941dyqmEzQHgNC. A question card has status `question`,
  then `answered`. Cory answers in a comment on the card. Next free card order: 109. Sara's session cannot open the Desk; the main session places her cards. After changes, refresh the
  Dashboard with `python -X utf8 scripts/course_status.py <out.json>` (Desk doc `stats/courses`) and the Roadmap
  tab with `python -X utf8 scripts/desk_roadmap.py <out.json>` (Desk doc `stats/roadmap`).
- Core subjects first (BASELINE rule 24, a soft goal): see "The order after the pilot".
- Cory's standing rules that bite most often: every one of the 105 courses is finished to the adoption bar (a
  firm bar; never call it unrealistic); no countdown timer shown to a student; no library or paywalled access;
  teach first by default in grades 2 to 5; Cory wants pushback and welcomes questions about earlier decisions.

## Where things stand

| Layer | State |
|---|---|
| 1 Foundation | [FOUNDATION.md](FOUNDATION.md). Done. |
| 2 Standards | `data/standards/`. Checked 2026-11-11: nothing superseded; gaps listed below. |
| 3 Approach | [APPROACH.md](APPROACH.md), [APPROACH-MATH.md](APPROACH-MATH.md). Decisions answered. Cory still owes a read of the pages as a whole; his mother is reading "The principles" onward as a grade 2 teacher. ELA: [APPROACH-ELA.md](APPROACH-ELA.md), drafted 2026-11-11, read by the expert, revised once; two points wait for Cory. Science approach page: Sara's piece 3 ([courses/NEXT-SPINES.md](courses/NEXT-SPINES.md)). |
| 4 Progressions | Math grades 3 to 5 done. |
| 5 Spine | Grade 4 math, plus science and ELA spines waiting for Cory's final yes. 3 of 105 courses have a spine. |
| 6 Stretch sheets and unit plans | Fields fixed in [courses/UNIT-PLAN.md](courses/UNIT-PLAN.md). Word caps are 1,250 (unit plan), 1,250 (stretch sheet) and 1,800 (one-unit stretch) since 2026-11-11. Grade 4 math: stretches 1, 2, 3, 9, 10 and 11 are planned, which is 13 of 43 units (the status table shows 17 because it counts stretch sheets too). 30 units to go (stretches 4 to 8 and 12 to 18). **Planning is frozen at these six until the pilot is read.** |
| 7 Lessons, tools, print | Unit 11.1 (grade 4 math) is built but for its tool, see "Start here" step 4. Template: [courses/LESSON-DAY.md](courses/LESSON-DAY.md). |
| Texts (ELA) | Grade 6 stretch 2 only: [courses/ela-6/RIGHTS.md](courses/ela-6/RIGHTS.md). Every row is "found, not yet second-read"; fifteen questions wait for the second reader (a person, FOUNDATION 7.3). No text is taught before that read. |
| The bar | Math: [RUBRIC-MATH-K8.md](RUBRIC-MATH-K8.md). All other subjects but ELA and science: [ADOPTION-BAR-SUBJECTS.md](ADOPTION-BAR-SUBJECTS.md), second draft. ELA: [RUBRIC-ELA.md](RUBRIC-ELA.md), drafted 2026-11-11, read by the expert, revised once. Science rubric file: Sara's piece 3. |

Course count: 105, of which 56 are in the four core subjects ([COURSES-STATUS.md](COURSES-STATUS.md), generated;
never edit by hand). World languages are shelved (see below) but still counted in the table, as a reminder (Cory).

## What Cory decided on 2026-11-11 (evening), in his words

### Card q-plans-4d-1: grade 4 math plans

> 1, yes. 2, yes. 3, yes but mark for follow up after more progress. 4, agree. 5, yes. 6, yes, always cover the
> whole standard. 7, yes. 8, yes. 9, yes.

1. **Stretch 3 order:** benchmarks and the same whole come before common denominators. No stretch moves; the
   units inside stretch 3 swap.
2. **Word caps:** a unit plan is 1,000 words not counting its checks, errors and days fields (fields 3, 4, 6); a
   stretch sheet is 800 words not counting its check tables and error register (fields 4, 5, 6); tool gaps move
   to one tool-asks file per course.
3. **Fraction Wall Duel** is a light tool for now; day 23 runs on paper. **Follow up after more progress.**
4. **Number line splitter:** wait until stretch 7 is planned, then spec it once for stretches 3 to 7.
5. **Facts check** in stretch 1: 36 products in the day 3 warm-up, 36 quotients in the day 4 warm-up, untimed,
   mark 32 of 36. Students below the mark keep a 9 by 9 multiplication table through stretch 3.
6. **Day 14** teaches the equivalence rule in both directions. **New standing rule: always cover the whole
   standard.**
7. **No-reuse rule in fractions:** it applies to the fractions an item gives; the given pair and the answer must
   both be new.
8. **Stretch 10 number sizes:** one-digit facts and their divisions; one digit times a multiple of 10, and 10
   times a number, multiplying only; adding and subtracting within 1,000. Two-step problems are chosen so one
   equation needs no brackets; two equations are always allowed.
9. **Stretch 2 limits:** pattern terms under 1,000, no further than the 10th step; the second readiness item is
   written.

### Card q-bar-subjects: the bar for subjects with no rubric on file

> 1 needs a better option. this may require a unification of content standards or possibly a "high watermark"
> method. 2 shelf foreign languages for a later pass (ASL included). 3 all. 4 they can stay separate but are
> allowed to be smaller than other courses by nature of the subject. 5 is another place where i feel a "high
> watermark" may be best (follow the higher quality or rigor). 6 i lean to once per year, but up to three times
> if the evidence indicates a need for more. 7 accept for now. 8 i agree for now but this is a future area of
> growth. 9 yes and it might be small and thats okay. 10 yes but mark this for a deeper review. 11, agreed

1. **Social studies content standards: NOT decided.** Cory wants a better option than "pick one state": a
   unified set, or a "high watermark" method (take the more demanding expectation where states differ). This is
   to be worked up and brought back to him. No social studies spine before it is settled.
2. **World languages are shelved for a later pass, American Sign Language included.** Do not write spines, load
   standards or plan video for them now.
3. **Health:** carry all the sensitive topics, each able to be left out without breaking the course. (The paid
   specialist read per band was part of the pick and was not objected to; confirm the cost with Cory before
   spending anything.)
4. **SEL and library skills stay separate courses**, and may be smaller than other courses by the nature of the
   subject.
5. **Values conflicts between state instruments:** Cory leans to a "high watermark" here too: follow the higher
   quality or rigor. This is not the same as the pick (FOUNDATION promise 7 governs). **Needs working out with
   item 1 and brought back**: what "higher" means when instruments conflict on values and not on rigor.
6. **Informed action in social studies:** once a year per course, up to three times if the evidence shows a
   need for more.
7. **The pass rule:** accepted for now. Test it on the first finished course.
8. **Professional learning:** none for now; a future area of growth.
9. **Library skills:** our own bar, named as ours; it may be small.
10. **SEL and personal finance:** the design half is the bar. **Marked for a deeper review.**
11. **Family notes** in English and Spanish, written when a unit is finished.

### Card q-standards-currency: gaps in the loaded standards

> 1, agree. 2 agree, lets fully update and cleanup where needed. 3, yes. 4, yes, fix with an opus model later.
> 5, agree but dont lose the note to load them when writing the spine.

1. **Computer science 9 to 12:** load the 135 Specialty standards. The high school course teaches the
   Foundational set; Specialty standards are claimed only where a module already goes that far.
2. **Health and PE:** keep the 2024 standards, write the mapping to the older-keyed review tools, and **fully
   update and clean up where needed** (file headers, labels, the stale "2018" on the library standards file).
3. **2026 can-do statements:** yes, but world languages are shelved (card above), so this waits with them.
4. **Licence page and the SEL file header:** yes, fix. Cory asked that this be done later, with an Opus model.
5. **AP and psychology modules (26) with no standards file:** mark them now as not yet standards-checked.
   **Do not lose this: load the course framework when that course's spine is written.**

## Applied on 2026-11-11 (late), after Cory said to act on the answers

Everything in the three cards that could be applied has been. Where each landed:

| Decision | Where it is now |
|---|---|
| Word caps: unit plan 1,250, stretch sheet 1,250, merged one-unit stretch 1,800 (first set at 1,000 and 800, raised by Cory the same night); tool asks in one file per course | `docs/courses/UNIT-PLAN.md` ("Length", "Decided"); `docs/courses/math-4/TOOL-ASKS.md` (9 tools); sheets s01, s02, s03, s09, s10, s11 link to it |
| Always cover the whole standard | UNIT-PLAN.md rule 19; BASELINE rule 23 |
| No-reuse rule for fractions | UNIT-PLAN.md rule 4 |
| Stretch 3: benchmarks first | Spine, `data/units.csv`, s03, u03-1 to u03-4. Now: 3.1 days 10 to 12; 3.2 days 13 to 16; 3.3 comparing to one half and one, the same whole, days 17 to 18; 3.4 common denominator or numerator, days 19 to 24 (check on 24) |
| Facts check; stretch 2 limits; stretch 10 numbers; day 14 both ways; readiness timing in "The checks"; stretch 1 balance; tool column | `docs/courses/math-4-spine.md`, dated change block for 2026-11-11 |
| Fraction Wall Duel light for now; splitter waits for stretch 7 | TOOL-ASKS.md, s03, spine |
| The bar: all eleven answers | `docs/ADOPTION-BAR-SUBJECTS.md` ("Decided" in Cory's words; "Still open with Cory"; world languages part headed "Shelved") |
| Computer science Specialty standards | `data/standards/csta-2026-specialty-ids.txt` (135 ids); `scripts/standards.py` accepts them |
| Health and PE mapping and clean-up | `docs/standards-notes/health-2007-to-2024.md`, `pe-2014-to-2024.md`; headers fixed in nhes-2024, aasl-2018, csta-2026-ids |
| 26 AP and psychology modules | `docs/standards-notes/modules-without-standards.md`: not yet standards-checked; load the framework when that course's spine is written |
| Core subjects first | BASELINE rule 24; ROADMAP above the layers |
| Expert reads go to Sara | `docs/courses/NEXT-SPINES.md`, piece 1 |

**Not applied, on purpose:**

- (Done since: the licence page and the SEL file header were fixed on 2026-11-11, night, when Cory accepted the
  strategic review. The focus file `data/standards/ccss-math-focus.csv` was said to have no header; it has one,
  with source, version, date and terms, checked 2026-11-12.)
- The course status table still counts world languages. Cory: leave it as a reminder.
- World languages: the 2026 can-do statements and the ASL standards wait with the shelved subject.

**Left open by the apply work (small):**

- Unit 3.4 now has six days; the spine names it as the exception to "1 to 5 days".
- Unit 3.3 has a new written task (3/4 and 5/6, day 18): the old one needed common denominators.
- Against the caps of 1,250: u03-4 is still over (about 1,400); s03 (about 1,230) and s10 (845) now fit. Unit
  plans other than stretch 3's were not recounted.
- Growth Spurt's "key" mark is the plan's own, not a decision of Cory's. It is settled at step 4e.
- Cory's answers left three things undefined, to ask before the spine that needs them: what "smaller" means for
  SEL and library courses (fewer days or fewer units); what evidence would raise informed action above once a
  year; and the specialist health read was taken as included in "3 all" (no spend without his yes).
- Fixed 2026-11-11: `scripts/overlap/standards.py` crashed because `docs/agents/overlap/tags.csv` still lists four
  tools that are no longer in `data/tools-concepts.csv` (food-web-wobble, planet-builder, molecule-builder,
  span-the-gap). The loader now skips them and says so. The tags file itself is unchanged.
- The federal PE review tool could not be opened (addresses return 404); the PE and health keying rests on the
  earlier report.

## Decided 2026-11-11 (night): the strategic review, accepted in full

Cory: "i accept all of the reviewers recommendations, even the ones that overturn my decisions earlier. please
action those decisions so they take effect." The review is
[reviews/strategic-review-2026-11-11.md](reviews/strategic-review-2026-11-11.md).

| # | Decision | Where it is now | Still to do |
|---|---|---|---|
| 1 | Build pilot unit 11.1 to the bottom now, ahead of the other unit plans and the key-tool ranking | BASELINE rule 25; ROADMAP order; "Start here" | The build itself |
| 2 | Freeze stretch planning at the six on file until the pilot is read (exception: start-of-year check, stretch 4 readiness items) | BASELINE rule 25; Sara's list | Nothing |
| 3 | A lesson-day template before the pilot is built | BASELINE rule 27 | Write `docs/courses/LESSON-DAY.md` (the next action) |
| 4 | Keyed items as data; a script recomputes every key | BASELINE rule 27; FOUNDATION 7.2; built, see "Plan weight" | The other five stretches |
| 5 | A grade 3 to 5 teacher, one taught run, three timed students | FOUNDATION 7.3; [pilots/README.md](pilots/README.md) with five draft questions | Cory finds the people |
| 6 | Spec fixing stops now; old tools and specs sorted into three bins by demand | BASELINE rule 26; FOUNDATION 6.5 (open question closed); `docs/spec-fixes/` marked stopped; sorted by `scripts/tool_bins.py` into [TOOL-BINS.md](TOOL-BINS.md): 15 named by a plan (plus 3 asked for and not built), 3 on the shelf, 782 frozen. The shelf count rests on a rough machine read of the teaching test; 17 Recess and Curiosities folders sit outside the sort | Nothing |
| 7 | Qualified people named where a course needs them | FOUNDATION 7.3 table; BASELINE rules 5 and 28 | Names and budget: none yet, Cory's |
| 8 | First ELA and science pilots right after 11.1 is read | BASELINE rule 25; Sara's list pieces 3 and 4 | ELA pages drafted; science pages are Sara's piece 3 |
| 9 | Item-level choices settled by the expert, weekly digest; Cory decides scope, audience, money, people, moves of standards | BASELINE "What goes to Cory"; EXPERT.md | Started 2026-11-12; keep it up after every read |
| 10 | One current-state page | This page; ROADMAP cut to the order, history in `docs/archive/` | Keep it so |
| 11 | Licence page fixed | `LICENSE-CONTENT.md`; SEL file header | Nothing |
| 12 | Six more pieces listed for a finished course | ROADMAP "What a finished course holds"; FOUNDATION open questions | Cory says in or not-now for each |

These overturn earlier answers of Cory's, with his say: Sara's spec batches were to stop after batch 4; "we
don't wait on outside human reviewers" (BASELINE rule 5); the licence fix was to wait for a later session; the
step order 4d, 4e, 4f.

**The expert and its data.** Cory: "i agree that the AI expert needs to be good enough, thats why i pushed for
added data (esp in pedagogy). that may need more work soon." So the expert stays the main read. Expect a piece
of work on its sources (`docs/APPROACH-SOURCES.md`, the pedagogy sources named in `docs/APPROACH.md`): what it
must open before judging each subject, and what is still unread. Not scheduled yet.

## Plan weight: facts in data, scripts as gates (built 2026-11-11, on stretch 11)

Cory asked whether the plan is still too heavy when an AI manages it. Yes, for different reasons than for a
person: no agent can hold a 125,000-word course; prose repeats facts and the repeats drift; prose cannot be
checked by a machine; every word is paid for several times; and Cory cannot sample what has no fixed shape.
He then said: "Let's implement those architectural fixes".

| Fix | What exists now |
|---|---|
| Facts in data, one home each | `data/plans/math-4/`: parts, days, items, wrongs, errors. Stretch 11: 18 items, 31 wrong answers, 5 days, 5 errors, 7 standard parts |
| Scripts as gates | `scripts/plan.py check`: keys recomputed exactly, every standard part has an end-check item, no reused numbers, day counts against `data/units.csv`, minutes add up, tool folders exist. Stretch 11 passes; a planted wrong key failed |
| Prose only for judgment | The tables in `s11.md` are generated (`scripts/plan.py tables`). The prose was cut by the cold read (about 170 words that repeated a table or DEFAULTS.md) and stands at 1,898 words against a cap of 1,800. Settled 2026-11-12: it stays; the overage is the generator sheet and record sheet definitions, which move to the built pages (DIGEST.md) |
| Defaults written once | `docs/courses/math-4/DEFAULTS.md`, a draft from stretch 11 and the spine only |
| Plans just in time | BASELINE rule 25 |
| A reading pack per agent | `scripts/plan.py pack math-4 11` |
| A defect ledger | `data/plans/defects.csv`; `scripts/plan.py defect` and `defects`. 49 logged on 2026-11-12: 15 on the pilot plan (0 open), 34 on the three ELA pages (6 open, the six questions on card `q-ela-piece-2`) |

Rules: `docs/courses/UNIT-PLAN.md`, "Facts live in data". How to use it: `data/plans/README.md`.

**Not done:** stretches 1, 2, 3, 9 and 10 (12 units) are still prose only, so their keys have not been recomputed
by the script. Tool asks are still prose in TOOL-ASKS.md. The number limits of a stretch (for example "products
within 100") are not yet a gate. `DEFAULTS.md` has been checked against stretch 11 only. ELA has no data shape yet (its text
record, question set and word list wait for Cory's answer on card `q-ela-piece-2`, question 3).

## The order after the pilot

**Core subjects first (Cory, 2026-11-11; a soft goal, BASELINE rule 24).** Math, English language arts, science
and social studies (56 of the 105 courses) come first; this bends where work is complementary. Every course is
still finished to the bar; this sets the order, not the scope.

1. The pilot is read; templates and the plan design are fixed from what it showed.
2. Grade 4 math is the main thread (Cory, 2026-11-12, card 111): the course a stretch at a time, each planned
   only when the one before is built. Stretch 10 is next.
3. Alongside it, once 11.1 has its teacher read: the ELA and science pilots, so a unit's cost is known in three
   subjects. No other math course is built until they are in.
4. The plan with sizes and dates for all 105 courses, written from three real unit costs.
5. The social studies content standard goes to Cory before any social studies spine.

**Sara's list is [courses/NEXT-SPINES.md](courses/NEXT-SPINES.md)**. Done by her session: piece 1 (the pilot
plan's cold read) and piece 2 (ELA rubric page, approach page, rights list). Owed from those: her own read as a
teacher at the top of four reports. Next for her: piece 3 (science rubric page, approach page, pilot unit
materials), then piece 4 (the start-of-year check and stretch 4's readiness items, as data rows), then piece 5
(the social studies options). Spines, progression pages and stretches 4 to 8
came off it until the pilot is read.

## Owed, smaller

- Cory's read of the approach pages; his final yes on the science and ELA spines.
- Three `data/modules.csv` description notes; footnoted limits in `data/standards/ccss-math-standards.txt`; the
  shape file `math-4.md` build order against the spine; science `sequence.csv` errors.
- Tool spec gaps: Community Plot Planner (eight asks, all in TOOL-ASKS.md); Egg Carton Factory (no ordered search, no
  equation form, names prime and composite a day early, check numbers 77 and 93 sit on Rush card 2c); Rule
  Machine; Fraction Wall Duel; Growth Spurt; Road Trip Logbook. All go in TOOL-ASKS.md.
- `s09.md` puts five minutes of teacher-judged answers on day 78, before Check 2.
- The K to 2 device assumption is undecided.
- Grade 6 ELA spine, found while applying the expert's edits on 2026-11-12, all item-level and for the expert
  when the ELA pilot is planned: the readiness check's ten minutes do not fit a 50-minute ELA period on a check
  day, and stretch 2's would land on day 4; "every day ends with a written exit question" still stands in the
  spine though the approach page dropped it for writing and check days; the stretch 2 audio row still says "to
  verify"; the Monkey King cut measures 10.5, the top of the band, and the spine does not say so; "the easiest
  anchor passage of the year" was said with only stretch 2 measured.
- `scripts/tool_bins.py` reads TOOL-ASKS.md by its layout and has been run on one course only. Its shelf bin
  (3 tools) uses the rough machine read of the teaching test; four tools a judge report calls passing in prose
  are counted as frozen.
- The usage limit stopped four agents mid-run once on 2026-11-11. They were resumed and finished; nothing was
  lost, but stretches 1, 2, 3, 9 and 10 were written across that break.

## What has not been verified

- The source search, the bar draft and the standards check rest on agent reports. Instruments named as "read in
  part" or "not opened" in those files are still so.
- No plan, check or tool here has been tried with a student or read by a working teacher.
- In the pilot plan, the ranking of wrong answers for error C and the examples for errors D and E rest on
  memory, not on a source that was opened. The pilot's student work is the test.
- No licence line in the ELA rights list has had its second read.
- Only 5 of the 23 stale lines in the strategic review's records table were checked by the working session
  before the clean-up; the clean-up worked from the reviewer's table.
- Tool minutes in the plans are estimates; no build was played.

## Reports from 2026-11-11, by question

| Question | File |
|---|---|
| What instruments exist for the other subjects | `docs/reviews/bar-other-subjects-2026-11-11.md` |
| Expert on the bar's first draft | `docs/reviews/bar-subjects-2026-11-11.md` |
| Are the loaded standards current | `docs/reviews/standards-currency-2026-11-11.md` |
| Expert on the three trial plans (4c) | `docs/reviews/unit-plans-2026-11-11.md` |
| Expert on stretches 1 to 3 (4d) | `docs/reviews/unit-plans-4d-2026-11-11.md` |
| Is the whole project on a solid path | `docs/reviews/strategic-review-2026-11-11.md` |
| Expert on the pilot unit plan (stretch 11) | `docs/reviews/unit-plan-s11-2026-11-12.md` |
| Expert on the ELA rubric page | `docs/reviews/rubric-ela-2026-11-11.md` |
| Expert on the ELA approach page | `docs/reviews/approach-ela-2026-11-11.md` |
| Expert on the grade 6 stretch 2 rights list | `docs/reviews/rights-ela-6-s2-2026-11-11.md` |
| Sara's six questions for Cory, in full | `docs/reviews/piece-2-cards-for-cory-2026-11-11.md` |
| What the expert settled without Cory | `docs/reviews/DIGEST.md` |
