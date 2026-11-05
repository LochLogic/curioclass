# Codex review: place-mood-makeover

## Played

Cold Grade 4 play before builder notes covered all three wrong artist guesses and clue reveals, all places,
an earned Cozy picture, opposing clue tags, partner guessing, divider and the writing card. Later checks verified
kept reasons and saved writing. Also checked projector framing. The best moment is defending the glove as Cozy.

## Findings fixed

- **Blocker, general, phone/compact interaction:** a pinned studio covered scrolled controls, so goal/light taps,
  clue cards, Partner guess and Write could miss. Phone scroll insets now protect targets; compact studio pinning is
  removed. The phone picture, compass and hint stay available. Real held-click completion and modal checks pass.
- **Should fix, general, layout:** Weather crowded its label; compact targets were narrow; 1000x625 cut the compass;
  phone Next and compact partner choices crossed the fold. Fixed spacing, widths, scene fitting and compact cards.
- **Should fix, general, clue card:** scrolling the reason hid its title/Close. A sticky heading keeps both accessible.
- **Should fix, general, teaching state:** old partner results survived revisions; writing stayed visible after
  agreement failed; replaced global clues retained old interpretations. Cleared stale results/tags and gated writing
  while preserving saved text. Same-tag taps retain reasons; Write stays open on repeat taps.
- **Should fix, general, guidance/focus:** last artist still named Next; closing the divider kept its old hint;
  artist transitions could leave focus behind. Fixed current hints and deliberate focus with preventScroll.
- **Should fix, general, voice:** tugs could wait behind a welcome, and removed clues could keep speaking. Current
  events take priority and stale speech stops while Read remains protected. Plural subjects and all Read hints are
  cataloged consistently in content.json and voice/lines.json.
- **Should fix, general, art:** floating/overlapping details, a projecting shop window, mismatched lamp head and pink
  plate edges weakened the scene. Redrew four assets and anchored/separated details, chains, ground art and glows.
- **Polish, general, payoff:** the gold compass alone was flat. The student's completed picture now gains its own
  mood title and gold frame. Partner guessing hides those cues. The original paintings and rich studio remain.

## Findings left

- **Should fix, general, spec conflict:** the explicit compact strip and lower phone/secondary scrolling conflict
  with the standing all-choices-at-once rule. Preserved the prescribed layout and art; a different navigation model
  needs a spec decision. Every control remains reachable. No other confirmed blocker or should-fix remains.

## Flattest moment left

The Plain studio still waits for the student to choose a mood and make the first clue. A preset or challenge would
change the open sandbox specified here, so none was added.

## Graphics

Inspected all 41 assets and all three composed detail sets at final size; none shows people or a placeholder.
Regenerated bus-window, bus-broken-lamp, place-porch and place-playground with built-in imagegen, then art.py --rekey.
Prompts/provenance: art/prompts.json; originals: art/raw/. Art 1349.9 KiB; final bundle 1915.0 KiB.
Compared the studio beside Beat Lab and opened Snowy Mail Route. Evidence: Scratch review-feel-comparison.jpg.

## Audit

One audit completed within 40 minutes: **284 mechanical leads; all 97 frames inspected** in 17 contact sheets.
Confirmed scroll/click obstruction, cropped compass, hidden hint and fold leads were repaired; targeted real inputs
reach the intended controls. Modal/background and divider-label overlap, correct "1 pulls" grammar, and five
first-tap own-line welcome skips are explained in Scratch review-audit-dispositions.md. The specified scrolling
constraint remains above. Resize stress found no exceptions/stuck controls; repeat and quick-tap samples were clean.
Rechecked 12 affected states, phone writing (both fields visible), and the changed voice paths. No second full audit.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Light Cool tug | event | 5 | 5 |
| Every clue points to Cozy | event | 5 | 5 |
| compassHow | how | 1 | 1 |

Independent checks: all 44 clue vectors and ten contrast ratios match; browser paths complete all 15 place/mood
pairs. Empty/kept reasons, tag retention, partner concealment, reload, per-place reset, keyboard-only play,
grayscale, Motion off and a real divider drag pass. Notes have the required opening sections and all four standards
are practiced. Source/resource checks found no external requests; all 41 art tokens resolve. Test Chrome/server
processes are closed and host.html is absent. Evidence is under Scratch review-* and post-*. No commits.

## Left open

The layout/spec conflict above; optional recorded soft-breath narration (recording forbidden in this pass).
The full audit precedes its targeted repairs, as the one-audit rule requires. No classroom trial was claimed.
