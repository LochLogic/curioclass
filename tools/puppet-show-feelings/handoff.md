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

## Next review
The single full audit completed with ten leads. The report dispositions all of them. Final repairs received targeted checks rather than a second full audit: ending props, Line pictures, worried icon, repeated target praise, same-mode welcomes and Like me's ring layout. All 81 audit frames and all follow-up frames were inspected.

Use the report and `_scratch/puppet-show-feelings/` for frame and audit evidence. Review the feel of the simplified cue model with a class, and listen to babble and browser narration through speakers. A later recording pass can supply the specified narrator without changing the queue.
