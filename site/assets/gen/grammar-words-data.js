// Word and sentence banks for the Grammar and Word Study generator (grammar-words.js), loaded before it.
// Every item is hand-written and tagged; the generator's verify() re-checks the tags with spelling and grammar rules
// where a rule exists (verb forms, contractions, comparatives, suffix spelling, possessives, comma and quotation
// marks, word parts), so a mistyped bank line fails the checker instead of reaching a key.
Gen.gw = {
  // base, -s form, past, past participle, -ing form; S = stress on the last syllable (doubles before a vowel suffix)
  verbs: `jump jumps jumped jumped jumping|walk walks walked walked walking|play plays played played playing
help helps helped helped helping|look looks looked looked looking|kick kicks kicked kicked kicking
cook cooks cooked cooked cooking|pull pulls pulled pulled pulling|paint paints painted painted painting
call calls called called calling|clean cleans cleaned cleaned cleaning|open opens opened opened opening
visit visits visited visited visiting|finish finishes finished finished finishing|learn learns learned learned learning
start starts started started starting|score scores scored scored scoring|live lives lived lived living
flood floods flooded flooded flooding|fix fixes fixed fixed fixing|race races raced raced racing
carry carries carried carried carrying|bake bakes baked baked baking|hop hops hopped hopped hopping
clap claps clapped clapped clapping|cry cries cried cried crying|smile smiles smiled smiled smiling
stop stops stopped stopped stopping|wash washes washed washed washing|watch watches watched watched watching
dance dances danced danced dancing|push pushes pushed pushed pushing|climb climbs climbed climbed climbing
listen listens listened listened listening|talk talks talked talked talking|plant plants planted planted planting
go goes went gone going|run runs ran run running|eat eats ate eaten eating|see sees saw seen seeing
take takes took taken taking|write writes wrote written writing|sing sings sang sung singing
swim swims swam swum swimming|make makes made made making|build builds built built building
find finds found found finding|ride rides rode ridden riding|bring brings brought brought bringing
think thinks thought thought thinking|teach teaches taught taught teaching|catch catches caught caught catching
fly flies flew flown flying|drink drinks drank drunk drinking|give gives gave given giving
come comes came come coming|begin begins began begun beginning S|grow grows grew grown growing
know knows knew known knowing|sit sits sat sat sitting|buy buys bought bought buying
sleep sleeps slept slept sleeping|tell tells told told telling|throw throws threw thrown throwing
draw draws drew drawn drawing|sell sells sold sold selling|drive drives drove driven driving
leave leaves left left leaving|read reads read read reading|rise rises rose risen rising
set sets set set setting|have has had had having|do does did done doing|win wins won won winning`,
  // regular verbs a first grader can use with no spelling change, then grade 2 adds spelling changes
  tense1: 'jump walk play help look kick cook pull paint call clean listen talk climb plant',
  tense2: 'bake hop clap cry smile stop wash watch dance push carry race',
  tense3: 'go run eat see take write sing swim make build find ride bring think teach catch fly drink give come grow know sit buy sleep tell throw draw sell drive',

  // change to past tense: present sentence | the verb's base form
  tensechange: ['Our town builds a new library.|build', 'We go to the market on Saturday.|go', 'The baker makes fresh bread.|make', 'Kids play in the park.|play',
    'The bus stops at the corner.|stop', 'Farmers grow corn near the river.|grow', 'Mia rides her bike to school.|ride', 'The mayor gives a speech.|give',
    'People sell fruit at the market.|sell', 'The train comes at noon.|come', 'My brother catches the ball.|catch', 'We eat lunch at the diner.|eat',
    'The children sing a song.|sing', 'The store opens at nine.|open', 'Dad drives us to the lake.|drive', 'Workers fix the old bridge.|fix',
    'The town has one school.|have', 'Leo writes a letter to Grandma.|write', 'The river floods every spring.|flood', 'We find shells on the beach.|find',
    'The fire truck races down the street.|race', 'Ana carries the basket.|carry', 'The class plants a tree.|plant', 'My grandpa teaches me to fish.|teach'],
  // perfect tenses: sentence with ___ | base verb | tense (prp present perfect, pp past perfect, fp future perfect) | subject (s takes has, p takes have)
  perfect: ['By the time we arrived, the movie ___.|start|pp|s', 'Maya ___ Chicago twice.|visit|prp|s', 'By next June, I ___ fifth grade.|finish|fp|p',
    'The students ___ three essays this year.|write|prp|p', 'Before the storm hit, the farmers ___ the cows inside.|bring|pp|p', 'By 8:00, the bakery ___ all the bread.|sell|fp|s',
    'We ___ each other since kindergarten.|know|prp|p', 'Leo ___ lunch before practice started.|eat|pp|s', 'By Friday, our class ___ the whole book.|read|fp|s',
    'My dog ___ three new tricks.|learn|prp|s', 'The bus ___ when we reached the corner.|leave|pp|s', 'By the end of the season, Ana ___ twenty goals.|score|fp|s',
    'They ___ in this town for five years.|live|prp|p', 'Before the rescue boat came, the river ___ two feet.|rise|pp|s', 'By the time you get home, I ___ my room.|clean|fp|p',
    'She ___ on a plane only once.|fly|prp|s', 'The sun ___ before we got back to camp.|set|pp|s', 'My parents ___ a new car.|buy|prp|p'],

  // capitals and end marks: the corrected sentence (the sheet prints it all lower case with no end mark)
  caps: ['My dog likes to run.', 'Sam and I went to the park.', 'We live on Oak Street.', 'Is it time for lunch?',
    'Look at that big frog!', 'Mom made soup for dinner.', 'Can Lily come over today?', 'I like to read books.',
    'We go to school on Monday.', 'Ben has a red kite.', 'Did you see the moon?', 'Grandma lives in Texas.',
    'We saw a bird in the tree.', 'My birthday is in May.', 'Can you help me?', 'Max and I play tag.',
    'The bus is late today.', 'Where is my hat?', 'Ana and I like to paint.', 'We went to Lake Erie in June.',
    'Our class visited the zoo on Friday.', 'Is Dr. Lee here today?', 'I have a cat named Pepper.', 'Wow, that is a tall tree!'],
  // end marks: chosen by a rule on the first word (question words ask, a strong feeling word exclaims)
  endmark: ['The dog is brown', 'I like to swim', 'We have a new baby', 'My dad is a nurse', 'The sun is hot', 'Ben has two cats',
    'We read a book', 'The frog is green', 'My hat is red', 'We go to the park',
    'Can you play with me', 'Where is my hat', 'Do you like cake', 'What is your name', 'Is it time to go', 'Who is at the door',
    'How old are you', 'Did you see the bird', 'Are you ready', 'Will you help me',
    'Wow, look at that big fish', 'Oh no, the milk spilled', 'Hooray, we won', 'Ouch, that hurts', 'Yay, it is snowing', 'Help, my kite is stuck'],
  // kinds of sentences; ^ marks a command
  kinds: ['The library opens at nine.', 'My cat sleeps on my bed.', 'We are going to the zoo on Friday.', 'Bats sleep during the day.',
    'Owls hunt at night.', 'My brother plays the drums.', 'Where did you put the glue?', 'Can you hear the rain?',
    'How many legs does a spider have?', 'Is it your turn?', 'Are you ready for the test?', 'Who wants to read first?',
    '^Please hand me the scissors.', '^Put your coat on the hook.', '^Line up at the door.', '^Turn to page ten.',
    '^Wash your hands before lunch.', '^Close the window, please.', 'What a beautiful sunset that is!', 'That was the best game ever!',
    'I can\'t believe we won!', 'How tall that giraffe is!', 'The bus is finally here!', 'This is the best day ever!'],
  // and, but, or: first sentence | second sentence | joining word
  conj: ['Sam likes apples.|Mia likes pears.|and', 'The sun came out.|We went to the park.|and', 'I can ride a bike.|My brother can skate.|and',
    'Dad made pancakes.|Mom cut the fruit.|and', 'The bell rang.|The kids lined up.|and', 'We clapped our hands.|The band played a song.|and',
    'Ana fed the fish.|Leo walked the dog.|and',
    'I wanted to play outside.|It was raining.|but', 'The dog is big.|It is very gentle.|but', 'Ana ran fast.|She did not win the race.|but',
    'I like soup.|My sister does not like it.|but', 'The box was heavy.|Leo lifted it.|but', 'We looked for my hat.|We could not find it.|but',
    'The cake looked good.|It tasted bad.|but',
    'We can play a game.|We can read a book.|or', 'Do you want milk?|Do you want juice?|or', 'You can draw a cat.|You can draw a dog.|or',
    'We can walk to school.|Dad can drive us.|or', 'Will you sing a song?|Will you dance?|or', 'Is the box under the bed?|Is it in the closet?|or'],
  names: 'I Sam Mia Dad Mom Ana Leo Lily Ben Max Grandma',

  // parts of speech: [word:tag] marks a tagged word
  pos: ['The [hungry:adj] [puppy:n] [chewed:v] my shoe.', '[She:pron] [quickly:adv] [opened:v] the [door:n].',
    'We played [under:prep] the [tall:adj] tree.', '[Wow:interj], that [rocket:n] is [loud:adj]!',
    'Leo [and:conj] Mia [walked:v] [slowly:adv] home.', 'The [bright:adj] sun [warmed:v] the [sand:n].',
    '[They:pron] sang [happily:adv] [at:prep] the party.', 'I wanted a snack, [but:conj] the [kitchen:n] was [empty:adj].',
    '[Oops:interj], [I:pron] [dropped:v] my pencil.', 'A [small:adj] [bird:n] [sat:v] [on:prep] the fence.',
    'The [students:n] [listened:v] [carefully:adv] to the story.', '[He:pron] put his boots [by:prep] the door.',
    'The [old:adj] dog [slept:v] [near:prep] the fire.', 'You can have soup [or:conj] a [sandwich:n].',
    'My [grandmother:n] [bakes:v] [delicious:adj] bread.', 'The [wind:n] howled [loudly:adv] [during:prep] the storm.',
    '[Hooray:interj], [we:pron] [won:v] the game!', 'The [clever:adj] fox [jumped:v] [over:prep] the log.',
    'Ana [painted:v] a [colorful:adj] [picture:n].', '[It:pron] [rained:v] [yesterday:adv].',
    'The [cold:adj] water [splashed:v] [against:prep] the rocks.', 'My [brother:n] [often:adv] [reads:v] comics.',
    '[Ouch:interj], the [stove:n] is [hot:adj]!', 'Sam was tired, [so:conj] [he:pron] [went:v] to bed.',
    'The [playful:adj] kittens [chased:v] the [yarn:n].', 'The [team:n] [practiced:v] [hard:adv] [before:prep] the game.',
    'Please put the books [into:prep] the [box:n].', 'The [huge:adj] [truck:n] [rumbled:v] [down:prep] the road.',
    '[We:pron] [waited:v] [patiently:adv] for the bus.', 'The [baby:n] [giggled:v] [softly:adv].',
    'Dad [fixed:v] the [wobbly:adj] chair.', '[Yikes:interj], a [spider:n] [crawled:v] up the wall!',
    'The museum was closed, [yet:conj] we had fun.', '[Everyone:pron] [cheered:v] [for:prep] the [runners:n].',
    'The [shiny:adj] [coin:n] [fell:v] [behind:prep] the couch.', '[Mia:n] [writes:v] [neatly:adv].',
    'The [gentle:adj] horse [ate:v] an apple [from:prep] my hand.', '[They:pron] [built:v] a [sturdy:adj] fort.',
    '[Hey:interj], [you:pron] forgot your lunch!', 'We wanted to swim, [but:conj] the pool was [cold:adj].'],

  // collective nouns: collective | noun | other collective words that also fit the noun
  collective: ['herd|cows|', 'flock|sheep|herd', 'school|fish|', 'pack|wolves|', 'swarm|bees|', 'pride|lions|', 'litter|puppies|',
    'bunch|bananas|', 'pod|whales|', 'colony|ants|swarm', 'deck|cards|pack', 'bouquet|flowers|bunch', 'gaggle|geese|flock', 'band|musicians|',
    'crew|sailors|', 'troop|monkeys|', 'stack|pancakes|', 'team|players|'],

  // comparatives: adjective | comparative | superlative
  comp: ['tall|taller|tallest', 'fast|faster|fastest', 'big|bigger|biggest', 'hot|hotter|hottest', 'sad|sadder|saddest',
    'happy|happier|happiest', 'funny|funnier|funniest', 'busy|busier|busiest', 'large|larger|largest', 'nice|nicer|nicest',
    'brave|braver|bravest', 'cold|colder|coldest', 'small|smaller|smallest', 'loud|louder|loudest', 'strong|stronger|strongest',
    'wet|wetter|wettest', 'thin|thinner|thinnest', 'early|earlier|earliest', 'heavy|heavier|heaviest', 'beautiful|more beautiful|most beautiful',
    'careful|more careful|most careful', 'famous|more famous|most famous', 'exciting|more exciting|most exciting',
    'curious|more curious|most curious', 'dangerous|more dangerous|most dangerous', 'colorful|more colorful|most colorful',
    'good|better|best', 'bad|worse|worst', 'far|farther|farthest', 'many|more|most',
    'safe|safer|safest', 'quick|quicker|quickest', 'dry|drier|driest', 'sunny|sunnier|sunniest', 'difficult|more difficult|most difficult'],
  irrComp: 'good better best|bad worse worst|far farther farthest|little less least|many more most',

  // contractions (the rule builds each one; verify re-derives it)
  contract1: ['do not', 'is not', 'cannot', 'I am', 'it is', 'I will', 'we are', 'did not', 'you are', 'he is', 'she is', 'that is', 'let us', 'was not', 'are not', 'has not'],
  contract2: ['will not', 'they are', 'we will', 'I have', 'you have', 'they have', 'we have', 'could not', 'should not', 'would not', 'does not',
    'were not', 'have not', 'what is', 'she will', 'they will', 'I would', 'you would', 'he would', 'you will', 'there is', 'who is'],

  // possessives: owner | owner is plural (1/0) | thing | thing is plural (1/0)
  poss: ['dog|0|bone|0', 'dogs|1|bowls|1', 'girl|0|backpack|0', 'girls|1|coats|1', 'children|1|toys|1', 'teacher|0|desk|0',
    'teachers|1|meeting|0', 'cat|0|whiskers|1', 'bird|0|nest|0', 'birds|1|songs|1', 'baby|0|blanket|0', 'babies|1|bottles|1',
    'men|1|team|0', 'women|1|choir|0', 'mice|1|cheese|0', 'sister|0|room|0', 'brothers|1|bikes|1', 'team|0|bus|0',
    'players|1|helmets|1', 'farmer|0|tractor|0', 'horses|1|barn|0', 'people|1|votes|1', 'boy|0|shoes|1', 'kittens|1|basket|0'],

  // subject-verb agreement: sentence with ___ | singular verb | plural verb | s or p | first grade
  sva: ['The dog ___ at the mail carrier.|barks|bark|s|2', 'The dogs ___ at the mail carrier.|barks|bark|p|2',
    'My sister ___ to school.|walks|walk|s|2', 'The birds ___ in the morning.|sings|sing|p|2', 'Leo ___ his bike every day.|rides|ride|s|2',
    'We ___ soccer after school.|plays|play|p|2', 'She ___ the plants on Monday.|waters|water|s|2', 'They ___ pizza on Fridays.|eats|eat|p|2',
    'The baby ___ when she is hungry.|cries|cry|s|2', 'The kids ___ at the joke.|laughs|laugh|p|2', 'My shoes ___ wet.|is|are|p|2',
    'He ___ his homework at night.|does|do|s|2', 'The flowers ___ in spring.|blooms|bloom|p|2', 'Sam and Mia ___ in the band.|plays|play|p|3',
    'Math ___ my favorite subject.|is|are|s|3', 'The girl with the red boots ___ fast.|runs|run|s|4', 'The box of crayons ___ on the shelf.|is|are|s|4',
    'The books on the table ___ mine.|is|are|p|4', 'There ___ three apples in the bowl.|is|are|p|4', 'The teacher and the students ___ ready.|is|are|p|4',
    'One of my friends ___ a pet snake.|has|have|s|5', 'Each of the players ___ a water bottle.|has|have|s|5', 'Everyone ___ the new teacher.|likes|like|s|5',
    'Neither Ana nor her brothers ___ the answer.|knows|know|p|6', 'Either my parents or my aunt ___ us up after practice.|picks|pick|s|6',
    'The list of chores ___ on the fridge.|hangs|hang|s|6', 'The leaves on that old tree ___ red in the fall.|turns|turn|p|5'],

  // pronouns: sentence | options | answer
  pronoun: ['Maya lost ___ jacket at the park.|her/their/his|her', 'The boys packed ___ lunches.|his/their/its|their',
    'The bird built ___ nest in the tree.|its/their/it\'s|its', 'My parents said ___ would be home soon.|he/they/it|they',
    'Leo and I finished ___ project early.|our/their/them|our', 'The cats licked ___ paws.|its/their/they|their',
    'Grandpa fixed the gate and painted ___.|them/it/him|it', 'Ana gave the books to Sam, and he thanked ___.|she/her/hers|her',
    '___ and I are going to the game.|Him/He|He', 'Mom drove Ben and ___ to school.|I/me|me', 'Dad and ___ planted tomatoes.|I/me|I',
    'The coach gave ___ new uniforms.|we/us|us', '___ students cleaned the park.|We/Us|We', 'Between you and ___, this puzzle is hard.|I/me|me',
    'Sam and ___ built a snow fort.|she/her|she', 'The teacher asked ___ and me to help.|him/he|him', 'The tree lost all of ___ leaves.|its/their/it\'s|its',
    'When the students arrived, ___ hung up their coats.|they/he/it|they', 'Jamal called his sister, but ___ did not answer.|she/he/they|she',
    'The puppies chased ___ tails.|its/their/his|their'],

  // homophones and often-confused words: sentence | options | answer | first grade
  homophone: ['The kids left ___ coats on the bus.|their/there/they\'re|their|2', 'Put the box over ___.|their/there/they\'re|there|2',
    '___ going to the park after lunch.|Their/There/They\'re|They\'re|2', 'Can I come ___?|to/too/two|too|2', 'We have ___ cats and a dog.|to/too/two|two|2',
    'Let\'s walk ___ the store.|to/too/two|to|2', 'Is this ___ backpack?|your/you\'re|your|2', '___ my best friend.|Your/You\'re|You\'re|2',
    'I can ___ the birds singing.|hear/here|hear|2', 'Come over ___ and sit down.|hear/here|here|2', 'Please ___ your name on the paper.|write/right|write|2',
    'Turn ___ at the stop sign.|write/right|right|2', 'Do you ___ the answer?|know/no|know|2', 'There is ___ milk left.|know/no|no|2',
    'I ___ a sandwich for lunch.|ate/eight|ate|2', 'My sister is ___ years old.|ate/eight|eight|2', 'We went to the ___ to swim.|sea/see|sea|2',
    'Can you ___ the moon?|sea/see|see|2', 'The ___ is shining today.|sun/son|sun|2', 'Mr. Lee walked with his ___.|sun/son|son|2',
    'I ate a juicy ___.|pear/pair|pear|2', 'I need a new ___ of shoes.|pear/pair|pair|2', 'Dad wants to ___ a new car.|buy/by/bye|buy|2',
    'The cat sleeps ___ the window.|buy/by/bye|by|2', 'Wave and say ___ to Grandma.|buy/by/bye|bye|2', 'A bee landed on the ___.|flower/flour|flower|2',
    'We need ___ to bake bread.|flower/flour|flour|2', 'The dog wagged ___ tail.|its/it\'s|its|4', '___ raining outside.|Its/It\'s|It\'s|4',
    'My bike is faster ___ yours.|than/then|than|4', 'First we ate, and ___ we played.|than/then|then|4', '___ coat is this?|Whose/Who\'s|Whose|4',
    '___ coming to the party?|Whose/Who\'s|Who\'s|4', 'Check the ___ before the hike.|weather/whether|weather|4', 'I can\'t decide ___ to stay or go.|weather/whether|whether|4',
    'Don\'t ___ your library card.|lose/loose|lose|4', 'My front tooth is ___.|lose/loose|loose|4', 'Everyone went on the trip ___ Sam.|accept/except|except|6',
    'I ___ your apology.|accept/except|accept|6', 'How did the storm ___ the crops?|affect/effect|affect|6', 'The medicine had a strong ___.|affect/effect|effect|6',
    'The ___ greeted every student at the door.|principal/principle|principal|6', 'Honesty is an important ___.|principal/principle|principle|6',
    'The bus was ___ at the red light.|stationary/stationery|stationary|7', 'I wrote the letter on fancy ___.|stationary/stationery|stationery|7'],

  // relative pronouns: sentence | options | answer
  relpron: ['The girl ___ won the race is my cousin.|who/which/whose|who', 'The boy ___ bike was stolen called the police.|who/which/whose|whose',
    'Our school, ___ was built in 1950, has a new roof.|who/which/whose|which', 'I like the book ___ you gave me.|that/who/whose|that',
    'The doctor ___ helped me was kind.|who/which/whose|who', 'Ms. Lee, ___ class went on a trip, smiled at us.|who/which/whose|whose',
    'The river, ___ flows past our town, is very wide.|who/which/whose|which', 'We met a man ___ owns a bakery.|who/which/whose|who',
    'The dog ___ tail is fluffy is named Max.|that/who/whose|whose', 'The cake ___ Dad baked was delicious.|that/who/whose|that',
    'My bike, ___ is red, has a flat tire.|who/which/whose|which', 'The students ___ finished early read quietly.|who/which/whose|who',
    'The author ___ book we read visited our class.|who/which/whose|whose', 'The game ___ we played was fun.|that/who/whose|that',
    'Our town library, ___ opened last year, has a garden.|who/which/whose|which', 'I have a friend ___ speaks three languages.|who/which/whose|who'],

  // commas: the corrected sentence | kind
  commas: ['We packed apples, bread, and cheese.|series', 'Mia likes to swim, run, and jump rope.|series', 'The flag is red, white, and blue.|series',
    'Bring a pencil, a ruler, and an eraser.|series', 'Ducks, geese, and swans swam in the pond.|series', 'Leo fed the cat, washed the dishes, and made his bed.|series',
    'We saw lions, tigers, and bears at the zoo.|series', 'I wanted to go to the beach, but my brother wanted to stay home.|compound',
    'We can eat lunch now, or we can wait until noon.|compound', 'The puppy chewed my shoe, so Mom put it in its crate.|compound',
    'Ana studied hard for the test, and she got every answer right.|compound', 'The movie was long, but we enjoyed every minute.|compound',
    'The store was closed, so we went home.|compound', 'My dad likes to cook, and my mom likes to bake.|compound',
    'After the long game, the team rested.|intro', 'When the bell rang, the students ran outside.|intro', 'If it snows tomorrow, we will build a fort.|intro',
    'Because the road was icy, Dad drove slowly.|intro', 'However, the bus was late.|intro', 'First, read all of the directions.|intro',
    'Yes, I would like more soup.|yesno', 'No, the library is closed today.|yesno', 'Well, that was a surprise.|yesno',
    'Sam, please pass the salt.|address', 'Thank you for your help, Mrs. Diaz.|address', 'Can you help me, Leo?|address', 'I think, Ana, that you are right.|address',
    'It is cold today, isn\'t it?|tag', 'You finished your homework, didn\'t you?|tag', 'That was a great game, wasn\'t it?|tag', 'We can go now, can\'t we?|tag',
    'We moved here on June 5, 2019.|date', 'The fair opened on July 1, 2024, and closed a week later.|date', 'My cousin was born on March 12, 2015.|date',
    'My aunt lives in Denver, Colorado.|place', 'We visited Paris, France, last summer.|place', 'The museum is in Chicago, Illinois.|place',
    'Mom said, "Dinner is ready."|quote', '"I love this song," said Ana.|quote', 'The coach shouted, "Run faster!"|quote', '"We should leave now," said Dad.|quote',
    'Our garden has carrots, beans, and peas.|series', 'Tim packed socks, shirts, and shoes.|series', 'The baby can clap, wave, and smile.|series',
    'Owls, bats, and moths fly at night.|series', 'We need glue, tape, and scissors.|series', 'Nora sang, danced, and played the drum.|series',
    'The soup has rice, corn, and beans in it.|series', 'Maple, oak, and pine trees grow here.|series',
    'The rain stopped, and the sun came out.|compound', 'I called Grandma, but she was not home.|compound', 'You can read a book, or you can draw.|compound',
    'The ice melted, so the pond was full.|compound', 'Jay found a frog, and he showed it to us.|compound', 'The cake looked good, but it tasted dry.|compound',
    'We were tired, so we went to bed early.|compound', 'The lights went out, and everyone gasped.|compound',
    'Before we ate, we washed our hands.|intro', 'After school, Ana went to the park.|intro', 'In the morning, the birds sang.|intro',
    'Although it was late, we kept reading.|intro', 'Finally, the train arrived.|intro', 'Since the game was canceled, we went home.|intro',
    'During the storm, the power went out.|intro', 'As soon as the music started, the kids danced.|intro', 'Luckily, no one was hurt.|intro',
    'Yes, we can walk to the park.|yesno', 'No, I have not seen your hat.|yesno', 'Dad, may I have a snack?|address', 'Your drawing is beautiful, Maya.|address',
    "The test was easy, wasn't it?|tag", "You like apples, don't you?|tag",
    'School starts on August 20, 2025.|date', 'The bridge opened on May 27, 1937.|date', 'On April 3, 2022, our town had a parade.|date',
    'Tom lives in Austin, Texas.|place', 'We drove to Portland, Oregon, for a wedding.|place', 'Her pen pal lives in Tokyo, Japan.|place',
    'Dallas, Texas, is a big city.|place', 'We flew to Miami, Florida, in May.|place', 'The letter came from Boise, Idaho.|place',
    '"Look at the rainbow," said Jade.|quote', `Grandpa said, "Let's go fishing."|quote`, '"It is my turn," said Ben.|quote',
    'Ms. Lee asked, "Who knows the answer?"|quote', '"Please close the door," said Mom.|quote', 'Kim whispered, "The baby is asleep."|quote',
    '"The game starts at noon," said Coach Ray.|quote', 'Sam asked, "May I come too?"|quote', '"I can help," said Luis.|quote',
    'The teacher said, "Line up at the door."|quote', '"Watch out for the puddle," said Ava.|quote'],

  // dialogue: the corrected line (the sheet removes quotation marks and commas and the capital inside the quote)
  quotes: ['Mia said, "Can we play outside?"', '"I found a shell," said Ben.', 'Dad asked, "Who wants pancakes?"', '"Look at the rainbow!" shouted Ana.',
    '"We should bring water," said Leo.', 'Grandma said, "Wear your coat."', '"Where is my backpack?" asked Sam.', 'The coach yelled, "Great job, team!"',
    '"My turn is next," said Ruby.', 'Max whispered, "The baby is sleeping."', '"I can help you," said the librarian.', 'Lily asked, "May I borrow a pencil?"',
    '"This soup is hot," said Dad.', 'Mr. Kim said, "Open your books."', '"Let\'s build a fort," said Nora.', 'Jada said, "I lost my tooth!"'],

  // titles: sentence with {title} | kind of work
  titles: ['My class read the book {The Lost Kite}.|book', 'We watched the movie {Ocean Friends} on Friday.|movie', 'Ana memorized the poem {Rain on the Roof}.|poem',
    'The choir sang the song {Morning Bells}.|song', 'Leo read the short story {The Brave Little Tugboat}.|short story', 'Dad reads the newspaper {The Valley News}.|newspaper',
    'I found a recipe in the magazine {Kids Cook}.|magazine', 'Our class wrote the play {The Missing Crown}.|play', 'Did you read the article {How Bees Talk}?|article',
    'The first chapter of the book is called {A Strange Map}.|chapter', 'My favorite TV show is {Science Squad}.|TV show', 'We listened to the album {Songs for the Road}.|album',
    'Mia read the poem {The Old Oak Tree} aloud.|poem', 'Grandpa loves the movie {Race to the Moon}.|movie', 'The magazine {Young Explorer} has great photos.|magazine',
    'We sang the song {Over the Hills} at the concert.|song', 'Nora borrowed the book {Owls at Midnight}.|book', 'The article {Saving the Monarchs} was in the paper.|article',
    'My brother wrote the short story {The Night Train}.|short story', 'The episode {Lost in Space} was the funniest one.|episode'],
  longWorks: 'book movie newspaper magazine play TV show album',

  // fragments and run-ons: sentence | complete, fragment or run-on | one fix
  frag: ['The puppy slept on the rug.|complete|', 'We baked cookies for our neighbors.|complete|', 'Leo plays the drums.|complete|',
    'The kids laughed at the funny clown.|complete|', 'Please close the window.|complete|', 'After school, Mia rode her bike home.|complete|',
    'Running down the street.|fragment|I saw a dog running down the street.', 'Because the bus was late.|fragment|We were tardy because the bus was late.',
    'The tall man in the blue hat.|fragment|The tall man in the blue hat waved at us.', 'After school on Friday.|fragment|We will go swimming after school on Friday.',
    'Ate all the popcorn.|fragment|My brother ate all the popcorn.', 'When the lights went out.|fragment|When the lights went out, we found a flashlight.',
    'Under the kitchen table.|fragment|The cat hid under the kitchen table.',
    'I like pizza my brother likes tacos.|run-on|I like pizza, but my brother likes tacos.', 'The dog barked the cat ran away.|run-on|The dog barked, and the cat ran away.',
    'It was raining we stayed inside.|run-on|It was raining, so we stayed inside.', 'Mia finished her homework, she went outside to play.|run-on|Mia finished her homework. She went outside to play.',
    'The game was over everyone went home.|run-on|The game was over, so everyone went home.', 'We went to the lake we saw a heron.|run-on|We went to the lake. We saw a heron.'],

  // sentence types: sentence | independent clauses | dependent clauses
  stype: ['The dog ran across the yard.|1|0', 'Mia and Leo built a sandcastle.|1|0', 'We swam and played all afternoon.|1|0',
    'After lunch, the class went outside.|1|0', 'My little brother loves trucks.|1|0', 'The old bridge creaked in the wind.|1|0',
    'The dog ran across the yard, and the cat hid under the bed.|2|0', 'I wanted pizza, but we had tacos.|2|0', 'You can take the bus, or you can walk.|2|0',
    'The sun set; the stars came out.|2|0', 'The rain stopped, so we went outside.|2|0',
    'When the bell rang, the students lined up.|1|1', 'We stayed inside because it was raining.|1|1', 'The book that I borrowed is overdue.|1|1',
    'Although the test was hard, Ana passed it.|1|1', 'If you finish early, you may read.|1|1', 'The girl who lives next door plays the violin.|1|1',
    'When the storm ended, we went outside, and the kids played in the puddles.|2|1', 'I wanted to go, but I stayed home because I was sick.|2|1',
    'Although it was late, Dad made popcorn, and we watched a movie.|2|1', 'The team that won the game celebrated, but the coach stayed calm.|2|1'],

  // phrase or clause: word group | p (phrase), i (independent clause), d (dependent clause)
  clause: ['after the long game|p', 'in the back of the bus|p', 'running down the hall|p', 'to finish the project|p', 'under the old bridge|p',
    'the girl with red boots|p', 'during the storm|p', 'having eaten lunch|p', 'over the hills and far away|p', 'before sunrise|p',
    'the dog barked|i', 'we stayed inside|i', 'Maya finished her essay|i', 'the river flooded the town|i', 'they won the game|i', 'the bus arrived late|i',
    'because the dog barked|d', 'when we stayed inside|d', 'although Maya finished her essay|d', 'if the river floods|d', 'after they won the game|d',
    'since the bus was late|d', 'while the baby slept|d', 'who lives next door|d', 'that we planted last spring|d', 'until the rain stops|d'],
  subordinators: 'because when although if after since while who that until unless before whenever whereas',

  // coordinate adjectives: adjective | adjective | noun (verify uses the adjective kinds below)
  coord: ['cold|dark|night', 'happy|healthy|baby', 'long|boring|speech', 'warm|sunny|day', 'quiet|peaceful|lake', 'smart|funny|friend',
    'strong|brave|firefighter', 'exciting|scary|movie', 'bright|red|car', 'three|small|kittens', 'old|wooden|bridge', 'big|brown|dog',
    'famous|French|author', 'tall|oak|tree', 'delicious|chocolate|cake', 'soft|wool|sweater', 'kind|patient|teacher', 'loud|crowded|room',
    'little|red|wagon', 'two|tired|hikers'],
  // q = an opinion or quality word; anything else (number, size, age, color, shade, origin, material, kind) stacks without a comma
  adjKind: 'cold q|dark q|happy q|healthy q|long q|boring q|warm q|sunny q|quiet q|peaceful q|smart q|funny q|strong q|brave q|exciting q|scary q|kind q|patient q|loud q|crowded q|tired q|bright shade|red color|three number|two number|small size|big size|little size|old age|wooden material|brown color|famous q|French origin|tall size|oak kind|delicious q|chocolate material|soft q|wool material',

  // verbals: sentence with [verbal phrase] | gerund, participle or infinitive | noun, adjective or adverb
  verbal: ['[Swimming] is my favorite sport.|gerund|noun', 'The [crying] baby needed a nap.|participle|adjective', 'We went to the store [to buy milk].|infinitive|adverb',
    'Maya loves [painting landscapes].|gerund|noun', '[To win the race] was her goal.|infinitive|noun', 'The [broken] window let in cold air.|participle|adjective',
    'I need a book [to read on the trip].|infinitive|adjective', '[Running late], Leo grabbed his bag.|participle|adjective', 'His job is [teaching music].|gerund|noun',
    'The students [waiting for the bus] laughed.|participle|adjective', 'She practiced every day [to improve her skills].|infinitive|adverb',
    'Everyone enjoyed [hearing the band].|gerund|noun', '[Exhausted from the hike], we rested by the stream.|participle|adjective', 'He wants [to become a pilot].|infinitive|noun',
    'The [frozen] lake sparkled in the sun.|participle|adjective', 'We are happy [to help].|infinitive|adverb', '[Reading before bed] helps me relax.|gerund|noun',
    'The dog [barking at the gate] belongs to our neighbor.|participle|adjective'],

  // active and passive voice: active | passive
  voice: ['The dog chased the cat.|The cat was chased by the dog.', 'Maya wrote the report.|The report was written by Maya.',
    'The chef cooks the meals.|The meals are cooked by the chef.', 'The wind knocked down the fence.|The fence was knocked down by the wind.',
    'English settlers founded Jamestown in 1607.|Jamestown was founded in 1607 by English settlers.', 'The students planted the trees.|The trees were planted by the students.',
    'A bee stung my brother.|My brother was stung by a bee.', 'The team will paint the mural.|The mural will be painted by the team.',
    'Our class has collected the cans.|The cans have been collected by our class.', 'Lightning struck the old oak.|The old oak was struck by lightning.',
    'Frederick Douglass wrote three autobiographies.|Three autobiographies were written by Frederick Douglass.',
    'The Wright brothers flew the first powered airplane in 1903.|The first powered airplane was flown by the Wright brothers in 1903.',
    'Marie and Pierre Curie discovered radium in 1898.|Radium was discovered by Marie and Pierre Curie in 1898.', 'The mayor opened the new park.|The new park was opened by the mayor.',
    'Volunteers clean the beach every spring.|The beach is cleaned by volunteers every spring.', 'The storm damaged several houses.|Several houses were damaged by the storm.'],

  // verb mood: sentence | mood
  mood: ['The museum opens at nine.|indicative', 'Water boils at 100 degrees Celsius at sea level.|indicative', 'Our class finished the mural yesterday.|indicative',
    'Turn off the lights before you leave.|imperative', 'Please hand in your essays on Friday.|imperative', 'Bring a jacket to the game.|imperative',
    'Did you finish the reading?|interrogative', 'Where will the team practice next week?|interrogative', 'Have you ever seen a comet?|interrogative',
    'I would call you, but my phone is dead.|conditional', 'With more time, we could finish the mural.|conditional', 'If we leave now, we might catch the bus.|conditional',
    'I wish it were summer.|subjunctive', 'The teacher asked that each student bring a pencil.|subjunctive', 'It is essential that he be on time.|subjunctive',
    'She acts as if she were the boss.|subjunctive', 'We recommend that the club meet on Fridays.|subjunctive'],

  // semicolon or colon: left | right | reason (ic two independent clauses, ca conjunctive adverb, ser series with commas, list, exp explanation)
  semi: ['Maya trained all summer|her brother spent it at camp.|ic', 'The museum closes at five|the gift shop stays open until six.|ic',
    'The library was quiet|the gym was loud.|ic', 'Our team lost the first game|however, we won the next three.|ca', 'The road was icy|therefore, school started late.|ca',
    'Leo forgot his umbrella|consequently, he got soaked.|ca', 'The trip had been planned for months|nevertheless, the weather ruined it.|ca',
    'The recipe calls for three things|flour, sugar, and butter.|list', 'Bring the following supplies|a notebook, two pens, and a calculator.|list',
    'I have three favorite subjects|math, art, and science.|list', 'The club has visited Austin, Texas|Reno, Nevada; and Boise, Idaho.|ser',
    'The winners were Ana, a sixth grader|Leo, a fourth grader; and Sam, a first grader.|ser', 'She had one goal|to finish the marathon.|exp',
    'The plant died for a simple reason|no one watered it.|exp', 'The speaker made her final point|every vote counts.|exp', 'The answer was clear|we needed more volunteers.|exp'],
  conjAdverbs: 'however therefore consequently nevertheless moreover furthermore meanwhile otherwise instead',

  // hyphens in compound modifiers: sentence with [modifier] | b (before the noun) or a (after the noun or not a modifier)
  hyphen: ['She is a [well known] author.|b', 'He found a [part time] job.|b', 'We need a [long term] plan.|b', 'They printed it on [high quality] paper.|b',
    'The class used an [up to date] map.|b', 'We made a [last minute] change.|b', 'A [world famous] chef visited our school.|b', 'They live in a [two story] house.|b',
    'My [ten year old] cousin plays chess.|b', 'The team hired a [full time] coach.|b', 'The author is [well known] in our town.|a', 'My sister works [part time].|a',
    'Is the map [up to date]?|a', 'We finished the project at the [last minute].|a', 'Our coach works [full time].|a', 'We planned for the [long term].|a',
    'He is a [highly skilled] carpenter.|b', 'We crossed the [newly built] bridge.|b', 'They read in a [brightly lit] room.|b', 'It was a [carefully planned] trip.|b'],

  // parallel structure: faulty | fixed
  parallel: ['Maya likes hiking, swimming, and to ride her bike.|Maya likes hiking, swimming, and riding her bike.',
    'The coach told us to stretch, to drink water, and that we should rest.|The coach told us to stretch, to drink water, and to rest.',
    'The job requires patience, skill, and being creative.|The job requires patience, skill, and creativity.',
    'We can drive, take the train, or flying is also an option.|We can drive, take the train, or fly.',
    'The report was clear, accurate, and it was well organized.|The report was clear, accurate, and well organized.',
    'She would rather read a book than watching TV.|She would rather read a book than watch TV.',
    'The colonists protested by writing letters, boycotting goods, and they gave speeches.|The colonists protested by writing letters, boycotting goods, and giving speeches.',
    'Reading the map is easier than to ask for directions.|Reading the map is easier than asking for directions.',
    'Lincoln was known for his honesty, his humor, and he could tell stories well.|Lincoln was known for his honesty, his humor, and his storytelling.',
    'Our goals are to raise money, to clean the park, and planting trees.|Our goals are to raise money, to clean the park, and to plant trees.',
    'The scientist observed the cells, recorded the data, and then she was writing a report.|The scientist observed the cells, recorded the data, and wrote a report.',
    'He was tired, hungry, and wanted to go home.|He was tired, hungry, and ready to go home.',
    'The new rules are simple, fair, and people can understand them easily.|The new rules are simple, fair, and easy to understand.',
    'Volunteers sorted cans, packed boxes, and were delivering meals.|Volunteers sorted cans, packed boxes, and delivered meals.'],

  // concise writing: wordy | concise model
  concise: ['Due to the fact that it was raining, the game was canceled.|Because it was raining, the game was canceled.',
    'In my personal opinion, I think recess should be longer.|I think recess should be longer.', 'At this point in time, we are ready to begin.|We are ready to begin now.',
    'The box was large in size and red in color.|The box was large and red.', 'She made the decision to leave early.|She decided to leave early.',
    'Each and every student must sign the form.|Every student must sign the form.', 'We will meet together at 3 p.m. in the afternoon.|We will meet at 3 p.m.',
    'He returned back to the classroom to get his book.|He returned to the classroom to get his book.', 'The reason why we were late is because the bus broke down.|We were late because the bus broke down.',
    'In order to win the game, we need to practice.|To win the game, we need to practice.', 'There are many students who enjoy art.|Many students enjoy art.',
    'The final outcome of the vote was a surprise.|The outcome of the vote was a surprise.', 'Please repeat that again.|Please repeat that.',
    'It is important to plan ahead for the future.|It is important to plan ahead.', 'She is a person who is very kind.|She is very kind.',
    'The team was in agreement that the plan was good.|The team agreed that the plan was good.'],

  // linking words: sentence 1 | sentence 2 | relation (sentence 2 starts after the linking word)
  linkAdv: ['Our town has a big park.|it does not have a pool.|contrast', 'Penguins are birds.|they cannot fly.|contrast', 'The test was long.|most students finished on time.|contrast',
    'Many people think bats are blind.|most bats can see quite well.|contrast', 'The colonists wanted to trade freely.|the king placed new taxes on their goods.|contrast',
    'Exercise makes your heart stronger.|it can help you sleep better.|add', 'Reading builds your vocabulary.|it teaches you about the world.|add',
    'The new library has more books.|it stays open later on weekends.|add', 'Our school has a garden.|it has a small greenhouse.|add',
    'The river flooded the road.|school was closed for the day.|result', 'Leo practiced every day.|he made the team.|result', 'The power went out.|we ate dinner by candlelight.|result',
    'The farmers had no rain for months.|their crops dried up.|result', 'The bridge was too narrow for trucks.|the city built a wider one.|result',
    'Many animals sleep through the winter.|bears rest in dens for months.|example', 'Some foods are high in protein.|eggs and beans have a lot of it.|example',
    'Our class helps the community.|we picked up trash at the park last week.|example', 'Many inventions changed daily life.|the telephone let people talk across long distances.|example',
    'Frogs lay their eggs in water.|many fish lay their eggs in water.|similar', 'Bees help plants by spreading pollen.|butterflies carry pollen from flower to flower.|similar',
    'Wolves live and hunt in packs.|lions live and hunt in groups called prides.|similar'],
  linkWords: 'contrast:However:5,Nevertheless:7|add:In addition:5,Moreover:6|result:As a result:5,Therefore:6,Consequently:7|example:For example:5,For instance:6|similar:Similarly:5,Likewise:7',
  // because, although, so: sentence | answer
  linkSub: ['We stayed inside ___ it was raining.|because', 'It was raining, ___ we stayed inside.|so', '___ it was raining, we played outside.|although',
    'Dogs make good pets ___ they are loyal.|because', 'I finished the race ___ my legs were tired.|although', 'The store was closed, ___ we went home.|so',
    'Plants need sunlight ___ they use it to make food.|because', 'Sam was tired, ___ he went to bed early.|so', 'Mia kept walking ___ her feet hurt.|although',
    'Our class should get a fish tank ___ we could learn about fish.|because', 'The soup was too hot, ___ I waited.|so', '___ the movie was long, nobody got bored.|although',
    'Recess should be longer ___ kids need time to move.|because', 'The path was muddy, ___ we wore boots.|so'],

  // spelling patterns: group | category label | test (a regular expression) | words
  patterns: {
    fam: [['-at family', 'at$', 'cat hat bat mat sat rat flat chat'], ['-ig family', 'ig$', 'big dig pig wig fig twig jig'],
      ['-op family', 'op$', 'hop mop top pop stop shop drop chop'], ['-an family', 'an$', 'can fan man pan ran van plan'],
      ['-ug family', 'ug$', 'bug hug mug rug dug jug plug'], ['-en family', 'en$', 'hen pen ten men den then'], ['-it family', 'it$', 'sit hit bit fit kit quit'],
      ['-ot family', 'ot$', 'hot pot dot cot lot spot not']],
    short: [['short a', '^[^aeiou]*a[^aeiou]*$', 'cat map bag jam fan sad clap ham'], ['short e', '^[^aeiou]*e[^aeiou]*$', 'bed pen ten web leg jet hen net'],
      ['short i', '^[^aeiou]*i[^aeiou]*$', 'pig sit fin lid mix big win dip'], ['short o', '^[^aeiou]*o[^aeiou]*$', 'hop dog pot log box mop fox top'],
      ['short u', '^[^aeiou]*u[^aeiou]*$', 'bug cup sun rug nut mud bus duck']],
    magic: [['short vowel (no e)', '^[^aeiou]+[aeiou][^aeiou]+$', 'cap kit hop cub tap pin not cut mad rid'],
      ['silent e (long vowel)', '^[^aeiou]+[aeiou][^aeiou]e$', 'cape kite hope cube tape pine note cute made ride']],
    digraph: [['sh', 'sh', 'ship fish shop dish shell wish'], ['ch', 'ch', 'chip chin lunch chop much rich'], ['th', 'th', 'thin bath math with them path']],
    teams: [['long a: ai or ay', 'ai|ay', 'rain tail paint day play tray mail snail'], ['long e: ee or ea', 'ee|ea', 'feet tree seed sheep leaf team beach seat'],
      ['long o: oa', 'oa', 'boat coat road soap goat toad loaf'], ['long i: igh', 'igh', 'night light high right sight might']],
    rctl: [['ar', 'ar', 'car star farm park barn yard shark'], ['or', 'or', 'corn fork horn storm sport short'], ['er, ir or ur', 'er|ir|ur', 'her bird girl turn fern burn shirt nurse']],
  },

  // compound words: first | second ; extra = more real compound words that a wrong match could make
  compound: 'sun flower|back pack|rain bow|foot ball|cup cake|star fish|snow man|bed room|play ground|butter fly|pop corn|gold fish|sail boat|tooth brush|mail box|rain coat|sun set|home work|base ball|fire fly|sea shell|lady bug|sand box|door bell|pan cake|note book|bath tub|hair cut|moon light|cow boy|day light|week end',
  compoundExtra: 'sunlight sunshine sunflower sunset sunrise raindrop rainfall rainbow raincoat football footprint snowball snowflake snowman starfish starlight moonlight daylight cupcake pancake bedroom bathroom classroom playground backyard backpack mailbox sandbox toolbox lunchbox goldfish catfish butterfly firefly fireworks homework housework notebook cookbook baseball basketball doorbell doorway haircut hairbrush toothbrush popcorn sailboat seashell seashore ladybug bathtub cowboy weekend bedbug bedtime playtime daytime bathrobe sandman mailman snowboard skateboard backbone sunburn sandcastle fishbowl bookcase daydream birthday',

  // root words with endings (grades 1-2): verbs from the verb list with -s, -ed, -ing
  rootword1: 'jump look play help walk kick cook pull paint call clean climb plant talk',
  rootword2: 'bake hop clap smile stop wash dance race carry cry',

  // prefixes and suffixes: affix | meaning | first grade
  prefixes: 'un|not|1,re|again|1,pre|before|3,dis|not or the opposite of|3,mis|wrongly|3,non|not|4,over|too much|4',
  suffixes: 'ful|full of|1,less|without|1,er|one who|1,ly|in a way that is|2,able|able to be|3,ment|the act or result of|3,ness|the state of being|3',
  // base | affix | built word | meaning
  affix: ['happy|un|unhappy|not happy', 'lock|un|unlock|to open a lock', 'kind|un|unkind|not kind', 'safe|un|unsafe|not safe', 'tie|un|untie|to undo a knot',
    'fair|un|unfair|not fair', 'read|re|reread|to read again', 'build|re|rebuild|to build again', 'fill|re|refill|to fill again', 'paint|re|repaint|to paint again',
    'heat|pre|preheat|to heat before', 'view|pre|preview|to look at before', 'agree|dis|disagree|to not agree', 'like|dis|dislike|to not like',
    'honest|dis|dishonest|not honest', 'spell|mis|misspell|to spell wrongly', 'behave|mis|misbehave|to behave wrongly', 'stop|non|nonstop|without stopping',
    'fiction|non|nonfiction|writing that is not made up', 'sleep|over|oversleep|to sleep too long', 'cook|over|overcook|to cook too much',
    'help|ful|helpful|full of help', 'care|ful|careful|full of care', 'hope|ful|hopeful|full of hope', 'play|ful|playful|full of play', 'joy|ful|joyful|full of joy',
    'color|ful|colorful|full of color', 'beauty|ful|beautiful|full of beauty', 'fear|less|fearless|without fear', 'care|less|careless|without care',
    'home|less|homeless|without a home', 'end|less|endless|without an end', 'help|less|helpless|without help', 'teach|er|teacher|one who teaches',
    'paint|er|painter|one who paints', 'farm|er|farmer|one who farms', 'bake|er|baker|one who bakes', 'swim|er|swimmer|one who swims', 'run|er|runner|one who runs',
    'quick|ly|quickly|in a way that is quick', 'slow|ly|slowly|in a way that is slow', 'soft|ly|softly|in a way that is soft', 'happy|ly|happily|in a way that is happy',
    'wash|able|washable|able to be washed', 'read|able|readable|able to be read', 'enjoy|able|enjoyable|able to be enjoyed', 'rely|able|reliable|able to be relied on',
    'use|able|usable|able to be used', 'move|ment|movement|the act of moving', 'pay|ment|payment|the act of paying', 'enjoy|ment|enjoyment|the act of enjoying',
    'agree|ment|agreement|the result of agreeing', 'excite|ment|excitement|the state of being excited', 'kind|ness|kindness|the state of being kind',
    'dark|ness|darkness|the state of being dark', 'sad|ness|sadness|the state of being sad', 'happy|ness|happiness|the state of being happy', 'lazy|ness|laziness|the state of being lazy'],
  // suffix spelling rules (grades 5-8): base | suffix | built word ; S = stress on the last syllable
  sufspell: ['hope|ing|hoping', 'hop|ing|hopping', 'cry|ed|cried', 'play|ed|played', 'carry|ing|carrying', 'excite|ment|excitement', 'begin|ing|beginning|S',
    'forget|ing|forgetting|S', 'occur|ed|occurred|S', 'admit|ed|admitted|S', 'visit|ed|visited', 'open|ing|opening', 'happy|ness|happiness', 'use|able|usable',
    'care|ful|careful', 'shop|er|shopper', 'plan|ing|planning', 'bake|ery|bakery', 'busy|ly|busily', 'joy|ful|joyful', 'write|ing|writing', 'rely|able|reliable',
    'hot|est|hottest', 'sad|ly|sadly', 'large|est|largest', 'enjoy|ed|enjoyed', 'study|ing|studying', 'study|ed|studied', 'hike|er|hiker', 'thin|er|thinner',
    'pity|ful|pitiful', 'move|ment|movement', 'fit|ness|fitness', 'stir|ing|stirring', 'swim|er|swimmer', 'wrap|ed|wrapped', 'smile|ing|smiling', 'greet|ing|greeting'],

  // word parts: part | meaning | kind (r root, p prefix, s suffix, o connecting letter)
  parts: `tele|far|r,phone|sound|r,phon|sound|r,phono|sound|r,photo|light|r,graph|write, draw or record|r,scope|look at, see|r,vis|see|r,ion|the act or result of|s,auto|self|r,para|beside|p,bio|life|r,y|the act or state of|s,ic|having to do with|s,
trans|across|p,port|carry|r,ex|out|p,im|in or into|p,able|able to be|s,re|back or again|p,e|out|p,rupt|break|r,inter|between|p,dis|apart or away|p,ure|the act or result of|s,con|together|p,struct|build|r,in|in or into|p,in~not|not|p,dis~not|not|p,de|down or away|p,
logy|study of|s,geo|earth|r,therm|heat|r,o|connecting letter|o,meter|measure|r,metr|measure|r,al|having to do with|s,stat|keep steady|r,sphere|ball, globe|r,anti|against|p,tic|having to do with|s,
aud|hear|r,ience|state of|s,ible|able to be|s,io|having to do with|s,ual|having to do with|s,dict|say|r,ate|to make or do|s,pre|before|p,contra|against|p,ary|a place or thing for|s,ver|true|r,
bell|war|r,i|connecting letter|o,ger|wage or carry on|r,er|one who|s,ent|having the quality of|s,ante|before|p,um|noun ending|s,cred|believe|r,it|noun ending|s,ose|full of|s,
cede|go or yield|r,ceed|go|r,cess|go|r,pro|forward|p,ac|to or toward|p,suc|under or after|p,or|one who|s,
cardi|heart|r,card|heart|r,gastr|stomach|r,itis|inflammation|s,brady|slow|p,tachy|fast|p,ia|condition|s,dermat|skin|r,arthr|joint|r,neur|nerve|r,hemat|blood|r,ectomy|surgical removal|s,megaly|enlargement|s,algia|pain|s,oste|bone|r,hepat|liver|r,peri|around|p,endo|within|p,scopy|viewing with an instrument|s,leuk|white|r,erythr|red|r,cyte|cell|r,hyper|over or above normal|p,tens|stretch or strain|r,
chron|time|r,syn|together|p,ize|to make|s,psych|mind|r,ics|study or skill of|s,sym|together|p,micro|small|r,hydr|water|r,astr|star|r,nomy|law or system of|s,path|feeling or disease|r,
act|do|r,ive|tending to|s,form|shape|r,ation|the act or result of|s,uni|one|p,sign|mark|r,as|to or toward|p,
spect|look|r,ator|one who|s,at|to or toward|p,ject|throw|r,tract|pull|r,sub|under|p,mit|send|r,miss|send|r,vert|turn|r,scribe|write|r,script|write|r,manu|hand|r`,
  // word | parts joined by + | meaning ; grouped in sets
  roots: {
    tpg: ['telephone|tele+phone|a device that carries sound far away', 'telescope|tele+scope|a tool for seeing things far away', 'television|tele+vis+ion|a device for seeing pictures sent from far away',
      'photograph|photo+graph|a picture recorded with light', 'autograph|auto+graph|a person\'s own handwritten name', 'paragraph|para+graph|a group of written sentences about one idea',
      'biography|bio+graph+y|a written story of a person\'s life', 'telegraph|tele+graph|a machine that sends written messages far away', 'graphic|graph+ic|having to do with drawing or writing',
      'phonograph|phono+graph|an early machine that recorded and played sound', 'autobiography|auto+bio+graph+y|the story of a person\'s life written by that person'],
    prs: ['transport|trans+port|to carry across from one place to another', 'export|ex+port|to send goods out of a country', 'import|im+port|to bring goods into a country',
      'portable|port+able|able to be carried', 'report|re+port|to carry back news or information', 'erupt|e+rupt|to break out', 'interrupt|inter+rupt|to break in between',
      'disrupt|dis+rupt|to break apart or upset', 'rupture|rupt+ure|a break or burst', 'construct|con+struct|to build by putting parts together', 'structure|struct+ure|something that is built',
      'instruct|in+struct|to teach, to build knowledge in someone', 'destruction|de+struct+ion|the act of tearing something down', 'reconstruct|re+con+struct|to build again'],
    bgt: ['biology|bio+logy|the study of living things', 'geology|geo+logy|the study of the earth and its rocks', 'thermometer|therm+o+meter|a tool that measures heat',
      'geography|geo+graph+y|the study and description of the earth\'s surface', 'thermal|therm+al|having to do with heat', 'thermostat|therm+o+stat|a device that keeps heat steady',
      'biosphere|bio+sphere|the part of the earth where life exists', 'geothermal|geo+therm+al|having to do with heat from inside the earth', 'antibiotic|anti+bio+tic|a medicine that works against bacteria',
      'geometry|geo+metr+y|the math of shapes, first used to measure land'],
    avd: ['audience|aud+ience|a group of people who listen', 'audible|aud+ible|able to be heard', 'audio|aud+io|having to do with sound that is heard', 'visible|vis+ible|able to be seen',
      'vision|vis+ion|the ability to see', 'invisible|in~not+vis+ible|not able to be seen', 'visual|vis+ual|having to do with seeing', 'dictate|dict+ate|to say words for someone to write down',
      'predict|pre+dict|to say what will happen before it happens', 'contradict|contra+dict|to say the opposite', 'dictionary|dict+ion+ary|a book of words and what they mean',
      'verdict|ver+dict|a jury\'s decision, a true saying'],
    bcd: ['rebellion|re+bell+ion|an act of fighting back against those in power', 'belligerent|bell+i+ger+ent|eager to fight', 'bellicose|bell+ic+ose|likely to start fights or wars',
      'antebellum|ante+bell+um|before a war, often before the Civil War', 'credible|cred+ible|able to be believed', 'incredible|in~not+cred+ible|hard to believe',
      'credit|cred+it|belief or trust that someone will pay later', 'discredit|dis~not+cred+it|to make people stop believing someone', 'predict|pre+dict|to say what will happen before it happens',
      'contradict|contra+dict|to say the opposite', 'dictate|dict+ate|to say words for someone to write down', 'verdict|ver+dict|a jury\'s decision, a true saying'],
    ced: ['precede|pre+cede|to go before', 'recede|re+cede|to go back or move away', 'proceed|pro+ceed|to go forward', 'exceed|ex+ceed|to go beyond a limit',
      'process|pro+cess|a series of steps that moves forward', 'recess|re+cess|a break when people go away from work', 'access|ac+cess|a way to go in or reach something',
      'concede|con+cede|to give in or admit', 'intercede|inter+cede|to go between people to help settle a problem', 'procession|pro+cess+ion|a group moving forward in a line',
      'excess|ex+cess|an amount that goes beyond what is needed', 'predecessor|pre+de+cess+or|a person who held a job before someone else', 'success|suc+cess|the result of reaching a goal'],
    med: ['cardiology|cardi+o+logy|the study of the heart', 'gastritis|gastr+itis|inflammation of the stomach', 'bradycardia|brady+card+ia|a slow heart rate',
      'tachycardia|tachy+card+ia|a fast heart rate', 'dermatitis|dermat+itis|inflammation of the skin', 'arthritis|arthr+itis|inflammation of a joint',
      'neurology|neur+o+logy|the study of the nerves and nervous system', 'hematology|hemat+o+logy|the study of blood', 'gastrectomy|gastr+ectomy|surgical removal of part or all of the stomach',
      'cardiomegaly|cardi+o+megaly|an enlarged heart', 'neuralgia|neur+algia|nerve pain', 'arthralgia|arthr+algia|joint pain', 'dermatology|dermat+o+logy|the study of the skin',
      'osteoarthritis|oste+o+arthr+itis|a joint disease that wears down the ends of bones (the name says inflammation of bone and joint)', 'hepatitis|hepat+itis|inflammation of the liver', 'pericarditis|peri+card+itis|inflammation of the sac around the heart',
      'endoscopy|endo+scopy|looking inside the body with an instrument', 'leukocyte|leuk+o+cyte|a white blood cell', 'erythrocyte|erythr+o+cyte|a red blood cell',
      'hypertension|hyper+tens+ion|blood pressure that is higher than normal'],
    greek: ['chronology|chron+o+logy|the order in which events happened', 'chronic|chron+ic|lasting a long time', 'synchronize|syn+chron+ize|to make things happen at the same time',
      'psychology|psych+o+logy|the study of the mind', 'phonics|phon+ics|the study of letters and their sounds', 'symphony|sym+phon+y|a long piece of music where instruments sound together',
      'microphone|micro+phone|a device that picks up small sounds', 'microscope|micro+scope|a tool for seeing very small things', 'hydrology|hydr+o+logy|the study of water on and under the earth',
      'astronomy|astr+o+nomy|the study of stars and space', 'sympathy|sym+path+y|sharing the feelings of another person', 'photograph|photo+graph|a picture recorded with light'],
    afs: ['action|act+ion|the act of doing something', 'react|re+act|to act back in response', 'transaction|trans+act+ion|an exchange carried out between people', 'actor|act+or|one who acts',
      'active|act+ive|tending to do things, busy', 'inform|in+form|to give shape to someone\'s knowledge, to tell', 'reform|re+form|to shape again, to improve',
      'transform|trans+form|to change from one shape to another', 'formation|form+ation|the act of shaping something', 'uniform|uni+form|having one shape, all the same',
      'signal|sign+al|a mark or sign that sends a message', 'design|de+sign|to mark out a plan', 'assign|as+sign|to mark out a task for someone'],
    misc: ['inspect|in+spect|to look closely at', 'spectator|spect+ator|one who looks on', 'respect|re+spect|to look up to', 'project|pro+ject|to throw forward',
      'reject|re+ject|to throw back, to refuse', 'inject|in+ject|to throw or force into', 'eject|e+ject|to throw out', 'tractor|tract+or|a machine that pulls',
      'subtract|sub+tract|to pull away, to take away', 'attract|at+tract|to pull toward', 'extract|ex+tract|to pull out', 'transmit|trans+mit|to send across',
      'submit|sub+mit|to send in or give in', 'dismiss|dis+miss|to send away', 'convert|con+vert|to turn into something else', 'describe|de+scribe|to write or tell about',
      'manuscript|manu+script|a book or paper written by hand'],
  },

  // shades of meaning: grade | low end | high end | words from low to high
  shades: ['2|softest|hardest|toss throw hurl', '2|a little happy|very happy|glad happy thrilled', '2|a little angry|very angry|annoyed mad furious',
    '2|quietest|loudest|whisper talk shout', '2|slowest eating|fastest eating|nibble eat gobble', '2|slowest|fastest|walk jog run sprint', '2|a little wet|very wet|damp wet soaked',
    '2|smallest|biggest|tiny small large enormous', '2|a little|the most|like love adore', '3|least good|best|good great excellent', '3|least cold|coldest|cool cold freezing',
    '3|least hot|hottest|warm hot scorching', '3|a little afraid|very afraid|nervous scared terrified', '3|lightest rain|heaviest rain|drizzle rain downpour',
    '3|shortest look|longest look|glance look stare', '4|coldest|hottest|freezing cold cool warm hot scorching', '4|weakest wind|strongest wind|breeze wind gale',
    '4|least pretty|most beautiful|pretty beautiful gorgeous', '4|fewest|most|few several many', '4|least often|most often|never sometimes often always',
    '5|least sure|most sure|possible likely certain', '5|mildest feeling|strongest feeling|dislike hate loathe', '5|softest knock|loudest knock|tap knock pound',
    '6|least strange|most strange|unusual strange bizarre', '6|dimmest|brightest|dim bright dazzling', '6|least water|most water|trickle stream flood'],
  // connotation: grade | positive | neutral | negative
  connot: ['5|thrifty|frugal|stingy', '5|slender|thin|skinny', '5|determined|firm|stubborn', '5|curious|interested|nosy', '5|aroma|smell|stench',
    '5|youthful|young|childish', '5|relaxed|inactive|lazy', '5|unique|unusual|weird', '5|home|house|shack', '6|affordable|inexpensive|cheap',
    '6|assertive|forceful|pushy', '6|famous|well known|notorious', '6|chat|talk|gossip', '7|confident|bold|arrogant', '7|cautious|hesitant|cowardly'],

  // synonyms and antonyms: word | synonym | antonym | grade | group (no distractor from the same group)
  synant: ['happy|glad|sad|1|mood', 'right|correct|wrong|1|right', 'push|shove|pull|1|push', 'fast|quick|slow|1|speed', 'start|begin|finish|1|start', 'shut|close|open|1|open', 'big|large|small|1|size',
    'loud|noisy|quiet|1|sound', 'smile|grin|frown|1|face', 'below|under|above|1|place', 'cold|chilly|hot|1|temp', 'difficult|hard|easy|2|hard',
    'angry|mad|calm|2|mood2', 'shout|yell|whisper|2|sound2', 'brave|bold|scared|2|brave', 'tired|sleepy|rested|2|sleep', 'sick|ill|healthy|2|health',
    'friend|pal|enemy|2|friend', 'smart|clever|foolish|3|smart', 'rich|wealthy|poor|3|money', 'enormous|gigantic|tiny|3|size', 'shiny|bright|dull|3|light',
    'rude|impolite|polite|3|manners', 'fix|repair|break|3|fix', 'buy|purchase|sell|3|buy', 'ancient|old|modern|4|age', 'damp|moist|dry|4|wet',
    'victory|win|defeat|4|win', 'generous|giving|selfish|4|give', 'cautious|careful|reckless|5|care', 'accept|receive|reject|5|accept',
    'increase|grow|decrease|5|amount', 'ending|conclusion|beginning|5|start', 'rapid|swift|sluggish|6|speed', 'abundant|plentiful|scarce|6|amount'],

  // idioms: idiom | meaning | group (no two from a group on one sheet)
  idiom: ['raining cats and dogs|raining very hard|rain', 'a piece of cake|very easy|easy', 'break the ice|get people talking and feeling comfortable|ice',
    'under the weather|feeling sick|sick', 'spill the beans|tell a secret|secret', 'hit the books|study hard|study', 'cost an arm and a leg|be very expensive|cost',
    'once in a blue moon|very rarely|rare', 'hold your horses|wait and be patient|wait', 'on cloud nine|very happy|happy', 'beat around the bush|avoid saying something directly|direct',
    'the ball is in your court|it is your turn to decide or act|turn', 'time flies|time seems to pass quickly|time', 'in hot water|in trouble|trouble',
    'get cold feet|get nervous about doing something you planned|nervous', 'see eye to eye|agree|agree', 'bite off more than you can chew|take on more than you can handle|much',
    'hit the hay|go to bed|bed', 'when pigs fly|never|rare', 'break a leg|good luck (said before a performance)|luck', 'keep an eye on|watch carefully|watch',
    'a dime a dozen|very common and easy to find|common', 'save for a rainy day|save for a time of need|save', 'in the same boat|in the same situation|same',
    'pull someone\'s leg|joke with or tease someone|joke', 'down to the wire|until the very last moment|last', 'on the fence|unable to decide|decide',
    'burn the midnight oil|stay up late working|bed', 'cut corners|do a job badly to save time or money|cut', 'face the music|accept the results of your actions|face',
    'feel blue|feel sad|sad', 'let the cat out of the bag|tell a secret|secret', 'over the moon|very happy|happy', 'butterflies in your stomach|a nervous feeling|nervous'],

  // fact or opinion: sentence | signal word or phrase ('' for a fact)
  factop: ['A spider has eight legs.|', 'Water freezes at 32 degrees Fahrenheit.|', 'The sun rises in the east.|', 'Dogs are mammals.|', 'There are seven days in a week.|',
    'Abraham Lincoln was the sixteenth president of the United States.|', 'Bees make honey.|', 'The Pacific is the largest ocean on Earth.|', 'Penguins cannot fly.|',
    'A triangle has three sides.|', 'Pizza is the best food.|best', 'I think recess should be longer.|I think', 'Summer is the most fun season.|most fun',
    'Cats are better pets than dogs.|better', 'In my opinion, math is easy.|In my opinion', 'That movie was boring.|boring', 'Everyone should learn to swim.|should',
    'Red is the prettiest color.|prettiest', 'I believe soccer is exciting.|I believe', 'Spiders are scary.|scary', 'Winter is the worst season.|worst'],

  // literal or figurative: sentence | plain meaning ('' for literal)
  figlit: ['The cat sat on the warm rug.|', 'It rained all afternoon.|', 'Leo ran to the bus stop.|', 'The soup was very hot.|', 'My sister laughed at the joke.|',
    'The wind blew the leaves across the yard.|', 'We planted beans in the garden.|', 'It\'s raining cats and dogs.|It is raining very hard.',
    'My backpack weighs a ton.|My backpack is very heavy.', 'Leo ran like the wind.|Leo ran very fast.', 'The classroom was a zoo.|The classroom was loud and wild.',
    'I\'m so hungry I could eat a horse.|I am very hungry.', 'The stars winked at us.|The stars twinkled.', 'He has a heart of gold.|He is very kind.',
    'The test was a piece of cake.|The test was very easy.', 'The leaves danced in the wind.|The leaves moved in the wind.', 'My brother is a couch potato.|My brother sits around and watches TV a lot.',
    'Her smile lit up the room.|Her smile made everyone feel happy.'],

  // point of view: first-person version | third-person version
  pov: ['I grabbed my backpack and ran to the bus. My heart pounded because I was late again.|Maya grabbed her backpack and ran to the bus. Her heart pounded because she was late again.',
    'I set up the tent near the lake. Then Dad showed me how to build a safe campfire.|Sam set up the tent near the lake. Then his dad showed him how to build a safe campfire.',
    'I could not believe my eyes. A tiny kitten was hiding in the mailbox.|Ana could not believe her eyes. A tiny kitten was hiding in the mailbox.',
    'I walked into the dark gym, and the lights snapped on. Everyone cheered, and I felt my face turn red.|Leo walked into the dark gym, and the lights snapped on. Everyone cheered, and he felt his face turn red.',
    'I fished with Grandpa all morning. We caught three trout before lunch.|Ben fished with his grandpa all morning. They caught three trout before lunch.',
    'I opened the dusty box slowly. Inside, I found an old map.|Ms. Park opened the dusty box slowly. Inside, she found an old map.',
    'My twin and I argued about the last cookie. Finally, our mom cut it in half.|The twins argued about the last cookie. Finally, their mom cut it in half.',
    'I practiced my lines every night. On the day of the play, I did not miss a word.|Nora practiced her lines every night. On the day of the play, she did not miss a word.',
    'I tripped on the stairs and dropped my tray. My friends helped me pick up the mess.|Omar tripped on the stairs and dropped his tray. His friends helped him pick up the mess.',
    'I planted the seeds in April. By July, my garden was full of tomatoes.|Rosa planted the seeds in April. By July, her garden was full of tomatoes.',
    'We hiked to the top of the hill. From there, we could see the whole town.|The scouts hiked to the top of the hill. From there, they could see the whole town.',
    'I heard a strange noise in the attic. I grabbed a flashlight and climbed the ladder.|Jamal heard a strange noise in the attic. He grabbed a flashlight and climbed the ladder.'],

  // formal or casual: sentence | formal version ('' when already formal)
  register: ['Could you please send me the schedule?|', 'I would like to request more information.|', 'Thank you for your time and consideration.|',
    'The results of the experiment were surprising.|', 'I am writing to apply for the volunteer position.|', 'Please let me know if you have any questions.|',
    'Our group respectfully disagrees with this decision.|', 'I apologize for arriving late to class.|',
    'Hey, what\'s up?|Hello, how are you?', 'Gimme the schedule.|Could you please give me the schedule?', 'That test was super hard, no joke.|The test was very difficult.',
    'Gonna be late, sorry!|I am sorry, but I will be late.', 'Thanks a bunch!|Thank you very much.', 'The movie was kinda boring.|The movie was somewhat boring.',
    'Wanna come to my party?|Would you like to come to my party?', 'LOL, that\'s so funny.|That is very funny.', 'This book is awesome!|This book is excellent.',
    'I dunno the answer.|I do not know the answer.', 'Yeah, I\'ll do it.|Yes, I will do it.'],

  // signal words: word | category
  signal: ['because|cause', 'since|cause', 'due to|cause', 'as a result of|cause', 'caused by|cause',
    'so|effect', 'as a result|effect', 'therefore|effect', 'consequently|effect', 'that is why|effect', 'for this reason|effect',
    'similarly|compare', 'likewise|compare', 'both|compare', 'in the same way|compare', 'just like|compare',
    'but|contrast', 'however|contrast', 'unlike|contrast', 'on the other hand|contrast', 'instead|contrast', 'in contrast|contrast',
    'first|begin', 'to begin|begin', 'at the start|begin', 'first of all|begin', 'next|middle', 'then|middle', 'after that|middle', 'second|middle',
    'finally|end', 'last|end', 'in the end|end', 'at last|end', 'for example|example', 'for instance|example', 'such as|example', 'to illustrate|example'],

  // collocations: sentence | answer (options make, take, do, have)
  colloc: ['We need to ___ a decision by Friday.|make', 'Everyone can ___ a mistake.|make', 'Close your eyes and ___ a wish.|make', 'It is easy to ___ friends at camp.|make',
    'Please do not ___ noise in the library.|make', '___ your bed every morning.|make', 'Let\'s ___ a photo of the sunset.|take', 'The players ___ turns at bat.|take',
    'Please ___ notes during the video.|take', 'Come in and ___ a seat.|take', 'I always ___ my homework after school.|do', 'Can you ___ the dishes tonight?|do',
    'Just try to ___ your best.|do', 'Could you ___ me a favor?|do', 'We ___ the laundry on Sundays.|do', 'I hope you ___ fun at the party.|have',
    'Do you ___ any questions?|have', 'We always ___ a good time at the zoo.|have', 'Let\'s ___ a picnic in the park.|have'],

  // phrasal verbs: base | sentence with ___ | answer | group (one per group on a sheet)
  phrasal: ['figure out|I can\'t ___ how to open this jar.|figure out|think', 'give up|Don\'t ___! You can finish the race.|give up|quit',
    'look into|The principal will ___ the missing books.|look into|study', 'run out of|We ___ milk, so Dad went to the store.|ran out of|use',
    'look up|___ the word in the dictionary.|Look up|search', 'put off|Don\'t ___ your homework until Sunday night.|put off|delay',
    'turn down|She ___ the job offer because it was too far away.|turned down|refuse', 'get along|My cat and dog ___ well.|get along|friend',
    'show up|Only five people ___ for practice yesterday.|showed up|arrive', 'come up with|Our group needs to ___ a name for the project.|come up with|think',
    'take off|The plane will ___ at noon.|take off|leave', 'set up|Help me ___ the tent before dark.|set up|build', 'break down|Our car ___ on the highway last night.|broke down|fail',
    'look after|My aunt will ___ our dog this weekend.|look after|care', 'wake up|I ___ at 6:30 every morning.|wake up|sleep', 'check out|You can ___ three books from the library.|check out|borrow',
    'find out|We will ___ our test scores tomorrow.|find out|think', 'pick up|Please ___ the toys on the floor.|pick up|clean'],

  // nominalization: verb | noun
  nominal: 'pollute pollution|erode erosion|evaporate evaporation|decide decision|explain explanation|discover discovery|arrive arrival|grow growth|develop development|invent invention|observe observation|protect protection|destroy destruction|describe description|predict prediction|conclude conclusion|fail failure|refuse refusal|analyze analysis|react reaction|migrate migration|settle settlement|expand expansion|persuade persuasion|compare comparison|produce production|consume consumption|choose choice|lose loss|solve solution',
  nominalRw: ['Because the factory polluted the river, the fish died.|The factory\'s pollution of the river killed the fish.',
    'The town decided to close the park, and people were angry.|The town\'s decision to close the park angered people.',
    'When the soil eroded, the farmers lost their crops.|Soil erosion caused the farmers to lose their crops.',
    'Scientists discovered penicillin, and this changed medicine.|The discovery of penicillin changed medicine.',
    'Because prices rose, families bought less.|The rise in prices led families to buy less.',
    'The colonists refused to pay the tax, which angered the king.|The colonists\' refusal to pay the tax angered the king.',
    'When the settlers arrived, the valley changed.|The arrival of the settlers changed the valley.',
    'The team analyzed the data carefully, so the results were strong.|Careful analysis of the data strengthened the results.',
    'People consume more energy in winter.|Energy consumption rises in winter.', 'Because the city grew quickly, it needed more schools.|The city\'s rapid growth created a need for more schools.',
    'The birds migrate south every fall.|The birds\' migration south happens every fall.', 'If we protect the wetlands, more animals will survive.|Protection of the wetlands will help more animals survive.'],

  // sentence frames for English learners: function | level (e emerging, x expanding, b bridging) | frames
  frames: {
    describe: { e: ['I see ___.', 'It is ___.', 'It has ___.', 'The ___ is ___.', 'It can ___.', 'It looks ___.'],
      x: ['The ___ is ___ and ___.', 'It has ___ and ___.', 'I notice that the ___ is ___.', 'It feels ___ because ___.', 'The ___ looks like ___.', 'One part of it is ___.'],
      b: ['One feature I notice is ___, which ___.', 'The ___ is not only ___ but also ___.', 'Compared with ___, it is ___.', 'What stands out most is ___ because ___.', 'It is ___, so it can ___.', 'If you look closely, you can see ___.'] },
    compare: { e: ['___ is like ___.', '___ is not like ___.', 'Both are ___.', '___ is bigger than ___.', '___ has ___, but ___ does not.', 'They are the same because ___.'],
      x: ['___ and ___ are alike because they both ___.', '___ is different from ___ because ___.', '___ is ___, but ___ is ___.', 'One thing they share is ___.', '___ has ___, while ___ has ___.', '___ is more ___ than ___.'],
      b: ['Although ___ and ___ both ___, they differ in ___.', 'Unlike ___, ___ ___.', '___ resembles ___ in that ___.', 'The most important difference is ___ because ___.', 'Similarly, ___.', 'On the other hand, ___.'] },
    cause: { e: ['___ because ___.', 'It happened because ___.', 'First ___. Then ___.', '___ made ___ happen.', 'It was ___, so ___.', 'The cause is ___.'],
      x: ['___ happened because ___.', 'Since ___, ___.', '___, so ___.', 'One reason ___ is ___.', 'When ___, ___.', 'The effect of ___ was ___.'],
      b: ['As a result of ___, ___.', '___ led to ___, which ___.', 'Because ___, ___; therefore, ___.', 'One consequence of ___ is ___.', 'If ___, then ___.', '___ was caused by ___, and this ___.'] },
    opinion: { e: ['I like ___.', 'I think ___.', 'My favorite is ___.', 'I like ___ because ___.', 'I do not like ___.', '___ is good because ___.'],
      x: ['In my opinion, ___.', 'I think ___ because ___.', 'I agree that ___ because ___.', 'I prefer ___ to ___ because ___.', 'One reason I believe ___ is ___.', 'I disagree that ___ because ___.'],
      b: ['From my point of view, ___ because ___.', 'I am convinced that ___, mainly because ___.', 'Although some people think ___, I believe ___.', 'The strongest reason for ___ is ___.', 'It is clear to me that ___, since ___.', 'While I understand ___, I still think ___.'] },
    sequence: { e: ['First, ___.', 'Next, ___.', 'Then, ___.', 'Last, ___.', 'After that, ___.', 'At the end, ___.'],
      x: ['First, ___. Second, ___.', 'Before ___, ___.', 'After ___, ___.', 'Next, ___, and then ___.', 'While ___, ___.', 'Finally, ___.'],
      b: ['To begin, ___.', 'Once ___, ___.', 'Meanwhile, ___.', 'Shortly after ___, ___.', 'By the time ___, ___.', 'In the end, ___ because ___.'] },
    ask: { e: ['What is ___?', 'Where is ___?', 'Who ___?', 'Can you ___?', 'Do you ___?', 'What do you ___?'],
      x: ['Why do you ___?', 'How do you ___?', 'When did you ___?', 'What happens when ___?', 'Can you tell me about ___?', 'How is ___ different from ___?'],
      b: ['What would happen if ___?', 'How do you know that ___?', 'Why do you think ___?', 'What evidence shows that ___?', 'Could you explain how ___?', 'What is the most important thing about ___?'] },
    request: { e: ['May I ___, please?', 'Can you help me ___?', 'I need ___, please.', 'Can I have ___, please?', 'Please ___.', 'Thank you for ___.'],
      x: ['Could you please ___?', 'Would you mind ___?', 'Is it OK if I ___?', 'Excuse me, can you ___?', 'I would like ___, please.', 'Thank you for helping me ___.'],
      b: ['Would it be possible to ___?', 'I was wondering if you could ___.', 'Could you please explain ___?', 'I would appreciate it if you ___.', 'Do you have time to ___?', 'Thank you for taking the time to ___.'] },
    discuss: { e: ['I agree with ___.', 'I disagree with ___.', 'I think ___.', 'Can you say ___ again, please?', 'My idea is ___.', 'I want to add ___.'],
      x: ['I agree with ___ because ___.', 'I disagree with ___ because ___.', 'I want to add on to what ___ said: ___.', 'So you are saying ___?', 'What do you mean by ___?', 'I have a different idea: ___.'],
      b: ['Building on what ___ said, ___.', 'I see it differently because ___.', 'If I understand you correctly, you are saying ___.', 'Could you clarify what you mean by ___?', 'That is a good point, but ___.', 'Another way to look at it is ___.'] },
  },
};
