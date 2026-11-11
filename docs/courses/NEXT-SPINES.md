# Sara's next work: spines, approach pages and rubric files

Set up 2026-11-11 (Cory: "yes write it but lets give her a bit more to do, even if it needs corrected later";
"maybe she can also do the drafts for the approach pages and rubric files for science and english"). This is the
work after batch 4 of docs/spec-fixes/NEXT.md, and it can start sooner if a batch is waiting on something.

It replaces the earlier plan of "unit pieces" for now. Unit pieces cannot start until the unit plan fields are
tried on three units (ROADMAP step 4c), which Cory's session is doing. Nothing on this page is blocked.

**Everything made here is a draft.** It will be corrected by the grade 4 pilot unit and by Cory's read. That is
expected and fine. A draft that exists and has been read by the expert is worth more than a perfect one later.

## Read first (once)

1. docs/FOUNDATION.md. Nothing may contradict it.
2. docs/ROADMAP.md, "The layers".
3. docs/APPROACH.md and docs/APPROACH-MATH.md, and the review that shaped them: docs/reviews/approach-2026-11-11.md.
4. docs/courses/math-4-spine.md (the model for every spine: copy its sections and tables), and
   docs/reviews/math-4-spine-2026-11-11.md (what the expert caught in it).
5. docs/courses/math-3-5-progression.md (the model for a progression page) and its findings file.
6. docs/agents/EXPERT.md (how the curriculum expert is run).

## How every piece is made

The same five moves each time. Your Claude session does the reading and drafting; you steer and judge.

1. **Gather.** Read what the piece rests on (listed under each piece below). For outside sources start from
   docs/APPROACH-SOURCES.md, which has working addresses and the way to open a PDF. No library access: a paywalled
   source stays unread and nothing may rest on it.
2. **Draft.** One file, in the place named below. Plain words. Every claim about the standards quotes the standard's
   own verb and code. Every claim about how students learn names a source that was opened, and says how much of it
   was read.
3. **Expert read.** Run the curriculum expert cold: a fresh agent told to read docs/agents/EXPERT.md first and
   follow it, given the file to review and what will be built on it. Its report goes in
   docs/reviews/<what>-<date>.md.
4. **Revise once** from the report. Corrections are applied. Anything that changes what a course teaches, who it is
   for, or a rule of the site is not applied: it goes to Cory as a question card on the Review Desk with a pick, and
   is written into the draft as "Proposed, waiting for Cory's yes".
5. **Record and push.** Tick the piece below, add one line to docs/agents/decisions/DESK-ANSWERS.md, commit and push
   your own files.

**Your part, Sara.** Read each draft as the teacher who would have to use it. The expert checks sources; you are the
one who can say "no one could teach this in a week" or "this order would lose my class". Write what you see at the
top of the review file under "Sara's read". That note goes to Cory with the draft.

## The pieces, in order

### 1. Grade 3 math spine

- [ ] docs/courses/math-3-spine.md, expert read, revised once.
- Rests on: the grade 3 standards in data/standards/, docs/courses/math-3-5-progression.md (what grade 4 needs from
  grade 3 is already written there, stretch by stretch), docs/agents/catalog/shape/math-3.md (the tools that exist),
  docs/RUBRIC-MATH-K8.md, and the scope and sequence of two well-reviewed open grade 3 courses.
- Must show: every teaching day of the year in order; major work at 65 percent or more of days; the stretches and
  units; the limits of the grade; builds-on and sets-up by code; where each major idea comes back; the checks at
  the stretch, each cumulative check with a respond day; a fluency plan (3.OA.C.7 and 3.NBT.A.2 are this grade's);
  what is missing today, said plainly.
- Grade 4 depends on: fractions as numbers on the number line, multiplication and division facts from memory by the
  end of the year, area as rows and columns.

### 2. Grade 5 math spine

- [ ] docs/courses/math-5-spine.md, expert read, revised once.
- Rests on: the same, with docs/agents/catalog/shape/math-5.md. The progression page says what grade 4 hands over.
- Watch: the standard algorithm for multiplication is this grade's fluency (5.NBT.B.5); decimal arithmetic starts
  here (5.NBT.B.7); fraction work is the largest block.

### 3. Science: rubric files, then the approach page

- [ ] docs/RUBRIC-SCIENCE-K5.md (and 6 to 8 if the same guide covers it). Follow the shape of
  docs/RUBRIC-MATH-K8.md: what the rubric asks, indicator by indicator, in our own words, with a link. The
  curriculum review organizations' text is all rights reserved: link and summarize, never copy. Sources: the
  EdReports science evidence guides and the EQuIP rubric for science (addresses in docs/APPROACH-SOURCES.md, or
  found from them).
- [ ] docs/APPROACH-SCIENCE.md, expert read, revised once. It says how science carries out each of the ten shared
  principles. The approach review already listed what it must add or override (docs/reviews/approach-2026-11-11.md,
  finding F1): a phenomenon or design problem comes first as the rule, with sense-making and teaching following;
  three dimensions in every end task; investigation days and materials tiers; no daily exit question (the notebook
  and the class model are the daily evidence); worked examples apply to calculation and data work, not to building
  an explanation; models are revised, not withdrawn. It must also read at least one source on hands-on science
  teaching, which the shared page admits nobody has read. Main sources: A Framework for K-12 Science Education, the
  NGSS appendices, the EQuIP rubric.
- When both exist, the grade 4 science spine (a draft waiting for Cory's final yes) gets one more expert read
  against them.

### 4. English language arts: rubric file, the approach page, the text plan

- [ ] docs/RUBRIC-ELA.md (grades 3 to 8, and 6 to 12 where the guide differs). Same shape and same copying rule.
- [ ] docs/APPROACH-ELA.md, expert read, revised once. From the same review finding: the text is the unit; text
  complexity; text sets that build knowledge; volume of reading; the writing process and the writing calendar;
  vocabulary taught from the texts; foundational skills in the lower grades; the daily question is always about the
  text; "model then fade" becomes modelled reading and writing, with weaker evidence than math worked examples;
  "fluency" here means reading fluency. Main sources: the ELA standards and their appendices, the publishers'
  criteria for ELA, the federal practice guides on reading comprehension, foundational skills and writing.
- [ ] The grade 6 ELA text plan (docs/courses/ela-6-spine.md): every text marked "to verify" is checked (it exists,
  where a free legal copy lives, its licence, its level), and an informational shelf is proposed. Changes to which
  texts are taught go to Cory as a card.

### 5. More math spines, working outward from grade 4

A progression page comes before the spines of its band, the same way the grades 3 to 5 page came before these.

- [ ] docs/courses/math-k-2-progression.md, then
- [ ] docs/courses/math-2-spine.md
- [ ] docs/courses/math-6-8-progression.md, then
- [ ] docs/courses/math-6-spine.md
- [ ] docs/courses/math-1-spine.md
- [ ] docs/courses/math-7-spine.md
- [ ] docs/courses/math-k-spine.md
- [ ] docs/courses/math-8-spine.md

Two things are undecided and must be marked, not settled: whether kindergarten to grade 2 assumes a device per
student (FOUNDATION, section 5), and how a K to 2 day is shaped. Write the K to 2 spines so they work either way,
and say where the answer would change them. The rubric for grades K to 2 counts major work at 65 percent of days
too; check docs/RUBRIC-MATH-K8.md.

## Rules for all of it

- No rows go into data/units.csv, and no tool is specced, built or changed from these drafts. A spine becomes real
  only with Cory's yes.
- Do not edit the grade 4 math spine or the approach pages. If a draft shows one of them is wrong, write the finding
  in your review file and on a Desk card.
- No em dashes anywhere. Always "Curio Class" in full. Never say Curio Class was reviewed by, meets or is endorsed
  by anyone. Public copy names no companies.
- Do not touch the Word Wall files (data/closet, closet/words, data/media-manifest.txt).
- Where you are unsure, say so on the page. A marked guess is useful; an unmarked one costs a unit.
