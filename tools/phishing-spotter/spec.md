# Phishing Spotter

## One idea
Messages, texts and sign-in pages from made-up places slide in one after another and you keep or report each in seconds, but a report only scores full points when you also tap the tell that gave it away (a look-alike address, a link that really goes somewhere else, a rush, a request for a password), so speed is built on reasons, not hunches.

## Not like
- data-defenders (grade 5, same family): slow escape-room puzzles about a school's stored data. Here it is fast rounds about tricks aimed at you.
- capture-the-flag (9-12, same family): deep single challenges with a patch step. Here many short calls, each a few seconds.
- packet-race (6-8, same wave group): a race of steering on a map. Here a score chase of reading.
- misleading-charts (6-8): spotting tricks in charts. Here the tricks are in messages, and every example is made up.
- algorithm-audit (6-8): auditing a system for bias; nothing to do with messages.

## Who and how
- Grades 6 to 8, computer science. Module: Cyber Attacks and Defense (Systems and Security), "Common attacks and the CIA triad".
- Topic line: "spotting phishing messages and fake sign-in pages".
- Driver: students on their own laptops; the teacher can run Practice on a projector first.
- 10 to 20 minutes: Practice (5 min), Arcade rounds (60 s each, as many as time allows), Tells (any time).
- Standards (CSTA 2026, as listed): MS-SYS-SE-32, MS-SYS-SE-33. 2017 crosswalk: 2-NI-05 (explain how physical and digital security measures protect electronic information).
- tool.json: driver "students", minutes "10-20", modes ["Practice", "Arcade", "Tells"], grades_label "Grades 6-8". Kit starter plus `kit:security`.

## Screens and modes
Header (kit): "Phishing Spotter", small line "Keep it or report it". Mode buttons: **Practice** (opens first), **Arcade**, **Tells**. Then Motion, Sound, Read.

Stage: a dark arcade cabinet frame around a bright "screen". On the screen, the current message drawn by the security engine: an email card, a text bubble thread on a phone outline, or a sign-in page in a browser frame. A status bar along the bottom of the screen shows a link's real address on hover, focus or long-press. Beside the screen (below it under 1000 wide), the **Address book** card: the six real places and their real addresses (Content), the way you'd know your own school's site.

Panel: `#hint`; two big buttons **Keep** (check icon, key K) and **Report** (flag icon, key R); after Report on a message, a "Tap the tell" prompt with a 4 s ring (Arcade) or no limit (Practice); then the result strip. Practice adds **Next** and the **Why** card. Arcade adds the clock ring (60 s), Score, Streak, **Start round**, **Best** and **Clear best**.

### Mode 1: Practice (no clock)
A message shows. Hover or focus links to read their real address. Keep or Report. If Report: tap the tell spot(s) on the message (any number; **Done** when finished). The Why card then lists the message's tells with arrows to each spot, or for a safe message the "why it's fine" line. Next brings a new message (all 20 in a shuffled order, then reshuffle).

### Mode 2: Arcade (60-second rounds)
Start round: the clock starts and messages come one at a time from a shuffle of all 20 (no repeats in a round). Scoring per message: Keep a safe one +1. Report a phish, then tap one of its tells within 4 s: +2 (the spot glows, its tell name pops). Report a phish without a right tell (wrong spot or time out): +1, the tells flash. Keep a phish: 0, "Missed" with the tells shown 1.5 s. Report a safe one: 0, "False alarm" with its why line 1.5 s. The next message slides in after each result. Streak counts right calls in a row (display only, no multiplier). At 0: the round card shows Score, right calls "13 of 15", tells tapped, Best, **Play again**.

### Mode 3: Tells (explore)
Eight tell cards (Content), each with a mini example cut from a pool message (tap it to open that message in Practice). A tick marks tells you tapped this page load. A **What to do** card: "Don't click, reply or open the attachment. Report it: tell a trusted adult, or use the Report button in your mail app. To check, go to the real site by typing the address you know."

## Content
Real places and addresses (Address book): Maple Grove Middle School, maplegrove.example (student portal portal.maplegrove.example); Riverbend Library, riverbendlibrary.example; Pebble Quest (a game), pebblequest.example; Hilltop Parcel (deliveries), hilltopparcel.example; Tune Tower (a music app), tunetower.example; Maple Grove Rec Center, maplegroverec.example. All are made up, on reserved domains.

Tells: T1 **Look-alike sender**: the address isn't the real one (a sender name can say anything). T2 **Link goes somewhere else**: the real address under the link isn't the real site. T3 **Rush or threat**: "within 1 hour", "or it will be deleted". T4 **Asks for a password or code**: real services never ask you to send these. T5 **Prize out of nowhere**: free stuff you didn't sign up for. T6 **Surprise attachment**: a file you weren't expecting, especially .zip or .html. T7 **Fake sign-in page**: the address bar isn't the real site, even if the page looks right. T8 **Keep it secret**: asks you not to tell anyone.

Phishing messages (spots are the tells listed):
| id | kind | from (name and address) | subject / title | body | link text, real href / attachment | tells |
|---|---|---|---|---|---|---|
| P1 | email | Maple Grove IT, it-help@rnaplegrove.example | Your school account closes today | "We are updating accounts. Sign in within 1 hour or your account will be closed." | "portal.maplegrove.example", maplegrove.account-check.test/login | T1, T2, T3 |
| P2 | text | +1 555 0142 | | "Hilltop Parcel: your package is on hold. Pay a $1.99 fee today or it goes back: hilltop-parcel-fees.test/pay" | hilltop-parcel-fees.test/pay | T2, T3 |
| P3 | email | Pebble Quest, rewards@pebblequest-prizes.test | You won 10,000 free gems! | "Claim them tonight before they disappear." | "Claim gems", pebblequest-prizes.test/claim | T1, T5, T3, T2 |
| P4 | sign-in | address bar pebblequest.example.signin-help.test | Pebble Quest: Sign in | user name and password fields | | T7 |
| P5 | email | Ms. Ruiz, ms.ruiz.maplegrove@mailbox.test | Quick favor | "I'm in a meeting. Send me the code that just came to your phone. Don't tell anyone, it's a surprise for the class." | | T1, T4, T8 |
| P6 | email | Riverbend Library, notices@riverbend-library.test | Overdue fine: open the attached bill | "You owe a fine. Open the attachment to see it." | fine-notice.zip | T1, T6 |
| P7 | text | Tune Tower, 55590 | | "Your account is locked. Reply with your password to unlock it." | | T4, T3 |
| P8 | sign-in | address bar maplegrove-portal.test | Maple Grove Student Portal | user name and password fields | | T7 |
| P9 | email | Maple Grove Rec Center, frontdesk@maplegrove-rec.test | Free summer camp spot for you! | "You were picked for a free spot. Open the form to claim it." | camp-form.html | T1, T5, T6 |
| P10 | email | Tune Tower, billing@tunetovver.example | Payment failed | "Update your card in 24 hours or lose your playlists." | "Update payment", tunetovver.example/billing | T1, T3, T2 |

Safe messages (and the why line):
| id | kind | from | subject / title | body | link, href / attachment | why |
|---|---|---|---|---|---|---|
| S1 | email | Maple Grove Middle School, office@maplegrove.example | Picture day is Thursday | "Wear your best smile. Order forms are on the school site." | "Picture day info", maplegrove.example/picture-day | Real address, and the link goes where it says. No rush, no request. |
| S2 | email | Riverbend Library, holds@riverbendlibrary.example | Your hold is ready | "The Lighthouse Map is waiting at the front desk. Pick it up by Friday." | | Real address and a normal deadline, with nothing to click or type. |
| S3 | text | Hilltop Parcel, 55512 | | "Your package was delivered at 3:12 p.m. Track it: hilltopparcel.example/t/48213" | hilltopparcel.example/t/48213 | The link goes to the real hilltopparcel.example and asks for nothing. |
| S4 | sign-in | address bar portal.maplegrove.example | Maple Grove Student Portal | fields | | The address bar shows the real portal.maplegrove.example. |
| S5 | email | Pebble Quest, news@pebblequest.example | New level: Crystal Caves is open | "Explore the new caves this weekend." | "See what's new", pebblequest.example/news | Real address, and the link stays on pebblequest.example. |
| S6 | email | Mr. Okafor, j.okafor@maplegrove.example | Science fair sign-up sheet | "As I said in class today, here is the sign-up sheet." | science-fair-signup.pdf | A teacher you know, at the real school address, sending what he said he would. Unsure? Ask him in person. |
| S7 | email | Tune Tower, hello@tunetower.example | Your year in music | "See the songs you played most this year." | "See your year", tunetower.example/year | Real address; the link stays on tunetower.example. |
| S8 | sign-in | address bar pebblequest.example/signin | Pebble Quest: Sign in | fields | | The address starts with the real pebblequest.example. |
| S9 | text | Maple Grove Rec, 55012 | | "Swim lessons start Monday at 4. Reply STOP to unsubscribe." | | A known sender with a normal reminder and nothing to click. |
| S10 | email | Pebble Quest, security@pebblequest.example | New sign-in on a new device | "If this wasn't you, open the Pebble Quest app yourself and change your password. We will never ask for your password." | | Real address. It tells you to open the app yourself and never asks for your password: that is what real alerts do. |

Spot layout: every message's from address, subject, each body sentence, each link, each attachment and (sign-in) the address bar are spots; only the listed tells score. Sign-in pages draw the place's code-drawn logo (a simple shape and its name, made up) so a fake looks the same as the real one: only the address bar differs.

## Interactions in detail
- Links never navigate: a tap on a link in Practice shows "In real life, this would open: <href>" in the status bar; in Arcade it counts as tapping that spot.
- Sign-in fields can't be typed in (they show a lock note "Practice page: nothing you type goes anywhere" on focus, and accept no input).
- Arcade timing: the 4 s tell ring runs inside the round clock; if the round ends during it, the message scores as +1 if it was a phish report.
- Keys: K keep, R report, 1 to 8 tap spots in reading order, Enter for Next or Start round.
- Best score: localStorage `curio-phishing-spotter` (try/catch), Clear best asks Yes/No. Nothing else is stored.
- Motion off: no slide-in; messages swap in place with the same timing; the tell ring becomes a counting number.
- Sizes: the screen card draws at real pixel size, message text 15 px or more (13 px minimum in the 680x425 preview); Keep and Report always visible without scrolling at every size in STANDARDS.md (a bottom bar at 760 wide and below). At 375 wide the Address book folds into a button.
- `window.__tool = {state, sec, setMode, show(id), answer('keep'|'report', spots), round()}`.

## Look
Accent `--brand #b6f23a` (arcade lime) with `--brand-ink #142000`. Band 6-8, own `:root`, dark cabinet with a light screen.
- Cabinet: `--paper #12141c`, `--panel #1b1f2b`, `--ink #eef1f6`, `--muted #a5adbd`, `--line #2c3242`, `--btn #262c3b`, `--head-ink #eef1f6`, `--focus #ffd23f`.
- Screen: `#fbfbf8` with ink `#1c1f26`, muted `#555c6b`, link blue `#1a56c4`, status bar `#e9ebef`. Tell glow `#ffd23f` outline 3 px plus the tell's name in a tag. Keep button green `#7ee0a8` text on panel with a check icon; Report `#ff8f80` with a flag icon; Missed and False alarm tags `#b42318` on the screen with an icon.
- Contrast (computed): lime on cabinet 13.79:1; lime-ink on lime 12.74:1; ink on cabinet 16.23:1; muted on panel 7.29:1; screen ink 15.91:1; screen muted 6.47:1; link blue on screen 6.39:1; report coral on panel 7.43:1; keep green on panel 10.27:1; focus yellow on panel 11.38:1; red tag on screen 6.34:1. All pass AA.
- Neighbors: packet-race red on paper, network-architect blueprint, capture-the-flag pink. Arcade energy without confetti: a short pop on +2, nothing more.

## Art
none: drawn in code. Cabinet, email cards, phone outline, browser frames, the made-up logos and preview.svg are SVG and CSS. (Made-up logos are simple shapes: a pebble for Pebble Quest, a tower for Tune Tower, a leaf for Maple Grove, a box for Hilltop Parcel, a book for Riverbend, a wave for the Rec Center.)

## Voice
Bank voice `lively-host` (Sadachbia), "Say with lively energy, like a friendly game show host". Fits an arcade score chase. Not used by any 6-8 CS neighbor or group sibling (its other users are robot-dance, K, and beat-buddies, K music). Message texts are on screen only. `Curio.voice`, `scope: () => state.mode`.
- w-practice (how): "Read the message. Hover a link to see where it really goes. Then press Keep or Report."
- tell (how, first Report): "Now tap the part that gave it away. Then press Done."
- next (how, first Why card): "Press Next for another message."
- w-arcade (how): "Sixty seconds. Keep the real ones, report the fakes, and tap the tell for double points. Press Start round."
- go (event, each round start): "Go!"
- end (event, round end; stale when a new round starts): "Time! Check your score and the tells you caught."
- best (event, new best): "New best score!"
- w-tells (how): "These are the eight tells. Tap an example to try that message."

## Family engine
`kit/security.js`, described in full in tools/data-defenders/spec.md. This tool uses: **World** (the six made-up places above; `sec.safeDomain` must pass every address in the pools, including the fakes on `.test` and `.example`), **Artifacts** `email`, `sms` and `login`, **Spots** with the link status bar, and **Clock** (60 s rounds, 4 s tell ring). No Checks or Locks.

## Sources
- CSTA 2026 ids MS-SYS-SE-32, MS-SYS-SE-33 (`data/standards/csta-2026-ids.txt`); CSTA 2017 2-NI-05: https://csteachers.org/k12standards/
- Phishing signs (urgency, requests for passwords or codes, prizes, unexpected attachments, look-alike senders and links) and what to do: FTC Consumer Advice, "How To Recognize and Avoid Phishing Scams", https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams ; CISA, "Recognize and Report Phishing", https://www.cisa.gov/secure-our-world/recognize-and-report-phishing
- Check where a link really goes by hovering; go to sites by typing the address you know: CISA, "Avoiding Social Engineering and Phishing Attacks", https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks
- Real companies won't ask you to send a password or sign-in code by email or text: FTC Consumer Advice, "How To Recognize and Avoid Phishing Scams" (above), and CISA, "Recognize and Report Phishing" (above).
- Reserved example domains (.example, .test): RFC 2606 and RFC 6761, https://www.rfc-editor.org/rfc/rfc2606 ; 555-01xx numbers reserved for fiction: NANPA, https://nationalnanpa.com
- Every place, person and message is made up for Curio Class; no real site or brand appears.

## Done when
1. Every pool message renders with the Content fields; every address passes `sec.safeDomain`; no real brand or domain appears anywhere.
2. Hovering, focusing or long-pressing each link shows its real href in the status bar; links never navigate.
3. Arcade scoring matches the rules for all five outcomes (keep safe, report with tell, report without tell, keep phish, report safe), checked with `__tool.answer`.
4. A 60 s round shows no repeats; the round card totals match; Best saves and Clear best (after Yes) clears it.
5. Practice Why cards point to every listed tell (phish) or show the why line (safe).
6. Sign-in fields accept no typing.
7. Keyboard play (K, R, 1 to 8, Enter) works with visible focus; Keep and Report visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`.
8. Voice: welcomes once per mode, how lines once, Go and Time every round; Read speaks the hint; console clean; no network requests; the name only as "Curio Class".
