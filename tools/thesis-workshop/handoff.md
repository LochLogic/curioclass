# Handoff: thesis-workshop

## Structure

`src.html` starts from the kit starter. The CSS is organized as room frame, manuscript, chips, promise meter, evidence cards, paragraph, and responsive layouts. The single script owns state, persistence, the chip predicates, text lighting, saved theses, evidence, paragraph assembly, and Curio.voice. `content.json` is loaded by a `json:content` bundle token and contains complete source text plus character ranges and tags. Generated HTML is the offline deliverable.

The promise meter and the primary action stay fixed beside a scrolling work page. Prove pins its evidence picker above the primary actions, so choosing one quotation cannot bury the other choices under the new card. At small landscape sizes the chip labels shorten, with their complete wording retained in accessible names and titles. At portrait widths of 760 and below the Text and Bench tabs share the workspace; Text shows the lit count. Draft expands the paragraph and reduces the manuscript to passage ids; its phone Text tab still opens the full text.

`window.__tool` exposes state, mode and text changes, chip selection, meter and Because predicates, paragraph assembly, the voice inventory and `vlog` for review. Browser checks, count calculations, source snapshots, full-size frames, contact sheets and process wrappers are in `_scratch/thesis-workshop/`.

## Decisions and spec tensions

- Retained the complete mild ghost story for grade 10, as the spec leans. Teacher notes name its fictional drowning and graveyard material.
- Retained Frost's popular reading as N3. The four crossed passages make its evidence problem visible rather than hiding that reading.
- Preserved Frost's line 18 with `--`, as requested in Content. Saki's original long dashes also become `--` to obey the no-em-dash build rule. Words are unaltered; source whitespace and italic markers are normalized.
- Used the requested built-in image tool rather than the older local FLUX instruction. Both paintings have `people: false` and `drawn_by: codex` in prompts.json.
- Kept the spec's light writing room and its explicit palette. This is a mature writing instrument with no points or confetti.
- The brief asks for an early report, while the user's direct instruction says to stop when the report is written. Evidence was accumulated in Scratch; `codex-report.md` is written once as the final build action.
- Used the existing bundled bar tools for the required visual opening. Rebundling another tool would violate the user's write boundary.
- The exact prescribed Because predicates are word matches, so they cannot validate reasoning. They stay visible as non-graded nudges. Copied quotes and very short matching-word inputs receive a separate explanation prompt. Draft never awards an overall success score or badge. A crafted unrelated sentence can still match both words; a reader must judge it.
- “Workable or better” has no better category in the scope scale. Draft checks Workable; Too broad is not treated as better.
- Meaning's Any chip leaves the interpretation uncommitted. It says Pick a meaning and requires a concrete meaning before Use this one, rather than inventing fit tags for an unspecified interpretation.

## Persistence and revision

Only `tw.v1` is used for writing. All storage operations are caught; the session continues with a notice if access fails. Five snapshots are allowed per text and a sixth opens a replacement dialog. Evidence ids are unique and must be lit. A chip change removes evidence outside the new scope and clears the old contradiction response. Paragraph edits survive evidence changes, with a reconciliation notice. Clear removes both texts after confirmation and does not immediately recreate the key.

## Voice

Bank: smooth-narrator, Algieba. No recordings were generated, as instructed. Browser fallback supplies speech. Read speaks the current hint, never the literary text. The first completed topic-and-move pair starts the meaning instruction immediately so it is not lost behind the welcome at a two-second tap pace. Scope events use event narration; how lines use heard checks and state validity. Mode changes hush stale speech.

## Sensitivity

The story is an early twentieth-century English fiction with a fabricated tale set near the Ganges, the historical phrase “pariah dogs,” and reference to a cemetery. Review whether preserving the original wording with the teacher-note context is appropriate. Do not present Vera's invented account as factual information about India. The tool touches fictional fear and death, not health guidance. Paintings are empty landscapes and an empty room, with no people.

## Engine changes wanted

None. Shared kit files are unchanged.

## Audit helper limitations

The single audit's `scripts/audit_tool.py` mode discovery looks only inside a `header`. This tool's top mode ribbon is a sibling of the title header, so automatic mode discovery misses it. The explicit evidence and paragraph states, the separate held-input writing walk, and the phone frames cover those modes. A future helper change could include `nav.seg[aria-label="Workshop mode"] button` in `MODES_JS` without changing the tool's layout.

The audit's phone context lookup failed on its own host. The independent 8785 host run successfully inspected the actual 375-pixel iframe and recorded zero console errors and no sideways overflow. The final report distinguishes those results from missing audit coverage. State-size labels in audit-states.json use the helper's exact `375x812` spelling.

## Art still to paint

None. Two watercolor headers are generated, inspected and bundled. Raw images and prompts are retained. There are no people assets.

## Build verification and next review

The independent content/browser run passed 1,105 assertions. The single mechanical audit completed with 30 pre-repair leads and no exceptions, infinite motion or resize lockups. Its tool findings were repaired and verified through focused held-click and frame checks. Repaired Prove choices and the focused Because field fit at 680, 1366 and 375; mode transitions retain focus; repeated selected-mode taps do not cut speech; rapid chip taps keep the final state synchronized.

The full source, generated bundle and evidence hashes are in the Scratch build manifest. Chrome ports 9980-9983 and server 8785 were checked closed, and tool host.html is removed. On this Windows session taskkill left three test-host processes alive; stop_host.py identified only command lines for this tool's exact host invocation and terminated them. The reusable Scratch host wrapper now terminates and waits on its own process directly.

The next step is the separate cold Build review requested by the owner, not another polish round in this session. Review the quality of actual student explanations, the compact scrolling tradeoff, authored voice recording when authorized, and the sensitivity notes. The lexical checks intentionally remain formative word nudges and cannot be a semantic assessment.
