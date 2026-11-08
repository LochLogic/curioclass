# Handoff: fallacy-field-guide

## Structure

src.html starts from the kit starter. The stylesheet lays out the cloth-and-paper field notebook, four habitat skins, field kit, guide book, writing slips and native dialogs. The script contains the species catalog, all 24 original specimens, a marked pure family block, state and persistence, Curio.voice, and DOM renderers. __tool exposes state, setMode, select, fx, specimens, catalog, allLines, vlog and vq for verification.

## Decisions and contradictions

- No tool-specific open questions. Shared decisions follow BASELINE.md.
- The spec requests local FLUX; the owner's explicit image-tool instruction wins. All 11 images were generated with the built-in image tool, copied into art/raw, and processed with art.py --rekey. None show people.
- BUILD.md says do not draw art, while CODEX-BUILD.md and the owner require it. The build-specific and owner instructions win.
- kit/fallacies.js does not exist, and the spec says there is no family document. A marked pure block implements the requested API locally; no kit files were changed.
- After two misses, correct calls remain study-only. This closes the every-option cheat while preserving retries and Show me. Attempts and revealed status persist through reloads.
- The guide's Confirmed state is sticky as specified, even if current sighting counts later decrease. The footer explains this.
- F10's no-staff claim is absent from the original fictional news-story context. The context now includes that detail from F10, so its fair-summary key can be assessed.
- F13's distance alone cannot prove a missed bus connection. Its note is understood as an attributed timetable judgment, as the supplied key intends. No real bus timetable or numerical travel calculation is implied.
- F23 is keyed to expertise offered as support; a dentist can have a valid personal movie preference. Teacher notes preserve that boundary.
- F15's field note mentions being good for you, but the text states sales and says millions cannot be wrong. Its intended Bandwagon key depends on reading an implied quality claim. Preserve this content issue for review rather than inventing a health claim in the specimen.
- The Make one species picker is a menu beside a plate. Its welcome names the menu accurately rather than asking students to tap a card that is not present in that mode.
- The Hasty generalization and Bandwagon questions are not grammatically yes-or-no questions, and Post hoc combines two questions. Small on-screen legends make the supplied Yes/No controls unambiguous: many/fair versus few/biased; popularity itself versus quality/truth; fair comparison accounting for differences versus sequence alone.
- Make one's test is explicitly a self-check, never an automated semantic grade. Arbitrary text and favorable self-reported answers earn no guide cards.
- The processing Python on PATH lacks numpy. art.py ran using its existing compatible local site-packages without modifying the environment or installing anything.

## Sensitivity

No culture, religion, hard history or people art. F3 mentions dentists, teeth and sealants; F12 mentions a broken wrist. These are fictional argument specimens, not health recommendations. The supplied expert-relevance example does not establish the truth of a treatment claim. Review the distinction between evaluating reasoning and judging people.

## Art made

Eleven generated plates and habitat assets, all people:false. Full prompts in art/prompts.json; raw originals in art/raw; final WebP files in art. No downloaded art or recorded audio.

## Art still to paint

None.

## Engine changes wanted

kit/fallacies.js, new module: promote the marked pure fallacies block only when the shared-engine baseline is met. Preserve spot, test and cards APIs, parameterized catalog/specimens, overlap threshold, and five-extra-word rule. The requested file is currently missing. Habitat rendering remains tool-owned until a real sibling establishes a shared need.

## Verification

Build-only evidence and remaining issues are recorded in codex-report.md. Scratch contains scripts, source-generation template, number checks, screenshot recipes and audit output. No commits or polish round.

## Cold review repairs

Practice-only successes now use their own event voice, not Logged. Choosing an already selected species preserves a logged sighting. Long marked writing stays inside bounded slip passages, keeping Field test it reachable. Field and writing tests speak the question and the supplied Yes/No interpretation; Read repeats the current question and instructions. Guide details include the student's saved marked specimen texts, lifting the collection's comparison payoff.

Audit-frame follow-ups keep the Legit prompt in the reserved hint instead of inserting a row, put compact comment avatars in the specimen header, move saved-specimen navigation above the guide's reading content, and restore side-by-side slips at 760 wide. Selected specimens explicitly say they are invented. These local layout/copy repairs are checked with scoped frames after the single frozen-bundle audit.

The phone was redrawn in ink and watercolor, with an opaque empty screen and a magenta-key cutout, and is turned sideways in wide habitats so the whole bezel is visible. An initial native-alpha candidate had an unwanted inner transparent rim and was corrected before acceptance. Existing magenta-key plates were reprocessed with despill. Voice manifest and audit states were updated. No shared kit files changed.

Content boundaries F13, F15 and F23 and the conflict between compact continuous-word selection and uniform 44-pixel word targets remain spec decisions, recorded in the cold review. The requested missing family engine remains tool-local under BASELINE rule 13.

## Cold review verification

The one review audit completed with exit 0 in 2062.4 seconds, with 98 frames. Its 2066 leads and their dispositions are in codex-review.md. No full audit rerun followed the narrow final repairs. The 12-shot scoped follow-up had no console errors; the main voice order, rapid-edit cancellation, stationary Legit kit, guide jump controls and phone practice path passed. The phone words clear their navigation by 22.9 pixels. Pure checks passed 529 assertions.

Bundle 1034.7 KiB, art 674.1 KiB, 48 prepared voice lines. Final bundle SHA-256: de8e2b4eb2256b717ef01fdae0d6c56e9736dd34b69667622066a5b7e9584529. Evidence and final-review-checks.json are under _scratch/fallacy-field-guide. All assigned ports closed; host.html absent. Further regression states are retained for the next reviewer.

## Build verification repairs

The single completed audit produced 777 leads, mostly repeated inline-word target sizes. Repairs were staged in Scratch while its original input stayed fixed, checked with focused browser shots, then bundled into this folder. final-stats.json in Scratch records SHA-256 equality with the verified repair bundle.

The Field tab now measures 44 pixels wide. Writing inputs have explicit accessible names and block labels. Writing hints advance from the eight-word requirement to marking, then to the enabled test. Native dialog close and Escape restore the current mode's hint. Active habitat and specimen tabs preserve valid instructions and work. Word tokens stay in single inline boxes so a hyphenated word does not acquire a misleading rectangle spanning two lines.

At 760 wide all eight guide cards fit. At 375 wide both ordinary writing slips and their marking controls fit above the fixed action bar; longer writing scrolls within the marked passage. Phone card art sits above its explanation. Species stamps retain their glyph and name when a sighting is reopened. Confirmation flips are consumed after the first reveal.

The remaining project-standard failure is the 44-pixel size of individual word targets. The continuous passage uses smaller inline words with a complete arrow-key and Enter alternative. The 375-wide Guide scrolls as its explicit one-card-per-row specification requires. See the report for the content ambiguities and the recorded build-scope exception involving ignored reference bundles.
