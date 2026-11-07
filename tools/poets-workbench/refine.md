OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 4 (general 1, family 3), should fix 18 (general 6, family 12), polish accepted 11

# Refine: poets-workbench

Lens files: `refine/teaching.md`, `refine/play.md`, `refine/craft.md`. Frames: Teaching in
`S:/CurioClass-codex-scratch/poets-workbench/teaching/frames/`, Play in `.../play/`, Craft in `.../craft/frames/`,
shared audit in `.../audit-r1/`. Integrator spot-checks (2026-11-05): `BLOCKED` at src.html:287-290 is about 70 words
and "coon" shows in the default Perfect list for "moon" (craft `frames/moon-drawer.png`); `lengthName` at
src.html:406 prints `feetCount.toFixed(1)+' feet'`; the two-letter labels at src.html:424 are joined with no gap at
src.html:469; `#mirror` has a `transform` (own stacking context) and `#editor` comes after it, so `.proof{z-index:3}`
cannot lift the marks over the textarea (src.html:74-75, 84). All four claims hold.

## Blocker

1. **The rhyme drawer offers slurs and explicit words as rhymes for everyday words.** `BLOCKED` src.html:287-290,
   `rhymeList` src.html:581-596; every drawer kind. "moon" lists coon (in the common-words tier, on screen without
   scrolling), coons, spook, redskin, douche; "like"/"bike" list dyke, gook, polack; "map" lists jap, japs, rape, wop;
   "top" lists wop, darkie, nazi; "hit"/"pick" list tits, prick, redskin, niggard (craft `frames/moon-drawer.png`,
   `frames/like-drawer.png`, `s2.json`: 13 of 72 common test words surface at least one). Rule 6. Fixed looks like:
   (a) a broad classroom offensive-word filter (ethnic, racial, religious, disability, LGBTQ and Native slurs, sexual
   and explicit terms, expletives and their spelling variants and plurals), not a few added words; (b) the words are
   dropped at pack time in the Scratch pack script, so the shipped bundle neither offers them nor lists them in view
   source (this takes in Craft's polish item 9: no slur list in plain text in a public K-12 page or repo); (c) a check
   script in Scratch that runs the Perfect, Same vowel and Same ending lists of every word in the SCOWL common tier
   (and at least moon, like, bike, map, top, hit, pick, late, spot, night, ball, back) against the filter and fails on
   any hit; its output and the final filter list go in notes.md for the exit check. (d) The final filter list goes to
   the fresh-agent sensitivity review (rule 5: it touches Native, ethnic and LGBTQ terms); its PASS is part of the
   gate. Keep the spec's "names stay" rule for ordinary names; a surname that is also a slur goes. (general)

2. **"here"/"hear" do not rhyme with "near", "year", "fear", so Frost's scheme and the drawer are wrong.**
   `pronunciation()` src.html:322 (rhyme keys), `poemAnalysis` src.html:414-428, Manual src.html:840. CMU writes
   here, hear, ear, tier, we're as `IY1 R` (31 entries) but near, year, fear, dear, clear, queer as `IH1 R` (192), a
   dictionary inconsistency, not a real difference in American speech. Seen: Stopping by Woods, the default poem,
   reads `AABA CCDC DDED EEEE` (teaching `t-frost.png`), so Done when 5 fails; the drawer for "hear" lists 34 perfect
   rhymes, mostly surnames, without fear, near, dear, year, clear (`t-hear.png`); a student's own couplet "standing
   here / have you near / sky is clear / another year" reads ABBB (play q09). The Manual note calls the split
   "strict" hearing, which tells students two words they say alike sound different. Fixed: fold `IY R` into `IH R`
   when building rhyme keys (and check the other pre-R vowel pairs CMU mixes the same way), state it in the Manual as
   a normalisation like primary and secondary stress, drop the "strict" note. Frost reads AABA BBCB CCDC DDDD.
   (family:curiosity)

3. **Meter names with fractions of a foot: "anapestic 2.7 feet", "trochaic 3.5 feet".** `scanLine` src.html:405-407.
   227 of 529 shelf lines show a decimal; 85 show thirds (teaching `meters-out.json`). The Tiger: 12 of 24 lines
   "trochaic 3.5 feet"; The Raven: 42 lines "trochaic 7.5 feet"; Invictus "anapestic 2.7 feet"; every classic
   limerick line "anapestic 2.7 feet" even with the Anapest lens on (play q07-limerick-frame.png); "trochaic 39.0
   feet" on a long line (play p15). A grade 7 student learns meter comes in fractions: a meter that misleads when its
   assumption fails. Fixed: name the length from whole feet or stressed beats and say the remainder in words
   ("trochaic tetrameter, last syllable dropped", "anapestic trimeter, missing its first syllable", "iambic
   tetrameter + 1 extra"); never print a decimal; very long lines say "N feet" with a whole number. (family:curiosity;
   Play tagged it general)

4. **The rhyme-scheme strip runs two-letter labels together into a false scheme.** Letters src.html:424, strip
   src.html:469. After Z the letters go AA, AB..., joined with no gap, so The Raven's last stanzas read
   `AABABBBB AABACBBB ADBJBBB AEBAFBBB`, which looks like 8- and 7-line stanzas in a poem of 6-line stanzas (teaching
   `t-raven-end.png`); Paul Revere's Ride the same. Fixed: separate letters inside each stanza group when any label
   has two letters (A·B·AB), or restart lettering where the reader needs it; margin letter and strip use the same
   form. (family:curiosity)

## Should fix

1. **Tapping a stress mark does not flip it; it opens the rhyme drawer.** `.proof` src.html:84-88 under `#editor`
   src.html:75; handler src.html:928-936. `elementFromPoint` on a mark returns the editor; a click on the "/" over
   "woods" placed the caret and opened the drawer, mark unchanged (craft `frames/proofclick-after.png`). The spec
   control, Things to do 5 and the Manual all promise it. Fixed: lift the marks above the editor (z-index on
   `#mirror` with `pointer-events:none` on everything but `.proof` buttons) so a tap on a mark flips or steps it.
   (general)

2. **Read does nothing visible and carries a build note.** `$('read').onclick` src.html:1042-1050; Manual
   src.html:824-825. With no clip (expected until the Forge, BASELINE rule 18), Read only changes a tooltip and puts
   "Type a line. The recorded hint is not supplied in this build." in the live region; the hint stays hidden
   (play p17-read-press, craft `read-after-typing` in `s3.json`, `vlog` empty). The Manual says Read "shows and
   announces the hint as text", which is not true. Fixed: until the clip lands, Read shows the hint on the page again
   and announces only "Type a line."; remove "not supplied in this build" from the Manual, tooltip and live region
   (it belongs in notes.md). (family:curiosity; Play tagged it general)

3. **Play is silent on the default screen.** The caret opens on the empty line under the Frost line, so the red Play
   key only announces "This line is silent..." to the live region; nothing is seen or heard (play q05-play-mid.png,
   `playing:false`; with the caret on line 1 it works, r01-play-line1.png). Fixed: on an empty line Play taps the
   nearest line above with words (or the poem), so the first press always makes sound and light. (general)

4. **Long poems drop well below 60 fps while typing.** `render()` src.html:450-522 re-scans every line and rebuilds
   the whole mirror 60 ms after each key. The Raven: about 20 ms per render unthrottled, 131 ms at 4x CPU throttle;
   typing into it at 4x, 61 of 208 frames over 33 ms, p95 122 ms (craft `scripts/throttle.py`, `typing` in
   `s2.json`). Fixed: cache `scanLine` by line text, lens and overrides, and patch only changed `.verse` nodes; re-run
   the 4x throttle on The Raven and report p95. (family:curiosity)

5. **One-syllable words with two pronunciations can never be corrected.** src.html:613-614. Stress and Alt F only
   flip stress for one-syllable words; they never step tears (T EH1 R Z / T IH1 R Z), wind, read, lead, live, bow,
   close to their other pronunciation, and the rhyme letter takes whichever variant fit the meter. Invictus reads
   ABAB CDCE FGHG IBIB (tears/years split, unbowed takes B OW1 D against aloud); flipping "tears" left the scheme
   unchanged (play q04-invictus-tears). Fixed: step such words through their pronunciations (then stress), and let
   an end word prefer a variant that rhymes with a nearby line end. (family:curiosity)

6. **Names read stressed on both syllables (secondary stress counted strong).** CMU gives many names a final `IY2`
   (cory `K AO1 R IY2`; 552 entries end `IY2`), so Cory, Kylie, Aiden show `/ /` and Aaliyah `/ / /` (teaching
   `t-name.png`, play p05); "midnight" costs The Raven's first line a match. Things to do 1 is "type your name".
   Fixed: treat secondary stress as flexible (follows the meter, like free function words, shown as such), or at
   least a word-final `IY2` in a two-syllable word as weak; say so in the Manual. (family:curiosity; Play rated it
   polish, general)

7. **Common words outside the dictionary get first-syllable stress and break shelf lines.** `variants()`
   src.html:339-347. "unconquerable" scans /xxxx and Invictus falls to a fractional meter; Paul Revere's Ride has 21
   unknown words, most made of known parts: hyphenated compounds (pea-green, hoof-beats, to-night, belfry-tower),
   possessives (bosom's, demon's, sentinel's), old -'d endings (mock'd, stamp'd, untrimm'd) (teaching
   `meters-out.json`). Fixed: look up hyphenated parts separately, drop 's, read -'d as the -ed word minus a
   syllable; real coinages (brillig) stay guessed and dotted. (family:curiosity)

8. **In Auto, a poem's meter name changes from line to line.** `scanLine` per line, src.html:361. The Road Not Taken
   (iambic tetrameter) names 9 meters in 20 lines and "dactylic trimeter" (6 lines) outnumbers "iambic tetrameter"
   (4); Ozymandias puts 4 of 14 lines in "dactylic 3.3 feet" (teaching `t-road.png`, `meters-out.json`). Fixed inside
   the spec's rule (the line takes the foot that matches most syllables): break ties toward the poem's most common
   foot, and show the poem's meter in the top strip ("mostly iambic tetrameter") so a line that differs reads as a
   variation. The bigger change (judge every line against the poem's foot by default) is under the spec's open
   questions. (family:curiosity)

9. **Sounds shades nearly every word, so The Raven's inner rhymes cannot be found.** src.html:474-485. Assonance
   counts function words and uses one plum for every repeated vowel over the whole word box including its marks: 408
   words shaded on The Raven (play p06-raven-sounds.png, teaching `t-sounds-raven.png`); on "Peter Piper" the IH and
   EH pairs look the same (play q08-sounds-simple.png); function words "alliterate" ("The ... the"). Things to do 8
   and 9 depend on it. Fixed: leave free function words out, one ink per repeated vowel (dreary/weary one,
   napping/tapping/rapping another), shading at text height only, and mark rhymes inside a line (same perfect key)
   distinctly. (family:curiosity; Play rated it polish)

10. **The alliteration underline is the same green as rhyme family B.** `.word.allit` src.html:82 and `COLORS[1]`
    src.html:275 used by `.word.ending`. With Sounds on, B end words and alliterating words carry identical green
    underlines ("lore" and "quaint", "curious", "forgotten" in The Raven, craft `frames/raven-sounds.png`); assonance
    is colour only. Fixed: draw alliteration as a distinct mark (bracket or dotted mark at the first letter, not an
    underline), keep it out of the rhyme inks, and give assonance a shape as well as a colour. (general)

11. **Paper guides are drawn on top of the syllable count.** Left margin, haiku, limerick, common, sonnet. The faint
    guide number or letter overprints the count, so 5 against 5 or 8 against 6 is a smudge (play q06-zoom-margin.png,
    q07-zoom-margin.png, r05-sonnet-paper.png). Fixed: guide beside the count ("5 / 5") or in its own column; letters
    for limerick and sonnet beside the rhyme letter. (family:curiosity)

12. **Paper guides count blank lines.** `guideFor(li)` src.html:430 uses the raw line index, so a stanza break takes
    a guide slot: Sonnet 18 on sonnet paper puts "C" on the blank line and every later letter is off by one (play
    r05-sonnet-paper.png); common meter on Dickinson would shift to 6, 8, 6, 8 after the first break. Fixed: count
    only lines with words; haiku and limerick restart at each stanza. (family:curiosity)

13. **Replace word is on by default.** `state.replace:true` src.html:274; drawer. Tapping "spot" for "I like to eat
    my pizza hot" gives "I like to eat my pizza spot" (play q03-insert-spot). The spec says Enter "inserts at the
    caret". Fixed: default to inserting at the caret as it was before the tap (or at the start of the next line),
    Replace as the option. (general)

14. **The drawer buries common rhymes under surnames.** Groups sort by syllable count first, so the one-syllable
    group of "hot" holds 154 entries and turns to surnames by row five (baht, bhatt, bott, brott; play
    q02-click-hot.png); "think" reaches cinq, finck, hinck within five rows (p13-midline-click.png); forgot and apricot
    sit below about 150 names. Fixed, keeping the spec's syllable grouping: the common-words tier grouped by syllable
    count first, then one "Names and rare words" fold (also grouped) after it. (family:curiosity)

15. **The pronunciation readout has no key.** Drawer head `#phones` src.html:603; Manual. "HH IY1 R" and "/ x · 2/3"
    are never explained, though the Manual's own facts use the symbols ("tea has IY"). Fixed: a short Manual key
    (digits 1 main, 2 second, 0 none; a small table of vowel symbols with example words) and label the index on
    screen ("pronunciation 2 of 3"). (family:curiosity)

16. **Alt R and Alt F do not work on a Mac.** src.html:1028-1029 test `event.key`; Option+R gives "®" and Option+F
    "ƒ", which also get typed into the poem. Found by reading code (no Mac here). Fixed: test `event.code` 'KeyR' and
    'KeyF'. (general)

17. **Form is shown but never linked to meaning (RL.7.5), and notes overstate RL.7.4.** Manual "Things people have
    found" src.html:839 ("its final two lines repeat" stops short of why). Fixed inside the Curiosity shape: a few
    found-entries that join form to meaning (Frost's repeated last line; the short "In Flanders fields." line;
    Sonnet 18's couplet turning to "So long lives this"; "Nevermore" closing every Raven stanza), each sourced, plus
    one form question in notes.md "Talk together"; notes.md "What it teaches" says "the sound half of RL.7.4". No
    goals or prompts on the desk. (general)

18. **Stray ":," marks in two shelf texts.** material.json: The Raven line 26 "here I opened wide the door:,";
    Annabel Lee line 37 "Of the beautiful ANNABEL LEE:,". Left by the dash clean-up. Fixed: one mark each, checked
    against the source text (a semicolon or colon, no em dash). (family:curiosity)

## Polish accepted

1. **The match count counts free syllables.** src.html:408. "I hear the rain" reads 4 of 4 because free words always
   match. Better: count fixed syllables and show free ones ("6 of 6 · 2 free"). (teaching P1)
2. **Manual wording above grade 7.** src.html:804-836 ("compares a foot at each starting offset", "a universal
   account of speech"). Plain sentences with an example word each. (teaching P2, general)
3. **Content notes under a builder heading.** notes.md "Review care points" mixes shelf content (death, grief, war,
   Hughes) with layout notes. Move the content to a "Content notes" line in Good to know (BASELINE parent-preview
   call); drop the build notes. Not a request for a shelf review. (teaching P3, general)
4. **Unstressed-only forms in perfect rhymes.** "the" (`DH IY0`) ranks high for "tea", "a" for "obey", because a word
   with no stressed vowel falls back to its first vowel (src.html:322-324). Leave unstressed-only forms out of
   perfect rhymes. (teaching N1, family:curiosity)
5. **A click to place the caret reflows the desk twice.** Editor click src.html:919-927 opens the drawer on any click
   in a word; the page narrows 50 px and shifts (848 to 798 wide, 293 to 198 px left), then moves back on the next key
   (play p13-midline-click.png, craft `clickword` in `s2.json`); at 680x425 the tapped word wraps under the drawer
   (play p20-680-drawer.png). Better: the drawer opens over the desk edge without resizing the page grid. (Play 11 +
   Craft 8, general)
6. **Empty page says nothing.** After clearing, the "Type a line." hint never returns and Play and Rhymes answer only
   in the live region (play p14-empty). Bring the hint back whenever the page is empty. (play 13, general)
7. **Marks just appear.** Only `@keyframes drawer-in` exists (src.html:128); the spec's "marks drop in above it" and
   Done when 7 ("Motion off removes the typebar ... animations") assume one. Add a short drop of a finished word's
   marks, removed by `.calm`. (craft 7, family:curiosity)
8. **Sounds gives no readout when it finds nothing.** On the Frost line Sounds lights and nothing changes (audit
   `state-sound-repeats-1366x768.png`). Add a top-strip readout ("repeats: 0 consonant, 0 vowel"). (craft 10, general)
9. **Provenance wording.** src.html:536 "YOUR PAGE / stays on this device only when saved" reads as if unsaved text
   leaves. Use "YOUR PAGE / not saved" (Drafts already states privacy). (Play 15 + Craft 11, nit, general)
10. **Doubled tempo control.** src.html:221-223: the knob (`role=slider`, tabindex 0) and the range input are two
    sliders for one value. Keep one in the tab order and accessibility tree; hide the other. (craft 12, nit, general)
11. **Drawer kind buttons mix roles.** src.html:253-255 set `aria-selected` and `aria-pressed` on `role="tab"`. Drop
    `aria-pressed`. (craft 13, nit, general)

## Settled calls

- **No shelf poem needs a sensitivity review** (Cory, 2026-11-05, spec open questions). Not re-raised. The only
  sensitivity routing here is Blocker 1's filter list.
- **here/near level:** Teaching rated it a blocker, Play a should fix. Blocker: it is a readout that misleads on the
  default poem and Done when 5 fails (REFINE, "a meter or estimate that misleads").
- **Fractional feet:** both lenses; Teaching blocker, Play should fix. Blocker for the same REFINE rule. Tag
  family:curiosity (it comes from this engine's naming).
- **Sounds overlay and secondary stress:** Teaching should fix, Play polish. Should fix: Things to do 1, 8 and 9 rest
  on them.
- **Read without a clip:** the missing smooth-narrator clip is correct until the collective Forge pass (BASELINE
  rule 18). Do not record or synthesize one; fix only what Read shows and says.
- **The "N of M" readout stays a readout.** Polish 1 refines what it counts; it is not a score and gets no goal,
  colour verdict or praise. Nothing on the list adds a goal, score, level or finish (CODEX-CURIOSITY).
- **Rhyme drawer keeps the spec's syllable grouping** (should fix 14 orders inside it, not across it).
- **SCOWL common-words sort:** already built ("Common words first. Names included." in the drawer); the spec's open
  question is answered by the build. The filter check in Blocker 1 uses that tier.
- **Audit leads that are by design, do not change:** `#editor`/`#hint` overlap, editor focus on load (uses
  `preventScroll`), hint out of view after the first action, Manual and Drafts over the editor (modal dialogs), tempo
  knob "nothing changed" on a plain click (drag and arrows turn it), Print "nothing changed" (headless print dialog),
  shelf books "off screen" and Sympathy "covered" (a scroll list).

## To the spec's open questions

- **RL.7.4's word-meaning half (figurative and connotative language) is taught by no built tool** on
  ela-7-sound-and-form-in-poetry; Poetry Soundboard, the module's lesson card, is still a concept. Rule 2: decide
  whether Poetry Soundboard carries it or the code half moves; log it for the module, not for this Curiosity.
- **Auto meter default:** whether Auto should judge every line against the poem's best foot by default and show a
  line's own closest foot only where it really differs (Teaching S1). Should fix 8 does the in-spec part (ties, poem
  meter in the strip); the default change alters the spec's scansion rule.

## Not taken

- Shelf at 1366x768 with six books below the fold (play 14, nit): it is a labelled scroll list ("THE SHELF / 16");
  smaller spines would cost legibility.
- Hughes "Dark like me" / "Black like me" with "me" marked weak (teaching, Sensitivity): the student can flip it, the
  function-word rule is the spec's, and no shelf review is wanted (Cory, 2026-11-05).
- Separate "hash the block list" option (craft 9): taken into Blocker 1 as dropping the words at pack time instead.
