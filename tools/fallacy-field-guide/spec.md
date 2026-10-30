# Fallacy Field Guide

## One idea
Every fallacy has a harmless lookalike that uses the same move fairly (an expert who really is one, a choice that really has two sides), and a species card in your field guide only counts as confirmed once you have spotted the fallacy in the wild and also correctly let its lookalike go.

## Not like
- logic-gym (ela 7, family sibling, not built): quick arcade rounds on whether evidence is relevant and sufficient, with streaks. Here there is no clock and no streak; the subject is telling a fallacy from its fair twin, and the reward is a confirmed card.
- rhetoric-spotter (ela 9): sorts real speech lines by appeal. Appeals there are tools, not faults; here the question is whether the reasoning holds.
- argument-map (ela 12): tests which claims hold up an essay. Here each specimen is a short, single move of reasoning.
- ad-agency (ela 12): runs an agency that uses persuasion techniques and then audits them. Here nothing is made or sold; specimens are found and named.
- fake-or-fact-lab (ela 6-8): asks who is behind a page and checks it elsewhere. Here the source doesn't matter; the reasoning on the page is the specimen.
- satire-decoder (ela 11): separates what a text says from what it means. Here the text means what it says, and the test is whether its reasoning follows.

## Who and how
- Grade 10 ELA. Module: Evaluating Arguments and Fallacies (Reading Informational Text), "Validity of reasoning; false statements and fallacies".
- Driver: students on laptops, alone or in pairs; a teacher can project one habitat and have the class call each specimen. 25 to 40 minutes (four habitats of six specimens).
- Standards: RI.9-10.8 (delineate and evaluate the argument and specific claims in a text, assessing whether the reasoning is valid and the evidence is relevant and sufficient; identify false statements and fallacious reasoning): Field (spot, name, or release as legit), the test questions, and Make one.
- tool.json: driver "students or teacher", minutes "25-40", modes ["Field", "Guide", "Make one"], grades_label "Grade 10". Kit starter plus `kit:fallacies`.

## Screens and modes
Header: title "Fallacy Field Guide", small line "Spot it. Then tell it from its twin."; mode buttons **Field** (opens first), **Guide**, **Make one**; Motion, Sound, Read.

### Field (opens first)
- Focus: the habitat with its six specimens, filling the stage, and the selected specimen enlarged and outlined in it; the field kit is in the panel beside it.
- Habitat tabs along the top: **Ad board**, **Comment section**, **Headlines**, **Group chat**. Each habitat shows its six specimens in its own made-up look: posters drawn in code pinned to a painted corkboard (art: habitat-cork); a comment thread under a made-up news story about a skatepark (code); a feed of headlines and posts (code); a chat drawn in code inside a painted phone (art: habitat-phone). Specimens are numbered (F1 to F24).
- Panel: `#hint`; the **Field kit**: eight species buttons with their glyphs, plus **Legit**; **Field test**; the current specimen's status.
- To log a sighting: tap a specimen to select it, then tap the words where the reasoning goes wrong (the field mark: tap the first and last word). Then choose a species, or **Legit**. Choosing Legit asks one more thing: "It looks like which species?" (the lookalike it resembles).
- **Log sighting** checks: the words must overlap at least half of the key's field-mark words and the species (or Legit plus the right lookalike) must match. A right call shows "Logged" with a one-line field note (Content) and stamps the specimen. A miss shows what doesn't fit without giving the answer ("This does name a real expert. Is the expert's field the one the claim is about?") and the student may try again; a second miss offers **Show me** (the key and note; the sighting is not counted).
- **Field test** (any time on a selected specimen): shows the test question of the species the student is considering, with **Yes** and **No**, and what each answer suggests. It never says the answer.
- Each habitat footer: "Logged 4 of 6".

### Guide
- Focus: the eight species cards, each led by its painted animal plate.
- The field guide book: eight species cards in two rows. Each card has its painted plate (art: species kit), its glyph, name, also-called names, two field marks, its legitimate lookalike, its test question, and a sightings count. Card states: **Unseen** (the plate as a flat dark silhouette, name only), **Spotted** (the fallacy has been logged at least once), **Confirmed** (spotted, and its lookalike specimen correctly logged as Legit). Confirmed cards get a painted pressed flower (art: pressed-flower) and the word "Confirmed".
- Tapping a card opens it full size with the specimens where it was seen, each with **Go to it**.
- Guide footer: "Confirmed 3 of 8. Spotted 6 of 8."

### Make one
- Focus: the two slips side by side, the largest thing on the stage.
- Pick a species card (any state). Two blank specimen slips: **The fallacy** and **Its fair twin**. The student writes one of each on a topic of their choice (examples offered as chips: lunch rules, a phone plan, a sports team, a video game), then marks the field mark on each with the same tap method.
- **Field test it**: walks the student through the species' test question on both slips with Yes and No buttons, and shows "Your twin passes the test" or "Your twin still fails the test: look at the field mark again" from the student's own answers.
- Slips stay on this device (localStorage) with **Clear my slips**.

## Content
All specimens are original, written for this tool; every brand, person and place is made up. Species definitions are paraphrased from Dowden, "Fallacies", Internet Encyclopedia of Philosophy (Sources); the lookalike idea follows that article's notes that most appeals to authority are not fallacious and that correlation is often good evidence.

### Species (glyph, name, also called, field marks, lookalike, test question)
- ◆ **Ad hominem** (attacking the person). Marks: the reply is about the speaker, not the reasons; the trait named has nothing to do with the claim. Lookalike: questioning a source's reliability for a reason that bears on the claim (who paid for the study). Test: "Would this point about the person change whether the reasons are true?"
- ▲ **Straw man**. Marks: the other side's view is restated in a weaker or sillier form; the reply attacks that version. Lookalike: a fair summary the other side would accept. Test: "Would the other side say 'yes, that's what I mean'?"
- ■ **Black-or-white** (false dilemma). Marks: only two options are offered; other reasonable options are left out. Lookalike: a real choice that truly has two options (a yes or no ballot). Test: is "the limited menu fair or unfair" (Dowden)? Asked as: "Are there really only these two choices?"
- ● **Slippery slope**. Marks: a chain of "then... then..." ending in disaster; the steps are not supported. Lookalike: a chain where each step is supported by evidence. Test: "Is there a reason given for each step, and is the ending likely?"
- ✚ **Hasty generalization**. Marks: a claim about all or most from one or two cases. Lookalike: a generalization from a large, randomly chosen sample. Test: "How many cases, and were they chosen fairly?"
- ★ **Unqualified authority**. Marks: a famous or titled person backs a claim outside their field. Lookalike: an expert speaking within their field. Test: "Is this person an expert on this exact question?"
- ◗ **Bandwagon**. Marks: a claim is said to be right because many people believe or buy it. Lookalike: popularity cited where popularity is the point (crowds on a busy trail). Test: "Is the claim about how popular something is, or about whether it is good or true?"
- ◇ **Post hoc** (false cause). Marks: B came after A, so A caused B; no other cause considered. Lookalike: a cause shown by a fair comparison (a trial with a control group). Test: "Was anything else different, and was there a comparison?"

### Specimens (id, habitat, text, field-mark words, key, field note)
Ad board
- F1 "Everyone at Westbrook High is switching to GlowCase phone cases. Don't be the last one with a boring phone." Mark: "Everyone at Westbrook High is switching". Bandwagon. Note: how many people switch says nothing about whether the case is good.
- F2 "Pro skater Dax Rivera says FocusMint gum boosts your test scores. Ask for it by name." Mark: "Pro skater Dax Rivera says". Unqualified authority. Note: a skater is not an expert on memory or tests.
- F3 "Our town's children's dentists, who see 4,000 kids a year, recommend sealants on back teeth." Mark: "children's dentists, who see 4,000 kids a year, recommend". Legit, lookalike of Unqualified authority. Note: dentists speaking about teeth are in their field.
- F4 "Give $20 to the Clean Creek Fund, or admit you don't care about our river." Mark: "or admit you don't care about our river". Black-or-white. Note: you can care about the river and give nothing, or give elsewhere.
- F5 "The ballot has two choices on the library levy: yes or no. Read both arguments before you vote." Mark: "two choices on the library levy: yes or no". Legit, lookalike of Black-or-white. Note: a levy vote really has two options.
- F6 "Since I started wearing my lucky socks, our team has won four games straight. These socks work." Mark: "Since I started wearing my lucky socks". Post hoc. Note: winning came after the socks; nothing shows the socks did it.
Comment section (under a made-up story: "Ridgeway council weighs a skatepark open 8 a.m. to 8 p.m. with posted rules")
- F7 "Why listen to Councilmember Ortiz about the skatepark budget? She can't even skate." Mark: "She can't even skate". Ad hominem. Note: skating skill has nothing to do with a budget.
- F8 "Before we trust that noise study, note it was paid for by the company that wants to build the park." Mark: "paid for by the company that wants to build the park". Legit, lookalike of Ad hominem. Note: who paid for a study bears on how much to trust it; it is a reason to check, not a smear.
- F9 "So the skatepark people want kids to run wild all night with no rules. No thanks." Mark: "want kids to run wild all night with no rules". Straw man. Note: the plan says 8 to 8 with posted rules.
- F10 "If I understand the plan, the park would be open 8 to 8 with posted rules and no staff on site. My worry is the no-staff part." Mark: "open 8 to 8 with posted rules and no staff on site". Legit, lookalike of Straw man. Note: an accurate summary, then a real objection.
- F11 "First a skatepark, then they'll want a BMX track, then a stadium, and soon there won't be a blade of grass left in Ridgeway." Mark: "then a stadium, and soon there won't be a blade of grass left". Slippery slope. Note: no reason is given for any step after the first.
- F12 "My cousin went to a skatepark once and broke his wrist. Skateparks are a hospital trip waiting to happen." Mark: "My cousin went to a skatepark once". Hasty generalization. Note: one case can't show what usually happens.
Headlines
- F13 "Bridge repairs will close Elm Street Bridge for six weeks. The transit office says the detour adds 3 miles, so Route 9 will miss its connection at Central Station." Mark: "the detour adds 3 miles, so Route 9 will miss its connection". Legit, lookalike of Slippery slope. Note: each step has a stated reason from the office that runs the buses.
- F14 "A survey of 1,200 randomly chosen county residents found that 58 percent use the library at least once a month." Mark: "1,200 randomly chosen county residents". Legit, lookalike of Hasty generalization. Note: a large random sample.
- F15 "Millions of people can't be wrong: VitaBlast is the country's top-selling energy drink." Mark: "Millions of people can't be wrong". Bandwagon. Note: sales show popularity, not that it is good for you.
- F16 "Pine Ridge Trail is the most-hiked trail in the park on weekends, so expect crowds and start early." Mark: "most-hiked trail in the park on weekends, so expect crowds". Legit, lookalike of Bandwagon. Note: the claim is about crowds, so popularity is the right evidence.
- F17 "Attendance fell after the new principal arrived in September. She is driving students away." Mark: "fell after the new principal arrived". Post hoc. Note: autumn colds, schedule changes and more could explain it; nothing was compared.
- F18 "In a trial, 200 students were split at random. The group that got reminder texts turned in 20 percent more homework than the group that didn't." Mark: "200 students were split at random". Legit, lookalike of Post hoc. Note: a random split with a comparison group.
Group chat (friends planning a movie night)
- F19 "Don't listen to Maya about the movie, she still watches cartoons." Mark: "she still watches cartoons". Ad hominem.
- F20 Jae: "Can we skip the arcade this time? I'm low on money." Reply: "So Jae thinks having fun is a waste of money. Okay, grandpa." Mark: "So Jae thinks having fun is a waste of money". Straw man.
- F21 "Either we make the 7:00 show or the whole night is ruined." Mark: "or the whole night is ruined". Black-or-white.
- F22 "The last two movies I saw at that theater were sold out. That place sells out every night." Mark: "The last two movies I saw at that theater were sold out". Hasty generalization.
- F23 "My uncle's a dentist and he says this movie's ending is the best ever made." Mark: "My uncle's a dentist and he says". Unqualified authority. Note: the uncle may be right, but being a dentist doesn't make him an expert on endings.
- F24 "If we let Sam pick the snacks once, he'll pick every time, then he'll pick the movie, and we'll never see anything good again." Mark: "he'll pick every time, then he'll pick the movie". Slippery slope.
Each species has two fallacy specimens and one lookalike: Ad hominem F7, F19 / F8; Straw man F9, F20 / F10; Black-or-white F4, F21 / F5; Slippery slope F11, F24 / F13; Hasty generalization F12, F22 / F14; Unqualified authority F2, F23 / F3; Bandwagon F1, F15 / F16; Post hoc F6, F17 / F18.

## Interactions in detail
- Overlap rule: the student's marked words must cover at least half of the key's field-mark words (rounded up), and may include up to 5 words outside it. A mark too wide (more than 5 extra words) gets "Narrow it to where the reasoning goes wrong." At 5, no specimen can be logged by marking its whole text.
- A logged specimen can be reopened; changing a logged call removes it from the counts until logged again.
- Card states recompute from logged sightings; a card never loses Confirmed once earned in a session unless **Reset field guide** (asks first).
- Make one: each slip needs at least 8 words and a marked field mark before Field test it is enabled.
- Storage `fallacy-field-guide:v1` (try/catch): sightings, card states, slips.
- Mode and habitat changes call `V.hush()`.
- A tap while a stamp lands or a card flips to Confirmed (400 ms) acts at once: the animation jumps to its end and the tap works.
- Sizes: at 760 and below the field kit becomes a bottom sheet with species in a 3-column grid; at 375 the guide shows one card per row. At 680x425 a full specimen and the kit buttons are visible without scrolling. No horizontal scroll at any listed size.

## Look
- Plates in ink and soft watercolor on cream, earthy greens and browns, the way an old field guide prints them. Own light `:root`, a naturalist's field guide: `--paper #efe9d4` (khaki cloth), `--panel #faf6e8`, `--ink #23220f`, `--muted #57553a`, `--line #cfc7a6`, accent `--brand #5c5c08` (field-guide olive: header rule, Log sighting, card spines, active tab), `--btn #5c5c08`, `--btn-line #8f8a66`, `--head-ink #ffffff`, `--focus #1f5fa8`. Legit stamp `#1d6b3e` with "Legit"; fallacy stamp `#a3261b` with the species name. Each species has its glyph everywhere it appears. Habitats keep their own made-up looks inside a frame so they never look like the tool's chrome.
- Neighbors: rhetoric-spotter electric blue, thesis-workshop slate indigo, theme-ledger wine, research-notebook fountain-pen blue. Nearest catalog accents: decision-tree `#4a6417` (dE 12.9; greener) and stress-toolkit (16.6), neither in ELA.
- Contrast (WCAG 2.1): white on brand 7.02:1; brand on paper 5.78:1, on panel 6.49:1; ink on paper 13.22:1; muted on paper 6.25:1, on panel 7.02:1; focus on paper 5.30:1; Legit green on panel 6.02:1; fallacy red on panel 6.81:1. All pass AA.

## Art
Local FLUX (`scripts/localart.py`), one naturalist field-guide style (ink and soft watercolor on cream), asked in one session. No people: chat names and commenters keep letter avatars. Every specimen's words stay in code, because the student taps them.
- Species plates (kit of 8 cutouts, one shared prompt): "<animal>, a naturalist field-guide plate, fine ink lines and soft watercolor, plain cream background"; 1:1; cutout yes; people no; the top of each Guide card (about half its height), small beside each species button in the Field kit, and as a dark silhouette for Unseen cards. Each animal fits its species: Ad hominem "a hissing goose with its neck stretched forward"; Straw man "a straw scarecrow on a wooden pole with a plain burlap sack head and straw tufts for arms"; Black-or-white "a black and white magpie on a fence post"; Slippery slope "a garden snail sliding down a wet, tilted leaf"; Hasty generalization "a brown hare in full sprint"; Unqualified authority "a peacock with its tail fanned in full display"; Bandwagon "a row of ducklings following one another"; Post hoc "a rooster crowing on a fence rail at sunrise".
- pressed-flower: "A single pressed and dried wildflower lying flat, faded purple petals and a thin stem, a naturalist field-guide plate, plain cream background"; 1:1; cutout yes; people no; the Confirmed stamp on a card corner, rotated a few degrees.
- habitat-cork: "A full-frame close view of a cork bulletin board with a few brass pushpins, evenly lit"; 16:10; cutout no; people no; Ad board background, with the six posters drawn in code and pinned on it.
- habitat-phone: "A smartphone seen straight from the front, a plain black glass screen with a thin bezel, plain white background"; 9:16; cutout yes; people no; the frame of the Group chat habitat, with the chat drawn in code inside the screen area.
11 images, none with people. Drawn in code: specimen texts and posters, the comment thread, the headline feed, chat bubbles, letter avatars, glyphs, buttons and the cards' text.

## Voice
Bank voice `gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old ranger who keeps a field guide in his pocket." Not used by any neighbor or another tool in this batch. `Curio.voice`, `scope: () => state.mode + state.habitat`. Event line ids: logged, confirmed, miss.
- w-field (how, welcome on Field; stale when a specimen is tapped): "Tap a specimen. Then tap the first and last word where the reasoning goes wrong."
- pick (how, the first time a mark is made; stale when a species or Legit is tapped): "Now tap a species in your field kit, or tap Legit. Then tap Log sighting."
- legit (how, the first Legit choice; stale when a lookalike is picked): "Legit ones still look like something. Tap the species it resembles."
- miss (event, each missed call; stale when the mark or call changes): "Not quite. Read the note, or tap Field test."
- logged (event, each right call; stale on specimen change): "Logged."
- confirmed (event, each card turning Confirmed; stale on mode change): "{species}: confirmed. You can tell it from its twin."
- w-guide (how, welcome on Guide; stale when a card is tapped): "Your field guide. A card is confirmed when you've caught it and let its twin go. Tap a card to open it."
- w-make (how, welcome on Make one; stale when a species is picked): "Tap a species card. Then write one fallacy and its fair twin, and tap Field test it."
- Read speaks the hint, which names the next control (a specimen, the words, a species or Legit, then Log sighting).

## Family engine
`kit/fallacies.js` (the fallacies family: logic-gym, grade 7; fallacy-field-guide, grade 10). No family doc exists; this spec holds the full description. Pure parts in one marked block, exposed as `__tool.fx`.
- **Species catalog**: `{id, glyph, name, aka:[], marks:[], lookalike, test:{question, yes, no}}`. A tool may pass a subset; logic-gym can add `relevance` and `sufficiency` checks as species-like categories.
- **Specimens**: `{id, habitat, text, mark:[start,end], key: speciesId|{legit: speciesId}, note}`; the text may carry a speaker line (`who`) and a context line.
- **Spot**: `fx.spot(specimen, picked:[start,end], call)` returns `{ok, markOk, callOk, why}` using the overlap rule (at least half of the key's words, rounded up, at most `extra` outside, default 5) and the call match; `why` is a hint keyed to the miss (wrong species, legit called fallacy, fallacy called legit, mark off).
- **Field test**: `fx.test(speciesId)` returns the question and what yes and no suggest; it never reads the key.
- **Guide**: `fx.cards(sightings)` returns each species' state (`unseen`, `spotted`, `confirmed`) and count.
- **Habitats**: renderers for `board`, `thread`, `feed`, `chat`, each with its own look; specimens render inside them.
This tool uses all of it, with the eight species and 24 specimens above.

## Sources
- Species definitions and the lookalike notes (most appeals to authority are not fallacious; correlation is often good evidence; the black-or-white "limited menu is fair or unfair" test): Bradley Dowden, "Fallacies", Internet Encyclopedia of Philosophy, https://iep.utm.edu/fallacy/ (paraphrased; one short quotation, credited).
- All specimens, brands, people and places (Westbrook High, GlowCase, FocusMint, Dax Rivera, Clean Creek Fund, Ridgeway, Councilmember Ortiz, VitaBlast, Pine Ridge Trail) are made up for this tool.
- Checks run (Python, 2026-10-29): all 24 field marks appear word for word in their specimen texts; marks run 4 to 13 words, so "half, rounded up" needs 2 to 7. Each species has two fallacy specimens and one lookalike (8 x 3 = 24). Worst case, marking a whole specimen: with the old limit of 6 extra words, F3, F9, F21 and F22 could be logged that way (exactly 6 extra each); at 5 none can, so the limit is now 5 and the Done when check uses 6 extra words. Contrast ratios in Look recomputed with the WCAG 2.1 formula; all match to 0.01.

## Done when
- All 24 specimens appear in their four habitats, each in its own look.
- Logging F3 as Legit with lookalike Unqualified authority counts; logging it as Unqualified authority gives the "real expert... their field" hint.
- A mark covering less than half of a key mark misses with "where the reasoning goes wrong"; a mark with 6 extra words gets "Narrow it"; marking the whole text of F3, F9, F21 or F22 gets "Narrow it".
- Logging F2 makes Unqualified authority Spotted; then logging F3 correctly as Legit makes it Confirmed.
- Field test shows the selected species' question with Yes and No and never reveals the key.
- Make one runs the test on two student slips and reports from the student's answers.
- Sightings and slips survive a reload; Reset field guide asks first.
- At 375 wide the kit is a bottom sheet and nothing scrolls sideways; at 680x425 a specimen and the kit show together.
- Focus: at 1366x768 and 680x425 the selected specimen is the largest, outlined item in its habitat, and each Guide card shows its painted plate (a silhouette while Unseen).
- Tap while it plays: tapping another specimen or mode while a stamp lands acts at once, with no stale line.
- Every waiting line names its control; "Logged." plays on every right call.

## Open questions
- None beyond the group's shared ones.
