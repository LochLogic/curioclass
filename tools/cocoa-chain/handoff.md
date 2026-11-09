# Cocoa Chain handoff

Build only. No commit, deployment or polish round.

## Implementation

src.html starts from the kit starter and uses kit CSS, Motion, Sound, tones and Curio.voice.
The source contains responsive scene styling, six stop records, shared season state, map and scene renderers,
the two dated dollar studies, a pure explanation validator, and persistent keyboard/drag controls.
map.json contains locally thinned Natural Earth coastline geometry and is loaded by the bundle token.
Worker cards have a short visible introduction and their complete supplied text under More and Read.
All scene art uses art tokens and is embedded in the bundle. Raw originals remain under art/raw as required.

The six numbered pins answer the current unanswered needs question. Once answered, pins navigate.
Back, Next stop and the dollar strip navigate without requiring a needs answer. This resolves the specification’s
dual assignment of navigation and answering to the same map tap. Initial pins navigate immediately.
The shared rains state survives mode changes. Reflection choices survive turning the rains off and back on.
Explanation edits invalidate a pass immediately; reading revalidates rather than trusting a button flag.

## Open question decisions and contradictions

- The supplied concept/idea says drought; the detailed spec explicitly prefers the actual 2023 rains. Used the rains.
- The spec mentions Gemini for people; the current build brief and user explicitly require the image tool.
  Used OpenAI gpt-image, credited in the manifest. Every people asset has people: true.
- The only open question is sensitivity review. Retained the supplied historical and child-labor text, made respectful
  adult art, and left the independent fresh-agent review to the cold review stage. No questions require an answer here.
- Natural Earth 1:110m was requested. Available local verified geometry was 1:50m; used it, thinned locally and credited.
  The map remains equirectangular over lon -100 to 20 and lat -5 to 60. Pins use leader spacing for adjacent stops.
- The calculation note says 2 x 452 kg = 905 kg. It is 904 kg, 14.464 net bags, then 11.709 under the national ratio.
  Keeping the requested 14-to-11 illustration therefore cannot be described as that exact yield calculation.
  Scene labels explicitly identify the bags as illustrative; no household income is calculated.
- 16 x 64 kg gross is 1,024 kg gross, not one net tonne. The COCOBOD 16-bag price convention is retained,
  with net-versus-gross explained in notes. No arithmetic exercise equates the gross mass to 1,000 kg.
- 5.04 to 4.37 million tonnes is a 13.29% decline, not 13.5%. About 14% is supported by the World Bank’s 4.9-to-4.2 series.
- $4 times the 2015 maker/store share is 317.6 cents, rounded 318 in the spec. The strip keeps one decimal for exact sums.
- The spec’s compact Explain layout (six 44px rows, four 44px tray rows, two 44px chip rows, plus header) cannot fit
  425px high. STANDARDS target sizes win. This build permits scrolling for the explanation workspace at that extreme.
  Follow’s frequently used controls and the whole scene remain the compact priority.

## Sensitivity

Cold review should inspect Ghanaian names, skilled contemporary adult representation, all twelve people images,
the Ghanaian places, the child-labor card, Tetteh Quarshie’s credit, the earlier-missionary note and South American origin.
No child is pictured or asked about their own household. The farming couple’s children are described as in school.
Working art was redrawn for the couple to remove scenery; both Luis poses were redrawn to match his supplied role.
The contact sheet and all review evidence live in _scratch/cocoa-chain/.

## Engine changes wanted

None required. A tool-local space avoids bundle_tool.py treating an object’s art:wet as an image token.
No kit or repository script was edited.

## Review next

See codex-report.md for actual checked results, audit dispositions and remaining limitations.
Recorded voice was prohibited in Build; voice/lines.json selects friendly-dad (Achird) for a later recording stage.
Until then Curio.voice uses the browser fallback. No fixed-voice fidelity claim is made.

## Build verification and remaining limits

The single full audit completed in 28.3 minutes with 64 mechanical leads. Each is answered in
_scratch/cocoa-chain/audit-responses.md. Repairs covered narrow map overlaps, 10px tags, the 760px Explain layout,
sticky modal controls, correct first-action guidance, retained dollar focus and stale explanation passes.
The dry 680px worker card uses a shorter name and first sentence; the full role, names and supplied text remain
under More and Read. A wrong pin keeps the question visible while giving its corrective hint.

At phone width and short landscape heights, Explain still scrolls. This is a reported failure of the all-choices
above-the-fold rule, not a claim of complete responsive compliance. Its hint and voice now explain the scrolling.
In the 680px rain preview the three outcome choices remain visible; secondary reference buttons require scrolling.
The 760x900 Explain layout now shows all sentences and chips at once.

Strict validator enumeration tested 20,160 sentence orders and 360 chip arrangements, with one valid result each.
Real held-click, keyboard, native drag, six-link, season reversal and stale-pass tests are preserved in Scratch.
The puzzle provides corrective feedback by design and is not an independent mastery assessment or scored game.
No tries, grade or best score is stored. Reflection marks mean participation only.

The user's stop-on-report instruction overrides the brief's request to create codex-report.md early.
The report was drafted in Scratch during the build, then copied to its final path only as the final work step.

## Cold review changes

The review first played the complete tool before reading this handoff or the builder report.
Port art was redrawn in the same style and container overlays now fill their bottom row before the top row.
Compact route views retain goods/money arrow pairs. The ocean label moved away from the money line.
The paragraph finish reconnects the six steps to painted scenes; selected sentences now have once-only spoken placement guidance.
Used tiles retain ink contrast instead of fading. Three source qualifications were corrected: September 2023 farm price,
first-half-2024 export earnings, and announced 2025 US price/pack changes. Source links are in notes.md.

Review decisions without an attendant: retained full text and 44px controls rather than shrinking the short/phone
Explain workspace, and retained the specified first-error feedback and optional needs questions. These are open
spec conflicts, not waived checks. A blind trial using only feedback passed Explain, and pin sweeping reached six links.
The cold-review report records these as blockers to using completion as independent evidence of learning.
No new feature, engine edit, recording, commit or publication was introduced.

The fresh cultural review should still judge the fictional Ghanaian names, the adult working/thinking art,
the child-labor card, and whether the Ecuador origin should explicitly credit Indigenous makers.
The current text retains Ghanaian farmer agency and Quarshie's 1879 Mampong credit without calling him the first planter.

## Cold review final verification

The single review audit completed under its 40-minute limit with 41 leads. Three compact-reference leads were repaired
by placing existing reference controls outside the worker card and ahead of secondary content in compact views.
Fifteen phone Explain leads remain under the documented specification conflict. The other 23 leads are intentional
modal coverage, already-answered prompt cancellation, BASELINE 16 welcome skips and two obsolete/corrective speech cuts.
The exact disposition ledger is _scratch/cocoa-chain/review-audit-responses.md. No full audit was repeated.
Only affected frames were re-shot. All compact reference buttons are visible; the 1000px workspace and its voice agree;
repeated selections no longer cut a still-fitting how line; Sound width is stable and its label stays on one line.
Native drag, keyboard placement, strict validator, Read invalidation, calm mode and rapid season changes were checked.

An additional unresolved source conflict belongs to the spec owner: USDA FAS GH2025-0048 gives 530,873 tonnes for
2023/24 while COCOBOD's newer sector-reform release gives 432,145. The model's specified numbers were retained;
notes.md and codex-review.md disclose the conflict rather than presenting either series as universally settled.
No clean-release or independent-mastery claim is made. The pin sweep and first-error oracle remain explicit blockers.
