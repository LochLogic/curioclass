# Codex review: audience-talkback

## Played

Cold grade-4 exploration of all three modes preceded the builder's report, handoff and source. Then completed the repaired main path with Sound on and checked the projected-teacher controls. The painted theater and the bear's change to concern at line 8 are strong.

## Findings fixed

- **blocker/general, src.html playback:** immediate speech errors completed lines in milliseconds. Speech/clip failures now preserve the remaining caption time; forced failures cannot rush the watched check.
- **blocker/general, notebook:** five base lines followed by a last-instant Lights flip and Stop produced a fair trial without observing the change. Recipe revisions and whole-line observation now keep that row out of results.
- **blocker/general, notebook:** replaced an arbitrary-five-lines predicate with the first five setup lines. Short-line hopping plus the ending cannot earn a trial.
- **should fix/general, storage:** null legacy rows aborted loading. Valid work now survives; version-1 ratings remain editable but lack verified observation and cannot contaminate new results.
- **should fix/general, hints:** base replays no longer assume a swap. Unobserved trials explicitly say to tap Play again; incomplete Watch runs retain the appropriate starting instruction.
- **should fix/general, Watch:** unreliable 33/21-second browser labels now say Timing varies. Complete future recordings calculate measured totals including pauses.
- **should fix/general, phone:** moved the hint above the stage. Hint, full-size stage, four switches, Play/Stop and ten ticks fit at 375x812, including after resizing during playback.
- **should fix/general, Clear:** clearing work also restores Base A and AAAA.
- **polish/general, results:** added a finding drawn from the student's ratings, including ties and no change. Zero ratings draw no colored bar. Four bars and their labels fit at 680x425.
- **polish/general, art:** redrew the weakest prop, the bicycle, with a clearer slack chain and damaged wheel while retaining the painted style.

## Findings left

**blocker/general:** twenty acted character clips and twenty-five host/Read/card recordings are absent. The required [CODEX-BUILD.md](../../docs/agents/CODEX-BUILD.md) says, "Do not download anything or record audio." This review obeyed that rule. The tool remains a labeled browser preview; final authored acting, bank identities, measured clip lengths and audible mix quality are unverified. The full audio portions of Done when 2 and 3 remain open.

## Break it

- Rapid Play/Stop rhythm and jump-to-10: no notebook row. Five short lines plus the ending: no row.
- Late switch then Stop, followed by A lot: editable unobserved row, no chart bar. A normal single swap and a genuinely observed live swap produce fair rows and correct bars.
- Two changes then undo one: both remain in the trial and are excluded. Base replay: excluded, with an appropriate instruction.
- Zero and repeated ratings: zero-length bar and correct 1.5 average. The chart states its 0/1/2 mapping; opinions have no answer key or mastery badge.
- Fourth criterion rejected. Six chosen A/B ratings and both verdicts survive a reload. Legacy notes survive safely; denied storage shows saving unavailable.
- Held teacher-counter clicks after scrolling: 1/0, 1/1, 2/1, then Reset to 0/0. This is an explicitly manual teacher counter, not a student score.

## Voice walk

Sound on, 120 ms presses, 2-second tap pace: stage, A, B, feelings, Go to lab, Lights, Play through five setup lines, Stop, rating, results, Talkback, three criteria/six ratings, verdicts, audience cards. Both full Watch versions completed.
Line starts in order: welcomeWatch, watchNext, feelHow, welcomeLab, rateHow, welcomeTalkback, verdictHow. A full audience run then starts audienceAR, audienceLM, audienceST and talkbackDone in order, ending with an empty queue.

| Line | Kind | Expected starts | Observed |
|---|---|---|---|
| welcomeWatch | how/welcome | 1 | 1 |
| welcomeLab | how/welcome | 1 per page | 1, then 5 silent heard returns |
| rateHow | how | 1 | 1 |
| welcomeTalkback, verdictHow | how | 1 each | 1 each |
| audienceAR/LM/ST, talkbackDone | event | 1 each per full reveal | 1 each |
| Read | forced read | 2 in side walk | 2, including Sound off |

Read/hide/mode cancellation drops stale speech; no host line starts inside actor playback. Some instructions are cut when the student's next action makes them stale, as the spec requires. The new stopped-trial instruction was separately heard while Play was enabled. Logs are in ../../_scratch/audience-talkback/voice-review/ and audience-review/.

## Facts checked

- Personal experience, differing responses, criteria and technical elements: [National Core Arts Standards, Theatre](https://www.nationalartsstandards.org/content/theatre), Re8.1.3-5.a and Re9.1.4-5.a/b. Notes identify these strands rather than implying every substandard.
- Design choices support storytelling: [Educational Theatre Association, Production & Design Elements: Where to Begin](https://schooltheatre.org/production-design-elements-where-to-begin/). No universal blue-equals-sad rule is taught.
- Controlled-variable comparisons: [NGSS Appendix F, Practice 3, grades 3-5](https://www.nextgenscience.org/sites/default/files/resource/files/Appendix%20F%20%20Science%20and%20Engineering%20Practices%20in%20the%20NGSS%20-%20FINAL%20060513.pdf).
- Independent enumeration: 16 recipes, four single swaps per base, eight directed fair comparisons. Nine gaps plus the pre-line-8 pause total 4.8 s for A and 2.3 s for B; pre-recording estimates are 32.8/21.3 s. See ../../_scratch/audience-talkback/review-math.json.
- Contrast recomputed using [W3C WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html): coral/paper 6.812:1, ink/paper 14.776, muted/paper 8.120, ink/panel 12.584, coral/panel 5.801, dark/A 11.934, dark/B 9.465; result ticket 9.173.
- The ten-line scene, recipes, music and audience cards are original Curio Class content from the spec. The same dialogue is used in both deliveries. The knee injury is fiction, not medical guidance.

## Sensitivity

No represented culture, religion, Native tradition or hard history; all actors are fictional animals. A reviewer should check family-experience prompts without assuming every student has a grandmother or allowance. The three cards describe individual fictional experiences.

## Flattest moment left

The browser acting preview remains the flattest moment. Authored performances are needed for convincing vocal evidence. The formerly bare chart now ends with the student's own finding, without rewarding a preferred opinion.

## Graphics

All ten images checked in contact sheets and stage frames; no missing listed art or people assets. Kept the theater, palette, poses and quiet motion. The bike redraw used built-in image generation; final asset is [art/bike.webp](art/bike.webp), with its prompt and provenance in [art/prompts.json](art/prompts.json). Generated alpha is preserved. Colored RGB outside alpha was invisible in the real stage, so it was not a visible keying defect.
Art totals 461.2 KiB; final self-contained bundle is 817,892 bytes, about 799 KiB. Compared the finish with the saved Beat Lab reference frame.

## Audit

Completed the single audit within its 40-minute limit: 62 leads, 51 PNGs inspected. All eight initial sizes were clean. No runtime, focus, repeat, Motion-off or resize failures.
Phone hint placement and its inaccurate notebook keep fixture were fixed afterward. Targeted 375/680/1366 frames, a live 375-to-680-to-375 resize, scrolled notebook access, reset and held vote clicks passed. The compact feelings screen also retains every choice and tick.
Remaining leads concern intentional long-form scrolling, the visible Talkback hint's hidden mirror, required welcome suppression during actors/dialogs, idempotent resets and teacher-counter movement. Every lead has a disposition in [review-audit-responses.md](../../_scratch/audience-talkback/review-audit-responses.md).
The audit was not repeated after the phone repair. Final checks and hashes are in [review-validation.json](../../_scratch/audience-talkback/review-validation.json). Test-host favicon 404s were distinguished from tool errors.

## Left open

Release remains blocked by the missing authored audio described above. Retained the spec's sample-first recording route without asking unattended questions. No new topic, kit change or git commit. Writes stayed in the tool and its Scratch folder; all owned Chrome/host ports are closed and no host.html remains.

