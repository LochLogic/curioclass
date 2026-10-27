# Satire Decoder

## One idea
Every satire runs two cases at once: the speaker's face-value case is already pinned on the board, and you pull clues out of the text, line by line, until you can prove the case the author is really making.

## Not like
- tone-dial: there you turn a dial to rewrite tone; here nothing is rewritten, you gather evidence that one text means something other than it says.
- fallacy-field-guide: there you collect fallacy cards from ads; here the "bad logic" is deliberate, and the question is what the author is aiming it at.
- rhetorical-situation-simulator: there you change speaker and audience to see what works; here the speaker is a fixed mask and you work out who is behind it.
- premise-inspector: there you test the real premises of sincere founding documents; here the premises are false on purpose and you decode the true argument.
- ambiguity-lab: there you change a story's structure to shift meaning; here the text is fixed and you defend one reading with clues.
- thesis-workshop and argument-map: those build or map an argument of your own; here the claim is a narrow two-layer read (said vs meant) of a single text.
- usage-panel and ad-agency: role play and persuasion making; no detective board, no irony.

## Who and how
Grade 11 (works 10-12), ELA. Driver: students, often alone on laptops; a teacher can project one case for the class. 15 to 40 minutes (one case is about 12 minutes). Standards: RL.11-12.6 (distinguish what is directly stated from what is really meant: satire, sarcasm, irony, understatement). Also RL.11-12.1 (cite strong and thorough textual evidence: each clue is a quoted line).

Look: 9-12 band. Link `kit:curio` then `kit:theme-912`; set `--brand` to a muted oxblood (about #8a3b3b, keep AA contrast against the theme). A dark detective desk: the passage on an aged paper card at left, a corkboard-style "case board" at right drawn in code (two columns, pins, string lines). Minimal celebration: no confetti, no mascots.

## Screens and modes
Header: title "Satire Decoder" with small line "Said one way. Meant another." Mode buttons (`.seg`): **Case Files**, **Sincere or Satire?**, **Open a Case**. Then the kit buttons **Motion**, **Sound**, **Read**.

### Case Files (default, explore first)
1. **Case shelf.** Four case folders as cards (cover image, title, author, year, one-line teaser). Click a folder to open it. Button on each: **Open case**.
2. **Case desk.** Left: the passage, split into numbered lines (the chunks in Content). Right: the case board with two columns.
   - Top of the board, already filled: **Face value**, a typed card stating what the speaker literally says (from Content). It has a faint stamp "AS STATED".
   - Below it, empty: **What is meant**, with three slots **Target**, **Charge**, **Method**, and a **Clues** tray.
   - Buttons above the passage: **Background** (opens a drawer with 3 context lines and a short glossary), **Back to shelf**.
   - A stage stepper under the header: **1 Gather clues**, **2 Make the claim**, **3 Defend it**, **4 Open the case file**. All four are clickable at any time (explore first); 4 asks "Open the case file now? You can still change your read afterward." with **Open it** and **Not yet**.
3. **Gather clues.** Tap any line. A tag menu pops beside it with the seven tags (Content, "Tags"), each with a one-line meaning, plus **Clear tag**. A tagged line gets a colored margin mark and the tag name in text (never color alone). Tagged lines (except Plain setup) appear as small index cards in the Clues tray. A counter reads "Clues: 3".
4. **Make the claim.** Each of the three slots opens a list of four options for this case. Pick one per slot. The chosen text fills the slot on the board. Nothing says right or wrong yet.
5. **Defend it.** Drag (or tap, then tap **Pin**) two or three clue cards onto the claim. String lines draw from each pinned clue to the claim. If fewer than two are pinned, step 4 still opens but the board shows "A claim with fewer than two clues is a guess."
6. **Open the case file.** A manila folder slides over the board (fades when Motion is off). It shows:
   - The passage again with the case file's own tags in the margin, each with its note. Lines where your tag matched (primary or "also fits") show "Same read". Lines you tagged differently show both tags: "You: Blown up. File: Mock logic." Lines the file flagged that you skipped show "Missed clue".
   - The file's claim beside yours, slot by slot, with the verdict text for whatever option you chose (best, partial or misread, as written in Content). Verdict words are shown as plain labels: "Strongest read", "Partly there", "Misread".
   - One "Talk it over" question for the case.
   - Buttons: **Change my read** (closes the folder, keeps everything), **Reset case** (clears tags, claim, pins for this case), **Next case**.

### Sincere or Satire? (optional challenge)
Ten short original pieces, one at a time, on a clipping card. Three buttons: **Sincere**, **Satire**, **Need more context**. After a choice, the card flips to show the answer and "The tell" (one or two sentences). Buttons: **Next clipping**, **Start over**. A small tally at the end: "You matched 7 of 10." No timer, no stars. Final screen line: "An extreme idea is not proof of satire. Look for the writer signaling a second meaning."

### Open a Case (bring your own text)
A paste box (limit 4,000 characters, counter shown) with **Split into lines**. Sentences split on . ! or ? followed by a space or line break; each becomes a tappable line with the same seven tags. The board has an editable **Face value** box and three free-text slots (Target, Charge, Method) plus the Clues tray and pinning. Buttons: **Print case** (window.print with a clean print stylesheet: passage with tags, face value, claim, pinned clues), **Clear**. Note under the box: "Your text stays on this device. Nothing is sent anywhere." A draft may be kept in localStorage `curio-satire-draft` (try/catch).

## Content

### Tags (the satirist's toolkit)
1. **Straight face**: a calm, reasonable voice delivering a terrible idea.
2. **Blown up**: a real attitude pushed to an extreme.
3. **Mock logic**: careful numbers or reasoning built on a monstrous or absurd premise.
4. **Wrong size**: a trivial cause with huge stakes, or the reverse.
5. **Sting in the praise**: praise, thanks or pleasant words that really mean blame.
6. **The mask slips**: a line where the real target shows through the speaker.
7. **Plain setup**: no trick; this line builds the world or earns trust.

Quotations below are exact from the cited editions. Straight or curly apostrophes are both fine; keep spelling (cabbin, publick, fricasee) as the source has it. "[...]" marks a cut and must be shown. In The War Prayer, "--" is the edition's own double hyphen: render it as two hyphens, never as an em dash. Underscored words are italic in the source.

### Case 1: A Modest Proposal (Jonathan Swift, 1729)
Teaser: "A calm economist has a plan to end poverty in Ireland." Cover: proposal.
Face value: "PROPOSAL: Poor families in Ireland should nurse their babies for one year, then sell them as meat to the wealthy. CLAIMED BENEFITS: fewer beggars, income for mothers, fine dishes for landlords, more trade. SPEAKER: a modest, public-spirited planner."
Background: Published as a pamphlet in Dublin in 1729. Swift was Dean of St Patrick's Cathedral, Dublin. Much of Ireland's land was owned by landlords, many of them absent in England, while the rural poor faced hunger after failed harvests in the late 1720s.
Glossary: dear = expensive; alms = charity; the Pretender = James Francis Edward Stuart, Catholic claimant to the British throne; sell themselves to the Barbadoes = sign on as indentured servants in the West Indies; per annum = per year; absentees = landlords living abroad; expedients = remedies.
Lines (file tag; also fits; note):
1. "It is a melancholy object to those, who walk through this great town, or travel in the country, when they see the streets, the roads, and cabbin-doors crowded with beggars of the female sex, followed by three, four, or six children, all in rags, and importuning every passenger for an alms." Plain setup. Note: The suffering is real and the voice sounds sincere. Swift earns your trust before he springs the trap.
2. "I think it is agreed by all parties, that this prodigious number of children [...] is in the present deplorable state of the kingdom, a very great additional grievance; and therefore whoever could find out a fair, cheap and easy method of making these children sound and useful members of the commonwealth, would deserve so well of the publick, as to have his statue set up for a preserver of the nation." Plain setup; also Straight face. Note: "Useful" and "cheap" are the words of a planner, not a neighbor. Children are already being counted as a problem to manage.
3. "I shall now therefore humbly propose my own thoughts, which I hope will not be liable to the least objection." Straight face; also Sting in the praise. Note: "Humbly" and "least objection" set up the shock. The modesty is the mask.
4. "I have been assured by a very knowing American of my acquaintance in London, that a young healthy child well nursed, is, at a year old, a most delicious nourishing and wholesome food, whether stewed, roasted, baked, or boiled; and I make no doubt that it will equally serve in a fricasee, or a ragoust." Straight face; also Blown up. Note: The monstrous idea arrives in the language of a cookbook. The calm tone is what makes it horrifying.
5. "I grant this food will be somewhat dear, and therefore very proper for landlords, who, as they have already devoured most of the parents, seem to have the best title to the children." The mask slips. Note: "Devoured" turns the joke into a charge: landlords already consume the poor through rents. This is the real target.
6. "I have already computed the charge of nursing a beggar's child (in which list I reckon all cottagers, labourers, and four-fifths of the farmers) to be about two shillings per annum, rags included; and I believe no gentleman would repine to give ten shillings for the carcass of a good fat child [...]" Mock logic. Note: Prices and profit margins treat people as livestock, which is how the speaker says the system already treats them.
7. "Those who are more thrifty (as I must confess the times require) may flay the carcass; the skin of which, artificially dressed, will make admirable gloves for ladies, and summer boots for fine gentlemen." Blown up; also Mock logic. Note: Luxury goods for the rich made from the bodies of the poor: the real economy, pushed to its end.
8. "Therefore let no man talk to me of other expedients: Of taxing our absentees at five shillings a pound: [...] Of quitting our animosities and factions [...] Of being a little cautious not to sell our country and consciences for nothing: Of teaching landlords to have at least one degree of mercy towards their tenants." The mask slips. Note: The "rejected" remedies are the reforms Swift actually wanted. The real argument is smuggled in as a list of things not to talk about.
9. "I profess in the sincerity of my heart, that I have not the least personal interest in endeavouring to promote this necessary work [...] I have no children, by which I can propose to get a single penny; the youngest being nine years old, and my wife past child-bearing." Straight face; also Mock logic. Note: His proof of honesty is that his own children are too old to sell. The last line keeps the mask on and twists the knife.
Claim options (verdict: text):
- Target: (a) "Landlords and the ruling class who treat Ireland's poor as a resource" Strongest read: lines 5 and 8 name them. (b) "Poor Irish mothers who beg" Misread: that is the speaker's view; the satire aims past him. (c) "Planners who reduce people to numbers" Partly there: a real second target (lines 2, 6), but not the main one. (d) "People who eat unusual food" Misread: the food is the vehicle, not the point.
- Charge: (a) "They already devour the poor and ignore the real reforms" Strongest read. (b) "Ireland simply has too many children" Misread: that is the mask talking. (c) "The rich spend too much on luxury" Partly there: in line 7, but in service of the larger charge. (d) "Swift wants the plan adopted" Misread: nothing signals a sincere proposal.
- Method: (a) "A reasonable-sounding planner proposes a monstrous plan in calm economic language" Strongest read. (b) "An angry direct attack on landlords" Misread: the anger never speaks in its own voice. (c) "A funny animal fable" Misread. (d) "Real economic logic pushed to its end" Partly there: true, but it needs the calm mask to work.
Talk it over: "Line 8 lists Swift's real ideas. Why hide them inside the satire instead of arguing for them straight?"

### Case 2: Gulliver in Lilliput (Jonathan Swift, 1726)
Teaser: "An official explains a long and bloody war over eggs." Cover: egg.
Face value: "BRIEFING: The secretary of Lilliput tells a visitor that the court is split into two parties by the height of their shoe heels, and that a war with Blefuscu began over which end of an egg to break. REQUEST: help us fight."
Background: From Gulliver's Travels (1726), Part I, Chapter IV. The speaker is Reldresal, a Lilliputian official. Readers have long taken Lilliput and Blefuscu as stand-ins for England and France, the heels for Britain's Tory and Whig parties, and the egg war for Catholic and Protestant conflict.
Glossary: faction = political party; animosities = hatreds; drurr = an invented unit; schism = split in a church; Alcoran = old spelling of Quran, used here for Lilliput's holy book; magistrate = ruler or official.
Lines:
1. "[...] as flourishing a condition as we may appear to be in to foreigners, we labour under two mighty evils: a violent faction at home, and the danger of an invasion, by a most potent enemy, from abroad." Plain setup. Note: Ordinary statesman talk. You expect a serious crisis.
2. "[...] there have been two struggling parties in this empire, under the names of Tramecksan and Slamecksan, from the high and low heels of their shoes, by which they distinguish themselves." Wrong size. Note: A national divide over a fraction of an inch of shoe.
3. "[...] his majesty's imperial heels are lower at least by a drurr than any of his court (drurr is a measure about the fourteenth part of an inch)." Mock logic; also Wrong size. Note: Precise measurement makes the loyalty test look as small as it is.
4. "The animosities between these two parties run so high, that they will neither eat, nor drink, nor talk with each other." Blown up. Note: Real party hatred, only slightly exaggerated. That is the uncomfortable part.
5. "We apprehend his imperial highness, the heir to the crown, to have some tendency towards the high heels; at least we can plainly discover that one of his heels is higher than the other, which gives him a hobble in his gait." The mask slips. Note: An heir who keeps a foot in both parties limps. The joke points at real court politics.
6. "It is allowed on all hands, that the primitive way of breaking eggs, before we eat them, was upon the larger end; but his present majesty's grandfather, while he was a boy, going to eat an egg, and breaking it according to the ancient practice, happened to cut one of his fingers." Wrong size. Note: A cut finger becomes law for a whole nation.
7. "It is computed that eleven thousand persons have at several times suffered death, rather than submit to break their eggs at the smaller end." Straight face; also Wrong size. Note: Eleven thousand deaths, reported as a statistic about eggs. The flat tone is the point.
8. "[...] the words are these: 'that all true believers break their eggs at the convenient end.' And which is the convenient end, seems, in my humble opinion to be left to every man's conscience, or at least in the power of the chief magistrate to determine." The mask slips. Note: The holy text never says which end. People killed each other over an interpretation the text does not settle.
9. "[...] we have lost forty capital ships, and a much greater number of smaller vessels, together with thirty thousand of our best seamen and soldiers; and the damage received by the enemy is reckoned to be somewhat greater than ours." Sting in the praise; also Mock logic. Note: The comfort offered is that the enemy lost a little more. War accounting as consolation.
Claim options:
- Target: (a) "Britain's party feuds and its religious wars" Strongest read. (b) "The tiny people of Lilliput" Misread: Lilliput is a mirror, not the target. (c) "Kings who are careless with knives" Misread. (d) "Religious faith itself" Partly there: Swift was a clergyman; line 8 aims at fighting over interpretation, not at belief.
- Charge: (a) "Nations kill and divide over differences as small as the end of an egg" Strongest read. (b) "Lilliput's navy is too weak" Misread. (c) "Leaders hide their real loyalties" Partly there: line 5, a side charge. (d) "Eggs should be broken at the small end" Misread.
- Method: (a) "Shrink the conflict until its pettiness shows, and let a solemn official explain it with a straight face" Strongest read. (b) "Open mockery from the narrator" Misread: Gulliver reports it without comment. (c) "Exaggerate the death toll" Partly there: line 4 exaggerates; the numbers in 7 and 9 are delivered flat. (d) "A dream sequence" Misread.
Talk it over: "Name a real disagreement today that might look like the egg war from far enough away. Is the comparison fair?"

### Case 3: The War Prayer (Mark Twain, dictated 1904-05)
Teaser: "A church prays for victory. A stranger finishes the prayer." Cover: pews.
Face value: "STORY: A town sends its young soldiers to war with a prayer for victory. A stranger claims to bring God's reply and speaks the part of the prayer no one said aloud. The congregation decides he was a lunatic."
Background: Twain dictated it in 1904-05, while the United States was fighting in the Philippines; it was not published in his lifetime and first appeared in Europe and Elsewhere (1923). Twain was an outspoken opponent of that war. Teacher note in notes.md: the stranger's prayer contains violent war imagery.
Glossary: martial = of war; supplication = humble request; smite = strike; unavailing = useless; travail = suffering; contrite = sorry.
Lines:
1. "It was a time of great and exalting excitement. The country was up in arms, the war was on, in every breast burned the holy fire of patriotism;" Blown up. Note: The gushing narrator sounds like the crowd. Watch how much is sacred here: "holy fire".
2. "It was indeed a glad and gracious time, and the half dozen rash spirits that ventured to disapprove of the war and cast a doubt upon its righteousness straightway got such a stern and angry warning that for their personal safety's sake they quickly shrank out of sight and offended no more in that way." Sting in the praise. Note: "Glad and gracious" sits next to dissenters being threatened into silence.
3. "[...] help them to crush the foe, grant to them and to their flag and country imperishable honor and glory--" Plain setup. Note: The spoken prayer. It sounds noble. Keep it in mind.
4. "For it is like unto many of the prayers of men, in that it asks for more than he who utters it is aware of--except he pause and think." The mask slips. Note: Twain's thesis, said almost outright by the messenger.
5. "When you have prayed for victory you have prayed for many unmentioned results which follow victory--_must_ follow it, cannot help but follow it." Mock logic; also The mask slips. Note: Pure logic, no exaggeration: victory for one side means defeat for the other.
6. "O Lord our God, help us to tear their soldiers to bloody shreds with our shells; help us to cover their smiling fields with the pale forms of their patriot dead;" The mask slips; also Blown up. Note: The hidden half of the prayer, said out loud. The enemy dead are "patriots" too.
7. "We ask it, in the spirit of love, of Him Who is the Source of Love, and Who is the ever-faithful refuge and friend of all that are sore beset and seek His aid with humble and contrite hearts. Amen." Straight face; also Sting in the praise. Note: The language of love wrapped around a request for suffering. The clash is the charge.
8. "It was believed afterward that the man was a lunatic, because there was no sense in what he said." Straight face. Note: A deadpan last line. The crowd's verdict on him becomes Twain's verdict on the crowd.
Claim options:
- Target: (a) "Patriotic crowds and churches who pray for victory without facing its cost to others" Strongest read. (b) "The young soldiers" Misread: they are shown as young and dreaming, not blamed. (c) "Prayer and religion as a whole" Partly there: a defensible wider reading, but the text aims at the unthinking war prayer. (d) "The stranger" Misread: he is the truth-teller.
- Charge: (a) "To pray for victory is to pray for the enemy's suffering, and the crowd will not think it through" Strongest read. (b) "The minister's prayer was too long" Misread. (c) "Dissent is crushed in wartime" Partly there: line 2, a real side charge. (d) "The war was lost" Misread.
- Method: (a) "A messenger says the hidden meaning out loud, then a deadpan ending turns the crowd's verdict back on itself" Strongest read. (b) "A gross exaggeration of war" Partly there: the images are vivid, but line 5 argues they are simply what victory means. (c) "A sarcastic narrator mocks the town in every line" Misread: the narrator mostly stays inside the crowd's view. (d) "A comic misunderstanding" Misread.
Talk it over: "Is the stranger's prayer exaggeration, or the literal truth said plainly? What changes if it is the truth?"

### Case 4: The Devil's Dictionary (Ambrose Bierce, 1911)
Teaser: "A reference book that tells the truth about polite words." Cover: dictionary.
Face value: "REFERENCE BOOK: Neutral dictionary definitions of everyday words, in standard form: headword, part of speech, meaning."
Background: Bierce, an American journalist, published these definitions in newspapers for years; they were collected as The Cynic's Word Book (1906) and retitled The Devil's Dictionary (1911).
Glossary: n. = noun; v.i. = verb with no object; hypocrisy = pretending to virtues you lack; blackguard = scoundrel.
Lines:
1. "ACQUAINTANCE, n. A person whom we know well enough to borrow from, but not well enough to lend to." Straight face; also The mask slips. Note: A dictionary voice, a selfish truth about how "we" behave.
2. "APOLOGIZE, v.i. To lay the foundation for a future offence." Straight face. Note: The definition names what the act is for, not what it claims to be.
3. "CONSULT, v.i. To seek another's disapproval of a course already decided on." Straight face; also Mock logic. Note: Asking for advice we have no intention of taking.
4. "ADMIRATION, n. Our polite recognition of another's resemblance to ourselves." Sting in the praise. Note: Admiring others turns out to be admiring ourselves.
5. "POLITENESS, n. The most acceptable hypocrisy." Sting in the praise. Note: A compliment and an insult in four words.
6. "PATIENCE, n. A minor form of despair, disguised as a virtue." Sting in the praise; also The mask slips. Note: The pattern of the whole book: a virtue unmasked.
7. "EGOTIST, n. A person of low taste, more interested in himself than in me." The mask slips. Note: The definer convicts himself. Bierce includes the reader and the writer in the joke.
8. "PEACE, n. In international affairs, a period of cheating between two periods of fighting." Straight face; also Blown up. Note: Turns a hopeful word into a cynical cycle.
9. "OCEAN, n. A body of water occupying about two-thirds of a world made for man--who has no gills." Wrong size. Note: Human self-importance measured against two thirds of the planet. (Bierce's own figure; Earth's surface is about 71 percent water.)
Claim options:
- Target: (a) "Everyday vanity and the polite words people use to cover it" Strongest read. (b) "Dictionaries" Partly there: the form is parodied, but the target is the people who use the words. (c) "Lawyers and politicians only" Partly there: some entries, too narrow for this set. (d) "The ocean" Misread.
- Charge: (a) "Our nice words are cover stories for selfish motives" Strongest read. (b) "People should stop apologizing" Misread: it describes; it does not advise. (c) "Peace is impossible" Partly there: one entry, not the whole charge. (d) "Bierce is better than everyone" Misread: entry 7 turns the joke on him.
- Method: (a) "The calm voice of a reference book delivers cynical verdicts" Strongest read. (b) "Long angry essays" Misread. (c) "Invented words" Misread. (d) "Puns" Partly there: some wordplay, but the engine is the deadpan form.
Talk it over: "Write a Devil's Dictionary definition for a word from school life. Which tag does it use?"

### Sincere or Satire? clippings (original text written for Curio Class)
1. "Breaking: Local student reads entire assigned chapter. Teachers baffled. 'We have never seen anything like it,' said one, who asked to sit down." Satire. Tell: A normal act is treated as a shocking event (wrong size), which pokes at low expectations.
2. "I know a four-day school week sounds extreme. Our Friday buses run nearly empty, and longer days Monday to Thursday would keep the same hours. I may be wrong, so tell me what it costs families who need Friday child care." Sincere. Tell: It admits costs and invites objections. No hidden target.
3. "Good news for the town budget: we closed the library and saved money. Since no one can read the closing notice, no one has complained." Satire. Tell: The logic eats itself, and the calm "good news" tone is a straight face.
4. "Ban all cars from Main Street on Saturdays. Every one. I know it sounds drastic. Bikes, strollers and food carts only, from 8 to 2. Try it for one summer and count the shoppers." Sincere. Tell: Bold, but it proposes a real test and means exactly what it says.
5. "The cafeteria has answered complaints about cold fries. They are now 'chilled potato sticks,' a premium item, one dollar more." Satire. Tell: The fix changes the label, not the problem. The target is institutions that rebrand instead of repair.
6. "Dear Council, the crosswalk on Fifth Street needs a signal. Twice this month I watched drivers fail to stop. Please put it on the next agenda." Sincere. Tell: Direct, specific, asks for one action. Nothing signals a second meaning.
7. "Thank you, landlord, for raising our rent again. We were getting far too comfortable with heat." Satire. Tell: Sting in the praise: the thanks is the complaint.
8. "Homework should be abolished in ninth grade. Not reduced. Abolished. Give us evenings for sleep, jobs and family, and judge us by what we do in class." Sincere. Tell: Extreme, but argued in the writer's own voice with real reasons.
9. "To protect students from distraction, the school has removed all windows. Focus is up, and weather has stopped being a problem entirely." Satire. Tell: An absurd fix reported with a straight face.
10. "The new uniforms are just perfect. Truly. I could not be happier." Need more context. Tell: This could be sincere or sarcastic. Without knowing the speaker, the audience or the uniforms, there is no evidence either way.

## Interactions in detail
- Line tapping: one tag per line; choosing a new tag replaces the old; **Clear tag** removes it and removes its clue card (and unpins it). Keyboard: lines are buttons in tab order; Enter opens the tag menu; arrow keys move through tags; Escape closes.
- Clue cards show line number, first 8 words and the tag. Pinning a fourth clue is refused with the note "Three clues is enough. Unpin one first."
- A claim slot can be changed at any time, including after the case file opens; verdicts update live while the folder is open.
- Case file comparison: "Same read" if the student's tag equals the file tag or any "also fits" tag. Plain setup lines the student tagged as a trick show "File: Plain setup" with the note. No totals or percentages in Case Files.
- State per case is kept in memory for the session (switching cases or modes keeps it). **Reset case** clears only that case. localStorage only for the Open a Case draft and nothing else.
- Background drawer and glossary: glossary words are underlined in the passage; tapping one shows its gloss in a small tip (does not open the tag menu; tag menu opens from the line number or the rest of the line).
- Open a Case extremes: empty paste disables **Split into lines**; over 4,000 characters the counter turns to a warning and the extra is not accepted; a single giant sentence still becomes one line; more than 80 lines shows "Long text: consider pasting one passage at a time." and still works.
- Read button: reads the hint for the current step (kit fallback); it never reads the full passage unless the student selects a line and presses Read, which reads that line with the browser voice.
- Motion off: folder and card flips become instant fades; string lines appear without drawing animation.
- Small screens: below about 900px wide, the board stacks under the passage with a **Board** / **Text** toggle.

## Art
Made locally by FLUX. No people, faces or hands anywhere.
- cover-proposal: an 18th-century printed pamphlet lying folded on a dark wooden table beside an empty pewter plate and fork, candlelight, muted; 16:10; cutout no; people no.
- cover-egg: a single soft-boiled egg in a tiny ornate egg cup, top cracked, beside a toy-sized wooden sailing ship, dark velvet background; 16:10; cutout no; people no.
- cover-pews: empty wooden church pews and tall organ pipes in dim morning light, a small flag on a stand near the front; 16:10; cutout no; people no.
- cover-ink: a tipped-over glass inkwell with a sharp steel pen nib on yellowed paper, a small pool of spilled black ink, warm lamplight (changed at the spec check: usage-panel already uses an open dictionary); 16:10; cutout no; people no.
- board-texture: dark cork detective board surface, seamless, low contrast (changed at the spec check: savings-plan already uses a walnut desk); 16:9; cutout no; people no.
The case board, pins, string, index cards, stamps, tag marks and the manila folder are drawn in code.

## Voice
Bank "hs-narrator", voice "Kore", style "Read clearly and naturally, at a moderate pace". Passages are read on screen, not narrated.
1. welcome: "Welcome to the Satire Decoder. Every case here says one thing and means another. Your job is to prove the difference."
2. shelf: "Pick a case file. Each one holds a real piece of satire, written long ago."
3. gather: "Read the speaker's words. Tap any line that feels wrong for what it is saying, and tag the trick it uses."
4. claim: "Now make your claim. Who is the real target, what is the charge, and how does the writer land it?"
5. defend: "Pin two or three clues to your claim. A claim with no clues is only a guess."
6. file: "Here is the case file. Compare its reading with yours. Where you differ, decide who has the better evidence."
7. case-proposal: "Dublin, seventeen twenty nine. The poor are starving, and a calm planner has a solution."
8. case-egg: "The empire of Lilliput is at war. An official explains why."
9. case-pews: "A church prays for victory before its soldiers march. Then a stranger walks in."
10. case-dictionary: "A dictionary that defines polite words by what people really mean."
11. sincere: "Some of these clippings are satire. Some are sincere, even when they sound extreme. Read each one and decide."
12. sincere-end: "Remember, an extreme idea is not proof of satire. Look for the writer signaling a second meaning."
13. open: "Paste any text you want to decode. It stays on this device. Nothing is sent anywhere."

## Family engine
none. Keep the tag menu, clue tray and pinning in one clearly marked block ("CASE BOARD") so it could later be lifted into a kit file.

## Sources
- Jonathan Swift, A Modest Proposal (1729), Project Gutenberg eBook #1080: https://www.gutenberg.org/ebooks/1080
- Jonathan Swift, Gulliver's Travels (1726), Part I, Chapter IV, Project Gutenberg eBook #829: https://www.gutenberg.org/ebooks/829
- Mark Twain, "The War Prayer" (dictated 1904-05), in Europe and Elsewhere (1923), Project Gutenberg eBook #68604: https://www.gutenberg.org/ebooks/68604
- Ambrose Bierce, The Devil's Dictionary (1911), Project Gutenberg eBook #972: https://www.gutenberg.org/ebooks/972
- Context for A Modest Proposal (Dublin 1729, Swift as Dean of St Patrick's, absentee landlords, famine conditions): Encyclopaedia Britannica, "A Modest Proposal" and "Jonathan Swift": https://www.britannica.com/topic/A-Modest-Proposal
- Readings of Lilliput, Blefuscu, the heels and the egg war: Encyclopaedia Britannica, "Gulliver's Travels": https://www.britannica.com/topic/Gullivers-Travels
- Twain's opposition to the Philippine-American War and The War Prayer's publication history: Encyclopaedia Britannica, "Mark Twain"; Mark Twain Project, University of California: https://www.britannica.com/biography/Mark-Twain
- The Cynic's Word Book (1906) retitled The Devil's Dictionary (1911): Encyclopaedia Britannica, "Ambrose Bierce": https://www.britannica.com/biography/Ambrose-Bierce
- Earth's surface about 71 percent water: USGS Water Science School, "How Much Water is There on Earth?": https://www.usgs.gov/special-topics/water-science-school/science/how-much-water-there-earth
- Sincere or Satire? clippings, face value cards, notes, tags and claim options: original text written for Curio Class.

## Done when
1. All four cases open from the shelf; every quoted line matches the cited Gutenberg text word for word (spot-check lines 5 and 8 of Case 1, line 7 of Case 2, line 5 of Case 3), with "[...]" shown where cut and no em dashes anywhere.
2. Tagging, retagging and clearing a line updates its margin mark (text label, not color only) and the Clues tray.
3. Picking an option in each claim slot fills the board; pinning a fourth clue is refused with the message; fewer than two pins shows the guess warning.
4. The case file opens from step 4 at any point, shows Same read / Missed clue / differing tags correctly, and shows the verdict for each chosen option; changing a slot with the folder open updates the verdict.
5. Change my read keeps all work; Reset case clears only that case; switching modes and back keeps case state.
6. Sincere or Satire? runs all ten clippings with three buttons, shows each tell, and ends on the tally plus the closing line; no timer.
7. Open a Case splits pasted text into lines, enforces the 4,000 character limit, supports tags and pinning, prints a clean case sheet, and makes no network request.
8. Fully keyboard usable with visible focus; targets at least 44px; Motion off removes movement; works in a 16:10 iframe and full screen, and stacks below 900px.
9. Exactly 13 voice lines exist; no image contains a person, face or hand.
