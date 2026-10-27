# Credit Card Builder

## One idea
A credit is a trail back to the person who made something: you build each credit card by tapping the facts right on the book, web page or photo you borrowed from, then a reader follows your card back through a library shelf and a website, and a missing or wrong piece strands them at a row of look-alikes, so the creator never gets their thank-you postcard.

## Not like
- keyword-fishing (3-5, this group): finding pages with search words. Here the sources are already found and on your poster; the job is to say exactly where they came from.
- fair-use-court (9-12, this group): whether a use is allowed at all, the four factors, Creative Commons licenses. Here permission never comes up; every use is a class poster, and the only question is a complete credit.
- game-remix (5, built): credits the author of a remixed program in one line. Here three kinds of source each need their own card, tested by a trail.
- library-adventure (K-2, built): spine labels and shelves to find a book. Here the shelf is the test of a credit, and it is full of same-title books on purpose.
- Source Sorter (ela grade 6, research family, not built): judges credibility and builds a citation for you. Here you build the credit yourself, piece by tapped piece, and nobody judges the source.

## Who and how
- Grades 3 to 5, library. Module: Giving Credit (Research), "Why and how to credit sources".
- Topic line: "giving credit to creators and sources".
- Driver: students on laptops (pairs work well), or a teacher on a projector building the first card with the class. 15 to 25 minutes.
- Standards: AASL.Engage (VI.B.2 acknowledging authorship and respecting the intellectual property of others; VI.B.3 including elements that let others credit content).
- tool.json: driver "students or teacher", minutes "15-25", modes ["Build", "Creator's Corner"], grades_label "Grades 3-5".

## Screens and modes
Kit frame, own `:root` (kraft paper and index cards). Header: title "Credit Card Builder", small line "Give credit where it's due"; mode buttons **Build** (card icon, opens first) and **Creator's Corner** (mailbox icon); Motion, Sound, Read.

### Build (opens first)
Project strip above the stage: **Owl Poster**, **Honeybee Slides**, **Moon Report** (each shows "0 of 3 found" or a "3 of 3 found" ribbon).
Stage, left part: the project, drawn in code (a poster, three slides, or a report page) with three borrowed pieces: a fact from a book, a fact from a web page, a photo. Each piece has a tag: "Needs credit" (dashed), "Card made" (solid), or "Found!" (green with a check) after a test.
Stage, right part: the **Source viewer**, showing the source of the selected piece:
- Book: three pages to flip with **‹** and **›**: the cover, the title page, the copyright page.
- Web page: a browser frame with an address bar, the site's name and logo strip, a page heading, a byline and date line, body text and an ad box.
- Photo page: the photo, its title, a "Photo by" line, an "Uploaded by" line, the site's name and a **Download** button that does nothing but say "Not needed for a credit."
Every printed detail in the viewer (names, titles, years, dates, addresses, ads, buttons, page numbers) is a tappable chip.
Panel: `#hint`; the **Credit card** for the selected piece (an index card with labelled slots, per type below); the live **Credit line** under it, built from the slots; buttons **Test my credits** (big), **Clear card**.
To fill a slot: tap the slot (it glows), then tap a chip in the viewer; the text flies onto the card (400 ms; instant with Motion off). Tapping a filled slot and a new chip replaces it. Undated web pages offer a chip **Date I looked: [today]** inside the date slot itself.

Card slots and credit line (the tool's own kid format, built on the core parts every style asks for: who, what, when, where):
- Book: "Who wrote it?", "Title", "Year". Line: "[Who]. [Title]. [Year]."
- Web page: "Page title", "Website name", "Date", "Web address". Line: "[Page title]. [Website name]. [Date]. [Web address]."
- Photo: "Who took it?", "Photo title", "Where I found it". Line: "Photo: [Photo title], by [Who]. [Where]."

**Test my credits** (enabled once every piece of the project has a card, even an unfinished one): the stage turns into the **Trail**. A small code-drawn reader (a paper-airplane note with a magnifier) follows each card in turn: to the library shelf for the book, through the website's pages for the web page, to the photo site for the photo. Each trail ends in **Found it!** (the source glows, its tag turns "Found!", and a thank-you postcard flies to that creator's mailbox) or **Stuck** (the reader stops at the place the card led to, shows the look-alikes, and the hint names what's missing without filling it in). Then **Back to my cards**.

### Creator's Corner
A street of nine mailboxes, one per creator (code-drawn, each with the creator's initials, a tool icon: pen, laptop or camera, and the work they made). Tap one: their card shows what they made, a one-line story of making it (Content), and their mailbox, holding the thank-you postcards earned in Build (or empty, "No thank-you yet"). Three **Why credit?** cards along the top: "It's fair. They did the work." "Readers can find the source and check it." "A creator owns what they make from the moment they make it."
A **No credit** switch on each creator card shows the project with that creator's piece labelled "Photo: ???" (or "Fact from: ???") and the mailbox locked: "With no name, nobody knows who to thank."

## Content
All people, books, sites and photos are made up; web addresses use the reserved `.example` ending.

Project 1: Owl Poster
- Book piece "Barn owls can find a mouse in the dark by sound alone." Cover: "Owls of the Night", "by Ana Ruiz", "illustrated by Leo Brandt", series badge "Night Animals 3". Title page: "Owls of the Night", "Ana Ruiz", "Pictures by Leo Brandt", "Fern Hill Books". Copyright page: "Text copyright 2019 Ana Ruiz", "Illustrations copyright 2019 Leo Brandt", "First edition 2019", "Page 14" footer. Answer: Ana Ruiz / Owls of the Night / 2019.
- Shelf (test): "Owls of the Night", Ana Ruiz, 2019 (the one); "Owls of the Night", Ana Ruiz, 2023, new edition; "Owls of the Night", Maya Chen, 2016; "Owl Babies at Dusk", Ana Ruiz, 2021; "Night Herons", Leo Brandt, 2020.
- Web piece "Barn owls swallow small prey whole." Address bar "wildwingskids.example/owls/barn-owl"; logo strip "Wild Wings Kids"; nav chips "Home", "Owls", "Shop"; heading "Barn Owl Facts"; byline "By the Wild Wings team"; date "Updated May 3, 2024"; ad box "Win free bird stickers!". Answer: Barn Owl Facts / Wild Wings Kids / May 3, 2024 / wildwingskids.example/owls/barn-owl.
- Photo piece: image cc-snowy-owl. Title "Snowy Owl at Dawn"; "Photo by Sam Okafor"; "Uploaded by: lakeclub_photos"; site "Open Nature Photos". Answer: Sam Okafor / Snowy Owl at Dawn / Open Nature Photos.

Project 2: Honeybee Slides
- Book piece "A hive can have one queen and thousands of workers." Cover "The Busy Hive", "by Grace Liu", "illustrated by Omar Haddad", series badge "Garden Friends 1". Title page "The Busy Hive", "Grace Liu", "Pictures by Omar Haddad", "Maple Lane Press". Copyright page "Text copyright 2021 Grace Liu", "Illustrations copyright 2021 Omar Haddad", "First edition 2021", "Page 6". Answer: Grace Liu / The Busy Hive / 2021.
- Shelf: "The Busy Hive", Grace Liu, 2021; "The Busy Hive", Grace Liu, 2024, new edition; "The Busy Hive", Tom Reyes, 2018 (a cookbook); "Bees Up Close", Grace Liu, 2022; "Garden Bugs", Omar Haddad, 2019.
- Web piece "Bees make honey from flower nectar." Address "littlesciencelab.example/bees/honey"; logo "Little Science Lab"; nav "Home", "Bees", "Next page: Wasps"; heading "How Bees Make Honey"; byline "By Dot Fischer"; date "Updated September 12, 2023"; ad box "Science kits on sale!". Answer: How Bees Make Honey / Little Science Lab / September 12, 2023 / littlesciencelab.example/bees/honey.
- Photo piece: cc-honeybee-sunflower. Title "Honeybee on a Sunflower"; "Photo by Priya Nair"; "Uploaded by: garden_club_7"; site "Sunny Day Images". Answer: Priya Nair / Honeybee on a Sunflower / Sunny Day Images.

Project 3: Moon Report
- Book piece "The Moon has no air to breathe." Cover "Our Moon", "by David Osei", "illustrated by Ana Ruiz", series badge "Sky Watch 2". Title page "Our Moon", "David Osei", "Pictures by Ana Ruiz", "Fern Hill Books". Copyright page "Text copyright 2020 David Osei", "Illustrations copyright 2020 Ana Ruiz", "First edition 2020", "Page 9". Answer: David Osei / Our Moon / 2020. (Ana Ruiz is the trap: she wrote the owl book but only drew this one.)
- Shelf: "Our Moon", David Osei, 2020; "Our Moon", Lena Sato, 2015; "Moon and Stars", David Osei, 2022; "Owls of the Night", Ana Ruiz, 2019; "Our Moon", David Osei, 2025, new edition.
- Web piece "The Moon looks different through the month because we see different parts of its sunny side." Address "starpathkids.example/moon/phases"; logo "Star Path Kids"; nav "Home", "Planets", "Games"; heading "Moon Phases for Kids"; no byline; no date (the date slot offers "Date I looked: [today's date]"); ad box "Glow stars for your room!". Answer: Moon Phases for Kids / Star Path Kids / Date I looked / starpathkids.example/moon/phases.
- Photo piece: cc-moon-lake. Title "Moon Over Clear Lake"; "Photo by Jonas Berg"; "Uploaded by: jonasberg" (here uploader and creator are the same person, written differently); site "Open Nature Photos". Answer: Jonas Berg / Moon Over Clear Lake / Open Nature Photos.

Facts on the pieces (sourced): barn owls locate prey by sound alone (Cornell Lab); owls swallow small prey whole and cough up pellets (Cornell Lab); a colony has one queen and thousands of workers (USDA ARS honey bee); bees make honey from nectar (USDA ARS); the Moon has almost no atmosphere (NASA); phases come from how much of the sunlit half we see (NASA).

Trail results (the tool's own rules, checked in this order for each card):
- Book: Who is the illustrator → stuck at the illustrator's own book: "This book is by [illustrator]. They drew the pictures, but someone else wrote the words." Who empty or not a name on that shelf → "[n] books are called [title]. Who wrote yours?" Title empty or wrong → "[author] wrote [n] books on this shelf. Which one?" Year empty or wrong → "Two editions match: [year] and [year]. Which year?" All right → Found it!
- Web page: Web address is an ad, nav chip or empty → for an ad: "This goes to the sticker ad, not the page!"; for empty or a nav chip: "[site] has 120 pages. Which one?" Page title wrong or empty → "The address works, but the title doesn't match. Readers might doubt it." (counts as Stuck). Website name wrong or empty → "Which website is this? Add its name." Date empty → Found it! with a note "Pages change. Adding the date tells readers which version you saw." All right → Found it!
- Photo: Who is the uploader (not the creator) → the postcard flies to the uploader's mailbox and bounces: "[uploader] only shared it. The thank-you went to the wrong person!" (Project 3: "jonasberg" is accepted as Jonas Berg.) Who empty → "Nobody knows who to thank." Title empty or wrong → "[site] has 5,000 photos. Which one?" Where empty → "Where did you find it?" All right → Found it!

Creator stories (made up): Ana Ruiz watched owls near her home for two years before writing. Leo Brandt painted 30 pictures for the owl book. Sam Okafor waited in the snow three mornings for the owl to land. Grace Liu kept bees for ten years. Omar Haddad drew every bug from life. Dot Fischer visited a bee farm to check her facts. Priya Nair grew the sunflower herself. David Osei taught science for twenty years. Jonas Berg stayed up until 2 in the morning for the moonrise. The Wild Wings team and Star Path Kids are each shown as a group card ("a team of writers").

## Interactions in detail
- Chips are always tappable; nothing says right or wrong while building. Printed lines are split into chips at their parts: "Text copyright 2019 Ana Ruiz" is three chips ("Text copyright", "2019", "Ana Ruiz"), "Updated May 3, 2024" is two ("Updated", "May 3, 2024"), "Photo by Sam Okafor" is two. The only judgment is the Trail.
- The credit line updates as each slot fills; empty slots show as gray "___".
- A trail takes about 3 s per card (1 s with Motion off: no flight, just the end state). Cards are tested in project order: book, web page, photo.
- Re-testing after a fix tests all three again; postcards already earned stay. A creator's mailbox holds at most one postcard per piece.
- Clear card empties the selected card only. **Start over** (panel footer, asks "Clear all three projects?" Yes / No) clears every card and postcard.
- Progress (cards and postcards) saves in localStorage (`ccb-progress`, try/catch); Start over clears it.
- Keyboard: Tab order is panel (slots, buttons), then viewer chips, then project pieces. A focused slot plus Enter on a chip fills it. Visible focus.
- Sizes: the card, the viewer and Test my credits visible without scrolling at 1280x720 and 1366x768; at 680x425 the project art shrinks to a strip of three piece tags above the viewer; at 375 wide the viewer stacks above the card and its chips wrap.

## Look
- Accent `--brand #b91c1c` (rubber-stamp crimson: header, slot glow, "Found!" stamp border, Test button). `--head-ink #ffffff`.
- Own `:root` (kraft desk): `--paper #f6efe3`, `--panel #fffdf8`, `--ink #2a2118`, `--muted #6a5a48`, `--line #e5d9c5`, `--btn #b91c1c`, `--focus #1d4ed8`. Index cards `#fffbea` with pale blue rules #9cc3e6 and a red top rule; Found tags `#166534` with a ✓ and the word "Found!"; Stuck shown with a "?" sign and the word "Stuck" (never color alone).
- Neighbors: keyword-fishing olive, fake-or-fact-lab violet, research-quest teal; nearest 3-5 reds are fitness-circuit raspberry #c2185b and art-style-match wine #9b2457, both pinker.
- Contrast: white on brand 6.47:1; brand on paper 5.66:1; brand on panel 6.36:1; ink on paper 13.82:1; muted on paper 5.80:1; muted on panel 6.52:1; focus on panel 6.59:1; ink on index card 15.23:1; Found green on index card 6.87:1. All pass AA.

## Art
- cc-snowy-owl: a snowy owl perched on a fence post in fresh snow at dawn, soft pink sky, nature photograph style, plain background; 4:3; cutout no; people no; the photo on the Owl Poster and its photo page. FLUX.2 (`scripts/cfart.py`).
- cc-honeybee-sunflower: a honeybee on the center of a bright sunflower, close-up nature photograph, green garden blurred behind; 4:3; cutout no; people no; the photo on the Honeybee Slides and its photo page. FLUX.2.
- cc-moon-lake: a full moon rising over a still lake with dark pine trees on the far shore, its reflection on the water, night nature photograph; 4:3; cutout no; people no; the photo on the Moon Report and its photo page. FLUX.2.
Book covers, pages, browser frames, shelf, trail, reader, mailboxes and postcards are drawn in code.

## Voice
Bank voice `bright-teacher` (Autonoe), "Say brightly and cheerfully, like an upbeat first grade teacher": cheerful for the youngest of the 3-5 band. Its other wave users are K-2 (target-toss); no 3-12 neighbor uses it. `Curio.voice`, `scope: () => state.mode`. Source details and credit lines are on screen only (Read speaks them).
- w-build (how): "Tap a piece of the poster to open its source. Tap a slot on the card, then tap the fact on the source."
- flip (how, the first time a book opens): "Books hide facts on more than one page. Tap the arrows to turn the pages."
- test (how, the first time every piece has a card): "Every piece has a card. Press Test my credits."
- found (event; stale when the trail moves on): "Found it! A thank-you is on its way."
- stuck (event; stale when the trail moves on): "Stuck! Read the hint, then fix that card."
- allFound (event, all three found; stale on project change): "All three found! Every creator got a thank-you."
- w-corner (how): "These are the creators. Tap a mailbox to see their story and your thank-you notes."
- nocredit (how, first No credit switch): "With no name, nobody knows who to thank."

## Family engine
none

## Sources
- AASL, National School Library Standards (2018), Standards Framework for Learners, Engage VI.B.2 and VI.B.3. https://standards.aasl.org/framework/
- MLA Style Center, "Works Cited: A Quick Guide" (core elements: author, title, container, date, location; an access date for undated online works). https://style.mla.org/works-cited/works-cited-a-quick-guide/ The card format itself is the tool's own simplification.
- U.S. Copyright Office, Circular 1 "Copyright Basics": copyright exists from the moment a work is created and fixed. https://www.copyright.gov/circs/circ01.pdf
- Cornell Lab of Ornithology, All About Birds, Barn Owl (finds prey by sound alone in darkness; swallows small prey whole and coughs up pellets). https://www.allaboutbirds.org/guide/Barn_Owl/
- USDA Agricultural Research Service, honey bee facts (one queen, thousands of workers; honey from nectar). https://www.ars.usda.gov/oc/br/apis/
- NASA Science, Moon facts (almost no atmosphere) and Moon phases. https://science.nasa.gov/moon/
- All people, books, websites, photos and stories are made up for Curio Class.

## Done when
1. Every chip in all nine sources fills a selected slot, and the credit line reads exactly as the Content format.
2. With every Content answer, all nine trails end in Found it! and nine postcards reach the nine right mailboxes.
3. Each trail rule fires with its own message: illustrator as author, missing author, missing title, missing year, ad as address, missing address, uploader as photographer (and "jonasberg" accepted), missing photographer.
4. Undated Moon page: the "Date I looked" chip shows today's date and the trail finds the page.
5. Creator's Corner shows nine creators and two team cards; the No credit switch shows "???" on the project and a locked mailbox.
6. Progress survives a reload; Start over (after Yes) clears it.
7. Card, viewer and Test my credits visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`; keyboard fills a slot without a mouse.
8. Voice: welcome once per mode, how lines once, Found and Stuck every trail and dropped when the trail moves on; Read speaks the hint; console clean; no network requests; only "Curio Class".
