# Rhetoric Spotter

## One idea
Sorting a speech line into ethos, pathos or logos only counts when you can point at the exact words that do the persuading, so every line you sort asks you to tap those words, and then the whole speech is read back to you with your marks lit as it goes by.

## Not like
- rhetorical-situation-simulator (ela 11, family sibling): changes the audience and moment around a fixed speech. Here the situation is the real one and the work is naming what each line does.
- argument-map (ela 12, family sibling): maps how claims hold each other up. Here each line is judged on its own appeal and device; no structure is built.
- fallacy-field-guide (ela 10): tells bad reasoning from its legitimate lookalike in made-up ads and comments. Here the texts are real historic speeches and nothing is a fallacy hunt; appeals are tools, not faults.
- founding-words-explorer (ela 9): reads founding documents word by word with a period dictionary. Here the texts are speeches and the lens is persuasion, not word meaning.
- audience-shift-briefing (ela 9): the student builds a briefing for three rooms. Here the student analyzes other people's speeches.
- ad-agency (ela 12): persuasion techniques in made-up ads, run as a business. Here the speeches are real and nothing is sold.

## Who and how
- Grade 9 ELA. Module: Rhetoric and persuasion (Reading Informational Text).
- Driver: students on laptops, alone or in pairs; a teacher can project Hear it after the class sorts. 25 to 40 minutes (one speech per sitting; each has 9 or 10 lines).
- Standards: RI.9-10.6 (determine an author's point of view or purpose and analyze how an author uses rhetoric to advance it): Sort (appeals and the words that carry them), Devices, and the purpose line each speech ends with.
- tool.json: driver "students or teacher", minutes "25-40", modes ["Sort", "Devices", "Hear it"], grades_label "Grade 9". Kit starter plus `kit:rhetoric`.

## Screens and modes
Header: title "Rhetoric Spotter", small line "Point at the words that persuade."; speech picker **Henry, 1775** / **Anthony, 1873** / **Roosevelt, 1933**; mode buttons **Sort** (opens first), **Devices**, **Hear it**; Motion, Sound, Read. Each speech opens with a context card (Content) the student closes with **Start sorting**; **Context** reopens it.

### Sort (opens first)
- Stage, top: the line deck: the current line on a large card, with its number ("Line 3 of 10") and the paragraph it comes from (a **Show it in the speech** link opens the full text in a side drawer with the line boxed).
- Stage, bottom: three bins side by side: **Ethos** (◆ "trust in the speaker"), **Pathos** (● "the listeners' feelings"), **Logos** (■ "reasons and evidence"). Each bin has its glyph, its word and a one-line meaning; color is extra.
- The student drags the card into a bin, or taps a bin button under the card (keys 1, 2, 3). **Also fits** lets one more bin be added (a line may sit in two bins, never three).
- Then **Which words do it?**: the line's words become tappable chips; the student taps 1 to 8 words that carry the appeal, then **Done**. The words get the bin's underline style (◆ double underline, ● wavy, ■ solid).
- **Next line** moves on; **Back** returns to any sorted line to change it.
- After the last line, **Compare with one reading** shows, per line, "Same", "Also fair" or "Another reading" (the tool's bins and reason from Content), and "Your words and the reading's words: 3 of 4 the same" with the reading's cue words in a dotted box beside the student's. Words and bins are never marked wrong.
- **Purpose**: the last card asks "What did this speaker want the audience to do or believe?" with three choices from Content (one fits the whole speech, two fit only part of it) and **Why?** reveals the reasoning for each.

### Devices
- The whole speech's sorted lines as a list. Four device tabs: **Anaphora** (repeated opening words), **Antithesis** (opposites set side by side), **Rhetorical question** (a question that expects no answer), **Tricolon** (three parallel parts). Each tab shows a two-line definition.
- For the chosen device, the student taps every line that uses it, then taps the words that make it (the repeated words, the two opposites, the three parts). **Check this device** shows how many of the reading's lines were found ("Found 2 of 3") and lights any missed line with a hint of where to look ("Look at the start of each clause"). No penalty for extras; each extra shows the reading's note if it has one.

### Hear it
- The speech, in order, as lines of text. **Play** reads the sorted lines aloud one at a time in the tool's voice (`rh.play`), lighting each line and showing the student's bin glyph and underlined words as it is spoken, plus any device marks. **Pause**, **Step** and **Stop**. A note under the controls: "Read by the Curio Class narrator, not by the speaker. No recording of Henry or Anthony exists."
- **Show only**: chips **Ethos**, **Pathos**, **Logos** and each device filter which marks are lit, so a student can hear only the pathos lines.
- With Sound off, lines light at reading pace (`est`) so the replay still works silently.

## Content
Exact texts from the named editions (Sources). Source em dashes are shown as "--". Each line: id, text, the reading's bins (first is the main), devices, cue words (the reading's "words that do it") and the reason shown on compare.

### Patrick Henry, Second Virginia Convention, St. John's Church, Richmond, March 23, 1775
Context card: "Henry spoke to Virginia's leaders, Washington and Jefferson among them, arguing that the colony should arm. No one wrote the speech down. This text was put together by William Wirt in 1817, more than 40 years later, from the memories of older men who heard it, so we read Wirt's version of Henry. Henry often called British rule 'slavery'. He himself held people in slavery: 67 enslaved people at his death in 1799."
- H1 "No man thinks more highly than I do of the patriotism, as well as abilities, of the very worthy gentlemen who have just addressed the House." Ethos. Cue: "No man thinks more highly". Reason: he shows respect for opponents so they will hear him out.
- H2 "I have but one lamp by which my feet are guided, and that is the lamp of experience." Logos, also Ethos. Cue: "lamp of experience". Reason: he promises to argue from past facts.
- H3 "Are fleets and armies necessary to a work of love and reconciliation?" Logos, also Pathos. Device: rhetorical question. Cue: "fleets and armies", "love and reconciliation". Reason: the British warships contradict the British promises.
- H4 "They tell us, sir, that we are weak; unable to cope with so formidable an adversary. But when shall we be stronger?" Logos. Device: rhetorical question. Cue: "when shall we be stronger". Reason: he answers the other side's objection with a question it cannot answer.
- H5 "Shall we gather strength by irresolution and inaction? Shall we acquire the means of effectual resistance by lying supinely on our backs and hugging the delusive phantom of hope, until our enemies shall have bound us hand and foot?" Pathos, also Logos. Devices: anaphora ("Shall we"), rhetorical question. Cue: "lying supinely on our backs", "bound us hand and foot". Reason: an image of helplessness makes waiting feel shameful.
- H6 "If we wish to be free-- if we mean to preserve inviolate those inestimable privileges for which we have been so long contending--if we mean not basely to abandon the noble struggle in which we have been so long engaged, and which we have pledged ourselves never to abandon until the glorious object of our contest shall be obtained--we must fight!" Pathos. Devices: anaphora ("if we"), tricolon (three "if" clauses). Cue: "if we", "we must fight". Reason: three building conditions end in one command.
- H7 "Our chains are forged! Their clanking may be heard on the plains of Boston!" Pathos. Cue: "chains", "clanking". Reason: a sound you can almost hear stands in for the British troops in Boston.
- H8 "Gentlemen may cry, Peace, Peace-- but there is no peace." Pathos, also Logos. Device: antithesis. Cue: "Peace, Peace", "no peace". Reason: it sets the hope against the fact.
- H9 "Is life so dear, or peace so sweet, as to be purchased at the price of chains and slavery?" Pathos. Device: rhetorical question. Cue: "price of chains and slavery". Reason: it makes comfort sound like a shameful bargain.
- H10 "I know not what course others may take; but as for me, give me liberty or give me death!" Pathos, also Ethos. Device: antithesis. Cue: "as for me", "liberty or give me death". Reason: he stakes his own life on the choice.
- Purpose choices: "Persuade the convention to arm Virginia now" (fits the whole speech); "Prove that Britain had been unfair for ten years" (part: H2, H3); "Praise the delegates who spoke before him" (part: H1 only).

### Susan B. Anthony, her argument before trial, Monroe and Ontario Counties, New York, spring 1873
Context card: "In November 1872 Anthony voted in the presidential election in Rochester, New York, and was arrested, because women could not vote. Before her trial she gave this speech in 29 districts of Monroe County, then in 21 districts of Ontario County when the trial was moved there, to reach the men who might sit on her jury. At her trial at Canandaigua, which began June 17, 1873, the judge found her guilty and fined her $100. She told him: 'I shall never pay a dollar of your unjust penalty.' Women won the vote nationwide in 1920, fourteen years after her death."
- A1 "I stand before you to-night, under indictment for the alleged crime of having voted illegally at the last Presidential election." Ethos, also Pathos. Cue: "under indictment", "alleged crime". Reason: she names her own risk, which earns attention and sympathy.
- A2 "I shall endeavor this evening to prove to you that in voting, I not only committed no crime, but simply exercised my 'citizen's right,' guaranteed to me and all United States citizens by the National Constitution, beyond the power of any State to deny." Logos. Device: antithesis ("no crime" against "citizen's right"). Cue: "prove", "National Constitution". Reason: she promises a legal proof, not a plea.
- A3 "It was we, the people, not we, the white male citizens, nor yet we, the male citizens, but we, the whole people, who formed this Union." Logos, also Pathos. Devices: anaphora ("we"), tricolon. Cue: "we, the whole people". Reason: she reads the Preamble's own words against those who exclude women.
- A4 "And we formed it, not to give the blessings of liberty, but to secure them; not to the half of ourselves and the half of our posterity, but to the whole people--women as well as men." Logos. Device: antithesis. Cue: "not to give... but to secure", "women as well as men". Reason: two "not this, but that" turns sharpen the claim.
- A5 "To them this government is not a democracy. It is not a republic." Pathos. Device: anaphora ("It is not" / "is not"). Cue: "not a democracy", "not a republic". Reason: short, blunt sentences deny the country's proudest names.
- A6 "Are women persons? And I hardly believe any of our opponents will have the hardihood to say they are not." Logos. Device: rhetorical question. Cue: "Are women persons?". Reason: the question has one answer, and the argument rests on it.
- A7 "Being persons, then, women are citizens, and no State has a right to make any new law, or to enforce any old law, that shall abridge their privileges or immunities." Logos. Cue: "Being persons, then", "privileges or immunities". Reason: a chain of reasoning that uses the Fourteenth Amendment's words.
- A8 "Webster, Worcester and Bouvier all define citizen to be a person, in the United States, entitled to vote and hold office." Logos, also Ethos. Cue: "Webster, Worcester and Bouvier". Reason: she borrows the authority of dictionaries and a law dictionary.
- A9 "An oligarchy of wealth, where the rich govern the poor; an oligarchy of learning, where the educated govern the ignorant; or even an oligarchy of race, where the Saxon rules the African, might be endured; but surely this oligarchy of sex ... can not be endured." (The tool shows the ellipsis and the full sentence in the drawer.) Pathos. Devices: anaphora ("an oligarchy of"), tricolon, antithesis. Cue: "might be endured", "can not be endured". Reason: three lesser wrongs are set against the one she calls worst. A note card opens with this line (see Open questions): "Look closely at what Anthony is willing to call bearable. She ranks rule by race as something that 'might be endured'. In 1873 Black men had won the vote on paper (Fifteenth Amendment, 1870), and Black women had neither the vote nor a place in her ranking. Strong rhetoric can carry a ranking the speaker never argues for."
- Purpose choices: "Convince future jurors that her vote was legal" (whole speech); "Explain what a citizen is" (part: A7, A8); "Describe her arrest" (part: A1).

### Franklin D. Roosevelt, First Inaugural Address, Washington, March 4, 1933
Context card: "Roosevelt took office in the worst year of the Great Depression. Banks were closing and millions had no work. This text is the one the American Presidency Project prints; it notes that the speech as delivered differed in some respects from the printed version."
- R1 "This is preeminently the time to speak the truth, the whole truth, frankly and boldly." Ethos. Cue: "the truth, the whole truth". Reason: he presents himself as an honest witness.
- R2 "So, first of all, let me assert my firm belief that the only thing we have to fear is fear itself--nameless, unreasoning, unjustified terror which paralyzes needed efforts to convert retreat into advance." Pathos. Device: tricolon ("nameless, unreasoning, unjustified"). Cue: "fear is fear itself". Reason: he names the audience's feeling as the real danger.
- R3 "Values have shrunk to fantastic levels; taxes have risen; our ability to pay has fallen" Logos. Device: tricolon. Cue: "shrunk", "risen", "fallen". Reason: a plain list of facts the audience already knows.
- R4 "Yes, the money changers have fled from their high seats in the temple of our civilization." Pathos. Cue: "money changers", "temple". Reason: a Bible image casts the bankers as the ones Jesus drove from the temple.
- R5 "Happiness lies not in the mere possession of money; it lies in the joy of achievement, in the thrill of creative effort." Pathos. Device: antithesis. Cue: "not in... money", "joy of achievement". Reason: it turns loss of money into a lesson about values.
- R6 "This Nation is asking for action, and action now." Pathos, also Ethos. Cue: "action now". Reason: he speaks as the voice of the nation's demand.
- R7 "It can be helped by preventing realistically the tragedy of the growing loss through foreclosure of our small homes and our farms. It can be helped by insistence that the Federal, the State, and the local governments act forthwith on the demand that their cost be drastically reduced." Logos. Device: anaphora ("It can be helped by"). Cue: "It can be helped by". Reason: a list of concrete measures.
- R8 "We must act. We must act quickly." Pathos. Device: anaphora. Cue: "We must act". Reason: two short sentences make urgency audible.
- R9 "They have made me the present instrument of their wishes. In the spirit of the gift, I take it." Ethos. Cue: "instrument of their wishes". Reason: his power is framed as the people's gift.
- Purpose choices: "Give a frightened country confidence that he will act" (whole speech); "Blame bankers for the Depression" (part: R4); "List the country's problems" (part: R3).

## Interactions in detail
- Dragging is optional everywhere: every drag has a tap and keyboard path (Tab to a line, 1/2/3 for bins, Space to add a second bin, W to start word picking).
- A line in two bins shows both glyphs; its first bin is the main one. A third bin is refused with "Two is the limit. Which matters most?"
- Word picking: tapping a picked word unpicks it; a ninth word is refused with "Pick the few words that carry it." Compare uses `rh.cueOverlap`; punctuation is never a word.
- Compare is enabled after every line has a bin and words; **Show it now** (second press) reveals early. Answers per speech are kept in localStorage `rhetoric-spotter:v1` (try/catch) with **Start this speech over**.
- Devices: a line found for a device it doesn't use shows the reading's note if any (for example H8 under Tricolon: "Two parts, not three"), else "The reading doesn't count this one. Do you?" with no penalty.
- Hear it with unsorted lines: they play with no glyph and a grey "not sorted" tag. Mode or speech change calls `V.hush()` and stops the Player.
- Sizes: at 375 wide the bins stack under the card as three full-width buttons; the drawer becomes a full-screen sheet with **Close**. No horizontal page scroll at any listed size.

## Look
- Own light `:root`, a podium in morning light: `--paper #f5f7ff`, `--panel #ffffff`, `--ink #141a33`, `--muted #4f5875`, `--line #d5dbef`, accent `--brand #1947ff` (electric podium blue: header rule, active mode, Compare, the light that moves through Hear it), `--btn #1947ff`, `--btn-line #8b97c4`, `--head-ink #ffffff`, `--focus #c2410c`. Bin tints: Ethos `#dbe4ff`, Pathos `#ffe0e6`, Logos `#dff5e8`; Hear it current-line light `#fff3b0`. Glyphs and underline styles carry the meaning; tints are extra.
- Neighbors: satire-decoder oxblood and usage-panel ink red (dark), research-notebook fountain-pen blue `#2348a6` (dE 51, much duller), fake-or-fact-lab violet (dE 19.1), argument-map cyan (dark).
- Contrast (WCAG 2.1): white on brand 6.20:1; brand on paper 5.80:1, on panel 6.20:1; ink on paper 16.02:1; muted on paper 6.58:1, on panel 7.03:1; focus on paper 4.84:1, on panel 5.18:1; ink on Ethos tint 13.51:1, Pathos 13.92:1, Logos 14.99:1, current-line light 15.26:1. All pass AA.

## Art
None: drawn in code (cards, bins, glyphs). No portraits, so no speaker is pictured from a modern likeness.

## Voice
Bank voice `firm-captain` (Alnilam), style "Say firmly but kindly, like a speech coach calling the next drill." Not used by any 9-12 ELA tool; family siblings use knowing-guide and clear-teacher. The same voice reads the speech lines in Hear it (Player), so the student hears one steady reader. `Curio.voice`, `scope: () => state.mode + state.speech`.
- w-sort (how): "Drag the line into the bin that fits, then tap the words that do the persuading."
- words (how, first word picking): "Tap the few words that carry it, then press Done."
- also (how, first time a line is sorted): "If a line does two jobs, press Also fits."
- compare (how, when every line is sorted): "Every line is sorted. Press Compare with one reading."
- w-devices (how): "Pick a device, then tap every line that uses it."
- found (event, Check this device; stale on tab change): "You found {n} of {m}."
- w-hear (how): "Press Play to hear the speech with your marks lit."
- limit (event): "Two is the limit. Which matters most?"
- Speech lines in Hear it are passage text, spoken through `rh.play`, not voice table lines; they are never "how" lines and are spoken every time Play is pressed.

## Family engine
`kit/rhetoric.js`, described in full in tools/argument-map/spec.md. This tool uses: Passage (three speeches, units = the lines above inside their full paragraphs), Marks (bin underline layers, device marks), Tagger (bins Ethos, Pathos, Logos with `multi: 2`; device bins with `multi: 4`; key from Content; `rh.cueOverlap` for the words), Player (Hear it). Not Map or Order.

## Sources
- Henry text: Avalon Project, Yale Law School, "Patrick Henry: Give Me Liberty or Give Me Death", https://avalon.law.yale.edu/18th_century/patrick.asp (from Wirt, 1817).
- Henry facts (Wirt's 1817 reconstruction from witnesses' memories decades later; St. John's Church, March 23, 1775; Washington and Jefferson present; 67 enslaved people at his death in 1799): Wikipedia, "Give me liberty, or give me death!" and "Patrick Henry", checked 2026-10-27; confirm the 67 figure against Red Hill (Patrick Henry National Memorial) at build.
- Anthony text and trial facts (voted November 1872 in Rochester; 29 districts of Monroe and 21 of Ontario; trial June 17, 1873, at Canandaigua; $100 fine; "I shall never pay a dollar of your unjust penalty"): Stanton, Anthony and Gage, History of Woman Suffrage, vol. 2 (1882), chapter 25, Wikisource transcription, https://en.wikisource.org/wiki/History_of_Woman_Suffrage/Volume_2/Chapter_25. Do not use Wikisource's separate page for the speech, which was found vandalized on 2026-10-27.
- Fifteenth Amendment (1870) and Nineteenth Amendment (1920): National Archives, Constitution amendments 11-27 transcript, https://www.archives.gov/founding-docs/amendments-11-27. Anthony died in 1906: National Park Service, Women's Rights National Historical Park, "Susan B. Anthony".
- Roosevelt text and note on delivered versus printed text: The American Presidency Project, UC Santa Barbara, "Inaugural Address", March 4, 1933, https://www.presidency.ucsb.edu/documents/inaugural-address-8.
- Appeal definitions: Aristotle, Rhetoric, Book I, chapter 2, trans. W. Rhys Roberts (1924), MIT Internet Classics Archive, https://classics.mit.edu/Aristotle/rhetoric.1.i.html.

## Done when
- Each speech has its context card, 9 or 10 lines, and every line text matches its edition (`rh.check` is silent).
- A line can take one or two bins, never three; word picking accepts 1 to 8 words.
- Compare shows Same, Also fair or Another reading with the reason for every line, and a word-overlap count; no "wrong".
- Devices: the Anaphora check on Henry finds H5 and H6 when both are tapped ("Found 2 of 2"); a missed line gets its look-here hint.
- Hear it plays every line in order with the student's glyphs lit; Pause, Step and Stop work; Sound off still steps at reading pace.
- The Anthony A9 note card opens when A9 is first shown.
- Answers survive a reload; Start this speech over clears only that speech.
- At 375 wide the bins become buttons and everything works by tap with no horizontal scroll; at 680x425 the card and bins are visible without scrolling.

## Open questions
- Anthony's "oligarchy of race... might be endured" (A9) is kept, with a note card that names what it ranks. Keep it, or drop the line and mention it only in the teacher notes?
- Henry's own slaveholding is on the context card. Fine for grade 9 as written?
- Hear it uses the narrator voice for historical speakers. Fine, or should Hear it show the text lighting up in silence only?
