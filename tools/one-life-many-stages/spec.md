# One Life, Many Stages

## One idea
The student follows Mai, a made-up person, from birth to age 80 along a timeline of eight stops, and at each stop predicts what she will do before the research answers: at 8 months, will she cry when her parent leaves the room and how will she greet them back (Ainsworth's Strange Situation); at 6 months, does she know a hidden toy still exists (Piaget's object permanence, and Baillargeon's later evidence that babies know earlier); at 4, where will her friend look for a moved marble (the false-belief test); at 6 and at 9, is the tall glass fuller than the wide one (conservation); at 15, will she take more risks in a driving game with friends watching (Steinberg); at 25, is her brain done developing; at 45, who is she caring for; at 75, has her memory for names slipped while her vocabulary has grown, and is she happier or sadder than at 25 (Carstensen); each stop shows the physical, cognitive and social side, and the student's predictions stack up beside the findings, so a twelfth grader learns physical, cognitive and social development across the lifespan and how researchers found it out.

## Not like
- train-your-dog (12, spec): learning by conditioning. Here growing across a life.
- brain-explorer (12, spec): brain structures. Here how a person changes with age.
- trait-lab (12, spec): personality and intelligence measures. Here change over time.
- remembrance-archive (10, spec): real lives in documents. Here one made-up life with real research.

## Who and how
- Grade 12, Psychology, module "Lifespan Development". Standards: APA.Development and Learning (APA National Standards for High School Psychology Curricula, the lifespan half: physical, cognitive and social development from infancy through old age, and the research methods behind it; the learning half is taught in train-your-dog).
- Format: timeline. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Eight stops, each with a prediction, a study, and physical, cognitive and social cards; a summary of predictions against findings. Extra: Second life (a second made-up person, Theo, with different circumstances, to see which findings hold across lives). tool.json `modes: ["Mai's life", "Second life"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| APA.Development and Learning (cognitive) | Predict object permanence, false belief and conservation, then see the study | the study set-up and result; Piaget's stage and the later challenges | 2 |
| APA.Development and Learning (social) | Predict attachment, peer influence and older adults' well-being, then see the study | the Strange Situation; the driving game; the well-being chart | 3 |
| APA.Development and Learning (physical and methods) | Read each stop's physical card and name the method (observation, experiment, longitudinal, cross-sectional) | the physical card; the method tag | 4 |

## Screens and modes
Header (kit): title "One Life, Many Stages"; `Mai's life`, `Second life`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A photo album opens to a baby picture labeled "Mai, 8 months (made up for this tool)". A timeline runs across the bottom from 0 to 80 with eight stops. A prediction card: "Mai's parent leaves the room for three minutes. What will Mai do? And when the parent comes back?" The welcome is queued (`welcomeAfter: true`): "You'll follow one life from first year to old age. At every stop, guess first. Then see what the research found. Tap a prediction." First hint: "Tap a prediction for Mai at 8 months."

**Stops (focus: the prediction and the study).** At 1366x768 the album fills the left with the study card right; at 680x425 the card is a sheet. Each stop: a prediction, then the study, then three cards (physical, cognitive, social) and a method tag.
1. 6 to 8 months: object permanence (Piaget saw searching for a hidden toy at about 8 months; Baillargeon's looking-time studies from 1985 suggest babies expect objects to persist by about 4 months). Attachment: the Strange Situation (Ainsworth, 1978); in many samples about two in three babies are classed as securely attached.
2. Age 4: false belief (Wimmer and Perner, 1983; Baron-Cohen, Leslie and Frith, 1985): most 4-year-olds pass, most 3-year-olds don't.
3. Ages 6 and 9: conservation of liquid; younger children judge by the tall glass, older children don't (Piaget's preoperational and concrete operational stages).
4. Age 15: risk in a driving game rises with peers watching for teens more than adults (Gardner and Steinberg, 2005); puberty's physical changes.
5. Age 25: brain imaging shows the prefrontal cortex still maturing into the mid-20s (Giedd and colleagues, 1999, and later longitudinal scans).
6. Age 45: caring for children and aging parents at once; Erikson's generativity.
7. Age 75: processing speed and memory for names decline on average while vocabulary and knowledge hold or grow (fluid and crystallized intelligence; Salthouse); older adults report more positive emotional lives on average (Carstensen and colleagues, 2011).
8. Age 80: looking back; Erikson's integrity.
- Each method tag: observation, experiment, longitudinal (the same people over years) or cross-sectional (different ages at once), with one limit each.

**The summary (the aha).** The student's predictions beside the findings across eight stops. "I was right about ___. I was surprised by ___. Development at every age is physical, cognitive and social: at ___, Mai showed all three when ___." Narrator: "Nobody stops developing. They just change what they're getting better at."

**The end.** The album, the predictions and findings, and the summary. `Print` prints them.

**Second life (extra).** Theo (made up) grows up with different circumstances; the student checks which findings held.

## Content
- Mai and Theo are made up and labeled; eight stops with published studies and stated findings; method tags; the summary template.
- Findings are stated as averages with their limits; no stop asks about the student's own life.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The study waits for a prediction; stops open in order and can be revisited.
- Keyboard: Tab to the timeline, predictions, study and cards; Enter to choose.
- With Motion off the album turns pages without animating.

## Look
- Accent `--brand` #8a3b5c lifespan rose (header, the timeline, the album); gold #f4c542 (the current stop, the chosen prediction); paper #faf1f5; ink #260b18; muted #605259.
- Contrast (WCAG 2.1, computed): white on brand 7.34:1; brand on paper 6.63:1; ink on paper 16.59:1; muted on paper 6.66:1; ink on gold 11.29:1.
- Never color alone: stops carry ages; method tags carry words.
- Different from this batch (biscuit brown, chart navy, Fed green, trait indigo).

## Art
- People (illustrated) for Mai at eight ages and Theo at four ages, labeled "illustration" (Gemini, `people: true`, 12; cutout yes; one consistent look per person across ages).
- Drawn in code: the study set-ups (the hidden toy, the marble boxes, the glasses), the timeline, charts.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator of Mai's life; `warm-teacher` as the explainer of studies and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.stop + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each stop's scene.
- how `predict`: "Pick what you think Mai will do."
- event, whole, each study.
- how `method`: "Name how the researchers found this."
- how `summary`: "Write what surprised you."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the album timeline, predictions, study cards, method tags, the summary.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Pick the first option | Predictions aren't scored; the summary asks which ones were wrong and why. |
| Method tags | Tag everything "experiment" | Each tag checks against the study. |
| Summary | Write about one age | It needs one stop showing all three kinds of development. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Scene (whole), waits; `predict`.
2. Study (whole); `method`.
3. The next stop.
4. `summary`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| APA.Development and Learning wording | APA, "National Standards for High School Psychology Curricula" (2022) | data/modules/social-studies.txt | yes |
| The Strange Situation and secure attachment rates | Ainsworth and colleagues, "Patterns of Attachment" (Erlbaum, 1978) | van IJzendoorn and Kroonenberg, Child Development (1988) | yes |
| Object permanence: Piaget, then Baillargeon's earlier evidence | Piaget, "The Construction of Reality in the Child" (1954) | Baillargeon, Spelke and Wasserman, Cognition (1985) | yes |
| False belief passed by most 4-year-olds | Wimmer and Perner, Cognition (1983) | Wellman, Cross and Watson, Child Development (2001) | yes |
| Conservation and Piaget's stages | Piaget and Inhelder, "The Psychology of the Child" (1969) | Siegler, "Children's Thinking" (4th ed., 2005) | yes |
| Peers raise teen risk-taking in a driving game | Gardner and Steinberg, Developmental Psychology (2005) | Steinberg, "Age of Opportunity" (Houghton Mifflin, 2014) | yes |
| Prefrontal maturation into the mid-20s | Giedd and colleagues, Nature Neuroscience (1999) | National Institute of Mental Health, "The Teen Brain" | yes |
| Fluid declines, crystallized holds; older adults' emotional well-being | Salthouse, Journal of the International Neuropsychological Society (2010) | Carstensen and colleagues, Psychology and Aging (2011) | yes |
| Erikson's stages | Erikson, "Childhood and Society" (Norton, 1950) | APA Dictionary of Psychology | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r23, 2026-11-09): eight stops in age order from 6 months to 80 years; Baillargeon's age is about half Piaget's; every stop has three development cards and a method tag; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 album and card; at 680x425 sheet.
2. Cognitive stops show prediction, study and the later challenge to Piaget. (APA.Development and Learning)
3. Social stops show attachment, peer influence and older adults' well-being. (APA.Development and Learning)
4. Every stop has a physical card and a method tag with a limit. (APA.Development and Learning)
5. Mai and Theo are labeled made up; no stop asks about the student's own life.
6. Findings are stated as averages with limits.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no page turns; no network requests.

## Open questions
None.
