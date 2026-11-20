# Health: the standard, made usable

**DRAFT, 2026-11-16, fixed 2026-11-19 after a cold read (docs/reviews/prework-health-read-2026-11-19.md).**

Written 2026-11-16 as pre-work for health (four courses, one per band). It answers the health row of "Before a
scope and sequence in this subject" in docs/ADOPTION-BAR-SUBJECTS.md. The bar is the health part of that page. The
lens is docs/agents/lenses/health.md. The approach page is docs/courses/health/APPROACH.md (draft).

| Owed | State | Where |
|---|---|---|
| Read one topic module | Done in part 2026-11-16: the Sexual Health module's description, instructions, PreK-2 and 3-5 knowledge expectations and scoring pages; Appendix 3 (all behaviour outcomes) and Appendix 5 (building a scope and sequence) | Section 3 |
| Write the band coverage map | Done (draft, ours) | Section 4 |
| Write the 2007 to 2024 note | Done 2026-11-11 | docs/standards-notes/health-2007-to-2024.md |
| Fix the file header to "SHAPE America, 2024" | Done 2026-11-11 | data/standards/nhes-2024.txt header |
| Keep the 2024 standards, with the mapping to the older-keyed tool | Done (decided 2026-11-11) | Section 1; the 2007 to 2024 note |
| Carry all sensitive topics, each unit removable | Rule written | Section 5 |
| The expert read for criterion 7 | Settled 2026-11-16 (Cory, Desk card q-later-arts-health-pe): a self-built health expert agent, no paid read | Section 6; docs/agents/lenses/health.md |

## 1. The standard and the review tool

- **Standard:** National Health Education Standards, 2024, SHAPE America (it calls this the third edition).
  Always named "SHAPE America, 2024". Loaded in data/standards/nhes-2024.txt: 172 indicators, ids only,
  `NHES.S<standard>.<span end>.<n>`, spans ending at grade 2, 5, 8 and 12. Eight standards: use health
  information; analyse influences; find valid and reliable resources; communicate with others; decide; set goals;
  practise healthy behaviours; advocate.
- **Review tool:** CDC's Health Education Curriculum Analysis Tool (HECAT), 2021 edition. Topics and healthy
  behaviour outcomes are in data/standards/hecat-topics.txt (9 topics with 81 outcomes, plus the combined module).
  The tool is keyed to the 2007 standards; our mapping is docs/standards-notes/health-2007-to-2024.md. Both
  editions are named wherever the tool is used.
- scripts/standards.py checks the standard (1 to 8), the span end (2, 5, 8 or 12) and a one or two digit number; it
  does not check that the number exists, and it does not check HECAT ids. scripts/progression.py checks both
  against the files. The coverage map cells below are not machine-checked.
- **Our words.** Each NHES id in nhes-2024.txt carries one line in Curio Class's own words, and each HECAT outcome
  in hecat-topics.txt one plain line (2026-11-19). Plans cite the id and state its action in these words.
- **Module skill expectations** are keyed to the 2007 indicators. They are read against the 2024 standard of the
  same number; the planner picks the 2024 indicators by matching the skill's verb and records the match on the unit
  plan. Standard 1 is reread against NHES.S1 itself (the 2007 to 2024 note). No indicator-by-indicator crosswalk.

## 2. Reuse terms (read at source, 2026-11-16)

- **SHAPE America, 2024:** the free standards page shows the standards and indicators in full, with no reuse terms
  and a site footer of "All Rights Reserved". The book is sold. So: ids and our own words only, as for every
  all-rights-reserved instrument. No indicator sentence is copied into a page.
- **HECAT 2021:** a CDC publication, a US government work. Its topic names and outcome numbers are used freely.
  We still write outcomes in our own words, so a page never reads as the tool's checklist. Module text is not
  copied into lessons, and no page says Curio Class was scored by or meets the tool.

## 3. What the topic module showed (read in part)

From the Sexual Health module and appendices 3 and 5 (our words):

- Each module lists knowledge expectations by span, each tagged to the outcomes it serves, then skill
  expectations under standards 2 to 8. A curriculum is scored on how much of each list it covers. Standards 2 to 8
  get two scores: whether the skill is named, and whether students practise it.
- Users are told to add, drop or revise expectations to fit local needs. That is the tool's own room for a
  school to leave out a unit.
- Expectations deepen by span. In this module the early span has a handful (body part names, families, safe and
  unsafe touch, germs); the next has about twenty (puberty, relationships, consent, gender identity defined,
  HIV basics); the middle span has many more.
- Appendix 5: a scope and sequence shows balance across topics, reinforces without repeating, builds each skill
  across topics, and is checked with a coverage map of standards by span and topic. A single topic need not
  carry all eight standards; the whole program must.
- Still unread: the other eight modules' span tables. Each band's unit planner reads the modules its units use,
  before the units are planned.

## 4. The band coverage map (draft, ours)

Outcomes are HECAT 2021 numbers (`HECAT.<topic>.HBO<n>` in hecat-topics.txt). "All" means every outcome of the
topic. "(s)" marks a sensitive unit (section 5). This is our placement, made from the outcome list and the module
read; it is checked against each module's span tables when the band's units are planned.

| Topic | K to 2 | 3 to 5 | 6 to 8 | 9 to 12 |
|---|---|---|---|---|
| Personal health and wellness (PHW) | 1, 2, 3, 4, 5 | 1 to 9 | All but 12 | All |
| Food and nutrition (FN) | 1, 2, 3, 6, 7 | 1 to 8, 12 | 1 to 9, 12 | All |
| Mental and emotional health (MEH) | 1, 2, 3, 4, 5, 7 | 1 to 5, 7 to 9 | All; 6 in a sensitive unit (s) | All; 6 in a sensitive unit (s) |
| Physical activity (PA) | 1, 4, 6 (with PE) | 1 to 7 (with PE) | All (with PE) | All (with PE) |
| Safety (S) | 1, 3, 4, 5, 6, 7 | 1, 3 to 8 | All | All |
| Violence prevention (V) | 1, 3, 7; 8 in body safety (s) | 1, 2, 3, 5, 7; 8, 9 in body safety (s) | 1 to 3, 5 to 7; 4, 8, 9, 10 in a sensitive unit (s) | All; 4, 8, 9, 10 in a sensitive unit (s) |
| Tobacco (T) | 1, 2 | 1, 2, 3, 4 | All | All |
| Alcohol and other drugs (AOD) | 1 (medicine safety) | 1, 2, 3 | 1 to 4, 6, 8 | All |
| Sexual health (SH) | 1, 2, 3 (s) | 1, 2, 3, 4, 6 (s) | 1 to 9 (s) | All (s) |

Key: a number listed in a sensitive part of a cell is taught only in the sensitive unit. MEH 6 is not taught
before grade 6; a grade 3 to 5 mental health unit teaches getting help for sad or worried feelings under the
help-seeking outcome, which the planner confirms from our outcome wording. PHW 12 is left to 9 to 12; the 6 to 8
planner confirms the reason from its wording. In the 9 to 12 column, an outcome 6 to 8 already teaches is a
revisit (a short practice unit), not taught again in full.

Standards by band: every band teaches all eight NHES standards across its topics, and every skill standard
(2 to 8) is practised in at least two topics in the band. Each band's scope and sequence carries the full map in
this shape, with unit names in the cells, plus a second table of NHES standards by unit.

**Years within a band.** NHES indicators are written per span, not per grade. Bands K to 2, 3 to 5 and 6 to 8
are three grade years each: the scope and sequence names each grade's units, and each topic is claimed at least
in alternate years. Each year touches all eight standards. Band 9 to 12 is one course of one semester: it teaches
in full the outcomes not met by grade 8 and revisits the rest. If the 9 to 12 map cannot fit a semester even so,
the planner brings it to Cory rather than dropping outcomes. Topics return each year at more depth; a topic is
never a one-off lesson (bar criterion 5).

**In the progression** (data/progressions/health.csv): each indicator has exactly one owner grade, the grade where
it is first fully met, in any grade of its span, and is met no later than the span's last grade; other grades of
the span that prepare or reuse it carry `~CODE`. For 9 to 12 the owner grade is the grade of the semester course
(grade 9 unless the frame says otherwise). scripts/progression.py checks this.

## 5. Sensitive topics: all carried, each unit removable

Decided 2026-11-11: Curio Class carries all of the tool's sensitive topics, and each sensitive unit can be left out
without breaking the course. The rule:

1. **Sensitive content lives in its own units.** These units are sensitive: sexual health (every band); body
   safety, meaning unwanted touch and abuse (V 8, 9; K to 5); sexual violence, abuse and dating violence (V 4, 8, 9;
   6 to 12); suicide and self-harm (MEH 6, V 10; 6 to 12). No sensitive content sits inside a non-sensitive unit.
2. **No skill lives only in a sensitive unit.** Each NHES indicator claimed in a sensitive unit is also claimed
   in a non-sensitive unit of the same band. A sensitive unit practises a skill already taught elsewhere.
3. **Getting help is taught twice.** How to tell a trusted adult and where to find help is taught in a
   non-sensitive unit (safety or mental health) in every band, so leaving out a sensitive unit never leaves a
   student without it.
4. **No later unit assumes a sensitive unit,** except a later sensitive unit on the same topic.
5. **Each sensitive unit has a leave-out note** on its first page: what it covers, the outcomes and indicators
   that go with it, what the course still meets without it, who is affected by leaving it out (for growing-up
   content, children whose bodies change early), and that the school or family decides. Correct body part names
   are first taught in non-sensitive terms in Personal health and wellness, K to 2, so leaving out a sexual health
   unit never removes them; this is the one place the sensitive-unit rule is eased. A family note
   (English and Spanish) goes home before it, with the outline and how to opt out, in the school's own process.
6. **Day counts.** A sensitive unit's days are counted as optional. A school that leaves it out has those days free;
   the scope and sequence names a non-sensitive unit to extend.
7. **Content.** Sensitive units are medically accurate, age-matched to the tool's span expectations, inclusive,
   free of scare tactics and shame, and dated.

## 6. The expert read (bar criterion 7)

Settled 2026-11-16 (Cory, Desk card q-later-arts-health-pe): "no outside readers available. use a self built
expert agent". No paid read and no spend. Criterion 7 is met this way:

- **Who reads.** A health expert agent, built for this subject from the expert read section of
  docs/agents/lenses/health.md. It is the named reader; its name in the record is "Curio Class health expert agent".
- **What it reads.** Every health unit plan and every health day, before the unit's Exit check, for medical and
  scientific accuracy: facts, figures with their source and year, correct terms for the age, and safe messaging on
  sensitive topics. It reads against current public health sources, not memory alone.
- **The record.** Each read is dated and kept with the unit (the reader, the date, what was checked, what was
  fixed). A unit or day changed after its read is read again. A figure older than its source's latest edition is
  a finding.
- **Public copy.** The record stays in our docs. A course page may say: "Figures last checked against their
  sources on DATE. A school's health staff should read it too." It never says or suggests a clinician read it, and
  never names how the read was done (public pages do not describe our tools).
- **The job brief** for this reader (sources by topic, what to record, web access needed) is written when the
  first health unit plan is ready. It never claims the
  content was reviewed or approved by anyone (AGENTS.md).

## 7. Left out, and why

- No separate pre-kindergarten indicators exist: the PreK-2 span is taught from kindergarten, so all 172 are in
  play.
- The National Consensus for School Health Education set of the same name (2022): a different publisher; one set is
  loaded.
- The combined module (CHE) as a topic: it has no outcomes of its own.
- State health standards and state-required topics (for example, specific drug or safety laws): the course page
  says a school adds them.

## 8. Leans on the core progressions and other subjects

- **Physical education:** the physical activity topic is shared. Health teaches why and planning (PA outcomes
  as knowledge and goal-setting); PE teaches the moving. Units in each name the other.
- **Science:** body systems, puberty, germs and disease, nutrition chemistry lean on the life science progression;
  a health unit does not reteach the science model, it uses it.
- **Math:** reading food labels, serving sizes and simple data on behaviour lean on ratio and statistics (grades
  6 to 7); health uses the skill, math teaches it.
- **ELA:** analysing influences (standard 2) and finding valid sources (standard 3) lean on the reading information
  and research standards; advocacy (standard 8) leans on argument writing and speaking.
- **SEL:** communication, decision and goal skills overlap with the SEL courses; the SEL course page and this one
  name each other so a skill is not taught twice in the same year.

## 9. Existing topic stubs

The 21 health stubs in data/modules.csv are placeholders. Each band's scope and sequence keeps, renames or drops
each with its reason: body-systems content is used from science, not retaught; digital wellness sits inside MEH, S
and V as skills; first aid sits in Safety.
