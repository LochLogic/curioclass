# Script Read-Through

## One idea
The student takes one part in a short play, "The Lighthouse Keeper's Cat", and rehearses alone with a scrolling prompter that marks pauses and stress words while a recorded cast reads the other parts; tapping a long word splits it into parts and plays it slowly; each take is recorded and played with the cast, and take 1 and take 3 play back to back with a wave that shows steadier pace and real pauses, so the student hears their own reading get smoother and more expressive; at grade 5 a register round has them read the same news as a radio announcer, a 1920s letter and a text-message kid.

## Not like
- echo-reader (1, spec): echoing a model passage line by line. Here taking a part in a scene with cast partners, at grades 3-5.
- planetarium-guide (3-5, spec): planning and giving an original talk. Here reading a written script with expression.
- syllable-surgeon (3, spec): a decoding clinic. Here splitting long words in place while reading.
- radio-hour-notes (3-5, spec): listening. Here performing.
- stay-in-character (3, spec): what a character would do. Here how a character sounds.

## Who and how
- Grades 3-5, ELA, module "Readers Theater and Fluency" (Foundational Skills). Standards: RF.3.4, RF.4.3, RF.4.4, RF.5.3, RF.5.4, L.5.3 (taken in from draft-car-wash).
- Driver: one student alone (tool.json `driver: "student"`); class mode lets a small group split the parts on one screen.
- Records with the microphone; the privacy line always shows: "Your recordings stay on this device and are gone when you close the page." No speech recognition: the student compares with the model reading.
- Two scripts by grade: grade 3 "The Lighthouse Keeper's Cat" (4 parts), grades 4-5 "The Night the Museum Lights Went Out" (4 parts, longer words); grade 5 adds the register round. tool.json `modes: ["Solo", "Group"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`. Without a microphone, the student can still rehearse with the prompter and model lines.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RF.3.4, RF.4.4, RF.5.4 (accuracy, rate, expression) | Read your part with the prompter at a chosen pace, recording takes | the prompter with pause marks and bold stress words | 2, 3 |
| RF.3.4c, RF.4.4c, RF.5.4c (self-correct from context) | The self-check card after each take asks about slips fixed from meaning | the card with three checks | 4 |
| RF.4.3, RF.5.3 | Tap a long word to split it into prefix, syllables, suffix and root and hear it slowly | the split word in place | 5 |
| RF.x.4 (rereading) | Take 1 and take 3 play back to back with a wave showing pauses and pace | two waves aligned | 6 |
| L.5.3 | Register round: read one piece of news three ways, then match the words and grammar that set them apart and where each fits | three cards with matched features | 7 |

## Screens and modes
Header (kit): title "Script Read-Through"; `Scripts`, `Register round` (grade 5); `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A small stage with a script on a music stand, four chairs for the cast, and Stage Manager Ruth, a raccoon with a clipboard and headset. First hint: "Tap a script to pick your part." The first tap opens the cast list; the welcome is queued after it (`welcomeAfter: true`).

**Cast list.** Four parts with pictures and line counts (data). Pick one; the cast plays the rest.

**Rehearse.** Focus: the prompter (a column 640 wide, 24 px type). Lines of other parts are shown in gray with the character's name; the student's lines are dark with marks: a slash for a pause, bold for stress words, a small up arrow at questions. Pace picker: Slow, Medium, Natural (the scroll speed per word, from data: 90, 110, 130 words per minute). `Hear model` plays the model reading of the student's next line. Tapping any long word (7 or more letters, marked with a dotted underline) shows its split (un|be|liev|a|ble) and plays the slow clip, then the whole word clip.

**Take.** `Record take`: the cast's lines play, and when the student's line comes up the prompter lights it and records until the student taps `Next` (or 12 seconds pass). The full take plays back with the cast. Takes are kept in memory (up to 5).

**Compare.** Pick any two takes; their waves (from the read-aloud engine) show side by side for one chosen line, aligned at the first sound, with quiet spans shaded. A readout says: "Take 3: 4 pauses at the marks (take 1: 1)". Pause matching: quiet spans of 300 ms or more near a pause mark (within 0.6 seconds of where the model reading pauses, mapped by line length).

**Self-check card** after each take: "Did I pause at the slashes? Did my voice go up at questions? Did I fix a slip by thinking about what the sentence means?" (yes, not yet).

**Register round (grade 5).** The same news (the town library is reopening after a flood) in three texts: a radio announcer's script, a 1920s letter from a great-grandmother (written for Curio Class in the style of the time), and a text message from a kid. The student reads each aloud (recorded), then matches feature cards (full sentences and formal words; old-fashioned words and long sentences; short forms and emoji words) to the text and picks where each fits (on air, a keepsake letter, a quick message to a friend). Every register is shown as right for its place; none is wrong.

At 1366x768 the prompter and controls fit; at 680x425 the controls fold under the prompter.

## Content
- "The Lighthouse Keeper's Cat" (original, 4 parts: Keeper Ann, Whiskers the cat, Gull, the Narrator; about 45 lines; long words: lighthouse, extraordinary, unbelievable, comfortable, disappeared, wonderful). Story: a storm puts out the lamp; Whiskers climbs the stairs to wake the keeper; the ship is warned.
- "The Night the Museum Lights Went Out" (original, 4 parts; about 60 lines; long words: archaeologist, mysterious, unbreakable, information, remarkable, electricity).
- Each long word: a split from data and slow and whole clips. Splits follow the syllable rules in syllable-surgeon's data.
- Register round: three texts of 60 to 90 words each, and 9 feature cards.

## Interactions in detail
- Every tap acts at once; a new line stops the old one (the take recording is the exception: a voice hint never plays during recording).
- Recording uses the browser's media recorder; audio stays in memory only.
- The prompter can be paused and dragged; tapping a line jumps there.
- Group mode: each part is assigned to a reader name typed on the cast list; one take records everyone in turn on one device.

## Look
- Accent `--brand` #7b2d5b curtain plum (header, curtains, part tags); gold #f4c542 (the lit line, stage lights); paper #fbf4f8; ink #250f1c; muted #625061. Scene: a small school stage with velvet curtains.
- Contrast (WCAG 2.1, computed): white on brand 8.87:1; brand on paper 8.19:1; ink on paper 16.67:1; muted on paper 6.83:1; ink on gold 11.09:1.
- Never color alone: the student's lines are dark and labeled with the part name; pause marks are slashes, stress is bold.
- Different from this batch (film-set red, cork brown, notecard green, blueprint blue).

## Art
Local FLUX (`scripts/localart.py`); the cast are animals and people shown small. The register round's three speakers are shown as objects (a microphone, an old letter, a phone), so no people art.
- stage (1); Ruth (4 poses); cast pictures (8: Keeper Ann as an old sea lion, Whiskers, Gull, the Narrator as an owl; museum cast as animals); script backdrops (2); register objects (3).
About 18 images. Drawn in code: prompter, marks, waves, cards.

## Voice
Stage Manager Ruth is `clear-teacher`. The cast are recorded from bank voices: `warm-teacher` (Keeper Ann), `playful-friend` (Whiskers), `gravel-ranger` (Gull), `big-sister` (Narrator), and the museum cast reuse those four. The register round: `news-reader` (announcer), `wise-mentor` (the letter), `casual-peer` (the text message). All unique in this batch. Model readings of each part's lines use the part's voice. `Curio.voice` with `scope: () => state.script + ':' + state.part + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Welcome to rehearsal! Pick a part. The cast will read the others, and you'll record your lines."
- how `rehearseHow`: "Read along as the prompter scrolls. Slashes mean pause. Bold words get extra punch."
- event `split`: "{Ex-tra-or-di-nar-y}. Now the whole word: {extraordinary}." (from clips)
- how `takeHow`: "Tap Record take. When your line lights up, read it, then tap Next."
- event `compare`: "Take {3} paused at {4} of the marks. Take {1} paused at {1}."
- how `registerHow`: "Same news, three ways. Read each one the way its speaker would."
- event `fits`: "Every way of talking fits somewhere."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
read-aloud (`kit/read-aloud.js`), described in full in tools/echo-reader/spec.md, exposed as `__tool.ra`. This tool uses: Passage (lines with a `part`), Highlight, Take, Wave (`ra.wave`, `ra.rests`, `ra.length`), Compare, Prompter (scrolls lines by part and plays cast clips for the other parts), Split (stored syllable and part data). Not `ra.pitch`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pause readout | Stay silent | Silence on a line ends the take at 12 seconds; the readout counts pauses only within a spoken line. |
| Pause readout | Pause everywhere | The readout counts only pauses near marks and shows the total pauses too. It is a mirror, not a score. |
| Self-check | Tap yes on all | It is self-reflection by design; the side-by-side waves make the honest answer audible. |
| Register match | Guess | 9 cards to 3 texts; wrong matches show the line that gives it away. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a script: cast list, `welcome` (queued, first time).
2. Rehearse: `rehearseHow` (first time); word taps: `split`.
3. Take: `takeHow` (first time); after compare: `compare`.
4. Register round: `registerHow`; matched: `fits`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RF.3.4 to RF.5.4, RF.4.3, RF.5.3, L.5.3 wording | thecorestandards.org, Foundational Skills and Language Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
| Reading fluency means accuracy, rate and expression (prosody); repeated reading of a passage builds it | Reading Rockets, fluency | National Reading Panel report (2000), fluency section | yes |
| Readers theater (reading scripts aloud, no costumes or sets needed) gives a reason for repeated reading | Reading Rockets, readers theater | ReadWriteThink, readers theater strategy guide | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): the 90, 110 and 130 words per minute prompter paces; the 300 ms pause and 0.6 second window.

Sensitivity note: the register round's three texts go to the fresh-agent review so no variety of English is mocked; each register is shown as right for its place.

Checks run (Python, scratchpad b11, 2026-11-09): every listed long word has 7 or more letters and a split whose pieces each have a vowel; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the prompter and controls fit; at 680x425 controls fold under.
2. The prompter scrolls at three paces with pause and stress marks. (RF.x.4)
3. Takes record with the cast and play back. (RF.x.4)
4. The self-check card appears after each take. (RF.x.4c)
5. Long words split and play slowly. (RF.4.3, RF.5.3)
6. Compare aligns two takes and reports pauses at marks.
7. The register round reads, matches features and places each register. (L.5.3)
8. The privacy line always shows; without a microphone the prompter still works.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the prompter steps line by line instead of scrolling; no network requests.

## Open questions
- None for Cory.
