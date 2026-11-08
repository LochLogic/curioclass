# Worry Size Sorter handoff

## Current shape
This fix follows CODEX-CURIOSITY.md and the user's explicit override. The old kit header, My week goal builder,
check-off chart, reflection and finite Sort end panel are removed. Sort is a continuing desk, with at most one current
placement per fictional card. There are no goal, score, level, quiz or finish controls. NHES S6 is not claimed by this version.
The shared curriculum map is outside this task's write boundary and may still need the integrator's update.

The desk draws its own controls and layout; only kit/curio.js supplies settings, tones and voice. The lower-left Manual
contains use, readout limits, sources and permissions. The maker's plate omits a number because neither the spec nor
docs/CURIOSITIES.md assigns this id a Curiosity number. tool.draft.json has curiosity true and plate null; do not invent a number.

## Fix mechanisms
- All destinations animate the card into the basket with a persistent invisible end state. Motion off hides it at once.
  Re-rendering a sorted card keeps the empty slot. Big situations always land in Big regardless of the requested basket.
- The meter handles digits 1 through 5 only when it holds focus. Desk selectors handle 1 through 3 only while focused.
  A key inside a running tool cannot change mode. Arrow/Enter sorting and native Tab work.
- Breathing defaults to three full rounds, with one optional fourth. Shorter count (3) has a fixed label and aria-pressed.
  Timing remains real time with Motion off. Squeeze still has three independently tapped parts.
- Body links are derived directly from D.clues.tools. Tummy has both Box breathing and Talk back. Leaders are computed
  from actual ring rectangles to image-relative anatomical anchors after rendering and on resize.
- Folding is two phases, halves then quarters. The folded slip centers above the painted slot; the drop ends at that slot.
- Helpers save under wss-helpers and show the device-only privacy line at the saving control. Blocked storage is caught.
  Legacy wss-week is ignored; existing saved records are not erased or migrated. No new weekly record is written.
- Read uses registered L.hints and finite registered content, never arbitrary panel innerText. allLines and lines.json match.
  The Curiosity brief's voice policy wins: only the first quiet hint may speak automatically, then narration is on Read.
  The old automatic Big speech wait and Listening state were removed along with mode welcomes. No safety content was removed.

## Safety and material
b1 is now a closed notebook on a school bench in daylight, without people, bedroom or night scene. The asset token is
unchanged. The prompt and raw source were replaced. The four affected hair edges were re-despilled, preserving alpha
and every pose; no new people image was generated. The toes pose is unchanged.

b1 names known/family adults; b3 avoids promising an adult's reaction and states that the child is not at fault.
b2, b4 and b5 include the requested support wording. Adult notes include the online exploitation and disclosure routes.
Hotlines remain out of the student interface. The on-screen immediate-danger 911 wording is the settled US-specific call.

The material is fictional Curio Class situations and original explanatory text, not an empirical dataset. Each student-facing factual
reference has a name, rights statement and URL in the Manual. Adult reporting references remain in notes and metadata. Protected source articles and illustrations
were not imported. No claim that a source's copyright has become CC BY is made. Sources are not endorsements.

## Spec decisions
The merged list's final section reserves spec text updates to its owner, so spec.md is untouched. Its lesson-flow lines,
two-round wording and old art/safety prompts are superseded by this handoff and the user's Curiosity instruction.
The source-only replacement art has no person, so it adds no contact-sheet entry. Existing sensitivity reasoning was read;
this fix does not claim a new cold sensitivity verdict. Recorded audio is a later media step; no recording service was called.

## Evidence
All evidence for this pass is under _scratch/worry-size-sorter/fix/, with the mechanical audit in fix-audit/.
The original source, data, notes, voice manifest and prompts are archived in fix/original/. No refine file was edited.

## Engine changes wanted
scripts/audit_tool.py: MODES_JS currently searches only header descendants. Include a Curiosity's own navigation buttons,
such as .desk-switches button[data-mode], without requiring a lesson header. Suppress welcome-per-mode expectations when
tool metadata says curiosity true. The tool's explicit audit states cover both other views, so no engine edit was made.

## Final audit response
The single mechanical audit exited 0. Its layout leads were corrected with focused checks: maker text is at least
10 px, compact result meter targets are at least 44.59 px wide, phone result actions and the save privacy line stay
visible, and the Manual title clears Close. The sorted card is also visibility hidden after its flight, so invisible
text is absent from hit testing. Compact results omit the redundant phase strip to keep the adult-help advice in view.
The final Manual has 17 student-facing references; all 24 remain in adult notes and metadata. No adult hotline number
is displayed in the drawer. The modal intentionally covers the background hint, and lesson welcomes remain absent.
The audited bundle was preserved until that run finished; only the confirmed leads were re-shot after the small fixes.
