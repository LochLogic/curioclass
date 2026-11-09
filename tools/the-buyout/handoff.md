# The Buyout build handoff

## Structure

src.html derives from the kit starter. It contains responsive scene CSS, persistent controls, a pure market model, then the application. It uses kit:curio, kit:theme-912, Curio.voice, Curio.tone and the kit Motion, Sound and Read controls. No family engine exists for this market. The generated offline file is the-buyout.html. tool.draft.json remains stage built for the next cold review.

The editable source is readable and uncompressed. Scratch includes assembly fragments, image-path provenance, raw number checks, browser test scripts, audit evidence and a contact sheet. Rebuilding from scratch fragments is a build convenience; future edits can go directly into src.html.

## Tricky parts

- market uses unrounded logit probabilities, distinguishes all shoppers from shares of sales, and aggregates concentration by owner. One lab costs once per owner; fixed costs apply to each brand. Research advances after a committed quarter, for sale in the next one.
- Rivals post their sequential best responses once per quarter. Preview never repeatedly reprices competitors while the student slides Price. Buyout choices apply to all brands.
- A lab's research points belong to its lead firm. On breakup, the divested owner keeps the existing model but builds its own research progress. This matches the spec's calculation scripts and preserves the intended unequal Q8 models after the split.
- Market results update immediately. The crowd is a largest-remainder illustration of 20 figures, each about 5,000 shoppers. Crowd motion never blocks controls. Play to the end remains live; mode switches pause it. Each run is retained separately.
- Remedy firms are deterministic. All defaults and the cap sweep use the same best-reply solver. Real case cards provide historical precedents, not causal estimates for the model. Changing a cap can change the view rankings.
- Compare marks require four played quarters per run and exactly three buyer measures. Ratings teach with feedback and have no correctness score. Switch evidence requires all ratings and a performed test.
- Memo uses three visible leaves to avoid a scrolling panel. The check verifies reason fit, different opened remedies, both inspected views, two current evidence chips including a ledger chip for the first remedy, and an explanation of at least 12 words with eight distinct words. It explicitly does not grade the argument's quality. Editing invalidates a successful check and Save rechecks everything.
- Saved writing is restored as a draft. Evidence is re-earned on a fresh run; stored values never confer completed status. localStorage failures are caught. The privacy statement appears beside Save.
- Voice metadata requests news-reader. No recordings were made because this is Build only with an explicit no-recording instruction. The kit falls back to browser speech, so the bank's exact timbre is not guaranteed.

## Open questions and build decisions

- The sole listed open question is settled in the spec. Retained the default clash: Buyers' view puts Block it first, Everyone's view puts Do nothing first. Kept the Williamson note and critics, with no extended horizon.
- The art paragraph says 14 plus 6 people images but names 19 assets. Made all 19 individually: shelf, six cartons, six shoppers, old charger and five remedies. Every shopper has people: true. The owner explicitly requests the image tool, so these use OpenAI gpt-image rather than the older Gemini wording.
- CODEX-BUILD and the user require painted art, overriding BUILD's old Do not draw art sentence. All drawings are newly generated and credited. No placeholders remain.
- The spec explicitly requests load focus on Price, while BUILD's wave lesson says nothing takes focus on load. Followed the more specific spec with preventScroll; cold review should retain this documented exception or settle it.
- The stated 896px stage plus 470px panel exceeds 1366px once gaps are included. The desktop split is approximately 66/34 with the panel inset inside its width.
- At small sizes the non-buyer Compare measures fold away while the five buyer rows remain. Memo uses three leaves within its required Memo page. This preserves 44px controls without a scrolling choice panel.
- At 680x425 the three Compare rating groups also page through Rivals, Buyout and Buyers, advancing to an unrated group after a choice. Group tabs preserve access to previous ratings. Small mini shelves abbreviate names to a symbol and initial and show watts; complete names are in tooltips and image alternatives. The main shelf keeps complete labels.
- At short heights a memo check replaces the editor with its complete six-part result list. Edit explanation restores the editor. This avoids clipping a failed requirement below the fold.
- The Compare welcome originally names Switch test before it is enabled. Reworded it to name the three rating groups; a separate how line names Switch test only after all ratings exist.
- The cap outcome retains the buyer-gain chart. Its ownership strip adds a coral cap line, quarter prices and falling stars, keeping price and dollar buyer gain on separate scales.
- The literal USB-C case phrase any charger works overstates universal power compatibility. Kept the specified dates and port standard while using the narrower phrase the standard opens the charging port. Teacher notes clarify power requirements.
- Exact total shopper counts differ by one or two from sums of rounded quarterly references. Display sums of unrounded units. The Switch test sends 8,032, not 8,033, to rivals. Numbers and differences are documented in the report.
- At a two-second tap pace, simultaneous launch announcements cannot all finish before the quarter changes. Launch sequences now interrupt older welcomes and start immediately, then drop remaining stale lines when the quarter moves on, as the event validity rule requires. Visual watts update immediately. The report records the actual logs rather than claiming all launch speech finishes.

## Sensitivity

The six individually painted shoppers include varied ages, skin tones, clothing, body types and an older woman using a cane. They are ordinary shoppers with equal agency; nobody is tied to a particular purchasing outcome or moral category. The contact sheet is _scratch/the-buyout/art-sheet.png. A fresh reviewer should inspect people art for anatomy, representation and respectful portrayal before shipping. No cultural identity is asserted. The historical cases concern economic regulation, not a reenactment of personal harm.

## Engine changes wanted

None. All work uses the current kit without edits.

## Build QA disposition

The single full audit completed within its forty-minute budget. Its original snapshot is retained in Scratch. Focused fixes address Read's width, stable header widths on Sound toggles, ownership ribbon wrapping and paint order, 1280x720 table/chart spacing, narrow regulator labels, Finish focus, and an explicit textarea accessible name. Active mode taps now preserve speech. Short memo results retain the privacy line. The hosted phone checks use drive.py because the audit's iframe context probe failed; this remains a documented audit coverage gap, not a claim that the automatic phone pass was clean.

The system python command is a LibreOffice launcher. It left native background host children after parent shutdown. Cleanup queried normal command-line metadata, matched only drive.py the-buyout --host 8785, and closed those ten children. Other processes were excluded. host-cleanup.json and final-manifest.json record this. Earlier host contention is a plausible cause of the audit's automatic iframe failure. All three used ports were verified closed at completion. Future host helpers should launch the native Python executable directly and keep its process handle.

The user required stopping immediately after the final codex-report.md write. A working report draft was kept in Scratch during checks, then placed in the tool folder only at completion. This takes precedence over the build brief's early-report-file timing.

## Next handoff

Cold review evidence and remaining limits are in codex-review.md. No commits were made. The tool remains stage built for the separate blind Refine lenses.

## Cold review repairs

The cold reviewer played both runs, Compare, all remedies and the memo before reading this handoff or the source. Review evidence uses the review-prefixed files, cold-frames, size-before, cheat-before, cheat-after and post-frames in Scratch. The final review report supersedes the build's outstanding findings.

- Memo length now excludes isolated alphabet letters except a and I, closing a twelve-letter padding bypass. The check still explicitly evaluates structure, not prose quality.
- Combined model launches have one fixed announcement per quarter, including both firms when they share a launch. All combinations live in L and voice/lines.json. This retains every factual event at a two-second tap pace without holding up play.
- Switch results interrupt obsolete how-to speech and then offer the marking how-to while it is relevant. The result tracks visualize retained buyers, rival switching and going without. Motion off removes the reveal and retains the figures.
- HHI feedback identifies the equal-share starting point for the 7,500-point example. The BT card distinguishes Littlechild's proposed RPI-X from the government's later choice of three percentage points.
- End-of-Buyout hints name Rivals or Compare. If research reaches its maximum under keyboard focus, focus moves to Next quarter with preventScroll.
- Read's fixed hints now belong to L and the voice inventory. Compare names only enabled Finish buttons and directs students to Regulator after three marks. Its 375px layout keeps all five buyer rows in view after the Switch result.
- At short landscape heights, Memo uses one navigation row with a Remedies return button. Duplicate Evidence instructions are omitted because the hint already says them. This keeps the maximum eight chips and privacy line visible; focus moves off a hidden panel tab to the current memo leaf.
- Redrew remedy-standard with the built-in image tool. Its three matching USB-C ports and one cable connector now face the viewer at card size. Prompt/provenance are in art/prompts.json; the prior raw image is preserved only in Scratch.
- Final audit completed inside forty minutes, with eleven leads. Eight load-focus notices follow the explicit spec; two missing welcomes follow BASELINE rule 16. The confirmed 375px ownership overlap is repaired by giving Buyout's shelf thirty-two more pixels and separating the products from its banner. No full audit was repeated.
- Final focused craft repairs preserve speech on repeated active memo tabs/leaves, use solid/dotted/dashed chart patterns, and keep evidence/marking how-to lines consistent with completed prerequisites. Evidence with Compare chips but no first remedy now directs the student to Reasons.
