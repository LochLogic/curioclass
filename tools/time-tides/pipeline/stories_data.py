# Curated historical stories, era briefings, guided story arcs, and major empire profiles.
# Designed to pair directly with the 39 historical-basemaps milestones (3000 BC - 2010 AD).

ERA_STORIES = {
    -10000: {
        "lead": "As the last Ice Age retreats and sea levels rise, human communities span every habitable continent—foraging, fishing, and domesticating the first wild grains in the Fertile Crescent.",
        "shifts": [
            {"title": "Fertile Crescent Proto-Farming", "lon": 38.0, "lat": 36.5, "text": "Early sedentary settlements like Göbekli Tepe and Jericho emerge along the Levantine corridor."},
            {"title": "Peopling of the Americas", "lon": -100.0, "lat": 35.0, "text": "Post-glacial hunting and gathering cultures flourish across North and South America."}
        ]
    },
    -8000: {
        "lead": "The Neolithic Revolution takes root independently in the Fertile Crescent, Yellow and Yangtze rivers, and Mesoamerica—anchoring permanent villages that will birth the first territories.",
        "shifts": [
            {"title": "Anatolian & Levantine Villages", "lon": 33.0, "lat": 37.8, "text": "Wheat, barley, sheep, and goats sustain dense mudbrick towns like Çatalhöyük."},
            {"title": "Early Rice & Millet Basins", "lon": 116.0, "lat": 31.5, "text": "Millet on the Yellow River and rice along the Yangtze lay the demographic base of East Asia."}
        ]
    },
    -5000: {
        "lead": "Irrigation canals transform desert river valleys into grain surpluses. Copper metallurgy spreads across Anatolia and the Balkans as farming reaches Europe and the Nile.",
        "shifts": [
            {"title": "Ubaid Mesopotamia", "lon": 45.5, "lat": 31.2, "text": "Canal-irrigated towns across southern Iraq pioneer temple economies and long-distance obsidian trade."},
            {"title": "Yangshao River Settlements", "lon": 111.0, "lat": 34.8, "text": "Painted-pottery villages thrive across China's central plains."}
        ]
    },
    -4000: {
        "lead": "The world's first true cities—Uruk in Sumer and predynastic towns along the Nile—rise alongside horse domestication on the Pontic-Caspian steppe.",
        "shifts": [
            {"title": "Urban Explosion at Uruk", "lon": 45.6, "lat": 31.3, "text": "Uruk grows to tens of thousands of residents, inventing cylinder seals and proto-writing."},
            {"title": "Steppe Horse Domestication", "lon": 46.0, "lat": 48.0, "text": "Pastoralists north of the Black and Caspian seas begin harnessing horses, transforming mobility."}
        ]
    },
    -3000: {
        "lead": "Along the Nile, Tigris-Euphrates, and Indus rivers, the first centralized states emerge from Neolithic farming villages, inventing writing to track grain, tribute, and boundaries.",
        "shifts": [
            {"title": "Unification of Upper & Lower Egypt", "lon": 31.2, "lat": 27.5, "text": "King Narmer unites the Nile Valley into history's first enduring territorial kingdom."},
            {"title": "Sumerian City-States of Ur & Uruk", "lon": 45.8, "lat": 31.0, "text": "Walled temple-cities compete across southern Mesopotamia, pioneering cuneiform and urban law."},
            {"title": "Indus Valley Urban Network", "lon": 68.5, "lat": 27.3, "text": "Planned brick cities like Harappa and Mohenjo-daro flourish across the Indus basin."}
        ]
    },
    -2000: {
        "lead": "Bronze-working kingdoms expand trade routes across Eurasia, linking Egypt's Middle Kingdom, Mesopotamian dynasties, and early East Asian settlements.",
        "shifts": [
            {"title": "Middle Kingdom Egypt", "lon": 31.5, "lat": 26.5, "text": "Pharaohs push forts deep into Nubia and secure trade routes to the Levant."},
            {"title": "Steppe Chariot Horizon", "lon": 65.0, "lat": 51.0, "text": "Spoked-wheel chariots and bronze metallurgy spread rapidly across the Eurasian steppe."}
        ]
    },
    -1500: {
        "lead": "An interconnected Late Bronze Age world takes shape: New Kingdom Egypt, the Hittite Empire, Mitanni, and Shang China compete through diplomacy, chariots, and royal marriages.",
        "shifts": [
            {"title": "Egypt's Levantine Reach", "lon": 34.5, "lat": 31.0, "text": "New Kingdom pharaohs extend imperial control into Canaan and Syria, colliding with the Hittites."},
            {"title": "Rise of Shang China", "lon": 114.3, "lat": 35.8, "text": "Along the Yellow River, Shang kings cast monumental bronzes and record divinations on oracle bones."}
        ]
    },
    -1000: {
        "lead": "In the aftermath of the Late Bronze Age Collapse, iron metallurgy transforms warfare. New kingdoms—Zhou China, early Israel, Phoenician sea-traders, and reviving Assyria—redraw the map.",
        "shifts": [
            {"title": "Zhou Mandate of Heaven", "lon": 111.0, "lat": 34.5, "text": "The Zhou overthrow the Shang and establish a feudal network of states across northern China."},
            {"title": "Phoenician Mediterranean Network", "lon": 35.5, "lat": 33.9, "text": "Tyre and Sidon seed trading colonies from Cyprus to Spain, spreading the alphabet."}
        ]
    },
    -700: {
        "lead": "The Neo-Assyrian Empire builds the ancient world's first true iron-age military superpower, deporting populations and stitching Mesopotamia, Syria, and Egypt under imperial roads.",
        "shifts": [
            {"title": "Neo-Assyrian Expansion", "lon": 43.1, "lat": 36.3, "text": "From Nineveh, Assyrian kings conquer Babylonia, Aram, and Israel with siege engineering."},
            {"title": "Greek Colonization Wave", "lon": 22.0, "lat": 38.5, "text": "City-states plant settlements across southern Italy, Sicily, and the Black Sea coast."}
        ]
    },
    -520: {
        "lead": "Darius I secures the Achaemenid throne and builds Persepolis, organizing the Persian Empire into twenty satrapies connected by the 2,700-kilometer Royal Road from Sardis to Susa.",
        "shifts": [
            {"title": "Darius I's Imperial Reorganization", "lon": 52.8, "lat": 29.9, "text": "Standardized gold darics, Aramaic bureaucracy, and postal relays bind Egypt, Anatolia, Mesopotamia, and the Indus."},
            {"title": "Kingdom of Kush on the Upper Nile", "lon": 33.7, "lat": 16.9, "text": "From Meroë, Nubian kings smelt iron and guard trade routes linking sub-Saharan Africa to the Mediterranean."}
        ]
    },
    -500: {
        "lead": "The Achaemenid Persian Empire stretches from the Aegean to the Indus—the largest empire the world had yet seen—while classical Greece, Carthage, and Magadha rise on its flanks.",
        "shifts": [
            {"title": "Achaemenid Royal Road", "lon": 52.5, "lat": 30.0, "text": "Cyrus and Darius organize twenty satrapies connected by postal relays from Sardis to Susa."},
            {"title": "Carthaginian Western Sea", "lon": 10.2, "lat": 36.8, "text": "Carthage dominates western Mediterranean trade from North Africa to Iberia and Sicily."},
            {"title": "Warring Zhou States", "lon": 114.0, "lat": 34.0, "text": "Fragmented Chinese states innovate iron plows, crossbows, and Confucian and Daoist philosophy."}
        ]
    },
    -400: {
        "lead": "In the wake of the Peloponnesian War, Greek city-states exhaust themselves while Achaemenid Persia holds the Near East and China enters the fierce Warring States era.",
        "shifts": [
            {"title": "Warring States of China", "lon": 113.5, "lat": 34.5, "text": "Seven major kingdoms—Qin, Chu, Qi, Zhao, Wei, Han, and Yan—compete with massive conscript armies."},
            {"title": "Post-Peloponnesian Greece", "lon": 22.4, "lat": 37.5, "text": "Sparta's victory over Athens leaves Greece divided, opening the door for Macedon to the north."}
        ]
    },
    -323: {
        "lead": "In eleven lightning years, Alexander of Macedon topples the Persian Empire and marches to the Indus. At his sudden death in Babylon, his realm spans three continents—poised to fracture.",
        "shifts": [
            {"title": "Alexander's Eurasian Sweep", "lon": 44.4, "lat": 32.5, "text": "Macedonian phalanxes erase Achaemenid rule from Egypt to Bactria, founding dozens of Alexandrias."},
            {"title": "Rise of Magadha & Maurya", "lon": 85.1, "lat": 25.6, "text": "In the Ganges plain, Chandragupta Maurya prepares to unify northern India in Alexander's wake."}
        ]
    },
    -300: {
        "lead": "Alexander's generals carve his empire into the Seleucid, Ptolemaic, and Antigonid kingdoms—while Chandragupta Maurya unifies northern India and Rome consolidates central Italy.",
        "shifts": [
            {"title": "Hellenistic Successor Kingdoms", "lon": 36.1, "lat": 36.2, "text": "Seleucus rules from Syria to Bactria while Ptolemy builds Alexandria into the Mediterranean's scholarly capital."},
            {"title": "Mauryan Expansion", "lon": 85.1, "lat": 25.6, "text": "Chandragupta defeats Seleucus's eastern frontier and builds India's first subcontinental empire."}
        ]
    },
    -260: {
        "lead": "After the devastating Kalinga War, Mauryan Emperor Ashoka renounces conquest by the sword—governing nearly the entire Indian subcontinent and dispatching Buddhist envoys to Sri Lanka and the Hellenistic world.",
        "shifts": [
            {"title": "Ashoka's Mauryan Zenith", "lon": 85.1, "lat": 25.6, "text": "Rock and pillar edicts inscribed across Afghanistan, India, and Nepal proclaim dhamma, hospitals, and religious tolerance."},
            {"title": "Ptolemaic & Seleucid Rivalry", "lon": 35.5, "lat": 33.5, "text": "Alexander's successor empires contest Syria and the Levant while Alexandria's Library becomes antiquity's intellectual capital."}
        ]
    },
    -250: {
        "lead": "Across temperate Europe, Iron Age Celtic (La Tène) societies flourish from Ireland and Iberia to the Danube, while in East Asia the state of Qin prepares its final campaign to unify China.",
        "shifts": [
            {"title": "Celtic La Tène Horizon", "lon": 2.5, "lat": 47.0, "text": "Celtic hillforts, ironworking, and gold torc trade networks span Gaul, Britain, Ireland, and Central Europe."},
            {"title": "Qin's Ascendancy in China", "lon": 108.9, "lat": 34.3, "text": "Legalist reforms turn Qin into an unmatched war machine poised to conquer the rival Warring States."},
            {"title": "Ashoka's Mauryan India", "lon": 85.1, "lat": 25.6, "text": "Emperor Ashoka rules nearly the entire Indian subcontinent, carving peace edicts on stone pillars."}
        ]
    },
    -220: {
        "lead": "In 221 BC, Qin Shi Huang conquers the last rival kingdom, unifying China for the first time—standardizing writing, weights, axle widths, and linking northern walls into the first Great Wall.",
        "shifts": [
            {"title": "First Imperial Unification of China", "lon": 108.9, "lat": 34.3, "text": "Qin replaces centuries of feudal kingdoms with centralized commanderies administered from Xianyang."},
            {"title": "Hellenistic & Punic Tensions", "lon": 12.5, "lat": 41.9, "text": "Rome and Carthage prepare for the Second Punic War as Hannibal marches through Celtic Iberia and Gaul."}
        ]
    },
    -200: {
        "lead": "Four continental giants anchor the Old World: the newly founded Han Dynasty in China, the Mauryan Empire in India, the Seleucid Kingdom in Persia, and a surging Roman Republic.",
        "shifts": [
            {"title": "Han Unification of China", "lon": 108.9, "lat": 34.3, "text": "Following Qin's short-lived unification, the Han Dynasty consolidates an enduring imperial bureaucracy."},
            {"title": "Xiongnu Steppe Confederation", "lon": 104.0, "lat": 46.5, "text": "Modu Chanyu unites nomadic tribes north of the Great Wall, rivaling Han power for centuries."},
            {"title": "Roman Victory over Carthage", "lon": 12.5, "lat": 41.9, "text": "Defeating Hannibal in the Second Punic War makes Rome master of the western Mediterranean."}
        ]
    },
    -100: {
        "lead": "Emperor Wu of Han pushes into Central Asia, opening the Silk Road that links Chang'an to Bactria, Parthia, and the expanding Roman Republic.",
        "shifts": [
            {"title": "Opening of the Silk Road", "lon": 82.0, "lat": 40.5, "text": "Han garrisons secure the Hexi Corridor and Tarim Basin, creating transcontinental trade arteries."},
            {"title": "Roman Republic Eats the Mediterranean", "lon": 23.7, "lat": 38.0, "text": "Greece, Macedonia, and western Anatolia fall under Roman provincial governors."}
        ]
    },
    -55: {
        "lead": "Julius Caesar pushes Roman legions deep into Celtic Gaul and crosses the Channel to Britannia, redrawing Western Europe's frontier permanently along the Rhine.",
        "shifts": [
            {"title": "Caesar's Gallic & British Expeditions", "lon": 2.0, "lat": 48.5, "text": "Celtic confederations under Vercingetorix make their stand in Gaul while Britain and Ireland remain independent Celtic realms."},
            {"title": "Han Protectorate of the Western Regions", "lon": 83.0, "lat": 41.5, "text": "Han China establishes formal administrative control over the Silk Road oases of the Tarim Basin."}
        ]
    },
    -1: {
        "lead": "Augustus transforms Rome into a Mediterranean-wide empire just as Han China reaches 57 million citizens. Between them, Parthia profits from every caravan of silk and glass.",
        "shifts": [
            {"title": "Pax Romana Begins", "lon": 12.5, "lat": 41.9, "text": "Rome controls every shoreline of the Mediterranean—'Mare Nostrum'—from Gibraltar to Judea."},
            {"title": "Parthian Crossroads", "lon": 48.0, "lat": 33.5, "text": "Arsacid kings hold Mesopotamia and Iran, blocking Roman expansion eastward."}
        ]
    },
    100: {
        "lead": "Classical antiquity reaches its geopolitical zenith: Rome, Parthia, the Kushan Empire, and Han China form an unbroken chain of four empires spanning from Scotland to Vietnam.",
        "shifts": [
            {"title": "Roman Peak Frontiers", "lon": 24.0, "lat": 45.5, "text": "Trajan pushes across the Danube into Dacia, bringing Rome near its maximum territorial extent."},
            {"title": "Kushan Bridge of Cultures", "lon": 69.2, "lat": 34.5, "text": "Straddling Afghanistan and northern India, the Kushans transmit Buddhism along the Silk Road."}
        ]
    },
    200: {
        "lead": "Plague, civil war, and frontier pressure strain both ends of Eurasia. Han authority fractures into warlord realms while Rome's Severan emperors militarize the Rhine and Euphrates.",
        "shifts": [
            {"title": "Twilight of the Han", "lon": 113.6, "lat": 34.7, "text": "The Yellow Turban Rebellion and rival warlords split China toward the Three Kingdoms era."},
            {"title": "Roman Frontier Fortifications", "lon": 9.0, "lat": 49.0, "text": "Stone limes and legionary fortresses harden the boundary between empire and Germanic tribes."}
        ]
    },
    225: {
        "lead": "Following the collapse of the Han Dynasty in 220 AD, China splits into the legendary Three Kingdoms—Cao Wei in the north, Shu Han in the southwest, and Eastern Wu along the Yangtze.",
        "shifts": [
            {"title": "Three Kingdoms Partition of China", "lon": 113.5, "lat": 31.5, "text": "Rival courts at Luoyang, Chengdu, and Jianye fight legendary campaigns that reshape Chinese statecraft and culture."},
            {"title": "Rise of Sasanian Persia", "lon": 51.4, "lat": 30.0, "text": "Ardashir I topples the Parthian Empire in 224 AD, founding a fiercely centralized Persian dynasty."}
        ]
    },
    260: {
        "lead": "Sasanian Shah Shapur I captures Roman Emperor Valerian at the Battle of Edessa—humbling Rome at the height of its Third-Century Crisis as Palmyra and the Gallic Empire briefly splinter off.",
        "shifts": [
            {"title": "Shapur I's Victory at Edessa", "lon": 38.8, "lat": 37.1, "text": "Sasanian cavalry shatter Rome's eastern legions, carving triumphal reliefs at Naqsh-e Rustam and dominating Mesopotamia."},
            {"title": "Three Kingdoms Endgame", "lon": 112.4, "lat": 34.6, "text": "Northern Cao Wei prepares to absorb Shu Han, setting the stage for China's brief Jin reunification."}
        ]
    },
    300: {
        "lead": "Diocletian splits Roman administration into the Tetrarchy to survive crisis, while the vigorous Sasanian dynasty replaces Parthia and the Jin briefly reunite China.",
        "shifts": [
            {"title": "The Roman Tetrarchy", "lon": 29.0, "lat": 40.8, "text": "Four co-emperors divide defense of the empire across Trier, Milan, Sirmium, and Nicomedia."},
            {"title": "Sasanian Persia", "lon": 51.4, "lat": 32.6, "text": "Centralized Zoroastrian shahs revive Persian imperial power from Ctesiphon."}
        ]
    },
    350: {
        "lead": "King Ezana of Aksum adopts Christianity and mints gold coins along the Red Sea—making Aksum one of the four great powers of late antiquity alongside Rome, Persia, and China.",
        "shifts": [
            {"title": "Peak of the Aksumite Empire", "lon": 38.7, "lat": 14.1, "text": "Controlling Adulis on the Red Sea, Aksum bridges Roman Mediterranean ships with Indian Ocean ivory and spice merchants."},
            {"title": "Samudragupta's Indian Campaigns", "lon": 82.9, "lat": 25.3, "text": "Gupta armies unify the Ganges heartland and extract tribute from kingdoms across northern and central India."}
        ]
    },
    400: {
        "lead": "The Roman Empire permanently divides into Western and Eastern halves as steppe migrations accelerate. In India, the Gupta Empire presides over a golden age of math and astronomy.",
        "shifts": [
            {"title": "Permanent East-West Roman Split", "lon": 18.0, "lat": 42.0, "text": "After Theodosius I dies in 395, Ravenna and Constantinople govern separate imperial courts."},
            {"title": "Gupta Golden Age", "lon": 82.0, "lat": 25.3, "text": "Chandragupta II unifies northern India, fostering Sanskrit literature and decimal mathematics."},
            {"title": "Hunnic Advance into Europe", "lon": 20.0, "lat": 47.0, "text": "Nomadic Hunnic horsemen push Goths and Vandals across the Danube and Rhine."}
        ]
    },
    450: {
        "lead": "Attila's Hunnic Empire shakes both halves of Rome to their core, while the Gupta Empire enjoys its classical zenith in India and maritime Funan links Indian Ocean trade to Southeast Asia.",
        "shifts": [
            {"title": "Attila's Hunnic Empire", "lon": 20.0, "lat": 47.0, "text": "From the Hungarian plain, Hunnic armies force tribute from Constantinople and invade Gaul on the eve of the Catalaunian Plains."},
            {"title": "Gupta Classical Flowering", "lon": 77.2, "lat": 26.5, "text": "Nalanda University and Sanskrit scholarship flourish across northern India before White Hun incursions."}
        ]
    },
    500: {
        "lead": "Western Roman rule has vanished, replaced by Ostrogothic Italy, Visigothic Spain, and Frankish Gaul. Yet the Eastern Roman (Byzantine) Empire and Sasanian Persia remain wealthy titans.",
        "shifts": [
            {"title": "Post-Roman Successor Kingdoms", "lon": 3.5, "lat": 46.5, "text": "Clovis unites the Franks in Gaul while Theodoric rules Italy from Ravenna."},
            {"title": "Northern Wei in China", "lon": 112.5, "lat": 34.6, "text": "Xianbei rulers sinicize northern China, carving monumental Buddhist grottoes at Longmen."}
        ]
    },
    550: {
        "lead": "In Mesoamerica, Teotihuacan and Classic Maya kingdoms like Tikal and Calakmul build towering pyramid cities, while in the Mediterranean Justinian's Byzantium reconquers Italy and North Africa.",
        "shifts": [
            {"title": "Classic Maya & Teotihuacan Zenith", "lon": -90.0, "lat": 17.5, "text": "Maya city-states weave dynastic alliances across the Petén jungle while Teotihuacan's influence spans central Mexico."},
            {"title": "Justinian's Byzantine Reconquest", "lon": 14.0, "lat": 41.0, "text": "Eastern Roman armies briefly restore imperial rule over Rome, Ravenna, Carthage, and southern Spain."}
        ]
    },
    600: {
        "lead": "The Sui Dynasty reunifies China after three centuries of division, the Göktürk Khaganate spans the entire steppe, and Byzantium and Persia lock into a catastrophic final war.",
        "shifts": [
            {"title": "Sui Reunification & Grand Canal", "lon": 116.0, "lat": 33.5, "text": "China is stitched back together economically by the Grand Canal linking north and south."},
            {"title": "First Turkic Khaganate", "lon": 95.0, "lat": 46.0, "text": "The Göktürks control the Silk Road steppe from the Black Sea to Manchuria."}
        ]
    },
    650: {
        "lead": "In the British Isles, Gaelic Irish, Pictish, and Brythonic Celtic kingdoms flourish beside the Anglo-Saxon Heptarchy, while Tang China expands westward and the Rashidun Caliphate transforms the Near East.",
        "shifts": [
            {"title": "Insular Celtic Golden Age", "lon": -6.5, "lat": 54.0, "text": "Monastic scholarship and illuminated manuscripts thrive across Gaelic Ireland, Dál Riata, Pictland, and Welsh kingdoms."},
            {"title": "Rashidun & Early Tang Surge", "lon": 44.0, "lat": 33.0, "text": "Arab armies topple Sasanian Persia just as Tang emperors extend Chinese borders deep into Central Asia."}
        ]
    },
    700: {
        "lead": "Emerging from Arabia, the Umayyad Caliphate rockets from the Atlantic to Central Asia in a single lifetime—reshaping the Mediterranean, Persia, and North Africa forever.",
        "shifts": [
            {"title": "Umayyad Transcontinental Sweep", "lon": 36.3, "lat": 33.5, "text": "From Damascus, Umayyad armies conquer Sasanian Persia, Byzantine Syria, Egypt, and the Maghreb."},
            {"title": "Tang Cosmopolitan China", "lon": 108.9, "lat": 34.3, "text": "Chang'an becomes the world's largest city, welcoming Persian, Sogdian, and Japanese envoys."}
        ]
    },
    750: {
        "lead": "At the midpoint of the 8th century, Tang China reaches its cultural and territorial height under Xuanzong—even as the Abbasid Revolution overthrows the Umayyads and Tang and Arab armies meet at Talas.",
        "shifts": [
            {"title": "High Tang & Battle of Talas", "lon": 71.5, "lat": 42.5, "text": "Tang China and the rising Abbasid Caliphate collide in Central Asia, accelerating the westward spread of papermaking."},
            {"title": "Abbasid Revolution", "lon": 44.4, "lat": 33.3, "text": "The Caliphate's center of gravity shifts from Damascus toward Mesopotamia, while Umayyad survivors establish Córdoba in Spain."}
        ]
    },
    800: {
        "lead": "On Christmas Day 800, Charlemagne is crowned Emperor in Rome. In Baghdad, the Abbasid Caliphate's House of Wisdom leads global science, while Tibet challenges Tang China.",
        "shifts": [
            {"title": "Charlemagne's Carolingian Empire", "lon": 6.1, "lat": 50.8, "text": "From Aachen, Frankish rule unites France, Germany, the Low Countries, and northern Italy."},
            {"title": "Abbasid Golden Age", "lon": 44.4, "lat": 33.3, "text": "Baghdad thrives as a global hub of algebra, medicine, and Indian Ocean trade."},
            {"title": "Tibetan Empire at Height", "lon": 91.1, "lat": 29.6, "text": "Tibetan armies control the Tarim Basin and briefly sack the Tang capital."}
        ]
    },
    850: {
        "lead": "Following the 843 Treaty of Verdun, Charlemagne's empire fractures into West, Middle, and East Francia—laying the permanent border blueprints of France and Germany as Viking longships reshape Britain and Ireland.",
        "shifts": [
            {"title": "Treaty of Verdun Partition", "lon": 5.5, "lat": 49.2, "text": "Three grandsons split the Carolingian realm, creating the contested Franco-German borderlands for the next millennium."},
            {"title": "Viking Settlements in Celtic Isles", "lon": -6.2, "lat": 53.3, "text": "Norse raiders found Dublin and challenge Gaelic, Pictish, and Anglo-Saxon kingdoms across the Irish and North seas."}
        ]
    },
    900: {
        "lead": "Great centralized empires splinter: Carolingian Europe divides into rival realms facing Viking raids, the Tang Dynasty collapses, and regional emirates chip away at Baghdad.",
        "shifts": [
            {"title": "Viking & Rus River Routes", "lon": 30.5, "lat": 50.4, "text": "Norse traders and raiders forge Kyivan Rus along the Dnieper and settle Normandy and Danelaw."},
            {"title": "Fragmentation of Tang & Abbasids", "lon": 114.0, "lat": 32.0, "text": "China enters the Five Dynasties period while Samanids and Tulunids assert autonomy."}
        ]
    },
    1000: {
        "lead": "At the turn of the millennium, Song China pioneers paper money and gunpowder, the Holy Roman Empire stabilizes Central Europe, and the Fatimids rule Cairo and the Red Sea.",
        "shifts": [
            {"title": "Song Commercial Revolution", "lon": 114.3, "lat": 34.8, "text": "Iron production, movable type, and maritime trade surge across Song China."},
            {"title": "Kyivan Rus & Christianization", "lon": 30.5, "lat": 50.4, "text": "Vladimir the Great aligns Rus with Byzantine Orthodoxy, anchoring Eastern Europe."}
        ]
    },
    1025: {
        "lead": "Rajendra Chola I launches an audacious blue-water naval expedition across the Bay of Bengal against Srivijaya—cementing the Chola Empire as the premier maritime power of the Indian Ocean.",
        "shifts": [
            {"title": "Chola Naval Expedition to Southeast Asia", "lon": 79.1, "lat": 10.8, "text": "From Thanjavur, Chola fleets open direct maritime trade corridors between southern India, Sumatra, and Song China."},
            {"title": "Ghaznavid Raids in South Asia", "lon": 68.4, "lat": 33.5, "text": "Mahmud of Ghazni expands from Afghanistan into Punjab, reshaping the northwestern frontier of India."}
        ]
    },
    1050: {
        "lead": "At the southern edge of the Sahara, the Ghana Empire (Wagadu) grows fabulously wealthy taxing gold-for-salt caravans, while the Seljuk Turks sweep into Persia and Iraq.",
        "shifts": [
            {"title": "Ghana Empire & Trans-Saharan Gold", "lon": -7.9, "lat": 15.7, "text": "Koumbi Saleh links West African goldfields to North African merchants, drawing Almoravid attention from the desert."},
            {"title": "Seljuk Advance into Baghdad", "lon": 51.6, "lat": 32.6, "text": "Tughril Beg's Seljuk Turks consolidate Persia, preparing to enter Baghdad and challenge Fatimid Egypt."}
        ]
    },
    1066: {
        "lead": "William of Normandy's victory at Hastings binds England to northern France for centuries, while Northern Song China booms with iron and printing and the Seljuks march toward Byzantine Anatolia.",
        "shifts": [
            {"title": "Norman Conquest of England", "lon": 0.5, "lat": 50.9, "text": "Normandy and England unite under one crown, transforming English law, language, and Anglo-French border politics."},
            {"title": "Northern Song & Liao Frontier", "lon": 114.3, "lat": 35.5, "text": "The wealthy Song Dynasty shares northern China with the Khitan Liao Dynasty along a negotiated diplomatic frontier."}
        ]
    },
    1100: {
        "lead": "Seljuk Turkic armies reshape Anatolia and the Middle East, triggering the First Crusade. Across North Africa and Iberia, the Almoravids unite Marrakech to Zaragoza.",
        "shifts": [
            {"title": "Seljuk Surge into Anatolia", "lon": 35.0, "lat": 39.0, "text": "After Manzikert (1071), Turkic rule spreads across Asia Minor, reshaping the Byzantine heartland."},
            {"title": "Almoravid Trans-Saharan Realm", "lon": -7.9, "lat": 31.6, "text": "Gold caravans link West Africa directly to Morocco and Al-Andalus."}
        ]
    },
    1127: {
        "lead": "In the Jingkang Incident, Jurchen Jin cavalry capture Kaifeng and seize northern China, forcing the Song court to flee south to Hangzhou—splitting China along the Huai River for over a century.",
        "shifts": [
            {"title": "Jurchen Jin vs. Southern Song", "lon": 116.5, "lat": 33.0, "text": "Northern China falls to the Jurchen Jin while the Southern Song turns Hangzhou into a maritime commercial marvel."},
            {"title": "Crusader States in the Levant", "lon": 35.2, "lat": 31.8, "text": "The Kingdom of Jerusalem and neighboring Latin states hold a narrow coastal strip along the eastern Mediterranean."}
        ]
    },
    1180: {
        "lead": "Henry II's Angevin Empire stretches from the Scottish border to the Pyrenees, Saladin unites Egypt and Syria under the Ayyubid banner, and Khmer kings build Angkor's vast stone temples.",
        "shifts": [
            {"title": "The Angevin Empire", "lon": -0.5, "lat": 47.5, "text": "English monarchs control more of France than the French king himself, igniting a centuries-long territorial rivalry."},
            {"title": "Saladin's Ayyubid Unification", "lon": 36.3, "lat": 33.5, "text": "Uniting Cairo and Damascus, Saladin encircles the Crusader States on the eve of Hattin."},
            {"title": "Khmer Empire at Angkor", "lon": 103.8, "lat": 13.4, "text": "Jayavarman VII expands Angkor's hydraulic road network across mainland Southeast Asia."}
        ]
    },
    1200: {
        "lead": "On the Mongolian steppe, Temüjin—soon to be Genghis Khan—is uniting rival tribes. Meanwhile, Saladin's Ayyubids, the Jin and Southern Song, and feudal Europe stand unaware of the coming storm.",
        "shifts": [
            {"title": "Birth of the Mongol Empire", "lon": 107.0, "lat": 47.5, "text": "Temüjin consolidates the Mongolian plateau, forging a meritocratic decimal army."},
            {"title": "Divided China: Jin vs. Song", "lon": 118.0, "lat": 32.0, "text": "The Jurchen Jin hold the north while the wealthy Southern Song govern from Hangzhou."}
        ]
    },
    1279: {
        "lead": "Kublai Khan completes the conquest of Southern Song China, marking the zenith of Mongol Eurasia. Four allied khanates stretch unbroken from the Danube and Persian Gulf to the Sea of Japan.",
        "shifts": [
            {"title": "Pax Mongolica Across Eurasia", "lon": 116.4, "lat": 39.9, "text": "Kublai's Yuan Great Khanate rules all of China, connected by postal relays to Persia and Russia."},
            {"title": "Golden Horde & Ilkhanate", "lon": 48.0, "lat": 47.5, "text": "Mongol successor khanates govern the Russian principalities, Iran, Iraq, and Central Asia."}
        ]
    },
    1300: {
        "lead": "Four great Mongol khanates still span Eurasia, Marco Polo's travels have just been published, the Delhi Sultanate commands northern India, and Osman I plants the seed of the Ottoman state in Anatolia.",
        "shifts": [
            {"title": "Birth of the Ottoman Beylik", "lon": 29.8, "lat": 40.1, "text": "On the crumbling Byzantine frontier in northwestern Anatolia, Osman I founds a dynasty that will last 600 years."},
            {"title": "Mali & Trans-Saharan Gold", "lon": -7.9, "lat": 12.6, "text": "The Mali Empire rises along the Niger River, preparing for Mansa Musa's legendary golden age."}
        ]
    },
    1325: {
        "lead": "Fresh from his legendary pilgrimage to Mecca—where his generosity flooded Cairo with gold—Mansa Musa turns the Mali Empire into a global beacon of wealth and scholarship at Timbuktu.",
        "shifts": [
            {"title": "Mansa Musa's Mali Golden Age", "lon": -3.0, "lat": 16.7, "text": "Mali controls the Niger River bend from the Atlantic coast to Gao, building the Sankore universities of Timbuktu."},
            {"title": "Founding of Tenochtitlan", "lon": -99.1, "lat": 19.4, "text": "In the Valley of Mexico, the Mexica establish an island city on Lake Texcoco that will become the Aztec capital."}
        ]
    },
    1335: {
        "lead": "Under Muhammad bin Tughluq, the Delhi Sultanate reaches its widest territorial sweep across the Indian subcontinent—just as the Ilkhanate collapses in Persia and Vijayanagara rises in southern India.",
        "shifts": [
            {"title": "Delhi Sultanate at Maximum Extent", "lon": 77.2, "lat": 28.6, "text": "Tughluq armies briefly unify nearly all of India before overextension sparks regional sultanates and the Hindu Vijayanagara Empire."},
            {"title": "Collapse of the Mongol Ilkhanate", "lon": 46.3, "lat": 38.1, "text": "The death of Abu Sa'id without an heir splinters Persia into rival successor dynasties."}
        ]
    },
    1350: {
        "lead": "As the Black Death sweeps across Afro-Eurasia, England and France clash in the Hundred Years' War, Mali anchors West African gold routes, and the maritime Majapahit Empire dominates Indonesia.",
        "shifts": [
            {"title": "Hundred Years' War", "lon": 1.5, "lat": 48.0, "text": "English longbows win at Crécy as territorial claims over Aquitaine and the French crown tear Western Europe apart."},
            {"title": "Majapahit Maritime Thalassocracy", "lon": 112.4, "lat": -7.5, "text": "From Java, Majapahit's spice-trade fleets project influence across the Indonesian archipelago."}
        ]
    },
    1370: {
        "lead": "In 1368, Zhu Yuanzhang drives the Mongol Yuan back to the steppe and proclaims the Ming Dynasty—restoring native Han rule over China and launching massive border fortifications.",
        "shifts": [
            {"title": "Ming Expulsion of the Yuan", "lon": 118.8, "lat": 32.1, "text": "From Nanjing, the Hongwu Emperor consolidates all of China while the Northern Yuan retreats onto the Mongolian plateau."},
            {"title": "Ottoman Crossing into Europe", "lon": 26.5, "lat": 41.7, "text": "Establishing Edirne as their European capital, the Ottomans encircle Constantinople and advance into the Balkans."}
        ]
    },
    1400: {
        "lead": "After the Black Death shatters the Mongol order, the Ming Dynasty restores Han rule in China, Timur carves a dazzling Central Asian empire from Samarkand, and the Mali Empire gleams with gold.",
        "shifts": [
            {"title": "Timur's Conquests", "lon": 66.9, "lat": 39.6, "text": "From Samarkand, Timur builds a vast empire across Persia, Mesopotamia, and northern India."},
            {"title": "Ming Restoration", "lon": 118.8, "lat": 32.1, "text": "The Ming expel the Yuan, rebuild the Great Wall, and prepare Zheng He's treasure fleets."},
            {"title": "Kalmar Union of Scandinavia", "lon": 12.5, "lat": 55.7, "text": "Denmark, Norway, and Sweden unite under a single northern crown."}
        ]
    },
    1405: {
        "lead": "At Timur's death en route to invade Ming China, his Timurid Empire spans from Ankara and Damascus to Samarkand and Delhi—the same year Zheng He launches Ming China's colossal Indian Ocean treasure fleet.",
        "shifts": [
            {"title": "Timurid Empire at Maximum Reach", "lon": 66.9, "lat": 39.6, "text": "Samarkand glows with artisans gathered from Persia, Syria, and India as Timur's realm dominates Central Asia."},
            {"title": "Zheng He's First Treasure Voyage", "lon": 118.8, "lat": 32.1, "text": "Over 300 Ming ships sail into the Indian Ocean, projecting diplomatic power from Java to East Africa."}
        ]
    },
    1450: {
        "lead": "On the eve of the early modern world, the Americas see explosive imperial growth: Pachacuti expands Inca Tawantinsuyu from Cusco while the Aztec Triple Alliance dominates central Mexico.",
        "shifts": [
            {"title": "Inca Expansion from Cusco", "lon": -71.9, "lat": -13.5, "text": "Pachacuti transforms Cusco into the heart of a rapidly growing Andean empire linked by mountain highways."},
            {"title": "Aztec Triple Alliance", "lon": -99.1, "lat": 19.4, "text": "Tenochtitlan, Texcoco, and Tlacopan collect tribute from Mesoamerican city-states stretching toward both coasts."}
        ]
    },
    1492: {
        "lead": "The last year before permanent Afro-Eurasian and American contact: the Inca Tawantinsuyu spans the Andes, the Aztec Triple Alliance rules central Mexico, and Granada falls to Spain.",
        "shifts": [
            {"title": "Inca & Aztec Zeniths", "lon": -71.9, "lat": -13.5, "text": "Stone highways knit 4,000 km of the Andes together just as Tenochtitlan rivals Europe's largest cities."},
            {"title": "Rise of Moscow & Ottomans", "lon": 37.6, "lat": 55.7, "text": "Grand Duchy of Moscow throws off Mongol tribute while Ottomans rule from Constantinople."}
        ]
    },
    1500: {
        "lead": "Vasco da Gama has reached India around Africa, Columbus has crossed the Atlantic, and Cabral sights Brazil—triggering the Columbian Exchange and Europe's oceanic pivot.",
        "shifts": [
            {"title": "Portuguese Indian Ocean Entry", "lon": 75.8, "lat": 11.2, "text": "Direct sea routes bypass Ottoman and Venetian middlemen, linking Lisbon directly to Malabar spices."},
            {"title": "Safavid Awakening in Persia", "lon": 46.3, "lat": 38.1, "text": "Shah Ismail prepares to unite Iran from Tabriz, founding the Safavid Empire."}
        ]
    },
    1520: {
        "lead": "Askia Mohammad guides the Songhai Empire to its peak across West Africa, the Kingdom of Kongo negotiates with Portugal, Suleiman ascends the Ottoman throne, and Cortés lays siege to Tenochtitlan.",
        "shifts": [
            {"title": "Songhai Empire at Zenith", "lon": -0.05, "lat": 16.2, "text": "From Gao and Timbuktu, Songhai administers West Africa's largest pre-colonial empire with standing river fleets and legal courts."},
            {"title": "Ottoman & Safavid Ascendancy", "lon": 29.0, "lat": 41.0, "text": "Fresh from conquering Mamluk Egypt and Syria, the Ottomans become the paramount power of the Mediterranean and Red Sea."}
        ]
    },
    1530: {
        "lead": "Gunpowder and ocean caravels redraw the globe overnight. Spain claims Mexico and eyes Peru, Suleiman's Ottomans reach Vienna, and Babur founds the Mughal Empire in India.",
        "shifts": [
            {"title": "Spanish Empire in the Americas", "lon": -99.1, "lat": 19.4, "text": "Following Cortés's conquest of the Aztecs, New Spain becomes the anchor of Atlantic silver trade."},
            {"title": "Ottoman-Safavid-Mughal Trio", "lon": 29.0, "lat": 41.0, "text": "Three Islamic gunpowder empires dominate the entire belt from Hungary to Bengal."}
        ]
    },
    1550: {
        "lead": "With the Inca and Aztec empires conquered, Spain establishes the vast Viceroyalties of New Spain and Peru—shipping Potosí silver across both oceans as Portugal settles coastal Brazil.",
        "shifts": [
            {"title": "Potosí Silver & Viceroyalty of Peru", "lon": -65.7, "lat": -19.6, "text": "Andean silver mines finance Habsburg armies in Europe and flow across the Pacific to Ming China."},
            {"title": "Portuguese Brazil", "lon": -38.5, "lat": -12.9, "text": "Salvador da Bahia becomes the royal seat of Portugal's growing Atlantic sugar colony."}
        ]
    },
    1600: {
        "lead": "Silver mined in Potosí flows across both oceans to Ming China, creating the first truly global economy. Muscovy pushes across Siberia while Dutch and English trading companies challenge Iberia.",
        "shifts": [
            {"title": "Russian March Across Siberia", "lon": 85.0, "lat": 58.0, "text": "Cossack fur traders advance rapidly across Eurasia's northern rivers toward the Pacific."},
            {"title": "Mughal Consolidation under Akbar", "lon": 78.0, "lat": 27.2, "text": "Akbar unifies northern and central India into one of the wealthiest empires on Earth."}
        ]
    },
    1620: {
        "lead": "English, French, and Dutch colonies take root along North America's Atlantic coast and St. Lawrence River—just as Europe plunges into the Thirty Years' War and Manchu armies press Ming China.",
        "shifts": [
            {"title": "Colonial North America Takes Root", "lon": -71.0, "lat": 42.0, "text": "Jamestown, Plymouth, Quebec, and New Netherland plant rival European footholds beside powerful Indigenous confederacies like the Haudenosaunee."},
            {"title": "Thirty Years' War Ignites", "lon": 14.4, "lat": 50.1, "text": "Bohemian revolt triggers a devastating continental war that will redraw Central Europe's borders."}
        ]
    },
    1650: {
        "lead": "The Peace of Westphalia (1648) invents modern sovereign borders in Europe, while Manchu armies sweep into Beijing to establish the Qing Dynasty.",
        "shifts": [
            {"title": "Birth of Westphalian Sovereignty", "lon": 10.5, "lat": 51.0, "text": "Ending the Thirty Years' War, European states formalize territorial sovereignty and non-interference."},
            {"title": "Manchu Qing Conquest of China", "lon": 116.4, "lat": 39.9, "text": "Manchu banners topple the Ming and begin doubling China's imperial territory."}
        ]
    },
    1680: {
        "lead": "Emperor Aurangzeb pushes Mughal India toward its largest territorial span—yet in the Deccan mountains, Shivaji's Maratha Empire pioneers guerrilla sovereignty that will reshape South Asia.",
        "shifts": [
            {"title": "Mughal Peak & Maratha Challenge", "lon": 74.0, "lat": 18.5, "text": "While Mughal wealth peaks, the Maratha Confederacy carves an independent Hindu kingdom in western India."},
            {"title": "Qing & Russian Frontier Meeting", "lon": 124.0, "lat": 52.0, "text": "Manchu banners and Russian Cossacks collide along the Amur River, leading toward the 1689 Treaty of Nerchinsk."}
        ]
    },
    1700: {
        "lead": "At the dawn of the 18th century, Aurangzeb's Mughal Empire reaches its widest southern extent, the Kangxi Emperor stabilizes Qing China, and Europe braces for the War of the Spanish Succession.",
        "shifts": [
            {"title": "Mughal Maximum Extent", "lon": 77.2, "lat": 20.5, "text": "Mughal borders encompass nearly the entire Indian subcontinent before Maratha resistance rises."},
            {"title": "Great Northern War Begins", "lon": 30.3, "lat": 59.9, "text": "Peter the Great challenges Swedish dominance in the Baltic to forge a modern Russian Empire."}
        ]
    },
    1715: {
        "lead": "After the War of the Spanish Succession, Britain gains naval supremacy, Peter the Great westernizes Russia into a Baltic power, and the Mughal Empire begins to decentralize.",
        "shifts": [
            {"title": "Russian Empire Turns West", "lon": 30.3, "lat": 59.9, "text": "St. Petersburg becomes Russia's window on Europe as Tsardom transforms into Empire."},
            {"title": "Colonial Americas Mature", "lon": -75.0, "lat": -10.0, "text": "Spanish Viceroyalties, Portuguese Brazil, New France, and British colonies divide the hemisphere."}
        ]
    },
    1740: {
        "lead": "Military genius Nader Shah revives Persian power under the Afsharid dynasty—reclaiming borders from the Ottomans and Russians, sacking Mughal Delhi, and crossing into Central Asia.",
        "shifts": [
            {"title": "Nader Shah's Afsharid Empire", "lon": 59.6, "lat": 36.3, "text": "From Mashhad, Nader Shah briefly turns Persia into Asia's fiercest military power, fracturing Mughal authority in northern India."},
            {"title": "War of the Austrian Succession", "lon": 16.4, "lat": 50.8, "text": "Frederick the Great's Prussia seizes Silesia from Austria, elevating Prussia into a top-tier European power."}
        ]
    },
    1750: {
        "lead": "On the eve of the Seven Years' War, New France stretches from Quebec down the Mississippi to New Orleans, hemming in Britain's Thirteen Colonies—while Qianlong's Qing Empire nears its continental peak.",
        "shifts": [
            {"title": "New France vs. British America", "lon": -80.0, "lat": 40.5, "text": "Rival fur-trade and settler empires collide in the Ohio Valley, sparking the first truly global European war."},
            {"title": "Qing Consolidation of Inner Asia", "lon": 88.0, "lat": 43.0, "text": "Qing campaigns against the Dzungar Khanate prepare to incorporate Xinjiang into China's imperial borders."}
        ]
    },
    1783: {
        "lead": "The Treaty of Paris recognizes the independent United States, sparking an Age of Revolutions. Meanwhile, Qing China hits its historic peak and British influence deepens in Bengal.",
        "shifts": [
            {"title": "Birth of the United States", "lon": -77.0, "lat": 38.9, "text": "Thirteen colonies win independence from Britain, stretching to the Mississippi River."},
            {"title": "Qing Empire at Maximum Extent", "lon": 104.0, "lat": 36.0, "text": "Under Qianlong, Qing borders encompass Mongolia, Xinjiang, Tibet, and Taiwan."}
        ]
    },
    1800: {
        "lead": "Napoleon Bonaparte has just seized power in revolutionary France, preparing to upend Europe's ancient monarchies; across the Atlantic, the young United States eyes the vast Louisiana frontier.",
        "shifts": [
            {"title": "Napoleonic Europe Dawns", "lon": 2.3, "lat": 48.8, "text": "French revolutionary armies push borders to the Rhine and northern Italy, dissolving centuries-old feudal lines."},
            {"title": "British Consolidation in India", "lon": 76.6, "lat": 12.3, "text": "After defeating Tipu Sultan of Mysore, the British East India Company dominates southern and eastern India."}
        ]
    },
    1815: {
        "lead": "After Napoleon's defeat at Waterloo, diplomats at the Congress of Vienna redraw Europe to restore balance of power—even as independence wars ignite across Spanish America.",
        "shifts": [
            {"title": "Congress of Vienna Redraws Europe", "lon": 16.4, "lat": 48.2, "text": "Prussia, Austria, Russia, and Britain craft a conservative European border order lasting decades."},
            {"title": "Latin American Independence", "lon": -66.9, "lat": 10.5, "text": "Bolívar and San Martín challenge Spanish Viceroyalties from Caracas to Buenos Aires."}
        ]
    },
    1825: {
        "lead": "Three centuries of Iberian colonial rule collapse almost overnight: Gran Colombia, Mexico, Brazil, Peru, Bolivia, and Argentina stand as independent nations across the Western Hemisphere.",
        "shifts": [
            {"title": "Independence Across Latin America", "lon": -74.0, "lat": 4.6, "text": "After the Battle of Ayacucho (1824), Spanish mainland rule ends across South and Central America."},
            {"title": "Empire of Brazil & Federal Mexico", "lon": -43.2, "lat": -22.9, "text": "Brazil declares independence intact as an empire while Mexico stretches from Central America to California."}
        ]
    },
    1878: {
        "lead": "At the Congress of Berlin, Europe's great powers redraw the Balkans after the Russo-Turkish War—recognizing independent Romania, Serbia, and Montenegro while shrinking Ottoman Europe.",
        "shifts": [
            {"title": "Congress of Berlin & the Balkans", "lon": 23.3, "lat": 42.7, "text": "Ottoman territory in southeastern Europe contracts sharply as Bulgaria gains autonomy and Austria-Hungary occupies Bosnia."},
            {"title": "Meiji Modernization in Japan", "lon": 139.7, "lat": 35.7, "text": "Rapid industrialization transforms Japan into Asia's first modern constitutional great power."}
        ]
    },
    1880: {
        "lead": "Railroads, steamships, and telegraphs accelerate industrial empires. Germany and Italy have newly unified, Japan's Meiji Restoration modernizes East Asia, and Europe eyes Africa.",
        "shifts": [
            {"title": "German & Italian Unifications", "lon": 13.4, "lat": 52.5, "text": "Bismarck's German Empire reshapes Central Europe's balance of power overnight."},
            {"title": "British Raj Across India", "lon": 77.2, "lat": 28.6, "text": "Direct British Crown rule administers the Indian subcontinent and Burma."}
        ]
    },
    1885: {
        "lead": "At the Berlin Conference (1884–1885), European diplomats draw ruler-straight colonial claims across Africa without a single African representative present—accelerating the Scramble for Africa.",
        "shifts": [
            {"title": "Berlin Conference & Congo Free State", "lon": 21.0, "lat": -2.0, "text": "European powers establish 'effective occupation' rules, turning coastal trading posts into continent-spanning colonial borders."},
            {"title": "Ethiopian Sovereignty Holds", "lon": 38.7, "lat": 9.0, "text": "Emperor Yohannes IV and Menelik II modernize Ethiopia's army to defend its independence against European encroachment."}
        ]
    },
    1900: {
        "lead": "At the turn of the 20th century, European colonial rule reaches its global apex, the United States acquires overseas territories after 1898, and Qing China reels from the Boxer Uprising.",
        "shifts": [
            {"title": "Imperial High Tide in Africa & Asia", "lon": 24.0, "lat": -25.0, "text": "Britain fights the Boer War in southern Africa while French Indochina and German colonies harden global imperial maps."},
            {"title": "Twilight of Imperial China", "lon": 116.4, "lat": 39.9, "text": "Foreign spheres of influence and internal reform movements push the Qing Dynasty toward its final decade."}
        ]
    },
    1914: {
        "lead": "On the eve of World War I, European colonial empires claim over 80% of the globe's land surface, and Africa has been carved up almost entirely—yet rigid alliances sit on a powder keg.",
        "shifts": [
            {"title": "Scramble for Africa Complete", "lon": 18.0, "lat": 6.0, "text": "Following the Berlin Conference, European colonial lines slice across African kingdoms; only Ethiopia and Liberia remain independent."},
            {"title": "Powder Keg of Europe", "lon": 18.4, "lat": 43.8, "text": "The German, Austro-Hungarian, Russian, and Ottoman empires collide in the Balkans."}
        ]
    },
    1920: {
        "lead": "World War I shatters four multi-ethnic empires in a single stroke: the Russian, Ottoman, Austro-Hungarian, and German empires collapse, birthing Poland, Czechoslovakia, Yugoslavia, the USSR, and Middle Eastern mandates.",
        "shifts": [
            {"title": "Collapse of Central & Eastern Empires", "lon": 19.0, "lat": 50.0, "text": "New nation-states emerge across Central Europe from the ruins of Austria-Hungary and Imperial Germany."},
            {"title": "Partition of the Ottoman Middle East", "lon": 38.0, "lat": 34.0, "text": "Sykes-Picot and San Remo draw straight-line mandates across Syria, Iraq, Lebanon, and Palestine."},
            {"title": "Birth of the Soviet Union", "lon": 37.6, "lat": 55.7, "text": "Revolution and civil war transform the Russian Empire into the Bolshevik Soviet state."}
        ]
    },
    1930: {
        "lead": "A decade after Versailles, the Great Depression destabilizes interwar democracies—straining Weimar Germany, fueling nationalism in Japan, and deepening Stalin's industrialization of the USSR.",
        "shifts": [
            {"title": "Fragile Interwar Europe", "lon": 13.4, "lat": 52.5, "text": "Post-1919 borders across Poland, Czechoslovakia, and the Weimar Republic face mounting economic and political strain."},
            {"title": "Nationalist Consolidation in China", "lon": 118.8, "lat": 32.1, "text": "The Kuomintang nominally unifies much of China from Nanjing amid civil conflict and looming Japanese pressure."}
        ]
    },
    1938: {
        "lead": "On the brink of World War II, revisionist powers shatter the Versailles order: Nazi Germany annexes Austria and the Sudetenland, and Imperial Japan expands deep into Manchuria and eastern China.",
        "shifts": [
            {"title": "Anschluss & Munich Crisis", "lon": 14.5, "lat": 48.5, "text": "Germany absorbs Austria and dismembers Czechoslovakia as Europe slides toward global war."},
            {"title": "Japanese Expansion in East Asia", "lon": 124.0, "lat": 42.0, "text": "Manchukuo and coastal China fall under Imperial Japanese military occupation."}
        ]
    },
    1945: {
        "lead": "World War II ends with Germany and Korea divided, Japan stripped of its empire, Europe split by an emerging Iron Curtain, and anti-colonial movements surging across Asia and Africa.",
        "shifts": [
            {"title": "Division of Europe & Germany", "lon": 13.4, "lat": 52.5, "text": "Allied occupation zones harden into NATO and the Soviet Eastern Bloc."},
            {"title": "End of Axis Empires", "lon": 139.7, "lat": 35.7, "text": "Korea is divided at the 38th parallel and colonial rule in Southeast Asia begins to unravel."}
        ]
    },
    1947: {
        "lead": "At midnight on August 15, 1947, British rule in India ends in Independence and Partition—creating India and Pakistan along the hastily drawn Radcliffe Line and triggering history's largest mass migration.",
        "shifts": [
            {"title": "Independence & Partition of South Asia", "lon": 74.3, "lat": 31.5, "text": "The British Raj divides into the Dominions of India and Pakistan (West and East), reshaping borders for 400 million people."},
            {"title": "Cold War Lines Harden", "lon": 13.4, "lat": 52.5, "text": "The Truman Doctrine and Marshall Plan formalize the geopolitical divide between Western and Soviet spheres."}
        ]
    },
    1960: {
        "lead": "The 'Year of Africa': seventeen African nations declare independence in a single year, joining newly independent India, Pakistan, Indonesia, and Middle Eastern republics as European empires dissolve.",
        "shifts": [
            {"title": "The Year of Africa", "lon": 10.0, "lat": 8.0, "text": "French West Africa, Belgian Congo, Nigeria, and Somalia rapidly transition to sovereign republics."},
            {"title": "Partition & Post-Colonial Asia", "lon": 78.0, "lat": 23.0, "text": "Independent India, Pakistan, and the People's Republic of China reshape Asia's geopolitics."}
        ]
    },
    1994: {
        "lead": "The Cold War ends abruptly: the Soviet Union dissolves into fifteen independent republics, Germany reunifies, Yugoslavia fractures, and South Africa holds its first multiracial democratic election.",
        "shifts": [
            {"title": "Dissolution of the USSR", "lon": 55.0, "lat": 52.0, "text": "Fifteen new sovereign borders appear overnight from the Baltics and Ukraine to Kazakhstan."},
            {"title": "Reunified Germany & Fractured Balkans", "lon": 16.0, "lat": 45.0, "text": "The Berlin Wall's fall reunites Germany even as Yugoslavia breaks into warring republics."}
        ]
    },
    2000: {
        "lead": "Entering the 21st century, the European Union prepares to launch the Euro, Hong Kong and Macau have returned to China, and globalization knits sovereign borders into dense digital and trade networks.",
        "shifts": [
            {"title": "European Integration Deepens", "lon": 4.3, "lat": 50.8, "text": "Schengen open borders and monetary union reshape Western and Central Europe's economic geography."},
            {"title": "Rise of Emerging Economies", "lon": 116.4, "lat": 39.9, "text": "China prepares to join the WTO as India, Brazil, and ASEAN expand their global footprint."}
        ]
    },
    2010: {
        "lead": "A world of nearly 200 sovereign nation-states: borders are more legally codified than at any time in history, yet frozen conflicts, maritime claims, and regional unions continue to test the lines on the map.",
        "shifts": [
            {"title": "Modern Nation-State Mosaic", "lon": 15.0, "lat": 48.0, "text": "Supranational blocs like the European Union soften internal borders while external frontiers harden."},
            {"title": "Multipolar Asia-Pacific", "lon": 110.0, "lat": 30.0, "text": "China, India, ASEAN, and Japan anchor the 21st century's fastest-growing economic corridor."}
        ]
    }
}

STORY_ARCS = [
    {
        "id": "rome",
        "title": "The Rise & Fracture of Rome",
        "subtitle": "200 BC – 600 AD · 5 Chapters",
        "tag": "Classical Mediterranean",
        "chapters": [
            {"year": -200, "lon": 12.5, "lat": 40.0, "zoom": 3.4, "focus": ["Roman Republic", "Carthaginian Empire"], "title": "1. Master of the Western Sea", "text": "After surviving Hannibal's invasion, the Roman Republic leaps from an Italian power to a Mediterranean hegemon—setting its sights on Greece and the East."},
            {"year": 100, "lon": 16.0, "lat": 41.5, "zoom": 2.6, "focus": ["Roman Empire"], "title": "2. Mare Nostrum at Peak", "text": "Under Trajan, Roman borders encircle the entire Mediterranean from Hadrian's Wall to the Euphrates. A single currency, legal code, and road network bind 60 million people."},
            {"year": 400, "lon": 18.0, "lat": 42.5, "zoom": 2.8, "focus": ["Western Roman Empire", "Eastern Roman Empire"], "title": "3. One Empire Becomes Two", "text": "Too vast to defend from a single throne, Rome splits permanently in 395 AD. The wealthier East fortifies Constantinople while the West faces cascading frontier breaches."},
            {"year": 500, "lon": 10.0, "lat": 43.0, "zoom": 2.9, "focus": ["Eastern Roman Empire", "Ostrogoths", "Frankish Kingdom"], "title": "4. The Western Mosaic", "text": "Within a century, the Western Empire dissolves into Frankish, Ostrogothic, Visigothic, and Vandal kingdoms—sowing the map of medieval Europe."},
            {"year": 600, "lon": 26.0, "lat": 38.5, "zoom": 3.0, "focus": ["Eastern Roman Empire", "Sasanian Empire"], "title": "5. Byzantine Resilience", "text": "Far from falling, Eastern Rome endures as Byzantium—reconquering Italy and North Africa before locking horns with Sasanian Persia."}
        ]
    },
    {
        "id": "mongols",
        "title": "The Mongol Steppe Storm",
        "subtitle": "1200 – 1400 AD · 4 Chapters",
        "tag": "Eurasian Integration",
        "chapters": [
            {"year": 1200, "lon": 102.0, "lat": 44.0, "zoom": 2.4, "focus": ["Mongol Empire", "Song Empire", "Kara Khitai Khaganate"], "title": "1. Sparks on the Steppe", "text": "In 1200, Eurasia is a patchwork of wealthy sedentary dynasties—Song, Jin, Khwarazm, and Rus—separated by steppe tribes just beginning to unite under Temüjin."},
            {"year": 1279, "lon": 88.0, "lat": 43.0, "zoom": 1.65, "focus": ["Great Khanate", "Khanate of the Golden Horde", "Ilkhanate", "Chagatai Khanate"], "title": "2. The Largest Land Empire", "text": "By 1279, Kublai Khan completes the conquest of Song China. Four Mongol khanates stretch continuously from Eastern Europe to Korea, enabling Pax Mongolica trade."},
            {"year": 1279, "lon": 48.0, "lat": 44.0, "zoom": 2.8, "focus": ["Khanate of the Golden Horde", "Ilkhanate"], "title": "3. Western Khanates", "text": "The Golden Horde collects tribute from Russian princes while the Ilkhanate rules Persia and Baghdad—transforming both Islamic and Slavic political geography."},
            {"year": 1400, "lon": 82.0, "lat": 38.0, "zoom": 2.0, "focus": ["Ming Empire", "Timurid Empire", "White Horde"], "title": "4. After the Storm", "text": "Plague and succession wars shatter Mongol unity. The Ming reclaim China, while Timur briefly revives steppe conquest from Samarkand."}
        ]
    },
    {
        "id": "gunpowder",
        "title": "Gunpowder & Oceanic Empires",
        "subtitle": "1492 – 1715 AD · 4 Chapters",
        "tag": "Early Modern Shift",
        "chapters": [
            {"year": 1492, "lon": -68.0, "lat": 4.0, "zoom": 1.9, "focus": ["Inca Empire", "Aztec Empire", "Ming Empire"], "title": "1. Two Worlds Apart", "text": "In 1492, the Inca and Aztec empires command millions across the Americas, completely unconnected to Eurasia's Ming, Ottoman, and European courts."},
            {"year": 1530, "lon": 42.0, "lat": 32.0, "zoom": 2.2, "focus": ["Ottoman Empire", "Safavid Empire", "Mughal Empire"], "title": "2. The Gunpowder Belt", "text": "Cannon and muskets consolidate three vast Islamic empires—Ottoman, Safavid, and Mughal—controlling the overland crossroads between Europe and Asia."},
            {"year": 1650, "lon": 106.0, "lat": 35.0, "zoom": 2.2, "focus": ["Manchu Empire", "Tsardom of Muscovy"], "title": "3. Qing & Russian Giants", "text": "While Europe signs the Peace of Westphalia, Manchu armies establish the Qing Dynasty and Russian pioneers reach the Pacific Ocean."},
            {"year": 1715, "lon": -62.0, "lat": 8.0, "zoom": 1.6, "focus": ["Viceroyalty of New Spain", "Viceroyalty of Peru", "Viceroyalty of Brazil"], "title": "4. Transatlantic Viceroyalties", "text": "European maritime empires now administer entire American continents, linking Potosí silver, Atlantic plantations, and Asian textiles."}
        ]
    },
    {
        "id": "vienna_to_ww1",
        "title": "Revolutions to the Brink of 1914",
        "subtitle": "1783 – 1914 AD · 4 Chapters",
        "tag": "Modern Nation-States",
        "chapters": [
            {"year": 1783, "lon": -78.0, "lat": 37.0, "zoom": 2.5, "focus": ["United States of America", "Viceroyalty of New Spain"], "title": "1. A Republic in the Americas", "text": "The Treaty of Paris carves the independent United States out of British North America—igniting a wave of republican revolutions on both sides of the Atlantic."},
            {"year": 1815, "lon": 14.0, "lat": 49.0, "zoom": 3.2, "focus": ["Russian Empire", "Austrian Empire", "France", "Prussia"], "title": "2. The Congress of Vienna", "text": "After Napoleon's defeat, monarchs redraw Europe to prevent another continental conqueror—creating a delicate balance that holds for nearly a century."},
            {"year": 1880, "lon": 78.0, "lat": 24.0, "zoom": 2.4, "focus": ["British Raj", "Manchu Empire", "Russian Empire"], "title": "3. High Industrial Imperialism", "text": "Steamships and rail allow Britain's Raj, Tsarist Russia, and unified Germany to project power globally as traditional Asian empires strain under pressure."},
            {"year": 1914, "lon": 18.0, "lat": 6.0, "zoom": 1.9, "focus": ["French West Africa", "Anglo-Egyptian Sudan", "Algeria"], "title": "4. The Partitioned Planet", "text": "By 1914, almost all of Africa has been partitioned into European colonies, while Europe's great powers lock into rival alliances poised to shatter."}
        ]
    },
    {
        "id": "four_empires",
        "title": "The Shattering of Four Empires",
        "subtitle": "1914 – 1945 AD · 4 Chapters",
        "tag": "20th-Century Upheaval",
        "chapters": [
            {"year": 1914, "lon": 24.0, "lat": 47.0, "zoom": 2.8, "focus": ["Russian Empire", "Ottoman Empire", "German Empire", "Austria-Hungary"], "title": "1. Four Dynastic Giants", "text": "In July 1914, four sprawling dynastic empires—German, Austro-Hungarian, Russian, and Ottoman—still dominate Central Europe, Eurasia, and the Middle East."},
            {"year": 1920, "lon": 26.0, "lat": 45.0, "zoom": 2.6, "focus": ["USSR", "Poland", "Turkey", "Yugoslavia"], "title": "2. Redrawn Overnight", "text": "Four years of total war erase all four dynasties. New nation-states fill Central Europe, the USSR rises from Russia's ruins, and mandates partition the Middle East."},
            {"year": 1938, "lon": 15.0, "lat": 49.5, "zoom": 3.2, "focus": ["Germany", "USSR", "Italy"], "title": "3. The Fracturing Peace", "text": "Grievances over the 1919–1920 borders fuel revisionist expansion: Austria and Czechoslovakia fall as Europe marches into World War II."},
            {"year": 1945, "lon": 18.0, "lat": 50.0, "zoom": 2.6, "focus": ["USSR", "United States", "China"], "title": "4. Bipolar World", "text": "Out of 1945's rubble, the Iron Curtain divides Europe and two superpowers—the United States and the Soviet Union—define a new global order."}
        ]
    },
    {
        "id": "chinese_dynasties",
        "title": "The Cycle of Chinese Dynasties",
        "subtitle": "220 BC – 1750 AD · 6 Chapters",
        "tag": "East Asian Empires",
        "chapters": [
            {"year": -220, "lon": 109.0, "lat": 34.5, "zoom": 2.7, "focus": ["Qin", "Qin Dynasty"], "title": "1. First Unification Under Qin", "text": "In 221 BC, Qin Shi Huang ends centuries of Warring States fragmentation, forging China's first centralized imperial state and linking the northern frontier walls."},
            {"year": 100, "lon": 105.0, "lat": 35.0, "zoom": 2.4, "focus": ["Han", "Han Dynasty"], "title": "2. Han & the Silk Road", "text": "The Han Dynasty turns imperial unity into a 400-year golden age, pushing garrisons into the Tarim Basin to open direct trade with Central Asia and Rome."},
            {"year": 225, "lon": 112.0, "lat": 32.0, "zoom": 2.8, "focus": ["Cao Wei", "Shu Han", "Eastern Wu", "Cao Cao"], "title": "3. The Three Kingdoms", "text": "When the Han collapses, China fractures into three competing courts—Wei, Shu, and Wu—ushering in centuries of northern and southern division."},
            {"year": 750, "lon": 104.0, "lat": 35.5, "zoom": 2.3, "focus": ["Tang Dynasty", "Tang Empire"], "title": "4. Cosmopolitan High Tang", "text": "Reunified and outward-looking, Tang China becomes the cultural beacon of East Asia, with Chang'an welcoming merchants and envoys from Persia to Japan."},
            {"year": 1127, "lon": 114.0, "lat": 33.5, "zoom": 2.7, "focus": ["Great Jin", "Northern Song", "Southern Song"], "title": "5. Jin & Southern Song Split", "text": "Jurchen horsemen conquer northern China, pushing the Song south to Hangzhou—where maritime commerce, printing, and paper currency flourish."},
            {"year": 1750, "lon": 104.0, "lat": 37.0, "zoom": 2.1, "focus": ["Qing Dynasty", "Qing Empire"], "title": "6. Ming Restoration to Qing Peak", "text": "After the Ming expel the Mongol Yuan in 1368, the Manchu Qing expand China to its largest territorial footprint, encompassing Mongolia, Xinjiang, and Tibet."}
        ]
    },
    {
        "id": "americas_arc",
        "title": "The Americas: Empires to Independence",
        "subtitle": "550 – 1825 AD · 6 Chapters",
        "tag": "Western Hemisphere",
        "chapters": [
            {"year": 550, "lon": -92.0, "lat": 18.0, "zoom": 3.0, "focus": ["Teotihuacan", "Maya", "Tikal", "Moche"], "title": "1. Classic Mesoamerica & the Andes", "text": "Long before European contact, Teotihuacan, Classic Maya city-states, and Andean kingdoms build monumental cities, astronomy, and trade roads."},
            {"year": 1450, "lon": -80.0, "lat": 2.0, "zoom": 2.0, "focus": ["Inca Empire", "Aztec Empire", "Tawantinsuyu"], "title": "2. Rise of the Aztec & Inca", "text": "By 1450, the Aztec Triple Alliance commands central Mexico while Pachacuti's Inca state stitches together thousands of miles of the Andes."},
            {"year": 1550, "lon": -78.0, "lat": 0.0, "zoom": 1.8, "focus": ["Spanish Empire", "Viceroyalty of Peru", "Viceroyalty of New Spain"], "title": "3. Spanish Viceroyalties", "text": "Within decades of 1492, Spanish conquistadors topple both empires—reorganizing the hemisphere around Mexico City, Lima, and Potosí silver."},
            {"year": 1620, "lon": -74.0, "lat": 41.0, "zoom": 2.8, "focus": ["Spanish Empire", "New France", "English Colonies", "Haudenosaunee"], "title": "4. Colonial North America", "text": "English, French, and Dutch settlements take root along the Atlantic and St. Lawrence alongside powerful Indigenous nations."},
            {"year": 1750, "lon": -82.0, "lat": 39.0, "zoom": 2.4, "focus": ["New France", "British Empire", "Spanish Empire"], "title": "5. Imperial Rivalry in North America", "text": "New France wraps from Quebec to Louisiana behind Britain's Thirteen Colonies—setting the stage for the Seven Years' War and the American Revolution."},
            {"year": 1825, "lon": -68.0, "lat": -8.0, "zoom": 1.7, "focus": ["Gran Colombia", "Empire of Brazil", "Federated Republic of Mexico", "United States of America"], "title": "6. A Hemisphere of Republics", "text": "By 1825, independence wars sweep away Iberian colonial rule, birthing Mexico, Gran Colombia, Brazil, Peru, and Argentina."}
        ]
    },
    {
        "id": "celtic_medieval",
        "title": "Celtic Worlds & Medieval Europe",
        "subtitle": "250 BC – 1350 AD · 6 Chapters",
        "tag": "European Frontiers",
        "chapters": [
            {"year": -250, "lon": 2.0, "lat": 48.0, "zoom": 3.0, "focus": ["Celts", "Gaul", "Roman Republic"], "title": "1. Iron Age Celtic Europe", "text": "Before Roman expansion, Celtic-speaking tribes and hillfort confederations span from Ireland and Britain across Gaul to the Danube."},
            {"year": -55, "lon": 1.0, "lat": 49.0, "zoom": 3.2, "focus": ["Roman Republic", "Gaul", "Britannia"], "title": "2. Caesar Crosses to Gaul & Britain", "text": "Rome's conquest of Gaul pushes the imperial border to the Rhine and English Channel, leaving Ireland and northern Britain as independent Celtic bastions."},
            {"year": 650, "lon": -4.0, "lat": 54.0, "zoom": 3.8, "focus": ["Picts", "Dál Riata", "Northumbria", "Mercia", "Gwynedd"], "title": "3. Insular Celtic & Anglo-Saxon Isles", "text": "After Rome's withdrawal, Gaelic Irish, Pictish, and Welsh kingdoms flourish beside Anglo-Saxon realms in a vibrant patchwork of monastic learning."},
            {"year": 850, "lon": 6.0, "lat": 49.0, "zoom": 3.0, "focus": ["West Francia", "Middle Francia", "East Francia"], "title": "4. Verdun & the Viking Age", "text": "Charlemagne's empire divides into West, Middle, and East Francia while Norse fleets raid and settle along Britain, Ireland, and Normandy."},
            {"year": 1066, "lon": 1.0, "lat": 50.5, "zoom": 3.4, "focus": ["Kingdom of England", "Kingdom of France", "Kingdom of Scotland"], "title": "5. The Norman Transformation", "text": "William's 1066 victory binds England to Normandy, reshaping feudal borders across Britain, Ireland, and France."},
            {"year": 1350, "lon": 2.0, "lat": 48.0, "zoom": 3.2, "focus": ["Kingdom of France", "Kingdom of England", "Kingdom of Scotland", "Crown of Castile"], "title": "6. Hundred Years' War", "text": "Dynastic border wars between England and France forge early national identities across late-medieval Western Europe."}
        ]
    },
    {
        "id": "african_kingdoms",
        "title": "Kingdoms of Africa: Gold & Sovereignty",
        "subtitle": "350 – 1960 AD · 6 Chapters",
        "tag": "African History",
        "chapters": [
            {"year": 350, "lon": 38.7, "lat": 14.0, "zoom": 3.0, "focus": ["Aksumite Empire", "Kingdom of Aksum", "Axum"], "title": "1. Aksum & the Red Sea Crossroads", "text": "By 350 AD, Aksum stands as one of the ancient world's four great empires—minting gold coins and linking East African highlands to Rome and India."},
            {"year": 1050, "lon": -6.0, "lat": 15.0, "zoom": 2.8, "focus": ["Ghana Empire", "Almoravid Dynasty", "Fatimid Caliphate"], "title": "2. Wagadu (Ghana) & Saharan Gold", "text": "Controlling the southern terminus of trans-Saharan salt-and-gold caravans, the Ghana Empire anchors West African trade and statecraft."},
            {"year": 1325, "lon": -4.0, "lat": 15.5, "zoom": 2.8, "focus": ["Mali Empire", "Mamluk Sultanate"], "title": "3. Mansa Musa's Mali Golden Age", "text": "Following Mansa Musa's famed 1324 pilgrimage, Mali's borders stretch from the Atlantic to Gao, turning Timbuktu into a world-renowned center of scholarship."},
            {"year": 1520, "lon": 1.0, "lat": 15.0, "zoom": 2.6, "focus": ["Songhai Empire", "Ethiopian Empire", "Kingdom of Kongo"], "title": "4. Songhai, Kongo & Ethiopia", "text": "Under Askia Mohammad, the Songhai Empire governs the Sahel with river fleets and courts, while Kongo and Ethiopia thrive as sovereign Atlantic and Highland kingdoms."},
            {"year": 1885, "lon": 18.0, "lat": 4.0, "zoom": 1.9, "focus": ["British Africa", "French Africa", "Ethiopian Empire"], "title": "5. The Berlin Partition", "text": "In 1885, European powers carve up the continent at the Berlin Conference—imposing colonial lines that slice across historic kingdoms, while Ethiopia defends its sovereignty."},
            {"year": 1960, "lon": 16.0, "lat": 6.0, "zoom": 1.9, "focus": ["Nigeria", "Ghana", "Algeria", "Zaire", "Sudan"], "title": "6. Independence Reclaimed", "text": "In 1960's 'Year of Africa,' seventeen nations win independence in a single twelve-month span, transforming colonial territories into sovereign republics."}
        ]
    },
    {
        "id": "indian_ocean",
        "title": "South Asia & the Indian Ocean",
        "subtitle": "260 BC – 1947 AD · 6 Chapters",
        "tag": "Maritime & Subcontinental",
        "chapters": [
            {"year": -260, "lon": 80.0, "lat": 23.0, "zoom": 2.7, "focus": ["Maurya Empire", "Mauryan Empire"], "title": "1. Ashoka's Mauryan Unity", "text": "In 260 BC, Emperor Ashoka unites nearly the entire Indian subcontinent, inscribing edicts of dhamma and sending Buddhist missions across Asia."},
            {"year": 450, "lon": 80.0, "lat": 24.0, "zoom": 2.7, "focus": ["Gupta Empire"], "title": "2. The Gupta Golden Age", "text": "Under the Guptas, northern India enjoys a classical renaissance of decimal mathematics, astronomy, sculpture, and trans-oceanic trade."},
            {"year": 1025, "lon": 88.0, "lat": 10.0, "zoom": 2.4, "focus": ["Chola Dynasty", "Chola Empire", "Srivijaya"], "title": "3. Chola Blue-Water Empire", "text": "Rajendra Chola I projects naval power across the Bay of Bengal to Sumatra and Malaya, binding South India and Southeast Asia into a vibrant maritime web."},
            {"year": 1335, "lon": 78.0, "lat": 22.0, "zoom": 2.7, "focus": ["Tughlaq Dynasty", "Delhi Sultanate", "Vijayanagara Empire"], "title": "4. Delhi Sultanate & Vijayanagara", "text": "The Tughluq Delhi Sultanate reaches its widest sweep across India just as the Vijayanagara Empire rises to champion southern Indian culture."},
            {"year": 1680, "lon": 77.0, "lat": 22.0, "zoom": 2.6, "focus": ["Mughal Empire", "Maratha Empire", "Maratha Confederacy"], "title": "5. Mughal Zenith & Maratha Rise", "text": "Accounting for a quarter of world output, the Mughal Empire pushes to its widest frontiers while the Marathas forge a dynamic challenger state in the Deccan."},
            {"year": 1947, "lon": 76.0, "lat": 24.0, "zoom": 2.6, "focus": ["Dominion of India", "Dominion of Pakistan", "India", "Pakistan"], "title": "6. Independence & Partition", "text": "In August 1947, British colonial rule ends and the subcontinent divides into independent India and Pakistan—redrawing South Asia's modern map."}
        ]
    },
    {
        "id": "silk_road_persia",
        "title": "Silk Road Crossroads: Persia & Central Asia",
        "subtitle": "520 BC – 1740 AD · 6 Chapters",
        "tag": "Heart of Eurasia",
        "chapters": [
            {"year": -520, "lon": 53.0, "lat": 32.0, "zoom": 2.3, "focus": ["Achaemenid Empire"], "title": "1. Darius I & the Royal Road", "text": "From Persepolis and Susa, the Achaemenid Persians build the first transcontinental highway system, binding Egypt, Greece's doorstep, and the Indus."},
            {"year": 260, "lon": 52.0, "lat": 33.0, "zoom": 2.5, "focus": ["Sasanian Empire", "Roman Empire"], "title": "2. Sasanian Persia Humbles Rome", "text": "After defeating Emperor Valerian at Edessa, Shapur I establishes Sasanian Persia as Rome's co-equal superpower and gatekeeper of Silk Road trade."},
            {"year": 750, "lon": 62.0, "lat": 37.0, "zoom": 2.3, "focus": ["Abbasid Caliphate", "Tang Dynasty", "Uyghur Khaganate"], "title": "3. Abbasids & Tang Meet at Talas", "text": "The Abbasid Revolution shifts Islamic power toward Persia and Baghdad just as Arab and Tang Chinese armies meet in Central Asia."},
            {"year": 1405, "lon": 63.0, "lat": 37.0, "zoom": 2.4, "focus": ["Timurid Empire", "Ming Dynasty"], "title": "4. Timur's Samarkand Empire", "text": "From Samarkand, Timur carves a breathtaking empire across Persia, Mesopotamia, and Central Asia—sparking the turquoise-domed Timurid Renaissance."},
            {"year": 1530, "lon": 53.0, "lat": 33.0, "zoom": 2.6, "focus": ["Safavid Empire", "Ottoman Empire", "Mughal Empire"], "title": "5. Safavid Revival of Iran", "text": "The Safavids reunify Persia under a distinct Shi'a imperial identity, turning Isfahan into one of the early modern world's grandest capitals."},
            {"year": 1740, "lon": 58.0, "lat": 34.0, "zoom": 2.5, "focus": ["Afsharid Iran", "Mughal Empire", "Russian Empire"], "title": "6. Nader Shah's Lightning Empire", "text": "Nader Shah drives back Ottoman and Russian encroachment and marches to Delhi—one final dramatic expansion of Persian power across the Silk Road."}
        ]
    },
    {
        "id": "decolonization",
        "title": "Decolonization & Today's Borders",
        "subtitle": "1945 – 2010 AD · 4 Chapters",
        "tag": "The Modern Map",
        "chapters": [
            {"year": 1945, "lon": 22.0, "lat": 10.0, "zoom": 1.8, "focus": ["India", "Algeria", "Zaire"], "title": "1. Dusk of Colonialism", "text": "Exhausted by war, European powers can no longer hold overseas empires. Independence movements surge from Delhi to Algiers and Accra."},
            {"year": 1960, "lon": 16.0, "lat": 6.0, "zoom": 2.1, "focus": ["Algeria", "Sudan", "Zaire", "Nigeria"], "title": "2. The Year of Africa", "text": "In 1960 alone, seventeen African nations declare independence, transforming colonial administrative lines into sovereign national borders."},
            {"year": 1994, "lon": 54.0, "lat": 52.0, "zoom": 2.0, "focus": ["Russia", "Kazakhstan", "Ukraine"], "title": "3. The Soviet Dissolution", "text": "In December 1991, the world's largest state dissolves peacefully into fifteen independent republics, redrawing Eurasia from the Baltics to Central Asia."},
            {"year": 2010, "lon": 15.0, "lat": 25.0, "zoom": 1.15, "focus": ["China", "India", "United States", "Russia"], "title": "4. Our Contemporary Atlas", "text": "Nearly 200 sovereign states now tile the continents—each border a palimpsest of ancient rivers, imperial treaties, and modern revolutions."}
        ]
    }
]

EMPIRE_BIOS = {
    "Roman Empire": {"capital": "Rome / Constantinople", "bio": "The archetypal Mediterranean empire, uniting Western Europe, North Africa, and the Levant under Roman law, paved highways, and civic architecture for over four centuries before splitting East and West."},
    "Roman Republic": {"capital": "Rome", "bio": "An expansionist oligarchic republic that defeated Carthage and Hellenistic kingdoms to seize control of the Mediterranean basin before transitioning to imperial rule under Augustus."},
    "Western Roman Empire": {"capital": "Milan / Ravenna", "bio": "The western administrative half of the Roman world after 395 AD, battered by civil wars and Germanic migrations until its last emperor was deposed in 476 AD."},
    "Eastern Roman Empire": {"capital": "Constantinople", "bio": "Known to modern historians as the Byzantine Empire, the eastern half of Rome endured for a thousand years after the West fell, preserving Greek learning and Roman law."},
    "Achaemenid Empire": {"capital": "Persepolis / Susa", "bio": "Founded by Cyrus the Great, the first Persian Empire pioneered tolerant multi-ethnic governance through satrapies, a standardized postal road, and monumental architecture."},
    "Empire of Alexander": {"capital": "Babylon (planned)", "bio": "Forged in a decade of undefeated campaigns from Greece to the Indus River, Alexander's fleeting empire fused Greek and Near Eastern cultures across the Hellenistic world."},
    "Han Empire": {"capital": "Chang'an", "bio": "China's classical golden age: the Han established Confucian civil administration, invented papermaking, and opened the Silk Road into Central Asia."},
    "Han": {"capital": "Chang'an / Luoyang", "bio": "One of history's most influential dynasties, whose 400-year rule gave China's majority ethnic group its name and anchored the eastern terminus of the Silk Road."},
    "Mauryan Empire": {"capital": "Pataliputra", "bio": "First empire to unify most of the Indian subcontinent; under Ashoka the Great, it championed Buddhist dharma and erected inscribed stone edicts across South Asia."},
    "Gupta Empire": {"capital": "Pataliputra", "bio": "Presided over India's Classical Golden Age, pioneering zero and decimal notation, Sanskrit drama, and astronomical breakthroughs."},
    "Parthian Empire": {"capital": "Ctesiphon", "bio": "Rival of Rome for three centuries, the Arsacid Parthians blended Iranian and Hellenistic traditions while profiting from Silk Road trade across Mesopotamia and Iran."},
    "Sasanian Empire": {"capital": "Ctesiphon", "bio": "The last pre-Islamic Persian empire, renowned for centralized administration, Zoroastrian statecraft, and fierce cultural and military rivalry with Byzantium."},
    "Umayyad Caliphate": {"capital": "Damascus", "bio": "Expanded the early Islamic world at breathtaking speed from Iberia to Sindh, establishing Arabic as the administrative lingua franca across three continents."},
    "Abbasid Caliphate": {"capital": "Baghdad", "bio": "From its round capital of Baghdad, the Abbasids presided over the Islamic Golden Age of mathematics, optics, medicine, and global translation."},
    "Tang Empire": {"capital": "Chang'an", "bio": "A cosmopolitan high-water mark of Chinese civilization—celebrated for poetry, woodblock printing, Silk Road openness, and cultural influence across Korea and Japan."},
    "Song Empire": {"capital": "Kaifeng / Hangzhou", "bio": "An economic and technological powerhouse that introduced paper currency, magnetic compasses, gunpowder weapons, and bustling urban commerce."},
    "Great Khanate": {"capital": "Khanbaliq (Beijing)", "bio": "The Yuan heartland of the Mongol Empire under Kublai Khan, uniting all of China and Mongolia while serving as nominal suzerain over Eurasia's western khanates."},
    "Mongol Empire": {"capital": "Karakorum", "bio": "Founded by Genghis Khan in 1206, the Mongols built the largest contiguous land empire in human history, reconnecting East and West through Pax Mongolica."},
    "Khanate of the Golden Horde": {"capital": "Sarai", "bio": "The northwestern Mongol khanate that ruled the Pontic-Caspian steppe and exacted tribute from Russian principalities for over two centuries."},
    "Ilkhanate": {"capital": "Tabriz / Sultaniyya", "bio": "The Mongol khanate of Persia and Iraq, which patronized Persian miniature painting, astronomy, and trans-Eurasian diplomacy."},
    "Ming Empire": {"capital": "Nanjing / Beijing", "bio": "Restored native Han rule after the Mongols, constructing the Forbidden City, rebuilding the Great Wall in stone, and launching Zheng He's Indian Ocean voyages."},
    "Ming Chinese Empire": {"capital": "Beijing", "bio": "A vibrant commercial empire whose appetite for silver connected Spanish American mines and Japanese ports into the first truly global trade web."},
    "Ottoman Empire": {"capital": "Constantinople (Istanbul)", "bio": "For over six centuries, the Ottomans bridged Europe, Asia, and North Africa—commanding the Eastern Mediterranean, Balkans, and Arab heartlands until World War I."},
    "Mughal Empire": {"capital": "Agra / Delhi", "bio": "Founded by Babur and consolidated by Akbar, the Mughals unified most of South Asia, generating roughly a quarter of global GDP and iconic Indo-Persian architecture."},
    "Safavid Empire": {"capital": "Isfahan", "bio": "Reunified Iran under a distinctive Shi'a imperial identity, transforming Isfahan into an architectural jewel and rivaling the Ottomans for Mesopotamian frontiers."},
    "Manchu Empire": {"capital": "Beijing", "bio": "The Qing Dynasty, founded by Manchu banners, doubled imperial China's territory to encompass Manchuria, Mongolia, Xinjiang, and Tibet."},
    "Qing Empire": {"capital": "Beijing", "bio": "China's final imperial dynasty, reaching peak prosperity and territorial scale in the 18th century before facing internal rebellions and 19th-century imperialism."},
    "Timurid Empire": {"capital": "Samarkand", "bio": "Carved by Timur across Central Asia and Persia, igniting the Timurid Renaissance of turquoise-domed architecture, astronomy, and Persianate arts."},
    "Tsardom of Muscovy": {"capital": "Moscow", "bio": "Expanded rapidly from a forest principality across the Volga and Ural Mountains into Siberia, laying the geographic foundation of modern Russia."},
    "Russian Empire": {"capital": "Saint Petersburg", "bio": "Stretched across one-sixth of the Earth's landmass from Poland to Alaska, acting as a decisive great power in Europe and Central Asia until the 1917 Revolution."},
    "USSR": {"capital": "Moscow", "bio": "The Union of Soviet Socialist Republics (1922–1991), a nuclear superpower and ideological pillar of the Cold War whose dissolution created fifteen independent nations."},
    "Russia": {"capital": "Moscow", "bio": "The world's largest country by area, spanning eleven time zones across Eastern Europe and northern Asia following the 1991 breakup of the USSR."},
    "British Raj": {"capital": "Calcutta / New Delhi", "bio": "Direct British Crown rule over the Indian subcontinent (1858–1947), administering hundreds of millions of people via railways and civil services until Partition."},
    "Viceroyalty of New Spain": {"capital": "Mexico City", "bio": "Centerpiece of Spain's American empire, stretching from Central America across Mexico to California and linking Manila galleons to Seville."},
    "Viceroyalty of Peru": {"capital": "Lima", "bio": "Spain's South American imperial hub, built atop the former Inca realm and funded by vast Andean silver mines at Potosí."},
    "United States": {"capital": "Washington, D.C.", "bio": "Born from the 1776 Revolution, expanded across North America in the 19th century, and emerged after 1945 as a global economic and military superpower."},
    "United States of America": {"capital": "Philadelphia / Washington, D.C.", "bio": "The first modern constitutional federal republic in the Americas, whose rapid continental expansion reshaped the Western Hemisphere."},
    "China": {"capital": "Beijing", "bio": "Successor to millennia of imperial dynasties; following 20th-century revolution and reform, it grew into the world's second-largest economy and East Asia's pivotal power."},
    "India": {"capital": "New Delhi", "bio": "Emerging from British colonial rule in 1947 as the world's largest democracy, uniting immense linguistic and cultural diversity across South Asia."},
    "Seljuk Empire": {"capital": "Isfahan", "bio": "Turkic dynasty that unified Persia, Iraq, and Anatolia in the 11th century, reshaping the Islamic world and catalyzing the Crusades."},
    "Fatimid Caliphate": {"capital": "Cairo", "bio": "Shi'a caliphate that founded Cairo and Al-Azhar University, dominating North Africa, Sicily, and Red Sea commerce around 1000 AD."},
    "Tibetan Empire": {"capital": "Lhasa", "bio": "A formidable Himalayan military power of the 7th–9th centuries that controlled the Silk Road's southern rim and introduced Buddhism to Tibet."},
    "Carthaginian Empire": {"capital": "Carthage", "bio": "Phoenician maritime superpower in modern Tunisia that dominated western Mediterranean trade before its three epic Punic Wars with Rome."}
}
