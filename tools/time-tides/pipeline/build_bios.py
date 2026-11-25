import json, gzip, base64, math, re, zipfile, urllib.request, urllib.parse, concurrent.futures
from pathlib import Path
import sys

SCRATCH = Path(r"C:\Users\Cory\.gemini\antigravity\brain\6fbd6632-042c-48d5-b34e-bfe1abcf53d4\scratch")
ATLAS_B64 = SCRATCH / "atlas_data.b64"
CLIO_ZIP = SCRATCH / "cliopatria.geojson.zip"
BIOS_CACHE = SCRATCH / "wiki_bios_cache.json"

sys.path.insert(0, str(SCRATCH))
import stories_data

# Hand-crafted overviews for collective / regional / tricky labels that don't map 1:1 to a single Wikipedia article
CURATED_EXTRA = {
    "Central Asian Khanates": "A shifting constellation of Turkic and Turco-Mongol successor states—including the Khanates of Bukhara, Khiva, and Kokand, as well as the Kazakh Khanate—that controlled the Silk Road oases and steppes between Russia, Persia, and China from the 16th through 19th centuries.",
    "Chinese Warlords": "Following the fall of the Qing Dynasty in 1912 and Yuan Shikai's death in 1916, China fractured into competing regional military cliques—such as the Fengtian, Zhili, and Kuomintang factions—vying for national reunification.",
    "Post-Ming Warlords": "Regional Ming loyalists, rebel armies, and southern resistance regimes that held parts of China during the turbulent mid-17th-century transition from Ming to Manchu Qing rule.",
    "Hindu & Buddhist Kingdoms": "A diverse tapestry of regional South and Southeast Asian monarchies that fostered temple architecture, Sanskrit and Pali scholarship, and Indian Ocean maritime trade.",
    "Minor Hindu Kingdoms": "Regional Indian principalities and dynastic states—spanning Rajasthan, the Deccan, and southern India—operating alongside or between major subcontinental empires.",
    "Hindu kingdoms": "Independent Indian monarchies and regional dynasties flourishing across the subcontinent, cultivating classical literature, temple art, and inland commerce.",
    "Hindu kingdoms and republics": "Early South Asian mahajanapadas—combining hereditary monarchies and oligarchic republics—across the Ganges plain and Deccan during classical antiquity.",
    "Islamic and Hindu states": "Regional sultanates and Rajput or Deccan kingdoms coexisting across South Asia alongside the expanding Mughal Empire.",
    "Regional States": "Local kingdoms, federations, and autonomous realms occupying borderlands between continental empires.",
    "Indianized Kingdoms": "Early Southeast Asian polities—such as Funan, Champa, and Srivijaya—that blended indigenous governance with Indian script, statecraft, Hinduism, and Buddhism.",
    "Aramaean & Levantine Kingdoms": "Iron Age kingdoms of Syria and the Levant—including Aram-Damascus, Israel, Judah, and Phoenician city-states—straddling the trade crossroads between Egypt and Mesopotamia.",
    "Early City-States": "Fortified urban centers—pioneered in Sumer, Elam, and the Levant—that invented writing, codified law, and monumental temple administration.",
    "Zhou states": "Semi-independent feudal states—including Qin, Qi, Chu, Jin, and Yan—nominally under the Zhou Dynasty that competed fiercely during China's Spring and Autumn and Warring States periods.",
    "Sixteen Kingdoms": "A turbulent 4th-century era in northern China when numerous short-lived dynasties founded by steppe and Han rulers vied for control after the Western Jin collapse.",
    "French West Africa": "A vast federation of eight French colonial territories across the Sahel and Atlantic coast (1895–1960), administered from Dakar before dissolving into independent nations in 1960.",
    "French Equatorial Africa": "A federation of French colonial possessions across central Africa—comprising modern Chad, Central African Republic, Republic of the Congo, and Gabon—from 1910 until independence in 1960.",
    "French Indochina": "A grouping of French colonial territories in Southeast Asia (1887–1954) encompassing modern Vietnam, Laos, and Cambodia.",
    "French Africa": "France's sprawling African colonial sphere spanning the Maghreb, West Africa, Equatorial Africa, and Madagascar from the late 19th century until decolonization in the 1950s–1960s.",
    "British Africa": "Britain's African colonial territories—stretching from Egypt and Sudan through Kenya, Rhodesia, South Africa, Nigeria, and Ghana—administered under varied crown colony and protectorate models.",
    "British Colonial Empire": "Britain's global network of dominions, crown colonies, and protectorates spanning six continents, reaching its largest territorial extent in the early 20th century.",
    "Anglo-Egyptian Sudan": "A joint British-Egyptian condominium (1899–1956) administering the vast Nile basin south of Egypt until Sudan achieved independence.",
    "Belgian Congo": "Central Africa's vast Congo basin under Belgian colonial administration (1908–1960), following King Leopold II's Congo Free State, before winning independence in 1960.",
    "Congo-Léopoldville": "The newly independent Republic of the Congo (1960–1971), centered on Léopoldville (Kinshasa), navigating intense post-colonial crisis before being renamed Zaire in 1971.",
    "DR Congo": "The Democratic Republic of the Congo—Africa's second-largest country by area, renamed from Zaire in 1997 and spanning the mineral-rich Congo River basin.",
    "Zaire": "The name of the Democratic Republic of the Congo under Mobutu Sese Seko (1971–1997), marked by 'authenticity' cultural policies and Cold War geopolitics.",
    "Southern Rhodesia": "A self-governing British colony in southern Africa (1923–1980) centered on Salisbury (Harare), which achieved internationally recognized independence as Zimbabwe in 1980.",
    "Dutch East Indies": "The Dutch colonial archipelago across modern Indonesia (1800–1949), built atop the Dutch East India Company's spice-trade network until Indonesian independence.",
    "Rupert's Land": "A colossal North American territory encompassing the Hudson Bay drainage basin (1670–1870), granted to the Hudson's Bay Company before its transfer to the Dominion of Canada.",
    "New South Wales": "Britain's earliest Australian colony (founded 1788 at Sydney), which originally claimed the entire eastern half of the Australian continent before federating in 1901.",
    "Viceroyalty of New Granada": "Spain's northern South American colonial jurisdiction (1717–1819), centered on Bogotá and covering modern Colombia, Venezuela, Ecuador, and Panama.",
    "Viceroyalty of Brazil": "Portugal's vast South American colony, elevated to a viceroyalty in 1763 with Rio de Janeiro as capital before becoming the independent Empire of Brazil in 1822.",
    "United Provinces of the Río de la Plata": "The revolutionary union of South American provinces (1810–1831) centered on Buenos Aires that broke free from Spain and evolved into modern Argentina.",
    "Gran Colombia": "Simón Bolívar's short-lived northern South American republic (1819–1831) uniting modern Colombia, Venezuela, Ecuador, and Panama after independence from Spain.",
    "Denmark-Norway": "A maritime real union (1537–1814) uniting Denmark, Norway, Iceland, and Greenland under the Oldenburg crown until the 1814 Treaty of Kiel.",
    "Kalmar Union": "A personal union (1397–1523) joining the kingdoms of Denmark, Norway, and Sweden under a single Scandinavian monarch.",
    "Turan": "A historic Persianate geographical and political term for Central Asia north of the Oxus (Amu Darya), long inhabited by Turkic and Iranian-speaking peoples and khanates.",
    "Belarus": "An Eastern European nation bridging Poland, Russia, and Ukraine; historically part of Kyivan Rus, Lithuania, the Polish-Lithuanian Commonwealth, and the USSR before independence in 1991.",
    "Myanmar": "A Southeast Asian nation bridging South Asia and Indochina along the Irrawaddy River; known internationally as Burma until its official name change in 1989.",
    "Burma": "Historic name of Myanmar—home to the Pagan, Toungoo, and Konbaung kingdoms before British colonial annexation and independence in 1948.",
    "Persia": "The historic international name of Iran prior to 1935, home to a continuous succession of major empires from the Achaemenids and Sasanians to the Safavids and Qajars.",
    "Iran": "Officially adopted as the country's international name in 1935, spanning the Iranian Plateau from the Caspian Sea to the Persian Gulf.",
    "Cimmerians": "Ancient Indo-European nomadic horsemen from the Pontic steppe who raided Anatolia and the Near East in the 8th–7th centuries BC.",
    "Pechenegs": "Semi-nomadic Turkic steppe confederation that dominated the Pontic steppe north of the Black Sea from the 9th to 11th centuries, pressuring Byzantium and Kyivan Rus.",
    "Kara-Khanids": "The first Turkic Muslim dynasty in Central Asia (840–1212), ruling Transoxiana and Kashgar along the Silk Road.",
    "Kazakh Khanate": "A vast steppe khanate (1465–1847) uniting the Kazakh hordes across modern Kazakhstan between the Volga, Siberia, and the Silk Road oases.",
    "Khanate of Bukhara": "A major Uzbek-ruled Silk Road state (1500–1785) centered on Bukhara and Samarkand, famed for madrasas, trade, and Persianate scholarship.",
    "Khanate of Khiva": "A historic Central Asian oasis state (1511–1920) along the lower Amu Darya in Khwarazm, thriving on irrigated agriculture and caravan trade.",
    "Khanate of Kokand": "A dynamic Central Asian state (1709–1876) centered in the fertile Fergana Valley, controlling key mountain passes toward Qing Xinjiang.",
    "Dzungar Khanate": "The last great nomadic steppe empire (1634–1758), led by Oirat Mongols across Xinjiang and Central Asia before its conquest by the Qing Dynasty.",
    "Afsharid Iran": "A short-lived but formidable Persian empire (1736–1796) founded by military commander Nader Shah, briefly stretching from the Caucasus to Delhi.",
    "Cuman-Kipchak confederation": "A vast Turkic nomadic confederation (11th–13th centuries) spanning the Eurasian steppe from the Danube to Kazakhstan until the Mongol invasions.",
    "Kimek-Kipchak confederation": "An early medieval Turkic steppe confederation across western Siberia and northern Kazakhstan between the 9th and 11th centuries.",
    "Ruanruan": "The Rouran Khaganate (330–555 AD), a powerful proto-Mongolic steppe confederation north of China that pioneered the imperial title 'Khagan'.",
    "Rouran Khaganate": "A dominant nomadic steppe empire (330–555 AD) controlling Mongolia and Silk Road trade routes until overthrown by the Göktürks.",
    "Göktürks": "The First and Second Turkic Khaganates (552–744 AD), which spanned the Eurasian steppe from the Black Sea to Manchuria and left the earliest Turkic inscriptions.",
    "Xiongnu": "A formidable nomadic steppe empire (3rd century BC – 1st century AD) north of China whose rivalry with the Han Dynasty shaped the Great Wall and Silk Road.",
    "Satavahana Empire": "A major ancient Deccan dynasty (2nd century BC – 3rd century AD) that bridged northern and southern India and prospered through Roman Indian Ocean trade.",
    "Zhou": "China's longest-reigning dynasty (1046–256 BC), which introduced the Mandate of Heaven and birthed Confucianism, Daoism, and classical Chinese philosophy.",
    "Qin": "The western Chinese state that unified China in 221 BC under Qin Shi Huang, standardizing script, coinage, and imperial bureaucracy.",
    "Jin": "Chinese dynasty (266–420 AD) that briefly reunited China after the Three Kingdoms era before retreating south as the Eastern Jin.",
    "Great Jin": "The Jurchen-led Jin Dynasty (1115–1234) that conquered northern China from the Liao and Song, ruling from Beijing until the Mongol conquests.",
    "Northern Song": "The first half of China's Song Dynasty (960–1127), centered at Kaifeng, renowned for movable-type printing, paper money, and urban commerce.",
    "Southern Song": "The Song Dynasty after 1127, governing southern China from Hangzhou and pioneering blue-water maritime trade and gunpowder weapons.",
    "Yuan Dynasty": "The Mongol-led dynasty of China (1271–1368) founded by Kublai Khan, uniting all of China within the wider Pax Mongolica.",
    "Ming Dynasty": "Native Han dynasty (1368–1644) that expelled the Mongols, built the Forbidden City and stone Great Wall, and launched Zheng He's voyages.",
    "Qing Dynasty": "China's final imperial dynasty (1644–1912), founded by Manchu rulers who expanded imperial borders across Mongolia, Xinjiang, Tibet, and Taiwan.",
    "Tang Dynasty": "Widely regarded as China's cosmopolitan golden age (618–907), celebrated for poetry, Silk Road openness, and cultural leadership across East Asia.",
    "Han Dynasty": "Foundational Chinese empire (202 BC – 220 AD) that established Confucian governance, invented papermaking, and opened the Silk Road.",
    "Sui Empire": "Short-lived but pivotal dynasty (581–618) that reunified China after centuries of division and constructed the Grand Canal.",
    "Toba Wei": "The Northern Wei Dynasty (386–535), founded by Xianbei rulers who unified northern China and patronized monumental Buddhist cave art.",
    "Mali Empire": "A wealthy West African empire (c. 1230–1600) along the Niger River, famed for gold trade, Mansa Musa's pilgrimage, and the libraries of Timbuktu.",
    "Songhai Empire": "West Africa's largest pre-colonial empire (c. 1464–1591), centered at Gao and Timbuktu with river fleets, standing armies, and Islamic scholarship.",
    "Ghana Empire": "Known locally as Wagadu (c. 300–1200), West Africa's earliest major Sahelian empire, enriched by trans-Saharan gold-for-salt trade.",
    "Aksumite Empire": "A major Red Sea trading empire (c. 100–940 AD) in northern Ethiopia and Eritrea, known for monumental stelae, gold coinage, and early Christianity.",
    "Ethiopian Empire": "The historic highland monarchy of East Africa (1270–1974), which uniquely preserved its independence during the 19th-century Scramble for Africa.",
    "Inca Empire": "Tawantinsuyu (1438–1533), the largest empire in pre-Columbian America, knitting the Andes together with 40,000 km of stone highways from Cusco.",
    "Aztec Empire": "The Mexica-led Triple Alliance (1428–1521) centered on island capital Tenochtitlan, commanding tribute across central Mesoamerica.",
    "Chola Dynasty": "A maritime Tamil empire of southern India (9th–13th centuries) famous for bronze sculpture, grand temples, and naval expeditions to Southeast Asia.",
    "Tughlaq Dynasty": "A Turko-Indian dynasty of the Delhi Sultanate (1320–1413) that briefly unified nearly the entire Indian subcontinent.",
    "Delhi Sultanate": "A succession of five Islamic dynasties (1206–1526) ruling northern India from Delhi, blending Indo-Persian art, architecture, and governance.",
    "Sultanate of Delhi": "A succession of five Islamic dynasties (1206–1526) ruling northern India from Delhi, blending Indo-Persian art, architecture, and governance.",
    "Vijayanagara Empire": "A prosperous South Indian empire (1336–1646) centered at Hampi, celebrated for temple architecture, Sanskrit and Telugu arts, and spice trade.",
    "Maratha Confederacy": "An 18th-century Indian imperial confederacy that succeeded Mughal dominance across central and western India before colliding with British power.",
    "Ayyubid Sultanate": "Founded by Saladin in 1171, uniting Egypt, Syria, and Yemen and recapturing Jerusalem in 1187 during the Crusades.",
    "Mamluk Sultanate": "A military-aristocratic sultanate (1250–1517) ruling Egypt and Syria from Cairo, famed for halting the Mongol advance at Ain Jalut.",
    "Almoravid Dynasty": "A Berber imperial dynasty (c. 1050–1147) uniting Morocco, western Sahara, and Al-Andalus from its capital Marrakech.",
    "Almoravid dynasty": "A Berber imperial dynasty (c. 1050–1147) uniting Morocco, western Sahara, and Al-Andalus from its capital Marrakech.",
    "Rashidun Caliphate": "The first four caliphs of Islam (632–661), whose rapid expansion united Arabia, Persia, Syria, and Egypt within a single generation.",
    "Kyivan Rus": "A medieval East Slavic federation (9th–13th centuries) centered on Kyiv along the Dnieper trade route, ancestor of Ukraine, Belarus, and Russia.",
    "Kievan Rus": "A medieval East Slavic federation (9th–13th centuries) centered on Kyiv along the Dnieper trade route, ancestor of Ukraine, Belarus, and Russia.",
    "Kievan Rus'": "A medieval East Slavic federation (9th–13th centuries) centered on Kyiv along the Dnieper trade route, ancestor of Ukraine, Belarus, and Russia.",
    "Novgorod Republic": "A wealthy medieval Russian merchant republic (1136–1478) governing northern fur trade routes and participating in the Hanseatic League.",
    "Grand Duchy of Moscow": "The late-medieval Russian principality (1283–1547) that threw off Mongol tribute and unified northeastern Rus into the Tsardom of Russia.",
    "Tsardom of Russia": "The centralized Russian state (1547–1721) from Ivan the Terrible to Peter the Great, which expanded across Siberia to the Pacific Ocean.",
    "Holy Roman Empire": "A multi-ethnic Central European imperial confederation (800/962–1806) uniting hundreds of German, Bohemian, and northern Italian realms.",
    "Byzantine Empire": "The medieval continuation of the Eastern Roman Empire (330–1453) centered on Constantinople, blending Roman law, Greek culture, and Orthodox Christianity.",
    "Austrian Empire": "The Habsburg monarchy's centralized empire (1804–1867), a pillar of the Congress of Vienna before transforming into Austria-Hungary.",
    "Austria-Hungary": "The Dual Monarchy (1867–1918) uniting Austria and Hungary across Central Europe until its dissolution at the end of World War I.",
    "German Empire": "Unified under Bismarck in 1871, rapidly becoming continental Europe's leading industrial and military power until World War I.",
    "Kingdom of France": "Medieval and early modern France (987–1792), evolving from feudal duchies into Europe's archetype of royal absolutism.",
    "Kingdom of England": "Unified in the 10th century and reshaped by the 1066 Norman Conquest, laying the foundations of common law, Parliament, and the British state.",
    "Kingdom of Scotland": "An independent northern British kingdom (843–1707) forged from Pictish and Gaelic roots before uniting with England to form Great Britain.",
    "Spanish Empire": "One of history's first global empires (1492–1898), spanning Iberia, the Americas, and the Philippines and launching the first worldwide silver economy.",
    "Portuguese Empire": "Pioneered the Age of Discovery (1415–1999), linking Lisbon to Brazil, coastal Africa, India, Malacca, and Macau by sea.",
    "British Raj": "Direct British Crown rule over the Indian subcontinent (1858–1947), administering hundreds of millions across modern India, Pakistan, Bangladesh, and Burma.",
    "Dominion of India": "The newly independent Indian state (1947–1950) created at Partition before adopting its republican constitution in 1950.",
    "Dominion of Pakistan": "The newly independent state (1947–1956) formed at Partition, originally comprising West Pakistan and East Bengal (modern Bangladesh).",
    "North Korea": "The Democratic People's Republic of Korea, established in 1948 in the northern half of the Korean Peninsula after World War II.",
    "South Korea": "The Republic of Korea, established in 1948 in the southern half of the Korean Peninsula, rising into a major global industrial and technological democracy.",
    "United Kingdom": "The United Kingdom of Great Britain and Northern Ireland, a parliamentary constitutional monarchy whose industrial and maritime reach reshaped the modern world.",
    "Liao": "The Khitan-led Liao Dynasty (916–1125), a formidable dual-administration empire ruling Manchuria, Mongolia, and northern China alongside the Song Dynasty.",
    "Imperial Japan (Fujiwara)": "Heian-period Japan (794–1185), when the aristocratic Fujiwara clan dominated the imperial court at Kyoto as regents, presiding over classical Japanese court literature and art.",
    "Shogun Japan (Kamakura)": "The Kamakura Shogunate (1185–1333), Japan's first military government led by samurai shoguns, which successfully repelled two massive Mongol invasion fleets.",
    "Japan (Warring States)": "Japan's Sengoku ('Warring States') period (1467–1600), an age of rival daimyo warlords and castle-building that ended with unification under Oda Nobunaga, Toyotomi Hideyoshi, and Tokugawa Ieyasu.",
    "Mongol Khanate": "The Northern Yuan and post-imperial Mongol steppe khanates (14th–17th centuries) centered on the Mongolian plateau, maintaining Chinggisid royal lineages after retreating from Ming China.",
    "Ghaznavid Emirate": "A Persianate Turkic dynasty (977–1186) centered at Ghazni in Afghanistan that expanded across Khorasan and northern India, patronizing Persian literature such as Ferdowsi's Shahnameh.",
    "Tiahuanaco Empire": "Tiwanaku (c. 500–1000 AD), a monumental pre-Inca Andean polity near Lake Titicaca known for precision stone architecture, raised-field agriculture, and highland-to-coast trade.",
    "Maya city-states": "A network of competing Classic and Postclassic Maya kingdoms—including Tikal, Calakmul, Palenque, and Chichen Itza—famed for hieroglyphic writing, astronomy, and stepped pyramids.",
    "Maya chiefdoms and states": "Preclassic and Postclassic Maya polities across the Yucatán Peninsula and Central American highlands, linked by obsidian, jade, and cacao trade.",
    "Mesoamerican city-states and chiefdoms": "Early urban centers and regional kingdoms across central Mexico, Oaxaca, and the Gulf Coast—precursors to Teotihuacan, Monte Albán, and the Aztec Empire.",
    "Celtic kingdoms": "Independent Iron Age and early medieval Celtic realms across Ireland, Scotland, Wales, Cornwall, and Brittany, preserving Gaelic and Brythonic languages, law, and monastic scholarship.",
    "Burmese kingdoms": "Successive kingdoms along the Irrawaddy River—including Pagan, Ava, Pegu, and Toungoo—that shaped Theravada Buddhist culture and Southeast Asian geopolitics.",
    "Islamic city-states": "Independent coastal and oasis trading states—such as the Swahili Coast sultanates and Arabian Sea ports—linking Indian Ocean monsoons with inland Africa and Asia.",
    "Malaysian Islamic states": "Maritime Malay sultanates—including Malacca, Johor, Aceh, and Brunei—that controlled the Strait of Malacca and spread Islam and spice trade across Southeast Asia.",
    "England and Ireland": "The English Crown's rule over England and the Lordship/Kingdom of Ireland prior to the 1707 Union with Scotland.",
    "Sinic": "Early Sinitic-speaking farming and bronze-age societies of the Yellow and Yangtze river basins, ancestral to China's classical dynasties.",
    "Cambodia": "A Southeast Asian nation centered on the Mekong basin and Tonlé Sap, heir to the medieval Khmer Empire of Angkor.",
    "Malaya": "The Malay Peninsula, historic crossroads of the Strait of Malacca connecting Indian Ocean and South China Sea commerce.",
    "Ainu": "Indigenous people of Hokkaido, Sakhalin, and the Kuril Islands, renowned for distinctive animist traditions, bear ceremonies, and maritime hunting and trade.",
    "Maori": "The Indigenous Polynesian people of Aotearoa (New Zealand), whose voyaging ancestors settled the islands in the 13th–14th centuries and built fortified pā settlements.",
    "Māori": "The Indigenous Polynesian people of Aotearoa (New Zealand), whose voyaging ancestors settled the islands in the 13th–14th centuries and built fortified pā settlements.",
    "Papuans": "Diverse Indigenous Melanesian societies of New Guinea, home to one of the world's oldest independent centers of highland agriculture and over 800 languages.",
    "Shellfish gatherers": "Coastal foraging communities thriving along productive marine shorelines and estuaries, leaving extensive shell-midden archaeological records.",
    "Alwa": "Alodia (Alwa), the southernmost medieval Christian Nubian kingdom (6th–16th centuries) along the Blue and White Nile near modern Khartoum.",
    "Lunda": "The Lunda Empire (c. 1665–1887), a major Central African confederation spanning southern DR Congo, northeastern Angola, and northwestern Zambia.",
    "Luba": "The Luba Empire (c. 1585–1889), an influential Central African kingdom in the Upemba Depression famed for sacred kingship, ivory carving, and long-distance copper trade.",
    "Lozi": "The Barotse (Lozi) Kingdom of the upper Zambezi floodplain in western Zambia, known for seasonal royal migrations (Kuomboka) and canal engineering.",
    "Ayutthaya": "The Kingdom of Ayutthaya (1351–1767), a cosmopolitan Siamese empire whose river-island capital became one of early modern Asia's wealthiest trading cities.",
    "Kalinga": "An influential ancient coastal kingdom of eastern India (modern Odisha), famous for its maritime trade and for the 261 BC war that transformed Emperor Ashoka.",
    "Saba": "The ancient South Arabian Kingdom of Sheba (Saba) in modern Yemen, celebrated for the monumental Marib Dam and frankincense caravan trade.",
    "Moche": "A brilliant pre-Inca civilization (c. 100–700 AD) along Peru's arid north coast, renowned for portrait ceramics, goldwork, and vast adobe pyramids.",
    "Chavin": "The Chavín horizon (c. 900–200 BC) of the Peruvian highlands, an early pan-Andean ceremonial and artistic center at Chavín de Huántar.",
    "Avars": "The Pannonian Avar Khaganate (567–822 AD), a Eurasian steppe empire centered on the Carpathian Basin that rivaled Byzantium and the Franks.",
    "Asante": "The Ashanti Empire (1670–1902) of modern Ghana, a gold-rich West African forest kingdom unified around the sacred Golden Stool at Kumasi.",
    "Kanem": "The Kanem–Bornu Empire (c. 700–1900), a long-lived Lake Chad superpower controlling central trans-Saharan trade routes.",
    "Songhai": "West Africa's largest pre-colonial empire (c. 1464–1591), centered at Gao and Timbuktu with standing river fleets and Islamic universities.",
    "Oyo": "The Oyo Empire (c. 1300–1896), a powerful Yoruba cavalry state in modern southwestern Nigeria and Benin.",
    "Wadai": "The Wadai Empire (1635–1912), a Sahelian sultanate in eastern Chad that commanded eastern trans-Saharan caravan routes.",
    "Kush": "The ancient Nubian Kingdom of Kush (c. 1070 BC – 350 AD) along the upper Nile, whose pharaohs once ruled all of Egypt as the 25th Dynasty.",
    "Chauhans": "The Chahamana (Chauhan) Rajput dynasty (6th–12th centuries) of northern India, ruling Ajmer and Delhi under celebrated figures like Prithviraj Chauhan.",
    "Oromo": "The largest Cushitic-speaking people of the Horn of Africa, organized historically around the democratic Gadaa age-grade governance system.",
    "Burmese": "The Bamar-led kingdoms of the Irrawaddy valley that shaped Myanmar's royal courts, literature, and Theravada Buddhist heritage.",
    "Emirate of Bin Shal'an": "The Rwala Bedouin leadership of the Sha'lan family in the Syrian Desert and northern Arabia, commanding major desert caravan and tribal alliances.",
}

def trim_sentences(text, max_chars=240):
    text = re.sub(r"\s+", " ", (text or "").strip())
    if not text:
        return ""
    # Split on sentence boundaries
    sents = re.split(r"(?<=[.!?])\s+", text)
    out = sents[0]
    if len(out) < 130 and len(sents) > 1 and len(out) + 1 + len(sents[1]) <= max_chars + 45:
        out = out + " " + sents[1]
    if len(out) > max_chars + 55:
        out = out[:max_chars].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return out

def fetch_wiki_search_fallback(name):
    """For disambiguations or variant names, ask Wikipedia search for the closest historical/geographic article."""
    # Handle colonial/occupation parentheticals like "Western Australia (UK)" or "Madagascar (France)"
    m = re.match(r"^(.+?)\s*\((UK|France|Spain|Portugal|Italy|Netherlands|USA|Soviet|British Raj|Belgium|Germany|Denmark)\)$", name)
    if m:
        place, power = m.group(1).strip(), m.group(2).strip()
        power_label = {"UK": "British", "USA": "United States", "France": "French", "Spain": "Spanish", "Portugal": "Portuguese", "Italy": "Italian", "Netherlands": "Dutch", "Belgium": "Belgian", "Germany": "German", "Denmark": "Danish", "Soviet": "Soviet", "British Raj": "British Raj"}.get(power, power)
        sub = fetch_wiki_batch([(place, place)])
        base = sub.get(place, "")
        if base:
            return trim_sentences(f"{place} under {power_label} administration. {base}", max_chars=245)
        return f"Historical territory of {place} under {power_label} colonial or military administration during this era."

    # Try Wikipedia search with historical context
    q = f'"{name}" empire OR kingdom OR dynasty OR tribe OR people OR country OR state'
    url = (
        "https://en.wikipedia.org/w/api.php?action=query&list=search&srlimit=3&format=json&srsearch="
        + urllib.parse.quote(q)
    )
    req = urllib.request.Request(url, headers={"User-Agent": "ChroniaAtlasBuilder/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        hits = (data.get("query") or {}).get("search") or []
        if not hits:
            return ""
        best_title = hits[0]["title"]
        res = fetch_wiki_batch([(name, best_title)])
        return res.get(name, "")
    except Exception:
        return ""
def fetch_wiki_batch(pairs):
    """Fetch up to 20 Wikipedia 2-sentence intro extracts in a single polite API call."""
    # pairs: list of (atlas_name, wiki_title)
    titles_param = "|".join(wk for _, wk in pairs)
    url = (
        "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&explaintext=1"
        "&exsentences=2&redirects=1&format=json&titles=" + urllib.parse.quote(titles_param)
    )
    req = urllib.request.Request(url, headers={"User-Agent": "ChroniaAtlasBuilder/1.0 (https://github.com/chronia-atlas)"})
    out = {}
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        q = data.get("query") or {}
        norm_map = {n["from"]: n["to"] for n in q.get("normalized", [])}
        redir_map = {r["from"]: r["to"] for r in q.get("redirects", [])}
        pages = q.get("pages") or {}
        title_to_ext = {}
        for p in pages.values():
            if "missing" in p: continue
            ext = p.get("extract") or ""
            if not ext or "may refer to:" in ext or "can refer to:" in ext: continue
            title_to_ext[p.get("title", "")] = trim_sentences(ext, max_chars=230)
        for nm, wk in pairs:
            t = norm_map.get(wk, wk)
            t = redir_map.get(t, t)
            ext = title_to_ext.get(t, "")
            if ext:
                out[nm] = ext
    except Exception:
        pass
    return out

def build():
    raw = json.loads(gzip.decompress(base64.b64decode(ATLAS_B64.read_text(encoding="utf-8"))))
    names = raw["names"]

    # Map Cliopatria Name -> Wikipedia title where available
    clio_wiki = {}
    if CLIO_ZIP.exists():
        with zipfile.ZipFile(CLIO_ZIP) as z:
            clio = json.loads(z.read(z.namelist()[0]).decode("utf-8"))
        for f in clio["features"]:
            p = f.get("properties") or {}
            nm = (p.get("Name") or "").strip()
            wk = (p.get("Wikipedia") or "").strip()
            if nm and wk and nm not in clio_wiki:
                clio_wiki[nm] = wk

    # Score every territory by prominence = era_count * log1p(max_area)
    stats = {}
    for era in raw["eras"]:
        for tup in era["e"]:
            nid, _, is_ns, _, _, _, area10, _ = tup
            nm = names[nid]
            st = stats.setdefault(nm, {"count": 0, "max_area": 0.0, "is_ns": is_ns})
            st["count"] += 1
            if area10 / 10.0 > st["max_area"]:
                st["max_area"] = area10 / 10.0

    ranked = sorted(
        stats.items(),
        key=lambda kv: (0 if kv[1]["is_ns"] == 0 else -1000) + kv[1]["count"] * math.log1p(kv[1]["max_area"] + 1.0),
        reverse=True
    )

    # Load existing wiki cache
    cache = json.loads(BIOS_CACHE.read_text(encoding="utf-8")) if BIOS_CACHE.exists() else {}

    # Seed with curated bios first
    final_bios = {}
    for k, v in stories_data.EMPIRE_BIOS.items():
        final_bios[k] = v["bio"]
    for k, v in CURATED_EXTRA.items():
        final_bios[k] = v

    # Batch-fetch Wikipedia summaries for ALL remaining territories (20 titles per polite request!)
    to_fetch = []
    for nm, _ in ranked:
        if nm in final_bios:
            continue
        if nm in cache and cache[nm]:
            final_bios[nm] = cache[nm]
            continue
        to_fetch.append((nm, clio_wiki.get(nm, nm)))

    batches = [to_fetch[i:i+20] for i in range(0, len(to_fetch), 20)]
    print(f"Curated/cached: {len(final_bios)} | Batch-fetching {len(to_fetch)} territories in {len(batches)} requests...")
    if batches:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
            for res in ex.map(fetch_wiki_batch, batches):
                for nm, ext in res.items():
                    cache[nm] = ext
                    final_bios[nm] = ext
        BIOS_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")

    # Second pass: resolve any remaining missing organized states via smart search / parenthetical fallback
    still_missing = [nm for nm, st in ranked if st["is_ns"] == 0 and nm not in final_bios]
    print(f"After batch pass: {len(final_bios)} bios | Resolving {len(still_missing)} remaining states via search fallback...")
    if still_missing:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
            futs = {ex.submit(fetch_wiki_search_fallback, nm): nm for nm in still_missing}
            for f in concurrent.futures.as_completed(futs):
                nm = futs[f]
                ext = f.result()
                if ext:
                    cache[nm] = ext
                    final_bios[nm] = ext
        BIOS_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")

    # Filter final_bios to only names present in our atlas (keeps payload tight!)
    name_set = set(names)
    packed_bios = {k: v for k, v in final_bios.items() if k in name_set and v}

    raw_bytes = json.dumps(packed_bios, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    gz_bytes = gzip.compress(raw_bytes, compresslevel=9)
    b64_str = base64.b64encode(gz_bytes).decode("ascii")
    (SCRATCH / "bios_data.b64").write_text(b64_str, encoding="utf-8")

    print(f"Packed offline bios: {len(packed_bios)} territories")
    print(f"Raw JSON: {len(raw_bytes):,} B ({len(raw_bytes)/1024:.1f} KB)")
    print(f"Gzipped:  {len(gz_bytes):,} B ({len(gz_bytes)/1024:.1f} KB)")
    print(f"Base64:   {len(b64_str):,} B ({len(b64_str)/1024:.1f} KB)")

if __name__ == "__main__":
    build()
