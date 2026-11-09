# Paragraph Surgeon

## One idea
The student operates on one strong informational paragraph at a time, lifts out or moves a sentence and watches a vital-signs monitor show what the key concept just lost (its definition, its limits, its example, its "but"), while a reader card shows the misunderstanding that follows ("So any rare animal is endangered?"), then tags each sentence's job and restores the strongest order, so they learn how particular sentences develop and refine a key concept.

## Not like
- explainer-sections (6-8, spec): how sections build a whole text. Here the sentences inside one paragraph, grade 8.
- essay-train (5, spec): transitions between paragraphs. Here each sentence's job within one.
- argument-map (12, concept): which claims hold up an essay. Here a concept's definition, limits and examples.
- flashback-editor (8, spec, this batch): reordering story scenes in time. Here removing a sentence and seeing what the idea loses.
- old-patterns-new-stories (8, spec, this batch): pairing details across stories. Here roles within one paragraph.

## Who and how
- Grade 8, ELA, module "Analyzing Structure and Paragraphs" (Reading Informational Text). Standard: RI.8.5.
- Driver: one student; class mode is "Case conference", where the projector shows one sentence and the class votes on its job (tool.json `driver: "student"`). Every sentence is read on tap.
- Four patients: "Endangered" (science), "Planet" (science), "Fruit" (science, with one sentence that does nothing) and "Primary source" (history, arrives scrambled). tool.json `modes: ["Patients", "Final case", "Case conference"]`, `minutes: "20-30"`, `grades_label: "Grade 8"`.
- Nothing is saved; `Print` prints each paragraph with its surgical notes.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.8.5 (role of a sentence in developing a concept) | Lift out a sentence and read which monitor line drops and the reader card's misunderstanding | the monitor lines Defined, Narrowed, Illustrated, Qualified, Connected | 2 |
| RI.8.5 (role of each sentence) | Tag each sentence's job | the tags beside the sentences | 3 |
| RI.8.5 (structure of a paragraph) | Try another order; say why an order with every line steady still reads worse | the order note | 4 |
| RI.8.5 | Remove the sentence that does nothing; rebuild a scrambled paragraph and write a surgical note for each sentence | the rebuilt paragraph and notes | 5 |

## Screens and modes
Header (kit): title "Paragraph Surgeon"; `Patients`, `Final case`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A bright operating room drawn in code, a paragraph laid on the table as sentence strips, and a monitor with five lines: Defined, Narrowed, Illustrated, Qualified, Connected; Dr. Amara Bello leads the team. First hint: "Tap the paragraph to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Patient 1, "Endangered".** Written for Curio Class from the law's wording:
1. Under the U.S. Endangered Species Act, a species is endangered when it is in danger of extinction throughout all or a significant portion of its range. (Defines)
2. Being rare is not the same thing; some animals have always been rare without being in danger. (Narrows)
3. A fish that lives in only one desert spring could vanish if that spring dries up. (Illustrates)
4. A species that is likely to become endangered in the foreseeable future is listed as threatened instead. (Qualifies)
5. Listing a species is the first step toward protecting the places it lives. (Connects)
Lifting sentence 2 drops Narrowed and brings the reader card "So any rare animal is endangered?" Lifting 1 flatlines Defined: "Endangered means what, exactly?"

**Patient 2, "Planet".** In 2006 the International Astronomical Union defined a planet in our solar system as a body that orbits the Sun, is massive enough that its own gravity pulls it into a nearly round shape, and has cleared the neighborhood around its orbit; the next sentences narrow (a moon orbits a planet, not the Sun), illustrate (Pluto orbits among many icy bodies in the Kuiper Belt) and qualify (so in 2006 Pluto became a dwarf planet). Lifting the qualifying sentence brings "So Pluto's still a planet?"

**Patient 3, "Fruit".** To a botanist, a fruit is the part of a flowering plant that grows from the flower and holds the seeds; it includes a filler sentence ("Many people enjoy fruit at breakfast.") that the student can remove with every line steady. Lifting a working sentence drops a line; lifting the filler drops none, and the student tags it "does nothing".

**Order.** In each patient the student can drag strips into another order. Some orders keep every line steady but read worse (the example before the definition); the student picks why from prompts (the reader meets an example of nothing yet; the "but" comes before what it limits) or writes their own.

**Final case, "Primary source".** A history paragraph arrives scrambled: a primary source is a record made at the time by someone who took part or saw it (defines); not everything old is primary (narrows); a soldier's letter home from 1863 (illustrates); a modern textbook about that letter is a secondary source (qualifies); historians start from primary sources to check what others say (connects). The student rebuilds it and writes a one-line surgical note for each sentence's job.

**Case conference.** One sentence on the projector; the class votes its job and the teacher reveals the monitor.

At 1366x768 the table and monitor fit side by side; at 680x425 the monitor sits above the table.

## Content
Written for Curio Class: the four paragraphs, their keyed roles with accepted alternates, the monitor line each sentence holds up, the reader cards and the order prompts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Every lift can be undone with `Put back`.
- With Motion off the monitor lines step to their new level without tracing; the alarm is a word ("Narrowed: dropped"), with no flashing.

## Look
- Accent `--brand` #1e6650 surgical green (header, scrubs, monitor frame); gold #f4c542 (the lifted strip, restored lines); paper #eff7f4; ink #08231b; muted #4a5e57. Scene: a clean, bright operating room.
- Contrast (WCAG 2.1, computed): white on brand 6.84:1; brand on paper 6.28:1; ink on paper 15.22:1; muted on paper 6.36:1; ink on gold 10.19:1.
- Never color alone: each monitor line is labeled and shows "steady" or "dropped" in words.
- Different from this batch (curtain red, slate blue, bronze, council violet).

## Art
- People art goes to Gemini: Dr. Amara Bello (a Nigerian American woman in her forties in green scrubs), 4 poses; a nurse, Sam Whitfield (a white man in his twenties who uses a wheelchair), 2 poses; "illustrated friendly surgeon <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`), as small pictures on each patient's chart: a desert spring with small fish (1), a Pluto-like icy world far from the Sun (1), a cut apple showing seeds (1), an old handwritten letter (1).
- No blood, tools in use or real surgery shown; the "operation" is on paper strips.
About 10 images. Drawn in code: operating room, monitor, strips.

## Voice
Bank voice `clear-teacher` as Dr. Bello and the hint voice (unique in this batch); the paragraphs are read by `science-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.patient + ':' + state.sentence`, `welcomeAfter: true`.
- how `welcome`: "Every sentence here has a job. Lift one out and watch what the idea loses."
- event, whole, `paragraph`: the paragraph as it stands.
- event `dropped`: "{Narrowed} dropped."
- event `reader`: the reader card's misunderstanding.
- event `steady`: "Every line steady. That sentence did nothing."
- event `orderAsk`: "Every line's steady, but does it read well? Why not?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: sentence strips with keyed roles and monitor lines, lift and put back, reader cards, order prompts, the scrambled final case.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag every sentence Defines | Each sentence's role is keyed; a wrong tag shows the monitor line it actually holds. |
| Filler | Remove sentences until one drops nothing | Removing a working sentence drops a line and must be put back before the patient is done. |
| Order note | Pick any prompt | The note must match the keyed problem with that order. |
| Final case | Copy the order from Patient 1 | The final case's notes need a role word per sentence that matches its key. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the paragraph: `paragraph` (whole), `welcome` (queued, first time).
2. Lift: `dropped` (waits), then `reader`; or `steady`.
3. Order: `orderAsk` when an order keeps every line steady but is keyed weaker.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.8.5 wording | thecorestandards.org, Reading Informational Text Grade 8 | CCSS ELA 2010 PDF | yes |
| Endangered means in danger of extinction throughout all or a significant portion of its range; threatened means likely to become endangered within the foreseeable future | Cornell Law LII, 16 U.S.C. 1532 (checked 2026-11-09) | U.S. Fish and Wildlife Service, Endangered Species Act glossary | yes |
| The IAU's 2006 planet definition (orbits the Sun, nearly round from its own gravity, has cleared its orbit's neighborhood); Pluto became a dwarf planet | IAU Resolution B5, press release iau0603 (2006) | NASA Science, dwarf planets (checked 2026-11-09) | yes |
| In botany a fruit develops from the flower and holds the seeds | Britannica, fruit | Merriam-Webster, fruit (botany sense) | yes |
| A primary source was made at the time by someone who took part or saw it; secondary sources are about primary ones | Library of Congress, using primary sources | National Archives, primary and secondary sources | yes |
Backed twice: 5. Cut: 0.

Design choices (not claims): the desert spring fish and the 1863 letter are general examples, not named species or people.

Checks run (Python, scratchpad b23, 2026-11-09): the saved LII page contains "in danger of extinction throughout all or a significant portion of its range" and "foreseeable future throughout all or a significant portion of its range"; NASA's page says dwarf planets "have not been able to clear" their orbits; in every patient no monitor line is held by two sentences, and Fruit has one filler; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and monitor fit; at 680x425 the monitor sits above.
2. Lifting a sentence drops its keyed line and shows a reader card; Put back restores it. (RI.8.5)
3. Tags check against keyed roles. (RI.8.5)
4. Reordering takes a keyed order note. (RI.8.5)
5. The filler is removed with every line steady; the final case rebuilds with notes. (RI.8.5)
6. Case conference works on the projector.
7. Print shows paragraphs with notes.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: monitor lines step without tracing and nothing flashes; no network requests.

## Open questions
- None for Cory.
