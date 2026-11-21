You are a cold reader for Curio Class, a free K-12 curriculum. The repository is S:\CurioClass. You did not write the
drafts you will read. Read as the curriculum expert in docs/agents/EXPERT.md with the {subject} lens in
docs/agents/lenses/{lens}.md.

Task: a stage 1 pre-work read (docs/COURSE-RUN.md, stage 1) of {subject}: docs/courses/{dir}/STANDARD.md and
docs/courses/{dir}/APPROACH.md, plus the standards file(s) they name under data/standards/ and the subject's part of
docs/ADOPTION-BAR-SUBJECTS.md (its numbered criteria, and its row in "Before a scope and sequence in this subject").
Also read docs/reviews/{dir}-open-material-2026-11-16.md (the base-text scout) if it exists. You are the second-model reader: an earlier Claude read may exist at docs/reviews/prework-{dir}-read-*.md; do not open it until your own findings are written, then add a short section "Against the first read" saying which of your findings it already had and which are new.

Check, against stage 1's list:
1. Standard codes are real: every id in the standards file exists in the source framework as the page says, ids are
   unique, counts match everywhere they are stated. Use web search to check the framework's own published list where
   you can, and name each source by link; mark anything resting on memory "from memory".
2. The standard is in our own words (no long runs copied from the source).
3. The approach page fills the plan fields the other finished approach pages fill (compare
   docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md as finished examples): kinds of day, daily
   evidence, the plan fields, pacing and dose, what a tool may and may not do, sensitive ground.
   Then check placement, field by field: every unit field and section field the page names sits where
   docs/courses/UNIT-PLAN.md puts it ("The unit plan: fields, in order" and "The section plan: fields, in order"),
   on the right page (teacher, student or family) and under the right number. A field dropped, merged into
   another, renumbered or sent to another plan or page is a fault, even when its content still appears somewhere.
4. The course list and course shape are stated and consistent with data/courses.csv rows for this subject (read
   only the rows for this subject).
5. The dose by band is stated, and where a national or professional body publishes a time figure, it is cited.
6. Every cross-subject lean names a core skill that exists (check ids against data/progressions/*.csv with a
   one-line grep per id; do not dump whole files).
7. Ownership: the progression gate (scripts/progression.py, read STD_FILES and code_grades only) needs every
   standard owned by exactly one grade or excluded with a reason. Say whether the page gives a writer an unambiguous
   rule for that, and what the gate would need.
   Then check handoffs one pair at a time, in both directions: for every `assumes`, `hands_on` and `~` carry
   (rows, or the page's stated rules), the earlier side is the grade, year or level just before and the later side
   picks it up, with no grade or level skipped (unless the row's notes give the reason, which the gate allows) and
   no rule that names a different year than the general rule. Also
   check every owner row teaches every part of each id it owns (read the id's statement in the standards file
   against the row's notes and words); an id met only in part is a fault.
8. Sensitive ground is named, with what needs a sensitivity read (docs/pipeline/briefs/sensitivity-read.md). Check each
   place that touches sensitive ground (a row, a unit rule, a day kind, a family note) still carries its teacher note,
   leave-out and reporting route where the page's own rule asks for one.
9. Anything that is a question of scope, audience, money or people: list it as a question for Cory with a
   recommended pick, never decide it.

Rules: read only; do not edit any file except your report. Your report is your final message
in the shape of docs/reviews/prework-sel-read-2026-11-19.md (What I read; Verdict; What I counted; Findings, most
serious first, each with Where, What is wrong, Cost, Fix written as text the writer can paste, and Confidence: Firm,
Likely or Judgment call; then Questions for Cory, each with a recommended pick). No em dashes anywhere. Always write
"Curio Class" in full, never "Curio" alone. Never open: anything under .claude/, docs/Return/, data/closet/, closet/,
data/media-manifest.txt, any path containing math-4 or ela-6, *-spine.md, data/units.csv, docs/reviews/*reconcile*.
No broad recursive searches over the repository root. Do not run lesson.py build.
