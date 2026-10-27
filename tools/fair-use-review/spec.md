# Fair Use Review
Renamed from: Fair Use Court

## One idea
You review uploads on a made-up student video site, and each upload has switches for its facts (a parody or just a borrowed tune, three short clips or the whole ending, free or sold on T-shirts): flip one and the senior reviewer's lean on each of the four fair use factors moves in front of you, so you see which facts each factor cares about and how one change can turn "keep it up" into "take it down".

## Not like
- The overlap pass: Fair Use Court was one of four mock trials in 9-12. Taking the suggested reshape, there is no courtroom, judge or verdict: you are a reviewer working a queue, your call is a site decision (keep, ask for changes, take down), and the senior reviewer's call is shown as one reasonable view, never "the answer".
- data-policy-council (9-12 CS, wave 1): writes rules for a school's data with a council vote. Here no rules are written; existing law (17 U.S.C. 107) is applied to cases, and facts are what you change.
- credit-card-builder (3-5, this group): full credits as trails back to creators. Here credit is one part of a license's conditions, and the bigger question is whether the use is allowed at all.
- boolean-builder, keyword-fishing, fake-or-fact-lab (this group): finding and judging sources. Here the sources are known; the question is what you may do with them.
- brand-builder (9-12 arts, wave 1): makes a brand of your own. Here you decide about other people's work and license your own.

## Who and how
- Grades 9 to 12, library. Module: Citation, Copyright and Fair Use (Research), "Citation styles, plagiarism, copyright and Creative Commons".
- Topic line: "copyright, fair use and Creative Commons".
- Driver: students on their own laptops; works well as pairs who must agree before submitting. A teacher can project one case for a class vote on each factor. 25 to 40 minutes.
- Standards: AASL.Engage (VI.A.2 understanding the ethical use of information, technology and media; VI.B.1 ethically using and reproducing others' work), AASL.Include (weighing the creator's and the remixer's perspectives); also MA:Cn11 (media arts in ethical and legal contexts: fair use).
- tool.json: driver "students", minutes "25-40", modes ["Review queue", "Your upload"], grades_label "Grades 9-12".

## Screens and modes
Kit frame, own light `:root` (a daylit review desk). Header: title "Fair Use Review", small line "Kestrel Clips Rights Desk"; mode buttons **Review queue** (opens first) and **Your upload**; Motion, Sound, Read. Footer line on every screen: "Practice, not legal advice. Fair use is decided case by case, and only a court decides it for sure."

### Review queue (opens first)
Queue strip: six upload cards (C1 to C6), each "To review" or "Reviewed". Any order.
Stage: the open upload: a code-drawn video thumbnail and title, the uploader's handle, the description, a **What it uses** box (the borrowed work: title, creator, kind, its license or "All rights reserved"), the **Facts** list, and two **What if** switches, each a labelled two-way toggle (left is the case as uploaded). A **Myths** fold at the bottom of the stage (four cards, Content).
Panel: `#hint`; the four **Factors**, each a row with its plain question and a five-step lean control: **Strongly against**, **Against**, **Neutral**, **Favors**, **Strongly favors** (fair use); then **Your call**: **Keep it up**, **Ask for changes**, **Take it down**; then **Submit review** (enabled when all four factors and a call are set).
After Submit: the **Senior review** card from Theo Marsh, senior reviewer: a second marker on each factor row (Theo's lean, a brass diamond with his initials), one reason line per factor, his call, and, where one fits, a **Real case** card. Rows where your lean and Theo's differ by 2 or more steps get the label "You differ". No score.
From then on the What if switches drive Theo's markers live: flipping one moves the markers that change (each changed row flashes once and shows "moved by: [switch]"), his reason lines and his call update, and the case summary line reads "As uploaded" or "With [switch text]". Your own leans stay where you put them, so you can compare.

### Your upload
You made a two-minute video, "Trees of Our Town". Stage: a **Materials shelf** of seven items (Content), each a card with its title, creator, kind and license badge; **Add to video** puts it on a timeline strip; **Remove** takes it off. Each item on the timeline gets a status chip: ✓ "OK, with credit", ✓ "Free to use", ! "OK, with a condition" or ✗ "Can't use this way", with the reason.
Panel: `#hint`; **Credits**: one TASL line per item on the timeline (Title, Author, Source, License), built from the item's card, with each of the four parts labelled T, A, S, L under it; then the **License chooser** for your own video: "Let others share changed versions of your video?" **Yes** / **Yes, if they share alike** / **No**; "Let others use it commercially?" **Yes** / **No**; or **Waive all rights (CC0)**. The result shows the license name (for example "CC BY-NC-SA 4.0") and its condition badges. Conflicts with your materials show as ✗ lines under the result, naming the item.

## Content
The site, people, works and uploads are made up. Lean values: Strongly against -2, Against -1, Neutral 0, Favors +1, Strongly favors +2. Theo's leans and calls below are the tool's authored judgments, built from the Copyright Office's description of each factor; the card says "One reviewer's call. Reasonable reviewers can differ."

Factor questions (the four factors of 17 U.S.C. 107): 1 "Purpose and character: Does it add something new, like comment or criticism? Is it commercial or nonprofit educational?" 2 "Nature of the work: Is the original creative (a song, film, novel) or factual?" 3 "Amount: How much was used, and was it the heart of the work?" 4 "Market effect: Could it replace the original or a sale or license of it?"

Cases (Theo's leans as F1, F2, F3, F4 and his call, for each switch setting):
- C1 "Homework Static (parody)", @maple_hall_band. Uses: the song "Summer Static" by the band Neon Harbor, all rights reserved. Facts: same melody, all new lyrics, 2 min 40 s, free, no ads. Switch A: "New lyrics poke fun at the original song" / "New lyrics are about homework and never mention the song". Switch B: "Free to watch" / "Sold as a $1 download". As uploaded (+2, -1, 0, +1) Keep it up. A (0, -1, -1, +1) Ask for changes. B (+1, -1, 0, 0) Keep it up. A and B (-1, -1, -1, 0) Take it down. Reasons: F1 "A parody comments on the original, which adds something new." / A "Borrowing a song to joke about something else needs more reason to use that song." / B "Selling it weighs against it, but it doesn't decide the case alone." F2 "A song is creative work." F3 "A parody has to call up the original, so using the melody can be reasonable." / A "Without the parody, the whole melody is more than needed." F4 "Fans of the song won't buy a parody instead." / B "A paid version is closer to competing with the song." Real case: Campbell v. Acuff-Rose Music (1994): a commercial parody of "Oh, Pretty Woman" could be fair use; being commercial did not settle it.
- C2 "Review: Starfall Run", @film_club_kc. Uses: the movie "Starfall Run", Bright Arc Pictures, all rights reserved. Facts: a 6-minute spoken review with three 10-second clips. Switch A: "Three 10-second clips" / "The whole final 8 minutes, including the ending". Switch B: "Talks about each clip" / "Clips play with music, no talking". As uploaded (+2, -1, +1, +2) Keep it up. A (+2, -1, -2, 0) Ask for changes. B (-1, -1, +1, +1) Ask for changes. A and B (-1, -1, -2, -1) Take it down. Reasons: F1 "Criticism adds something new." / B "With no comment, it's just the movie again." F2 "A film is creative work." F3 "Short clips, only what the review needs." / A "The ending is the heart of a movie." F4 "A review doesn't replace seeing the movie." / A "Showing the ending could replace part of watching it." / B "A clip reel adds nothing a viewer would watch instead of the movie, but it also offers nothing new." Real case: Harper & Row v. Nation Enterprises (1985): about 300 words from an unpublished memoir were not fair use because they were the heart of the book and hurt a planned sale.
- C3 "The Water Cycle (class slideshow)", @ms_okafor_period3. Uses: the photo "Falls at First Light" by the photographer June Abara, sold as a license on her site. Facts: the whole photo, as the slideshow's title background. Switch A: "Photo sold as a license, all rights reserved" / "Photo marked CC BY by June Abara". Switch B: "Used as a background picture" / "Used in a lesson about how the long-exposure shot was made". As uploaded (0, -1, -2, -1) Ask for changes. B (+2, -1, -2, -1) Keep it up. A, or A and B: factors read "Not needed: the license allows it" and the call is Keep it up, "as long as the credit names the title, author, source and license". Reasons: F1 "Schoolwork helps, but the photo is used for the same reason it was made: to show a waterfall." / B "Studying the photo itself is commentary on it." F2 "A photo like this is creative." F3 "The whole photo was used." F4 "She sells licenses, so free use costs her a sale." Real case: Andy Warhol Foundation v. Goldsmith (2023): licensing an artist's version of a photo to a magazine served the same purpose as the photo, so the first factor favored the photographer.
- C4 "When the lunch line is long (meme)", @hallway_humor. Uses: one frame of the TV show "Castle Kitchen", Larkspur TV, all rights reserved. Facts: one still frame, a new caption about the school cafeteria, posted free. Switch A: "One frame with a caption" / "The full 22-minute episode with a caption on top". Switch B: "Posted free" / "Printed on T-shirts the club sells". As uploaded (+1, -1, +1, +2) Keep it up. A (0, -1, -2, -2) Take it down. B (0, -1, +1, 0) Ask for changes. A and B (-1, -1, -2, -2) Take it down. Reasons: F1 "A new caption gives it a new meaning." / A "A caption on a whole episode adds little." / B "Selling shirts is commercial." F2 "A TV show is creative." F3 "One frame of a long show." / A "The whole episode." F4 "Nobody skips the show because of a meme." / A "The episode itself, free, replaces watching it." / B "Shows license their images for shirts." No case card: "No single case; the four factors decide."
- C5 "ShelfSearch (coding club demo)", @code_club_ks. Uses: 200 novels from made-up publishers, all rights reserved. Facts: scans the books so you can search inside them; shows only 3-line snippets around your search word. Switch A: "Shows 3-line snippets" / "Shows whole chapters". Switch B: "Free" / "Costs $2 a month". As uploaded (+2, -1, 0, +1) Keep it up. A (0, -1, -2, -2) Take it down. B (+1, -1, 0, +1) Keep it up. A and B (-1, -1, -2, -2) Take it down. Reasons: F1 "Searching inside books is a new purpose." / A "Reading chapters is the books' own purpose." F2 "Novels are creative." F3 "Whole books are copied, but readers see only snippets." / A "Readers see whole chapters." F4 "Snippets don't replace the books." / A "Chapters can replace buying the book." Real case: Authors Guild v. Google (2d Cir. 2015): scanning books to make them searchable and showing snippets was fair use.
- C6 "Lo-fi Study Mix, 1 hour", @night_owl_beats. Uses: 12 songs by made-up artists. Facts: each whole song with a drum beat added. Switch A: "Songs all rights reserved" / "Songs licensed CC BY, credited". Switch B: "Whole songs with a beat" / "15-second clip of each song with a spoken review". As uploaded (-1, -1, -2, -2) Take it down. B (+2, -1, 0, +1) Keep it up. A, or A and B: "Not needed: the license allows it", Keep it up with credits. Reasons: F1 "A beat on top adds little; it's still listening to the songs." / B "Reviewing each song is commentary." F2 "Songs are creative." F3 "Whole songs." / B "Short clips, enough to review." F4 "Listeners would hear the songs here instead." / B "A review sends listeners to the songs."

Myths (each marked ✗ "Myth" with the fact): "Under 10 seconds is always OK." There is no set number of words, lines, notes or seconds that is automatically fair (U.S. Copyright Office). / "If I give credit, it's fair use." Credit is not one of the four factors; when in doubt, ask permission (17 U.S.C. 107; Copyright Office FAQ). / "School projects are always fair use." Nonprofit education counts in factor 1, but all four factors are weighed. / "If it's online, it's free." A work is under copyright from the moment it is created and fixed (Copyright Office, Circular 1).

Your upload, materials (status when added):
- "Morning Ferry", song, Lumen Quartet, CC BY-NC 4.0: ! "OK, with a condition: no commercial use of this song."
- "Old Mill Bridge, 1925", photo, unknown photographer, published 1925, public domain: ✓ "Free to use. Published in the U.S. before 1931." (credit shown as a courtesy).
- "Paper Lanterns", song, Ivy Coast, CC BY-ND 4.0: ✗ "Can't use this way. Putting music to video makes an adapted work, and ND doesn't allow sharing adaptations. Ask Ivy Coast, or pick another song."
- "Oak Leaves in Rain", photo, K. Ito, CC BY-SA 4.0, which you crop and recolor: ! "OK, with a condition: your video must use BY-SA."
- "Drone over Elm Park", video clip, Sky Lens Club, CC BY 4.0: ✓ "OK, with credit."
- "City Skyline at Night", photo, Arturo Vance, all rights reserved: ✗ "Needs permission from Arturo Vance, or a strong fair use case."
- "Birdsong Loop", sound, Pell Audio Lab, CC0: ✓ "Free to use."
License chooser rules: Yes/Yes = CC BY; Yes/No = CC BY-NC; Share alike/Yes = CC BY-SA; Share alike/No = CC BY-NC-SA; No/Yes = CC BY-ND; No/No = CC BY-NC-ND; CC0 = public domain dedication. Conflicts: with "Oak Leaves in Rain" on the timeline, anything but CC BY-SA shows ✗ "Oak Leaves in Rain is BY-SA, so your video must be BY-SA." With both "Oak Leaves in Rain" and "Morning Ferry": ✗ "BY-SA and BY-NC material can't be combined in one adapted work. Drop one." With "Morning Ferry" and a license allowing commercial use: ! "Morning Ferry stays non-commercial even if your video allows it. Choosing No keeps it simple." CC0 with any BY, SA or NC item: ✗ "You can only waive rights you own. Those items keep their licenses."
TASL line format: "[Title] by [Author], from [Source], licensed under [License]." Public domain: "[Title], [Author or 'unknown'], [year], public domain."

## Interactions in detail
- Factor controls are segmented buttons (keys 1 to 5 when a row is focused). Changing your leans after Submit is allowed; Theo's markers are unaffected.
- What if switches are disabled with a lock and "Submit your review first" until Submit, so the first read is the case as uploaded.
- Theo's markers slide 300 ms when a switch moves them (instant with Motion off); the "moved by" label stays until the next switch.
- Reviewed cases keep your leans, call and switch positions; **Reset case** clears them. **Clear desk** (asks Yes / No) resets all six and Your upload.
- Your upload: a timeline holds all seven at most; an item can be removed any time; credits and conflicts update at once.
- Saved in localStorage (`fur-desk`, try/catch): leans, calls, switch positions, timeline and license choice. Clear desk empties it.
- Keyboard: queue, then panel factor rows, call, Submit, then stage switches. Visible focus.
- Sizes: the four factor rows, the call and Submit visible without scrolling at 1280x720 and 1366x768; at 680x425 the factor questions collapse to their short names (Purpose, Nature, Amount, Market) with the full question on focus; at 375 wide the upload card sits above the panel and the switches stack.

## Look
- Accent `--brand #b45309` (brass: header rule, Submit, Theo's markers, selected call). `--head-ink #ffffff`.
- Own light `:root` (review desk): `--paper #f5f3ef`, `--panel #ffffff`, `--ink #1f1b16`, `--muted #5f574c`, `--line #ddd6cb`, `--btn #b45309`, `--focus #1d4ed8`. Lean scale ends: favors `#0f766e` with "Favors", against `#9f1239` with "Against" (word and position, never color alone). Your markers are filled circles, Theo's brass diamonds with initials. Myth cards on `#fdf2e2` with a ✗ and the word "Myth". License badges drawn in code as text pills (BY, SA, NC, ND, CC0), not logos.
- Neighbors: data-policy-council civic navy (light), brand-builder emerald, captain-s-choices coral, and its group siblings olive, crimson, violet, teal and orchid (dark). Brass is new in 9-12.
- Contrast: white on brand 5.02:1; brand on paper 4.53:1; brand on panel 5.02:1; ink on paper 15.45:1; muted on paper 6.41:1; muted on panel 7.11:1; focus on panel 6.70:1 and on paper 6.05:1; favors teal on panel 5.47:1 and on paper 4.94:1; against red on paper 7.23:1 and on panel 8.02:1; ink on myth tint 15.47:1. All pass AA.

## Art
none: drawn in code (thumbnails as titled color cards with a kind icon, switches, scales, timeline, license pills and preview.svg).

## Voice
Bank voice `easy-coach` (Umbriel), "Say in an easy-going, encouraging way, like a relaxed sports coach": Theo, a laid-back senior reviewer showing a new teammate the ropes. Its other 9-12 wave users are health tools (game-day-fuel, health-claim-checker), not library tools or close neighbors; no group sibling uses it. The bank has no free voice that fits 9-12 better. `Curio.voice`, `scope: () => state.mode`. Case texts and reasons are on screen only.
- w-queue (how): "Welcome to the Rights Desk. Pick an upload, set a lean for each of the four factors, make your call, and press Submit review."
- switches (how, first Submit): "Now flip a What if switch and watch which factors move."
- differ (event, each Submit with a "You differ" row; stale on case change): "We see one factor differently. Read my reason, then decide if you'd change yours."
- agree (event, each Submit with no "You differ" row; stale on case change): "We're on the same page with this one."
- w-upload (how): "Your turn as a creator. Add materials to your video, check each one's status, then choose a license."
- conflict (event, each new ✗ conflict; stale when it clears): "Something on your timeline doesn't fit that license. Read the red line."

## Family engine
none

## Sources
- 17 U.S.C. 107, Limitations on exclusive rights: Fair use (the four factors; nonprofit educational purposes named in factor 1). https://www.copyright.gov/title17/92chap1.html#107
- U.S. Copyright Office, "More Information on Fair Use" and the Fair Use Index (transformative use; creative vs factual; quantity and quality, including the heart; market harm; no formula or set amount). https://www.copyright.gov/fair-use/more-info.html and https://www.copyright.gov/fair-use/
- U.S. Copyright Office, FAQ "Can I Use Someone Else's Work?" (no fixed number of words or notes; get permission when in doubt). https://www.copyright.gov/help/faq/faq-fairuse.html
- U.S. Copyright Office, Circular 1 "Copyright Basics" (copyright from the moment of creation and fixation). https://www.copyright.gov/circs/circ01.pdf
- Campbell v. Acuff-Rose Music, Inc., 510 U.S. 569 (1994); Harper & Row v. Nation Enterprises, 471 U.S. 539 (1985); Andy Warhol Foundation for the Visual Arts v. Goldsmith, 598 U.S. 508 (2023); Authors Guild v. Google, Inc., 804 F.3d 202 (2d Cir. 2015). Summaries as in the Copyright Office Fair Use Index.
- Creative Commons, "About CC Licenses" (BY, SA, NC, ND and the six licenses). https://creativecommons.org/share-your-work/cclicenses/
- Creative Commons, CC BY 4.0 legal code, section 1(a) (music synced to moving images is always an adapted work). https://creativecommons.org/licenses/by/4.0/legalcode.en
- Creative Commons wiki, license compatibility chart (BY-SA and BY-NC can't be combined in an adaptation). https://wiki.creativecommons.org/wiki/Wiki/cc_license_compatibility
- Creative Commons wiki, "Recommended practices for attribution" (TASL: title, author, source, license). https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution
- Creative Commons, CC0 public domain dedication. https://creativecommons.org/public-domain/cc0/
- Cornell University Library, "Copyright Term and the Public Domain in the United States" (works published before 1931 are public domain as of 2026). https://guides.library.cornell.edu/copyright/publicdomain
- AASL, National School Library Standards (2018), Engage VI.A.2 and VI.B.1, Include. https://standards.aasl.org/framework/
- All uploads, works, people and the site are made up for Curio Class; Theo's leans and calls are the tool's own authored judgments.

## Done when
1. All six cases open; switches stay locked until Submit; Submit needs four leans and a call.
2. For every case and all four switch settings, Theo's leans, reasons and call match Content exactly (`__tool.theo(case, a, b)`), and the moved rows flash with "moved by".
3. "You differ" appears exactly on rows two or more steps apart; no score anywhere.
4. Licensed settings (C3 A, C6 A) show "Not needed: the license allows it" on all four rows.
5. Real case cards appear on C1, C2, C3 and C5 only; the Myths fold shows four myths with their facts.
6. Your upload: each of the seven materials shows its Content status; the chooser yields all seven results; every conflict rule fires and clears when its cause is removed; TASL lines match the format.
7. State survives a reload; Clear desk (after Yes) resets everything.
8. Factor rows, call and Submit visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`.
9. Voice: welcome once per mode, how lines once, the agree or differ line every Submit and dropped on case change; Read speaks the hint; console clean; no network requests; only "Curio Class"; the legal disclaimer is on every screen.

## Open questions
- The four real case cards name real people and works (Roy Orbison's "Oh, Pretty Woman", Gerald Ford's memoir, a photo of Prince, Google). They are court-case citations from the Copyright Office's index, not made-up content. Keep them, or describe each case without names?
- Theo's leans and calls are authored judgments on made-up cases, labelled as one reviewer's view with a not-legal-advice line. Is that framing enough, or should a teacher toggle hide Theo's call and show only his factor reasons?
