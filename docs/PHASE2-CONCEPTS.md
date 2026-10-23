# Phase 2: Tool Concepts

Status: DRAFT, 2026-10-22. Concepts only, nothing built.
586 tool concepts, one for every module. Concepts use 21 formats, and 86 shared "families" (engines reused across tools) cover 253 of them.

Files:
- `data/concepts/*.txt`: source, one line per tool: `module_id|title|format|family|concept`
- `data/formats.csv`: the 21 formats (play styles)
- `data/tools-concepts.csv`: generated catalog (`python scripts/check_concepts.py --write`)
- `scripts/check_concepts.py`: checks coverage, valid formats, unique titles and variety

## Variety: not cookie-cutter

Every tool is professional, but each subject mixes play styles. The checker enforces this:
- **No format above 25% of any subject.** Actual highest: CTE simulator 21%, arts studio 20%. Big subjects stay under 18%.
- **Each subject uses at least 8 formats** (or all of them, if it has fewer than 8 modules). Math, science, social studies and ELA use 19-20 of the 21.
- **No three tools in a row with the same format** within a grade.
- **No duplicate titles.** Every tool has its own name and personality.

| Format | Tools | Format | Tools | Format | Tools |
|---|---|---|---|---|---|
| Builder | 59 | Studio | 35 | Story | 23 |
| Explorer | 57 | Role Play | 30 | Mystery | 21 |
| Simulator | 57 | Sandbox | 28 | Map | 21 |
| Puzzle | 43 | Tycoon | 28 | Card Game | 19 |
| Lab | 37 | Class Showdown | 25 | Race | 16 |
| Data Desk | 25 | Sort | 23 | Arcade | 15 |
| Timeline | 11 | Creature | 7 | Escape Room | 6 |

A few examples of the range:
- **Balance the Beam** (grade 1): a balance-scale puzzle that kills the "equals means the answer comes next" myth.
- **Medical Test Paradox** (Geometry, probability): a simulator showing why a positive test isn't the whole story.
- **Bug Hunt** (grade 8, natural selection): you're the bird, and camouflage evolves in front of you.
- **Fed Chair** (Economics): set interest rates and live with the consequences.
- **Fair Use Court** (library, 9-12): rule on memes and remixes with the four factors.

## Families: how the site gets built and browsed

A family is one engine reused across tools (for example `number-line`, `graphing`, `ml-lab`, `money`, `spanish`, `asl`). Families matter twice:
1. **Build economy (Phase 3):** build the engine once, then each new tool is mostly content. The 15 largest families cover about 100 tools.
2. **Site structure:** families become **collections** teachers can follow across grades. For example, a "Money" collection runs from Corner Store (grade 2) to the Market Time Machine (12th-grade personal finance).

Largest families: spanish 11, money 9, asl 9, data-desk 9, graphing 8, research 7, evidence 6, number-line 5, ml-lab 5, feelings 5, founding-docs 5.

## What this means for the site

Each tool's card (and its page) shows:
- **Title and one-line hook**, from the concept
- **Module, grade and subject**, with standards codes from Phase 1
- **Format badge** (Puzzle, Mystery, Tycoon...) so teachers can pick a play style for the day
- **Collection link**, if the tool is in a family
- **Who drives:** teacher on projector (all K-2, plus every Class Showdown) or students on devices

Browsing paths (from the Phase 1 decisions plus this phase):
- **Grade** → subject → module → tool
- **Grade band** (for example, all of 6-8 science)
- **Topic search** (American Revolution, fractions, photosynthesis)
- **Standard code** (NGSS MS-PS1-4 → tools)
- **Play style** (all Mysteries, all Class Showdowns for a Friday)
- **Collections** (Money, Data Desk, ASL, Spanish...)

## Content guardrails written into the concepts

- **K-2 is teacher led.** Every K-2 tool, whatever its format, is designed to be driven on a projector or smartboard by the teacher while the class responds.
- **Hard history is never gamified.** Slavery, the Holocaust and Native removal use Explorer formats with primary sources, testimony and teacher guidance. No points, timers or win states.
- **Literature uses public-domain texts** (or our own original writing) so tools can be free and shareable.
- **ASL tools use video by Deaf signers** and are reviewed by Deaf educators before release.
- **Health topics** (growing up, substance use, mental health) are configurable to district policy and link to support resources.
- **No student data leaves the device.** Recording, journaling and question-box tools store only in the browser.
- **Finance tools are educational only.** They use historical index data, never picks or advice.
- **Existing tools mapped:** The Elements Inspector → Chemistry, atomic structure. State Quest → grade 4, US regions and states.

## Next (Phase 3 planning, not started)

- [ ] Cory reviews the concepts (skim by subject; flag any to rethink)
- [ ] Pick a pilot set for Phase 3: a handful across grades and formats, built on 2-3 families, plus the two existing tools
- [ ] Design direction for the site and tools (template is parked; fresh design pass)
