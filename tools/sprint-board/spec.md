# Sprint Board

## One idea
Your real team of two to four shares one laptop and builds a bus-arrival app for a made-up transit client in three sprints of 10 points each, passing the laptop as roles rotate (product lead, designer, developer, tester): 41 points of tempting cards won't fit in 30, so every sprint the spec checklist and five user testers (a blind rider with a screen reader, a parent with one free thumb, a night-shift worker) hand back what you skipped, and the client's values (no ads, don't track riders) push back on what you chose.

## Not like
- network-architect (9-12 CS, builder): one student designs a network and runs tests on it. Here a team plans and ships an app over time, and the tests include people.
- chore-flowcharts (6-8, builder): one flowchart tested against days. Here nothing is programmed; the work is choosing, ordering and testing features as a team.
- accessibility-test-team (6-8, gap fill, not specced): rotates roles to test a design for every user. Here accessibility is one of three pressures (spec, users, client values) across a whole release.
- emerging-tech-pitch (this group): one concept, compared and pitched. Here the concept is fixed (the client wants it) and the question is what to build first and how to know it works. The bus problem lives here, not there.
- pull-request-review (this group): judges code someone else wrote. Here the team never sees code; it runs a product process.
- design-for-a-friend (CS, cs-data): interview one user and design for them. Here five users test what you shipped, and they disagree about what matters.

## Who and how
- Grades 9 to 12, computer science. Module: Design, Test and Refine (Computing and Society), "Human-centered design with a team workflow, spec checks, user testing and refinement". Topic line: "human-centered design in a team sprint".
- Driver: a team of 2 to 4 students at one laptop (pairs and threes double up roles). 40 to 50 minutes (design doc 8, each sprint about 12).
- Standards (module codes, CSTA 2026): HS-ALG-IM-09 (design for the people who use it: the design doc and personas), HS-PRO-TR-19 (test against a specification: the spec checklist), HS-PRO-TR-20 (user testing and refinement: user tests raise cards for the next sprint), HS-PRO-PD-15 (work in team roles: rotating roles with hand-offs). CSTA 2017 crosswalk: 3A-AP-19 (design programs for broad audiences with user feedback), 3A-AP-21 (make artifacts more usable and accessible), 3A-AP-22 (develop artifacts in team roles using collaborative tools), 3B-AP-17 (use a software life cycle process).
- tool.json: driver "students", minutes "40-50", modes ["Design doc", "Sprint", "Release"], grades_label "Grades 9-12".

## Screens and modes
Own light `:root` (a whiteboard with sticky cards), theme-912 class names kept with light values. Header: "Sprint Board", small line "Maple Valley Transit: Next Bus app". Modes: **Design doc** (first), **Sprint**, **Release** (Release opens after sprint 3 or any time, showing the board so far). Motion, Sound, Read.

Start: a **Team** card asks "How many in your team?" with **2**, **3**, **4**. Seats are numbered (Seat 1 to Seat 4), never named. Roles per sprint (rotating one seat each sprint):
- 4 seats: Product lead, Designer, Developer, Tester, one each.
- 3 seats: Product lead and Designer combined; Developer; Tester.
- 2 seats: Product lead and Developer; Designer and Tester.
A role strip under the header always shows "Sprint 1: Seat 1 Product lead, Seat 2 Designer, ..." and the active role glows.

### Design doc
Stage: a one-page document with four parts, each filled by picking, not typing:
- **Who it's for**: five persona cards (Content); mark up to three **Design for first**.
- **Problem**: pick one of three statements (Content).
- **Must have**: from the backlog, mark up to five cards "Must" (they get a pin).
- **Won't do this release**: mark any cards "Won't" (they leave the backlog lane, can be restored).
- Fixed at the bottom: the client's **Values** (Content) and the **Spec** checklist S1 to S8.
Panel: **Copy design doc**, **Start sprint 1**.

### Sprint
Stage: the board, five lanes: **Backlog**, **This sprint**, **Doing**, **Testing**, **Done**. Cards are sticky notes with title, points, type color plus a type word (Spec, Access, User, Extra), pins and tags ("Reported by Ana"). A capacity bar over This sprint: "8 of 10 points".
Each sprint runs four steps, shown as a stepper; each step starts with a full-width **hand-off** screen "Pass the laptop to Seat 3: Developer" and a **Ready** button.
1. **Plan** (Product lead): drag cards from Backlog into This sprint (or select a card, then **Add to sprint**), up to 10 points; order them by dragging (or **Up**, **Down**). A card that breaks a client value shows a red-bordered "Value: No ads" label but can still be planned.
2. **Build** (Developer): **Build sprint** moves each planned card to Doing, then Testing, in plan order, skipping ahead to build a card's dependency first if it is planned too. A card whose dependency is neither Done nor planned is **Blocked** ("Needs: Next arrival time"): it uses its points and returns to the Backlog at the end of the sprint.
3. **Test** (Tester): **Run spec checks**: S1 to S8 each show ✓ Pass, ✗ Fail or "Not built". Then **Move tested cards to Done**.
4. **User test and review** (Designer, then everyone): **Run user tests**: five persona sessions, each with Succeeded, Struggled or Blocked and a quote; new issue tags appear on the matching backlog cards. Then the **client review**: any Done card that breaks a value comes back with the client's note and moves to Backlog with a "Client said no" tag (its points are spent). Then **Retro**: pick one "Went well" and one "Change next time" chip (Content). **Next sprint** rotates the roles.
Panel (all steps): the active step's instructions as the hint, the spec checklist with current results, the persona strip (five faces drawn as simple initials badges with their last result), and **Undo last move** (Plan only).
Sprint 2 begins with an event card: "Tuesday night the arrival data feed went down for an hour." From then on, Jay's session tests what the app shows when data can't load.

### Release
Stage: the release scorecard: spec checks passed of 8; personas Succeeded, Struggled, Blocked; client values kept of 4; points Done of 30; cards left in Backlog; the three retros. Below: auto release notes ("Next Bus 1.0: pick your stop, see the next arrival, alerts 5 minutes ahead ... Known gaps: Spanish text, text-message alerts."). Panel: **Copy release notes**, **Save board on this device**, **Clear saved**, **New project** (confirm first).

## Content
Client brief: "Riders call us every day asking where the bus is. We want a free web app: pick your stop, see when the next bus really comes, get an alert before it arrives."
Values (client): V1 Free for every rider. V2 No ads. V3 Don't track where riders go. V4 Works for riders with disabilities. Scoring at Release: V2 and V3 count as broken if card 14 or 12 ever reached Done (even if the client sent it back); V4 is kept when S5, S6 and S7 all pass; V1 is always kept (no card charges riders).
Problem statements: "Riders can't tell when the next bus will really come." / "Riders want a map of every bus." / "The transit office gets too many calls." (any can be picked; the first matches the brief best and the Release notes quote the picked one).

Backlog (id, title, points, type, needs, effect):
1. Stop picker (3, Spec): S1.
2. Next arrival time for a stop (3, Spec, needs 1): S2.
3. Alert 5 minutes before (3, Spec, needs 2): S3.
4. Refresh times every 30 seconds (2, Spec, needs 2): S4; Jay.
5. Screen reader names on every button (2, Access): S5; Ana.
6. Text grows to 200 percent without cutting off (2, Access): S6; Walt.
7. Text contrast 4.5:1 (1, Access): S7; Walt.
8. Spanish language option (3, User): Rosa.
9. Route map (5, Extra): Jay "Nice, but I just wanted the time."
10. Save favorite stops on this phone (2, User): Dee likes it.
11. Big "Next bus" button on the home screen (1, User): Dee.
12. "Near me" finder that sends your location to the server (3, Extra): breaks V3.
13. "Near me" finder that stays on your phone (4, User): Dee and Jay find their stop faster.
14. Ads banner to pay for hosting (1, Extra): breaks V2.
15. Text-message alerts for flip phones (4, User): Walt "I don't carry my smartphone at night."
16. "Times may be wrong" message when data can't load (2, Spec): S8; Jay from sprint 2.
Total 41 points; three sprints hold 30.

Spec checklist: S1 Pick a stop from a list. S2 Shows the next arrival for that stop. S3 Alerts 5 minutes before arrival. S4 Times refresh at least every 30 seconds. S5 Every control has a name a screen reader can say (WCAG 2.2, 4.1.2). S6 Text can be resized to 200 percent without losing content (WCAG 1.4.4). S7 Text contrast at least 4.5:1 (WCAG 1.4.3). S8 When arrival data can't load, the app says so instead of showing old times. A check passes when its card is Done; "Not built" when it isn't; Fail never appears unless a blocked card was planned for it this sprint ("✗ Fail: blocked").

Personas (all made up; task for everyone: "Find when the next bus comes to your stop."):
- Ana, uses a screen reader (blind). Blocked if 1 or 2 not Done. If 5 not Done: Blocked, "The buttons just say 'button'." Else Succeeded, "I heard the time right away."
- Walt, 72, low vision, sets text very large. If 6 not Done: Struggled, "The times got cut off when I made the text bigger." If 7 not Done: Struggled, "Gray on gray. I can't read it." Else Succeeded. If 15 not Done, an extra note (no result change): "I don't carry my smartphone at night. A text would help."
- Rosa, reads Spanish best. If 8 not Done: Struggled, "I guessed what 'Arriving' meant." Else Succeeded, "Ya sé cuándo llega." with "(I know when it's coming.)"
- Dee, parent with a stroller, one thumb free. If 11 not Done: Struggled, "Four taps every time, with one thumb." Else Succeeded; plus "Saved stops helped" if 10 Done; plus "Found my stop fast" if 13 Done.
- Jay, works nights. If 4 not Done: Struggled, "The time didn't change while I waited." From sprint 2, if 16 not Done: Struggled, "One night it showed times from an hour ago." Else Succeeded.
Everyone is Blocked if card 1 or 2 is not Done. Struggled lines raise their card's tag "Reported by (name)" and move it to the top of the Backlog.
Client review notes: card 14 "Client: We said no ads. Please take it out."; card 12 "Client: This sends where riders are. We promised we wouldn't."
Retro chips, Went well: "We stuck to the plan", "We fixed what testers found", "Everyone had a say", "We kept the client's values". Change next time: "Plan smaller", "Test before Done", "Ask the client sooner", "Read the user notes together".

Checked plans (the build reproduces each):
- Plan A (spec first): sprint 1: 1, 2, 3, 7 (10); sprint 2: 4, 5, 6, 16, 11 (9); sprint 3: 8, 10, 13 (9). Release: 8 of 8 checks; 5 Succeeded; 4 of 4 values; 28 points Done.
- Plan B (shiny first): sprint 1: 1, 9, 14 (9); sprint 2: 2, 12, 3, 11 (10); sprint 3: 4, 5, 6, 7 (7) plus 8 (3) = 10. Release: S1 to S7 pass, S8 Not built (7 of 8); Jay Struggled (data feed), others Succeeded; values kept 2 of 4 (V2 and V3 broken, cards 14 and 12 sent back); 29 points spent, 25 Done and kept.
- Plan C (blocked): sprint 1: 1, 3, 4 (8) with 2 not planned: 3 and 4 Blocked, only 1 Done; everyone Blocked in user tests; 5 points spent on blocked cards.

## Interactions in detail
- Capacity is enforced at Plan: a card that would pass 10 points won't drop in ("Over by 2 points"). Unused points are simply unused.
- Dependency order in Build: if a card's dependency is planned later in the same sprint, the dependency is built first and the order shown changes with a note.
- Hand-off screens hide the board so seats really switch (the smallest team is 2; there is no solo mode). A **Skip hand-offs** toggle in the panel footer exists for teachers demonstrating on a projector.
- Undo last move works for Plan moves only. Nothing else can be undone; **New project** starts over.
- Won't do cards can be restored in Design doc at any time before sprint 3.
- Save board on this device stores the board, results and retros (no names exist); Clear saved removes it.
- Keyboard: every card is focusable; Enter picks up, arrows choose a lane or position, Enter drops. Visible focus.
- Sizes: all five lanes and the capacity bar fit without scrolling at 1366x768 and 1280x720 (cards compact to title and points; tap to expand). At 760 wide the lanes become tabs with counts. At 680x425 the hand-off screen and the active lane fit. Card text at least 13 px.

## Look
- Own light palette: whiteboard `#f7f8fa`, panel `#ffffff`, ink `#1c2330`, muted `#555e6e`, lane rules `#d5d9e0`, accent `--brand #2d3fbf` (marker blue: header rule, buttons, the active role glow, capacity bar) with white text.
- Card colors by type (always with the type word): Spec `#fff4b8`, Access `#d9f2e4`, User `#ffd9e2`, Extra `#dbe7ff`; value-break label border `#b91c1c` with the word "Value".
- Contrast (computed): brand on whiteboard 7.67:1, white on brand 8.16:1; ink on Spec 14.17:1, Access 13.34:1, User 12.21:1, Extra 12.67:1; muted on whiteboard 6.15:1. All pass AA.
- Neighbors: pull-request-review (this group) wine on a pale page, catalog-column-rules purple on manila, cloud-through-time teal on archive paper; data-policy-council navy on paper; the dark 9-12 CS tools. Marker blue on a whiteboard is unused.

## Art
none: drawn in code (board, sticky cards, persona initials badges, the phone mockup in Release, preview.svg: the board mid-sprint with a "Reported by Ana" card).

## Voice
Bank voice `easy-coach`, style "Say in an easy-going, encouraging way, like a relaxed sports coach": a coach calling the team's plays. Not used by a 9-12 CS tool or a group sibling. Light narration:
1. how, welcome (Design doc): "Pick who you're designing for and what you won't do. Then start sprint one."
2. how, first Plan step: "Product lead, drag cards into this sprint. Ten points fit."
3. event, every hand-off (stale once Ready is pressed): "Pass the laptop to the [role]." (four recorded variants, one per role)
4. event, any card Blocked in Build: "A card got blocked. It needs another card done first."
5. event, a persona Struggled or Blocked (once per sprint, after user tests): "Your testers found problems. Their cards moved to the top of the backlog."
6. event, client sends a card back: "The client said no to a card. Read their note."
7. how, welcome (Release): "Here's what you shipped. Copy the release notes for your class."
Read speaks the hint. Persona quotes are read on screen, not spoken.

## Family engine
none

## Sources
- CSTA 2026 PK-12 Computer Science Standards: https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA 2017: https://csteachers.org/k12standards/
- Sprints, backlog, capacity and retrospectives: Schwaber and Sutherland, "The Scrum Guide", November 2020: https://scrumguides.org/scrum-guide.html
- Human-centered design and usability testing: ISO 9241-210:2019 (human-centred design for interactive systems), summarized at https://www.iso.org/standard/77520.html ; Nielsen Norman Group, "Usability Testing 101": https://www.nngroup.com/articles/usability-testing-101/
- Spec checks S5 to S7: W3C, WCAG 2.2: 4.1.2 Name, Role, Value; 1.4.4 Resize Text (200 percent); 1.4.3 Contrast (Minimum) 4.5:1: https://www.w3.org/TR/WCAG22/
- Maple Valley Transit, the personas, the backlog and the values are made up; checked plans were worked out with the rules above.

## Done when
1. Team of 3: the role strip shows Seat 1 Product lead and Designer, Seat 2 Developer, Seat 3 Tester; sprint 2 rotates them.
2. Plan refuses a card that passes 10 points with "Over by N points".
3. Plan A gives 8 of 8 checks, 5 Succeeded, 4 of 4 values, 28 points Done.
4. Plan B ends with S8 Not built, Jay Struggled with the old-times quote, cards 14 and 12 sent back with the client notes, values 2 of 4.
5. Plan C: cards 3 and 4 Blocked with "Needs: Next arrival time", every persona Blocked.
6. A Struggled result tags its card "Reported by" and moves it to the top of the Backlog.
7. Hand-off screens hide the board until Ready; Skip hand-offs removes them.
8. Five lanes and the capacity bar fit without scrolling at 1366x768; at 760 wide lanes become tabs.
9. Voice: line 2 plays once; line 3 plays at each hand-off and is dropped if Ready is pressed first.

## Open questions
- [sprint-board] The tool is built for one shared laptop with hand-off screens. Should it also support each student on their own laptop (that would need syncing, which the no-network rule rules out)?
