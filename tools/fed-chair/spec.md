# Fed Chair

## One idea
The student takes the chair of the Federal Reserve in four real moments, the high inflation of late 1979, the financial crisis of late 2008, the lockdowns of March 2020 and the price surge of 2022, and at each meeting sets the interest rate (and, in 2008 and 2020, how much to buy in bonds) while a fiscal panel shows what Congress is choosing beside them (tax cuts, relief checks, spending), which the student can recommend; a teaching model, with its rules and lags stated, moves inflation, unemployment and lending over the following two to three years; short scenes show a bank deciding on loans, a family's mortgage, and a small business choosing whether to hire as each rate change lands; at the end the student's path sits beside the real one (Paul Volcker's rate near 20 percent and the deep recession of 1982, rates near zero in 2008 and 2020, the fast hikes of 2022 to 2023), and the student writes which mix of monetary and fiscal policy fit each condition and why, so a twelfth grader learns to evaluate the selection of monetary and fiscal policies in a variety of economic conditions.

## Not like
- economy-dashboard (12, spec): reading real data. Here making the call.
- inflation-wallet (10, spec): a family through hyperinflation. Here the people setting policy.
- stock-market-1929 (11, spec): one crash as an investor. Here four crises as the central bank.
- two-villages (12, concept): property rights and the rule of law. Here money and rates.

## Who and how
- Grade 12, Social Studies (Economics), module "Money and the Federal Reserve". Standards: D2.Eco.12.9-12 (evaluate the selection of monetary and fiscal policies in a variety of economic conditions). D2.Eco.9.9-12 from this module is taught in two-villages, as the idea card proposes.
- Format: simulator. Driver: one student alone, or the class sitting as the committee and voting (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Four eras with about six meetings each, the fiscal panel, the bank and family scenes, the comparison, the evaluation. Extra: Committee vote (the class votes each meeting's rate; the median wins, as on the real committee's majority vote). tool.json `modes: ["The chair", "Committee vote"]`, `minutes: "35-45"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.12.9-12 (monetary) | Set the rate and bond purchases at each meeting and watch the lagged effects | the rate dial; inflation, unemployment and lending lines | 2 |
| D2.Eco.12.9-12 (fiscal) | Read Congress's choices and recommend one per era | the fiscal panel | 3 |
| D2.Eco.12.9-12 (evaluation) | Compare the student's path with the real one and write which mix fit each condition | the side-by-side paths; the evaluation | 4 |

## Screens and modes
Header (kit): title "Fed Chair"; `The chair`, `Committee vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** The Federal Reserve boardroom, a long table and a rate dial. The 1979 dashboard: inflation above 11 percent and rising, unemployment near 6 percent, gas lines on the news. The welcome is queued (`welcomeAfter: true`): "Prices are climbing every month. You control one lever: the interest rate. Its effects take a year or more to show. Turn the dial." First hint: "Turn the rate dial."

**Meetings (focus: the dial and the lines).** At 1366x768 the dashboard fills the left with the dial and fiscal panel right; at 680x425 the panel is a sheet. Each meeting: set the rate (and bond purchases where they apply), see the next quarters play with stated lags (about 12 to 18 months for most of the effect on inflation), then the next meeting.
1. 1979 to 1983: Volcker took office in August 1979; in October 1979 the Fed shifted to controlling money growth; the federal funds rate reached about 20 percent; unemployment hit 10.8 percent in late 1982; inflation fell to about 3 percent by 1983. Fiscal panel: the 1981 tax cuts and rising defense spending.
2. 2008 to 2010: Lehman Brothers failed on September 15, 2008; the Fed cut to near zero (0 to 0.25 percent) on December 16, 2008 and began buying bonds; fiscal panel: the 2009 Recovery Act (about $787 billion).
3. 2020 to 2021: the Fed cut to near zero on March 15, 2020 and bought bonds; fiscal panel: the CARES Act (about $2.2 trillion, March 27, 2020) and later relief.
4. 2022 to 2023: inflation reached about 9 percent in June 2022; the Fed began raising rates in March 2022, including several 0.75-point hikes, to 5.25 to 5.5 percent by July 2023; unemployment stayed low.
- The model is labeled "a teaching model, not a forecast", with its rules on a card.

**Bank and family scenes.** After each rate change: a bank officer (made up) tightens or eases loans; a family (made up) sees its mortgage offer change (for example, a 30-year rate above 18 percent in 1981 and near 3 percent in 2021); a small business owner (made up) decides whether to hire.

**The comparison and evaluation (the aha).** The student's rate path and outcomes beside the real ones for each era. "In ___, the right mix was ___ because inflation was ___ and unemployment was ___. Fiscal policy helped (or hurt) by ___." Narrator: "Every rate decision is a bet about a year from now, made with last month's numbers."

**The end.** Four eras' paths, the scenes and the evaluation. `Print` prints them.

**Committee vote (extra).** The class votes each meeting; the median vote sets the rate.

## Content
- Four eras with real starting data, about twenty-four meetings, the stated teaching model with lags, fiscal panels with real acts and sizes, made-up bank and family scenes (labeled), the real paths, the evaluation template.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each meeting waits for a rate; the quarters then play.
- Keyboard: Tab to the dial, bond slider, fiscal panel, scenes and comparison; arrow keys move the dial by 0.25 points.
- With Motion off lines draw at once and the dial jumps.

## Look
- Accent `--brand` #24504a Fed green (header, the dial, lines); gold #f4c542 (the rate set, the real path); paper #eff5f4; ink #081c19; muted #4f5957.
- Contrast (WCAG 2.1, computed): white on brand 9.05:1; brand on paper 8.20:1; ink on paper 15.99:1; muted on paper 6.57:1; ink on gold 10.85:1.
- Never color alone: the student's path is solid and labeled, the real path dashed and labeled.
- Different from this batch (biscuit brown, lifespan rose, chart navy, trait indigo).

## Art
- Local FLUX (`scripts/localart.py`): the boardroom (1, 16:9), a bank office (1, 16:9), a family's kitchen table (1, 16:9), a small shop (1, 16:9).
- People (illustrated) for the made-up bank officer, family and owner, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Drawn in code: the dial and charts.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as the staff economist briefing each meeting; `smooth-narrator` as the narrator, scenes and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.era + ':' + state.meeting + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each meeting's briefing.
- how `set`: "Set the rate for this meeting."
- event, whole, each scene.
- how `fiscal`: "Recommend one fiscal choice for this era."
- event, whole, each era's real path.
- how `evaluate`: "Write which mix fit, and why."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the teaching model with lags, the dial, the fiscal panel, scenes, the comparison. Era data sits in a marked block `/* FED-CHAIR DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Meetings | Set the same rate every time | Outcomes show; the evaluation asks why the student's path differed. |
| Fiscal | Recommend the biggest package | The model shows its effect on inflation in that era. |
| Evaluation | Write one rule for all four eras | It needs a mix and a reason per era. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Briefing (whole), waits; `set`.
2. Scene (whole); `fiscal`.
3. Real path (whole).
4. `evaluate`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.12.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Volcker took office August 1979; the October 1979 shift; rates near 20 percent | Federal Reserve History, "The Great Inflation" | Federal Reserve History, "Volcker's Announcement of Anti-Inflation Measures" | yes |
| Unemployment 10.8 percent late 1982; inflation about 3 percent by 1983 | Bureau of Labor Statistics | FRED (UNRATE, CPIAUCSL) | yes |
| Near-zero rates December 16, 2008 and March 15, 2020 | Federal Reserve, FOMC statements | Federal Reserve History, "The Great Recession" | yes |
| The 2009 Recovery Act (about $787 billion); the CARES Act (about $2.2 trillion) | Congressional Budget Office | Congress.gov, H.R. 1 (111th) and H.R. 748 (116th) | yes |
| 2022 hikes from March, to 5.25 to 5.5 percent by July 2023 | Federal Reserve, FOMC statements | FRED (DFEDTARU) | yes |
| 30-year mortgage rates above 18 percent (1981) and near 3 percent (2021) | Freddie Mac, Primary Mortgage Market Survey | FRED (MORTGAGE30US) | yes |
| Monetary policy affects inflation with long lags | Federal Reserve Bank of San Francisco, "How long does it take for monetary policy to affect the economy?" | Friedman, "A Program for Monetary Stability" (Fordham, 1960) | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r23, 2026-11-09): four eras in date order; the 2022 to 2023 hikes total 5.25 points from near zero; the 2020 cut came 12 days before the CARES Act; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 dashboard and dial; at 680x425 sheet.
2. Each meeting's rate moves the lines with stated lags. (D2.Eco.12.9-12)
3. Each era has a fiscal recommendation. (D2.Eco.12.9-12)
4. The evaluation names a mix and a reason per era. (D2.Eco.12.9-12)
5. The model is labeled a teaching model with its rules shown.
6. The real path is shown dashed beside the student's.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: lines draw at once; no network requests.

## Open questions
- The idea card moves D2.Eco.9.9-12 to two-villages (default used: fed-chair teaches D2.Eco.12.9-12 only; two-villages takes D2.Eco.9.9-12).
- The idea card flags a data source (default used: historical rates and indicators from FRED and Federal Reserve statements, with a stated teaching model checked against the real paths before build).
