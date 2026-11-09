# Verb Conjugation Race

## One idea
The student drives a rally car while the co-driver calls out short sentences with the verb missing (Nosotros ___ (vivir) en la costa), and each correct present-tense form keeps the car at speed, while the student's own answers build the ending chart and the "boot" shape of stem-changing verbs stage by stage (nosotros and vosotros outside the boot), so the pattern is found rather than memorized and the student learns to form present-tense verbs accurately in sentences that mean something.

## Not like
- detective-del-pasado (6-12, spec): past tenses chosen by meaning. Here present-tense forms at speed.
- consejero (9-12, spec later): the subjunctive in advice. Here the present indicative.
- el-restaurante (K-12, spec): gustar inside a dialogue. Here verbs across all persons.
- por-dónde (6-12, spec, this batch): commands to give directions. Here statements in every person.
- word-problem-decoder (6-8, spec, this batch): spotting patterns in math words. Here building a pattern from your own answers.

## Who and how
- Grades 6 to 12, World Languages (Spanish), module "Present Tense Verbs". Standard: ACTFL Intermediate Low (creates with language in simple present-tense sentences).
- Driver: one student; class mode is "Carrera por equipos", where two teams on the projector take turns answering the co-driver (tool.json `driver: "student"`). Every sentence is spoken in Spanish with its text; the hint voice speaks English.
- Seven stages: -ar verbs; -er and -ir verbs; e to ie; o to ue; e to i; yo-irregulars (tengo, hago, salgo, pongo, conozco); ser, estar, ir and tener; then a mixed final against the ghost. Help levels: Lots (tap answers from three choices), Some (type with the ending chart visible), Little (type, chart hidden). A vosotros toggle adds vosotros for Spain-focused courses (off by default). tool.json `modes: ["Rally", "Mi tabla", "Carrera por equipos"]`, `minutes: "10-20"`, `grades_label: "Grades 6-12"`.
- The ghost of the student's best run per stage is saved on this device only (localStorage), and the screen says so: "Your best times stay on this device. Nothing is uploaded." `Borrar mis tiempos` clears them.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Intermediate Low (regular present forms) | Complete sentences with -ar, -er and -ir forms | the ending chart filling from answers | 2 |
| ACTFL Intermediate Low (stem changers) | Complete sentences with e to ie, o to ue, e to i verbs | the boot shape forming | 3 |
| ACTFL Intermediate Low (irregular verbs) | Complete yo-irregular and fully irregular forms | the irregular cards | 4 |
| ACTFL Intermediate Low (meaning in sentences) | Use the subject in the sentence, including names and plural nouns | the sentence with its subject lit | 2 |

## Screens and modes
Header (kit): title "Verb Conjugation Race"; `Rally`, `Mi tabla`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Accent buttons (á é í ó ú ñ) sit beside the answer box.

**On load and first tap.** A rally car at a dirt-road start line in the hills, a faint ghost car beside it, and the co-driver, Nuria, with a route book. Stage 1 is lit: "-ar". First hint: "Tap Start to hear the first call." The first call plays; the welcome is queued after it (`welcomeAfter: true`).

**Rally.** The car drives a winding stage of 12 calls. Each call is a short sentence with a blank and the verb in brackets: "Mis primos ___ (hablar) inglés y español." "Yo ___ (comer) arroz con frijoles." "¿Tú ___ (poder) venir hoy?" The student answers before the next bend. A right form keeps speed. A wrong form slows the car and shows the needed ending with the stem and ending split (habl | an), and the call repeats later in the stage. A missing accent counts as "almost": the car slips a little and a card shows why it matters (está, "is", and esta, "this"; habló and hablo). The co-driver never shouts; speed is the only pressure, and at Lots help there is no clock at all.

**Mi tabla.** After each stage the student's correct answers fill a chart of persons and endings. In the stem-changer stages the changed forms light and form a boot (yo, tú, él, ellos inside; nosotros and vosotros outside), and the co-driver says "¿Ves la bota?" The chart prints.

**Final.** A mixed stage at full speed against the ghost of the best run.

**Carrera por equipos.** On the projector, two teams alternate calls.

At 1366x768 the road and answer box fit; at 680x425 the chart is a tab.

## Content
- About 300 sentences written for Curio Class, 12 to 20 per stage plus the final, each with a meaningful subject (names, pronouns, plural nouns) and everyday topics (family, school, sports, food, music).
- Verbs per stage, about 10 each: hablar, estudiar, bailar; comer, vivir, escribir; querer, pensar, empezar; poder, dormir, volver, jugar (u to ue); pedir, servir, repetir; tener, hacer, salir, poner, conocer; ser, estar, ir.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Typing never times out at Lots help; at Some and Little the car slows but never stops for a slow answer.
- With Motion off the road doesn't scroll; a progress bar fills per call and the car icon moves one step per answer.

## Look
- Accent `--brand` #b3261e rally red (header, the car, stage flags); gold #f4c542 (the right ending, the boot); paper #fdf1f0; ink #2e0906; muted #6d5250. Scene: a hillside dirt rally road.
- Contrast (WCAG 2.1, computed): white on brand 6.54:1; brand on paper 5.92:1; ink on paper 16.42:1; muted on paper 6.40:1; ink on gold 11.15:1.
- Never color alone: right, almost and wrong show a word and a symbol; the boot is outlined.
- Different from this batch (plaza green, lab blue, plum, playroom orange).

## Art
- People art goes to Gemini: Nuria (a Uruguayan woman in her thirties in a rally suit with a route book), 4 poses; "illustrated rally co-driver <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Drawn in code: road, car, ghost, chart and boot for speed and clarity.
- Local FLUX (`scripts/localart.py`): a hillside backdrop per stage (7).
About 11 images.

## Voice
Bank voice `easy-coach` as the English hint voice (unique in this batch); Nuria is read by `lively-host` in Spanish, with a neutral Latin American accent by default and a Peninsular accent when the vosotros toggle is on (unique in this batch). `Curio.voice` with `scope: () => state.stage + ':' + state.call`, `welcomeAfter: true`.
- how `welcome`: "Nuria reads a sentence with the verb missing. Type the right form before the next bend."
- event `call`: the sentence.
- event `right`: "¡Bien!"
- event `fix`: the right form, stem then ending.
- event `almost`: "Casi. Mind the accent."
- event `boot`: "¿Ves la bota?"
- event `privacy`: "Your best times stay on this device. Nothing is uploaded."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio and `es.say` for calls, and `es.check` with its accent note for answers. The stages, car, ghost (localStorage wrapped in try and catch), chart and boot are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Forms | Always type the infinitive | Never accepted; the car slows and the call repeats. |
| Choices (Lots) | Tap at random | Wrong taps repeat later in the stage; the chart fills only from right answers. |
| Boot | Change the stem in every person | Nosotros forms are keyed unchanged (podemos, not puedemos). |
| Accents | Skip accents | Counted "almost" with the meaning card; the stage still counts it as a slip. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Start: `call`, `welcome` (queued, first time).
2. Each call: `call`, then `right`, `fix` or `almost`.
3. After a stem stage: `boot`. First save: `privacy`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Intermediate Low: creates with language in simple sentences on familiar topics | ACTFL Proficiency Guidelines 2012, Speaking, Intermediate Low | NCSSFL-ACTFL Can-Do Statements (2017), Intermediate Low | yes |
| Present-tense stem changes (e to ie, o to ue, u to ue in jugar, e to i) fall in stressed syllables, so nosotros and vosotros keep the original stem | Real Academia Española, Nueva gramática, irregular verbs (diphthongizing verbs) | Instituto Cervantes, Plan curricular, A1-A2 grammar | yes |
| Yo-irregulars (tengo, hago, salgo, pongo, conozco) and irregular ser, estar, ir | Real Academia Española, Nueva gramática, conjugation models | Instituto Cervantes, Plan curricular, A1 grammar | yes |
| Written accents change meaning in pairs such as está and esta, hablo and habló | Real Academia Española, Ortografía (2010), the written accent | Fundéu RAE, guidance on diacritic accents | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b28, 2026-11-09): a conjugator for the stage verbs gives the keyed forms in every person, the stem change appears in yo, tú, él and ellos and never in nosotros or vosotros, and jugar gives juego and jugamos; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 road and answer box fit; at 680x425 chart is a tab.
2. Regular forms keep speed; wrong forms show stem and ending. (ACTFL Intermediate Low)
3. Stem-changer answers build the boot. (ACTFL Intermediate Low)
4. Irregular stages and the mixed final run against the ghost. (ACTFL Intermediate Low)
5. Accents count as "almost" with the meaning card.
6. Help levels and the vosotros toggle behave as in Who and how.
7. Carrera por equipos and Print work; best times persist; the privacy line shows; Borrar clears.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no scrolling road; no network requests.
10. Storage blocked: the tool still works and says best times won't be kept.

## Open questions
- Spanish audio review: same as calendario-vivo (default used: a fresh agent checks the Spanish text, and Sara or Cory listens to a sample of 20 lines).
