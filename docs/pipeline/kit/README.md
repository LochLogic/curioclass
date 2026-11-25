# The course-run kit

KIT-VERSION: 6 (2026-11-25)

The job templates, notes and rules that `scripts/coursegen.py` fills to write a course run's job queue, in the order of
docs/COURSE-RUN.md (stages 5 and 6, with the retool and sweep rules of its sections 1 and 4). Built from the
ad hoc kit of the social studies and ELA run (_scratch/ladder2/, copied and cleaned) plus that run's report findings
("retool 0", see RETOOL.md). Every generated job file starts with the KIT-VERSION line, so a run can say which version
it used.

## The retool rule

- **The kit is frozen within a grade.** Templates, notes and rules do not change while a grade's jobs run, and no
  lead run notes are added to prompts: if a rule is missing, the job is a faulty job, fixed after the grade.
- **Changes land only between grades** (and after a subject's first-grade probe, once, in a subject's first grade).
  Each change is logged in RETOOL.md with the date, the finding it answers (with the stage that found it and the stage
  that made it) and the new KIT-VERSION, which is bumped in this file. The remaining queue is then regenerated.
- A fault found in a later stage but made in an earlier one is fixed in that stage and swept (sweep.txt), and the
  template or check that let it through is retooled at the next retool point.
- Job files already generated keep the version they name.
- 2026-11-22: following Cory's decision of 2026-11-20, math files are fully open to math runs. The never-open list in
  common.txt no longer blinds math-4, the math-3-5 progression, `*-spine.md`, NEXT-SPINES.md, im-g4-draft-map.csv or
  data/units.csv. It keeps `.claude/`, docs/Return/, the spec2 folder, closet/words, the media manifest, the
  `*reconcile*` reviews and ela-6. (Logged in RETOOL.md, retool 0.)

## Generating a queue

```
python -X utf8 scripts/coursegen.py <subject> <course> [<course> ...] --out <dir> [--probe] [--texts]
python -X utf8 scripts/coursegen.py sweep <subject> <course> --out <dir> --made-at <stage> --found-at <stage> \
    --fault "..." --test "..." [--found-in ...] [--tool ...] [--scope ...] [--tag ...]
```

Subject is `ela`, `social-studies`, `math` or `science`; courses go in grade order. `--probe` runs the first course's
unit 1 all the way through days before the other units' section plans, then stops for a probe retool. `--texts` (ELA
only) adds the text jobs. queue.txt lists every job on one line: `number | kind | course | detail | file`. GATE lines
carry the ledger gate command that precedes a day job (the day job file also runs it as its step 0); LEAD lines are
steps for the lead, not agents. A course whose inputs are missing is reported by stage (days.csv is stage 3, unit
plans s01.md and so on stage 4) and skipped with every course after it. Dates in report names ({DATE}) are the
generation date.

## Order generated, per grade

1. LEAD: section skeletons present (stage 5 section cuts). With `--texts`, text jobs and a merge step.
2. Section plans, unit by unit (a unit over 5 sections is cut in two jobs). With `--probe` in a subject's first grade,
   unit 1 first goes through its data, key read and days, then a probe retool stop.
3. Plan read (fresh readers, 4 units each), one plan fix, LEAD gate check.
4. Per unit: plan data, answer-key read, then day jobs of 4 to 6 days (as the sections allow), each preceded by its
   ledger gate; course-level check days run in day order between the unit jobs.
5. LEAD gate check, grade sample (two readers, ten days, one a decile, seeded by the course id), cleanup, retool stop.
6. After the last grade: the continuity read (`ledger.py recheck`) and one continuity fix per grade from the second.

## Templates (docs/pipeline/kit/<name>.txt)

| Template | Used for | Main tokens |
|---|---|---|
| section | section plans, one unit (or half) a job | UNIT UU SECTIONS |
| plan-read | fresh read of a grade's plans, report only | UNITS PART |
| plan-fix | the one fix job after the plan read | |
| data | plan data per unit: items, wrongs, errors, pieces, sources | UNIT UU SECTIONS FIRST LAST UNITLEVEL ENDITEMS |
| key | the cold answer-key read per unit; fixes keys and splits two-part items | UNIT UU FIRST LAST |
| day | 4 to 6 days; step 0 is the ledger gate | UNIT UU FIRST LAST SECTIONTEXT PREVDAY GATELINE |
| checks | course-level check days | CHECKDAYS FIRST LAST GATELINE |
| sample-read | grade-close read of ten days, report only | PART DAYS |
| cleanup | one fix job from the sample reports, plus key lines in child pieces | |
| retool-stop | lead-only checklist at grade close | |
| continuity-read | cross-grade claims against what was written (`ledger.py recheck`) | COURSES |
| continuity-fix | one fix per grade | |
| sweep | a fault made earlier is fixed there, then looked for in every unused piece | FAULT FOUND_AT MADE_AT TEST SCOPE TOOL GATES |
| text, text2 | ELA core texts and commissioned texts (optional, `--texts`) | UNIT UU |
| common, gate-line | shared rules (never-open list, no git, CSV safety, sources, cost, gate counts), ledger gate step | |

Other tokens, set by the generator: COURSE, SUBJ (ledger name), SUBJWORD, DATE (today), KITVERSION, JOB (temp folder
name), PLANGATE and LESSONGATE (the filtered gate commands for the course), COMMON, GATELINE, GRADENOTE and SUBJNOTE.
Tokens are upper-case words in braces and are filled in one pass: no token can sit inside another word (the old
UNIT-in-UNIT-PLAN.md bug) and an unknown token stops generation. Lower-case braces such as `{course}` in a brief's own
wording are left alone.

## Notes (data files)

- notes/subject-<subject>.txt: ela, social-studies, math, science (science added 2026-11-23, retool 2).
- notes/grade-<band>.txt: k and 1 to 6. The grade comes from data/plans/frames.csv; a grade 7 or higher course needs
  its note first, and the generator stops without it.
- Notes may use DATE and COURSE tokens. Both kinds are inserted into every template that names them.
