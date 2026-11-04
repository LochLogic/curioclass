// Rubrics and Checklists, grades K-12. A layout generator: no computed answers (noKey). Frames for judging work in the
// arts, PE, world languages and teamwork, built from the teacher's typed criteria or a built-in list for the subject:
//   analytic rubric (criteria x 3 or 4 named levels, points and evidence lines optional; one partner, or a panel
//   scoring 2 or 3 performers or groups on one grid), single-point rubric (grow, criterion, glow), peer feedback forms
//   (glow and grow, two stars and a wish, warm-cool-question, I noticed / I wonder / what if, describe-ask-suggest,
//   Critical Response Process, describe-analyze-interpret-judge, visitor comment card) with sentence starters by band
//   and an optional yes / not yet criteria checklist, ACTFL-style can-do self-checks (Novice, Intermediate, Advanced;
//   spoken or ASL; or a portfolio reflection against the level's descriptors), skill-cue checklists for PE or
//   performance (built-in cues for common skills or typed cues, a column for each try), K-2 faces and stars sheets,
//   and a build-a-rubric frame where students write the level descriptors or what strong work looks like.
// Starters, tips and some wording come from banks, so New sheet gives a fresh wording of the same frame. The teacher
// page holds a model of vague and specific feedback for the subject, or notes on the can-do and skill sheets.
// Standards: NCAS anchor 9 (apply criteria to evaluate work) and anchors 5 and 6 (refine, rehearse, present): DA:Re9,
// DA:Pr5, MU:Re9, MU:Pr5, TH:Re9, TH:Pr5, VA:Re9, VA:Cr3, MA:Re9, MA:Cr3; World-Readiness Standards for Learning
// Languages (Communication: interpersonal, interpretive, presentational) with the NCSSFL-ACTFL Can-Do Statements;
// SHAPE America National PE Standards (motor skills and movement concepts, peer observation); CCSS ELA SL.1.
(() => {
const { esc } = Gen.h;

const KINDS = [['rubric', 'Analytic rubric (criteria and levels)'], ['single', 'Single-point rubric (grow, criterion, glow)'],
  ['feedback', 'Peer feedback form'], ['cando', 'Can-do self-check (world languages)'], ['skill', 'Skill-cue checklist (PE or performance)'],
  ['faces', 'Faces and stars (grades K-2)'], ['build', 'Build-a-rubric frame']];
const GALL = [['k', 'Kindergarten'], ...Array.from({ length: 12 }, (_, i) => [String(i + 1), `Grade ${i + 1}`])];
const GFROM = { rubric: 3, single: 3, build: 3, cando: 3, feedback: 1, skill: 0, faces: 0 };
const gnum = g => g === 'k' ? 0 : +g;
const bandOf = g => { const n = gnum(g); return n <= 2 ? 'k2' : n <= 5 ? '35' : n <= 8 ? '68' : '912'; };
const BANDNAME = { k2: 'Grades K-2', 35: 'Grades 3-5', 68: 'Grades 6-8', 912: 'Grades 9-12' };
const LH = { k2: 0.44, 35: 0.34, 68: 0.3, 912: 0.29 };
const SUBJ = [['dance', 'Dance'], ['music', 'Music'], ['theater', 'Theater'], ['visual', 'Visual art'], ['media', 'Media arts'],
  ['pe', 'Physical education'], ['lang', 'World language'], ['general', 'Teamwork and presenting']];
const SNAME = Object.fromEntries(SUBJ);
const ANCHOR = { dance: 'Count or moment', music: 'Measure or moment', theater: 'Line or moment', visual: 'Part of the work', media: 'Time or shot',
  pe: 'Try or moment', lang: 'Line or moment', general: 'Moment' };

/* ---------- built-in criteria: [name, what strong work looks like], young (K-5) and older (6-12) ---------- */
const CRIT = {
  dance: { y: [['Spacing', 'Stays in their own space and in the right spot.'], ['Focus', 'Eyes go where the dance needs them; no talking.'],
    ['Energy', 'Moves are full and strong, not floppy.'], ['Timing', 'Moves match the beat and the counts.'], ['Clear shapes', 'Shapes are held still and easy to see.'],
    ['Start and end', 'A clear ready shape and a frozen end shape.'], ['Feeling shown', 'Face and body show the feeling.'], ['Levels and pathways', 'Uses high, middle and low levels and different pathways.']],
  o: [['Technique', 'Alignment, control and clean steps.'], ['Spacing and formations', 'Formations are clear and spacing stays even.'], ['Timing and musicality', 'On the counts; phrasing fits the music.'],
    ['Intent', 'The idea or message reads clearly to an audience.'], ['Performance quality', 'Focus, projection and commitment from start to finish.'], ['Transitions', 'Sections link smoothly.'],
    ['Structure', 'A clear form: motif, development and contrast.'], ['Originality', 'Fresh movement choices, not only borrowed steps.']] },
  music: { y: [['Steady beat', 'Keeps the beat steady all the way through.'], ['Tone', 'A clear, pleasant singing or playing sound.'], ['Rhythm', 'Sings or plays the rhythms correctly.'],
    ['Dynamics', 'Loud and soft where the music asks.'], ['Expression', 'The sound shows the mood of the music.'], ['Watching the leader', 'Eyes on the leader for starts and stops.'],
    ['Ending', 'Ends together and holds the last sound.'], ['Balance', 'Every part can be heard; no one covers the others.']],
  o: [['Tone', 'Full, focused, characteristic sound.'], ['Intonation', 'Pitches are in tune with the ensemble.'], ['Rhythm and tempo', 'Accurate rhythms at a steady, fitting tempo.'],
    ['Technique', 'Articulation, breath or bow control, and posture.'], ['Balance and blend', 'Parts are heard in the right proportion and blend.'], ['Dynamics and expression', 'Dynamic contrast and phrasing shape the music.'],
    ['Interpretation', 'Style and phrasing fit the piece and its era.'], ['Stage presence', 'Poised entrance, focus and a clean finish.']] },
  theater: { y: [['Voice', 'Loud, clear words the back row can hear.'], ['Body', 'The body shows who the character is.'], ['Face', 'The face shows the character\'s feelings.'],
    ['Staying in role', 'Stays in character the whole time.'], ['Listening', 'Listens and reacts to the other actors.'], ['Story', 'The audience can follow what happens.'],
    ['Using the stage', 'Faces the audience and does not block others.'], ['Teamwork', 'Shares the stage and helps the group.']],
  o: [['Objective', 'What the character wants is clear in every beat.'], ['Vocal choices', 'Projection, diction and variety.'], ['Physical choices', 'Posture, gesture and movement fit the character.'],
    ['Truthfulness', 'Reactions feel real, not shown on purpose.'], ['Blocking and stage picture', 'Clear sightlines and a balanced stage picture.'], ['Pacing', 'Cues are picked up and the scene keeps moving.'],
    ['Ensemble', 'Actors listen and support each other.'], ['Concept', 'Choices serve the story and the concept.']] },
  visual: { y: [['Neat and finished', 'Clean edges and no unfinished parts.'], ['Color', 'Colors are chosen on purpose.'], ['Lines and shapes', 'Lines and shapes are clear and varied.'],
    ['Tells a story', 'A viewer can tell what is happening.'], ['Fills the space', 'Uses the whole paper.'], ['Details', 'Small details make it interesting.'],
    ['Care and effort', 'Took time and tried their best.'], ['Own idea', 'The idea is the artist\'s own.']],
  o: [['Composition', 'Elements lead the eye, with balance and emphasis.'], ['Craftsmanship', 'Clean, controlled use of materials.'], ['Elements and principles', 'Line, shape, color, value and space are used on purpose.'],
    ['Concept and intent', 'The idea comes through to a viewer.'], ['Originality', 'A personal, inventive approach.'], ['Media skill', 'Technique fits the medium.'],
    ['Risk and experimentation', 'Tries new approaches and learns from them.'], ['Presentation', 'Finished, labeled and ready to display.']] },
  media: { y: [['Clear order', 'Beginning, middle and end are in order.'], ['Sound', 'Sound or music fits and can be heard.'], ['Pictures', 'Pictures are clear and help tell the story.'],
    ['Clear message', 'The audience knows what it is about.'], ['Eye-catching design', 'Colors and layout grab attention.'], ['Readable words', 'Words are big enough to read.'],
    ['Smooth motion', 'Movement looks smooth, not jumpy.'], ['Teamwork', 'Everyone on the crew helped.']],
  o: [['Story and structure', 'A clear arc with a strong opening and ending.'], ['Framing and shots', 'Shot choices serve the story.'], ['Editing and pacing', 'Cuts are clean and the rhythm fits the mood.'],
    ['Sound design', 'Dialogue, music and effects are clear and balanced.'], ['Clarity of message', 'The audience gets the main idea.'], ['Audience fit', 'Style and content fit the intended audience.'],
    ['Technical quality', 'Exposure, focus and audio levels are clean.'], ['Fairness and context', 'Voices are balanced and facts have context.']] },
  pe: { y: [['Safety', 'Follows the safety rules.'], ['Uses the cues', 'Shows the cues for the skill.'], ['Effort', 'Keeps trying the whole time.'], ['Self-space', 'Stays in their own space.'],
    ['Teamwork', 'Passes, shares and helps.'], ['Fair play', 'Follows the rules and is a good sport.'], ['Listening', 'Stops and listens on the signal.'], ['Tries again', 'Keeps going after a miss.']],
  o: [['Skill technique', 'Uses the critical cues with control.'], ['Positioning', 'Moves to open space and covers space on defense.'], ['Decision making', 'Picks the right play at the right time.'],
    ['Communication', 'Calls for the ball and talks to teammates.'], ['Teamwork', 'Involves every teammate.'], ['Effort', 'Hustles on and off the ball.'],
    ['Sportsmanship', 'Respects opponents, officials and rules.'], ['Safety', 'Plays under control and uses equipment safely.']] },
  lang: { y: [['Easy to understand', 'A listener or reader can follow it.'], ['Vocabulary', 'Uses new words from our unit.'], ['Accuracy', 'Words and sentences are mostly correct.'],
    ['Clear delivery', 'Clear sounds, or clear handshapes and movement in ASL.'], ['Complete', 'Includes every part of the task.'], ['Effort', 'Tries to use the language the whole time.'],
    ['Organization', 'Ideas are in a clear order.'], ['Culture', 'Includes a cultural detail we learned.']],
  o: [['Comprehensibility', 'A listener or reader understands it without effort.'], ['Vocabulary', 'Varied, accurate, on-topic words.'], ['Language control', 'Accurate grammar, agreement and verb forms.'],
    ['Fluency', 'Keeps going with few long pauses.'], ['Organization', 'Ideas connect with transitions.'], ['Register', 'Formal or informal language fits the audience.'],
    ['Evidence and content', 'Ideas are supported with examples or sources.'], ['Clear delivery', 'Clear pronunciation, or clear handshapes and movement in ASL.']] },
  general: { y: [['Listening', 'Listens and does not interrupt.'], ['Teamwork', 'Shares the work and helps others.'], ['Effort', 'Keeps working until it is done.'], ['Clear speaking', 'Speaks clearly so others can hear.'],
    ['Preparation', 'Has materials ready.'], ['Kindness', 'Uses kind words.'], ['Problem solving', 'Tries ideas when stuck.'], ['Finishing', 'Finishes the job on time.']],
  o: [['Communication', 'Clear, respectful and to the point.'], ['Teamwork', 'Shares the load and builds on others\' ideas.'], ['Reliability', 'On time, prepared and follows through.'],
    ['Problem solving', 'Finds causes and tries workable fixes.'], ['Time management', 'Plans steps and meets deadlines.'], ['Initiative', 'Starts tasks without being asked.'],
    ['Eye contact and clarity', 'Looks at the audience and speaks clearly.'], ['Examples', 'Backs up points with specific examples.']] },
};

/* ---------- K-2 faces sheets: lines about myself and lines about someone else ---------- */
const FACE = {
  dance: { self: ['I kept my own space.', 'I froze when the music stopped.', 'I landed softly.', 'I looked where I went.', 'I showed a feeling.', 'I held my end shape.'],
    other: ['Big, clear moves', 'Showed a feeling', 'Stayed in their space', 'Still end shape', 'High and low moves', 'Moved with the music'] },
  music: { self: ['I used my singing voice.', 'I kept a steady beat.', 'I shared my song.', 'I watched the leader.', 'I listened to others.', 'I stopped at the end.'],
    other: ['Steady beat', 'Singing voice', 'Clear words', 'Loud and soft', 'Good ending', 'Brave sharing'] },
  theater: { self: ['I stayed in role.', 'I used a loud voice.', 'I used my body.', 'I listened.', 'I used my prop.', 'I used my face.'],
    other: ['Loud voice', 'Big body', 'Clear feelings', 'Stayed in role', 'Clear story', 'Listened to others'] },
  visual: { self: ['My art is neat.', 'My art is finished.', 'My art tells a story.', 'I used many colors.', 'I filled the page.', 'I tried my best.'],
    other: ['Bright colors', 'Lines', 'Shapes', 'Tells a story', 'Neat', 'Lots of details'] },
  media: { self: ['My story is in order.', 'My sound fits.', 'My pictures are clear.', 'I shared with my crew.', 'I listened to my crew.', 'I helped my crew.'],
    other: ['Clear order', 'Good sound', 'Clear pictures', 'Easy to read', 'Clear message', 'Eye-catching'] },
  pe: { self: ['I stayed in my space.', 'I used the cues.', 'I tried my best.', 'I took turns.', 'I played safe.', 'I helped a friend.'],
    other: ['Safe moves', 'Used the cues', 'Tried hard', 'Took turns', 'Played fair', 'Kind words'] },
  lang: { self: ['I said hello.', 'I used new words.', 'I listened.', 'I asked a question.', 'I sang along.', 'I tried my best.'],
    other: ['Said hello', 'Used new words', 'Clear voice', 'Asked a question', 'Listened', 'Tried hard'] },
  general: { self: ['I listened.', 'I took turns.', 'I shared.', 'I tried my best.', 'I helped.', 'I finished my work.'],
    other: ['Listened', 'Took turns', 'Shared', 'Kind words', 'Tried hard', 'Finished'] },
};

/* ---------- word banks for young students ---------- */
const WORDS = {
  dance: ['level', 'speed', 'shape', 'pathway', 'energy', 'freeze', 'beat', 'feeling', 'balance'],
  music: ['beat', 'rhythm', 'loud', 'soft', 'fast', 'slow', 'high', 'low', 'melody'],
  theater: ['voice', 'face', 'body', 'character', 'gesture', 'prop', 'setting', 'feeling', 'listen'],
  visual: ['line', 'shape', 'color', 'texture', 'pattern', 'space', 'bright', 'dark', 'detail'],
  media: ['order', 'sound', 'picture', 'shot', 'music', 'title', 'message', 'color', 'motion'],
  pe: ['cue', 'aim', 'step', 'follow through', 'balance', 'space', 'speed', 'safe', 'teamwork'],
  lang: ['word', 'sound', 'question', 'greeting', 'clear', 'loud', 'new word', 'sentence', 'answer'],
  general: ['listen', 'share', 'help', 'kind', 'clear', 'ready', 'team', 'finish', 'idea'],
};

/* ---------- skill presets: cues commonly taught for each skill ---------- */
const SKILLS = [
  ['overhand', 'Overhand throw', ['Side to the target', 'Arm way back', 'Step with the opposite foot', 'Turn hips and shoulders', 'Follow through across the body']],
  ['underhand', 'Underhand throw', ['Face the target', 'Swing the arm back', 'Step with the opposite foot', 'Let go at waist height', 'Follow through to the target']],
  ['catch', 'Catch', ['Ready hands', 'Eyes on it', 'Reach for it', 'Hands give (pull it in)']],
  ['kick', 'Kick', ['Run up to the ball', 'Plant foot beside the ball', 'Eyes on the ball', 'Kick with the laces or inside of the foot', 'Follow through to the target']],
  ['skip', 'Skip', ['Step, then hop', 'Switch feet each time', 'Arms swing', 'Light feet']],
  ['jump', 'Jump and land', ['Arms swing back, then forward', 'Bend knees to take off', 'Take off on two feet', 'Land on two feet', 'Bend knees to land softly']],
  ['dribble', 'Dribble (hands)', ['Finger pads, not the palm', 'Push the ball down', 'Ball at waist height or lower', 'Eyes up', 'Ball to the side, away from the defender']],
  ['chest', 'Chest pass', ['Ball at the chest, thumbs behind', 'Step toward the target', 'Push and straighten the arms', 'Thumbs point down at the finish', 'Aim at the partner\'s chest']],
  ['forearm', 'Forearm pass (volleyball)', ['Ready stance, knees bent', 'Hands together, arms straight', 'Contact on the forearms', 'Lift with the legs, not a big arm swing', 'Angle the platform to the target']],
  ['scarf', 'Scarf juggling', ['Toss across the body', 'Toss to eye level or higher', 'Toss the next scarf when the last one peaks', 'Catch with a clawing, palm-down hand', 'Keep a steady rhythm']],
  ['forehand', 'Forehand strike (racket or paddle)', ['Side to the net', 'Racket back early', 'Step with the opposite foot', 'Contact beside the front foot', 'Follow through over the shoulder']],
  ['chip', 'Golf-style chip', ['Narrow stance', 'Weight on the front foot', 'Hands ahead of the ball', 'Rock the shoulders like a pendulum', 'Hold the finish toward the target']],
  ['batting', 'Batting swing', ['Side stance, hands together', 'Eyes on the ball', 'Step toward the pitch', 'Turn the hips and swing level', 'Follow through']],
  ['custom', 'Your own skill (type the cues below)', []],
];
const SKILL = Object.fromEntries(SKILLS.map(s => [s[0], s]));

/* ---------- level names and the wording inside the level boxes ---------- */
const SCALES = [['auto', 'Set by grade (Not yet to Got it, or Beginning to Advanced)'], ['grow', 'Not yet, Getting there, Got it, Above and beyond'],
  ['std', 'Beginning, Developing, Proficient, Advanced'], ['num', 'Numbers only (1 to 4)']];
const LNAMES = { grow: { 3: ['Not yet', 'Getting there', 'Got it'], 4: ['Not yet', 'Getting there', 'Got it', 'Above and beyond'] },
  std: { 3: ['Developing', 'Proficient', 'Advanced'], 4: ['Beginning', 'Developing', 'Proficient', 'Advanced'] },
  num: { 3: ['1', '2', '3'], 4: ['1', '2', '3', '4'] } };
const QUAL = {
  3: [['Not yet', 'Sometimes', 'Every time'], ['Not yet seen', 'Starting to show', 'Clear and strong'], ['Missing or unclear', 'Shows up in places', 'Strong throughout'],
    ['Not there yet', 'Partly there', 'All there']],
  4: [['Not yet seen', 'Sometimes', 'Most of the time', 'Every time'], ['Not yet', 'Starting to show', 'Clear most of the way', 'Clear and strong throughout'],
    ['Missing or unclear', 'Shows up in places', 'Shows up most of the way', 'Strong from start to finish'], ['Not there yet', 'Partly there', 'Mostly there', 'All there, with bold choices']],
};

/* ---------- feedback protocols ---------- */
const PROTOS = [['glow1', 'Glow and grow (one each)'], ['glow2', 'Two glows and a grow'], ['glow22', 'Two strengths, two next steps'], ['stars', 'Two stars and a wish'],
  ['wcq', 'Warm, cool, question'], ['notice', 'I noticed, I wonder, what if'], ['das', 'Describe, ask, suggest'], ['clr', 'Critical Response Process (4 steps)'],
  ['daij', 'Describe, analyze, interpret, judge'], ['card', 'Visitor comment card (notice, kind question)']];
const PNAME = Object.fromEntries(PROTOS);
const PTITLE = { glow1: 'Glow and Grow', glow2: 'Two Glows and a Grow', glow22: 'Two Strengths, Two Next Steps', stars: 'Two Stars and a Wish', wcq: 'Warm, Cool, Question',
  notice: 'I Noticed, I Wonder, What If', das: 'Describe, Ask, Suggest', clr: 'Critical Response', daij: 'Describe, Analyze, Interpret, Judge', card: 'Visitor Comment Card' };
const PSECS = {
  glow1: [['glow', 'Glow'], ['grow', 'Grow']], glow2: [['glow', 'Glow'], ['glow', 'Glow'], ['grow', 'Grow']],
  glow22: [['glow', 'Strength'], ['glow', 'Strength'], ['grow', 'Next step'], ['grow', 'Next step']], stars: [['star', 'Star'], ['star', 'Star'], ['wish', 'Wish']],
  wcq: [['warm', 'Warm'], ['cool', 'Cool'], ['ques', 'Question'], ['resp', 'Artist\'s response']], notice: [['notice', 'I noticed'], ['wonder', 'I wonder'], ['whatif', 'What if']],
  das: [['describe', 'Describe'], ['ask', 'Ask'], ['suggest', 'Suggest']],
  clr: [['meaning', '1. Statements of meaning'], ['artistq', '2. Artist as questioner'], ['neutral', '3. Neutral questions'], ['opinion', '4. Permissioned opinions']],
  daij: [['describe', 'Describe'], ['analyze', 'Analyze'], ['interpret', 'Interpret'], ['judge', 'Judge']],
  card: [['notice', 'One thing I notice'], ['kindq', 'One kind question'], ['resp', 'The artist\'s answer']],
};
const SECQ = {   // a short guiding prompt beside each section label
  glow: 'What worked? Name the moment.', grow: 'What could be stronger? Be kind and specific.', star: 'Something done well.', wish: 'Something to try next time.',
  warm: 'A strength you noticed.', cool: 'A place that could be clearer or stronger.', ques: 'Something you want to know.', resp: 'The artist answers here.',
  notice: 'What you saw or heard, without judging.', wonder: 'A question the work raised.', whatif: 'An idea to try.',
  describe: 'Only what you saw or heard.', ask: 'A question about a choice.', suggest: 'One idea, tied to a moment.',
  meaning: 'What was meaningful, striking or exciting?', artistq: 'The artist asks; responders answer.', neutral: 'Questions with no opinion hidden inside.',
  opinion: 'Ask first: "I have an opinion about ... Would you like to hear it?"', analyze: 'How do the parts work together?', interpret: 'What does it mean or express?',
  judge: 'How well does it work? Use the criteria.', kindq: 'Ask about a choice the artist made.',
};
const ST = {   // sentence starters by section, young (K-5) and older (6-12)
  glow: { y: ['I liked how you', 'You did a great job', 'My favorite part was', 'It was strong when you'], o: ['One strength was', 'It worked well when', 'The strongest moment was', 'A clear choice was', 'You showed'] },
  grow: { y: ['Next time, try', 'You could', 'Maybe add', 'One thing to work on is'], o: ['One next step is', 'Consider', 'It could be stronger if', 'Try', 'To sharpen this, you could'] },
  star: { y: ['I liked', 'You were great at', 'My favorite part was'], o: ['One strength was', 'It worked well when', 'The strongest moment was'] },
  wish: { y: ['I wish', 'Next time, maybe', 'I hope you try'], o: ['I wish', 'Next time, consider', 'I would love to see'] },
  warm: { y: ['I liked', 'It made me feel', 'You did well at'], o: ['A strong choice was', 'I was drawn to', 'It works when'] },
  cool: { y: ['It was hard to see', 'Maybe change', 'I was not sure about'], o: ['I was unsure about', 'It might be clearer if', 'I wanted more'] },
  ques: { y: ['Why did you', 'How did you'], o: ['How did you decide', 'Why did you choose', 'What were you hoping'] },
  resp: { y: ['I chose this because', 'I was trying to'], o: ['I chose this because', 'I was trying to', 'Next I plan to'] },
  notice: { y: ['I noticed', 'I saw', 'I heard', 'I spotted'], o: ['I noticed', 'I observed', 'One detail I saw was'] },
  wonder: { y: ['I wonder', 'I wonder why', 'I wonder how'], o: ['I wonder', 'I wonder why', 'I wonder how'] },
  whatif: { y: ['What if', 'What if you tried'], o: ['What if', 'What if you tried', 'What would happen if'] },
  describe: { y: ['I saw', 'I heard', 'There was'], o: ['I saw', 'I heard', 'The work shows'] },
  ask: { y: ['Why did you', 'How did you'], o: ['Why did you', 'How did you', 'What were you thinking when'] },
  suggest: { y: ['You might try', 'Maybe'], o: ['You might try', 'Consider', 'What if you'] },
  meaning: { y: ['I liked', 'I remember'], o: ['I was struck by', 'It was meaningful when', 'I remember', 'It was exciting when'] },
  artistq: { y: ['The artist asked'], o: ['The artist asked', 'The artist wanted to know'] },
  neutral: { y: ['What were you', 'How did you'], o: ['What were you', 'How did you decide', 'What was your thinking when', 'What happens when'] },
  opinion: { y: ['I have an opinion about'], o: ['I have an opinion about', 'I have an opinion on'] },
  analyze: { y: ['The parts fit together by'], o: ['The parts work together by', 'The pattern I see is', 'Contrast shows up when'] },
  interpret: { y: ['I think it means'], o: ['I think it means', 'The mood is', 'The artist may be saying'] },
  judge: { y: ['I think it works because'], o: ['I think it is successful because', 'It works best when', 'Using the criteria, I judge'] },
  kindq: { y: ['How did you', 'Why did you'], o: ['How did you', 'Why did you', 'What gave you the idea'] },
};
const ANCHORED = new Set(['glow', 'grow', 'star', 'wish', 'warm', 'cool', 'describe', 'notice', 'suggest']);

/* ---------- can-do statements: [mode, spoken, signed (when different)] ---------- */
const MODES = { ip: ['Interpersonal', 'talking with others', 'signing with others'], it: ['Interpretive', 'understanding what I hear or read', 'understanding what I see signed'],
  pr: ['Presentational', 'speaking or writing to an audience', 'signing to an audience'] };
const CAN = {
  novice: [
    ['ip', 'I can greet people, introduce myself and say goodbye.', 'I can greet people, introduce myself and sign goodbye.'],
    ['ip', 'I can ask and answer simple questions about my family, school and likes.'],
    ['ip', 'I can say what I like and do not like, and ask others what they like.', 'I can sign what I like and do not like, and ask others what they like.'],
    ['ip', 'I can ask someone to repeat or slow down when I do not understand.'],
    ['it', 'I can recognize familiar words and phrases when I hear them.', 'I can recognize familiar signs and phrases when I see them.'],
    ['it', 'I can understand simple questions about myself, like my name and age.'],
    ['it', 'I can understand numbers, dates and times in a short message.', 'I can understand numbers, dates and times in a short signed message.'],
    ['it', 'I can find familiar words in a short text, such as a menu, sign or schedule.', 'I can understand fingerspelled names and familiar fingerspelled words.'],
    ['pr', 'I can introduce myself and my family to a group.'],
    ['pr', 'I can describe my home, school or a friend with simple phrases.'],
    ['pr', 'I can tell about my daily routine with phrases I have practiced.'],
    ['pr', 'I can write lists and fill out a simple form about myself.', 'I can fingerspell my name and short words clearly.'],
  ],
  intermediate: [
    ['ip', 'I can start, keep going and end a conversation on a familiar topic.'],
    ['ip', 'I can ask and answer questions about daily life, plans and past events.'],
    ['ip', 'I can make plans with someone: what to do, where and when.'],
    ['ip', 'I can handle an everyday situation, such as ordering food or buying a ticket.'],
    ['it', 'I can understand the main idea and some details of a short conversation or video.', 'I can understand the main idea and some details of a short signed conversation or video.'],
    ['it', 'I can understand the main idea of short texts like messages, ads and articles.', 'I can understand the main idea of a short signed story or announcement.'],
    ['it', 'I can follow directions and announcements about everyday things.'],
    ['it', 'I can understand questions about my opinions and experiences.'],
    ['pr', 'I can describe people, places and things in connected sentences.'],
    ['pr', 'I can tell about something that happened, using past time.'],
    ['pr', 'I can give a short presentation on a familiar topic with some details.'],
    ['pr', 'I can write a short message or story in connected sentences.', 'I can sign a short story, using space and classifiers to show where things are.'],
  ],
  advanced: [
    ['ip', 'I can carry on a conversation about events in the past, present and future.'],
    ['ip', 'I can handle a situation with a complication, such as fixing a problem with a purchase.'],
    ['ip', 'I can exchange and support opinions on community or current-event topics.'],
    ['ip', 'I can explain and defend a point of view when someone disagrees.'],
    ['it', 'I can follow the main ideas and many details of a lecture, news report or interview.', 'I can follow the main ideas and many details of a signed lecture, news report or interview.'],
    ['it', 'I can understand the main ideas and supporting details of an article or essay.', 'I can follow a long signed story with role shift and changes in time.'],
    ['it', 'I can tell fact from opinion in an argument I hear or read.', 'I can tell fact from opinion in a signed argument.'],
    ['it', 'I can explain how a speaker or writer shows a point of view.', 'I can explain how a signer shows a point of view.'],
    ['pr', 'I can narrate and describe in past, present and future in connected paragraphs.', 'I can narrate and describe in past, present and future with clear, connected structure.'],
    ['pr', 'I can give an organized presentation on a social or academic topic.'],
    ['pr', 'I can write a well-organized essay that compares viewpoints with details.', 'I can tell an extended story using role shift, eye gaze and classifiers.'],
    ['pr', 'I can adjust my language for formal and informal audiences.', 'I can adjust my signing for formal and informal audiences.'],
  ],
};
const LEVELS = [['novice', 'Novice'], ['intermediate', 'Intermediate'], ['advanced', 'Advanced']];
const LNAME = Object.fromEntries(LEVELS);
// the ACTFL Proficiency Guidelines, paraphrased: the level, then its Low, Mid and High sublevels
const DESC = {
  novice: ['Communicates with single words, lists and memorized phrases on very familiar topics.',
    ['Low', 'Uses a few isolated words and memorized phrases.'], ['Mid', 'Uses memorized words and phrases on familiar topics, often with pauses.'],
    ['High', 'Handles many simple tasks with memorized language and sometimes makes new sentences, but cannot keep it up.']],
  intermediate: ['Creates with language: asks and answers questions and uses sentences and strings of sentences on everyday topics.',
    ['Low', 'Makes simple sentences on familiar topics, with effort, in a few uncomplicated situations.'], ['Mid', 'Handles a variety of everyday situations with sentences and some strings of sentences.'],
    ['High', 'Handles everyday situations with ease and often narrates and describes in connected paragraphs, but cannot keep it up across time frames.']],
  advanced: ['Narrates and describes in past, present and future in connected paragraphs, and handles a situation with a complication.',
    ['Low', 'Narrates and describes in the major time frames in paragraphs, with some breakdowns.'], ['Mid', 'Narrates and describes in all major time frames with good control and detail.'],
    ['High', 'Does advanced tasks with ease and confidence, and sometimes supports opinions and hypothesizes, but not consistently.']],
};

/* ---------- small banks: tips, evidence starters, closing prompts, drawing prompts ---------- */
const TIPS = {
  y: ['Look and listen first. Then mark.', 'Be kind and be honest.', 'Say what you saw, not just "good job."', 'Point to the part you mean.', 'Tell what you saw or heard.'],
  o: ['Name the moment: a count, a measure, a line or a time.', 'Describe before you judge.', 'Specific beats general: "the turn at count 5" beats "the dancing."',
    'Kind, specific and helpful: aim for all three.', 'Tie every rating to something you saw or heard.', 'A next step should be something the person can try tomorrow.'],
};
const EVID = { y: ['I saw', 'I heard', 'For example,', 'One time,'], o: ['For example, at', 'The clearest moment was', 'I saw this when', 'At'] };
const AFTER = [['next', 'One strength and one next step'], ['goals', 'Two goals'], ['lowest', 'Plan for the lowest-rated criterion'], ['change', 'One moment to do differently'], ['none', 'Nothing after the rubric']];
const SKAFTER = [['both', 'Cue seen most, cue to work on, praise and tip'], ['cues', 'Cue seen most and cue to work on'], ['praise', 'One praise and one tip'], ['none', 'Nothing after the grid']];
const CLOSE = {
  next: { self: [['One strength', ['My strongest area was', 'I am proud of', 'I did well at']], ['One next step', ['Next time I will', 'I want to work on', 'My next step is']]],
    other: [['One strength', ['Your strongest area was', 'You did well at', 'A real strength was']], ['One next step', ['Next time, try', 'One thing to practice is', 'Your next step could be']]] },
  goals: { self: [['Goal 1', ['I will', 'My goal is to', 'Next time I want to']], ['Goal 2', ['I will also', 'Another goal is to', 'I also want to']]],
    other: [['Goal 1', ['You could aim to', 'A goal for you:', 'Try to']], ['Goal 2', ['Another goal:', 'You could also', 'Also try to']]] },
  lowest: { self: [['My lowest criterion', ['The area I scored lowest was', 'My lowest score was in']], ['My plan to improve it', ['To improve, I will', 'I will practice by', 'My plan is to']]],
    other: [['The area to work on most', ['The area that needs the most work is', 'The lowest score was in']], ['One way to practice it', ['You could practice by', 'Try', 'One drill that would help is']]] },
  change: { self: [['One moment I would do differently', ['If I did it again, at', 'I would change the part where']], ['How and why', ['I would', 'This would help because']]],
    other: [['One moment to change', ['The moment I would change is', 'At']], ['How and why', ['You could', 'This would help because']]] },
};
const DRAWS = [['like', 'Draw one thing you liked'], ['fav', 'Draw a favorite moment'], ['change', 'Draw one thing to change'], ['goal', 'Draw your goal'], ['none', 'No drawing box']];
const DRAWQ = { like: ['Draw one thing you liked.', 'Draw the part you liked best.', 'Draw something you liked.'], fav: ['Draw your favorite moment.', 'Draw the best part.', 'Draw a moment you remember.'],
  change: ['Draw one thing to change next time.', 'Draw one thing to do better.', 'Draw what you will try next time.'], goal: ['Draw your goal for next time.', 'Draw what you want to get better at.', 'Draw your next goal.'] };

/* ---------- parsing typed lists ---------- */
// "a, b, c" or "a; b; c" (semicolons win, so items may hold commas) -> up to max trimmed items, each at most maxLen long
function list(text, max, maxLen) {
  const t = String(text || '').trim();
  if (!t) return [];
  const parts = t.split(/[;\n]/.test(t) ? /\s*[;\n]+\s*/ : /\s*,\s*/).map(x => x.trim()).filter(Boolean);
  return parts.slice(0, max).map(x => x.length > maxLen ? x.slice(0, maxLen - 3).replace(/\s+\S*$/, '') + '...' : x);
}
// criteria: "Name: what strong looks like" or just "Name"; two or more, or none (the caller falls back to the built-in list)
function critList(text, max = 8) {
  const out = list(text, max, 120).map(x => {
    const i = x.indexOf(':');
    if (i > 0 && i < 40) return [x.slice(0, i).trim(), x.slice(i + 1).trim()];
    return [x.length > 40 ? x.slice(0, 37).replace(/\s+\S*$/, '') + '...' : x, ''];
  }).filter(c => c[0]);
  return out.length >= 2 ? out : [];
}
const cap = s => s.charAt(0).toUpperCase() + s.slice(1);

/* ---------- drawing pieces ---------- */
const FACEP = { yes: 'M12 24 Q20 32 28 24', mid: 'M13 27 H27', no: 'M12 30 Q20 22 28 30' };
const faceSvg = k => `<svg class="rc-ico" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17" fill="none" stroke="#222" stroke-width="2"/><circle cx="14" cy="16" r="2.2" fill="#222"/><circle cx="26" cy="16" r="2.2" fill="#222"/><path d="${FACEP[k]}" fill="none" stroke="#222" stroke-width="2.2" stroke-linecap="round"/></svg>`;
const starSvg = () => `<svg class="rc-ico" viewBox="0 0 40 40" aria-hidden="true"><polygon points="20,3 25,15 38,15 28,23 32,36 20,28 8,36 12,23 2,15 15,15" fill="none" stroke="#222" stroke-width="2" stroke-linejoin="round"/></svg>`;
const box = '<span class="rc-box" aria-hidden="true"></span>';
const ln = (label, starter, cls = '') => `<p class="rc-ln${cls ? ' ' + cls : ''}">${label ? `<b>${esc(label)}</b>` : ''}<span>${starter ? `<i>${esc(starter)}</i>` : ''}</span></p>`;
const lines = (n, lh, starter) => `<div class="rc-lines" style="--lh:${lh}in">${Array.from({ length: n }, (_, i) => `<span>${i === 0 && starter ? `<i>${esc(starter)}</i>` : ''}</span>`).join('')}</div>`;
const critCell = c => `<span class="rc-crit">${esc(c[0])}</span>${c[1] ? `<span class="rc-look">${esc(c[1])}</span>` : ''}`;
const wordBank = (subj, k2) => `<p class="rc-bank"><b>Word bank:</b> ${WORDS[subj].slice(0, k2 ? 6 : 9).map(w => `<span>${esc(w)}</span>`).join('')}</p>`;
const whoLabel = (who, n, i) => who === 'group' ? (n > 1 ? `Group ${i + 1}` : 'Group') : who === 'recv' ? `Reviewer ${i + 1}` : n > 1 ? `Classmate ${i + 1}` : 'Partner';
const levelNames = (v, b, L) => LNAMES[v.scale === 'auto' || !LNAMES[v.scale] ? (b === '35' || b === 'k2' ? 'grow' : 'std') : v.scale][L];

/* ---------- the kinds: each returns { html } ---------- */
const BUILD = {
  rubric(c) {
    const { v, r, b, crit, yo, who, perf } = c, L = +v.levels, names = levelNames(v, b, L), qual = r.pick(QUAL[L]);
    const pts = !!v.points, num = names[0] === '1';
    if (perf > 1) {   // a panel grid: one score column per performer, the scale printed as a key
      const key = `<p class="rc-key"><b>Score each criterion:</b> ${names.map((n, i) => `<span>${i + 1} = ${num ? esc(qual[i]) : `${esc(n)} (${esc(qual[i].toLowerCase())})`}</span>`).join(' ')}</p>`;
      const cols = Array.from({ length: perf }, (_, i) => whoLabel(who, perf, i));
      const rows = crit.map(cr => `<tr><td class="rc-left">${critCell(cr)}</td>${cols.map(() => '<td class="rc-score"></td>').join('')}</tr>`).join('');
      const total = pts ? `<tr class="rc-total"><td class="rc-left"><b>Total</b> (out of ${crit.length * L})</td>${cols.map(() => '<td></td>').join('')}</tr>` : '';
      const nm = `<tr class="rc-names"><td class="rc-left"><b>Name or group</b></td>${cols.map(() => '<td></td>').join('')}</tr>`;
      const table = `<table class="rc-table rc-panel"><colgroup><col style="width:${perf === 3 ? 46 : 54}%">${cols.map(() => '<col>').join('')}</colgroup><thead><tr><th>Criterion</th>${cols.map(x => `<th>${esc(x)}</th>`).join('')}</tr></thead><tbody>${nm}${rows}${total}</tbody></table>`;
      const cards = cols.map(x => `<div class="rc-card"><p class="rc-cardh">${esc(x)}</p>${ln('Strength:', r.pick(ST.glow[yo]))}${ln('', '')}${ln('Next step:', r.pick(ST.grow[yo]))}${ln('', '')}</div>`).join('');
      return { html: key + table + `<h3 class="rc-h">Comments</h3>` + cards };
    }
    const ev = v.evidence, evs = r.pick(EVID[yo]);
    const head = i => num ? `${i + 1}` : `${esc(names[i])}${pts ? ` <span class="rc-pt">${i + 1}</span>` : ''}`;
    const rows = crit.map(cr => `<tr><td class="rc-left">${critCell(cr)}</td>${names.map((_, i) => `<td class="rc-cell"><span class="rc-q">${esc(qual[i])}</span></td>`).join('')}</tr>` +
      (ev ? `<tr class="rc-evrow"><td colspan="${L + 1}">${ln('Evidence:', evs)}</td></tr>` : '')).join('');
    const total = pts ? `<p class="rc-totalp"><b>Total:</b> <span class="rc-blank rc-sm"></span> out of ${crit.length * L}</p>` : '';
    return { html: `<table class="rc-table rc-rubric${ev ? ' rc-ev' : ''}"><colgroup><col style="width:${L === 3 ? 31 : 27}%">${names.map(() => '<col>').join('')}</colgroup><thead><tr><th>Criterion</th>${names.map((_, i) => `<th>${head(i)}</th>`).join('')}</tr></thead><tbody>${rows}</tbody></table>${total}` };
  },
  single(c) {
    const { r, crit, yo, b } = c, h = b === '35' ? 0.95 : 0.85;
    const [gl, gr] = yo === 'y' ? [['I see it!', 'What shows it is there'], ['Not yet', 'What to work on']] : [['Glow', 'Evidence it is there'], ['Grow', 'What would make it stronger']];
    const rows = crit.map(cr => `<tr style="height:${h}in"><td></td><td class="rc-mid">${critCell(cr)}</td><td></td></tr>`).join('');
    return { html: `<p class="rc-sub">${esc(r.pick(['The middle column says what strong work looks like.', 'Each criterion in the middle describes the target.', 'The middle column is the goal; the sides are for what you see.']))}</p>` +
      `<table class="rc-table rc-single"><colgroup><col style="width:33%"><col style="width:34%"><col style="width:33%"></colgroup><thead><tr><th>${gr[0]}<span class="rc-thq">${gr[1]}</span></th><th>Criteria<span class="rc-thq">What strong work looks like</span></th><th>${gl[0]}<span class="rc-thq">${gl[1]}</span></th></tr></thead><tbody>${rows}</tbody></table>` };
  },
  feedback(c) {
    const { v, r, b, crit, yo, who, perf, subj } = c, k2 = b === 'k2', secs = PSECS[v.protocol];
    const cols = Array.from({ length: perf }, (_, i) => whoLabel(who, perf, i));
    let html = '';
    if (v.bank && yo === 'y') html += wordBank(subj, k2);
    if (v.checks) {
      const opts = yo === 'y' ? ['Yes', 'Not yet'] : ['Yes', 'Partly', 'Not yet'];
      const head = perf > 1 ? cols.map(x => `<th>${esc(x)}<span class="rc-thq">${opts.join(' / ')}</span></th>`).join('') : opts.map(o => `<th>${o}</th>`).join('');
      const cells = perf > 1 ? cols.map(() => `<td class="rc-circle">${opts.map(o => `<span>${o}</span>`).join('')}</td>`).join('') : opts.map(() => `<td class="rc-tick">${box}</td>`).join('');
      html += `<h3 class="rc-h">${esc(r.pick(['Criteria check', 'Look for these', 'Checklist']))}</h3><table class="rc-table rc-checks"><colgroup><col style="width:${perf > 1 ? 40 : 58}%"></colgroup><thead><tr><th>Criterion</th>${head}</tr></thead><tbody>${crit.map(cr => `<tr><td class="rc-left">${critCell(cr)}</td>${cells}</tr>`).join('')}</tbody></table>`;
    }
    const nl = k2 ? 1 : perf === 1 ? (secs.length <= 3 ? (yo === 'o' ? 4 : 3) : 3) : 2;
    const form = x => {
      const s = secs.map(([k, lab]) => {
        const icon = k === 'star' ? starSvg() : k === 'wish' ? '<span class="rc-wish" aria-hidden="true">?</span>' : '';
        const anchor = yo === 'o' && ANCHORED.has(k) ? `<span class="rc-where">${esc(ANCHOR[subj])}: <span class="rc-blank"></span></span>` : '';
        return `<div class="rc-sec"><p class="rc-sech">${icon}<b>${esc(lab)}</b> <span class="rc-secq">${esc(SECQ[k])}</span>${anchor}</p>` +
          (k2 ? `<div class="rc-draw" style="height:${perf > 1 ? 0.7 : 0.95}in"><span>Draw</span></div>` : '') + lines(nl, LH[b], r.pick(ST[k][yo])) + '</div>';
      }).join('');
      return `<div class="rc-form${secs.length >= 4 && !k2 ? ' rc-form2' : ''}"><p class="rc-cardh">${esc(x)}: <span class="rc-blank"></span></p><div class="rc-secs">${s}</div></div>`;
    };
    if (v.checks || (v.bank && yo === 'y')) html += `<h3 class="rc-h">${esc(PNAME[v.protocol].replace(/ \(.*\)$/, ''))}</h3>`;
    html += cols.map(form).join('');
    if (who === 'recv') html += `<h3 class="rc-h">My decision</h3>${ln('A suggestion I will use:', r.pick(['I will use', 'The most useful idea was']))}${ln('Why:', '')}${ln('A suggestion I will not use, and why:', '')}`;
    return { html };
  },
  cando(c) {
    const { v, r, b } = c, signed = v.lang === 'asl', lev = v.level;
    if (v.form === 'portfolio') {
      const d = DESC[lev];
      const desc = `<div class="rc-desc"><p><b>${LNAME[lev]}:</b> ${esc(d[0])}</p><ul>${d.slice(1).map(([s, t]) => `<li><b>${LNAME[lev]} ${s}:</b> ${esc(t)}</li>`).join('')}</ul></div>`;
      const pieces = [1, 2, 3].map(i => `<div class="rc-card"><p class="rc-cardh">Piece ${i}: <span class="rc-blank rc-wide"></span></p>` +
        `<p class="rc-circ">Circle the mode: <span>Interpersonal</span><span>Interpretive</span><span>Presentational</span></p>` +
        `<p class="rc-circ">Circle the rating: ${d.slice(1).map(([s]) => `<span>${LNAME[lev]} ${s}</span>`).join('')}</p>` + lines(2, LH[b], r.pick(['This piece shows', 'The evidence is', 'In this piece I', 'Look at the part where'])) + '</div>').join('');
      const growth = `<h3 class="rc-h">My growth</h3>${lines(4, LH[b], r.pick(['At the start of the year, I could', 'Comparing my first and last pieces,', 'The biggest change in my language is']))}` +
        `<h3 class="rc-h">My next step toward the next level</h3>${lines(2, LH[b], r.pick(['Next, I want to be able to', 'To reach the next level, I will', 'My goal is to']))}`;
      return { html: `<h3 class="rc-h">The ${LNAME[lev]} level (ACTFL)</h3>${desc}<h3 class="rc-h">Three pieces of my work</h3>${pieces}${growth}` };
    }
    const typed = list(v.cans, 12, 110).filter(x => x.length > 2);
    let groups;
    if (typed.length >= 2) groups = [['My can-do statements', typed.map(x => /^i can\b/i.test(x) ? cap(x) : 'I can ' + x.replace(/^(to\s+)/i, ''))]];
    else {
      const per = +v.count / 3;
      groups = ['ip', 'it', 'pr'].map(m => [`${MODES[m][0]}: ${MODES[m][signed ? 2 : 1]}`, CAN[lev].filter(s => s[0] === m).slice(0, per).map(s => signed && s[2] ? s[2] : s[1])]);
    }
    const scale = ['Not yet', 'With help', 'On my own'];
    let n = 0;
    const body = groups.map(([h, ss]) => `<tr class="rc-mode"><td colspan="5">${esc(h)}</td></tr>` + ss.map(s => `<tr><td class="rc-n">${++n}</td><td class="rc-left">${esc(s)}</td>${scale.map(() => `<td class="rc-tick">${box}</td>`).join('')}</tr>`).join('')).join('');
    const table = `<table class="rc-table rc-cando"><colgroup><col style="width:5%"><col style="width:59%"><col><col><col></colgroup><thead><tr><th>#</th><th>I can ...</th>${scale.map(s => `<th>${s}</th>`).join('')}</tr></thead><tbody>${body}</tbody></table>`;
    const evid = [1, 2, 3].map(() => `<div class="rc-ev3"><p class="rc-cardh">Statement # <span class="rc-blank rc-sm"></span></p>${lines(2, LH[b], r.pick(['For example, I', 'One time I', 'In class, I', 'Proof: I']))}</div>`).join('');
    const goals = [1, 2].map(i => ln(`Goal ${i}:`, r.pick(i === 1 ? ['I want to be able to', 'Next, I will learn to', 'By the next unit, I can'] : ['I will also', 'Another goal is to', 'I also want to']))).join('');
    return { html: table + `<h3 class="rc-h">Show it: an example for 3 statements</h3>${evid}<h3 class="rc-h">My 2 goals</h3>${goals}` };
  },
  skill(c) {
    const { v, r, b, who, yo } = c, k2 = b === 'k2', tries = +v.tries, mark = v.mark;
    const typed = list(v.cues, 6, 60).filter(x => x.length > 1);
    const preset = SKILL[v.skill] || SKILL.overhand;
    const cues = typed.length >= 2 ? typed : preset[2];
    const rowsC = cues.length ? cues : ['', '', '', ''];
    const cell = mark === 'smile' ? `<td class="rc-tick">${faceSvg('yes')}</td>` : mark === 'level' ? '<td class="rc-circle rc-sgn"><span>S</span><span>G</span><span>N</span></td>' : `<td class="rc-tick">${box}</td>`;
    const tryCols = Array.from({ length: tries }, (_, i) => tries === 1 ? (k2 ? 'Did it' : 'Seen') : k2 ? `${i + 1}` : `Try ${i + 1}`);
    const legend = mark === 'smile' ? r.pick(['Color the smile if you saw the cue.', 'Saw it? Color the smile.', 'Color a smile for each cue you see.'])
      : mark === 'level' ? 'Circle one each time: S = smooth, G = getting there, N = not yet.'
        : r.pick(['Check the box when you see the cue on that try.', 'Put a check in the box for each cue you see on each try.', 'A check means you clearly saw the cue on that try.']);
    const totals = tries > 1 && !k2;
    const rows = rowsC.map((cue, i) => `<tr><td class="rc-left"><span class="rc-num">${i + 1}</span> ${cue ? esc(cue) : '<span class="rc-blank rc-wide"></span>'}</td>${tryCols.map(() => cell).join('')}${totals ? '<td></td>' : ''}</tr>`).join('');
    const head = `<tr><th>Cue</th>${tryCols.map(x => `<th>${x}</th>`).join('')}${totals ? '<th>Total</th>' : ''}</tr>`;
    const wcue = tries >= 8 ? 32 : tries >= 5 ? 38 : 52;
    const table = `<table class="rc-table rc-skill"><colgroup><col style="width:${wcue}%"></colgroup><thead>${head}</thead><tbody>${rows}</tbody></table>`;
    const after = v.after;
    let tail = '';
    if (k2) tail = ln(who === 'self' ? 'I am best at:' : 'My partner is best at:', '') + (after !== 'none' ? ln(who === 'self' ? 'I will practice:' : 'Next, try:', '') : '');
    else {
      if (after === 'both' || after === 'cues') tail += ln('Cue seen most:', '') + ln('Cue to work on:', '') + (tries >= 5 ? ln('Pattern I noticed:', r.pick(['Over the tries,', 'Most misses came when', 'The cue that slipped was'])) : '');
      if (after === 'both' || after === 'praise') tail += ln('Praise:', r.pick(ST.glow[yo])) + ln('Tip:', r.pick(ST.grow[yo]));
    }
    const nameLine = !cues.length ? ln('Skill:', '') : '';
    return { html: nameLine + `<p class="rc-sub">${esc(legend)}</p>` + table + (tail ? `<div class="rc-tail">${tail}</div>` : '') };
  },
  faces(c) {
    const { v, r, who, perf, subj } = c;
    const typed = list(v.crit, 6, 50).filter(x => x.length > 1);
    const items = typed.length >= 2 ? typed : FACE[subj][who === 'self' ? 'self' : 'other'].slice(0, +v.count);
    const cols = who === 'self' ? [''] : Array.from({ length: perf }, (_, i) => whoLabel(who, perf, i) + (who === 'peer' && perf === 1 ? '' : ''));
    const mk = v.mark;
    const marks = mk === 'stars' ? `<span class="rc-icons">${starSvg()}${starSvg()}${starSvg()}</span>`
      : mk === 'yesno' ? `<span class="rc-yn"><span>${box} Yes</span><span>${box} Not yet</span></span>`
        : `<span class="rc-icons">${['yes', 'mid', 'no'].map(k => faceSvg(k)).join('')}</span>`;
    const legend = mk === 'stars' ? r.pick(['Color 1, 2 or 3 stars.', 'Color the stars: 3 is the most.', 'More stars means more yes.'])
      : mk === 'yesno' ? r.pick(['Check yes or not yet.', 'Mark one box on each line.', 'Pick yes or not yet.']) : r.pick(['Circle one face on each line.', 'Circle the face that fits.', 'Circle a face for each one.']);
    const head = who === 'self' ? '' : `<tr><th></th>${cols.map(x => `<th>${esc(x === 'Partner' ? 'My friend' : x.replace('Classmate', 'Friend'))}</th>`).join('')}</tr>`;
    const reason = v.reason ? `<tr class="rc-evrow"><td colspan="${cols.length + 1}">${ln('Why?', r.pick(['Because', 'I think so because', 'I saw']))}</td></tr>` : '';
    const rows = items.map(it => `<tr><td class="rc-left rc-item">${esc(it)}</td>${cols.map(() => `<td>${marks}</td>`).join('')}</tr>${reason}`).join('');
    const dh = Math.max(1.1, (v.reason ? 1.4 : 2.0) - Math.max(0, items.length - 4) * 0.3);
    const draw = v.draw !== 'none' ? `<div class="rc-drawbox" style="height:${dh.toFixed(2)}in"><span>${esc(r.pick(DRAWQ[v.draw]))}</span></div>` : '';
    const bank = v.bank ? wordBank(subj, true) : '';
    return { html: `<p class="rc-sub rc-big">${esc(legend)}</p><table class="rc-table rc-faces"><colgroup><col style="width:${cols.length > 1 ? 40 : 55}%"></colgroup><tbody>${head}${rows}</tbody></table>${bank}${draw}` };
  },
  build(c) {
    const { v, r, b, crit, subj, yo } = c, blank = v.blank, L = +v.levels;
    const crows = blank ? Array.from({ length: +v.count }, () => ['', '']) : crit;
    const bankList = blank ? `<p class="rc-bank"><b>Choose from these, or write your own:</b> ${CRIT[subj][yo].map(x => `<span>${esc(x[0])}</span>`).join('')}</p>` : '';
    const cc = cr => cr[0] ? critCell(cr) : '<span class="rc-blank rc-full"></span>';
    if (v.bform === 'lookfor') {
      const h = b === '35' ? 1.25 : 1.1;
      return { html: bankList + `<table class="rc-table rc-build"><colgroup><col style="width:24%"><col style="width:38%"><col style="width:38%"></colgroup><thead><tr><th>Criterion</th><th>What strong work looks like<span class="rc-thq">Write this before you watch</span></th><th>Notes while watching<span class="rc-thq">What you actually see</span></th></tr></thead><tbody>${crows.map(cr => `<tr style="height:${h}in"><td class="rc-left">${cc(cr)}</td><td></td><td></td></tr>`).join('')}</tbody></table>` +
        `<p class="rc-cardh">${esc(r.pick(['Overall judgment', 'Did it meet the criteria?', 'My overall view']))}</p>${lines(2, LH[b], r.pick(['Overall, the work', 'The strongest criterion was', 'Using my notes, I think']))}` };
    }
    const names = levelNames(v, b, L), h = crows.length > 4 ? 1.05 : 1.25, num = names[0] === '1';
    return { html: bankList + `<p class="rc-sub">${esc(r.pick(['Write the top level first, then work down one step at a time.', 'Start with the strongest level. What changes as you go down?', 'Use words someone could see or hear, not just "good" or "bad."']))}</p>` +
      `<table class="rc-table rc-build"><colgroup><col style="width:${L === 3 ? 25 : 20}%">${names.map(() => '<col>').join('')}</colgroup><thead><tr><th>Criterion</th>${names.slice().reverse().map((n, i) => `<th>${esc(n)}${num ? '' : ` <span class="rc-pt">${L - i}</span>`}</th>`).join('')}</tr></thead><tbody>${crows.map(cr => `<tr style="height:${h}in"><td class="rc-left">${cc(cr)}</td>${names.map(() => '<td></td>').join('')}</tr>`).join('')}</tbody></table>` };
  },
};

/* ---------- titles, directions, notes ---------- */
function titleOf(kind, v, who, perf, subj) {
  const S = SNAME[subj];
  if (kind === 'rubric') return perf > 1 ? `${S} Panel Scoring Rubric` : who === 'self' ? `${S} Self-Assessment Rubric` : who === 'group' ? `${S} Performance Critique Rubric` : `${S} Peer Rubric`;
  if (kind === 'single') return who === 'self' ? `${S} Single-Point Self-Check` : `${S} Single-Point Peer Review`;
  if (kind === 'feedback') return who === 'recv' ? 'Feedback on My Work' : PTITLE[v.protocol];
  if (kind === 'cando') return v.form === 'portfolio' ? `${LNAME[v.level]} Portfolio Reflection` : `${LNAME[v.level]} Can-Do Self-Check`;
  if (kind === 'skill') return v.skill === 'custom' ? (who === 'self' ? 'Skill Self-Check' : 'Partner Skill Check') : `${SKILL[v.skill][1].replace(/ \(.*\)$/, '')}: ${who === 'self' ? 'Self-Check' : 'Partner Cue Check'}`;
  if (kind === 'faces') return who === 'self' ? 'How Did I Do?' : who === 'group' ? 'How Did the Group Do?' : 'Watching a Friend';
  return v.bform === 'lookfor' ? 'Watching With Criteria' : 'Build a Rubric';
}
function directionsOf(kind, v, r, who, perf, b) {
  const watch = { self: 'Think about your own work.', peer: perf > 1 ? 'Watch each classmate carefully.' : 'Watch your partner carefully.',
    group: perf > 1 ? 'Watch each group carefully.' : 'Watch the group carefully.', recv: 'Share your work and ask classmates to fill in a box each.' }[who] || '';
  if (kind === 'rubric') return perf > 1 ? `${watch} ${r.pick(['Write a score for each criterion in each column, then write a strength and a next step for each.', 'Score every criterion for each performer, then add one strength and one next step.'])}`
    : `${watch} ${r.pick(['For each criterion, circle the box that matches what you saw.', 'Circle one box in each row: the level that fits best.', 'Read each row, then circle the level that matches.'])}${v.evidence ? ' Then write your evidence: what you saw or heard that shows it.' : ''}`;
  if (kind === 'single') return `${watch} ${r.pick(['Read each criterion in the middle. Write evidence that it is there on the right, and what would make it stronger on the left.', 'For each criterion, write what is working on the right and what to work on on the left.'])}`;
  if (kind === 'feedback') return (b === 'k2' ? r.pick(['Watch. Then draw and write.', 'Look and listen. Then fill in each box.']) : `${watch} ${r.pick(['Fill in each box with specific, kind feedback.', 'Use the starters if they help, and point to a specific moment.', 'Be specific: name the moment you mean.'])}`) + (v.checks ? ' Mark the checklist first.' : '');
  if (kind === 'cando') return v.form === 'portfolio' ? r.pick(['Choose 3 pieces of your work from this year. Rate each one against the level, give evidence, and explain your growth.', 'Pick 3 pieces of work that show your best language. Rate each against the descriptions, then tell how you have grown.'])
    : r.pick(['Read each statement. Check how well you can do it now. Then give an example for 3 statements and set 2 goals.', 'Rate yourself honestly on each statement. Give an example for 3 of them and set 2 goals.']);
  if (kind === 'skill') return b === 'k2' ? (who === 'self' ? r.pick(['Try the skill. Mark each cue you did.', 'Try it. Then mark each cue.']) : r.pick(['Watch your partner. Mark each cue you see.', 'Watch your partner try. Mark each cue.']))
    : `${who === 'self' ? r.pick(['Try the skill and mark each cue you used.', 'Do the skill, then mark the cues you used on each try.']) : r.pick(['Watch your partner try the skill and mark each cue you see on every try.', 'Watch each try closely. Mark the cues you see.'])}${v.after === 'none' ? '' : ' Then fill in the lines below.'}`;
  if (kind === 'faces') return who === 'self' ? r.pick(['Think about what you did. Mark each line.', 'How did you do? Mark each line.']) : r.pick(['Watch. Then mark each line.', 'Look and listen. Then mark each line.']);
  return v.bform === 'lookfor' ? r.pick(['Before you watch, write what strong work looks like for each criterion. While you watch, take notes in the last column.', 'First describe the target for each criterion. Then watch and take notes.'])
    : r.pick(['Write what the work looks like at each level for every criterion.', 'Describe each level so that anyone could use this rubric to score a performance.']);
}
const MISTAKES = {
  rubric: 'Ratings with no evidence, or every box circled at the top. Ask for one moment per criterion; a rating without evidence does not count yet.',
  single: 'Writing only on the glow side. Every row should have something on at least one side, and the grow side should name a next step, not just a weakness.',
  feedback: 'Vague comments ("good job," "make it better"). Have students name a moment and a choice: what, where and why it worked or could be stronger.',
  cando: 'Checking "On my own" for everything. Ask for an example before a statement counts as on my own.',
  skill: 'Watching the result (did it go in?) instead of the body (did the cue happen?). Model one try and mark it together before partners start.',
  faces: 'Circling the happy face every time. Read each line aloud and talk about what "not yet" looks like first.',
  build: 'Levels that only swap one word ("good, very good, excellent"). Each level should describe something you can see or hear.',
};
const USE = {
  rubric: 'Use it for a performance, a draft showing or a recording. With 2 or 3 performers it becomes a panel score sheet.',
  single: 'A single-point rubric lists only the target, so feedback goes to what is above or below it. It suits drafts and work in progress.',
  feedback: 'Model the protocol once with a sample before students use it with each other.',
  cando: 'The statements follow the three modes of communication. Have students keep the sheet and rate again later in the year.',
  skill: 'Teach and demonstrate the cues first. Partners can watch one cue at a time if the skill is new.',
  faces: 'Read each line aloud. Students can point instead of circling if they need to.',
  build: 'Build criteria with the class, then use the finished chart to score a performance.',
};
const SAMPLE = {
  dance: ['Good dancing.', 'At count 5 of the second phrase, your arms reached all the way out, so the shape read clearly from the back.', 'Try holding the end shape for a full 4 counts; it ended before the music did.'],
  music: ['It sounded nice.', 'In measures 9 to 12 the crescendo grew evenly, so the phrase had a clear peak.', 'Watch the cutoff in measure 16: two voices held on after the conductor stopped.'],
  theater: ['Good acting.', 'When you said "I can\'t go back," you stepped away and dropped your voice, so we felt the fear.', 'Turn out on your exit line; we lost your face to the back wall.'],
  visual: ['I like it.', 'The bright orange in the top corner pulls my eye straight to the bird.', 'The bottom third is empty; a shadow or ground line could connect it to the rest.'],
  media: ['Cool video.', 'At 0:42 the cut on the door slam made the jump scare land.', 'The music at 1:10 covers the voice; lower it so we can hear the line.'],
  pe: ['Good throw.', 'On tries 3 and 4 you stepped with the opposite foot, and the ball went straight to the target.', 'Turn your side to the target before you throw; on tries 1 and 5 you faced it.'],
  lang: ['Good job.', 'You used three past-tense verbs correctly in the second sentence of your story.', 'Check agreement in your last sentence: the adjective needs to match the noun.'],
  general: ['You did good.', 'When the group got stuck, you asked each person for one idea, and that got us moving.', 'Look up at the audience at the end of each slide, not only at the screen.'],
};
function teacherHtml(kind, subj, v) {
  if (kind === 'cando') return `<h3>About the statements</h3><p>The built-in statements paraphrase the kinds of tasks in the NCSSFL-ACTFL Can-Do Statements for the ${LNAME[v.level]} range, grouped by the three modes of communication. They are not the official list; type your program's own statements, separated by semicolons, to use those instead.</p>` +
    (v.form === 'portfolio' ? '<p>The level descriptions on the sheet paraphrase the ACTFL Proficiency Guidelines. A rating of one piece of work is a sample, not an official proficiency rating.</p>' : '');
  if (kind === 'skill') return `<h3>Before partners start</h3><p>Demonstrate the skill and say each cue as you do it. Then do one try in front of the class and mark it together. Remind observers to watch the body, not where the ball or object went.</p>`;
  const s = SAMPLE[subj];
  return `<h3>Model: vague and specific feedback</h3><table class="ws-table rc-model"><tbody><tr><th>Vague</th><td>${esc(s[0])}</td></tr><tr><th>Specific strength</th><td>${esc(s[1])}</td></tr><tr><th>Specific next step</th><td>${esc(s[2])}</td></tr></tbody></table><p>Share the model before students start. A useful comment names a moment, says what happened, and (for a next step) gives something to try.</p>`;
}

const CSS = `
.rc { margin-top: 2px; }
.rc-tip { margin: 0 0 4px; font-size: 13px; }
.rc-sub { margin: 2px 0 4px; font-size: 13px; color: #333; }
.rc-big { font-size: 16px; }
.rc-h { font: 700 13px/1.3 var(--sans); text-transform: uppercase; letter-spacing: .06em; margin: .12in 0 .03in; }
.rc-table { width: 100%; border-collapse: collapse; table-layout: fixed; margin: .04in 0 .06in; }
.rc-table th { border: 1.5px solid #222; padding: 4px 5px; font: 700 12.5px/1.2 var(--sans); background: #eee; -webkit-print-color-adjust: exact; print-color-adjust: exact; text-align: center; vertical-align: bottom; }
.rc-table td { border: 1.5px solid #222; padding: 4px 6px; vertical-align: middle; text-align: center; height: .42in; }
.rc-table td.rc-left { text-align: left; }
.rc-thq { display: block; font: 400 11px/1.2 var(--sans); color: #444; margin-top: 2px; }
.rc-crit { display: block; font-weight: 700; font-size: 13.5px; line-height: 1.25; overflow-wrap: anywhere; }
.rc-look { display: block; font-size: 11.5px; line-height: 1.25; color: #444; font-style: italic; overflow-wrap: anywhere; }
.rc-q { font-size: 11.5px; color: #555; line-height: 1.2; }
.rc-pt { display: inline-block; min-width: 1.4em; border: 1.5px solid #222; border-radius: 50%; font-size: 11px; line-height: 1.4em; margin-left: 3px; background: #fff; }
.rc-table tr.rc-evrow td { height: auto; padding: 0 6px 5px; border-top: 0; }
.rc-ev tbody tr:not(.rc-evrow) td { border-bottom: 1px dashed #888; }
.rc-ln { display: flex; align-items: flex-end; gap: 6px; margin: 6px 0 0; font-size: 13px; text-align: left; }
.rc-ln b { white-space: nowrap; }
.rc-ln > span { flex: 1; border-bottom: 1px solid #555; min-height: 1.35em; }
.rc-ln > span i { font-size: 12px; color: #555; }
.rc-lines span { display: block; height: var(--lh); border-bottom: 1px solid #888; position: relative; }
.rc-lines span i { position: absolute; left: 0; bottom: 2px; font-size: 12.5px; color: #555; white-space: nowrap; }
.rc-blank { display: inline-block; min-width: 1.2in; border-bottom: 1.5px solid #222; height: 1em; vertical-align: -2px; }
.rc-blank.rc-wide { min-width: 2.2in; }
.rc-blank.rc-full { display: block; min-width: 0; width: 100%; }
.rc-blank.rc-sm { min-width: .5in; }
.rc-totalp { text-align: right; font-size: 14px; margin: 4px 0; }
.rc-key { font-size: 12.5px; margin: 2px 0 4px; }
.rc-key span { margin-right: 10px; white-space: nowrap; display: inline-block; }
.rc-panel td.rc-score { height: .5in; }
.rc-panel tr.rc-names td, .rc-panel tr.rc-total td { height: .34in; }
.rc-card, .rc-ev3, .rc-form { border: 1.5px solid #222; border-radius: 8px; padding: .04in .1in .08in; margin: .08in 0; break-inside: avoid; }
.rc-cardh { margin: .04in 0 2px; font: 700 13px/1.4 var(--sans); }
.rc-sec { margin: 4px 0 6px; break-inside: avoid; }
.rc-sech { margin: 0; font-size: 13.5px; line-height: 1.35; display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.rc-secq { font-size: 12px; color: #444; font-style: italic; }
.rc-where { margin-left: auto; font-size: 11.5px; color: #333; }
.rc-where .rc-blank { min-width: .9in; }
.rc-form2 .rc-secs { display: grid; grid-template-columns: 1fr 1fr; gap: 0 .18in; }
.rc-form2 .rc-where { margin-left: 0; }
.rc-ico { display: inline-block; width: .34in; height: .34in; vertical-align: middle; }
.rc-icons { white-space: nowrap; }
.rc-sech .rc-ico { width: .3in; height: .3in; }
.rc-wish { display: inline-grid; place-items: center; width: .28in; height: .28in; border: 2px solid #222; border-radius: 50%; font: 700 14px var(--sans); }
.rc-draw, .rc-drawbox { border: 1px dashed #888; border-radius: 6px; margin: 4px 0 2px; position: relative; }
.rc-draw span, .rc-drawbox span { position: absolute; left: 8px; top: 4px; font-size: 11px; color: #777; }
.rc-drawbox { margin-top: .12in; }
.rc-drawbox span { font-size: 15px; color: #333; }
.rc-bank { font-size: 13px; margin: 4px 0 6px; line-height: 1.8; }
.rc-bank span { display: inline-block; border: 1.2px solid #555; border-radius: 12px; padding: 0 8px; margin: 0 4px 0 0; line-height: 1.5; }
.rc-box { display: inline-block; width: .2in; height: .2in; border: 1.5px solid #222; border-radius: 3px; vertical-align: middle; background: #fff; }
.rc-circle span { display: inline-block; margin: 0 4px; font-size: 12px; }
.rc-sgn span { font: 700 13px var(--sans); margin: 0 4px; }
.rc-num { display: inline-grid; place-items: center; width: 1.4em; height: 1.4em; border: 1.5px solid #222; border-radius: 50%; font: 700 11px var(--sans); margin-right: 4px; }
.rc-skill td { height: .4in; }
.rc-skill td.rc-left { font-size: 13px; line-height: 1.25; }
.rc-skill .rc-ico { width: .3in; height: .3in; }
.rc-tail { margin-top: .06in; }
.rc-cando td { height: .34in; }
.rc-cando td.rc-left { font-size: 12.5px; line-height: 1.25; }
.rc-cando tr.rc-mode td { background: #f2f2f2; font: 700 12px/1.2 var(--sans); text-align: left; height: auto; padding: 3px 6px; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.rc-n { font-size: 12px; }
.rc-desc { border: 1.5px solid #222; border-radius: 8px; padding: .04in .12in; font-size: 12.5px; }
.rc-desc p { margin: 2px 0; }
.rc-desc ul { margin: 2px 0 4px; padding-left: 1.1em; }
.rc-circ { margin: 3px 0; font-size: 12.5px; }
.rc-circ span { display: inline-block; margin: 0 6px; }
.rc-single td { vertical-align: top; }
.rc-single td.rc-mid { background: #f6f6f6; -webkit-print-color-adjust: exact; print-color-adjust: exact; vertical-align: middle; }
.rc-build td { vertical-align: top; }
.rc-faces td { height: .62in; }
.rc-faces .rc-item { font-size: 17px; line-height: 1.25; }
.rc-faces .rc-ico { width: .44in; height: .44in; margin: 0 3px; }
.rc-faces th { font-size: 14px; }
.rc-yn > span { display: inline-block; margin: 0 6px; font-size: 15px; }
.rc-yn .rc-box { width: .26in; height: .26in; }
.rc-k2 .rc-lines span i { font-size: 15px; }
.rc-k2 .rc-sech { font-size: 16px; }
.rc-k2 .rc-secq { font-size: 13.5px; }
.rc-k2 .rc-bank { font-size: 15px; }
.rc-k2 .rc-ln { font-size: 16px; }
.rc-k2 .rc-skill td.rc-left { font-size: 15px; }
.rc-model th { text-align: left; white-space: nowrap; width: 1%; vertical-align: top; }
.rc-model td { text-align: left; height: auto; }
`;

const WHO = { rubric: [['peer', 'A partner or classmates'], ['group', 'A group, ensemble or show'], ['self', 'My own work (self-assessment)']],
  single: [['peer', 'A partner'], ['self', 'My own work (self-assessment)']],
  feedback: [['peer', 'A partner or classmates'], ['group', 'A group, ensemble or show'], ['recv', 'My work (classmates fill it in for me)']],
  faces: [['self', 'Myself'], ['peer', 'A friend'], ['group', 'A group']],
  skill: [['peer', 'A partner'], ['self', 'Myself']] };
const COUNT = { cando: [['12', '12 statements (4 per mode)'], ['9', '9 statements (3 per mode)'], ['6', '6 statements (2 per mode)']],
  faces: [['4', '4 lines'], ['3', '3 lines'], ['5', '5 lines'], ['6', '6 lines']] };
const MULTI = ['rubric', 'feedback', 'faces'];

Gen.add('rubric-checklist', {
  title: 'Rubrics and Checklists', type: 'Rubric', noKey: true, css: CSS,
  fields: [
    { id: 'kind', label: 'Kind', type: 'select', options: KINDS, def: 'rubric' },
    { id: 'grade', label: 'Grade', type: 'select', options: v => GALL.filter(g => gnum(g[0]) >= GFROM[v.kind] && (v.kind !== 'faces' || gnum(g[0]) <= 2)), def: '4' },
    { id: 'subject', label: 'Subject (sets the built-in criteria, word bank and sample feedback)', type: 'select', options: SUBJ, def: 'dance', show: v => v.kind !== 'cando' && v.kind !== 'skill' },
    { id: 'topic', label: 'Title (optional), for example Spring Concert Self-Check', type: 'text', def: '' },
    { id: 'who', label: 'Who is assessed', type: 'select', options: v => WHO[v.kind] || [['peer', 'A partner']], def: 'peer', show: v => !!WHO[v.kind] },
    { id: 'perf', label: 'How many on one sheet', type: 'select', options: v => [['1', '1'], ['2', '2'], ...(bandOf(v.grade) === 'k2' ? [] : [['3', '3']])], def: '1',
      show: v => MULTI.includes(v.kind) && v.who !== 'self' },
    { id: 'protocol', label: 'Feedback protocol', type: 'select', options: PROTOS, def: 'glow1', show: v => v.kind === 'feedback' },
    { id: 'crit', label: 'Your own criteria (optional), comma or semicolon separated, a look-for after a colon: Timing: on the counts; Focus; Energy', type: 'text', def: '',
      show: v => ['rubric', 'single', 'feedback', 'build', 'faces'].includes(v.kind) },
    { id: 'count', label: 'How many built-in criteria (or statements)', type: 'select', options: v => COUNT[v.kind] || [['4', '4'], ['3', '3'], ['5', '5'], ['6', '6']], def: '4',
      show: v => v.kind !== 'skill' && !(v.kind === 'cando' && v.form === 'portfolio') },
    { id: 'levels', label: 'Levels', type: 'select', options: [['4', '4 levels'], ['3', '3 levels']], def: '4', show: v => v.kind === 'rubric' || (v.kind === 'build' && v.bform !== 'lookfor') },
    { id: 'scale', label: 'Level names', type: 'select', options: SCALES, def: 'auto', show: v => v.kind === 'rubric' || (v.kind === 'build' && v.bform !== 'lookfor') },
    { id: 'points', label: 'Number the levels and add a total score', type: 'check', def: true, show: v => v.kind === 'rubric' },
    { id: 'evidence', label: 'Evidence line under each criterion', type: 'check', def: true, show: v => v.kind === 'rubric' && !(MULTI.includes(v.kind) && v.who !== 'self' && +v.perf > 1) },
    { id: 'checks', label: 'Criteria checklist (yes / not yet) above the comments', type: 'check', def: true, show: v => v.kind === 'feedback' },
    { id: 'bank', label: 'Word bank (grades K-5)', type: 'check', def: true, show: v => (v.kind === 'feedback' && gnum(v.grade) <= 5) || v.kind === 'faces' },
    { id: 'after', label: 'After the grid', type: 'select', options: v => v.kind === 'skill' ? SKAFTER : AFTER, def: 'next', show: v => ['rubric', 'single', 'skill'].includes(v.kind) },
    { id: 'bform', label: 'Frame', type: 'select', options: [['levels', 'Describe each level'], ['lookfor', 'What strong looks like, then notes while watching']], def: 'levels', show: v => v.kind === 'build' },
    { id: 'blank', label: 'Students choose and write the criteria (prints a list to choose from)', type: 'check', def: false, show: v => v.kind === 'build' },
    { id: 'level', label: 'Proficiency level', type: 'select', options: LEVELS, def: 'novice', show: v => v.kind === 'cando' },
    { id: 'lang', label: 'Language', type: 'select', options: [['spoken', 'A spoken language (Spanish, French and others)'], ['asl', 'American Sign Language']], def: 'spoken', show: v => v.kind === 'cando' },
    { id: 'form', label: 'Sheet', type: 'select', options: [['self', 'Can-do self-check, with evidence and 2 goals'], ['portfolio', 'Portfolio reflection: rate 3 pieces of work against the level']], def: 'self', show: v => v.kind === 'cando' },
    { id: 'cans', label: 'Your own can-do statements (optional), separated by semicolons: I can order food; I can ask for directions', type: 'text', def: '', show: v => v.kind === 'cando' && v.form !== 'portfolio' },
    { id: 'skill', label: 'Skill', type: 'select', options: SKILLS.map(s => [s[0], s[1]]), def: 'overhand', show: v => v.kind === 'skill' },
    { id: 'cues', label: 'Your own cues (optional), comma separated: eye line, stillness, breath', type: 'text', def: '', show: v => v.kind === 'skill' },
    { id: 'tries', label: 'Tries to watch', type: 'select', options: v => bandOf(v.grade) === 'k2' ? [['3', '3'], ['2', '2'], ['1', '1'], ['5', '5']] : [['5', '5'], ['3', '3'], ['6', '6'], ['8', '8'], ['10', '10'], ['1', '1']], def: '5', show: v => v.kind === 'skill' },
    { id: 'mark', label: 'Marks', type: 'select', options: v => v.kind === 'faces' ? [['faces', 'Faces to circle'], ['stars', 'Stars to color'], ['yesno', 'Yes or not yet']]
      : bandOf(v.grade) === 'k2' ? [['smile', 'Smiles to color'], ['check', 'Check boxes']] : [['check', 'Check boxes (cue seen)'], ['level', 'Smooth, getting there, not yet']], def: 'smile', show: v => v.kind === 'skill' || v.kind === 'faces' },
    { id: 'reason', label: 'A "Why?" line under each', type: 'check', def: false, show: v => v.kind === 'faces' },
    { id: 'draw', label: 'Drawing box', type: 'select', options: DRAWS, def: 'like', show: v => v.kind === 'faces' },
  ],
  make(v, r) {
    const kind = v.kind, b = bandOf(v.grade), yo = b === 'k2' || b === '35' ? 'y' : 'o', subj = SNAME[v.subject] ? v.subject : 'dance';
    const who = WHO[kind] ? v.who : 'self';
    const perf = MULTI.includes(kind) && who !== 'self' ? +v.perf || 1 : 1;
    const typed = critList(v.crit);
    const crit = typed.length ? typed : CRIT[subj][yo].slice(0, +v.count || 4);
    const topic = String(v.topic || '').trim(), longTopic = topic.length > 55;
    const out = BUILD[kind]({ v, r, b, yo, crit, who, perf, subj });
    const tip = (longTopic ? `<p class="rc-tip"><b>Title:</b> ${esc(topic)}</p>` : '') + (kind === 'cando' ? '' : `<p class="rc-tip"><b>Tip:</b> ${esc(r.pick(TIPS[yo]))}</p>`);
    const parts = [['', `<div class="rc rc-${b}">${tip}${out.html}</div>`]];
    if ((kind === 'rubric' || kind === 'single') && CLOSE[v.after]) {
      const set = CLOSE[v.after][who === 'self' ? 'self' : 'other'];
      parts.push([who === 'self' ? 'Looking ahead' : 'Wrap-up', `<div class="rc rc-${b}">${set.map(([lab, sts]) => `<p class="rc-cardh">${esc(lab)}${perf > 1 ? ' (choose one performer)' : ''}</p>${lines(2, LH[b], r.pick(sts))}`).join('')}</div>`]);
    }
    const eyebrow = { rubric: 'Rubric', single: 'Single-point rubric', feedback: 'Feedback · ' + PNAME[v.protocol], cando: 'Can-do checklist · ACTFL ' + LNAME[v.level],
      skill: 'Skill-cue checklist', faces: who === 'self' ? 'Self-check' : 'Peer check', build: 'Build a rubric' }[kind];
    const ican = { rubric: 'I can use criteria to judge work and back up each rating with evidence.', single: 'I can compare work to a clear target and say what is working and what is next.',
      feedback: yo === 'y' ? 'I can give kind, specific feedback.' : 'I can give kind, specific, helpful feedback tied to a moment in the work.',
      cando: v.form === 'portfolio' ? 'I can show my growth in the language with evidence from my work.' : 'I can rate what I can do in the language and set goals.',
      skill: b === 'k2' ? 'I can watch for the cues of a skill.' : 'I can watch a skill closely and spot which cues are there.', faces: 'I can think about how it went.',
      build: 'I can describe what strong work looks like.' }[kind];
    return {
      title: (!longTopic && topic) || titleOf(kind, v, who, perf, subj), eyebrow, level: BANDNAME[b],
      ican, directions: directionsOf(kind, v, r, who, perf, b),
      minutes: { rubric: 20, single: 20, feedback: 15, cando: 25, skill: 15, faces: 10, build: 25 }[kind],
      materials: 'pencil' + (b === 'k2' ? ', crayons' : '') + (kind === 'skill' ? ', the equipment for the skill' : ''),
      parts, items: [],
      mistakes: MISTAKES[kind],
      notes: `${USE[kind]} The starters, tips and some wording change with each New sheet; the criteria and layout stay the same.`,
      teacher: teacherHtml(kind, subj, v),
    };
  },
  // nothing to answer, so check the frame against the settings with an independent re-parse of the typed lists
  verify(s, v) {
    const bad = [], html = s.parts.map(p => p[1]).join('');
    if (/<of>|"animals"/.test(html)) bad.push('typed text printed without escaping');
    const kind = v.kind, band = bandOf(v.grade);
    const split = t => { t = String(t || '').trim(); return t ? t.split(/[;\n]/.test(t) ? /[;\n]/ : /,/).map(x => x.trim()).filter(Boolean) : []; };
    const pieces = split(v.crit);
    const critShown = (['rubric', 'single'].includes(kind)) || (kind === 'build' && !v.blank) || (kind === 'feedback' && v.checks);
    if (critShown) {
      const n = (html.match(/class="rc-crit"/g) || []).length;
      const want = pieces.length >= 2 ? Math.min(8, pieces.length) : +v.count;
      if (n !== want) bad.push(`expected ${want} criteria, found ${n}`);
      if (pieces.length >= 2) for (const p of pieces.slice(0, 8)) { const name = p.split(':')[0].trim(); if (name.length <= 36 && !html.includes(esc(name))) bad.push(`criterion missing: ${name}`); }
    }
    if (kind === 'rubric' && (v.who === 'self' || +v.perf === 1)) {
      const table = html.slice(html.indexOf('<thead>'), html.indexOf('</thead>'));
      const heads = (table.match(/<th>/g) || []).length - 1;
      if (heads !== +v.levels) bad.push(`expected ${v.levels} level columns, found ${heads}`);
    }
    if (kind === 'cando' && v.form !== 'portfolio') {
      const rows = (html.match(/class="rc-n"/g) || []).length;
      const typed = split(v.cans).filter(x => x.length > 2);
      const want = typed.length >= 2 ? Math.min(12, typed.length) : +v.count;
      if (rows !== want) bad.push(`expected ${want} statements, found ${rows}`);
    }
    if (kind === 'skill') {
      const rows = (html.match(/class="rc-num"/g) || []).length;
      const typed = split(v.cues).filter(x => x.length > 1);
      const want = typed.length >= 2 ? Math.min(6, typed.length) : (SKILL[v.skill][2].length || 4);
      if (rows !== want) bad.push(`expected ${want} cues, found ${rows}`);
    }
    if (kind === 'faces' && band !== 'k2') bad.push('faces sheet outside K-2');
    return bad;
  },
});
})();
