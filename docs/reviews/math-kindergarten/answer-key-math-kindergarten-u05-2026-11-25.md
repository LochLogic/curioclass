# Answer-key read: math-kindergarten, unit 5

Job 042, kit 14. Job date: 2026-11-25. Read and fixes performed: 2026-11-26.

## Verdict

Fail under the job's literal prohibition on reusing numbers from shared instruction. Six item-level faults are fixed, all numerical keys agree with the cold solutions, and the remaining numerical-reuse conflict requires a unit-plan decision rather than an unsupported claim of compliance.

## What I studied

- `docs/pipeline/briefs/sensitivity-read.md`, sections 1 to 3, answer-key kind: solve and record before comparing, distinguish item faults from reader errors.
- `docs/courses/math-kindergarten/DEFAULTS.md`: 60-minute days, spoken single asks, picture responses, one marking scale, no independent reading, and a 60-word student-page cap.
- `docs/pipeline/briefs/section-write.md`, rules 7 to 10: one spoken ask, counted turns, shown / shown with help / not yet seen, and one actor per scene.
- `docs/courses/math-kindergarten/s05.md` and the four `u05-*.md` section plans: limits, goals, standards, reserved evidence, feedback, and the carried unit 4 record.
- `data/plans/math-kindergarten/items.csv`, filtered to days 87 to 103 and exit/readiness/end: **61 items**, consisting of 16 exits and 45 end rows. There are no readiness items in these days. Four end rows are teacher-only administrative interpretations, not new child questions.
- All **88 associated wrongs.csv rows**, the relevant handbacks, and the unit's original student stimulus masters, shared practice, private teacher keys and Before class references. The private keys' repeated entries were compared with the same authoritative CSV items, not counted as additional items.
- Filtered case-ledger reads using `ledger.py show math --before math-kindergarten --kind case --term "<word>"`: bookmarks, kites, hats, puzzle, stamps, peaches, crescent, nine-cell and concealed tower. Only kindergarten matches appeared; there is no lower grade in this subject ladder.

The study step was the cold solving below. Item IDs and non-key fields were listed first. Answer, steps, samples and wrongs columns and private keys were withheld until all 61 initial answers and methods had been recorded. No external answer source was consulted.

## Faults and fixes

Counts refer to findings: **key 2, ambiguous 4, rule4 1 systemic finding left**. Numerical key errors: 0. Off-goal, needs-info, two-asks and key-on-child-page findings: 0 after resolving the reader errors below.

| Item | Kind | What was wrong | Fix and status | Stage that made it |
|---|---|---|---|---|
| s05-X96 | key | The stem said "Circle the model that fits Rin's story." The look-fors required tracing seven initial marks and one incoming mark and refused a circle alone. That extra scoring requirement was never requested. | Fixed: "Trace Rin's starting boats and added boat on the matching model." Tracing the two story quantities is the single response. Removed the separate circle requirement, synchronized the sample and descriptive wrong row, and updated the student card and private teacher key. | section plan |
| s05-X101 | key | "Show the partner that completes this tower of ten" permits an isolated correct three, but the look-fors required the three to be connected to seven. | Fixed: "Show ten by joining the missing pieces to these seven." The key accepts a line, enclosure or continuous train joining the three new marks to seven; an additional spoken explanation is optional. Student card and private key synchronized. | section plan |
| s05-X88 | ambiguous | "Show two ways to make a seven-piece design" permits rearranging shapes with unchanged type counts. The key instead required different triangle/square counts. | Fixed: "Show two seven-piece designs with different numbers of triangles." Both have seven slots, with the existing triangle/square picture bank. Updated data, student card and private key. | section plan |
| s05-X94 | ambiguous | The card said "Rin decorates seven paper hats with stars or spots." It omitted the section plan's restriction that a hat belongs to just one decoration category, while double assignment was scored wrong. | Fixed the setup in the card, CSV look-fors and private key: "Rin decorates seven hats. Each hat has only stars or only spots." The single drawing ask and numerical key are unchanged. | data |
| s05-X95 | ambiguous | "Rin's nine puzzle pieces have round or square tabs" does not specify the one marked tab that the section plan uses to make the categories exclusive. A piece can have several tabs. | Fixed the setup in the card, CSV look-fors and private key: "Rin has nine puzzle pieces. Each has one marked tab, round or square." Both solutions still use nine pieces, each assigned once. | data |
| s05-X102 | ambiguous | "a different pair" can be read as the unordered-pair convention used elsewhere in the unit, but this labeled fruit key explicitly accepts eight peaches/two plums after two peaches/eight plums. "Tell" also obscured the planned picture response for every child. | Fixed: "Show a ten-fruit story with a different number of peaches." This states precisely which labeled count must change and allows the planned marked scene. Kept the correct labeled-allocation key, including eight peaches/two plums. Updated data, card and private key. | section plan |
| s05-F2 full-range set, with numerical reuse also present in F1 and make-ten exits | rule4 | Shared instruction deliberately shows the same finite number pairs that later assessment must cover. For example, u05-3/opener.md explicitly says "Demonstrate completed 3/7, 1/9, 2/8 and 5/5 ... then 4/6"; practice-98.md shows a completed four/six picture. F2 later requires all starts one through nine, including four with six and six with four. Fresh layouts do not satisfy the job's separate literal ban on repeated numbers. | Left explicitly unresolved. All F2 starts and the full F1 range are required by the unit plan and must remain on their goals; changing assessed numbers cannot remove this overlap. Removing the teaching quantities would change the teaching design and other CSV rows outside this job's edit scope. The lead must resolve the rule in the unit plan or commission a consistent redesign. This is a plan point, not a template exception. | unit plan |

Six items.csv rows and one wrongs.csv row were updated through rows.py, with a successful dry run before each write. Updated six exit cards and three private key files. No item IDs, days, goals, assessment slots or handback routes changed. Other wrong rows remain valid under the clarified asks. Each repaired task still has one response demand; no new split item or handback row was necessary.

## Initial cold answers and methods

These are the answers recorded before opening keys. Open-response samples are examples, not the only accepted solutions. The initial zero-panel suspicion is preserved in the record and corrected under "My own errors."

| Item | My answer and method before comparison |
|---|---|
| s05-X87 | 1+4 and 2+3; partition each five-dot copy without losing dots. |
| s05-X88 | 1 triangle+6 squares and 2 triangles+5 squares; count seven shapes in each design. |
| s05-X89 | 5+4; the first part gains the indicated cell and the second loses one, total nine. |
| s05-X90 | Cards 1 and 3 both show 1+7, although the seven dots have different arrangements. |
| s05-X91 | 7=1+6 and 7=2+5, with matching dot partitions. |
| s05-X92 | 9 bookmarks, counting three plus six. |
| s05-X93 | 1 striped+7 plain, then 2 striped+6 plain, each total eight. |
| s05-X94 | Seven hats, e.g. two with stars and five with spots. Wording permits a hat with both, so clarify one decoration type per hat. |
| s05-X95 | 1 round-tab+8 square-tab and 2 round-tab+7 square-tab pieces, total nine. |
| s05-X96 | A represents seven plus one. B and C also give eight but depict different actions/parts. |
| s05-X97 | Four empty frame cells, ten minus six. |
| s05-X98 | 10=8+2, counting eight filled and two outlined marks. |
| s05-X99 | Four covered counters, ten minus six. Picture uses square counters despite generic counter stem. |
| s05-X100 | One, ten minus nine. |
| s05-X101 | Three covered tower cells, ten minus seven. |
| s05-X102 | Rin has three peach pictures and seven plum pictures, ten altogether. Different unordered pair from 2 and 8. |
| s05-F1-0-1 | 0+0, but zero panel is absent from portfolio-99. |
| s05-F1-1-1 | 0+1, one mark in either part. |
| s05-F1-2-1 | 0+2; count two total. |
| s05-F1-2-2 | 1+1; different unordered pair from 0+2. |
| s05-F1-3-1 | 0+3. |
| s05-F1-3-2 | 1+2, different unordered pair. |
| s05-F1-4-1 | 0+4. |
| s05-F1-4-2 | 1+3, different unordered pair. |
| s05-F1-5-1 | 0+5. |
| s05-F1-5-2 | 1+4, different unordered pair. |
| s05-F1-6-1 | 0+6. |
| s05-F1-6-2 | 1+5, different unordered pair. |
| s05-F1-7-1 | 0+7. |
| s05-F1-7-2 | 1+6, different unordered pair. |
| s05-F1-8-1 | 0+8. |
| s05-F1-8-2 | 1+7, different unordered pair. |
| s05-F1-9-1 | 0+9. |
| s05-F1-9-2 | 1+8, different unordered pair. |
| s05-F1-10-1 | 0+10. |
| s05-F1-10-2 | 1+9, different unordered pair. |
| s05-F1-equation | 6=1+5 for my chosen six split; align total and part marks. |
| s05-F3-1 | One red-album stamp and three blue-album stamps, four total; card itself supplies no total outside teacher_note, assessment-100 lacks it entirely. |
| s05-F3-2 | Two red and two blue, different from 1+3, four total. |
| s05-F2-1 | 6, because frame shows 4 of 10. |
| s05-F2-2 | 9, because frame shows 1 of 10. |
| s05-F2-3 | 3, because frame shows 7 of 10. |
| s05-F2-4 | 7, because frame shows 2 of 10? Recount: three dots at top first, bottom second and fourth => 3, hence 7. |
| s05-F2-5 | 1, because frame shows 9 of 10. |
| s05-F2-6 | 8, because frame shows 2 of 10. |
| s05-F2-7 | 4, because frame shows 6 of 10. |
| s05-F2-8 | 2, because frame shows 8 of 10. |
| s05-F2-9 | 5, because frame shows 5 of 10. |
| s05-C101-F1 | For a selected split, one part gains one, the other loses one, total unchanged; direction not given. |
| s05-C102-F1 | Same relational invariant on child's selected split; no designated starting card. |
| s05-C103-F1 | Same relational invariant on child's selected split; no designated starting card. |
| s05-C101-F2 | My starting four and partner six fill ten, one mark per place. |
| s05-C102-F2 | My starting four and partner six fill ten, one mark per place. |
| s05-C103-F2 | My starting four and partner six fill ten, one mark per place. |
| s05-C101-F3 | My 1+3 and 2+2 each use exactly four stamps across the two albums. |
| s05-C102-F3 | My 1+3 and 2+2 each use exactly four stamps across the two albums. |
| s05-C103-F3 | My 1+3 and 2+2 each use exactly four stamps across the two albums. |
| s05-A103-F1 | Administrative scoring row, no new child question. Evidence should show correct total-preserving splits. |
| s05-A103-F2 | Administrative scoring row, no new child question. F2 partners in order 6,9,3,7,1,8,4,2,5. |
| s05-A103-F3 | Administrative scoring row, no new child question. Four-stamp solutions 1+3 and 2+2. |
| s05-A103-F4 | Carried evidence from unit four, not independently solvable here. No new child question. |

All arithmetic and conservation relationships agree with the authoritative keys. Different sample allocations are valid alternatives. The nine F2 pictures were independently counted, including their nonconsecutive occupied positions, rather than inferred from row numbers.

## Cold solutions after the changes

The six revised asks were solved again from their revised wording and unchanged pictures. These answers were recorded before the final gate.

| Item | New answer and method |
|---|---|
| s05-X88 | One triangle and six squares, then two triangles and five squares. Each design has seven pieces and the triangle counts differ. |
| s05-X94 | Two hats with only stars and five hats with only spots. Seven hats each belong to exactly one category. |
| s05-X95 | Two round-tab pieces and seven square-tab pieces, then three round-tab pieces and six square-tab pieces. Each picture shows nine pieces with one marked tab each. |
| s05-X96 | Trace the seven initial marks and the one incoming mark on A. Its joining action matches Rin's seven boats plus one. |
| s05-X101 | Add three missing-piece marks and join them to the visible seven with an enclosing mark or a linking line: seven plus three is ten. |
| s05-X102 | Show Rin with three peach pictures and seven plum pictures. Ten pictures total and the peach count differs from the supplied two. Eight peaches and two plums is also valid. |

The four other kinds of task retain their original answers: full-range F1 partitions, total-left equation correspondence, labeled four-stamp allocations, and the three retained-product conference explanations. The administrative carry row s05-A103-F4 also agrees with s04-A83-F1: 3 + 5 = 8 and 9 - 4 = 5, in either equation order. No unit 4 file was edited.

## Goal, grade and administration checks

- Decomposition items preserve the required whole, distinguish labeled from unordered pairs, and allow empty parts. Zero and one have only one unordered pair; two different pairs are required only for totals two through ten.
- Total-unknown and both-parts-unknown stories use the given quantities and one invented actor, Rin. The revised decoration and tab setups supply the necessary category constraints.
- Make-ten items preserve the given part and record the complement. The model-choice item has three models ending with eight, so final-result counting alone cannot eliminate the distractors. The equation-choice item has three true equations totaling ten; its pictured parts determine the match.
- Day 91's picture/equation record and the separate F1 equation ask test representation. The conference asks separately address one-up/one-down, the structure of ten and the two labeled story solutions. The teacher-only closing rows request no new student work.
- The original stems are at most 13 words. The revised stems are at most 12 words, and the six edited exit masters remain below the 60-word page cap by a text count. All labels and equations are read aloud, and existing drawing, pointing, dictation and directed-marking access remains available.
- Existing timing allows six 45-second observations within each eight-minute exit. The separate three-ask conferences require 2.25 minutes per child: 11.25, 22.5 and 33.75 minutes for the respective rosters of five, ten and fifteen, inside their 20-, 30- and 40-minute blocks. No new turns were added.
- Records use shown, shown with help and not yet seen; pending is a scheduling flag. Practice pieces and original assessment masters are distinct. Assessment source masters combined into the day 100 paper are alternative print sources, not additional required copies.

## Rule 4, pictures and disclosure

No duplicate practice case or identical stimulus picture was found among the exits and independent assessment products. Full retained-product conference explanations and administrative closure reuse the child's existing evidence by design, without recollecting the original task. I found no lower-grade case reuse in the filtered ledger results.

I cannot certify the separate literal numerical-reuse clause. The concrete four/six and other make-ten overlaps above remain, and the plans themselves state that finite pairs recur in the full-range records. No wording change in this report waives that clause.

No exit or end answer key was found on a child-held page. The private key files are identified in Before class, and the section 5.1 teacher-key.md file is a private-key location note. The total-ten label is necessary given information, not the unknown partner's answer. The square/triangle banks and story category icons are stimulus information, not printed solutions.

## Facts, sources and safety

Checked directly: counts in original vector pictures, every stated sum and complement, exhaustive/disjoint part conditions, the finite zero/one exceptions, and correspondence between each diagram and its key. Invented quantities are mathematical givens rather than claims about a real person, place, species or event.

The unit's sources.csv row s05-original covers days 87 to 103 and explicitly identifies these scenes and quantities as invented original work with no external factual hinges. The base-text rows supply sequence provenance, not a factual premise needed to solve these items. No external factual premise required a web page, no outside page was opened for this read, and no source was marked checked. Existing source statuses were left untouched.

Judged from the written conditions only: large adult-cut paper pieces, supervision, replacement of mouthed or damaged pieces with drawn marks, pictured fruit rather than food, and no required fingers or hidden children. These are not claims of classroom testing or measured safety. Browser check: none.

## Section plan field 3 lines requiring writer sync

The data writer owns these syncs; no section plan was edited.

| File / exit line | Stale text | Current items.csv text |
|---|---|---|
| docs/courses/math-kindergarten/u05-1.md, E88 | "Show two ways to make a seven-piece design using triangles and squares." | "Show two seven-piece designs with different numbers of triangles." |
| docs/courses/math-kindergarten/u05-2.md, E96 | "Circle the model that fits Rin's story." The paragraph also requires a circle with tracing. | "Trace Rin's starting boats and added boat on the matching model." No circle is required. |
| docs/courses/math-kindergarten/u05-4.md, E101 | "Show the partner that completes this tower of ten." | "Show ten by joining the missing pieces to these seven." |
| docs/courses/math-kindergarten/u05-4.md, E102 | "Tell a fruit story for ten with a different pair from this one." | "Show a ten-fruit story with a different number of peaches." |

E94 and E95 already include the exclusive-category constraints in field 3, so those section-plan lines are not newly stale. No other field 3 exit line differs from its corresponding item stem.

## My own errors

1. A truncated display omitted the zero panel from the text I could see. I initially recorded that it was missing and mentioned that candidate finding in progress. A targeted read confirmed s05-F1-0-1 is present; portfolio-99.md has all ten required panels. No zero-panel repair was made.
2. I initially treated eight peaches/two plums as a repeat of the unordered pair two/eight. Fruit labels distinguish those allocations, so the existing key is right to accept the swap. The actual wording ambiguity was repaired by specifying a different peach count.
3. While counting F2 row 4, I briefly wrote two occupied places, then recounted all three before comparing with the key. The recorded final complement was seven. This was my counting slip, not a key fault.
4. The combined day 100 paper alone did not state the first four-stamp setup. I initially suspected missing information, then confirmed d100.md explicitly directs the teacher to read that setup from story-record.md, which is named in its dependencies. The existing item steps also state four stamps. No missing-information finding remains.

## Gate and environment evidence

The final command was `python -X utf8 scripts/gate.py --course math-kindergarten`, with the environment below. It exited 0 and reported **0 failing findings against the stored baseline**, with **9 new informational note lines**. The 293 existing failing lines are unchanged.

New lines printed:

```text
note courses/math-kindergarten/u05-1/exit-88.md: blank, 16 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u05-1/key-teacher.md: story, 4082 words, 0 failure(s)
note courses/math-kindergarten/u05-2/exit-94.md: blank, 29 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u05-2/exit-95.md: blank, 33 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u05-2/exit-96.md: blank, 30 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u05-2/key-teacher.md: story, 3040 words, 0 failure(s)
note courses/math-kindergarten/u05-4/exit-101.md: blank, 19 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u05-4/exit-102.md: blank, 33 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u05-4/key-teacher.md: story, 4891 words, 0 failure(s)
```

The gate did not verify print pagination for the six changed student masters because Chrome wrote nothing. Text caps and mathematical checks do not establish rendered page count. No build command was run.

The initial launcher reported its executable as a directory. Setting PYTHONEXECUTABLE to the installed python.exe allowed child checks to run. Markdown and pypdf were absent, so copies were installed only in this job's permitted scratch dependency folder and supplied through PYTHONPATH. No repository script or system installation was changed. Earlier crashed gate attempts did not create a baseline; the first complete pre-edit run did.

Helper code, the exact change manifest and these temporary dependencies remain under _scratch/l87/tmp/math-kindergarten-key-u5/ for the lead to clear. No stray empty folder was observed.

## Could not settle

The literal no-reused-numbers instruction conflicts with this unit's required full-range assessment and the quantities deliberately taught in its shared instruction. This needs the lead's rule/design resolution; the original number range, goals, shared plan files and out-of-scope data were preserved. The four section-plan sync lines above remain with their owning writer.
