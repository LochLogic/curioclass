# Codex review: usage-panel

## Played

Played cold as a Grade 11 student before reading codex-report, handoff, notes or src; then checked the projected teaching path.
All five cases, 16 sentences, five voices, voting, evidence, Record, Ruling and the earned usage note. Strong editorial atmosphere; the dated reversals are the best moment.

## Findings fixed

- Should fix, general, Hearing/private marks: Jordan's note suggested a hidden sentence vote. It now names Next sentence and another panelist.
- Should fix, general, evidence/Read: twelve cards were spoken, including off-screen material. Read now selects one visible card; opening/closing updates the hint, and Close stops reading.
- Should fix, general, Record/percentages: carried-forward statistics looked like a new survey at the slider year. Every percentage now carries its actual survey year.
- Should fix, general, Your panel: end-of-record narration could continue after its suggested action. Adding/selecting the personal marker hushes it. A direct marker tap during playback also refreshes the hint instead of falsely saying the record is still playing.
- Should fix, general, Record/private marker: the four choices were only in hover text and the selected card. The marker now shows Text, News, Essay and Speech choices; compact layouts retain every marker target above 44 px.
- Should fix, general, Year keyboard: unique-year jumps skipped AP/Chicago in 2017 and APA/Merriam-Webster in 2019. Page Up/Down now visits each marker in both directions, including the personal marker.
- Should fix, general, paper contrast: secondary ink fell to 4.31-4.43:1 on the darkest paper. Metadata, placeholder and status now measure at least 5.63:1.
- Should fix, general, overlay voice/access: Evidence as first tap could welcome the chair while covering its named panelists. Open overlays suppress welcomes; confirmations hush speech and expose their question through aria-describedby.
- Polish, general, Ruling: flat note updates and an undifferentiated personal card. Added a brief ink-settle response, quiet diamond seal and separate lines for the student's settings. Motion off removes the response.
- Polish, general, art: green key fringes on five cutouts; cleaned through art.py --rekey. Redrew the weakest paper stack with clearer layers, turned corner and clip detail, retaining the painterly set.
- Polish, general, storage: a successful retry now restores the saved status after an earlier error.

## Findings left

No confirmed blocker or should-fix finding remains. Clear-ruling focus concern rejected by real input: focus remained on Clear; no unnecessary change made.

## Break it

- Votes: tried every option, rapid changes, all 16 sentences and a hidden Jordan vote. Comparisons are fixed to exact sentences/years; hidden personal voting is refused. No correctness, points or achievement is awarded.
- Persuasive/Not for me: marked without reading and changed opinions. These affect only private marks/reasons; they award nothing. Jordan's hint stays respectful and actionable.
- Ruling/ruled status: selected easy rows, every option and all reasons. This is a private contextual judgment, not mastery. The documented ruled status means at least one chosen setting.
- Notes: recomputed 40,960 setting/reason combinations; no null/undefined prose and empty grids stay empty. Confirm/cancel, copying and edited-note reload were exercised.
- Timeline/percent bars: swept endpoints and recent dates, used arrows and marker-jump keys, dragged with whole-pixel jitter, and interrupted playback. No earned score exists to cheat; 2016 Chicago is unknown, 2017 against, 2024 accepts.
- Playback: two normal sweeps reached 2026 at 26.00/26.08 s with normal frame jitter; record-end spoke twice. Calm took 26.01 s, stepped through marker years, and left zero infinite animations. Real dragging stopped the sweep immediately and the year stayed fixed.
- No quiz, reflection gate, best score or success meter exists; none was added.

## Voice walk

Final main path, Sound/Motion on, default fresh work, real 120 ms held clicks at two-second pace: sentence, Copy Editor, Linguist, Persuasive, vote, Record, Play, wait for 2026, Your ruling, Ruling, all four settings, Copy note.
Heard in order: welcome, Copy Editor, Linguist, Record how-to, record-end, Ruling how-to, note-ready. Each mode's instruction started once, with no stale queue. The completed note copied successfully. Log/frame: voice-path-final.json/png in Scratch.
The welcome was cut by the next tap; its queued case question was dropped unmarked. The vote instruction became stale after voting. BASELINE 16 permits first-tap cuts; the chair premise and voting action remain in the hint/Read. A separate unvoted five-repeat run heard the vote instruction once.
Side path: Hopefully, Reporter, Read, Record, Ruling, Less, Sound off, Read, Sound on. Read interrupted correctly and worked with Sound off. First-tap Evidence now has an empty voice queue; opening confirmation cuts its earlier instruction.
All 37 fixed lines match allLines and voice/lines.json. Browser fallback only; firm-captain recordings remain a separate production step, as the build rules prohibit recording here.

| Line / run | Kind | Expected / spoken |
|---|---|---|
| Hearing, Record, Ruling instruction, final path | how / welcome | 1 / 1 each |
| Note-ready, final path | how | 1 / 1 |
| Requested Poet argument, five repeats | event | 5 / 5 |
| Vote instruction after those repeats | how | 1 / 1 |
| Record-end, two validation sweeps | event | 2 / 2 |

## Facts checked

Checked live against these named sources; scripted panelist opinions are labeled arguments, not authority quotations.

- They: use since about 1300; 2008 acceptance 56/59%; 1996 rejection 80%; 2015 rejection 48/58%. [AHD, they](https://ahdictionary.com/word/search.html?q=they). Recomputed complements: 20/52/42%.
- They: early-1590s Shakespeare quote, Act 4 Scene 3, checked in [The Comedy of Errors](https://www.gutenberg.org/cache/epub/1504/pg1504-images.html).
- They: Austen quote and 1813 publication, checked in [Pride and Prejudice](https://www.gutenberg.org/cache/epub/1342/pg1342-images.html).
- They: AP limited generic use and Chicago formal-writing caution, both 2017, plus personal-pronoun distinction. [CJR, Merrill Perlman, March 27, 2017](https://www.cjr.org/language_corner/stylebooks-single-they-ap-chicago-gender-neutral.php).
- They: APA generic and personal singular they, seventh edition/2019. [APA's guidance](https://apastyle.apa.org/style-grammar-guidelines/grammar/singular-they).
- They: Chicago's 2024 formal generic acceptance. [Publisher's announcement](https://cmosshoptalk.com/2024/04/16/announcing-the-chicago-manual-of-style-18th-edition/) and [edition changes](https://www.chicagomanualofstyle.org/help-tools/what-s-new.html).
- They: Merriam-Webster nonbinary sense in September 2019 and Word of the Year in December. [Associated Press, via WHYY](https://whyy.org/articles/merriam-webster-declares-they-its-2019-word-of-the-year/).
- They: 1993 Chicago account names reviser Russell Harper's [Five Changes That Matter](https://www.writersdigest.com/write-better-fiction/5-changes-that-matter-from-the-chicago-manual-of-style-18th-edition); full page returned 429. Attribution retained; independent full-text verification remains open.
- Literally: Dickens 1838-1839 phrase, [Nicholas Nickleby](https://www.gutenberg.org/cache/epub/967/pg967-images.html); Twain 1876 phrase, [Tom Sawyer, chapter 2](https://www.gutenberg.org/cache/epub/74/pg74-images.html); Fitzgerald 1925 phrase, [Gatsby, chapter 5](https://www.gutenberg.org/cache/epub/64317/pg64317-images.html). All checked in the works.
- Literally: hyperbolic sense exists and requires care; 2026 is a current-entry marker, not its addition date. [Merriam-Webster's own explanation](https://www.merriam-webster.com/grammar/misuse-of-literally).
- Hopefully: sentence-adverb use in 1648 and AP acceptance April 2012. [Merriam-Webster](https://www.merriam-webster.com/grammar/yes-you-can-use-hopefully-to-mean-i-hope).
- Hopefully: older manner sense, objections in the 1960s; 34% in 1999, 63% and comparison 89% in 2012. [AHD, hopefully](https://ahdictionary.com/word/search.html?q=hopefully).
- Split: Layamon early 1200s, Wycliffe 1300s, proposal 1834, Alford 1864, Fowler 1926, MWDEU 1994, Economist 2012/2018. Checked against [the specified cited-work account](https://en.wikipedia.org/wiki/Split_infinitive): Layamon; Hall 1882; New-England Magazine 7(6), pp.467-470; Alford; Fowler p.559; MWDEU pp.867-868; Economist editions 10 and 12. Original editions not all independently inspected.
- Less: Alfred 888 partitive, Baker's personal preference 1770, MWDEU 1995 and Cambridge Guide 2004. [Specified cited-work account](https://en.wikipedia.org/wiki/Fewer_versus_less): OED; Baker p.55; MWDEU p.592; Cambridge p.205. Secondary verification only for these historical editions.
- Less: count/amount distinction and distance, time, money and sign exceptions corroborated by [Merriam-Webster's current usage guidance](https://www.merriam-webster.com/grammar/fewer-vs-less).
- Approximate dates retain their labels; no-ruling means no ruling in this dataset. Nominal playback totals recomputed: 26, 14, 15.5, 20, 14 seconds. Original sentences are specification writing, not attributed quotations.

## Sensitivity

Personal pronouns/nonbinary identity: a cultural reviewer should check the respectful separation of a person's pronouns from contested generic use, and the risk of treating prescriptive school conventions as judgments about a home dialect or intelligence. Jordan never has an acceptability vote. Notes explicitly protect that distinction. A cultural reviewer should also judge whether the private Not for me mark on that example could be mistaken for judging a person; it is a case-wide argument note. No people appear in the art.

## Flattest moment left

The specified 1.5-second pauses are too short to read longer evidence cards fully. Stop and manual markers allow inspection; changing the prescribed pacing would need a spec decision. The personal-ruling payoff and note response were lifted without adding scoring.

## Graphics

Viewed all six finished images and rendered scenes. One style, directional lamp light, walnut/brass/paper layers, no text artifacts, no people, all people flags false. Paper emblem redrawn with built-in imagegen: art/raw/papers.png and art/papers.webp; full prompt set in art/prompts.json.
Compared existing Beat Lab and Snowy Mail Route bundles without writing into their folders. Kept the richer hearing materials and sober older-student instrument layout. Art 213.7 KB; final bundle 404.9 KB. Side-by-side frame: ../../_scratch/usage-panel/review-comparison.jpg.

## Audit

The one full audit finished within its 40-minute limit, at about 39 minutes: ../../_scratch/usage-panel/review-audit/audit.md. All 70 audit frames were opened and inspected; full sizes, all states in its frozen input list, Motion off, repeated controls, quick taps and resize stress completed.
Its 18 leads were 3 intentionally hidden phone button words (visible icons retain accessible names), 2 compact note-editor fold flags (all setting/reason choices remain visible; the specified editor is below and the hint says Scroll), and 13 skipped first-tap welcomes where the control spoke its own fitting line. BASELINE 16 allows those skips; the premise stays reachable in Hearing hint/Read.
The click log also exposed the Evidence welcome mismatch, which the audit treated as welcome heard. Fixed it, the contrast, visible personal label, duplicate-year keys and interrupted-marker hint; re-shot only affected frames at 680, 1366 and/or the real 375 iframe. Targeted checks and the final full voice path passed without runtime warnings/errors. No second audit or polish round.
Final contrast checks: brand/panel 6.35:1; brand/section 6.01:1; brand-ink/brand 6.77:1; ink/panel 14.70:1; muted/section 7.71:1; plate 5.20:1. Grayscale and keyboard-only frames were inspected. Owned Chrome ports 9961-9963 and host 8765 closed; temporary tool host.html removed.

## Left open

Full-text Chicago 1993 verification and the named historical original editions remain provenance limits; no invented replacement facts or new markers were added. The specified 1834 event is one proposal, not a claim that no earlier objection existed.
SL.11-12.1 needs the specified paired discussion; solo use prepares a judgment but cannot itself be collaborative discussion. Notes already state this accurately.
Unattended choices followed the spec: retained the note-only Jordan example, contextual private opinions, no recordings and the original playback schedule. No questions, commits, shared-kit edits or new topics.
