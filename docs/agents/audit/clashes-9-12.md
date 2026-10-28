# Curio Class overlap and gap audit: clashes, grades 9-12

Judge for band 9-12, Phase 2 of docs/agents/AUDIT.md. Input: the 64 band 9-12 rows of docs/agents/overlap/pairs.csv
(from the re-tagged tags.csv) and the 9-12 overlap risks named in docs/agents/IDEA-PASS-LOG.md. Every tool was judged
from its spec.md (or idea.md where no spec exists; tool.json and spec.md for live tools). Method and kept-hit reasons
follow docs/agents/overlap/method.md and clusters.md (C57); decisions follow docs/agents/decisions/BASELINE.md.

## Decision table

One row per tool that changes or carries a note. Live tools never move. No merges (rule 1).

| tool_id | cluster | fix | new concept line (data/concepts style) or note |
|---|---|---|---|
| build-a-government | K06 | reshape | `social-studies-12-foundations-of-government\|Build a Government\|builder\|\|Write the constitution for a newly independent country with three regions, two languages and a river shared with a neighbor; test it against crises from a contested election to a water treaty, and see which real nation's results yours resembles.` (40 words) |
| lake-commons | K06 | reshape (catalog line synced to the spec) | `science-9-resources-and-sustainability\|Lake Commons\|tycoon\|\|Run a lake town for 100 years in five-year turns: set the fishing boats, forest cuts, new homes and energy, then live through floods and droughts; take about what grows back or watch the lake empty.` (36 words) |
| startup-booth | K09 | reshape (catalog line synced to the spec) | `cte-9-12-entrepreneurship\|Startup Booth\|tycoon\|\|Run a Saturday market booth for 12 weeks; every price you test drops a dot on a demand chart, the break-even line shows which prices keep the business alive, and you pitch an investor with numbers you earned.` (38 words) |
| compound-interest-head-start | K02 | keep, note | Kept beside the live savings-plan: there the student designs deposit rules and sums a series with no interest; here the deposit is fixed and the only levers are start age and rate, read as deposits, interest and interest on interest. Cory has already ruled on this spec (w2-07). Spec check: no deposit-sequence design, no series formulas. |
| design-the-study | K03 | keep, note | Kept beside the live poll-workshop: experiments (assignment, control, placebo, blinding), never surveys or sampling; the hand-off at S-IC.B.3 written in the spec stays. Skill key is experiment-design, as the first pass set it. |
| grid-operator | K06 | keep, note | Ridgeport is an island city because an isolated grid is the physics; keep the island as a backdrop only (no island map as the hero picture), since 9-12 already has trade-island and the live imaginary-island. |
| inflation-wallet | K11 | keep, spec note | Bread through the 1923 hyperinflation is the historical fact and stays. Spec check: show it from the family's kitchen and wallet, not a bakery shop scene; mole-bakery owns the bakery picture in 9-12. |

**Tag corrections for tags.csv** (the orchestrator applies; I edited nothing). Eleven specced tools still carry their
pre-fix tags from the first pass, so twelve of the 64 hits are stale-tag artifacts; the specs already made the first
pass's fixes. The corrected tags below are re-checked with the rule (see "Re-check").

| tool_id | was (skill, action, setting group) | should be | why (from the spec) |
|---|---|---|---|
| who-decides | community-project, trace, town | civic-action, trace, town | Civics only: offices, public comment, testimony (C05). The live tool is CASEL leadership. |
| grid-operator | energy-sources, manage, town | energy-sources, manage, control-room | Spec: "no city management at all, only the grid control room" (C06). |
| compound-interest-head-start | savings-growth, simulate-tune, garden-farm | savings-growth, simulate-tune, generic | The garden is gone; two savers' plain account balances. Skill key left coarse on purpose (method.md). |
| design-the-study | study-design, plan, newsroom | experiment-design, plan, newsroom | First pass after-tag; the spec is experiments only. |
| zipline-energy | energy-conservation, build, amusement-park | energy-conservation, build, zipline | Cliff-to-tree zipline, no coaster (C09). |
| curling-stones | newtons-laws, simulate-tune, space | newtons-laws, simulate-tune, sports | Curling ice, no zero-g cargo (C39). |
| lake-commons | sustainability, manage, island | sustainability, manage, water | One town on one lake, "no island" (C41). |
| rigid-motion-twins | rigid-motions, solve, sports | rigid-motions, solve, nature | Fossil trackway casts, no golf (C38). |
| polynomials-as-numbers | polynomial-area-model, build, garden-farm | polynomial-arithmetic, explore, generic | Place-value columns, no rectangle, no garden (C29). |
| question-sharpener | research-project, manage, business-money | research-questions, fix, generic | The question is the product; "the currency is time, not money" (C40). |
| covered-insurance-claims | scams-insurance, solve, cyber | insurance, compare, generic | Quotes, deductibles and your own policy page; no escape board, no systems (C43). |
| build-a-government | government-foundations, build, island | government-foundations, build, generic | After the reshape above. |

## Summary

- **64 rule hits** in 9-12 grouped into **18 clusters** (K01 to K18), plus the idea-pass risks (K19).
- **14 hits are new** since the first pass; **50 are carried over** from C57 and re-confirmed against the current
  specs and idea cards.
- Of the 14 new hits, **12 are stale tags** on specced tools whose specs already made the first pass's fixes (K01, K04,
  K05, K06, K07, K08, K09, K10); 2 are real and kept with a note (K02 with the live savings-plan, K11).
- **Changed tools: 3 reshapes** (build-a-government; lake-commons and startup-booth as catalog lines synced to their
  specs) and **4 keep-with-note** (compound-interest-head-start, design-the-study, grid-operator, inflation-wallet).
  No live tool changes. No merge, no move-to-gap.
- **Clashes with live tools:** five rule hits name a live tool. Three are stale tags (community-project-planner twice,
  rollercoaster-polynomials); poll-workshop is kept with the existing hand-off; savings-plan against
  compound-interest-head-start still meets the rule on skill and action and is kept with a note (K02).
- **Re-check:** with the tag corrections and the build-a-government reshape applied, the rule finds 52 hits in 9-12
  (the 50 carried-over pairs plus K02 and K11), each with a reason below. No reshape or correction creates a new hit in
  any band.

## Clusters

Tool notation: id (subject, grade, live / spec / idea). Tags: skill_key, action, setting group.

### A. Rule hits that name a live tool

### K01. Community projects and the grid beside community-project-planner

- **Tools:** community-project-planner (SEL, 9-12, live); who-decides (social studies, g12, idea); grid-operator
  (science, g12, spec)
- **Hits:** community-project-planner and who-decides (skill+setting); community-project-planner and grid-operator
  (action+setting).
- **Judgment:** both are stale tags of the first pass's fixes (C05, C06). The live tool leads a volunteer team through a
  six-week project (CASEL Relationship Skills). who-decides traces which office decides a local problem and drafts
  testimony, a petition and a letter (D2.Civ.13, D2.Civ.14, D4.3, D4.7, D4.8); there is no team to run. grid-operator
  works only in a grid control room ("no city management at all"). The tag agent keyed who-decides as community-project
  because both start from a local problem; a teacher would call one leadership and the other civic action.
- **Fix:** keep both; tag corrections above. grid-operator also carries the island note (K06).

### K02. Savings that grow: a new spec beside savings-plan

- **Tools:** compound-interest-head-start (CTE, 9-12, spec); savings-plan (math, g11, live); market-time-machine (CTE,
  9-12, live)
- **Hit:** compound-interest-head-start and savings-plan (skill+action: savings-growth, simulate-tune). With the stale
  garden setting it was skill+action only too.
- **Background:** C08 reshaped compound-interest-garden to Rainy Day Fund; the wave 2 spec brought compound interest
  back as the core (BATCH-W2.md: "the pass had moved it to emergency funds"), with an emergency-fund card, and Cory
  answered w2-07 on this spec. C56 fenced "no more 9-12 savings-growth simulators".
- **Judgment:** the student really does something different. savings-plan: build deposit plans as sequences, read the
  balance as a partial sum, derive the series formulas; no interest at all (its spec says so). Head Start: one fixed
  $50 deposit, two start ages, and a stacked bar that splits deposits, interest and interest on interest; no sequence
  design, no formulas. market-time-machine is real market returns and risk; Head Start is one fixed rate, no risk. The
  coarse key savings-growth is left as is (method.md merged it on purpose), so the pair stays on the record.
- **Fix:** keep, with the spec check in the decision table. Not sent to Cory: the spec is written and they have already
  ruled on it.

### K03. Study design beside poll-workshop

- **Tools:** design-the-study (math, g12, spec); poll-workshop (math, g11, live)
- **Hit:** skill+setting (study-design, newsroom). Both modules carry S-IC.B.
- **Judgment:** the spec made the C04 fix: experiments only (random assignment, control, placebo, blinding, a biased
  timer), "no survey and no sampling frame", with the hand-off to poll-workshop at S-IC.B.3. The tag agent's
  study-design key undoes the first pass's after-tag (experiment-design).
- **Fix:** keep, note and tag correction above.

### K04. Zipline beside the coaster

- **Tools:** zipline-energy (science, g11, spec); rollercoaster-polynomials (math, g11, live)
- **Hit:** action+setting (build, amusement-park).
- **Judgment:** stale tag. The C09 fix holds in the spec: a 300 m zipline from a cliff to a tree, an energy ledger
  with friction, drag and a brake; no track, no polynomial.
- **Fix:** keep; tag correction (setting zipline).

### B. Stale tags between planned tools

### K05. Space simulators

- **Tools:** curling-stones (science, g11, spec); launch-pad (math, g9, spec); orbit-lab (science, g9, spec)
- **Hits:** curling-stones with launch-pad and with orbit-lab (action+setting, space); launch-pad and orbit-lab
  (carried over, C57: quadratic projectiles and Kepler's laws).
- **Judgment:** curling-stones still carries space-cargo's "zero-g cargo" tag; the spec is a stone on ice with F = ma
  and friction (C39). With the corrected sports setting it has no hit. 9-12 sports settings stay at five (curling
  replaced golf in rigid-motion-twins, K07).
- **Fix:** keep all three; tag correction.

### K06. Islands in 9-12

- **Tools:** lake-commons (science, g9, spec); trade-island (social studies, g12, idea); build-a-government (social
  studies, g12, idea); grid-operator (science, g12, spec); imaginary-island (math, g11, live)
- **Hit:** lake-commons and trade-island (action+setting, island).
- **Judgment:** the spec made the C41 fix (one town on one lake, "no island"), but two things undo it on paper. The
  catalog line in data/concepts/science.txt still reads "Manage an island's fish, forests and water", and the tag says
  island. Separately, the idea pass put build-a-government back on "a new island nation" with "a neighbor across the
  strait", reversing C41's Write the Charter reshape (below the bar, but it is the same picture). grid-operator's
  Ridgeport is an island city because an isolated grid is the physics; it is fine as a backdrop.
- **Fix:** trade-island keeps the islands (the two-island model is how comparative advantage is taught). Reshape
  build-a-government off the island: a newly independent country with three regions, two languages and a river shared
  with a neighbor, so the treaty crisis stays (D2.Civ.3) and the real-country comparison stays (D2.Civ.8). The title
  stays, since the idea card kept it. Sync lake-commons's catalog line to its spec. grid-operator keeps the island as a
  backdrop only. After these changes, 9-12 islands are trade-island, imaginary-island (live, a metaphor for the complex
  plane), grid-operator's backdrop, and carrying-capacity's real St. Matthew Island case study.
- **Re-check:** build-a-government (government-foundations, build, generic) has no hit in 9-12; no other tool carries
  its skill key.

### K07. Two golf courses

- **Tools:** equation-golf (math, g9, spec); rigid-motion-twins (math, g10, spec)
- **Hit:** action+setting (solve, sports).
- **Judgment:** stale tag. rigid-motion-twins (C38) is now a fossil trackway where a plaster cast is moved onto its
  print; equation-golf is the only golf course.
- **Fix:** keep; tag correction (setting nature). No hit with the 9-12 nature tools (fallacy-field-guide,
  carrying-capacity, reserve-designer, water-shapes-earth, fire-lookout-triangles), whose actions differ.

### K08. Gardens in 9-12 math

- **Tools:** polynomials-as-numbers (math, g9, spec); optimization-workshop (math, g12, spec)
- **Hit:** action+setting (build, garden-farm).
- **Judgment:** stale tag. polynomials-as-numbers (C29) has "no rectangle at all, only place-value columns", and no
  garden. optimization-workshop's barn fence is one of several workbenches.
- **Fix:** keep; tag correction.

### K09. Business tycoons and the research season

- **Tools:** question-sharpener (ELA, g12, spec); ad-agency (ELA, g12, spec); startup-booth (CTE, 9-12, spec)
- **Hits:** question-sharpener with ad-agency and with startup-booth (action+setting, manage, business-money);
  ad-agency and startup-booth (carried over, C57).
- **Judgment:** the C40 fix holds in the spec: question-sharpener prices a research question in hours against a
  27-hour season; "the currency is time, not money, and nothing is bought or sold". The student mostly redrafts the
  question (fix). ad-agency profits from ad tricks, then audits them as a watchdog; startup-booth finds a demand curve
  by testing prices at a market booth. Three different jobs. startup-booth's catalog line still reads "plan, budget,
  market and pitch to investors", which no longer describes the spec.
- **Fix:** keep all three; tag correction for question-sharpener; sync startup-booth's catalog line to its spec.

### K10. Scams in a cyber setting

- **Tools:** covered-insurance-claims (CTE, 9-12, spec); capture-the-flag (CS, 9-12, spec)
- **Hit:** action+setting (solve, cyber).
- **Judgment:** stale tag from Scam Shield. The C43 fix holds: three renters quotes, a deductible slider, a year chart,
  then fake "claim refund" texts checked against your own policy page. capture-the-flag finds and patches holes in a
  made-up company's systems. Each spec's "Not like" names the other.
- **Fix:** keep; tag correction (insurance, compare, generic). With a business-money setting it would hit the-buyout
  on paper, so generic is the honest group: real insurance documents, no metaphor.

### C. A new pair between planned tools

### K11. Bread in grade 10

- **Tools:** mole-bakery (science, g10, spec); inflation-wallet (social studies, g10, idea)
- **Hit:** action+setting (manage, shop-food).
- **Judgment:** the student does different things. mole-bakery: grams to moles through a balanced equation, the
  limiting ingredient, percent yield (HS-PS1-7). inflation-wallet: a Berlin family's wallet and ballot from 1919 to
  1933, then a cause board for the fall of Weimar (D2.His.14, D2.Civ.8). Bread at hyperinflation prices is the
  historical fact (rule 5), and leavening is the standard stoichiometry hook. The only risk is the same bakery picture
  twice in one grade.
- **Fix:** keep, with the inflation-wallet spec note in the decision table.

### D. Carried-over hits, re-confirmed

Each pair below was kept in C57; the current spec or idea card was re-read and the reason still holds.

### K12. Lab benches (16 pairs)

- **Pairs (action+setting, experiment, lab unless noted):** collision-lab (live) with illusion-lab, gas-law-lab,
  hand-warmer-lab, prototype-lab, sign-parameters-lab; gas-law-lab with illusion-lab, hand-warmer-lab, prototype-lab,
  sign-parameters-lab; hand-warmer-lab with illusion-lab, prototype-lab, sign-parameters-lab; illusion-lab with
  prototype-lab, sign-parameters-lab; prototype-lab with sign-parameters-lab; prototype-lab and
  design-challenge-studio (skill+setting).
- **Reason:** a lab bench is the default setting for science, and each runs a different experiment: momentum (live),
  absolute zero from gas lines, bond energy in a hand warmer, perception and memory on yourself, a phone stand printed
  and tested. sign-parameters-lab is the K-12 ASL tool whose format is lab, not a bench. prototype-lab and
  design-challenge-studio keep the C53 spec note (iterate one product; breaking down a global problem belongs to the
  studio).

### K13. Debates (10 pairs)

- **Pairs (action+setting, debate, council-debate):** among usage-panel, counterpoint-frames, data-policy-council,
  debate-en-español and empire-debate.
- **Reason (C42):** debate is the target skill in each, on different content: a dictionary usage ruling, ELD counter
  moves, a district data policy clause by clause, a Bogotá Ciclovía question in Spanish, the 1899 Philippines
  annexation with the Filipino voices left out.

### K14. Mysteries (6 pairs)

- **Pairs (action+setting, investigate, detective):** among satire-decoder, health-claim-checker,
  detective-del-pasado and ph-mystery-liquids.
- **Reason (C31, C32):** every mystery-format tool is tagged detective; the cases differ: a satire's real argument, a
  health claim's retelling chain, Spanish past tenses as clues, unlabeled bottles in a flooded prep room.

### K15. Money simulators (3 pairs)

- **Pairs (action+setting, simulate-tune, business-money):** savings-plan (live) with fed-chair and
  stock-market-1929; stock-market-1929 and fed-chair.
- **Reason (C57):** different skills and eras: sequences and series, setting rates in four real moments, a margin
  account through the real 1929 closes.

### K16. Body and medicine (3 pairs)

- **Pairs (action+setting, simulate-tune, body-medical):** medical-test-paradox with body-thermostat and outbreak-model
  (live); outbreak-model and body-thermostat.
- **Reason (C57):** a disease test is the standard example for conditional probability; homeostasis and exponential
  growth are other skills.

### K17. Family trees (3 pairs)

- **Pairs (action+setting, explore, family-tree):** word-family-tree, function-family-reunion, tree-of-life.
- **Reason (C57):** the family-tree metaphor is native to each subject: word roots, parent functions, common ancestry.

### K18. Maps and the other single pairs (8 pairs)

- **Maps (travel-map):** ideas-that-spread and where-s-my-phone-from (trace); mundo-hispano and scramble-for-africa
  (explore). Maps are native to history and world languages; each covers a different place and era.
- **ad-agency and startup-booth** (manage, business-money): persuasion and launching a business (C40, K09).
- **beat-lab (live) and sound-studio** (compose, music): music production and wave physics.
- **courtroom-statistics and supreme-court-simulator** (debate, courtroom): the courtroom is the teaching frame in one
  and the subject in the other (C30).
- **factory-floor and home-front-mobilizer** (manage, factory): a Lancashire mill from 1760 and West Coast war plants
  from 1942; the factories are the history in both.
- **flight-planner and speedometer** (simulate-tune, vehicle): vectors and derivatives; speedometer keeps its C53 note.
- **inbox-simulator and interview-simulator** (converse, business-money): register in email and answers in an
  interview (C53).
- (launch-pad and orbit-lab is in K05.)

### E. Idea-pass overlap risks

### K19. Risks the idea pass named that touch 9-12

All are cross-band (6-8 against 9-12, or 3-5 and 6-8 against 9-12), so the same skill one band apart is a spiral. None
matches on all three tags. Each idea card already states the line that keeps them apart; the spec writer keeps it.

| 9-12 tool | other tool (band) | kept apart by |
|---|---|---|
| collision-lab (live) | crash-test-lab (6-8) | crash-test-lab stays on force pairs and fair tests, no momentum math. |
| hand-warmer-lab | reaction-kitchen (6-8) | kitchen materials and conservation of mass, no bond energies. |
| zipline-energy | half-pipe-energy (6-8) | frictionless bars and proportional graphs; friction and brakes stay in grade 11. |
| orbit-lab | planet-builder (6-8) | qualitative gravity and scale; Kepler's laws with numbers stay in grade 9. |
| energy-accountant | leaf-factory (6-8) | one leaf's choices; the carbon ledger stays in grade 9. |
| economy-dashboard | economy-checkup (6-8) | four neighbors and how indicators touch them; the full dashboard and forecasting stay in grade 12. |
| catalog-column-rules | lunch-survey-cleanup (6-8), fair-survey-kit (3-5) | drop, reformat or keep per answer; rules you write and three checking methods stay in 9-12. |
| director-s-chair | scene-staging-comparison (6-8) | responding to two productions of a different play; directing Antigone in five theaters stays in 9-12. |
| fair-use-review | viral-video-breakdown (6-8) | fair use only as the reposting question, with a link out. |
| choreography-for-a-cause | choreography-board (6-8) | revising one phrase with devices; choreographing from research stays in 9-12. |
| mini-documentary-crew | morning-show-crew (6-8) | one story across formats in a week; one long film with a full crew stays in 9-12. |
| museum-courtyard-performance | dancers-on-tour (6-8) | the performer adapting across venues; producing one site-specific concert stays in 9-12. |

## Re-check

Run with the tag corrections and the build-a-government reshape applied to the rule in scripts/overlap/common.py
(scratch script, nothing in the repo changed): 52 hits in 9-12, the 50 carried-over pairs plus K02 and K11. The
corrected and reshaped rows (who-decides, grid-operator, compound-interest-head-start, design-the-study,
zipline-energy, curling-stones, lake-commons, rigid-motion-twins, polynomials-as-numbers, question-sharpener,
covered-insurance-claims, build-a-government) make no new hit in any band, and none crosses a band on all three tags.
Module codes were checked for each change: build-a-government keeps D2.Civ.3 (the water treaty and the crises) and
D2.Civ.8 (the real-country comparison); the two synced lines describe what their specs already teach.

## Note for the orchestrator

Eleven specced tools still had pre-fix tags in the merged tags.csv. The first pass's `--after` logic skips a decision
when a spec exists ("tags.csv already carries its tags"), but these rows were never updated. The same may be true in
other bands for any specced tool that a first-pass decision changed.
