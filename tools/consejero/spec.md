# Consejero

## One idea
Friends text the student their everyday problems in a group chat in Spanish (a partner who does nothing on the group project, a lost phone, too many practices, a sister who borrows clothes), and the student answers with advice, wishes, doubts and feelings (Te recomiendo que hables con ella, Ojalá que lo encuentres, No creo que sea tu culpa), choosing what they want to do, then the trigger, the new subject and the verb form, while paired lines show that the subjunctive appears when one person wants, doubts, feels or recommends something about another (Quiero hablar, but Quiero que hables), so they learn to use the present subjunctive in connected sentences.

## Not like
- debate-en-español (9-12, spec, this batch): positions on a public question in paragraphs. Here personal advice in a chat.
- el-restaurante (K-12, spec): likes and polite requests. Here wishes, doubts and recommendations about other people.
- detective-del-pasado (6-12, spec): past narration. Here the present subjunctive.
- verb-conjugation-race (6-12, spec): present indicative forms at speed. Here choosing indicative or subjunctive by meaning.
- first-impressions-check (9-12, spec, this batch): guesses about strangers. Here help for friends.

## Who and how
- Grades 9 to 12, World Languages (Spanish), module "The Subjunctive and Opinions". Standard: ACTFL Intermediate High (connected sentences; handles uncomplicated situations).
- Driver: one student; class mode is "Consultorio", an advice-column page where the projector shows one letter and the class answers it together (tool.json `driver: "student"`). Messages appear as text and play aloud in Spanish; the hint voice speaks English.
- Twelve problems from four friends. Help levels: Lots (trigger and verb choices of three), Some (trigger tiles, typed verb with `es.check`), Little (typed replies, with the trigger chart hidden). A vosotros toggle swaps the group chat to vosotros (off by default). tool.json `modes: ["Chat", "Mi tabla", "Consultorio"]`, `minutes: "20-30"`, `grades_label: "Grades 9-12"`.
- Nothing is saved; `Print` prints the chat and the trigger chart.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| ACTFL Intermediate High (recommend and advise) | Build "Te recomiendo que..." and "Es importante que..." with the subjunctive | the reply bubble and the friend's answer | 3 |
| ACTFL Intermediate High (wishes and emotions) | Build "Ojalá que...", "Espero que...", "Me alegra que..." | the reply bubble | 3 |
| ACTFL Intermediate High (doubt versus belief) | Choose "Creo que es" or "No creo que sea" by meaning | the paired lines | 4 |
| ACTFL Intermediate High (same subject versus new subject) | Choose infinitive or que plus subjunctive | the paired lines | 4 |
| ACTFL Intermediate High (connected sentences) | Write one longer advice message on their own | the final message | 5 |

## Screens and modes
Header (kit): title "Consejero"; `Chat`, `Mi tabla`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. Spanish first; English gloss only at Lots help.

**On load and first tap.** A phone on a desk with a group chat called "Los de siempre" and four friends: Valentina, Andrés, Sami and Carolina. A message pops up from Valentina: "¡Necesito un consejo! Mi compañero no hace nada en el proyecto." First hint: "Tap Valentina's message to hear it." The first tap plays it; the welcome is queued after it (`welcomeAfter: true`).

**Chat.** Each problem is a short exchange. The student first picks what they want to do (recommend, wish, doubt, react with feeling, or simply say what they believe), then builds the reply: the trigger (Te sugiero que, Es importante que, Ojalá que, Dudo que, Me alegra que, Creo que), the subject and the verb form. The friend answers in character:
- a clear reply gets a real answer that moves the story ("Tienes razón. Mañana hablo con él.");
- a form that changes the meaning gets a puzzled "¿Qué? ¿Tú crees que sí o que no?" (for example "No creo que es" read as mixed);
- a wrong form that keeps the meaning gets the right form shown in the friend's reply, without a buzzer.
Paired lines appear the first time a rule matters: "Quiero hablar con él." (same person) next to "Quiero que hables con él." (another person); "Creo que es verdad." next to "No creo que sea verdad."

**Mi tabla.** The student's replies sort themselves into a chart by trigger group: deseos (quiero que, espero que, ojalá que), emociones (me alegra que, me preocupa que, siento que), dudas (dudo que, no creo que, no es cierto que), recomendaciones (te recomiendo que, te sugiero que, es importante que). The indicative side lists the belief triggers (creo que, es cierto que, estoy seguro de que).

**Final message.** Carolina sends a longer problem; the student writes one advice message of four to six sentences on their own, using at least three trigger groups, and Carolina answers.

**Consultorio.** On the projector, one advice-column letter for the class to answer together.

At 1366x768 the phone and builder fit; at 680x425 the builder is below the phone.

## Content
- Twelve everyday problems written for Curio Class: group projects, a lost phone, too many practices, a borrowed sweater, a canceled concert, a new kid in class, a driving test, a fight over a video game, a pet that's sick (mild, with a vet visit), a cousin's quinceañera outfit, a part-time job schedule, a surprise party plan.
- Problems stay everyday; nothing touches self-harm, abuse or crises. A teacher note in the tool says where to send a student who brings up something serious.
- Friends speak neutral Latin American Spanish with tú; usted appears in one exchange with a friend's grandmother.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Replies can be rebuilt before sending; there is no score.
- With Motion off bubbles appear without sliding and typing dots don't animate.

## Look
- Accent `--brand` #00607a chat teal (header, the student's bubbles, the chart frame); gold #f4c542 (the trigger word, the subjunctive ending); paper #eef6f8; ink #05212a; muted #4a5c62. Scene: a phone on a desk with a group chat.
- Contrast (WCAG 2.1, computed): white on brand 7.11:1; brand on paper 6.49:1; ink on paper 15.25:1; muted on paper 6.39:1; ink on gold 10.27:1.
- Never color alone: triggers are underlined and endings boxed; chart groups are labeled.
- Different from this batch (council maroon, dawn indigo).

## Art
- People art goes to Gemini: chat avatars and reaction stickers for Valentina (a Colombian American girl), Andrés (a Guatemalan American boy), Sami (a Cuban American teen who is nonbinary, pronouns elle in Spanish and they in English, shown in the profile), Carolina (a Puerto Rican girl), each about sixteen, 4 expressions each; "illustrated teen chat avatar <expression>, soft gouache, plain white background"; 1:1; cutout yes.
- Drawn in code: the phone, chat and chart.
About 16 images.

## Voice
Bank voice `upbeat-guide` as the English hint voice (unique in this batch); Valentina and Carolina are read by `playful-friend`, Andrés by `casual-peer` and Sami by `bright-teacher` styled as a teen, all in Spanish with neutral Latin American accents (each unique in this batch). `Curio.voice` with `scope: () => state.problem + ':' + state.turn`, `welcomeAfter: true`.
- how `welcome`: "Your friends need advice. Choose what you want to say, then build it in Spanish."
- event `message`: the friend's message.
- event `reply`: the student's reply read back.
- event `confused`: "¿Qué? ¿Tú crees que sí o que no?"
- event `pair`: the paired lines.
- event, whole, `final`: the final message, then Carolina's answer.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
spanish (`kit/spanish.js`, `__tool.es`), described in full in tools/calendario-vivo/spec.md. This tool uses: word records with audio and `es.say`, `es.tiles` for triggers and subjects, and `es.check` with mood tags in the keys (indicative or subjunctive) and its accent note. The chat, friend reactions, pairs and the trigger chart are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Mood | Use the subjunctive after every que | Belief triggers (creo que, es cierto que) are keyed to the indicative; "Creo que sea" gets the confused reply. |
| Subject | Always add que | Same-subject wishes are keyed to the infinitive (Quiero ir, not Quiero que vaya yo). |
| Choices (Lots) | Tap at random | Wrong forms get shown fixed and the exchange repeats once. |
| Final | Paste three short replies | The final needs at least three trigger groups and Carolina's name or her problem's words. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Valentina's message: `message`, `welcome` (queued, first time).
2. Each turn: `message` (waits); after sending, `reply`, then the friend's answer or `confused`; `pair` the first time a rule appears.
3. Final: `final` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| ACTFL Intermediate High: connected sentences, handles uncomplicated tasks, emerging paragraph-length speech | ACTFL Proficiency Guidelines 2012, Speaking, Intermediate High | NCSSFL-ACTFL Can-Do Statements (2017), Intermediate High | yes |
| The subjunctive follows verbs of wishing, emotion, doubt and influence when the subject changes; with the same subject the infinitive is used | Real Academia Española, Nueva gramática, the subjunctive in noun clauses | Instituto Cervantes, Plan curricular, B1 grammar | yes |
| "Creo que" takes the indicative and "No creo que" usually takes the subjunctive | Real Academia Española, Nueva gramática, negation and mood | Instituto Cervantes, Plan curricular, B1 grammar | yes |
| "Ojalá" is followed by the subjunctive | Real Academia Española, Diccionario panhispánico de dudas, "ojalá" | Instituto Cervantes, Plan curricular, B1 grammar | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b29, 2026-11-09): every keyed reply's mood matches its trigger group (subjunctive for wish, emotion, doubt and recommendation with a new subject; indicative for belief; infinitive for same subject); a present-subjunctive generator gives hables, encuentres, sea, vayas and tengas; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 phone and builder fit; at 680x425 builder below.
2. Messages play in Spanish with text.
3. Recommendations, wishes and feelings take the subjunctive with a new subject. (ACTFL Intermediate High)
4. Belief and doubt, and same and new subject, are shown in pairs and checked. (ACTFL Intermediate High)
5. The final message uses three trigger groups and gets an answer. (ACTFL Intermediate High)
6. Help levels and the vosotros toggle behave as in Who and how.
7. Mi tabla, Consultorio and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: bubbles appear without sliding; no network requests.

## Open questions
- Spanish audio review: same as calendario-vivo (default used: a fresh agent checks the Spanish text, and Sara or Cory listens to a sample of 20 lines).
