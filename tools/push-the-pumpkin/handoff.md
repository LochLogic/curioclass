# Handoff: Push the Pumpkin

Build only. No commits or polish round. Writes confined to this tool and its Scratch folder.

## Structure

The kit starter supplies the document, settings and narration. Tool CSS lays out a real-pixel canvas beside a picture-card panel. Canvas drawings use generated paintings plus precise code posts, arrows, flags, trails and buckets. Accessible HTML controls overlay the comparison lanes and barn placement spots. Controls use tap placement and pointer drags.

The three state machines live in `src.html`: Push keeps its eight flags; Find out retains five test objects and honest first predictions and comparisons; Barn retains each level's design, run snapshot, original verdict and analysis answer. The rule model is separate from drawing. Editing during a roll changes only the next design, not the run snapshot.

`Curio.voice` owns the queue, Read and sound settings. The voice manifest selects upbeat-guide. No audio was recorded in this build. Browser speech is the fallback. Scope is mode plus test or level. Mode changes cancel obsolete speech; how lines use the kit's heard set.

## Spec differences and decisions

- The named asset list has 17 non-person assets plus six Jo poses, 23 total. Its printed total says 19 plus six. All named assets are included.
- Noise plus the stated roll-time formula gives 1.005 to 2.445 seconds, rather than 1.05 to 2.4. Follow the formula, which remains below 2.5 seconds.
- The first-piece rule applies to obstacles after a Start ramp has changed speed. Otherwise the required ramp-and-board level cannot work. Exact enumeration matches all three design counts and every level-three outcome count.
- A random no-repeat search with two successes has expected first success at (n + 1) / 3: 7.667 and 15 tries for levels two and three, not 11.5 and 22.5. No such statistic is displayed to children.
- Open questions: the spec lists none. Jo has medium brown skin, curly dark hair, a mustard jacket, teal overalls and boots, consistent across six poses. The fresh representation check and owner contact sheet are retained in Scratch.
- The current build brief explicitly permits Codex-generated people and requires its image tool. This supersedes older Gemini-only and do-not-draw wording in BUILD and ART.

## Sensitivity

No cultural, Native, religious or hard-history content. Jo is a fictional child. Check the six people-marked poses for anatomy, respectful representation and consistency before publication.

## Engine changes wanted

None. Shared kit, scripts and docs were not modified.

## Cold review changes

The ghost comparison now reaches the same no-piece endpoint as the original run. Uphill ramp pieces are mirrored in both the live HTML spot and the canvas result. The Barn opening is aligned to the door post and sized so the short ball stays visibly outside it. The test wall now shows the learner's picture choices and two recorded stop flags, rather than relying on text alone.

Jo's pulling pose was redrawn with a low backward grasp, matching the original child and painted style. All six people cutouts were rekeyed with enclosed-key cleanup to reduce their colored fringe. These assets remain people-marked in prompts.json. See the cold review report and review evidence in Scratch for independent checks and any remaining limits.

The cold review's final audit did not finish: Chrome DevTools timed out before the first size and no audit.md was saved. Independent all-size, design-model, cheap-pass and voice checks completed, but the full mechanical gate and all resize/voice edge cases remain unverified. See Scratch review-audit-failure.txt. All review Chrome endpoints and host 8745 were closed; host.html was removed.

## Review next

See codex-report.md for measured checks, source links and any limitations. Record upbeat-guide narration in the later media workflow. This build has no classroom observation claim.

## Verification details

Scratch `check_model.py` compares all 76 JavaScript designs with an independent Python model. `functional.py` walks all five tests and three levels using held pointer clicks, with intentional wrong comparisons, the unfair plan, wrong verdicts, a wrong analysis answer and a mid-roll edit. `voice_walk.py` walks the main Find out and Barn paths with Sound on, plus five repeated failed verdicts and the Push side path. `resume-shots.json` checks leaving during feedback and returning to the test or ghost comparison.

Images total about 724 KB. The pond was redrawn to remove an unwanted miniature farm, and the two pushing poses were redrawn with low hands. Every cutout was processed with despill enabled. The updated Jo sheet passed the fresh people-art check. The contact sheet is available to the owner in Scratch; this unattended build does not claim the owner has personally reviewed it.

The single full audit found 22 leads. Its HTML snapshot remains in Scratch. Four actual issues were repaired: compact Go clipping, a privacy-label overlap, a stale choice catalogue and focus loss on busy Go. The remaining leads concern first-action welcome skipping, inactive spots and comparisons across randomized or naturally completed runs. Focused checks verify those dispositions without a second full audit.

Final responsive rules keep the 680-pixel preview side by side, use 60-pixel ordinary-size controls, stack the 760-pixel portrait scene over a stable control desk, and give the completed phone wall extra height. Current hints retain the question situation for Read. Student work is session-only; the shared kit remembers Motion on this device.
