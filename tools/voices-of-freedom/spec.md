# Voices of Freedom

## One idea
A quiet reading room holds real first-person sources from people who were enslaved, people who escaped, people who helped them, and people who fought slavery in law and print: Frederick Douglass's Narrative (1845), Harriet Jacobs's Incidents in the Life of a Slave Girl (1861), William Still's records of people who reached Philadelphia, women's antislavery petitions to Congress, and interviews with formerly enslaved people recorded in the 1930s; the child opens each source (a real portrait where one exists, a short excerpt, a plain-language note on when, where and who), answers a reflection card about what shaped the speaker's view (their situation, faith, the law, the risk they faced), links each source to events on a timeline strip (the Fugitive Slave Act, Dred Scott, John Brown's raid, secession), then builds a means-of-change wall (escape, testimony, petitions, the press, armed resistance, the Underground Railroad) compared with how people press for change today, and a chain of causes toward the Civil War; there are no points, timers or game mechanics, so an eighth grader learns what shaped people's perspectives, the causes and effects of resistance and growing division, and how means of changing society then compare with now.

## Not like
- remembrance-archive (10, concept): the family's Holocaust sources. Here sources on American slavery.
- reconstruction-amendments (8, spec): after the war. Here before it.
- expansion-map (8, spec): territory and removal on a map. Here voices in a reading room.
- who-gets-to-vote (8, spec): voices about voting. Here voices about freedom itself.

## Who and how
- Grade 8, Social Studies (History and Civics), module "Slavery and Sectionalism". Standards: D2.His.4.6-8 (analyze multiple factors that influenced the perspectives of people during different historical eras), D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past), D2.Civ.14.6-8 (compare historical and contemporary means of changing societies, and promoting the common good).
- Format: explorer. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every note. Controls 44 px or more.
- Ten sources on four shelves, reflection cards, the timeline strip, the means-of-change wall, the causes chain. Extra: Teacher notes (discussion prompts and context for each source, printable). tool.json `modes: ["Reading room", "Teacher notes"]`, `minutes: "35-45"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.4.6-8 | Answer each source's reflection card (what shaped this view: situation, faith, law, risk) | the reflection card with the child's picks and one line | 2 |
| D2.His.14.6-8 | Link sources to events on the strip, then build a causes chain toward secession | the timeline strip; the chain with because lines | 3, 5 |
| D2.Civ.14.6-8 | Place each means of change on the wall and pair it with a present-day means | the means-of-change wall, then and now | 4 |

## Screens and modes
Header (kit): title "Voices of Freedom"; `Reading room`, `Teacher notes`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A calm reading room: a long table, a lamp, four shelves labeled "People who were enslaved," "People who escaped," "People who helped," "People who fought it in law and print." A timeline strip from 1830 to 1861 runs along the wall. No score, no clock. The welcome is queued (`welcomeAfter: true`): "These are real words from people who lived through slavery and fought it. Take your time. Pick a shelf and open a source." First hint: "Tap a shelf."

**The sources (focus: the open source).** At 1366x768 the source fills the center with the reflection card at the right; at 680x425 the card is a sheet. Each source shows a real portrait where one exists, an excerpt of a few sentences chosen with care, and a plain note.
- People who were enslaved: two interviews from the 1930s Federal Writers' Project (Library of Congress, "Born in Slavery"), with a note that most interviewers were white, that some speakers may not have spoken freely, and that the interviewers' spelling of speech is their choice, not the speaker's; excerpts chosen without slurs.
- People who escaped: Frederick Douglass, Narrative (1845), on learning to read; Harriet Jacobs, Incidents (1861), on hiding for seven years in a tiny space before escaping; Harriet Tubman, as told to Sarah Bradford (1869), with a note that it is told through another writer.
- People who helped: William Still's records (kept in the 1850s, published 1872) of people arriving in Philadelphia; a Quaker family's station account.
- People who fought it in law and print: a women's antislavery petition to Congress (1830s), with a note on the "gag rule" that blocked such petitions from 1836 to 1844; William Lloyd Garrison's The Liberator (1831); Douglass's North Star (1847).
- Content notes appear before sources that describe violence; excerpts avoid graphic detail and slurs.

**Reflection cards (D2.His.4.6-8).** For each source: "What shaped this person's view?" Pick from situation, faith, law, risk, family, place; then one line in the child's words. A note after each shows what historians say about that source's perspective.

**The timeline strip (D2.His.14.6-8).** Events: Nat Turner's revolt (1831) and the harsher laws after it; the gag rule (1836); the Fugitive Slave Act (1850), which forced free states to help return people who escaped; Uncle Tom's Cabin (1852); Dred Scott (1857), ruling that Black Americans could not be citizens; John Brown's raid on Harpers Ferry (1859); Lincoln's election (1860); South Carolina's secession (December 1860), whose declaration named the defense of slavery. The child links each source to the events it speaks to.

**The means-of-change wall (D2.Civ.14.6-8).** Six means: escape; testimony (narratives and speeches); petitions; the press; armed resistance (Turner, Brown); the Underground Railroad network. For each the child picks a present-day means it is like (testimony and memoir today; petitions to Congress; independent journalism; organized networks of mutual aid; lawsuits) or marks it "no peaceful match" (armed resistance), with a note explaining why historians still debate it.

**The causes chain (the aha).** The child builds a chain toward secession from the strip's events with because lines (the Fugitive Slave Act made Northerners face slavery directly, so more opposed it; Dred Scott, so...). Narrator: "These voices didn't only describe slavery. They helped change how a nation saw it."

**The end.** The reflection cards, the strip, the wall and the chain. `Print` prints them.

**Teacher notes (extra).** Context, discussion prompts and handling guidance for each source, printable.

## Content
- Ten real sources with portraits, excerpts and plain notes; reflection cards; eight timeline events; six means with present-day pairings; chain tiles; teacher notes.
- Every source, excerpt and event is real, with Library of Congress or publisher references; excerpts are short and chosen to avoid slurs and graphic detail.
- No points, timers, scores or game mechanics.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Sources open in any order; the wall and chain open after six sources are read.
- Reflection answers are not graded right or wrong; the historians' note follows each.
- Keyboard: Tab to shelves, sources, cards, strip events, wall slots and chain tiles; Enter to open, pick and place.
- With Motion off nothing fades or slides.

## Look
- Accent `--brand` #4a3d5c dusk violet (header, shelves, the strip); gold #f4c542 (the open source's frame, a linked event); paper #f5f3f8; ink #151020; muted #57536a.
- Contrast (WCAG 2.1, computed): white on brand 9.94:1; brand on paper 9.02:1; ink on paper 16.91:1; muted on paper 6.69:1; ink on gold 11.46:1.
- Never color alone: shelves carry labels; links on the strip carry lines and names.
- Different from this batch (map slate, claret, ballot green, prairie rust). Calm and plain, with lots of space.

## Art
- Public domain portraits and pages (Library of Congress and National Portrait Gallery, ids checked at build): Frederick Douglass (1840s daguerreotype); Harriet Jacobs (1894 photograph); Harriet Tubman (about 1868 to 1869 photograph); William Still; title pages of the Narrative, Incidents, The Liberator and the North Star; a women's petition (National Archives); portraits of two Federal Writers' Project interviewees from the collection. Each with credit.
- Real faces only; no illustrated stand-ins for real people.
- Local FLUX (`scripts/localart.py`): the reading room (1, 16:9).
About 13 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the plain notes and hints; `wise-mentor` as the reader of excerpts, introduced each time as "reading the words of" the person, never playing them. `Curio.voice` with `scope: () => state.mode + ':' + state.source + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each plain note.
- event, whole, each excerpt.
- how `reflect`: "Pick what shaped this person's view, then write one line."
- how `link`: "Link this source to an event on the strip."
- how `wall`: "Place each way of seeking change and pair it with one today."
- how `chain`: "Build a chain of causes toward secession."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
primary-sources (no engine or family doc on main yet). This tool keeps its source data (id, shelf, person, date, place, excerpt, plain note, portrait credit, content note, linked events) as plain data in one marked block, `/* PRIMARY-SOURCES DATA: begin */ ... /* end */`, so a family engine can take it later. Tool-only code: the reading room, reflection cards, the strip, the wall, the chain.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reflection | Skip the line | The card needs a pick and a line before the source closes. |
| Strip | Link every source to every event | Links check that the source speaks to the event (dates and content). |
| Chain | Link events in any order | Each link checks dates and needs a because. |
This tool has no score; the checks keep the work honest without making it a game.

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Plain note (whole), waits; excerpt (whole).
2. `reflect`; `link`.
3. `wall`.
4. `chain`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.4.6-8, D2.His.14.6-8 and D2.Civ.14.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Douglass's Narrative (1845) and the North Star (1847) | Library of Congress, Frederick Douglass Papers | Documenting the American South (UNC), Narrative text | yes |
| Jacobs's Incidents (1861), hiding seven years | Documenting the American South (UNC), Incidents text | Yellin, "Harriet Jacobs: A Life" (Basic Civitas, 2004) | yes |
| William Still's records, published 1872 | Library of Congress, "The Underground Rail Road" | Pennsylvania Abolition Society and Historical Society of Pennsylvania, Still journal | yes |
| The Federal Writers' Project interviews (1936 to 1938) and their limits | Library of Congress, "Born in Slavery" collection and its essay on limitations | National Archives, WPA records | yes |
| Women's antislavery petitions and the gag rule (1836 to 1844) | National Archives, "Petitions against slavery" | U.S. House of Representatives History, "The gag rule" | yes |
| Fugitive Slave Act (1850), Dred Scott (1857), Harpers Ferry (1859) | National Archives, milestone documents | Britannica entries for each | yes |
| South Carolina's secession declaration named the defense of slavery | Avalon Project (Yale Law School), "Declaration of the Immediate Causes" (1860) | National Park Service, "Secession" | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: slavery is the subject; excerpts are short, chosen to avoid slurs and graphic detail, with content notes before descriptions of violence; the 1930s interviews' dialect spellings are explained as the interviewers' choices; real faces only, and the excerpt voice never plays a real person. A fresh-agent read of every excerpt is needed before build.

Checks run (Python, scratchpad r16, 2026-11-09): timeline events in order (1831, 1836, 1850, 1852, 1857, 1859, 1860); the gag rule lasted 8 years; ten sources across four shelves with at least two each; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 source and card; at 680x425 sheet.
2. Each source's reflection card needs a pick and a line, followed by the historians' note. (D2.His.4.6-8)
3. Sources link to timeline events that check. (D2.His.14.6-8)
4. The means-of-change wall pairs each means with today. (D2.Civ.14.6-8)
5. The causes chain links events with because lines. (D2.His.14.6-8)
6. No score, timer or game mechanic appears anywhere.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: nothing fades or slides; no network requests.

## Open questions
- Sensitivity flag: slavery told through real first-person sources (default used: short excerpts without slurs or graphic detail, content notes, dialect spelling explained, real faces only, fresh-agent read of every excerpt before build).
