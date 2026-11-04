// Writing Frames, grades 1-12. A layout generator: no computed answers (noKey). Genre and grade set the structure:
// grades 1-2 a few sentences with a starter on each line; grade 3 one paragraph; grades 4-5 a short multi-paragraph frame;
// grades 6-8 a five-part essay frame; grades 9-12 an argument-style frame with counterclaim and rebuttal (where the genre
// has one). Starters and transition words are drawn from banks, so New sheet gives fresh ones. A checklist matched to the
// Common Core writing standard for the grade sits at the bottom; the teacher page has a model written for a sample topic.
(() => {
const { esc } = Gen.h;

const GRADES = Array.from({ length: 12 }, (_, i) => [String(i + 1), `Grade ${i + 1}`]);
const GENRES = [['opinion', 'Opinion / argument'], ['informative', 'Informative / explanatory'], ['narrative', 'Narrative'],
  ['cer', 'Claim, evidence, reasoning (science)'], ['compare', 'Compare and contrast'], ['summary', 'Summary']];
const bandOf = g => g <= 2 ? 'p' : g === 3 ? 'g3' : g <= 5 ? 'g45' : g <= 8 ? 'g68' : 'g912';
const LH = { p: 0.44, g3: 0.36, g45: 0.34, g68: 0.3, g912: 0.28 };
const GROW = /*GROW*/{"opinion-p1-plan":0.8,"opinion-p-plan":0.87,"opinion-g3-plan":0.83,"opinion-g45-plan":0.93,"opinion-g68-plan":1.51,"opinion-g912-plan":0.92,"informative-p1-plan":0.61,"informative-p-plan":0.67,"informative-g3-plan":0.83,"informative-g45-plan":1.36,"informative-g68-plan":1.51,"informative-g912-plan":0.87,"narrative-p1-plan":0.89,"narrative-p-plan":0.95,"narrative-g3-plan":0.83,"narrative-g45-plan":1.09,"narrative-g68-plan":1.43,"narrative-g912-plan":0.97,"cer-p1-plan":0.61,"cer-p-plan":0.95,"cer-g3-plan":0.87,"cer-g45-plan":0.93,"cer-g68-plan":1.15,"cer-g912-plan":1.12,"compare-p1-plan":0.69,"compare-p-plan":1.03,"compare-g3-plan":1.11,"compare-g45-plan":1.48,"compare-g68-plan":1.66,"compare-g912-plan":1.06,"summary-p1-plan":0.73,"summary-p-plan":1.07,"summary-g3-plan":1.14,"summary-g45-plan":1.16,"summary-g68-plan":1.34,"summary-g912-plan":1.19,"opinion-p1-draft":1.16,"opinion-p-draft":1.03,"opinion-g3-draft":1.26,"opinion-g45-draft":1.49,"opinion-g68-draft":1.6,"opinion-g912-draft":1.6,"informative-p1-draft":0.77,"informative-p-draft":0.71,"informative-g3-draft":1.33,"informative-g45-draft":1.47,"informative-g68-draft":1.59,"informative-g912-draft":1.57,"narrative-p1-draft":1.16,"narrative-p-draft":1.03,"narrative-g3-draft":1.33,"narrative-g45-draft":1.78,"narrative-g68-draft":1.64,"narrative-g912-draft":1.66,"cer-p1-draft":0.77,"cer-p-draft":1.03,"cer-g3-draft":1.23,"cer-g45-draft":1.36,"cer-g68-draft":1.72,"cer-g912-draft":1.84,"compare-p1-draft":0.83,"compare-p-draft":1.24,"compare-g3-draft":1.61,"compare-g45-draft":1.51,"compare-g68-draft":1.64,"compare-g912-draft":1.73,"summary-p1-draft":0.89,"summary-p-draft":1.23,"summary-g3-draft":1.61,"summary-g45-draft":1.74,"summary-g68-draft":1.88,"summary-g912-draft":1.85}/*GROW*/;   // per genre, band and length: stretch the writing space to fill the page (tuned by print tests)

/* ---------- starter banks (each section draws two or three, so New sheet changes them) ---------- */
const S = {
  op_claim_p: ['I think', 'I like', 'My favorite is', 'I believe'], op_reason_p: ['One reason is', 'I think this because', 'This is because'],
  op_reason2_p: ['Also,', 'Another reason is', 'And'], op_end_p: ['That is why', 'So,', 'Now you know why'],
  op_claim: ['In my opinion,', 'I strongly believe that', 'I think that', 'It is clear to me that', 'I am convinced that', 'There are good reasons why'],
  op_r1: ['One reason is that', 'First,', 'The most important reason is', 'To begin with,'],
  op_rn: ['Another reason is', 'In addition,', 'Also,', 'Second,', 'Besides that,'],
  op_rl: ['Finally,', 'Most importantly,', 'The last reason is', 'Above all,'],
  op_ex: ['For example,', 'For instance,', 'To illustrate,', 'One time,'],
  op_end: ['That is why', 'For these reasons,', 'In conclusion,', 'As you can see,', 'Clearly,'],
  hook: ['Imagine', 'Have you ever', 'Every day,', 'Most people agree that', 'It may seem that', 'What would happen if'],
  arg_claim: ['This essay will show that', 'It is clear that', 'The evidence shows that', 'I will argue that', 'We should'],
  arg_reason: ['One reason is that', 'First,', 'The strongest reason is', 'Another reason is', 'In addition,', 'Equally important,'],
  arg_ev: ['According to', 'For example,', 'One source reports that', 'The data show', 'As one expert explains,', 'For instance,'],
  arg_explain: ['This shows that', 'This matters because', 'In other words,', 'This means that', 'This suggests that'],
  arg_counter: ['Some people argue that', 'Critics claim that', 'It is true that', 'Opponents point out that', 'One might object that'],
  arg_rebut: ['However,', 'While this is partly true,', 'Even so,', 'This argument overlooks', 'Nevertheless,'],
  arg_end: ['In the end,', 'Ultimately,', 'For these reasons,', 'If we', 'The choice is clear:', 'In conclusion,'],
  inf_topic_p: ['I am going to tell you about', 'This is about', 'Did you know'], inf_fact_p: ['One fact is', 'They can', 'They have', 'It is'],
  inf_fact2_p: ['Also,', 'Another fact is', 'They also'], inf_end_p: ['Now you know about', 'That is why', 'I like learning about'],
  inf_topic: ['Have you ever wondered', 'Did you know that', 'There are many interesting facts about', 'Imagine', 'Many people do not know that'],
  inf_detail: ['One important fact is', 'For example,', 'Another detail is', 'In addition,', 'Also,', 'Scientists have found that'],
  inf_define: ['This word means', 'This is a kind of', 'This is called', 'In other words,'],
  inf_end: ['In conclusion,', 'As you can see,', 'Now you know', 'All in all,', 'This shows why'],
  inf_thesis: ['This report explains', 'To understand this topic, it helps to know', 'Three key ideas explain', 'This essay examines'],
  inf_point: ['The first key idea is', 'Another important aspect is', 'Equally important is', 'A final point is'],
  inf_analyze: ['This means that', 'As a result,', 'This is important because', 'In other words,', 'This helps explain'],
  inf_conc: ['Taken together,', 'In the end,', 'Understanding this matters because', 'Ultimately,'],
  nar_beg_p: ['One day,', 'Last summer,', 'Once,', 'It was'], nar_mid_p: ['Next,', 'Then', 'After that,'], nar_end_p: ['Finally,', 'At the end,', 'I felt'],
  nar_open: ['It all started when', 'I will never forget the day', 'The morning began like any other.', 'Have you ever', 'Nobody expected'],
  nar_event: ['Suddenly,', 'A few minutes later,', 'Just then,', 'Before long,', 'Meanwhile,', 'After that,'],
  nar_feel: ['My heart', 'I felt', 'I could hear', 'I wondered', 'I took a deep breath and'],
  nar_end: ['In the end,', 'Finally,', 'Since that day,', 'Now I know', 'Looking back,'],
  cer_q: ['The question is', 'We wanted to find out'], cer_claim_p: ['I think'], cer_ev_p: ['I saw', 'I noticed', 'We found'], cer_why_p: ['This shows', 'I know because'],
  cer_claim: ['I claim that', 'Our results show that', 'The answer is', 'Based on our test,'],
  cer_ev: ['The data show', 'In our test,', 'We observed', 'When we', 'The table shows'],
  cer_reason: ['This evidence supports my claim because', 'This happens because', 'The science idea that explains this is', 'This shows that'],
  cer_counter: ['Another explanation could be', 'Someone might argue', 'One possible source of error is'],
  cer_rebut: ['However,', 'This is less likely because', 'To test this, we could'],
  cmp_alike_p: ['They are alike because', 'They both'], cmp_diff_p: ['They are different because', 'But', 'One is'], cmp_end_p: ['I like', 'Both are'],
  cmp_intro: ['Both', 'At first glance,', 'have a lot in common, but', 'Although'],
  cmp_alike: ['Both', 'Similarly,', 'Likewise,', 'In the same way,', 'They are alike because'],
  cmp_diff: ['However,', 'In contrast,', 'On the other hand,', 'Unlike', 'One difference is'],
  cmp_end: ['Overall,', 'In conclusion,', 'Although they are different,', 'The most important difference is'],
  sum_beg_p: ['At the beginning,', 'First,'], sum_mid_p: ['In the middle,', 'Then'], sum_end_p: ['At the end,', 'Last,'],
  sum_open: ['The text', 'In the story', 'In the article', 'The author explains that'],
  sum_first: ['First,', 'At the beginning,', 'The text begins with', 'To start,'],
  sum_detail: ['Next,', 'Then,', 'After that,', 'The author also explains', 'Later,'],
  sum_end: ['In the end,', 'Overall,', 'The main idea is', 'The author\'s main point is'],
};
const TRANS = {
  opinion: { g3: ['because', 'therefore', 'since', 'for example', 'also', 'another reason', 'so', 'first', 'finally', 'in conclusion'],
    g45: ['for instance', 'in order to', 'in addition', 'consequently', 'specifically', 'for example', 'also', 'most importantly', 'as a result', 'in conclusion'],
    g68: ['furthermore', 'moreover', 'as a result', 'for this reason', 'in addition', 'although', 'on the other hand', 'consequently', 'in fact', 'therefore'],
    g912: ['nevertheless', 'conversely', 'admittedly', 'consequently', 'furthermore', 'in light of', 'to be sure', 'thus', 'even so', 'notably'] },
  informative: { g3: ['also', 'another', 'and', 'more', 'but', 'first', 'next', 'for example', 'in conclusion', 'too'],
    g45: ['another', 'for example', 'also', 'because', 'in contrast', 'especially', 'in addition', 'such as', 'as a result', 'finally'],
    g68: ['for example', 'in addition', 'as a result', 'similarly', 'in contrast', 'specifically', 'consequently', 'for instance', 'therefore', 'in particular'],
    g912: ['in turn', 'consequently', 'by contrast', 'likewise', 'notably', 'in particular', 'as a result', 'to illustrate', 'thus', 'moreover'] },
  narrative: { g3: ['first', 'then', 'next', 'after that', 'later', 'finally', 'that night', 'the next day', 'suddenly', 'at last'],
    g45: ['meanwhile', 'suddenly', 'a few minutes later', 'before long', 'just then', 'eventually', 'later that day', 'at that moment', 'afterward', 'finally'],
    g68: ['meanwhile', 'moments later', 'by the time', 'without warning', 'as soon as', 'earlier that day', 'eventually', 'in the distance', 'that night', 'afterward'],
    g912: ['years later', 'in that instant', 'all the while', 'by then', 'only later', 'even now', 'until then', 'in the meantime', 'that was when', 'looking back'] },
  cer: { g3: ['because', 'so', 'therefore', 'for example', 'this shows', 'also'], g45: ['because', 'so', 'therefore', 'for example', 'this shows', 'as a result', 'in addition', 'since'],
    g68: ['therefore', 'as a result', 'this indicates', 'consequently', 'in addition', 'because', 'for example', 'this suggests'],
    g912: ['therefore', 'consequently', 'this indicates', 'however', 'whereas', 'thus', 'in contrast', 'this suggests'] },
  compare: { g3: ['both', 'also', 'but', 'another', 'same', 'different', 'too', 'and'], g45: ['both', 'similarly', 'likewise', 'however', 'in contrast', 'on the other hand', 'unlike', 'also', 'while', 'but'],
    g68: ['similarly', 'likewise', 'in the same way', 'however', 'in contrast', 'on the other hand', 'whereas', 'unlike', 'conversely', 'although'],
    g912: ['whereas', 'conversely', 'by contrast', 'likewise', 'correspondingly', 'nonetheless', 'just as', 'in the same vein', 'differs from', 'parallels'] },
  summary: { g3: ['first', 'next', 'then', 'after that', 'finally', 'in the end'], g45: ['first', 'next', 'then', 'after that', 'later', 'finally', 'in the end', 'the author explains'],
    g68: ['first', 'next', 'then', 'later', 'as a result', 'finally', 'the author explains', 'the author argues'],
    g912: ['the author argues', 'the author contends', 'initially', 'subsequently', 'ultimately', 'in turn', 'the speaker asserts', 'the text concludes'] },
};

/* ---------- frames: rows of sections. sec = [label, prompts, starter bank, writing weight] ---------- */
function frame(genre, band, grade, r) {
  const sec = (lab, q, st, w = 1, o = {}) => ({ lab, q, st, w, ...o });
  if (genre === 'opinion') {
    if (band === 'p') return [[sec('My opinion', ['What do you think?', 'Tell what you like or think.'], 'op_claim_p')], [sec('My reason', ['Why do you think that?', 'Tell one reason.'], 'op_reason_p')],
      ...(grade === 2 ? [[sec('Another reason', ['Tell one more reason.', 'Why else?'], 'op_reason2_p')]] : []), [sec('My ending', ['Say your opinion again.', 'Wrap it up.'], 'op_end_p')]];
    if (band === 'g3') return [[sec('Topic sentence: my opinion', ['State your opinion clearly.', 'What do you think about the topic?'], 'op_claim')],
      [sec('Reason 1', ['Give a reason, then an example.', 'Why? Back it up.'], 'op_r1', 1, { sub: 'op_ex' })], [sec('Reason 2', ['Give another reason and an example.', 'What else supports your opinion?'], 'op_rn', 1, { sub: 'op_ex' })],
      [sec('Reason 3', ['Save a strong reason for last.', 'Give your last reason.'], 'op_rl', 1, { sub: 'op_ex' })], [sec('Concluding sentence', ['Restate your opinion in a new way.', 'Wrap it up.'], 'op_end')]];
    if (band === 'g45') return [[sec('Paragraph 1: Introduction', ['Hook the reader, introduce the topic and state your opinion.', 'Start with a hook, then give your opinion.'], 'hook', 1, { sub: 'op_claim' })],
      [sec('Paragraph 2: First reason', ['A reason, plus facts and details that support it.', 'Reason, then facts and details.'], 'op_r1', 1.5, { sub: 'op_ex' })], [sec('Paragraph 3: Second reason', ['Another reason, with facts and details.', 'Your next reason and its support.'], 'op_rn', 1.5, { sub: 'op_ex' })],
      [sec('Paragraph 4: Conclusion', ['Restate your opinion and end with a thought for the reader.', 'Connect back to your opinion. What should the reader do or think?'], 'op_end')]];
    if (band === 'g68') return [[sec('Introduction', ['Hook, background on the issue, and your claim.', 'Grab attention, explain the issue, then state your claim.'], 'hook', 1, { sub: 'arg_claim' })],
      [sec('Body 1: Reason', ['Reason, evidence, explanation.', 'Topic sentence, evidence, then explain it.'], 'arg_reason', 1.4, { sub: 'arg_ev' }), sec('Body 2: Reason', ['Reason, evidence, explanation.', 'A second reason with evidence.'], 'arg_reason', 1.4, { sub: 'arg_ev' }),
        sec(grade >= 7 ? 'Body 3: Opposing claim' : 'Body 3: Reason', grade >= 7 ? ['Name an opposing claim, then answer it with evidence.', 'What would someone who disagrees say? Respond.'] : ['Your strongest reason, evidence, explanation.', 'A third reason with evidence.'], grade >= 7 ? 'arg_counter' : 'arg_reason', 1.4, { sub: grade >= 7 ? 'arg_rebut' : 'arg_explain' })],
      [sec('Conclusion', ['Restate the claim, sum up your reasons, and end with why it matters.', 'Remind the reader of your claim and leave them with a final thought.'], 'arg_end')]];
    return [[sec('Introduction', ['Context or hook, then a precise, arguable claim.', 'Set up the issue and state a precise claim.'], 'hook', 1, { sub: 'arg_claim' })],
      [sec('Reason 1', ['Reason, evidence (cite it), analysis.', 'Topic sentence, cited evidence, then explain how it proves your claim.'], 'arg_reason', 1.4, { sub: 'arg_ev' }), sec('Reason 2', ['Reason, evidence (cite it), analysis.', 'Another line of reasoning, with cited evidence and analysis.'], 'arg_reason', 1.4, { sub: 'arg_explain' })],
      [sec('Counterclaim', ['State the strongest opposing argument fairly, with its evidence.', 'What is the best case against your claim?'], 'arg_counter', 1.1), sec('Rebuttal', ['Answer the counterclaim: what does it miss, or why does your claim still hold?', 'Point out the limits of the counterclaim.'], 'arg_rebut', 1.1)],
      [sec('Conclusion', ['Return to the claim and explain its significance: why should the reader care?', 'Sum up and show what is at stake.'], 'arg_end')]];
  }
  if (genre === 'informative') {
    if (band === 'p') return [[sec('Beginning', ['Name your topic.', 'What will you teach about?'], 'inf_topic_p')], [sec('A fact', ['Tell one fact.', 'What is one thing you know?'], 'inf_fact_p')],
      [sec(grade === 2 ? 'Another fact' : 'Another fact', ['Tell another fact.', 'What else do you know?'], 'inf_fact2_p')], ...(grade === 2 ? [[sec('A word to know', ['Tell what a topic word means.', 'Teach a word about your topic.'], 'inf_define')]] : []),
      [sec('My ending', ['End your writing.', 'Wrap it up.'], 'inf_end_p')]];
    if (band === 'g3') return [[sec('Topic sentence', ['Introduce your topic.', 'Tell the reader what this is about.'], 'inf_topic')], [sec('Detail 1', ['A fact or definition.', 'Teach one thing.'], 'inf_detail')],
      [sec('Detail 2', ['A related fact or detail.', 'Add another fact.'], 'inf_detail')], [sec('Detail 3', ['One more fact, detail or definition.', 'Add a third fact.'], 'inf_detail')], [sec('Concluding sentence', ['Sum up the topic.', 'End with something to remember.'], 'inf_end')]];
    if (band === 'g45') return [[sec('Paragraph 1: Introduction', ['Hook the reader and introduce the topic.', 'Start with a question or surprising fact, then name the topic.'], 'inf_topic')],
      [sec('Paragraph 2: First subtopic', ['Facts, definitions, details or examples about one part of the topic.', 'Pick one part of the topic and explain it with facts and examples.'], 'inf_detail', 1.5, { sub: 'inf_define', head: true }),
        sec('Paragraph 3: Second subtopic', ['Facts, definitions, details or examples about another part.', 'Explain the next part of the topic.'], 'inf_detail', 1.5, { sub: 'inf_define', head: true })],
      [sec('Paragraph 4: Conclusion', ['Sum up the most important ideas.', 'Remind the reader why the topic matters.'], 'inf_end')]];
    if (band === 'g68') return [[sec('Introduction', ['Hook, background, and a thesis that previews your main points.', 'Introduce the topic and tell what you will explain.'], 'inf_topic', 1, { sub: 'inf_thesis' })],
      [sec('Body 1', ['Topic sentence, facts or quotations, explanation.', 'One main point with support.'], 'inf_point', 1.4, { sub: 'inf_analyze' }), sec('Body 2', ['Topic sentence, facts or quotations, explanation.', 'A second main point with support.'], 'inf_point', 1.4, { sub: 'inf_analyze' }),
        sec('Body 3', ['Topic sentence, facts or quotations, explanation.', 'A third main point with support.'], 'inf_point', 1.4, { sub: 'inf_analyze' })],
      [sec('Conclusion', ['Sum up the main points and explain why the topic matters.', 'Pull your points together and leave the reader with something to think about.'], 'inf_conc')]];
    return [[sec('Introduction', ['Context, then a thesis that frames the topic and its complexity.', 'Set up the topic and state your controlling idea.'], 'inf_topic', 1, { sub: 'inf_thesis' })],
      [sec('Section 1', ['Point, evidence (cite it), analysis.', 'A key idea, developed with cited facts and explanation.'], 'inf_point', 1.3, { sub: 'inf_analyze' }), sec('Section 2', ['Point, evidence (cite it), analysis.', 'Build on section 1.'], 'inf_point', 1.3, { sub: 'inf_analyze' })],
      [sec('Section 3', ['Point, evidence, analysis.', 'A third key idea that completes the picture.'], 'inf_point', 1.3, { sub: 'inf_analyze' }), sec('Key terms', ['Define two or three words a reader must know.', 'Domain-specific words and what they mean.'], 'inf_define', 1.3)],
      [sec('Conclusion', ['Explain the implications or significance of the topic.', 'Why does this matter? What follows from it?'], 'inf_conc')]];
  }
  if (genre === 'narrative') {
    if (band === 'p') return [[sec('Beginning', ['Who is in it? Where are they?', 'What happened first?'], 'nar_beg_p')], [sec('Middle', ['What happened next?', 'Tell the next part.'], 'nar_mid_p')],
      ...(grade === 2 ? [[sec('Feelings', ['How did you or the character feel? Why?', 'Tell a thought or a feeling.'], 'nar_feel')]] : []), [sec('End', ['How did it end?', 'What happened last?'], 'nar_end_p')]];
    if (band === 'g3') return [[sec('Beginning', ['Introduce the narrator or characters and the situation.', 'Who, where and what is going on?'], 'nar_open')], [sec('Event 1', ['What happens first? Add an action or a feeling.', 'Start the action.'], 'nar_event')],
      [sec('Event 2', ['What happens next? Try some dialogue.', 'Add what a character says.'], 'nar_event')], [sec('Event 3', ['What happens after that?', 'Show thoughts and feelings.'], 'nar_feel')], [sec('Ending', ['How does it end? How do the characters feel?', 'Close the story.'], 'nar_end')]];
    if (band === 'g45') return [[sec('Opening', ['Introduce the narrator, characters and setting. Use a sensory detail.', 'Set the scene so the reader can see and hear it.'], 'nar_open')],
      [sec('The problem', ['What goes wrong, or what does the main character want?', 'Introduce the problem.'], 'nar_event', 1.1)],
      [sec('Events', ['Tell what happens in order. Use dialogue and description. Slow down at the most important moment.', 'The main events, with dialogue and details. Pace the big moment slowly.'], 'nar_event', 1.6, { sub: 'nar_feel' })],
      [sec('Ending', ['How is the problem solved? What did the character learn or feel?', 'Wrap up the story and show how things changed.'], 'nar_end')]];
    if (band === 'g68') return [[sec('Exposition', ['Set the context and point of view; introduce the narrator and characters.', 'Where, when, who, and whose eyes we see through.'], 'nar_open')],
      [sec('Rising action', ['Events that build the conflict. Use dialogue and description.', 'What complications pile up?'], 'nar_event', 1.4, { sub: 'nar_feel' }), sec('Climax', ['The turning point. Slow the pace down here.', 'The moment of highest tension.'], 'nar_feel', 1.4)],
      [sec('Falling action', ['What happens right after the turning point?', 'How do things begin to settle?'], 'nar_event'), sec('Resolution and reflection', ['How does it end, and what does the narrator realize?', 'Close the story and reflect on its meaning.'], 'nar_end')]];
    return [[sec('Opening', ['Establish the situation, point of view and tone.', 'Begin in a way that sets the tone you want.'], 'nar_open')],
      [sec('Complication', ['What disrupts the situation? Use telling details.', 'Introduce the conflict.'], 'nar_event', 1.3), sec('Escalation', ['Raise the stakes. Consider a second plot line or a flashback.', 'Build tension through events that connect.'], 'nar_event', 1.3, { sub: 'nar_feel' })],
      [sec('Turning point', ['The moment everything changes. Control the pacing.', 'The climax, slowed down.'], 'nar_feel', 1.3), sec('Resolution', ['How are the conflicts resolved, or not?', 'What is the outcome?'], 'nar_end', 1.3)],
      [sec('Reflection', ['What does the experience mean? How has the narrator changed?', 'Close with reflection that builds toward the tone you chose.'], 'nar_end')]];
  }
  if (genre === 'cer') {
    if (band === 'p') return [[sec('My question', ['What did we want to find out?', 'Write the question.'], 'cer_q')], [sec('I think', ['Answer the question.', 'What is your answer?'], 'cer_claim_p')],
      [sec('I saw', ['What did you see or find out?', 'Tell what happened in the test.'], 'cer_ev_p')], [sec('Because', ['Why does what you saw prove your answer?', 'Tell why.'], 'cer_why_p')]];
    if (band === 'g3' || band === 'g45') return [[sec('Question', ['What question are you answering?', 'Write the investigation question.'], 'cer_q', 0.6)], [sec('Claim', ['One sentence that answers the question.', 'Your answer, as a complete sentence.'], 'cer_claim', 0.8)],
      [sec('Evidence 1', ['Data or an observation that supports the claim.', 'A measurement or something you saw.'], 'cer_ev'), sec('Evidence 2', ['More data or another observation.', 'Another piece of evidence.'], 'cer_ev')],
      [sec('Reasoning', ['Explain why the evidence supports the claim. Use a science idea.', 'Why does the evidence prove your claim?'], 'cer_reason', 1.3)], [sec('Concluding sentence', ['Sum up what you learned.', 'End by restating your claim.'], 'op_end', 0.6)]];
    if (band === 'g68') return [[sec('Question and claim', ['State the question, then a precise claim that answers it.', 'Question, then your claim.'], 'cer_q', 0.9, { sub: 'cer_claim' })],
      [sec('Evidence 1', ['Specific data with units.', 'A measurement or result.'], 'cer_ev', 1.2), sec('Evidence 2', ['Specific data with units.', 'Another result.'], 'cer_ev', 1.2), sec('Evidence 3', ['Specific data or an observation.', 'A pattern in the data.'], 'cer_ev', 1.2)],
      [sec('Reasoning', ['Name the scientific principle and explain how it links each piece of evidence to the claim.', 'Why does the evidence support the claim? Name the science idea.'], 'cer_reason', 1.4)],
      [sec('Conclusion', ['Restate the claim and say what you would test next.', 'Sum up, and name one question you still have.'], 'op_end', 0.8)]];
    return [[sec('Claim', ['A precise claim, limited to what your data support.', 'State your claim and its scope.'], 'cer_claim', 0.8)],
      [sec('Evidence', ['Specific, sufficient data: numbers, units, trends. Cite sources if used.', 'Your strongest quantitative evidence.'], 'cer_ev', 1.3), sec('Reasoning', ['The scientific principle that connects evidence to claim.', 'Explain the mechanism.'], 'cer_reason', 1.3)],
      [sec('Alternate explanation', ['Another explanation someone could give for the data.', 'A counterclaim or confounding variable.'], 'cer_counter', 1.1), sec('Rebuttal', ['Why your claim is still the better explanation, or how a new test would decide.', 'Answer the alternate explanation.'], 'cer_rebut', 1.1)],
      [sec('Limitations and next steps', ['Sources of error, and what you would test next.', 'What could make this result wrong?'], 'cer_counter', 0.8)]];
  }
  if (genre === 'compare') {
    if (band === 'p') return [[sec('What I am comparing', ['Name the two things.', 'Tell what two things you will compare.'], 'cmp_intro', 0.6)], [sec('Alike', ['How are they the same?', 'Tell one way they are alike.'], 'cmp_alike_p')],
      [sec('Different', ['How are they different?', 'Tell one way they are not the same.'], 'cmp_diff_p')], [sec('My ending', ['Which do you like better? Why?', 'Wrap it up.'], 'cmp_end_p')]];
    if (band === 'g3') return [[sec('Topic sentence', ['Name both things you are comparing.', 'Introduce the two things.'], 'cmp_intro')], [sec('How they are alike', ['Two ways they are the same.', 'Tell how they are alike.'], 'cmp_alike', 1.3)],
      [sec('How they are different', ['Two ways they are different.', 'Tell how they are not the same.'], 'cmp_diff', 1.3)], [sec('Concluding sentence', ['Sum up how they compare.', 'End with what you think.'], 'cmp_end')]];
    if (band === 'g45') return [[sec('Paragraph 1: Introduction', ['Introduce both subjects and why you are comparing them.', 'Name both and hook the reader.'], 'cmp_intro')],
      [sec('Paragraph 2: Alike', ['How are they alike? Give facts and details.', 'Similarities, with details.'], 'cmp_alike', 1.5), sec('Paragraph 3: Different', ['How are they different? Give facts and details.', 'Differences, with details.'], 'cmp_diff', 1.5)],
      [sec('Paragraph 4: Conclusion', ['Sum up. Are they more alike or more different?', 'Finish with your main point about the two.'], 'cmp_end')]];
    if (band === 'g68') return [[sec('Introduction', ['Introduce both subjects and a thesis about how they compare.', 'Hook, background, thesis.'], 'cmp_intro')],
      [sec('Body 1: Point of comparison', ['One point; discuss both subjects with evidence.', 'Name a point, then compare both on it.'], 'cmp_alike', 1.4), sec('Body 2: Point of comparison', ['A second point, both subjects.', 'Compare both on another point.'], 'cmp_diff', 1.4),
        sec('Body 3: Point of comparison', ['A third point, both subjects.', 'The point that matters most.'], 'cmp_diff', 1.4)],
      [sec('Conclusion', ['Why does the comparison matter? What does it reveal?', 'Sum up and explain what the comparison shows.'], 'cmp_end')]];
    return [[sec('Introduction', ['Context, then a thesis that states the relationship between the subjects.', 'Set up both subjects; your thesis should be arguable.'], 'cmp_intro')],
      [sec('Point 1', ['Criterion, both subjects, analysis.', 'Compare, cite, then analyze.'], 'cmp_alike', 1.3), sec('Point 2', ['Criterion, both subjects, analysis.', 'A second criterion.'], 'cmp_diff', 1.3)],
      [sec('Point 3', ['Criterion, both subjects, analysis.', 'The most revealing criterion.'], 'cmp_diff', 1.3), sec('Synthesis', ['What does the pattern of likeness and difference reveal?', 'Go beyond the list: what does it mean?'], 'arg_explain', 1.3)],
      [sec('Conclusion', ['State the significance of the comparison.', 'Why should a reader care how these compare?'], 'cmp_end')]];
  }
  // summary
  if (band === 'p') return [[sec('Title', ['What is the story or book called?'], null, 0.5)], [sec('Beginning', ['What happened first?', 'Who is in it, and what happens at the start?'], 'sum_beg_p')],
    [sec('Middle', ['What happened next?', 'What was the problem?'], 'sum_mid_p')], [sec('End', ['How did it end? What is the lesson?', 'What happened last? What is the big idea?'], 'sum_end_p')]];
  if (band === 'g3' || band === 'g45') return [[sec('Opening sentence', ['Name the title, the author and the main idea.', 'Title, author and what it is mostly about.'], 'sum_open')],
    [sec('Key detail 1', ['The first important event or idea.', 'What comes first?'], 'sum_first'), sec('Key detail 2', ['The next important event or idea.', 'What comes next?'], 'sum_detail')],
    [sec('Key detail 3', ['The last important event or idea.', 'How does it end?'], 'sum_detail'), sec('Leave out', ['Small details and your own opinion do not belong. List one thing you left out.', 'What did you leave out, and why?'], null, 1)],
    [sec('Concluding sentence', ['Restate the main idea or the lesson.', 'End with the big idea.'], 'sum_end')]];
  return [[sec('Opening sentence', band === 'g912' ? ['Author, title, genre, and the central idea or claim.', 'Name the text and state its central claim or purpose.'] : ['Title, author, genre, and the central idea.', 'Name the text and state its central idea.'], 'sum_open')],
    [sec('Key point 1', ['The first key point, in your own words.', 'Paraphrase; do not copy.'], 'sum_first'), sec('Key point 2', ['The next key point.', 'How does the idea develop?'], 'sum_detail'), sec('Key point 3', ['The last key point.', 'How does the text end?'], 'sum_detail')],
    [sec(band === 'g912' ? 'How the text is built' : 'How the ideas connect', band === 'g912' ? ['How does the author develop the central idea across the text?', 'Structure: how do the parts work together?'] : ['How do the key points connect to the central idea?', 'Link the points together.'], 'arg_explain', 1)],
    [sec('Concluding sentence', ['Restate the central idea objectively.', 'End without adding your opinion.'], 'sum_end')]];
}

/* ---------- checklists (Common Core writing standards, paraphrased for students) ---------- */
const CHECK = {
  opinion: { 1: ['I name my topic or book.', 'I tell my opinion.', 'I give a reason.', 'I have an ending.', 'I start sentences with capitals and end with periods.'],
    2: ['I tell my topic and my opinion.', 'I give reasons for my opinion.', 'I use linking words like because, and, also.', 'I have a closing sentence.', 'I check capitals, spelling and end marks.'],
    3: ['I introduce my topic and state my opinion.','I give reasons that support my opinion, in an order that makes sense.', 'I use linking words like because, therefore, since and for example.', 'I end with a concluding statement.', 'I check my spelling and punctuation.'],
    4: ['I introduce my topic and state my opinion clearly.', 'Each reason is backed by facts and details.', 'I link ideas with words like for instance, in order to and in addition.', 'I group related ideas into paragraphs.', 'My conclusion connects back to my opinion.'],
    5: ['I introduce my topic and state my opinion clearly.', 'My reasons are in a logical order and backed by facts and details.', 'I link ideas with words and phrases like consequently and specifically.', 'I group related ideas into paragraphs.', 'My conclusion connects back to my opinion.'],
    6: ['I introduce my claim clearly.', 'I support it with clear reasons and relevant evidence from credible sources.', 'I use transitions to show how my claim, reasons and evidence connect.', 'I keep a formal style.', 'My conclusion follows from my argument.'],
    7: ['I introduce my claim and acknowledge an opposing claim.', 'I support my claim with logical reasoning and relevant evidence from accurate, credible sources.', 'I use transitions to show how claims, reasons and evidence connect.', 'I keep a formal style.', 'My conclusion follows from and supports my argument.'],
    8: ['I introduce my claim and set it apart from opposing claims.', 'I support my claim with logical reasoning and relevant evidence from accurate, credible sources.', 'I use transitions to show how claims, counterclaims, reasons and evidence connect.', 'I keep a formal style.', 'My conclusion follows from and supports my argument.'],
    9: ['I state a precise claim and set it apart from opposing claims.', 'I develop my claim and the counterclaim fairly, with evidence for each.', 'I point out the strengths and limits of each side.', 'I use transitions that link sections and show relationships.', 'I keep a formal style and objective tone.', 'My conclusion follows from and supports my argument.'],
    11: ['I state a precise, knowledgeable claim and show why it matters.', 'I develop claims and counterclaims fairly and thoroughly, with the most relevant evidence for each.', 'I anticipate my audience\'s knowledge, concerns, values and possible biases.', 'I use varied sentence structure to link sections and show relationships.', 'I keep a formal style and objective tone.', 'My conclusion follows from and supports my argument.'] },
  informative: { 1: ['I name my topic.', 'I give some facts about it.', 'I have an ending.', 'I start sentences with capitals and end with periods.'],
    2: ['I introduce my topic.', 'I use facts and definitions to explain it.', 'I have a closing sentence.', 'I check capitals, spelling and end marks.'],
    3: ['I introduce my topic.', 'I group related facts together.', 'I use facts, definitions and details.', 'I use linking words like also, another, and, more and but.', 'I end with a concluding statement.'],
    4: ['I introduce my topic and group related information in paragraphs.', 'I use facts, definitions, details, quotations or examples.', 'I link ideas with words like another, for example, also and because.', 'I use exact words and topic vocabulary.', 'My conclusion is about the information I gave.'],
    5: ['I introduce my topic with a general observation and focus.', 'I group related information logically.', 'I use facts, definitions, details, quotations or examples.', 'I link ideas with words and phrases like in contrast and especially.', 'I use exact words and topic vocabulary.', 'My conclusion is about the information I gave.'],
    6: ['I introduce my topic and organize ideas (definition, classification, comparison, cause and effect).', 'I develop the topic with relevant facts, definitions, details and quotations.', 'I use transitions to show how ideas connect.', 'I use precise language and topic vocabulary.', 'I keep a formal style.', 'My conclusion follows from the information I presented.'],
    7: ['I introduce my topic clearly and preview what is to follow.', 'I organize ideas (definition, classification, comparison, cause and effect).', 'I develop the topic with relevant facts, definitions, details and quotations.', 'I use transitions that create cohesion.', 'I use precise language and keep a formal style.', 'My conclusion follows from and supports the information I presented.'],
    8: ['I introduce my topic clearly and preview what is to follow.', 'I organize ideas into broader categories.', 'I develop the topic with relevant, well-chosen facts, definitions, details and quotations.', 'I use varied transitions that create cohesion.', 'I use precise language and keep a formal style.', 'My conclusion follows from and supports the information I presented.'],
    9: ['I introduce my topic and organize complex ideas to show important connections and distinctions.', 'I develop the topic with well-chosen, relevant facts, details and quotations.', 'I use varied transitions to link major sections.', 'I use precise language and topic vocabulary.', 'I keep a formal style and objective tone.', 'My conclusion follows from my explanation, for example by showing why the topic matters.'],
    11: ['I introduce my topic and organize complex ideas so each builds on the one before.', 'I develop the topic thoroughly with the most significant and relevant evidence.', 'I use varied transitions and syntax to link sections and manage complexity.', 'I use precise language and techniques like analogy to manage complexity.', 'I keep a formal style and objective tone.', 'My conclusion explains the implications or significance of the topic.'] },
  narrative: { 1: ['I tell two or more events in order.', 'I add some details.', 'I use order words like first, next, then.', 'I have an ending.'],
    2: ['I tell an event or a short set of events.', 'I add details about actions, thoughts and feelings.', 'I use order words to show when things happen.', 'I have an ending.'],
    3: ['I introduce the narrator or characters and the situation.', 'My events happen in a natural order.', 'I use dialogue and describe actions, thoughts and feelings.', 'I use time words to show the order of events.', 'I have an ending.'],
    4: ['I introduce the narrator or characters and the situation.', 'I use dialogue and description to show what happens.', 'I use transitions to show the order of events.', 'I use concrete words and sensory details.', 'My ending follows from the events.'],
    5: ['I introduce the narrator or characters and the situation.', 'I use dialogue, description and pacing.', 'I use transitions to show the order of events.', 'I use concrete words and sensory details.', 'My ending follows from the events.'],
    6: ['I set the context and introduce the narrator or characters.', 'My events unfold naturally and logically.', 'I use dialogue, pacing and description.', 'I use transitions to show order and shifts in time or setting.', 'I use precise words and sensory language.', 'My conclusion follows from the events.'],
    7: ['I set the context and point of view and introduce the narrator or characters.', 'My events unfold naturally and logically.', 'I use dialogue, pacing and description.', 'I use transitions to show order and shifts in time or setting.', 'I use precise words and sensory language.', 'My conclusion follows from and reflects on the events.'],
    8: ['I set the context and point of view and introduce the narrator or characters.', 'My events unfold naturally and logically.', 'I use dialogue, pacing, description and reflection.', 'I use transitions to show order, shifts in time or setting, and how events relate.', 'I use precise words and sensory language.', 'My conclusion follows from and reflects on the events.'],
    9: ['I set up a problem, situation or observation and a point of view.', 'I use dialogue, pacing, description, reflection and multiple plot lines.', 'I sequence events so they build on one another into a whole.', 'I use precise words, telling details and sensory language.', 'My conclusion reflects on what was experienced or resolved.'],
    11: ['I set up a problem, situation or observation and its significance.', 'I use dialogue, pacing, description, reflection and multiple plot lines.', 'I sequence events so they build toward a particular tone and outcome.', 'I use precise words, telling details and sensory language.', 'My conclusion reflects on what was experienced or resolved.'] },
  cer: { p: ['I wrote the question.', 'I told what I think.', 'I told what I saw.', 'I told why.'],
    g3: ['My claim answers the question in one sentence.', 'I give two pieces of evidence (data or observations).', 'My reasoning uses a science idea to explain why.', 'I use linking words like because, so and therefore.', 'I end with a concluding statement.'],
    g68: ['My claim is precise and answers the question.', 'My evidence is specific: numbers, units, observations.', 'My reasoning names the scientific principle that links evidence to claim.', 'I use transitions to connect claim, evidence and reasoning.', 'I keep a formal, objective style.'],
    g912: ['My claim is precise and limited to what the data support.', 'I use enough specific evidence, with numbers and units.', 'My reasoning explains the science that connects evidence and claim.', 'I address an alternate explanation fairly.', 'I name limits of my data or sources of error.', 'I keep a formal style and objective tone.'] },
  compare: { p: ['I name the two things.', 'I tell how they are alike.', 'I tell how they are different.', 'I have an ending.'],
    g3: ['I name both things in my topic sentence.', 'I tell how they are alike and how they are different.', 'I use linking words like both, also, but and another.', 'I end with a concluding statement.'],
    g45: ['I introduce both subjects.', 'I group likenesses and differences in paragraphs.', 'I use facts and details for each subject.', 'I use comparison words like both, similarly, however and in contrast.', 'My conclusion sums up how they compare.'],
    g68: ['I introduce both subjects and my main point about them.', 'I organize by points of comparison.', 'I support each point with relevant facts, details or quotations.', 'I use transitions that show similarity and difference.', 'I keep a formal style.', 'My conclusion explains why the comparison matters.'],
    g912: ['My thesis states the relationship between the subjects.', 'Each point compares both subjects with evidence.', 'I analyze, not just list: I explain what the likenesses and differences mean.', 'I use varied transitions and precise language.', 'I keep a formal style and objective tone.', 'My conclusion explains the significance of the comparison.'] },
  summary: { p: ['I tell the title.', 'I tell the important parts of the beginning, middle and end, in order.', 'I tell the lesson or big idea.', 'I use my own words.'],
    g3: ['I name the title and the main idea.', 'I tell the key details in order.', 'I use my own words.', 'I leave out small details and my opinions.'],
    g45: ['I name the title, the author and the main idea.', 'I include only the most important details.', 'I keep the details in order.', 'I use my own words.', 'I leave out my opinions.'],
    g68: ['My first sentence names the title, author and central idea.', 'I include the key points in a logical order.', 'I paraphrase in my own words.', 'I stay objective: no opinions or judgments.', 'My summary is much shorter than the original.'],
    g912: ['My first sentence names the author, title and central idea or claim.', 'I show how the central idea develops across the text.', 'I paraphrase accurately; any quotation is short and exact.', 'I stay objective: no opinions or judgments.', 'My summary is much shorter than the original.'] },
};
function checklist(genre, grade, band) {
  const pickKey = (o, keys) => { for (const k of keys) if (o[k]) return o[k]; };
  let items, code;
  if (genre === 'opinion' || genre === 'informative' || genre === 'narrative') {
    const keys = [grade, ...[11, 9, 8, 7, 6, 5, 4, 3, 2, 1].filter(k => k <= grade)];
    items = pickKey(CHECK[genre], keys);
    const w = { opinion: 1, informative: 2, narrative: 3 }[genre];
    code = `Common Core W.${grade <= 8 ? grade : grade <= 10 ? '9-10' : '11-12'}.${w}`;
  } else {
    const k = band === 'g45' && !CHECK[genre].g45 ? 'g3' : band;
    items = CHECK[genre][k] || CHECK[genre].g3;
    const gs = grade <= 8 ? grade : grade <= 10 ? '9-10' : '11-12';
    code = genre === 'cer' ? (grade <= 5 ? `Common Core W.${gs}.1, used in science` : `Common Core WHST.${grade <= 8 ? '6-8' : gs}.1`) + '; NGSS practice: arguing from evidence'
      : genre === 'compare' ? `Common Core W.${gs}.2` : (grade <= 2 ? `Common Core RL.${gs}.2 and W.${gs}.2` : `Common Core RL.${gs}.2 or RI.${gs}.2, and W.${gs}.2`);
  }
  return { items, code };
}

/* ---------- models for the teacher page (written for a sample topic at each level) ---------- */
const MODELS = {
  opinion: { p: { topic: 'Should our class get a pet fish?', text: ['I think our class should get a pet fish. One reason is that fish are easy to care for. Also, watching a fish swim helps us feel calm. That is why a fish would be a great class pet.'] },
    m: { topic: 'Should recess be longer?', text: ['In my opinion, recess should be longer. One reason is that students need time to move. For example, running and climbing help our bodies stay strong. Another reason is that recess helps us learn to get along. When we play games, we practice taking turns and solving problems. Finally, a break helps us focus. After recess, it is easier to sit still and listen. For these reasons, our school should make recess longer.'] },
    g68: { topic: 'Should middle and high schools start later?', note: 'A thesis plus one body paragraph, the part students find hardest.', text: ['Claim: Middle and high schools should start no earlier than 8:30 a.m. because teenagers need more sleep to learn well.',
      'One reason schools should start later is that teenagers\' bodies are built to fall asleep later. During puberty, the body\'s sleep cycle shifts, so many teens are not sleepy until around 11 p.m. Sleep experts recommend that teens get 8 to 10 hours of sleep a night, which is hard to do when the bus comes at 6:30 a.m. In 2014, the American Academy of Pediatrics recommended that middle and high schools start at 8:30 a.m. or later. This shows that a later start is not about laziness; it matches how teenagers\' bodies actually work.'] },
    g912: { topic: 'Should the voting age be lowered to 16?', note: 'A claim plus the counterclaim and rebuttal paragraph, the part that is new at this level.', text: ['Claim: The voting age for local elections should be lowered to 16, because the decisions made there shape teenagers\' daily lives and early voting can build a lifelong habit.',
      'Critics argue that 16-year-olds lack the maturity and knowledge to vote responsibly. It is true that teenagers are still developing, and no one wants elections decided on a whim. However, this argument sets a bar that is not applied to adults: voters are not tested on civics or judgment, and many adults vote with little information. Sixteen-year-olds can already work, pay taxes on their wages and, in most states, drive, and many take civics or government classes in high school. Places that have tried it offer a test case: Takoma Park, Maryland, opened its city elections to 16-year-olds in 2013, and Austria lowered its national voting age to 16 in 2007. Rather than proving teenagers unready, the maturity objection is a reason to give them practice while they are still in a classroom that can prepare them.'] } },
  informative: { p: { topic: 'Honeybees', text: ['I am going to tell you about honeybees. Honeybees live together in a hive. They drink nectar from flowers and use it to make honey. Also, bees carry pollen from flower to flower, which helps plants make seeds. Bees are busy helpers!'] },
    m: { topic: 'The water cycle', text: ['Have you ever wondered where rain comes from? Rain is part of the water cycle, the way water moves between Earth and the sky. First, the sun warms water in oceans, lakes and puddles. The water evaporates, which means it turns into a gas called water vapor and rises into the air. High in the sky, the air is cooler, so the vapor condenses into tiny drops that form clouds. When the drops join and grow heavy, they fall as rain, snow, sleet or hail. This is called precipitation. As you can see, the same water is used over and over again.'] },
    g68: { topic: 'Why volcanoes form where they do', note: 'A thesis plus one body paragraph.', text: ['Thesis: Most volcanoes form at the edges of Earth\'s tectonic plates, where plates pull apart or one slides beneath another, though a few form over hot spots far from any edge.',
      'The first key idea is that many volcanoes form where one plate sinks beneath another. At these subduction zones, the sinking plate carries water down into the hot mantle. The water lowers the melting point of the surrounding rock, so it melts into magma. Because magma is less dense than solid rock, it rises and can erupt at the surface. This is why a ring of volcanoes, often called the Ring of Fire, lines much of the Pacific Ocean. In other words, the volcanoes are not scattered at random; they trace the places where plates collide.'] },
    g912: { topic: 'How vaccines train the immune system', note: 'A thesis plus one body section.', text: ['Thesis: Vaccines protect against disease by giving the immune system a safe preview of a germ, so that it can respond quickly and strongly to the real thing.',
      'The first key idea is that a vaccine presents an antigen, a recognizable piece of a pathogen, without causing the disease. Depending on the vaccine, this may be a weakened or inactivated form of the germ, a single protein from its surface, or genetic instructions, such as mRNA, that tell the body\'s own cells to make that protein for a short time. The immune system responds as it would to an infection: it makes antibodies that bind to the antigen and, crucially, memory B and T cells that persist for months or years. As a result, if the person is later exposed to the actual pathogen, those memory cells recognize it and mount a faster, larger response, often clearing the infection before serious illness develops. This helps explain why vaccination works best before exposure: its value lies in the memory it leaves behind.'] } },
  narrative: { p: { topic: 'Learning to ride a bike', text: ['One day, my dad took me to the park to ride my bike. Next, he held the seat while I pedaled. Then he let go, and I did not even know! I felt so proud. Finally, I rode all the way to the big tree by myself.'] },
    m: { topic: 'The day the power went out', text: ['It all started when the lights blinked and the whole house went dark. "Mom?" I called, gripping the edge of the table. Rain drummed on the roof, and thunder rumbled far away. Mom found a flashlight and a box of candles in the hall closet. Before long, the kitchen glowed with soft yellow light. We played cards on the floor and ate peanut butter sandwiches for dinner. Just as we started a second game, the refrigerator hummed and the lights flicked back on. I was almost disappointed. Since that night, I keep a flashlight by my bed, but I secretly hope for another storm.'] },
    g68: { topic: 'A first day at a new school', note: 'An opening that sets context and point of view, then the start of the rising action.', text: ['The hallway smelled like floor wax and someone else\'s lunch. I stood by locker 214, turning the dial the way the office lady had shown me, and for the third time it would not open. Kids streamed past in groups, laughing about a summer I had not been part of.',
      'Without warning, the bell rang. I gave the lock one last yank, and it held. "It sticks," said a voice behind me. A girl with a paint-stained backpack reached past me, thumped the locker door once with her fist, and it swung open. "Thanks," I said, but she was already gone. I did not know her name yet. By the end of that week, I would know a lot more than that.'] },
    g912: { topic: 'The last summer at the lake', note: 'An opening paragraph that sets tone and point of view and hints at reflection.', text: ['That was the summer the dock began to lean. My grandfather noticed it first, the way he noticed everything about the lake: the heron that came at six, the water line on the third piling, the exact sound the screen door made when someone forgot to latch it. He did not fix the dock. I thought, at fourteen, that he was getting lazy. Only later did I understand that he was letting go of the place one board at a time, and that he had been waiting for me to notice before he said it out loud.'] } },
  cer: { p: { topic: 'What does a magnet pull?', text: ['My question: What does a magnet pull? I think a magnet pulls some metal things. I saw the magnet pick up a paper clip and a nail. It did not pick up a penny, a crayon or a ball of foil. This shows that magnets pull some metals, but not everything.'] },
    m: { topic: 'Which wrap keeps ice from melting longest? (sample data)', text: ['Our results show that the wool wrap kept the ice cube frozen longest. In our test, the cube wrapped in a wool sock took 95 minutes to melt. The cube in foil took 60 minutes, and the cube with no wrap melted in 40 minutes. This evidence supports my claim because wool traps air, and trapped air is a poor conductor of heat. The wool slowed the heat moving from the warm room into the ice. For these reasons, wool is the best wrap for keeping ice frozen.'] },
    g68: { topic: 'Does water temperature change how fast sugar dissolves? (sample data)', text: ['Our results show that sugar dissolves faster in warmer water. In our test, one teaspoon of sugar dissolved in 95 seconds in 20 °C water, in 50 seconds in 40 °C water and in 28 seconds in 60 °C water, stirring the same way each time. As the temperature went up, the time went down in every trial. This happens because water molecules move faster at higher temperatures. Faster molecules collide with the sugar crystals more often and with more energy, pulling sugar molecules away from the crystal sooner. Therefore, raising the temperature speeds up dissolving. Next, we would test whether stirring speed matters as much as temperature.'] },
    g912: { topic: 'Does light intensity affect the rate of photosynthesis? (sample data, floating leaf disk method)', text: ['Claim: Within the range tested, increasing light intensity increased the rate of photosynthesis in spinach leaf disks.',
      'Evidence and reasoning: With the lamp 10 cm away, half of the disks floated after about 6 minutes; at 30 cm, it took about 14 minutes; at 50 cm, about 25 minutes. Disks float as oxygen produced by photosynthesis collects in the air spaces of the leaf, so a shorter time to float indicates a faster rate. Light supplies the energy for the light-dependent reactions, which split water and release oxygen, so more light energy drives oxygen production faster.',
      'Alternate explanation and rebuttal: Someone might argue that heat from the closer lamp, not light, sped up the reaction. However, we placed a container of water between the lamp and the cups as a heat shield, and the cup temperature stayed within 1 °C across trials. A remaining limit is that we tested only three distances, so we cannot say where the rate levels off.'] } },
  compare: { p: { topic: 'Cats and dogs', text: ['Cats and dogs are alike because they are both pets with fur. They are different because dogs bark and cats meow. Dogs like to go on walks, but cats like to climb. I like dogs better because they play catch with me.'] },
    m: { topic: 'Alligators and crocodiles', text: ['Alligators and crocodiles look a lot alike, but they are not the same. Both are large reptiles with scaly skin, and both lay eggs. They also both hunt in and near water. However, they have some clear differences. An alligator has a wide, U-shaped snout, while a crocodile\'s snout is narrower and shaped more like a V. When a crocodile closes its mouth, some of its lower teeth still show. In addition, alligators mostly live in fresh water, but crocodiles can live in salty water too. Overall, they are close relatives with a few differences you can spot if you know where to look.'] },
    g68: { topic: 'Weather and climate', note: 'A thesis plus one body paragraph organized by a point of comparison.', text: ['Thesis: Weather and climate both describe conditions in the atmosphere, but they differ in time scale, which is why a cold week does not disprove a warming climate.',
      'The first point of comparison is time. Weather describes conditions over a short period, such as today\'s temperature, rain or wind. It can change within hours. Climate, in contrast, is the average pattern of weather in a place over a long period, usually 30 years or more. For example, one snowy day in a desert city is weather, but the fact that the city is usually dry and hot is its climate. In other words, weather is what you get on a given day, while climate is what you can expect.'] },
    g912: { topic: 'Democracy in ancient Athens and in the United States', note: 'A thesis plus one point of comparison with analysis.', text: ['Thesis: Athenian and American democracy share the principle that power comes from citizens, but they answer the question of who participates, and how, in nearly opposite ways.',
      'The clearest contrast lies in how citizens govern. In Athens, citizens voted directly on laws and war in the Assembly, and many officials were chosen by lot rather than election, on the theory that any citizen could serve. The United States, by contrast, is a representative democracy: voters elect officials who make laws on their behalf, within limits set by a written Constitution. Yet on the question of who could take part, the contrast runs the other way. Athens\'s direct power belonged to a narrow group, adult male citizens, excluding women, enslaved people and foreigners, whereas the United States has, over time and through amendments, extended the vote far more widely. The comparison suggests a trade-off: Athens offered intense participation to a few, while the United States offers less direct power to many more.'] } },
  summary: { p: { topic: 'The Tortoise and the Hare (Aesop)', text: ['At the beginning, a fast Hare makes fun of a slow Tortoise, so they have a race. In the middle, the Hare runs far ahead and takes a nap. At the end, the Tortoise keeps going and wins the race. The lesson is that slow and steady wins.'] },
    m: { topic: 'The Lion and the Mouse (Aesop)', text: ['In the fable "The Lion and the Mouse," a small mouse proves that even a little friend can be a big help. First, a lion catches a mouse that has run across his paw. The mouse begs to be let go and promises to help the lion someday. The lion laughs at the idea but lets him go. Later, the lion is caught in a hunter\'s net. The mouse hears him roar, chews through the ropes and sets him free. The lesson is that kindness is never wasted, and even the smallest creature can help.'] },
    g68: { topic: 'The Ant and the Grasshopper (Aesop)', text: ['Aesop\'s fable "The Ant and the Grasshopper" shows the importance of preparing for the future. During the summer, a grasshopper spends his days singing and playing while an ant works hard to store food. The grasshopper teases the ant for working instead of enjoying the warm weather. When winter comes, the grasshopper has nothing to eat and asks the ant for food. The ant reminds him that he chose to play while she worked. The fable concludes that those who plan ahead are ready when hard times come.'] },
    g912: { topic: 'The Gettysburg Address (Abraham Lincoln, November 19, 1863)', text: ['In the Gettysburg Address, delivered at the dedication of a soldiers\' cemetery in Gettysburg, Pennsylvania, President Abraham Lincoln argues that the best way to honor the Union dead is to finish the work they died for. He opens by recalling that the nation was founded on liberty and the proposition that all men are created equal, and he frames the Civil War as a test of whether such a nation can last. He then states that the living cannot truly consecrate the ground, because the soldiers\' sacrifice has already done so. Lincoln closes by turning the ceremony into a charge: the audience must dedicate itself to the unfinished task so that government of the people, by the people, for the people does not perish. The speech moves from past to present to future, using a brief dedication to redefine the purpose of the war.'] } },
};
const modelKey = band => band === 'p' ? 'p' : band === 'g68' ? 'g68' : band === 'g912' ? 'g912' : 'm';

const MISTAKES = {
  opinion: 'Reasons that just repeat the opinion in new words, and examples that do not connect back to the reason. At 6-12, watch for evidence dropped in with no explanation after it.',
  informative: 'Slipping in opinions ("bees are the coolest") and lists of facts with no grouping. Each paragraph or section should be about one part of the topic.',
  narrative: 'Stories that summarize ("then we had fun") instead of showing, and endings that stop rather than close. Push for one slowed-down moment with dialogue or sensory detail.',
  cer: 'A claim that is really a guess written before looking at the data, evidence with no numbers or units, and reasoning that restates the evidence instead of naming the science idea.',
  compare: 'Writing all about one subject, then all about the other, with no direct comparison. Each point should mention both subjects.',
  summary: 'Retelling every detail, copying sentences, and adding opinions ("I loved this part"). A summary should be much shorter than the text.',
};
const USE = {
  opinion: 'Have students talk through their opinion and reasons with a partner first. The starters are a menu: they can pick one, change it, or write their own.',
  informative: 'Students do better when the research is done first. Have them sort notes into the sections before drafting.',
  narrative: 'Brainstorm a small moment, not a whole day or trip. A small moment told in detail beats a long list of events.',
  cer: 'Use after a lab or with a provided data table. The question can be yours or the class\'s. Model the reasoning section aloud the first time.',
  compare: 'Pair it with the Venn or compare-and-contrast organizer from the Graphic Organizer Maker as a planning step.',
  summary: 'Use after reading a short text the whole class knows. Have students underline the key points in the text first, then write.',
};
const NAMES = { opinion: 'Opinion Writing', informative: 'Informative Writing', narrative: 'Narrative Writing', cer: 'Claim, Evidence, Reasoning', compare: 'Compare and Contrast Writing', summary: 'Summary Writing' };

const CSS = `
.wf-sec { border: 1.5px solid #222; border-radius: 8px; padding: .05in .1in .07in; break-inside: avoid; display: flex; flex-direction: column; background: #fff; }
.wf-row { display: grid; gap: .12in; margin: .1in 0; }
.wf-head { margin: 0; line-height: 1.3; }
.wf-lab { font: 700 12.5px/1.3 var(--sans); text-transform: uppercase; letter-spacing: .06em; margin-right: 4px; }
.wf-q { font-size: 12.5px; color: #444; font-style: italic; }
.wf-try { margin: 2px 0 0; font-size: 12.5px; }
.wf-try b { font-weight: 600; }
.wf-try i { margin-right: 2px; }
.wf-try .wf-sep { color: #999; margin: 0 4px; }
.wf-lines { margin-top: auto; }
.wf-lines span { display: block; height: var(--lh); border-bottom: 1px solid #888; position: relative; }
.wf-lines span i { position: absolute; left: 0; bottom: 2px; font-size: 13px; color: #555; white-space: nowrap; }
.wf-p .wf-lines span::after { content: ''; position: absolute; left: 0; right: 0; top: 50%; border-top: 1px dashed #bbb; }
.wf-p .wf-lines span i { font-size: 16px; }
.wf-p .wf-lab { font-size: 16px; text-transform: none; letter-spacing: 0; }
.wf-p .wf-q { font-size: 14px; }
.wf-draw { border: 1px dashed #888; border-radius: 6px; margin: 4px 0; position: relative; }
.wf-draw span { position: absolute; left: 6px; top: 3px; font-size: 10.5px; color: #888; }
.wf-topic { margin: 0 0 4px; font-size: 14px; display: flex; gap: 6px; align-items: baseline; }
.wf-topic span { flex: 1; border-bottom: 1.5px solid #222; height: 1.1em; }
.wf-bank { display: flex; flex-wrap: wrap; gap: 3px 14px; border: 1.5px dashed #555; border-radius: 6px; padding: 4px 10px; margin: 4px 0 6px; font-size: 13px; }
.wf-bank b { font-weight: 700; margin-right: 2px; }
.wf-check { border-top: 1.5px solid #222; margin-top: .1in; padding-top: 4px; break-inside: avoid; }
.wf-check-h { margin: 0 0 3px; font: 700 12.5px var(--sans); }
.wf-check-h span { font-weight: 400; color: #555; }
.wf-check ul { list-style: none; padding: 0; margin: 0; columns: 2; column-gap: 22px; font-size: 12.5px; }
.wf-check li { margin: 0 0 3px; break-inside: avoid; padding-left: 1.4em; text-indent: -1.4em; }
.wf-check li::before { content: ''; display: inline-block; width: .85em; height: .85em; border: 1.5px solid #333; border-radius: 2px; margin-right: .5em; vertical-align: -1px; }
.wf-p .wf-check ul { font-size: 14px; }
.wf-model { border-left: 4px solid #333; padding: 2px 0 2px 12px; margin: 6px 0; }
.wf-model p { margin: 0 0 6px; line-height: 1.5; }
.wf-cont { break-before: page; }
`;

Gen.add('writing-frame', {
  title: 'Writing Frames', type: 'Writing frame', noKey: true, css: CSS,
  fields: [
    { id: 'grade', label: 'Grade', type: 'select', options: GRADES, def: '4' },
    { id: 'genre', label: 'Kind of writing', type: 'select', options: GENRES, def: 'opinion' },
    { id: 'topic', label: 'Topic or prompt (optional)', type: 'text', def: '' },
    { id: 'space', label: 'Writing space', type: 'select', options: [['plan', 'Planning frame (1 page)'], ['draft', 'Drafting frame (2 pages)']], def: 'plan' },
  ],
  make(v, r) {
    const grade = +v.grade, band = bandOf(grade), genre = v.genre, topic = String(v.topic || '').trim(), draft = v.space === 'draft';
    const gk = `${genre}-${grade === 1 ? "p1" : band}`, lh = LH[band], g = GROW[`${gk}-${v.space}`] || (draft ? (GROW[`${gk}-plan`] || 1) : 1);
    const base = { p: 1.32, g3: 0.72, g45: 0.68, g68: 0.6, g912: 0.56 }[band] * (draft ? 2.3 : 1) * g * (topic.length > 85 ? 0.96 : 1);
    const lines = (n, starter) => {
      return `<div class="wf-lines" style="--lh:${lh}in">${Array.from({ length: n }, (_, i) => `<span>${i === 0 && starter ? `<i>${esc(starter)}</i>` : ''}</span>`).join('')}</div>`; };
    const rows = frame(genre, band, grade, r);
    // share whole lines across rows (largest remainder), so the page total tracks the target instead of jumping by a line per box
    const want = rows.map(row => base * Math.max(...row.map(s => s.w)) * (row.length > 1 ? 1.25 : 1) / lh);
    const rowN = want.map(x => Math.max(band === 'g68' || band === 'g912' ? 2 : 1, Math.floor(x)));
    let spare = Math.round(want.reduce((a, b) => a + b, 0)) - rowN.reduce((a, b) => a + b, 0);
    want.map((x, i) => [x - Math.floor(x), i]).sort((a, b) => b[0] - a[0] || a[1] - b[1]).forEach(([, i]) => { if (spare > 0) { rowN[i]++; spare--; } });
    const html = rows.map((row, ri) => {
      const cells = row.map(s => {
        const q = r.pick(s.q);
        let tryLine = '', first = '';
        if (s.st && band === 'p') first = r.pick(S[s.st]);
        else if (s.st) {
          const n = row.length > 1 ? 2 : 3;
          const pool = r.sample(S[s.st], Math.min(n, S[s.st].length)).concat(s.sub ? r.sample(S[s.sub], row.length > 1 ? 1 : 2) : []);
          tryLine = `<p class="wf-try"><b>Try:</b> ${[...new Set(pool)].map(x => `<i>${esc(x)}</i>`).join('<span class="wf-sep">/</span>')}</p>`;
        }
        return `<div class="wf-sec"><p class="wf-head"><span class="wf-lab">${esc(s.lab)}</span> <span class="wf-q">${esc(q)}</span></p>${tryLine}${lines(rowN[ri], first)}</div>`;
      });
      return `<div class="wf-row" style="grid-template-columns:repeat(${row.length}, 1fr)">${cells.join('')}</div>`;
    });
    // grade 1 draws a picture first; drafting frames break onto the second page halfway through the sections
    if (grade === 1) html.unshift(`<div class="wf-sec"><p class="wf-head"><span class="wf-lab">Draw your idea</span> <span class="wf-q">${esc(r.pick(['Draw first. Then write.', 'Draw a picture of what you will write about.']))}</span></p><div class="wf-draw" style="height:${(draft ? 2.6 : 1.5) * g}in"><span>Draw</span></div></div>`);
    if (draft && html.length > 2) {   // break before the row that best balances the two pages (page 1 carries the header, page 2 the checklist)
      const est = [...(grade === 1 ? [2.6 * g + 0.4] : []), ...rowN.map(n => n * lh + 0.5)], tot = est.reduce((x, y) => x + y, 0);
      let at = 1, best = 1e9, cum = 0;
      for (let i = 1; i < est.length; i++) { cum += est[i - 1]; const worst = Math.max(2.4 + cum, 1.2 + tot - cum); if (worst < best) { best = worst; at = i; } }
      html[at] = html[at].replace(/^<div class="wf-(row|sec)"/, '<div class="wf-$1 wf-cont"');
    }
    const tb = TRANS[genre][band === 'g45' ? 'g45' : band];
    const bank = tb ? `<div class="wf-bank"><b>${genre === 'narrative' ? 'Time words' : 'Linking words'}:</b> ${r.sample(tb, band === 'g3' ? 6 : 8).map(esc).join(' · ')}</div>` : '';
    const topicLine = topic ? (topic.length > 55 ? `<p class="wf-topic"><b>Topic:</b> ${esc(topic)}</p>` : '')
      : `<p class="wf-topic"><b>${genre === 'summary' ? 'Text I am summarizing' : genre === 'cer' ? 'Investigation' : 'My topic'}:</b><span></span></p>`;
    const ck = checklist(genre, grade, band);
    const check = `<div class="wf-check"><p class="wf-check-h">Checklist <span>(${esc(ck.code)})</span></p><ul>${ck.items.map(x => `<li>${esc(x)}</li>`).join('')}</ul></div>`;

    const genreLabel = genre === 'opinion' && grade >= 6 ? 'Argument' : genre === 'summary' && grade <= 2 ? 'Retell' : GENRES.find(x => x[0] === genre)[1].replace(/ \/.*$/, '').replace(' (science)', '');
    const structure = { p: 'a few sentences', g3: 'one paragraph', g45: 'a short multi-paragraph piece', g68: 'a five-part essay', g912: 'a full essay' }[band];
    const m = MODELS[genre][modelKey(band)];
    const directions = band === 'p' ? `${grade === 1 ? 'Draw your idea first. Then write' : 'Write'} a sentence in each box. You can use the words on the first line to start.`
      : `Plan ${structure}: write in each box, in order.${band === 'g3' ? ' Then copy your sentences as one paragraph.' : ''} Pick a starter from "Try" or begin your own way. Check the list at the bottom when you finish.`;
    const ican = { opinion: grade >= 6 ? 'I can write an argument that supports a claim with reasons and evidence.' : 'I can write my opinion and give reasons.',
      informative: 'I can write to teach a reader about a topic.', narrative: 'I can write a story with events in order and details that show what happens.',
      cer: 'I can answer a science question with a claim, evidence and reasoning.', compare: 'I can write about how two things are alike and different.',
      summary: grade <= 2 ? 'I can retell the important parts of a story.' : 'I can summarize a text in my own words.' }[genre];
    const teacher = `<h3>Model: ${esc(m.topic)}</h3><p>Written for this level${m.note ? '. ' + esc(m.note) : ''}. Read it aloud and have students find each part of the frame in it.</p>` +
      `<div class="wf-model">${m.text.map(p => `<p>${esc(p)}</p>`).join('')}</div>`;
    return {
      title: (topic && topic.length <= 55) ? topic : `${genreLabel === 'Argument' ? 'Argument Writing' : genreLabel === 'Retell' ? 'Retell' : NAMES[genre]} Frame`,
      eyebrow: `Writing frame · ${genreLabel}`, level: `Grade ${grade}`,
      ican, directions, minutes: band === 'p' ? 20 : draft ? 45 : 30, materials: 'pencil' + (genre === 'cer' ? ', your data or notes' : genre === 'summary' ? ', the text' : ''),
      parts: [['', `<div class="wf wf-${band}">${topicLine}${bank}${html.join('')}${check}</div>`]], items: [],
      mistakes: MISTAKES[genre],
      notes: `${USE[genre]} This frame builds ${structure}; the checklist matches ${esc(ck.code)}. The starters and linking words change with each New sheet. ${draft ? 'The drafting frame gives room for full sentences across two pages.' : 'Choose the drafting frame for more room to write.'}`,
      teacher,
    };
  },
});
})();
