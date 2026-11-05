# Credit Card Builder build handoff

## Structure

src.html starts from the kit starter and uses the kit frame, Curio.voice, tones, chimes, motion settings and Read. The first style block lays out a kraft desk, source viewer, index card, trail and mailbox street at actual viewport sizes. DATA contains the three fictional projects; CREATORS contains nine individual stories and two writing teams. evaluate is a pure ordered rule table. The rest renders sources, fills persistent slots, manages token-cancelled trails and saves cards and earned postcards.

The editable source is src.html. credit-card-builder.html is its generated offline bundle. tool.draft.json stays at stage built. No voice recordings were made. voice/lines.json lists the eight fixed lines using bright-teacher, Autonoe; browser speech is the kit fallback. There is no family engine.

## Tricky parts

- Building accepts every source chip into every slot without judging. The trail is the only correctness test. First matching rule wins, including an illustrator in the author slot before other missing fields.
- The book shelves each have three matching titles, three books by the author and two matching editions. A missing web date can still find the page with a version-date reminder. A non-date chip cannot. The Moon page offers today's date in America/Denver. jonasberg is accepted for Jonas Berg only on the Moon photo.
- Opening or editing a piece makes its card available for testing, even if it remains unfinished. Initial Book is selected but not made until opened or edited. Card made is presence, not correctness. Found tags are invalidated by edits. Previously earned postcards remain and are deduplicated by project-piece key.
- Every trail control stays live. Back, modes and projects increment a generation token; sleeping async steps cannot later revive the cancelled trail. A piece tag cancels the sequence and immediately shows that card's ending.
- Panel buttons and slots are persistent nodes. Fills do not rebuild source chips. Keyboard order is panel, source chips and page arrows, then piece tags. Explicit focus restoration uses preventScroll.
- Progress uses ccb-progress inside try/catch. Stored values have type and length guards; found tags are re-evaluated. Start over clears all projects and postcards only after Yes.
- Compact slots deliberately ellipsize long values with the full value in title and aria-label. The live credit line retains its full text in a bounded text scroller. The undated date chip sits inside the Date field. At shorter heights, Test, Clear and the footer's Start over share a visible action row. On phones the source stacks before the card.
- The No credit switch changes the mailbox art and shows a miniature project with an unknown credit. Its control comes first in creator details at tight sizes. Creator stories may scroll below it.

## Open questions and build decisions

The spec has no explicit open-question list. These conflicts were resolved using its stated direction:

- The art section requests local FLUX, while the owner explicitly requests the image tool. All 23 assets were generated with the built-in OpenAI image tool. Two mailbox poses were redrawn from the original closed mailbox to preserve the same design. No people are pictured.
- The text names nine individual creators plus two writing teams but also asks for nine mailboxes and two team cards. Nine physical mailboxes represent the nine individuals. The two teams have group cards that show their own earned postcard status. The nine borrowed pieces have nine distinct recipients, including those teams. Illustrators Leo Brandt and Omar Haddad have stories but earn no postcard from borrowed book text.
- The interaction paragraph requests a one-second Motion off trail, but STANDARDS and POLISH say motion changes movement, never time. Each card remains three seconds with Motion off, nine seconds total. Calm shows the ending immediately and holds it without flight.
- The report is written only after checks finish, following the owner's explicit stop instruction. Working evidence and draft report notes stayed in Scratch rather than creating an early report.

## Art

Every art token is used. Nature photos are realistic; covers, books, shelf, reader, postcards, mailbox poses, tool icons and street share a warm painted style. Prompts and provenance are in art/prompts.json. Raw originals stay in art/raw. Native transparency in the two mailbox redraws is preserved by disabling another chroma-key pass for those assets; rekey still sizes and encodes them. Their native_alpha and revision fields explain this.

## Verification artifacts

All evidence is in S:/CurioClass-codex/_scratch/credit-card-builder:

- numbers.py and numbers.json independently count shelf identities, editions, the art total and trail duration.
- core_checks.js and core-results.json enumerate 78,783 complete card combinations and every ordered failure branch.
- interaction_checks.js and interaction-results.json check 371 fills across 15 source views, immediate cancellation, tag jumps, Read and the access-date chip.
- project-0-complete.json through project-2-complete.json record held-click complete projects, all nine successful trails and nine postcards.
- storage-results.json records reload and confirmed reset; keyboard-final.json records a keyboard-only author fill.
- voice-two-second.json records held taps at a two-second pace. Found events repeat; Read interrupts immediately. How lines are keyed through V.heard and the kit's once-per-load queue.
- read-priority.json holds Read across automatic trail transitions: zero automatic hushes while the trail reaches its third piece. Automatic transitions drop stale queued lines and only hush a playing event; they preserve an active Read. Explicit Back, mode changes and reset still stop it.
- early-frames, functional-frames, late-frames, size-frames and more-frames preserve build checks and fixes. The latest targeted frames supersede earlier defects. feel-comparison.png places this tool beside Snowy Mail Route; Beat Lab was also opened and inspected.
- static-results.json records contrast, exact bundle size, all 23 art tokens, source readability and no external resource or network API code.
- audit contains the one final mechanical audit and its frames. Its dispositions are in codex-report.md.
- lead-frames and lead-*.json repeat only the affected page measurements after audit fixes. All target, below-fold, overlap, hidden-text, clipped-text, hint and scroll-choice arrays are empty at those ten checked views. final-frames includes the longest wrong credits, mailbox restoration and storage-write failure. proof-frames and matching JSONs check the shipped source's full rule table, every chip fill, keyboard use and quick re-taps.

## Engine changes wanted

scripts/art.py, main: preserve an already meaningful alpha channel rather than passing it into cut_out as if its transparent border RGB were a chroma key. Dark mailbox interiors were incorrectly removed when transparent pixels had black RGB. The two redraw assets work around this by retaining native alpha through the normal --rekey sizing path. No shared file was edited.

## Scope and next work

Build only. No commits, branches, deployments or polish round. The required bar bundle commands regenerated ignored reference HTML bundles outside the requested two folders; no reference source files were changed. All authored source, art, notes, tests and browser artifacts are confined to this tool and its Scratch folder. This exception is recorded for transparency.

Cold review can use the saved rule, interaction and frame evidence. Recorded narration remains optional follow-up. See codex-report.md for audit leads, remaining limitations and process cleanup.

The full audit completed within its 40-minute cap. Changes after its frozen bundle were confined to its layout/voice leads and the final edge cases described above, then checked with targeted frames and the audit's page-measurement code. The full audit was not repeated. A same-mode or same-project re-tap now preserves an in-progress welcome instead of hushing it. The source's rule table did not change.

## Cold review changes

Cold play covered all three projects before reading this handoff or the builder report. The review evidence uses review-* names in the same Scratch folder; the builder evidence above describes the earlier bundle.

- Trail endings now hold for the longer of message-reading time or event-speech time, using 1400 + 75 milliseconds per character. Flight takes 1700 milliseconds first in either Motion setting. This supersedes the nine-second duration above: readable teaching feedback and uncut voice take precedence under POLISH/STANDARDS. Piece tags still jump immediately and Back still cancels immediately.
- Card-slot and access-date taps during a trail return to the source before editing. Start over stops the trail before asking for confirmation, so no hidden run changes cards behind the dialog.
- Team cards track No credit with a locked status and aria-pressed, then restore the earned status when another creator is selected. Ad failures refer to the actual ad generically, rather than calling every ad a sticker ad.
- Web/photo trails now show a page index and photo contact sheet in the route. Compact readers, mailboxes and postcards leave source labels readable. Shelf readers sit below identifying labels.
- cc-reader-stuck was redrawn with built-in imagegen from both existing reader poses, then processed with art.py --rekey. The saved prompt and revision are in art/prompts.json. All 23 original asset roles remain in use.
- Audit states now include a successful photo ending, a team with No credit and recovery through an active slot during a trail.

Independent review checks: 78,276 chip combinations, 312 slot fills, all shelf counts and nine contrast ratios passed. All nine saved postcards survived reload; confirmed Start over removed progress. Keyboard-only entry and Sound-off Read worked. Five No credit activations spoke its how line once; five explicit stuck tag jumps each spoke their event. Automatic Found events completed three times without cuts.

The final review audit and its dispositions are recorded in codex-review.md. Fixed narration still uses the browser fallback; no clips were recorded. No shared files or other tool folders were edited and no commits were made.

The cold review audit completed once within its 40-minute limit, with 12 expected leads: the confirmation modal covers the background hint, and 11 first taps correctly skip an overridden or stale welcome. All eight sizes, states, Motion off, focus/Enter checks, repeats, quick taps and resize interruptions were clean. No audit-confirmed code repair was needed. Its 72 frames and audit.md are in _scratch/credit-card-builder/review-audit. codex-review.md records the dispositions and remaining spec ambiguities.
