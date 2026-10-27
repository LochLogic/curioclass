# Rhetorical Situation Simulator

## One idea
A great speech is great for one room on one day: keep the words of Lincoln, Roosevelt or Chief Joseph exactly as they are, turn the five dials of the situation around them (speaker, audience, purpose, moment, medium), and watch which lines still hold and which strain, each strain with the reason, then rewrite the broken lines for the new room.

## Not like
- source-mixer (ela 11, research group): a mixing desk with faders for sources. Here there is no desk and nothing is mixed; the board flips between whole situations.
- rhetoric-spotter (ela 9, family sibling): names each line's appeal and device in its real setting. Here the line's appeal is taken as given; what changes is the world around it.
- argument-map (ela 12, family sibling): takes the structure inside an essay apart. Here the text is never rearranged; the situation is.
- audience-shift-briefing (ela 9): the student builds their own short briefing for three fixed rooms and the main variable is the slides and visuals. Here the speech is a famous one the student did not write, all five situation dials move, and media is only one of them.
- tone-dial (ela 10, not built): turns a tone dial and rewrites a paragraph's word choices. Here tone is never a setting; the speaker, audience, purpose, moment and medium are, and the text stays fixed until the student chooses to rewrite.
- premise-inspector (ela 11, founding-docs): compares later speeches against the Declaration's premises. Here each speech is compared only against its own possible situations.

## Who and how
- Grade 11 ELA. Module: Writing for task, purpose and audience; speaking for context.
- Driver: students on laptops, alone or in pairs (pairs read rewrites aloud to each other). 30 to 45 minutes.
- Standards: W.11-12.4 (writing whose development, organization and style are appropriate to task, purpose and audience): Explore and Rewrite. W.11-12.1 and W.11-12.2 (argument and explanation): every rewrite carries a "because" line explaining the change, and Rewrite's "Make the case" box asks for a short argument for which dial matters most. SL.11-12.6 (adapt speech to a variety of contexts and tasks): the Medium and Moment dials, and the read-aloud step with a partner.
- tool.json: driver "students", minutes "30-45", modes ["Explore", "What changed?", "Rewrite"], grades_label "Grade 11". Kit starter plus `kit:theme-912` and `kit:rhetoric`.

## Screens and modes
Header: title "Rhetorical Situation Simulator", small line "Same words. Different room."; speech picker **Lincoln, 1865** / **Roosevelt, 1941** / **Joseph, 1879**; mode buttons **Explore** (opens first), **What changed?**, **Rewrite**; Motion, Sound, Read. Each speech opens with a context card (Content), closed with **Begin**; **Context** reopens it.

### Explore (opens first)
- Stage, top: the situation board, five dials drawn as rows of a split-flap departures board, like an old train station sign: **Speaker**, **Audience**, **Purpose**, **Moment**, **Medium**. Each row has three stops; the real one carries a small star and the word "real". A row flips to its next stop by a tap on it, by its **‹** and **›** buttons, or by arrow keys; the flap letters spell the current stop's words.
- Stage, below: the five lines of the speech, as cards on a teleprompter strip, each with a status badge: **Holds** (✓) or **Strains** (✗ plus a count "2 reasons").
- Tapping a straining card opens its reasons, one per missing tag, each naming the dial that removed it ("Moment: 'Yesterday' only works the day after.").
- Panel: `#hint`; **Fit**: "3 of 5 lines hold"; **Which dial moved most**: a five-row bar list counting how many lines each dial is currently straining, with the dial's name and number; **Real setting** (flips every row back to its star); **Hear the line** (plays the selected line through the Player).
- A **Full speech** drawer shows the whole text with the five cards boxed in place.

### What changed?
- The tool secretly turns one dial (rounds 1 to 3) or two dials (rounds 4 to 6) away from the real setting, without showing which. The teleprompter shows only which lines hold and strain, not the reasons.
- The student guesses by flipping rows, then presses **Lock my guess**. Result: "Right dial and stop", "Right dial, different stop: same lines strain, so both fit" (counted as right when the strain pattern matches), or "Not this one: your setting strains line 2, the mystery doesn't". Then the reasons are shown.
- Rounds draw from all three speeches' dials. **New round**. A tally "4 of 6" is shown; nothing else is scored.

### Rewrite
- Choose any situation (rows as in Explore). Each straining line gets a **Rewrite for this room** button. It opens a private pad: the original line above (read only), the reasons below it, a text box "Your version", and a box "Because..." (one sentence on what you changed and why).
- **Read it aloud** step: a checkbox "I read my version aloud to a partner" and a prompt "Did it sound like it belonged in this room? Change one word if not." No microphone.
- **Make the case**: one box per speech, "Which dial changes this speech the most, and why?" with the Which dial moved most readout beside it as evidence.
- **My rewrites** lists every saved rewrite by speech and situation, with **Copy all** (to the clipboard as plain text) and **Clear all**. Everything stays on this device (localStorage).

## Content
Exact texts from the named editions (Sources). Source em dashes are shown as "--". Each speech has five lines with the tags they depend on, three stops per dial (the real one first) with the tags each stop supplies, and one reason per line per tag. A line holds when every tag it depends on is supplied by the current stops.

### Lincoln, Second Inaugural Address, Washington, March 4, 1865
Context card: "Lincoln had just been re-elected. The Civil War was nearly over, and about 600,000 soldiers had died. He spoke from the Capitol to a crowd that included Black soldiers and Frederick Douglass, and to a country that would read the speech in the papers. Six weeks later he was shot and killed. The speech names slavery as the cause of the war."
Tags: `power` (can set the government's course), `both` (the audience includes both sides of the war), `heal` (the purpose is reunion), `solemn` (a grave moment), `aloud` (heard, not read), `room` (space for length).
- Speaker: "Lincoln, just re-elected president" [power] (real); "A Union general" []; "A New York newspaper editor" [].
- Audience: "The crowd at the Capitol and the whole country, North and South" [both] (real); "Union soldiers in camp" []; "Freedpeople at a church in Washington" [].
- Purpose: "Prepare a divided country to reunite without revenge" [heal] (real); "Celebrate the coming victory" []; "Demand that the South be punished" [].
- Moment: "His second inauguration, the war nearly won" [solemn] (real); "A victory parade" []; "A funeral for soldiers" [solemn].
- Medium: "Spoken outdoors, printed in newspapers" [aloud, room] (real); "A telegram to army commanders" []; "A printed pamphlet" [room].
- L1 "Both parties deprecated war, but one of them would make war rather than let the nation survive, and the other would accept war rather than let it perish, and the war came." Depends: both ("With one side listening, the fair account of both sides speaks past them."), aloud ("'And the war came' lands as a spoken pause; on paper it is just a clause.").
- L2 "One-eighth of the whole population were colored slaves, not distributed generally over the Union, but localized in the southern part of it. These slaves constituted a peculiar and powerful interest. All knew that this interest was somehow the cause of the war." Depends: power ("Naming the cause of the war for the government is the president's job."), room ("A telegram has no space to explain causes.").
- L3 "Both read the same Bible and pray to the same God, and each invokes His aid against the other." Depends: both ("'Both' needs both sides in the audience."), solemn ("At a parade, a reflection on shared prayer stops the cheering.").
- L4 "Fondly do we hope, fervently do we pray, that this mighty scourge of war may speedily pass away." Depends: solemn ("A prayer for the war to end sounds wrong at a victory party."), aloud ("Its rhyme and beat are made for the ear.").
- L5 "With malice toward none, with charity for all, with firmness in the right as God gives us to see the right, let us strive on to finish the work we are in, to bind up the nation's wounds" Depends: heal ("If the purpose is punishment, 'malice toward none' says the opposite."), power ("'Let us strive on' is a plan for peace; only the president can promise one.").

### Roosevelt, Address to Congress Requesting a Declaration of War, December 8, 1941
Context card: "The day before, Japanese planes attacked the US fleet at Pearl Harbor, Hawaii. Roosevelt spoke to both houses of Congress, and millions heard him on the radio. Ten weeks later, his Executive Order 9066 led to the forced removal of about 122,000 people of Japanese ancestry from the West Coast, nearly 70,000 of them American citizens. They were never charged with any crime. 'The American people' in this speech did not protect them."
Tags: `power` (commander in chief), `congress` (lawmakers who can declare war are listening), `rally` (the purpose is to unite and commit), `soon` (the day after), `aloud` (heard live), `room` (space for detail).
- Speaker: "President Roosevelt, Commander in Chief" [power] (real); "A radio news announcer" []; "A sailor who survived the attack" [].
- Audience: "A joint session of Congress, with the nation on the radio" [congress] (real); "Families of sailors lost at Pearl Harbor" []; "Ambassadors of neutral countries" [].
- Purpose: "Ask Congress to declare war and unite the country" [rally] (real); "Report the facts calmly" []; "Comfort the grieving" [].
- Moment: "December 8, 1941, the day after" [soon] (real); "December 7, 1942, one year later" []; "A memorial, ten years later" [].
- Medium: "Spoken to Congress and carried live on radio" [aloud, room] (real); "A newspaper statement" [room]; "A telegram to allies" [].
- D1 "Yesterday, December 7, 1941--a date which will live in infamy--the United States of America was suddenly and deliberately attacked by naval and air forces of the Empire of Japan." Depends: soon ("'Yesterday' only works the day after."), aloud ("The pause around 'a date which will live in infamy' is built for a listener.").
- D2 "The United States was at peace with that Nation and, at the solicitation of Japan, was still in conversation with its Government and its Emperor looking toward the maintenance of peace in the Pacific." Depends: congress ("This is evidence for lawmakers deciding on war; grieving families need something else."), room ("A telegram would cut the diplomatic record.").
- D3 "Last night Japanese forces attacked Hong Kong. Last night Japanese forces attacked Guam. Last night Japanese forces attacked the Philippine Islands. Last night the Japanese attacked Wake Island." Depends: aloud ("The repeated 'Last night' is a drumbeat; read silently it is a list."), soon ("A year later, 'last night' is false.").
- D4 "No matter how long it may take us to overcome this premeditated invasion, the American people in their righteous might will win through to absolute victory." Depends: rally ("A calm report or a comfort speech doesn't promise victory."), power ("Only the commander in chief can pledge the nation's might.").
- D5 "I ask that the Congress declare that since the unprovoked and dastardly attack by Japan on Sunday, December 7, 1941, a state of war has existed between the United States and the Japanese Empire." Depends: power ("Only the president asks Congress for war."), congress ("The request needs the people who can grant it.").

### Chief Joseph (In-mut-too-yah-lat-lat), "An Indian's View of Indian Affairs", North American Review, April 1879
Context card: "Joseph led the Wallowa band of the Nez Perce. In 1877 the army fought his people for more than three months as they tried to escape being forced onto a reservation. He surrendered at Bear Paw Mountain, Montana, after General Miles promised they could go home. Instead they were sent to Fort Leavenworth and then to Indian Territory, where, he says, seventy of his people died. In Washington he told his story through an interpreter, and the magazine printed it with an introduction by a missionary bishop. We read his words as the interpreter and editors set them down."
Tags: `own` (Joseph speaking for his own people), `officials` (the people who made and broke the promises are listening), `plea` (the purpose is a specific request), `after` (after the broken promises and exile), `reach` (the wider public can read it), `room` (space for length).
- Speaker: "Joseph, chief of the Wallowa band, in exile" [own] (real); "A sympathetic missionary bishop, writing about him" []; "An army officer who fought him" [].
- Audience: "Magazine readers and officials in Washington" [officials] (real); "His own people in Indian Territory" []; "Another Nez Perce band" [].
- Purpose: "Ask the government to let his people go home and live under equal law" [plea] (real); "Record the history of the war" []; "Warn of a new war" [].
- Moment: "1879, after surrender, exile and many deaths" [after] (real); "Spring 1877, before the war" []; "Autumn 1877, during the retreat" [].
- Medium: "Told through an interpreter, printed in a national magazine" [reach, room] (real); "A letter to one official" [room]; "A telegram" [].
- J1 "Good words do not last long unless they amount to something." Depends: after ("Before General Miles's promise was broken, the line has nothing to point at."), officials ("It is aimed at the people who gave the good words.").
- J2 "I have heard talk and talk, but nothing is done." Depends: own ("From a bishop or an officer, it becomes a complaint about someone else's wait."), after ("Before the exile, the long record of talk without action did not exist yet."). Note in the tool: the magazine prints "no- thing" across a line break; the tool joins it.
- J3 "The earth is the mother of all people, and all people should have equal rights upon it." Depends: own ("Coming from Joseph, it is his people's belief; from an officer, it is borrowed."), reach ("It is a principle for the whole public; in a letter to one official it loses its listeners.").
- J4 "If you tie a horse to a stake, do you expect he will grow fat?" Depends: plea ("The question argues for release; a history has no request to back."), officials ("'You' are the ones who hold the stake.").
- J5 "Let me be a free man--free to travel, free to stop, free to work, free to trade where I choose, free to choose my own teachers, free to follow the religion of my fathers, free to think and talk and act for myself--and I will obey every law, or submit to the penalty." Depends: plea ("It is a bargain offered to a government; a warning of war breaks it."), room ("A telegram cannot carry seven 'free to' clauses.").
Fit check for the build: with every row on its star, all 15 lines hold. Every non-real stop strains at least one line in its speech except Lincoln's "A funeral for soldiers", which keeps every line holding: a useful surprise the tool leaves in (a funeral is as grave as the inauguration).

## Interactions in detail
- Every flip recomputes all five lines at once (pure function: stops in, line statuses and reasons out). Holds and Strains badges change with a 150 ms flip (none with Motion off); the words always change.
- Two missing tags on one line show two reasons. A line that strains under two dials lists both dials.
- Which dial moved most: for each dial at a non-real stop, the number of lines that strain because of a tag only that dial removed; a line strained by two dials counts for both.
- What changed?: the mystery is drawn so that at least one line strains. "Right" means the student's setting gives the same strain pattern on all five lines. Six rounds, then **New round** keeps going; speech picker is hidden in this mode (rounds pick their own speech, named on screen).
- Rewrite saves per speech and full situation (`rss:v1`, try/catch): reopening that situation shows the saved text. **Copy all** writes plain text with each situation spelled out. **Clear all** asks "Clear every rewrite on this device?" with **Clear** and **Keep**.
- Speech or mode change calls `V.hush()` and stops the Player.
- Sizes: at 375 wide the rows shrink to two lines each (dial name above, stop below) with their arrows; the lines scroll beneath. At 680x425 all five rows and at least three line badges are visible without scrolling. No horizontal page scroll at any listed size.

## Look
- Base `kit:theme-912` (dark instrument), styled as a station departures board: black split-flap rows with warm lettering that clack over when flipped (a short flip animation and a soft click with Sound on; the letters change instantly with Motion off), above a teleprompter strip with a soft top glow. Accent `--brand #ffd18c` (warm footlight: header rule, flap lettering, Real setting star, selected card ring), `--brand-ink #1c1203`. Holds uses `--ok #6fdca6` with ✓, Strains `--warn #ffb8a8` with ✗; never color alone.
- Neighbors: argument-map blueprint cyan (dark), rhetoric-spotter electric blue (light), satire-decoder oxblood and usage-panel ink red (dark), audience-shift-briefing magenta (light). Nearest catalog accents: energy-accountant and polynomials-as-numbers (dE 13.5, both math and science, not ELA); the default theme amber `#f2a93b` is avoided (this is paler and pinker).
- Contrast (WCAG 2.1): ink on panel 14.70:1, on sec-bg 13.93:1; muted on sec-bg 7.71:1; brand on panel 12.16:1, on sec-bg 11.52:1; brand-ink on brand 12.97:1; ok on panel 10.27:1; warn on panel 10.45:1; focus on panel 12.03:1. All pass AA.

## Art
None: drawn in code (split-flap rows, teleprompter, badges). No portraits.

## Voice
Bank voice `knowing-guide` (Sadaltager), style "Say in a knowledgeable, friendly way, like a veteran speechwriter backstage." Not used by any family sibling or 9-12 ELA neighbor. `Curio.voice`, `scope: () => state.mode + state.speech`. Hear the line uses the same voice through the Player.
- w-explore (how): "Flip any row on the board. Watch which lines still hold."
- reasons (how, first strain): "Tap a line that strains to see why."
- real (how, first time three or more lines strain): "Press Real setting to flip every row back."
- w-mystery (how): "Someone changed the room. Flip the rows until the same lines strain, then lock your guess."
- right (event, Lock my guess when right; stale on New round): "That's the room."
- notyet (event, Lock my guess when not; stale on New round): "Not this one. Look at which lines differ."
- w-rewrite (how): "Pick a room, then rewrite a line that strains. Say why in one sentence."
- aloud (how, first saved rewrite): "Now read it aloud to a partner. Does it belong in this room?"

## Family engine
`kit/rhetoric.js`, described in full in tools/argument-map/spec.md. This tool uses: Passage (three speeches, five units each, in their full text for the drawer), Marks (the boxed lines in the drawer), Player (Hear the line), and Situation tags (each unit's `depends`; the dial stops and reasons live in the tool). Not Tagger, Map or Order. The pure strain function `situate(stops, units)` sits in the tool's marked pure block, exposed as `__tool.situate`.

## Sources
- Lincoln text: Avalon Project, Yale Law School, "Second Inaugural Address of Abraham Lincoln", https://avalon.law.yale.edu/19th_century/lincoln2.asp.
- Lincoln facts (Booth present; assassinated April 14, 1865; about six weeks later): Wikipedia, "Second inauguration of Abraham Lincoln", checked 2026-10-27. Frederick Douglass and Black soldiers in the crowd: confirm against the Library of Congress or the National Park Service (Lincoln Home) at build; drop the clause if not confirmed. About 600,000 deaths: confirm against the National Park Service, "Civil War Facts", at build.
- Roosevelt text: The American Presidency Project, "Address to Congress Requesting a Declaration of War with Japan", December 8, 1941, https://www.presidency.ucsb.edu/node/210408.
- Executive Order 9066 (February 19, 1942; about 122,000 removed; nearly 70,000 citizens; no charges): National Archives, "Executive Order 9066", https://www.archives.gov/milestone-documents/executive-order-9066.
- Chief Joseph text and facts (Bear Paw, General Miles's promise, Fort Leavenworth, Indian Territory, seventy deaths, the interpreter, Bishop Hare's introduction): North American Review, vol. 128, no. 269 (April 1879), Internet Archive, https://archive.org/details/sim_north-american-review_1879-04_128_269.
- "More than three months" (June to October 1877): National Park Service, Nez Perce National Historical Park, "The Nez Perce War of 1877"; confirm at build.

## Done when
- With every row on its star, all five lines hold in each speech; each non-real stop strains at least one line, except Lincoln's funeral stop, which strains none.
- Turning Roosevelt's Moment to "one year later" strains D1 and D3 with the "Yesterday" and "last night" reasons.
- Turning Lincoln's Purpose to "Demand that the South be punished" strains L5 with the malice reason and nothing else.
- Which dial moved most counts match the reasons shown.
- What changed?: setting the same strain pattern by a different stop counts as right.
- A rewrite and its because line survive a reload; Copy all copies plain text; Clear all asks first.
- Context cards appear for all three speeches, including Executive Order 9066 and the interpreter note.
- At 375 wide the rows stack with arrows; at 680x425 all rows and line badges show without scrolling; no horizontal scroll.

## Open questions
- The Roosevelt context card names Executive Order 9066 and the incarceration of Japanese Americans. Keep it on the card, or move it to teacher notes?
- Chief Joseph's statement is read as recorded by an interpreter and magazine editors. Should a Nez Perce (Nimiipuu) educator or the Nez Perce Tribe review the card and the Joseph name spelling before release?
