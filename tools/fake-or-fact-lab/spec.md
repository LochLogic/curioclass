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
- Standards: AASL.Curate (IV.B.3 systematically questioning and assessing the validity and accuracy of information), AASL.Engage (VI.A.3 evaluating information for accuracy, validity, social and cultural context); C3 D3.2.6-8 (judging a source's credibility from its relevance and intended use). CCSS ELA: W.6.8, W.7.8, W.8.8 (assess the credibility and accuracy of each source).
- tool.json: driver "students or teacher", minutes "25-40", modes ["Lab", "Report"], grades_label "Grades 6-8". Kit starter plus `kit:fact-check`.

## Screens and modes
Kit frame, own `:root` (a clean lab bench). Header: title "Fake or Fact Lab", small line "Read inside. Then read outside."; mode buttons **Lab** (flask icon, opens first), **Report** (table icon); Motion, Sound, Read.

### Lab (opens first)
Specimen tray across the top: six specimen jars, "S1" to "S6", each labelled with its kind (site, post, news story, blog; "news" when the screen is narrow) and a state: "New", "Inside done" ("Inside" when not wide), "Tested". The kinds never give away the answer: the trusted Gazette and the untrusted Zapline Now are both "news story". Under the tray one line: "Every page in this lab is made up for practice. Your calls are saved on this device only." (the second sentence drops on narrow screens). Any specimen opens in any order.
Stage: the engine's mock browser (tab strip, back button, read-only address bar, page area). The specimen opens in tab 1.
Panel, top to bottom: `#hint`; the **Pass** badge ("Pass 1: Inside read" on `--inside`, or "Pass 2: Outside read" on `--outside`); the **Notebook** (evidence cards, newest first); the **Verdict** buttons, each with its meaning under the word: **Trust it** ("The main claim holds, and the source is who it says."), **Partly true, stretched** ("A real fact is under it, but the claim goes further than the evidence."), **Don't trust it** ("The main claim is false, or the source hides who is behind it."); then **Lock my call** (big).

Pass 1, Inside read: the student may scroll the page and follow links that stay on the same site (About us, other articles, the author's bio on that site), except citation links: a cite link (the small ↗, such as S1's "our 2025 family survey") is a Pass 2 move (Trace) and is locked in Pass 1, even when its target is on the same site. The new tab button "+", the search box, "Search this image", "Who runs this site?" and cite links are shown locked with a padlock and the label "Pass 2". Things the page says about itself become notebook cards tagged "Inside" when tapped (the About text, a credential, a share count, a "studies show" line). Lock my call records the inside verdict and the seconds spent, then unlocks Pass 2.

Pass 2, Outside read: "+" opens a new tab on **Wayfind**, the made-up search engine (a search box and suggestion chips). On the specimen tab, images get a "Search this image" corner button and every page gets a "Who runs this site?" button (a site lookup card). Citation links can be followed to their source (**Trace**). Each result page that holds evidence adds a notebook card tagged with one of three questions: **Who's behind it?**, **What's the evidence?**, **What do other sources say?** Lock my call records the outside verdict and seconds. The outside call needs an outside move first: a new tab opened, or a lookup, image search or Trace that added an outside card; until then Lock my call stays disabled and the hint says "Your outside call needs an outside look first. Press the plus for a new tab."

Reveal (after the outside call): the card **What a fact-checker would find: Sx** (with Hide / Show) slides up over the bottom of the stage: "A fact-checker would say:" and the verdict (Content), the why, then "What decides it (your notebook has N of M)": the two or three deciding findings, each marked "You found this" or "Not in your notebook", and the row this specimen just added to the lab table (inside call, outside call, fact-checker, seconds and tabs for each pass). The footer says every page is made up for practice and the row is saved on this device only. In the panel, **Next specimen** is the big button; under it a small **Retest** with "Your first try stays in the lab table." Focus moves to Next specimen.

### Report
The lab table: one row per tested specimen: specimen, inside call, outside call, fact-checker (each call tagged "Matches" or "Doesn't match"; the ✓ ~ ✗ marks belong to the verdicts only), seconds inside, seconds outside, tabs opened outside. A retested specimen's row shows the first try with a "retested" tag. Under it, two counts: "Inside read matched the fact-checker on [a] of [n]." and "Outside read matched on [b] of [n]." Then one line that reacts to the student's own counts (for example "Your outside read matched 2 more times than your inside read. Which specimen fooled your inside read?"). With untested specimens left, the welcome adds "Press Lab to test the next specimen." Then the conclusion card: "In a Stanford study, professional fact-checkers left an unfamiliar site quickly to see what others said about it, and judged sites more accurately than historians and college students who read the site closely." and the three questions as a takeaway strip. **Clear lab** (asks Yes / No) empties the table.

## Content
Every site, person, post and organization is made up. Addresses use reserved endings (`.example`, `example.org`), checked by the engine.

Verdict match rule (the tool's own): a call matches when it equals the fact-checker's verdict exactly.

Every name below was web-searched before use and has no real match (the searches are listed in handoff.md). Reserved domains only.

S1, site: "Gloverly Study Institute", gloverlystudy.example.org. Inside: polished logo, "Independent. Nonpartisan. Research for families." banner; article "Study apps raise grades by 40%, research shows" citing "our 2025 family survey" (a cite link, locked in Pass 1); About: "A nonprofit research center helping families make smart choices about learning." Outside: Wayfind "Gloverly Study Institute" → Openpedia entry "The Gloverly Study Institute is an advocacy group founded in 2024 by Quillbop Apps, maker of the Gradewhistle homework app." (Who's behind it?); Glimmerlake Tribune article "Group praising study apps is funded by an app maker" (What do other sources say?); site lookup "Registered in 2024 to Quillbop Apps, Inc." (Who's behind it?); Trace "our 2025 family survey" → survey page: "412 Gradewhistle customers asked if their grades went up" (What's the evidence?). Fact-checker: **Don't trust it**. Why: "A study-app company runs this site to sell study apps. The 40% came from asking its own customers."

S2, post on Tweedlebeak (made-up social site) by Squallnook Alerts, @SquallnookAlerts (12,400 followers): photo ff-shark-street, text "Port Alder flooding RIGHT NOW. A shark swam down Main Street!! Share!!", 8,900 shares. Inside: the photo, the share count, the account's other posts (all weather alerts). Outside: Search this image → earliest copy "Street Shark, digital collage, 2019" on the portfolio of artist Rhea Lind, labelled "edited image" (What's the evidence?); Wayfind "Port Alder flooding" → Port Alder Gazette "Rain floods streets near the harbor" with photo ff-flooded-street, no shark (other sources); Truthlamp Fact Desk (made-up fact-check site, "Checking viral posts") "No, a shark did not swim down Main Street" (other sources); Wayfind "Squallnook Alerts" → only the account itself, nothing tying it to any weather service (Who's behind it?). Fact-checker: **Don't trust it**. Why: "The flood was real, but the post's news is the shark, and that photo is a 2019 art collage. The account names no source."

S3, news story: Port Alder Gazette, portaldergazette.example, "Library to cut Sunday hours", by Marisol Vega, staff reporter, dated. Inside: plain old-fashioned layout, small photo ff-library-front captioned "(file photo)", a Dockfiddle Hardware ad, no share buttons. Outside: Openpedia "Port Alder Gazette: a local newspaper in the town of Port Alder, founded in 1921" (Who's behind it?); Wayfind "Marisol Vega" → her Gazette staff page with articles from 2020 to 2026 (Who's behind it?); Wayfind "Port Alder library Sunday hours" → town council minutes on portalder.example: "Vote 4 to 1 to close the library on Sundays starting March 1" (What's the evidence?); Glimmerlake Tribune brief reporting the same (other sources). Fact-checker: **Trust it**. Why: "A long-running local paper that reports town news, a named reporter and the council's own minutes agree. A plain design says nothing either way."

S4, news story: "Zapline Now", zaplinenow.example, "BREAKING: Every school will switch to a four-day week next fall" by J. Carter, with a "Breaking" banner and 31,000 shares. Inside: slick news layout, "Trusted by millions" badge, author bio "J. Carter covers education". Outside: Wayfind "J. Carter education reporter" → no other articles anywhere (Who's behind it?); site lookup "Registered 3 weeks ago, owner hidden" (Who's behind it?); Wayfind "four-day school week next fall" → no other outlet or school district reports it, plus a Glimmerlake Tribune piece "Some districts have tried four-day weeks; there is no national plan" (other sources). Fact-checker: **Don't trust it**. Why: "A new site with a hidden owner, built to get shares. The author has no other work, and nobody else reports it."

S5, blog: "Pixelpuddle Parent", pixelpuddleparent.example, "Scientists PROVE video games make kids smarter", "Posted by the Pixelpuddle dad", linking "a new study". Inside: friendly blog, the author's bio "Dad of three, gamer.", the link (locked in Pass 1). Outside: Trace the link → study page "Quellmont Journal of Child Learning, 2024: Puzzle games and spatial skills in 200 children": "Children who played puzzle games more had slightly higher spatial test scores. This study cannot show that the games caused the difference." (What's the evidence?); Wayfind "puzzle games spatial skills study" → Glimmerlake Tribune "Small study finds link between puzzle games and spatial skills" (other sources). Fact-checker: **Partly true, stretched**. Why: "A fan blog cheering for games. There is a real study under it, but the study found a small link in one skill, not proof that games make kids smarter."

S6, blog: "Ms. Park's Pond Notes", parkpondnotes.example, a teacher's homemade blog with a hit counter and clip-art border: "Wood frogs freeze in winter and come back in spring!" with photo ff-wood-frog, and an "About me" card: "Hi! I teach science at Puddlewick Middle School. I love frogs!" Inside: odd-looking design, exclamation marks, no sources on the page, the About me claim. Outside: Openpedia "Wood frog: In cold winters, the wood frog freezes solid. Its heart stops beating. In spring it thaws, and its heart starts beating again." (What's the evidence?); Brambleskip Nature Center (made-up) page saying the same (other sources); Wayfind "Ms. Park science teacher" → Puddlewick Middle School staff page: science teacher (Who's behind it?). Fact-checker: **Trust it**. Why: "Strange but true. Other sources agree, and her school's staff page shows she teaches science there, as her page says."

Search folds words (plurals, the numbers 0 to 12, punctuation), so "4-day week", "sharks" and "libraries" find the same results as "four day week", "shark" and "library", and the one-word names (Gloverly, Quillbop, Gradewhistle, Squallnook, Tweedlebeak, Truthlamp, Zapline, Pixelpuddle, Quellmont, Brambleskip, Puddlewick, Glimmerlake) each find their page.

Wayfind suggestion chips on each specimen's new tab: the site's name, the author's name, the claim's key words. Free search uses the engine's index (Family engine); a query with no match shows "No good results. Try the site's name, the author's name, or the claim's key words."

## Interactions in detail
- Locked Pass 2 controls (and cite links) stay visible so students see what they will get; tapping one says "That's for the outside read. Pick a verdict, then press Lock my call."
- Lock my call needs a verdict selected; it is disabled until then (`needs` on the how-to). In Pass 2 it also needs an outside move (above).
- After the inside lock, focus moves to "+"; after the outside lock, to Next specimen; after Retest, to Trust it; after Clear lab > Yes, to Lab.
- Tabs: up to 8; a ninth "+" asks to close one. Back works per tab. Links never leave the page.
- The notebook adds a card only once per finding; cards show their tag icon and the word.
- Seconds are counted per pass while the tool is visible (paused when the page is hidden) and shown only in the reveal and report, never as a running clock.
- Reopening a tested specimen shows it read-only with its reveal. **Next specimen** is the main button. **Retest** starts that specimen again at Pass 1, but the first try stays: the lab table keeps the first try's calls in the row, tagged "retested", and the counts use the first try, so a retest can't erase what the inside read did.
- The table saves in localStorage (`fofl-table`, try/catch); Clear lab (after Yes) empties it.
- Keyboard: panel before stage; verdicts 1, 2, 3; Enter locks only from the page body, from Lock my call or from the verdict already picked (Enter on another verdict picks it). Visible focus.
- The table is saved when a specimen opens and when the page is hidden or closed.
- Sizes: page area, verdict buttons and Lock my call visible without scrolling at 1280x720 and 1366x768; at 680x425 the notebook collapses to a count chip that opens it; at 375 wide the browser stacks above the panel and the tab strip scrolls sideways.

## Look
- Accent `--brand #6d28d9` (lab violet, like a UV lamp that shows what the page hides: header, Lock my call, selected verdict ring). `--head-ink #ffffff`.
- Own `:root` (lab bench): `--paper #f4f6fb`, `--panel #ffffff`, `--ink #161b2e`, `--muted #545b70`, `--line #d9deea`, `--btn #6d28d9`, `--focus #b45309`; pass colors `--inside #ede9fe` (with the word "Inside") and `--outside #fef3c7` (with "Outside"). Verdicts: Trust it `#15803d` ✓, Partly `#a16207` ~, Don't trust it `#b91c1c` ✗, always with the word. Specimen pages keep their own made-up designs inside the browser frame so the tool's chrome never looks like a page.
- Neighbors: misleading-charts fuchsia #a21caf (redder), phishing-spotter lime #b6f23a, health-claim-checker yellow #ffe066, design-fixer indigo #4338ca (bluer), world-music-map plum #7a2e8a; the 6-8 blues (screen-week, workplace-scenarios, algorithm-audit) are avoided on purpose. Group siblings: olive, crimson, teal, brass, and orchid on boolean-builder's dark theme.
- Contrast: white on brand 7.10:1; brand on paper 6.57:1; brand on panel 7.10:1; ink on paper 15.79:1; muted on paper 6.25:1; focus on panel 5.02:1 and on paper 4.64:1; ink on inside 14.38:1; ink on outside 15.33:1; Trust green on white 5.02:1; Partly amber on white 4.92:1; Don't red on white 6.47:1. All pass AA.

## Art
- ff-shark-street: a tall curved gray shark dorsal fin with a dark trailing edge, swept back like a real shark's, breaking the surface of brown floodwater in a city street lined with parked cars and shop fronts with blank signs, overcast sky, realistic photo look; 4:3; cutout no; people no; S2's post photo and, framed as "Street Shark, digital collage, 2019", the artist's portfolio page. FLUX.2 (`scripts/cfart.py`).
- ff-flooded-street: the same kind of city street flooded with brown water up to car doors, shop fronts with blank signs, overcast sky, realistic news photo; 4:3; cutout no; people no; the Gazette's real flood photo in S2's outside read. FLUX.2.
- ff-library-front: a small red-brick town library with white columns and a blank sign board, green leafy trees, daytime; 4:3; cutout no; people no; S3's article photo. FLUX.2.
- ff-wood-frog: a brown wood frog with a dark eye mask sitting on frosty fallen leaves, close-up nature photo; 4:3; cutout no; people no; S6's blog photo. FLUX.2.
Logos, avatars (initials), browser frame, social post frame, encyclopedia pages, site lookup cards, specimen jars and the table are drawn in code.

## Voice
Bank voice `wise-mentor` (Gacrux), "Say thoughtfully and warmly, like a wise high school mentor": the patient voice of "slow down, then look elsewhere". Its only 6-8 wave user is relationship-spectrum (health), not a close neighbor; it differs from misleading-charts (news-reader), phishing-spotter (lively-host) and health-claim-checker (easy-coach). `Curio.voice`, `scope: () => state.mode`. Page text, results and expert notes are on screen only.
- w-lab (how): "Read this page. Tap lines to save them in your notebook. Then pick a verdict, and lock your call. Tap a jar for another specimen."
- outside (how, first Pass 2, only while just the specimen tab is open): "Now leave the page. Press the plus to open a new tab and search the site, the author or the claim."
- tools (how, first Pass 2, after outside): "You can also tap Who runs this site."
- image (how, after tools, while a Search this image button shows): "This photo has a Search this image button. Tap it to find where the photo came from."
- locked (how, first tap on a locked control): "That's for the outside read. Pick a verdict, then press Lock my call."
- expert (event, each reveal; stale on specimen change; queued how lines are dropped first, so a fast Next does not lose it): "Here's what a fact-checker would find. Compare it with your two calls."
- w-report (how): "This is your lab table. Compare your inside reads with your outside reads." With untested specimens left, w-report-more adds "Press Lab to test the next specimen."

## Family engine
`kit/fact-check.js` (the fact-check family: fake-or-fact-lab, fact-check-desk, ad-agency). This spec holds the full description; the siblings say what they feed it.
- **World**: a tool passes `{sites, people, posts, images, entries, index}`. Site `{domain, name, look, pages:[{path, kind, title, blocks}], lookup:{registered, owner|'hidden'}}`; person `{name, works:[urls]}`; post `{site:'chirp', handle, followers, text, image, shares}`; image `{id, copies:[{url, date, label}]}` (earliest first); entry (Openpedia) `{title, text}`. Every domain must end in `.example`, `example.org`, `example.com` or `example.net`; `fc.safeDomain(url)` checks it and logs a console error otherwise, so no real site slips in.
- **Browser**: tab strip (max 8), back per tab, read-only address bar, page renderer for kinds `article`, `about`, `post`, `profile`, `entry`, `search`, `imageSearch`, `lookup`, `document` (minutes, study pages). Each site renders with its own `look` (fonts, colors, logo shape) so pages differ from each other and from the tool chrome. Links never navigate the real window.
- **Locks**: `fc.lock(['newTab','search','image','lookup','leave','trace'])` and `fc.unlock()` (`trace` locks cite links); locked controls stay visible with a padlock and fire `onLocked`.
- **Search** (pure): `fc.search(query)` lowercases, drops little words (a, an, the, of, to, in, on, is, are, and, for), folds plurals and the numbers 0 to 12, and returns index entries `{terms, results:[{title, url, snippet}]}` whose terms are all in the query, best overlap first; an empty list gives the tool's no-results line and suggestion chips. `fc.imageSearch(id)` returns the image's copies. `fc.lookup(domain)`.
- **Trace**: a link marked `cite` opens its target with the matching passage highlighted, or "This source doesn't say that." when the passage is missing.
- **Notebook**: `fc.note({id, text, tag, from})` adds a card once; tags `inside`, `who`, `evidence`, `others`. A page block can carry a `note` that is added when the block is seen or tapped.
- **Calls**: `fc.call(specimen, pass, verdict)` records verdict, seconds (visible time only) and tabs opened.
- Pure parts in one marked block, exposed as `__tool.fc`.
This tool uses: World (six specimens above plus Openpedia, Glimmerlake Tribune, Truthlamp Fact Desk, Port Alder town site, Rhea Lind portfolio, Quellmont Journal of Child Learning, Brambleskip Nature Center, Puddlewick Middle School), Browser, Locks (Pass 1), Search with the index terms named in Content, imageSearch (S2), lookup (S1, S4), Trace (S1, S5), Notebook, Calls.

## Sources
- AASL, National School Library Standards (2018), Standards Framework for Learners: Curate IV.B.3, Engage VI.A.3. https://standards.aasl.org/framework/
- Wineburg, S. and McGrew, S. (2019). "Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information." Teachers College Record 121(11). (Fact-checkers left sites to read laterally and judged more accurately than historians and students.)
- Digital Inquiry Group (formerly Stanford History Education Group), Civic Online Reasoning: the three questions "Who's behind the information? What's the evidence? What do other sources say?" https://cor.inquirygroup.org/
- Caulfield, M. "SIFT (The Four Moves)", 2019 (stop, investigate the source, find better coverage, trace claims to the original). https://hapgood.us/2019/06/19/sift-the-four-moves/
- ICANN Registration Data Lookup (what a domain lookup shows: registration date, registrant, often hidden). https://lookup.icann.org/
- National Park Service, Denali National Park, "Amphibians" (wood frogs freeze solid in winter, do not breathe and their hearts do not beat, and thaw in spring). https://www.nps.gov/dena/learn/nature/amphibians.htm
- All specimens, sites, people, studies and organizations are made up for Curio Class. The verdict match rule and the three-verdict scale are the tool's own choices.

## Done when
1. All six specimens open; in Pass 1 the new tab, search, image search, site lookup and cite links are locked and say so when tapped; other same-site links work.
2. Every outside finding in Content can be reached (by its suggestion chip and by typing its terms) and adds its notebook card once, with the right tag.
3. Trace on S1 and S5 opens the source with the passage highlighted; Search this image on S2 lists the 2019 collage first; Who runs this site? on S1 and S4 shows the Content lookup.
4. Lock my call is disabled until a verdict is picked (and, in Pass 2, until an outside move); each pass records verdict, seconds and tabs; the reveal shows the fact-checker's verdict, why and the deciding findings; a Retest keeps the first try in the table, tagged "retested".
5. Report counts match the table (recompute from `__tool.fc` calls); Clear lab (after Yes) empties it; the table survives a reload.
6. `fc.safeDomain` passes every address in the world; no real site, brand or person appears.
7. Page area, verdicts and Lock my call visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`; verdict keys 1 to 3 work.
8. Voice: welcome once per mode, how lines once, the expert line every reveal and dropped on specimen change; Read speaks the hint; console clean; no network requests; only "Curio Class".

## Open questions
- None. (The shark photo stays, settled in w1-51.)
