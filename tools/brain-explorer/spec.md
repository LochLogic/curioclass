# Brain Explorer

## One idea
An illustrated brain turns and slices on screen, and each region opens through a real case: in 1848 an iron rod passed through railroad foreman Phineas Gage's left frontal lobe and he lived, but friends said he was "no longer Gage"; in 1861 Paul Broca's patient could say only one syllable and the damage sat in the left frontal lobe; split-brain patients in the 1960s could name an object seen by one half of the brain but not the other; for each case the student predicts what the damage will change before reading what happened and how we know (injury cases, brain imaging, electrical recording, stimulation); then the student zooms from a region to one neuron, fires an action potential, watches it travel and release neurotransmitter at the synapse, and adds caffeine, an SSRI or curare to see what each changes; a body map traces a near miss on a bicycle through the nervous system's branches and the endocrine system's stress hormones; at the end the student names the region and system behind new everyday moments, so a twelfth grader learns brain structures and functions, how neurons communicate, the nervous and endocrine systems, and the methods used to study them.

## Not like
- illusion-lab (12, spec): perception and memory tasks. Here the brain's parts and wiring.
- train-your-dog (12, concept): learning by conditioning. Here the biology under behavior.
- trait-lab (12, concept): personality traits. Here brain regions and cells.
- case-conference (12, concept): disorders and treatment. Here how the healthy brain works.

## Who and how
- Grade 12, Psychology, module "Brain and Behavior". Standards: APA.Biological (APA National Standards for High School Psychology Curricula, Biological Bases of Behavior: structure and function of the nervous system, neural transmission, the endocrine system, and the methods used to study the brain).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Six region cases, the neuron zoom with three substances, the body map stress scene, the case quiz. Extra: Case relay (teams race to match new cases to regions and systems). tool.json `modes: ["Explore", "Case relay"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| APA.Biological (structure and function) | Open each case, predict the change, read the outcome | the lit region; the prediction card; the outcome and region card | 2 |
| APA.Biological (methods) | Mark how we know each region's job (injury, imaging, recording, stimulation) | the "how we know" tag on each region card | 2 |
| APA.Biological (neural transmission) | Fire a neuron, then add a substance and predict its effect at the synapse | the membrane voltage trace; the synapse with transmitter and receptors | 3 |
| APA.Biological (nervous and endocrine systems) | Trace the bike near miss through the body map | sympathetic branch, adrenal glands, adrenaline and cortisol over time | 4 |

## Screens and modes
Header (kit): title "Brain Explorer"; `Explore`, `Case relay`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A brain, side view, with four lobes labeled. A case shelf: the first card reads "In 1848 an iron rod passed through this man's head. He lived. What changed?" The welcome is queued (`welcomeAfter: true`): "Every part of this brain has a job. We learned most of them from people whose brains were hurt. Tap the first case." First hint: "Tap the first case card."

**Cases (focus: the region).** At 1366x768 the brain fills the left with the case card right; at 680x425 the card is a sheet. The brain turns (side, top, midline slice) with drag or arrow buttons. Six cases:
1. Phineas Gage (September 13, 1848): a 3-foot-7-inch tamping iron through the left frontal lobe; he lived until 1860; his doctor, John Harlow, reported changes in judgment and manner. Region: prefrontal cortex. How we know: injury case.
2. Broca's patient Leborgne (1861): could say only "tan". Region: left frontal speech area. How we know: injury case and autopsy.
3. Wernicke's patients (1874): fluent speech with little meaning. Region: left temporal language area.
4. Henry Molaison, known as H.M. (surgery 1953): could not form new lasting memories. Region: hippocampus. How we know: surgery and decades of testing.
5. Split-brain patients (Sperry and Gazzaniga, 1960s): after surgery cutting the corpus callosum, an object shown to the left visual field couldn't be named. Region: corpus callosum and the two hemispheres. Sperry's Nobel Prize, 1981.
6. A brain scan case (labeled "a composite built from published studies"): the motor cortex lights in an fMRI scan when a hand moves. How we know: imaging.
- Before each outcome the student picks a prediction from three; the outcome card then explains.

**Neuron zoom (neural transmission).** From a region the student zooms to one neuron. A voltage trace shows rest near -70 millivolts; a tap adds input; past threshold near -55 millivolts the neuron fires to about +40 millivolts and resets. The signal runs down the axon (faster with myelin) and releases transmitter at the synapse. Substances: caffeine blocks adenosine receptors, so the "slow down" signal is muffled; an SSRI blocks serotonin's reuptake, so it stays longer in the gap; curare blocks acetylcholine receptors at the muscle, so the signal can't make the muscle move. The student predicts each before it plays.

**Body map (nervous and endocrine systems).** A near miss on a bicycle: the eyes see the car, the amygdala signals alarm, the sympathetic nervous system speeds the heart in under a second, the adrenal glands release adrenaline, and cortisol rises over minutes; then the parasympathetic system calms things down. The student traces each step and marks fast (nerves) or slower (hormones).

**The case quiz (the aha).** Six new everyday moments (forgetting a name you just heard, a jump at a loud noise, catching a ball, finding the word on the tip of your tongue, a coffee in the morning, a racing heart before a test): the student names the region or synapse and the system. Narrator: "Behavior is biology you can see from the outside."

**The end.** The cases, the zoom, the body map trace and the quiz. `Print` prints them.

**Case relay (extra).** Teams take turns matching new cases to regions and systems.

## Content
- Six cases with real dates and published sources, region cards with "how we know" tags, the neuron model with stated voltages, three substances, the stress scene, six quiz moments.
- Anatomy art is reviewed for accuracy against a neuroanatomy text before build.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each outcome waits for a prediction; a wrong prediction is fine and gets a "here's why" line.
- Keyboard: Tab to the brain, view buttons, cases, the neuron controls, the body map and the quiz; arrow keys turn the brain; Space fires the neuron.
- With Motion off the brain turns in steps and the signal jumps along the axon.

## Look
- Accent `--brand` #a12b5e brain magenta (header, regions, the neuron); gold #f4c542 (the lit region, the firing signal); paper #fbf1f5; ink #2c0a19; muted #625259.
- Contrast (WCAG 2.1, computed): white on brand 6.95:1; brand on paper 6.29:1; ink on paper 16.32:1; muted on paper 6.62:1; ink on gold 11.09:1.
- Never color alone: regions carry labels; the voltage trace carries numbers; fast and slow carry words.
- Different from this batch (Senate rust, olive drab, web teal, civic blue).

## Art
- Illustrated anatomy (Gemini, layered, 4: side, top, midline, the neuron; accuracy checked against Kandel and colleagues, "Principles of Neural Science").
- Public domain: the daguerreotype of Phineas Gage with his tamping iron and Harlow's drawings (Warren Anatomical Museum, Harvard, ids and rights checked at build); Broca's preserved brain photograph, if free to use.
- Drawn in code: the voltage trace, the synapse, the body map.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the case narrator; `clear-teacher` as the explainer and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.view + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each case story.
- how `predict`: "Pick what you think changed."
- event, whole, each outcome.
- how `fire`: "Tap to add input until the neuron fires."
- how `substance`: "Add a substance and predict its effect."
- how `trace`: "Trace the near miss through the body."
- how `quiz`: "Name the region and the system."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the turning brain, cases, the neuron model, the synapse, the body map, the quiz.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Guess fast | Predictions aren't scored; the region card must be opened before the next case. |
| Substances | Tap through | Each substance needs a prediction of what changes at the synapse. |
| Quiz | Pick the same region | Each moment checks both the region and the system. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Case story (whole), waits; `predict`; outcome (whole).
2. `fire`; `substance`.
3. `trace`.
4. `quiz`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| APA.Biological wording | APA, "National Standards for High School Psychology Curricula" (2022) | data/modules/social-studies.txt (Brain and Behavior row) | yes |
| Gage's accident (September 13, 1848), survival to 1860, Harlow's reports | Macmillan, "An Odd Kind of Fame" (MIT, 2000) | Harlow, Publications of the Massachusetts Medical Society (1868) | yes |
| Broca's patient (1861) and Wernicke (1874) | Kandel and colleagues, "Principles of Neural Science" (6th ed., 2021) | Dronkers and colleagues, Brain (2007) | yes |
| H.M.'s 1953 surgery and memory loss | Scoville and Milner, Journal of Neurology, Neurosurgery and Psychiatry (1957) | Corkin, "Permanent Present Tense" (Basic, 2013) | yes |
| Split-brain studies; Sperry's 1981 Nobel Prize | Nobel Prize, "Roger W. Sperry, Facts" | Gazzaniga, Nature Reviews Neuroscience (2005) | yes |
| Resting potential near -70 mV, threshold near -55 mV | Kandel and colleagues (2021) | Purves and colleagues, "Neuroscience" (6th ed., 2018) | yes |
| Caffeine blocks adenosine receptors; SSRIs block serotonin reuptake; curare blocks acetylcholine receptors | Purves and colleagues (2018) | National Institute on Drug Abuse and National Library of Medicine, StatPearls | yes |
| The stress response: sympathetic nerves, adrenaline, cortisol | Harvard Health Publishing, "Understanding the stress response" | Purves and colleagues (2018) | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r21, 2026-11-09): Gage lived about 11.7 years after the accident; threshold is 15 mV above rest; six cases each have a region and a method; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 brain and card; at 680x425 sheet.
2. Six cases each light a region and name how we know. (APA.Biological)
3. The neuron fires at threshold and each substance changes the synapse as stated. (APA.Biological)
4. The near miss traces nerves and hormones, marked fast and slow. (APA.Biological)
5. The quiz names region and system for six new moments.
6. Anatomy art is checked against a neuroanatomy text.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: stepped turns; no network requests.

## Open questions
None.
