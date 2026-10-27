# Health Claim Checker

## One idea
Follow a viral health claim back up its chain of retellings (post, article, press release, study) with the words that changed at each hop highlighted, and pin the exact hop where "a small study in mice found a link" became "this cures it."

## Not like
- satire-decoder (9-12 ELA, mystery): tags lines of one fixed text on a case board to prove what an author means. Health Claim Checker has no case board and no tagging; it walks a chain of different sources and compares each one with the next.
- fake-or-fact-lab (6-8 library, lab, fact-check family): lateral reading of made-up sites (authors, dates). Here the source is found already; the question is what the study really showed and how the claim grew on the way out.
- misleading-charts (6-8 CS, mystery): charts that mislead by their drawing. No charts here; the claims mislead by their words and study design.
- label-detective (3-5 health, mystery): proves an answer with a label line. Here proof is a hop in a chain and a study's design.
- first-aid-responder and meal-and-move-planner (same group): acting and planning. This one is judging information, untimed.
- mind-map (9-12 health, built): mental health facts. No mental health claims in these cases.

## Who and how
- Grade 9-12, Health, module Accessing Valid Health Information (evaluate sources, products and services).
- Driver: students on laptops (alone or in pairs). A teacher can project one case and let the class vote on the verdict.
- Minutes: 15-40 (one case is 6 to 8 minutes).
- Standards: NHES.S3 (access valid health information, products and services); also NHES.S2 (analyze how media and commercial interests shape a health claim).
- Topic line: "evaluating health information and sources".
- Modes (tool.json): ["Cases", "Toolkit"]. No points; a case ends with the case file, not a score.

## Screens and modes
Header (theme-912): title "Health Claim Checker" with small line "Evaluating health information and sources", mode buttons **Cases**, **Toolkit** (keys 1, 2), **Motion**, **Sound**, **Read**.

A line under the header in both modes: "Every post, person, product, outlet and study in these cases is made up for practice. The real facts in the case files are sourced."

### Cases (opens first)
- Case shelf: six case cards (title, the viral post's text as a teaser, "3 hops" or "4 hops", and "Closed" once done this session). Tap **Open case**.
- Case screen, stage: **the chain**, a vertical column. At the top the viral post (styled as a plain social card: made-up handle, likes, the claim). Under it a **Trace it ↓** button. Each press reveals the next hop down (an article, a product page, a press release, a study summary), joined by a link line. Each hop card shows: what kind of source it is (icon and word), who made it, **Who gains?** (a button that reveals the motive line), and the claim as that source states it.
- The diff: on every hop above the bottom one, words that are new compared with the hop below are highlighted (yellow marker, plus underline), and a "Lost on the way" line under the card lists the words the hop below had that this one dropped, struck through. The diffs are written by hand in Content, not computed.
- The bottom hop is the source: a study card with fields **Who was studied**, **How many**, **How long**, **Compared with**, **What they measured**, **What they found**, **Who paid**, **Kind of study**. Or, for one case, "No study found" with what the search turned up.
- Panel, the case notes (three steps, each always open, any order):
  1. **Pin where it broke**: tap a hop's **📌 Pin** button (one or two hops), then pick up to two reasons from the eight reason chips (Content) or **It holds up**.
  2. **Verdict**: **Holds up**, **Overstated**, **Not supported**.
  3. **Close the case** (enabled once there is a pin or It holds up, and a verdict). The case file opens: the right verdict and pins (each of yours marked ✓ or ✗ in words), the explanation, an **Honest version** of the claim in one sentence, and for real-topic cases the real facts with their source. **Back to cases**, **Next case ▶**, **Reopen** (clears your notes).
- No "Closed" state, pin or verdict is stored after the page closes.

### Toolkit
- **Questions to ask** (ten cards, each with a one-line why): Who made it and who pays? Is someone selling something? What is the source, and can you find it? Was it in people? How many? Compared with what? A link, or a cause? Relative or absolute risk? Do other experts and reviews agree? How new is it?
- **Study ladder**: five rungs from weakest to strongest evidence for "does X cause Y in people" (Content), each a card with an example from the cases. Tap a rung to see which case uses it.
- **Risk calculator** (small sandbox): two steppers, "cases per 1,000 without" and "with" (0 to 100). It shows relative risk ("2 times the risk", "+100 percent") beside absolute ("1 more person in 1,000") and draws two 1,000-dot grids.

## Content

### Reason chips
**In animals or cells**, **A link, not a cause**, **Too few people**, **No comparison group**, **Seller made or paid for it**, **Picked one result**, **Scary relative risk**, **No real source**, and **It holds up**.

### Study ladder (weakest to strongest)
1. A story or testimonial ("It worked for me"). 2. Lab or animal study. 3. Observational study (watches people, finds links). 4. Randomized controlled trial (people randomly given it or not). 5. Review of many good studies.

### Cases (hop 1 is the post; the last hop is the source; "new" is highlighted, "lost" is struck)
1. **Just vapor** (Not supported; pins: hop 2 or hop 3; reasons: No real source, Seller made or paid for it)
   - Hop 1, post (@cloudchaser_z, 48K likes): "Vapes are just flavored water vapor. Zero harm." New: "Zero harm".
   - Hop 2, shop page (Mist Theory Vapor Lounge, made up): "Our smooth, water-based vapor." Who gains: sells vapes. Lost: none.
   - Hop 3, source search: "No study cited. The shop's page links to nothing."
   - Case file, real facts: e-cigarette aerosol is not harmless water vapor; it can contain nicotine, ultrafine particles, flavorings such as diacetyl, cancer-causing chemicals and heavy metals such as nickel, tin and lead. Most vapes contain nicotine, which is highly addictive and can harm the developing teen brain. Honest version: "Vape aerosol is not just water vapor, and most of it carries nicotine."
2. **Coffee and a longer life** (Overstated; pins: hop 2 or hop 3; reasons: A link, not a cause)
   - Hop 1, post (@lifehack_daily): "Science says: drink coffee, live longer." New: "drink coffee, live longer". Lost: "linked", "adults 50 to 70".
   - Hop 2, news (DailyBuzz Health, made up): "Coffee drinkers live longer, huge study finds." New: "live longer". Lost: "linked to", "lower risk of dying during the study".
   - Hop 3, press release (Northfield University, made up): "Coffee drinking linked to lower risk of dying in large study of older adults."
   - Hop 4, study: 300,000 adults aged 50 to 70, surveyed once about coffee, followed 12 years; compared with non-drinkers; measured deaths; those drinking 2 to 3 cups a day had about a 10 percent lower risk of dying during the study; paid for by a government health agency (made up); observational. The authors write that coffee drinkers also differed in other ways.
   - Honest version: "In a big study of older adults, coffee drinkers died a little less often over 12 years. It shows a link, not that coffee caused it, and says nothing about teens."
3. **Muscle powder** (Not supported; pins: hop 3; reasons: Seller made or paid for it, No comparison group, Too few people)
   - Hop 1, post (@liftwithjay, "use my code"): "TitanBuild = 3x faster muscle gains. Clinically proven." New: "3x faster", "Clinically proven". Lost: "pilot", "10 men".
   - Hop 2, product page (TitanBuild, made up): "Clinically proven to triple muscle growth.*" Fine print: "*Based on a pilot study." Who gains: sells the powder.
   - Hop 3, study: 10 young men, 8 weeks of weight training while taking the powder; no comparison group; gained an average of 1.2 kg of lean mass; "3x" compares this with 0.4 kg from an unrelated older study; paid for by TitanBuild's maker; a company report, not a reviewed journal.
   - Case file, real facts: the FDA does not review dietary supplements for safety or effectiveness before they are sold; most teens can get the protein they need from food. Honest version: "Ten men who lifted for 8 weeks while taking the powder gained some muscle. With no comparison group, we can't tell what the powder added."
4. **Sweetener doubles your risk** (Overstated; pins: hop 1 or hop 2; reasons: Scary relative risk, A link, not a cause)
   - Hop 1, post (@cleanlivingclub): "Zentrose DOUBLES your risk of kidney stones. Stop drinking diet soda now!" New: "DOUBLES", "Stop drinking diet soda now". Lost: "linked".
   - Hop 2, news (Metro Wellness Wire, made up): "Sweetener Zentrose linked to twice the risk of kidney stones." New: "twice the risk". Lost: "2 in 1,000", "1 in 1,000".
   - Hop 3, study: 20,000 adults followed 5 years; compared daily Zentrose drinkers with non-drinkers; kidney stones in 2 per 1,000 drinkers and 1 per 1,000 non-drinkers; observational; paid for by a university (made up). Zentrose is a made-up sweetener.
   - Honest version: "In one study, people who drank Zentrose daily had kidney stones a little more often: 2 in 1,000 instead of 1 in 1,000. It shows a link, not a cause."
5. **Broccoli reverses aging** (Overstated; pins: hop 2 or hop 3; reasons: In animals or cells)
   - Hop 1, post (@youngforever): "Eat broccoli, reverse aging. Scientists proved it." New: "Eat broccoli", "reverse aging", "proved". Lost: "mice", "compound".
   - Hop 2, blog (Glow Daily, made up; sells a "BX-7" supplement): "Broccoli compound turns back the clock." New: "turns back the clock". Lost: "in aging mice", "muscle".
   - Hop 3, press release (Lakeshore Institute, made up): "Compound found in broccoli improves muscle strength in aging mice."
   - Hop 4, study: 80 old mice, half given purified compound BX-7 by injection at a dose far above what food could provide, half not; 6 weeks; grip strength improved in treated mice; paid for by a research grant (made up); animal study.
   - Honest version: "A purified compound from broccoli helped old mice's muscles. It hasn't been tested in people, and broccoli itself wasn't tested." Real fact in the file: vegetables like broccoli are part of a healthy eating pattern anyway.
6. **Teens need more sleep** (Holds up; pins: none; reason: It holds up)
   - Hop 1, post (@nurse_ortiz_rhs, a made-up school nurse): "Teens need 8 to 10 hours of sleep a night. Your focus and mood will thank you."
   - Hop 2, article (Riverside Herald health page, made up): "How much sleep do teens need? 8 to 10 hours, says the CDC."
   - Hop 3, source: CDC, "About Sleep": teens 13 to 18 need 8 to 10 hours per 24 hours; CDC also reports that teens who don't get enough sleep are more likely to have trouble with attention, mood and schoolwork. Who gains: no product; a public health agency.
   - Honest version: the claim as posted.

### Pin and verdict rules
A pin is ✓ if the hop is in the case's pin list; a reason is ✓ if it is in the case's reasons. The case file always shows the full answer whatever the student chose. "It holds up" on case 6 with Holds up is fully ✓; any pin on case 6 is shown ✗ with "This chain kept the claim intact."

## Interactions in detail
- Trace it reveals one hop at a time with a 300 ms slide (instant with Motion off); **Show all hops** reveals the rest. Pins work only on revealed hops.
- Who gains? reveals per hop; the reveal stays for the case.
- Diff highlights appear only after the hop below is revealed (you can't compare with what you haven't seen); until then the hop shows its plain text and "Trace further to compare."
- Changing a pin or verdict after Close reopens the notes and hides the case file (so the file never disagrees with the notes on screen).
- Risk calculator: steppers clamp 0 to 100; "with" equal to "without" shows "no difference"; "without" 0 shows relative risk as "can't divide by zero: look at the absolute numbers".
- Keyboard: Tab order is the panel steps first, then the chain top to bottom; Enter pins or reveals.
- Nothing saved: no localStorage except the kit's Motion.
- Sizes: at 1366x768 the post and two hops, and the whole case-notes panel, are visible; the chain scrolls inside the stage. Under 900 px tall the case notes collapse each step to one line until tapped. At 375 wide the notes move below the chain with a sticky **Notes** button.

## Look
- `kit/theme-912.css` with its own accent `--brand` #ffe066 (highlighter yellow, the same color as the diff marks), `--brand-ink` #2a2200.
- Contrast: accent on panel #141b25 13.28:1, on sec-bg #18202b 12.58:1; brand-ink on accent 12.13:1 (the highlighted words are ink #2a2200 on #ffe066). Struck "lost" words in theme --muted (7.7:1 on sec-bg) with the label "Lost on the way". ✓ and ✗ in --ok and --warn with glyphs and words.
- The chain: hop cards on #18202b with a 2 px left rule colored by source kind (post #c9a0ff, news #5aa9ff, product page #ff8a8a, press release #5fd39a, study #e8edf3), each also labeled in words.
- Group siblings: body-systems-tour orange, growing-up-q-a mauve, first-aid-responder mint, meal-and-move-planner sky blue. 9-12 neighbors: fitness-program-designer lime, captain-s-choices coral; satire-decoder oxblood.

## Art
none: drawn in code (social card, hop cards, study card, link lines, dot grids). Handles get a colored initial circle, no avatars.

## Voice
`casual-peer` (Zubenelgenubi): "Say casually and naturally, like a friendly teenager explaining something." Different from first-aid-responder (firm-captain), meal-and-move-planner (easy-coach), fitness-program-designer (calm-professor).
| Key | Kind | Line | Stale when |
|---|---|---|---|
| wCases | how | Pick a case. Tap Trace it to follow the claim back to where it started. | mode left |
| wTool | how | These are the questions to ask any health claim. Tap a card or try the risk calculator. | mode left |
| howPin | how | Tap Pin on the hop where the claim changed, then pick a reason. | a pin placed |
| howClose | how | Pick a verdict, then tap Close the case. | case closed |
| closed | event | Case closed. Here's what the source really showed. | case left or reopened |
Hop texts, study cards and case files are read on screen; Read speaks the newest revealed hop, the open case file or the hint.

## Family engine
none

## Sources
- NHES 2024 (SHAPE America), Standard 3: https://www.shapeamerica.org/standards/health/
- Questions to ask and checking who runs and pays for a source: MedlinePlus, "Evaluating Internet Health Information": https://medlineplus.gov/webeval/webeval.html ; NCCIH, "Finding and Evaluating Online Resources": https://www.nccih.nih.gov/health/finding-and-evaluating-online-resources
- Study types, animal and lab studies vs people, observational vs randomized trials, link vs cause, relative vs absolute risk: NCCIH, "Know the Science": https://www.nccih.nih.gov/health/know-science
- FDA doesn't review supplements before sale; most people can get nutrients from food: NIH ODS, "Dietary Supplements: What You Need to Know": https://ods.od.nih.gov/factsheets/WYNTK-Consumer/
- Vape aerosol contents, nicotine in most vapes, addiction and teen brain: CDC, "E-Cigarettes and Youth: What Parents Need to Know" and "Health Effects of Vaping": https://www.cdc.gov/tobacco/e-cigarettes/
- Teen sleep 8 to 10 hours and effects of too little sleep: CDC, "About Sleep": https://www.cdc.gov/sleep/about/index.html ; CDC, "Sleep and Health" (schools): https://www.cdc.gov/healthy-schools/sleep/
- Vegetables in a healthy eating pattern: Dietary Guidelines for Americans: https://www.dietaryguidelines.gov/
- All case people, handles, outlets, products, sweetener Zentrose, compound BX-7 and studies 2 to 5 are made up and labeled so on screen.

## Done when
1. All six cases open; Trace it reveals hops one at a time; hop counts are 3, 4, 3, 3, 4, 3.
2. Highlights and "Lost on the way" lines match Content and appear only after the hop below is revealed.
3. Close the case is disabled until a pin (or It holds up) and a verdict are set; the case file marks each choice ✓ or ✗ against the case's lists.
4. Case 6 with It holds up and Holds up shows every choice ✓; a pin on case 6 shows ✗ with its line.
5. Changing a choice after closing hides the case file again.
6. Risk calculator: 1 and 2 per 1,000 shows "2 times the risk", "+100 percent" and "1 more person in 1,000"; 0 without shows the divide-by-zero line.
7. Nothing persists after reload except Motion.
8. At 1366x768 the post, two hops and the full notes panel are visible; at 375 wide the Notes button reaches the notes; keyboard alone can trace, pin, judge and close a case.
9. The made-up line shows in both modes; no real brand, outlet or product name appears anywhere.

## Open questions
1. The vaping case uses CDC facts and a made-up shop. Vaping is a topic parents may want to preview; keep it as case 1, or move it later in the shelf?
