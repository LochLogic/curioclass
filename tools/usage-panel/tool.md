# Usage Panel: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: usage-panel

#### Built
Built all five cases and Hearing, Record and Ruling from the kit starter. Six original paintings frame a working editorial hearing; a single embedded CASES array holds 16 sentences, 25 scripted arguments and 33 dated events.
The tool uses Curio.voice, the 9-12 theme, optional validated device storage, live contextual notes, confirmation dialogs and an honest private ruling marker. No score, timer, correctness gate, network request, recording, commit or polish round was added.
Required files are in tools/usage-panel; tests, reference bundles, images for inspection and audit evidence are in _scratch/usage-panel.

#### Numbers check
_scratch/usage-panel/prep.py recomputed the source numbers before implementation. AHD complements: 100 minus 80 = 20 percent; 100 minus 48 = 52 percent; 100 minus 58 = 42 percent. Distinct test sentences never share a borrowed survey figure.
Eight moving seconds plus 1.5 seconds per marker gives They 26, Literally 14, Hopefully 15.5, To boldly 20 and Less 14 seconds. The longest sweep was run twice normally and once with Motion off; end-year 2026 and repeatable record-end narration were verified.
Computed contrast: brand/panel 6.35:1; brand/sec-bg 6.01:1; brand/paper 6.89:1; brand-ink/brand 6.77:1; ink/panel 14.70:1; muted/sec-bg 7.71:1. All match the spec.
Approximate dates retain their words, while numeric placements are documented. The Hopefully note says the 1960s; Literally's current-entry marker is not presented as an addition date.

#### Facts checked
The following are the facts used on screen, with their named sources and verification limits. Fictional panelist positions are labeled scripted arguments, not authority quotations or measured claims about all readers.

- **They, about 1300:** Plural pronouns with singular antecedents are documented from at least about 1300. [AHD, they usage note](https://ahdictionary.com/word/search.html?q=they).
- **They, early 1590s:** There's not a man I meet but doth salute me / As if I were their well-acquainted friend. [Shakespeare, The Comedy of Errors, 4.3](https://www.gutenberg.org/ebooks/1504).
- **They, 1813:** everybody said, they never saw so fat a haunch [Austen, Pride and Prejudice, 1813](https://www.gutenberg.org/ebooks/1342).
- **They, 1993:** The 14th edition spoke in favor of reviving singular they, according to the later reviser's account. This marker is not a stance-board ruling on formal generic they. [Russell Harper, Chicago reviser, Five Changes That Matter (Writer's Digest)](https://www.writersdigest.com/write-better-fiction/5-changes-that-matter-from-the-chicago-manual-of-style-18th-edition). Corroborated in the reviser's search excerpt; full replacement page rate-limited.
- **They, 1996:** 80 percent rejected the sentence about a person at that level: 20 percent accepted it. [AHD, they usage note](https://ahdictionary.com/word/search.html?q=they).
- **They, 2008:** 56 percent accepted the anyone calls sentence. 59 percent accepted Everyone returned to their seats. These are different sentences from the stance-board example. [AHD, they usage note](https://ahdictionary.com/word/search.html?q=they).
- **They, 2015:** 48 percent rejected sentence (b), so 52 percent accepted it. 58 percent rejected the anonymous-reviewer sentence (c). [AHD, they usage note](https://ahdictionary.com/word/search.html?q=they).
- **They, March 2017:** AP uses a person's pronoun. Generic they is allowed in limited cases where rewording is overly awkward. [CJR, AP and Chicago changes, 27 March 2017](https://www.cjr.org/language_corner/stylebooks-single-they-ap-chicago-gender-neutral.php).
- **They, 2017:** Uses they for a person who uses that pronoun. Generic they is still not fully accepted in formal writing. [CJR, AP and Chicago changes, 27 March 2017](https://www.cjr.org/language_corner/stylebooks-single-they-ap-chicago-gender-neutral.php).
- **They, 2019:** Endorses singular they as a generic pronoun. [APA 7, 2019; singular they guidance](https://apastyle.apa.org/style-grammar-guidelines/grammar/singular-they).
- **They, 2019:** Adds the nonbinary sense in September; names they its Word of the Year in December. [Associated Press via WHYY, 10 December 2019](https://whyy.org/articles/merriam-webster-declares-they-its-2019-word-of-the-year/).
- **They, September 2024:** Generic singular they is acceptable even in formal writing. [Chicago, 18th edition, What's New, 5.51 and 5.266](https://www.chicagomanualofstyle.org/help-tools/what-s-new.html).
- **Literally, 1838-1839:** after he had literally feasted his eyes [Dickens, Nicholas Nickleby, 1838-1839](https://www.gutenberg.org/ebooks/967).
- **Literally, 1876:** Tom was literally rolling in wealth [Twain, Tom Sawyer, chapter 2, 1876](https://www.gutenberg.org/ebooks/74).
- **Literally, 1925:** He literally glowed [Fitzgerald, The Great Gatsby, chapter 5, 1925](https://www.gutenberg.org/ebooks/64317).
- **Literally, 2026:** Lists the in effect, virtually sense with a usage note. Its usage guide treats this as hyperbole needing care. 2026 marks the current entry, not a confirmed first-inclusion year. [Merriam-Webster, Did we change the definition of literally?](https://www.merriam-webster.com/grammar/misuse-of-literally).
- **Hopefully, 1648:** Merriam-Webster cites a sentence-adverb use in Samuel Hartlib's A Further Discoverie of the Office of Publick Address for Accomodations. [Merriam-Webster, Can hopefully mean I hope?](https://www.merriam-webster.com/grammar/yes-you-can-use-hopefully-to-mean-i-hope).
- **Hopefully, 1960s:** Critics begin objecting to the sentence-adverb use during the 1960s. The axis uses 1960 for this decade, not an exact first-objection year. [AHD, hopefully usage note](https://ahdictionary.com/word/search.html?q=hopefully).
- **Hopefully, 1999:** 34 percent accepted the treaty sentence. [AHD, hopefully usage note](https://ahdictionary.com/word/search.html?q=hopefully).
- **Hopefully, April 2012:** AP accepts hopefully in the it is hoped sense. [Merriam-Webster, Can hopefully mean I hope?](https://www.merriam-webster.com/grammar/yes-you-can-use-hopefully-to-mean-i-hope).
- **Hopefully, 2012:** 63 percent accepted the treaty sentence. 89 percent accepted the comparable mercifully sentence. [AHD, hopefully usage note](https://ahdictionary.com/word/search.html?q=hopefully).
- **To boldly, early 1200s:** A split infinitive appears in the early 1200s. 1200 is an approximate axis placement. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **To boldly, 1300s:** Wycliffe often splits infinitives in the 1300s. 1350 represents the century, not a precise dated example. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **To boldly, 1834:** A writer proposes a rule against splitting infinitives. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **To boldly, 1864:** Henry Alford condemns split infinitives. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **To boldly, 1926:** Avoiding a split may require rewriting the sentence, not merely moving one word, and is not always worth it. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **To boldly, 1994:** The guide says the objection never had a rational basis. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **To boldly, 2012:** Advises against splitting infinitives. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **To boldly, 2018:** Allows a split when moving the modifier would ruin rhythm or meaning. [Split infinitive, cited works: Layamon; Wycliffe; New-England Magazine (1834); Alford (1864); Fowler (1926); MWDEU (1994); Economist (2012, 2018)](https://en.wikipedia.org/wiki/Split_infinitive). Secondary source and its cited works; original edition not independently inspected.
- **Less, 888:** læs worda: less of words. The OED example is reported by the secondary source cited here. [Fewer versus less, cited works: OED; Robert Baker (1770); MWDEU (1995); Cambridge Guide (2004)](https://en.wikipedia.org/wiki/Fewer_versus_less). Secondary source and its cited works; original edition not independently inspected.
- **Less, 1770:** Baker states his preference for fewer with a number: most commonly used in speaking of a Number; where I should think Fewer would do better. [Fewer versus less, cited works: OED; Robert Baker (1770); MWDEU (1995); Cambridge Guide (2004)](https://en.wikipedia.org/wiki/Fewer_versus_less). Secondary source and its cited works; original edition not independently inspected.
- **Less, 1995:** The guide describes Baker's preference becoming an absolute rule. [Fewer versus less, cited works: OED; Robert Baker (1770); MWDEU (1995); Cambridge Guide (2004)](https://en.wikipedia.org/wiki/Fewer_versus_less). Secondary source and its cited works; original edition not independently inspected.
- **Less, 2004:** The guide treats the choice as a matter of style. [Fewer versus less, cited works: OED; Robert Baker (1770); MWDEU (1995); Cambridge Guide (2004)](https://en.wikipedia.org/wiki/Fewer_versus_less). Secondary source and its cited works; original edition not independently inspected.

- They survey sentences: 2008 anyone 56 percent accepted; everyone 59 percent accepted; 1996 sentence (b) 80 percent rejected; 2015 (b) 48 percent rejected and (c) 58 percent rejected. Confirmed in [AHD, they](https://ahdictionary.com/word/search.html?q=they).
- Hopefully treaty sentence: 1999 acceptance 34 percent; 2012 63 percent; comparable mercifully 89 percent. Confirmed in [AHD, hopefully](https://ahdictionary.com/word/search.html?q=hopefully).
- Known-person pronouns use the person's pronoun: AP and Chicago 2017 in the supplied [CJR account](https://www.cjr.org/language_corner/stylebooks-single-they-ap-chicago-gender-neutral.php); [APA's own guidance](https://apastyle.apa.org/style-grammar-guidelines/grammar/singular-they) confirms its 2019 seventh-edition change. Merriam-Webster's 2019 sense is in the cited AP/WHYY account.
- Older hopeful manner and distance/time/money less are the supplied comparison examples, checked against the AHD senses and the cited less/fewer discussion. Uncredited sentences are original spec writing.
- The supplied Indiana University APA link is dated 2016 and cannot establish a 2019 change. The supplied Chicago announcement does not establish the 1993 claim; the reviser's Writer's Digest search excerpt corroborates it, but the full article returned 429.
- Original editions behind the split-infinitive and less/fewer secondary summaries were not all independently inspected. The split-infinitive source now mentions a possible 1803 prohibition; this tool preserves the specified 1834 marker as the start of this dataset, not an absolute origin.

#### Break it
- Blindly tried every vote on every sentence. A vote only reveals the same exact dated comparison; it earns no approval or score. Before the first vote, the bar is empty. No-survey sentences say so.
- Tried programmatically activating the hidden personal-they vote buttons. The vote handler refuses; all five personal-they statements remain respectful and the note replaces voting.
- Exhausted 256 setting combinations times 32 reason subsets times five cases: 40,960 notes. Empty grids produce no generated note; undecided settings and empty groups are omitted; no undefined or null prose appeared.
- Tried setting choices without evidence, checking all reasons, changing opinions and toggling every option. These remain private judgments and never claim mastery. The docket's ruled label means at least one setting has a choice, as notes.md explains.
- Tested Chicago at 2016, 2017 and 2024; unknown, advises against and accepts were distinct. Sweeping the slider changes recorded history only, never an earned result.
- Tried interrupting playback with markers, slider input, real jittered whole-pixel dragging, modes and case changes. Controls respond immediately; no stale sweep keeps updating another case.
- Canceled Rebuild and Clear, then confirmed each. Cancel preserves edits; confirmed rebuild uses the current grid; confirmed clear removes only that case's contextual ruling. An unruled diamond says Not ruled yet.
- Saved an edited note, opened a fresh page, and recovered the exact text and choices. Denied storage still allowed working choices and showed the session-only status. Storage data is type-checked and user text is never rendered as HTML.
- Copy note returned Copied note on a real held-click path with all reasons selected. The final 212 functional assertions and 40,960 combinations passed; captured results are in functional-final-result.json, copy-result.json and the related Scratch files.

#### Voice walk
No speech occurred before input. At a two-second held-click pace, the main path heard Copy Editor, Linguist, Record how-to, Ruling how-to and note-ready, in that order. The queue ended empty.
The vote instruction was dropped when newer speaker choices and the student's vote made it stale; it stayed in the hint and Read. The first-tap welcome was skipped by the tap's own line under BASELINE rule 16. Speaker changes now hush an older argument immediately.
The side path heard the Hopefully case line, Reporter argument, Read, Record how-to, Ruling how-to and Less case line. Read interrupted the argument, and changing modes released Read without a dead queue.
Both normal sweeps spoke record-end, including the second run; Motion off also spoke it. Automatic how lines did not repeat. Explicit emblem requests replay their argument. Same-mode and same-case quick taps no longer cut an instruction that is already speaking. Default Sound was used throughout these walks. Sound and Read behavior use the shared kit rather than copied queue logic.
Logs: voice-main.json, voice-side.json, play-twice-result.json and play-calm-result.json. No voice was recorded as directed; the browser fallback does not reproduce the planned firm-captain timbre.

#### Feel check
Played the chair's path through competing arguments, sentence votes, historical reversals, contextual choices, editable notes and the personal marker. The best moment is seeing Chicago switch from advises against to accepts, then placing one's own four-setting ruling in that record.
Flat moment 1: compact layouts made the emblems too small and clipped the longest hearing's plates. Increased medium-height art, measured all 16 sentences, tightened the compact paper treatment where needed, and verified a visible Persuasive mark at 680x425.
Flat moment 2: the dense record cluster and a clipped fifth reason obscured real choices. Fanned the labels with true-date leaders, reserved minimum marker height, and arranged reasons in two columns where space permits. All four setting rows and five reasons remain available together.
Compared both reference tools after bundling copies into Scratch. The hearing has richer painted materials and a clear focal sentence; Record deliberately has the sober finish of an editorial instrument. It has less rapid action than Beat Lab, consistent with the specified unscored hearing.
Comparison: [Usage Panel beside Beat Lab](../../_scratch/usage-panel/feel-comparison.png). No separate polish round was started.

#### Done when
1. PASS: all five dockets, 16 sentences, 25 case arguments and 33 evidence cards exist; the functional run visited every sentence and all personal-they variants.
2. PASS: six finished paintings, no person, face or hand; emblems have role-named brass plates and the Teacher's check is drawn in code.
3. PASS: vote-gated comparisons show the exact per-sentence figures; every non-survey sentence has the required no-vote message, and personal they has no vote.
4. PASS: Chicago is unknown at 2016, against at 2017 and accepts at 2024. Native arrow input and the custom Page Up/Down, Home and End handlers were checked.
5. PASS: nominal maximum 26 seconds, same Motion-off timing, repeatable end event and immediate real-drag/marker/case/mode interruption. Frame scheduling adds normal millisecond jitter.
6. PASS: 2015-2019 markers have separate readable targets and leaders, checked at 1280x800 and in the real 375 px iframe.
7. PASS: exhaustive note grammar, live updates, edited-note reload, copying and both confirmation outcomes checked. The note editor scrolls below the grid in narrow layouts as specified.
8. PASS: Your panel, 2026 appears as a diamond; its selected card and accessible label list the actual four settings, including undecided ones.
9. PASS: shapes plus words survive grayscale, named contrast ratios pass AA, and measured interactive targets meet 44 px. Final phone label and icon styles are at least 10 px, with 18 px visible icon glyphs.
10. PASS: no pre-input voice; mode/case changes hush; no repeated how-to starts on the main and side walks; record-end repeats. A first action can legitimately skip the welcome or invalidate queued speech.
11. PASS: the sentence is Hearing's largest type at 1366x768 and 680x425; Record's true axis spans its work area; all four Ruling rows are central and visible. Short Record source cards and narrow usage-note editors require scrolling, not the primary choices.

#### Wave lessons
- Hint and voice: PASS. Hints change synchronously and name actions; Read uses the current state. Stale instructions are dropped and the queue is governed by Curio.voice.
- Focus and layout: PASS. Hearing updates existing controls; live ruling updates preserve native radio focus. Dialog return uses preventScroll and nothing takes focus on load.
- Sizes: PASS for primary choices and 44 px targets across every STANDARDS size. Phone labels were raised to 10 px; narrower note editors deliberately scroll below the grid.
- No giveaways: PASS. No correctness key, reward meter or reflection gate exists. The AHD bar is a dated source statistic and cannot be changed by choosing another opinion.
- Honest numbers: PASS. Exact sentence/year labels, visible unknown stances, disclosed approximate dates and a current-entry label prevent false precision.
- Standards: PASS for L.11-12.1 and its convention/change subpoint through solo judgments and historical comparison. SL.11-12.1 is supported when partners discuss; solo clicks do not falsely claim a collaborative discussion. No family engine is specified.
- Motion off: PASS. No infinite animation remains; the active emblem does not lift and playback keeps its duration.
- Short choices: PASS for all votes, four setting rows, five reasons and panelists. The audit's narrow editor-scroll lead concerns the downstream note editor and its three actions, retained below the grid with an explicit scroll hint.
- Resize mid-animation: PASS in the audit: no exceptions or controls left disabled. Record timing and drawer fitting carry the current state through resizing.
- Late welcome: PASS. Multi-mode welcomes never use welcomeAfter. The first tap's own line can skip welcome under the baseline.
- Unknown as unknown: PASS. Dashed No ruling on record precedes the first dated stance; no past opinion is inferred.
- One look, one meaning: PASS. Circle = use, square = authority ruling, diamond = one's own ruling; stance shapes accompany words. Grayscale was inspected.
- Badge truth and restored hints: PASS. Ruled means a choice exists, not a correct answer; case and mode changes reset the context and hint.
- No answer by copying words: PASS. This is contextual judgment rather than a keyed answer-matching task.

#### Audit leads
The single full audit completed on Chrome 9981, using host 8785, within its 40-minute bound. It reported 35 leads. No exceptions, disabled controls, focus failures or stuck playback were found in its completed click and resize stress walks. The audit ran across an earlier build while its leads were addressed; final targeted frames and result files verify the corrections below. It was not rerun.
- Eight initial phone text leads and one later ruled-label lead: fixed. Docket status labels are 10 px. Header controls use 10 px accessible text and visible 18 px pseudo-element icons; all three final phone modes were measured again.
- Two narrow Ruling scroll-panel leads: retained as specified. All four setting rows and five reasons are available together; the editable note and Rebuild, Copy and Clear sit below the grid. A visible hint names the scroll. The final phone test scrolls to Copy and verifies it is reachable while the docket remains visible.
- Two evidence keep-region leads: fixed. Evidence is a nonmodal drawer constrained inside the work stage; it leaves the docket and hint unobscured. Final short-preview and phone probes check bounds and docket hit-testing. A real docket click changes case and closes the drawer.
- Fourteen first-tap welcome leads: permitted under BASELINE rule 16. The tapped action speaks its own case, argument or mode line. The chair premise remains in Hearing's hint and Read, and later mode instructions are heard on the main path. No stale welcome is queued behind another context.
- Eight quick double-tap leads: fixed. Selecting the already active case or mode does not hush its current instruction. Real 0.7-second double-taps on Record and Literally start each line once without cutting it. Explicit emblem requests are events and replay on a second request, verified separately with two real clicks.
All 64 audit PNGs were individually opened and inspected. Final affected-state frames also cover phone fonts, short-preview sentence fit, the evidence drawer, editor reach and repeated input. Earlier failing images remain in Scratch for provenance.
The final 16-sentence short-preview probe caught a four-pixel overflow on They sentence (c). Its compact card treatment was corrected and the affected check rerun: all 16 now fit, including a visible Persuasive mark. No full size or audit run was repeated.


#### Frames looked at
bar-frames: 2; early-frames: 4; fix-frames: 2; functional-frames: 4; voice-frames: 5; late-frames: 29; target-frames: 10; phone-early-frames: 1; phone-frames: 5; postfix-frames: 12; compact-final-frames: 3; audit: 64.
All listed PNGs were opened and inspected, including every audit frame. Earlier failing frames are retained as evidence; final targeted frames cover the corrected states. The full multi-size pass ran once, with only affected states re-shot afterward.
All screenshot batches used muted Chrome on 9980; the audit used 9981. Narrow hosting used 8785. Host pages were removed and each owned Chrome and server was closed after its batch.

#### Art made
Six images generated separately with built-in imagegen; first candidates were retained after raw and final-size inspection. No people and no redraws. Full saved prompt set: art/prompts.json. Raw originals are in art/raw.
Finished assets: art/hearing-room.webp, art/pencil.webp, art/trumpet.webp, art/papers.webp, art/quill.webp and art/notebook.webp. All six are used in the tool, with people false and drawn_by codex.
Final art: 220.2 KB; recorded voice: 0 KB; final bundle: 410.3 KB (420,150 bytes), below the 2 MB goal. No teaching image was dropped to reduce size.
Credit: Illustrations generated with OpenAI gpt-image, edited for Curio Class.

#### Art still to paint
None.

#### Engine changes wanted
None. No kit, scripts, docs or other tool sources were edited.

#### Left open
- Some original historical guide editions remain secondhand, as detailed under Facts checked. The supplied Chicago 1993 source needed a better route; its full replacement article was rate-limited.
- Browser narration is the required Build fallback, not a recording of the named bank voice. No recordings were requested or made.
- Narrow note editors and short-preview source cards scroll; their primary judgment controls remain visible. The 1.5-second source-card pause is retained from the spec despite being short for longer cards.
- No published percentage for the exact Jordan sentence is supplied. The different AHD personal-pronoun survey was not substituted; the spec's note-only option remains.
- Process exception: the first two read-only inspection commands finished immediately but lacked explicit timeout wrappers. Subsequent commands used explicit limits. A dependency-install attempt timed out; art processing succeeded with existing local dependencies instead.
- The single full audit completed. Historical source limits and the specified narrow-editor scrolling are the remaining review items.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: usage-panel

#### Played

Played cold as a Grade 11 student before reading codex-report, handoff, notes or src; then checked the projected teaching path.
All five cases, 16 sentences, five voices, voting, evidence, Record, Ruling and the earned usage note. Strong editorial atmosphere; the dated reversals are the best moment.

#### Findings fixed

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

#### Findings left

No confirmed blocker or should-fix finding remains. Clear-ruling focus concern rejected by real input: focus remained on Clear; no unnecessary change made.

#### Break it

- Votes: tried every option, rapid changes, all 16 sentences and a hidden Jordan vote. Comparisons are fixed to exact sentences/years; hidden personal voting is refused. No correctness, points or achievement is awarded.
- Persuasive/Not for me: marked without reading and changed opinions. These affect only private marks/reasons; they award nothing. Jordan's hint stays respectful and actionable.
- Ruling/ruled status: selected easy rows, every option and all reasons. This is a private contextual judgment, not mastery. The documented ruled status means at least one chosen setting.
- Notes: recomputed 40,960 setting/reason combinations; no null/undefined prose and empty grids stay empty. Confirm/cancel, copying and edited-note reload were exercised.
- Timeline/percent bars: swept endpoints and recent dates, used arrows and marker-jump keys, dragged with whole-pixel jitter, and interrupted playback. No earned score exists to cheat; 2016 Chicago is unknown, 2017 against, 2024 accepts.
- Playback: two normal sweeps reached 2026 at 26.00/26.08 s with normal frame jitter; record-end spoke twice. Calm took 26.01 s, stepped through marker years, and left zero infinite animations. Real dragging stopped the sweep immediately and the year stayed fixed.
- No quiz, reflection gate, best score or success meter exists; none was added.

#### Voice walk

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

#### Facts checked

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

#### Sensitivity

Personal pronouns/nonbinary identity: a cultural reviewer should check the respectful separation of a person's pronouns from contested generic use, and the risk of treating prescriptive school conventions as judgments about a home dialect or intelligence. Jordan never has an acceptability vote. Notes explicitly protect that distinction. A cultural reviewer should also judge whether the private Not for me mark on that example could be mistaken for judging a person; it is a case-wide argument note. No people appear in the art.

#### Flattest moment left

The specified 1.5-second pauses are too short to read longer evidence cards fully. Stop and manual markers allow inspection; changing the prescribed pacing would need a spec decision. The personal-ruling payoff and note response were lifted without adding scoring.

#### Graphics

Viewed all six finished images and rendered scenes. One style, directional lamp light, walnut/brass/paper layers, no text artifacts, no people, all people flags false. Paper emblem redrawn with built-in imagegen: art/raw/papers.png and art/papers.webp; full prompt set in art/prompts.json.
Compared existing Beat Lab and Snowy Mail Route bundles without writing into their folders. Kept the richer hearing materials and sober older-student instrument layout. Art 213.7 KB; final bundle 404.9 KB. Side-by-side frame: ../../_scratch/usage-panel/review-comparison.jpg.

#### Audit

The one full audit finished within its 40-minute limit, at about 39 minutes: ../../_scratch/usage-panel/review-audit/audit.md. All 70 audit frames were opened and inspected; full sizes, all states in its frozen input list, Motion off, repeated controls, quick taps and resize stress completed.
Its 18 leads were 3 intentionally hidden phone button words (visible icons retain accessible names), 2 compact note-editor fold flags (all setting/reason choices remain visible; the specified editor is below and the hint says Scroll), and 13 skipped first-tap welcomes where the control spoke its own fitting line. BASELINE 16 allows those skips; the premise stays reachable in Hearing hint/Read.
The click log also exposed the Evidence welcome mismatch, which the audit treated as welcome heard. Fixed it, the contrast, visible personal label, duplicate-year keys and interrupted-marker hint; re-shot only affected frames at 680, 1366 and/or the real 375 iframe. Targeted checks and the final full voice path passed without runtime warnings/errors. No second audit or polish round.
Final contrast checks: brand/panel 6.35:1; brand/section 6.01:1; brand-ink/brand 6.77:1; ink/panel 14.70:1; muted/section 7.71:1; plate 5.20:1. Grayscale and keyboard-only frames were inspected. Owned Chrome ports 9961-9963 and host 8765 closed; temporary tool host.html removed.

#### Left open

Full-text Chicago 1993 verification and the named historical original editions remain provenance limits; no invented replacement facts or new markers were added. The specified 1834 event is one proposal, not a claim that no earlier objection existed.
SL.11-12.1 needs the specified paired discussion; solo use prepares a judgment but cannot itself be collaborative discussion. Notes already state this accurately.
Unattended choices followed the spec: retained the note-only Jordan example, contextual private opinions, no recordings and the original playback schedule. No questions, commits, shared-kit edits or new topics.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Usage Panel handoff

Build only. No commits or polish round. Read spec.md and codex-report.md before changes.

#### Structure
src.html starts from the kit starter and includes the dark 9-12 theme. A single CASES array is inside the clearly marked case-data and timeline block. SOURCES names each evidence source. Hearing nodes stay in place during votes and speaker changes. Ruling controls rebuild only on entry or case change; individual radio and checkbox events update the note without replacing their controls.

asOf handles dated stance lookup. playRecord uses one cancellable animation-frame clock: eight seconds of moving time plus 1.5 seconds for every marker, including same-year markers separately. Motion off changes year movement only. Stop, slider pointerdown/input, markers, cases and modes invalidate the clock immediately. Record labels fan into a grid with leaders to the true linear dates so the 2015-2019 cluster remains selectable.

fitHearing measures the sentence card and panelist rows after content or size changes, keeping the marks inside the short preview. All 16 sentences were checked at 680x425 after voting. Long compact cards use tighter sentence spacing; larger screens retain the generous painted emblems.

buildNote is a pure function. Partial rulings omit undecided settings and empty choice groups. Every case owns votes, private marks, reasons, choices and edited text. Storage is validated on load and every access is caught. Copy has a clipboard fallback. Confirmation uses a keyboard-accessible dialog and returns focus with preventScroll. __tool exposes state, cases, saved work, note builder, stance lookup and the kit voice log.

#### Open questions and specification tensions
- The only listed open question asks about AHD evidence for personal they. Keep the Jordan sentence note-only, with no acceptability vote or borrowed statistic. The AHD entry has a 2015 survey about a different sentence; that figure is not transferred here.
- The brief requests built-in image generation and overrides the spec's local FLUX provider. All six assets were generated with built-in imagegen, copied to art/raw and processed only with art.py --rekey. No people appear.
- The exact original edition sources for several historical markers are not all accessible from the supplied links. Keep those provenance gaps visible in the report, especially Chicago 1993 and the split-infinitive guide dates. The sources are named, not invented.
- The spec supplies uncertain date ranges but requires an integer slider. Labels retain the uncertainty; numeric placements are explained in notes.md.
- Markers that share recent years cannot have both readable 44 px labels and literal coincident horizontal positions. The axis keeps true positions, while labels stack and fan with thin leader lines.
- The spec's note ending says earlier authorities ruled differently even when Literally's only authority marker is the current entry at 2026. That case uses a factual current-entry ending rather than pretending the inclusion year is known.
- The prescribed 1.5-second marker pause is short for some source cards. It is retained; Stop and all controls remain live so students can inspect a card.
- The spec's Indiana University APA link is dated 2016. The same guidance is checked against APA's own singular-they page, with the edition date retained from the spec.
- Compact Ruling keeps the grid central and the note below it as specified. Reference content can scroll. See report for measured layout limits.
- At short preview heights, Record's stance board sits beside the fanned marker labels under a full-width axis, with the source card below. Year and playback controls remain sticky while reading it. This fits readable 44 px marker targets and the board together.
- The under-760 hearing card grid conflicts with fitting a 680x425 preview. STANDARDS wins: short landscape previews keep the five emblems in one row; tall phones use the requested two rows.
- Some supplied panelist statements exceed the brief's two-short-sentence reading guideline. Their specified wording is retained, with Read and a scrollable statement region.
- The They usage note explicitly says generic singular they, so a contextual Avoid choice cannot be read as a ruling on a known person's pronouns.

#### Sensitivity
Singular they includes personal pronouns and nonbinary identity. The known-person example never asks whether that person's pronoun is acceptable. Review the respectful distinction between personal pronouns and the generic-usage disagreement. No portraits, bodies, religion, Indigenous topics or hard-history scenes are depicted. Do not equate home-language conventions or dialects with intelligence.

#### Engine changes wanted
None. Kit, scripts, docs and other tool sources remain untouched. Reference tool copies were bundled only inside Scratch.

#### Voice and art
The chair premise remains in the Hearing hint and Read even when the first action skips welcome. Explicit emblem requests replay their argument as events; automatic how-to instructions remain once per load. Evidence is a nonmodal drawer fitted inside the work stage, so docket tabs and the hint remain visible and usable. Case and mode changes close it; Escape and Close also dismiss it.

voice/lines.json lists the specified firm-captain voice and all fixed spoken lines. No recordings were made, as required by the Build brief. Browser fallback does not reproduce the bank voice's timbre. art/prompts.json is the complete saved prompt set; all six assets have people false and drawn_by codex. No paintings are missing.

#### Cold review changes
Read in the evidence drawer selects one visible card instead of speaking all off-screen cards. Opening and closing that drawer updates the hint synchronously; closing also stops its reading. Private marks on the personal-pronoun example never suggest a hidden vote control. Adding or selecting Your panel hushes earlier instructions. Carried-forward panel percentages include their original survey year. Successful storage writes restore the saved status after an earlier error.

The teacher paper stack was redrawn through built-in imagegen on magenta, with the complete prompt saved in art/prompts.json. All five cutouts were reprocessed with art.py --rekey using despill and hole handling. Their warm painted style, room, plates and materials remain. The personal ruling card has a restrained diamond seal and separate setting lines; live note changes have a brief ink-settle treatment that stops with Motion off. No new topic, assessment or mode was added.

Post-audit fixes: private marker labels show all four short setting choices, with compact layouts reserving two columns for that label. Page Up/Down visits both markers when years repeat, and can reach the personal marker. Paper metadata, placeholder and status ink now use #6a4c2d, at least 5.63:1 on the darkest paper. No welcome may start over an open drawer or confirmation; opening confirmation hushes speech, and the dialog describes its question to assistive technology.

Selecting the private marker directly also refreshes the hint. This covers interrupting an active sweep after the marker was already added; the old playing hint must not survive that stop.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
