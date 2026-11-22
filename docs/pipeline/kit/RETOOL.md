# Kit retool log

Each retool is dated, names the KIT-VERSION it produced, and logs every change with the finding behind it, the stage
that found it and the stage that made it. The kit changes only here, between grades (README.md, "The retool rule").

## Retool 0: KIT-VERSION 1 (2026-11-22)

Source: the social studies and ELA K to 3 run report (docs/reviews/ladder-ss-ela-report-2026-11-19.md, its findings,
patterns and recommendations), the fix notes (docs/reviews/ladder-ss-ela-fixes-2026-11-22.md), the alignment audit
(docs/reviews/course-run-alignment-2026-11-20.md, steps 1, 5, 6 and the step 8 sweep template) and the lead rules that
lived only in prompts and _scratch/ladder2/STATE.md.

### Report findings and where each went

| Finding (stage that found / made it) | Where it went |
|---|---|
| Review claims drifted when the lower grade changed after it was cited (capstone: 36 drifted claims; found at capstone, made at section and day) | Ledger gating: a day job starts with `ledger.py gate` and stops on non-zero (day, checks, gate-line); the "planned only" rule for review notes (section, day, cleanup, continuity); continuity read and fix use `ledger.py recheck` |
| Cost 79k a day against 60k; the fixed reading cost dominates short days (found at report / made at job shape) | Day jobs of 4 to 6 days from one read of plan and ledger (generator); cost reminder in common.txt (read only what is needed, filter CSVs, never re-read after an edit) |
| Gates caught almost none of the 95 sample FIRM findings; agents' gate counts missed FAIL lines after the course summary (found at sample / made at agent reporting) | common.txt: report all filtered lines, own counts not trusted, lead re-runs (retool-stop step 1, queue LEAD lines) |
| Exit does not measure the goal; rule 4; two asks in one stem; spoken items the child writes (section, data) | Item rules in data.txt, key.txt (splits two-part items), day.txt, plan-read.txt; path honesty in section, data, day, checks |
| Shape sharing: practice, model or card shares an exit's shape (unit plan and section plan set it) | "Shape:" lines required on every exit and check item in section.txt; checked by plan-read; held in data and day; sweep template for the unit-plan cause |
| Parts that cannot run in their minutes, repair slots too small, marking time | Turn-taking time (about 45 s a child per spoken ask, a rotating six with a hand-back, real repair minutes) in section, data, day, checks, plan-read, sample-read |
| Sources: Wikipedia or a search summary as the record; 403 sites; over-cutting of core facts | Sources rule in common.txt (never Wikipedia or a summary; one other solid source; unreadable facts cut, core facts kept and marked "browser check") |
| Id-only matching corrupts rows; a CSV truncated by opening for write first | CSV safety rule in common.txt (full id with prefix, read whole file first) |
| Key lines in child pieces (74 piece files) | Key rule in data, day, checks (keys in teacher key pieces); key-line scan in cleanup.txt; "key-on-child-page" kind in sample-read and key |
| "Template point" used as a shield | common.txt: a plan design choice is not a template point |
| Agents ran git status and git --version; stray temp folders | No-git wording in common.txt (the word git is never typed, "re-read the file you edited"); helper folder rule |
| Key readers' cold solve was not blind (shared pieces print keys) | Cold-solve rule at the top of key.txt |
| Stale plan field 3 exit lines after data changes | data.txt may update field 3 and `## Day N` blocks to match items.csv; key.txt lists stale lines; day.txt says items.csv is the truth |
| Held words and cases practised before their exit (wagon beats) | Held-word rule in day.txt and checks.txt (check practice words against items.csv first; end items never practised with their own words in the ELA note) |
| Day job reads the previous "Tomorrow" line | day.txt |
| Facts that rest on sites that refuse reads; a hinge with no fallback (local nation page, visitor, photo) | Hinge fallback rule in section, data and the social studies note; sources rule |
| ELA texts: commissioned texts with no rows, on-file rows with no file | text.txt and text2.txt carried over (optional, `--texts`) |
| Mid-course check days written out of order (found at day 44 before day 43) | Generator places course-level check days in day order between unit day jobs |
| Plan stage skipped: no fresh read of a grade's plans, no probe, one sample after all grades, ad hoc retool | plan-read, plan-fix, probe mode, per-grade sample and cleanup, retool-stop, RETOOL.md (alignment audit section 4) |
| Template bug: UNIT replaced inside UNIT-PLAN.md; report date hardcoded | Upper-case brace tokens filled in one pass, `{DATE}` filled at generation (alignment audit section 2) |

### Changes to the kit itself

- Job files and notes copied from _scratch/ladder2/ and cleaned: no "L81, second test" labels, no hardcoded dates, no
  lead-run-note references; blind-list and scratch paths now point at _scratch/l87/.
- Subject and grade notes are data files (notes/subject-<s>.txt, notes/grade-<band>.txt); the math note is a stub.
- Added templates: plan-read, plan-fix, sample-read (from the science sample job), cleanup (from the sample-fix job),
  continuity-read and continuity-fix (from capstone-read and capstone-fix, using `ledger.py recheck`), retool-stop,
  sweep, and the generator `scripts/coursegen.py` replacing gen2.py and daysmode.py.
- 2026-11-22, never-open list: following Cory's decision of 2026-11-20, math files are fully open to future math
  runs. The common rules drop the math-4, math-3-5-progression, `*-spine.md`, NEXT-SPINES.md, im-g4-draft-map.csv and
  data/units.csv blinds and keep `.claude/`, docs/Return/, the spec2 folder, closet/words, the media manifest, the
  `*reconcile*` reviews and ela-6.

### Left for a later retool (not in version 1)

- Scripts behind the checks (alignment audit section 5): unit-level ledger seed, plan.py one-ask and cold-word checks,
  lesson.py turn-time and marking-time checks, defects.csv `made_at` column, token report. Other agents own those.
- Gate quirks the writers listed as template points (warm-up id rule on repair days, `assess=observe` versus the
  unitplan check, no-exit day kinds, 300 to 500 word teacher caps on short days). These are gate or DEFAULTS changes,
  settled by the lead and Cory, then logged here.
- A math subject note; grade notes for grades 4 and up.
