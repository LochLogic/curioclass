# Polish: worry-size-sorter (Codex fix, round 1)

The required workspace was S:\CurioClass-codex and was verified before work. No git command or commit was made.
All authored changes stayed in tools/worry-size-sorter/ and _scratch/worry-size-sorter/. refine.md and refine/ were untouched.
Evidence paths below are relative to `_scratch/worry-size-sorter/fix/`; audit paths use `../fix-audit/`.
The original source, data, notes, manifest and prompts are preserved in `original/`.

The user's Curiosity instruction supersedes the older lesson spec: My week, goals, checks, reflection and the Sort
finish panel were removed. The material fills an open-ended desk with its own controls, lower-left Manual and maker's
plate. Nothing was converted into a quiz or scored task. The one-file bundle is 1.76 MB.

## Blocker
1. FIXED. The b1 bedroom/night vignette was reproduced in `before/before-b1.png` and inspected full size.
   Replaced it with a closed notebook on a sunlit school bench, without people. `proof-a/after-b1-card.png` and
   `art/ws-card-door.webp` were inspected. Prompt and raw source updated with the token retained. The list's final
   section reserves spec text edits to the spec owner, so spec.md was not edited.

## Should fix
1. FIXED by removal under the Curiosity override. `before/before-because-up.png` reproduced a 2-to-4 reason supporting
   a goal. There is now no goal builder or Because generator: `validation.json` reports zero weekly controls;
   `numeric-proof.json` shows no finish controls after 26 cards, repeated with three basket patterns.
2. FIXED by removing the conflicting goal question. `before/before-clue-mismatch.png` reproduced Box breathing with
   busy thoughts and no tummy choice. Retained clue-to-tool links are now generated from D.clues.tools, including
   both tummy tools. `proof-b/after-body-1366.png`, `proof-b/after-clue-link.png`, `clue-proof.json`: tummy to Talk back
   opens tool 1. The audit's tummy-tool-link also opens Box breathing. No new fact question was added.
3. FIXED. `before/before-breath.png`: target 2 and two-round instruction. `proof-a/after-breath-default.png`: target 3.
   Actual held-click runs in `timing/`: three rounds took 48,144 ms at count 4 and 36,098 ms at count 3 (including
   polling overhead). `fourth-proof.json`: fourth round runs, fifth disabled. Cleveland Clinic and WebMD references below.
4. FIXED. `before/before-digit.png`: meter key 4 switched to week. `retry-final/after-digit-meter-final.png` and
   `digit-proof.json`: mode tools, rating 4. `running-key.json`: digit 1 left breathing running in tools.
   Numeric view shortcuts act only on the desk selectors. Removing My week leaves three view shortcuts, 1 to 3.
5. FIXED. `before/before-settle.png`: returned card opacity .85. After 1.2 seconds, `settle-proof.json` and real jittered
   drag `drag-proof.json` both report Big and opacity 0. `proof-a/after-b1-settled.png` shows the persistent empty slot;
   `retry-settle/after-settle-b1.png` proves the immediate Motion-off destination. Small and Medium use the same mechanism.
6. FIXED. `before/before-privacy.png` reproduced saving with no line. `retry-final/after-privacy-final.png` shows
   "Saved on this device only." at the helper control. `retry-final/after-storage-blocked-final.png` adds the browser
   failure sentence. Result meters now share a horizontal row so this line stays visible at laptop height.
7. FIXED. `before/before-read.png`: the Body clues hint was unregistered. Read now uses L.hints and finite named
   content instead of arbitrary panel innerText. `voice-body.json`, `voice-tools.json`, `voice-final.json` and
   `validation.json`: 146 runtime lines, 146 manifest lines, zero missing and zero extra. See Voice walk for the override.
8. FIXED. Reproduced at all requested widths in `before/before-body-1366.png`, `before-body-680.png`,
   `before-body-375.png`. Inspected after frames `proof-b/after-body-1366.png`, `after-body-680.png`, `after-body-375.png`.
   The Head ring clears the face; Tummy is on the hoodie pocket; heart is on the viewer's right; the hand leader reaches
   the hand. Leaders now use actual ring rectangles and image anchors on render and resize. Final layout also checked by audit.
9. FIXED. `before/before-b3.png` reproduced the promise. `proof-a/after-b3.png` shows the requested blame-free reason;
   worry-data.json and the manifest agree. It makes no promise about another adult's reaction. Spec wording left to owner.
10. FIXED. `before/before-b1.png` lacked the known/family-adult line. `proof-a/after-b1-settled.png` and
    `retry-final/after-read-big-final.png` show/read it; `voice-final.json` records the same text. Spec wording left to owner.
11. FIXED. The top 23 percent hair-region test found 111, 118, 98 and 71 green-dominant pixels on stand, fists,
    shoulders and loose. Re-despill leaves 0 in all four, with 0 changed alpha pixels. `hair-proof.json` and the inspected
    `hair-comparison.png` preserve each original pose. This is edge cleaning, not a person redraw. Toes was untouched.
12. FIXED. `before-numbers.json` records no CyberTipline route in notes. `validation.json` confirms the three requested
    route strings in the adult notes. NCMEC and current DOJ independently confirm the reporting number/URL and Take It Down.
    The latter is qualified for eligible images and participating platforms; no promise of universal removal. Nothing added on screen.

## Polish accepted
1. FIXED. The card-linked note is now "Think about this worry for a moment." Card-free breathing and squeeze have no
   worry text or that note. See `last-retry/final-tools.png` and `proof-b/after-clue-link.png` for the two relevant states.
2. FIXED. Body clue Try names are real buttons, derived from the clue data; `clue-proof.json` and the tummy-tool-link audit state.
3. FIXED. Medium results add the talk-it-over question; `proof-b/after-medium.png` and `medium-proof.json`.
4. FIXED. b5 names a trusted grown-up, school counselor or doctor; `retry-safety/after-b5.png`, data and manifest.
5. FIXED by removal under the Curiosity override. There is no weekly reflection, "I forgot" chip or next-week assignment.
6. FIXED. `retry-settle/after-settle-s1.png` and `after-settle-m2.png` show the same persistent destination for Small and Medium.
7. FIXED with a sourcing adjustment. "You can put this in Medium. Small is fine too." and the mirror keep the flexible
   tone without inventing a "Many kids" survey claim. `medium-proof.json` and `proof-b/after-medium.png`.
8. FIXED. The slip folds in two stages (halves, quarters), centers above the actual painted slot, then drops to it.
   `proof-b/after-folded.png`, `checks/after-boxed.png` and `focused-safety/fold-calm.png`; Motion off has zero slip animations.
9. FIXED. Four matching inline SVG icons, with different breathing-square and slotted-box shapes; `last-retry/final-tools.png`.
10. FIXED. Adults are one sentence in Read and "Tell one grown-up you trust" occurs once. `voice-final.json` and
    `retry-final/after-read-big-final.png`. The Big hint now only names Next worry, avoiding a repeated telling line.
11. FIXED. b4 and b2 add the requested no-blame statements; `retry-safety/after-b4.png`, `after-b2.png`, data and manifest.
12. FIXED. Home support and teacher disclosure steps added, adult-facing only; `validation.json` verifies the exact routes
    and steps. Childhelp is described as support, not as a substitute for mandated reporting.
13. FIXED. Both rising results and meterOther name a grown-up you trust; `retry-settle/after-rise.png`, `rise-proof.json`, manifest.
14. FIXED by removal under the Curiosity override. No end panel or end-count sentence exists. Baskets retain their
    current contents, and Next worry continues after card 13; `numeric-proof.json`.
15. FIXED. Notes and metadata share 24 named references and rights statements; the Manual has the 17 student-facing references. One canonical YoungMinds
    URL is used, credited for avoiding bedtime; NHS is credited for the ten-minute option. The Build-only fallback claim is removed.
16. FIXED by removing the old automatic-speech wait under the Curiosity voice rule. No Listening state or disabled Next
    remains. All adult-help content stays readable and is in Read. See `voice-final.json` and `proof-a/after-b1-settled.png`.
17. FIXED. Fixed "Shorter count (3)" label with aria-pressed; `proof-a/after-breath-default.png`, both timing frames.
18. FIXED. The placed card's accessible name says Sorted; `settle-proof.json` records it. It no longer says Pick up worry card.

## Settled calls
- Preserved data-based body/tool pairing, with tummy included, and corrected all five ring positions.
- Digits are scoped to focused controls. The removed fourth lesson mode has no shortcut.
- The Curiosity brief supersedes per-mode welcomes and automatic Big narration. The first quiet hint may be cut by action;
  later speech is requested with Read. No new welcome screen, goal, quiz or forced finish was added.
- The US-only "Danger right now? Call 911." wording is retained. NCMEC/Childhelp details remain in adult notes only.
- No score, timer challenge or streak; all-Big remains accepted and offers adult help without marking an answer wrong.
- Replacement card art has no person. No adult figure was added to any vignette.
- Spec-owner open questions were left open; spec.md and refine.md were not edited.

## Cheats tried
- All-Small, all-Medium and all-Big for 26 cards each: every intrinsic Big still lands in Big; no finish control appears;
  the desk remains open, with 13 unique placements. No choice earns credit. `numeric-proof.json`.
- Jittered real drag of b1 into Small: goes to Big and remains hidden from the stack, opacity 0. `drag-proof.json`.
- Rate 5, immediately Stop, then rate 1: gives a personal check-in with an early-stop note, no success or saved score.
  The audit's early-stop-rating covers this. Helpers remain an explicit personal preference, not verified mastery.
- All 25 before/after pairs: 10 decreases, 10 increases, 4 unchanged above 1, one calm-to-calm. The text reports the
  rating without making a causal claim. `numeric-proof.json`.
- Digits during a run and while rating cannot switch the view. A fifth breathing round cannot start. Results above.

## Voice walk
Held clicks were 0.12 seconds, with 2-second gaps on body and tool Read walks. There is no lesson welcome path.
Main walk: Body clues, Tummy, Read. The log contains the ring hint, tummy fact, its two Try tools and the too-big help.
Side walk: breathing Before, Read at Practice, Start, Stop, after rating, Read. The log contains the current practice
hint, square instruction and three-round line, then the helper hint and rising-rating advice.
Big walk: b1, Small, Read. The final log contains the next-action hint, premise, card and corrected reason, Big heading,
one adult sentence, three ways to start, keep-telling advice, emergency line and one privacy/tell-one line.
All parts are registered, with 146/146 exact manifest parity. Headless test audio is muted; this verifies the actual
kit Read invocation/log and recording readiness, not a human listening session or the quality of future recorded takes.

## Engine changes wanted
No shared file changed. `handoff.md` names the exact audit change: MODES_JS should discover Curiosity navigation outside
headers, and curiosity metadata should suppress lesson welcome-per-mode expectations. Explicit states cover this tool.

## The real material
No external dataset, clinical record, template or source illustration was imported. The thirteen scenarios, flexible
basket assignments and example replies are fictional Curio Class content (CC BY 4.0); code is MIT. Original generated
illustrations remain credited. The replacement uses the built-in imagegen tool; its full prompt is in art/prompts.json,
and its local raw PNG is art/raw/ws-card-door.png. Hair cleanup is reproducible in fix_material.py.

Live source checks on 2026-11-06 covered Cleveland Clinic, WebMD's respiratory-therapist article, CDC, NIMH, YoungMinds,
NHS, Childhelp, eSafety, NCMEC, Take It Down and DOJ. The main WebMD URL returned 403; the old DOJ tip-sheet endpoint
was inaccessible, so the current named DOJ reference was used. No unavailable reference was invented as a successful fetch.
Other references are inherited fact-check context from the spec, not newly fetched material. The complete rights and
claim catalogue is `source-notes.json`, recorded in tool.draft.json; its student-facing subset is in the Manual. Protected articles
are references only; their copyright is not a permissive dataset licence. No publisher or government endorsement is implied.

- [Nemours KidsHealth · Anxiety](https://kidshealth.org/en/teens/anxiety.html): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [CDC · Anxiety and Depression in Children](https://www.cdc.gov/children-mental-health/about/about-anxiety-and-depression-in-children.html): US federal text is generally public domain; third-party exceptions. Facts referenced, no CDC assets copied; no endorsement. Free at the source. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NIMH · Children and Mental Health](https://www.nimh.nih.gov/health/publications/children-and-mental-health): US federal government public-domain information; no third-party assets copied. Fact-check reference only. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Cleveland Clinic · Box Breathing](https://health.clevelandclinic.org/box-breathing-benefits): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [WebMD · Box Breathing](https://www.webmd.com/balance/what-is-box-breathing): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [WebMD · Respiratory Therapist Breathing Exercises](https://www.webmd.com/lung-cancer/features/respiratory-therapist-breathing-exercises-for-lung-cancer-patients): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Michigan Medicine · Progressive Muscle Relaxation](https://www.uofmhealth.org/health-library/ta4146): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [HealthLink BC · Progressive Muscle Relaxation](https://www.healthlinkbc.ca/healthwise/progressive-muscle-relaxation): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [HereToHelp BC / Anxiety Canada · Healthy Thinking for Younger Children](https://www.heretohelp.bc.ca/sites/default/files/healthy-thinking-for-younger-children.pdf): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [YoungMinds · How to make a worry box](https://www.youngminds.org.uk/parent/blog/how-to-make-a-worry-box-a-guide-for-parents/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NHS Every Mind Matters · Tackling your worries](https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/tackling-your-worries/): NHS website content: Open Government Licence v3.0, with stated exceptions. Reference only; no source text or assets bundled. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Just One Norfolk NHS · Worry box](https://www.justonenorfolk.nhs.uk/media/us1bjpvw/worry-box.pdf): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Childhelp · Safe vs Unsafe Secrets](https://childhelp.org/safe-vs-unsafe-secrets-how-to-talk-to-kids-about-the-difference/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [eSafety Commissioner · Secrets and surprises](https://www.esafety.gov.au/sites/default/files/2026-09/secrets-and-surprises-sept-2026.pdf): Australian Government copyright; no blanket open licence verified for this PDF. Fact reference only; no PDF/text/art copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Advocates for Youth · Seeking Help](https://www.advocatesforyouth.org/wp-content/uploads/2023/07/2.5_Seeking-Help_3Rs2023.pdf): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NCMEC · NetSmartz / CyberTipline](https://www.missingkids.org/gethelpnow/cybertipline): Copyright NCMEC, all rights reserved. Facts and service names only; no banner, text or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [US Attorney · Online safety tip sheet](https://www.justice.gov/usao-ri/file/765166/dl): DOJ federal text: public domain unless otherwise marked. No source assets copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [US DOJ · Threats to Children Online](https://www.justice.gov/criminal/media/1437006/dl?inline=): DOJ federal text: public domain unless otherwise marked. Facts independently checked with NCMEC; no logos or illustrations copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NCMEC · Take It Down](https://takeitdown.ncmec.org/): Copyright NCMEC, all rights reserved. Service facts only; no assets copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Childhelp · Responding to a disclosure](https://childhelp.org/what-to-do-if-a-child-tells-you-theyre-being-abused-a-step-by-step-guide/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Childhelp · National Child Abuse Hotline](https://childhelphotline.org/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Michigan Department of Education · Reporting duties](https://www.michigan.gov/mde/services/ed-serv/educator-conduct/abuse-neglect): State of Michigan copyright; fact-check reference only, no source text copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [American Red Cross · Children’s swim lessons](https://www.redcross.org/take-a-class/swimming/swim-lessons/kids-swim-lessons): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [SHAPE America · NHES 2024](https://shapeamerica.org/standards/health/new-he-standards/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.

## Short test and lesson creep
The desk was exercised over more than ten minutes of interactions, including real-duration breathing and muscle practice.
Kid opening unassigned: plausible for trying the worry cloud, baskets and folding; no teacher setup required.
Adult using it: useful for trying the same techniques, but its intrinsic playful depth is narrower than Beat Lab's.
Real material is the interface: comfortable timed breathing, muscle tension/release and a personal rating are usable;
the fictional scenarios are explicitly labelled as examples, never presented as measured psychological data.
No score or finish: yes, proved by the repeated-sort traces and source search. A long-term engagement claim is not made.
The approved models were opened and used in `models/`; a side-by-side reference frame is saved as `comparison.png`.
The safety copy retains "wrong" only for unsafe secrets, adult wrongdoing and telling never being wrong. "Try again"
is optional practice advice. The local variable level is only cloud art size. No goal/score/points/sticker/badge exists.

## Audit
The one required audit finished with exit 0 in ../fix-audit/. Its 42 leads were checked, grouped by cause below.
No console errors, exceptions, disabled-control resize failures or continuously running Motion-off animations were found.
Five held clicks and two quick taps were clean for Sort, Manual, Motion and Read. The 99 audit frames were inspected in
13 contact sheets (`audit-final-sheets/`), with problem frames also opened full size. The audit was not run a second time.

- FIXED, maker text: 9 px at 680x425, 800x500, 1000x625 and 375x812 is now 10 px. Numbers and frames in
  `lead-sort-*.json` and `focused-layout/lead-sort-*.png`; no sideways overflow.
- FIXED, all sorted-card overlap rows across the eight sizes: the audit counted text inside an opacity-zero parent.
  After its flight the card now also has inherited visibility hidden, leaving only the empty slot and thumbnail.
  Focused 680, 800, 1000 and 375 traces show hidden and both result actions visible. The flight still plays normally.
- FIXED, phone Try action: both Try a tool on it and Next worry now precede the optional prose.
  `focused-layout/lead-sort-375.png` and `lead-sort-375.json` show both above the footer.
- FIXED, #meter1 through #meter5 in talk-result, source-result, early-stop-rating and helper-privacy:
  the shared result layout now has at least 44.59 px width in all three compact landscape sizes. Focused meter frames
  and numbers cover 680x425, 800x500, 1000x625, 375x812 and 1366x768. Result text remains readable.
- FIXED, helper-privacy at 680x425 and 375x812: privacy is inside the action block, directly under its buttons.
  It is visible in normal and blocked-storage phone states. `focused-safety/blocked-storage-phone.png` shows both sentences.
- FIXED, phone Manual title/Close bounding overlap: title now clears the floated button, with a 14 px gap.
  `lead-manual-phone.json` and `focused-safety/lead-manual-phone.png` prove it.
- ACCEPTED, the Manual covers #hint: a native modal deliberately covers and makes the desk inert. Its Close button
  is visible and focus returns to Manual; the covered background hint is not a missing instrument control.
- ACCEPTED, missing welcomes on Body clues, Tools, the card and the three baskets: Curiosity policy and the settled
  first-action call supersede this lesson audit expectation. All relevant guidance is available in hints and Read.

The final targeted checks also found and corrected two details: adult reporting source rows are excluded from the
student Manual (zero hotline numbers, 17 relevant references), and the first quiet hint cannot speak over that drawer.
Phone rising-rating advice now fits in full by dropping the redundant phase strip from compact result panels.
`final-result/final-rise-680.png` and `final-rise-375.png` show the grown-up advice, with numbers confirming the full result
above the footer. Reduced-motion folding has zero active slip animations. Final voice parity is still 146/146.
`final-validation.json` contains the final measurements. The source passed `node --check`; the final bundle succeeded.
Successful drive batches have zero console errors. Transient Chrome timeout/connection failures in proof-c.log and
last.log were retained; smaller or successful-profile retries provided the actual passing frames, not inferred passes.
Bundle, drive and audit limits were 120, 300 and 2400 seconds respectively. No audit timeout occurred. Test Chrome ports are closed, the host server is stopped, and temporary host.html was removed. A final keyboard-only Tab/Enter path entered Body clues, then Tools, rated before, started and stopped breathing, and rated after; focus remained on meter3. The grayscale frame retained named baskets and clear controls. See access/final-keyboard.png, access/final-grayscale.png and keyboard-final.json.


## Left open
- Neither the spec nor docs/CURIOSITIES.md assigns this id a Curiosity number or concept entry. The maker's plate has
  the correct family wording and name; plate is null in metadata rather than an invented number.
- The integrator should reconcile the legacy S6 curriculum mapping and spec text with this explicit Curiosity pivot.
  No shared files could be edited in this task. The tool does not claim to teach the removed goal-setting indicators.
- No new cold sensitivity verdict or recorded voice takes were produced; the next exit check remains independent.
- Adult-use appeal is a design judgement, not user research. No clinical benefit or month-long engagement is claimed.
