# E-Bike Buyer

## One idea
A savings jar on a bedroom shelf holds $900, and three e-bikes glow on a phone screen, a flashy ad bike promising "50-mile range!", a review site's favorite, and the one the child's friend Marco owns (Marco is made up, labeled "illustration"), and the child compares what each source says, the ad's claim against the review's tested range of about 28 miles and Marco's story of his battery dying on hills, and checks each battery for a safety certification label; then the child adds the true cost to a receipt, a $700 bike plus a $60 lock, a $40 helmet and $30 of lights, $830 in all with $70 left in the jar; next the child picks one way to protect the bike, a 2-year warranty for $90, theft insurance at $8 a month, a repair fund of $10 a month, or nothing, and lives through a year of monthly event cards: two flat tires at $25 each, a lock attack at month 7 that a good lock stops, and a battery that fails at month 10 and costs $450 to replace; with the warranty the year costs $140, with insurance $596 because the theft never happened, with nothing $500 straight from savings, and the repair fund covers $120 of the $500; at the end the child sees that the sticker price is not the cost, and that each kind of protection fits some risks and not others, so a student in grades 6 to 8 learns smart spending and how to manage the risk of loss.

## Not like
- the-credit-card-diaries (Grades 9-12, spec): credit. Here cash, true cost and protection.
- first-apartment-budget (Grades 9-12, live): a monthly budget. Here one purchase and its year.
- workplace-scenarios (Grades 6-8, spec): choices at work. Here choices as a buyer.
- startup-shares (Grades 6-8, spec): investing risk. Here the risk of loss on something you own.

## Who and how
- Grades 6-8, Personal Finance (CTE explore), module "E-Bike Buyer". Standards: NSPFE Spending, NSPFE Managing Risk (National Standards for Personal Financial Education, 2021).
- Format: story. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card and line. Controls 48 px or more.
- Three bikes, three sources, a true-cost receipt, four protection choices, twelve monthly cards, the year's tally. Extra: Compare all four (replay the same year with each protection side by side). tool.json `modes: ["Buy", "Compare all four"]`, `minutes: "20-30"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| NSPFE Spending | Compare the ad, review and friend; check the label; add the true cost | the receipt at $830 | 2 |
| NSPFE Managing Risk | Pick protection; live the year; compare | $140, $500, $596 and the fund | 3 |

## Screens and modes
Header (kit): title "E-Bike Buyer"; `Buy`, `Compare all four`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bedroom shelf with the $900 jar and a phone showing three bikes. The welcome is queued (`welcomeAfter: true`): "You saved $900. Tap a bike to see what people say." First hint: "Tap a bike."

**Compare (focus: the phone).** At 1366x768 the phone is left with the source panel right; at 680x425 the panel is a sheet. Each bike shows its ad claim, the review's tested numbers, Marco's story and the battery label (certified or no label).

**True cost.** The child drags needed extras to the receipt; the jar drains as items land.

**Protect.** Four cards with price and what each covers and doesn't.

**Live the year.** Twelve month cards flip; each event draws from the protection or the jar, with a running tally.

**Sticker isn't cost (the aha).** Narrator: "The price tag was $700. The year cost more, and the right protection depended on what went wrong."

**The end.** The receipt, the protection and the year's tally. `Print` prints them.

**Compare all four (extra).** Four tallies side by side.

## Content
- Prices are dated 2025 to 2026 ranges labeled "typical"; bikes are generic with no brand marks; Marco is labeled "illustration".
- The year's events are fixed so all four choices can be compared fairly.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The bike and protection can be changed until `Start the year`; the year can be replayed.
- Keyboard: Tab to bikes, sources, extras, protection cards and months; Enter picks or flips.
- With Motion off months appear without flips.

## Look
- Accent `--brand` #1f5f86 e-bike blue (header, the receipt, buttons); gold #f4c542 (the month in focus, the jar); paper #edf4f8; ink #071b28; muted #4a5560.
- Contrast (WCAG 2.1, computed): white on brand 6.91:1; brand on paper 6.22:1; ink on paper 15.79:1; muted on paper 6.85:1; ink on gold 10.79:1.
- Never color alone: covered and not covered carry a check or an X and words.
- Different from this batch (bookshelf walnut, notebook moss).

## Art
- People (illustrated): Marco, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the bedroom shelf (1, 16:9), three generic e-bikes (3, 4:3), a bike shop and a street (2, 16:9).
- Drawn in code: the phone, receipt, cards and tally.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Marco; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.month + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `bike`: "Tap a bike."
- how `source`: "Tap the ad, the review or Marco's story."
- how `extras`: "Drag what you need onto the receipt."
- how `protect`: "Pick one way to protect your bike."
- how `month`: "Tap the next month."
- event, whole, sticker isn't cost.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
Money family engine (as described for first-apartment-budget and market-time-machine; the integrating session decides its file). Tool-only code: the source compare, the receipt, protection rules, the fixed year of events.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Compare | Pick the ad bike | Its range claim fails the review, and its battery has no label. |
| True cost | Skip the lock | Month 7's attack takes the bike. |
| Protect | Pick at random | The end asks which risk each choice covered. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `bike`; `source`.
2. `extras`; `protect`.
3. `month`.
4. Sticker isn't cost (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NSPFE Spending and Managing Risk wording | data/standards/nspfe-2021.txt | data/modules.csv module line | yes |
| E-bike batteries should carry a safety certification (UL 2849 or UL 2271) | U.S. Consumer Product Safety Commission, "Micromobility Products-Related Deaths, Injuries and Hazard Patterns" and e-bike safety guidance | New York City Fire Department, lithium-ion battery safety rules for e-bikes | yes |
| Real e-bike range is often far below ad claims and depends on hills and load | Consumer Reports, e-bike buying guide and range testing | U.S. Department of Energy, Alternative Fuels Data Center, "Electric Bicycles" | yes |
| Extended warranties and insurance fit some risks and not others | Federal Trade Commission, "Extended Warranties and Service Contracts" | Consumer Financial Protection Bureau, consumer guidance on insurance and emergency savings | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s28, 2026-11-10): $700 plus $130 of extras is $830, leaving $70; the year costs $140 with the warranty, $596 with insurance, $500 with nothing, and the $120 fund covers part of $500; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 phone and panel; at 680x425 panel as a sheet.
2. Three sources are compared, the label checked and the true cost added. (NSPFE Spending)
3. A protection is chosen, the year lived and the four choices compared. (NSPFE Managing Risk)
4. Prices are dated typical ranges; no brand marks.
5. The year's events are the same for every choice.
6. `Read` reads every card and line; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no flips; no network requests.

## Open questions
- E-bike, repair, warranty and insurance prices and theft rates (default used: dated typical 2025 to 2026 ranges with a $700 bike and a $450 battery; refresh at Build).
