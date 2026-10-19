#!/usr/bin/env python3
"""Enrich Volume III (.rst folios) with normalized 4-level headings and :term:, :cite:, and :person: roles."""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional, Tuple

_REPO_ROOT = Path(__file__).resolve().parents[1]
_LOCAL_SRC = _REPO_ROOT / "src"
_PROJECTS_ROOT = _REPO_ROOT.parents[1]
_PUBLISH_SRC = _PROJECTS_ROOT / "photon-platform" / "publish" / "src"

for _p in (_PUBLISH_SRC, _LOCAL_SRC):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

for _ws_venv in (
    _REPO_ROOT / ".venv",
    _PROJECTS_ROOT / "photon-platform" / "publish" / ".venv",
    _PROJECTS_ROOT / "geometor" / "elements" / ".venv",
    _PROJECTS_ROOT / "geometor" / "hoenen" / ".venv",
    _PROJECTS_ROOT / "geometor" / "pacioli" / ".venv",
    _PROJECTS_ROOT / "geometor" / "model" / ".venv",
):
    for _sp in sorted(_ws_venv.glob("lib/python*/site-packages")):
        if _sp.exists() and str(_sp) not in sys.path:
            sys.path.append(str(_sp))

from photon_platform.publish.rst_renderer import render_rst_html

_ADORNMENT_RE = re.compile(r"^([=!~^\"'`#*+\-_])\1{3,}\s*$")


def _column_width(text: str) -> int:
    width = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            width += 2
        else:
            width += 1
    return max(width, len(text), 4)


# ---------------------------------------------------------------------------
# 1. Fixed 4-Level Heading Hierarchy (=, -, ~, ^) for Volume III
# ---------------------------------------------------------------------------

_LEVEL_1_EXACT = {
    "THE THIRTEEN BOOKS OF EUCLID'S ELEMENTS",
    "THE THIRTEEN BOOKS OF EUCLID’S ELEMENTS",
    "CONTENTS OF VOLUME III.",
    "BOOK X.",
    "BOOK X. PROPOSITIONS.",
    "BOOK XI.",
    "BOOK XI. PROPOSITIONS.",
    "BOOK XII.",
    "BOOK XII. PROPOSITIONS.",
    "BOOK XIII.",
    "BOOK XIII. PROPOSITIONS.",
    "APPENDIX.",
    "GENERAL INDEX OF GREEK WORDS AND FORMS.",
    "GENERAL INDEX.",
}

_LEVEL_2_EXACT = {
    "VOLUME III",
    "VOLUME III.",
    "INTRODUCTORY NOTE.",
    "HISTORICAL NOTE.",
    "DEFINITIONS.",
    "DEFINITIONS II.",
    "DEFINITIONS III.",
    "PROPOSITIONS.",
    "ANCIENT EXTENSIONS OF THE THEORY OF BOOK X.",
    "I. THE CONTENTS OF THE SO-CALLED BOOK XIV. BY HYPSICLES.",
    'II. NOTE ON THE SO-CALLED "BOOK XV."',
}

_LEVEL_2_PATTERNS = [
    re.compile(r"^\[?DEFINITIONS?\s+\d+(?:\s*,\s*\d+)*\.$", re.I),
    re.compile(r"^\[?PROPOSITIONS?\s+\d+(?:\s*,\s*\d+)*\.$", re.I),
]

_LEVEL_4_PATTERNS = [
    re.compile(r"^Pappus[’']\s+(?:solution|method)", re.I),
    re.compile(
        r"^(?:K\.C\.B\.,\s+K\.C\.V\.O\.,\s+F\.R\.S\.,|SC\.D\.\s+CAMB\.,\s+HON\.\s+D\.SC\.\s+OXFORD|"
        r"HONORARY\s+FELLOW.*|CAMBRIDGE|AT\s+THE\s+UNIVERSITY\s+PRESS|1926)$"
    ),
]


def classify_heading_char(title: str, rel_path: str) -> str:
    """Return the canonical heading adornment character (=, -, ~, ^) for a given title."""
    norm = title.strip().replace("’", "'").replace("“", '"').replace("”", '"')
    if norm in _LEVEL_1_EXACT or title.strip() in _LEVEL_1_EXACT:
        return "="
    if norm in _LEVEL_2_EXACT or title.strip() in _LEVEL_2_EXACT:
        return "-"
    for pat in _LEVEL_2_PATTERNS:
        if pat.match(norm):
            return "-"
    for pat in _LEVEL_4_PATTERNS:
        if pat.match(norm) or pat.match(title.strip()):
            return "^"
    return "~"


# ---------------------------------------------------------------------------
# 2. Glossary & Defined Terms (:term:)
# ---------------------------------------------------------------------------

def _slugify_term(text: str) -> str:
    s = re.sub(r"[\*\"“”‘’'`]", "", text.strip().lower())
    s = re.sub(r"[^a-z0-9\u0370-\u03ff\u1f00-\u1fff]+", "-", s)
    return s.strip("-")


_DEFINITION_TERM_SLUGS: Dict[str, str] = {
    # Book X Definitions I (0014.rst)
    "commensurable": "commensurable",
    "incommensurable": "incommensurable",
    "commensurable in square": "commensurable-in-square",
    "incommensurable in square": "incommensurable-in-square",
    "rational": "rational",
    "irrational": "irrational",
    # Book X Proposition-level Definitions
    "medial": "medial",
    "binomial": "binomial",
    "first bimedial straight line": "first-bimedial-straight-line",
    "first bimedial": "first-bimedial",
    "second bimedial straight line": "second-bimedial-straight-line",
    "second bimedial": "second-bimedial",
    "major": "major",
    "side of a rational plus a medial area": "side-of-a-rational-plus-a-medial-area",
    "side of the sum of two medial areas": "side-of-the-sum-of-two-medial-areas",
    "apotome": "apotome",
    "first apotome of a medial straight line": "first-apotome-of-a-medial-straight-line",
    "second apotome of a medial straight line": "second-apotome-of-a-medial-straight-line",
    "minor": "minor",
    "that which produces with a rational area a medial whole": "side-of-a-medial-minus-a-rational-area",
    "that which produces with a medial area a medial whole": "side-of-a-medial-minus-a-medial-area",
    # Book X Definitions II (0105.rst, 0106.rst)
    "first binomial straight line": "first-binomial-straight-line",
    "second binomial": "second-binomial",
    "third binomial": "third-binomial",
    "fourth binomial": "fourth-binomial",
    "fifth binomial": "fifth-binomial",
    "sixth binomial": "sixth-binomial",
    # Book X Definitions III (0181.rst)
    "first apotome": "first-apotome",
    "second apotome": "second-apotome",
    "third apotome": "third-apotome",
    "fourth apotome": "fourth-apotome",
    "fifth": "fifth-apotome",
    "sixth": "sixth-apotome",
    # Book XI Definitions 1-28 (0264.rst-0266.rst)
    "solid": "solid",
    "surface": "surface",
    "at right angles to a plane": "right-angles-to-plane",
    "plane is at right angles to a plane": "plane-at-right-angles-to-plane",
    "inclination of a straight line to a plane": "inclination-of-line-to-plane",
    "inclination of a plane to a plane": "inclination-of-plane-to-plane",
    "similarly inclined": "similarly-inclined-planes",
    "parallel planes": "parallel-planes",
    "similar solid figures": "similar-solid-figures",
    "equal and similar solid figures": "equal-and-similar-solid-figures",
    "solid angle": "solid-angle",
    "pyramid": "pyramid",
    "prism": "prism",
    "sphere": "sphere",
    "axis of the sphere": "axis-of-sphere",
    "centre of the sphere": "centre-of-sphere",
    "diameter of the sphere": "diameter-of-sphere",
    "cone": "cone",
    "right-angled": "right-angled-cone",
    "obtuse-angled": "obtuse-angled-cone",
    "acute-angled": "acute-angled-cone",
    "axis of the cone": "axis-of-cone",
    "base": "base-of-cone",
    "cylinder": "cylinder",
    "axis of the cylinder": "axis-of-cylinder",
    "bases": "bases-of-cylinder",
    "similar cones and cylinders": "similar-cones-and-cylinders",
    "cube": "cube",
    "octahedron": "octahedron",
    "icosahedron": "icosahedron",
    "dodecahedron": "dodecahedron",
}

# Greek & Latin technical terms -> canonical slug
_GREEK_LATIN_TERMS: List[Tuple[str, str]] = [
    # Multi-word Greek technical phrases in Volume III
    ("ἡ μετὰ ῥητοῦ μέσον τὸ ὅλον ποιοῦσα", "side-of-a-medial-minus-a-rational-area"),
    ("ἡ μετὰ μέσου μέσον τὸ ὅλον ποιοῦσα", "side-of-a-medial-minus-a-medial-area"),
    ("ῥητὸν καὶ μέσον δυναμένη", "side-of-a-rational-plus-a-medial-area"),
    ("ἡ δύο μέσα δυναμένη", "side-of-the-sum-of-two-medial-areas"),
    ("μέσης ἀποτομὴ πρώτη", "first-apotome-of-a-medial-straight-line"),
    ("μέσης ἀποτομὴ δευτέρα", "second-apotome-of-a-medial-straight-line"),
    ("ἐκ δύο μέσων πρώτη", "first-bimedial-straight-line"),
    ("ἐκ δύο μέσων δευτέρα", "second-bimedial-straight-line"),
    ("ἡ ἐκ δύο ὀνομάτων", "binomial"),
    ("ἄρρητος διάμετρος τῆς πεμπάδος", "irrational-diameter-of-five"),
    ("τὸ ὑποκείμενον ἐπίπεδον", "plane-of-reference"),
    ("συνημμένη ἀναλογία", "continuous-proportion"),
    ("ἑξῆς ἀνάλογον", "in-continued-proportion"),
    ("ἀναγράφειν ἀπό", "anagraphein-apo"),
    ("κοινὴ τομή", "common-section"),
    ("ἴσον ἰσάκις", "equal-multiplied-by-equal"),
    # Single-word Greek technical terms in Volume III (from Greek Index 0525-0530)
    ("προσαρμόζουσα", "annex"),
    ("παραλληλεπίπεδος", "parallelepiped"),
    ("παραβάλλειν", "paraballein"),
    ("δωδεκάεδρον", "dodecahedron"),
    ("εἰκοσάεδρον", "icosahedron"),
    ("ὀκτάεδρον", "octahedron"),
    ("ἑτερομήκης", "oblong"),
    ("προμήκης", "prolate"),
    ("διορισμός", "diorismos"),
    ("διαστάσεις", "dimensions"),
    ("διαστατόν", "extended"),
    ("ἀσύμμετρος", "incommensurable"),
    ("σύμμετρος", "commensurable"),
    ("ἀσύνθετος", "incomposite"),
    ("σύνθετος", "composite"),
    ("πηλικότης", "size"),
    ("ἀμβλυγώνιος", "obtuse-angled"),
    ("ὀξυγώνιος", "acute-angled"),
    ("ὀρθογώνιος", "right-angled"),
    ("εὐθύγραμμος", "rectilineal"),
    ("ἀναλογία", "proportion"),
    ("ἀνάλογον", "proportional"),
    ("ἀπαγωγή", "apagoge"),
    ("ἀποτομή", "apotome"),
    ("δυνάμεις", "dynameis"),
    ("δύνασθαι", "dynasthai"),
    ("δυναμένη", "dynamene"),
    ("δύναμις", "dynamis"),
    ("δυνάμει", "in-square"),
    ("διῃρημένη", "discrete-proportion"),
    ("συνθέντι", "componendo"),
    ("διελόντι", "separando"),
    ("ἀναστρέψαντι", "convertendo"),
    ("ἐναλλάξ", "alternando"),
    ("ἀνάπαλιν", "invertendo"),
    ("ἐπιφάνεια", "surface"),
    ("ἐπίπεδον", "plane"),
    ("κύλινδρος", "cylinder"),
    ("πυραμίς", "pyramid"),
    ("σφαῖρα", "sphere"),
    ("πρίσμα", "prism"),
    ("στερεόν", "solid"),
    ("κῶνος", "cone"),
    ("κύβος", "cube"),
    ("κέντρον", "centre"),
    ("διάμετρος", "diameter"),
    ("κάθετος", "perpendicular"),
    ("εὐθεῖα", "straight-line"),
    ("γωνία", "angle"),
    ("ἀριθμός", "number"),
    ("μονάς", "unit"),
    ("μῆκος", "length"),
    ("μήκει", "in-length"),
    ("πλάτος", "breadth"),
    ("βάθος", "depth"),
    ("ῥητός", "rational"),
    ("ἄλογος", "irrational"),
    ("ἄρρητος", "irrational"),
    ("μείζων", "major"),
    ("ἐλάσσων", "minor"),
    ("μαθήματα", "mathemata"),
    ("νεύσεις", "neuseis"),
    ("συνεχής", "continuous"),
    ("ἐφεξῆς", "successive"),
    ("ἐφόδιον", "method"),
    ("λόγος", "ratio"),
    ("ὅρος", "term"),
    ("κλίσις", "inclination"),
    ("ἄξων", "axis"),
    ("βάσις", "base"),
    # Latin & English italicized technical phrases in Volume III
    ("*reductio ad absurdum*", "reductio-ad-absurdum"),
    ("*per impossibile*", "per-impossibile"),
    ("*convertendo*", "convertendo"),
    ("*separando*", "separando"),
    ("*componendo*", "componendo"),
    ("*Componendo*", "componendo"),
    ("*alternando*", "alternando"),
    ("*ex aequali*", "ex-aequali"),
    ("*dividendo*", "dividendo"),
    ("*a fortiori*", "a-fortiori"),
    ("*ad infinitum*", "ad-infinitum"),
    ("*method of exhaustion*", "method-of-exhaustion"),
    ("*commensurable in square only*", "commensurable-in-square-only"),
    ("*commensurable in length*", "commensurable-in-length"),
    ("*incommensurable in length*", "incommensurable-in-length"),
    ("*first apotome of a medial straight line*", "first-apotome-of-a-medial-straight-line"),
    ("*second apotome of a medial straight line*", "second-apotome-of-a-medial-straight-line"),
    ("*first apotome of a medial*", "first-apotome-of-a-medial-straight-line"),
    ("*second apotome of a medial*", "second-apotome-of-a-medial-straight-line"),
    ("*first bimedial*", "first-bimedial"),
    ("*second bimedial*", "second-bimedial"),
    ("*first trimedial*", "first-trimedial"),
    ("*second trimedial*", "second-trimedial"),
    ("*first binomial*", "first-binomial"),
    ("*second binomial*", "second-binomial"),
    ("*third binomial*", "third-binomial"),
    ("*fourth binomial*", "fourth-binomial"),
    ("*fifth binomial*", "fifth-binomial"),
    ("*sixth binomial*", "sixth-binomial"),
    ("*first apotome*", "first-apotome"),
    ("*second apotome*", "second-apotome"),
    ("*third apotome*", "third-apotome"),
    ("*fourth apotome*", "fourth-apotome"),
    ("*fifth apotome*", "fifth-apotome"),
    ("*sixth apotome*", "sixth-apotome"),
    ("*trinomial*", "trinomial"),
    ("*quadrinomial*", "quadrinomial"),
    ("*multinomial*", "multinomial"),
]


# ---------------------------------------------------------------------------
# 3. Historical Persons (:person:)
# ---------------------------------------------------------------------------

_PERSONS: List[Tuple[str, str]] = [
    # Multi-word names first (longest match wins)
    ("Isidorus of Miletus", "isidorus_of_miletus"),
    ("Isidore of Miletus", "isidorus_of_miletus"),
    ("Theodorus of Cyrene", "theodorus_of_cyrene"),
    ("Hippocrates of Chios", "hippocrates_of_chios"),
    ("Theon of Alexandria", "theon_of_alexandria"),
    ("Theon of Smyrna", "theon_of_smyrna"),
    ("Heron of Alexandria", "heron"),
    ("Hero of Alexandria", "heron"),
    ("Basilides of Tyre", "basilides_of_tyre"),
    ("Diogenes Laertius", "diogenes_laertius"),
    ("Leonardo of Pisa", "fibonacci"),
    ("Johannes of Palermo", "johannes_of_palermo"),
    ("Luca Paciuolo", "pacioli"),
    ("Michael Stifel", "stifel"),
    ("Hieronimo Cardano", "cardano"),
    ("Simon Stevin", "stevin"),
    ("Meier Hirsch", "hirsch"),
    ("Claudius Ptolemy", "ptolemy"),
    ("Vettius Valens", "vettius_valens"),
    ("David Gregory", "david_gregory"),
    ("Robert Simson", "simson"),
    ("Thomas Simpson", "thomas_simpson"),
    ("De Morgan", "de_morgan"),
    ("H. M. Taylor", "h_m_taylor"),
    ("G. Vitali", "vitali"),
    ("von Staudt", "staudt"),
    ("an-Nairīzī", "an_nairizi"),
    # Single-word canonical ancient & modern mathematicians/philosophers/scholars
    ("Archimedes", "archimedes"),
    ("Apollonius", "apollonius"),
    ("Aristotle", "aristotle"),
    ("Aristaeus", "aristaeus"),
    ("Theaetetus", "theaetetus"),
    ("Theodorus", "theodorus_of_cyrene"),
    ("Theodosius", "theodosius"),
    ("Pythagoras", "pythagoras"),
    ("Eratosthenes", "eratosthenes"),
    ("Hippocrates", "hippocrates_of_chios"),
    ("Hippasus", "hippasus"),
    ("Democritus", "democritus"),
    ("Hypsicles", "hypsicles"),
    ("Basilides", "basilides_of_tyre"),
    ("Protarchus", "protarchus"),
    ("Isidorus", "isidorus_of_miletus"),
    ("Eutocius", "eutocius"),
    ("Simplicius", "simplicius"),
    ("Proclus", "proclus"),
    ("Pappus", "pappus"),
    ("Geminus", "geminus"),
    ("Eudoxus", "eudoxus"),
    ("Eudemus", "eudemus"),
    ("Plutarch", "plutarch"),
    ("Ptolemy", "ptolemy"),
    ("Plato", "plato"),
    ("Theon", "theon_of_alexandria"),
    ("Heron", "heron"),
    ("Suidas", "suidas"),
    # Modern/Renaissance scholars in Volume III
    ("Bretschneider", "bretschneider"),
    ("Rausenberger", "rausenberger"),
    ("Nesselmann", "nesselmann"),
    ("Christensen", "christensen"),
    ("Billingsley", "billingsley"),
    ("Commandino", "commandino"),
    ("Cavalieri", "cavalieri"),
    ("Tartaglia", "tartaglia"),
    ("Todhunter", "todhunter"),
    ("Legendre", "legendre"),
    ("Poselger", "poselger"),
    ("Paciuolo", "pacioli"),
    ("Chrystal", "chrystal"),
    ("Sevenoak", "sevenoak"),
    ("Schultze", "schultze"),
    ("Dedekind", "dedekind"),
    ("Cardano", "cardano"),
    ("Cossali", "cossali"),
    ("Heiberg", "heiberg"),
    ("Hultsch", "hultsch"),
    ("Zeuthen", "zeuthen"),
    ("Tannery", "tannery"),
    ("Clavius", "clavius"),
    ("Fourier", "fourier"),
    ("Holgate", "holgate"),
    ("Killing", "killing"),
    ("Woepcke", "woepcke"),
    ("Allman", "allman"),
    ("Cantor", "cantor"),
    ("Cauchy", "cauchy"),
    ("Crelle", "crelle"),
    ("Curtze", "curtze"),
    ("Hankel", "hankel"),
    ("Hirsch", "hirsch"),
    ("Lorenz", "lorenz"),
    ("Mehler", "mehler"),
    ("Stevin", "stevin"),
    ("Stifel", "stifel"),
    ("Staudt", "staudt"),
    ("Simson", "simson"),
    ("Vitali", "vitali"),
    ("August", "august"),
    ("Hiller", "hiller"),
    ("Kluge", "kluge"),
    ("Loria", "loria"),
    ("Stolz", "stolz"),
    ("Suter", "suter"),
    ("Cobet", "cobet"),
    ("Diels", "diels"),
]


# ---------------------------------------------------------------------------
# 4. Bibliographic & Classical Locus Citations (:cite:)
# ---------------------------------------------------------------------------

def _norm_num(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[—–\-]+", "-", s)
    s = re.sub(r"[^a-z0-9.]+", ".", s)
    return s.strip(".")


def _build_cite_patterns() -> List[Tuple[re.Pattern, object]]:
    patterns: List[Tuple[re.Pattern, object]] = []

    # 1. Proclus, p. <page>, <line>
    patterns.append((
        re.compile(r"\bProclus,\s*pp?\.\s*(\d+(?:\s*[—–-]\s*\d+)?)(?:,\s*(\d+(?:\s*[—–-]\s*\d+)?))?"),
        lambda m: (
            f":cite:`Proclus, p. {m.group(1)}"
            + (f", {m.group(2)}" if m.group(2) else "")
            + f" <proclus:in_euclidem:{_norm_num(m.group(1))}"
            + (f".{_norm_num(m.group(2))}" if m.group(2) else "")
            + ">`"
        ),
    ))

    # 2. Aristotle works with Bekker or book/chapter numbers
    aristotle_works = [
        (r"\*Anal\.\s*Post\.\*", "analytica_posteriora"),
        (r"\*Anal\.\s*prior\.\*", "analytica_priora"),
        (r"\*Metaph\.\*", "metaphysica"),
        (r"\*Metaphysics\*", "metaphysica"),
        (r"\*Phys\.\*", "physica"),
        (r"\*Physics\*", "physica"),
        (r"\*De\s+caelo\*", "de_caelo"),
        (r"\*De\s+anima\*", "de_anima"),
        (r"\*De\s+lin\.\s*insec\.\*", "de_lineis_insecabilibus"),
        (r"\*Eth\.\s*Nic\.\*", "ethica_nicomachea"),
        (r"\*Soph\.\s*El\.\*", "sophistici_elenchi"),
        (r"\*Topics\*", "topica"),
        (r"\*Meteor\.\*", "meteorologica"),
    ]
    for w_pat, w_slug in aristotle_works:
        patterns.append((
            re.compile(
                rf"({w_pat})"
                r"(?:,?\s+([IVXLCDMivxlcdm]+\.\s*\d+(?:,\s*)?))?"
                r"(?:,?\s*(\d{3,4}\s*[ab]\s*\d+(?:\s*(?:[—–-]\s*\d+|,\s*\d+|sqq\.))?))?"
            ),
            lambda m, slug=w_slug: (
                f":cite:`{m.group(0)} <aristotle:{slug}"
                + (
                    f":{_norm_num(m.group(3))}"
                    if m.group(3)
                    else (f":{_norm_num(m.group(2))}" if m.group(2) else "")
                )
                + ">`"
            ),
        ))

    # 3. Plato dialogues with Stephanus numbers or standalone
    plato_works = [
        (r"\*Theaetetus\*", "theaetetus"),
        (r"\*Theaet\.\*", "theaetetus"),
        (r"\*Republic\*", "republic"),
        (r"\*Rep\.\*", "republic"),
        (r"\*Timaeus\*", "timaeus"),
        (r"\*Sophist\*", "sophist"),
        (r"\*Parmenides\*", "parmenides"),
        (r"\*Meno\*", "meno"),
        (r"\*Laws\*", "laws"),
        (r"\*Phaedo\*", "phaedo"),
        (r"\*Epinomis\*", "epinomis"),
    ]
    for w_pat, w_slug in plato_works:
        patterns.append((
            re.compile(
                rf"({w_pat})(?:,?\s*([IVXLCDM]+\.\s*)?(\d+\s*[A-Ea-e](?:\s*(?:[—–-]\s*[A-Ea-e0-9]+|,\s*[A-Ea-e0-9]+|sqq\.))?))?"
            ),
            lambda m, slug=w_slug: (
                f":cite:`{m.group(0)} <plato:{slug}"
                + (f":{_norm_num(m.group(3))}" if m.group(3) else "")
                + ">`"
            ),
        ))

    # 4. Classical & Modern works in Volume III
    standalone_works = [
        # Archimedes
        (r"\*On the Sphere and Cylinder\*(?:,?\s*([IVX]+\.(?:\s*\d+)?))?", "archimedes:de_sphaera_et_cylindro"),
        (r"\*On Conoids and Spheroids\*", "archimedes:de_conoidibus"),
        (r"\*Quadrature of the Parabola\*", "archimedes:quadratura_parabolae"),
        (r"\*Measurement of a Circle\*", "archimedes:dimensio_circuli"),
        (r"\*Sand-reckoner\*", "archimedes:arenarius"),
        (r"\*The Works of Archimedes\*(?:,\s*p\.\s*[xlvi0-9]+)?", "heath:works_of_archimedes"),
        (r"\*The Method of Archimedes\*", "heath:method_of_archimedes"),
        (r"\*Archimedis opera omnia\*", "heiberg:archimedis_opera"),
        (r"Ἀρχιμήδους περὶ τῶν μηχανικῶν θεωρημάτων πρὸς Ἐρατοσθένην ἔφοδος", "archimedes:methodus"),
        # Apollonius & Aristaeus & Pappus & Euclid
        (r"\*Comparison of the dodecahedron with the icosahedron\*", "apollonius:comparison_dodecahedron_icosahedron"),
        (r"\*Comparison of the five regular solids\*", "aristaeus:comparison_five_solids"),
        (r"\*Comparison of the five figures\*", "aristaeus:comparison_five_solids"),
        (r"\*Solid Loci\*", "aristaeus:solid_loci"),
        (r"\*Plane Loci\*", "apollonius:plane_loci"),
        (r"\*Surface-loci\*", "euclid:surface_loci"),
        (r"\*De divisionibus\*", "euclid:de_divisionibus"),
        (r"\*Sectio Canonis\*", "euclid:sectio_canonis"),
        (r"\*Porisms\*", "euclid:porisms"),
        (r"\*Data\*", "euclid:data"),
        (r"\*Phaenomena\*", "euclid:phaenomena"),
        (r"\*Optics\*", "euclid:optics"),
        (r"\*Elements\*", "euclid:elements"),
        (r"\*Treasury of Analysis\*", "pappus:synagoge:7"),
        (r"\*Synagoge\*", "pappus:synagoge"),
        (r"\*History of Geometry\*", "eudemus:history_of_geometry"),
        (r"\*Metrica\*", "heron:metrica"),
        (r"\*Sphaerica\*", "theodosius:sphaerica"),
        (r"\*Comm\. on Archimedes\*", "eutocius:in_archimedem"),
        (r"\*Comment\. in Aristot\. Phys\.\*(?:\s*p\.\s*\d+)?", "simplicius:in_physica"),
        (r"\*De Comm\. Not\. adv\. Stoicos\*(?:\s*[xlvi]+,\s*\d+)?", "plutarch:de_communibus_notitiis"),
        (r"περὶ ἀλόγων γραμμῶν καὶ ναστῶν βʹ", "democritus:peri_alogon_grammon"),
        # Renaissance & Modern works in Volume III
        (r"\*Liber Abaci\*", "fibonacci:liber_abaci"),
        (r"\*Arithmetica integra\*", "stifel:arithmetica_integra"),
        (r"\*Appendice des incommensurables grandeurs[^*]+\*", "stevin:appendice_incommensurables"),
        (r"\*Oeuvres mathématiques\*", "stevin:oeuvres_mathematiques"),
        (r"\*Origine, trasporto in Italia, primi progressi in essa dell' Algebra\*", "cossali:origine_algebra"),
        (r"\*Algebraischer Commentar über das zehente Buch der Elemente des Euklides\*", "hirsch:algebraischer_commentar"),
        (r"\*Ueber das zehnte Buch der Elemente des Euklides\*", "poselger:zehnte_buch"),
        (r"\*Die Algebra der Griechen\*(?:,\s*pp\.\s*\d+[—–-]\d+)?", "nesselmann:algebra_der_griechen"),
        (r"\*Le scienze esatte nell' antica Grecia\*(?:,\s*1914,\s*pp\.\s*\d+[—–-]\d+)?", "loria:scienze_esatte"),
        (r"\*Zeitschrift für Math\. u\. Physik \(Historisch-litterarische Abtheilung\)\*", "christensen:zeitschrift_math_phys"),
        (r"\*Penny Cyclopaedia\*", "de_morgan:penny_cyclopaedia"),
        (r"\*Mémoires présentés à l[’']Académie des Sciences\*", "woepcke:memoires_academie"),
        (r"\*Mémoires de la Société des sciences physiques et naturelles de Bordeaux\*", "tannery:memoires_bordeaux"),
        (r"\*Euklid-studien\*(?:,\s*pp\.\s*\d+[—–-]\d+)?", "heiberg:euklid_studien"),
        (r"\*Die Mathematiker und Astronomen der Araber und ihre Werke\*(?:,\s*pp\.\s*\d+\s+and\s+\d+)?", "suter:mathematiker_araber"),
        (r"\*Neue Jahrbücher für Philologie und Pädagogik\*", "hultsch:neue_jahrbuecher"),
        (r"\*Geschichte der Mathematik im Altertum und Mittelalter\*(?:,\s*p\.\s*\d+)?", "zeuthen:geschichte_altertum"),
        (r"\*Greek Geometry from Thales to Euclid\*(?:,\s*(?:1889,\s*)?pp\.\s*\d+(?:,\s*\d+[—–-]\d+|[—–-]\d+))?", "allman:greek_geometry"),
        (r"\*Geschichte der Mathematik\*", "cantor:vorlesungen"),
        (r"\*Gesch\.\s*d\.\s*Math\.\*", "cantor:vorlesungen"),
        (r"\*Text-book of Algebra\*", "chrystal:textbook_of_algebra"),
        (r"\*Éléments de Géométrie\*", "legendre:elements_de_geometrie"),
        (r"\*De Euclidis elementorum libris qui feruntur XIV et XV\*", "kluge:de_euclidis_xiv_xv"),
        (r"\*Real-Encyclopädie der classischen Altertumswissenschaft\*", "pauly_wissowa:real_encyclopaedie"),
        (r"\*Questioni riguardanti le matematiche elementari\*", "vitali:questioni"),
        (r"Diog\.\s*Laert\.\s*ix\.\s*47", "diogenes_laertius:vitae:9.47"),
    ]
    for w_pat, w_target in standalone_works:
        patterns.append((
            re.compile(w_pat),
            lambda m, tgt=w_target: f":cite:`{m.group(0)} <{tgt}>`",
        ))

    return patterns


_CITE_PATTERNS = _build_cite_patterns()


# ---------------------------------------------------------------------------
# 5. Inline Protection & Enrichment Engine
# ---------------------------------------------------------------------------

_PROTECTED_INLINE_RE = re.compile(
    r"(``[^`\n]+``|:[a-zA-Z0-9_.-]+:`[^`\n]+`|`[^`\n]+`_|`[^`\n]+`|\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\[\#f[^\]]+\]_|\[\d+\]_|\[[A-Za-z0-9_.-]+\]_)"
)

_PROTECTED_WITH_EMPH_RE = re.compile(
    r"(``[^`\n]+``|:[a-zA-Z0-9_.-]+:`[^`\n]+`|`[^`\n]+`_|`[^`\n]+`|\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\[\#f[^\]]+\]_|\[\d+\]_|\[[A-Za-z0-9_.-]+\]_|\*\*[^*\n]+\*\*|\*[^*\n]+\*)"
)

_VALID_OPENERS = set(" \t([{\"“‘'—–-/:")
_VALID_CLOSERS = set(" \t.,;:!?)]}\"”’'—–-/\\")


def _can_insert_role(text: str, start: int, end: int) -> bool:
    before = text[start - 1] if start > 0 else ""
    after = text[end] if end < len(text) else ""
    if before and before not in _VALID_OPENERS:
        return False
    if after and after not in _VALID_CLOSERS:
        return False
    return True


def _apply_to_unprotected_segments(line: str, fn, protect_emph: bool = False) -> str:
    splitter = _PROTECTED_WITH_EMPH_RE if protect_emph else _PROTECTED_INLINE_RE
    parts = splitter.split(line)
    for idx in range(0, len(parts), 2):
        if parts[idx]:
            parts[idx] = fn(parts[idx])
    return "".join(parts)


def enrich_line(line: str, rel_path: str, stats: Dict[str, int]) -> str:
    """Enrich a single body line with :term:, :cite:, and :person: roles."""
    is_def_folio = (
        rel_path == "book_x/introductory_note/0014.rst"
        or rel_path.startswith("book_x/propositions/")
        or rel_path in (
            "book_xi/definitions/0264.rst",
            "book_xi/definitions/0265.rst",
            "book_xi/definitions/0266.rst",
        )
    )

    # Step A: Bolded defined terms in Euclid's Definitions (Book X & Book XI)
    if is_def_folio and "**" in line:
        def _replace_bold_def(seg: str) -> str:
            def _sub_b(m: re.Match) -> str:
                if not _can_insert_role(seg, m.start(), m.end()):
                    return m.group(0)
                inner = m.group(1).strip()
                # Check if inner ends with a period inside the bold (e.g. **apotome.**)
                trailing_dot = ""
                lookup = inner.lower()
                if lookup.endswith(".") and lookup[:-1] in _DEFINITION_TERM_SLUGS:
                    trailing_dot = "."
                    inner_clean = inner[:-1]
                    slug = _DEFINITION_TERM_SLUGS[lookup[:-1]]
                elif lookup in _DEFINITION_TERM_SLUGS:
                    inner_clean = inner
                    slug = _DEFINITION_TERM_SLUGS[lookup]
                else:
                    return m.group(0)
                stats["term"] += 1
                return f":term:`**{inner_clean}** <{slug}>`{trailing_dot}"

            return re.sub(r"\*\*([^\*\n]+)\*\*", _sub_b, seg)

        line = _apply_to_unprotected_segments(line, _replace_bold_def)

    # Step B: Citations (:cite:)
    for pat, repl_fn in _CITE_PATTERNS:
        def _replace_cite(seg: str, p=pat, rfn=repl_fn) -> str:
            out = []
            last = 0
            for m in p.finditer(seg):
                if _can_insert_role(seg, m.start(), m.end()):
                    out.append(seg[last:m.start()])
                    out.append(rfn(m))
                    stats["cite"] += 1
                    last = m.end()
            out.append(seg[last:])
            return "".join(out)

        line = _apply_to_unprotected_segments(line, _replace_cite)

    # Step C: Greek & Latin technical terms (:term:)
    # Skip the Greek Index itself (0525-0530) and General Index (0531-0550) so index tables stay clean
    if not rel_path.startswith("general_index"):
        for phrase, slug in _GREEK_LATIN_TERMS:
            if phrase not in line:
                continue
            escaped = re.escape(phrase)
            is_italic_phrase = phrase.startswith("*")
            if is_italic_phrase:
                p_re = re.compile(rf"(?<!\*){escaped}(?!\*)")
            else:
                p_re = re.compile(rf"(?<![\w\u0370-\u03ff\u1f00-\u1fff\*]){escaped}(?![\w\u0370-\u03ff\u1f00-\u1fff\*])")

            def _replace_gl(seg: str, pat=p_re, ph=phrase, sl=slug) -> str:
                out = []
                last = 0
                for m in pat.finditer(seg):
                    if _can_insert_role(seg, m.start(), m.end()):
                        out.append(seg[last:m.start()])
                        out.append(f":term:`{ph} <{sl}>`")
                        stats["term"] += 1
                        last = m.end()
                out.append(seg[last:])
                return "".join(out)

            line = _apply_to_unprotected_segments(line, _replace_gl, protect_emph=not is_italic_phrase)

    # Step D: Historical Persons (:person:)
    if not rel_path.startswith("general_index"):
        for name, slug in _PERSONS:
            if name not in line:
                continue
            p_re = re.compile(rf"(?<![\w\*]){re.escape(name)}(?![\w\*])")

            def _replace_person(seg: str, pat=p_re, nm=name, sl=slug) -> str:
                out = []
                last = 0
                for m in pat.finditer(seg):
                    if _can_insert_role(seg, m.start(), m.end()):
                        out.append(seg[last:m.start()])
                        out.append(f":person:`{nm} <{sl}>`")
                        stats["person"] += 1
                        last = m.end()
                out.append(seg[last:])
                return "".join(out)

            line = _apply_to_unprotected_segments(line, _replace_person, protect_emph=True)

    return line


# ---------------------------------------------------------------------------
# 6. File Processor & Validation
# ---------------------------------------------------------------------------

def process_folio(rst_path: Path, vol3_dir: Path, stats: Dict[str, int]) -> bool:
    rel_path = str(rst_path.relative_to(vol3_dir))
    orig_text = rst_path.read_text(encoding="utf-8")
    lines = orig_text.splitlines()

    # Pass 1: Normalize 4-level section headings (=, -, ~, ^) and uppercase Proposition N.
    heading_line_indices = set()
    for i in range(1, len(lines)):
        s = lines[i].strip()
        if _ADORNMENT_RE.match(s):
            prev = lines[i - 1].strip()
            if prev and not prev.startswith("..") and not prev.startswith(":"):
                # Normalize "Proposition 24." -> "PROPOSITION 24."
                if re.match(r"^Proposition\s+\d+\.$", prev):
                    prev = prev.upper()
                    lines[i - 1] = prev
                ch = classify_heading_char(prev, rel_path)
                w = _column_width(prev)
                new_adorn = ch * w
                if lines[i] != new_adorn:
                    lines[i] = new_adorn
                    stats["headings_normalized"] += 1
                heading_line_indices.add(i - 1)
                heading_line_indices.add(i)

    # Pass 2: Enrich body lines outside directives/headers/code-blocks/math-blocks
    out_lines: List[str] = []
    in_code_block = False
    in_math_block = False
    code_indent = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track $$ ... $$ multi-line math blocks
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4:
            out_lines.append(line)
            continue
        if stripped.startswith("$$"):
            in_math_block = not in_math_block
            out_lines.append(line)
            continue
        if in_math_block:
            if stripped.endswith("$$"):
                in_math_block = False
            out_lines.append(line)
            continue

        if in_code_block:
            if stripped and (len(line) - len(line.lstrip(" "))) <= code_indent and not stripped.startswith(":"):
                in_code_block = False
            else:
                out_lines.append(line)
                continue

        if i in heading_line_indices:
            out_lines.append(line)
            continue

        # Skip bibliographic field list lines or directive option lines (:key: val)
        if re.match(r"^\s*:[a-zA-Z0-9_.-]+:(?:\s|$)", line):
            out_lines.append(line)
            continue

        # Check for directive lines (.. name:: arg)
        m_dir = re.match(r"^(\s*)\.\.\s+([a-zA-Z0-9_-]+)::(.*)$", line)
        if m_dir:
            dname = m_dir.group(2).lower()
            if dname in ("code-block", "math", "raw"):
                in_code_block = True
                code_indent = len(m_dir.group(1))
            out_lines.append(line)
            continue

        # Skip transition lines (----)
        if re.fullmatch(r"-{4,}", stripped):
            out_lines.append(line)
            continue

        out_lines.append(enrich_line(line, rel_path, stats))

    new_text = "\n".join(out_lines) + "\n"
    if new_text != orig_text:
        rst_path.write_text(new_text, encoding="utf-8")
        return True
    return False


def validate_folio_rst_strict(rst_text: str) -> List[str]:
    """Strictly validate heading underlines, role syntax, and Docutils start/end boundaries."""
    warnings: List[str] = []
    lines = rst_text.splitlines()

    # 1. Check section underline widths and allowed 4-level characters (=, -, ~, ^)
    for i in range(1, len(lines)):
        s = lines[i].strip()
        if _ADORNMENT_RE.match(s):
            prev = lines[i - 1].strip()
            if prev and not prev.startswith("..") and not prev.startswith(":"):
                ch = s[0]
                if ch not in ("=", "-", "~", "^"):
                    warnings.append(f"Line {i+1}: Non-standard heading underline char {ch!r}")
                expected_w = _column_width(prev)
                if len(s) < expected_w:
                    warnings.append(
                        f"Line {i+1}: Underline too short ({len(s)} < {expected_w}) for {prev!r}"
                    )

    # 2. Check inline roles outside code blocks
    in_code = False
    code_indent = 0
    role_re = re.compile(r"(.?)(:[a-zA-Z0-9_.-]+:`[^`\n]+`)(.?)")

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if in_code:
            if stripped and (len(line) - len(line.lstrip(" "))) <= code_indent and not stripped.startswith(":"):
                in_code = False
            else:
                continue
        m_dir = re.match(r"^(\s*)\.\.\s+([a-zA-Z0-9_-]+)::", line)
        if m_dir:
            if m_dir.group(2).lower() in ("code-block", "math", "raw"):
                in_code = True
                code_indent = len(m_dir.group(1))
            continue

        line_no_lit = re.sub(r"``[^`\n]+``", lambda m: " " * len(m.group(0)), line)
        for m_r in role_re.finditer(line_no_lit):
            pre, role_tok, post = m_r.group(1), m_r.group(2), m_r.group(3)
            if pre and pre not in _VALID_OPENERS:
                warnings.append(f"Line {i}: Invalid char {pre!r} before role {role_tok}")
            if post and post not in _VALID_CLOSERS:
                warnings.append(f"Line {i}: Invalid char {post!r} after role {role_tok}")

    return warnings


def main() -> None:
    vol3_dir = _REPO_ROOT / "resources" / "heath" / "volume_III"
    rst_files = sorted(
        p for p in vol3_dir.rglob("*.rst") if not p.name.endswith(".notes.rst")
    )
    stats = {
        "files_modified": 0,
        "headings_normalized": 0,
        "term": 0,
        "cite": 0,
        "person": 0,
    }

    for rst_p in rst_files:
        if process_folio(rst_p, vol3_dir, stats):
            stats["files_modified"] += 1

    # Count total roles across all 550 folios
    totals = {"term": 0, "cite": 0, "person": 0, "g": 0, "just": 0, "line": 0}
    heading_levels = {"=": 0, "-": 0, "~": 0, "^": 0}
    errors = []

    for rst_p in rst_files:
        txt = rst_p.read_text(encoding="utf-8")
        for rname in totals:
            totals[rname] += len(re.findall(rf":{rname}:`[^`\n]+`", txt))
        lines = txt.splitlines()
        for i in range(1, len(lines)):
            s = lines[i].strip()
            if _ADORNMENT_RE.match(s):
                prev = lines[i - 1].strip()
                if prev and not prev.startswith("..") and not prev.startswith(":"):
                    ch = s[0]
                    heading_levels[ch] = heading_levels.get(ch, 0) + 1

        try:
            rendered = render_rst_html(txt)
            if not rendered and txt.strip():
                errors.append((str(rst_p.relative_to(vol3_dir)), "Empty rendered HTML"))
        except Exception as exc:
            errors.append((str(rst_p.relative_to(vol3_dir)), str(exc)))

        w_list = validate_folio_rst_strict(txt)
        if w_list:
            errors.append((str(rst_p.relative_to(vol3_dir)), "; ".join(w_list)))

    print(
        f"Processed {len(rst_files)} folios in volume_III: "
        f"modified={stats['files_modified']}, "
        f"headings_normalized={stats['headings_normalized']}"
    )
    print(f"Heading level distribution across volume_III: {heading_levels}")
    print(f"Total semantic roles in volume_III: {totals}")
    print(f"Validation warnings/errors across {len(rst_files)} files: {len(errors)}")
    for rel, w in errors[:20]:
        print(f"  {rel}: {w}")


if __name__ == "__main__":
    main()
