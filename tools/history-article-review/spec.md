# History Article Review

## One idea
The child is the reviewer for a kids' history magazine and gets three short article proofs about the American Revolution, each hiding one weakness (one claims everyone in Boston cheered the Tea Party but rests on a single memory written sixty years later; one tells how Saratoga won the French alliance with the steps out of order; one tells who fought for freedom but leaves out Black soldiers, Native nations and Loyalists); for each the child writes the main claim in one sentence, checks the argument (is there enough evidence for the claim?) and the explanation (do the steps follow in order?), asks whose voices are missing, and gives stars with a reason before the editor's own review appears, so a fifth grader learns to summarize a history article's claim and to judge its evidence and reasoning.

## Not like
- revolution-road (concept): the Revolution's events from three viewpoints. Here judging articles about them.
- source-scout (concept): judging raw sources. Here judging finished secondary articles.
- made-for-whom (4, spec): audience and purpose of primary sources. Here claim, evidence and order in secondary writing.
- headline-writer (ELA, concept): the main idea of a news story. Here a history article's central claim and its support.

## Who and how
- Grade 5, Social Studies (History and Inquiry), module "History Article Review". Standards: D2.His.17.3-5 (summarize the central claim in a secondary work of history), D4.4.3-5 (critique arguments), D4.5.3-5 (critique explanations).
- Format: the idea card changes it from explorer to studio, because the child writes a summary and a review rather than browsing.
- Driver: one child alone (tool.json `driver: "student"`). `Read` reads every article. Controls 44 px or more.
- Three articles, each with a review card; the editor's review after each. Extra: a fourth article with no planted weakness, to see whether reviewers invent problems. tool.json `modes: ["Review", "Fourth article"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.17.3-5 | Build the article's main claim in one sentence from tiles, then compare it to the headline | the Main claim line on the review card; a hint if it only repeats the headline or names a detail | 2 |
| D4.4.3-5 | Mark each piece of evidence, then judge: enough for the claim? fits the claim? | evidence marks in the article; the Argument line with a reason | 3 |
| D4.5.3-5 | Put the article's steps on a mini timeline and judge whether the explanation follows in order and links causes to effects | the step strip; the Explanation line with a reason | 4 |
| D4.4.3-5 (voices) | Ask "Whose voices are missing?" and pick from groups who were part of the story | the Voices line | 5 |

## Screens and modes
Header (kit): title "History Article Review"; `Review`, `Fourth article`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A reviewer's desk: three article proofs from "Time Travelers Magazine", a red pencil, and a blank review card (Main claim / Argument / Explanation / Voices / Stars). The welcome is queued (`welcomeAfter: true`): "You're the new reviewer for a kids' history magazine. Each article has one problem the editor wants you to find. Pick up the first article." First hint: "Tap the first article."

**Reviewing (focus: the article and the review card).** At 1366x768 the article sits left and the card right; at 680x425 the card opens as a sheet with `Card` and `Article` tabs.

Article 1, "Boston's Big Tea Party" (weakness: thin evidence). About 180 words: on December 16, 1773, colonists boarded three ships and dumped 342 chests of tea into Boston Harbor to protest the tea tax; the article claims "every person in Boston cheered" and its only evidence is one participant's memory, told when he was in his nineties, about sixty years later. The child's checks find: one source, written long after; and other evidence that not everyone cheered (Benjamin Franklin wrote that the tea should be paid for). Editor: "Good story, thin evidence. One old memory can't show what everyone thought."

Article 2, "How Saratoga Won a Friend" (weakness: steps out of order). The article says France joined the war first and then the Americans won at Saratoga because French troops helped. The child places four steps on the strip by their dates (the American victory at Saratoga, October 1777; news reaches France; the Treaty of Alliance, February 1778; French ships and soldiers arrive). The strip shows the article had the order backward. Editor: "The facts are mostly right, but the explanation runs backward. Saratoga came first and helped convince France."

Article 3, "Who Fought for Freedom?" (weakness: missing voices). The article tells only of white Patriot soldiers and says "Americans" all wanted independence. The child picks the missing groups from six: Black soldiers who fought for the Patriots (such as the 1st Rhode Island Regiment); enslaved people who escaped to the British, who promised freedom (Dunmore's Proclamation, 1775); Native nations, most of whom sided with the British to protect their lands while the Oneida and Tuscarora fought with the Patriots; Loyalists, colonists who stayed loyal to Britain; women who kept farms and businesses running; and one distractor that wasn't part of the story ("astronauts"). Editor: "Clear and well written, but it leaves out most of the people who lived through the war. A trustworthy article tells more of the story."

- Each review card: Main claim (tiles: a subject, a verb phrase, an ending; e.g. "The Boston Tea Party / was a protest / against the tea tax"); Argument (Enough evidence? Yes / Some / No, plus a reason tile); Explanation (In order? Yes / No, plus a reason tile); Voices (Missing? pick); Stars (1 to 5) with one reason from tiles.
- Main claim hints: a claim that only copies the headline: "That's the title. What is the article trying to show?"; a claim that names one detail: "That's one fact. What's the big idea all the facts support?"
- After the child's card, `See the editor's review` opens it beside the child's, with matches marked. No score; the narrator: "Your stars and the editor's don't have to match. Your reasons matter most."

**The end.** All three cards side by side. Narrator: "A well-written article can rest on thin evidence. A plain one can be the most trustworthy. Check the claim, the evidence, the order and the voices." `Print` prints the three review cards.

**Fourth article (extra).** "The Soldier Named Robert Shurtleff": Deborah Sampson disguised herself as a man and served in the Continental Army in 1782 and 1783; the article cites her enlistment, her later army pension and letters about her. No planted weakness. The child reviews it; if they mark a weakness, the editor's review shows the evidence that answers it.

## Content
- Three articles (about 180 words each) with one planted weakness each; question tiles; a four-step date strip; six voice choices; editor's reviews; the fourth article.
- "Time Travelers Magazine" and its editor are made up; every fact in the articles is real and sourced, except the planted mistakes, which the editor names.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `See the editor's review` shows only after the card is filled. Articles open in order.
- Keyboard: Tab through tiles and choices; Enter to place; arrow keys on the star row.
- With Motion off the review slides in without moving.

## Look
- Accent `--brand` #9b1c31 red pencil (header, the card frame, evidence marks); gold #f4c542 (a matched line with the editor, the selected tile); paper #fbf1f2; ink #2d0710; muted #64504f.
- Contrast (WCAG 2.1, computed): white on brand 8.06:1; brand on paper 7.28:1; ink on paper 16.50:1; muted on paper 6.77:1; ink on gold 11.23:1.
- Never color alone: evidence marks are underlined and numbered; matches carry a check.
- Different from this batch (timeline violet, trade harbor teal, ship's log wood, interest green).

## Art
- People art goes to Gemini with `people: true`: the editor (2 poses: reading, smiling; cutout yes).
- Local FLUX (`scripts/localart.py`): the reviewer's desk (1, 16:9); four magazine spreads' header pictures (4, 3:2, illustrated history scenes).
- Drawn in code: the article proofs, red pencil marks, the review card, the date strip, the side-by-side view.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `clear-teacher` as the narrator and article reader; `news-reader` as the editor. `Curio.voice` with `scope: () => state.mode + ':' + state.article + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each article.
- how `claim`: "Build the main claim with the tiles."
- event, whole, the claim hints.
- how `evidence`: "Underline each piece of evidence. Is it enough?"
- how `order`: "Put the steps in order by their dates."
- how `voices`: "Whose voices are missing? Pick them."
- how `stars`: "Give stars and pick a reason."
- event, whole, each editor's review (editor voice).
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: article proofs with markable evidence, the tile claim builder with hint checks, the date strip, the review card and the side-by-side view.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Main claim | Copy the headline | The headline hint plays and the card waits for a claim. |
| Argument | Say "enough" every time | The editor's review shows the gap; the narrator asks what a second source would add. |
| Order | Accept the article's order | The strip sorts by real dates and shows the mismatch. |
| Voices | Pick all six | "Astronauts" weren't part of the story; picking it plays a gentle "not in 1776". |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Article (whole), waits.
2. `claim`; hints (whole); `evidence`; `order`; `voices`; `stars`.
3. Editor's review (whole). After three: `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.17.3-5, D4.4.3-5 and D4.5.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Boston Tea Party, December 16, 1773, 342 chests; George Hewes's account was published in the 1830s | Massachusetts Historical Society, "The Boston Tea Party" | Boston Tea Party Ships and Museum, "Historic figures: George Hewes" | yes |
| Benjamin Franklin said the destroyed tea should be paid for | Founders Online (National Archives), Franklin to Thomas Cushing, February 1774 | Library of Congress, Franklin papers commentary | yes |
| Saratoga, October 1777, led to the Treaty of Alliance with France, February 1778 | National Park Service, Saratoga National Historical Park | U.S. Department of State, Office of the Historian, "French alliance" | yes |
| Black soldiers served in the 1st Rhode Island Regiment; Dunmore's Proclamation (1775) offered freedom to enslaved people who joined the British | Museum of the American Revolution, "Black founders" and Dunmore's Proclamation | Library of Congress, "African Americans in the Revolutionary period" | yes |
| Most Haudenosaunee nations sided with the British; the Oneida and Tuscarora sided with the Patriots | Oneida Indian Nation, "Revolutionary War" | National Park Service, Fort Stanwix National Monument | yes |
| Loyalists made up a sizable share of colonists | Museum of the American Revolution, "Loyalists" | Encyclopaedia Britannica, "Loyalist" | yes |
| Deborah Sampson served disguised as Robert Shurtleff and later received a pension | National Women's History Museum, "Deborah Sampson" | Massachusetts State House Art Collection / National Archives pension file | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the missing-voices article covers Native nations and enslaved people in the Revolution. Each group is named with what it did and why, from its own or a museum source; a fresh-agent read of the articles and voices list is needed before build.

Checks run (Python, scratchpad r8, 2026-11-09): the Saratoga strip's four steps sort by date to October 1777, late 1777, February 1778, 1778; 1773 plus about sixty years is the 1830s, matching Hewes's account; the voices list has five real groups and one distractor; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 article and card fit; at 680x425 the card is a sheet.
2. A claim that copies the headline or names one detail gets its hint. (D2.His.17.3-5)
3. Article 1's evidence check shows one late source. (D4.4.3-5)
4. Article 2's strip sorts by real dates and shows the backward order. (D4.5.3-5)
5. Article 3's voices pick takes the five real groups. (D4.4.3-5)
6. The editor's review shows only after the child's card.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
- Sensitivity flag: the missing-voices article names Black soldiers, enslaved people who escaped to the British, Native nations and Loyalists (default used: museum and nation sources for each, fresh-agent read before build).
