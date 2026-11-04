// Project Frames, grades K-12. A layout generator: no computed answers (noKey). Pick a kind of project page and a grade
// band; the band sets the layout, the writing space and the wording, and the topic goes in the title. Prompts and tips
// come from banks, so New sheet gives fresh wording of the same frame. The teacher page holds a filled-in model.
// Kinds:
//   research planner (big question, smaller questions, keywords and a search string, where to look, 1 to 4 source note
//     boxes, a source list with a citation pattern, a step plan with due dates)            CCSS W.K-12.7, W.3-12.8
//   presentation planner (informative talk, opinion speech, pitch or book talk; opening, points with evidence, visuals and
//     transitions, closing, a timing budget worked out for a 1 to 5 minute talk, a practice check)   CCSS SL.K-12.4, SL.2-12.5
//   slide-by-slide planner (3 to 8 slides with a sketch, words on the slide and speaker notes; typed slide titles)
//   storyboard (3 to 12 panels with shot, action and sound lines or the teacher's own lines; shot type key)  NCAS MA:Cr2, MA:Cr3
//   shot list and timing sheet (4 to 16 shots, seconds or frames at 12 or 24 per second, a total row; typed columns)
//   script page (4 to 16 lines with character, line and a stage direction, sound cue or action column) CCSS W.3-8.3, NCAS TH:Cr1
//   dance count sheet (8 to 32 counts in eights, rows for move, level, direction or the teacher's own rows, such as
//     Dancer A to D for a canon; optional & counts and a class symbol key)                   NCAS DA:Cr2, DA:Pr4, DA:Pr5
//   stage plan (a drawn stage with the 9 areas USR to DSL and the audience, with a moves table for 4 to 8 moves, or
//     4 or 6 small stages for formations and transitions)                                    NCAS TH:Cr2, TH:Pr5, DA:Pr5
//   art project planner (idea, a bank of elements, colors, principles, values or poster parts to choose from, swatches,
//     2 to 6 thumbnail sketches, choose the strongest, materials and steps, reflection)       NCAS VA:Cr1.2, VA:Cr2.1, VA:Cr3
//   decision matrix (2 to 6 options against typed criteria, 1 to 5 scores, optional weights, total and rank)
//     NGSS 3-5-ETS1-2, MS-ETS1-2, HS-ETS1-3; CSTA 2-IC-20; Jump$tart Employment and Income
//   interview planner (who and why, 3 to 10 questions in typed groups, follow-ups, note space, thank-you)  CCSS SL.K-12.1, W.K-12.8
//   debate prep (resolution, side, 2 or 3 arguments with evidence, counterarguments and rebuttals, speaker roles, speaking
//     frames in English, Spanish or French)                                                  CCSS SL.6-12.1, SL.6-12.3, ACTFL Presentational
//   coaching session plan (learner, skill, learning stage, 3 cues, drill sketch and setup, practice type, feedback words,
//     a success check)                                                                         SHAPE America Standards 1, 2 and 4
(() => {
const { esc } = Gen.h;

const BANDS = [['k2', 'Grades K-2'], ['35', 'Grades 3-5'], ['68', 'Grades 6-8'], ['912', 'Grades 9-12']];
const KINDS = [['research', 'Research planner'], ['present', 'Presentation or speech planner'], ['slides', 'Slide-by-slide planner'],
  ['storyboard', 'Storyboard'], ['shotlist', 'Shot list and timing sheet'], ['script', 'Script page'], ['counts', 'Dance count sheet'],
  ['stage', 'Stage plan and blocking'], ['art', 'Art project planner'], ['matrix', 'Decision matrix'], ['interview', 'Interview planner'],
  ['debate', 'Debate prep'], ['coach', 'Coaching session plan']];
const KNAME = Object.fromEntries(KINDS);
const LH = { k2: 0.44, 35: 0.34, 68: 0.3, 912: 0.28 };   // ruled line spacing in inches
const young = b => b === 'k2' || b === '35';

// how many: per kind, K-2 options and the options for grades 3-12, with the noun for the label
const COUNT = {
  research: { k2: ['1', '2'], d: ['2', '3', '4'], n: 'source' },
  present: { k2: ['2', '3'], d: ['2', '3', '4', '5'], n: 'main point' },
  slides: { k2: ['3', '4', '6'], d: ['3', '4', '6', '8'], n: 'slide' },
  storyboard: { k2: ['3', '4', '6'], d: ['3', '4', '6', '8', '10', '12'], n: 'panel' },
  shotlist: { k2: ['4', '6'], d: ['4', '6', '8', '10', '12', '16'], n: 'shot' },
  script: { k2: ['4', '6'], d: ['4', '6', '8', '10', '12', '16'], n: 'line' },
  counts: { k2: ['8', '16'], d: ['8', '16', '24', '32'], n: 'count' },
  stage: { k2: ['4', 'f4'], d: ['4', '5', '6', '8', 'f4', 'f6'], n: 'move' },
  art: { k2: ['2', '3'], d: ['2', '3', '4', '6'], n: 'thumbnail sketch' },
  matrix: { k2: ['2', '3'], d: ['2', '3', '4', '5', '6'], n: 'option' },
  interview: { k2: ['3', '4'], d: ['3', '4', '6', '8'], n: 'question' },
  debate: { k2: ['2'], d: ['2', '3'], n: 'argument' },
};
const countLabel = (kind, c) => {
  if (kind === 'stage') return c[0] === 'f' ? `${c.slice(1)} formations (small stages)` : `One stage, ${c} moves`;
  if (kind === 'counts') return `${c} counts (${c / 8} eight${c === '8' ? '' : 's'})`;
  if (kind === 'present') return `${c} ${c === '1' ? 'point' : 'points or reasons'}`;
  return `${c} ${COUNT[kind].n}${c === '1' ? '' : (COUNT[kind].n.endsWith('sketch') ? 'es' : 's')}`;
};

// "size, color, where it lives" -> up to max short labels (none when blank)
function list(text, max = 8, maxLen = 32) {
  return String(text || '').split(',').map(x => x.trim()).filter(Boolean).map(x => x.length > maxLen ? x.slice(0, maxLen - 1).trim() + '.' : x).slice(0, max);
}
const cap = s => s.charAt(0).toUpperCase() + s.slice(1);
const mmss = s => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;

/* ---------- drawing kit ---------- */
function kit(b, r) {
  const lh = LH[b];
  const pk = x => Array.isArray(x) ? r.pick(x) : x;
  const lines = (n, starter) => `<div class="pf-lines" style="--lh:${lh}in">${Array.from({ length: Math.max(1, n) }, (_, i) => `<span>${i === 0 && starter ? `<i>${esc(starter)}</i>` : ''}</span>`).join('')}</div>`;
  // a labeled box: q = guiding prompt (string or bank), n = ruled lines, draw = sketch height in inches, st = starter (string or bank)
  const box = (lab, o = {}) => `<div class="pf-box${o.cls ? ' ' + o.cls : ''}">` +
    `<p class="pf-head"><span class="pf-lab">${lab}</span>${o.q ? ` <span class="pf-q">${pk(o.q)}</span>` : ''}</p>` + (o.pre || '') +
    (o.draw ? `<div class="pf-draw" style="height:${o.draw}in"><span>${o.dl || 'Sketch'}</span></div>` : '') +
    (o.n ? lines(o.n, o.st ? pk(o.st) : '') : '') + (o.extra || '') + '</div>';
  const grid = (cols, items, cls = '') => `<div class="pf-grid${cls ? ' ' + cls : ''}" style="grid-template-columns:${cols}">${items.join('')}</div>`;
  const line = lab => `<p class="pf-line"><b>${lab}</b><span></span></p>`;          // a label with a line to the end
  const lineRow = labs => `<div class="pf-linerow">${labs.map(line).join('')}</div>`;  // several on one row
  const circ = (lab, opts) => `<p class="pf-circ"><b>${lab}</b> ${opts.map(o => `<span>${o}</span>`).join('')}</p>`;   // circle one or more
  const checks = opts => `<p class="pf-checks">${opts.map(o => `<span><i></i> ${o}</span>`).join('')}</p>`;
  const nums = (n, h = 1) => `<ol class="pf-nums" style="--lh:${(lh * h).toFixed(2)}in">${Array.from({ length: n }, () => '<li><span></span></li>').join('')}</ol>`;
  const tab = (head, rows, o = {}) => `<table class="pf-tab${o.cls ? ' ' + o.cls : ''}">` +
    (o.w ? `<colgroup>${o.w.map(w => `<col style="width:${(+w).toFixed(1)}%">`).join('')}</colgroup>` : '') +
    `<thead><tr>${head.map(h => `<th>${h}</th>`).join('')}</tr></thead><tbody>` +
    rows.map(row => `<tr${o.rh && row.cls !== 'pf-ex' ? ` style="height:${o.rh}in"` : ''}${row.cls ? ` class="${row.cls}"` : ''}>${row.map(c => `<td>${c}</td>`).join('')}</tr>`).join('') + '</tbody></table>';
  const tip = (list) => `<p class="pf-tip"><b>Tip:</b> ${esc(pk(list))}</p>`;
  return { lh, pk, lines, box, grid, line, lineRow, circ, checks, nums, tab, tip };
}

/* ---------- tips (one per sheet, from the bank) ---------- */
const TIPS = {
  research: { y: ['A good question starts with how, why or what.', 'Write notes in your own words, not whole sentences from the book.', 'Write the title of each book as soon as you open it.', 'If one place has nothing, try your backup place.', 'Ask the librarian to help you find a book.', 'Check a fact in two places before you use it.'],
    o: ['Record the citation the moment you open a source; it is much harder to find later.', 'Paraphrase: read, look away, then write the idea in your own words.', 'If a search gives too many results, add a keyword with AND; too few, try a synonym with OR.', 'Note which smaller question each source answers, so you can see the gaps.', 'Put exact phrases in quotation marks in your notes and mark the page.', 'Check the date: is this source current enough for your question?'] },
  present: { y: ['Practice out loud two times before you share.', 'Look up at your friends when you talk.', 'Speak slowly and loudly so everyone can hear.', 'Hold your picture where everyone can see it.', 'Start with something that makes people want to listen.', 'Say thank you at the end.'],
    o: ['Time yourself in practice; most people talk faster when they are nervous.', 'One idea per point. If a point needs two visuals, it may be two points.', 'Your opening and closing are what people remember best; plan them word for word.', 'Practice the transitions, not just the points.', 'Pause after your most important sentence.', 'Know your first line by heart, so you start strong.'] },
  slides: { y: ['Put just a few words on each slide.', 'Draw big so your picture is easy to see.', 'Check that the slides go in order.', 'Each slide tells one thing.', 'Use the same colors on every slide.', 'Say more than the slide shows.'],
    o: ['Keep slide text short; say the details out loud.', 'One message per slide; the title can state it.', 'Pick one font and two or three colors for the whole set.', 'Pictures should explain, not just decorate.', 'Number your slides so speaker notes match.', 'Plan a strong first and last slide.'] },
  storyboard: { y: ['Draw stick people. Quick sketches are fine.', 'Each box shows one moment.', 'Show the face up close when the feeling matters.', 'Make sure the story has a beginning, middle and end.', 'Draw arrows to show who moves.', 'Tell the story to a friend using your boxes.'],
    o: ['Sketch fast with stick figures; a storyboard is a plan, not a finished drawing.', 'Vary your shots: a wide shot sets the place, a close-up shows feeling.', 'Draw arrows in the frame for camera moves and character moves.', 'Each panel is a new shot or a new moment, not the same picture twice.', 'Keep a character on the same side of the frame across a conversation.', 'Read the panels in order: could a stranger follow the story with no words?'] },
  shotlist: { y: ['List the shots in the order you will film them.', 'Keep the camera still for each shot.', 'Check off each shot when it is done.', 'Count your frames out loud as you take them.', 'Small moves look smooth; big moves look jumpy.', 'Tape the camera spot on the floor.'],
    o: ['Group shots by camera setup and film them together, even if they are out of story order.', 'Check off each shot as you get it, and note the take you liked.', 'Plan a little extra at the start and end of each shot for editing.', 'Frames per second times seconds gives the frames you need.', 'Write sound needs too: room tone, effects and dialogue.', 'Mark the camera position on the floor so you can come back to it.'] },
  script: { y: ['Each line starts with who is talking.', 'Read your lines out loud. Do they sound like real talk?', 'Stage directions tell what the actor does.', 'Give each character something they want.', 'Make sure something changes by the end.', 'Short lines are easy to say.'],
    o: ['Read the scene aloud; cut any line no one would really say.', 'Stage directions are short and in the present tense.', 'Each character wants something; the scene is about who gets it.', 'Let actions show feelings instead of saying them.', 'Every line should move the story or show a character.', 'Mark where the turn happens: the moment something changes.'] },
  counts: { y: ['Clap the counts first, then dance.', 'Say the counts out loud: 1, 2, 3, 4, 5, 6, 7, 8.', 'Draw a little picture of each move.', 'Hold a freeze on the last count.', 'Try your dance two times.', 'Teach your counts to a partner.'],
    o: ['Count out loud while you set the phrase; then try it silently.', 'A move can take more than one count; draw a long arrow across the counts it fills.', 'Check that each eight adds up to 8 counts.', 'Mark where you breathe or hold; stillness is a choice too.', 'Change at least one element (level, direction, speed) in every eight.', 'Write moves in short words so a partner can read them fast.'] },
  stage: { y: ['Stage right is the actor\'s right when facing the audience.', 'Draw a dot where each person starts.', 'Draw an arrow to show where they move.', 'Do not turn your back to the audience.', 'Leave space between people.', 'Walk your path before you draw it.'],
    o: ['Stage right and left are the performer\'s, not the audience\'s.', 'Use a letter for each performer and an arrow for each path.', 'Every move needs a reason, or it will look like wandering.', 'Check sightlines: can the audience see every face that matters?', 'Avoid lining people up straight across; try diagonals and levels.', 'Walk the blocking with a partner before you write it down.'] },
  art: { y: ['Sketch small and fast. Try more than one idea.', 'Fill the whole box with your picture.', 'Big shapes first, details last.', 'Pick colors that match the feeling.', 'Look at your sketches. Which one do you like best?', 'Try one idea that surprises you.'],
    o: ['Thumbnails are quick: spend about two minutes each.', 'Make each thumbnail different, not the same picture four times.', 'Plan your darks and lights before color.', 'Ask: where does the eye go first? That is your focal point.', 'Choose by the plan, not the prettiest drawing.', 'Note one change you would make to your favorite.'] },
  matrix: { y: ['Score each option the same way.', 'Talk about each score with a partner.', 'A high number means good.', 'Add the scores across.', 'The biggest total is the top pick.', 'Is the winner the one you guessed?'],
    o: ['Score down each column so you compare options on one criterion at a time.', 'Decide what a 1 and a 5 mean before you score.', 'Give the most important criterion the biggest weight.', 'If the winner surprises you, check the weights, not just the scores.', 'A close total means both options are worth a second look.', 'Write one reason for any score of 1 or 5.'] },
  interview: { y: ['Questions that start with how and why get long answers.', 'Look at the person when they talk.', 'Say please and thank you.', 'Write one or two words, then listen more.', 'Ask one question at a time.', 'It is OK to ask them to say it again.'],
    o: ['Open questions (how, why, describe, tell me about) get stories; yes-or-no questions get one word.', 'Ask permission before you record or quote someone.', 'Listen for something surprising and ask a follow-up about it.', 'Write key words while they talk; fill in full notes right after.', 'Put easy, friendly questions first and harder ones later.', 'Read back a quote to check you got it right.'] },
  debate: { y: ['Give a reason for every idea.', 'Listen to the other side.', 'Be kind, even when you disagree.', 'Say "because" to give a reason.', 'Use one fact to back up your idea.', 'Speak loudly and clearly.'],
    o: ['Argue the idea, never the person.', 'Evidence beats opinion; name your source out loud.', 'Write the other side\'s best argument, not their weakest.', 'A rebuttal answers the point, then gives your own evidence.', 'Keep notes on what the other team says; you will need them for rebuttal.', 'Practice your opening so you can speak, not read.'] },
  coach: { y: ['Give one tip at a time.', 'Say what went well first.', 'Show the move, then let them try.', 'Use short words, like "step" or "reach".', 'Count the good tries together.', 'Smile and cheer each try.'],
    o: ['Pick one cue at a time; too many cues overload a learner.', 'Name what went well before the fix.', 'Demonstrate, then let them try before you talk again.', 'Specific feedback ("your elbow was high") beats general ("good job").', 'Watch the same body part on every try.', 'End on a success, even if it means an easier task.'] },
};

/* ---------- prompt banks ---------- */
const Q = {
  bigY: ['What do you wonder about?', 'What do you want to find out?', 'What is one thing you want to learn?'],
  bigO: ['What do you want to find out? Make it a question with no one-word answer.', 'Write a research question that is not too big and not too small.', 'What question will your project answer?'],
  subO: ['Break your big question into smaller ones. Each one should lead you to facts.', 'What do you need to know first to answer the big question?', 'Write smaller questions that together answer the big one.'],
  hookY: ['How will you get your friends to listen?', 'What is a fun way to start?', 'What will you say first?'],
  hookO: ['Open with a question, a surprising fact, a short story or a quote.', 'How will you grab your audience in the first few seconds?', 'Write your first sentence word for word.'],
  closeO: ['End by restating your main idea in a new way and leaving the audience something to think about or do.', 'What do you want the audience to remember? Say it last.', 'Close with a call to action, a question or a link back to your opening.'],
  ideaY: ['What will your art show?', 'What is your picture about?', 'What will you make?'],
  ideaO: ['What is your subject, and what mood or meaning do you want it to have?', 'Describe your idea in one or two sentences: subject, mood and message.', 'What should a viewer think or feel?'],
  chooseO: ['Which thumbnail is strongest? Explain using your plan, not just "it looks good".', 'Pick one thumbnail to develop. What makes it stronger than the others?', 'Which sketch best shows your idea? What will you change in the final?'],
  reflectO: ['After: what worked, and what would you do differently next time?', 'After: how well does the finished piece show your idea? Give one strength and one change.', 'After: what did you learn about your materials or process?'],
  decideO: ['Which option do you choose? Use the totals and one other reason.', 'Write your recommendation and back it with the matrix.', 'What is your decision, and what is the main reason?'],
  doubtO: ['What is the biggest weakness of your choice, and how could you handle it?', 'Which score are you least sure of? How would you check it?', 'What would have to change for a different option to win?'],
  afterIntY: ['What was the best thing you learned?', 'Draw or write one thing they told you.', 'What surprised you?'],
  afterIntO: ['What was the most surprising answer? What new question does it raise?', 'Write your thank-you note: one thing you learned and why it mattered to you.', 'Which answer will you use in your project, and how?'],
};

/* ---------- the kinds: each returns the frame html ---------- */
const BUILD = {
  research(b, K, c, r) {
    const n = +c.count;
    if (b === 'k2') {
      const books = Array.from({ length: n }, (_, i) => `<div class="pf-src">${K.line(`Book${n > 1 ? ' ' + (i + 1) : ''} title:`)}${K.line('Author:')}</div>`).join('');
      return K.box('I wonder', { q: Q.bigY, n: 2, st: ['I wonder', 'How do', 'Why do'] }) +
        K.box('Where I will look', { extra: K.checks(['a book', 'a website with a grown-up', 'a person who knows', 'a video']) }) +
        K.box(n > 1 ? 'My books' : 'My book', { extra: books }) +
        K.box('What I found out', { q: ['Draw and write.', 'Draw it. Then write one sentence.'], draw: n > 1 ? 1.5 : 2.0, n: 1, st: ['I learned'] });
    }
    const subN = b === '35' ? 3 : 4, notes = 3;
    const types = b === '35' ? ['book', 'website', 'magazine', 'video', 'person'] : ['book', 'database article', 'website', 'interview', 'video', 'primary source'];
    const src = Array.from({ length: n }, (_, i) => K.box(`Source ${'ABCD'[i]}`, {
      pre: K.circ('Type:', types) + K.line(b === '35' ? 'Answers question #' : 'Answers smaller question #') +
        (b === '912' ? K.line('Can I trust it? Author, date, purpose:') : ''),
      n: notes, st: i === 0 ? (b === '35' ? 'Notes in my words:' : 'Notes (paraphrase; quote marks and page for exact words):') : '' }));
    const pattern = b === '35' ? 'Author last name, first name. <i>Title</i>. Publisher, year.'
      : 'Author last name, first name. "Title of Article or Page." <i>Website, Book or Journal</i>, Publisher, date, URL or pages.';
    const cites = Array.from({ length: n }, (_, i) => `<div class="pf-cite"><b>${'ABCD'[i]}</b>${K.lines(2)}</div>`).join('');
    const steps = { 35: ['Write my questions', 'Find my sources', 'Take notes', 'Make my report', 'Share it'],
      68: ['Questions and keywords', 'Find and check sources', 'Notes and citations', 'Draft', 'Revise and present'],
      912: ['Question and search plan', 'Find and evaluate sources', 'Notes and citations', 'Draft and peer feedback', 'Revise, cite and present'] }[b];
    return K.box('Big question', { q: Q.bigO, n: b === '35' ? 2 : 1 }) +
      K.box('Smaller questions', { q: Q.subO, extra: K.nums(subN) }) +
      K.grid('1.15fr 1fr', [
        K.box('Keywords', { extra: K.tab(['Keyword', b === '35' ? 'Other words for it' : 'Synonyms and related terms'], [['', ''], ['', ''], ['', '']], { rh: LH[b] + 0.04 }) +
          K.line(b === '35' ? 'Search words (try AND, OR):' : 'Search string (AND, OR, "quotes"):') }),
        K.box('Where to look', { extra: K.circ('Circle:', b === '35' ? ['library catalog', 'kids database', 'website', 'encyclopedia', 'expert'] : ['library catalog', 'database', 'search engine', 'encyclopedia', 'expert or interview']) +
          K.line('First place:') + K.line('Backup place:') })]) +
      K.grid('1fr 1fr', src) +
      K.box(b === '35' ? 'Source list' : 'Works cited', { q: b === '35' ? 'Write each source like the pattern.' : ['Follow the pattern (MLA style), in order by author.', 'Write a full citation for each source, then put them in ABC order by author.'],
        pre: `<p class="pf-pattern">Pattern: ${pattern}</p>`, extra: cites }) +
      K.box('My plan', { extra: K.tab(['Step', 'Due', 'Done'], steps.map(s => [esc(s), '', '<i class="pf-cb"></i>']), { w: [62, 26, 12], rh: LH[b] + 0.04 }) });
  },

  present(b, K, c, r) {
    const form = c.form, n = +c.count;
    if (b === 'k2') {
      const talk = form === 'opinion' ? { lab: 'What I think', st: ['I think', 'My idea is'], parts: ['One reason is', 'Another reason is', 'Also,'] }
        : form === 'booktalk' ? { lab: 'My book', st: ['My book is', 'The book is called'], parts: ['It is about', 'My favorite part is', 'You will like it if'] }
        : form === 'pitch' ? { lab: 'My idea', st: ['My idea is', 'I want to make'], parts: ['It helps', 'It needs', 'It is good because'] }
        : { lab: 'My topic', st: ['I will tell about', 'This is my'], parts: ['First,', 'It can', 'I like it because'] };
      return K.box(talk.lab, { q: ['What will you talk about?', 'Write it here.'], n: 1, st: talk.st }) +
        K.box('Things I will say', { q: ['Say each one out loud first.', 'One idea on each line.'], extra: talk.parts.slice(0, n).map(p => K.lines(1, p)).join('') }) +
        K.box('What I will show', { q: ['Draw the picture or thing you will hold up.', 'Draw what you will show.'], draw: 1.8 }) +
        K.box('When I talk', { extra: K.checks(['stand tall', 'speak loud', 'look at my friends', 'say thank you']) });
    }
    const T = +c.mins * 60, sec = c.timing;
    const chip = name => `<span class="pf-time">about ${mmss(sec[name])}</span>`;
    const point = (lab, key, q, evid) => K.box(`${lab} ${chip(key)}`, { q, n: b === '35' ? 2 : 1, st: '',
      pre: '', extra: K.line(evid) + K.lineRow(b === '35' ? ['Visual:'] : ['Visual or media:', 'Transition:']) });
    let body = '';
    const opening = K.box(`Opening ${chip('open')}`, { q: Q.hookO, n: 2 });
    const closing = K.box(`Closing ${chip('close')}`, { q: Q.closeO, n: 2 });
    if (form === 'report' || form === 'opinion') {
      const claim = form === 'opinion' ? K.box('My claim', { q: ['State your opinion in one clear sentence.', 'What do you want the audience to agree with?'], n: 1 }) : '';
      const pts = Array.from({ length: n }, (_, i) => form === 'opinion'
        ? point(`Reason ${i + 1}`, 'p' + i, ['Why should the audience agree?', 'Give a reason, not a fact yet.'], b === '35' ? 'A fact or example:' : 'Evidence (with source):')
        : point(`Point ${i + 1}`, 'p' + i, i === 0 ? ['Your first main idea, in one sentence.', 'Start with the point the audience needs first.'] : ['Your next main idea, in one sentence.', 'How does this build on the point before?'], b === '35' ? 'Fact or detail:' : 'Evidence or details (with source):')).join('');
      const counter = form === 'opinion' ? K.box(`Other side ${chip('counter')}`, { q: ['What might someone who disagrees say? How do you answer?', 'Name the strongest opposing point, then respond.'], n: 2, st: ['Some people say', 'Others may argue that'] }) : '';
      body = opening + claim + pts + counter + closing;
    } else if (form === 'pitch') {
      const P = [['Problem', 'pr', 'What problem do people have? Who has it?'], ['Solution', 'so', 'What is your idea, and how does it solve the problem?'],
        ['Who it helps', 'cu', 'Who are your customers or audience?'], ['What it needs', 'co', 'Costs, materials, people and time.'], ['Risks', 'ri', 'What could go wrong, and how will you handle it?']];
      body = opening + K.grid('1fr 1fr', P.map(([lab, key, q]) => K.box(`${lab} ${chip(key)}`, { q, n: 3 }))) +
        K.box(`The ask ${chip('close')}`, { q: ['What do you want the audience to do or give? End on it.', 'Close with exactly what you are asking for.'], n: 2 });
    } else {
      body = opening + K.box('Title and author', { extra: K.lineRow(['Title:', 'Author:']) }) +
        K.box(`What it is about ${chip('ab')}`, { q: ['Three details that make people curious. No spoilers!', 'Tell the setup, not the ending.'], extra: K.nums(3) }) +
        K.box(`Who might enjoy it ${chip('who')}`, { q: ['If you liked..., you will like this because...', 'Who should read it, and why?'], n: 2, st: 'You will like this book if' }) + closing;
    }
    const prac = K.box('Practice', { extra: K.checks(['practiced aloud twice', 'timed it: ____', 'eye contact', 'loud and clear', 'slow at key points']) +
      (b === '35' ? '' : K.line('A question someone might ask, and my answer:') + K.lines(1)) });
    return K.box('Audience and purpose', { extra: K.lineRow(['Who will listen:', 'Goal:']) + `<p class="pf-small">Total time: ${c.mins} minute${c.mins === '1' ? '' : 's'}. The times on each part add up to it.</p>` }) + body + prac;
  },

  slides(b, K, c, r) {
    const n = +c.count, titles = c.titles;
    const cols = b === 'k2' && n !== 4 ? 3 : 2;
    const draw = b === 'k2' ? (n === 3 ? 1.8 : n === 4 ? 1.5 : 1.15) : n > 6 ? 1.15 : n > 4 ? 1.3 : 1.6;
    const cards = Array.from({ length: n }, (_, i) => {
      const t = titles[i] ? `<b>${esc(cap(titles[i]))}</b>` : '';
      const head = `Slide ${i + 1}${t ? ': ' : ''}${t}`;
      return b === 'k2'
        ? K.box(head, { pre: t ? '' : K.line('Title:'), draw, dl: 'Draw', n: 1, st: i === 0 ? 'Words:' : '' })
        : K.box(head, { pre: t ? '' : K.line('Title:'), draw, n: 1, st: i === 0 ? 'Words on the slide:' : '',
          extra: K.lines(b === '35' ? 1 : 2, i === 0 ? (b === '35' ? 'What I will say:' : 'Speaker notes or narration:') : '') });
    });
    const top = b === 'k2' ? '' : K.box('Plan', { extra: K.lineRow(['Topic:', 'Audience:']) + K.line(K.pk(['Main message in one sentence:', 'What should people learn?', 'The big idea:'])) });
    const end = b === 'k2' ? K.box('Check', { extra: K.checks(['in order', 'big pictures', 'a few words', 'I can tell about each one']) })
      : K.box('Check', { extra: K.checks(['slides in order', 'one idea per slide', 'few words, big pictures', 'notes say more than the slide', 'sources credited']) });
    return top + K.grid(`repeat(${cols}, 1fr)`, cards) + end;
  },

  storyboard(b, K, c, r) {
    const n = +c.count;
    const lab = b === 'k2' ? ['What happens'] : c.lines.length ? c.lines.map(cap) : { 35: ['Shot', 'Action', 'Sound'], 68: ['Shot and angle', 'Action', 'Sound or dialogue'], 912: ['Shot and angle', 'Movement', 'Sound or dialogue', 'Transition'] }[b];
    const named = n === 3 ? ['Beginning', 'Middle', 'End'] : n === 4 && young(b) ? ['First', 'Next', 'Then', 'Last'] : [];
    const cols = b === 'k2' ? (n === 3 ? 1 : n === 4 ? 2 : 3) : n >= 6 ? 3 : 2;
    const fh = b === 'k2' ? (n === 3 ? 1.6 : n === 4 ? 1.7 : 1.3) : cols === 3 ? (n >= 10 ? 1.2 : 1.3) : 1.75;
    const panels = Array.from({ length: n }, (_, i) => {
      const head = `<p class="pf-ph"><b>${i + 1}</b>${named[i] ? ' ' + named[i] : ''}${b === 'k2' ? '' : '<span class="pf-sec">sec ____</span>'}</p>`;
      const frame = `<div class="pf-frame" style="height:${fh}in"></div>`;
      const ls = b === 'k2' ? K.lines(n === 3 ? 3 : 2) : lab.map(l => K.line(esc(l) + ':')).join('');
      return b === 'k2' && n === 3 ? `<div class="pf-panel pf-side">${head}<div class="pf-sidegrid">${frame}<div>${ls}</div></div></div>` : `<div class="pf-panel">${head}${frame}${ls}</div>`;
    });
    const top = b === 'k2' ? K.box('My story', { q: ['Who is in it? What happens?', 'Tell your story in one sentence.'], n: 1 })
      : K.box('Story in one sentence', { extra: K.lines(1) + K.lineRow(['Total length (seconds):', 'Audience:']) });
    const key = c.key && b !== 'k2' ? `<div class="pf-key"><p><b>Shots:</b> WS wide shot (whole place) · MS medium shot (waist up) · CU close-up (face or object) · ECU extreme close-up (eyes, a detail) · OTS over the shoulder · POV point of view (what a character sees)</p>` +
      `<p><b>Angles:</b> eye level · high angle (camera looks down) · low angle (camera looks up)${b === '35' ? '' : ' · <b>Moves:</b> pan (turns side to side) · tilt (up and down) · zoom (lens closer or farther) · track (camera travels)'}</p></div>` : '';
    return top + key + K.grid(`repeat(${cols}, 1fr)`, panels, 'pf-board');
  },

  shotlist(b, K, c, r) {
    const n = +c.count, t = c.tcol;
    const mid = c.cols.length ? c.cols.map(x => esc(cap(x))) : { k2: ['Draw the shot', 'What moves?'], 35: ['What we see', 'Shot type', 'Camera spot'],
      68: ['Setup', 'Shot type and angle', 'What happens', 'Sound'], 912: ['Setup', 'Shot and angle', 'Camera move', 'Action', 'Sound'] }[b];
    const time = t === 'sec' ? ['Seconds'] : ['Frames', 'Seconds'];
    const head = ['#', ...mid, ...time, 'Done'];
    const w = [5, ...mid.map(() => (95 - 7 - time.length * 10) / mid.length), ...time.map(() => 10), 7];
    const rh = b === 'k2' ? 0.6 : n > 12 ? 0.42 : n > 8 ? 0.5 : 0.58;
    const rows = Array.from({ length: n }, (_, i) => [String(i + 1), ...mid.map(() => ''), ...time.map(() => ''), '<i class="pf-cb"></i>']);
    const total = ['', `<b>Total</b>`, ...mid.slice(1).map(() => ''), ...time.map(() => ''), '']; total.cls = 'pf-total';
    rows.push(total);
    const fps = +t, f = c.fx;   // worked example: frames to seconds
    const help = t === 'sec' ? K.box('Timing', { extra: K.lineRow(['Target length (seconds):', 'My total:']) + `<p class="pf-small">Add the seconds column for your total. If you are long, cut or shorten a shot.</p>` })
      : K.box('Timing', { extra: `<p class="pf-small">At ${fps} frames per second, ${fps} frames make 1 second. Seconds = frames ÷ ${fps}. Example: ${f * fps} frames ÷ ${fps} = ${f} seconds.</p>` +
        K.lineRow(['Target length (seconds):', `Frames needed (seconds × ${fps}):`]) });
    return K.box('Project', { extra: K.lineRow(['Title:', b === 'k2' ? 'Camera person:' : 'Crew:']) }) +
      K.tab(head, rows, { w, rh, cls: 'pf-shots' }) + help;
  },

  script(b, K, c, r) {
    const n = +c.count, names = c.names, cue = c.cue;
    const cueHead = { stage: 'Stage direction', sound: 'Sound or music cue', action: 'Action (what we see)' }[cue];
    const ex = { stage: [['MAYA', 'Where did it go?', '(looks under the desk)'], ['OMAR', 'I bet it is in the hall.', '(crosses to the door)'], ['JADE', 'Did you hear that?', '(whispers, eyes wide)']],
      sound: [['NARRATOR', 'Night falls on the farm.', 'Crickets chirp. A door creaks.'], ['SAM', 'Who is there?', 'Soft, slow music begins.'], ['NARRATOR', 'The rain will not stop.', 'Thunder, far away.']],
      action: [['LEO', 'Wait for me!', 'Leo runs after the bus.'], ['ANA', 'This is it.', 'Ana opens the box slowly.'], ['KAI', 'Not again.', 'Kai drops his bag on the bench.']] }[cue];
    const e = K.pk(ex);
    const who = names.length >= 2 && names.length <= 4 ? `<span class="pf-names">${names.map(x => `<span>${esc(x)}</span>`).join('')}</span>` : '';
    const rh = b === 'k2' ? 0.72 : n > 12 ? 0.5 : 0.6;
    const exRow = ['Ex.', ...e.map(x => `<i>${esc(x)}</i>`)]; exRow.cls = 'pf-ex';
    const rows = [exRow, ...Array.from({ length: n }, (_, i) => [String(i + 1), who, '', ''])];
    const head = b === 'k2' ? ['#', who ? 'Who talks (circle)' : 'Who talks', 'What they say', cue === 'stage' ? 'What they do' : cue === 'sound' ? 'Sound' : 'What we see'] : ['#', 'Character', 'Line', cueHead];
    const top = b === 'k2'
      ? K.box('My play', { extra: K.lineRow(['Where:', 'Who:']) + K.lines(1, 'The problem is') })
      : K.box('Scene', { extra: K.lineRow(['Setting (where and when):', 'Characters:']) + (names.length ? `<p class="pf-small"><b>Characters:</b> ${names.map(esc).join(', ')}</p>` : '') +
        K.line(b === '35' ? 'The problem:' : 'What each character wants:') + K.line(b === '35' ? 'How it changes:' : 'The turn (the moment something changes):') });
    const check = b === 'k2' ? K.box('Check', { extra: K.checks(['every line has who', 'read it out loud', 'something changes']) })
      : K.box('Check', { extra: K.checks(['every line has a speaker', cue === 'stage' ? 'directions in (parentheses), present tense' : cue === 'sound' ? 'every cue says what we hear' : 'actions say only what we can see', 'it sounds like real talk', 'something changes by the end']) });
    return top + K.tab(head, rows, { w: b === 'k2' ? [6, 20, 44, 30] : [5, 17, 48, 30], rh, cls: 'pf-script' }) + check;
  },

  counts(b, K, c, r) {
    const eights = +c.count / 8, ands = c.ands && b !== 'k2';
    const layers = b === 'k2' ? ['Move'] : c.layers.length ? c.layers.map(cap) : { 35: ['Move', 'Level', 'Direction'], 68: ['Move', 'Level', 'Direction or facing', 'Energy'], 912: ['Move', 'Level', 'Facing', 'Pathway', 'Dynamics'] }[b];
    const beats = ands ? [1, 2, 3, 4, 5, 6, 7, 8].flatMap(x => [String(x), '&']) : ['1', '2', '3', '4', '5', '6', '7', '8'];
    const lw = b === 'k2' ? 12 : 16, cw = (100 - lw) / beats.length;
    const rh = b === 'k2' ? (eights === 1 ? 1.6 : 1.05) : layers.length > 4 ? 0.36 : 0.42;
    const blocks = Array.from({ length: eights }, (_, e) => {
      const head = [`Eight ${e + 1}`, ...beats.map(x => x === '&' ? '<span class="pf-and">&amp;</span>' : x)];
      const rows = layers.map(l => [`<b>${esc(l)}</b>`, ...beats.map(() => '')]);
      return (b === 'k2' ? '' : `<p class="pf-eight">${K.line(`Eight ${e + 1} idea or section:`)}</p>`) +
        K.tab(head, rows, { w: [lw, ...beats.map(() => cw)], rh, cls: 'pf-counts' });
    }).join('');
    const key = c.key ? `<div class="pf-key"><p><b>Class symbol key</b> (make your own for anything else): ` +
      `&#8594; &#8592; &#8593; &#8595; travel that way · &#8635; turn · &#9679; hold (stillness) · &#8743; jump${b === 'k2' ? '' : ' · H M L high, middle, low level · &gt; accent (sharp, strong)'}</p></div>` : '';
    const top = b === 'k2' ? K.box('My dance', { q: ['What is your dance about?', 'Give your dance a name.'], n: 1 })
      : K.box('Phrase', { extra: K.lineRow(['Idea or theme:', 'Music or tempo:']) });
    const end = b === 'k2' ? K.box('Try it', { extra: K.checks(['clapped the counts', 'danced it two times', 'showed a friend']) })
      : K.box('Notes', { q: ['Transitions, formations, and what changes from eight to eight.', 'Where do you hold, speed up or change level? Why?', 'What will a partner find hardest to read? Make it clearer here.'], n: 2,
        extra: K.checks(['every eight adds up to 8 counts', 'a partner can read it', 'danced it from the sheet']) });
    return top + key + blocks + end;
  },

  stage(b, K, c, r) {
    const formations = c.count[0] === 'f', n = +c.count.replace('f', '');
    const legend = b === 'k2' ? `<p class="pf-small">The front of the stage is near the audience. Stage right is your right hand when you face the audience.</p>`
      : `<p class="pf-small"><b>Areas:</b> USR up stage right · USC up stage center · USL up stage left · SR stage right · CS center stage · SL stage left · DSR down stage right · DSC down stage center · DSL down stage left. Stage right and left are the performer's right and left when facing the audience; down stage is closest to the audience.</p>`;
    const letters = b === 'k2' ? 'ABC' : b === '35' ? 'ABCD' : 'ABCDEF';
    const who = K.box('Who is who', { q: ['Give each performer a letter.', 'Use these letters on the stage plan.'], extra: `<div class="pf-linerow">${[...letters].map(x => K.line(x + ' =')).join('')}</div>` });
    if (formations) {
      const cards = Array.from({ length: n }, (_, i) => `<div class="pf-panel"><p class="pf-ph"><b>${i + 1}</b> Formation ${b === 'k2' ? '' : '<span class="pf-sec">counts ____</span>'}</p>${stageSvg(b, true)}${K.line(i === n - 1 ? (b === 'k2' ? 'How we end:' : 'Ending (hold, exit or bow):') : (b === 'k2' ? 'How we move:' : 'Transition to the next:'))}</div>`);
      return legend + who + K.grid('1fr 1fr', cards, 'pf-board');
    }
    const head = b === 'k2' ? ['#', 'Who', 'From', 'To'] : ['#', 'Who', 'From', 'To', b === '35' ? 'When' : 'When (line or count)', b === '35' ? 'Why?' : 'Why (motivation) or note'];
    const rows = Array.from({ length: n }, (_, i) => [String(i + 1), ...head.slice(1).map(() => '')]);
    return legend + `<div class="pf-stagebig">${stageSvg(b, false)}</div>` + who +
      K.tab(head, rows, { w: b === 'k2' ? [8, 22, 35, 35] : [5, 9, 12, 12, 20, 42], rh: b === 'k2' ? 0.48 : 0.44, cls: 'pf-moves' }) +
      (b === 'k2' ? '' : K.box('Sightlines', { q: ['Can the audience see every face that matters? Where might someone block someone?', 'Which move is the most important? How does the blocking make it stand out?', 'Where is the focus at the start, and how does it shift?'], n: 2 }));
  },

  art(b, K, c, r) {
    const n = +c.count, focus = c.focus;
    const thumbLab = { elements: 'What I used', color: 'Colors', principles: 'Principle', value: 'Light, middle, dark', poster: 'Layout idea', none: 'Idea' }[focus];
    const bank = {
      elements: young(b) ? [['Shapes', ['circle', 'square', 'triangle', 'rectangle', 'oval', 'star']], ['Lines', ['straight', 'curved', 'wavy', 'zigzag', 'dotted', 'spiral']],
        ['Colors', ['red', 'yellow', 'blue', 'orange', 'green', 'purple']], ['Textures', ['smooth', 'rough', 'bumpy', 'fuzzy', 'scaly', 'spiky']]]
        : [['Elements', ['line', 'shape', 'form', 'value', 'color', 'texture', 'space']]],
      color: b === 'k2' ? [['Primary', ['red', 'yellow', 'blue']], ['Secondary', ['orange', 'green', 'purple']]]
        : [['Scheme', ['warm', 'cool', 'complementary', 'analogous', 'monochromatic']], ['Mood', ['calm', 'cheerful', 'lonely', 'mysterious', 'energetic', 'tense']]],
      principles: b === 'k2' ? [['Make it', ['big and small', 'a pattern', 'balanced', 'stand out']]]
        : [['Principles', ['balance', 'contrast', 'emphasis', 'movement', 'pattern', 'rhythm', 'unity', 'variety', 'proportion']]],
      value: b === 'k2' ? [['Use', ['light', 'dark', 'in between']]] : [['Value', ['high contrast', 'low contrast', 'light (high key)', 'dark (low key)']], ...(young(b) ? [] : [['Perspective', ['one-point', 'two-point', 'none']]])],
    }[focus];
    const bankHtml = bank ? K.box(b === 'k2' ? 'Circle what you will use' : 'My choices', {
      q: focus === 'principles' && b !== 'k2' ? 'Circle 2 principles and tell how you will use each.' : focus === 'color' && b !== 'k2' ? 'Circle a scheme and a mood. Why do they fit?' : b === 'k2' ? '' : 'Circle your choices.',
      extra: bank.map(([lab, opts]) => K.circ(lab + ':', opts)).join('') + (b === 'k2' ? '' : K.lines(focus === 'principles' || focus === 'color' ? 2 : 1, focus === 'principles' ? 'I will use' : focus === 'color' ? 'These fit because' : '')) }) : '';
    const sw = (labs) => `<div class="pf-swatches">${labs.map(l => `<div><i></i>${l ? `<span>${l}</span>` : '<b></b>'}</div>`).join('')}</div>`;
    const swatch = focus === 'color' ? K.box('Swatches', { q: b === 'k2' ? 'Color a box for each color you will use.' : young(b) ? 'Test your colors here. Label each one.' : 'Test a tint, the pure hue and a shade of two colors.',
      extra: b === 'k2' ? sw(['', '', '', '']) : young(b) ? sw(['', '', '', '', '', '']) : sw(['tint', 'hue', 'shade', 'tint', 'hue', 'shade']) })
      : focus === 'value' ? K.box('Value scale', { q: b === 'k2' ? 'Color light, then in between, then dark.' : 'Fill the scale from lightest to darkest with your medium.', extra: sw(b === 'k2' || b === '35' ? ['light', 'middle', 'dark'] : ['1 light', '2', '3 middle', '4', '5 dark']) }) : '';
    const poster = focus === 'poster' ? K.box('Message', { extra: (b === 'k2' ? K.line('Who will see it:') + K.line('Big words:') + K.line('Colors:') + K.line('Where it will hang:')
      : K.lineRow(['Audience:', 'Where it will hang:']) + K.line('Message in one sentence:') + K.line('Slogan or headline:') + K.line('Picture:') + K.line('Colors and why:') +
        (b === '35' ? '' : K.line('Fact 1 and source:') + K.line('Fact 2 and source:')) + K.line('Call to action:')) }) : '';
    const cols = n === 2 ? 2 : n === 4 ? 2 : 3;
    const th = b === 'k2' ? (n === 2 ? 1.7 : 1.45) : n === 6 ? 1.45 : cols === 2 ? 1.9 : 1.6;
    const thumbs = Array.from({ length: n }, (_, i) => `<div class="pf-panel"><p class="pf-ph"><b>${i + 1}</b></p><div class="pf-frame pf-thumb" style="height:${th}in"></div>${b === 'k2' ? '' : K.line(thumbLab + ':')}</div>`);
    const choose = b === 'k2' ? K.box('My favorite', { extra: K.lines(1, ['I like number', 'My best one is number']) })
      : K.box('Choose', { q: Q.chooseO, n: 2, st: ['Number', 'I choose number'] });
    const make = b === 'k2' ? K.box('I will use', { extra: K.checks(['crayons', 'markers', 'paint', 'colored paper', 'glue', 'scissors']) })
      : K.grid('1fr 1.3fr', [K.box('Materials', { n: 3 }), K.box('Steps', { extra: K.nums(3) })]);
    const after = b === 'k2' ? '' : K.box('Reflect', { q: Q.reflectO, n: 2 });
    return K.box(b === 'k2' ? 'My idea' : 'Idea', { q: b === 'k2' ? Q.ideaY : Q.ideaO, n: b === 'k2' ? 1 : 2 }) + poster + bankHtml + swatch +
      K.box(b === 'k2' ? 'Sketches' : 'Thumbnail sketches', { q: b === 'k2' ? 'Draw a few ideas.' : ['Try a different idea in each box.', 'Change the view, layout or focal point each time.', 'Quick sketches: about two minutes each.'],
        extra: K.grid(`repeat(${cols}, 1fr)`, thumbs, 'pf-board') }) + choose + make + after;
  },

  matrix(b, K, c, r) {
    const n = +c.count, wt = c.weights && b !== 'k2';
    const dflt = { k2: ['Is it fun?', 'Is it safe?', 'Is it easy?'], 35: ['Cost', 'How well it works', 'Safety', 'Fun or interest'], 68: ['Cost', 'Effectiveness', 'Time needed', 'Impact on people'], 912: ['Cost', 'Effectiveness', 'Feasibility', 'Fairness', 'Long-term impact'] }[b];
    const crit = c.crit.length >= 2 ? c.crit.slice(0, b === 'k2' ? 3 : wt ? 5 : 6).map(cap) : dflt;
    const opts = c.opts;
    const scale = b === 'k2' ? '3 = yes!, 2 = kind of, 1 = no' : '5 = excellent, 4 = good, 3 = OK, 2 = weak, 1 = poor';
    const cell = wt ? '<span class="pf-sc"></span><span class="pf-x">× w =</span><span class="pf-sc"></span>' : '';
    const ow = b === 'k2' ? 30 : 20, tw = b === 'k2' ? 16 : 10, rw = b === 'k2' ? 0 : 8;
    const cw = (100 - ow - tw - rw) / crit.length;
    const head = [b === 'k2' ? 'Choice' : 'Option', ...crit.map(x => esc(x)), 'Total', ...(rw ? ['Rank'] : [])];
    const rows = [];
    if (wt) { const w = ['<b>Weight (1 to 3)</b>', ...crit.map(() => ''), '', '']; w.cls = 'pf-weight'; rows.push(w); }
    for (let i = 0; i < n; i++) rows.push([opts[i] ? `<b>${esc(cap(opts[i]))}</b>` : '', ...crit.map(() => cell), '', ...(rw ? [''] : [])]);
    const rh = b === 'k2' ? 0.75 : n > 4 ? 0.5 : 0.64;
    const ex = c.ex;
    const example = b === 'k2' ? '' : wt
      ? `<p class="pf-example"><b>How to score:</b> write the score, multiply by the column's weight, and write the product. Example: score ${ex.s} × weight ${ex.w} = ${ex.s * ex.w}. The total is the sum of the products across the row.</p>`
      : `<p class="pf-example"><b>How to score:</b> score each option on each criterion, then add across the row. Example: scores ${ex.list.join(', ')} make a total of ${ex.list.reduce((a, x) => a + x, 0)}.</p>`;
    const top = K.box(b === 'k2' ? 'We need to pick' : 'Decision', { extra: K.line(b === 'k2' ? 'We are choosing:' : 'The question we are deciding:') + (b === 'k2' || opts.length ? '' : `<p class="pf-small">Write one option in each row of the first column.</p>`) +
      `<p class="pf-small"><b>Scale:</b> ${scale}.</p>` });
    const after = b === 'k2' ? K.box('We pick', { extra: K.lines(1, 'We pick') + K.lines(1, 'because') })
      : K.box('Decide', { q: Q.decideO, n: 2 }) + K.box(b === '35' ? 'Check' : 'Think again', { q: b === '35' ? ['Is the winner the one you guessed? Why or why not?', 'Which score was hardest to give? Why?'] : Q.doubtO, n: 2 });
    return top + example + K.tab(head, rows, { w: [ow, ...crit.map(() => cw), tw, ...(rw ? [rw] : [])], rh, cls: 'pf-matrix' }) + after;
  },

  interview(b, K, c, r) {
    const n = +c.count, groups = c.groups;
    const starters = ['Who', 'What', 'Where', 'When', 'Why', 'How'];
    const s0 = r.int(0, 5);
    const qBlock = (i) => b === 'k2'
      ? `<div class="pf-qk"><p><b>${i + 1}.</b> <span class="pf-start">${starters[(s0 + i) % 6]}</span><span class="pf-fill"></span> ?</p><div class="pf-draw" style="height:${n === 3 ? 0.75 : 0.5}in"><span>Answer: draw or write</span></div></div>`
      : `<div class="pf-qb"><p class="pf-qline"><b>${i + 1}.</b><span></span></p>${b === '35' ? '' : K.line('Follow-up:')}${K.lines(2, i === 0 ? 'Notes on the answer:' : '')}</div>`;
    let qs = '';
    if (groups.length >= 2 && b !== 'k2') {
      const g = Math.min(groups.length, n);
      let k = 0;
      for (let j = 0; j < g; j++) {
        const m = Math.floor(n / g) + (j < n % g ? 1 : 0);
        qs += `<p class="pf-group">${esc(cap(groups[j]))}</p>`;
        for (let t = 0; t < m; t++) qs += qBlock(k++);
      }
    } else qs = Array.from({ length: n }, (_, i) => qBlock(i)).join('');
    const top = b === 'k2' ? K.box('I will ask', { extra: K.line('Name:') + K.line('They are a:') })
      : K.box('Who and why', { extra: K.lineRow(['Person:', 'Their job or role:']) + K.line('Why I am asking them:') +
        (b === '35' ? '' : K.lineRow(['Where and when:', 'OK to record or quote? yes / no'])) });
    const intro = b === 'k2' ? '' : K.box('How I will start', { q: ['Say who you are, why you are asking, and how long it will take.', 'Greet them, thank them for their time, and explain your project.'], n: 1, st: ['Hello, my name is', 'Thank you for meeting with me. I am'] });
    const tipq = b === 'k2' ? `<p class="pf-small">Start with a question word. Good questions cannot be answered with yes or no.</p>`
      : `<p class="pf-small"><b>Open starters:</b> How, Why, What was it like, Tell me about, Describe. Avoid yes-or-no starters like Do, Is, Can, Are.</p>`;
    return top + intro + `<p class="pf-sect">Questions</p>${tipq}${qs}` + K.box(b === 'k2' ? 'After' : 'After the interview', { q: b === 'k2' ? Q.afterIntY : Q.afterIntO, n: b === 'k2' ? 1 : 2, st: b === 'k2' ? 'Thank you for' : '' });
  },

  debate(b, K, c, r) {
    const n = +c.count, lang = c.lang;
    const FR = {
      en: ['I believe that ... because ...', 'One reason is ...', 'According to ..., ...', 'Some people say ..., but ...', 'I disagree because ...', 'In conclusion, ...'],
      es: ['Creo que ... porque ...', 'Una razón es que ...', 'Según ..., ...', 'Algunos dicen que ..., pero ...', 'No estoy de acuerdo porque ...', 'En conclusión, ...'],
      fr: ['Je pense que ... parce que ...', 'Une raison est que ...', 'Selon ..., ...', 'Certains disent que ..., mais ...', 'Je ne suis pas d\'accord parce que ...', 'En conclusion, ...'],
    }[lang];
    const frames = K.box(lang === 'en' ? 'Speaking frames' : lang === 'es' ? 'Speaking frames (en español)' : 'Speaking frames (en français)', { extra: `<ul class="pf-frames">${FR.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` });
    if (b === 'k2') {
      return K.box('The question', { extra: K.lines(1) }) +
        K.box('What I think', { extra: K.circ('Circle:', ['I agree', 'I disagree']) }) +
        Array.from({ length: 2 }, (_, i) => K.box(`Reason ${i + 1}`, { draw: 0.65, dl: 'Draw', n: 1, st: 'because' })).join('') +
        K.box('The other side', { q: ['What might a friend who disagrees say?', 'What would someone on the other side say?'], n: 1, st: 'Some people say' }) + frames;
    }
    const sides = b === '912' ? ['Affirmative (for)', 'Negative (against)'] : ['For', 'Against'];
    const args = Array.from({ length: n }, (_, i) => K.box(`Argument ${i + 1}`, { extra: K.line('Claim:') + K.line('Evidence and source:') + K.lines(1) + K.line(b === '35' ? 'Why it matters:' : 'Reasoning (why the evidence proves the claim):') }));
    const ct = K.tab(['They might say', 'Our rebuttal', 'Our evidence'], Array.from({ length: n }, () => ['', '', '']), { w: [33, 37, 30], rh: 0.75 });
    const roles = b === '35' ? '' : K.box('Roles', { extra: K.tab(['Role', 'Who', 'Job'], [['Opening speaker', '', 'States the side and the arguments'], ['Rebuttal speaker', '', 'Answers the other team\'s points'], ['Closing speaker', '', 'Sums up why our side wins'], ['Researcher and timekeeper', '', 'Finds evidence, watches the time']], { w: [30, 22, 48], rh: 0.36 }) });
    return K.box('Resolution', { q: ['The statement being debated, word for word.', 'Write the resolution exactly as given.'], n: 1, extra: K.circ('Our side:', sides) }) +
      args + K.box('Counterarguments', { q: ['What will the other side say? Plan your answer to each.', 'List their strongest points, then your rebuttals.'], extra: ct }) +
      roles + K.box('Closing statement', { q: ['Why should the judges agree with your side? Plan your last sentence.', 'Sum up your best argument in two sentences.'], n: 2 }) + frames;
  },

  coach(b, K, c, r) {
    if (b === 'k2') {
      return K.box('I will teach', { extra: K.line('Friend:') + K.line('Skill:') }) +
        K.box('Show it', { q: ['Draw the skill.', 'Draw your friend doing it.'], draw: 1.6 }) +
        K.box('My tips', { q: 'Use one or two words, like "step" or "look".', extra: K.nums(2) }) +
        K.box('Try it', { extra: K.circ('Tries:', ['3', '5', '10']) + K.lines(1, 'Good tries:') }) +
        K.box('How did it go?', { extra: K.circ('Circle:', ['great', 'good', 'keep trying']) });
    }
    const stages = b === '912' ? ['cognitive (beginning: thinks about each step)', 'associative (practicing: fewer errors)', 'autonomous (automatic)']
      : ['beginner', 'getting better', 'skilled'];
    return K.box('Learner and skill', { extra: K.lineRow(['Learner:', 'Skill:']) + K.circ('Learning stage:', stages) }) +
      K.box('Cues', { q: ['Two to four words each, in the order of the movement.', 'Short, clear cues a learner can remember.', 'What should the learner think about, in order?'], extra: K.nums(3) }) +
      K.grid('1fr 1fr', [
        K.box('Drill setup', { q: ['Draw players, cones, targets and arrows.', 'Sketch the space and equipment.'], draw: 1.5 }),
        K.box('How it runs', { extra: K.nums(3) + K.line('Reps or time:') + (b === '35' ? '' : K.circ('Practice type:', ['blocked', 'random', 'variable'])) })]) +
      K.box('Feedback', { extra: K.line('Praise words:') + K.line('Fix-it cue:') + (b === '35' ? '' : K.line(b === '912' ? 'When and how often I give feedback:' : 'When I give feedback:')) }) +
      K.box('Success check', { extra: K.lines(1, ['Success is ___ out of ___ tries with', 'The learner is ready to move on when']) }) +
      K.box('After the session', { q: ['What did you see? What is the next step for the learner?', 'Which cue helped most? What will you change next time?'], n: 2 });
  },
};

// the little stage drawing: 9 areas (or back, middle, front for K-2), audience at the bottom
function stageSvg(b, small) {
  const W = 720, H = small ? (b === 'k2' ? 360 : 420) : b === 'k2' ? 300 : 360, top = 34, bot = H - 54, L = 70, R = W - 70;
  const fs = small ? 22 : 17;
  let s = `<rect x="${L}" y="${top}" width="${R - L}" height="${bot - top}" fill="none" stroke="#222" stroke-width="${small ? 4 : 3}"/>`;
  const rowsY = [top, top + (bot - top) / 3, top + 2 * (bot - top) / 3, bot];
  for (const y of rowsY.slice(1, 3)) s += `<line x1="${L}" y1="${y}" x2="${R}" y2="${y}" stroke="#999" stroke-width="2" stroke-dasharray="8 7"/>`;
  if (b === 'k2') {
    ['Back', 'Middle', 'Front'].forEach((t, i) => { s += `<text x="${L + 10}" y="${rowsY[i] + fs + 6}" font-size="${fs}" fill="#777">${t}</text>`; });
  } else {
    const colsX = [L, L + (R - L) / 3, L + 2 * (R - L) / 3, R];
    for (const x of colsX.slice(1, 3)) s += `<line x1="${x}" y1="${top}" x2="${x}" y2="${bot}" stroke="#999" stroke-width="2" stroke-dasharray="8 7"/>`;
    const names = [['USR', 'USC', 'USL'], ['SR', 'CS', 'SL'], ['DSR', 'DSC', 'DSL']];
    names.forEach((row, i) => row.forEach((t, j) => { s += `<text x="${colsX[j] + 10}" y="${rowsY[i] + fs + 6}" font-size="${fs}" fill="#777" font-weight="700">${t}</text>`; }));
  }
  const side = small ? 20 : 16;
  s += `<text x="${L / 2}" y="${(top + bot) / 2}" font-size="${side}" fill="#333" text-anchor="middle" transform="rotate(-90 ${L / 2} ${(top + bot) / 2})">STAGE RIGHT</text>`;
  s += `<text x="${W - L / 2}" y="${(top + bot) / 2}" font-size="${side}" fill="#333" text-anchor="middle" transform="rotate(90 ${W - L / 2} ${(top + bot) / 2})">STAGE LEFT</text>`;
  s += `<text x="${W / 2}" y="${top - 10}" font-size="${side}" fill="#333" text-anchor="middle">UPSTAGE (back)</text>`;
  s += `<text x="${W / 2}" y="${H - 12}" font-size="${side + 4}" fill="#222" text-anchor="middle" font-weight="700" letter-spacing="6">AUDIENCE</text>`;
  s += `<text x="${W / 2}" y="${bot + 20}" font-size="${side - 2}" fill="#555" text-anchor="middle">downstage (front)</text>`;
  return Gen.h.svg(W, H, s, b === 'k2' ? 'Stage plan with back, middle and front areas and the audience at the bottom' : 'Stage plan with nine areas from up stage right to down stage left and the audience at the bottom');
}

/* ---------- timing for the presentation planner: seconds per part that add up to the talk length ---------- */
function timing(form, n, T) {
  const parts = form === 'pitch' ? [['open', 1], ['pr', 1.2], ['so', 1.6], ['cu', 1], ['co', 1], ['ri', 1], ['close', 1]]
    : form === 'booktalk' ? [['open', 1], ['ab', 2.5], ['who', 1.2], ['close', 1]]
    : [['open', 1], ...Array.from({ length: n }, (_, i) => ['p' + i, 2]), ...(form === 'opinion' ? [['counter', 1.5]] : []), ['close', 1]];
  const sum = parts.reduce((a, p) => a + p[1], 0), out = {};
  let used = 0;
  parts.forEach(([k, w], i) => {
    const s = i === parts.length - 1 ? T - used : Math.max(5, Math.round(T * w / sum / 5) * 5);
    out[k] = s; used += s;
  });
  return out;
}

/* ---------- words for each kind ---------- */
const NAME = { research: 'Research Planner', present: 'Presentation Planner', slides: 'Slide Planner', storyboard: 'Storyboard', shotlist: 'Shot List',
  script: 'Script Page', counts: 'Count Sheet', stage: 'Stage Plan', art: 'Art Project Planner', matrix: 'Decision Matrix', interview: 'Interview Planner', debate: 'Debate Prep', coach: 'Coaching Plan' };
const ICAN = {
  research: ['I can ask a question and find out about it in a book.', 'I can plan research: a focused question, a search, sources with notes, and a citation for each.'],
  present: ['I can plan what I will say and show.', 'I can plan a talk with a clear opening, organized points, support, a strong close, and timing.'],
  slides: ['I can plan pictures and words in order.', 'I can plan each slide\'s picture, words and what I will say.'],
  storyboard: ['I can tell a story in pictures, in order.', 'I can plan a story shot by shot, with shots, action and sound.'],
  shotlist: ['I can plan the pictures I will take.', 'I can plan each shot and its timing before filming.'],
  script: ['I can write who talks and what they say and do.', 'I can write a script with speakers, lines and directions.'],
  counts: ['I can put dance moves on the counts 1 to 8.', 'I can write a dance phrase in counts so someone else can dance it.'],
  stage: ['I can show where people stand and move on a stage.', 'I can plan positions and moves on a stage using the stage areas.'],
  art: ['I can plan my art with ideas and sketches.', 'I can plan an artwork with choices, thumbnails and a reason for my final choice.'],
  matrix: ['I can pick using what matters most.', 'I can score options against criteria and use the totals to make a decision.'],
  interview: ['I can ask good questions and listen.', 'I can plan open questions and take notes in an interview.'],
  debate: ['I can tell what I think and give reasons.', 'I can prepare arguments with evidence and plan answers to the other side.'],
  coach: ['I can help a friend learn a skill.', 'I can plan a short practice that helps a partner improve one skill.'],
};
const DIR = {
  research: ['Write what you wonder. Find a book. Draw and write what you learned.', 'Fill in your questions and search plan first. Take notes from each source in your own words, then write the source list and plan your steps.'],
  present: ['Fill in what you will say and draw what you will show. Practice out loud.', 'Plan each part, word for word for the opening and closing. Use the suggested times, then practice and check it off.'],
  slides: ['Draw a picture and write a few words for each slide, in order.', 'Plan one idea per slide: a sketch, the words on the slide and what you will say.'],
  storyboard: ['Draw what happens in each box, in order. Write about it on the lines.', 'Sketch one shot in each frame, in order. Fill in the lines under each frame.'],
  shotlist: ['Draw each shot in order and tell what moves.', 'List every shot in the order you will film it, with its timing. Check off each shot when you get it.'],
  script: ['Write who talks, what they say and what they do on each line.', 'Fill in the scene first. Then write one line per row: who speaks, what they say, and the direction or cue.'],
  counts: ['Say the counts. Draw or write a move for each count. Then dance it.', 'Write your phrase one eight at a time. Fill each row across the counts, then dance it from the sheet.'],
  stage: ['Give each person a letter. Draw where they start and where they move.', 'Give each performer a letter. Mark start spots on the stage and draw each path with an arrow, then fill in the table.'],
  art: ['Write your idea, circle your choices, and sketch. Then pick your favorite.', 'Plan your idea and choices, sketch a different thumbnail in each box, then choose one and plan how to make it.'],
  matrix: ['Score each choice. Add across. Pick the one with the most points.', 'Fill in the options and criteria, score every box, add the totals, then decide and explain.'],
  interview: ['Write your questions. Ask them. Draw or write the answers.', 'Plan who and why, write open questions, then take notes during the interview and reflect after.'],
  debate: ['Tell what you think and draw two reasons.', 'Write the resolution and your side. Plan each argument with evidence, then plan rebuttals and roles.'],
  coach: ['Plan how you will help a friend learn a skill.', 'Plan the skill, cues, drill and feedback, run the session, then fill in what you saw.'],
};
const USE = {
  research: 'Use with any inquiry project; for primary grades, read the books aloud and let students draw their findings.',
  present: 'The timing chips are a suggested budget: the opening and closing are short and the points share the rest, adding up to the talk length you picked.',
  slides: 'Works for a slideshow, a pitch deck, a digital book or a poster series. Type slide titles to fill each slide\'s heading.',
  storyboard: 'Use for film, animation, stop-motion, comics and ASL or dance sequences. Type your own lines under the panels (for example Shot, Classifier, Facial expression).',
  shotlist: 'Turn a storyboard into a shot list or an animatic timing sheet. Type your own columns for B-roll, coverage or exposure-sheet details.',
  script: 'Works for a stage scene, puppet play, audio drama, podcast or animation script. Typed character names print at the top (and as choices to circle when there are 2 to 4).',
  counts: 'Type your own rows to make a canon or unison score (Dancer A, Dancer B, Dancer C) or a symbol phrase (Symbol, Level, Facing).',
  stage: 'Abbreviations follow the performer\'s point of view; some programs write UR, C and DL for USR, CS and DSL. The formation pages work for dance formations and spacing charts.',
  art: 'The bank changes with the focus: elements, color, principles, value or poster parts. Pair with a critique after the final piece.',
  matrix: 'Type the options and the criteria to fit any decision: designs, careers, energy sources, productions, research questions.',
  interview: 'Type question groups (for example tools, teamwork, training) to split the questions under headings. Practice with a partner before a guest visit.',
  debate: 'Speaking frames print in the language you pick; the planning labels stay in English.',
  coach: 'Pair students; the coach plans, runs the session, then switches roles. Works with any motor skill.',
};
const MISTAKES = {
  research: 'Copying whole sentences into notes; questions with one-word answers; forgetting to record where a fact came from.',
  present: 'Reading from the page; too many points for the time; skipping the practice timing.',
  slides: 'Too much text on a slide; slides that repeat the same idea; notes that just repeat the slide.',
  storyboard: 'Every panel the same distance and angle; missing the moment of change; detailed drawings that eat the time.',
  shotlist: 'Listing shots in story order when grouping by setup would save time; totals that do not match the target length.',
  script: 'Stage directions that describe feelings the actor cannot play; every line the same length; no change by the end.',
  counts: 'Eights that do not add up to 8 counts; moves written so loosely a partner cannot read them.',
  stage: 'Mixing up stage right and audience right; moves without a reason; performers blocking each other.',
  art: 'Thumbnails that are four copies of one idea; choosing without a reason; skipping the materials plan.',
  matrix: 'Scoring without agreeing what a 1 and a 5 mean; arithmetic slips in the totals; ignoring the weights.',
  interview: 'Yes-or-no questions; reading the next question instead of following up; not asking permission to quote.',
  debate: 'Opinions with no evidence; attacking people instead of points; rebuttals that only repeat the claim.',
  coach: 'Too many cues at once; general praise only; no clear success check.',
};
// filled-in models for the teacher page (sample topics)
const MODEL = {
  research: { topic: 'How do frogs survive the winter?', rows: [['Big question', 'How do frogs survive the winter?'], ['Smaller questions', '1. Where do frogs go in winter? 2. What happens to a frog\'s body in the cold? 3. Do all frogs do the same thing?'],
    ['Keywords', 'frogs, winter; synonyms: amphibians, hibernation, cold. Search string: frogs AND (hibernation OR winter)'], ['Source A notes', 'Many water frogs rest at the bottom of ponds; toads dig down below the frost line; wood frogs can partly freeze and thaw in spring.'],
    ['Plan', 'Questions by Monday, sources by Wednesday, notes by Friday, report next Wednesday.']] },
  present: { topic: 'Honeybees (3-minute informative talk)', rows: [['Opening', 'About one in three bites of food we eat depends on pollinators like bees. Here is why that matters.'], ['Point 1', 'Bees make honey from flower nectar. Visual: photo of a honeycomb.'],
    ['Point 2', 'Bees pollinate many fruits and vegetables. Visual: an apple blossom.'], ['Point 3', 'A hive has one queen and thousands of workers. Transition: "So what can we do to help?"'], ['Closing', 'Plant flowers bees like, such as clover and lavender.']] },
  slides: { topic: 'Our field day', rows: [['Slide 1', 'Title: Field Day! Sketch: our class on the field. Say: "Here is our best day of the year."'], ['Slide 2', 'Sack race. Words: "Hop, hop, hop!"'],
    ['Slide 3', 'Water relay. Words: "Do not spill!"'], ['Slide 4', 'What we learned. Words: "Teamwork wins." Say: "We cheered for every team."']] },
  storyboard: { topic: 'The lost puppy', rows: [['1', 'WS, eye level: a park; a puppy runs off. Sound: barking, kids laughing.'], ['2', 'CU: Rosa\'s worried face. Sound: "Biscuit? Biscuit!"'],
    ['3', 'MS, low angle: Rosa looks under a slide. Sound: footsteps.'], ['4', 'POV: a wagging tail behind a bush. Sound: soft whine.'], ['5', 'MS: Rosa hugs the puppy. Sound: happy music.']] },
  shotlist: { topic: 'Morning at school (12 frames per second)', rows: [['1', 'WS, bus pulls up; camera on a tripod by the gate; 36 frames = 3 seconds'], ['2', 'MS, kids walk in; same setup; 24 frames = 2 seconds'],
    ['3', 'CU, the bell; new setup by the door; 12 frames = 1 second'], ['Total', '72 frames = 6 seconds']] },
  script: { topic: 'The lost library book', rows: [['1', 'MAYA: (looking under the desk) It was right here!'], ['2', 'OMAR: (crossing to the shelf) Did you check the return cart?'],
    ['3', 'MAYA: (slumping) Twice. It is due today.'], ['4', 'OMAR: (holding up a book) Is this it? It was in my bag the whole time.'], ['Turn', 'Line 4: the problem is solved, and Maya has to decide whether to be upset.']] },
  counts: { topic: 'Spring phrase (16 counts)', rows: [['Eight 1', '1-4 walk forward; 5-6 turn right; 7-8 hold. Level: middle, then low on 7-8.'], ['Eight 2', '1-2 rise to high; 3-4 reach up; 5-8 sideways slide to the left, accent on 8.'],
    ['Change', 'Eight 2 changes level (low to high) and direction (forward to sideways).']] },
  stage: { topic: 'Scene with three actors', rows: [['Start', 'A at USL, B at CS, C at DSR.'], ['Move 1', 'A crosses from USL to DSC on "Wait!" Why: to stop B from leaving.'],
    ['Move 2', 'B turns from CS to face A, then sits. Why: B gives in and listens.'], ['Move 3', 'C exits SR on "Fine." Why: C is angry and wants to be alone.']] },
  art: { topic: 'Under the sea (color focus)', rows: [['Idea', 'A calm underwater scene with a sea turtle.'], ['Scheme', 'Cool colors: blue, green and purple, because cool colors feel calm.'],
    ['Thumbnails', '1 turtle in the center; 2 turtle low with tall seaweed; 3 close-up of the turtle\'s face.'], ['Choice', 'Number 2: the tall seaweed leads the eye down to the turtle.']] },
  matrix: { topic: 'How should our class travel to the museum?', rows: [] },
  interview: { topic: 'A longtime neighbor', rows: [['1', 'What did this street look like when you moved here? Follow-up: What store or place do you miss most?'], ['2', 'How has the school changed? Follow-up: Why do you think it changed?'],
    ['3', 'Tell me about a big event in town you remember. Follow-up: How did people help each other?'], ['After', 'Surprise: there used to be a train station two blocks away.']] },
  debate: { topic: 'Phones should be put away during lunch', rows: [['Claim 1', 'Phone-free lunch helps students talk with each other.'], ['Evidence', 'Our class survey (cite your own data or a source you found).'],
    ['They might say', 'Students need phones for emergencies.'], ['Our rebuttal', 'Phones stay in bags, not taken away, so families can still reach students.']] },
  coach: { topic: 'Overhand throw', rows: [['Cues', '1. Side to target. 2. Step with the opposite foot. 3. Follow through across your body.'], ['Drill', 'Partner throws at a wall target from 3 meters; 10 throws, then switch.'],
    ['Feedback', 'Praise: "Great step!" Fix-it cue: "Opposite foot."'], ['Success', '7 out of 10 throws with a step on the opposite foot.']] },
};
// the matrix model is worked out here so the totals are right
function matrixModel() {
  const crit = [['Cost', 1], ['Time', 2], ['Safety', 3]];
  const opts = [['Bus', [4, 5, 5]], ['Walk', [5, 2, 4]], ['Bike', [5, 4, 3]]];
  const rows = [['Weights', crit.map(([c, w]) => `${c} ${w}`).join(', ')]];
  let best = null;
  for (const [o, sc] of opts) {
    const tot = sc.reduce((a, s, i) => a + s * crit[i][1], 0);
    rows.push([o, `scores ${sc.join(', ')}; weighted ${sc.map((s, i) => `${s} × ${crit[i][1]}`).join(' + ')} = ${tot}`]);
    if (!best || tot > best[1]) best = [o, tot];
  }
  rows.push(['Decision', `${best[0]} has the highest total (${best[1]}), mostly because safety has the biggest weight.`]);
  return rows;
}
MODEL.matrix.rows = matrixModel();
function modelHtml(m) {
  return `<h3>Model: ${esc(m.topic)}</h3><p>A filled-in example for a sample topic. Show it after students try, or fill part of it with the class.</p>` +
    `<table class="ws-table pf-model"><tbody>${m.rows.map(([k, v]) => `<tr><th>${esc(k)}</th><td>${esc(v)}</td></tr>`).join('')}</tbody></table>`;
}

const CSS = `
.pf { margin-top: 2px; }
.pf-grid { display: grid; gap: .1in; margin: .06in 0; }
.pf-grid > .pf-box { margin: 0; }
.pf-box { border: 1.5px solid #222; border-radius: 8px; padding: .05in .1in .07in; break-inside: avoid; margin: .07in 0; background: #fff; }
.pf-head { margin: 0 0 2px; line-height: 1.3; }
.pf-lab { font: 700 12.5px/1.3 var(--sans); text-transform: uppercase; letter-spacing: .06em; margin-right: 4px; }
.pf-q { font-size: 12.5px; color: #444; font-style: italic; }
.pf-lines span { display: block; height: var(--lh); border-bottom: 1px solid #888; position: relative; }
.pf-lines span i { position: absolute; left: 0; bottom: 2px; font-size: 12px; color: #555; white-space: nowrap; }
.pf-k2 .pf-lines span::after { content: ''; position: absolute; left: 0; right: 0; top: 50%; border-top: 1px dashed #bbb; }
.pf-k2 .pf-lines span i { font-size: 15px; }
.pf-k2 .pf-lab { font-size: 16px; text-transform: none; letter-spacing: 0; }
.pf-k2 .pf-q { font-size: 14px; }
.pf-draw { border: 1px dashed #888; border-radius: 6px; margin: 4px 0 2px; position: relative; }
.pf-draw span { position: absolute; left: 6px; top: 3px; font-size: 10.5px; color: #888; }
.pf-line { display: flex; align-items: flex-end; gap: 5px; margin: 0; min-height: .3in; font-size: 12.5px; }
.pf-line b { font-weight: 600; white-space: nowrap; }
.pf-line span { flex: 1; border-bottom: 1px solid #888; height: 1.1em; }
.pf-k2 .pf-line { font-size: 15px; min-height: .42in; }
.pf-linerow { display: flex; gap: .2in; }
.pf-linerow .pf-line { flex: 1; }
.pf-circ { margin: 3px 0; font-size: 12.5px; line-height: 1.7; }
.pf-circ b { font-weight: 600; margin-right: 4px; }
.pf-circ span { display: inline-block; margin-right: 12px; }
.pf-k2 .pf-circ { font-size: 15px; }
.pf-checks { display: flex; flex-wrap: wrap; gap: 4px 16px; margin: 4px 0; font-size: 12.5px; }
.pf-checks i, .pf-cb { display: inline-block; width: .95em; height: .95em; border: 1.5px solid #333; border-radius: 2px; vertical-align: -2px; }
.pf-k2 .pf-checks { font-size: 15px; gap: 6px 22px; }
.pf-nums { margin: 2px 0 0; padding-left: 1.4em; font-size: 12.5px; }
.pf-nums li span { display: block; height: var(--lh); border-bottom: 1px solid #888; }
.pf-k2 .pf-nums { font-size: 15px; }
.pf-tab { width: 100%; border-collapse: collapse; margin: 3px 0 .06in; table-layout: fixed; }
.pf-tab th { font: 700 11.5px/1.2 var(--sans); padding: 3px 4px; border: 1.5px solid #222; background: #eee; text-align: center; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pf-k2 .pf-tab th { font-size: 14px; }
.pf-tab td { border: 1px solid #555; padding: 2px 4px; font-size: 12px; vertical-align: middle; }
.pf-tab td:first-child { text-align: center; font-weight: 600; }
.pf-tab tr.pf-ex td { height: auto !important; padding: 3px 4px; color: #444; font-size: 11.5px; background: #f6f6f6; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pf-k2 .pf-tab tr.pf-ex td { font-size: 13px; }
.pf-tab tr.pf-total td, .pf-tab tr.pf-weight td { border-top: 2px solid #222; font-size: 11.5px; }
.pf-tab tr.pf-weight td { border-top: 1px solid #555; border-bottom: 2px solid #222; background: #f6f6f6; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pf-matrix td:first-child, .pf-script td:nth-child(2) { text-align: left; }
.pf-matrix td { text-align: center; white-space: nowrap; }
.pf-sc { display: inline-block; width: .3in; height: .22in; border-bottom: 1px solid #555; }
.pf-x { font-size: 11px; color: #555; margin: 0 2px; }
.pf-counts td:first-child { text-align: left; font-size: 11.5px; }
.pf-counts th:first-child { text-align: left; }
.pf-and { color: #777; font-weight: 400; }
.pf-eight { margin: .06in 0 0; }
.pf-tip { margin: 0 0 3px; font-size: 13px; }
.pf-k2 .pf-tip { font-size: 14.5px; }
.pf-small { margin: 3px 0; font-size: 12px; color: #333; }
.pf-k2 .pf-small { font-size: 14px; }
.pf-example { margin: 4px 0; font-size: 12.5px; border-left: 3px solid #999; padding-left: 8px; }
.pf-pattern { margin: 2px 0 4px; font-size: 12px; background: #f3f3f3; padding: 3px 6px; border-radius: 4px; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pf-cite { display: grid; grid-template-columns: .25in 1fr; align-items: end; }
.pf-src { margin: 2px 0 6px; }
.pf-time { font: 600 10.5px var(--sans); text-transform: none; letter-spacing: 0; border: 1px solid #555; border-radius: 10px; padding: 0 6px; margin-left: 6px; color: #333; vertical-align: 1px; }
.pf-board { gap: .1in; }
.pf-panel { break-inside: avoid; }
.pf-ph { margin: 0 0 2px; font-size: 12.5px; display: flex; gap: 6px; align-items: baseline; }
.pf-ph b { display: inline-grid; place-items: center; min-width: 1.5em; height: 1.5em; border: 1.5px solid #222; border-radius: 50%; font-size: 11.5px; }
.pf-k2 .pf-ph { font-size: 15px; }
.pf-sec { margin-left: auto; font-size: 11px; color: #555; }
.pf-frame { border: 2px solid #222; border-radius: 3px; margin-bottom: 3px; }
.pf-thumb { border-width: 1.5px; }
.pf-side .pf-sidegrid { display: grid; grid-template-columns: 1.15fr 1fr; gap: .12in; align-items: end; }
.pf-key { border: 1px solid #888; border-radius: 6px; padding: 3px 8px; margin: .06in 0; font-size: 12px; }
.pf-sect { margin: .1in 0 2px; font: 700 12.5px/1.3 var(--sans); text-transform: uppercase; letter-spacing: .06em; }
.pf-k2 .pf-sect { font-size: 16px; text-transform: none; letter-spacing: 0; }
.pf-key p { margin: 1px 0; }
.pf-swatches { display: flex; flex-wrap: wrap; gap: .12in; margin: 4px 0; }
.pf-swatches div { text-align: center; font-size: 11px; color: #444; }
.pf-swatches b { display: block; border-bottom: 1px solid #888; height: 1.1em; }
.pf-swatches i { display: block; width: .62in; height: .45in; border: 1.5px solid #222; border-radius: 3px; }
.pf-k2 .pf-swatches i { width: .8in; height: .5in; }
.pf-names span { display: inline-block; margin-right: 8px; font-size: 11.5px; }
.pf-k2 .pf-names span { font-size: 13px; }
.pf-stagebig { margin: .04in auto; text-align: center; }
.pf-stagebig svg { width: 100%; }
.pf-board svg { width: 100%; }
.pf-qb { margin: 4px 0 6px; break-inside: avoid; }
.pf-qline { display: flex; gap: 6px; align-items: flex-end; margin: 0; min-height: .32in; font-size: 13px; }
.pf-qline span { flex: 1; border-bottom: 1.5px solid #222; height: 1.1em; }
.pf-qk { margin: 3px 0 5px; break-inside: avoid; }
.pf-qk p { display: flex; gap: 6px; align-items: flex-end; margin: 0; font-size: 16px; min-height: .44in; }
.pf-qk .pf-fill { flex: 1; border-bottom: 1.5px solid #222; height: 1.1em; }
.pf-start { font-weight: 700; }
.pf-group { margin: .08in 0 0; font: 700 12px var(--sans); text-transform: uppercase; letter-spacing: .06em; border-bottom: 1.5px solid #222; }
.pf-frames { columns: 2; margin: 2px 0; padding-left: 1.2em; font-size: 12.5px; }
.pf-k2 .pf-frames { font-size: 14px; }
.pf-model th { text-align: left; white-space: nowrap; width: 1%; vertical-align: top; }
.pf-model td { text-align: left; }
`;

Gen.add('project-frames', {
  title: 'Project Frames', type: 'Planner', noKey: true, css: CSS,
  fields: [
    { id: 'kind', label: 'Kind of page', type: 'select', options: KINDS, def: 'research' },
    { id: 'band', label: 'Grade band', type: 'select', options: BANDS, def: '35' },
    { id: 'topic', label: 'Topic or title (optional)', type: 'text', def: '' },
    { id: 'form', label: 'Kind of talk', type: 'select', options: [['report', 'Informative talk'], ['opinion', 'Opinion speech'], ['pitch', 'Pitch (problem to the ask)'], ['booktalk', 'Book talk']], def: 'report', show: v => v.kind === 'present' },
    { id: 'count', label: 'How many', type: 'select', options: v => (COUNT[v.kind] ? COUNT[v.kind][v.band === 'k2' ? 'k2' : 'd'] : ['3']).map(c => [c, COUNT[v.kind] ? countLabel(v.kind, c) : c]), def: '3',
      show: v => v.kind !== 'coach' && !(v.kind === 'present' && (v.form === 'pitch' || v.form === 'booktalk')) },
    { id: 'mins', label: 'Talk length', type: 'select', options: [['1', '1 minute'], ['2', '2 minutes'], ['3', '3 minutes'], ['5', '5 minutes']], def: '3', show: v => v.kind === 'present' && v.band !== 'k2' },
    { id: 'titles', label: 'Slide titles, comma separated: Problem, Solution, Team', type: 'text', def: '', show: v => v.kind === 'slides' },
    { id: 'lines', label: 'Lines under each panel, comma separated: Shot, Action, Sound', type: 'text', def: '', show: v => v.kind === 'storyboard' && v.band !== 'k2' },
    { id: 'key', label: 'Print the shot or symbol key', type: 'check', def: true, show: v => v.kind === 'storyboard' || v.kind === 'counts' },
    { id: 'timing', label: 'Timing column', type: 'select', options: [['sec', 'Seconds'], ['12', 'Frames at 12 per second'], ['24', 'Frames at 24 per second']], def: 'sec', show: v => v.kind === 'shotlist' },
    { id: 'cols', label: 'Your own columns, comma separated: Shot type, What moves, Camera', type: 'text', def: '', show: v => v.kind === 'shotlist' },
    { id: 'cue', label: 'Third column', type: 'select', options: [['stage', 'Stage direction (play)'], ['sound', 'Sound or music cue (audio, podcast)'], ['action', 'Action (film, animation)']], def: 'stage', show: v => v.kind === 'script' },
    { id: 'names', label: 'Characters, comma separated: Mia, Leo', type: 'text', def: '', show: v => v.kind === 'script' },
    { id: 'layers', label: 'Rows under each count, comma separated: Move, Level, Dancer A', type: 'text', def: '', show: v => v.kind === 'counts' && v.band !== 'k2' },
    { id: 'ands', label: 'Add the & counts between beats', type: 'check', def: false, show: v => v.kind === 'counts' && v.band !== 'k2' },
    { id: 'focus', label: 'Focus', type: 'select', options: [['elements', 'Elements (line, shape, color, texture)'], ['color', 'Color scheme and swatches'], ['principles', 'Principles of design'], ['value', 'Value and perspective'], ['poster', 'Poster or ad (message, slogan, audience)'], ['none', 'Open (no bank)']], def: 'elements', show: v => v.kind === 'art' },
    { id: 'crit', label: 'Criteria, comma separated: cost, safety, fun', type: 'text', def: '', show: v => v.kind === 'matrix' },
    { id: 'opts', label: 'Options being scored, comma separated: bike, bus, walk', type: 'text', def: '', show: v => v.kind === 'matrix' },
    { id: 'weights', label: 'Weighted criteria (score × weight)', type: 'check', def: false, show: v => v.kind === 'matrix' && v.band !== 'k2' },
    { id: 'groups', label: 'Question groups, comma separated: tools, teamwork, training', type: 'text', def: '', show: v => v.kind === 'interview' && v.band !== 'k2' },
    { id: 'lang', label: 'Speaking frames in', type: 'select', options: [['en', 'English'], ['es', 'Spanish'], ['fr', 'French']], def: 'en', show: v => v.kind === 'debate' },
  ],
  make(v, r) {
    const b = v.band, kind = v.kind, topic = String(v.topic || '').trim();
    const K = kit(b, r);
    const c = {
      count: String(v.count), form: v.form, mins: String(v.mins), key: !!v.key, ands: !!v.ands, weights: !!v.weights,
      titles: list(v.titles, 8, 28), lines: list(v.lines, 4, 22), cols: list(v.cols, 5, 24), names: list(v.names, 8, 18), layers: list(v.layers, 5, 18),
      crit: list(v.crit, 6, 22), opts: list(v.opts, +v.count || 6, 24), groups: list(v.groups, 5, 28), cue: v.cue, focus: v.focus, lang: v.lang, tcol: v.timing,
    };
    const fixedForm = kind === 'present' && (v.form === 'pitch' || v.form === 'booktalk');
    if (kind === 'present' && b !== 'k2') c.timing = timing(v.form, +c.count, +c.mins * 60);
    if (kind === 'shotlist') c.fx = r.int(2, 6);
    if (kind === 'matrix') c.ex = { s: r.int(2, 5), w: r.int(2, 3), list: Array.from({ length: 3 }, () => r.int(1, 5)) };
    const body = BUILD[kind](b, K, c, r);
    let name = NAME[kind];
    if (kind === 'present') name = { report: 'Presentation Planner', opinion: 'Speech Planner', pitch: 'Pitch Planner', booktalk: 'Book Talk Planner' }[v.form];
    if (kind === 'stage' && c.count[0] === 'f') name = 'Formations Plan';
    if (kind === 'art' && v.focus === 'poster') name = 'Poster Planner';
    const short = topic && topic.length <= 44;
    const title = short ? `${name}: ${topic}` : name;
    const topicLine = topic && !short ? `<p class="pf-tip"><b>Topic:</b> ${esc(topic)}</p>` : '';
    const yo = young(b) ? 'y' : 'o';
    const band = BANDS.find(x => x[0] === b)[1];
    const html = `<div class="pf pf-${b}">${topicLine}${K.tip(TIPS[kind][yo])}${body}</div>`;
    const mats = { storyboard: 'pencil, ruler', shotlist: 'pencil, your storyboard', counts: 'pencil, music', stage: 'pencil, colored pencils for paths', art: 'pencil, eraser, colored pencils or paint for swatches',
      matrix: 'pencil' + (c.weights ? ', calculator (optional)' : ''), research: 'pencil, your sources', coach: 'pencil, equipment for the drill' }[kind] || 'pencil';
    const sheet = {
      title, eyebrow: 'Project frame · ' + KNAME[kind], level: band,
      ican: ICAN[kind][b === 'k2' ? 0 : 1],
      directions: kind === 'stage' && c.count[0] === 'f' ? (b === 'k2' ? 'Give each person a letter. Draw where they stand in each picture and an arrow for how they move.'
        : 'Give each performer a letter. Draw each formation with the letters, add arrows for the paths, and write how the group gets to the next one.') : DIR[kind][b === 'k2' ? 0 : 1],
      minutes: { research: 30, present: 25, slides: 25, storyboard: 30, shotlist: 20, script: 30, counts: 25, stage: 20, art: 35, matrix: 20, interview: 20, debate: 30, coach: 20 }[kind],
      materials: mats + (b === 'k2' && !/crayons/.test(mats) ? ', crayons' : ''),
      parts: [['', html]], items: [],
      mistakes: MISTAKES[kind],
      notes: `${USE[kind]} The tip and some prompts change with each New sheet, so neighbors can get different wording of the same frame.${fixedForm ? ' A pitch and a book talk have set parts, so the number of points does not apply.' : ''}`,
      teacher: modelHtml(MODEL[kind]),
    };
    if (c.timing) sheet.timing = { parts: c.timing, total: +c.mins * 60 };
    if (c.ex) sheet.ex = c.ex;
    if (c.fx) sheet.fx = { f: c.fx, fps: +v.timing || 0 };
    return sheet;
  },
  // nothing to answer; check the worked numbers the sheet prints (timing budget, the scoring example, frames to seconds)
  verify(s, v) {
    const bad = [];
    if (s.timing) {
      const vals = Object.values(s.timing.parts);
      let sum = 0; for (const x of vals) sum += x;
      if (sum !== s.timing.total) bad.push(`timing parts add to ${sum}, not ${s.timing.total}`);
      if (vals.some(x => !(x > 0) || x % 5)) bad.push('a timing part is not a positive multiple of 5 seconds');
      const html = s.parts[0][1];
      for (const x of vals) if (!html.includes(`about ${Math.floor(x / 60)}:${String(x % 60).padStart(2, '0')}`)) bad.push(`timing ${x} not printed`);
    }
    if (s.ex && v.kind === 'matrix' && v.band !== 'k2') {
      const html = s.parts[0][1];
      if (v.weights) { let p = 0; for (let i = 0; i < s.ex.w; i++) p += s.ex.s; if (!html.includes(`= ${p}.`)) bad.push('weighted example product wrong'); }
      else { let t = 0; s.ex.list.forEach(x => { t += x; }); if (!html.includes(`total of ${t}.`)) bad.push('example total wrong'); }
    }
    if (s.fx && s.fx.fps) {
      const html = s.parts[0][1], { f, fps } = s.fx;
      let frames = 0; for (let i = 0; i < f; i++) frames += fps;
      if (!html.includes(`Example: ${frames} frames ÷ ${fps} = ${f} seconds`)) bad.push('frames example wrong');
    }
    return bad;
  },
});
})();
