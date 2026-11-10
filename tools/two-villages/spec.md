# Two Villages

## One idea
Two farming villages sit across a river, Eastbank and Westbank (both made up): in Eastbank every plot has a registered title and a fair court settles disputes, in Westbank land is held by custom with no papers and disputes go to whoever has the most pull; the student farms one plot for twenty years and each season decides whether to plant an orchard that pays only from year six, lend grain to a neighbor, use the land as security for a loan to start a shop, or play it safe with a yearly crop; random events (a boundary dispute, a neighbor who won't repay, a powerful family's claim) are settled by each village's rules; the student then plays the other village with the same choices and luck, and the two farms' results sit side by side; real evidence cards show the same pattern in Peru, Argentina and Ghana, where secure titles changed how much families invested; at the end the student writes why the same farmer built more in one village, so a twelfth grader learns how institutions such as clear property rights and the rule of law shape a market economy.

## Not like
- fed-chair (12, spec): central banking. Here the rules under every market.
- the-buyout (12, spec): market structure. Here the institutions beneath it.
- build-a-government (12, spec): designing a government. Here its effect on a farm.
- baron-or-builder (11, spec): industrial capitalism in history. Here property rules in a model.

## Who and how
- Grade 12, Social Studies (Economics), module "Property Rights and the Rule of Law". Standards: D2.Eco.9.9-12 (describe the roles of institutions such as clearly defined property rights and the rule of law in a market economy).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Two villages, twenty seasons in each with the same luck, four choices a season, five dispute events, three evidence cards, the comparison, the paragraph. Extra: Class runs (the class compares runs on one chart). tool.json `modes: ["Farm", "Class runs"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.9.9-12 (property rights) | Decide whether to plant, lend or borrow against land in each village | the orchard, the loan offer, the title or its absence | 2 |
| D2.Eco.9.9-12 (rule of law) | Watch disputes settled by a court or by pull | the dispute cards and outcomes | 3 |
| D2.Eco.9.9-12 (market economy) | Compare the two farms and the real evidence, then write why | the side-by-side ledger; the evidence cards; the paragraph | 4 |

## Screens and modes
Header (kit): title "Two Villages"; `Farm`, `Class runs`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Two villages across a river, both labeled "made up for this tool". Eastbank's land office has a wall of title papers and a courthouse; Westbank has a big house on the hill. A card: "Pick a village. Will you plant an orchard that pays from year six?" The welcome is queued (`welcomeAfter: true`): "Same land, same rain, same farmer. Only the rules differ. Tap a village to start farming." First hint: "Tap Eastbank or Westbank."

**Seasons (focus: the farm and the choice).** At 1366x768 the village fills the left with the choice panel and ledger right; at 680x425 the panel is a sheet. Each season one choice:
- Yearly crop: a small safe harvest.
- Plant an orchard: no harvest for five years, then a large one from year six; land lost before then loses the trees.
- Lend grain to a neighbor: paid back with interest if the deal can be enforced.
- Borrow against the land to start a shop: only possible where the land has a title a lender can check.
- The model's rules are on a card: in Eastbank the yearly chance of losing land to a dispute is 1 percent and courts enforce loans; in Westbank it is 10 percent and repayment depends on the borrower.
- The same random events play in both villages (the student is told so).

**Disputes (rule of law).** Five events: a boundary argument, a neighbor who won't repay, a new road through the field, a powerful family's claim, an inheritance. In Eastbank a court reads the title and rules; in Westbank the outcome follows pull. The student sees each ruling and its reason.

**The comparison (the aha).** Both ledgers side by side: what was built (orchard, shop, savings), what was lost. Three evidence cards:
1. Peru: a 1990s land titling program; titled households worked more outside the home because they no longer had to guard their land (Field, 2007).
2. Argentina: squatters near Buenos Aires who happened to get titles invested more in their houses than neighbors who didn't (Galiani and Schargrodsky, 2010).
3. Ghana: farmers with less secure rights left land fallow less, out of fear of losing it, and got lower yields (Goldstein and Udry, 2008).
The paragraph: "The same farmer built more in ___ because ___. Clear property rights let a person ___. The rule of law matters because ___." Narrator: "People plant trees when they believe they'll be there for the fruit."

**The end.** Both ledgers, the disputes and the paragraph. `Print` prints them.

**Class runs (extra).** The class's results plot on one chart by village.

## Content
- Two made-up villages, the stated model, four choices, five dispute events, three evidence cards with real studies, the paragraph template.
- Westbank is a model of insecure rules, not a picture of any real people or place; no culture is named or shown as backward.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A season waits for a choice; events play after the choice.
- Keyboard: Tab to villages, choices, events, ledger and cards; Enter to choose.
- With Motion off seasons change without animating and trees appear at full size.

## Look
- Accent `--brand` #6b5214 harvest ochre (header, the ledger, title papers); gold #f4c542 (the season's choice, the harvest); paper #fbf7ec; ink #221a05; muted #5c5648.
- Contrast (WCAG 2.1, computed): white on brand 7.39:1; brand on paper 6.90:1; ink on paper 16.11:1; muted on paper 6.81:1; ink on gold 10.60:1.
- Never color alone: villages carry names and icons (a scroll, a big house); ledger lines carry words.
- Different from this batch (clinic teal, clock blue, line crimson, map slate).

## Art
- Local FLUX (`scripts/localart.py`): the two villages across the river (1, 16:9), Eastbank's land office and court (1, 16:9), Westbank's hill house (1, 16:9), an orchard at three ages (3, 4:3), a village shop (1, 4:3).
- Drawn in code: the ledger, choice cards, dispute cards.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the village elder narrating seasons and disputes; `friendly-dad` as the farm neighbor and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.village + ':' + state.season + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `choose`: "Pick this season's choice."
- event, whole, each dispute ruling.
- event, whole, the orchard's first harvest or its loss.
- how `switch`: "Now farm the other village with the same luck."
- event, whole, each evidence card.
- how `paragraph`: "Write why the same farmer built more in one village."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the farm model with seeded events, the two rule sets, the ledger, disputes, the comparison. Model numbers sit in a marked block `/* TWO-VILLAGES DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Seasons | Play only the safe crop | The comparison shows both villages equal; the paragraph asks why nothing was built in either. |
| Second village | Skip it | The paragraph opens after both farms. |
| Paragraph | Write "Eastbank was better" | It needs property rights, the rule of law and one real case. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `choose`.
2. Dispute rulings and harvests (whole), waits.
3. `switch`; the second farm.
4. Evidence cards (whole); `paragraph`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.9.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Peru's titling program and household labor | Field, Quarterly Journal of Economics (2007) | World Bank, "Peru: Urban Property Rights Project" report | yes |
| Titled squatters in Buenos Aires invested more | Galiani and Schargrodsky, Journal of Public Economics (2010) | Di Tella, Galiani and Schargrodsky, Quarterly Journal of Economics (2007) | yes |
| Insecure tenure in Ghana and shorter fallowing | Goldstein and Udry, Journal of Political Economy (2008) | Besley, Journal of Political Economy (1995) | yes |
| Secure property rights and investment in general | de Soto, "The Mystery of Capital" (Basic Books, 2000) | Acemoglu, Johnson and Robinson, American Economic Review (2001) | yes |
| Collateral needs a title a lender can check | World Bank, "Doing Business: Registering Property" | de Soto (2000) | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r24, 2026-11-09): at a 10 percent yearly risk the chance of keeping land 20 years is about 12 percent, at 1 percent about 82 percent; an orchard paying from year six gives 15 paying years of 20; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 village and panel; at 680x425 sheet.
2. Planting, lending and borrowing play out differently by village. (D2.Eco.9.9-12)
3. Five disputes are settled by each village's rules with a reason shown. (D2.Eco.9.9-12)
4. The comparison, three evidence cards and the paragraph appear after both farms. (D2.Eco.9.9-12)
5. Both villages are labeled made up; the model's rules are on a card.
6. Both farms use the same random events.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animation; no network requests.

## Open questions
None.
