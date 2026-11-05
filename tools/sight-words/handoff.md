# Handoff: sight-words

## Structure

src.html started from the kit starter. It embeds the existing words.json with the json token, unchanged. The source has parchment and blue-border CSS, picker, reader, ready screen, results, flagged dialog, then deck and timing logic. Curio.voice owns the instruction queue; Curio owns Sound, Motion, Read and the perfect-score chime. There is no family engine.

window.__tool exposes state, setMode, allLines, vlog, vq, pool, tick and data. Practice uses wordAt, Challenge uses startedAt, both from performance.now(). The interval is 80 ms, visibility changes check the clock, and every score input checks the Challenge deadline before accepting a mark. A resize remeasures the current word from its normal font size so long entries fit on phones without splitting.

The mode navigation carries role group so the mechanical audit can discover its buttons. That attribute was added after the single audit's initial discovery, so the completed audit's automatic walk covers the picker; explicit audit states and separate held-click checks cover each reading mode. See the report for this verification limit and the targeted compact-spacing repair.

## Decisions and brief conflicts

- The owner's plain Look wins over the rich-art and gameplay brief. Parchment and one still quill are the only illustrations. There are no people or characters and no motion near the word. Normal navigation and scoring are quiet. The perfect Challenge is the only celebration.
- No Open questions section exists in this spec. No unresolved teaching question was invented.
- Nonsense Words initially had only spec.md and words.txt. Its source appeared during this build and was read along with handoff.md. Both tools use the same parchment/blue stationery pattern, palette, quill at upper left, mode and utility controls, centered plain word, large plain scoring controls, flags and privacy footer. Sight Words needs a separate picker and overlap tag. Its two images were generated within this chat; no sibling files were changed.
- The spec explicitly requests driver students, so metadata follows it despite generic K-2 teacher-driver wording. Notes and instructions make the adult/partner role clear.
- The explicit instructions-only voice wins over generic K-2 narration of every fixed line. The word, overlap tag and review words are never spoken. Browser speech is allowed by the spec. Eight short instruction lines cover picker, modes, ready screens, review and flags; no recordings were made.
- The picker is always the first screen, with remembered picks, list tab, Mix and mode. The clock starts only after Start on the ready screen. Re-tapping the current mode preserves the current session.
- Multiple picks can span Dolch and Fry. Duplicate words in a combined selection appear once; source label and tag use the first occurrence in the fixed Dolch-then-Fry set order. This preserves the supplied capitalization, including I and Santa Claus. A list-tab change leaves picks on the other tab selected, and the selected count reflects all picks.
- Practice and Challenge always shuffle; Mix controls shuffling across the combined Explore selection. Best scores are keyed by the exact sorted set combination. Flags are per word and shown within the current reading deck.
- Practice Skip is separate from Not yet internally, and both are in review. End also includes unread words so an early finish does not lose them. Challenge Skip counts as Not yet; unread timeout words also appear in review, clearly labeled as words left.
- One-word-at-a-time applies to the reading display. The required end review and flagged picker intentionally list several words.
- The report is written last because the user's explicit instruction says to stop as soon as codex-report.md is written. This takes precedence over the guide's early-report workflow.

## Content and numbers

The supplied content is untouched. Dolch counts: 40, 52, 41, 46, 41 and 95. Fry has ten hundreds. There are 315 unique Dolch entries, 1,000 unique Fry entries, 273 shared entries, and 1,042 unique entries across all sets. The independent numbers script is in Scratch. Browser checks walked every supplied word and its tag with zero mismatches.

## Art made

Built-in imagegen created both assets. Full prompts and house style are saved in art/prompts.json. Raw originals are art/raw/parchment.png and art/raw/flourish.png. Final files are art/parchment.webp and art/flourish.webp. The parchment is a quiet pale texture; the quill is small and still. The art.py rekey pipeline sized both assets and removed green spill from the flourish. No redraws or people. Finished assets were visually inspected.

## Art still to paint

None.

## Engine changes wanted

None.

## Verification and next work

See codex-report.md for completed checks and audit dispositions. Scratch holds the scripts, frames and evidence. Browser speech was scheduler-tested with muted Chrome, not listening-reviewed. No classroom trial was performed. A cold review is next; no polish round or git commit was started here.


## Final build verification

One full audit completed with 13 raw leads. Compact word/tag spacing, compact results visibility and repeated-mode speech interruption were repaired. Three modal-coverage leads were accepted with frame evidence. All 65 audit frames were inspected. The full size sweep and audit were not repeated after repairs; twelve focused layout/state frames, three rapid-tap voice frames and a celebration-exit frame were inspected instead. The final bundle exactly matches the checked final Scratch fixture. host.html is absent and the build's Chrome and server processes were closed.
