# Codex review: the-buyout

## Played
Cold Grade 12 solo play: both eight-quarter runs, Compare, every remedy, both views and Memo before builder notes/source; then a projection check. The shop and buyer substitution are strong; the policy clash earns discussion.

## Findings fixed
- blocker, general, Memo: twelve isolated letters passed Check and enabled Save. Only words count, with a/I allowed; padding now fails and a complete memo still saves.
- should fix, general, 680px Memo: the maximum eight evidence chips clipped the last two choices. Consolidated compact navigation and removed instructions duplicated in the hint, retaining 44px choices.
- should fix, general, 375px Compare: the fifth buyer row fell below the fold after Switch. Shortened mini shelves and compact result typography; all five rows now fit.
- should fix, family:market, voice: simultaneous launches dropped later makers. Each shared launch now has one fixed combined event; completion and Switch results start at their trigger.
- should fix, family:market, feedback: 7,500 looked like the difference between students' final runs. Named the four-equal-owner starting point and the rebuttable nature of the guideline presumption.
- should fix, family:market, BT case: wrongly attributed the chosen three-point cap to Littlechild's report. Distinguished his RPI-X proposal from the later government cap.
- should fix, general, hints/focus: Buyout's end named its current mode; partial Compare could name a disabled Finish control; Read's fixed hints were absent from the inventory; a top-model research button could retain disabled focus. Corrected all four.
- should fix, general, compact case toggle: changing remedies could leave Back to ledger on an already-visible ledger. Label and aria-expanded now follow the actual state.
- polish, family:market, flat Switch/Compare handoff: added proportional buyer-flow tracks and a next-step hint after three marks. Retained the shop, palette, ownership graphics and deliberate welfare clash.
- polish, art: replaced the common-charger vignette with a matching-style painting whose three shared USB-C ports and cable connector are clearly visible.

- should fix, general, final craft: active memo navigation cut its own instruction, chart series depended on color, and Evidence could request an unavailable first-remedy ledger. Preserved active-page speech, added matching dotted/solid legends and corrected prerequisite hints.
- should fix, general, phone Buyout: the ownership banner overlapped its ribbons. Increased shelf room and separated the banner; zero overlap, Next at y=683.

## Findings left
None known at blocker/should fix level.
- polish: rapid navigation cuts longer event speech. All four mode how-tos start once on the required path; no promise that every long event finishes before a student's next action.
- nit: a small magenta edge remains under one shopper shoe at enlarged inspection size; unobtrusive in the 34px lane.

## Break it
- Profit/buyers/share/HHI: real end-to-end Price drag, $40 autoplay, rapid Next taps and the default Solid/Steady price sweep. No score/best record exists; $40 loses $649,734.97, and at-cost $10 loses $720,000. Repeated taps book exactly eight quarters.
- Lab meter: inspected no-research and Fast/top-model behavior; at 65 W research disables and focus moves to Next. This is model progress, not a mastery meter.
- Ratings: wrong choices and trying options unlock the unscored demonstration, with corrective explanations. No correctness or saved skill result is awarded, as the spec intends.
- Compare marks: early marking is refused; four/five taps retain at most three distinct rows. Exactly three current marks supply evidence, not a correctness grade.
- Remedy/view/ranking: one view, duplicate remedy and missing/unopened choices fail. Changing cap changes the actual welfare ranking; sweeping cannot set a best score.
- Reasons/evidence: misfit and mixed fitting/misfit reasons fail; one/duplicate chip, wrong-remedy and stale-cap evidence fail. Eight available chips remain accessible.
- Explanation/Save: alphabet padding, repeated-word padding and eleven words fail; complete structure passes and saves locally with privacy text. Editing invalidates Check. The check explicitly does not judge persuasive economic prose.
- Evidence: cold-*.json, cheap-*-after.json, final-memo-gates.json, live-preview.json, top-research-focus.json and independent-numbers.json in Scratch.

## Voice walk
Default settings, held 120ms presses at two-second gaps: shelf, Rivals Q1-Q8, Buyout Q1-Q8, Compare ratings, Switch, three rows, Regulator, Block/Cap/Common, both views, Memo.
Started in order: welcomeRivals; Sparrow30; combined Ohmly/Tidewatt30; Sparrow45; combined Ohmly/Tidewatt45 + Sparrow65; runDone; welcomeBuyout; all30; all45; runDone; welcomeCompare; compareSwitch; switchResult; welcomeRegulator; Block; Cap; Common; memoReasons.
Mark/next-step lines are discarded when the student has already acted or left Compare; hints update immediately. Side checks covered Evidence, Write, Read interrupt, Sound off and mode changes.
| Line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| Each mode welcome | how-to | 1 | 1 each |
| memoWrite, five taps | how | 1 | 1, preserved through repeat taps |
| remedyBlock, five taps | event | 5 | 5 |
All fixed Read hints and combined lines are in voice/lines.json and allLines. Browser fallback is used; no recordings were made.

## Facts checked
- Remaining reference extremes independently recomputed in reference_extremes.py: None/Fast research, Flimsy/Premium quality, generous and $40 Buyout runs, owner research profits and six/twelve/twenty-round price convergence all match.
- Fictional shopper count, costs, quality values, research, savings, launches, logit shares, buyer gain, profit, HHI, remedy totals and all eight caps: spec Content, independently recomputed in independent_model.py; 59 numerical parity checks agree within 0.000001 in their respective units. Default profit $409,926.11; HHI 3,126.979.
- Unrounded counts explain small spec differences: 555,372 / 713,855 / 630,219 / 628,305 / 663,506 served. Switch computes 8,032.493 to rivals, displayed 8,032; 49% and 17%, and both profit directions, agree.
- HHI squared owner shares, 2,500/10,000, >1,800 and increase >100, rebuttable presumption: [DOJ/FTC 2023 Guideline 1](https://www.justice.gov/atr/merger-guidelines/applying-merger-guidelines/guideline-1), checked live.
- Staples/Office Depot 1997 block and lower prices with rivalry: [FTC case](https://www.ftc.gov/legal-library/browse/cases-proceedings/9710008-staples-inc-office-depot-inc) and [FTC pricing analysis](https://www.ftc.gov/news-events/news/speeches/econometric-analysis-ftc-v-staples); savings caveat also checked against the FTC's merger-specific-efficiencies account.
- Standard Oil 1911, Sherman Act 1890 and breakup into more than thirty: [Supreme Court opinion, 221 US 1](https://www.law.cornell.edu/supremecourt/text/221/1).
- AT&T suit 1974, agreement 1982, seven regional companies in 1984, retained long distance: [DOJ history](https://www.justice.gov/archives/atr/technological-innovation-and-monopolization) and [Congressional account](https://www.govinfo.gov/content/pkg/CRPT-106hrpt1048/html/CRPT-106hrpt1048.htm).
- BT: Littlechild's 1983 proposal and government's X=3 choice: [Littlechild 2024](https://www.jbs.cam.ac.uk/wp-content/uploads/2024/10/2024-eprg-littlechild-incentive-regulation.pdf); 1984 cap and service monitoring: [Oftel 1986 report](https://assets.publishing.service.gov.uk/media/5a7cac6fe5274a2f304ef634/0007.pdf).
- EU Directive 2022/2380, 28 Dec 2024 small-device and 28 Apr 2026 laptop dates: [European Commission](https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red/one-common-charging-solution-all_en). Port access is distinguished from required power.
- Schumpeter/Arrow innovation debate: Schumpeter 1942 and [Arrow 1962](https://www.nber.org/books-and-chapters/rate-and-direction-inventive-activity-economic-and-social-factors/economic-welfare-and-allocation-resources-invention); overlapping acquired drug projects less developed: [Cunningham, Ederer and Ma, JPE 2021](https://www.journals.uchicago.edu/doi/10.1086/712506). No charger-market inference claimed.
- Savings can outweigh lost trades in total welfare: Williamson 1968, confirmed by [OECD welfare framework](https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/10/economic-analysis-in-merger-investigations_697b181f/f9cc5dc4-en.pdf). Default buyer/total rankings are model results, not general policy advice.

## Sensitivity
Six people assets checked, all people:true: varied ages, skin tones, bodies and clothing, including a shopper using a cane. Whole figures and ordinary agency are preserved. A fresh sensitivity lens should inspect representation and any perceived association between shopper identity and outcome; these figures represent aggregates, not demographic estimates. The regulation cases are historical precedents, not reenactments of personal harm.

## Flattest moment left
The memo remains a deliberate writing pause. Its value is defending this student's tradeoff; automatic structure checking cannot judge the argument. Switch now shows the substitution and three marked measures lead clearly to Regulator.

## Graphics
All 19 named assets inspected, including all six people; none missing (the spec prose totals twenty but enumerates nineteen). One redraw, via built-in imagegen, full prompt/provenance in art/prompts.json, raw in art/raw/remedy-standard.png, processed by art.py --rekey. Art about 241 KiB; bundle 553.4 KiB. Warm shop, dimensional cartons and ownership graphics retained.

## Audit
The single audit finished inside forty minutes, exit 0, with 11 leads and 59 frames, all inspected. Eight Price load-focus notices follow the explicit spec; two first-tap welcome notices follow BASELINE rule 16. The one confirmed overlap, at 375px in Buyout, is repaired and re-shot at 375px.
All 50 held-click cases across four mode openings report no runtime errors; ten five-tap and ten rapid-tap cases are clean. The completed resize stress reports no exceptions or controls left disabled. No second full audit. Post-audit focused frames/logs cover repaired phone, memo navigation, prerequisite hints, filled grayscale charts and the main voice path.
Numerical and structural validation: 78 checks pass; sampled AA contrasts range from 5.78:1 to 15.43:1. Catalog module standards match the four spec codes and their student activities.

## Left open
- Reference assumption: the spec's 39%/25% quality-cut comparison uses Rivals at $16 and the profit-seeking Buyout price of $22. Prices are not specified beside that example; no fixed quality-cut percentage is shown in the tool. The spec is unchanged.
- Retained explicit spec Price focus on load despite BUILD's general no-load-focus lesson; preventScroll is used. No questions were required.
- Exact news-reader timbre needs recordings; the brief prohibits recording audio. Browser fallback remains.
- Opening reads and a few short log-tail reads lacked termination timers. Bundle, drive and audit processes used bounded wrappers; bundle 120s, drive batches 300s, audit 2400s. No commits.
- An early manual host favicon 404 was corrected in the harness; final hosted phone shots have no console errors. The offline tool makes no network requests. Owned hosts and Chrome close before completion.
