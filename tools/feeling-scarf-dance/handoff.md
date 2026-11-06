# Feeling Scarf Dance handoff

Cold review November 5, 2026, in S:/CurioClass-codex. No commit, upload or shared-file edit.

## Structure

src.html uses kit:curio, Curio.voice and kit:dance for four modes, original music, a 4+8+4 phrase and a tool-owned textured scarf. The engine owns joint positions, projection, root motion, clock and music. The 24-point scarf stays attached to world('rHa'). Nothing about the dance or audience feedback is persisted. The kit remembers Motion preference.

## Painted dancers

The owner's painted-people direction overrides the old code-figure Art section of spec.md. The engine model remains hidden. createDancerRenderer and paintedFigure are the replacement boundary: a single generated atlas has three children, each with one articulated pose plus a reverse view for turns. CAST holds registration coordinates. Every crop maps to engine screen joints; the original ribbon remains independent. Again rotates the demonstrator without associating any body or skin tone with a feeling. Shape buttons and audience chips use the same painted renderer.

art/prompts.json retains the hilltop and silk and replaces the unpainted eleven-pose proposal with the smaller articulated atlas. All people artwork is marked people true and drawn_by codex. The previous pose proposal is preserved in Scratch/original-pose-plan.json. The raw atlas is art/raw/dancers-rig.png; the processed asset is art/dancers-rig.webp. Built-in imagegen was used with the full manifest prompt and house style. Only art.py --rekey processed the chosen PNG; no paid art CLI or external image download was used.

The atlas contains brown skin and straight hair, deep brown skin and a fuller build with curls, and light freckled skin and red hair with a right lower-leg prosthesis. Front and reverse views preserve anatomical sides. The atlas and final contact sheet in Scratch need the normal owner/fresh sensitivity review before release. This review does not claim to be that independent review.

## Review repairs

- Further audit-path checks found stale audience ticks surviving changes to the dance. Changed feelings, parts and suggestions now clear those observations and invalidate old reflection/Freeze lines. Same-choice taps preserve observations. Idle edits label the part actually being previewed.
- Building parts before choosing a feeling now voices the missing feeling and then Watch it when the feeling completes the dance. Hints and how-to lines both follow the actual missing choices, including out-of-order construction.

- At a two-second tap pace Play and Go cut off their mode introductions. A pending start now keeps a fitting introduction intact, then starts the clock. Repeated Play/Go cancels a pending start. Stop, Read and mode changes invalidate the pending token. Opening a menu during preparation cancels it. No pending callback can launch an obsolete dance.
- Idle part edits previously displayed the first instant of a blend forever. Idle edits and mode entry now set their selected pose immediately; live edits retain their 180 ms transition.
- Audience chips record an observation, including on repeated taps; Swap clears them. Each event has a unique queue key and an observation-version validity check. No score, best score or automatic pass exists.
- Audience chips now echo the class's chosen shapes and movement trace. This lifts the generic final checklist without adding a mode or assessment.
- Choosing a feeling now invites a remembered experience on the screen and in its how-to line. No personal disclosure is required.

## Timing and specification interpretations

- One clock, play and music object; Stop holds the pose and scarf. Live changes keep count position; feeling and Slow update tempo on the next count. Mirror flips actor and ribbon layers together in Your turn.
- Sixteen counts plus four count-in clicks match the recomputed normal durations. Slow is 70 percent, so the slow Sad run can exceed twenty seconds; the spec's under-twenty statement applies to normal tempo.
- Twenty-four points have twenty-three segments. Each is 1.1/23 body heights, preserving the required total scarf length. The spec's 0.046 figure instead assumes twenty-four links.
- A grass contact constraint and edge inset keep the cloth in the painted view. Motion off uses one pose per count, a straight cloth and unchanged timing. Its shared layer translation keeps a low pose's long cloth visible.
- Your turn uses the same phrase and scarf renderer as Watch, with a four-count introduction, hidden painted dancer and faint hand marker. Freeze appears at the end and holds three silent seconds; its spoken reminder follows the quiet hold. This preserves the spec's quiet interval. The eventual reviewer should judge whether the spoken cue should precede that interval instead.
- The Calm track uses a high piano register for chimes because the engine has no chime instrument. Music and feeling suggestions are authored expressive options, never universal emotion rules.

## Voice

The audit-frame check found painted icon heads clipped by the code figure's old viewBox; icon bounds now include their full painted head. The final targeted frames cover filled Build cards and their small counterparts. The audit voice check also prompted clearer next-control wording for Feeling idea, Watch's reflection, Share, Swap and Freeze; voice/lines.json matches those changes. These get focused rechecks after the single audit, not a second full audit.

Curio.voice chooses how-to lines by heard state and drops stale lines. Hints update synchronously. The mode welcomes, event lines and every authored line are in voice/lines.json and allLines(). Read stops a run or pending start, then reads the current hint, including with Sound off. No narration is scheduled over music.

The 44 lines still use browser fallback. soft-breath / Enceladus is declared, but no recordings exist. CODEX-BUILD explicitly says not to record audio, so the cold review did not make them. Scheduling tests use muted Chrome with real timing; they do not verify Enceladus timbre or classroom loudness.

## Sensitivity

No named cultural dance, religion or historical tradition is represented. A fresh reviewer should inspect the people set for natural body representation, prosthetic-side continuity during turns, respectful articulated poses and the availability of seated or smaller versions. The suggested feeling-to-movement associations are optional; a child may use any shape or movement for any feeling. Faces do not diagnose feelings. Invite a life connection without requiring a disclosure.

## Named sources

- National Core Arts Standards Dance K-2, DA:Cr2, DA:Pr6 and DA:Cn10: https://www.nationalartsstandards.org/customize-handbook?discipline=Dance&grade_level=PK-2%2CPK%2CK%2C1st%2C2nd
- NDEO, How the Early Childhood Standards are Organized, movement analysis and individual developmental variation: https://www.ndeo.org/Learn/Dance-Education-Standards/Early-Childhood-Dance-Standards/How-the-Standards-are-Organized
- NDEO, Opportunity-to-Learn Standards for Dance, safe props and scarves as creative/sensory materials: https://www.ndeo.org/Portals/NDEO/Standards%20Documents/NDEO_Opportunity_to_Learn_Standards_2-22-18%281%29.pdf
- Gilbert's author, title, second edition and 2015 date are confirmed in Human Kinetics' 2017 publisher catalog: https://www.humankinetics.com/AcuCustom/Sitename/DAM/158/Human_Kinetics_2017_Product_Guide.pdf . The full book was not available for page-level verification; no quotes or unique book-specific claims were added.

## Engine changes wanted

- docs/families/dance.md, What each tool brings: add feeling-scarf-dance, K-2, square floor, poses/level/dyn, leap, phrase, clock, play, music, counts, icon; class-created 4+8+4 feeling dances, a 24-point textured hand scarf, scarf-only performance and audience observations. The write boundary forbids editing that shared file here.
- kit/dance.js, floor: consider a full-height square backdrop without its platform. This tool hides .dz-floor and sets backdrop height after resize, keeping the engine geometry.
- kit/curio.js, init: an optional memory-only Motion setting would reconcile literal no-storage specs with shared Motion preference. Standing STANDARDS takes priority here.

## Evidence

All review evidence is in _scratch/feeling-scarf-dance/: cold/ and cold-whole-result.json preserve the play before reading builder notes; numbers.json and facts-sources.json record recomputation and named sources; walk/results.json contains held-input voice and cheap-path checks; moves-shapes/, matrix-*/, special/, phone/ and review-audit/ contain the inspected frames. codex-review.md is the final one-pass review record.
