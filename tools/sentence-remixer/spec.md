# Sentence Remixer

## One idea
The student remixes a paragraph of eight short, choppy sentences about two friends fixing a bike before a race into varied ones on a mixing deck, joining them with and, but, because, when and who or opening with a phrase, while a rhythm strip shows the new sentence lengths; every time a merge causes a pronoun problem (a "she" that could mean Ana or Lena, "Him and me checked the chain", a shift from "you" to "they") the sentence glitches until it is fixed, so they learn to vary sentences without losing who is who.

## Not like
- parallel-parking (9, concept): parallel structure. Here sentence variety and pronouns, grade 6.
- sentence-diagram-builder (7, concept): clause types as a tree. Here combining for rhythm.
- comma-chameleon (4, spec): commas. Here combining and pronouns.
- pause-and-break (6-8, spec): punctuation as pauses. Here sentence patterns.
- grammar-garage (4, spec): grade 4 grammar. Here grade 6 pronouns.

## Who and how
- Grade 6, ELA, module "Pronouns and Sentence Variety" (Language). Standards: L.6.1 (a, b, c, d, e), L.6.3 (a, b).
- Driver: one student (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap.
- Change note (spec fix, 2026-11-10): the deck, DJ Fader, the rhythm strip and the glitches stay. Added: Fader remixes a short sample first as the model; glitch fixes are typed, not picked, and a second miss is logged; after each paragraph a Sound check tape of eight lines with five planted slips and no stripes, which the student must find and fix, so each pronoun skill and the tone skill get five or more items that differ (object and possessive case, reflexive against intensive, other shifts, unclear it, they and this); three more remix moves and a joiner check, so variety is about meaning and not only length; a fifth paragraph; Grandpa Joe's lines are marked as a set, informal forms that slip into narration are found and fixed, and the student writes the same news two ways. The sensitivity read is left for the fresh reader at final review; no wording about Grandpa Joe was changed.
- Five paragraphs: The Bike Race, The Bakery, The Storm Drill, The Science Fair; a fifth with Grandpa Joe's voice. Each is followed by a Sound check tape. One paragraph and its tape a sitting. tool.json `modes: ["Remix", "Three ways"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the before-and-after paragraph and the glitch log.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| L.6.1a | ensure that pronouns are in the proper case (subjective, objective, possessive) | the student | Type the fix for a case glitch after a merge; on each tape find the case slip with no stripe and type the fix | 1 glitch and 5 tape slips (2 subject, 2 object, 1 possessive) | the glitch and the typed fix | 2 |
| L.6.1b | use intensive pronouns | the student | Type the intensive pronoun where the meaning needs it; on each tape fix a -self slip or say whether a -self word is intensive or reflexive | 1 glitch and 5 tape items | the pronoun and its picture | 2 |
| L.6.1c | recognize and correct inappropriate shifts in pronoun number and person | the student | Fix a shift after a merge; on each tape find the shift with no stripe and type the fix | 1 glitch and 5 tape slips (3 person, 2 number) | the glitch log | 2 |
| L.6.1d | recognize and correct vague pronouns | the student | Say who a vague pronoun could mean, then type the fix; on each tape find an unclear she, it, they or this | 1 glitch and 5 tape slips | two flashing pictures and the fix | 3 |
| L.6.1e | recognize variations from standard English in their own and others' writing and speaking, and use strategies to improve expression in conventional language | the student | Mark Grandpa Joe's lines as a set; find five informal forms that slipped into narration, pick a strategy and type the standard form; write the same news two ways | 8 lines, 5 slips, 2 notes | the paragraph with voice marks | 4 |
| L.6.3a | vary sentence patterns for meaning, reader or listener interest, and style | the student | Remix with joiners, phrase openers, splits, a moved clause and a question; pass the joiner check; say what one change did for the reader | 5 paragraphs | the rhythm strip before and after | 5 |
| L.6.3b | maintain consistency in style and tone | the student | Fix slang dropped into narration; on each tape find the tone slip with no stripe | 1 glitch and 5 tape slips | the tone glitch | 6 |

## Screens and modes
Header (kit): title "Sentence Remixer"; `Remix`, `Three ways`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A DJ mixing deck with eight sentence tracks stacked like faders, the rhythm strip under them (all bars the same short length), and DJ Fader, a fox in big headphones. First hint: "Tap a sentence to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Fader's mix (the model).** DJ Fader remixes a four-sentence sample: merges two with "because" and says why that word ("The second one is the reason for the first"), hits a vague "he", names the two people it could mean, types the fix, then leaves one short sentence alone "for punch". It cannot be skipped the first time and `Fader's mix` reopens it.

**Remix.** The student selects two adjacent tracks and picks a joiner (and, but, so, because, when, while, who, which) or "open with a phrase" (the second sentence's time or place phrase moves to the front of the first). Three more moves work on one track: `Split` (a long sentence into two), `Flip` (move the when or because part to the front) and `Ask` (turn a statement into a question to the reader, offered where the data has one). Each combination is built from data: every pair of sentences has its merged forms written out, including the ones that cause glitches. The rhythm strip updates.

**Joiner check.** Some joiners make a sentence that reads smoothly but says the wrong thing ("Dad checked the chain because I checked the chain too."). These carry no stripe. Before Finish the student reads the remix and taps `Makes sense` or `Wrong link` on each merged sentence; a merged sentence keyed as a wrong link that is passed as fine is read back with "Is the second part really the reason?" and must be redone.

**Glitches.** A sentence with a problem shakes and shows a glitch stripe (Motion off: a stripe only):
- Vague: "Ana handed Lena the wrench, and she tightened the bolt." Two pictures flash (Ana tightening, Lena tightening); the student fixes it with a name chip or by picking a rebuild.
- Case: merging "Dad checked the chain." and "I checked the chain too." offers "Him and me checked the chain."; fix to "He and I".
- Shift: "If you want to win, racers have to check their tires."
- Intensive: a sentence where the meaning needs "herself" (no one helped Lena); the picture shows Lena alone.
- Tone: a remix choice that drops "lol it was totally broken" into the narration.
A fix is typed into the sentence (a name, a pronoun or a few words), not picked from chips; the data lists the accepted forms. A wrong fix keeps the glitch and can be tried once more; after a second miss Fader types it, the log says "Fader fixed it", and a slip of the same kind is added to the next tape. For a vague glitch the student first taps the two people the pronoun could mean.
The glitch log names each fix.

**Sound check.** After each paragraph, a tape of eight new lines plays with five slips in it and no stripes: one case, one -self word, one shift, one unclear pronoun, one tone slip (in the fifth tape the tone slip is informal grammar in narration). The student has five marks and `Check`. The check says how many marks are on a slip, not which; marks can be moved and checked once more, then the missed ones are shown and logged "shown". For each found slip the student types the fix. For the -self word the student may also be asked "Can you lift it out and still have a sentence?" to tell intensive (yes) from reflexive (no). Three lines on every tape are clean.

**Grandpa Joe.** The fourth paragraph includes Grandpa Joe, who talks the way people in his town do ("We was fixing bikes before you was born"). The student marks all eight lines as his dialogue (keep his voice) or narration (standard forms), then taps `Check`, which gives a count for the set; one more check, then the missed lines are shown. Changing his dialogue is answered with "That's how Grandpa Joe talks. His voice belongs in his own words." Across the paragraph and its tape, five informal forms have slipped into the narrator's lines. The student finds each, picks the strategy that would catch it (read it aloud; check the subject and its verb; swap in the word a report would use) and types the standard form.

**Two ways.** Last, the student writes the race result twice, three sentences each: as a text to a friend and as a report for the school paper. A model pair about a different event (a bake sale) and a guide sit beside the boxes: the text sounds like me; the report uses standard forms; both give the same facts. The student then underlines two places where the two differ. The tool cannot mark this, so the model and the guide do that job, and both print.

**Finish.** The remixed paragraph reads aloud; a before-and-after rhythm strip and the glitch log show what changed. The student picks one change and finishes the line "I changed this so the reader would ___" from four endings (know why; feel the hurry; see what came first; stop on the big moment) or their own words.

**Three ways.** The same paragraph remixed three times; the strips compare.

At 1366x768 the deck and strip fit; at 680x425 the strip is under the deck.

## Content
Written for Curio Class: five paragraphs of 8 sentences each; for each adjacent pair, all joiner forms with glitch tags and wrong-link tags; split, flip and ask forms where they exist; pictures for vague and intensive glitches; the four-sentence model sample; the bake sale model pair.
- Five Sound check tapes of 8 lines with 5 keyed slips each and accepted fixes:
- Case: "Me and Ana oiled the gears." (Ana and I); "The judge gave ribbons to Lena and I." (Lena and me); "Him and his sister baked all night." (He and his sister); "Between you and I, the drill was too long." (you and me); "The winning poster was her's." (hers).
- Self words: "Dad and myself loaded the van." (Dad and I); "The baker frosted every cake himself." (clean; intensive); "Ana taught herself to weld." (clean; reflexive); "The principal opened the door." where the next line says no one was sent to do it (the principal herself); "Give the forms to Mr. Okafor or myself." (or me).
- Shifts: "When we race, you have to watch the turns." (we have to); "A baker gets up early, and they knead the dough first, but then you rest it." (they rest it); "If someone hears the siren, we should walk." (they should walk); "The riders lined up, and he waited." (they waited); "The racers each checked his tires." (their tires).
- Unclear pronouns: "Lena told Ana that she had won." (name the winner); "The van hit the cone and it tipped over." (the cone); "They say the storm will pass." (the forecasters); "The oven broke and the order was late. This upset the baker." (the late order); "Take the tire off the bike and clean it." (the tire).
- Tone and informal forms in narration: "The race was, like, super close."; "The bread came out kinda weird."; "Everybody was freaking out in the hall."; "The judges were totally blown away."; and for the fifth tape "The racers was lined up by nine." Other informal forms in the Grandpa Joe narration: "ain't", "gonna", "real quick", "them bikes".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Merges can be split back.
- The rhythm strip shows word counts as numbers above each bar.
- Done needs no open glitches and sentences in all three length ranges (short under 8, medium 8 to 15, long over 15 words).

## Look
- Accent `--brand` #0d6e8a mixer cyan (header, deck, faders); gold #f4c542 (rhythm bars, fixed glitches); paper #f0f7fa; ink #062431; muted #475c66. Scene: a small bedroom DJ desk.
- Contrast (WCAG 2.1, computed): white on brand 5.81:1; brand on paper 5.36:1; ink on paper 14.86:1; muted on paper 6.48:1; ink on gold 9.90:1.
- Never color alone: glitches show a stripe and a label; bars show numbers.
- Different from this batch (studio slate, camera purple, raspberry, press olive).

## Art
- People art goes to Gemini: Ana (a Mexican American girl about 11 in a bike helmet), Lena (a white girl about 11 with a wrench), Grandpa Joe (an older white man from a rural town, flannel shirt); each in the vague and intensive pictures (8 pictures); "children's book illustration <scene>, warm gouache, no text"; 4:3.
- Local FLUX (`scripts/localart.py`): DJ desk (1); DJ Fader (4 poses), "A friendly fox DJ with big headphones at a mixing deck <pose>, soft gouache, plain white background"; 1:1; cutout yes; paragraph scenes (3: a bike race start, a bakery counter, a school hallway during a storm drill, no people).
About 16 images. Drawn in code: deck, strip, glitch effect.

## Voice
Bank voice `warm-teacher` as DJ Fader and the paragraph reader (unique in this batch); Grandpa Joe's lines are `friendly-dad` (unique in this batch). `Curio.voice` with `scope: () => state.paragraph + ':' + state.track`, `welcomeAfter: true`.
- how `welcome`: "Eight sentences, all the same length. Remix them, and keep track of who's who."
- event, whole, `sentence`: the tapped sentence.
- event `vague`: "Who tightened the bolt, Ana or Lena?"
- event `caseFix`: "{He and I} checked the chain."
- event `shift`: "{You}, then {racers}. Pick one."
- event `voiceBelongs`: "That's how Grandpa Joe talks. His voice belongs in his own words."
- event `finish`: the paragraph, read whole.
- how `typeFix`: "Type the fix right in the sentence."
- how `tape`: "Five slips are hiding in this tape. Mark them. Then tap Check."
- how `link`: "Read each joined sentence. Does the link make sense?"
- how `twoWays`: "Write it as a text to a friend. Then write it for the school paper."
- event `wrongLink`: "Is the second part really the reason?"
- event, whole, Fader's mix.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: pairwise merge data with glitch tags, rhythm strip, glitch log, voice marks.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Variety | Merge everything into one sentence | Done needs short, medium and long sentences, at least three kinds of move, and the joiner check passed. |
| Joiner check | Tap Makes sense on all | Wrong links passed as fine are read back and must be redone. |
| Glitches | Try fixes until one sticks | Fixes are typed; a second miss is logged "Fader fixed it" and adds a slip to the next tape. |
| Sound check | Mark every line | Five marks for eight lines, checked as a set with a count only; a second miss logs "shown"; each found slip still needs a typed fix. |
| Grandpa Joe | Standardize everything; flip labels until right | Changing his dialogue is turned back with a reason; labels are checked as a set with a count. |
| Two ways | Type the same thing twice | The student must underline two differences; both versions print beside the model. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. First visit: Fader's mix (whole). Tap a sentence: `sentence`, `welcome` (queued, first time).
2. Merges: glitches `vague`, `caseFix`, `shift` as they fire; `typeFix` on the first glitch.
3. Grandpa Joe: `voiceBelongs` as it fires; `twoWays`.
4. `link`; `wrongLink` as it fires. Finish: `finish`. Then `tape`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.6.1 (a to e) and L.6.3 (a, b) wording | thecorestandards.org, Language Grade 6 | CCSS ELA 2010 PDF | yes |
| Subject pronouns (I, he) are used in compound subjects; intensive pronouns end in -self or -selves | Purdue OWL, pronoun case | Merriam-Webster, intensive pronoun | yes |
| Sentence combining builds variety and is effective for teaching syntax | Graham and Perin, "Writing Next" (2007), Carnegie Corporation | Reading Rockets, sentence combining | yes |
| Regional and informal varieties of English are rule-governed ways of speaking | Linguistic Society of America, statement on language varieties | Center for Applied Linguistics, dialects in schools | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: Grandpa Joe's English is presented as a real way of speaking that belongs in his dialogue, never as wrong speech; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b18, 2026-11-09): the sample bike paragraph has 8 sentences of 4 to 7 words; one sample remix reaches short, medium and long ranges; contrast as in Look.

Spec fix checks (2026-11-10): counted, not run: five tapes with one slip of each of five kinds give 5 case (2 subject, 2 object, 1 possessive), 5 -self items (3 slips, 2 clean ones to sort), 5 shifts, 5 unclear pronouns and 5 tone or informal slips; 8 lines less 5 slips leaves 3 clean lines a tape. Two -self lines are clean on purpose, so those tapes carry a second slip of another kind to keep five; Build sets which. Singular "they" after "someone" is accepted as standard in the keyed fixes.

## Done when
1. Focus and fold: at 1366x768 deck and strip fit; at 680x425 the strip is under the deck.
2. Case, intensive and shift glitches fire and take a typed fix; each of five tapes hides one slip of each kind with no stripe. (L.6.1a, b, c)
3. Vague pronoun glitches flash two pictures and take a typed fix; each tape hides an unclear pronoun. (L.6.1d)
4. Grandpa Joe's lines are marked as a set and kept; five informal forms in narration are found and fixed with a strategy; Two ways is written. (L.6.1e)
5. The rhythm strip shows variety; done needs three ranges, three kinds of move and the joiner check. (L.6.3a)
6. Tone glitches fire for slang in narration, and each tape hides a tone slip. (L.6.3b)
7. Fader's mix plays first and can be reopened.
8. Three ways compares strips; Print shows before and after with the log, the tapes and Two ways.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: glitches show a stripe only; no network requests.

## Open questions
- None for Cory.
