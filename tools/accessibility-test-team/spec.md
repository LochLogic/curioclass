# Accessibility Test Team

## One idea
A club sign-up app sits in a phone frame, built by a student who tried it once and called it done, and three tester cards wait beside it, each a made-up student labeled "illustration": Marcus, who is blind and uses a screen reader; Lucía, who moved here from Colombia last year and is still learning English; and Theo, whose hand shakes; the child takes each tester's turn signing up for robotics club: in screen reader mode the page is read aloud in its real order ("image, image, button, button") with nothing saying which button signs up; in new-to-English mode the idioms and tiny print show the way they read ("Hop on board, it's a no-brainer!"); in shaky-hand mode the pointer trembles and the tiny Submit button keeps getting missed; each failure goes on a bug card with the tester, the step and what happened; then three teammates, each speaking for one tester, have time for four fixes, and the child runs a fair round where every voice gets at least one, then makes them (alt text, labels, plain words, bigger buttons); all three testers try again, and a scoreboard shows who can now sign up; at the end the child sees that the app worked for the person who built it and failed three other people, and testing with them is how you find out, so a student in grades 6 to 8 learns to find and fix accessibility gaps with user feedback and inclusive teamwork.

## Not like
- design-for-a-friend (5, spec): interviewing one user for a design. Here testing as three users and fixing.
- sprint-board (Grades 9-12, spec): team sprints with testers. Here one app and a fair fix round.
- three-route-rules (3, spec): rules that help some travelers. Here an app that blocks some users.
- metadata-x-ray (Grades 6-8, spec): personal data. Here access for every user.

## Who and how
- Grades 6-8, Computer Science, module "Design for Every User". Standards: MS-ALG-IM-09, MS-PRO-TR-20, MS-SYS-IM-36, MS-PRO-PD-15 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Find and fix accessibility gaps with user feedback and inclusive teamwork").
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three tester modes, bug cards, a fix round of four with three teammates, eight possible fixes, the retest scoreboard. Extra: Real team (three students each take a tester role). tool.json `modes: ["Test", "Real team"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ALG-IM-09 | Compare one design choice across testers | tiny print fine for one, a wall for another | 2 |
| MS-SYS-IM-36 | Use the app through a screen reader, plain view and a shaky pointer | three ways to reach one app | 2 |
| MS-PRO-TR-20 | Log failures; retest after fixing | bug cards; the scoreboard | 3 |
| MS-PRO-PD-15 | Run a fair round where every voice gets a fix | four fixes, three voices | 4 |

## Screens and modes
Header (kit): title "Accessibility Test Team"; `Test`, `Real team`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The app in a phone frame, three tester cards, an empty bug board. The welcome is queued (`welcomeAfter: true`): "This app works for the person who made it. Pick a tester and try to sign up." First hint: "Tap a tester card."

**Test as (focus: the app).** At 1366x768 the phone is center with testers left and bugs right; at 680x425 testers and bugs are tabs. Screen reader mode dims the screen and reads the elements in their real order using the browser's speech synthesis, with captions; Tab moves through them. New-to-English mode marks idioms and small print. Shaky-hand mode adds a gentle tremor to the pointer and keyboard focus stays steady. A step that fails offers `Log bug`.

**Bug card.** Tester, step, what happened; the child picks from chips.

**Fix round.** Three teammates (Marcus's friend Aisha, Lucía's lab partner Ben, Theo's brother Sam, labeled "illustration") each argue for a fix; there are four fix slots. The tool flags a round that leaves a voice with none. Fixes change the app's code for real (alt text, labels, plain wording, 44 px buttons, a bigger Submit).

**Retest.** All three testers try again; the scoreboard shows signed up or blocked and which bug remains.

**Test with them (the aha).** Narrator: "It worked for the builder and failed three people. You only find that out by testing with them."

**The end.** The bug board, the fixes and the scoreboard. `Print` prints them.

**Real team (extra).** Three roles.

## Content
- Testers are portrayed as capable people using their tools well; the app is what fails, never the person.
- The tremor is gentle and can be turned off with Motion; screen reader mode uses speech synthesis only, never the microphone.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Testers can be redone; fixes can be swapped until `Retest`.
- Keyboard: Tab to tester cards, the app's elements, bug chips, teammates and fix slots; Enter picks or logs.
- With Motion off the tremor becomes a narrow target outline that shows how small the button is.

## Look
- Accent `--brand` #2f6a3a test-kit green (header, the bug board, buttons); gold #f4c542 (the tester in focus, a fixed bug); paper #eff6f0; ink #0b220f; muted #4a574c.
- Contrast (WCAG 2.1, computed): white on brand 6.47:1; brand on paper 5.89:1; ink on paper 15.29:1; muted on paper 6.93:1; ink on gold 10.33:1.
- Never color alone: signed up and blocked carry words and icons; bugs carry the tester's name.
- Different from this batch (debugger amber, timeline navy, factory red-orange, x-ray plum).

## Art
- People (illustrated): three testers and three teammates, labeled "illustration" (Gemini, `people: true`, 6; cutout yes).
- Drawn in code: the app, so it can really break and be fixed; the bug board and scoreboard.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` for the teammates' fix pitches; `curious-librarian` as the narrator and hints. Screen reader mode uses the browser's speech synthesis, not the bank. `Curio.voice` with `scope: () => state.mode + ':' + state.tester + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `tester`: "Tap a tester card."
- how `try`: "Try to sign up for robotics club."
- how `log`: "Tap Log bug, then pick what happened."
- how `fix`: "Drag a fix into an open slot."
- how `retest`: "Tap Retest."
- event, whole, test with them.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the app as real HTML with planted gaps, a reading-order speaker, the tremor pointer, bug cards, the fair-round check, the retest.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Test | Test as one tester | The fix round opens after all three. |
| Fair round | Give all four fixes to one voice | The round flags a voice with none. |
| Retest | Skip it | The end needs the scoreboard. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `tester`; `try`.
2. `log`.
3. `fix`; `retest`.
4. Test with them (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Images need text alternatives and form fields need labels | W3C (2023), WCAG 2.2, success criteria 1.1.1 and 3.3.2 | WebAIM, "Alternative Text" and "Creating Accessible Forms" | yes |
| Screen readers read elements in page order | WebAIM, "Designing for Screen Reader Compatibility" | W3C (2023), WCAG 2.2, success criterion 1.3.2 Meaningful Sequence | yes |
| Small targets are hard to hit with a tremor; WCAG asks for at least 24 px | W3C (2023), WCAG 2.2, success criterion 2.5.8 Target Size (Minimum) | W3C WAI, "Understanding Success Criterion 2.5.5 Target Size" and its tremor examples | yes |
| Plain words help readers new to a language | PlainLanguage.gov, Federal Plain Language Guidelines | W3C WAI, "Making Content Usable for People with Cognitive and Learning Disabilities" | yes |
Backed twice: 5. Cut: 0.

Sensitivity: disability and language-learner portrayal; a fresh-agent sensitivity review is owed before Live.

Checks run (Python, scratchpad s25, 2026-11-10): four fixes across three voices gives each at least one with one to spare; fixed buttons are 44 px, above the 24 px minimum; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 phone, testers and bugs; at 680x425 testers and bugs as tabs.
2. All three testers are tried and their failures compared. (MS-ALG-IM-09, MS-SYS-IM-36)
3. Failures are logged and the app retested. (MS-PRO-TR-20)
4. A fair round gives every voice a fix. (MS-PRO-PD-15)
5. Testers are shown as capable; the app is what fails.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the tremor becomes an outline; no microphone; no network requests.

## Open questions
None.
