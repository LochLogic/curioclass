import os, json, gzip, base64, math, re, zipfile, urllib.request, concurrent.futures
from pathlib import Path

SCRATCH = Path(r"C:\Users\Cory\.gemini\antigravity\brain\6fbd6632-042c-48d5-b34e-bfe1abcf53d4\scratch")
CACHE = SCRATCH / "raw_geojson"
CACHE.mkdir(parents=True, exist_ok=True)
CLIOPATRIA_ZIP = SCRATCH / "cliopatria.geojson.zip"

# 53 Historical-Basemaps Global Milestones
HB_MILESTONES = [
    (-10000, "world_bc10000.geojson", "10000 BC", "End of the Ice Age"),
    (-8000,  "world_bc8000.geojson",  "8000 BC",  "Neolithic Agriculture"),
    (-5000,  "world_bc5000.geojson",  "5000 BC",  "Early River Villages"),
    (-4000,  "world_bc4000.geojson",  "4000 BC",  "First Cities Emerge"),
    (-3000,  "world_bc3000.geojson",  "3000 BC",  "Dawn of States"),
    (-2000,  "world_bc2000.geojson",  "2000 BC",  "Bronze Age Kingdoms"),
    (-1500,  "world_bc1500.geojson",  "1500 BC",  "New Kingdom & Hittites"),
    (-1000,  "world_bc1000.geojson",  "1000 BC",  "Iron Age Dawn"),
    (-700,   "world_bc700.geojson",   "700 BC",   "Assyrian Ascendancy"),
    (-500,   "world_bc500.geojson",   "500 BC",   "Achaemenid Persia"),
    (-400,   "world_bc400.geojson",   "400 BC",   "Classical Greece & Warring States"),
    (-323,   "world_bc323.geojson",   "323 BC",   "Alexander's Conquests"),
    (-300,   "world_bc300.geojson",   "300 BC",   "Hellenistic Kingdoms & Maurya"),
    (-200,   "world_bc200.geojson",   "200 BC",   "Han, Rome & Maurya"),
    (-100,   "world_bc100.geojson",   "100 BC",   "Silk Road Opens"),
    (-1,     "world_bc1.geojson",     "1 BC",     "Pax Romana & Han"),
    (100,    "world_100.geojson",     "100 AD",   "High Classical Empires"),
    (200,    "world_200.geojson",     "200 AD",   "Twilight of the Han"),
    (300,    "world_300.geojson",     "300 AD",   "Tetrarchy & Sasanians"),
    (400,    "world_400.geojson",     "400 AD",   "Roman Split & Gupta"),
    (500,    "world_500.geojson",     "500 AD",   "Post-Roman West"),
    (600,    "world_600.geojson",     "600 AD",   "Byzantium, Persia & Sui"),
    (700,    "world_700.geojson",     "700 AD",   "Umayyad & Tang Peak"),
    (800,    "world_800.geojson",     "800 AD",   "Charlemagne & Abbasids"),
    (900,    "world_900.geojson",     "900 AD",   "Medieval Fragments"),
    (1000,   "world_1000.geojson",    "1000 AD",  "Song, HRE & Fatimids"),
    (1100,   "world_1100.geojson",    "1100 AD",  "Seljuks & Crusades"),
    (1200,   "world_1200.geojson",    "1200 AD",  "Eve of the Mongols"),
    (1279,   "world_1279.geojson",    "1279 AD",  "Mongol Empire Peak"),
    (1300,   "world_1300.geojson",    "1300 AD",  "Khanates & Early Ottomans"),
    (1400,   "world_1400.geojson",    "1400 AD",  "Ming, Timurids & Mali"),
    (1492,   "world_1492.geojson",    "1492 AD",  "Eve of Global Contact"),
    (1500,   "world_1500.geojson",    "1500 AD",  "Age of Oceanic Voyages"),
    (1530,   "world_1530.geojson",    "1530 AD",  "Gunpowder & Oceanic Empires"),
    (1600,   "world_1600.geojson",    "1600 AD",  "Global Trade Networks"),
    (1650,   "world_1650.geojson",    "1650 AD",  "Westphalia & Qing Rise"),
    (1700,   "world_1700.geojson",    "1700 AD",  "Kangxi Qing & Peter the Great"),
    (1715,   "world_1715.geojson",    "1715 AD",  "Age of Absolutism"),
    (1783,   "world_1783.geojson",    "1783 AD",  "Age of Revolutions"),
    (1800,   "world_1800.geojson",    "1800 AD",  "Napoleonic Era Dawns"),
    (1815,   "world_1815.geojson",    "1815 AD",  "Congress of Vienna"),
    (1878,   "world_1878.geojson",    "1878 AD",  "Congress of Berlin"),
    (1880,   "world_1880.geojson",    "1880 AD",  "High Imperialism"),
    (1900,   "world_1900.geojson",    "1900 AD",  "Turn of the 20th Century"),
    (1914,   "world_1914.geojson",    "1914 AD",  "Eve of World War I"),
    (1920,   "world_1920.geojson",    "1920 AD",  "Fall of Four Empires"),
    (1930,   "world_1930.geojson",    "1930 AD",  "Interwar World"),
    (1938,   "world_1938.geojson",    "1938 AD",  "Eve of World War II"),
    (1945,   "world_1945.geojson",    "1945 AD",  "Dawn of the Cold War"),
    (1960,   "world_1960.geojson",    "1960 AD",  "Wave of Decolonization"),
    (1994,   "world_1994.geojson",    "1994 AD",  "Post-Cold War World"),
    (2000,   "world_2000.geojson",    "2000 AD",  "Turn of the Millennium"),
    (2010,   "world_2010.geojson",    "2010 AD",  "Contemporary Borders"),
]

# 33 Targeted Cliopatria Milestones: Celtic Europe, Chinese Dynasties, Americas, Medieval, Africa, Indian Ocean, Silk Road
CLIO_MILESTONES = [
    (-520, "520 BC",  "Darius I & the Achaemenid Royal Road"),
    (-260, "260 BC",  "Ashoka's Mauryan Zenith"),
    (-250, "250 BC",  "Celtic Europe & Warring States"),
    (-220, "220 BC",  "Qin Unification of China"),
    (-55,  "55 BC",   "Celtic Gaul & Britannia vs. Rome"),
    (225,  "225 AD",  "Three Kingdoms of China"),
    (260,  "260 AD",  "Shapur I & Sasanian Ascendancy"),
    (350,  "350 AD",  "Aksumite Empire & Late Antiquity"),
    (450,  "450 AD",  "Gupta Golden Age & Hunnic Horizon"),
    (550,  "550 AD",  "Classic Maya, Teotihuacan & Byzantium"),
    (650,  "650 AD",  "Celtic Isles, Early Tang & Rashidun"),
    (750,  "750 AD",  "High Tang Dynasty & Abbasid Dawn"),
    (850,  "850 AD",  "Post-Verdun Europe & Viking Age"),
    (1025, "1025 AD", "Chola Maritime Empire & Ghaznavids"),
    (1050, "1050 AD", "Ghana Empire & Seljuk Rise"),
    (1066, "1066 AD", "Norman Conquest & Northern Song"),
    (1127, "1127 AD", "Southern Song & Jurchen Jin Split"),
    (1180, "1180 AD", "Saladin, Angevin Europe & Angkor"),
    (1325, "1325 AD", "Mansa Musa's Mali Empire"),
    (1335, "1335 AD", "Delhi Sultanate Peak & Vijayanagara"),
    (1350, "1350 AD", "Hundred Years' War, Mali & Majapahit"),
    (1370, "1370 AD", "Ming Overthrows Mongol Yuan"),
    (1405, "1405 AD", "Timur's Empire at Peak"),
    (1450, "1450 AD", "Aztec & Inca Empires Rise"),
    (1520, "1520 AD", "Songhai, Safavids & Inca Peak"),
    (1550, "1550 AD", "Spanish Viceroyalties & Potosi Silver"),
    (1620, "1620 AD", "Colonial North America & Late Ming"),
    (1680, "1680 AD", "Mughal Zenith & Maratha Rise"),
    (1740, "1740 AD", "Nader Shah's Afsharid Persia"),
    (1750, "1750 AD", "New France, British Colonies & Qing Peak"),
    (1825, "1825 AD", "Independent Latin America"),
    (1885, "1885 AD", "Berlin Conference & Scramble for Africa"),
    (1947, "1947 AD", "Independence & Partition of India"),
]

BASE_URL = "https://raw.githubusercontent.com/aourednik/historical-basemaps/master/geojson/"
NE_BASE  = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"
NE_FILES = [
    ("ne_50m_land.geojson", NE_BASE + "ne_50m_land.geojson"),
    ("ne_110m_lakes.geojson", NE_BASE + "ne_110m_lakes.geojson"),
    ("ne_110m_rivers.geojson", NE_BASE + "ne_110m_rivers_lake_centerlines.geojson"),
]

NON_STATE_RE = re.compile(
    r"(hunter-gatherer|hunter gatherer|hunters|forager|pastoral|nomad|farmers|horticultur|culture$|cultures$|cultures\b|peoples$|tribes$|aboriginal|paleo-siberian|finno-ugric|subarctic|arctic marine|amazon hunter|savanna hunter|plain bison|desert hunter|band[s]?$|manioc|maïze|cereal|rice cultures|fisher|ficher|^khoisan$|^saami$|^sámi$|^dorset$|^thule$|^athabask|^siberians$|^tupis$|^tungus$|^inuit$|^bantu$|^semites$|^dravidians$|^austronesians$|^berbers$|^celts$|^samoyèdes$|^permians$|^anasazi$|^chukchi$|^cree$|^t'atsaot'ine$|^dënéndeh$|^beaker$|^afanasevo$|^andronovo$|^catacomb)",
    re.IGNORECASE
)

EXACT_NAME_FIXES = {
    "Byelarus": "Belarus",
    "Korea, Democratic People's Republic of": "North Korea",
    "Korea, Republic of": "South Korea",
    "Tanzania, United Republic of": "Tanzania",
    "Cyraneica (UK Lybia)": "Cyrenaica (British Libya)",
    "Fezzan (Frech Lybia)": "Fezzan (French Libya)",
    "Tripolitana (UK Lybia)": "Tripolitania (British Libya)",
    "Quazaq Khanate": "Kazakh Khanate",
    "Peshemegs": "Pechenegs",
    "Karkhanids": "Kara-Khanids",
    "Zhoa": "Zhou",
    "Cimerians": "Cimmerians",
    "Luisiana": "Louisiana",
    "Satavahanihara": "Satavahana Empire",
    "Tufan Empire": "Tibetan Empire",
    "Bokhara Khanate": "Khanate of Bukhara",
    "Bukara Khanate": "Khanate of Bukhara",
    "Chinese warlords": "Chinese Warlords",
    "central Asian khanates": "Central Asian Khanates",
    "French Indo-China": "French Indochina",
    "Union of Soviet Socialist Republics": "USSR",
    "Republic of Turkey": "Turkey",
    "Socialist Federal Republic of Yugoslavia": "Yugoslavia",
    "United Kingdom of Netherlands": "United Kingdom of the Netherlands",
    "Tibeto-Burmanese": "Tibeto-Burman Peoples",
    "Western Gokturk Khaganate": "Western Göktürk Khaganate",
    "Rustamid dynasty": "Rustamid Dynasty",
    "minor Hindu kingdoms": "Minor Hindu Kingdoms",
    "minor Hindu and Buddhist states": "Hindu & Buddhist Kingdoms",
    "minor Hindu and Buddhist kingdoms": "Hindu & Buddhist Kingdoms",
    "minor states": "Regional States",
    "minor states under Indian influence": "Indianized Kingdoms",
    "state societies and Aramaean kingdoms": "Aramaean & Levantine Kingdoms",
    "city-states": "Early City-States",
    "Libya (IT)": "Italian Libya",
    "Algeria (FR)": "French Algeria",
    "Algeria (France)": "French Algeria",
    "Senegal (FR)": "French Senegal",
    "Angola (Portugal)": "Portuguese Angola",
    "Congo (France)": "French Congo",
    "Eritrea (Italy)": "Italian Eritrea",
    "Ethiopia (Italy)": "Italian East Africa",
    "Syria (France)": "French Syria",
    "Sakhalin (RU)": "Russian Sakhalin",
    "Zaire (Belgium)": "Belgian Congo",
    "[Gáuigú (Kiowa)": "Kiowa",
    "Wabanaki (Dawnland Confederacy)": "Wabanaki Confederacy",
    "Wallmapu (Mapuche)": "Mapuche (Wallmapu)",
}

def normalize_territory_name(name, year, area=0.0):
    name = name.strip()
    if name in EXACT_NAME_FIXES:
        name = EXACT_NAME_FIXES[name]

    # Clean unreadable non-Latin script prefixes (e.g. Osage/Cherokee/Cree syllabics) by using the parenthetical English name
    if any(ord(ch) > 0x024F for ch in name) and "(" in name and name.endswith(")"):
        inner = name[name.rfind("(") + 1 : -1].strip()
        if inner and all(ord(ch) < 0x0250 for ch in inner):
            name = inner.split(",")[0].strip()

    # Era-aware globally appropriate historical names
    if name == "White Russia":
        # In 1930 geojson the entire USSR polygon (area ~3175) was mislabeled "White Russia"; in 1920 it is Belarus (area ~18)
        return "USSR" if (year >= 1925 or area > 200) else "Belarus"
    if name == "Zaire":
        if year <= 1947: return "Belgian Congo"
        if year == 1960: return "Congo-Léopoldville"
        if year >= 2000: return "DR Congo"
        return "Zaire" # 1971-1997 (e.g. 1994)
    if name == "Congo" and year >= 1994:
        return "Republic of the Congo"
    if name == "Burma" and year >= 1990:
        return "Myanmar"
    if name == "Zimbabwe" and year <= 1979:
        return "Southern Rhodesia"
    if name == "Ivory Coast" and year >= 1986:
        return "Côte d'Ivoire"
    if name == "Iran" and year <= 1934:
        return "Persia"
    if name == "Siam" and year >= 1940:
        return "Thailand"
    if name == "Ceylon" and year >= 1972:
        return "Sri Lanka"

    return name

def download_file(url, dest):
    if dest.exists() and dest.stat().st_size > 100:
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": "ChroniaReimaginedBuilder/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    dest.write_bytes(data)
    return dest

def fetch_all():
    tasks = [(u, CACHE / fn) for fn, u in NE_FILES]
    for _, fname, _, _ in HB_MILESTONES:
        tasks.append((BASE_URL + fname, CACHE / fname))
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        futs = [ex.submit(download_file, u, d) for u, d in tasks]
        for f in concurrent.futures.as_completed(futs):
            f.result()
    print(f"Downloaded/cached {len(tasks)} GeoJSON files.")

def dp_simplify(pts, eps):
    if len(pts) <= 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = True
    keep[-1] = True
    stack = [(0, len(pts) - 1)]
    eps2 = eps * eps
    while stack:
        s, e = stack.pop()
        if e <= s + 1:
            continue
        x1, y1 = pts[s]
        x2, y2 = pts[e]
        dx = x2 - x1
        dy = y2 - y1
        len2 = dx * dx + dy * dy
        max_d2 = -1.0
        idx = -1
        for i in range(s + 1, e):
            px, py = pts[i]
            if len2 == 0.0:
                d2 = (px - x1) ** 2 + (py - y1) ** 2
            else:
                t = ((px - x1) * dx + (py - y1) * dy) / len2
                if t < 0.0: t = 0.0
                elif t > 1.0: t = 1.0
                cx = x1 + t * dx
                cy = y1 + t * dy
                d2 = (px - cx) ** 2 + (py - cy) ** 2
            if d2 > max_d2:
                max_d2 = d2
                idx = i
        if max_d2 > eps2 and idx != -1:
            keep[idx] = True
            stack.append((s, idx))
            stack.append((idx, e))
    return [pts[i] for i in range(len(pts)) if keep[i]]

def ring_area_deg2(ring):
    a = 0.0
    n = len(ring)
    for i in range(n - 1):
        a += ring[i][0] * ring[i+1][1] - ring[i+1][0] * ring[i][1]
    return abs(a) * 0.5

def encode_pts(pts, scale=20.0, eps=0.15, is_ring=True):
    if is_ring:
        if len(pts) < 4: return None
        open_pts = pts[:-1] if pts[0] == pts[-1] else pts
        if len(open_pts) < 3: return None
    else:
        if len(pts) < 2: return None
        open_pts = pts
    simp = dp_simplify(open_pts, eps)
    if is_ring and len(simp) < 3: return None
    if not is_ring and len(simp) < 2: return None
    out = []
    px = int(round(max(-180.0, min(180.0, simp[0][0])) * scale))
    py = int(round(max(-84.0, min(84.0, simp[0][1])) * scale))
    out.append(px)
    out.append(py)
    for pt in simp[1:]:
        qx = int(round(max(-180.0, min(180.0, pt[0])) * scale))
        qy = int(round(max(-84.0, min(84.0, pt[1])) * scale))
        if qx == px and qy == py:
            continue
        out.append(qx - px)
        out.append(qy - py)
        px, py = qx, qy
    min_len = 6 if is_ring else 4
    return out if len(out) >= min_len else None

def centroid_of_ring(ring):
    a = 0.0; cx = 0.0; cy = 0.0
    n = len(ring)
    for i in range(n - 1):
        x0, y0 = ring[i]
        x1, y1 = ring[i+1]
        cross = x0 * y1 - x1 * y0
        a += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    if abs(a) < 1e-6:
        xs = [p[0] for p in ring]
        ys = [p[1] for p in ring]
        return (sum(xs)/len(xs), sum(ys)/len(ys))
    a *= 0.5
    return (cx / (6.0 * a), cy / (6.0 * a))

def build():
    fetch_all()
    SCALE = 20.0

    # 1. Natural Earth 50m Land, 110m Lakes & Rivers
    ne_land = json.loads((CACHE / "ne_50m_land.geojson").read_text(encoding="utf-8"))
    land_rings = []
    for feat in ne_land["features"]:
        geom = feat["geometry"]
        if not geom: continue
        polys = [geom["coordinates"]] if geom["type"] == "Polygon" else geom["coordinates"]
        for poly in polys:
            outer = poly[0]
            if max(p[1] for p in outer) < -60.0 or ring_area_deg2(outer) < 0.08: continue
            enc = encode_pts(outer, scale=SCALE, eps=0.14, is_ring=True)
            if enc: land_rings.append(enc)

    ne_lakes = json.loads((CACHE / "ne_110m_lakes.geojson").read_text(encoding="utf-8"))
    lake_rings = []
    for feat in ne_lakes["features"]:
        geom = feat["geometry"]
        if not geom: continue
        polys = [geom["coordinates"]] if geom["type"] == "Polygon" else geom["coordinates"]
        for poly in polys:
            outer = poly[0]
            if ring_area_deg2(outer) < 0.12: continue
            enc = encode_pts(outer, scale=SCALE, eps=0.12, is_ring=True)
            if enc: lake_rings.append(enc)

    ne_riv = json.loads((CACHE / "ne_110m_rivers.geojson").read_text(encoding="utf-8"))
    river_lines = []
    for feat in ne_riv["features"]:
        geom = feat["geometry"]
        if not geom: continue
        lines = [geom["coordinates"]] if geom["type"] == "LineString" else (geom["coordinates"] if geom["type"] == "MultiLineString" else [])
        for line in lines:
            if len(line) < 3: continue
            enc = encode_pts(line, scale=SCALE, eps=0.18, is_ring=False)
            if enc: river_lines.append(enc)

    name_to_id = {}
    names_list = []
    def get_name_id(name):
        if name not in name_to_id:
            name_to_id[name] = len(names_list)
            names_list.append(name)
        return name_to_id[name]

    def pack_entities_dict(entities, year, max_states=110):
        # Apply era-aware name normalization & merge any newly unified names (e.g. USSR)
        merged = {}
        for raw_name, ev in entities.items():
            clean_name = normalize_territory_name(raw_name, year, ev["area"])
            clean_subj = normalize_territory_name(ev["subj"], year, 0.0) if ev["subj"] else ""
            if clean_subj == clean_name:
                clean_subj = ""
            if clean_name not in merged:
                merged[clean_name] = {
                    "rings": list(ev["rings"]), "area": ev["area"],
                    "best_ring": ev["best_ring"], "best_area": ev["best_area"],
                    "bp": ev["bp"], "ns": ev["ns"], "subj": clean_subj
                }
            else:
                m = merged[clean_name]
                m["rings"].extend(ev["rings"])
                m["area"] += ev["area"]
                if ev["best_area"] > m["best_area"]:
                    m["best_area"] = ev["best_area"]
                    m["best_ring"] = ev["best_ring"]

        states = sorted(
            [(k, v) for k, v in merged.items() if v["rings"] and v["ns"] == 0 and v["area"] >= 0.25],
            key=lambda kv: kv[1]["area"], reverse=True
        )[:max_states]
        peoples = sorted(
            [(k, v) for k, v in merged.items() if v["rings"] and v["ns"] == 1 and v["area"] >= 4.0],
            key=lambda kv: kv[1]["area"], reverse=True
        )[:22]
        packed = []
        for ename, ev in states + peoples:
            nid = get_name_id(ename)
            sid = get_name_id(ev["subj"]) if ev["subj"] else -1
            cx, cy = centroid_of_ring(ev["best_ring"])
            packed.append([
                nid, sid, ev["ns"], ev["bp"],
                int(round(cx * 10)), int(round(cy * 10)),
                int(round(ev["area"] * 10)),
                ev["rings"]
            ])
        return packed

    eras_data = []

    # 2. Pack 53 Historical-Basemaps Milestones
    for year, fname, label, subtitle in HB_MILESTONES:
        raw = json.loads((CACHE / fname).read_text(encoding="utf-8"))
        entities = {}
        for feat in raw.get("features", []):
            props = feat.get("properties") or {}
            name = (props.get("NAME") or "").strip()
            subj = (props.get("SUBJECTO") or "").strip()
            part = (props.get("PART_OF") or "").strip()
            if not name: name = subj or part
            if not name or name.isdigit() or len(name) < 2 or name.lower() in ("unclaimed", "none", "null", "unknown", "antarctica"):
                continue
            is_non_state = 1 if NON_STATE_RE.search(name) else 0
            bp = props.get("BORDERPRECISION")
            try: bp = int(bp) if bp is not None else 2
            except Exception: bp = 2
            geom = feat.get("geometry")
            if not geom: continue
            polys = [geom["coordinates"]] if geom["type"] == "Polygon" else (geom["coordinates"] if geom["type"] == "MultiPolygon" else [])
            if name not in entities:
                entities[name] = {"rings": [], "area": 0.0, "best_ring": None, "best_area": 0.0, "bp": bp, "ns": is_non_state, "subj": subj if subj and subj != name else ""}
            ent = entities[name]
            for poly in polys:
                outer = poly[0]
                if max(p[1] for p in outer) < -60.0: continue
                area = ring_area_deg2(outer)
                if area < (0.20 if not is_non_state else 2.5): continue
                enc = encode_pts(outer, scale=SCALE, eps=(0.16 if not is_non_state else 0.45), is_ring=True)
                if enc:
                    ent["rings"].append(enc)
                    ent["area"] += area
                    if area > ent["best_area"]:
                        ent["best_area"] = area
                        ent["best_ring"] = outer
        eras_data.append({"y": year, "l": label, "s": subtitle, "e": pack_entities_dict(entities, year)})

    # 3. Pack 18 Targeted Cliopatria Milestones
    with zipfile.ZipFile(CLIOPATRIA_ZIP) as z:
        clio_raw = json.loads(z.read(z.namelist()[0]).decode("utf-8"))
    clio_feats = clio_raw["features"]
    print(f"Loaded {len(clio_feats)} Cliopatria features for 18 targeted milestones.")

    for year, label, subtitle in CLIO_MILESTONES:
        entities = {}
        for feat in clio_feats:
            props = feat.get("properties") or {}
            if props.get("Type") != "POLITY": continue
            fy = props.get("FromYear"); ty = props.get("ToYear")
            if fy is None or ty is None or not (fy <= year <= ty): continue
            name = (props.get("Name") or "").strip()
            # Skip parenthetical supra-polities like "(Spanish Empire)" to avoid overlap with specific realms
            if not name or (name.startswith("(") and name.endswith(")")):
                continue
            subj = (props.get("MemberOf") or "").strip()
            if subj.startswith("(") and subj.endswith(")"):
                subj = subj[1:-1].strip()
            geom = feat.get("geometry")
            if not geom: continue
            polys = [geom["coordinates"]] if geom["type"] == "Polygon" else (geom["coordinates"] if geom["type"] == "MultiPolygon" else [])
            if name not in entities:
                entities[name] = {"rings": [], "area": 0.0, "best_ring": None, "best_area": 0.0, "bp": 2, "ns": 0, "subj": subj if subj and subj != name else ""}
            ent = entities[name]
            for poly in polys:
                outer = poly[0]
                if not outer or max(p[1] for p in outer) < -60.0: continue
                area = ring_area_deg2(outer)
                if area < 0.18: continue
                enc = encode_pts(outer, scale=SCALE, eps=0.16, is_ring=True)
                if enc:
                    ent["rings"].append(enc)
                    ent["area"] += area
                    if area > ent["best_area"]:
                        ent["best_area"] = area
                        ent["best_ring"] = outer
        eras_data.append({"y": year, "l": label, "s": subtitle, "e": pack_entities_dict(entities, year, max_states=120)})

    # Sort all 71 milestones chronologically
    eras_data.sort(key=lambda e: e["y"])

    payload = {
        "scale": int(SCALE),
        "land": land_rings,
        "lakes": lake_rings,
        "rivers": river_lines,
        "names": names_list,
        "eras": eras_data
    }

    raw_json = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    gz_bytes = gzip.compress(raw_json, compresslevel=9)
    b64_str = base64.b64encode(gz_bytes).decode("ascii")
    (SCRATCH / "atlas_data.b64").write_text(b64_str, encoding="utf-8")

    summary = []
    for era in eras_data:
        org = [names_list[e[0]] for e in era["e"] if e[2] == 0]
        summary.append(f"{era['l']} ({era['s']}): {len(org)} states | Top: {', '.join(org[:10])}")
    (SCRATCH / "era_summary.txt").write_text("\n".join(summary), encoding="utf-8")

    print(f"Total Eras packed: {len(eras_data)} | Unique names: {len(names_list)}")
    print(f"Raw JSON:  {len(raw_json):,} B ({len(raw_json)/1024:.1f} KB)")
    print(f"Gzipped:   {len(gz_bytes):,} B ({len(gz_bytes)/1024:.1f} KB)")
    print(f"Base64:    {len(b64_str):,} B ({len(b64_str)/1024:.1f} KB)")

if __name__ == "__main__":
    build()
