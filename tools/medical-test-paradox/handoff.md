# Medical Test Paradox handoff

Build only. All implementation writes are confined to this tool and its Scratch folder. No commits or polish round.

## Structure
src.html starts from the kit starter, uses the 9-12 theme and Curio.voice, and contains the UI, local probability
mechanics and seven cases. The main state is exposed through window.__tool with every requested hook, allLines,
vlog, expected, Rand and hundred. No student state is persisted. Art is bundled through art tokens.

The canvas is a quantitative icon array, not a painted crowd. Filled versus outlined marks distinguish the condition;
plus badges distinguish positives. The expected-count display uses fractional icons. The large crowd uses ten people
per square. The table DOM remains stable while highlights change to retain keyboard focus.

The glossary is a native modal dialog, opened beside Reset mode. Its five chips remain available at small sizes
without displacing the simulation controls. Escape closes it and the prior hint returns. Cases keep numerical
settings and prediction controls first, with the explanatory story below. A case reveal returns focus to its card.
The tree chooses its compact vertical layout using both width and height, keeping text at readable pixel sizes.

Random towns use mulberry32 and two draws per person. At 100,000 people the single-town drawing yields in batches.
The 100-town run yields between towns, pools positive counts, and retains a stopped chart when interrupted.
All asynchronous sequences use a cancellation token. Slider changes cancel old work before recomputing.
The stopped chart retains the expected reference from its original settings. Second-test counts are labeled
as expected even when the first town was random.
The chart appears during the run and uses actual pixel coordinates for readable compact labels. Its accessible
summary updates with the pooled counts. In Chances, first-stage branches derive from the displayed town counts;
second-stage branches use the assumed test rates. Empty groups use model rates on their zero-mass branches.
counts() returns the displayed full-town groups, including C4's two-test final classification. second() returns
only outcomes among the first positives, so its negative totals intentionally exclude the first negatives.
caseCard accepts numeric IDs or C1-C7. divideBy accepts the visible row or column names and returns part, whole
and the fractional value; table returns the cell matrix and totals. A pristine Reset preserves valid narration.

## Decisions and contradictions
- The prompt's image-tool route takes precedence over the spec's local FLUX route. Five paintings were generated
  during the Build; the coin was redrawn once to remove a key-colored ground artifact.
- The probability family file and kit/probability.js do not exist in this checkout. The requested shared engine
  therefore cannot be used. Local implementations keep this tool runnable without touching shared files.
- Open question: retain the module's broad codes, and flag B.9 (+) as untaught here. It belongs elsewhere. B.8 (+)
  is served by multiplying along the independent two-test tree; no counting topic was added.
- Open question: retain the made-up condition with the historical teaching numbers and attribution. The case
  credits the study and does not name its real disease.
- STANDARDS says Motion off removes movement while preserving pacing, while this spec asks for instant test beats.
  This build follows STANDARDS: the two 950 ms beats and the 880 ms sort beat retain their timing with Motion off;
  the sort itself draws instantly while its instructional timing stays intact.
- The short-landscape side-by-side requirement in STANDARDS overrides the spec's under-1000 stacking rule.
- The prompt's stop-on-report instruction takes precedence over an early incomplete report in the tool folder.
  A working report is assembled in Scratch and the completed report is written last.
- No recorded audio was made, as required by the Build brief. The requested bank voice is metadata; the browser's
  available voice supplies narration in this build.
- The close-prediction line now describes numerical closeness rather than claiming the student read correctly.
  An untouched 50% guess is already close in C4, and a random guess can be close. Predictions carry no mastery claim.

## Sensitivity
This tool concerns people's bodies through fictional medical testing. Review the distinction between a model and
personal medical advice, the respectful treatment of missed cases and false alarms, and the repeated-testing
assumption. Generated paintings contain no people. Abstract population glyphs are chart marks drawn in code.

## Cold review repairs, 2026-11-08
- Leaving Town at the Predict pause abandons that prediction. Returning begins Ready, with unknown results,
  so the Table answer cannot sit beside an active guess control.
- Correct Table matches use event narration, preserving feedback on repeated matches. Wrong feedback remains
  the spec's guided practice: no score, completion state or claim that a student has mastered the skill.
- Table tracks questions whose answer has been supplied by a wrong-match hint. Later matches for those questions
  receive worked-example feedback, preserving the guidance without treating a hinted retry as unassisted.
  A new parameter set, case or Reset clears this page-session assistance state. No student record is saved.
- Compact Table layouts keep all six questions and the overlap, Reset and Glossary controls in view.
  The numeric addition explanation has its own scroll area when it needs more room. Phone Table trades its
  repeated stage title for a taller control panel, retaining the table, fraction and all fraction targets.
- Eight fixed Read-only hints, including all glossary definitions, now join the production voice inventory.
- Audit follow-up: the portrait prediction state uses an 80px town band to retain the result card above the
  controls at 760x900. The painting remains present. Glossary speaks its existing action hint once on opening,
  guarded by the modal's open state; Read and close continue to interrupt stale narration.
- The 100-town loop checks its cancellation token immediately after yielding, before touching the chart or status.
- The two positive routes through the repeat tree now have solid/dashed emphasis and dimensional leaf cards.
  Chances displays each positive leaf's product as a share of the whole town, as well as the conditional rates.
- The coin and cassette were edited with built-in imagegen to replace green-fringed cutouts. Their raw PNGs
  already contain alpha. prompts.json uses cutout false with transparent true so art.py --rekey only resizes
  and encodes them, preserving that alpha rather than applying a second chroma key.
- Review evidence and named-source checks are in Scratch review-* files; codex-review.md records final disposition.

Final cold-review audit: see codex-review.md and Scratch review-audit/audit.md. The audit ran once; only confirmed fixes were re-shot.

## Engine changes wanted
kit/probability.js and docs/families/probability.md are absent. Supply the interfaces in the spec: Rand, Frac,
Trials, Tally, Converge, Population, TwoWay and Tree. Population needs accessible summaries, fractional icons,
filled/outlined condition marks and positive plus badges. TwoWay must retain focus while changing denominators.
Trials needs a real cancellation token. Converge must preserve a partial stopped chart. Then replace the local
functions with the shared interfaces and run the same fixtures. No shared file was edited in this Build.
