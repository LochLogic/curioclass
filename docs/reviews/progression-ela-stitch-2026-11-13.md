# ELA progression stitch, 2026-11-13

The five band parts (data/progressions/parts/ela-k2, ela-35, ela-68, ela-910, ela-1112) joined into
data/progressions/ela.csv, with data/progressions/ela-excluded.csv (header only: no band excluded a code).

## What the stitch did

- Rows: 374 (K 29, 1 31, 2 30, 3 28, 4 30, 5 30, 6 29, 7 28, 8 29, 9 24, 10 26, 11 30, 12 30), grade order,
  band order kept inside a grade.
- Cross-band handoffs: 144 written, both ends (2 to 3: 39, 5 to 6: 37, 8 to 9: 31, 10 to 11: 36, plus one
  longer handoff, e8-dramatic-irony to e11-lit-irony, with the reason in both rows' notes). Every first-grade-of-band
  row now assumes at least one row of the grade before.
- Models: no synonyms found; every band used the shared names. Re-introductions turned into model_in:
  figurative-language (e3-literal-nonliteral), narrative-arc (e3-story-parts), text-structure (e3-text-connections),
  claim-evidence-reasoning (e4-reasons-evidence), argument-map (e6-trace-argument), rhetorical-situation
  (e6-author-purpose, e9-ri-purpose-rhetoric). claim-evidence-reasoning had a gap in grade 3; e3-text-connections
  (RI.3.8) and e3-opinion (W.3.1) now carry it. point-of-view (new name from the 6 to 8 writer, no earlier band
  had one) is kept and carried on through the RL.x.6 rows of grades 9 to 12 (e9-rl-world-stories,
  e10-rl-world-literature, e11-lit-irony, e12-lit-irony).
- Gate: `scripts/progression.py check ela` 0 failures; `scripts/plan.py check` clean on the progression line.

## Writers' "For the lead" items, with picks

"Changes a grade?" means: does the pick move a standard or change what a row teaches. None does.

| # | Band | Item | Pick | Changes a grade? |
|---|------|------|------|------------------|
| 1 | K-2 | Labs optional; module lessons plus the skills block kept | Keep | No |
| 2 | K-2 | r-controlled vowels in grade 1 | Keep (base text order, inside RF.1.3) | No |
| 3 | K-2 | RF.K.3b long vowel as letter name; CVCe in grade 1 | Keep (the standards' own split) | No |
| 4 | K-2 | Base text's 12 module topics kept, with original texts | Keep | No |
| 5 | K-2 | Digital publishing through a teacher device, no child accounts | Keep | No |
| 6 | 3-5 | Grade 3 unit 3 classic replaced by an original two-book series (rule 29), classic optional | Keep | No |
| 7 | 3-5 | Grade 4 history set moved off the American Revolution (grade 5 social studies) to a grade 4 social studies event | Keep | No (text set only) |
| 8 | 3-5 | Grade 4 voting-rights set kept as a preview of grade 5 suffrage | Keep | No |
| 9 | 3-5 | RL.4.9 myth set beside the play | Keep | No |
| 10 | 6-8 | Dashes taught as student punctuation (L.6.2a, L.8.2a) although Curio Class prose uses no em dashes | Teach them (the standards ask for it); dashes appear only inside the exercise sentences students punctuate. For Cory | No |
| 11 | 6-8 | RL.8.9 on myths and folktales, no religious work as anchor | Keep. For Cory (audience) | No |
| 12 | 9-10 | Long texts: Romeo and Juliet, the Odyssey in parts, Frankenstein, Julius Caesar | Keep | No |
| 13 | 9-10 | Public-domain liberty set in place of a work under copyright for RI.9-10.9 | Keep | No |
| 14 | 9-10 | Public-domain world literature in translation is narrow | Flag kept: draw from at least three regions and fill a thin region with an original Curio Class text. For Cory (scope) | No |
| 15 | 9-10 | One unit a year of recent public-domain nonfiction or original texts | Keep | No |
| 16 | 9-10 | One style manual all four years | Keep; the course frame names an open one | No |
| 17 | 9-10 | Writing shares 40/40/20, reported by the frame | Keep | No |
| 18 | 11-12 | Grade 11 American literature beside US History I; grade 12 British plus early 1900s American | Keep | No |
| 19 | 11-12 | RL.11-12.7 with public-domain recordings and own staged readings | Keep | No |
| 20 | 11-12 | The 19th century novel with a racial slur is not an anchor | Keep. For Cory (audience) | No |
| 21 | 11-12 | Long texts: The Scarlet Letter, Douglass's Narrative, Hamlet, The Great Gatsby | Keep | No |
| 22 | 11-12 | Writing balance 40/40/20 | Keep | No |

## Settled in the stitch

| Item | Pick | Why |
|------|------|-----|
| Frankenstein named in grade 10 and grade 12 | Grade 10 keeps it (read whole); grade 12's independent long book is now Pride and Prejudice (1813), offered first | Grade 10 rows are built on it: RL.9-10.5 nested frame narratives, RL.9-10.3 Victor and the creature, the W.9-10.3 two-narrator story. In grade 12 it was only an optional independent book; Pride and Prejudice fits the British year and carries on from the opening chapters e12-lit-irony reads |
| Douglass's July Fifth speech in grade 10 (e10-ri-seminal-documents set) and grade 11 (e11-info-rhetoric anchor) | Not changed; for the lead. Pick: keep it in grade 11, where it is read in parts for rhetoric, and swap grade 10's set item for another public-domain liberty text (for example Susan B. Anthony's 1873 speech on her vote) | Two bands planned the same text; a text suggestion, so the course frame settles it |

## Strands that stop

Only foundational, which ends after grade 5 as the standards do (RF stops at grade 5). The other five strands run
K to 12 without a gap.
