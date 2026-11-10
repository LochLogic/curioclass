# Colonial Newsroom

## One idea
The child edits two Boston papers at once, made for this game: the Patriot "Liberty Post" and the Loyalist "Crown Courier," for two editions, the Stamp Act in 1765 and the shooting on King Street in March 1770; from the same tray of real evidence (the Stamp Act's text, a merchant's letter, the crowd at the Liberty Tree, Paul Revere's engraving, Captain Preston's account, trial testimony) they pick and order facts and write a headline and first lines for each paper, while a "who pays for this paper?" card explains each editor's interests; then they lay their pages beside real Boston pages and accounts, build a cause-and-effect strip from 1765 to 1770, and run a "missing voices" check (Crispus Attucks left no account; enslaved Bostonians and women appear mostly through others' words), so an eighth grader learns how people's interests shaped their view, how perspective shaped what the sources record, what the record leaves out, and the causes and effects that led to 1770.

## Not like
- headline-writer (3, spec): a news story's main idea. Here one event, two slants.
- revolution-road (5, spec): a timeline from three viewpoints. Here making the slanted pages.
- museum-label-writer (6, spec): a neutral explanation. Here two sides' pages.
- printing-press (7, spec): running a print shop. Here editing the words.

## Who and how
- Grade 8, Social Studies (History), module "Road to Revolution". Standards: D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past), D2.His.4.6-8 (analyze multiple factors that influenced the perspectives of people during different historical eras), D2.His.10.6-8 (detect possible limitations in the historical record based on evidence collected from different kinds of historical sources), D2.His.6.6-8 (analyze how people's perspectives influenced what information is available in the historical sources they created).
- Format: studio. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Two editions, two papers each, the compare wall, the cause strip, the missing-voices check. Extra: Side by side (prints both front pages for each edition on one sheet). tool.json `modes: ["Newsroom", "Side by side"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.4.6-8 | Read each editor's "who pays for this paper?" card, then pick and order facts for each paper | the interest cards; the two front pages taking shape | 2 |
| D2.His.6.6-8 | Compare their pages with real pages and accounts and mark what each side chose to include | the compare wall with highlights | 3 |
| D2.His.14.6-8 | Build the 1765 to 1770 strip linking causes and effects | the strip with links | 4 |
| D2.His.10.6-8 | Run the missing-voices check and name whose words the record lacks | the check card with three gaps | 5 |

## Screens and modes
Header (kit): title "Colonial Newsroom"; `Newsroom`, `Side by side`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A Boston print shop in 1765: two type cases, one labeled Liberty Post, one Crown Courier; two blank front pages; an evidence tray. The welcome is queued (`welcomeAfter: true`): "You edit two newspapers, and they don't agree. One sides with the Patriots, one with the Crown. Same news, two front pages. Open the evidence tray." First hint: "Tap the evidence tray."

**Edition one, the Stamp Act (1765) (focus: the tray and the pages).** At 1366x768 the tray is left, the two pages right; at 680x425 the pages are tabs.
- Evidence: the Stamp Act's terms (passed March 1765, a tax on printed paper from November 1); a merchant's letter worried about trade; a crowd hanging an effigy of the stamp distributor Andrew Oliver from the Liberty Tree (August 1765); the governor's report; Parliament's view that colonists should help pay for their defense after the French and Indian War.
- Interest cards: the Liberty Post's editor needs Patriot merchants who advertise and buy; the tax falls hard on printers; the Crown Courier's editor prints government notices and needs officials' favor.
- For each paper: pick four facts and order them, choose a headline from tiles and write one line, and pick words (a "mob" or "the people"; a "tax" or "a fair share").

**Edition two, King Street (March 5, 1770).** Evidence: troops in Boston since 1768; a crowd taunting a sentry at the Custom House; soldiers under Captain Thomas Preston fire; five men die, including Crispus Attucks, a sailor of African and Native descent; Paul Revere's engraving "The Bloody Massacre" (copied from Henry Pelham's) showing soldiers firing in a line on command; Preston's account that he never gave an order to fire; trial testimony, including from Andrew, an enslaved man who saw the crowd; John Adams defends the soldiers; Preston and six soldiers acquitted, two convicted of manslaughter. Same task: two pages.

**The compare wall (D2.His.6.6-8).** The child's pages beside real ones (a Boston Gazette page from 1770, Revere's engraving, Preston's printed account, a trial summary). The child highlights what each side's source put in and left out, then picks why ("the engraving shows an order to fire; Preston said there was none").

**The cause strip (D2.His.14.6-8).** Cards to link: war debt after 1763; the Stamp Act 1765; protests and boycotts; repeal 1766 and the Declaratory Act; the Townshend Acts 1767; troops arrive 1768; the shooting 1770. Each link gets a because.

**Missing voices (the aha, D2.His.10.6-8).** A check card asks whose words are missing from the record: Crispus Attucks left no account of his own; women ran boycotts but appear mostly in others' writing; enslaved Bostonians like Andrew appear mainly in court records. The child names three gaps and the kind of source that might fill each. Narrator: "Every page was made by someone with a side. And some people were never asked."

**The end.** Four front pages, the compare wall, the strip and the check. `Print` prints them.

**Side by side (extra).** Both papers' front pages for each edition on one sheet.

## Content
- Two editions with about eight evidence pieces each, two interest cards, headline and word-choice tiles, real pages for comparison, seven strip cards, three missing-voice gaps.
- The two papers and their editors are made up and labeled; the events, people, engraving, accounts and testimony are real, quoted only in short phrases.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each page needs four facts in order, a headline and one line before the edition closes.
- Word-choice tiles show both sides' words; picking one shows how it tilts the line.
- Keyboard: Tab to the tray, pieces, page slots, tiles, highlights and strip; Enter to pick and place.
- With Motion off pages don't slide in.

## Look
- Accent `--brand` #6b4423 colonial leather (header, type cases, the tray); gold #f4c542 (the fact in hand, a highlight); paper #f9f4ee; ink #24160a; muted #5e544b.
- Contrast (WCAG 2.1, computed): white on brand 8.48:1; brand on paper 7.75:1; ink on paper 16.08:1; muted on paper 6.75:1; ink on gold 10.81:1.
- Never color alone: the two papers carry their mastheads and icons (a liberty pole, a crown); highlights are underlined.
- Different from this batch (committee green, amendment indigo, mill brick, transit teal).

## Art
- Public domain (Library of Congress and the Massachusetts Historical Society, checked at build): Revere's "The Bloody Massacre" (1770); a Boston Gazette page (1770); a Stamp Act protest print or stamp (1765); Preston's printed case. Each with credit.
- Local FLUX (`scripts/localart.py`): the print shop (1, 16:9); King Street and the Custom House at night in snow, no figures firing (1, 16:9).
- People art goes to Gemini with `people: true`: the two editors (2; cutout yes).
- Drawn in code: the front pages, mastheads, tiles, compare wall, strip, check card.
About 8 images.

## Voice
Three bank voices, each unique in this batch: `knowing-guide` as the neutral narrator and hints; `upbeat-guide` as the Liberty Post's editor; `firm-captain` as the Crown Courier's editor. `Curio.voice` with `scope: () => state.mode + ':' + state.edition + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each evidence piece.
- event, whole, each interest card in its editor's voice.
- how `pick`: "Pick four facts for this page and put them in order."
- how `headline`: "Pick a headline and write the first line."
- how `compare`: "Highlight what this source put in."
- how `strip`: "Link each cause to its effect."
- how `voices`: "Name three voices missing from the record."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the evidence tray, two front-page builders, word-choice tiles, the compare wall, the cause strip, the missing-voices check.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pages | Make both papers the same | The edition won't close until each page's word choices match its editor's interests. |
| Compare | Highlight everything | Each highlight must match a real inclusion or omission. |
| Strip | Link in any order | Each link checks dates and a because. |
| Voices | Name the editors | Gaps must be people whose own words are missing. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Evidence (whole), each waits; interest cards (whole).
2. `pick`; `headline`, for each paper and edition.
3. `compare`; `strip`.
4. `voices`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.6-8, D2.His.4.6-8, D2.His.10.6-8 and D2.His.6.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Stamp Act (March 1765, effective November 1) and the Liberty Tree protest against Andrew Oliver (August 1765) | Library of Congress, "Stamp Act" primary documents | Massachusetts Historical Society, "The Stamp Act" | yes |
| Repeal in 1766 and the Declaratory Act; Townshend Acts 1767; troops arrive 1768 | Britannica, "Stamp Act," "Townshend Acts" | Library of Congress, "Creating the United States" | yes |
| The King Street shooting of March 5, 1770; five killed, including Crispus Attucks | Massachusetts Historical Society, "The Boston Massacre" | Revolutionary Spaces (Old State House), "The Boston Massacre" | yes |
| Revere's engraving copied Pelham's and showed an ordered volley | American Antiquarian Society, "The Bloody Massacre" | Library of Congress, Revere print | yes |
| Preston's account; John Adams's defense; acquittals and two manslaughter convictions | Massachusetts Historical Society | Britannica, "Boston Massacre" | yes |
| Andrew, an enslaved man, testified at the soldiers' trial | Massachusetts Historical Society, trial records | Revolutionary Spaces, "Andrew" | yes |
| Women organized boycotts; Attucks left no account of his own | Massachusetts Historical Society | Revolutionary Spaces | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r15, 2026-11-09): strip dates in order (1763, 1765, 1766, 1767, 1768, 1770); five killed on King Street; each page has four fact slots; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 tray and pages; at 680x425 tabs.
2. Each paper's page is built from facts, a headline and word choices that fit its editor. (D2.His.4.6-8)
3. The compare wall checks inclusions and omissions. (D2.His.6.6-8)
4. The strip links causes and effects in order. (D2.His.14.6-8)
5. The missing-voices check names three gaps. (D2.His.10.6-8)
6. Side by side prints both papers.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
None.
