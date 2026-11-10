# Fact Rally

## One idea
On a sunny tennis court a friendly ball-machine bot named Volley serves addition and subtraction facts within 20 (7 + 8, 15 - 9), and the child hits each ball back by tapping the answer, with the ball's speed set by the child (slow, medium or quick, and slow is the default); when a strategy fits, its chip glows (near double for 7 + 8, make ten for 9 + 6, think addition for 15 - 9), and tapping the chip first flashes the quick picture (7 + 7 + 1) and turns the return into a power shot; rallies adapt with a scoreboard of all 100 one-digit sums, where facts the child misses come back in the next rally and facts they know rest, and each fact square turns from gray to green as it becomes quick; at the end the board is mostly green and the child sees that most facts got there through a strategy, so a second grader learns to add and subtract within 20 fluently using mental strategies and, by the end of grade 2, to know from memory all sums of two one-digit numbers.

## Not like
- make-ten-machine (1, spec): building each strategy slowly with counters. Here using strategies quickly.
- multiplication-dungeon (3, concept): times tables. Here sums and differences within 20.
- jump-line (2, spec): two- and three-digit strategies. Here one-digit facts.
- balance-the-beam (1, spec): the equal sign. Here speed with known facts.

## Who and how
- Grade 2, Math, module "Fluency Within 20". Standards: 2.OA.2 (fluently add and subtract within 20 using mental strategies; by end of grade 2, know from memory all sums of two one-digit numbers).
- Format: arcade. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Rallies of ten balls, four strategy chips (doubles, near doubles, make ten, think addition), the 100-square sum board, three ball speeds. Extra: Hot seat (two players take turns on one device). tool.json `modes: ["Court", "Hot seat"]`, `minutes: "5-15"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 2.OA.2 (strategies) | Tap a strategy chip before answering | the quick picture; the power shot | 2 |
| 2.OA.2 (fluency) | Return rallies of facts within 20 | the rally count; missed facts returning | 3 |
| 2.OA.2 (from memory) | Fill the sum board | gray squares turning green | 4 |

## Screens and modes
Header (kit): title "Fact Rally"; `Court`, `Hot seat`; `Read`, `Motion`, `Sound`, `Print`; a `Speed` switch (Slow, Medium, Quick; Slow first). Controls 56 px or more.

**On load and first tap.** A bright court from above, Volley the ball-machine bot across the net, a player's racket at the bottom, the sum board folded at the side. The welcome is queued (`welcomeAfter: true`): "Ready to rally? I serve a fact, you hit it back with the answer. Tap Serve." First hint: "Tap Serve."

**A rally (focus: the ball).** At 1366x768 the court fills the left with answer buttons along the bottom and the board at the right; at 680x425 the board is a tab and answers are one row. The ball carries a fact. Four answer buttons. A right tap returns it; a miss bounces softly and Volley shows the answer with its picture. No lives, no game over: a rally just counts.

**Strategy chips.** When a chip fits, it glows. Tapping it shows the picture (7 + 8 as 7 + 7 + 1) for a moment, then the answer buttons; a right answer after a chip is a power shot with a bigger swing.

**Adaptive repeats.** Missed facts get a small flag and return in the next rally (not right away); known facts rest for three rallies.

**The board (the aha).** A 10 by 10 grid of every sum from 0 + 0 to 9 + 9. Squares go from gray to light green (right once) to green (right and quick twice). Volley: "Look how many you got with a strategy! Now they're just known."

**The end.** The board and the best rally. `Print` prints the board.

**Hot seat (extra).** Two players take turns, each with their own board for the session only.

## Content
- Facts within 20 (sums of two one-digit numbers and their related subtractions), four chips, the 100-square board, all spoken. No timer bars, no lives; speed is the child's choice.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Pause` stops the ball at any time.
- Keyboard: Tab to Serve, chips and answers; number keys pick answers; Space pauses.
- With Motion off the ball appears at the racket and the swing is a still frame.

## Look
- Accent `--brand` #a3470c court clay orange (header, the net band, buttons); gold #f4c542 (a glowing chip, the power shot); paper #fdf4ee; ink #2a1205; muted #5f5048.
- Contrast (WCAG 2.1, computed): white on brand 6.06:1; brand on paper 5.59:1; ink on paper 16.30:1; muted on paper 7.09:1; ink on gold 10.88:1.
- Never color alone: board squares also show a dot (once) or a star (known).
- Different from this batch (closet blue, gym red, park green, vault indigo).

## Art
- Local FLUX (`scripts/localart.py`): the court from above (1, 16:9), Volley in three poses (serve, cheer, show) (3, 1:1).
- Drawn in code: the ball, racket, chips, pictures, the board.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as Volley; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.rally + ':' + state.fact + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `serve`: "Tap Serve."
- how `hit`: "Tap the answer."
- how `chip`: "Tap the glowing chip for a power shot."
- event, whole, each fact read aloud (short, cut off by the answer).
- event, whole, the board.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the rally, chips with pictures, the spaced-repeat queue (missed facts return next rally, known facts rest three), the board. Facts sit in a marked block `/* FACT-RALLY DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Answer | Tap at random | Misses return next rally; squares stay gray. |
| Chips | Tap every chip | Only fitting chips glow; others are disabled and not named. |
| Board | Answer only easy facts | The rally serves gray squares first. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `serve`.
2. `hit`; facts as served.
3. `chip`.
4. Board (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 2.OA.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Fluency grows best from strategies, not drill alone | Baroody (2006), "Why children have difficulties mastering the basic number combinations", Teaching Children Mathematics | National Research Council (2001), "Adding It Up" | yes |
| Spacing repeats over time helps facts stick | Cepeda and others (2006), "Distributed practice in verbal recall tasks", Psychological Bulletin | Rohrer and Taylor (2007), "The shuffling of mathematics problems improves learning", Instructional Science | yes |
| Timed pressure can raise math anxiety, so speed is the child's choice | Boaler (2014), "Research suggests that timed tests cause math anxiety", Teaching Children Mathematics | Ramirez and others (2013), "Math anxiety, working memory, and math achievement in early elementary school", Journal of Cognition and Development | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-10): 7 + 8 = 7 + 7 + 1 = 15; 15 - 9 = 6; the board has 100 sums, the largest 18; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 court, answers and board; at 680x425 board tab.
2. Strategy chips glow only when they fit and show their pictures. (2.OA.2)
3. Rallies serve facts within 20 and return missed facts next rally. (2.OA.2)
4. The 100-square board fills from gray to green. (2.OA.2)
5. Every card is spoken; every control is 56 px or more.
6. Slow is the default; no lives or game over.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still ball and swing; no network requests.

## Open questions
- The idea card flags overlap with make-ten-machine and multiplication-dungeon (default used: this tool uses strategies fast on a tennis court with a rally-spaced repeat; make-ten-machine builds them slowly; multiplication-dungeon gets a different repeat mechanic and look).
