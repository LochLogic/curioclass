# Globe Theatre Stage build handoff

Build only. No commits, shared edits or polish round. All work is in this tool and its matching scratch folder.

## Source map
src.html starts from the kit starter's structure and uses kit:curio and kit:theme-912. The local Bard interfaces, state management, production tableaux, rendering and listeners occupy readable sections in the inline script. scenes.json is loaded through the bundler's json: token and contains the public-domain excerpts, glosses, keys, reasons, evidence references and directing decisions. ART is the single map of bundled images. All 27 assets are referenced there.

The central stage uses real pixel layout around a 16:9 painted set. Figure positions use normalized floor coordinates and 30 to 38 percent image-height scaling. CSS transitions retarget immediately, with no movement queue. Delivery scores expose their marks in visible text. The source panel has its own scroll and a compact landscape drawer. Choice navigation remains mounted when ruling state changes, so it keeps focus.

Setup cards now sit before the excerpt. Name tags occupy a separate layer so front figures cannot cover them. Mr Hale remains as a faint, explicitly outside cast reference before his entrance and after his exit, preserving the requested five-figure scene without implying that he witnesses the final exchange. The hand tableaux use the specified standing/kneeling cutouts; they are snapshots rather than complete gesture animation.

Short windows use a native choice dropdown rather than a hidden scroll list. Compact framing crops unused architecture while retaining actors and their name tags. Phone production tabs use the measured header height so they remain pinned without covering the header. Read my production stays beside the Your production heading, including when the statement field needs panel scrolling.

A second review button follows the statement. Opening a scene or changing mode resets document scroll, fixing the far-down-picker entry case. The completed audit predates these scoped fixes; targeted final frames verify them. The audit was not rerun.

At 760 and 375 wide the required stage, score, script, then work-panel flow needs document scrolling. This conflicts with the standing rule that all frequently used controls and the hint stay in view. The build keeps the spec's explicit narrow flow and records this unresolved layout limitation rather than reducing the painted stage to a tiny thumbnail.

Compare stores separate rulings for all twelve productions. Linked evidence is a claim recorded by the student, never an automated judgment of its quality. Our key is revealed only after Check. License strips show the student's classifications and the data-derived key separately. Direct stores three independent decisions, linked lines, custom notes and a director's statement. An option change clears that decision's evidence. Output identifies unfinished fields rather than implying completion.

The evidence gate checks presence, not relevance. An unrelated line can be pinned, as the spec permits competing interpretations and forbids scoring them wrong. The count and strips explicitly record claims rather than certify their quality. A future semantic correctness gate would need a spec change; do not quietly restrict evidence to our suggested references.

## Open questions resolved
- Delivery is visual only. No play text is narrated, and there is no style-dependent recording key or engine change.
- Keep Trifles as the guest company, satisfying the American dramatist requirement in the same comparison tool.
- Use on-page and teacher content notes for Trifles and Shrew. No parent preview gate; no dead bird is painted.
- Retain all 19 people cutouts, including Bianca and the Widow. The current brief and baseline permit Codex people art, overriding the spec's older Gemini/Cory deferral.
- The guide asks for an early report stub, while the owner's direct instruction says to stop once codex-report.md is written. The report is therefore written once, after the build checks.
- The Macbeth endpoint initially looked inconsistent, but the source confirms exactly 17 verse lines through "Thus to mine eyes." The bell direction is retained after the cut and before the final three lines. No extra soliloquy is added.
- Shrew's contradiction check needs the exit direction omitted by the shorthand excerpt outline. That direction is retained immediately after the second cut, before the last two comments, so the student can link it.
- Excerpt counts are approximate: line wrapping and separate directions change the display count. Labels explicitly say excerpt line numbers, not edition numbers.
- The screen description says three to five choices per production, but the explicit Trifles content lists two, two and three. The build follows that content and its seven-choice key.

## Sensitivity
Grade 12 literary material includes suspected murder, an animal's death, marital power, cruelty and possible sexual wordplay in honest/nunnery. No dead bird is pictured; the closed box carries the implication. Shrew interpretations are framed as contested readings, not advice about relationships. A fresh cultural/people review in the next cold review should check respectful treatment, costume accuracy, skin-tone range, anatomy and the distinction between stage actors and historical character identities. The cast is adult and non-caricatured. No external contact or publication occurred.

## Art
All 27 images were generated during this build with the built-in image tool. Every actor asset has people:true and every asset drawn_by:codex. Raw originals are in art/raw; finished art uses the required art.py --rekey pipeline. The full contact sheet is in _scratch/globe-theatre-stage/art-contact.jpg. A horizontal light-dagger redraw corrects the first candidate's upright composition. Recorded voice remains intentionally absent; browser narration is the build fallback.

## Engine changes wanted
- Missing file kit/bard.js: supply Bard.Script, Bard.Gloss, Bard.Stage, Bard.Score and Bard.Store with the spec's interfaces. The tool currently implements them locally because shared edits are forbidden. Promotion should be decided after real reuse; do not silently replace this implementation without matching line selection, pinning and depth behavior.
- Missing docs/families/shakespeare.md: document the implemented API alongside the actual shared engine when it exists. The tool's spec currently supplies the only full family description.
- Bard.Stage.place: support cutout aspect ratio and instantaneous retargeting, 300 ms moves, reduced motion and anchored name tags; this build's local implementation does so without queuing motion.

## Evidence and next review
Scratch contains source snapshots, numbers.json, image provenance, contact sheets, held-input frame batches, functional checks and the single mechanical audit. Read codex-report.md for the final observed results and unresolved limits. The next action belongs to the separate cold review, not a builder polish round.

The broad functional pass recorded 944 assertions before the final scoped repairs. Subsequent checks cover Direct delivery, moving props, setup placement, character tags, hand poses, scrolled scene entry, copied output, actual reload, keyboard navigation, gloss sourcing and phone dialogs. audit-dispositions.json addresses every reported lead, including allowed first-tap welcome cuts under baseline rule 16.

The final native CDP key check selected excerpt lines 1, 43 and 42 with Home, End and ArrowUp, with no exceptions. The final gloss check opened orisons, prayers and its Folger source with no exceptions. Earlier synthetic-key batches timed out; their partial artifacts remain in Scratch and are not counted as passes. All owned Chrome profiles were closed, and host.html was removed.
