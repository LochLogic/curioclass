# Poetry Soundboard

## One idea
The student puts the first stanza of Poe's "The Raven" on a soundboard where rhyme, repetition, alliteration and meter each have a channel, mutes or changes one channel at a time and hears what the stanza loses (swap "rapping" and "tapping" for plain words and the knocking is gone), then rebuilds a shuffled Shakespeare sonnet to find where it turns and compares Juliet's "What's in a name?" speech with the same thoughts written as a conversation, so they learn that a poem's sounds and shape are part of what it says.

## Not like
- poem-drum (K-2, concept): clapping a poem's beat and finding rhymes. Here what each sound channel does to meaning, grade 7.
- double-meanings (8, spec, this batch): puns and irony. Here sound and form.
- pause-and-break (6-8, spec): punctuation as pauses. Here rhyme, repetition, alliteration and meter.
- simile-slam (5, spec): figurative comparisons. Here sound devices.
- script-read-through (3-5, spec): rehearsing a play part. Here hearing how a poem's sound makes meaning, then writing one.

## Who and how
- Grade 7, ELA, module "Sound and Form in Poetry" (Reading Literature). Standards: RL.7.4, RL.7.5.
- Driver: one student; class mode is a clap-the-meter reading (tool.json `driver: "student"`). Every line is read on tap.
- Texts, all public domain: "The Raven" by Edgar Allan Poe (1845), stanzas 1 and 2; Sonnet 29 ("When, in disgrace with fortune and men's eyes") and Sonnet 73 ("That time of year thou mayst in me behold") by William Shakespeare (1609); Juliet's speech from Romeo and Juliet, Act 2, Scene 2 ("O Romeo, Romeo, wherefore art thou Romeo?" through "Take all myself"). tool.json `modes: ["Soundboard", "Sonnet", "Speech", "My stanza", "Clap along"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.
- Records with the microphone in My stanza; the privacy line always shows: "Your recording stays on this device. Nothing is uploaded." No speech recognition. Nothing else is saved; `Print` prints the student's notes and stanza.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.7.4 (rhyme, repetition, alliteration) | Mute one channel at a time, hear both versions, and write what the stanza lost | the channel strips lit where each sound happens and the before-and-after lines | 2 |
| RL.7.4 (meter) | Break the meter by adding a syllable and hear the stumble | the beat marks over the line | 2 |
| RL.7.4 (connotation) | Compare swapped plain words with Poe's (rapping and tapping against knocking) | the swap list | 3 |
| RL.7.5 (sonnet form) | Rebuild a shuffled sonnet into three quatrains and a couplet and find the turn | the rebuilt sonnet with its turn marked | 4 |
| RL.7.5 (soliloquy or speech) | Compare Juliet's speech with the same thoughts written as a conversation; say what the speech form adds | the two versions side by side | 5 |
| RL.7.4 | Write a four-line stanza using two channels on purpose; record and tap its beats | the stanza with channels lit and the beats beside the meter aimed for | 6 |

## Screens and modes
Header (kit): title "Poetry Soundboard"; `Soundboard`, `Sonnet`, `Speech`, `My stanza`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A small recording studio with a mixing board of four channel strips (Rhyme, Repetition, Alliteration, Meter) under the stanza, and Mo, a studio engineer in headphones, at the board. First hint: "Tap Play to hear the stanza." The first tap plays the stanza; the welcome is queued after it (`welcomeAfter: true`).

**Soundboard.** The stanza with each channel lit where it happens: internal rhyme (dreary, weary; napping, tapping, rapping), end rhyme (lore, door, more), repetition ("tapping", "nothing more"), alliteration ("weak and weary", "nearly napping"), meter (eight stressed beats per line marked over the syllables). Muting a channel swaps in a keyed plain version (Rhyme muted: "While I nodded, nearly sleeping, suddenly there came a knocking"); the student plays both and writes what was lost, choosing from prompts (the pull, the knock, the spooky mood) or their own words. The Meter channel has a `Break it` switch that adds a syllable to one line so the stumble can be heard.

**Sonnet.** The fourteen lines of Sonnet 29 shuffled; the student rebuilds them into three quatrains and a couplet using the rhyme scheme (abab cdcd efef gg, shown as letters at line ends once placed) and the sense. Then they mark the turn, where the feeling changes ("Haply I think on thee"). Sonnet 73 is the harder second puzzle.

**Speech.** Juliet's speech beside a written-for-Curio-Class conversation with the same thoughts split between Juliet and the Nurse. The student answers what the speech form shows that the conversation hides (she argues with herself; she thinks no one is listening; the audience hears her private thoughts).

**My stanza.** Four lines on a topic the student picks, using two channels on purpose; the channel strips light where the student marks them. `Record` records a reading; playback shows a beat strip where the student taps the stresses they hear, beside the meter they aimed for.

**Clap along.** The stanza plays at a slow pace on the projector with beat marks, for the class to clap.

At 1366x768 the board and text fit; at 680x425 the strips stack under the text.

## Content
- "The Raven", Project Gutenberg #1065, stanzas 1 and 2, with keyed channel marks and muted versions written for Curio Class.
- Sonnets 29 and 73, Project Gutenberg #1041.
- Juliet's speech, Project Gutenberg #1513, with a conversation version written for Curio Class.
- Readings: the bank voice reads with the meter; each reading is checked by ear against the beat marks before release.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Channels can be muted in any combination.
- With Motion off the meters on the board don't bounce.

## Look
- Accent `--brand` #3b2f7a studio violet (header, board, strips); gold #f4c542 (lit sounds, the turn marker); paper #f4f3fb; ink #13102b; muted #56536b. Scene: a cozy recording studio.
- Contrast (WCAG 2.1, computed): white on brand 11.21:1; brand on paper 10.17:1; ink on paper 16.77:1; muted on paper 6.70:1; ink on gold 11.36:1.
- Never color alone: lit sounds are also underlined with the channel's name on hover and focus; muted strips say "muted".
- Different from this batch (gym brick red, field olive, chat teal, plum).

## Art
- Local FLUX (`scripts/localart.py`): recording studio (1); Mo the engineer (a robot with headphones, 4 poses), "A friendly small robot sound engineer with headphones <pose>, soft gouache, plain white background"; 1:1; cutout yes; a raven on a bust above a door in candlelight (1); a balcony at night with no faces shown (1).
About 7 images. Drawn in code: board, strips, beat marks.

## Voice
Bank voice `lively-host` as Mo (unique in this batch); poems and the speech are read by `smooth-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.channel`, `welcomeAfter: true`.
- how `welcome`: "Every sound in this stanza is doing a job. Mute one at a time, and hear what goes missing."
- event, whole, `stanza`: the stanza, as set on the board.
- event `muted`: "{Rhyme} muted. Play it and listen."
- event `stumble`: "Hear the stumble?"
- event `turn`: "Where does the feeling change?"
- event, whole, `speech`: the speech or conversation.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: channel marks and muted versions in data, line shuffle with rhyme letters, the turn marker, recording with a tapped beat strip.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Loss notes | Write the same thing for each channel | Each note needs a different channel word or keyed effect; the print shows them side by side. |
| Sonnet | Place lines by length | The rhyme letters and the keyed order check; the turn must be on the keyed line or within one of it with a reason. |
| My stanza | Mark channels that aren't there | Rhyme and repetition marks are checked against the words; alliteration needs matching first sounds. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Play: `stanza` (whole), `welcome` (queued, first time).
2. Channels: `muted`, then `stanza` on Play; `stumble` after a broken line plays.
3. Sonnet: `turn` when rebuilt.
4. Speech: `speech` (whole) per version.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.7.4 and RL.7.5 wording | thecorestandards.org, Reading Literature Grade 7 | CCSS ELA 2010 PDF | yes |
| "The Raven" (1845) text, public domain | Project Gutenberg eBook #1065 (checked 2026-11-09) | Poetry Foundation, "The Raven" | yes |
| Sonnets 29 and 73 text (1609), public domain; Sonnet 29's turn at "Haply I think on thee" | Project Gutenberg eBook #1041 (checked 2026-11-09) | Folger Shakespeare Library, Sonnets 29 and 73 | yes |
| Juliet's speech, Romeo and Juliet 2.2, public domain | Project Gutenberg eBook #1513 (checked 2026-11-09) | Folger Shakespeare Library, Romeo and Juliet 2.2 | yes |
| "The Raven" uses trochaic octameter with internal rhyme; a Shakespearean sonnet is three quatrains and a couplet, abab cdcd efef gg | Poetry Foundation, glossary (trochee, sonnet) and "The Raven" notes | Academy of American Poets, sonnet form | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b22, 2026-11-09): the Gutenberg files contain "Once upon a midnight dreary", "Haply I think on thee", "That time of year thou mayst in me behold" and "What's in a name"; the stanza's first line has 16 syllables (eight trochees); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 board and text fit; at 680x425 the strips stack.
2. Muting each channel plays a keyed version and takes a loss note; Break it plays the stumble. (RL.7.4)
3. Swapped words show beside Poe's. (RL.7.4)
4. Sonnets rebuild with rhyme letters and a marked turn. (RL.7.5)
5. The speech and conversation compare. (RL.7.5)
6. My stanza checks marked channels, records, and shows the tapped beats; the privacy line shows. (RL.7.4)
7. Clap along plays slowly with beat marks.
8. Print shows notes and the stanza.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the board's meters are still; no network requests.

## Open questions
- None for Cory.
