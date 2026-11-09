# Time Machine Talk

## One idea
The student rides the town museum's time machine to the same made-up street, Front Street in the river town of Millbrook, in 1905, 1942 and today, explores each stop (streetcar or wagon, the general store, the school, jobs, clothes), and back at the museum reports what they saw in the past tense with sequence words and then-and-now frames (In 1905 people rode the streetcar, but now they drive or take the bus), and the report only saves when the verbs and time words are right, so they learn to recount and compare how a community changed over time.

## Not like
- then-what-happened (6-12, spec): comic narration for older students. Here grade 3 to 5 history language with real photos.
- cause-and-effect-rewind (3-5, spec): science causes, played backward. Here past and present, compared.
- mi-día (K-12, spec, this batch): Spanish present-tense routine. Here English past tense.
- opinion-builder (3-5, spec, this batch): opinions with reasons. Here reports of what was seen.
- math-explainer (3-5, spec, this batch): steps of a solution. Here events in a visit.

## Who and how
- Grades 3 to 5, English Language Development, module "Then and Now Language". Standards: WIDA ELD-SS (Standard 5, the language of social studies), Narrate and Inform key language uses (WIDA 2020).
- Driver: one student; class mode is "Pick an era", where the class chooses a fourth stop (1925 or 1965) and reports together on the projector (tool.json `driver: "student"`). Every label, choice and sentence is read on tap.
- Help setting: Lots (picture tiles, full frames, both verb forms shown), Some (word tiles with frames), Little (starters only, then typing). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Ride", "Exhibit", "Pick an era"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the exhibit with the student's captions.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| WIDA Narrate (recount in order, past tense) | Report the visit with first, then, after that, at the end, and past forms | the report strip; the machine's gauge | 3 |
| WIDA Narrate (irregular past forms) | Pick ride or rode, buy or bought, see or saw, there is or there were | the present twin shown beside the past form | 3 |
| WIDA Inform (compare then and now) | Fill "In 1905 ___, but now ___." frames | the then and now photos side by side | 4 |
| WIDA ELD-SS (community change: transport, work, school, stores) | Use the topic words from each stop | the topic tiles | 4 |

## Screens and modes
Header (kit): title "Time Machine Talk"; `Ride`, `Report`, `Exhibit`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** The Millbrook Town Museum: a brass and wood time machine with a dial (1905, 1942, Today), a big window showing Front Street today, and the museum guide, Mr. Henry Begay, a retired bus driver. "Go back. Look around. Then come back and tell me what was different." First hint: "Tap Mr. Begay to hear him." The first tap plays his line; the welcome is queued after it (`welcomeAfter: true`).

**Ride.** The dial turns and Front Street appears in that year as an illustrated scene, with a real photograph from that time in a museum case beside it, labeled "A real street in 1905" (Richmond, Virginia) or "A real store in 1942" (Mount Orab, Ohio). The student explores five hotspots per era: transport, a store, school, a job, clothes. Each stop offers one choice that changes the visit: ride the streetcar or walk to the general store (1905); go to the grocery or the movie house (1942); take the bus or bike to the library (today). The era narrator speaks each hotspot in the present, as if there ("People ride the streetcar to work.").

**Report.** Back at the museum the student writes the visit: sequence words (first, then, after that, at the end), past forms and there was or there were. Irregular verbs show their present twin above (ride / rode, buy / bought, see / saw, wear / wore, go / went). A wrong form makes the machine's gauge flicker and stall with a hint ("Ride is now. What's the past?"); the story never blocks, and the report saves when every verb and time word is right.

**Exhibit.** After all three stops, the museum wall shows the three eras side by side with the student's sentences as captions, plus their compare sentences under each pair: "In 1905 people rode the streetcar, but now most people drive or take the bus."

**Pick an era.** The class picks 1925 or 1965 and reports together on the projector.

At 1366x768 the scene and report fit; at 680x425 the report is below.

## Content
- Millbrook and its people are made up for Curio Class; each era's scene is drawn from what real towns had then, using the photographs as references.
- 1905: streetcars and wagons, a general store, a one-room school, a blacksmith, long dresses and hats. 1942: cars and a bus, a grocery store, a movie house, a factory job, saving and recycling for the war effort. Today: buses, bikes and cars, a supermarket and a library, many kinds of jobs.
- A short honest note in the 1905 and 1942 stops, read with the scene: "Back then, laws in many states kept Black people and white people apart on streetcars, in schools and in stores. That was unfair. People worked for many years to change those laws." Each era's people show the town's mix of people for that time.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The dial can go to any era any time; reports can be edited any time.
- With Motion off the dial jumps, the scene appears without the spin, and the gauge shows "stalled" in words without flickering.

## Look
- Accent `--brand` #4d3b7a museum violet (header, machine trim, frames); gold #f4c542 (the brass dial, a correct verb); paper #f5f3fa; ink #17112b; muted #58546b. Scene: a small-town history museum with a brass time machine.
- Contrast (WCAG 2.1, computed): white on brand 9.45:1; brand on paper 8.59:1; ink on paper 16.57:1; muted on paper 6.59:1; ink on gold 11.21:1.
- Never color alone: the gauge shows words (ready, stalled); verb forms are labeled now and past.
- Different from this batch (party magenta, clock blue, chalkboard green, library brown).

## Art
- Real photographs (Library of Congress, "No known restrictions on publication", checked 2026-11-09): "Main Street, Richmond, VA [Virginia street railroad scenes]", 1905 (loc.gov item 2013646446); "View of Main Street, Norfolk, Va.", 1906 (item 2013646447), as a second 1905 view; "[Grocery store, Mt. Orab, Ohio, Route 74]", 1942, John Vachon (item 2017877913). Credit line under each.
- People art goes to Gemini: Mr. Henry Begay (a Diné man in his seventies with a museum badge), 3 poses; townspeople for each era, a mixed crowd dressed for the time (about 12 cutouts); "illustrated <era> townsperson <pose>, soft gouache, plain white background"; 1:1; cutout yes. The era scenes go to the fresh-agent review.
- Local FLUX (`scripts/localart.py`): Front Street in 1905, 1942 and today from one viewpoint (3); 1925 and 1965 for class mode (2); the museum interior (1).
About 24 images. Drawn in code: dial, gauge, report strip, exhibit wall.

## Voice
Bank voice `knowing-guide` as Mr. Begay and the hint voice (unique in this batch); the era narrator and the student's report are read by `gravel-ranger` (unique in this batch). `Curio.voice` with `scope: () => state.era + ':' + state.spot`, `welcomeAfter: true`.
- how `welcome`: "Turn the dial and go back. Look at the street. Then come back and tell me what you saw."
- event `spot`: the hotspot in the present, as if there.
- event `note`: the honest note about unfair laws.
- event `stall`: the stall hint (for example "Ride is now. What's the past?").
- event, whole, `report`: the report read back.
- event, whole, `exhibit`: the captions read in order.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: the era scenes and hotspots, choices, the past-tense check with present twins, sequence and compare frames, the exhibit wall.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Past tense | Add -ed to every verb ("rided") | Irregular verbs are keyed; "rided" stalls with the present twin shown. |
| Time words | Leave out sequence words | The report needs first and at least two more time words. |
| Compare | Copy the same sentence for then and now | The now half must use a now-era tile that differs from the then half. |
| Explore | Skip straight to the report | The report's tiles come from hotspots visited. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Mr. Begay: his line, `welcome` (queued, first time).
2. Ride: `spot` per hotspot; `note` the first time the 1905 or 1942 street opens (waits).
3. Report: `stall` as it fires; `report` (whole) on save.
4. Exhibit: `exhibit` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| WIDA 2020: Standard 5 is the language of social studies; Narrate recounts events in order and Inform describes and compares | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| The three photographs, dates and rights statements | loc.gov item JSON for 2013646446, 2013646447, 2017877913 (checked 2026-11-09) | Library of Congress Prints and Photographs catalog records | yes |
| Jim Crow laws, allowed by Plessy v. Ferguson (1896), kept Black and white Americans apart in transportation, schools and other public places until the civil rights laws of the 1960s | Wikipedia, Jim Crow laws (checked 2026-11-09) | Wikipedia, Racial segregation in the United States (checked 2026-11-09); National Archives, Plessy v. Ferguson | yes |
| During World War II Americans saved and collected scrap metal, rubber and paper for the war effort | National Archives, "Powers of Persuasion" poster exhibit | Library of Congress, WWII home front posters | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: the unfair-laws note is short and honest for grades 3 to 5, and each era shows the town's mix of people; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b26, 2026-11-09): the three LOC item records give the titles, dates and "No known restrictions on publication"; both Wikipedia pages name Plessy v. Ferguson; every irregular verb in the tile bank has a keyed past form and its present twin; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and report fit; at 680x425 report below.
2. Each era opens with hotspots, a choice and its real photo with a credit line.
3. Reports check past forms and sequence words; wrong forms stall with the present twin. (WIDA Narrate)
4. Compare frames fill and the exhibit shows the three eras with captions. (WIDA Inform, ELD-SS)
5. The note about unfair laws plays in 1905 and 1942.
6. Help levels behave as in Who and how.
7. Pick an era and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: dial jumps, no spin, gauge in words; no network requests.

## Open questions
- Home-language support: this follows Cory's open question on home-language glossaries for the ELD tools (default used: English only, with pictures and read-aloud).
