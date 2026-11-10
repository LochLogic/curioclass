# Build a Government

## One idea
The student writes the constitution for Lunara, a made-up newly independent country with three regions, two languages and a river it shares with a neighbor, by filling eight articles from option cards (a presidential or parliamentary system, federal or unitary, one or two chambers, a bill of rights, a court that can strike down laws or not, emergency powers, how to amend, which treaties to join), each card naming real countries that use it (the United States, the United Kingdom, Germany, India, South Africa, Switzerland); then the constitution faces five crises, a contested election, a region that wants to leave, a leader who declares an emergency, a minority language banned in schools, and a drought that tests the shared river, and its own rules decide what happens, step by step; a theory shelf explains where each choice came from (Locke, Montesquieu, the Federalist Papers, the Haudenosaunee Confederacy's influence as historians debate it, Germany's lessons from 1933, India's river treaty with Pakistan); at the end a scorecard rates stability, rights, representation and peace with the neighbor and names the real country whose choices match, and the student writes what they would change, so a twelfth grader learns how constitutions, laws and treaties keep order at home and abroad, and evaluates political systems by the democratic principles and civic virtues they promote.

## Not like
- constitutional-convention (8, spec): 1787 delegates bargaining. Here a new country's design.
- checks-and-balances (12, spec): playing the U.S. branches. Here choosing the branches.
- supreme-court-simulator (12, spec): rights cases in one court. Here whether a court can strike laws at all.
- independence-timeline (10, spec): how colonies became nations. Here what a new nation writes next.

## Who and how
- Grade 12, Social Studies (Government), module "Foundations of Government". Standards: D2.Civ.3.9-12 (analyze the impact of constitutions, laws, treaties, and international agreements on the maintenance of national and international order), D2.Civ.8.9-12 (evaluate social and political systems in different contexts, times, and places, that promote civic virtues and enact democratic principles).
- Format: builder. Driver: one student alone, or rival designs facing the same crisis (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Eight articles with three or four options each, five crises, the theory shelf, the scorecard and the note. Extra: Rival designs (groups' constitutions face the same crisis side by side). tool.json `modes: ["Draft", "Rival designs"]`, `minutes: "40-50"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.3.9-12 | Run each crisis and trace how the constitution's rules and the river treaty keep or lose order | the crisis stepper with the article that decided each step | 2, 3 |
| D2.Civ.8.9-12 | Read the scorecard and the matching real country, then write what to change | the scorecard; the country match; the note | 4 |

## Screens and modes
Header (kit): title "Build a Government"; `Draft`, `Rival designs`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A map of Lunara (made up): a coastal region, a mountain region and a river valley; two languages, Sel and Varo, spoken in different regions; the river Tamsa flows on into the neighbor, Orrin. A blank constitution with eight empty articles. The welcome is queued (`welcomeAfter: true`): "Lunara became independent today. It needs rules that will hold when things go wrong. Tap Article 1." First hint: "Tap Article 1."

**Drafting (focus: the article).** At 1366x768 the constitution fills the left with option cards right; at 680x425 the cards are a sheet. Articles and sample options (each card names real users):
1. Executive: presidential (United States), parliamentary (United Kingdom, Germany, India), collective council (Switzerland's seven-member Federal Council).
2. Federal or unitary: federal (United States, Germany, India, Switzerland), unitary (United Kingdom before devolution, France).
3. Legislature: one or two chambers; how seats are filled.
4. Rights: a bill of rights, with or without language rights (South Africa's 1996 constitution names eleven official languages, now twelve with sign language).
5. Courts: a court that can strike down laws (United States, Germany, South Africa) or parliamentary supremacy (United Kingdom).
6. Emergencies: broad powers (Weimar Germany's Article 48, used to rule by decree from 1930 and abused in 1933) or limited, reviewed powers (Germany's 1949 Basic Law).
7. Amending: hard (two-thirds plus regions) or easy.
8. Treaties: join a river treaty with Orrin or not (India and Pakistan's Indus Waters Treaty, 1960).

**Crises (D2.Civ.3.9-12).** Each crisis plays step by step, and every step names the article that decided it:
1. A contested election: the court reviews or the legislature decides.
2. The mountain region votes to leave: federal autonomy, a referendum rule or neither.
3. The leader declares an emergency: how long, who reviews it.
4. Schools ban the Varo language: whether rights and the court stop it.
5. A drought: the river treaty's sharing rule and dispute panel, or a standoff with Orrin.

**The theory shelf.** Short cards: Locke's "Two Treatises" (1689) on consent; Montesquieu's "The Spirit of the Laws" (1748) on separating powers; the Federalist Papers (1787 to 1788, 85 essays); the Haudenosaunee Confederacy and the debate over its influence on U.S. founders (noted by a 1988 congressional resolution and argued by historians); Germany's 1949 design after 1933.

**Scorecard (the aha, D2.Civ.8.9-12).** Four rows by stated rules: stability, rights, representation, peace with the neighbor; then the real country whose choices most match, with that country's real record (from published democracy indexes). The note: "My design kept order when ___. It failed when ___. I would change Article ___ to ___, because ___." Narrator: "Every rule is a bet about what will go wrong."

**The end.** The constitution, the crisis traces, the scorecard and the note. `Print` prints the constitution as a document.

**Rival designs (extra).** Two groups' constitutions face the same crisis side by side.

## Content
- Lunara, its regions, languages and neighbor are made up and labeled; every option card names real countries and dates; five crises with stated rule logic; the theory shelf; the scorecard rules and match.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Crises open after all eight articles are filled; any article can be changed and the crisis rerun.
- Keyboard: Tab to articles, cards, crises, the shelf and the scorecard; Enter places a card.
- With Motion off crisis steps appear without animation.

## Look
- Accent `--brand` #2e6b4f charter green (header, articles, the scorecard); gold #f4c542 (the article in focus, the deciding step); paper #eff6f2; ink #0a2018; muted #4e5a54.
- Contrast (WCAG 2.1, computed): white on brand 6.30:1; brand on paper 5.74:1; ink on paper 15.52:1; muted on paper 6.57:1; ink on gold 10.47:1.
- Never color alone: scorecard rows carry numbers and words; regions carry names.
- Different from this batch (court purple, branch amber, campaign blue, jury brown).

## Art
- Local FLUX (`scripts/localart.py`): Lunara's map scene (1, 16:9), a new capitol (1, 16:9), the river in drought (1, 16:9).
- People (illustrated) for citizens affected by each crisis, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Drawn in code: the constitution document, cards, the scorecard.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator, theory shelf and hints; `bright-teacher` as the crisis reporter. `Curio.voice` with `scope: () => state.mode + ':' + state.article + ':' + state.crisis + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `draft`: "Choose a card for this article."
- event, whole, each card's real-country note.
- event, whole, each crisis step.
- how `rerun`: "Change an article and rerun the crisis."
- event, whole, each theory card.
- how `note`: "Write what you'd change, and why."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the article builder, the crisis rule engine, the theory shelf, the scorecard and country match.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Crises | Skip reading | Each crisis asks which article decided it before the next. |
| Scorecard | Aim for all-high | No set of cards scores high on every row; the rules make trade-offs. |
| Note | Change nothing | The note needs one article to change and why. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `draft`; real-country note (whole).
2. Crisis step (whole), waits; `rerun`.
3. Theory card (whole).
4. `note`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.3.9-12 and D2.Civ.8.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Constitutional texts and features of the six countries | Constitute Project (University of Texas and partners) | each country's official constitution text | yes |
| Switzerland's seven-member Federal Council | Swiss Federal Chancellery, "The Swiss Confederation: A Brief Guide" | Constitute Project | yes |
| South Africa's official languages (eleven in 1996, twelve with sign language in 2023) | Constitution of the Republic of South Africa, Section 6 | South African Government, Constitution Eighteenth Amendment Act (2023) | yes |
| Weimar Article 48 decrees from 1930; the 1949 Basic Law's limits | U.S. Holocaust Memorial Museum, "Article 48" | German Bundestag, "Basic Law" | yes |
| Indus Waters Treaty (1960) | World Bank, "Fact Sheet: The Indus Waters Treaty 1960" | United Nations Treaty Collection | yes |
| Locke (1689), Montesquieu (1748), the Federalist (85 essays, 1787 to 1788) | Library of Congress, "Federalist Papers" | National Archives, Founders Online | yes |
| The Haudenosaunee influence debate; H.Con.Res. 331 (1988) | Congress.gov, H.Con.Res. 331 (100th Congress) | National Museum of the American Indian, "Haudenosaunee Guide" | yes |
| Country records for the match | V-Dem Institute, Democracy Report | Freedom House, "Freedom in the World" | yes |
Backed twice: 9. Cut: 0.

Checks run (Python, scratchpad r22, 2026-11-09): eight articles and five crises; every crisis step names an article from 1 to 8; the Basic Law came 16 years after 1933; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 constitution and cards; at 680x425 sheet.
2. All five crises run and each step names its deciding article. (D2.Civ.3.9-12)
3. The river crisis shows the treaty's effect, with or without it. (D2.Civ.3.9-12)
4. The scorecard, country match and note evaluate the design. (D2.Civ.8.9-12)
5. Every card names real countries; Lunara and Orrin are labeled made up.
6. The constitution prints as a document.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animation; no network requests.

## Open questions
None.
