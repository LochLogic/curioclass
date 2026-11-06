# Codex review: cover-version-review

## Played

Cold as a grade 7 student, then as a teacher projecting the strip. Played Listen, Measure, checked records, Review and taste before reading builder notes or source. The A/B contrast and illustrated record-desk world are strong; the blank review and tiny checked feedback were flatter.

## Findings fixed

- Blocker, general, Measure/Review: a single guessed field exposed all four answers, including an untapped tempo. Real held clicks reproduced it. Checks now expose only explicitly attempted fields; unchecked guesses no longer unlock evidence.
- Blocker, general, comparison: trying choices after seeing truth replaced a miss with a perfect comparison. First checked responses now persist through corrections and Clear taps, including the denominator. Corrections remain useful evidence, clearly separate from that initial record.
- Should fix, general, Review: blank claims and identical duplicates could fill the review without explaining anything. A Because explanation is required; exact duplicates stay disabled and changing criterion recomputes eligibility.
- Should fix, general, tapping: a partial, lost-beat or discarded retry could reuse a previous matching bpm. A fresh attempt clears and saves removal of the old estimate; invalid/lost attempts clear it too.
- Should fix, general, playback: A's line 7 ending was a short note, despite the held-note label. Lines 4 and 7 now sustain their final pitch over beats 6 through 8; the final word lights on those beats in both versions.
- Should fix, general, voice: a picker change dropped the fifth queued saved-claim announcement. Picker changes now drop stale how-to lines while preserving valid saved-claim events; deleted claims invalidate their pending event.
- Should fix, general, craft: narrow corner copy clipped and Version options truncated. Compact corner spacing and A/B/Both labels now fit. Replay synchronizes the draft pin; preferences credit the other version.
- Should fix, general, compact Review: the audit confirmed the first saved pin below the 680x425 fold. The newest playable claim now replaces the evidence row in short previews; tapping a lyric line restores its evidence choices. The native range/dialog return-focus path also has a guarded fallback.
- Should fix, general, modal voice/craft: Reset as the first tap could narrate Listen over its confirmation. Welcomes now wait until dialogs close. Taste tracks now span their endpoint labels with 44-pixel targets. Singular tap/cell/beat wording and copy feedback when storage is blocked were corrected.
- Polish, general: Check gives a restrained lane reveal instead of only changing a number; repeats identify themselves in the transport. Redrew the weakest art, the trombone, with an unmistakable long slide.

## Findings left

- Should fix, source/spec conflict: no authenticated pre-1930 printing verified. The cited Hudson score is a modern engraving. Preserved the explicit transcription limitation instead of claiming the normalized reference is historically verified.
- Nit: My taste repeats its heading inside the closing card. Left intact.

## Break it

- Empty Check is disabled. One loudness guess no longer reveals tempo, instruments or extras. Wrong -> Check -> correct -> Check keeps the original miss; clearing a wrong tempo cannot shrink the denominator.
- Review offers only checked fields; cycling unchecked options reveals no correctness. No pin, no chip or no explanation blocks Add. Exact duplicate blocks; eight-claim and 140-character states inspected. Interpretations and personal taste are not automatically graded.
- Real held taps at 58 and 120 bpm matched within 8 percent; three taps requested a fourth. Fast 100 ms tapping, lost-beat gaps and partial retries could not retain old bpm. Exact 30/240 boundaries accepted; 29/241 discarded.
- Both-version pin played A then B. Copy retained line numbers and evidence, actual clipboard checked. Reset cleared measurements, first comparisons, claims and preferences. Slider extremes do not earn a score.
- Listen intentionally shows reference values. Copying those can produce a matching record; this is an open listening/explanation tool, not a secure assessment. No score, best score or mastery award is claimed.

## Voice walk

Held clicks at a two-second pace: lyric 1 -> Play line -> A/B -> Stop -> Measure -> Play line -> Stop -> loudness -> Check -> Review -> Version B -> lyric 1 -> evidence -> explained claims -> Both pin -> Read -> Sound off/Read -> Reset.
Heard in order: welcomeListen, welcomeMeasure, checkDone, welcomeReview, needEvidence, five claimAddedSingle events, claimAdded, Read. Welcome starts are interrupted when the student starts music; no narration waits ahead of playback.

| Line | Kind | Expected | Heard |
|---|---|---|---|
| Each mode welcome | how/welcome | once | 1 each |
| needEvidence | how | once across repeats | 1 |
| claimAddedSingle | event | five | 5 |
| claimAdded | event | once for Both | 1 |

Read stopped music and worked with Sound off. No fixed lines were added; lines.json still matches allLines. Browser speech is used, with no recorded calm-professor takes; subjective headphone timbre remains open.

## Facts checked

- Brackett Jr., 1848, Alfred, Maine, Shaker dance song: [Canterbury Shaker Village finding aid, p. 4](https://www.shakers.org/wp-content/uploads/2020/05/ROGER-LEE-HALL-COLLECTION-Canterbury-Shaker-Village.pdf).
- Eight lyric lines and religious dance context: [Roger Lee Hall, Joseph Brackett's Simple Gifts](https://www.americanmusicpreservation.com/JosephBrackettSimpleGifts.htm). No Copland arrangement reproduced.
- Copland used the tune in Appalachian Spring, premiered in 1944 with Martha Graham: [Library of Congress](https://blogs.loc.gov/loc/2014/10/documenting-dance-the-making-of-appalachian-spring/).
- Meaning of cover version: [Oxford Learner's Dictionary](https://www.oxfordlearnersdictionaries.com/us/definition/english/cover-version).
- Interpret expressive intent, apply criteria, connect preference: [NCAS Music at a Glance](https://nationalartsstandards.org/sites/default/files/Music%20at%20a%20Glance%20rev%2010-2-14.pdf). Student actions: criterion-backed playable claims, interpretation, taste and comparison sentence.
- Fictional performers, all 64 content-table fields, keys, repeats, dynamics, instruments, 8 percent rule: spec Content/Sources, independently compared with source table. Numbers in review-numbers.json.
- A upper bound 69.3679 s; linear easing 68.8215 s. B 100 beats at 120 bpm = 50 s. Actual full plays: 68.8349 s and 50.1025 s. Four-tap 30 ms jitter, 20,000 trials: 100 percent at 58, 99.54 percent at 120. Contrast: ink/paper 15.55:1, muted/paper 6.45:1, white/brand 6.72:1, ink/A 14.15:1, ink/B 14.24:1.
- Historical source requirement remains unverified: [IMSLP Hudson #52769](https://imslp.org/wiki/Simple_Gifts_(Brackett,_Joseph)) identifies the consulted modern score. It cannot establish a pre-1930 printing.

## Sensitivity

Shaker religious dance song. A cultural reviewer should check songwriter/community credit, the origin of the words, and that fictional Porch/Parade treatments are not presented as Shaker performance practice. Questions about simplicity must not make either arrangement morally or culturally superior. Notes and handoff now name this. All eight illustrations depict objects/empty venues, with explicit people:false.

## Flattest moment left

Writing the Because explanation is still the slowest moment. Kept it: interpreting evidence is the skill. Check now visibly reveals attempted lanes, and repeated passages identify themselves. The compact first pin is now immediately playable instead of hidden below the writer. The expressive A/B contrast and playable pins remain the payoff.

## Graphics

Inspected all eight WebP images and their rendered sizes. Kept both rich venue sleeves and five other cutouts; replaced only the ambiguous trombone. Built-in imagegen replacement is art/trombone.webp, with its raw PNG and prompt in art/raw/ and art/prompts.json; predecessor retained in Scratch. No placeholders or missing art tokens. Final art 246,666 bytes; bundle 442,136 bytes (431.8 KiB). Opened both approved bar tools from existing Scratch bundles; retained this tool's own visual identity.

## Audit

Completed once within the 40-minute limit: eight leads. Four are the specified scrolling phone strip, three are intentional music-first welcome suppression, and one was the confirmed compact saved-pin flaw, now fixed. No second full audit.
Inspected all 40 audit frames, with full-size lead frames and seven labelled sheets. Controls, five-click/quick-tap narration, Motion off and resize stress checks were clean. Re-shot compact pins at 680/800/1000, all three affected taste sizes, modal voice, continuation/replay, singular wording and blocked storage. Final hosted phone run: zero errors.
The initially failing custom focus fixture had no active range. Real held-click mode entry, native End and dialog close now pass. Final validation has 16 passing checks; all owned Chrome/host ports are closed and host.html is removed. Evidence: review-validation.json, review-audit-dispositions.md, post-audit-frames/, voice-recheck/voice-main.json and the original cheap-before.json, all in this tool's Scratch folder.

## Left open

Authenticated historical printing and corresponding exact melody/rhythm comparison. No invented edition or unsupported historical-transcription claim added.
A line 8 spec conflict remains: table says Voice only, prose says guitar disappears on the repeat. Kept the explicit table rather than inventing an instrument change.
Browser speech cannot demonstrate the selected recorded bank voice; no recording was authorized. Physical headphone timbre/latency was not measured in muted Chrome.
One cold pass and focused rechecks only. No commits, no shared-file changes, no deployment. All evidence is in this tool's Scratch folder.
Process deviation: the first four read-only commands completed immediately with tool yield limits, before the enforced-deadline wrapper was installed. Subsequent shell commands had enforced deadlines. A full-A test first hit the driver's 60-second per-evaluation limit; the smaller retry completed without accelerating playback.
