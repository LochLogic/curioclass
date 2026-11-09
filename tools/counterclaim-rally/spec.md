# Counterclaim Rally

## One idea
The student volleys an argument across a table tennis table with Reza, a scripted eighth grader, and every return must answer the point Reza just played (concede and turn it, show it is outweighed, or show it is false, with a card from the evidence deck); a return that repeats the claim or answers a different point goes into the net, with a replay of what Reza actually said, and the rally sheet then becomes an essay that names the other side fairly and answers it, so they learn that a strong argument meets the opposing claim instead of talking past it.

## Not like
- debate-prep-desk (6, spec): building both sides from sources with a coach. Here live back-and-forth answering, then an essay, grade 7.
- claim-quote-comment (6-8, spec): one evidence paragraph. Here a full argument with a counterclaim.
- argument-x-ray (6, spec): tracing an author's argument. Here making your own against an opponent.
- claim-vs-claim (8, concept): distinguishing claims in formal style. Here answering the point just played.
- podcast-listening-club (6-8, spec): judging speakers. Here returning their points.

## Who and how
- Grade 7, ELA, module "Argument with Counterclaims" (Writing). Standard: W.7.1 (a, b, c, d, e).
- Driver: one student; pairs can play live in class mode with the same cards (tool.json `driver: "student"`). Every return is read aloud.
- Topics: "Should our school replace paper textbooks with tablets?" (based on real studies) and two practice topics labeled made up ("Should our town build a skate park or a library annex?", "Should class pets be allowed?"). tool.json `modes: ["Rally", "Pair rally"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.
- Nothing is saved; `Print` prints the rally sheet and the essay.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.7.1a (acknowledge alternate claims) | Return each of Reza's points with a move that answers it | the rally and the net replay on misses | 2 |
| W.7.1b (relevant evidence, credible sources) | Back each return with a card from the deck | the card on the return | 3 |
| W.7.1a (organize reasons logically) | Order the reasons in the essay outline | the outline with reasons in order | 4 |
| W.7.1c (transitions) | Join reasons and the counterclaim with transitions that show how they relate | the transition chips | 4 |
| W.7.1d (formal style) | Turn rally lines into formal sentences; casual phrases are flagged | the flagged phrases | 5 |
| W.7.1e (conclusion) | Write a conclusion that follows from the argument | the conclusion card | 5 |

## Screens and modes
Header (kit): title "Counterclaim Rally"; `Rally`, `Rally sheet`, `Essay`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A rec center table tennis table, a scoreboard, Reza (an eighth grader with a paddle) on the far side and Ref Kim (an umpire on a tall chair) at the net. A topic card sits on the table. First hint: "Tap the topic card to hear it." The first tap reads the topic; the welcome is queued after it (`welcomeAfter: true`).

**Serve.** The student picks a side and writes a one-sentence claim (the evidence engine's `ev.claimCheck` needs one that can be argued).

**Rally.** Reza returns an opposing point (keyed, one of six per side). The student plays a return:
- choose a move: concede and turn ("It's true that..., but..."), outweighed ("Even so, ... matters more because..."), or false ("That isn't what the evidence shows: ...");
- pick a card from the deck that answers that point;
- write or finish the return line.
A return is in when the move is keyed to fit that point and the card is keyed to it. A return that repeats the claim, answers a different point, or uses a card that doesn't bear on it goes into the net: the ball drops, Ref Kim calls "Net", and Reza's point replays. The rally is up to five exchanges; later ones are Reza's strongest points.

**Rally sheet.** Each exchange as a row: Reza's point, the student's move, card and line. The student stars the strongest opposing point to acknowledge in the essay.

**Essay.** Built with the engine's Draft: claim; two or three reasons in an order the student sets, each with a card; the starred counterclaim stated fairly and answered; transitions from chips (however, for example, as a result, even though); a conclusion. `ev.draftChecks` flags an essay that skips the counterclaim or only mentions it without an answer, and a formal-style list flags casual phrases ("kinda", "like", "super", "you guys").

**Pair rally.** Two students on one device; each plays a side and Ref Kim calls nets by the same keys.

At 1366x768 the table and deck fit; at 680x425 the deck is a drawer.

## Content
- Tablets topic cards (summaries written for Curio Class): a 2018 meta-analysis of 54 studies (Delgado and others, Educational Research Review) found readers understood informational texts better on paper than on screens, especially with time limits; a 2019 meta-analysis (Clinton, Journal of Research in Reading) found a similar small advantage for paper; practice cards labeled made up about cost, weight of backpacks and updated content.
- Reza's six points per side, keyed fitting moves and cards.
- Two practice topics labeled made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A return in the net can be replayed right away.
- With Motion off the ball jumps across; no spin.

## Look
- Accent `--brand` #b3400a rally orange (header, paddles, net tape); gold #f4c542 (the ball, starred points); paper #fcf4ef; ink #2e1003; muted #6a5246. Scene: a rec center gym.
- Contrast (WCAG 2.1, computed): white on brand 5.75:1; brand on paper 5.29:1; ink on paper 16.22:1; muted on paper 6.65:1; ink on gold 10.84:1.
- Never color alone: Ref Kim calls "In" or "Net" in words; moves have labels.
- Different from this batch (ivy green, cart amber, coaster magenta, roots blue).

## Art
- People art goes to Gemini: Reza (an Iranian American boy about 13 with a paddle), 4 poses; Ref Kim (a Korean American woman in her fifties in an umpire's polo on a tall chair), 3 poses; "illustrated <description> <pose>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): rec center with a table tennis table (1).
About 8 images. Drawn in code: table, ball, scoreboard, rally sheet.

## Voice
Reza is `casual-peer` and Ref Kim is `firm-captain` (also the hint voice); each is unique in this batch. `Curio.voice` with `scope: () => state.topic + ':' + state.view + ':' + state.exchange`, `welcomeAfter: true`.
- how `welcome`: Ref Kim: "Serve your claim. Every return has to answer the point just played, or it's in the net."
- event `point`: Reza's point.
- event `in`: "In!"
- event `net`: "Net. Here's what Reza said." then the replay.
- event `skipped`: "Your essay mentions the other side but doesn't answer it."
- event `casual`: "{Kinda} is casual. Try a formal word."
- event, whole, `essay`: the essay.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (the card deck), Claims with `ev.claimCheck`, Evidence links with `side` and rebuttal links (the returns), and Draft with `ev.draftChecks`. Not Spans, Series, Ledger view or Board view. The rally and keyed moves are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Returns | Always concede and turn | Each point has keyed fitting moves; a concede on a false point goes in the net. |
| Cards | Use the strongest card every time | A card must be keyed to that point. |
| Essay | Mention the counterclaim in one sentence | `ev.draftChecks` needs the answer sentence linked to it. |
| Formal style | Avoid flagged words only | The list catches common casual phrases; the teacher sees the essay printed. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the topic card: topic, `welcome` (queued, first time).
2. Rally: `point` (waits), then `in` or `net` per return.
3. Essay: `skipped` and `casual` as they fire; `essay` (whole) on Play.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.7.1 (a to e) wording | thecorestandards.org, Writing Grade 7 | CCSS ELA 2010 PDF | yes |
| Readers understood informational texts better on paper than on screens, especially under time limits (meta-analysis of 54 studies) | Delgado, Vargas, Ackerman and Salmerón (2018), Educational Research Review 25 | Clinton (2019), Journal of Research in Reading 42(2), a separate meta-analysis with a similar finding | yes |
| A strong argument acknowledges counterclaims and answers them | Purdue OWL, counterarguments | ReadWriteThink, argument writing | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): cost and backpack cards and two topics are practice, labeled made up on screen.

Checks run (Python, scratchpad b20, 2026-11-09): every one of Reza's points has at least one keyed fitting move and one keyed card; no single move fits all six points on a side; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and deck fit; at 680x425 the deck is a drawer.
2. Returns go in only with a fitting move and card; nets replay Reza's point. (W.7.1a)
3. Each return carries a card. (W.7.1b)
4. The essay outline orders reasons and uses transitions. (W.7.1a, W.7.1c)
5. Formal-style flags and a conclusion work. (W.7.1d, W.7.1e)
6. `ev.draftChecks` flags a missing or unanswered counterclaim.
7. Pair rally works on one device.
8. Print shows the rally sheet and essay.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the ball jumps; no network requests.

## Open questions
- None for Cory.
