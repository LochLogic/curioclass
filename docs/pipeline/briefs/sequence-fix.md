# Job: apply the reads of the scope and sequence of {course}

Added 2026-11-15 (PRODUCTION-PATH step 3, the fix pass after the expert read). The scope and sequence of {course} was
written by Codex (docs/pipeline/briefs/sequence-write.md), read by Codex, then read by a Claude expert. You apply both
reads. Model the work on the social studies fix reports (docs/reviews/sequence-3-5-fixes-2026-11-14.md).

## Read first (in S:\CurioClass)
1. AGENTS.md; docs/GLOSSARY.md; docs/pipeline/briefs/sequence-write.md, all of it (it has changed since the course was
   written: every rule in it binds now) and docs/pipeline/briefs/sequence-read.md.
2. The expert read docs/reviews/sequence-{course}-2026-11-1[45].md (the newest one that is not -codex) and the Codex
   read docs/reviews/sequence-{course}-codex-2026-11-1[45].md.
3. The lead calls docs/reviews/sequence-lead-calls-2026-11-15.md: "Every subject" and your subject's section. They are
   settled; apply them, do not re-decide them.
4. The "Across the band" section of every other expert read in your subject
   (`docs/reviews/sequence-*-2026-11-1[45].md`, skipping -codex): apply each item that touches your course.
5. Your course: docs/courses/{course}/frame.md, docs/courses/{course}/scope-and-sequence.md, data/plans/{course}/days.csv
   and source-map.csv where it exists; data/plans/calendar.csv; the progression rows (data/progressions/{subject}.csv);
   the lens docs/agents/lenses/{subject}.md and the bar: {bar}.

## The work
1. Apply every expert finding (serious, moderate and minor) and every row of the expert's "Settled by the expert"
   table. Apply every Codex finding the expert did not reject; where the two reads disagree, the expert wins unless you
   can show from the files that it is wrong (then say why). Do not re-decide what the expert settled.
2. Then the lead calls and the band items. Then re-run the brief's rule 2 lists yourself: every earlier-grade row with
   its last-use grade and treatment; each check's sampled codes; Collect once; each part of each code; end days; our
   words. Fix what you find and log it as your own finding.
3. Units, their order, owned rows and day counts stay as the frame sets them, except where a finding or lead call
   changes the frame; then change frame.md and days.csv together and say so.
4. Every change is logged. Nothing is called done that a gate fails.

## Files
You own, alone: docs/courses/{course}/scope-and-sequence.md, docs/courses/{course}/frame.md, data/plans/{course}/days.csv
and data/plans/{course}/source-map.csv. Other fixers run at the same time on other courses. Do not edit any other file:
data/progressions/*.csv, data/plans/frames.csv, data/plans/calendar.csv, data/plans/ela-texts.csv, another course's
files, DIGEST, later.csv, the standards files, any script, brief, glossary, calendar or path doc. List each change those
need, exact (file, row or line, old, new), under "For the structure pass" in your report; one structure pass applies
them all afterwards.

## Gates
`python -X utf8 scripts/sequence.py check {course}` (0 failures; it now also gates the source-map layout) and
`python -X utf8 scripts/frame.py check {course}`. Then `python -X utf8 scripts/frame.py calendar`: say whether your
course breaks the stagger rule (the calendar is regenerated in the structure pass, so a break caused only by a frame
change you made is expected; name it).

## Report (your last message, filed as it stands)
`# Fixes: scope and sequence of {course}, {date}`, then:
- **Applied**: one line per finding (expert n, Codex n, lead call, band item, own): file, what changed.
- **Not applied**: each with the reason.
- **Settled** (for DIGEST): a short table of the judgments you made that later writers should reuse.
- **For the structure pass**: exact edits to shared files.
- **For Cory**: only scope, money, people or audience (expect none).
- **Gates**: each gate's result.
Counts at the top: applied / not applied, by source.
