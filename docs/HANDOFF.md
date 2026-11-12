# Handoff: where the course work stands

**Written 2026-11-11, evening, at the end of a long session, for the next chat. Read this first, then
[ROADMAP.md](ROADMAP.md) ("The layers" and "Resume here"). Everything below is pushed to `spec/sara` and `main`.**

This page is the one place that says what was decided, what has been applied, and what to do next. If it
disagrees with another page, the other page is probably the stale one: check the date, fix it, and say so.

## How to work here

- Work only in the worktree `S:\CurioClass-spec2`, branch `spec/sara`. Never `cd` to `S:\CurioClass`.
- Push to both: `git pull -q --rebase origin main`, `git push -q origin HEAD:spec/sara`,
  `git push -q origin HEAD:main`. "Bypassed rule violations" on main is normal. Commit only your own files.
- No em dashes anywhere. Always "Curio Class" in full. Never say Curio Class was reviewed by, meets or is
  endorsed by anyone. Public copy names no companies. Outside rubrics are linked and put in our own words.
- Do not touch the Word Wall files (`data/closet`, `closet/words`, `data/media-manifest.txt`).
- A background agent that is editing files blocks `pull --rebase`. Commit and push after it finishes.
- The working pattern: a writer agent drafts; commit; the curriculum expert reads it cold (a fresh agent told to
  read [agents/EXPERT.md](agents/EXPERT.md) first; report goes to `docs/reviews/<what>-<date>.md`); revise once;
  anything that changes what a course teaches or a decided rule goes to Cory on the Review Desk **and** in chat.
- Records to update after every decision: this page, ROADMAP ("The layers" row and "Resume here"),
  [agents/decisions/DESK-ANSWERS.md](agents/decisions/DESK-ANSWERS.md), and the assistant's memory notes.
- The Review Desk is https://claude.ai/artifact/SVXBzgyS941dyqmEzQHgNC. A question card has status `question`,
  then `answered`. Cory answers in a comment on the card. Next free card order: 104. After changes, refresh the
  Dashboard with `python -X utf8 scripts/course_status.py <out.json>` (Desk doc `stats/courses`) and the Roadmap
  tab with `python -X utf8 scripts/desk_roadmap.py <out.json>` (Desk doc `stats/roadmap`).
- Core subjects first (BASELINE rule 24, a soft goal): see "Then, the next real work".
- Cory's standing rules that bite most often: every one of the 105 courses is finished to the adoption bar (a
  firm bar; never call it unrealistic); no countdown timer shown to a student; no library or paywalled access;
  teach first by default in grades 2 to 5; Cory wants pushback and welcomes questions about earlier decisions.

## Where things stand

| Layer | State |
|---|---|
| 1 Foundation | [FOUNDATION.md](FOUNDATION.md). Done. |
| 2 Standards | `data/standards/`. Checked 2026-11-11: nothing superseded; gaps listed below. |
| 3 Approach | [APPROACH.md](APPROACH.md), [APPROACH-MATH.md](APPROACH-MATH.md). Decisions answered. Cory still owes a read of the pages as a whole; his mother is reading "The principles" onward as a grade 2 teacher. Science and ELA approach pages are on Sara's list ([courses/NEXT-SPINES.md](courses/NEXT-SPINES.md)). |
| 4 Progressions | Math grades 3 to 5 done. |
| 5 Spine | Grade 4 math, plus science and ELA spines waiting for Cory's final yes. 3 of 105 courses have a spine. |
| 6 Stretch sheets and unit plans | Fields fixed in [courses/UNIT-PLAN.md](courses/UNIT-PLAN.md). Grade 4 math: stretches 1, 2, 3, 9, 10 and 11 are planned, which is 13 of 43 units (the status table shows 17 because it counts stretch sheets too). 30 units to go (stretches 4 to 8 and 12 to 18). |
| 7 Lessons, tools, print | Paused until the pilot unit (11.1). |
| The bar | Math: [RUBRIC-MATH-K8.md](RUBRIC-MATH-K8.md). All other subjects but ELA and science: [ADOPTION-BAR-SUBJECTS.md](ADOPTION-BAR-SUBJECTS.md), second draft. ELA and science rubric files are on Sara's list. |

Course count: 105, of which 56 are in the four core subjects ([COURSES-STATUS.md](COURSES-STATUS.md), generated;
never edit by hand). Languages are now shelved (see below) but still counted until the status script is told.

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

## Decided but not yet applied (do these first, in this order)

None of the evening's answers has been written into the spine, the template or the plans yet. Each line names
the files.

1. **Word caps** in `docs/courses/UNIT-PLAN.md` ("Length" and the "Decided" section) and the ROADMAP paragraph
   that quotes the old caps (1,500 / 700 / 2,500). Decide the one-unit merged document's cap by the same logic
   and mark it proposed. Create `docs/courses/math-4/TOOL-ASKS.md` and move the spec asks out of the sheets
   (s01 has 11, s02 has 5, s03 has 8; s09, s10 and s11 have theirs in the tools field).
2. **"Always cover the whole standard"** as a rule in UNIT-PLAN.md and `docs/agents/decisions/BASELINE.md`.
3. **Stretch 3 swap:** `docs/courses/math-4-spine.md` (unit rows, days), `data/units.csv`, `s03.md`, and
   `u03-3.md` / `u03-4.md` (which becomes 3.3 and which 3.4, days 17 to 23, tie and withdrawal days, exit
   question numbering, the two-pizzas opening). Remove the "Open, with Cory" line at the top of s03.md. Rework
   every key touched. Then one expert read of stretch 3 as a whole.
4. **Spine fixes found by the writers** (`math-4-spine.md`): "The checks" lines still describe first-day
   readiness; stretch 1 balance is 4/1/0/1; define the facts check and its mark (item 5 above); stretch 2 limits;
   stretch 10 numbers rule; day 14's title; the Tool column for stretch 3 (the Duel is light, one day); Growth
   Spurt fits in parts only; unit 10.3 has one teaching day.
5. **No-reuse rule wording** (item 7) in UNIT-PLAN.md.
6. **Bar page** `docs/ADOPTION-BAR-SUBJECTS.md`: move the answered choices into a "Decided" section in Cory's
   words; shelve the world languages part (keep the text, mark it shelved); note SEL and library may be small;
   leave choices 1 and 5 open with the high watermark idea; mark choice 10 for deeper review. Status line: not
   read by the expert since revision.
7. **Standards work** (card 3): load CS Specialty standards; health and PE mapping and header clean-up; mark the
   26 AP and psychology modules in `data/modules.csv` or the shape file; licence page with an Opus model.
8. **Course status:** teach `scripts/course_status.py` that world languages are shelved, regenerate
   `docs/COURSES-STATUS.md`, refresh the Desk.

## Then, the next real work

**Core subjects first (Cory, 2026-11-11; a soft goal).** Math, English language arts, science and social
studies (56 of the 105 courses) are the first focus; the other subjects follow. This bends where work is
complementary (a shared rule, a bar page, a standards fix that serves both). When a choice has to be made, the
core subjects come first. Every course is still finished to the bar; this sets the order, not the scope.
So: grade 4 math first, then the other core spines and plans. The social studies content standard question is
core work. Health, PE, arts, computer science, CTE, SEL, ELD and library work waits unless it is complementary.

- **Step 4d continues:** grade 4 math stretches 4 to 8, then 12 to 18, a stretch at a time, per UNIT-PLAN.md,
  with a cold expert read on a sample. Stretch 4's readiness items are already needed on day 24 (s03 points at
  a sheet that does not exist yet), so stretch 4 is next. The start-of-year check (day 1) is unwritten and must
  carry stretch 1's three readiness items.
- **Stretches 9 and 10 have had no expert read.** Read them cold before building on them. Stretch 11's second
  draft has had none either.
- **Work up the social studies content standard options** (unified set, high watermark, one state) with what
  each would cost and change, and the values question beside it. Bring both to Cory on the Desk.
- Then 4e (name the key tools from all the plans; goes to Cory) and 4f (build pilot unit 11.1 and have it read).

## Owed, smaller

- Cory's read of the approach pages; his final yes on the science and ELA spines.
- Three `data/modules.csv` description notes; footnoted limits in `data/standards/ccss-math-standards.txt`; the
  shape file `math-4.md` build order against the spine; science `sequence.csv` errors.
- Tool spec gaps: Community Plot Planner (1, 4, 5, in s11.md); Egg Carton Factory (no ordered search, no
  equation form, names prime and composite a day early, check numbers 77 and 93 sit on Rush card 2c); Rule
  Machine; Fraction Wall Duel; Growth Spurt; Road Trip Logbook. All go in TOOL-ASKS.md.
- `s09.md` puts five minutes of teacher-judged answers on day 78, before Check 2.
- The K to 2 device assumption is undecided.
- The usage limit stopped four agents mid-run once on 2026-11-11. They were resumed and finished; nothing was
  lost, but stretches 1, 2, 3, 9 and 10 were written across that break.

## What has not been verified

- The source search, the bar draft and the standards check rest on agent reports. Instruments named as "read in
  part" or "not opened" in those files are still so.
- No plan, check or tool here has been tried with a student or read by a working teacher.
- Tool minutes in the plans are estimates; no build was played.

## Reports from 2026-11-11, by question

| Question | File |
|---|---|
| What instruments exist for the other subjects | `docs/reviews/bar-other-subjects-2026-11-11.md` |
| Expert on the bar's first draft | `docs/reviews/bar-subjects-2026-11-11.md` |
| Are the loaded standards current | `docs/reviews/standards-currency-2026-11-11.md` |
| Expert on the three trial plans (4c) | `docs/reviews/unit-plans-2026-11-11.md` |
| Expert on stretches 1 to 3 (4d) | `docs/reviews/unit-plans-4d-2026-11-11.md` |
