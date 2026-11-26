# Cocoa Chain: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: cocoa-chain

#### Built

Two modes: Follow the bar and Explain it. Six painted workplaces connect Ghana, the Netherlands and the US.
Pull the opening red thread, follow goods and money, compare the shared 2023 rains, then construct the causal explanation.
Six needs answers draw six goods/money pairs; six worker reflections expose dated evidence without grading opinions.
The two older dollar studies scale from $1 to $4 and stay separate from the rains comparison.
Includes keyboard, tap and native drag placement, exact validation, Read, kit Sound and Motion, teacher notes and Hard facts.
All writes stayed in tools/cocoa-chain/ and _scratch/cocoa-chain/. Build only: no commit, publication or polish round.
The report was drafted in Scratch because the user's instruction to stop when codex-report.md is written overrides early report creation.

#### Numbers check

Recomputed in _scratch/cocoa-chain/check_numbers.py; results in numbers.json. No household income is estimated.

| Quantity | Computation and result | Treatment |
|---|---|---|
| Ghana harvest | 655,808 to 530,873 tonnes: 19.0505% loss | About 656,000 to 531,000; about one bag in five |
| Farm illustration | 2 x 452 = 904kg, not the spec's 905; 14.464 net 62.5kg bags | Requested 14 to 11 is explicitly illustrative |
| Farm after exact ratio | 14.464 x 530873/655808 = 11.7085 bags | Never called a measured family yield |
| Port illustration | 10 x national ratio = 8.0949 containers | Draws 10 to 8, an illustration |
| Gross versus net | 16 x 64kg gross = 1,024kg gross | Retains COCOBOD's 16-bag pricing convention; explains net/gross in notes |
| Farm price | 1308/800 = 1.635; 2070/800 = 2.5875; April rise = 58.26% | Bag prices dated in sourced reveal |
| Pricing tonne | 800, 1308, 2070 x 16 = 12800, 20928, 33120 | No false equation of gross mass to net tonne |
| World price | Over 10000/2400 = over 4.1667 | Over four times |
| World crop | 4.9 to 4.2 = 14.2857%; 5.04 to 4.37 = 13.2937%, not 13.5% | About 14%, using World Bank series |
| Dollar studies | 6.6+14+35.2+44.2 = 100; 11+19+70 = 100 | Separate dated strips; studies differ |
| $4 farm share | 26.4 cents and 44 cents | Exact visible cents |
| $4 maker plus store | 317.6 cents, versus spec's rounded 318 | Exact one-decimal values retained |
| Store example | $1 x 1.10 = $1.10 | Example label; smaller bar shown alongside full bar |
| Text contrast | Lowest checked pair 5.055:1; ink/paper 15.148:1 | See numbers.json; no color-only answers |

#### Facts checked

Checked against the supplied source map; live primary-source spot checks are identified below.
This does not claim every supplied reference was independently fetched. Figures are dated historical examples.

| Fact used | Source and verification |
|---|---|
| Heavy rains, black pod, tree virus, illegal mining and cocoa-price pressure | BLS, Why is candy so expensive these days?, September 2026; live checked |
| World crop about 14%, December 2024 cocoa above $10/kg | World Bank, Cocoa and coffee prices rebound on renewed supply concerns, January 7, 2025; live checked |
| Exact Ghana harvest 655,808 and 530,873 tonnes | USDA FAS Ghana Cocoa Beans and Cocoa Products Semi-Annual, GH2025-0048, p6; live checked |
| GHc800, 1308 and 2070 per bag, dates and 16-bag pricing | COCOBOD opening-season announcements, 2022-24; 2022 primary release live checked; dated later prices checked to spec sources |
| About 2 hectares, 800,000 families, hand harvest and leaf fermentation | Supplied COCOBOD/Nuamah source map; ICCO post-harvest primary page live checked for process, not exact seven-day duration |
| Takoradi/Tema export route and most exports as beans | Supplied Ghana route/trade sources; geography checked against coastline and place locations |
| Netherlands leading cocoa-bean importer by quantity | CBS, April 2026 cocoa trade release; live checked. Not confused with combined products' import value rank |
| European grinding low in four years; US 2025 prices about 10% or more and smaller packs | Supplied dated Reuters/ECA and chocolate-maker reporting in spec Sources |
| 2015 shares; 2020 French dark-chocolate shares | Supplied Make Chocolate Fair and BASIC studies; differing scope stated on screen |
| 1.56 million children, 2018-19, Ghana and Cote d'Ivoire | NORC 2020 report through US DOL; live checked; not presented as a current census |
| Hazardous work forbidden under 18 | Ghana child-labor framework and US DOL Ghana report; live checked |
| Ecuador cacao more than 5,000 years ago | Zarrillo et al., 2018, PMID 30374172; live checked, archaeological evidence about 5,300 years |
| Quarshie, Fernando Po, Mampong 1879, earlier missionaries | COCOBOD 2019 historical newsletter; live checked |
| Ghana and Cote d'Ivoire largest growers | Supplied ICCO/World Bank sources; historical comparison, not an invented production forecast |

Source links and teaching qualifications are in spec.md and notes.md. Workers are expressly made-up people.

#### Break it

- Enumerated all 20,160 ordered six-of-eight sentence selections: exactly one passes.
- Enumerated all 360 assignments of four distinct chips: exactly one passes. Evidence: adversarial.cjs and adversarial.json.
- Rejected empty work, duplicate sentence, repeated chip, both distractor sentences, farm-price X1, bag-count X2,
  swapped stages and missing evidence. Distractors have distinct, relevant feedback; no tries or score is stored.
- Shuffled both visual and DOM tray order; opaque IDs avoid a numbered answer key. A real Tab/Enter placement and native drag worked.
- After a valid answer, editing a sentence disabled reading and removed the paragraph; calling its handler still revalidated and rejected it.
- Six actual needs answers produced six brown goods and six gold money arrows. Reflection buttons reveal evidence, not a correctness score.
- Tried all navigation paths, first Before, first Store, More first, rapid season taps, dollar boundaries, $4 exact cents,
  season restoration at all six stops, Motion off, grayscale, and focus retention while updating dollar values.
- The early art-token syntax failure was fixed. Failed frames and the initial browser startup retry remain in Scratch as evidence.
- Final scoped repository contract checks passed, both bundled scripts parsed, JSON/hashes matched, and all test ports closed.
- Corrective feedback allows trial and error by design. Completing this lesson is not an independent mastery assessment.

#### Voice walk

Used real held clicks (0.12s), five repeats 2s apart, quiet settling, focused Enter twice and 0.7s quick taps.
Browser voice logs cover Follow, all needs, all links, rains, worker reveals, Explain, chips, Check, Clear, Read and Sound.
Five repeated empty Checks spoke the same needed instruction once; Back/Next repeats did not nag the Farm how line.
Fixed lost queued correct-answer/all-links feedback by playing the current result immediately.
The complete rains line finishes before its next instruction; pending outcome prompts drop after the outcome is already selected.
Leaving a scene stops its obsolete how line; wrong-pin feedback can replace it immediately, with the question retained on screen.
Modal hints name Close, and phone/short-preview explanation hints explicitly describe scrolling.
Read repeats current guidance and worker/card content; explanation Read requires a current valid solution.
78 lines select friendly-dad/Achird in voice/lines.json. Recorded voice is 0KB, as Build prohibits recording.
These checks verify browser-fallback runtime behavior, not a recorded voice performance or auditory fidelity review.

#### Feel check

Played the student path through the six links, every rain comparison and the finished explanation, using actual controls.
Best moment: the wet farm loses three visible bags, then the shrinking stock and smaller bar carry that change into the US store.
The route and opposite money arrows make the connection tangible; later stops change the job, object count and economic consequence.
The paragraph finish reconnects each sentence to a small scene icon instead of ending with a numeric score.
Compared 1366x768 frames against snowy-mail-route and beat-lab. Cocoa Chain has a richer painted world and full adult characters.
The farm, shed, dock and factory each have distinct silhouettes and readable foreground numbers, rather than six recolored panels.
Explain is deliberately quieter and more text-heavy; the phone scrolling costs fluency. That remaining limit is reported, not passed.
Evidence: feel-comparison.jpg, art-final-contact.jpg, scenes/, functional/, last/ and post-audit/.

#### Done when

1. PASS: scene largest, full worker visible, season/Back/Next visible at 1366x768; scene/season/Next remain at 680x425.
2. PASS: pointer/key actions finish pending visual motion immediately; rapid season and audit mid-animation resize had no lock or exception.
3. PASS: opening hint names the thread, first thread opens Farm, and Next traverses all six workplaces in order.
4. PASS: six right needs answers draw six arrow pairs and 6 of 6 links. Wrong-pin guidance is guarded once per stop; question stays visible.
5. PASS: all six stops changed objects/numbers/poses and restored; rain Store shows full/smaller comparison and about $1.10 or more.
6. PASS: judgments appear only during rains, all choices open the sourced reveal, and the Farm includes both harvests and the price change.
7. PASS: strict exhaustive validation; D1, D2 and X1 feedback differ; no attempts count; valid Read supplies all six sentences and four quantities.
8. PASS WITH DOCUMENTED CORRECTIONS: arithmetic errors in the spec are corrected or labelled illustrative; dollar strips say studies differ.
9. PASS FOR CHECKED RUNTIME: once-per-run how guards, five-repeat logs and complete rains sequencing checked. Recorded voice remains future work.
10. PASS: Hard facts/origin/Quarshie text retained, Read includes it, modal controls stay visible; every people asset shows adults only.

#### Wave lessons

| BUILD.md lesson | Result and evidence |
|---|---|
| Hint and voice | PASS: immediate sync, V.heard guards, modal/phone context, real repeated clicks; obsolete scene prompts stop on action |
| Focus and layout | PASS on checked paths: retained dollar DOM/focus, no load focus, reserved hint; audit overlap repairs in post-audit/ |
| Sizes | PASS for target sizes/current hints checked; FAIL for whole-choice visibility on phone/short Explain, detailed below |
| No giveaways | PASS for validator and scores: opaque shuffled tiles/DOM, strict evidence, no mastery/score from participation; trial correction is intrinsic |
| Honest numbers | PASS: dated sources, illustrative farm/containers/store example, no inferred household income, exact dollar sums |
| Standards | PASS: needs links, shared cross-border rain comparison, evidence-backed causal construction are solo student actions; no family engine |
| Motion off | PASS: audit calm clean, no infinite active animation; scene/state changes remain immediate |
| Short choices always visible | FAIL: phone and short landscape Explain scroll; 760x900 repaired. Rain outcomes all visible; compact secondary reference controls scroll |
| Resize mid-animation | PASS: full audit resized each state/action both ways; no exceptions or stranded disabled controls |
| Welcome after first tap | PASS: first action owns current guidance; no late welcomeAfter, modal no longer queues hidden-thread instructions |
| Unknown shown unknown | PASS: before/rain are explicitly selected historical views; no mystery state falsely painted as known |
| One look, one meaning | PASS: brown labelled goods and gold labelled money arrows have opposite direction; blue denotes the rain comparison |
| Badge says true | PASS: 6 of 6 means traced links, country marks mean participation, first Store no longer claims whole-chain completion |
| Hint changes back | PASS: every season/stop/mode syncs; six-stop reversal and initial Before checked |
| No copying answer words | FAIL as an independent assessment: supplied explanation intentionally recalls the scenes' sentences and quantities. Kept spec content, no mastery claim |

#### Audit leads

Ran scripts/audit_tool.py once, last, on Chrome 9991 and host 8795; completed in 28.3 minutes, 64 leads, no runtime exceptions.
The original audit and exact 64-item disposition ledger are _scratch/cocoa-chain/audit/audit.md and audit-responses.md.
Only targeted repair checks followed; the full audit was not repeated.

- Fixed 3 small-tag leads, 3 wide ocean/thread overlaps and 4 narrow map overlaps.
- Fixed all 14 below-fold Explain controls at 760x900; all choices now fit in the targeted bounds check.
- Left 15 phone Explain below-fold leads open: scrolling preserves readable text and 44px targets; guidance explains the path.
- Left 1 compact rain secondary-reference scroll lead open; all three actual outcome answers remain visible.
- Accepted 1 obsolete queued outcome how line dropping after the student already answered.
- Fixed 1 modal keep-region fixture; covered background hint is intentional. Fixed 1 compact modal Read-control lead with sticky controls.
- Answered all 19 welcome leads under first-action guidance rules; additionally fixed unvisited Store and initial Before truth.
- Accepted 2 fast-tap stale scene/how cuts; original needs question now remains visible through wrong-pin feedback.

#### Frames looked at

Inspected all shot PNGs, including failed initial frames. Reviewed audit/voice groups in labelled contact sheets, with problem frames separately.
Both modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900; actual 375x812 iframe host.
Opening, farm dry/wet, all six wet stops, all links, reflections, $4 dollar studies, cards, explanation pass/error/edit,
keyboard, native drag, grayscale, calm, rapid switching, resize and final compact modal frames.
Folders: first/, first-fixed/, sizes/, functional/, rechecks/, last/, scenes/, preaudit/, audit/, voice/, voice-fixed/,
post-audit/, compact-final/, phone/ and bars-frames/. Contact sheets and hashes are in Scratch.
Tool-console checks were clean. The temporary outer phone host's missing favicon produced a host-only 404, not an app error.

#### Art made

23 WebP assets: seven full scene backgrounds, four physical objects, twelve adult worker pose assets.
All generated with OpenAI gpt-image during this build; raw originals and prompts retained. Every people asset has people: true.
Four redraws: couple working cutout, both Luis poses, and rain farm with covered fermentation mat.
Art is 1460.21KiB; recorded voice 0KiB. Final embedded bundle is 2119.03KiB, about 2.07MiB.
Image-plus-voice assets meet the 2MB goal; base64 embedding lifts the complete bundle slightly over it, well below 6MB.
No stock search, downloaded illustration, font dependency or third-party request. Natural Earth geometry is separately credited.

#### Art still to paint

None. Fresh sensitivity review of the twelve people assets remains a review task, not a missing painting.

#### Engine changes wanted

None. No kit/shared script edited. Tool-local spacing avoids bundle art-token parsing of an art:wet object key.

#### Left open

- All-choice visibility fails on phone and short Explain previews. Do not mark the build fully compliant with that rule.
- Compact rain secondary references require panel scrolling. Main scene, season/navigation and judgment choices remain visible.
- Independent sensitivity/cold review is pending: Ghanaian representation, names/places, child labor, Quarshie and missionary history.
- Recorded voice is intentionally pending. Browser fallback behavior was checked; later recording needs its own listening pass.
- Used locally verified Natural Earth 1:50m geometry instead of requested 1:110m, thinned and credited in map.json.
- Used the detailed spec's 2023 rains over the old drought concept, and the user's image tool over the older Gemini suggestion.
- Arithmetic, route tap dual-purpose behavior, trial-feedback limits and every open-question decision are recorded in handoff.md.
- No claim of a cold review, complete mobile choice visibility, recorded voice quality or scored learning mastery.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: cocoa-chain
#### Played
Cold Grade 5 solo run: pulled the thread, walked all six stops, compared rains and workers, built and read the explanation before opening builder files. Replayed as a projected lesson. Rich scenes carry the geography; Explain feels more like a worksheet.
Workspace S:\CurioClass-codex. One review/fix pass, no commits. Evidence is in _scratch/cocoa-chain/review-*; browser ports 9950, 9953, 9954 and audit port 9951; host 8755.
#### Findings fixed
- **Should fix, general, buying station:** source/spec's October 2023 price date was wrong. Changed to September, against contemporary COCOBOD/Graphic reporting; left spec.md untouched.
- **Should fix, general, facts:** bounded the port earnings claim to first-half 2024 versus a year earlier. Described the 2025 US price/pack action as announced, rather than a measured universal retail rise. Dated the grower-ranking caption.
- **Should fix, general, compact map:** its renderer discarded every goods/money arrow. Restored all six pairs, with real-pixel curves and distinguishable outlined money arrows. A zero-size guard also prevents hidden-map SVG errors on mode changes.
- **Should fix, general, access:** used sentences/chips faded below normal text contrast. Kept dark ink and used a dashed border/background to mark placement.
- **Should fix, general, voice:** sentence selection gave no spoken destination instruction. Added once-only placement guidance, immediate current-state speech and stale-line cancellation; registered Read's composed hints and dollar lines too. Repeated selection now lets its current how line finish.
- **Should fix, general, previews:** moved the current needs question ahead of secondary worker references in short dry views. Gave the 1000x625 explanation a side-by-side workspace instead of an unnecessary vertical stack, with matching voice guidance. Existing compact reference buttons now stay above the fold.
- **Should fix, general, port art:** containers floated above the ship and eight containers left unsupported upper boxes. Redrew port-quay in the established style, aligned overlays to its flat deck and filled the lower row first.
- **Polish, general, header:** fixed Sound widths prevent horizontal shifts and keep its icon/text on one line.
- **Polish, general, payoff:** the completed paragraph was the flattest moment. Reconnected its causal steps to painted scenes and places; phone scenes use three columns. Moved the ocean label away from the money line. Kept the strong cast, palette, farm comparison and detailed workplaces.
#### Findings left
- **Should fix, general, source conflict:** the required USDA 2025 harvest series gives 530,873 tonnes, but a newer COCOBOD release gives 432,145 for 2023/24. Both are official sources; the discrepancy is not reconciled. Added the conflict to notes/handoff; retained the specified numerical model pending a spec decision.
- **Blocker, general, Explain:** first-error feedback is an answer oracle. A script that ignored sentence meanings solved it in 29 Checks; the post-fix rerun passed in 31. Exact order/chip validation does not prevent elimination. The required feedback order and unlimited correction are explicit in the spec; changing them needs a spec decision.
- **Blocker, general, needs links:** sweeping pins without reading reached 6 of 6 in 21 taps. The spec requires optional questions, free wrong-pin feedback and the count. Completion therefore cannot demonstrate independent learning; notes/handoff now say so. No score or best score is stored.
- **Should fix, general, small Explain:** 680x425, 800x500 and 375x812 still hide some full-text choices until scrolling. Keeping six slots, eight long sentences, six chips and 44px targets simultaneously is incompatible with those dimensions. Preserved content/targets and explicit scroll guidance; a different compact interaction needs a spec change.
#### Break it
- Needs count: tried every pin at each stop; 21 taps earned all six links before and after changes. Compact final DOM has six goods and six money paths. Open blocker above, not a PASS.
- Explanation: empty work, both distractors, swapped steps, missing chips, wrong units, the true-but-irrelevant farm-price chip, and repeated/changed placements were rejected. Exhaustively tried 20,160 ordered six-of-eight selections and 360 chip assignments: one valid result in each set.
- Cheap explanation: used only Check text to select successive candidates/chips. It still passes; strict validation and opaque shuffled IDs do not resolve this required-feedback conflict.
- Read gate: editing a valid answer disables Read my explanation, removes the paragraph, and direct activation cannot bypass revalidation.
- Reflection marks: Helped/Hurt/Both all reveal evidence and can mark each country, as specified. These are participation marks, with no correctness or assumed student mistake. No score, timer, best score or reward gate exists.
- Dollar display: swept $1 through $4 and beyond both ends; clamps correctly. $4 gives farm 26.4/44 cents and maker-plus-store 317.6 cents for 2015. No optimal-answer badge or score can be farmed.
- Season: ten rapid reversals ended in the last requested state. Shared state survives mode switches. Motion off has zero infinite animations. Native drag placed a tile; a Tab/Enter-only run placed a sentence and retained visible focus.
#### Voice walk
Held clicks 0.12s, 2s gaps, defaults/Sound on: thread -> Farm -> Buying -> Port -> Grinder -> Maker -> Store -> rains -> judgments/back through all stops -> Explain -> sentences/slots -> chip/socket.
Started lines in order: needsFarm, needs, atStore, rainsOn, askHurt, reveal (four current reveals), wExplain, placeSentence, afterPlace, placeChip. The first thread action skips the welcome under BASELINE 16. The rains sentence finishes intact; earlier queued prompts/results drop when their scene or unanswered moment is gone.
Side path: Farm -> Hard facts -> Read card -> Close -> Explain -> Sound off -> Read -> Follow. Read interrupts speech, includes the facts/card, works with Sound off, and mode changes discard stale speech.
| Line | Kind | Expected | Started |
|---|---|---:|---:|
| placeSentence, five selections | how | 1 | 1 |
| needsFarm / needs, main walk | how | 1 each | 1 each |
| empty1, five Checks | event | 5 | 5 |
Voice manifest and allLines match exactly. Browser fallback was exercised; no recorded clips were made or claimed to have been listened to.
#### Facts checked
Live named-source checks, with independent arithmetic in review-numbers.json. Spec arithmetic corrections: 2 x 452 is 904kg, not 905; 5.04 to 4.37 is 13.29%, not 13.5%. The displayed world loss uses the World Bank series. The model is historical and the people/particular route are fictional.
| Fact | Named source / result |
|---|---|
| 2022 hot/dry, 2023 heavy rains, black pod and supply pressure | [BLS Monthly Labor Review, 2026](https://www.bls.gov/opub/mlr/2026/article/why-is-candy-so-expensive-these-days.htm). Rain is one cause, not the whole history. |
| Tree virus, illegal mining and Ghana crop constraints | [USDA FAS Ghana semiannual GH2025-0048](https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Ghana+Cocoa+Beans+and+Cocoa+Products+Semi-Annual+-+The+Mid-Crop+MY+2024-2025+Update+_Accra_Ghana_GH2025-0048.pdf), alongside BLS. |
| World harvest about 14%; December 2024 above $10/kg | [World Bank, January 7, 2025](https://blogs.worldbank.org/en/opendata/cocoa-and-coffee-prices-rebound-on-renewed-supply-concerns): 4.9 to 4.2 million tonnes is 14.29%; $10/kg is $10,000/tonne. |
| Ghana 655,808 to 530,873 tonnes; about one bag in five | Matches the specified USDA 2025 series: 19.05% decline. [Newer COCOBOD figures differ](https://cocobod.gh/news/press-release-on-cocoa-sector-reforms-for-financial-viability-and-long-term-sustainability), giving 432,145; unresolved, not universally verified. 14/11 sacks and 10/8 containers are labelled illustrations. |
| Roughly 800,000 families, small farms/about 2 hectares, purchasing clerks, COCOBOD/CMC trade | [ICCO Ghana country report, August 2023, pp6-9](https://www.icco.org/wp-content/uploads/3-FEASIBILITY-STUDY-ON-AFRICA-COCOA-EXCHANGE__Annex_GHANA.pdf). |
| Hand harvesting, plantain-leaf fermentation, sun drying; about a week | ICCO country report and [ICCO harvesting/post-harvest](https://www.icco.org/harvesting-post-harvest-new/); methods/duration vary. The fictional family's process is plausible. |
| Takoradi/Tema ports; most Ghana cocoa exported as beans | ICCO Ghana report, pp6-7: export terminals and about 70% raw-bean exports. Ghana -> Netherlands -> US is an illustrative route, not traced provenance for a brand. |
| GH¢800 in 2022-23; sixteen-bag pricing tonne | [COCOBOD, October 6, 2022](https://cocobod.gh/news/press-release-opening-of-202223-main-crop-season). 16 x 800 = 12,800. 16 x 64kg gross = 1,024kg gross; notes distinguish net cocoa and trade pricing. |
| GH¢1,308 from September 2023; GH¢2,070 from April 5, 2024 | [COCOBOD September 12 release](https://citinewsroom.com/wp-content/uploads/2023/09/PRESS-RELEASE-12TH-SEPT.-2023.docx.pdf), [Graphic September 11](https://www.graphic.com.gh/news/general-news/govt-increases-cocoa-price-bag-up-from-gh-800-to-gh-1-308-tome-now-gh-20-943-from-gh-12-800.html), [COCOBOD April release](https://cocobod.gh/news/review-of-the-producer-price-of-cocoa-for-the-202324-cocoa-season). 16 x 2,070 = 33,120. |
| About $2,400/tonne in 2022; over four times by December 2024 | [ICCO December 2022 report](https://www.icco.org/wp-content/uploads/ICCO-Monthly-Cocoa-Market-Report-December-2022.pdf): $2,368 annual average; World Bank above. Over 10,000/2,400 is over 4.17. |
| Lower Ghana export earnings | [Bank of Ghana July 2024 data reported by MyJoyOnline](https://www.myjoyonline.com/ghanas-cocoa-crisis-deepens-2024-half-year-revenues-crash-by-nearly-700-million/). Qualified to first-half 2024, not all years/accounting streams. |
| Netherlands largest bean importer by volume; beans become paste, butter and powder | [CBS April 2026](https://www.cbs.nl/en-gb/news/2026/14/the-netherlands-is-the-world-s-leading-exporter-of-cocoa-products) and ICCO Ghana report/processing description. Import value of all cocoa products is a different ranking. |
| European late-2024 grinding lowest in four years | [ECA historical quarterly table](https://www.eurococoa.com/wp-content/uploads/WEBSITE-REPORT-WESTERN-STATS-Q1-2025-1.pdf): Q4 2024 331,853 tonnes, lower than every quarter since Q2 2020. Fewer shifts is explicitly a possible effect, not measured Sanne employment data. |
| 2025 US maker about 10% or higher pricing and smaller packs | [Company July 2025 remarks](https://hershey.gcs-web.com/static-files/96d3bd2f-5d2c-41cf-bbac-57ab132ecac1), [AP July 23 company statement](https://apnews.com/article/f597cd39672a05a3cac3b170a5541431). Corrected to announced plan. The $1/$1.10 store tags are calculated examples. |
| 2015 shares 6.6/14/35.2/44.2; 2020 shares 11/19/70 | [Cocoa Barometer 2015](https://voicenetwork.cc/wp-content/uploads/2019/07/Cocoa-Barometer-2015-USA.pdf), [BASIC 2020 study](https://basic.coop/en/productions/etude/comparative-study-on-the-distribution-of-value-in-european-chocolate-chains/), [FAO summary](https://www.fao.org/investment-centre/latest/news/detail/comprehensive-market-study-confirms-low-margins-for-cocoa-farmers--in-renewed-hope-for-increased-income/). Both strips total 100; grouped/residual values are not profit. |
| $4 farm cents 26.4/44; 2015 maker/store total 317.6 | Independent multiplication of the dated shares. Neither study changes with the rains; French dark chocolate is identified in the expanded dollar card. |
| 1.56 million children in 2018-19, mostly hazardous work including sharp tools/heavy loads | [NORC 2020 brief](https://www.norc.org/content/dam/norc-org/documents/standard-projects-pdf/NORC2028_CocoaBrief_10.pdf), [ICI technical summary](https://www.cocoainitiative.org/sites/default/files/resources/ICI_Technical_Summary_2018-19_NORC_survey.pdf). Dated estimate, not a current census or a claim about the fictional children. |
| Ghana hazardous-work minimum age 18 | [ILO Child Labour Observatory](https://webapps.ilo.org/clodashboard/section/2F); Children's Act sections 91/92, also listed in US DOL Ghana findings. |
| Cacao used in today's Ecuador more than 5,000 years ago | [Zarrillo et al., 2018](https://pubmed.ncbi.nlm.nih.gov/30374172/): approximately 5,300-year archaeological evidence, predating European arrival. |
| Quarshie, blacksmith/Fernando Po, Mampong 1879; earlier missionary trees | [COCOBOD 2019 historical newsletter](https://cocobod.gh/resource_files/cocobod-news-september-december-2019.pdf). The wording credits Ghanaian farmers and does not call Quarshie the first planter. |
| Ghana/Côte d'Ivoire leading growers | BLS and World Bank above; map wording is bounded to 2023-24. No current-price or permanent-rank claim. |
#### Sensitivity
Fresh cultural review should examine all twelve people assets, fictional Ghanaian names, contemporary work/clothes, representation, the child-labor card and the balance of farmer agency versus hardship. All people assets are marked people:true; all figures are adults, fully clothed and respectfully drawn. No child working is pictured or requested disclosure elicited.
Retained the specific Ghanaian credit, earlier-missionary qualification and pre-European Ecuador evidence. A reviewer should judge whether the Ecuador wording needs explicit Indigenous cultural attribution, and whether the cast's uniformly slim bodies need broader representation. These are judgment calls, not facts silently rewritten here.
#### Flattest moment left
Scrolling between the long sentence tray, ladder and chips in small Explain views. The added painted completion sequence lifts the ending, while the required six-sentence construction stays text-heavy.
#### Graphics
Reviewed all 23 finished assets, twelve adult pose images, all six scenes before/after, tiny and full-screen compositions, grayscale and Motion off. Redrew port-quay once with built-in imagegen; raw file is art/raw/port-quay.png, full prompt in art/prompts.json. Existing styles/characters remain.
Compared frames side by side in _scratch/cocoa-chain/review-benchmark-comparison.jpg. Its layered workplaces and cast hold the art bar against snowy-mail-route and beat-lab; the explanation has less replay pull. No art:<name> is missing. Art totals 1477.6 KiB; the bundle is 2147.2 KiB, well below the 6MB explanation threshold.
#### Audit
Completed once with the 40-minute process limit, Chrome 9951 and host 8755: 41 leads. Three compact-reference leads were fixed; all 15 phone Explain overflow leads remain under the named spec conflict. The other 23 are intentional modal coverage, already-answered prompt cancellation, allowed first-action welcome skips and two stale/corrective fast-tap cuts. See _scratch/cocoa-chain/review-audit-responses.md for every disposition.
Repetition and resize stress were clean. Only affected states were re-shot after repairs: _scratch/cocoa-chain/review-post-audit. Final targeted runs have zero tool-console errors. The early phone host favicon 404 was host-only; later host runs are clean.
Wave checks: current hints/voice, retained focus, no load focus, 44px targets, grayscale signals, truthful state labels, reversal, resize and Motion off checked. Cheap completion and compact Explain visibility are explicitly failed above. Every claimed frame was opened. All test Chrome/server ports were closed; no commits or writes outside the allowed artifact folders were made.
#### Left open
The two feedback/elimination blockers, unresolved official harvest figures and remaining compact all-choice conflict require specification decisions. No extra feature, kit change, attempt limit or assessment gate was invented. The review does not grant a clean release verdict.
Recorded voice remains a later production step. No listening claim beyond the browser-fallback main-path/Read logs. Notes retain their required opening three sections and contain source/assessment limits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Cocoa Chain handoff

Build only. No commit, deployment or polish round.

#### Implementation

src.html starts from the kit starter and uses kit CSS, Motion, Sound, tones and Curio.voice.
The source contains responsive scene styling, six stop records, shared season state, map and scene renderers,
the two dated dollar studies, a pure explanation validator, and persistent keyboard/drag controls.
map.json contains locally thinned Natural Earth coastline geometry and is loaded by the bundle token.
Worker cards have a short visible introduction and their complete supplied text under More and Read.
All scene art uses art tokens and is embedded in the bundle. Raw originals remain under art/raw as required.

The six numbered pins answer the current unanswered needs question. Once answered, pins navigate.
Back, Next stop and the dollar strip navigate without requiring a needs answer. This resolves the specification’s
dual assignment of navigation and answering to the same map tap. Initial pins navigate immediately.
The shared rains state survives mode changes. Reflection choices survive turning the rains off and back on.
Explanation edits invalidate a pass immediately; reading revalidates rather than trusting a button flag.

#### Open question decisions and contradictions

- The supplied concept/idea says drought; the detailed spec explicitly prefers the actual 2023 rains. Used the rains.
- The spec mentions Gemini for people; the current build brief and user explicitly require the image tool.
  Used OpenAI gpt-image, credited in the manifest. Every people asset has people: true.
- The only open question is sensitivity review. Retained the supplied historical and child-labor text, made respectful
  adult art, and left the independent fresh-agent review to the cold review stage. No questions require an answer here.
- Natural Earth 1:110m was requested. Available local verified geometry was 1:50m; used it, thinned locally and credited.
  The map remains equirectangular over lon -100 to 20 and lat -5 to 60. Pins use leader spacing for adjacent stops.
- The calculation note says 2 x 452 kg = 905 kg. It is 904 kg, 14.464 net bags, then 11.709 under the national ratio.
  Keeping the requested 14-to-11 illustration therefore cannot be described as that exact yield calculation.
  Scene labels explicitly identify the bags as illustrative; no household income is calculated.
- 16 x 64 kg gross is 1,024 kg gross, not one net tonne. The COCOBOD 16-bag price convention is retained,
  with net-versus-gross explained in notes. No arithmetic exercise equates the gross mass to 1,000 kg.
- 5.04 to 4.37 million tonnes is a 13.29% decline, not 13.5%. About 14% is supported by the World Bank’s 4.9-to-4.2 series.
- $4 times the 2015 maker/store share is 317.6 cents, rounded 318 in the spec. The strip keeps one decimal for exact sums.
- The spec’s compact Explain layout (six 44px rows, four 44px tray rows, two 44px chip rows, plus header) cannot fit
  425px high. STANDARDS target sizes win. This build permits scrolling for the explanation workspace at that extreme.
  Follow’s frequently used controls and the whole scene remain the compact priority.

#### Sensitivity

Cold review should inspect Ghanaian names, skilled contemporary adult representation, all twelve people images,
the Ghanaian places, the child-labor card, Tetteh Quarshie’s credit, the earlier-missionary note and South American origin.
No child is pictured or asked about their own household. The farming couple’s children are described as in school.
Working art was redrawn for the couple to remove scenery; both Luis poses were redrawn to match his supplied role.
The contact sheet and all review evidence live in _scratch/cocoa-chain/.

#### Engine changes wanted

None required. A tool-local space avoids bundle_tool.py treating an object’s art:wet as an image token.
No kit or repository script was edited.

#### Review next

See codex-report.md for actual checked results, audit dispositions and remaining limitations.
Recorded voice was prohibited in Build; voice/lines.json selects friendly-dad (Achird) for a later recording stage.
Until then Curio.voice uses the browser fallback. No fixed-voice fidelity claim is made.

#### Build verification and remaining limits

The single full audit completed in 28.3 minutes with 64 mechanical leads. Each is answered in
_scratch/cocoa-chain/audit-responses.md. Repairs covered narrow map overlaps, 10px tags, the 760px Explain layout,
sticky modal controls, correct first-action guidance, retained dollar focus and stale explanation passes.
The dry 680px worker card uses a shorter name and first sentence; the full role, names and supplied text remain
under More and Read. A wrong pin keeps the question visible while giving its corrective hint.

At phone width and short landscape heights, Explain still scrolls. This is a reported failure of the all-choices
above-the-fold rule, not a claim of complete responsive compliance. Its hint and voice now explain the scrolling.
In the 680px rain preview the three outcome choices remain visible; secondary reference buttons require scrolling.
The 760x900 Explain layout now shows all sentences and chips at once.

Strict validator enumeration tested 20,160 sentence orders and 360 chip arrangements, with one valid result each.
Real held-click, keyboard, native drag, six-link, season reversal and stale-pass tests are preserved in Scratch.
The puzzle provides corrective feedback by design and is not an independent mastery assessment or scored game.
No tries, grade or best score is stored. Reflection marks mean participation only.

The user's stop-on-report instruction overrides the brief's request to create codex-report.md early.
The report was drafted in Scratch during the build, then copied to its final path only as the final work step.

#### Cold review changes

The review first played the complete tool before reading this handoff or the builder report.
Port art was redrawn in the same style and container overlays now fill their bottom row before the top row.
Compact route views retain goods/money arrow pairs. The ocean label moved away from the money line.
The paragraph finish reconnects the six steps to painted scenes; selected sentences now have once-only spoken placement guidance.
Used tiles retain ink contrast instead of fading. Three source qualifications were corrected: September 2023 farm price,
first-half-2024 export earnings, and announced 2025 US price/pack changes. Source links are in notes.md.

Review decisions without an attendant: retained full text and 44px controls rather than shrinking the short/phone
Explain workspace, and retained the specified first-error feedback and optional needs questions. These are open
spec conflicts, not waived checks. A blind trial using only feedback passed Explain, and pin sweeping reached six links.
The cold-review report records these as blockers to using completion as independent evidence of learning.
No new feature, engine edit, recording, commit or publication was introduced.

The fresh cultural review should still judge the fictional Ghanaian names, the adult working/thinking art,
the child-labor card, and whether the Ecuador origin should explicitly credit Indigenous makers.
The current text retains Ghanaian farmer agency and Quarshie's 1879 Mampong credit without calling him the first planter.

#### Cold review final verification

The single review audit completed under its 40-minute limit with 41 leads. Three compact-reference leads were repaired
by placing existing reference controls outside the worker card and ahead of secondary content in compact views.
Fifteen phone Explain leads remain under the documented specification conflict. The other 23 leads are intentional
modal coverage, already-answered prompt cancellation, BASELINE 16 welcome skips and two obsolete/corrective speech cuts.
The exact disposition ledger is _scratch/cocoa-chain/review-audit-responses.md. No full audit was repeated.
Only affected frames were re-shot. All compact reference buttons are visible; the 1000px workspace and its voice agree;
repeated selections no longer cut a still-fitting how line; Sound width is stable and its label stays on one line.
Native drag, keyboard placement, strict validator, Read invalidation, calm mode and rapid season changes were checked.

An additional unresolved source conflict belongs to the spec owner: USDA FAS GH2025-0048 gives 530,873 tonnes for
2023/24 while COCOBOD's newer sector-reform release gives 432,145. The model's specified numbers were retained;
notes.md and codex-review.md disclose the conflict rather than presenting either series as universally settled.
No clean-release or independent-mastery claim is made. The pin sweep and first-error oracle remain explicit blockers.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
