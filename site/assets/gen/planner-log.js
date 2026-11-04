// Planners, Logs and Reflections, K-12. A layout generator: no computed answers (noKey). Pick a kind (project planner, reading
// log, practice log, science observation log, weekly reflection, exit reflection, goal setting) and a grade band; the band sets
// the layout, the size of the writing space and the wording. Prompts come from banks, so New sheet gives fresh ones.
// Also a design and engineering planner (problem, criteria, constraints, three ideas, chosen idea with a labeled sketch,
// materials, test plan, results, improve) and a trial, week, day, session or rehearsal log: a table with 3 to 12 numbered
// entries (10 at most for K-2) and a summary, with the teacher's own typed columns in place of the middle ones if given.
(() => {
const { esc } = Gen.h;

const BANDS = [['k2', 'Grades K-2'], ['35', 'Grades 3-5'], ['68', 'Grades 6-8'], ['912', 'Grades 9-12']];
const KINDS = [['project', 'Project planner'], ['reading', 'Reading log'], ['practice', 'Practice log'], ['science', 'Science observation log'],
  ['weekly', 'Weekly reflection'], ['exit', 'Exit reflection (2 slips)'], ['goal', 'Goal setting'], ['design', 'Design and engineering planner'], ['trial', 'Trial, week or day log']];
const LH = { k2: 0.44, 35: 0.34, 68: 0.3, 912: 0.28 };
const RH = { k2: 0.5, 35: 0.4, 68: 0.36, 912: 0.34 };
const GROW = /*GROW*/{"project-k2":1.03,"project-35":0.92,"project-68":0.76,"project-912":0.7,"reading-k2":1.15,"reading-35":1.16,"reading-68":1.17,"reading-912":1.13,"practice-k2":1.19,"practice-35":1.39,"practice-68":1.39,"practice-912":1.51,"science-k2":1.19,"science-35":1.15,"science-68":1.05,"science-912":0.99,"weekly-k2":1.3,"exit-k2":1.18,"goal-k2":1.29,"goal-35":0.95,"weekly-35":0.96,"exit-35":1.09,"exit-68":1.09,"exit-912":1.1,"goal-68":0.83,"weekly-68":2.15,"weekly-912":2.15,"goal-912":0.71,"design-k2":.78,"design-35":.68,"design-68":.64,"design-912":.66,"trial-k2":1,"trial-35":1,"trial-68":1,"trial-912":1}/*GROW*/;   // per kind and band: stretch the writing space to fill the page (tuned by print tests)
const DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

/* ---------- prompt banks ---------- */
const P = {
  read_k2: ['Draw your favorite part. Write about it.', 'Who was your favorite character? Why?', 'What happened at the end?', 'Would you tell a friend to read it? Why?',
    'What did the book make you think of?', 'Draw where the story happens. Tell about it.', 'What was the problem in the story?', 'What new thing did you learn?'],
  read_35: ['What is the main character trying to do? What is in the way?', 'Which part surprised you? Why?', 'What do you predict will happen next? What clues helped you?',
    'What lesson could a reader learn from this book?', 'Pick a new word you read. What do you think it means? What helped you figure it out?', 'How did a character change? What made them change?',
    'Nonfiction: what are two facts you learned, and which one surprised you?', 'What question would you ask the author?', 'Which character are you most like? Why?', 'Describe the setting. How does it matter to the story?'],
  read_68: ['How does the setting shape what happens?', 'What theme is developing? Which details support it?', 'Copy a sentence that stands out (with the page). Why does it matter?',
    'How does the author build suspense or tension?', 'Compare a character now with the same character at the start.', 'Who tells the story? How would it change from another point of view?',
    'What is the author\'s purpose in this section? How do you know?', 'Connect the reading to another text, a current event, or your life.', 'What conflict drives this section? Is it internal or external?', 'Nonfiction: what is the central idea, and how does the author support it?'],
  read_912: ['How does the author use structure (order, flashback, pacing) to create meaning?', 'Trace a motif or symbol. What does it suggest so far?', 'Analyze one word choice. How does it shape tone?',
    'What perspective or assumption does the text challenge?', 'How does a minor character shed light on a major one?', 'Nonfiction: evaluate the author\'s reasoning and evidence. Where is it strongest or weakest?',
    'What is left unsaid? Why might the author leave it out?', 'How does the historical or cultural context shape the text?', 'Where does the narrator seem unreliable or limited? What tells you?', 'Pose an interpretive question you cannot yet answer. What evidence points each way?'],
  prac_k2: ['What did you get better at?', 'What was fun?', 'What was tricky?', 'Who did you show what you can do?', 'What do you want to try next?',
    'Draw yourself practicing. What are you doing?', 'What will you practice tomorrow?', 'Who helped you practice?'],
  prac_35: ['What got easier this week?', 'What is still tricky? What will you try?', 'Which practice day went best? Why?', 'What is one goal for next week?',
    'What did a coach, teacher or video teach you?', 'What did you do when you got stuck?'],
  prac_old: ['Which specific skill did you isolate this week?', 'What feedback did you get, and what did you change?', 'Where did you make the most mistakes? What pattern do you see?',
    'Set a measurable goal for next week.', 'How did you practice the hardest part slowly or in small pieces?', 'Compare your first and last sessions: what improved, and how do you know?',
    'What would you tell a beginner about practicing this skill?', 'When was your focus best? What helped?'],
  sci_k2: ['What changed?', 'What stayed the same?', 'What do you wonder now?', 'What do you think will happen next?'],
  sci_35: ['What patterns do you notice?', 'What changed the most? What stayed the same?', 'What do you predict will happen next? Why?', 'What new questions do you have?', 'What surprised you?'],
  sci_old: ['What patterns or trends appear in the data?', 'Which observations do not fit the pattern? What might explain them?', 'What new questions does this raise?',
    'What would you change about how you collected data?', 'What do the data suggest so far? How confident are you?', 'What might you be missing or measuring wrong?'],
  wk_k2: ['This week I learned', 'I am proud of', 'Something hard was', 'I helped someone by', 'My favorite thing this week was', 'Next week I will'],
  wk_35: ['What is the most important thing you learned this week?', 'What are you proud of? Why?', 'What was hard? What did you do about it?', 'Who helped you, or whom did you help?',
    'What would you do differently if you could redo this week?', 'What question do you still have?', 'Which subject or activity went best? Why?', 'What is one goal for next week?'],
  wk_old: ['What is the most important idea you learned this week, and why does it matter?', 'Where did you struggle? What strategy did you use?', 'What feedback did you get, and how will you use it?',
    'What work are you proudest of this week? What made it good?', 'How well did you manage your time? What will you change?', 'What connections did you make between classes or to life outside school?',
    'What question is still on your mind?', 'Who did you work with, and how did it go?'],
  ex_k2: ['Today I learned', 'One thing I can do now is', 'I still wonder', 'My favorite part was', 'A word I learned is'],
  ex_35: ['What is one thing you learned today?', 'What is still confusing?', 'Explain today\'s big idea to a friend in one or two sentences.', 'Give an example of what we learned today.',
    'What question do you still have?', 'How could you use what you learned outside school?', 'What helped you learn today?'],
  ex_old: ['Summarize today\'s key idea in your own words.', 'What is one thing you are still unsure about?', 'How does today\'s lesson connect to something we learned before?',
    'Write one question you could answer now that you could not answer before class.', 'Where might you use this idea outside this class?', 'What would you want reviewed next time?',
    'Which part of today\'s work was most useful? Why?', 'Give an example of today\'s idea that was not in the lesson.'],
  chk_35: [['What is going well?', 'What do we do next?'], ['What did we finish?', 'What is in the way?'], ['How is it going?', 'What help do we need?']],
  chk_old: [['Progress since last check-in', 'Problem or risk', 'Next step'], ['What we finished', 'What is blocking us', 'Plan before next check-in'], ['Progress', 'Question for the teacher', 'Next step']],
  goal_why: ['Why does this goal matter to you?', 'How will reaching this goal help you?', 'Why did you choose this goal?'],
  goal_block: ['What might get in your way? What will you do then?', 'What could make this hard? What is your plan?', 'If you get stuck, what will you do?'],
  goal_help: ['Who can help you? How?', 'Who will you tell about your goal?', 'What tools or people will help?'],
  des_prob_y: ['What is the problem? Who needs it solved?', 'What needs to be made or fixed, and for whom?', 'What are you trying to solve?'],
  des_prob_o: ['Define the problem: who has it, what they need, and why it matters.', 'What problem are you solving, and for whom?', 'State the problem without naming a solution yet.'],
  des_crit: ['What must it do to be a success?', 'List what a good solution has to do.', 'How will you know it works?'],
  des_con_y: ['What limits do you have? (time, materials, size, cost)', 'What can you not use or do?'],
  des_con_o: ['Limits on materials, time, size, cost or safety.', 'What rules, budget or materials limit your design?'],
  des_why: ['Why this idea? How does it meet the criteria?', 'Which criteria does it meet best? What is the trade-off?', 'What made you choose this one over the others?'],
  des_test: ['What will you measure, and in what units?', 'What will you count, time or measure?', 'What result would show the design works?'],
  des_how: ['How will you test it? Steps, number of trials, what stays the same.', 'Describe the test so someone else could repeat it.', 'How many trials? What will you keep the same each time?'],
  des_res_y: ['What happened when you tested it?', 'Did it work? What did you see or measure?'],
  des_res_o: ['Record what you measured. Did it meet each criterion?', 'Results, with numbers. Which criteria did it meet? Which did it miss?'],
  des_imp_y: ['What would you change to make it better?', 'What will you try next time?'],
  des_imp_o: ['What would you change, and why? What would you test next?', 'Name one improvement and the evidence that it would help.', 'What failed, and what is your next version?'],
  tri_sum_y: ['What did you find out?', 'What changed from the first one to the last?', 'What happened most of the time?'],
  tri_sum_o: ['What pattern do you see across the entries?', 'Compare the first and last entries: what changed, and why?', 'What do the results suggest? What is still unclear?', 'Which entry stands out? What was different that time?'],
  tri_next_y: ['What will you try next?', 'What would you do differently?', 'What do you wonder now?'],
  tri_next_o: ['What would you change next time, and why?', 'What is one thing you would keep the same and one you would change?', 'What should the next test or week look like?'],
};
const WK_FEEL = ['happy', 'proud', 'tired', 'excited', 'worried', 'calm', 'curious', 'frustrated'];

/* ---------- building blocks ---------- */
function kit(b, g) {
  const lh = LH[b], rh = RH[b] * g;
  const lines = (h, starter) => { const n = Math.max(1, Math.round(h * g / lh));
    return `<div class="pl-lines" style="--lh:${lh}in">${Array.from({ length: n }, (_, i) => `<span>${i === 0 && starter ? `<i>${esc(starter)}</i>` : ''}</span>`).join('')}</div>`; };
  const box = (lab, q, o = {}) => `<div class="pl-box${o.cls ? ' ' + o.cls : ''}"><p class="pl-head">${lab ? `<span class="pl-lab">${esc(lab)}</span> ` : ''}${q ? `<span class="pl-q">${esc(q)}</span>` : ''}</p>` + (o.pre || '') +
    (o.draw ? `<div class="pl-draw" style="height:${(o.draw * g).toFixed(2)}in"></div>` : '') + (o.extra || '') + (o.h ? lines(o.h, o.st) : '') + '</div>';
  const grid = (cols, cells) => `<div class="pl-grid" style="grid-template-columns:${cols}">${cells.join('')}</div>`;
  const field = (lab, w) => `<span class="pl-field"><b>${esc(lab)}</b><span style="${w ? `width:${w}` : 'flex:1'}"></span></span>`;
  const fields = (...fs) => `<p class="pl-fields">${fs.join('')}</p>`;
  const table = (cols, n, o = {}) => `<table class="pl-tab"><thead><tr>${cols.map(([l, w]) => `<th${w ? ` style="width:${w}"` : ''}>${esc(l)}</th>`).join('')}</tr></thead><tbody>` +
    Array.from({ length: n }, (_, i) => `<tr style="height:${((o.rh || 1) * rh).toFixed(2)}in">${cols.map((c, j) => `<td>${o.fill ? (o.fill(i, j) || '') : ''}</td>`).join('')}</tr>`).join('') +
    (o.total ? `<tr class="pl-total">${cols.map((c, j) => `<td>${j === 0 ? 'Total' : ''}</td>`).join('')}</tr>` : '') + '</tbody></table>';
  const scale = (lab, opts) => `<p class="pl-scale"><b>${esc(lab)}</b> ${opts.map(o => `<span><i></i>${esc(o)}</span>`).join('')}</p>`;
  return { lines, box, grid, field, fields, table, scale, lh, g };
}
const sec = t => `<p class="pl-sec">${esc(t)}</p>`;

/* ---------- each kind ---------- */
const BUILD = {
  project(b, r, K, topic) {
    const head = K.fields(K.field(b === 'k2' ? 'We are making:' : 'Project:'), K.field('Due:', '1.3in'));
    if (b === 'k2') {
      const ck = r.pick([['How is it going?', 'Draw a face: happy, okay or stuck.'], ['What went well?', 'What will we fix?'], ['What did we finish?', 'What is next?']]);
      return head + K.box('Draw what we will make', '', { draw: 2.1 }) + K.box('What we need', r.pick(['List or draw the things you need.', 'What do you need to get?']), { h: 0.9 }) +
        K.grid('1fr 1fr 1fr', ['First', 'Next', 'Last'].map(x => K.box(x, '', { draw: 0.9, h: 0.44, extra: '<p class="pl-done"><i></i> Done</p>' }))) +
        K.grid('1fr 1fr', ck.map(q => K.box('', q, { h: 0.9 })));
    }
    if (b === '35') {
      const ck = r.pick(P.chk_35);
      return head + K.box('Our goal', r.pick(['What will you make, do or find out?', 'What will be finished when you are done?']), { h: 0.7 }) +
        K.grid('1fr 1fr', [K.box('Materials', 'What do you need?', { h: 1.1 }), K.box('Team jobs', '', { extra: K.table([['Name', '45%'], ['Job', '']], 3) })]) +
        sec('Steps') + K.table([['#', '6%'], ['What to do', ''], ['Who', '18%'], ['By when', '14%'], ['Done', '9%']], 6, { fill: (i, j) => j === 0 ? i + 1 : j === 4 ? '<i class="pl-cb"></i>' : '' }) +
        sec('Check-ins') + K.table([['Date', '14%'], [ck[0], ''], [ck[1], '']], 2, { rh: 1.5 });
    }
    const ck = r.pick(P.chk_old), old = b === '912';
    return head + K.grid('1fr 1fr', [K.box(old ? 'Goal and deliverable' : 'Driving question or goal', old ? 'What will exist when you finish, and in what form?' : 'What are you trying to make or find out?', { h: 0.8 }),
      K.box(old ? 'Success criteria' : 'Final product and audience', old ? 'How will you know the work is good? List 2 or 3 criteria.' : 'What will you make, and who is it for?', { h: 0.8 })]) +
      K.grid('1fr 1fr', [K.box('Resources', r.pick(['Materials, sources, tools and people.', 'What and whom will you need?']), { h: 0.9 }), K.box('Roles', '', { extra: K.table([['Name', '42%'], ['Responsible for', '']], 4) })]) +
      sec(old ? 'Milestones' : 'Tasks') + K.table([['#', '5%'], [old ? 'Milestone or task' : 'Task', ''], [old ? 'Owner' : 'Who', '16%'], ['Due', '12%'], [old ? 'Status' : 'Done', '11%']], old ? 7 : 7,
        { fill: (i, j) => j === 0 ? i + 1 : (!old && j === 4) ? '<i class="pl-cb"></i>' : '' }) +
      (old ? K.box('Risks and plan B', r.pick(['What could go wrong, and what will you do if it does?', 'Name the biggest risk to finishing on time and your backup plan.']), { h: 0.6 }) : '') +
      sec('Check-ins') + K.table([['Date', '11%'], ...ck.map(x => [x, ''])], 3, { rh: 1.4 });
  },
  reading(b, r, K) {
    if (b === 'k2') {
      return K.table([['Date', '15%'], ['Book title', ''], ['Minutes', '14%'], ['How I liked it', '22%']], 6, { fill: (i, j) => j === 3 ? '<span class="pl-stars">☆ ☆ ☆</span>' : '' }) +
        K.box('About my book', r.pick(P.read_k2), { draw: 1.5, h: 1.3 });
    }
    const n = b === '912' ? 5 : 7;
    const cols = b === '35' ? [['Date', '12%'], ['Title and author', ''], ['Pages', '13%'], ['Minutes', '11%'], ['Adult initials', '12%']]
      : [['Date', '11%'], ['Title and author', ''], ['Pages (from-to)', '15%'], ['Minutes', '11%'], [b === '912' ? 'Genre or form' : 'Genre', '15%']];
    const qs = r.sample(P['read_' + b], 2);
    return K.table(cols, n, { total: true }) + sec('Responses') + qs.map((q, i) => K.box(`Response ${i + 1}`, q, { h: 1.2 })).join('') +
      (b === '912' ? K.box('A line worth keeping', 'Copy a short quotation with the page number. Why did you choose it?', { h: 0.6 }) : '');
  },
  practice(b, r, K, topic) {
    const head = K.fields(K.field(topic ? 'Week of:' : 'Instrument, sport or skill:'), ...(topic ? [] : [K.field('Week of:', '1.4in')]));
    if (b === 'k2') {
      return head + K.table([['Day', '12%'], ['Minutes', '14%'], ['What I did', ''], ['How it went', '30%']], 7,
        { fill: (i, j) => j === 0 ? DAYS[i] : j === 3 ? '<span class="pl-circ">great · okay · tricky</span>' : '' }) +
        K.box('Think about it', r.pick(P.prac_k2), { draw: 1.1, h: 0.9 });
    }
    const old = b !== '35';
    const goal = K.box('My goal this week', old ? r.pick(['Make it specific: what exactly will you be able to do by Sunday?', 'One focused, measurable target for the week.']) : r.pick(['What do you want to get better at?', 'Pick one thing to improve.']), { h: 0.4 });
    const cols = old ? [['Day', '8%'], ['Min.', '8%'], ['Focus: what exactly I worked on', ''], ['How it went (1-5)', '12%'], ['Note for next time', '28%']]
      : [['Day', '10%'], ['Minutes', '11%'], ['What I worked on', ''], ['How it went (4 = best)', '24%']];
    return head + goal + K.table(cols, 7, { fill: (i, j) => j === 0 ? DAYS[i] : (!old && j === 3) ? '<span class="pl-circ">1 · 2 · 3 · 4</span>' : '', total: true }) +
      K.grid('1fr 1fr', r.sample(P[old ? 'prac_old' : 'prac_35'], 2).map(q => K.box('', q, { h: 1.0 })));
  },
  science(b, r, K, topic) {
    const head = topic ? '' : K.fields(K.field(b === 'k2' ? 'What I am watching:' : 'Question:'));
    if (b === 'k2') {
      return head + K.grid('1fr 1fr', [1, 2, 3, 4].map(d => K.box(`Day ${d}`, '', { pre: K.fields(K.field('Date:')), draw: 1.4, h: 0.44, st: r.pick(['I see', 'I notice', 'It looks', 'Now it is']) }))) +
        K.box('', r.pick(P.sci_k2), { h: 0.88 });
    }
    if (b === '35') {
      return head + K.fields(K.field('I predict:')) + K.grid('1fr 1fr', [1, 2, 3, 4].map(d => K.box(`Observation ${d}`, '', { pre: K.fields(K.field('Date:'), K.field('Time:', '0.8in')), draw: 1.1, h: 0.68, st: 'I notice' }))) + K.grid('1fr 1fr', r.sample(P.sci_35, 2).map(q => K.box('', q, { h: 0.68 })));
    }
    if (b === '68') {
      return head + K.fields(K.field('Prediction:')) + K.table([['Date', '10%'], ['Time', '8%'], ['Conditions', '16%'], ['Measurement (with units)', '18%'], ['What I observe', '']], 6, { rh: 1.4 }) +
        K.grid('1fr 1fr', [K.box('Sketch', 'Label the parts. Add a scale if you can.', { draw: 1.8 }), K.box('', r.pick(P.sci_old), { h: 1.8 })]) + K.box('', r.pick(P.sci_old.filter(q => !/patterns or trends/.test(q))), { h: 0.6 });
    }
    const qs = r.sample(P.sci_old, 2);
    return head + K.fields(K.field('Hypothesis:')) + K.grid('1fr 1fr 1fr', ['Independent variable', 'Dependent variable (units)', 'Controlled variables'].map(x => K.box(x, '', { h: 0.56 }))) +
      K.table([['Date and time', '14%'], ['Condition or trial', '16%'], ['Measurement (units)', '18%'], ['Qualitative observations', '']], 6, { rh: 1.4 }) +
      K.grid('1fr 1fr', [K.box('Sketch or graph', '', { draw: 1.6 }), K.box('', qs[0], { h: 1.6 })]) + K.box('Sources of error and next steps', r.pick(['What could make these results wrong, and what would you test next?', 'Name one possible error and how you would reduce it next time.']), { h: 0.56 });
  },
  weekly(b, r, K) {
    const head = K.fields(K.field('Week of:'));
    if (b === 'k2') {
      const a = r.pick(['This week I learned', 'My favorite thing this week was']), rest = r.sample(P.wk_k2.filter(x => x !== 'Next week I will' && x !== a), 2);
      return head + K.box('', '', { draw: 1.6, h: 0.44, st: a }) + rest.map(s => K.box('', '', { h: 0.88, st: s })).join('') +
        K.box('I felt', 'Circle one or two.', { extra: `<p class="pl-words">${r.sample(WK_FEEL, 5).map(esc).join('<span></span>')}</p>` }) + K.box('', '', { h: 0.44, st: 'Next week I will' });
    }
    const n = 4, pool = P[b === '35' ? 'wk_35' : 'wk_old'];
    const qs = r.sample(pool.filter(q => !/goal for next week/.test(q)), n);
    const bx = qs.map(q => K.box('', q, { h: b === '35' ? 1.2 : 0.95 }));
    return head + (b === '35' ? bx.join('') : K.grid('1fr 1fr', bx)) + K.scale('My effort this week:', ['1 not much', '2 some', '3 strong', '4 my best']) +
      K.box('Goal for next week', b === '35' ? 'One thing you will do better, and how.' : 'Specific and doable: what, by when, and how you will know.', { h: 0.6 });
  },
  exit(b, r, K, topic) {
    const qs = b === 'k2' ? [r.pick(P.ex_k2.slice(0, 2)), r.pick(P.ex_k2.slice(2))] : r.sample(P[b === '35' ? 'ex_35' : 'ex_old'], 3);
    const rate = b === 'k2' ? K.scale('Color one:', ['I get it', 'I am getting it', 'I need help']) : K.scale('How well do I understand?', ['1 not yet', '2 getting there', '3 got it', '4 I could teach it']);
    const slip = `<div class="pl-slip">${K.fields(K.field('Name:'), K.field('Date:', '1.2in'))}${topic ? '' : K.fields(K.field('Lesson:'))}` +
      (b === 'k2' ? K.box('', '', { draw: 1.0, h: 0.44, st: qs[0] }) + K.box('', '', { h: 0.44, st: qs[1] })
        : K.box('', qs[0], { h: 0.68 }) + K.grid('1fr 1fr', qs.slice(1).map(q => K.box('', q, { h: 0.68 })))) + rate + '</div>';
    return slip + '<p class="pl-cut">cut here</p>' + slip;
  },
  goal(b, r, K) {
    if (b === 'k2') {
      return K.box('My goal', '', { draw: 1.6, h: 0.44, st: 'I will' }) + K.box('', r.pick(P.goal_why), { h: 0.88 }) +
        K.grid('1fr 1fr 1fr', ['Step 1', 'Step 2', 'Step 3'].map(x => K.box(x, '', { h: 0.88, extra: '' }))) +
        K.box('', r.pick(P.goal_help), { h: 0.44 }) + K.fields(K.field('I did it! Date:', '1.6in'));
    }
    if (b === '35') {
      return K.box('My goal', r.pick(['What do you want to be able to do?', 'Write your goal as "I will..."']), { h: 0.7 }) + K.box('', r.pick(P.goal_why), { h: 0.7 }) +
        sec('My steps') + K.table([['#', '6%'], ['Step', ''], ['By when', '16%'], ['Done', '10%']], 4, { fill: (i, j) => j === 0 ? i + 1 : j === 3 ? '<i class="pl-cb"></i>' : '' }) +
        K.grid('1fr 1fr', [K.box('', r.pick(P.goal_help), { h: 0.7 }), K.box('', r.pick(P.goal_block), { h: 0.7 })]) +
        K.box('How will I know I reached it?', '', { h: 0.4 }) + sec('Check-ins') + K.table([['Date', '14%'], ['How am I doing?', ''], ['What will I change?', '']], 2, { rh: 1.4 });
    }
    const old = b === '912';
    const smart = [['S', 'Specific', r.pick(['What exactly will you do?', 'What, where and how? Be exact.', 'What will you do, in plain words?'])],
      ['M', 'Measurable', r.pick(['What number or evidence will show progress?', 'How will you measure it?', 'What will you count, time or score?'])],
      ['A', 'Achievable', r.pick(['Why is this realistic for you right now?', 'What makes this a stretch, but possible?', 'What have you done before that shows you can?'])],
      ['R', 'Relevant', old ? r.pick(['How does it connect to a bigger goal or plan?', 'Why this goal, and why now?']) : r.pick(['Why does it matter to you?', 'How will it help you?'])],
      ['T', 'Time-bound', r.pick(['By what date?', 'What is your deadline, and when will you check in?', 'When will you start, and when will you finish?'])]];
    return (old ? K.fields(K.field('Long-term goal (a year or more away):')) : '') + sec('Make it SMART') +
      `<table class="pl-tab pl-smart"><tbody>${smart.map(([l, w, q]) => `<tr style="height:${(RH[b] * 1.6 * K.g).toFixed(2)}in"><th><b>${l}</b>${w}<small>${esc(q)}</small></th><td></td></tr>`).join('')}</tbody></table>` +
      K.box('My SMART goal', r.pick(['Put it together in one sentence.', 'Combine all five parts into one goal.']), { h: 0.6, st: 'By' }) +
      sec('Action steps') + K.table([['#', '5%'], ['Step', ''], ['By when', '14%'], ['Done', '9%']], 3, { fill: (i, j) => j === 0 ? i + 1 : j === 3 ? '<i class="pl-cb"></i>' : '' }) +
      K.box('If-then plan', r.pick(P.goal_block), { h: 0.5, st: 'If' }) + sec('Check-ins') + K.table([['Date', '11%'], ['Progress (with evidence)', ''], ['Adjustment', '']], 2, { rh: 1.4 });
  },
  design(b, r, K, topic) {
    const head = topic ? '' : K.fields(K.field(b === 'k2' ? 'We are making:' : 'Design challenge:'));
    if (b === 'k2') {
      return head + K.box('The problem', r.pick(P.des_prob_y), { h: 0.66 }) + K.box('What it must do', r.pick(['What does it need to do?', 'How will you know it works?']), { h: 0.66 }) +
        sec('Ideas') + K.grid('1fr 1fr 1fr', ['Idea 1', 'Idea 2', 'Idea 3'].map(x => K.box(x, '', { draw: 0.95 }))) +
        K.box('My idea', 'Draw it and label the parts.', { draw: 1.4 }) +
        K.grid('1fr 1fr', [K.box('What I need', '', { h: 0.88 }), K.box('Test it', r.pick(P.des_res_y), { h: 0.88 })]) + K.box('Make it better', r.pick(P.des_imp_y), { h: 0.66 });
    }
    const old = b !== '35';
    const prob = K.box('The problem', r.pick(old ? P.des_prob_o : P.des_prob_y), { h: 0.5 });
    const cc = K.grid('1fr 1fr', [K.box('Criteria', r.pick(P.des_crit), { h: old ? 0.68 : 0.72 }), K.box('Constraints', r.pick(old ? P.des_con_o : P.des_con_y), { h: old ? 0.68 : 0.72 })]);
    const ideas = sec('Ideas') + K.grid('1fr 1fr 1fr', [1, 2, 3].map(i => K.box(`Idea ${i}`, '', { draw: old ? 0.75 : 0.85, h: 0.34 })));
    const chosen = sec('Chosen idea') + K.grid('1.25fr 1fr', [K.box('Labeled sketch', old ? 'Name the parts, materials and sizes.' : 'Label the parts.', { draw: old ? 1.75 : 1.6 }),
      K.box('Why this one', r.pick(P.des_why), { h: old ? 0.56 : 0.5, extra: `<p class="pl-sec" style="margin-top:4px">Materials</p>` + K.lines(old ? 0.84 : 0.8) })]);
    const test = sec('Test plan') + K.grid('1fr 1.3fr', [K.box('What I will measure', r.pick(P.des_test), { h: 0.68 }), K.box('How I will test it', r.pick(P.des_how), { h: 0.68 })]);
    const end = K.grid('1fr 1fr', [K.box('Results', r.pick(old ? P.des_res_o : P.des_res_y), { h: old ? 0.84 : 0.9 }), K.box('Improve', r.pick(old ? P.des_imp_o : P.des_imp_y), { h: old ? 0.84 : 0.9 })]);
    return head + prob + cc + ideas + chosen + test + end;
  },
  trial(b, r, K, topic, o) {
    const n = o.entries, unit = o.unit;
    const head = topic ? '' : K.fields(K.field(b === 'k2' ? 'What I am testing:' : 'What I am testing or tracking:'));
    // the teacher's own columns, when typed, replace the middle ones (the row label and date stay)
    const own = String(o.cols || '').split(/[,;]/).map(x => x.replace(/\s+/g, ' ').trim().slice(0, 30)).filter(Boolean).slice(0, 6);
    const cols = own.length ? [[unit, b === 'k2' ? '13%' : '10%'], [unit === 'Week' ? 'Week of' : 'Date', b === 'k2' ? '15%' : '11%'], ...own.map(x => [x, ''])]
      : b === 'k2' ? [[unit, '13%'], ['Date', '15%'], ['What I did', ''], ['What I saw', '30%']]
      : [[unit, '9%'], [unit === 'Week' ? 'Week of' : 'Date', '12%'], ['What I did', ''], ['What I measured or saw', '27%'], ['Notes', '20%']];
    // rows share the table space, so 4 entries get tall rows and 10 still fit on the page
    const rh = Math.max(b === 'k2' ? 0.95 : 1.1, Math.min(b === 'k2' ? 2.2 : 2.4, { k2: 3.8, 35: 4.9, 68: 5.1, 912: 5.2 }[b] / (n * RH[b] * K.g)));
    const table = K.table(cols, n, { rh, fill: (i, j) => j === 0 ? `${unit} ${i + 1}` : '' });
    const sum = K.box(b === 'k2' ? 'What I found out' : 'Summary', r.pick(b === 'k2' ? P.tri_sum_y : P.tri_sum_o), { h: b === 'k2' ? 0.88 : b === '35' ? 0.72 : 0.6 });
    const next = K.box('Next time', r.pick(b === 'k2' ? P.tri_next_y : P.tri_next_o), { h: b === 'k2' ? 0.44 : 0.5 });
    return head + table + sum + next;
  },
};

/* ---------- words for each kind ---------- */
const NAME = { project: 'Project Planner', reading: 'Reading Log', practice: 'Practice Log', science: 'Science Observation Log', weekly: 'Weekly Reflection', exit: 'Exit Reflection', goal: 'Goal Setting', design: 'Design Planner', trial: 'Trial Log' };
const TOPIC_LAB = { project: 'Project', reading: 'Reading', practice: 'Skill', science: 'Investigation', weekly: 'Class', exit: 'Lesson', goal: 'Goal area', design: 'Design challenge', trial: 'Testing' };
const ICAN = {
  project: ['I can plan the steps of a project and check my progress.', 'I can break a project into steps, share the work and check my progress.'],
  reading: ['I can keep track of my reading and tell about a book.', 'I can track my reading and respond thoughtfully to what I read.'],
  practice: ['I can practice a little each day and notice what gets better.', 'I can practice with a clear focus and reflect on my progress.'],
  science: ['I can watch something closely and draw and write what I see.', 'I can record careful observations and look for patterns.'],
  weekly: ['I can think about my week and plan what to do next.', 'I can reflect on my learning and set a goal for next week.'],
  exit: ['I can tell what I learned today.', 'I can explain what I learned and what I still need.'],
  goal: ['I can set a goal and plan steps to reach it.', 'I can set a SMART goal and plan the steps to reach it.'],
  design: ['I can plan something to make, test it and make it better.', 'I can define a problem, compare ideas against criteria and constraints, test a design and improve it.'],
  trial: ['I can write down what I did and what I saw each time.', 'I can record each trial the same way and look for a pattern across them.'],
};
const DIR = {
  project: { k2: 'Draw what you will make. List what you need. Draw each step and color the box when it is done.', x: 'Fill in the goal first. List the steps in order, then who does each and by when. Check off each step when it is done, and fill in a check-in row each time you meet.' },
  reading: { k2: 'Each time you read, fill in one row. Color a star for each part you liked. Then answer the question at the bottom.', x: 'Fill in one row each time you read. Add up your pages and minutes in the Total row. Answer the response questions in full sentences.' },
  practice: { k2: 'Each day you practice, write the minutes and what you did. Circle how it went.', x: 'Each day, log your minutes, what you worked on and how it went. Add the total. At the end of the week, answer the two questions.' },
  science: { k2: 'On each day, write the date, draw what you see, and finish the sentence.', x: 'Record each observation with the date and time. Draw what you see, measure when you can, and write what you notice. Answer the questions when you are done.' },
  weekly: { k2: 'Draw and write about your week. Finish each sentence.', x: 'Answer each question in full sentences. Rate your effort, then set one goal for next week.' },
  exit: { k2: 'Finish each sentence. Color how you feel about today\'s lesson.', x: 'Answer each question in a sentence or two, then circle how well you understand. Hand it in on your way out.' },
  goal: { k2: 'Draw your goal and finish the sentence. Draw or write three steps.', x: 'Write your goal, then fill in each part. Check off steps as you finish them and fill in a check-in row each time you look back.' },
  design: { k2: 'Write the problem. Draw three ideas, then pick one and draw it big with labels. Test it and tell what you would change.', x: 'Define the problem, then list the criteria and constraints before you draw. Sketch three ideas, choose one and label it. Plan the test, record the results, then say what you would improve.' },
  trial: { k2: 'Each time, write the date, what you did and what you saw. At the end, tell what you found out.', x: 'Fill in one row each time. Record what you measured with units, the same way every time. When the rows are full, write the summary.' },
};
const MISTAKES = {
  project: 'Steps that are too big ("do the project") and no dates. A good step can be finished in one sitting. Watch for one student holding every job.',
  reading: 'Responses that only retell the plot. Push for a reason or a page reference. A filled table with no responses means the log has become a chore; trim the table rather than the thinking.',
  practice: 'Rows that say "practiced" with no detail. The "what I worked on" column should name a specific piece, move or passage.',
  science: 'Mixing up observations (what you see or measure) with guesses (what you think caused it), and measurements with no units.',
  weekly: 'One-word answers ("good", "math"). Ask for a reason or an example after every answer.',
  exit: 'Copying the lesson title as "what I learned". Look for answers in the student\'s own words and an honest rating.',
  goal: 'Goals that are wishes ("be better at math") with no number, date or first step. The first step should be something they can do this week.',
  design: 'Jumping to a favorite idea before the criteria are written, and a test that only checks whether it "works" instead of measuring something. Criteria say what it must do; constraints say what limits you.',
  trial: 'Rows that change what is measured from one entry to the next, and results with no units. The point of a log is doing the same thing the same way each time.',
};
const USE = {
  project: 'Hand out at the start of the project and keep it in a folder. Hold short check-ins (5 minutes) at set points; the check-in rows are for those.',
  reading: 'Print one per week and send home, or keep one in a reading folder. Read the responses once a week and write one question back.',
  practice: 'Works for music, sports, typing, handwriting, a language, or any skill. Print one per week. Ask students to bring it to lessons or practices.',
  science: 'Use for anything that changes over days: seeds, the moon, weather, mold on bread, a melting experiment. Keep the time of day the same when you can.',
  weekly: 'Friday is a natural time. Read a few aloud (with permission) to celebrate effort, and look back at last week\'s goal before setting a new one.',
  exit: 'Two slips per page: print, cut, and hand out in the last five minutes. Sort them into three piles by the rating to plan tomorrow\'s small groups.',
  goal: 'Model one goal out loud first. Revisit the page at each check-in date; a goal no one looks at again does not get met.',
  design: 'Fits any build challenge: a bridge from straws, a boat that floats, a marble run, a phone stand. Have students write criteria and constraints before they sketch, and keep the page through the test and the redesign.',
  trial: 'One page per experiment, habit or project. Choose Trial for repeated tests, Week for something tracked over weeks, Day for a daily log, or Session, Rehearsal, Round or Entry. Pick the number of entries to match your plan, and type your own columns (Load, Reps, Effort) to replace the middle ones.',
};

/* ---------- filled-in models for the teacher page ---------- */
const MODEL = {
  project: { y: ['Make a bird feeder (grades 3-5)', [['Goal', 'Build a bird feeder from a milk carton and hang it where we can see it from the classroom window.'], ['Steps', '1. Wash and dry the carton (Ava, Monday). 2. Cut two windows (Mr. Lee helps, Tuesday). 3. Add a perch stick (Sam, Tuesday). 4. Fill with seed and hang it (everyone, Wednesday).'], ['Check-in', 'Going well: the carton is clean and cut. Next: find a strong string.']]],
    o: ['A short podcast on local water quality (grades 6-12)', [['Goal and deliverable', 'A 5-minute podcast episode explaining where our town\'s drinking water comes from and how it is tested.'], ['Success criteria', 'At least two sources, one interview, clear audio, under 6 minutes.'], ['Tasks', '1. Research the water source (Jordan, Oct 3). 2. Write interview questions (Maya, Oct 5). 3. Record the interview (Jordan and Maya, Oct 10). 4. Edit and add music (Leo, Oct 14).'], ['Check-in', 'Progress: research done. Risk: the interview may be hard to schedule. Next: email two backup contacts.']]] },
  reading: { y: ['A grades 3-5 response', [['Question', 'How did a character change? What made them change?'], ['Response', 'In Charlotte\'s Web, Wilbur starts out lonely, and when he learns he may be killed, he panics and cries. Charlotte helps him by spinning words like "Some Pig" in her web. By the end, Wilbur is brave and takes care of Charlotte\'s egg sac. He changed because a friend believed in him.']]],
    o: ['A grades 6-12 response', [['Question', 'How does the author use structure to create meaning?'], ['Response', 'In Holes, Louis Sachar switches between Stanley digging at Camp Green Lake and the story of Kissin’ Kate Barlow, set more than a hundred years earlier. At first the old story seems like a detour, but the two plots keep touching: the lake, the onions, the hidden treasure. The structure makes the reader see that Stanley’s bad luck is tied to the past, so when he carries Zero up the mountain, it feels like a whole family history being set right.']]] },
  practice: { y: ['Jump rope (grades 3-5)', [['Monday', '15 minutes. Two-foot jumps, counted to 50 without stopping. How it went: 3.'], ['Wednesday', '10 minutes. Tried criss-cross. Kept tripping. How it went: 2.'], ['What got easier?', 'I can do 50 two-foot jumps now. On Monday I only got to 30.']]],
    o: ['Piano (grades 6-12)', [['Goal this week', 'Play the C major scale hands together, two octaves, at 92 beats per minute with no stops.'], ['Tuesday', '20 min. Focus: thumb crossing in the left hand, slow at 72 bpm. Rating 3. Note: the crossing after the 3rd finger keeps bumping.'], ['Friday', '25 min. Hands together at 88 bpm. Rating 4. Note: try 92 with a metronome tomorrow.'], ['Reflection', 'Practicing the crossing alone, slowly, fixed the bump faster than playing the whole scale over and over.']]] },
  science: { y: ['A bean seed in a clear cup (grades K-5)', [['Day 1', 'I see a dry bean against the wet paper towel.'], ['Day 3', 'The bean is bigger and the skin is wrinkly. A small white root is coming out.'], ['Day 6', 'The root is long and has little hairs. A green stem is pushing up.'], ['What changed?', 'The bean grew a root first, then a stem.']]],
    o: ['Bean plant growth with sample data (grades 6-12)', [['Question', 'How fast does a bean seedling grow in its first week above the soil?'], ['Entries', 'Day 1: 1.0 cm, hook-shaped stem. Day 3: 4.5 cm, seed leaves opening. Day 5: 9.0 cm, first true leaves. Day 7: 12.5 cm, leaning toward the window.'], ['Pattern', 'Growth was fastest between days 3 and 5 (about 2.3 cm per day). The stem bent toward the light.'], ['Source of error', 'We measured from the soil, but the soil level sank when watered.']]] },
  weekly: { y: ['A grades 3-5 reflection', [['What was hard?', 'Long division was hard. I made a list of the steps and checked each one, and by Thursday I got four in a row right.'], ['Goal for next week', 'Finish my reading log every night before dinner so I do not forget.']]],
    o: ['A grades 6-12 reflection', [['Where did you struggle?', 'I lost points on the lab report because my conclusion did not use the data. I am going to reread the rubric before I write, not after.'], ['Goal for next week', 'Start the history essay by Tuesday and get feedback on my thesis by Thursday.']]] },
  exit: { y: ['Strong K-5 answers (sample lesson: equivalent fractions)', [['Today I learned', 'Two fractions can name the same amount, like 1/2 and 2/4.'], ['Rating', 'Getting there: I can do it with a picture but not yet without one.']]],
    o: ['Strong 6-12 answers (sample lesson: photosynthesis)', [['Key idea', 'Plants use light energy to turn carbon dioxide and water into sugar, and they release oxygen.'], ['Still unsure', 'Where does the oxygen come from: the water or the carbon dioxide?'], ['Rating', '3, got it.']]] },
  goal: { y: ['A grades 3-5 goal', [['My goal', 'I will read for 20 minutes five nights a week.'], ['Steps', '1. Pick two books from the library by Friday. 2. Set a timer each night. 3. Log my minutes.'], ['How will I know?', 'My log will show 100 minutes each week.']]],
    o: ['A SMART goal (grades 6-12)', [['Specific', 'Lower my mile time.'], ['Measurable', 'From 9:30 to 8:45.'], ['Achievable', 'I improved by 30 seconds last season with less training.'], ['Relevant', 'I want to make the cross-country team.'], ['Time-bound', 'By the spring fitness test, April 15.'], ['SMART goal', 'By April 15, I will run a mile in 8:45 by running three times a week and doing one interval workout each week.']]] },
};
MODEL.design = { y: ['A boat that floats (grades K-5)', [['The problem', 'Make a boat from foil that holds the most pennies without sinking.'], ['Criteria', 'Floats. Holds at least 10 pennies. Made only from one sheet of foil.'], ['Constraints', 'One 15 cm square of foil. Ten minutes to build.'], ['Chosen idea', 'A wide flat boat with low sides, because a wide bottom spreads the weight.'], ['Test', 'Added pennies one at a time. It held 23 before water came over the side.'], ['Improve', 'Make the sides a little taller and fold the corners tighter so water does not leak in.']]],
  o: ['A straw bridge (grades 6-12)', [['The problem', 'Build a bridge that spans a 30 cm gap and holds a 500 g load for 10 seconds.'], ['Criteria', 'Spans 30 cm. Holds 500 g at the center. Weighs under 40 g.'], ['Constraints', '30 straws, 1 m of tape, 25 minutes.'], ['Chosen idea', 'A truss of triangles, because triangles do not change shape under load; a flat beam would sag.'], ['Test plan', 'Measure: mass held before failure, in grams. Three trials, adding 100 g at a time, same load point each time.'], ['Results', 'Trial 1: 600 g. Trial 2: 700 g. Trial 3: 650 g. Mass 36 g. Met all criteria.'], ['Improve', 'The deck sagged first each time, so double the deck straws rather than the sides.']]] };
MODEL.trial = { y: ['Which paper airplane flies farthest? (grades K-5)', [['Trial 1', 'Oct 4. Threw the dart plane. It went 6 big steps.'], ['Trial 2', 'Oct 4. Threw the glider. It went 9 big steps.'], ['Trial 3', 'Oct 5. Threw the dart plane again. 7 big steps.'], ['What I found out', 'The glider went farther both times. It has bigger wings.']]],
  o: ['Dissolving sugar at different temperatures (grades 6-12)', [['Trial 1', 'Mar 3. 1 tsp sugar in 200 mL water at 20 °C, stirred 1 turn per second. Dissolved in 95 s.'], ['Trial 2', 'Mar 3. Same, water at 40 °C. 50 s.'], ['Trial 3', 'Mar 3. Same, water at 60 °C. 28 s. Note: thermometer read 58 °C by the end.'], ['Summary', 'Warmer water dissolved the sugar faster every time, and the drop from 20 to 40 °C was bigger than from 40 to 60 °C. Next: repeat each temperature three times to check the pattern.']]] };
const modelHtml = ([title, rows]) => `<h3>Model: ${esc(title)}</h3><table class="ws-table"><tbody>${rows.map(([a, b]) => `<tr><th>${esc(a)}</th><td>${esc(b)}</td></tr>`).join('')}</tbody></table>`;

const CSS = `
.pl-box { border: 1.5px solid #222; border-radius: 8px; padding: .05in .1in .07in; margin: .08in 0; break-inside: avoid; display: flex; flex-direction: column; background: #fff; }
.pl-grid { display: grid; gap: .1in; margin: .08in 0; }
.pl-grid .pl-box { margin: 0; }
.pl-head { margin: 0; line-height: 1.3; }
.pl-head:empty { display: none; }
.pl-lab { font: 700 12.5px/1.3 var(--sans); text-transform: uppercase; letter-spacing: .06em; margin-right: 4px; }
.pl-q { font-size: 13px; }
.pl-lines { margin-top: auto; }
.pl-lines span { display: block; height: var(--lh); border-bottom: 1px solid #888; position: relative; }
.pl-lines span i { position: absolute; left: 0; bottom: 2px; font-size: 13px; color: #555; white-space: nowrap; }
.pl-k2 .pl-lines span::after { content: ''; position: absolute; left: 0; right: 0; top: 50%; border-top: 1px dashed #bbb; }
.pl-k2 .pl-lines span i { font-size: 16px; }
.pl-k2 .pl-lab { font-size: 16px; text-transform: none; letter-spacing: 0; }
.pl-k2 .pl-q { font-size: 15px; }
.pl-draw { border: 1px dashed #888; border-radius: 6px; margin: 4px 0; }
.pl-fields { display: flex; gap: 16px; margin: 4px 0; font-size: 13.5px; align-items: baseline; }
.pl-k2 .pl-fields { font-size: 15px; }
.pl-field { display: flex; gap: 6px; align-items: baseline; flex: 1; }
.pl-field b { font-weight: 700; white-space: nowrap; }
.pl-field > span { border-bottom: 1.5px solid #222; height: 1.1em; min-width: .8in; }
.pl-field:has(> span[style*="width"]) { flex: 0 0 auto; }
.pl-sec { margin: .1in 0 2px; font: 700 12.5px var(--sans); text-transform: uppercase; letter-spacing: .06em; }
.pl-k2 .pl-sec { font-size: 15px; text-transform: none; }
.pl-tab { width: 100%; border-collapse: collapse; margin: 3px 0 .06in; table-layout: fixed; break-inside: avoid; }
.pl-tab th { font: 700 11.5px/1.2 var(--sans); text-align: left; padding: 3px 5px; border: 1.5px solid #222; background: #eee; vertical-align: bottom; }
.pl-k2 .pl-tab th { font-size: 14px; }
.pl-tab td { border: 1px solid #555; padding: 2px 5px; font-size: 12.5px; vertical-align: middle; }
.pl-tab td:first-child { font-weight: 600; }
.pl-tab .pl-total td { font-weight: 700; height: .3in; border-top: 2px solid #222; }
.pl-smart th { width: 30%; font: 400 12px/1.3 var(--sans); vertical-align: top; background: #f2f2f2; }
.pl-smart th b { display: inline-block; font: 700 20px/1 var(--serif, Georgia); margin-right: 6px; }
.pl-smart th small { display: block; font-size: 11.5px; color: #333; margin-top: 3px; }
.pl-cb { display: inline-block; width: .9em; height: .9em; border: 1.5px solid #333; border-radius: 2px; }
.pl-stars { font-size: 20px; letter-spacing: 4px; }
.pl-circ { font-size: 13px; color: #333; }
.pl-k2 .pl-circ { font-size: 14px; }
.pl-done { margin: 3px 0 0; font-size: 14px; }
.pl-done i { display: inline-block; width: 1em; height: 1em; border: 1.5px solid #333; border-radius: 2px; vertical-align: -2px; }
.pl-scale { display: flex; flex-wrap: wrap; gap: 6px 18px; align-items: center; margin: .07in 0; font-size: 13px; }
.pl-scale span { display: inline-flex; align-items: center; gap: 5px; }
.pl-scale i { display: inline-block; width: 1em; height: 1em; border: 1.5px solid #333; border-radius: 50%; }
.pl-k2 .pl-scale { font-size: 15px; }
.pl-k2 .pl-scale i { width: 1.4em; height: 1.4em; }
.pl-words { display: flex; flex-wrap: wrap; gap: 8px 26px; font-size: 16px; margin: 6px 4px 4px; }
.pl-slip { border: 1.5px solid #222; border-radius: 10px; padding: .08in .12in; break-inside: avoid; }
.pl-slip .pl-box { border-width: 1px; }
.pl-cut { display: flex; align-items: center; gap: 8px; margin: .12in 0; font-size: 10.5px; color: #555; }
.pl-cut::before, .pl-cut::after { content: ''; flex: 1; border-top: 1.5px dashed #555; }
.pl-topic { margin: 0 0 4px; font-size: 14px; }
`;

Gen.add('planner-log', {
  title: 'Planners, Logs and Reflections', type: 'Planner', noKey: true, css: CSS,
  fields: [
    { id: 'kind', label: 'Kind', type: 'select', options: KINDS, def: 'reading' },
    { id: 'band', label: 'Grade band', type: 'select', options: BANDS, def: '35' },
    { id: 'topic', label: 'Title, skill or topic (optional)', type: 'text', def: '' },
    { id: 'entries', label: 'Entries (rows)', type: 'select', options: v => [['3', '3'], ['4', '4'], ['6', '6'], ['8', '8'], ['10', '10'], ...(v.band === 'k2' ? [] : [['12', '12']])], def: '6', show: v => v.kind === 'trial' },
    { id: 'unit', label: 'Each row is a', type: 'select', options: [['Trial', 'Trial'], ['Week', 'Week'], ['Day', 'Day'], ['Session', 'Session'], ['Rehearsal', 'Rehearsal'], ['Round', 'Round'], ['Entry', 'Entry']], def: 'Trial', show: v => v.kind === 'trial' },
    { id: 'cols', label: 'Your own columns (optional), comma separated: Load, Reps, Effort 1 to 10', type: 'text', def: '', show: v => v.kind === 'trial' },
  ],
  make(v, r) {
    const b = v.band, kind = v.kind, topic = String(v.topic || '').trim(), young = b === 'k2' || b === '35';
    const K = kit(b, GROW[`${kind}-${b}`] || 1);
    const body = BUILD[kind](b, r, K, topic, { entries: +v.entries || 6, unit: v.unit || 'Trial', cols: v.cols });
    const short = topic && topic.length <= 40;
    const name = kind === 'trial' ? `${v.unit || 'Trial'} Log` : NAME[kind];
    const title = short ? `${name}: ${topic}` : name;
    const topicLine = topic && !short ? `<p class="pl-topic"><b>${esc(TOPIC_LAB[kind])}:</b> ${esc(topic)}</p>` : '';
    const eyebrowKind = kind === 'weekly' || kind === 'exit' ? 'Reflection' : kind === 'project' || kind === 'goal' || kind === 'design' ? 'Planner' : 'Log';
    return {
      title, eyebrow: eyebrowKind, level: BANDS.find(x => x[0] === b)[1],
      ican: ICAN[kind][b === 'k2' ? 0 : 1], directions: DIR[kind][b === 'k2' ? 'k2' : 'x'],
      minutes: { project: 20, reading: 10, practice: 10, science: 15, weekly: 15, exit: 5, goal: 20, design: 25, trial: 10 }[kind],
      materials: kind === 'science' || kind === 'design' ? 'pencil, ruler' : kind === 'exit' ? 'pencil, scissors (teacher)' : 'pencil' + (b === 'k2' ? ', crayons' : ''),
      parts: [['', `<div class="pl pl-${b}">${topicLine}${body}</div>`]], items: [],
      mistakes: MISTAKES[kind],
      notes: `${USE[kind]} The prompts change with each New sheet, so a class can use a fresh page every week.${kind === 'reading' && b !== 'k2' ? ' Count pages or minutes, whichever your class tracks; the other column can stay blank.' : ''}${kind === 'trial' ? ` This sheet has ${v.entries} rows; the row height shrinks as you add entries so it stays one page.` : ''}`,
      teacher: modelHtml(MODEL[kind][young ? 'y' : 'o']) + `<p>Share the model, or fill one in together on the board, before students start their own.</p>`,
    };
  },
});
})();
