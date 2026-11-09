# Verb Switchboard

## One idea
At a newsroom switchboard the student runs the same sentences through three panels: Voice (flip "The company dumped oil in the creek" to passive, then drop "by the company", and watch the blame meter fade the actor out of the headline), Mood (turn a fact into a command, a question, a "would" and a "were") and Job (move one verb, "repair", between verb, gerund, participle and infinitive), so they learn how verb forms change who is responsible, how certain a statement is, and what a word is doing in the sentence.

## Not like
- tone-dial (10, concept): word choice and tone. Here verb forms only: voice, mood and verbals, grade 8.
- sentence-diagram-builder (7, spec): clauses and phrases. Here what a verb's form does.
- sentence-remixer (6, spec): pronouns and variety. Here voice and mood shifts.
- bike-lane-briefing (8, spec, this batch): weighing articles against data. Here the grammar inside one headline.
- double-meanings (8, spec): a word doing two jobs for effect. Here the verb's grammatical job.

## Who and how
- Grade 8, ELA, module "Verbals and Voice" (Language). Standards: L.8.1 (a, b, c, d), L.8.3a.
- Driver: one student; class mode is a headline vote on which version is fair to readers (tool.json `driver: "student"`). Every sentence is read on tap.
- Three panels, each a full stage with about 12 sentences, plus the editor's challenge. tool.json `modes: ["Voice", "Mood", "Job", "Editor's challenge", "Headline vote"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.
- Nothing is saved; `Print` prints the student's rewrites and notes.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.8.1b | Flip sentences between active and passive and back | the switch, the sentence and the blame meter | 2 |
| L.8.3a | Choose active or passive for each story (name the actor in news; keep the action central in a lab report) | the story card and the chosen form | 2 |
| L.8.1c | Switch sentences between indicative, imperative, interrogative, conditional and subjunctive | the Mood dial and the sentence | 3 |
| L.8.3a | Use conditional or subjunctive to show uncertainty or a wish against the facts | the certainty meter | 3 |
| L.8.1a | Move a verb between jobs and name each job's function in the sentence | the Job panel's four slots | 4 |
| L.8.1d | Fix a paragraph with shifts in voice and mood that don't belong | the paragraph with the shifts marked | 5 |

## Screens and modes
Header (kit): title "Verb Switchboard"; `Voice`, `Mood`, `Job`, `Editor's challenge`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A busy small-town newsroom at night: a headline board above three switch panels labeled Voice, Mood and Job, and the night editor, Ruth Abernathy, at the copy desk. First hint: "Tap the headline to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Voice.** A sentence sits under a three-way switch: Active, Passive with "by", Passive without "by". "The company dumped oil in the creek" becomes "Oil was dumped in the creek by the company" and "Oil was dumped in the creek". The student builds each form from word tiles (the tool never does the flip for them); a check tests the "be" verb, the past participle and where the actor went. A blame meter shows how plainly the actor is named: full, half, gone. Then story cards ask which form fits: a news story about a spill (name the actor), a lab report ("The water was heated to 80 degrees", where the action matters), a school notice ("Lockers will be cleaned Friday"), a sports recap. The student picks and gives a reason from prompts or their own words.

**Mood.** A five-position dial on one base sentence ("The bridge closes at noon"): indicative ("The bridge closes at noon."), imperative ("Close the bridge at noon."), interrogative ("Does the bridge close at noon?"), conditional ("If the bridge closed, buses would reroute."), subjunctive ("If I were mayor, I would keep the bridge open."; "The council asks that the bridge be closed."). The student writes each form; a certainty meter shows sure, asking, ordering, maybe, against the facts. Then a paragraph where the mood shifts by accident ("If the storm were to hit, the roads would flood. Close the school. Buses will run late.") is fixed by the student.

**Job.** One verb in four slots: "Repairing bikes is fun." (gerund, a noun), "The repaired bike shone." (participle, an adjective), "She learned to repair a bike." (infinitive, a noun here), "He repairs bikes." (the verb itself). The student drags each sentence to a slot and names what the verbal is doing (subject, describes the bike, object of learned). Twelve sentences with eight verbs; three are traps where an "-ing" word is the main verb ("She is repairing").

**Editor's challenge.** A news brief written for Curio Class (a factory's runoff turns a creek orange). The student rewrites it twice, once to hold the company responsible and once to soften it, using only voice and mood, then writes one line on what changed for a reader. Then a final paragraph with three shifts in voice and two in mood to find and fix.

**Headline vote.** Two versions of a headline on the projector; the class votes which is fair to readers and says why.

At 1366x768 the board and panel fit; at 680x425 the panels are tabs.

## Content
Written for Curio Class: about 12 sentences per panel with keyed forms and accepted alternates, the story cards with keyed best forms, the briefs and the shift paragraphs. No real company is named.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each switch can be flipped back at any time; the student's built forms stay.
- With Motion off switches change position without sliding and meters show their level as a word.

## Look
- Accent `--brand` #2b3a67 newsroom navy (header, panels, switches); gold #f4c542 (the active switch, the meter's needle); paper #f3f4f9; ink #0e1428; muted #525a70. Scene: a small newsroom at night.
- Contrast (WCAG 2.1, computed): white on brand 11.03:1; brand on paper 10.04:1; ink on paper 16.63:1; muted on paper 6.26:1; ink on gold 11.23:1.
- Never color alone: meters show words (full, half, gone; sure, asking, ordering, maybe, against the facts); switches are labeled.
- Different from this batch (lane green, rust, club purple, calendar teal).

## Art
- People art goes to Gemini: Ruth Abernathy (a white woman in her sixties with reading glasses on a chain), 3 poses; a young reporter, Dev Malhotra (an Indian American man in his twenties), 2 poses; "illustrated newspaper editor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): newsroom at night (1); an orange creek by a factory fence, no people (1); a closed bridge with a detour sign (1); a bike shop bench with a bike on a stand (1).
About 9 images. Drawn in code: switches, dial, meters, slots.

## Voice
Bank voice `news-reader` as Ruth and the hint voice (unique in this batch); headlines and sentences are read by `big-sister` as Dev (unique in this batch). `Curio.voice` with `scope: () => state.panel + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "Same facts, different verbs. Flip the switches and watch who gets the blame, how sure we sound, and what each word is doing."
- event, whole, `sentence`: the sentence in its current form.
- event `blame`: "The actor is {gone}. Who did it?"
- event `certainty`: "Now it sounds {against the facts}."
- event `job`: "That's a {gerund}. What is it doing here?"
- event `shift`: "The voice changed here. Should it?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: word-tile builders with form checks, the voice switch, the mood dial, the job slots, meters, shift finding.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Voice builds | Move tiles until it passes | The check names the missing part (be verb, participle, actor) and counts tries in the print. |
| Story cards | Always pick active | Each card is keyed; lab and notice cards want passive. |
| Mood | Add "if" to any sentence | Conditional needs "would"; subjunctive needs "were" or a base-form verb after "that". |
| Job | Tag every "-ing" as gerund | The traps keep "-ing" main verbs keyed as verbs. |
| Challenge | Submit the same brief twice | The two rewrites must differ in voice or mood in at least three sentences. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the headline: `sentence`, `welcome` (queued, first time).
2. Voice: `sentence` (whole) after each flip, then `blame`.
3. Mood: `sentence` (whole), then `certainty`.
4. Job: `job` as each slot fills. Shifts: `shift` as marked.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.8.1 (a to d) and L.8.3a wording | thecorestandards.org, Language Grade 8 | CCSS ELA 2010 PDF | yes |
| Passive voice can leave out the actor; choose active to name who did it | Purdue OWL, active and passive voice | Merriam-Webster, passive voice usage guide | yes |
| Gerunds act as nouns, participles as adjectives, infinitives as nouns, adjectives or adverbs | Purdue OWL, verbals | Grammarly Handbook, verbals | yes |
| Subjunctive uses "were" for wishes against the facts and the base form after verbs like "ask that" | Merriam-Webster, subjunctive | Purdue OWL, subjunctive mood | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b24, 2026-11-09): every Voice sentence has a keyed active, passive-with-by and passive-without-by form; each Job sentence's verbal is keyed to one job and the three "-ing" traps are keyed as verbs; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 board and panel fit; at 680x425 the panels are tabs.
2. Voice forms build and check; the blame meter moves; story cards take a form and reason. (L.8.1b, L.8.3a)
3. Mood forms build and check with the certainty meter; the shift paragraph is fixed. (L.8.1c, L.8.3a)
4. Job slots take sentences and named jobs, with traps. (L.8.1a)
5. The editor's challenge takes two rewrites and a final paragraph fix. (L.8.1d, L.8.3a)
6. Headline vote works on the projector.
7. Print shows rewrites and notes.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: switches and meters change without moving; no network requests.

## Open questions
- None for Cory.
