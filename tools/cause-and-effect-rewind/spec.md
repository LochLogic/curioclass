# Cause and Effect Rewind

## One idea
A short science scene plays forward (an ice pop melts in the sun, a puddle shrinks, a bare hillside washes away in a storm, a bulb lights when a circuit closes), then the student pulls a Rewind lever to step back one link at a time and joins each pair of steps with because, so or as a result, and a connector pointing the wrong way makes the scene play backward on screen (the puddle grows back), so they learn to explain how and why things happen and that "so" and "because" point in opposite directions.

## Not like
- math-explainer (3-5, spec later): explaining the steps of a math solution. Here causes and effects in science.
- time-machine-talk (3-5, spec later): past tense in history. Here cause and effect language.
- opinion-builder (3-5, spec later): reasons for an opinion. Here reasons why something happened.
- bedtime-retell (K-2, spec, this batch): story order with first and then. Here cause order, with because and so.
- i-choose-because (K-2, spec, this batch): "because" for a choice. Here "because" for a cause.

## Who and how
- Grades 3 to 5, English Language Development, module "Cause and Effect Language". Standards: WIDA ELD-SC (Standard 4, the language of science), Explain key language use (WIDA 2020).
- Driver: one student; class mode is "Predict the rewind", where the class says the next step back before the lever is pulled (tool.json `driver: "student"`). Every step, tile and sentence is read on tap.
- Eight scenes in three sets (Heat and water; Land and water; Circuits). Help setting: Lots (picture steps, full frames), Some (word tiles, frames), Little (connector bank only, then typing). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Rewind", "Shuffle", "Predict the rewind"]`, `minutes: "15-25"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints each chain as a short paragraph.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA Explain (cause and effect connectors) | Join two steps with because or so in the right direction | the sentence and the scene playing forward or backward | 2 |
| WIDA Explain (both orders) | Write the same link both ways: "The puddle got smaller because the sun heated the water." and "The sun heated the water, so the puddle got smaller." | the pair of sentences | 3 |
| WIDA Explain (a whole chain) | Write the chain as a paragraph with as a result and this caused | the chain paragraph read back | 4 |
| WIDA ELD-SC (heating, melting, evaporating, erosion, circuits) | Use the science words in each link | the word tiles with pictures | 2 |
| WIDA Explain (what didn't cause it) | In Shuffle, find the step that happened but caused nothing | the "didn't cause it" tag | 5 |

## Screens and modes
Header (kit): title "Cause and Effect Rewind"; `Rewind`, `Shuffle`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A small film booth with a screen showing the first scene and a big brass lever marked Rewind; the projectionist, Dr. Lena Okafor, a science teacher in a lab coat, stands beside it. First hint: "Tap Play to watch the scene." The scene plays forward; the welcome is queued after it (`welcomeAfter: true`).

**The scenes.**
- Heat and water: an ice pop on a hot step (the sun heats the ice pop, so it melts, so it drips); a puddle after rain (the sun heats the water, it evaporates into the air, so the puddle gets smaller); wet laundry on a line on a windy, sunny day.
- Land and water: a bare hillside in a storm (heavy rain runs down the slope, the water carries soil away, so a gully forms); a grassy hillside in the same storm (roots hold the soil, so less washes away).
- Circuits: a battery, wire and bulb (the switch closes the loop, so electricity flows, so the bulb lights); an open switch (the loop is broken, so the bulb stays dark); a loose wire.

**Rewind.** Each pull steps back one link and shows two steps side by side. The student builds the link from tiles: [effect] because [cause], or [cause], so [effect], or [cause]. As a result, [effect]. If "so" sits where "because" belongs, the scene plays that link backward (the puddle grows back, the drips climb into the ice pop) and Dr. Okafor says "Hmm, that made it run backward. Which one happened first?" Then the student writes the same link the other way.

**Chain.** At the end of a scene the whole chain is laid out first cause to last effect, and the student writes it as a short paragraph using as a result and this caused; `Read it back` reads it.

**Shuffle.** Later scenes arrive with steps shuffled, plus one step that happened but caused nothing (a bird lands on the wire; a dog barks during the storm). The student orders the steps, tags the extra one "didn't cause it", and links the rest.

**Predict the rewind.** On the projector, the class predicts the step before each pull.

At 1366x768 the screen and tiles fit; at 680x425 the tiles are below.

## Content
Written for Curio Class: eight scenes, each three or four steps, with keyed links, science word tiles (heat, melt, evaporate, water vapor, erosion, soil, roots, circuit, switch, current), and one non-cause step per shuffle scene. Each scene's science is stated simply and correctly for grades 3 to 5.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The lever can be pulled forward again to replay; links can be rebuilt any time.
- With Motion off the scene shows before and after stills instead of playing, and a backward link shows a "backward" label on the stills.

## Look
- Accent `--brand` #7c4a03 rewind amber (header, lever, film frame); gold #f4c542 (a correct link, the bulb when lit); paper #fbf6ee; ink #271702; muted #635545. Scene: a cozy school film booth.
- Contrast (WCAG 2.1, computed): white on brand 7.40:1; brand on paper 6.88:1; ink on paper 16.14:1; muted on paper 6.69:1; ink on gold 10.67:1.
- Never color alone: forward and backward show arrows with words; connector tiles are labeled.
- Different from this batch (terracotta, hallway blue, town green, night indigo).

## Art
- People art goes to Gemini: Dr. Lena Okafor (a Nigerian American woman in her forties in a lab coat), 3 poses; "illustrated friendly science teacher <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): each scene as before and after stills, no faces (8 scenes, 2 to 4 stills each, about 26); the film booth (1).
About 30 images. Drawn in code: lever, link tiles, chain layout, simple circuit animation.

## Voice
Bank voice `science-narrator` as Dr. Okafor and the hint voice (unique in this batch); the student's sentences and chains are read back by `calm-professor` (unique in this batch). `Curio.voice` with `scope: () => state.scene + ':' + state.link`, `welcomeAfter: true`.
- how `welcome`: "Things happen for a reason. Rewind the scene one step at a time, and tell me why each step happened."
- event `step`: the step's caption.
- event, whole, `link`: the built sentence.
- event `backward`: "Hmm, that made it run backward. Which one happened first?"
- event `extra`: "Did that cause anything?"
- event, whole, `chain`: the chain paragraph.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: scene steps with keyed cause order, connector direction check, backward playback, the shuffle with a non-cause step, chain builder, help levels.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Direction | Always use "because" | Each link must also be written the other way with "so". |
| Science words | Leave out the science | At Some and Little help, each link needs the keyed science word for that step. |
| Shuffle | Link every step | The non-cause step is keyed; linking it gets "Did that cause anything?" |
| Chain | Repeat one link | The chain needs every link in order and "as a result" or "this caused". |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Play: each `step`, `welcome` (queued, first time).
2. Rewind: `step` for the two steps, then `link` (whole) when built; `backward` if it fires.
3. Shuffle: `extra` as it fires. Chain: `chain` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 4 is the language of science; Explain features include cause and effect relationships | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| Heat from the sun makes water evaporate into water vapor, so puddles shrink and laundry dries; wind speeds drying | USGS Water Science School, evaporation and the water cycle | NASA Climate Kids or NOAA SciJinks, the water cycle | yes |
| Running water carries soil away (erosion); plant roots hold soil and reduce it | USDA Natural Resources Conservation Service, soil erosion | National Geographic Education, erosion | yes |
| A bulb lights only when the circuit is a closed loop; an open switch stops the current | NGSS 4-PS3-2 and its clarification | Khan Academy or PhET, circuit basics | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b25, 2026-11-09): every scene's links reverse correctly between "because" and "so" (effect because cause; cause, so effect); each shuffle scene has exactly one keyed non-cause step; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 screen and tiles fit; at 680x425 tiles are below.
2. Links check direction; the wrong connector plays the link backward. (WIDA Explain)
3. Each link is written both ways. (WIDA Explain)
4. Chains are written as paragraphs and read back. (WIDA Explain, ELD-SC)
5. Shuffle finds the non-cause step. (WIDA Explain)
6. Help levels fade supports as in Who and how.
7. Predict the rewind and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: stills replace playback; no network requests.

## Open questions
- Home-language support: this follows Cory's open question on home-language glossaries for the ELD tools (default used: English only, with pictures and read-aloud).
