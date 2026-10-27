# Curio Class: standards coverage and overlap after spec wave 1

**Superseded 2026-10-27:** the code pass and the new modules suggested here are done. Current numbers and what changed:
`docs/agents/gapfill/REPORT.md`.

Written 2026-10-27, after the 75 wave 1 specs (BATCH-W1.md, log in BATCH-W1-LOG.md). It updates gaps.md (the first
overlap pass) with full official code lists, so every number below is "covered of the whole framework", not "covered
of the codes we happened to use".

How to rerun:
- `python scripts/overlap/coverage.py --missing` measures every framework per band at three stages.
- `python scripts/overlap/wave_standards.py docs/agents/BATCH-W1.md` compares each spec's standards with its module.
- `python scripts/overlap/rule.py --after` re-runs the clash rule on tags.csv (wave 1 now tagged from its specs).

The official lists live in `data/standards/` with their sources in each file's header.

A code counts as covered when the module of at least one tool carries it. "Live" means built and on the site; "all" adds
every specced and planned tool. A tool coded to a sibling standard may cover a gap in substance, so treat a gap as
"no tool claims this", not "no tool teaches this".

## Coverage at a glance

| Framework (official list) | Unit | Live | Live + specced | All planned |
|---|---|---|---|---|
| NGSS performance expectations | 208 PEs | 14 | 17 | 196 (94%) |
| CCSS math clusters | 147 clusters | 23 | 23 | 143 (97%) |
| CCSS ELA grade-level standards | 455 | 5 | 7 | 169 (37%) |
| ELA anchor x band (same data, coarser) | 167 cells | | | 103 (62%) |
| C3 social studies indicators | 283 | 10 | 12 | 116 (41%) |
| CSTA 2026 computer science | 196 | 15 | 85 | 85 (43%) |
| NCAS arts anchors x band (5 disciplines x 11 x 4) | 220 cells | 18 | 65 | 65 (30%) |
| NHES health standards x band | 32 cells | 11 | 23 | 23 (72%) |
| SHAPE PE standards x band | 16 cells | 1 | 9 | 9 (56%) |
| AASL foundations x band | 24 cells | 3 | 13 | 13 (54%) |
| CASEL competencies x band | 20 cells | 8 | 8 | 8 (40%) |
| WIDA standards x band | 20 cells | 5 | 5 | 20 (100%) |
| WIDA language uses x band | 16 cells | 2 | 2 | 11 (69%) |
| NSPFE personal finance x benchmark band (4, 8, 12) | 18 cells | 2 | 2 | 6 (33%) |

Wave 1 moved CSTA from 15 to 85, arts from 18 to 65 cells, health from 11 to 23 and PE from 1 to 9. In the non-core
subjects every planned tool is now specced, so for CS, arts, health, PE and library the "all planned" column is what
the catalog will reach unless modules are added. That is the main finding: **the non-core gaps below are not
going to close by building what is planned.** Each needs a new module (a new tool) or a code added to a module.

## Real gaps, with a suggested fix

Ordered by size and by how much a teacher would notice.

### 1. Arts: responding and connecting, theater and media arts (155 of 220 anchor cells empty)

- **By discipline (empty of 44):** media arts 37, theater 36, dance 32, music 25, visual art 25.
- **By process (empty):** performing 47 of 60, responding 45 of 60, connecting 32 of 40, creating 31 of 60.
- **Anchor 10, the personal and cultural connection anchor:** empty in every discipline and band. Every NCAS discipline has
  it ("synthesize and relate knowledge and personal experiences to make art").
- **Theater responding:** TH:Re7 and TH:Re9 are empty in every band.
- **Media arts K-5:** no tool at all (all 22 cells empty).
- **Suggested:**
  - Add anchor codes to the arts tools that already do the work: critique tools carry Re9, tools that tie art to a
    culture carry Cn11 and could carry Cn10.
  - Plan one later-wave module per empty discipline cluster: theater responding K-5 ("watch a scene, say what you
    noticed and why"), media arts K-2/3-5 (a simple stop-motion or sound-story maker), and a dance responding tool for
    K-8.
  - The specs named 24 finer performance standards (for example DA:Cr2.1.3a). modules.csv only carries anchors, so finer
    coverage can't be measured yet. The full list is in `data/standards/ncas-performance-standards.txt` (1,202 codes)
    if Cory wants to code at that level.

### 2. Computer science: computing and society, data (111 of 196 CSTA codes empty)

| Concept | K-2 | 3-5 | 6-8 | 9-12 |
|---|---|---|---|---|
| Algorithms (ALG) | 5/9 | 4/9 | 8/11 | 7/11 |
| Data (DAT) | 2/9 | 2/9 | 3/9 | 5/8 |
| Programming (PRO) | 6/12 | 9/15 | 3/9 | 4/9 |
| Computing and society (SOC) | 1/9 | 2/12 | 1/8 | **0/9** |
| Systems (SYS) | 6/9 | 6/12 | 4/8 | 7/9 |

- **The thinnest areas:** computing and society (history, ethics, culture, equity: 34 of 38 codes empty) and data
  (data collection, inference and models: 23 of 35 empty).
- **Why it matters:** several wave 1 CS specs teach computing and society ideas but carry only ALG, DAT or SYS codes:
  data-policy-council and ai-evaluator (9-12, privacy, fairness and law), internet-journey (3, where shared words end
  up) and secret-keeper (K, who sees what you share). biased-bot, algorithm-audit, design-for-a-friend and spot-the-ai
  already carry a SOC code.
- **Suggested, cheapest first:**
  - Add the matching SOC codes to those four modules, chosen by each code's wording. It is a data edit, and the specs
    already do the teaching.
  - Then plan 4 SOC tools in a later wave, one per band: computing history K-2/3-5, ethics 6-8, equity and law 9-12.
- **Note:** gaps.md G3 has the full code-by-code list (unchanged; wave 1 used only codes already on its modules).

### 3. ELA (286 of 455 grade-level standards; 64 of 167 anchor-band cells empty)

Measured at anchor x band (does any tool in the band teach RL.1, for example), the empty cells that matter most:
- **Evidence and theme in grades 6-12:** RL.1 and RL.2 (cite evidence, theme) and RI.1 (cite evidence, informational) in
  3-12. These are tested every year. Check first whether quote-evidence and the evidence tools carry a sibling code
  (W.9 or SL.1); if so, add RL.1/RI.1 to their modules.
- **Speaking and listening:** empty for grades 3-5 (SL.1 to SL.6 all empty).
- **Revising and editing:** W.5 is empty in every band.
- **Media and text features:** RL.7 is empty in K-8, and RI.7 in K-2 and 6-8.
- **Academic vocabulary:** L.6 is empty in 3-12.
- **Leave alone:** RL.10, RI.10 and W.10 (range of reading and writing) and W.6 (technology use) are poor fits for one
  tool. Leave them uncovered by design.

### 4. Social studies (167 of 283 C3 indicators empty)

- **D1 (asking compelling questions):** all 20 empty.
- **D3 (evaluating sources):** all 14 empty.
- **D4 (communicating and taking action):** 31 of 32 empty.
- **D2 economics:** 28 of the 30 empty economics indicators are in K-8.
- **D2 civics:** 24 empty.
- **D2 geography 9-12:** 9 empty.
- **D2 history** is the best covered.
- **Suggested:**
  - D1 and D3 are the inquiry arc. The library tools now teach it (research-quest, fake-or-fact-lab). Adding D1.x and
    D3.x codes to the history tools whose concept starts from a question or a primary source would close most of
    these cheaply.
  - Economics K-8 needs its own modules: the catalog has only piggy-bank-planner (2) and corner-store (2) in K-5.

### 5. Personal finance in grades 3-8 (NSPFE: 12 of 18 cells empty)

- **Where it stands:** only the 9-12 benchmark band is covered.
- **Already teaching it uncoded:** grocery-run (5, a budget) and lemonade-stand (6, price and sales). They teach
  Spending and Earning Income but carry only math codes.
- **Suggested:**
  - Add NSPFE.Spending to grocery-run's module and NSPFE.Earning Income to lemonade-stand's module.
  - Plan saving, credit, investing and risk tools for 3-8 in a later wave. The NSPFE grade 4 and 8 benchmarks are
    the guide.

### 6. SEL (CASEL: 12 of 20 cells empty)

- **Where it stands:** only 8 SEL modules exist, two per band, so each band covers 2 of the 5 competencies.
- **Health tools that teach SEL uncoded:** wave 1 health tools teach self-management and relationship skills
  (stress-toolkit, relationship-spectrum, pressure-point) but carry NHES codes only.
- **Suggested:**
  - Add the CASEL competency to those three modules.
  - Plan three more SEL modules per band in a later wave.

### 7. Health, PE and library (smaller)

- **NHES:** S2 (influences) in K-2 and 9-12, S3 (finding valid resources) in K-2, S4 (communication) in 3-5 and 9-12,
  S5 (decisions) in 9-12, S6 (goal-setting) in K-5, and S8 (advocacy) in 3-5 are empty.
  - health-claim-checker (9-12) is an S3 tool and could carry S2.
  - captain-s-choices (9-12 PE) is a decision tool and could carry NHES.S5.
- **SHAPE:** motor skills (S1) in 3-5 and 9-12, social skills (S3) in 6-8, personal skills (S4) in 3-5, and S2 to S4
  in K-2 are empty. K-2 covers only S1.
- **AASL:** Include (diverse perspectives) is empty in K-8, Collaborate in K-5 and 9-12, Explore in 3-12.
- **Health topics (CDC HECAT, `data/standards/hecat-topics.txt`), read by hand from the 16 health tools' concepts:**
  - K-2 covers personal health, food, feelings and safety.
  - 3-5 covers food, body and germs, and growing up.
  - 6-8 covers vaping and alcohol, stress, healthy relationships and screen time.
  - 9-12 covers nutrition, first aid, health claims and mental health.
  - No health tool in 9-12 covers alcohol, drugs or tobacco.
  - No health tool in K-5 covers violence prevention or bullying (the SEL tools touch it).
  - Safety is missing in 3-8 and mental health in 3-5.
  - Sexual health past puberty is absent, which may be deliberate for a free public site; Cory's call.
  - Suggested later-wave modules: a 9-12 substance-use decision tool, a 3-5 bullying upstander tool, a 3-5 or 6-8
    safety tool (online and home safety, medicine safety).
- **Finer levels:** the NHES 2024 indicators (172, `nhes-2024.txt`) and SHAPE 2024 indicators (210,
  `shape-pe-2024.txt`) are listed for a finer pass. Tools are not coded at that level yet.

### 8. Small, specific science and math holes

- **NGSS:** 12 PEs have no tool, the same as gaps.md G1 and G2 minus HS-LS2-5, which is now on energy-accountant's
  module:
  - K-2-ETS1 and 3-5-ETS1 (6): engineering design in K-5.
  - MS-PS2-4, MS-LS1-8, MS-LS4-5, HS-PS3-4, HS-LS2-3, HS-ESS2-7.
  - gaps.md G1 suggests adding K-2-ETS1 to shade-builder's module and 3-5-ETS1 to the Contraption Workshop module.
    Both are two-minute data edits and remain the best fix.
- **CCSS math:** 4 clusters have no tool: F-LE.B (interpret parameters in context), G-SRT.D (laws of sines and cosines,
  a (+) cluster), S-MD.A and S-MD.B (expected value, (+)). Only F-LE.B is a core cluster; it fits an existing
  exponential-growth tool.

## Data fixes found while matching codes

- **Math codes coded one level too deep (8):** A-REI.A.2, A-REI.B.4, A-REI.C.9, A-SSE.B.4, F-IF.A.3, F-LE.A.4,
  G-GPE.A.3, S-ID.A.4. coverage.py rolls them up to their cluster, so nothing is lost.
- **Math codes naming a whole domain with no cluster (5):** F-BF, F-IF, S-CP, S-ID, S-MD. Each needs its cluster
  chosen.
- **L.K.3 is not a real standard** (language standard 3 starts in grade 2). Its module needs a different code,
  probably L.K.1 or L.K.2.
- **Not measured:** AP units and APA psychology have no list here. ACTFL and World-Readiness, CTE, CASEL, AASL,
  WIDA and NSPFE have full official lists in `data/standards/` (sub-skills, competencies, outcomes), but modules.csv
  codes them at top level only, so the grids above are the finest measure today.

## Overlap check (wave 1 against the whole catalog)

The 75 were re-tagged from their specs (24 tags changed). The rule finds 93 pairs catalog-wide; 15 involve a wave 1
tool. None shares a skill; all 15 are action and setting matches only.

- **Real, worth a call:** misleading-charts (6-8 CS, specced) and fact-check-desk (ELA 8, planned) are both a
  newspaper fact-check desk where you investigate. The skills differ (deceptive charts and conflicting sources). The
  cheaper fix is to give fact-check-desk a different world when it is specced. It is still a one-line concept, and
  its title names the setting, so it would be renamed. fake-or-fact-lab's spec already designed the fact-check family
  engine that fact-check-desk will use, so the two should be specced together.
- **Weak, fine as is:**
  - career-cluster-explorer and cell-city (6-8 "town": a harvest festival and a cell drawn as a city).
  - secret-keeper and three-towns (K-2: a pretend online game park and city/suburb/country).
- **Broad settings that recur by nature, fine:**
  - world-music-map with three 6-8 history maps.
  - data-policy-council with three 9-12 debate rooms.
  - health-claim-checker with two 9-12 mysteries.
  - internet-journey with day-in-the-life.
  - flipbook-studio with vanishing-point-studio (both studios, different skills).
- **Same skill, same band:** snowy-mail-route and the live robot-dance (K-2, sequence and debug). Robot Dance
  programs moves; snowy-mail-route traces footprints back to the card that made them. Kept: the overlap review already
  reshaped this one.
- **Crowded settings to avoid in later waves:**
  - 9-12: lab 11, business and money 10, council and debate 8.
  - 6-8: travel map 10.
  - K-2: town 8, robot and machine 7.
  - 3-5: nature 7.

## What looks fine

- Every wave 1 spec claims exactly its module's standards now. 13 named a secondary code; those were added to
  modules.csv.
- No spec dropped a module code.
- NGSS and CCSS math are near complete once planned tools are built. Their remaining holes are small and listed above.
- WIDA's five standards are covered in every band by planned ELD tools.

## Suggested next step for Cory

One decision: approve a single data-only pass that adds the codes named above to existing modules, with no new tools:
- SOC codes on four CS modules.
- NSPFE on two math modules.
- CASEL on three health modules.
- NHES and arts anchors where tools already do the work.
- ETS1 on shade-builder and Contraption Workshop.
- RL.1 and RI.1 where the evidence tools teach them.
- The 13 malformed or invalid math and ELA codes.

That alone should lift arts, CSTA, CASEL and NSPFE noticeably. The new modules (theater and media arts responding, SOC
per band, economics and finance K-8, SEL, ELA speaking and listening) can then be planned as one later wave.
