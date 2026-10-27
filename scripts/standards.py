"""Registries of valid codes for each national framework Curio Class aligns to.

There are no federal K-12 content standards in the US (federal law bars a national
curriculum), so the top level is the national consensus framework for each subject.
validate(code) returns the framework name, or None if the code is not a real code.
"""
import re
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / 'data' / 'standards'
G = ['K', '1', '2', '3', '4', '5', '6', '7', '8']

# --- Common Core Math: cluster letters per grade and domain (thecorestandards.org)
CCSS_MATH_K8 = {
    'K': {'CC': 'ABC', 'OA': 'A', 'NBT': 'A', 'MD': 'AB', 'G': 'AB'},
    '1': {'OA': 'ABCD', 'NBT': 'ABC', 'MD': 'ABC', 'G': 'A'},
    '2': {'OA': 'ABC', 'NBT': 'AB', 'MD': 'ABCD', 'G': 'A'},
    '3': {'OA': 'ABCD', 'NBT': 'A', 'NF': 'A', 'MD': 'ABCD', 'G': 'A'},
    '4': {'OA': 'ABC', 'NBT': 'AB', 'NF': 'ABC', 'MD': 'ABC', 'G': 'A'},
    '5': {'OA': 'AB', 'NBT': 'AB', 'NF': 'AB', 'MD': 'ABC', 'G': 'AB'},
    '6': {'RP': 'A', 'NS': 'ABC', 'EE': 'ABC', 'G': 'A', 'SP': 'AB'},
    '7': {'RP': 'A', 'NS': 'A', 'EE': 'AB', 'G': 'AB', 'SP': 'ABC'},
    '8': {'NS': 'A', 'EE': 'ABC', 'F': 'AB', 'G': 'ABC', 'SP': 'A'},
}
CCSS_MATH_HS = {
    'N-RN': 'AB', 'N-Q': 'A', 'N-CN': 'ABC', 'N-VM': 'ABC',
    'A-SSE': 'AB', 'A-APR': 'ABCD', 'A-CED': 'A', 'A-REI': 'ABCD',
    'F-IF': 'ABC', 'F-BF': 'AB', 'F-LE': 'AB', 'F-TF': 'ABC',
    'G-CO': 'ABCD', 'G-SRT': 'ABCD', 'G-C': 'AB', 'G-GPE': 'AB', 'G-GMD': 'AB', 'G-MG': 'A',
    'S-ID': 'ABC', 'S-IC': 'AB', 'S-CP': 'AB', 'S-MD': 'AB',
}


def ccss_math(code):
    m = re.fullmatch(r'([K1-8])\.([A-Z]+)(?:\.([A-D])(?:\.\d{1,2})?)?', code)
    if m:
        g, d, c = m.groups()
        return d in CCSS_MATH_K8[g] and (c is None or c in CCSS_MATH_K8[g][d])
    m = re.fullmatch(r'([NAFGS]-[A-Z]{1,3})(?:\.([A-D])(?:\.\d{1,2})?)?', code)
    if m:
        d, c = m.groups()
        return d in CCSS_MATH_HS and (c is None or c in CCSS_MATH_HS[d])
    return False


# --- Common Core ELA: strand.grade.number, checked against the official list
ELA_IDS = set(l.strip() for l in (DATA / 'ccss-ela-standards.txt').read_text(encoding='utf-8').splitlines()
              if l.strip() and not l.startswith('#'))


def ccss_ela(code):
    """A grade-level standard on the official list, optionally with its sub-letter (L.3.1a)."""
    m = re.fullmatch(r'((?:RL|RI|RF|W|SL|L)\.(?:K|[1-8]|9-10|11-12)\.\d{1,2})[a-f]?', code)
    return bool(m) and m.group(1) in ELA_IDS


# --- NGSS performance expectations (nextgenscience.org): band-DCI -> highest number
NGSS = {
    'K-PS2': 2, 'K-PS3': 2, 'K-LS1': 1, 'K-ESS2': 2, 'K-ESS3': 3, 'K-2-ETS1': 3,
    '1-PS4': 4, '1-LS1': 2, '1-LS3': 1, '1-ESS1': 2,
    '2-PS1': 4, '2-LS2': 2, '2-LS4': 1, '2-ESS1': 1, '2-ESS2': 3,
    '3-PS2': 4, '3-LS1': 1, '3-LS2': 1, '3-LS3': 2, '3-LS4': 4, '3-ESS2': 2, '3-ESS3': 1, '3-5-ETS1': 3,
    '4-PS3': 4, '4-PS4': 3, '4-LS1': 2, '4-ESS1': 1, '4-ESS2': 2, '4-ESS3': 2,
    '5-PS1': 4, '5-PS2': 1, '5-PS3': 1, '5-LS1': 1, '5-LS2': 1, '5-ESS1': 2, '5-ESS2': 2, '5-ESS3': 1,
    'MS-PS1': 6, 'MS-PS2': 5, 'MS-PS3': 5, 'MS-PS4': 3, 'MS-LS1': 8, 'MS-LS2': 5, 'MS-LS3': 2,
    'MS-LS4': 6, 'MS-ESS1': 4, 'MS-ESS2': 6, 'MS-ESS3': 5, 'MS-ETS1': 4,
    'HS-PS1': 8, 'HS-PS2': 6, 'HS-PS3': 5, 'HS-PS4': 5, 'HS-LS1': 7, 'HS-LS2': 8, 'HS-LS3': 3,
    'HS-LS4': 6, 'HS-ESS1': 6, 'HS-ESS2': 7, 'HS-ESS3': 6, 'HS-ETS1': 4,
}


def ngss(code):
    m = re.fullmatch(r'(.+)-(\d)', code)
    return bool(m) and m.group(1) in NGSS and 1 <= int(m.group(2)) <= NGSS[m.group(1)]


# --- C3 Framework indicators, all four dimensions (socialstudies.org, rev 2017): the official list
C3_IDS = set(l.strip() for l in (DATA / 'c3-indicators.txt').read_text(encoding='utf-8').splitlines()
             if l.strip() and not l.startswith('#'))


def c3(code):
    return code in C3_IDS


# --- CSTA 2026 PK-12 CS Standards (csteachers.org, released July 2026)
CSTA = set((DATA / 'csta-2026-ids.txt').read_text().split())

# --- Frameworks without fine-grained codes: closed vocabularies
CLOSED = {
    'NCAS': re.compile(r'(VA|MU|TH|DA|MA):(Cr[123]|Pr[456]|Re[789]|Cn1[01])'),
    'NHES-2024': re.compile(r'NHES\.S[1-8]'),
    'SHAPE-PE-2024': re.compile(r'SHAPE\.S[1-4]'),
    'ACTFL': re.compile(r'ACTFL\.(Novice|Intermediate|Advanced) (Low|Mid|High)'),
    'World-Readiness': re.compile(r'WRS\.(Communication|Cultures|Connections|Comparisons|Communities)'),
    'NSPFE-2021': re.compile(r'NSPFE\.(Earning Income|Spending|Saving|Investing|Managing Credit|Managing Risk)'),
    'CASEL': re.compile(r'CASEL\.(Self-Awareness|Self-Management|Social Awareness|Relationship Skills|Responsible Decision-Making)'),
    'Career Clusters 2024': re.compile(r'CTE\.(Career Clusters|Career Ready Practices)'),
    'APA-HS-Psych': re.compile(r'APA\.(Scientific Inquiry|Biological|Development and Learning|Sociocultural|Cognition|Individual Variations|Mental and Physical Health)'),
    'WIDA-ELD-2020': re.compile(r'WIDA\.(ELD-[1-5]|Narrate|Inform|Explain|Argue)'),
    'AASL-2018': re.compile(r'AASL\.(Inquire|Include|Collaborate|Curate|Explore|Engage)'),
    'AP Precalculus':re.compile(r'AP-PRECALC\.U[1-4]'),
    'AP Statistics': re.compile(r'AP-STAT\.U[1-9]'),
    'AP Calculus': re.compile(r'AP-CALC\.U([1-9]|10)'),
}


def validate(code):
    if ccss_math(code):
        return 'CCSS-Math'
    if ccss_ela(code):
        return 'CCSS-ELA'
    if ngss(code):
        return 'NGSS'
    if c3(code):
        return 'C3'
    if code in CSTA:
        return 'CSTA-2026'
    for name, rx in CLOSED.items():
        if rx.fullmatch(code):
            return name
    return None
