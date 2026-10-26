"""The hand cuts for the Reading Room, kept as Python so they read easily; writes data/library/cuts.csv.

Each entry: id -> (pick, why). Pick syntax (see apply_cut in library_process.py): pieces split by " | ";
"#Heading" takes that heading's section ("#Heading @ words" picks the one holding the words); "start >> end" takes
a run of blocks between two phrases ("$" = to the end); "@N" names block N instead of a phrase (block numbers come
from `library_process.py --outline SOURCE`); a lone phrase takes one block; "[Label] " puts a heading on a piece;
"txt:first line" takes one poem from the book's plain-text file instead (for epubs that lost their stanzas).
Run: python scripts/library_cuts.py && python scripts/library_process.py <ids>
"""
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

CUTS = {
    # Aesop for Children: five fables a set
    "fables-k2-1": ("#THE LION AND THE MOUSE | #THE HARE AND THE TORTOISE | #THE ANTS AND THE GRASSHOPPER | "
                    "#THE FOX AND THE GRAPES | #THE CROW AND THE PITCHER", "set"),
    "fables-k2-2": ("#THE TOWN MOUSE AND THE COUNTRY MOUSE | #THE SHEPHERD BOY AND THE WOLF | #THE NORTH WIND AND THE SUN | "
                    "#THE DOG AND HIS REFLECTION | #THE ANT AND THE DOVE", "set"),
    "fables-k2-3": ("#THE GOOSE AND THE GOLDEN EGG | #THE FOX AND THE CROW | #TWO TRAVELERS AND A BEAR | "
                    "#THE CAT, THE COCK, AND THE YOUNG MOUSE | #THE FROGS AND THE OX", "set"),
    "fables-35-1": ("#BELLING THE CAT | #THE WOLF IN SHEEP'S CLOTHING | #THE FOX AND THE STORK | #THE BUNDLE OF STICKS | "
                    "#THE MILKMAID AND HER PAIL", "set"),
    "fables-35-2": ("#THE MILLER, HIS SON, AND THE ASS | #THE FROGS WHO WISHED FOR A KING | #THE LION'S SHARE | "
                    "#THE OAK AND THE REEDS | #THE BOY AND THE FILBERTS", "set"),
    "fables-35-3": ("#THE DOG IN THE MANGER | #THE WOLF AND THE CRANE | #THE ASS IN THE LION'S SKIN | "
                    "#THE FOX WITHOUT A TAIL | #THE TWO POTS", "set"),
    "andersen-soldier": ("#THE BRAVE TIN SOLDIER", "titled differently in this edition"),
    "andersen-pea": ("#THE PRINCESS AND THE PEA", "the full collection has it under this title"),
    "andersen-nightingale": ("#THE NIGHTINGALE", "in the full collection"),
    # Baldwin, Old Greek Stories (the book has no Hercules; set II is its other heroes)
    "baldwin-greek-1": ("#JUPITER AND HIS MIGHTY COMPANY | #THE GOLDEN AGE | #THE STORY OF PROMETHEUS | #THE FLOOD | "
                        "#THE WONDERFUL WEAVER | #THE LORD OF THE SILVER BOW | #THE HORSE AND THE OLIVE", "set: the gods"),
    "baldwin-greek-2": ("#CADMUS AND EUROPA | #THE QUEST OF MEDUSA'S HEAD | #THE STORY OF ATALANTA | "
                        "#THE ADVENTURES OF THESEUS | #THE WONDERFUL ARTISAN | #THE CRUEL TRIBUTE", "set: the heroes"),
    # Barker and Sinclair, West African Folk-Tales
    "westafrica-set": ("#II. HOW WISDOM BECAME | #III. ANANSI AND NOTHING | #IV. THUNDER AND ANANSI | #VI. TIT FOR TAT | "
                       "#VIII. THE SQUIRREL AND THE SPIDER | #XI. ANANSI THE BLIND FISHERMAN", "set of 6: Anansi"),
    "westafrica-set-2": ("#V. WHY THE LIZARD | #XX. HOW THE TORTOISE GOT ITS SHELL | #XXI. THE HUNTER AND THE TORTOISE | "
                         "#XXII. THE TAIL OF THE PRINCESS ELEPHANT | #XXX. KING CHAMELEON | #XXXV. HOW MUSHROOMS FIRST GREW",
                         "set of 6: tortoise and others"),
    # Bulfinch: chapters hold several myths with mixed heading levels, so cut by phrase
    "bulfinch-prometheus": ("The Roman poet Ovid gives us a connected narrative >> Thy godlike crime was to be kind", "chapter II"),
    "bulfinch-arachne": ("Minerva, the goddess of wisdom, was the daughter >> Oh, then, beware Arachne's fate", "chapter IX"),
    "bulfinch-orpheus": ("Orpheus was the son of Apollo and the muse >> Then on his ear what sounds", "chapter XVII"),
    "bulfinch-hercules": ("Hercules (in Greek, Heracles) was the son >> Deep degraded to a coward's slave", "chapter XII"),
    # Carroll: the poems are single blocks inside the chapters
    "jabberwocky": ("Twas brillig, and the slithy toves", "the poem alone"),
    "walrus-carpenter": ("The sun was shining on the sea", "the poem alone"),
    # Church, Stories from Livy
    "livy-romulus": ("#CHAPTER I. ~~ THE STORY OF ROMULUS", "chapter I"),
    "livy-horatius": ("#CHAPTER VI. ~~ THE STORY OF LARS PORSENNA", "chapter VI, Horatius at the bridge"),
    "livy-set": ("[The Story of Alba] #CHAPTER II. ~~ THE STORY OF ALBA | [The Story of Brutus] #CHAPTER V. ~~ THE STORY OF BRUTUS | "
                 "[The Story of Coriolanus] #CHAPTER VII. ~~ THE STORY OF CORIOLANUS | "
                 "[The Story of Cincinnatus] #CHAPTER IX. ~~ THE STORY OF CINCINNATUS | "
                 "[The Story of Camillus] #CHAPTER XII. ~~ THE STORY OF CAMILLUS", "set of 5: early heroes"),
    # Dayrell, Folk Stories from Southern Nigeria
    "nigeria-set": ("#Why the Bat flies by Night | #Why a Hawk kills Chickens | #Why the Flies Bother the Cows | "
                    "#Why the Cat kills Rats | #Why the Moon Waxes and Wanes | "
                    "#How the Tortoise overcame the Elephant", "set of 6: why stories"),
    # Dunbar-Nelson, Masterpieces of Negro Eloquence
    "eloquence-set": ("#WHAT TO THE SLAVE IS THE FOURTH OF JULY | #AN ADDRESS DELIVERED AT THE OPENING OF THE COTTON | "
                      "#CRISPUS ATTUCKS | #THE BLACK WOMAN OF THE SOUTH", "set of 4 speeches"),
    # Eastman, Wigwam Evenings: each evening's story sits under "N EVENING"
    "wigwam-set-1": ("[The Buffalo and the Field-Mouse] #FIRST EVENING | [The Frogs and the Crane] #SECOND EVENING | "
                     "[The Eagle and the Beaver] #THIRD EVENING | [The Raccoon and the Bee-Tree] #SIXTH EVENING", "set of 4"),
    "wigwam-set-2": ("[The Badger and the Bear] #SEVENTH EVENING | [The Good-Luck Token] #EIGHTH EVENING | "
                     "[Unktomee and His Bundle of Songs] #NINTH EVENING | [Unktomee and the Elk] #TENTH EVENING", "set of 4"),
    "wigwam-set-3": ("[The Little Boy Man] #FOURTEENTH EVENING | [The Return of the Little Boy Man] #FIFTEENTH EVENING | "
                     "[The Girl Who Married the Star] #TWENTY-THIRD EVENING | "
                     "[North Wind and Star Boy] #TWENTY-FOURTH EVENING", "set of 4"),
    # Linderman, Indian Why Stories
    "why-stories-1": ("#WHY THE CHIPMUNK'S BACK IS STRIPED | #HOW THE DUCKS GOT THEIR FINE FEATHERS | "
                      "#WHY THE KINGFISHER ALWAYS WEARS A WAR-BONNET | #WHY THE CURLEW'S BILL IS LONG AND CROOKED | "
                      "#WHY THE NIGHT-HAWK'S WINGS ARE BEAUTIFUL | #WHY THE MOUNTAIN-LION IS LONG AND LEAN", "set of 6"),
    "why-stories-2": ("#OLD-MAN REMAKES THE WORLD | #WHY BLACKFEET NEVER KILL MICE | #HOW THE OTTER SKIN BECAME GREAT | "
                      "#OLD-MAN STEALS THE SUN'S LEGGINGS | #WHY THE DEER HAS NO GALL | "
                      "#WHY THE BIRCH-TREE WEARS THE SLASHES IN ITS BARK", "set of 6"),
    # Wilhelm, The Chinese Fairy Book
    "chinese-set-1": ("#XI THE FOX AND THE TIGER | #XIV WHY DOG AND CAT ARE ENEMIES | "
                      "#XVI THE HERD BOY AND THE WEAVING MAIDEN | #XIX THE LADY OF THE MOON", "set of 4"),
    # The Real Mother Goose: one rhyme a heading
    "goose-animals": ("#THE MOUSE AND THE CLOCK | #LITTLE BO-PEEP | #BAA, BAA, BLACK SHEEP | #THE CAT AND THE FIDDLE | "
                      "#PUSSY-CAT AND QUEEN | #MY KITTEN | #TWO BIRDS | #LADYBIRD | #MARY'S CANARY | #THREE BLIND MICE",
                      "set of 10"),
    "goose-counting": ("#ONE, TWO, BUCKLE MY SHOE | #ONE, TWO, THREE | #ONE TO TEN | #FIVE TOES | #A COUNTING-OUT RHYME | "
                       "#GOING TO ST. IVES | #SOLOMON GRUNDY | #A WEEK OF BIRTHDAYS | #THIRTY DAYS HATH SEPTEMBER", "set of 9"),
    "goose-people": ("#JACK AND JILL | #HUMPTY DUMPTY | #LITTLE JACK HORNER | #MISS MUFFET | #OLD KING COLE | "
                     "#SIMPLE SIMON | #WEE WILLIE WINKIE | #MARY, MARY, QUITE CONTRARY | #LITTLE BOY BLUE | #PETER PIPER",
                     "set of 10"),
    "goose-weather": ("#RAIN @ go away | #DOCTOR FOSTER | #ONE MISTY MOISTY MORNING | #A SUNSHINY SHOWER | #MARCH WINDS | "
                      "#THE WINDS | #WINTER | #WHEN THE SNOW IS ON THE GROUND | #SUNSHINE | #THE FIRST OF MAY", "set of 10"),
    # Teasdale, Rainbow Gold
    "rainbow-gold-set": ("#MEG MERRILIES | #THE SONG OF WANDERING AENGUS | #SEA FEVER | #ESCAPE AT BEDTIME | #THE FAIRIES | "
                         "#STAR-TALK | #TIME, YOU OLD GIPSY MAN | #THE SNOW", "set of 8"),
    # Gibran, The Prophet: each sermon opens "Speak to us of ..."
    "prophet-set": ("[On Children] @134 >> @148 | [On Work] @201 >> @230 | [On Joy and Sorrow] @231 >> @246 | "
                    "[On Friendship] @444 >> @489", "set of 4 sermons"),
    # Cullen, Caroling Dusk: poem titles are plain lines, so cut by block
    "caroling-dusk": ("[We Wear the Mask (Paul Laurence Dunbar)] @76 >> @78 | "
                      "[The Negro Speaks of Rivers (Langston Hughes)] @813 >> @817 | [I, Too (Langston Hughes)] @791 >> @795 | "
                      "[To a Dark Girl (Gwendolyn B. Bennett)] @850 >> @852 | "
                      "[A Black Man Talks of Reaping (Arna Bontemps)] @893 >> @895 | "
                      "[Yet Do I Marvel (Countee Cullen)] @971 >> @972", "set of 6 poems"),
    # Dittmer, Te Tohunga
    "maori-set": ("[Tiki, the Ancestor of Mankind] #I TIKI—THE ANCESTOR OF MANKIND | "
                  "[The Creation of the Stars] #IV THE CREATION OF THE STARS | "
                  "[Maui and the Creation of New Zealand] #VIII MAUI—THE CREATION OF NEW ZEALAND | "
                  "[The Love of Hinemoa] #XII TE AROHA O THE LOVE OF HINEMOA", "set of 4"),
    # Sayers, Lord Peter Views the Body
    "lord-peter-views": ("#THE ENTERTAINING EPISODE OF THE ARTICLE IN QUESTION | "
                         "#THE FASCINATING PROBLEM OF UNCLE MELEAGER'S WILL | #THE LEARNED ADVENTURE OF THE DRAGON'S HEAD",
                         "set of 3"),
    # Milne, Now We Are Six
    "milne-six-poems": ("#KING JOHN'S CHRISTMAS | #BINKER | #US TWO | #FURRY BEAR | #THE ENGINEER | #SWING SONG | "
                        "#WIND ON THE HILL | #FORGIVEN", "set of 8"),
    # Dickinson: the epub lost the stanzas, the plain text kept them
    "dickinson-hope": ("txt:Hope is the thing with feathers", "the poem alone"),
    "dickinson-nobody": ("txt:I'm nobody!  Who are you?", "the poem alone"),
    "dickinson-death": ("txt:Because I could not stop for Death", "the poem alone"),
    "dickinson-frigate": ("txt:There is no frigate like a book", "the poem alone"),
    "dickinson-narrow": ("txt:A narrow fellow in the grass", "the poem alone"),
    "dickinson-success": ("txt:Success is counted sweetest", "the poem alone"),
    "poe-mother": ("Because I feel that, in the Heavens above >> than its soul-life", "the sonnet alone (the book has no heading for it)"),
    # single stories in collections whose title heading is also the book's
    "crane-open-boat": ("@45 >> @292", "the title story"),
    "wilde-happy-prince": ("@17 >> @102", "the title story"),
    "chopin-desiree": ("#DÉSIRÉE'S BABY", "one story from Bayou Folk"),
    "twain-jumping-frog": ("#THE NOTORIOUS JUMPING FROG OF CALAVERAS COUNTY", "the story, not Twain's joke retranslation"),
    "hughes-weary-blues": ("@39", "the title poem"),
    "teasdale-barter": ("txt:Life has loveliness to sell", "the poem alone"),
    "grimm-musicians": ("@1333 >> @1356", "the story (its title is a picture)"),
    "grimm-seven-kids": ("@373 >> @404", "the story (its title is a picture)"),
    "perrault-cinderella": ("#Cinderilla or The Little Glass Slipper", "the tale and its morals"),
    "china-pangu": ("#The Fashioner of the Universe", "the P'an Ku myth"),
    "spence-osiris": ("[The Myth of Osiris] #The Myth of Osiris | [The Grief of Isis] #The Grief of Isis", "two sections"),
    "spence-ra": ("#Ra, the Sun-God", "one section"),
    # single pieces whose headings are not their titles
    "poetic-edda": ("@38 >> @9118", "from the General Introduction to the last poem"),
    "age-of-innocence": ("@6 >> walked back alone to his hotel", "the novel, not the note on the text"),
    "constitution": ("We the people of the United States, in Order >> $", "the text, without the e-text notes"),
    "doctorow-printcrime": ("The coppers smashed my father's printer >> That's worth anything", "the story, not the bio"),
    "millay-candle": ("@8", "First Fig alone"),
    "teasdale-rains": ("@244 >> scarcely know that we were gone", "the poem alone"),
    "mccrae-flanders": ("@21", "the poem alone (the book opens with a memoir)"),
    "keller-story": ("@16 >> @379", "part I only (the letters and Sullivan's account follow)"),
    "prose-edda": ("#THE FOOLING OF GYLFE", "the Gylfaginning"),
    "space-tug": ("@47 >> @1294", "chapters 1-11, no ads"),
    "china-monkey": ("#How the Monkey Became a God", "chapter XIV"),
    "bulfinch-cupid": ("A certain king had three daughters >> @408", "the Psyche story, before chapter VII"),
    "christmas-carol": ("@29 >> $", "from Stave One"),
    "beowulf-verse": ("@4 >> @110", "the poem, no apparatus"),
    "beowulf-prose": ("@26 >> @406", "the story, no apparatus"),
    "declaration": ("@16 >> @51", "the text itself"),
    "doctorow-little-brother": ("@105 >> @3136", "the novel, no front or back matter"),
    "cane": ("@30 >> $", "the whole book"),
    "church-odyssey": ("@32 >> @729", "introduction and story, no contents or name list"),
    "ovid-pyramus": ("@510 >> @514", "Alcithoe's tale, without the argument and explanation"),
    "hawaii-folk": ("@14 >> @1005", "preface and tales, no glossary or ads"),
    "oedipus": ("@51 >> @53", "the play, without preface or notes"),
    "macaulay-horatius": ("@49 >> @125", "the lay, without the preface"),
}


def main():
    with open(ROOT / "data/library/cuts.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "pick", "why"])
        for k, (pick, why) in sorted(CUTS.items()):
            w.writerow([k, pick, why])
    print(len(CUTS), "cuts")


if __name__ == "__main__":
    main()
