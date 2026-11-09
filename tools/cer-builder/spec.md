# CER Builder

## One idea
The student runs a quick virtual experiment on a lab bench (which paper towel soaks up the most water, which color of cup heats fastest in the sun, which block melts ice faster, how much salt floats an egg), gets a table of three trials, and writes the lab report's conclusion as claim, evidence and reasoning with language frames, while the tool flags a claim the data do not support, evidence with no numbers, and reasoning that only repeats the evidence ("That says what happened. Why did it happen?"), so they learn that evidence is the numbers and reasoning is the science idea that connects them to the claim.

## Not like
- claim-quote-comment (ELA, spec): claims about an article. Here claims from your own data.
- cause-and-effect-rewind (3-5, spec): cause chains with because and so. Here a three-part lab conclusion for grades 6 to 8.
- argument-builder-pro (9, spec): a full argument with counterclaims. Here one science conclusion.
- summary-scaffold (6-8, spec, this batch): restating an author's ideas. Here stating your own finding.
- verb-conjugation-race (6-12, spec, this batch): speed and accuracy. Here a slow bench and a careful paragraph.

## Who and how
- Grades 6 to 8, English Language Development, module "Lab Reports and Claims". Standards: WIDA ELD-SC (Standard 4, the language of science), Argue key language use (WIDA 2020).
- Driver: one student; class mode is "Strong or weak?", where the projector shows two conclusions for the same data and the class says which part is missing (tool.json `driver: "student"`). Every label, row and sentence is read on tap.
- Four experiments. Help setting: Lots (full frames and a science-idea card), Some (frames with blanks), Little (part names only, then typing). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Lab", "Strong or weak?"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the data table and the conclusion.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA ELD-SC (investigation and measurement words) | Run trials and read the table with units (mL, °C, minutes) | the data table | 2 |
| WIDA Argue (claim supported by data) | Write a claim the data support | the claim checked against the table | 3 |
| WIDA Argue (evidence with numbers) | Cite averages or ranges with units | the evidence sentence with numbers lit | 3 |
| WIDA Argue (reasoning with a science idea) | Connect the evidence to the claim with the science idea | the reasoning sentence; the "why" card | 4 |
| WIDA ELD-SC (explanation words) | Use because, which means, this shows | the strong and weak paragraphs side by side | 5 |

## Screens and modes
Header (kit): title "CER Builder"; `Bench`, `Data`, `Conclusion`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A lab bench under bright windows with four experiment trays, safety goggles on a hook, and a question card on the first tray: "Which paper towel soaks up the most water?" The science teacher, Mr. Daniel Cho, leans on the bench: "Run it. Then tell me what you found and why." First hint: "Tap the question card to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**The experiments.**
1. Paper towels: one sheet each of brand A (thin, one layer), brand B (two layers, quilted) and brand C (recycled), dipped and wrung into a measuring cup. Typical averages: A about 19 mL, B about 40 mL, C about 26 mL. Science idea: water is pulled into the tiny spaces between fibers (capillary action); more layers and more space between fibers hold more water.
2. Cups in the sun: black, white and clear cups with 200 mL of water, 30 minutes in sunlight, starting at 20 °C. Typical rises: black about 11 °C, clear about 7 °C, white about 5 °C. Science idea: dark surfaces absorb more of the light that hits them and turn it into thermal energy; white surfaces reflect most of it.
3. Ice on blocks: two blocks at room temperature, one aluminum and one plastic; an ice cube on each. Typical melt times: aluminum about 6 minutes, plastic about 20 minutes. Science idea: metals conduct thermal energy quickly, so the room's energy flows into the ice faster.
4. Floating an egg: 500 mL of tap water; add salt one tablespoon at a time. Typical: the egg floats after about 4 to 7 tablespoons, depending on the egg. Science idea: dissolving salt makes the water denser; an object floats when the liquid is denser than it.

**Bench.** The student sets up and runs three trials; each trial's result varies a little (within a keyed range) so the averages are the student's own.

**Conclusion.** Three color-coded slots with frames: Claim ("The ___ absorbed the most water."), Evidence ("In three trials, it held an average of ___ mL, compared to ___ mL and ___ mL."), Reasoning ("This is because ___, which means ___."). Checks: a claim the data do not support ("Brand C absorbed the most.") gets "Look at your averages again."; evidence with no numbers gets "How much? Use your numbers."; reasoning that only repeats the evidence gets "That says what happened. Why did it happen?" and the science-idea card opens.

**Strong and weak.** The finished paragraph sits beside a weaker version that has no reasoning, with the three parts colored and labeled, so the student sees what reasoning adds.

**Strong or weak?** On the projector, two conclusions for the class to judge.

At 1366x768 bench and slots fit; at 680x425 the data table is a tab.

## Content
- Four experiments with keyed result ranges, frames, word banks, science-idea cards and weak sample paragraphs written for Curio Class. Ranges are typical classroom values, not lab standards, and the screen says "Real results vary."
- All four experiments use room-temperature water, ice or sunlight; there is no heating and no flame.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Trials can be rerun; slots can be rebuilt any time and checks update at once.
- With Motion off liquids and thermometers jump to their values and the egg appears floating without rising.

## Look
- Accent `--brand` #1d4f91 lab blue (header, bench edge, the claim slot); gold #f4c542 (numbers in the evidence slot, the reasoning slot border); paper #eff4fb; ink #0b1a30; muted #4b5a6e. Scene: a bright middle school science lab.
- Contrast (WCAG 2.1, computed): white on brand 8.14:1; brand on paper 7.37:1; ink on paper 15.77:1; muted on paper 6.36:1; ink on gold 10.72:1.
- Never color alone: claim, evidence and reasoning carry labels as well as colors; flags show a symbol and words.
- Different from this batch (plaza green, rally red, plum, playroom orange).

## Art
- People art goes to Gemini: Mr. Daniel Cho (a Korean American man in his thirties in a lab coat and goggles), 4 poses; "illustrated middle school science teacher <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the lab bench (1); each experiment setup, no faces (4).
About 9 images. Drawn in code: measuring cups, thermometers, timers, the egg and data tables.

## Voice
Bank voice `science-narrator` as Mr. Cho and the hint voice (unique in this batch); the student's conclusion and the weak sample are read by `calm-professor` (unique in this batch). `Curio.voice` with `scope: () => state.exp + ':' + state.slot`, `welcomeAfter: true`.
- how `welcome`: "Run three trials. Then write what you found, the numbers that show it, and the science that explains it."
- event `question`: the experiment question.
- event `trial`: the trial result with units.
- event `support`: "Look at your averages again."
- event `numbers`: "How much? Use your numbers."
- event `why`: "That says what happened. Why did it happen?"
- event, whole, `conclusion`: the conclusion read back.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`kit/evidence.js`, `__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Claims with `ev.claimCheck`, Evidence links with `ev.checks` (the `repeats` flag drives "That says what happened", `unexplained` the short-reasoning nudge), and the Board view as the three colored slots. Not Source pack spans, Series, Sides, Ledger or Draft. The bench, trials, data-table support check and science-idea cards are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Claim | Pick any option | The claim is checked against the student's own averages. |
| Evidence | Write "It held the most." | Evidence needs at least two numbers with units from the table. |
| Reasoning | Restate the evidence | Reasoning must use a keyed science-idea word (fibers, absorb, conduct, denser) and a connector. |
| Reasoning | Paste the science-idea card | Reasoning must also name the student's own claim item (brand B, the black cup). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the question: `question`, `welcome` (queued, first time).
2. Bench: `trial` per trial.
3. Conclusion: `support`, `numbers` or `why` as they fire; `conclusion` (whole) when all three parts pass.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 4 is the language of science; Argue covers claims, evidence and reasoning | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Claim, evidence and reasoning as a framework for middle school science explanations | McNeill and Krajcik, Supporting Grade 5-8 Students in Constructing Explanations in Science (Pearson, 2012) | NGSS Science and Engineering Practice 7, engaging in argument from evidence | yes |
| Capillary action pulls water into small spaces such as paper fibers | USGS Water Science School, capillary action | Britannica, capillarity | yes |
| Dark surfaces absorb more sunlight and warm more; white surfaces reflect more | NOAA SciJinks or NASA Earth Observatory, albedo | Britannica, albedo | yes |
| Metals conduct thermal energy much faster than plastics | Britannica, thermal conduction | NGSS MS-PS3-3 clarification and evidence statements | yes |
| Dissolving salt raises water's density; an egg floats when the water is denser than the egg | NOAA Ocean Service, ocean density | Britannica, density and buoyancy | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad b28, 2026-11-09): across 1,000 simulated runs of three trials within each keyed range, the same item wins every time (brand B, the black cup, aluminum), so the supported claim never flips; the egg's float point stays inside the keyed 4 to 7 tablespoon range in every run; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and slots fit; at 680x425 the data table is a tab.
2. Three trials per experiment fill the table with units. (WIDA ELD-SC)
3. Claims are checked against the data, and evidence needs numbers. (WIDA Argue)
4. Reasoning that repeats evidence opens the science-idea card. (WIDA Argue)
5. Strong and weak paragraphs show side by side with labeled parts. (WIDA ELD-SC)
6. Help levels behave as in Who and how.
7. Strong or weak? and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: values jump into place; no network requests.

## Open questions
- Home-language support: home-language glossaries for ELD frames (Cory's open question in RUNBOOK.md)? (default used: English only, with pictures and read-aloud)
