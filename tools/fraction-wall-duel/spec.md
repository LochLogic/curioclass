# Fraction Wall Duel

## One idea
A card game played against Rosa (a made-up rival, labeled "illustration") on a shared fraction wall: Rosa plays 3/4 face up and the child plays a card from a hand of five, both fractions light up as bars on the wall, and the bigger fraction wins the round, but only if the child names a reason the wall can show: rename to the same pieces (3/4 is 9/12, 5/6 is 10/12), the same number of pieces (3/5 against 3/8, and fifths are bigger), or the half line (5/8 is past 1/2, 3/7 is not); playing an equal fraction steals the round, but only after the child splits each third into two sixths on the wall to prove 2/3 is 4/6; later decks add tenths and hundredths, and trap cards that compare half of a big pizza with half of a small one, which the rule book voids because the wholes differ; at the end the child's winning reasons are listed, and the child sees that a fraction's size depends on both numbers and that one amount wears many names, so a fourth grader learns to explain and make equivalent fractions by splitting pieces, and to compare two fractions with different numerators and denominators by common pieces, common counts or the half benchmark, for the same whole.

## Not like
- fraction-trail (3, spec): fractions as places on a line. Here a wall and reasons.
- how-many-fit (6, concept): dividing fractions, same wall engine. Here equivalence and comparing.
- fraction-kitchen (5, concept): adding unlike fractions with cups. Here comparing them.
- money-and-meters (4, spec): tenths and hundredths in four views. Here a card duel.

## Who and how
- Grade 4, Math, module "Equivalent Fractions and Comparing". Standards: 4.NF.1 (explain why a fraction a/b is equivalent to a fraction (n x a)/(n x b) by using visual fraction models, with attention to how the number and size of the parts differ even though the two fractions themselves are the same size; use this principle to recognize and generate equivalent fractions), 4.NF.2 (compare two fractions with different numerators and different denominators, e.g., by creating common denominators or numerators, or by comparing to a benchmark fraction such as 1/2; recognize that comparisons are valid only when the two fractions refer to the same whole; record the results with symbols >, =, or <, and justify the conclusions, e.g., by using a visual fraction model).
- Format: cards. Driver: one student alone against the computer rival (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- A wall from halves to twelfths plus tenths and hundredths, one worked round by Rosa, three decks (twelve rounds each: seven compare rounds, two blank-card rounds, one forced steal, and two rounds that are a trap or a Rosa claim), three reasons the child carries out, the split tool, trap cards, the rule book. Extra: Two players (two students on one screen, hands hidden by a pass-the-device screen). tool.json `modes: ["Duel Rosa", "Two players"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.
- Change note (spec fix, 2026-11-10): the duel, Rosa and the wall stay. What changed is who does the work. Before, the child tapped one of three reason buttons and the wall did the renaming, and the split happened only if the child chose an equal card. Now every deck has blank-card rounds where the child splits the wall, writes the equal fraction and finishes the why sentence; every win needs the sign dragged in, the reason carried out by the child, and a one-line reason in the child's own words checked against a shown guide; a wrong sign or reason gives the round to Rosa; trap cards need the child to say why the wholes differ. The steal is no longer the only place 4.NF.1 is done.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NF.1 | explain why a/b = (n x a)/(n x b) with a model, noting number and size of parts; recognize and generate equivalent fractions (all parts here) | the student | Blank-card rounds: pick n, split each piece, write the new fraction, finish the why sentence; steals: spot the equal card and prove it; the rule card: fill in what is multiplied | 6 blank cards (n = 2, 3, 5 and 10 on halves, thirds, fourths, fifths and tenths) and 3 steals | pieces splitting, more and smaller pieces, the same length of bar | 2, 3 |
| 4.NF.2 (compare, record, justify) | compare two fractions with different numerators and denominators by common denominators, common numerators or a benchmark; record with >, = or <; justify (all parts here) | the student | Drag the sign between the cards, pick a reason and carry it out (type both renamed fractions, tap the bigger piece, or drag each bar's marker to its side of 1/2), then write one line of your own and check it against the guide | 21 compare rounds, at least 6 by each reason | bars, the sign between the cards, the child's own renaming | 4, 5 |
| 4.NF.2 (same whole) | recognize that comparisons are valid only for the same whole | the student | On a trap or a Rosa claim, lay one whole over the other and finish "They cannot be compared because ..." | 4 trap cards and 2 Rosa claims | two wholes of different size; the rule book's same-whole page | 6 |

## Screens and modes
Header (kit): title "Fraction Wall Duel"; `Duel Rosa`, `Two players`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A fraction wall on a game table, a hand of five cards and Rosa grinning across the table with 3/4 face up. The welcome is queued (`welcomeAfter: true`): "Rosa played 3/4. Beat it, or match it to steal! Drag a card onto the table." First hint: "Drag a card onto the table."

**Rosa shows one (the model, round 0).** Before the first deal Rosa plays 2/3 against a face-up 1/2 and thinks aloud, with every step shown on the wall: she splits thirds into sixths and halves into sixths, writes 4/6 and 3/6, drags the > sign between the cards so the table reads 2/3 > 1/2, and writes "Both are sixths now, and 4 sixths is more than 3 sixths." The round cannot be skipped and does not score. A `Rosa's example` button brings it back at any time.

**A compare round (focus: the wall).** At 1366x768 the wall fills the middle with hands below and above; at 680x425 the wall scrolls sideways and the hand is a tray. The child plays a card and the two bars appear as outlines with no fill, so their lengths are not on show yet. The round then has four steps, and none can be skipped:
1. Sign. The child drags `>`, `=` or `<` between the two cards. The table shows the record, for example 5/6 > 3/4.
2. Reason. The child picks `Same pieces`, `Same count` or `Half line`. A reason that does not fit the pair (Same count for 5/6 and 3/4) is turned away with the wall showing why, and it counts as the round's one miss.
3. Carry it out. Same pieces: the child picks the row to rename into and types both new fractions (9/12 and 10/12); the wall splits only after the typing. Same count: the child taps which pieces are bigger (fifths or eighths) on two single pieces. Half line: the child drags each fraction's marker to the left or right of 1/2.
4. Say it. A one-line box, "My reason:", with Rosa's model line in view. The child types or says a line, then ticks a three-box guide: names both fractions; names the same pieces, the same count or the half; says which is more. The tool cannot mark the words, so the guide and the model do that job, and the line is kept for the final list.
After step 4 the bars fill and the sign is judged against exact values. One miss in a round (a wrong sign, an unfit reason or a wrong renaming) can be fixed. A second miss gives the round to Rosa, who shows her own renaming, and the pair comes back later in the deck with new numbers. Rounds where the child's card is smaller are still played: the child records `<`, gives the reason and Rosa takes the trick.

**Blank-card rounds (two in every deck).** Rosa plays a fraction and the child's hand is five blank cards: "Make a card equal to mine." The child picks how many pieces to cut each piece into (2, 3, 4, 5 or 10) and taps `Split`, then types the numerator and denominator on the blank card. Then the why sentence, with typed blanks: "I cut each piece into __ . There are __ times as many pieces, and each piece is __ (bigger or smaller). The bar is the same length, so 2/3 = __/__ ." The six rounds are 1/2 by 2, 2/3 by 2, 3/4 by 3, 2/5 by 2, 1/2 by 5 and 3/10 by 10. A wrong card shows bars that do not line up and the child tries once more; a second miss gives Rosa the round and the same fraction returns with a different n.

**Steals.** Each deck deals one hand that holds an equal card (4/6 on Rosa's 2/3, 6/8 on 3/4, 50/100 on 5/10). The child must spot it, play it, record `=`, and prove it with the split tool and the why sentence. Playing a bigger card instead is allowed but Rosa says "You had my twin in your hand," and the steal is dealt again next hand until it is taken.

**The rule card (after the third blank card).** A card reads "To make an equal fraction, multiply the __ and the __ by the __ number." The child fills the three blanks from a word bank of six (top, bottom, same, different, biggest, smallest) and then writes it with letters by dragging n, a and b into (__ x __)/(__ x __). The filled card sits beside the wall for the rest of the game.

**Later decks.** Deck 2 adds tenths and hundredths (3/10 against 25/100). Decks 2 and 3 add trap cards: "half of the big pizza" against "half of the small pizza". No sign fits. The child opens the rule book, drags one whole on top of the other to see they do not match, and finishes the sentence "They cannot be compared because the wholes are __ ." by typing or picking `different sizes` from four choices, then voids the round. Playing a sign on a trap gives Rosa the round and the trap returns.

**Rosa's turn.** Twice Rosa claims a win with a bad reason ("My 1/2 of the big pizza beats your 3/4 of the small one"). The child must tap `Challenge`, lay the wholes over each other and finish the same sentence. Letting the claim pass gives her the round and the claim comes back.

**Final score (the aha).** The list of rounds with each recorded comparison and the child's own reason line. Rosa: "You didn't just win. You proved it every time. Same amount, many names."

**The end.** The reason list. `Print` prints it and a paper fraction wall.

**Two players (extra).** Hands hidden by a pass-the-device screen.

## Content
- Three decks of 24 cards, denominators 2, 3, 4, 5, 6, 8, 10, 12 and 100, four trap cards, two Rosa claims, six blank-card rounds, three steal hands, the rule card and the rule book, all readable with `Read`.
- Compare rounds per deck: seven, set so that across the game at least six are won only by Same pieces (5/6 and 3/4; 2/3 and 3/5; 7/10 and 65/100), six by Same count (3/5 and 3/8; 2/3 and 2/5; 5/6 and 5/12) and six by Half line (5/8 and 3/7; 7/12 and 4/10; 6/10 and 45/100). The hand is dealt so that every card in it differs from Rosa's in both numerator and denominator unless it is a same-count round.
- Model lines for the guide, one per reason: "Both are twelfths now, and 10 twelfths is more than 9 twelfths." "Both have 3 pieces, and fifths are bigger than eighths." "5/8 is more than half and 3/7 is less than half."
- Rosa is a friendly rival; losing a round just deals again, and a lost pair always returns with new numbers.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be put back until a reason is picked.
- Keyboard: Tab to cards, the reason buttons, the split tool, the rule book and challenge; Enter plays.
- With Motion off bars split and line up at once.

## Look
- Accent `--brand` #9a3d12 brick orange (header, the wall frame, card backs); gold #f4c542 (the card in hand, a winning bar); paper #fbf1ec; ink #2b1005; muted #5e5049.
- Contrast (WCAG 2.1, computed): white on brand 6.88:1; brand on paper 6.19:1; ink on paper 16.03:1; muted on paper 6.95:1; ink on gold 10.95:1.
- Never color alone: bars carry fraction labels; the child's and Rosa's bars carry names.
- Different from this batch (craft-fair plum, quilt navy, track teal, workbench olive).

## Art
- People (illustrated): Rosa, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the game table (1, 16:9), card back art (1, 3:4).
- Drawn in code: the wall, bars, split lines, cards, the half line.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Rosa; `knowing-guide` as the referee and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.deck + ':' + state.round + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `play`: "Drag a card onto the table."
- how `sign`: "Drag a sign between the two cards."
- how `reason`: "Pick a reason, then show it on the wall."
- how `sayit`: "Write your reason in the box, then check the guide."
- how `blank`: "Pick how many pieces to cut, then tap Split."
- how `split`: "Type your equal fraction on the blank card."
- event, whole, Rosa's worked round.
- how `trap`: "Open the rule book."
- event, whole, final score.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fraction-wall (family "fraction-wall"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* FRACTION-WALL ENGINE: begin */ ... /* end */`: a wall of rows from 1 down to twelfths plus tenths and hundredths, bars for any a/b, row splitting by n with matching checks, the half line, and exact comparison with `Frac`; how-many-fit reuses them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sign | Read the longer bar; guess one of three | Bars are outlines with no length until step 4 is done. A guess is right one time in three and the second miss gives Rosa the round. |
| Reason | Tap reasons until one works | An unfit reason is the round's miss; the fit reason must then be carried out by typing or dragging, which a tap cannot do. |
| Carry it out | Wait for the wall to rename | The wall splits only after both renamed fractions are typed. Same count asks about piece size, not the answer. |
| Say it | Tick the boxes on an empty line | The box must hold a line before the ticks open; the model line is beside it, and the line is printed in the final list for the teacher. |
| Blank card | Type numbers until the bars line up | Two tries, then Rosa takes it and a new n comes; the why sentence has typed blanks tied to the chosen n. |
| Steals | Never play an equal card | The steal hand is dealt again until it is taken. |
| Traps and claims | Play them as normal cards; let claims pass | Either gives Rosa the round and the card returns; the sentence must be finished to void. |
| Rule card | Try word-bank words in turn | Six words for three blanks, and the letter form must match (n x a)/(n x b). |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued), then Rosa's worked round (whole). `play`; `sign`; `reason`; `sayit`.
2. `blank`; `split`.
3. `trap`.
4. Final score (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.NF.1, 4.NF.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Comparing by common denominators, common numerators or benchmarks like 1/2 | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
| Equivalent fractions shown by splitting each part into n parts | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Van de Walle, Karp and Bay-Williams (2019), "Elementary and Middle School Mathematics: Teaching Developmentally", 10th edition | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s13, 2026-11-10): 3/4 = 9/12 and 5/6 = 10/12, so 5/6 > 3/4; 3/5 > 3/8; 3/7 < 1/2 < 5/8; 2/3 = 4/6; contrast as in Look.
Checks run again for the spec fix (Python `fractions`, scratchpad s/fx, 2026-11-10): the six blank cards give 2/4, 4/6, 9/12, 4/10, 5/10 and 30/100, each equal to its start; steals 4/6 = 2/3, 6/8 = 3/4, 50/100 = 5/10; every listed compare pair has the stated winner (5/6 > 3/4, 2/3 > 3/5, 7/10 > 65/100, 3/5 > 3/8, 2/3 > 2/5, 5/6 > 5/12, 5/8 > 3/7, 7/12 > 4/10, 6/10 > 45/100) and each half-line pair sits on opposite sides of 1/2; rounds per deck 7 + 2 + 1 + 2 = 12, so 36 in all with 21 compare rounds.

## Done when
1. Focus and fold: at 1366x768 wall and hands; at 680x425 wall scrolls, hand as a tray.
2. Six blank-card rounds are done: the child picks n, splits, writes the equal fraction and finishes the why sentence. (4.NF.1)
3. Three steals are spotted and proved, and the rule card is filled in words and in letters. (4.NF.1)
4. Every compare round has a sign dragged in before the bars fill, and a reason the child carries out. (4.NF.2)
5. Every compare round ends with the child's own reason line checked against the three-box guide; a second miss gives Rosa the round. (4.NF.2)
6. Four traps and two Rosa claims are voided with the same-whole sentence finished. (4.NF.2)
7. Rosa's worked round plays first and can be reopened.
8. `Read` reads every card; every control is 48 px or more.
9. Rosa is labeled illustration.
10. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
11. Motion off: bars split at once; no network requests.

## Open questions
None.
