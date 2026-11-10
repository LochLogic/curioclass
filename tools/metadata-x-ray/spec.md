# Metadata X-Ray

## One idea
Three everyday records sit face up on the screen, a photo of a dog, a day's step count, and a "checked in to class" badge from a school app, all belonging to Jordan, a made-up eighth grader in a made-up town (labeled "illustration"), and when the child presses the X-ray button each card shows the fields hiding behind it, the time to the second, the place, and the device; then the child turns two dials: a precision dial moves the photo's location from 2 decimal places (about 1 km, "somewhere in the city") to 5 (about 1 m, "Jordan's front door"), and a frequency dial moves step data from daily totals to every minute, until a map and a timeline beside the cards show Jordan leaving home at 7:42 a.m., stopping at a corner store, and getting to school at 8:05; Jordan's cousin, Dee (made up), narrates what each turn now reveals; finally the child drags each detail to who should hold it (stay on the phone, the app maker, the school, the family, or delete) and sees what each holder could now work out; at the end the child sees that more precise and more frequent data answers questions nobody asked, and deciding who holds it matters as much as collecting it, so a student in grades 6 to 8 learns how precision, granularity and metadata shape what personal data reveals, and who should hold it.

## Not like
- data-defenders (5, spec): keeping data secure. Here what data reveals.
- secret-keeper (K, spec): what to share. Here metadata nobody sees.
- data-policy-council (Grades 9-12, spec): privacy law. Here one student's records.
- family-tech-vote (3, spec): a gadget's data card. Here precision and frequency dials.

## Who and how
- Grades 6-8, Computer Science, module "Data, Metadata and You". Standards: MS-DAT-DC-21, MS-DAT-DC-22, MS-DAT-IM-28 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Precision, granularity and metadata in personal data, and who should hold it").
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every field and card. Controls 48 px or more.
- Three records, two dials, a map and a timeline, twelve details to place with five holders. Extra: Guess the route (a partner guesses Jordan's route from one dial setting). tool.json `modes: ["X-ray", "Guess the route"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-DAT-DC-22 | X-ray each record; name its metadata | time, place, device | 2 |
| MS-DAT-DC-21 | Turn precision and frequency; say what each reveals | the map sharpening | 3 |
| MS-DAT-IM-28 | Place each detail with a holder; defend it | what each holder can work out | 4 |

## Screens and modes
Header (kit): title "Metadata X-Ray"; `X-ray`, `Guess the route`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** Three cards on a desk, an X-ray button, and Dee on a video tile. The welcome is queued (`welcomeAfter: true`): "Every record carries extra data. Tap X-ray to see it." First hint: "Tap X-ray."

**X-ray (focus: the cards).** At 1366x768 cards left, map and timeline right; at 680x425 the map and timeline are tabs. Each card flips to its fields; the child taps each field to name it (time, place, device, account).

**Dials.** Precision: 2, 3, 4, 5 decimal places, with the circle on the map shrinking from about 1 km to about 1 m. Frequency: daily, hourly, every 15 minutes, every minute, with the timeline filling in. After each turn the child picks what can now be worked out from a short list.

**Who holds it.** Twelve detail chips; five holder bins. Each drop shows what that holder could now work out ("The app maker knows when Jordan leaves home each school day.").

**Questions nobody asked (the aha).** Dee: "Nobody asked where Jordan lives. The data answered anyway."

**The end.** The dial settings the child chose, the holder bins and a reason for each. `Print` prints them.

**Guess the route (extra).** Partner play.

## Content
- Jordan, the town, the map and all records are made up; no real location is ever read and no device sensor is used.
- Precision figures use about 111 km per degree of latitude.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Dials can be turned any time; chips can move between bins until `Done`.
- Keyboard: Tab to X-ray, cards, fields, the two dials (arrows turn them), chips and bins; Enter flips or drops.
- With Motion off the map redraws without the zoom.

## Look
- Accent `--brand` #7a2a6a x-ray plum (header, the dials, buttons); gold #f4c542 (the field in focus, Jordan's dot); paper #f8eff6; ink #260a20; muted #5a4c57.
- Contrast (WCAG 2.1, computed): white on brand 8.87:1; brand on paper 7.89:1; ink on paper 16.28:1; muted on paper 7.16:1; ink on gold 11.26:1.
- Never color alone: the map circle shows its size in words; holders carry icons and names.
- Different from this batch (debugger amber, timeline navy, factory red-orange, test-kit green).

## Art
- People (illustrated): Dee and Jordan, labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Local FLUX (`scripts/localart.py`): the dog photo (1, 4:3), a phone, a watch and a school app badge (3, 1:1).
- Drawn in code: the made-up town map, the timeline, dials and bins.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Dee; `knowing-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.dial + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `xray`: "Tap X-ray."
- how `field`: "Tap a field to name it."
- how `dial`: "Turn a dial, then pick what it reveals."
- how `hold`: "Drag a detail to who should hold it."
- how `why`: "Pick a reason for this holder."
- event, whole, questions nobody asked.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: made-up records with metadata, coordinate rounding, time binning, map and timeline redraws, holder inferences.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fields | Tap through | Each field must be named. |
| Dials | Turn to the end | Each step asks what it now reveals. |
| Holders | Delete everything | Some details are needed (the school needs attendance); delete shows what breaks. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `xray`; `field`.
2. `dial`.
3. `hold`; `why`.
4. Questions nobody asked (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Photo files store time, location and device in metadata (EXIF) | CIPA DC-008, "Exchangeable image file format for digital still cameras (Exif)" | Federal Trade Commission, consumer guidance on photo location data | yes |
| Each decimal place of latitude is ten times more precise; 5 places is about 1 m | U.S. Geological Survey, "How much distance does a degree, minute and second cover?" | National Geodetic Survey, geodetic coordinate precision guidance | yes |
| A few location points over time can identify a person | de Montjoye and others (2013), "Unique in the Crowd", Scientific Reports | Federal Trade Commission (2024), actions on sale of sensitive location data | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s25, 2026-11-10): 2, 3, 4 and 5 decimal places are about 1,113, 111, 11 and 1.1 m of latitude; a week has 10,080 minutes; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 cards, map and timeline; at 680x425 map and timeline as tabs.
2. All three records are X-rayed and their fields named. (MS-DAT-DC-22)
3. Both dials are turned and each step's reveal picked. (MS-DAT-DC-21)
4. Twelve details are placed with a reason. (MS-DAT-IM-28)
5. No real location is read; all data is made up.
6. `Read` reads every field and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no zoom; no network requests.

## Open questions
None.
