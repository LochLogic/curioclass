# Handoff: Puppet Show Feelings

## Built
One offline HTML tool with Show, Backstage and Like me. Teacher led for K-2. The supplied 27-cell table drives every audience result. There is no scoring, microphone or saved work.

## Source map
`src.html` starts from the Curio Class starter structure and shared kit. CSS defines responsive scene layouts. Content tables and fixed narration live at the start of the tool script. The animation loop interpolates tilt over 250 milliseconds and blends bounce amplitude and speed while preserving phase. Babble synthesizes two or three sine and noise blips per syllable and swaps painted mouth frames.

The Show runner uses a serial token so Back, Next, Again, Read and mode changes invalidate delayed babble or questions. Backstage keeps its own settings across mode changes. The audience card is hidden by every setting tap. Try it checks on changes and offers six targets with a two-second advance. Like me prompts and ending votes stay on this page only.

Selected mode taps return early so they do not cut a welcome or reset work. Every valid target change is a praise event, including a second setting combination that still matches. The Line button builds a miniature scene from the existing embedded art. Like me leaves a wider center gap and offsets the puppet by its preset head tilt so the cards do not cover its face.

`window.__tool` exposes state, content, the table, feeling lookup, mode entry, setting changes, ending selection, voice log and babble timing log for review.

## Art
Ten original assets, made with the built-in OpenAI image tool. Prompts are in `art/prompts.json`; originals are in `art/raw/`; all WebP processing used the free `art.py --rekey <name>` form. Pom and Dot open-mouth frames were redrawn from the corresponding closed frame as references. The park was redrawn to put the whole tree inside the curtain opening, with the stuck kite visibly in its branches. The new kite was redrawn to reduce pink edge paint. No people or human body parts were generated.

## Build decisions and open questions
- The spec lists no open questions.
- At short landscape sizes Backstage puts the nine controls beside Pom, following STANDARDS' side-by-side compact requirement. At laptop sizes they sit below the stage.
- At 760 pixels wide and tall, Show stacks its story card below the theater so Pom stays large.
- The listed voice identity, smooth-narrator / Algieba, is preserved in `voice/lines.json`. Build instructions prohibit recording audio, so this build uses the kit's browser speech fallback.
- Nothing from the lesson is stored. The shared kit still remembers its Motion preference, as the tool contract requires.

## Engine changes wanted
No runtime engine changes. For the audit helper, `scripts/audit_tool.py`, `MODES_JS`: add `nav .seg button` to its mode selector. Its header-only selector misses this tool's separate navigation bar, so the authored states and explicit interaction checks supply that coverage. No shared file was changed.

## Claude Refine repair, November 6, 2026
This section supersedes the older timing and Line-cycle descriptions below. Every first Show navigation or reveal action starts the welcome and baseline scene. Backstage Line cycles the four story scenes and the selected ending; it omits the silent choice scene. Setting changes hush the narrator and babble immediately, then offer the full first-change instruction. Audience says speaks its result before the flip explanation. A local completion flag uses the voice log's cut marker so an interrupted flip can return; the shared engine is unchanged.

Show me names posture, voice and bounce and keeps a running babble alive. Like me recalls Pom's matching story moment. A first ending vote asks the child's reason; a repeated tap on that tile offers the existing example reason. Passing remains welcome. There is no reflection grade or gate. Try it remains the exploration prompt the settled calls explicitly allow to be swept, not a mastery score.

Pom's shelf cuff is behind a drawn foreground ledge. Dot is inside the opening beside Pom, with the stick behind the puppets. Feeling faces have dot eyes and distinct worried, sad and calm cues. Head and Bounce controls and change arrows use SVG. No new painted art or recordings were needed; narration still uses the existing browser fallback and lines.json matches allLines().

### Repair proof left open
The final visual audit found the Up/Fast/Big Backstage pose clips the top of Pom's head at 375x812. See `_scratch/puppet-show-feelings/fix-audit/state-backstage-big-up-375x812.png`. The main 1366x768 and 680x425 poses and all nine controls are visible. Polish accepted item 5 remains NOT FIXED because of that phone regression. A follow-up should bound the puppet's phone size/base position against the full bounce excursion, then inspect both Up/Big and Down/Big at 375x812.

Should fix item 8 has revised natural-English literals for all six feelings, but its individual happy-praise voice proof is incomplete. The probe started already matching happy, so the no-op guard correctly prevented praise. To verify it: open Backstage, turn Try it on, cycle Next target three times to happy, change Head to Down and back to Up, and inspect the spoken log for "Yes! Pom looks happy!". Other five praise lines and all six audience lines were logged complete. No runtime changes were made after the single final audit.

## Cold review repairs, November 5, 2026
Read no longer reveals an unasked audience result. No-op setting taps and merely opening/cycling a matching target cannot earn praise. Target praise checks the current mode and settings; successful target advance resumes after returning to Backstage. Line waits for narration before babbling. A first tap on the theater starts the welcome and opening scene. A short first-change instruction replaces an unfinished welcome when needed. Closing Ending vote restores the selected feeling's prompt.

The first-change how-to is now the shorter "Say a clue. Tap Audience says." It starts before the babble and never waits behind the welcome; later changes babble immediately. Line playback waits for narration. Audience says stops the babble before the result. Personal prompts invite telling Pom or passing, so solo play and privacy work on screen.

The new-kite ending unfolds the new prop and keeps the original red kite visibly stuck. The heavy stick was redrawn with the built-in OpenAI image tool as a thin painted twig. All cutouts were rekeyed with edge despill; texture and the original stage were preserved. Motion's tooltip states its preference stays on the device.

The cold audit completed once with seven mechanical leads: two iframe-context leads, four intentional first-tap welcome skips when a control has its own line, and one intentional quick-Next cancellation. The separate mode bar still needs the documented audit discovery improvement. All 78 saved frames were inspected. The compact down-tilted puppet crowded the right edge at 1000x625; a pose-specific left offset now keeps the full face visible, without shrinking Pom. This narrow post-audit fix receives compact-size rechecks, not a second audit.

## Sensitivity
No named culture, religion, hard history or human figures. Review the simplified feeling map for overgeneralization across cultures and neurotypes. The cited studies support probabilistic cues, not universal readings. Personal memories are optional; invite passing, and do not infer a child's feelings from their posture or speed.

## Cold review left open
The spec requires automatic praise and a check as soon as settings match. A blind exhaustive sweep can earn that exploration check. Claude Refine's settled call explicitly permits it because there is no score and the notes explain the limitation. This is not an open blocker in the current round. Try it must not be represented as a mastery assessment. No attempt gate, new feature or kit change was made.

## Next review
The single full audit completed with ten leads. The report dispositions all of them. Final repairs received targeted checks rather than a second full audit: ending props, Line pictures, worried icon, repeated target praise, same-mode welcomes and Like me's ring layout. All 81 audit frames and all follow-up frames were inspected.

Use the report and `_scratch/puppet-show-feelings/` for frame and audit evidence. Review the feel of the simplified cue model with a class, and listen to babble and browser narration through speakers. A later recording pass can supply the specified narrator without changing the queue.
