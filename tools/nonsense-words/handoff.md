# Handoff: nonsense-words

## Structure
src.html starts from the kit starter and inlines the supplied bank, grouped exactly as words.txt. CSS lays out the quiet parchment page, deep blue border, header modes, kinds, reading area and actions. The JavaScript owns deck order, marks, flags and deadline checks. Curio.voice owns instruction playback; kit Sound, Motion and Read are used directly.

The public __tool hook exposes state, setMode, allLines, vlog and vq for verification. state.started and state.wordStarted use performance.now(). tick runs every 100 ms and also checks visibility changes. Every score input independently checks the Challenge deadline.

## Decisions and brief conflicts
- The owner's plain Look wins over the general rich-art/gameplay brief. Two assets only: quiet parchment and one small still quill. No people or characters; no motion or audio response to ordinary reading/scoring.
- First visit opens Explore. Later visits restore the remembered mode; Practice and Challenge stop at a ready screen until Start. This reconciles Explore opens first with remember last mode.
- The explicit instruction-only voice and prohibition on reading words win over generic K-2 narration of every fixed line. Browser voice is approved by the spec; twelve instruction lines, including Read hints, are prepared for voice night. Read never reads a target word.
- Metadata uses the spec's explicit driver students despite the generic K-2 teacher-driver contract. The notes and ready screens make the adult/partner support role clear.
- Practice and Challenge have a ready screen to avoid starting a clock while a teacher selects kinds or session length. Kinds and length are locked during a run; mode buttons can leave the run.
- No open-questions section is present. At least one kind stays selected; flags are per word and shown within current kinds, so overlapping mixes preserve flags. Best scores are per kind mix for comparable results.
- A Challenge timeout reports unreached words separately. Practice these covers attempted Not yet and skipped words, as specified. The denominator remains 30.
- Explore target words appear one at a time. The requested flagged picker and end-screen lists intentionally contain multiple words. They never speak the words.

## Bank for owner approval
The bank is preserved without additions, removals or spelling changes. The number check found exactly 200 unique entries and the specified group counts. Owner review is still needed before shipping.
- vape is a real modern English word, and fab is a familiar informal real word.
- nife is a sound-alike of knife, despite the bank's stated sound-alike filter.
- pam reads as the name Pam; names may or may not count for the owner's filter.
- fode: possible non-English rude-word concern, unverified during this build. It remains in the owner-supplied bank as instructed; flag for the owner's multilingual review.
- CVCe items ending in ge can invite soft-g versus hard-g interpretations; u can have more than one long-vowel reading. A reading partner should accept the taught plausible decoding. This tool supplies no pronunciation key.

## Sibling layout
Sight Words had only spec.md and words.json when this build began. Its source and handoff appeared during verification and were read. Both tools now share the parchment/blue stationery pattern and palette, quill and title at upper left, Explore / Practice test / Challenge, Sound / Motion / Read, centered plain word, large scoring controls, flags and privacy footer. Compact landscape places this tool's navigation and secondary controls alongside one another. The sibling needs its separate list picker and overlap tag. Both tools made their own assets. No sight-words files were changed.

## Art made
Built-in image_gen made parchment and quill. Prompts: art/prompts.json. Raw originals: art/raw/parchment.png and art/raw/quill.png. Final assets: art/parchment.webp and art/quill.webp. No redraws; no people. Each finished image was inspected. The quill is intentionally small and still.

## Art still to paint
None.

## Engine changes wanted
None.

## Verification
See codex-report.md for completed checks, exact evidence and limitations. No git commits, no changes outside this tool and its Scratch directory, and no polish round.

## Build verification repairs
The one mechanical audit found a compact-layout hit-area problem: the empty secondary-actions container covered Start after the landscape columns were widened for review controls. CSS now hides that container when every child is hidden. Real held-click checks cover Start and scoring at 680, 800 and 1000 widths, plus the compact results-to-review path and perfect run. Selected controls also keep white-on-blue contrast while hovered. The report distinguishes the original audit leads from these targeted repairs; no second full audit was run.

Closing a first-tap Flagged dialog now retries an unheard Explore welcome, once the reading controls are visible again. Re-tapping the current mode preserves the session and its instruction rather than resetting it or cutting speech. Targeted held-click checks cover both paths. The public setMode hook still intentionally resets for verification and internal transitions.

Rapid kind changes refresh the deck and hint without hushing a still-valid generic instruction. The audit's three quick-kind speech-cut leads were repaired this way. A six-tap held-click check toggled each kind off/on at 0.7-second gaps, restored all 200 words and logged one uninterrupted Explore instruction.

## Cold review repairs
Compact utility controls now keep the grade-band 60 px target. Explore instructions name enabled controls at the first, last and one-word review boundaries, with matching voice lines. Mode buttons carry the group role for complete automatic audit discovery. Practice results name the attempts and review count. Parchment is painted once with cover rather than visibly tiled; both original art assets are preserved. The owner's quiet Look and sibling structure remain controlling. See codex-review.md for independent evidence and remaining owner bank approval.

The audit frame at 680x425 revealed the perfect-result panel clipping the personal best. The compact layout now keeps the wide success banner, score and best visible by omitting its redundant second heading and tightening banner padding. The perfect audit state now explicitly keeps #best. Four additional fixed instruction hints are registered for Read and voice night; marking instructions use words without spoken check/cross glyphs. These are checked by focused follow-up shots, not a second full audit.

Additional bank candidates from cold review: include nog, fid, neg, dob and nesh in the owner's existing real-word/sound-alike review. These are candidate concerns, not a new pronunciation key or word-list edits. The complete original bank remains untouched.

The audit Flagged/Enter path cuts an Explore welcome by reopening the modal immediately after Close. The tool now rearms just that interrupted welcome through the public V.said set, so the next Close speaks it completely. A fully heard welcome remains silent on later dialog visits. The modal itself stays quiet, as specified. A modal left open correctly withholds the instruction for the covered reading controls.

## Cold review verification
The single full review audit completed with one confirmed modal-welcome lead. All 87 frames were inspected. Post-audit checks passed for the modal recovery, all four added Read hints, the real 375 px marking path, five complete cheer events, and compact success results. The final 680x425 panel has zero vertical scroll and a fully visible best score. Thirty-six functional assertions passed. The original bank matches the cold-review source snapshot exactly. Full evidence and remaining owner approval are in codex-review.md and _scratch/nonsense-words/review-verification-summary.json.
