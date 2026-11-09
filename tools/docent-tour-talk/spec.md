# Docent Tour Talk

## One idea
The student prepares a two-minute museum tour of one real public-domain object (Hokusai's "Great Wave", a blue faience hippo from ancient Egypt, an 1842 friendship quilt, or a brass astrolabe from Iran): they pick a claim, order three stops with the key point first, choose one zoomed detail per stop and say what it clarifies, rehearse by recording each stop with a timer, a volume meter and a script that fades each take, then redo only the opening for a curator, a family and a group of second graders, so they learn that a talk is built in a clear order with media that clarify, and changes with its audience.

## Not like
- pitch-deck-studio (8, concept): persuasive slides. Here a spoken tour of one object.
- audience-shift-briefing (9, concept): a research briefing for three rooms. Here a middle school tour opening for three listeners.
- page-audio-screen (concept): comparing media versions of a story. Here making a talk with media.
- myth-museum (4, spec): reading objects for myths. Here presenting an object.
- book-group-table (6, spec): discussion. Here a prepared talk.

## Who and how
- Grades 6-8, ELA, module "Presenting Claims and Findings" (Speaking and Listening). Standards: SL.6.4, SL.6.5, SL.6.6, SL.7.4, SL.7.5, SL.7.6, SL.8.6.
- Driver: one student (tool.json `driver: "student"`). Every card is read on tap. The student's recordings play back on the device.
- Four objects; one tour each. tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]` (grade 7 and 8 add the key-point-first check and formal-English notes), `minutes: "30-45"`, `grades_label: "Grades 6-8"`.
- Recording uses the microphone only after the student taps `Record`; footer and the record panel: "Your recordings stay on this device. Nothing is uploaded." No speech recognition; recordings are kept in this browser until `Clear my recordings`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.6.4, SL.7.4 | Pick a claim and order three stops; at grade 7 the key point goes first in each stop | the tour strip with three stops | 2 |
| SL.6.5, SL.7.5 | Choose one zoomed detail per stop and pick what it clarifies | the detail card with its "this shows" line | 3 |
| SL.6.4 (eye contact, volume, pronunciation) | Rehearse with a stop timer, a volume meter and a fading script; mark a self-check rubric after playback | the meter, timer and rubric | 4 |
| SL.6.6, SL.7.6, SL.8.6 | Rewrite and record the opening for a curator (formal English), a family (a story) and second graders (short sentences and a question) | three openings side by side | 5 |

## Screens and modes
Header (kit): title "Docent Tour Talk"; `Gallery`, `Plan`, `Rehearse`, `Audiences`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A quiet gallery with four lit cases and Ms. Halvorsen, the head docent with a name badge and a clipboard. First hint: "Tap an object to read its fact cards." The first tap reads the object's name; the welcome is queued after it (`welcomeAfter: true`).

**Gallery.** Four objects, each with three fact cards (written for Curio Class from the museum's own record) and the image with zoomable details (4 to 6 per object, set in data).

**Plan.** Claim chips (three per object, each one the facts can support, for example "This hippo shows how Egyptians saw the Nile as full of life") or a typed claim. Three stop slots; the student drags fact cards into stops and orders them. At grade 7 and 8, each stop's first line must be its key point (the student marks which line is the key point; the check is that it's first).

**Details.** For each stop, the student picks one zoomed detail and a "this shows" line from three; one of the three doesn't match the stop's point.

**Rehearse.** `Record` per stop (after the browser's microphone prompt; if it is refused, the tool says "You can practice aloud without recording" and the timer and fading script still work). A stop timer (target 30 to 45 seconds), a volume meter from the microphone's level (no words are recognized), and the script card, which fades by a third each take until it shows only the first words of each line. After playback, the student marks the rubric: clear order, key point first, looked up, loud enough, said the hard name right (each object has one: Katsushika Hokusai, faience, astrolabe, Qajar), with a tap-to-hear model of the name.

**Audiences.** Three audience cards: Curator (wants exact words and dates), Family (wants a story), Second graders (short sentences, one question for them). The student rewrites only the opening for each with a word-count guide (second graders: no sentence over 12 words; the tool counts) and a formal-English check for the curator (no slang from a small list; contractions flagged as a reminder). Three recordings play side by side.

At 1366x768 the object and plan fit side by side; at 680x425 the plan is a tab.

## Content
Objects (public domain; ids checked 2026-11-09):
- Katsushika Hokusai, "Under the Wave off Kanagawa" ("The Great Wave"), about 1830-32, woodblock print, from "Thirty-six Views of Mount Fuji"; The Met, object 45434.
- Hippopotamus ("William"), Egypt, Middle Kingdom, Dynasty 12, about 1961-1878 B.C., faience, about 20 cm long; The Met, object 544227.
- Friendship Quilt, 1842, Mount Holly (New Jersey), 85 squares inscribed with names and verses; Art Institute of Chicago, object 54071.
- Astrolabe, Iran, Qajar dynasty, late 18th century with later additions, brass, about 25 cm tall; Art Institute of Chicago, object 90589.
- Fact cards: three per object, from the museum record and one more source each.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Recording starts only on `Record` and stops on `Stop` or at 90 seconds.
- Takes are kept per stop; the latest take plays unless the student picks another.
- With Motion off the gallery doesn't pan and the script fades in steps.

## Look
- Accent `--brand` #7a2048 museum burgundy (header, wall color, stop slots); gold #f4c542 (the case lights, the meter's target band); paper #fbf3f6; ink #260a16; muted #63505a. Scene: a hushed gallery with burgundy walls.
- Contrast (WCAG 2.1, computed): white on brand 9.87:1; brand on paper 9.05:1; ink on paper 16.93:1; muted on paper 6.81:1; ink on gold 11.35:1.
- Never color alone: the meter shows "too quiet", "good" and "too loud" in words; rubric marks are words.
- Different from this batch (sky blue, storm violet, pumpkin, granite green).

## Art
- Public domain: the four objects' images from the museums' open-access records (downloaded at the Art step and stored locally; the Art step views each image and swaps any object whose image shows nudity or violence).
- People art goes to Gemini: Ms. Halvorsen (a white woman in her sixties, silver bob, name badge), 4 poses; the three audiences (a curator, a Black man in his forties in a tweed jacket; a family of a grandmother, a dad and two kids; a group of second graders on a carpet with their teacher); "illustrated museum scene <description>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): gallery room (1); no people.
About 12 images. Drawn in code: tour strip, meter, timer, script card.

## Voice
Bank voice `upbeat-guide` as Ms. Halvorsen (unique in this batch); the audience reactions are read by `wise-mentor` (curator), `friendly-dad` (family) and `hero-coach` (the second graders' teacher), each unique in this batch. `Curio.voice` with `scope: () => state.object + ':' + state.view + ':' + state.stop`, `welcomeAfter: true`.
- how `welcome`: "Every good tour has a point, three stops and one detail that makes people lean in. Pick your object."
- event, whole, `card`: the tapped fact card.
- how `orderHow`: "Drag your facts into three stops. Put the key point first."
- event `detail`: "This detail shows {the lotus flowers painted on its body}."
- how `recordHow`: "Tap Record when you're ready. Look up from the script when you can."
- event `name`: the object's hard name, said slowly.
- event `audience`: the audience's reaction ("I'd love the exact date." / "Tell us a story!" / "Can we ask a question?").
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: tour strip, detail zoom, recorder with level meter and timer, fading script, audience rewrite checks.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Plan | Drop facts in any order | Grade 7 and 8 check that the key point is first in each stop. |
| Details | Pick any "this shows" line | One of three doesn't match the stop's point and says why. |
| Second graders | Reuse the curator's opening | The 12-word sentence check and the question check both apply. |
| Rubric | Mark everything | The rubric is a self-check, not a score; the recordings sit side by side for the student to hear. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap an object: its name, `welcome` (queued, first time).
2. Cards: `card` (whole). Plan: `orderHow` (first time). Details: `detail`.
3. Rehearse: `recordHow` (first time); `name` on tap.
4. Audiences: `audience` per card.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.6.4 to SL.8.6 wording | thecorestandards.org, Speaking and Listening Grades 6-8 | CCSS ELA 2010 PDF | yes |
| "The Great Wave" by Katsushika Hokusai, about 1830-32, woodblock print, from "Thirty-six Views of Mount Fuji"; public domain | The Met, object 45434 (checked 2026-11-09) | Library of Congress, "The Great Wave" print and Hokusai | yes |
| "William", faience hippopotamus, Egypt, Middle Kingdom, Dynasty 12, about 20 cm long; public domain | The Met, object 544227 (checked 2026-11-09) | The Met, Heilbrunn Timeline of Art History, Middle Kingdom faience | yes |
| Friendship Quilt, 1842, 85 inscribed squares, possibly a farewell gift; public domain | Art Institute of Chicago, object 54071 (checked 2026-11-09) | Smithsonian National Museum of American History, signature and friendship quilts | yes |
| An astrolabe is a brass instrument for measuring the height of the sun and stars to tell time and find positions; this one is Iranian, Qajar dynasty, late 18th century; public domain | Art Institute of Chicago, object 90589 (checked 2026-11-09) | Museum of the History of Science, Oxford, astrolabes | yes |
Backed twice: 5. Cut: 1 (an Athenian toy pitcher from the Art Institute; its picture shows unclothed toddlers, so the hippo replaced it).

Sensitivity note: the Great Wave and the astrolabe come from living cultures (Japan and Iran); both go to the fresh-agent review; the tool records audio only on tap and keeps it on the device.

Checks run (Python, scratchpad b16, 2026-11-09): all four object records report public domain with the dates above; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the object and plan fit; at 680x425 the plan is a tab.
2. The plan takes a claim and three ordered stops; grade 7 and 8 check key point first. (SL.6.4, SL.7.4)
3. Details take a "this shows" line, one mismatched. (SL.6.5, SL.7.5)
4. Rehearsal records per stop with a timer, meter, fading script and rubric; a refused microphone still allows practice. (SL.6.4)
5. Three audience openings are checked and play side by side. (SL.6.6, SL.7.6, SL.8.6)
6. Recordings stay on the device and `Clear my recordings` removes them.
7. Print shows the tour plan and openings.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no panning; no network requests.

## Open questions
- None for Cory.
