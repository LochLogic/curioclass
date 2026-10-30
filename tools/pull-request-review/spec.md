# Pull Request Review

## One idea
An AI helper opened three pull requests on a robotics club's website and says "All tests pass": you are the reviewer, and every claim it makes is a lead to check (its tests never try a 13th signup, its "no third-party code" sits above a file copied from a GPL project, its search calls an array method that doesn't exist), so you leave comments on the exact lines, back each one with evidence you ran, and decide approve, request changes or rewrite, knowing one of the three is actually fine.

## Not like
- ai-code-inspector (6-8, gap fill, not specced): checks AI-written code against docs and tests and logs changes. Here the work is a full code review with verdicts, license compatibility and credit, and one pull request is clean so "AI wrote it" is never the verdict by itself.
- capture-the-flag (9-12 CS): finds holes in a made-up company's systems. Here nothing is attacked; the evidence is tests, a preview and documentation.
- api-playground (9-12 CS): builds an app from documented modules. Here you read someone else's code against requirements and a reference.
- misleading-charts (6-8, mystery): a fact-check desk for charts. Same case-file format, different evidence (code, tests, licenses).
- dice-in-the-chatbot (this group): how an AI picks words. This tool judges what an AI built, line by line.
- sprint-board (this group): a team plans and tests its own app. Here you review code you did not write.

## Who and how
- Grades 9 to 12, computer science. Module: Reviewing AI-Written Code (Algorithms and Programming), "Evaluate AI-generated code against requirements and credit every source". Topic line: "reviewing AI-written code and crediting sources".
- Driver: students on laptops, alone or in pairs. 30 to 45 minutes (Case 1 about 20).
- Standards (module codes, CSTA 2026): HS-PRO-RD-18 (evaluate AI-generated code against requirements and documentation: every case), HS-PRO-PD-14 (credit sources and respect licenses: Case 1's license and credit). CSTA 2017 crosswalk: 3B-AP-23 (evaluate key qualities of a program through code review), 3B-AP-21 (develop and use test cases), 3A-AP-20 (evaluate licenses that limit or restrict use of computational artifacts).
- tool.json: driver "students", minutes "30-45", modes ["Case 1", "Case 2", "Case 3"], grades_label "Grades 9-12".

## Screens and modes
Own light `:root` (a code-review page: white diff on a pale page), theme-912 class names kept with light values. Header: "Pull Request Review", small line "Lakeside Robotics Club website". Case buttons: **Case 1** (opens first), **Case 2**, **Case 3**, each with a status word (Open, Reviewed, Merged). Motion, Sound, Read.

Each case is one pull request page with tabs across the stage. Focus: the open tab's main object, centered and largest: the diff in Files changed (the case opens here after a first look at Conversation), the result list in Checks, the browser frame in Preview, the file in Repo files; the Case file panel beside it stays narrower.
- **Conversation**: the pull request title, the author "Helper (AI assistant)", its description (Content), the linked issue with the **Requirements** list, and the review timeline (comments the student posts appear here).
- **Files changed**: a unified diff per file, line numbers on the left, added lines with "+" on a blue tint, removed lines with "-" on an orange tint. Tap (or Enter on) any line: a comment box opens under it with six tag buttons, **Bug**, **Requirement not met**, **License or credit**, **Test gap**, **Question**, **Nit**, and a list of prewritten comment lines for that tag (Content gives the ones tied to clues; every tag also has "Something else looks off here"). Posting adds a marker on the line and an entry in the timeline. No free typing.
- **Checks**: two buttons, **Run PR tests** (the helper's own tests) and **Run club tests** (acceptance tests the club wrote from the requirements). Results list each test with ✓ Passed or ✗ Failed and its message, one row every 120 ms (under 1 s); a tap during the list (another run, a tab, a comment) fills the rest at once, then acts. Each run adds an evidence card.
- **Preview**: the feature running in a small browser frame drawn in the page (made-up site, nothing loads from a network). The club site's header shows its painted robot (Art) in both light and dark mode; Case 3's search results show each part's painted thumbnail. Case 1: a signup form plus **Fill 12 people** and **Add one more** buttons and the list of Confirmed, Waitlist and "Spots left". Case 2: the site with its toggle. Case 3: the parts search box. Errors show in a console strip under the frame. Each preview action that shows something adds an evidence card.
- **Repo files**: README, CONTRIBUTING.md, LICENSE, CREDITS.md and a **JavaScript reference** (Array methods list, Content). Tapping "Cite this line" on any line adds it as an evidence card.

Panel (all tabs): **Case file**: the comments posted, each with its evidence slots (**Attach evidence** opens the evidence cards gathered so far); then **Verdict**: **Approve**, **Request changes**, **Rewrite with credit** (Request changes and Rewrite with credit are enabled once the case has a blocking comment; Approve always is; Case 2 offers Approve and Request changes), and **Submit review**. Submitting needs every Bug, Requirement not met, License or credit and Test gap comment to have at least one evidence card; otherwise the panel lists which comments still need evidence. After Submit: **Maintainer's notes** (Content) open beside the case file, comparing the student's comments with the clues, never a score. For Case 1 and 3 with Request changes or Rewrite, a **Fix it** section appears: fix choices (Content), **Run club tests** again, and **Merge** (enabled only when every club test passes and no license comment is open).

## Content
Repo facts: LICENSE is MIT ("Copyright (c) 2025 Lakeside Robotics Club"). CONTRIBUTING.md: "This site is MIT licensed. Code you copy in must have a license that lets us share it under MIT, such as MIT, BSD or Apache-2.0. Credit every copied piece in CREDITS.md with its source and license." CREDITS.md starts with one line: "Fonts: (system fonts only)".

**Case 1: PR #15 "Add event signup with waitlist"** (fixes issue #14).
Description: "Adds a signup form, waitlist logic and tests. All tests pass ✓. No third-party code was used."
Requirements (issue #14): R1 A form asks for name and email; both are required. R2 A badly formed email is refused. R3 The event holds 12 people: signups 1 to 12 are confirmed, the 13th and later go on the waitlist. R4 The page shows how many spots are left. R5 One signup per email, ignoring capital letters. R6 When a confirmed person cancels, the first person on the waitlist is confirmed.
File `signup.js` (new):
```js
import { isValidEmail, normalizeEmail } from './utils/email.js';

export const CAPACITY = 12;

export function createEvent() {
  return { confirmed: [], waitlist: [] };
}

export function signUp(event, name, email) {
  if (!name || !email) return { ok: false, error: 'Name and email are required.' };
  if (!isValidEmail(email)) return { ok: false, error: 'Enter a real email address.' };
  const key = normalizeEmail(email);
  const everyone = [...event.confirmed, ...event.waitlist];
  if (everyone.some(p => p.key === key)) return { ok: false, error: 'You are already signed up.' };
  const person = { name, email, key };
  if (event.confirmed.length > CAPACITY) {
    event.waitlist.push(person);
    return { ok: true, status: 'waitlist' };
  }
  event.confirmed.push(person);
  return { ok: true, status: 'confirmed' };
}

export function cancel(event, email) {
  const key = normalizeEmail(email);
  const i = event.confirmed.findIndex(p => p.key === key);
  if (i === -1) return false;
  event.confirmed.splice(i, 1);
  if (event.waitlist.length > 0) event.confirmed.push(event.waitlist.shift());
  return true;
}

export function spotsLeft(event) {
  return CAPACITY - event.confirmed.length;
}
```
File `utils/email.js` (new):
```js
// Source: mailcheck-lite v2.1, src/validate.js
// Copyright (c) 2018 the mailcheck-lite authors. Licensed under GPL-3.0-or-later.
const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function isValidEmail(email) {
  return EMAIL_PATTERN.test(email.trim());
}

export function normalizeEmail(email) {
  return email.trim().toLowerCase();
}
```
File `signup.test.js` (new), the helper's tests: "confirms the first person", "fills all 12 spots" (12 signups, expects 12 confirmed), "refuses the same email twice" (same capitals both times), "requires name and email". All four pass.
Club tests: A1 name and email required ✓; A2 "sam@club" is refused ✓; A3 the 13th signup goes on the waitlist ✗ "expected 'waitlist', got 'confirmed'"; A4 spots left is 0 after 13 signups ✗ "expected 0, got -1"; A5 "Sam@Club.org" after "sam@club.org" is refused ✓; A6 after 14 signups, when person 1 cancels, the first waitlisted person is confirmed ✓.
Clues (each with its prewritten comment): C1 Bug on the line `if (event.confirmed.length > CAPACITY)`: "The 13th person is confirmed. This should be >=." C2 Test gap on "fills all 12 spots": "No test signs up a 13th person." C3 License or credit on the GPL header: "GPL-3.0 code can't be shared under our MIT license (CONTRIBUTING.md)." C4 Question on the description: "The description says no third-party code, but utils/email.js is copied." C5 License or credit on CREDITS.md (unchanged, shown as "no changes"): "The copied file isn't credited." Red herring: the email pattern "won't catch every bad address": A2 passes and R2 asks no more, so a Nit or Question is fine, a Bug comment is noted by the maintainer as "not required by R2".
Fix choices: Bug: "Change > to >=" (fixes A3 and A4) or "Change CAPACITY to 11" (A3 passes, A4 still fails "expected 0, got -1", and R3 says 12: shown so the student sees a patch that hides the bug). License: "Replace utils/email.js with our own two functions" (the club writes them: same code with the header "Written by Lakeside Robotics Club"), "Use validate-mini (MIT) and credit it in CREDITS.md" (adds the line "utils/email.js: from validate-mini 1.0, MIT License, (c) 2020 validate-mini contributors"), "Keep it and add a credit line" (refused at Merge: "Credit doesn't change the license"), "Switch the whole site to GPL-3.0" (refused: "Not a review fix. The club decides its license."). Test gap: "Add a test for the 13th signup" (adds test 5 to the helper's tests).
After ">=" and either good license fix: all six club tests pass and Merge is enabled; after Merge the case shows Merged with the final diff.

**Case 2: PR #16 "Add a dark mode toggle"** (issue #12). Description: "Adds a toggle that switches the site between light and dark and remembers the choice on this device."
Requirements: R1 A button switches light and dark. R2 The choice is remembered on this device. R3 Text and links are at least 4.5:1 in both modes. R4 The button works from the keyboard and says whether dark mode is on.
`theme.css` (changed): `:root { --bg: #ffffff; --text: #1c2330; --link: #0b5cad; }` and `:root[data-theme="dark"] { --bg: #121820; --text: #e6edf3; --link: #8cc8ff; }` with `body { background: var(--bg); color: var(--text); } a { color: var(--link); }`.
`theme.js` (new):
```js
const KEY = 'club-theme';
const btn = document.querySelector('#theme-toggle');

function applyTheme(t) {
  document.documentElement.dataset.theme = t;
  btn.setAttribute('aria-pressed', String(t === 'dark'));
}

let saved = null;
try { saved = localStorage.getItem(KEY); } catch (e) {}
applyTheme(saved === 'dark' ? 'dark' : 'light');

btn.addEventListener('click', () => {
  const t = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  applyTheme(t);
  try { localStorage.setItem(KEY, t); } catch (e) {}
});
```
`index.html` (changed): `<button id="theme-toggle" type="button" aria-pressed="false">Dark mode</button>`.
Club tests: B1 toggling sets data-theme to dark ✓; B2 the choice survives a reload ✓; B3 contrast: light text 15.76:1, light links 6.67:1, dark text 15.10:1, dark links 10.04:1, all at least 4.5 ✓; B4 the button is a real button with aria-pressed ✓. PR tests: 3, all pass.
No clues. One possible Nit: "Name t theme, so it reads clearly." Maintainer's notes: "This one is good. Approving it, with or without the nit, is the right call. Reviewing means checking, not rejecting."

**Case 3: PR #17 "Add search to the parts list"** (issue #9). Description: "Adds fuzzy search using the built-in Array.prototype.fuzzyFilter. Tests pass ✓."
Requirements: R1 Typing part of a name shows the matching parts. R2 Capital letters don't matter. R3 An empty search shows every part. R4 No matches shows "No parts match."
`parts.js` (unchanged, shown): Micro servo, Servo horn kit, Wheel 65 mm, Battery pack 4xAA, Ultrasonic distance sensor, Line sensor, Jumper wires, Motor driver board.
`search.js` (new):
```js
import { parts } from './parts.js';

// Uses the built-in Array.prototype.fuzzyFilter to match partial names.
export function searchParts(query) {
  const q = query.trim().toLowerCase();
  if (q === '') return parts;
  return parts.fuzzyFilter(p => p.name.toLowerCase(), q);
}
```
`search.test.js` (new): first line `parts.fuzzyFilter = (key, q) => parts.filter(p => key(p).includes(q));` then "finds servo" (expects 2). Passes.
Club tests: D1 "servo" finds 2 ✗ "TypeError: parts.fuzzyFilter is not a function"; D2 "SERVO" finds 2 ✗ same error; D3 empty search returns 8 ✓; D4 "zzz" finds 0 ✗ same error. Preview: typing any letter shows the error in the console strip.
JavaScript reference (Array methods listed): every, filter, find, findIndex, includes, indexOf, join, map, reduce, slice, some, sort. Each with a one-line description; no fuzzyFilter.
Clues: E1 Bug on the fuzzyFilter line: "There is no fuzzyFilter method in JavaScript (see the reference)." E2 Test gap on the test's first line: "The test creates fuzzyFilter itself, so it can't catch this." E3 Question on the comment line: "This calls a method the reference doesn't list."
Fix choices: "Use filter and includes" (`return parts.filter(p => p.name.toLowerCase().includes(q));`: D1 to D4 pass), "Add fuzzyFilter to Array.prototype" (D1 to D4 pass; Merge is allowed, with the maintainer's note "This works, but changing a built-in object can break other code. The club prefers filter."), "Delete the test" (refused: "The club tests still fail.").

Maintainer's notes per case: Case 1 lists C1 to C5 and the red herring, each marked "You found this" or "Look again at line N" (with a jump link). Case 3 lists E1 to E3 the same way.

## Interactions in detail
- All code is display only; the tests and preview run on the tool's own small model of each file's behavior, written to match the code shown exactly (the build includes a check that runs the real code shown above, as modules in the page, against every club test and compares).
- Evidence cards: a test run (each test result line), a preview action (for example "Added person 13: confirmed, spots left -1"), a cited repo or reference line. Cards are reused across comments.
- Approve with an open Bug or License comment: allowed, with a confirm line "You approved with 2 blocking comments open." Then the maintainer's notes say what would have shipped.
- Rewrite with credit opens Fix it with the license choices first.
- Reset case (in the panel footer) clears comments, evidence, verdict and fixes for that case. Nothing is saved after the page closes; no typed text exists.
- Keyboard: case buttons, tabs, then diff lines (arrow keys move between lines, Enter opens the comment box), then the panel. Visible focus.
- Sizes: the diff (at least 20 lines visible) and the Case file panel fit side by side without scrolling at 1366x768 and 1280x720; at 680x425 the panel becomes a drawer with a "Case file (3)" button. Code in the readout font at least 13 px; long lines wrap with a ↪ mark, never scroll sideways.

## Look
- Own light palette: page `#f6f7f9`, panels `#ffffff`, ink `#1c2330`, muted `#555e6e`, lines `#d9dde3`, accent `--brand #8e1b4f` (wine: verdict buttons, comment markers, the header rule) with white text.
- Diff: added lines tint `#ddeeff` with "+", removed `#ffe8d6` with "-" (a blue and orange pair that colorblind readers can tell apart, and the signs carry it anyway). Checks: ✓ Passed in `#166534`, ✗ Failed in ink on a pale `#fde2e2` row with a left bar.
- Contrast (computed): brand on page 8.10:1; white on brand 8.68:1; ink on white 15.76:1; muted on white 6.54:1; ink on the added tint 13.32:1 and on the removed tint 13.33:1; pass green on white 7.13:1. All pass AA.
- Neighbors: the dark 9-12 CS tools (pink, violet, lemon, sky blue, orange) and data-policy-council's navy on paper; sprint-board (this group) is royal blue on a whiteboard, catalog-column-rules purple on manila. Wine is unused.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: bright painted product illustration on plain white (cut out), like photos on a small club website.
- club-robot: "A small four-wheeled hobby robot with an ultrasonic sensor on the front, a blank circuit board on top and coiled wires, sitting on a wooden workbench, painted illustration"; 16:9; cutout no; people no; the club site's header in every Preview (light and dark).
- Parts thumbnails, one shared prompt "[part], painted product illustration, plain white background" with: part-servo "a small blue micro servo motor with a white horn"; part-horn-kit "a set of small white plastic servo horns in different shapes"; part-wheel "a rubber robot wheel with a yellow hub"; part-battery "a black battery holder with four AA batteries"; part-ultrasonic "an ultrasonic distance sensor board with two silver round transducers"; part-line-sensor "a small line sensor board with infrared emitters"; part-jumpers "a bundle of rainbow jumper wires"; part-motor-driver "a small red motor driver board with screw terminals"; 1:1 each; cutout yes; people no; Case 3's parts list in Preview, 48 px beside each name.
The pull request pages, the diff, checks, the browser frame chrome, the console strip, repo files and preview.svg are drawn in code (text and interface).
## Voice
Bank voice `firm-captain` (Alnilam), style "Say firmly but kindly, like a ship captain giving clear directions": the club's lead maintainer handing over reviews. Not used by a 9-12 CS tool or a group sibling. Light narration, `Curio.voice`, `scope: () => state.caseId`. Read speaks the hint. Code is never spoken.
- w-case1 (how, Case 1 welcome; stale on the first comment): "The helper says all tests pass. Check that yourself. Open Files changed and tap any line to leave a comment."
- evidence (how, first comment posted that needs evidence; stale when it gets a card): "Now back it up. Press Run club tests or try the Preview, then press Attach evidence."
- clubfail (event, Run club tests with any failure; stale after another run): "The club's own tests fail. Open the failing one and find the line behind it."
- sent (event, Submit review, every time; stale on Reset case): "Review sent. Read the maintainer's notes beside your case file."
- merged (event, Merge, every time; stale on case change): "Merged. Every club test passes."
- w-case2 (how, Case 2 welcome; stale on the first verdict pick): "Same helper, new pull request. Check it, then press Approve or leave a comment on a line."
- w-case3 (how, Case 3 welcome; stale on the first comment): "This one says its tests pass too. Open Checks and press Run club tests."
Request changes and Rewrite with credit are disabled until a blocking comment exists, and Merge until the club tests pass, so no line names them while disabled.
## Family engine
none

## Sources
- CSTA 2026 PK-12 Computer Science Standards: https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA 2017: https://csteachers.org/k12standards/
- GPL code can't be relicensed under MIT; MIT code can go into GPL projects: Free Software Foundation, "Frequently Asked Questions about the GNU Licenses": https://www.gnu.org/licenses/gpl-faq.html ; "Various Licenses and Comments about Them" (MIT/Expat is GPL-compatible, one way): https://www.gnu.org/licenses/license-list.html
- MIT License text (keep the copyright and permission notice): Open Source Initiative: https://opensource.org/license/mit
- Array methods and that no fuzzyFilter exists: MDN Web Docs, "Array": https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array ; modifying built-in prototypes is discouraged: MDN, "Inheritance and the prototype chain" (bad practice: extension of native prototypes).
- Contrast 4.5:1 for text: WCAG 2.2, Success Criterion 1.4.3: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum ; ratios computed with the WCAG formula.
- Code review practice: Google Engineering Practices, "How to do a code review": https://google.github.io/eng-practices/review/reviewer/
- The club, the helper, mailcheck-lite, validate-mini and all code are made up.
- Checks run (Python, 2026-10-29, a port of signup.js and the email pattern): with ">" the 13th signup is confirmed and spots left is -1 (A3 and A4 fail); A6 passes but leaves 13 confirmed; with ">=" A3 to A6 pass and spots left is 0; with CAPACITY 11 A3 passes and A4 still reads -1; "sam@club" is refused and "Sam@Club.org" after "sam@club.org" is a duplicate. Case 2 contrast 15.76, 6.67, 15.10, 10.04 and every ratio in Look recomputed with the WCAG formula; all as stated.

## Done when
1. Case 1 Run PR tests: 4 passed. Run club tests: A3 and A4 fail with the stated messages; the others pass.
2. Preview, Fill 12 people then Add one more: person 13 is Confirmed and Spots left reads -1.
3. Posting a Bug comment on the > line without evidence blocks Submit and names that comment; attaching the A3 result unblocks it.
4. Fix: ">=" plus "Replace with our own" makes all six club tests pass and enables Merge; "Keep it and add a credit line" keeps Merge disabled with its reason; "Change CAPACITY to 11" passes A3 but still fails A4 with "expected 0, got -1".
5. Case 2: all club tests pass, the contrast test lists 15.76, 6.67, 15.10 and 10.04; Approve with no comments submits, and the notes call it the right call.
6. Case 3: club tests D1, D2, D4 fail with the TypeError; the reference lists no fuzzyFilter; "Use filter and includes" makes all four pass.
7. The build's check runs the shown code itself and agrees with every club test result above.
8. Diff and Case file fit side by side at 1366x768; no horizontal scroll at 375 wide (lines wrap).
9. Focus: at 1366x768 and 1000x625 the open tab's main object (diff, results, preview frame, file) is the largest thing on the stage.
10. Tap while it plays: while club test rows are appearing, a tab switch or a comment acts at once and the list is complete when you come back; no voice line names a disabled verdict or Merge.

## Open questions
- [pull-request-review] Case 1's license lesson uses GPL-3.0 code in an MIT project. Is GPL the right example for grade 9-12, or would a "no license at all" snippet (all rights reserved) be clearer?
