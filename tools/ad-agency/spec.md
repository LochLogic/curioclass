# Ad Agency

## One idea
Every trick that sells leaves a trail: run a made-up ad agency for six weeks where a false claim, an influencer paid on the quiet or reviews you wrote yourself really do lift sales at first, then switch desks and work as the watchdog, following the trails in a made-up web (whose site is that "independent" review page, what does that cited study really say, who is that smiling reviewer) and sorting each ad into fair, persuasive but legal, or breaking a named rule, so you learn the tricks by profiting from them and the tells by catching them.

## Not like
- fake-or-fact-lab (library 6-8, family sibling): judges whether made-up pages are reliable, reading inside then laterally. Here the student first makes the ads, and the audit question is which rule an ad breaks, with persuasion that is legal kept as its own verdict.
- fact-check-desk (ela 8, family sibling, not built): two sources disagree on one fact. Here the sources are ads and the subject is how persuasion is regulated.
- startup-tycoon (financial literacy, not built): running a business on prices and costs. Here the money is only the temptation; there are no prices, stock or hiring.
- question-sharpener (ela 12): a weekly season priced in research hours. Here the weeks are a pressure loop that ends in a switch of sides.
- fallacy-field-guide (ela 10): bandwagon as a reasoning error. Here bandwagon is a legal technique when the number is true, and the audit has to say so.
- health-claim-checker (health): follows one claim up its chain of retellings to the hop where it broke. Here R3's overclaim is one ad among nine, and the question is which advertising rule it breaks.
- phishing-spotter (cs 6-8, same voice): scams that steal accounts. Here the ads are mostly lawful, and the line between selling hard and deceiving is the subject.

## Who and how
- Grade 12 ELA, module Media Literacy (Speaking and Listening): "Evaluate sources, bias and persuasion in media".
- Driver: students on laptops, alone or in pairs. 40 to 50 minutes (Agency about 20, Watchdog about 20).
- Standards: SL.11-12.2 (integrate multiple sources in diverse formats and media, evaluating credibility and accuracy): Watchdog's lateral checks. SL.11-12.3 (evaluate a speaker's point of view, reasoning, use of evidence and rhetoric): Agency choices and the three-way verdict.
- tool.json: driver "students", minutes "40-50", modes ["Agency", "Watchdog", "Rulebook"], grades_label "Grade 12". Kit starter plus `kit:fact-check` and `kit:theme-912`.

## Screens and modes
Header: title "Ad Agency", small line "Sell it. Then catch it."; mode buttons **Agency** (opens first), **Watchdog** (unlocks after week 6, or by **Skip to Watchdog**), **Rulebook**; Motion, Sound, Read. A strip under the header always shows "Lantern & Lark Agency: made up. Every client, product, person and site here is made up."

### Agency (opens first)
- Top bar: **Week 1 of 6**, client name, agency cash, and the **Risk** gauge (0 to 8, with the word **Quiet**, **Noticed**, **Watched**, **Letter coming**).
- Left: the **client file** (what is true and what is proven, Content). Center: the **ad board** with five slots: **Headline claim** (one of four), **Endorser** (one of six), **Techniques** (up to two of five), **Fine print** (one of three), **Medium** (one of four). Right: the ad as it will appear, rendered by the engine's Browser in the medium's look (a Chirp post, a video pre-roll transcript card, a page on bestpicks.example, a billboard).
- **Run the ad** closes the week. Results card: lift percent, income, client trust change, risk added, and two to four Chirp replies from made-up buyers (Content). Then **Next week**.
- When Risk reaches 8 at the end of a week, the next week opens with a **Watchdog letter** (Content): a $5,000 fine, the week's slot spent on a correction ad (lift 0), the named client's trust down 2, Risk back to 0. A client whose trust reaches -6 leaves; their later weeks read "No client this week".
- After week 6: a **Season card** with total cash, a week-by-week bar chart (bars drawn with values written on them), letters received and clients kept, plus "This is a game model, not a prediction. Real enforcement is slower and less certain, and honest ads can fail too."

### Watchdog
- The desk inbox lists nine ads: the student's three highest-risk weeks (or their first three if none had risk) and six rival ads R1 to R6 (Content). Each opens in the engine Browser with all tools unlocked: new tabs, Search, Search this image, Who runs this site?, and Trace on cited links.
- Notebook (engine) collects cards as the student finds things (tags `inside`, `who`, `evidence`, `others`).
- For each ad, the **Call** panel: **Fair**, **Persuasive but legal**, **Breaks a rule**. Breaks a rule then asks which rule card applies (from the Rulebook; one or more). **Lock my call** records it (engine Calls).
- **Expert call** after locking: the tool's verdict, the rule(s), and the finding that proves it, with "Same", "Close" (right verdict, different rule) or "Different". No score total.

### Rulebook
- Eight rule cards, each with the plain line, the exact words and the citation (Content). Cards link to the ads in this season that broke them ("Your week 2 ad, R1").
- **Clear my season** (confirm) wipes this tool's storage.

## Content
**Clients and files** (made up)
- Fizzwell sparkling energy water. True: 80 mg caffeine per can. Proven: nothing about focus. Its own taste test: 7 of 10 tasters preferred it.
- TrailPeak hiking boots. True: two-year warranty. Proven: waterproof for 24 hours in a lab test.
- StudyNest homework app. True: 12,000 downloads. Its own survey: 61 percent of users said homework felt "more organized". No study on grades.
Weeks: 1 Fizzwell, 2 TrailPeak, 3 StudyNest, 4 Fizzwell, 5 TrailPeak, 6 StudyNest.

**Headline claims** (per client: true / vague praise / unproven / false). Values: lift, trust, risk.
- True: Fizzwell "80 mg of caffeine in every can." TrailPeak "Waterproof for 24 hours in lab tests." StudyNest "61% of our users say homework feels more organized." +5, +1, 0.
- Vague praise: "The most refreshing can in the cooler." / "Built for the long haul." / "Your homework, sorted." +8, 0, 0.
- Unproven: "Proven to boost focus." / "Never get blisters again." / "Raise your grades a full letter." +20, -1, 3.
- False: "Doctors recommend Fizzwell." / "Worn by Everest guides." / "Teachers' number one homework app." +25, -2, 4.

**Endorsers** (lift, trust, risk, rule)
- N0 None. 0, 0, 0.
- N1 Real customer, with a typical-results line ("Results vary. Most users ..."). +6, +1, 0. 255.2(b).
- N2 Paid influencer, "#ad" at the start. +10, 0, 0. 255.5.
- N3 Paid influencer, no disclosure. +15, -1, 3. 255.5.
- N4 Five-star reviews the agency wrote. +18, -2, 4. 465.2.
- N5 Free product to anyone who posts a five-star review. +12, -1, 3. 465.4.

**Techniques** (up to two; lift, risk)
- Q1 Bandwagon with a true number ("12,000 students use it"). +6, 0.
- Q2 Limited time ("This week only", and it is). +8, 0.
- Q3 Before-and-after story. +7, 0 (with N1's typical-results line), else 1.
- Q4 "Beats the leading brand" with no test. +7, 2.
- Q5 Emotional story (a first long hike, a calm homework night). +6, 0.

**Fine print** (lift, trust, risk): P0 None: 0, 0, 0. P1 Clear, next to the claim: -2, +1, 0. P2 Tiny grey text at the end: 0, 0, 1 (not clear and conspicuous).

**Media** (lift, risk): M1 Chirp post +5, 0. M2 Video pre-roll +4, 0. M3 "Independent" review page on bestpicks.example that the agency secretly runs +12, 4 (465.6). M4 Billboard +2, 0.

**Rules of the model**: lift = claim + endorser + techniques + fine print + medium + 2 x client trust, floor 0. Income = $2,000 + $100 x lift; a correction week pays the $2,000 base only if that week has a client, minus the $5,000 fine; a week with no client pays $0. Client trust runs -6 to +6, starts 0. Risk adds up across weeks. Letter rule as in Screens. Worked examples (Done when): the honest plan (true claim, N2, Q1, Q5, P1, M1) every week totals $31,200; the trick plan (false claim, N4, Q1, Q4, P0, M3) every week totals $13,400 with three letters and three lost clients; week 1 pays $5,000 honest against $8,800 tricks.

**Buyer replies** (Chirp, made up; chosen by the week's worst choice): unproven or false claim "Drank two. Still can't focus on chemistry."; N3 "Wait, is she paid for this?"; N4 "Every review is five stars and posted the same day. Hmm."; M3 "bestpicks ranks this first for everything?"; honest week "Warranty actually covered my torn seam. Respect."; P2 "Had to zoom in 400% to read that."

**Watchdog letter** (made up office, real rules): "Watchdog Desk, Notice. Your ad for [client] in week [n] [broke rule card]. Fine: $5,000. Run a correction this week." The named client is the client of the week that pushed Risk to 8 or more; the rule is that week's riskiest choice.

**Rival ads** (Hightower Media, made up; findings via the engine)
- R1 Chirp post by @mayaonthego for GlowDrop face serum, no "#ad". Finding: her profile bio reads "GlowDrop partner. Code MAYA20." Expert: Breaks a rule, 255.5.
- R2 bestpicks.example "Top 5 Study Apps" with QuizRocket first, footer "Independent reviews". Finding: Who runs this site? shows registrant Hightower Media; hightower.example lists QuizRocket as a client. Expert: Breaks a rule, 465.6.
- R3 PeakPro protein bar: "Clinically proven to build muscle 2x faster", cited to sportsnutritionjournal.example. Finding: Trace shows "This source doesn't say that."; the study tested a protein powder in 12 adults for 4 weeks and reports no 2x result. Expert: Breaks a rule, Section 5 (an unproven claim made directly).
- R4 SnoozeWell pillow: "I slept 9 hours the first night!" Dana R., five stars. Finding: Search this image puts Dana's photo first on stockpix.example, labeled "Smiling woman, model, 2023". Expert: Breaks a rule, 465.2 and 255.2(b).
- R5 TrailMix Co. granola: "Now with 20% more almonds than our 2025 recipe." Finding: the product page's nutrition panel shows both recipes. Expert: Fair.
- R6 RideLoop bike app: "Join 2 million riders." Finding: Openpedia and the company's About page both give the rider count. Expert: Persuasive but legal (a true bandwagon).

**Rule cards** (plain line; exact words; citation)
- Section 5: Deceptive ads are against the law. "unfair or deceptive acts or practices in or affecting commerce, are hereby declared unlawful." 15 U.S.C. 45(a)(1).
- 255.1(a): An endorsement must be what the endorser really thinks. "Endorsements must reflect the honest opinions, findings, beliefs, or experience of the endorser."
- 255.2(a): Customer stories don't prove a product works. "Consumer endorsements themselves are not competent and reliable scientific evidence."
- 255.2(b): If one customer's result isn't typical, say what is. The ad "should clearly and conspicuously disclose the generally expected performance".
- 255.5: Paid or gifted endorsers must say so. "such connection must be disclosed clearly and conspicuously."
- 465.2: No fake reviewers. A business may not create a review that misrepresents "That the reviewer or testimonialist exists".
- 465.4: No paying for a particular star rating. Incentives may not be "conditioned ... on, the writing or creation of consumer reviews expressing a particular sentiment".
- 465.6: A company's own review site can't pose as independent. It may not misrepresent that a site "it controls, owns, or operates provides independent reviews or opinions".

## Interactions in detail
- Run the ad is disabled until claim, endorser, fine print and medium are set (techniques may be none). The ad preview updates on every choice.
- Risk gauge shows its number and word; the jump at Run is animated (instant with Motion off).
- Correction weeks: the board is locked and shows the correction text "Correction: Our earlier ad said [claim]. That was not supported."; **Run the correction** advances.
- Skip to Watchdog fills the three "own ads" slots with three fixed sample weeks from the trick plan.
- Watchdog uses the engine exactly as in fake-or-fact-lab: Search over the index terms in Content (glowdrop, maya, bestpicks, hightower, quizrocket, peakpro, protein study, snoozewell, dana, trailmix almonds, rideloop riders), imageSearch on R4, lookup on R2, Trace on R3. Every domain ends in `.example`.
- Calls record verdict, rules chosen, seconds and tabs; Expert call shows after Lock only.
- localStorage key `aa.v1` (try/catch): season state, calls, notebook. Without storage the season runs in memory and the strip says so.
- At 680 x 425 the client file collapses to a **File** button; board and Run stay visible.

## Look
Dark agency at night: theme-912 panels with a neon-sign accent. Brand #a3ff19 (acid lime) for the agency sign, Run button and lift numbers; brand-ink #142000 on lime fills. Verdicts: Fair #6fdca6 with a check, Persuasive but legal #ffd166 with a megaphone glyph, Breaks a rule #ff9e7a with a cross. Risk gauge ink #e8edf3 with tick words. Focus ring #8fe3ff (kit). Made-up sites keep their own looks (engine).
Contrast (WCAG): brand on panel #141b25 13.91, on paper 15.1; brand-ink on brand 13.65; Fair 10.27, Persuasive 12.0, Breaks 8.59 on panel; ink 14.7; muted 8.13; focus 12.03. Nearest catalog accent: phishing-spotter #b6f23a at dE 16.2 (a cs 6-8 tool, different subject and band).

## Art
none: drawn in code (agency sign, ad mockups, billboard frame, gauge, chart). The reviewer and influencer avatars are initials in shapes, not faces; R4's "stock photo" is a drawn silhouette card labeled as a photo placeholder. No people images.

## Voice
Bank voice `lively-host`, style "Say it like an upbeat game-show host who also reads the fine print." Not used by a family sibling or a grade 11-12 ELA neighbor (phishing-spotter, cs 6-8, also uses it). `Curio.voice`, `scope: () => state.mode + state.week`. Ads and replies are read on screen only.
- w-agency (how): "Read the client file, fill the board, then run the ad."
- file (how, first unproven or false claim chosen): "Check the file. Is that claim proven?"
- risk (event, Risk reaches Watched; stale at the next Run): "The watchdog is starting to notice."
- letter (event, a letter opens; stale on Run the correction): "A letter from the watchdog. This week goes to a correction."
- season (event, Season card; stale on mode change): "Season over. Now switch desks."
- w-watch (how): "Open an ad, then leave it. Check who is behind it before you call it."
- legal (how, first Persuasive but legal call): "Persuasive isn't the same as illegal. Name the rule, or call it legal."

## Family engine
`kit/fact-check.js`, described in full in tools/fake-or-fact-lab/spec.md (World, Browser, Locks, Search, Trace, Notebook, Calls, `__tool.fc`). This tool feeds:
- World: sites chirp (posts by the student's ads, @mayaonthego and her profile), bestpicks.example, hightower.example, sportsnutritionjournal.example (R3's study page), stockpix.example, glowdrop.example, peakpro.example, snoozewell.example, trailmix.example (product page with both nutrition panels), rideloop.example (About page), Openpedia entry "RideLoop"; image `dana` with copies stockpix (2023, first) and snoozewell; lookup for bestpicks.example (registrant Hightower Media) and hightower.example.
- Browser renders the student's own ads from their board choices as `post`, `article` (bestpicks) or `document` (pre-roll transcript, billboard).
- Locks: not used (Watchdog is fully unlocked; Agency has no browsing).
- Search index terms as listed in Interactions; Trace on R3; Notebook; Calls with an added `rules` field.

## Sources
- FTC Act section 5: 15 U.S.C. 45(a)(1), Legal Information Institute, https://www.law.cornell.edu/uscode/text/15/45.
- Endorsement Guides, 16 CFR 255.1(a), 255.2(a) and (b), 255.5(a): eCFR, https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255, checked 2026-10-27.
- Rule on the Use of Consumer Reviews and Testimonials, 16 CFR 465.2, 465.4, 465.6: eCFR, https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465, checked 2026-10-27.
- All clients, products, agencies, people, sites, numbers, the Watchdog Desk and the game model are made up for Curio Class.

## Done when
1. The honest plan in every week ends the season at $31,200 with no letters; the trick plan ends at $13,400 with three letters and Fizzwell, StudyNest and TrailPeak gone.
2. Week 1 pays $5,000 for the honest plan and $8,800 for the trick plan.
3. A week with Risk reaching 8 opens a letter the next week, locks the board to a correction and resets Risk to 0.
4. The ad preview changes with each board choice and renders in the chosen medium's look.
5. In Watchdog, R2's lookup shows Hightower Media, R3's Trace says "This source doesn't say that.", R4's image search lists stockpix.example first, R1's profile shows the partner line.
6. Expert calls: R5 Fair, R6 Persuasive but legal, R1 to R4 Breaks a rule with the rules in Content; Close appears when the verdict matches but the rule does not.
7. Every domain ends in `.example` (engine check logs no errors).
8. Season and calls survive a reload; Clear my season wipes them.
9. At 680 x 425 and 375 wide no horizontal scroll; the board and Run, and the Call panel, are reachable without scrolling.

## Open questions
- ad-agency: The model makes tricks lose over six weeks every time (letters are certain at Risk 8). Keep it certain for clarity, or add chance so a lucky trickster can win, which is closer to life?
- ad-agency: Name the real regulator (the FTC) in the letter, or keep the made-up Watchdog Desk with real rule citations as now?
