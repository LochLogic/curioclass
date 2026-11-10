# Muckraker Studio

## One idea
On a 1906 reporter's desk lie five case files, each tied to a real investigator (Upton Sinclair on the Chicago meatpacking plants, Lewis Hine on child labor in mills and mines, Ida Tarbell on Standard Oil, Ida B. Wells on lynching, Jacob Riis on New York tenements), and the student picks one, reads its notes, figures and photographs, chooses the strongest evidence, and writes a headline, lede and three short paragraphs into a 1906 magazine layout while a made-up editor checks that every claim has a source; after publishing, a reform timeline shows what really followed and who acted (the Meat Inspection Act of 1906, child labor laws struck down and finally passed in 1938, the Standard Oil breakup of 1911, anti-lynching bills blocked in the Senate for a century until 2022, the New York tenement law of 1901), sorting each step by government, citizens' groups and companies; at the end a then-and-now panel shows how each investigator was seen in their own time and how historians see them now (Riis's prejudices in his own book, Wells's recognition delayed for decades, Tarbell's father's ruin by Standard Oil), and the student writes why their significance shifted, so an eleventh grader learns how the significance of people's actions changes with time and context, compares means of changing society, and critiques the relationships among government, civil society and markets.

## Not like
- colonial-newsroom (8, spec): slanting headlines. Here a sourced expose.
- behind-the-podcast (11, spec): critiquing a secondary work. Here writing from primary evidence.
- baron-or-builder (11, spec): judging business leaders. Here exposing their effects.
- movement-strategy-room (11, spec): choosing protest tactics. Here reporting as a tactic.

## Who and how
- Grade 11, Social Studies (U.S. History and Civics), module "The Progressive Era". Standards: D2.His.3.9-12 (use questions generated about individuals and groups to assess how the significance of their actions changes over time and is shaped by the historical context), D2.Civ.14.9-12 (analyze historical, contemporary, and emerging means of changing societies, promoting the common good, and protecting rights), D2.Civ.6.9-12 (critique relationships among governments, civil societies, and economic markets).
- Format: studio. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Five case files, the writing studio with the editor's source check, the reform timeline, the then-and-now panel, the note. Extra: Class issue (each student's story becomes a page in one printed class magazine). tool.json `modes: ["Studio", "Class issue"]`, `minutes: "40-50"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.14.9-12 | Write the expose from sourced evidence, then compare it with other means of change on the timeline | the studio; the timeline sorted by means (exposes, lawsuits, laws, boycotts, campaigns) | 2, 3 |
| D2.Civ.6.9-12 | Sort each reform step by who acted: government, citizens' groups or companies | the timeline's three lanes | 3 |
| D2.His.3.9-12 | Write a question about the investigator, read the then-and-now panel, and write why their significance shifted | the then-and-now panel with dated views | 4 |

## Screens and modes
Header (kit): title "Muckraker Studio"; `Studio`, `Class issue`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A reporter's desk in 1906 with a typewriter, an inkwell and five manila case files labeled Meat, Mills, Oil, Lynching, Tenements. A sign on the wall: "Every claim needs a source. The Editor." The welcome is queued (`welcomeAfter: true`): "Five stories the powerful didn't want told. Pick one file and find the evidence. Tap a case file." First hint: "Tap a case file."

**Case files (focus: the evidence).** At 1366x768 the file fills the left with the studio right; at 680x425 the studio is a sheet. Each file holds six to eight real items (notes, figures, photographs, short excerpts under 15 words):
- Meat: Sinclair's "The Jungle" (book 1906) on the Chicago yards; the federal Neill-Reynolds report (1906) confirming filthy conditions.
- Mills: Hine's photographs for the National Child Labor Committee (from 1908) with his captions naming ages and hours; the 1900 census count of about 1.75 million working children aged 10 to 15.
- Oil: Tarbell's series in McClure's (1902 to 1904) built from court records and rebate contracts.
- Lynching: Wells's "Southern Horrors" (1892) and "A Red Record" (1895), built from newspaper reports and her own investigation after three friends were murdered in Memphis in 1892; her counts of the stated charges; no photographs of violence are used.
- Tenements: Riis's "How the Other Half Lives" (1890) with flash photographs of crowded rooms; city tenement statistics.

**The studio (D2.Civ.14.9-12).** The student writes a headline, a lede and three paragraphs into a 1906 magazine layout and picks one image. Each claim is linked to an item by dragging it onto the sentence; the editor (made up, labeled) flags any sentence with no source: "Where's your proof?" A note on screen: "Your draft stays on this device."

**The reform timeline (D2.Civ.14.9-12, D2.Civ.6.9-12).** After publishing, the real response appears in three lanes, government, citizens' groups and companies:
- Meat: the Meat Inspection Act and the Pure Food and Drug Act (June 30, 1906); packers pushed for federal stamps to win back buyers abroad.
- Mills: state laws; the federal Keating-Owen Act (1916) struck down in 1918; the Fair Labor Standards Act (1938).
- Oil: the antitrust suit and the Supreme Court breakup (1911).
- Lynching: Wells's speaking tours and the NAACP's campaigns; the Dyer bill passed the House in 1922 and died in the Senate; nearly 200 bills failed until the Emmett Till Antilynching Act (2022).
- Tenements: the New York Tenement House Act (1901).
- The student sorts each step into a lane and marks which means worked (an expose, a lawsuit, a law, a boycott, a campaign).

**Then and now (the aha, D2.His.3.9-12).** The student writes one question about their investigator, then reads dated views: Roosevelt's "muck-rake" speech (April 1906) praising and scolding them; Riis praised in his time, now also read for the ethnic stereotypes in his own book; Wells pushed aside by some reform leaders, then honored with a special Pulitzer citation in 2020; Tarbell's family ruined by Standard Oil's tactics, a fact some critics raised. The note: "In their time ___ was seen as ___. Now ___ because ___." Narrator: "What we value changes. So does who we remember."

**The end.** The published page, the sorted timeline and the note. `Print` prints them.

**Class issue (extra).** Each student's page joins a printed class magazine with a cover and contents.

## Content
- Five case files with six to eight real, credited items each; the studio with the source-link check; the reform timeline with three lanes; then-and-now views with dates; the note.
- The editor is made up and labeled; every investigator, item, law and date is real and sourced.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Publish opens only when every sentence in the story has a source.
- Drafts stay on the device and the screen says so.
- Keyboard: Tab to files, items, the studio fields, the timeline lanes and the panel; Enter to link, publish and sort.
- With Motion off the page prints without the press animation.

## Look
- Accent `--brand` #9a1b1b press red (header, the masthead, the editor's flags); gold #f4c542 (the linked item, a sorted step); paper #fbf3f1; ink #2b0a0a; muted #62524f.
- Contrast (WCAG 2.1, computed): white on brand 8.25:1; brand on paper 7.54:1; ink on paper 16.68:1; muted on paper 6.76:1; ink on gold 11.22:1.
- Never color alone: editor flags carry words and an icon; lanes carry names.
- Different from this batch (gilded bronze, archive teal, decade violet, suburb green).

## Art
- Public domain (Library of Congress, ids checked at build): Lewis Hine's National Child Labor Committee photographs; Jacob Riis's tenement photographs; portraits of Sinclair, Tarbell, Wells and Riis; the title pages of the books and McClure's. Each with credit.
- No photographs of lynching or of victims, ever.
- Local FLUX (`scripts/localart.py`): the reporter's desk (1, 16:9).
- Drawn in code: the 1906 magazine layout.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the made-up editor; `bright-teacher` as the narrator, item reader and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.file + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each case item.
- how `write`: "Write a headline, a lede and three paragraphs."
- how `link`: "Drag an item onto each claim."
- event, whole, each editor flag.
- how `sort`: "Sort each step: government, citizens or companies."
- how `ask`: "Write one question about your investigator."
- how `note`: "Write how their reputation changed."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the case files, the studio with source links, the editor's check, the timeline lanes, the then-and-now panel.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sources | Link one item to every sentence | The editor flags an item used for a claim it doesn't support. |
| Lanes | Put everything under government | Each step checks against who acted. |
| Note | Repeat the then view | It needs a then, a now and a because. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Case item (whole), waits.
2. `write`; `link`; editor flag (whole).
3. `sort`.
4. `ask`; `note`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.3.9-12, D2.Civ.14.9-12 and D2.Civ.6.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| "The Jungle" (1906); the Neill-Reynolds report; both acts signed June 30, 1906 | Library of Congress, "Pure Food and Drug Act" | U.S. Food and Drug Administration history | yes |
| Hine's NCLC photographs; about 1.75 million working children 10 to 15 in 1900 | Library of Congress, National Child Labor Committee Collection | U.S. Department of Labor, history of child labor | yes |
| Keating-Owen (1916), struck down 1918; the FLSA (1938) | Hammer v. Dagenhart, 247 U.S. 251 (1918) | U.S. Department of Labor, "Fair Labor Standards Act" | yes |
| Tarbell's McClure's series (1902 to 1904); the 1911 breakup | Allegheny College, Ida M. Tarbell Collection | Standard Oil Co. of New Jersey v. United States, 221 U.S. 1 (1911) | yes |
| Wells's pamphlets (1892, 1895) and the Memphis murders of 1892 | Library of Congress, "Southern Horrors" (digitized) | Giddings, "Ida: A Sword Among Lions" (Amistad, 2008) | yes |
| The Dyer bill (1922); the Emmett Till Antilynching Act (2022) | U.S. House of Representatives, History, Art and Archives | Congress.gov, H.R. 55 (117th Congress) | yes |
| Wells's 2020 Pulitzer special citation | The Pulitzer Prizes, 2020 special citation | National Museum of African American History and Culture | yes |
| Riis's book (1890), its stereotypes, and the 1901 Tenement House Act | Museum of the City of New York, Riis collection | Yochelson and Czitrom, "Rediscovering Jacob Riis" (New Press, 2007) | yes |
| Roosevelt's "muck-rake" speech, April 1906 | Theodore Roosevelt Center, Dickinson State University | Library of Congress | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: the lynching file deals with racial terror. It uses Wells's own words and counts only, no images of violence or victims, and frames her as the investigator; Riis's stereotypes are named, not repeated at length. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r20, 2026-11-09): five files with six to eight items each; the Emmett Till Act came 130 years after "Southern Horrors"; Keating-Owen to the FLSA is 22 years; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 file and studio; at 680x425 sheet.
2. Publish opens only when every sentence links to a supporting item. (D2.Civ.14.9-12)
3. Every reform step is sorted into a lane and the means that worked are marked. (D2.Civ.14.9-12, D2.Civ.6.9-12)
4. The note names a then view, a now view and a reason. (D2.His.3.9-12)
5. The lynching file uses no images of violence or victims.
6. The screen states that drafts stay on the device.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no press animation; no network requests.

## Open questions
- Sensitivity flag: the lynching case file (default used: Wells's own words and counts only, no images of violence or victims, Wells framed as the investigator, drafts stay on the device, fresh-agent read before build).
