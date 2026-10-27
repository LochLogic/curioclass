# Fake or Fact Lab

## One idea
Every made-up page or post is tested twice, the way a lab runs a control: first you may only read the page itself and must call it, then you leave it and open new tabs to see what the rest of a made-up web says about it, and your lab table shows, in your own data, how often the page's own polish fooled the inside read and how the outside read (lateral reading) did.

## Not like
- misleading-charts (6-8 CS, wave 1): the numbers are true and the drawing lies; checked with a ruler. Here nothing is measured on the page: the question is who is behind it and what other sources say, answered by leaving it.
- phishing-spotter (6-8 CS, wave 1): seconds-long keep or report calls on messages aimed at you, tells found on the message itself. Here the lesson is the opposite move: the page itself can't be trusted to tell you, so you look elsewhere, slowly.
- health-claim-checker (9-12 health, wave 1): health claims checked against evidence. Here no specimen is about health, and the method (inside read against outside read) is the subject.
- satire-decoder (ela 11, test batch): proves what one text really means. Here the text's meaning is plain; its source is in question.
- research-quest (6-8, this group): a research story where earlier choices come back at the end. Here each specimen is a short, separate experiment.
- fact-check-desk (ela 8) and ad-agency (ela 12), family siblings not built: they share this tool's engine (below) with different content.
- Source Sorter (ela 6, research family, not built): sorts finished sources by credibility from what they show. Here showing is not enough; the verdict must come from outside the page.

## Who and how
- Grades 6 to 8, library. Module: Is It Reliable? (Research), "Evaluate websites, authors and evidence; spot misinformation".
- Driver: students on laptops, alone or in pairs; a teacher can run specimen 1 on a projector with a class vote at each verdict. 25 to 40 minutes (six specimens at about 5 minutes, then the report).
- Standards: AASL.Curate (IV.B.3 systematically questioning and assessing the validity and accuracy of information), AASL.Engage (VI.A.3 evaluating information for accuracy, validity, social and cultural context).
- tool.json: driver "students or teacher", minutes "25-40", modes ["Lab", "Report"], grades_label "Grades 6-8". Kit starter plus `kit:fact-check`.

## Screens and modes
Kit frame, own `:root` (a clean lab bench). Header: title "Fake or Fact Lab", small line "Read inside. Then read outside."; mode buttons **Lab** (flask icon, opens first), **Report** (table icon); Motion, Sound, Read.

### Lab (opens first)
Specimen tray across the top: six specimen jars, "S1" to "S6", each labelled with its kind (site, post, article, blog) and a state: "New", "Inside done", "Tested". Any specimen opens in any order.
Stage: the engine's mock browser (tab strip, back button, read-only address bar, page area). The specimen opens in tab 1.
Panel, top to bottom: `#hint`; the **Pass** badge ("Pass 1: Inside read" on `--inside`, or "Pass 2: Outside read" on `--outside`); the **Notebook** (evidence cards, newest first); the **Verdict** buttons **Trust it**, **Partly true, stretched**, **Don't trust it**; then **Lock my call** (big).

Pass 1, Inside read: the student may scroll the page and follow links that stay on the same site (About us, other articles, the author's bio on that site). The new tab button "+", the search box, "Search this image" and "Who runs this site?" are shown locked with a padlock and the label "Pass 2". Things the page says about itself become notebook cards tagged "Inside" when tapped (the About text, a credential, a share count, a "studies show" line). Lock my call records the inside verdict and the seconds spent, then unlocks Pass 2.

Pass 2, Outside read: "+" opens a new tab on **Wayfind**, the made-up search engine (a search box and suggestion chips). On the specimen tab, images get a "Search this image" corner button and every page gets a "Who runs this site?" button (a site lookup card). Citation links can be followed to their source (**Trace**). Each result page that holds evidence adds a notebook card tagged with one of three questions: **Who's behind it?**, **What's the evidence?**, **What do other sources say?** Lock my call records the outside verdict and seconds.

Reveal (after the outside call): the **Expert check** card slides up over the bottom of the stage: the verdict professional fact-checkers reached (Content), two or three lines of why, and the row this specimen just added to the lab table (inside call, outside call, expert verdict, seconds and tabs for each pass). **Next specimen**.

### Report
The lab table: one row per tested specimen: specimen, inside call, outside call, expert verdict (each call marked ✓ match or ✗ no match, with the word), seconds inside, seconds outside, tabs opened. Under it, two counts: "Inside read matched the experts on [a] of [n]." and "Outside read matched on [b] of [n]." Then the conclusion card: "In a Stanford study, professional fact-checkers left an unfamiliar site quickly to see what others said about it, and judged sites more accurately than historians and college students who read the site closely." and the three questions as a takeaway strip. **Clear lab** (asks Yes / No) empties the table.

## Content
Every site, person, post and organization is made up. Addresses use reserved endings (`.example`, `example.org`), checked by the engine.

Verdict match rule (the tool's own): a call matches when it equals the expert verdict exactly.

S1, site: "Center for Smart Study", smartstudycenter.example.org. Inside: polished logo, "Independent. Nonpartisan. Research for families." banner; article "Study apps raise grades by 40%, research shows" citing "our 2025 family survey"; About: "A nonprofit research center helping families make smart choices about learning." Outside: Wayfind "Center for Smart Study" → Openpedia entry "Center for Smart Study: an advocacy group founded in 2024 by BrightPath Apps, maker of the StudyStar homework app" (card: Who's behind it?); Lakeshore Tribune article "Group praising study apps is funded by an app maker" (card: What do other sources say?); site lookup "Registered 2024 to BrightPath Apps, Inc." (card: Who's behind it?); Trace "our 2025 family survey" → survey page: "412 StudyStar customers asked if their grades went up" (card: What's the evidence?). Expert: **Don't trust it**. Why: "Run by a company that sells study apps. The 40% came from asking its own customers."

S2, post on Chirp (made-up social site) by @StormWatchNow (12,400 followers): photo ff-shark-street, text "Port Alder flooding RIGHT NOW. A shark swam down Main Street!! Share!!", 8,900 shares. Inside: the photo, the share count, the account's other posts (all weather alerts). Outside: Search this image → earliest copy "Street Shark, digital collage, 2019" on the portfolio of artist Rhea Lind, labelled "edited image" (card: What's the evidence?); Wayfind "Port Alder flooding" → Port Alder Gazette "Rain floods streets near the harbor" with photo ff-flooded-street, no shark (card: other sources); CheckPoint Desk (made-up fact-check site) "No, a shark did not swim down Main Street" (card: other sources); Wayfind "StormWatchNow" → no results tying the account to any weather service (card: Who's behind it?). Expert: **Don't trust it**. Why: "The flood was real. The shark photo is a 2019 art collage."

S3, article: Port Alder Gazette, portaldergazette.example, "Library to cut Sunday hours", by Marisol Vega, staff reporter, dated. Inside: plain old-fashioned layout, small photo ff-library-front, a hardware store ad, no share buttons. Outside: Openpedia "Port Alder Gazette: local newspaper, founded 1921" (Who's behind it?); Wayfind "Marisol Vega" → her other Gazette articles over six years (Who's behind it?); Wayfind "Port Alder library Sunday hours" → town council minutes on portalder.example: "Vote 4 to 1 to close the library on Sundays starting March 1" (What's the evidence?); Lakeshore Tribune brief reporting the same (other sources). Expert: **Trust it**. Why: "A long-running local paper, a named reporter and the council's own minutes agree. A plain design says nothing either way."

S4, site: "Daily Ledger Now", dailyledgernow.example, "BREAKING: Every school will switch to a four-day week next fall" by J. Carter, with a "Breaking" banner and 31,000 shares. Inside: slick news layout, "Trusted by millions" badge, author bio "J. Carter covers education". Outside: Wayfind "J. Carter education reporter" → no other articles anywhere (Who's behind it?); site lookup "Registered 3 weeks ago, owner hidden" (Who's behind it?); Wayfind "four-day school week next fall" → no other outlet or school district reports it, plus a Lakeshore Tribune piece "Some districts have tried four-day weeks; there is no national plan" (other sources). Expert: **Don't trust it**. Why: "A new site, an author with no other work, and nobody else reports it."

S5, blog: "Pixel Parent", pixelparent.example, "Scientists PROVE video games make kids smarter", linking "a new study". Inside: friendly blog, the author's bio "dad of three, gamer", the link. Outside: Trace the link → study page "Journal of Child Learning, 2024: Puzzle games and spatial skills in 200 children": "Children who played puzzle games more had slightly higher spatial test scores. This study cannot show that the games caused the difference." (What's the evidence?); Wayfind "puzzle games spatial skills study" → Lakeshore Tribune "Small study finds link between puzzle games and spatial skills" (other sources). Expert: **Partly true, stretched**. Why: "There is a real study, but it found a small link in one skill, not proof that games make kids smarter."

S6, blog: "Ms. Park's Pond Notes", parkpondnotes.example, a teacher's homemade blog with a hit counter and clip-art border: "Wood frogs freeze in winter and come back in spring!" with photo ff-wood-frog. Inside: odd-looking design, exclamation marks, no sources on the page. Outside: Openpedia "Wood frog: in the far north it freezes solid in winter, its heart stops beating, and it thaws in spring" (What's the evidence?); Northwoods Nature Center (made-up) page saying the same (other sources); Wayfind "Ms. Park pond notes" → Willow Creek Middle School staff page: science teacher (Who's behind it?). Expert: **Trust it**. Why: "Strange but true. Other sources agree, and the author is who she says she is."

Wayfind suggestion chips on each specimen's new tab: the site's name, the author's name, the claim's key words. Free search uses the engine's index (Family engine); a query with no match shows "No good results. Try the site's name, the author's name, or the claim's key words."

## Interactions in detail
- Locked Pass 2 controls stay visible so students see what they will get; tapping one says "That's for the outside read. Make your inside call first."
- Lock my call needs a verdict selected; it is disabled until then (`needs` on the how-to).
- Tabs: up to 8; a ninth "+" asks to close one. Back works per tab. Links never leave the page.
- The notebook adds a card only once per finding; cards show their tag icon and the word.
- Seconds are counted per pass while the tool is visible (paused when the page is hidden) and shown only in the reveal and report, never as a running clock.
- Reopening a tested specimen shows it read-only with its reveal; **Retest** clears that row and starts at Pass 1.
- The table saves in localStorage (`fofl-table`, try/catch); Clear lab (after Yes) empties it.
- Keyboard: panel before stage; verdicts 1, 2, 3; Enter locks. Visible focus.
- Sizes: page area, verdict buttons and Lock my call visible without scrolling at 1280x720 and 1366x768; at 680x425 the notebook collapses to a count chip that opens it; at 375 wide the browser stacks above the panel and the tab strip scrolls sideways.

## Look
- Accent `--brand #6d28d9` (lab violet, like a UV lamp that shows what the page hides: header, Lock my call, selected verdict ring). `--head-ink #ffffff`.
- Own `:root` (lab bench): `--paper #f4f6fb`, `--panel #ffffff`, `--ink #161b2e`, `--muted #545b70`, `--line #d9deea`, `--btn #6d28d9`, `--focus #b45309`; pass colors `--inside #ede9fe` (with the word "Inside") and `--outside #fef3c7` (with "Outside"). Verdicts: Trust it `#15803d` ✓, Partly `#a16207` ~, Don't trust it `#b91c1c` ✗, always with the word. Specimen pages keep their own made-up designs inside the browser frame so the tool's chrome never looks like a page.
- Neighbors: misleading-charts fuchsia #a21caf (redder), phishing-spotter lime #b6f23a, health-claim-checker yellow #ffe066, design-fixer indigo #4338ca (bluer), world-music-map plum #7a2e8a; the 6-8 blues (screen-week, workplace-scenarios, algorithm-audit) are avoided on purpose. Group siblings: olive, crimson, teal, brass, and orchid on boolean-builder's dark theme.
- Contrast: white on brand 7.10:1; brand on paper 6.57:1; brand on panel 7.10:1; ink on paper 15.79:1; muted on paper 6.25:1; focus on panel 5.02:1 and on paper 4.64:1; ink on inside 14.38:1; ink on outside 15.33:1; Trust green on white 5.02:1; Partly amber on white 4.92:1; Don't red on white 6.47:1. All pass AA.

## Art
- ff-shark-street: a large gray shark fin breaking the surface of brown floodwater in a city street lined with parked cars and shop fronts with blank signs, overcast sky, realistic photo look; 4:3; cutout no; people no; S2's post photo and, framed as "Street Shark, digital collage, 2019", the artist's portfolio page. FLUX.2 (`scripts/cfart.py`).
- ff-flooded-street: the same kind of city street flooded with brown water up to car doors, shop fronts with blank signs, overcast sky, realistic news photo; 4:3; cutout no; people no; the Gazette's real flood photo in S2's outside read. FLUX.2.
- ff-library-front: a small red-brick town library with white columns and a blank sign board, autumn trees, daytime; 4:3; cutout no; people no; S3's article photo. FLUX.2.
- ff-wood-frog: a brown wood frog with a dark eye mask sitting on frosty fallen leaves, close-up nature photo; 4:3; cutout no; people no; S6's blog photo. FLUX.2.
Logos, avatars (initials), browser frame, social post frame, encyclopedia pages, site lookup cards, specimen jars and the table are drawn in code.

## Voice
Bank voice `wise-mentor` (Gacrux), "Say thoughtfully and warmly, like a wise high school mentor": the patient voice of "slow down, then look elsewhere". Its only 6-8 wave user is relationship-spectrum (health), not a close neighbor; it differs from misleading-charts (news-reader), phishing-spotter (lively-host) and health-claim-checker (easy-coach). `Curio.voice`, `scope: () => state.mode`. Page text, results and expert notes are on screen only.
- w-lab (how): "Pick a specimen. First, read only the page itself. Then choose a verdict and press Lock my call."
- outside (how, first Pass 2): "Now leave the page. Press the plus to open a new tab and search the site, the author or the claim."
- tools (how, first Pass 2, after outside): "You can also tap Search this image, or Who runs this site."
- locked (how, first tap on a locked control): "That's for the outside read. Make your inside call first."
- expert (event, each reveal; stale on specimen change): "Here's what the fact-checkers found. Compare it with your two calls."
- w-report (how): "This is your lab table. Compare your inside reads with your outside reads."

## Family engine
`kit/fact-check.js` (the fact-check family: fake-or-fact-lab, fact-check-desk, ad-agency). This spec holds the full description; the siblings say what they feed it.
- **World**: a tool passes `{sites, people, posts, images, entries, index}`. Site `{domain, name, look, pages:[{path, kind, title, blocks}], lookup:{registered, owner|'hidden'}}`; person `{name, works:[urls]}`; post `{site:'chirp', handle, followers, text, image, shares}`; image `{id, copies:[{url, date, label}]}` (earliest first); entry (Openpedia) `{title, text}`. Every domain must end in `.example`, `example.org`, `example.com` or `example.net`; `fc.safeDomain(url)` checks it and logs a console error otherwise, so no real site slips in.
- **Browser**: tab strip (max 8), back per tab, read-only address bar, page renderer for kinds `article`, `about`, `post`, `profile`, `entry`, `search`, `imageSearch`, `lookup`, `document` (minutes, study pages). Each site renders with its own `look` (fonts, colors, logo shape) so pages differ from each other and from the tool chrome. Links never navigate the real window.
- **Locks**: `fc.lock(['newTab','search','image','lookup'])` and `fc.unlock()`; locked controls stay visible with a padlock and fire `onLocked`.
- **Search** (pure): `fc.search(query)` lowercases, drops little words (a, an, the, of, to, in, on, is, are, and, for) and returns index entries `{terms, results:[{title, url, snippet}]}` whose terms are all in the query, best overlap first; an empty list gives the tool's no-results line and suggestion chips. `fc.imageSearch(id)` returns the image's copies. `fc.lookup(domain)`.
- **Trace**: a link marked `cite` opens its target with the matching passage highlighted, or "This source doesn't say that." when the passage is missing.
- **Notebook**: `fc.note({id, text, tag, from})` adds a card once; tags `inside`, `who`, `evidence`, `others`. A page block can carry a `note` that is added when the block is seen or tapped.
- **Calls**: `fc.call(specimen, pass, verdict)` records verdict, seconds (visible time only) and tabs opened.
- Pure parts in one marked block, exposed as `__tool.fc`.
This tool uses: World (six specimens above plus Openpedia, Lakeshore Tribune, CheckPoint Desk, Port Alder town site, Rhea Lind portfolio, Journal of Child Learning, Northwoods Nature Center, Willow Creek Middle School), Browser, Locks (Pass 1), Search with the index terms named in Content, imageSearch (S2), lookup (S1, S4), Trace (S1, S5), Notebook, Calls.

## Sources
- AASL, National School Library Standards (2018), Standards Framework for Learners: Curate IV.B.3, Engage VI.A.3. https://standards.aasl.org/framework/
- Wineburg, S. and McGrew, S. (2019). "Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information." Teachers College Record 121(11). (Fact-checkers left sites to read laterally and judged more accurately than historians and students.)
- Digital Inquiry Group (formerly Stanford History Education Group), Civic Online Reasoning: the three questions "Who's behind the information? What's the evidence? What do other sources say?" https://cor.inquirygroup.org/
- Caulfield, M. "SIFT (The Four Moves)", 2019 (stop, investigate the source, find better coverage, trace claims to the original). https://hapgood.us/2019/06/19/sift-the-four-moves/
- ICANN Registration Data Lookup (what a domain lookup shows: registration date, registrant, often hidden). https://lookup.icann.org/
- National Park Service, Denali National Park, "Amphibians" (wood frogs freeze solid in winter, do not breathe and their hearts do not beat, and thaw in spring). https://www.nps.gov/dena/learn/nature/amphibians.htm
- All specimens, sites, people, studies and organizations are made up for Curio Class. The verdict match rule and the three-verdict scale are the tool's own choices.

## Done when
1. All six specimens open; in Pass 1 the new tab, search, image search and site lookup are locked and say so when tapped; same-site links work.
2. Every outside finding in Content can be reached (by its suggestion chip and by typing its terms) and adds its notebook card once, with the right tag.
3. Trace on S1 and S5 opens the source with the passage highlighted; Search this image on S2 lists the 2019 collage first; Who runs this site? on S1 and S4 shows the Content lookup.
4. Lock my call is disabled until a verdict is picked; each pass records verdict, seconds and tabs; the reveal shows the expert verdict and why.
5. Report counts match the table (recompute from `__tool.fc` calls); Clear lab (after Yes) empties it; the table survives a reload.
6. `fc.safeDomain` passes every address in the world; no real site, brand or person appears.
7. Page area, verdicts and Lock my call visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`; verdict keys 1 to 3 work.
8. Voice: welcome once per mode, how lines once, the expert line every reveal and dropped on specimen change; Read speaks the hint; console clean; no network requests; only "Curio Class".

## Open questions
- S2 shows a realistic edited photo (a shark in a flooded street) as the hoax. It is labelled as an art collage once found. Fine to generate and show, or swap for a less realistic fake?
