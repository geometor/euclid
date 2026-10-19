#!/usr/bin/env python3
"""Enrich Volume II (.rst folios) with normalized 4-level headings and :term:, :cite:, and :person: roles."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, Tuple

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
# 1. Fixed 4-Level Heading Hierarchy (=, -, ~, ^) for Volume II
# ---------------------------------------------------------------------------

_LEVEL_1_EXACT = {
    "THE THIRTEEN BOOKS OF EUCLID'S ELEMENTS",
    "CONTENTS OF VOLUME II.",
    "BOOK III.",
    "BOOK III. PROPOSITIONS.",
    "BOOK IV.",
    "BOOK IV. PROPOSITIONS",
    "BOOK IV. PROPOSITIONS.",
    "BOOK V.",
    "BOOK V. PROPOSITIONS.",
    "BOOK VI.",
    "BOOK VI. PROPOSITIONS.",
    "BOOK VII.",
    "BOOK VIII.",
    "BOOK IX.",
    "INDEX OF GREEK WORDS AND FORMS.",
    "ENGLISH INDEX.",
    "ENGLISH INDEX",
}

_LEVEL_2_EXACT = {
    "DEFINITIONS.",
    "DEFINITIONS",
    "PROPOSITIONS.",
    "INTRODUCTORY NOTE.",
}

_LEVEL_2_PATTERNS = [
    re.compile(r"^\[?DEFINITIONS?\s+\d+(?:\s*(?:,|—|-)\s*\d+)*\.$"),
    re.compile(r"^\[?PROPOSITIONS?\s+(?:\d+|[A-Z])(?:\s*,\s*\d+)*\.$"),
]

_LEVEL_4_PATTERNS = [
    re.compile(r"^[1-9]\.\s+"),
    re.compile(r"^\([a-z]\)\s+"),
]


def classify_heading_char(title: str, rel_path: str) -> str:
    """Return the canonical underline character ('=', '-', '~', '^') for a heading title."""
    t = title.strip()
    if t in _LEVEL_1_EXACT:
        return "="
    if t in _LEVEL_2_EXACT:
        return "-"
    for pat in _LEVEL_2_PATTERNS:
        if pat.match(t):
            return "-"
    for pat in _LEVEL_4_PATTERNS:
        if pat.match(t):
            return "^"
    return "~"


def normalize_headings(lines: List[str], rel_path: str) -> Tuple[List[str], int]:
    """Normalize all section underlines in `lines` to the 4-level hierarchy."""
    out = list(lines)
    changed = 0
    for i in range(1, len(out)):
        stripped = out[i].strip()
        if _ADORNMENT_RE.match(stripped):
            prev = out[i - 1].strip()
            if prev and not prev.startswith("..") and not prev.startswith(":"):
                target_ch = classify_heading_char(prev, rel_path)
                new_underline = target_ch * _column_width(prev)
                if out[i] != new_underline:
                    out[i] = new_underline
                    changed += 1
    return out, changed


# ---------------------------------------------------------------------------
# 2. Defined Terms, Technical Terms & Greek Terms (:term:)
# ---------------------------------------------------------------------------

# Explicit bolded defined terms in Books III, IV, V, VI, VII Definitions
_BOLD_DEF_TERMS: List[Tuple[str, str]] = [
    # Book III Definitions (0007.rst, 0008.rst)
    ("**Equal circles**", "equal-circles"),
    ("**touch one another**", "circles-touching"),
    ("**touch a circle**", "tangent-to-circle"),
    ("**equally distant from the centre**", "equally-distant-from-centre"),
    ("**at a greater distance**", "greater-distance-from-centre"),
    ("**segment of a circle**", "segment-of-circle"),
    ("**angle of a segment**", "angle-of-segment"),
    ("**angle in a segment**", "angle-in-segment"),
    ("**base of the segment**", "base-of-segment"),
    ("**stand upon**", "stand-upon-circumference"),
    ("**sector of a circle**", "sector-of-circle"),
    ("**Similar segments of circles**", "similar-segments-of-circles"),
    # Book IV Definitions (0084.rst)
    ("**inscribed in a rectilineal figure**", "inscribed-in-rectilineal-figure"),
    ("**circumscribed about a figure**", "circumscribed-about-figure"),
    ("**inscribed in a circle**", "inscribed-in-circle"),
    ("**circumscribed about a circle**", "circumscribed-about-circle"),
    ("**inscribed in a figure**", "circle-inscribed-in-figure"),
    ("**fitted into a circle**", "fitted-into-circle"),
    # Book V Definitions (0119.rst, 0120.rst, 0121.rst)
    ("**part**", "part-aliquot"),
    ("**multiple**", "multiple"),
    ("**ratio**", "ratio"),
    ("**have a ratio**", "have-a-ratio"),
    ("**be in the same ratio**", "in-the-same-ratio"),
    ("**in the same ratio**", "in-the-same-ratio"),
    ("**proportional**", "proportional"),
    ("**have a greater ratio**", "greater-ratio"),
    ("**greater ratio**", "greater-ratio"),
    ("**proportion in three terms**", "proportion-in-three-terms"),
    ("**duplicate ratio**", "duplicate-ratio"),
    ("**triplicate ratio**", "triplicate-ratio"),
    ("**corresponding magnitudes**", "corresponding-magnitudes"),
    ("**Alternate ratio**", "alternate-ratio"),
    ("**Inverse ratio**", "inverse-ratio"),
    ("**Composition of a ratio**", "composition-of-a-ratio"),
    ("**Separation of a ratio**", "separation-of-a-ratio"),
    ("**Conversion of a ratio**", "conversion-of-a-ratio"),
    ("**Ratio ex aequali**", "ratio-ex-aequali"),
    ("**perturbed proportion**", "perturbed-proportion"),
    # Book VI Definitions (0194.rst)
    ("**Similar rectilineal figures**", "similar-rectilineal-figures"),
    ("**Reciprocally related figures.**", "reciprocally-related"),
    ("**A straight line is said to have been cut in extreme and mean ratio**", "extreme-and-mean-ratio"),
    ("**extreme and mean ratio**", "extreme-and-mean-ratio"),
    ("**The height**", "height"),
    ("**height**", "height"),
    ("**compounded of the ratios**", "compound-ratio"),
    # Book VII Definitions (0283.rst, 0284.rst)
    ("**unit**", "unit"),
    ("**number**", "number"),
    ("**parts**", "parts-non-aliquot"),
    ("**even number**", "even-number"),
    ("**odd number**", "odd-number"),
    ("**even-times even number**", "even-times-even-number"),
    ("**even-times odd number**", "even-times-odd-number"),
    ("**odd-times odd number**", "odd-times-odd-number"),
    ("**prime number**", "prime-number"),
    ("**Numbers prime to one another**", "prime-to-one-another"),
    ("**prime to one another**", "prime-to-one-another"),
    ("**composite number**", "composite-number"),
    ("**Numbers composite to one another**", "composite-to-one-another"),
    ("**composite to one another**", "composite-to-one-another"),
    ("**multiply**", "multiply"),
    ("**plane**", "plane-number"),
    ("**solid**", "solid-number"),
    ("**sides**", "side-of-number"),
    ("**square number**", "square-number"),
    ("**cube**", "cube-number"),
    ("**Similar plane and solid numbers**", "similar-plane-and-solid-numbers"),
    ("**perfect number**", "perfect-number"),
]

# Italicized Latin & English technical terms in Volume II
_ITALIC_TERMS: List[Tuple[str, str]] = [
    ("*similar plane and solid numbers*", "similar-plane-and-solid-numbers"),
    ("*similar segments of circles*", "similar-segments-of-circles"),
    ("*similar rectilineal figures*", "similar-rectilineal-figures"),
    ("*extreme and mean ratio*", "extreme-and-mean-ratio"),
    ("*composition of a ratio*", "composition-of-a-ratio"),
    ("*superparticularis ratio*", "superparticularis-ratio"),
    ("*separation of a ratio*", "separation-of-a-ratio"),
    ("*conversion of a ratio*", "conversion-of-a-ratio"),
    ("*reductio ad absurdum*", "reductio-ad-absurdum"),
    ("*perturbed proportion*", "perturbed-proportion"),
    ("*angle of a segment*", "angle-of-segment"),
    ("*triplicate ratio*", "triplicate-ratio"),
    ("*angle of contact*", "angle-of-contact"),
    ("*mutatis mutandis*", "mutatis-mutandis"),
    ("*duplicate ratio*", "duplicate-ratio"),
    ("*alternate ratio*", "alternate-ratio"),
    ("*even-times even*", "even-times-even-number"),
    ("*even-times odd*", "even-times-odd-number"),
    ("*odd-times even*", "odd-times-even-number"),
    ("*compound ratio*", "compound-ratio"),
    ("*golden section*", "golden-section"),
    ("*hornlike angle*", "hornlike-angle"),
    ("*odd-times odd*", "odd-times-odd-number"),
    ("*inverse ratio*", "inverse-ratio"),
    ("*convertendo*", "convertendo"),
    ("*componendo*", "componendo"),
    ("*alternando*", "alternando"),
    ("*invertendo*", "invertendo"),
    ("*permutando*", "permutando"),
    ("*ex aequali*", "ratio-ex-aequali"),
    ("*a fortiori*", "a-fortiori"),
    ("*separando*", "separando"),
    ("*dirimendo*", "dirimendo"),
    ("*dividendo*", "dividendo"),
    ("*even-odd*", "even-times-odd-number"),
    ("*odd-even*", "odd-times-even-number"),
]

# Greek technical phrases & terms in Volume II (sorted longest-first at compile time)
_GREEK_TERMS_RAW: List[Tuple[str, str]] = [
    # Standard conclusions & phrases
    ("ὅπερ ἔδει δεῖξαι", "hoper-edei-deixai"),
    ("ὅπερ ἔδει ποιῆσαι", "hoper-edei-poiesai"),
    ("παραβολὴ τῶν χωρίων", "parabole-ton-chorion"),
    ("τόπος ἀναλυόμενος", "topos-analyomenos"),
    ("εἰς τὸ ἀδύνατον", "eis-to-adynaton"),
    ("ἡ εἰς τὸ ἀδύνατον ἀπαγωγή", "apagoge-eis-to-adynaton"),
    ("ἐπ᾽ ἄκρον καὶ μέσον λόγον", "extreme-and-mean-ratio"),
    ("ἄκρος καὶ μέσος λόγος", "extreme-and-mean-ratio"),
    ("ἐν τῷ αὐτῷ λόγῳ", "in-the-same-ratio"),
    ("λόγον ἔχειν πρὸς ἄλληλα", "have-a-ratio"),
    ("λόγον ἔχειν", "have-a-ratio"),
    ("ἐναλλὰξ λόγος", "alternate-ratio"),
    ("ἀνάπαλιν λόγος", "inverse-ratio"),
    ("σύνθεσις λόγου", "composition-of-a-ratio"),
    ("διαίρεσις λόγου", "separation-of-a-ratio"),
    ("ἀναστροφὴ λόγου", "conversion-of-a-ratio"),
    ("δι᾽ ἴσου λόγος", "ratio-ex-aequali"),
    ("τεταραγμένη ἀναλογία", "perturbed-proportion"),
    ("τεταραγμένης οὔσης τῆς ἀναλογίας", "perturbed-proportion"),
    ("διπλασίων λόγος", "duplicate-ratio"),
    ("τριπλασίων λόγος", "triplicate-ratio"),
    ("συγκείμενος λόγος", "compound-ratio"),
    ("γωνία τμήματος", "angle-of-segment"),
    ("κερατοειδὴς γωνία", "hornlike-angle"),
    ("μηνοειδὴς γωνία", "menoeides-gonia"),
    ("μικτὴ γωνία", "mikte-gonia"),
    ("τμῆμα κύκλου", "segment-of-circle"),
    ("τομεὺς κύκλου", "sector-of-circle"),
    ("ἀντιπεπονθότα σχήματα", "reciprocally-related"),
    ("ἀντιπεπονθέναι", "reciprocally-related"),
    ("ἀρτιάκις ἄρτιος ἀριθμός", "even-times-even-number"),
    ("ἀρτιάκις ἄρτιος", "even-times-even-number"),
    ("ἀρτιάκις περισσὸς ἀριθμός", "even-times-odd-number"),
    ("ἀρτιάκις περισσός", "even-times-odd-number"),
    ("περισσάρτιος", "odd-times-even-number"),
    ("περισσάκις ἄρτιος", "odd-times-even-number"),
    ("περισσάκις περισσὸς ἀριθμός", "odd-times-odd-number"),
    ("περισσάκις περισσός", "odd-times-odd-number"),
    ("πρῶτος ἀριθμός", "prime-number"),
    ("πρῶτοι πρὸς ἀλλήλους", "prime-to-one-another"),
    ("σύνθετος ἀριθμός", "composite-number"),
    ("σύνθετοι πρὸς ἀλλήλους", "composite-to-one-another"),
    ("ἐπίπεδος ἀριθμός", "plane-number"),
    ("στερεὸς ἀριθμός", "solid-number"),
    ("τετράγωνος ἀριθμός", "square-number"),
    ("κύβος ἀριθμός", "cube-number"),
    ("τέλειος ἀριθμός", "perfect-number"),
    ("ἑτερομήκης ἀριθμός", "heteromekes-arithmos"),
    ("προμήκης ἀριθμός", "promekes-arithmos"),
    ("ἐλλιπὴς ἀριθμός", "elleipes-arithmos"),
    ("ὑπερτελὴς ἀριθμός", "hyperteles-arithmos"),
    ("δεύτερος καὶ σύνθετος", "composite-number"),
    ("κοινὸν μέτρον", "koinon-metron"),
    ("μέγιστον κοινὸν μέτρον", "megiston-koinon-metron"),
    ("ἐλάχιστος κοινὸς πολλαπλάσιος", "elachistos-koinos-pollaplasios"),
    ("συνεχὴς ἀναλογία", "syneches-analogia"),
    ("διῃρημένη ἀναλογία", "dieiremene-analogia"),
    ("μονὰς προσλαβοῦσα θέσιν", "monas-proslabousa-thesin"),
    ("σύστημα μονάδων", "systema-monadon"),
    ("ποσότης χύμα", "posotes-chyma"),
    ("πλῆθος ὡρισμένον", "plethos-horismenon"),
    ("περαίνουσα ποσότης", "perainousa-posotes"),
    # Single & inflected Greek technical words in Volume II
    ("ἀδιαίρετος", "adiairetos"),
    ("ἀδιαίρετον", "adiaireton"),
    ("ἀσύμμετρος", "asymmetros"),
    ("ἀσύμμετρα", "asymmetros"),
    ("σύμμετρος", "symmetros"),
    ("σύμμετρα", "symmetros"),
    ("ἀνθυφαίρεσις", "anthyphairesis"),
    ("ἀνθυφαιρεῖν", "anthyphairein"),
    ("ἀνταναίρεσις", "antanairesis"),
    ("ἀντιπεπονθότα", "reciprocally-related"),
    ("ἀντιπεπονθός", "reciprocally-related"),
    ("ἀντιπεπόνθησις", "antipeponthesis"),
    ("ἀνάλογον", "proportional"),
    ("ἀναλογία", "analogia"),
    ("ἀναλογίας", "analogia"),
    ("ἀναλογίαι", "analogia"),
    ("μεσότης", "mesotes"),
    ("μεσότητες", "mesotes"),
    ("λόγος", "ratio"),
    ("λόγου", "ratio"),
    ("λόγον", "ratio"),
    ("λόγοι", "ratio"),
    ("λόγων", "ratio"),
    ("διάστημα", "diastema"),
    ("διαστήματος", "diastema"),
    ("σχέσις", "schesis"),
    ("πηλικότης", "pelikotes"),
    ("πηλικότητα", "pelikotes"),
    ("μέγεθος", "megethos"),
    ("μεγέθους", "megethos"),
    ("μεγέθη", "megethos"),
    ("μεγεθῶν", "megethos"),
    ("μέρος", "part-aliquot"),
    ("μέρη", "parts-non-aliquot"),
    ("μόριον", "morion"),
    ("πολλαπλάσιος", "multiple"),
    ("πολλαπλάσιον", "multiple"),
    ("πολλαπλάσια", "multiple"),
    ("ἰσάκις", "isakis"),
    ("ὁμόλογος", "corresponding-magnitudes"),
    ("ὁμόλογα", "corresponding-magnitudes"),
    ("ἡγούμενον", "hegoumenon"),
    ("ἡγούμενα", "hegoumenon"),
    ("ἑπόμενον", "hepomenon"),
    ("ἑπόμενα", "hepomenon"),
    ("ἐναλλάξ", "alternando"),
    ("ἀνάπαλιν", "invertendo"),
    ("συνθέντι", "componendo"),
    ("κατὰ σύνθεσιν", "componendo"),
    ("διελόντι", "separando"),
    ("κατὰ διαίρεσιν", "separando"),
    ("ἀναστρέψαντι", "convertendo"),
    ("δι᾽ ἴσου", "ratio-ex-aequali"),
    ("μονάς", "unit"),
    ("μονάδος", "unit"),
    ("μονάδα", "unit"),
    ("μονάδες", "unit"),
    ("μονάδων", "unit"),
    ("ἀριθμός", "number"),
    ("ἀριθμοῦ", "number"),
    ("ἀριθμόν", "number"),
    ("ἀριθμοί", "number"),
    ("ἀριθμῶν", "number"),
    ("ἄρτιος", "even-number"),
    ("ἄρτιοι", "even-number"),
    ("περισσός", "odd-number"),
    ("περισσοί", "odd-number"),
    ("πρῶτος", "prime-number"),
    ("πρῶτοι", "prime-number"),
    ("σύνθετος", "composite-number"),
    ("σύνθετοι", "composite-number"),
    ("πολλαπλασιάζειν", "multiply"),
    ("ἐπίπεδος", "plane-number"),
    ("ἐπίπεδοι", "plane-number"),
    ("στερεός", "solid-number"),
    ("στερεοί", "solid-number"),
    ("πλευρά", "side-of-number"),
    ("πλευραί", "side-of-number"),
    ("τετράγωνος", "square-number"),
    ("τετράγωνοι", "square-number"),
    ("κύβος", "cube-number"),
    ("κύβοι", "cube-number"),
    ("τέλειος", "perfect-number"),
    ("τέλειοι", "perfect-number"),
    ("ἑτερομήκης", "heteromekes-arithmos"),
    ("ἑτερομήκεις", "heteromekes-arithmos"),
    ("προμήκης", "promekes-arithmos"),
    ("προμήκεις", "promekes-arithmos"),
    ("σφηκίσκος", "sphekiskos"),
    ("βωμίσκος", "bomiskos"),
    ("πλινθίς", "plinthis"),
    ("δοκίς", "dokis"),
    ("σκαληνός", "skalenos"),
    ("παραλληλεπίπεδος", "parallelepipedos"),
    ("κυβόκυβος", "kybokybos"),
    ("δυναμοδύναμις", "dynamodynamis"),
    ("δυναμόκυβος", "dynamokybos"),
    ("δύναμις", "dynamis"),
    ("δυνάμει", "dynamei"),
    ("κύκλος", "kyklos"),
    ("κύκλου", "kyklos"),
    ("κύκλοι", "kyklos"),
    ("κέντρον", "kentron"),
    ("κέντρου", "kentron"),
    ("διάμετρος", "diametros"),
    ("διαμέτρου", "diametros"),
    ("διάμετρον", "diametros"),
    ("περιφέρεια", "periphereia"),
    ("περιφερείας", "periphereia"),
    ("περιφέρειαν", "periphereia"),
    ("χορδή", "chorde"),
    ("ἐφαπτομένη", "ephaptomene"),
    ("ἐφάπτεσθαι", "ephaptesthai"),
    ("τέμνειν", "temnein"),
    ("τμῆμα", "segment-of-circle"),
    ("τμήματος", "segment-of-circle"),
    ("τμήματα", "segment-of-circle"),
    ("τομεύς", "sector-of-circle"),
    ("τομέως", "sector-of-circle"),
    ("ἡμικύκλιον", "hemikyklion"),
    ("ἡμικυκλίου", "hemikyklion"),
    ("κερατοειδής", "hornlike-angle"),
    ("ἐγγράφειν", "engraphein"),
    ("περιγράφειν", "perigraphein"),
    ("ἐναρμόζειν", "enarmozein"),
    ("πεντάγωνον", "pentagonon"),
    ("ἑξάγωνον", "hexagonon"),
    ("πεντεκαιδεκάγωνον", "pentekaidekagonon"),
    ("γνώμων", "gnomon"),
    ("γνώμονος", "gnomon"),
    ("γνώμονα", "gnomon"),
    ("παραβολή", "parabole"),
    ("ὑπερβολή", "hyperbole"),
    ("ἔλλειψις", "elleipsis"),
    ("ἐλλεῖπον", "elleipon"),
    ("ὑπερβάλλον", "hyperballon"),
    ("παραβάλλειν", "paraballein"),
    ("ὕψος", "height"),
    ("βάσις", "basis"),
    ("ὅμοιος", "homoios"),
    ("ὅμοια", "homoios"),
    ("ἰσογώνιος", "isogonios"),
    ("πορισμός", "porismos"),
    ("πόρισμα", "porisma"),
    ("λῆμμα", "lemma"),
    ("ἔκθεσις", "ekthesis"),
    ("διορισμός", "diorismos"),
    ("κατασκευή", "kataskeue"),
    ("ἀπόδειξις", "apodeixis"),
    ("συμπέρασμα", "symperasma"),
    ("ἔνστασις", "enstasis"),
    ("ἀπαγωγή", "apagoge"),
    ("ἀνάλυσις", "analysis"),
    ("σύνθεσις", "synthesis"),
]

_GREEK_MAP: Dict[str, str] = {}
for _gw, _gslug in sorted(_GREEK_TERMS_RAW, key=lambda kv: (-len(kv[0]), kv[0])):
    if _gw not in _GREEK_MAP:
        _GREEK_MAP[_gw] = _gslug

_GREEK_PATTERN = re.compile(
    r"(?<![\w\u0370-\u03ff\u1f00-\u1fff`])("
    + "|".join(re.escape(k) for k in _GREEK_MAP)
    + r")(?![\w\u0370-\u03ff\u1f00-\u1fff`])"
)


# ---------------------------------------------------------------------------
# 3. Bibliographic & Classical Locus Citations (:cite:)
# ---------------------------------------------------------------------------

def _norm_locus_slug(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return s or "ref"


_CLASSICAL_WORK_MAP: Dict[str, str] = {
    "Anal. Post.": "aristotle:anal-post",
    "Anal. post.": "aristotle:anal-post",
    "Anal. Prior.": "aristotle:anal-prior",
    "Anal. prior.": "aristotle:anal-prior",
    "Metaph.": "aristotle:metaphysics",
    "Metaphysics": "aristotle:metaphysics",
    "Phys.": "aristotle:physics",
    "Physics": "aristotle:physics",
    "Topics": "aristotle:topics",
    "Topica": "aristotle:topics",
    "De caelo": "aristotle:de-caelo",
    "De anima": "aristotle:de-anima",
    "Meteor.": "aristotle:meteorologica",
    "Meteorologica": "aristotle:meteorologica",
    "Eth. Nic.": "aristotle:eth-nic",
    "Cat.": "aristotle:categories",
    "Categories": "aristotle:categories",
    "Soph. El.": "aristotle:soph-el",
    "Mech.": "aristotle:mechanica",
    "Mechanics": "aristotle:mechanica",
    "Probl.": "aristotle:problemata",
    "Problems": "aristotle:problemata",
    "De lin. insec.": "aristotle:de-lin-insec",
    "De incessu animalium": "aristotle:de-incessu-animalium",
    "Republic": "plato:republic",
    "Meno": "plato:meno",
    "Theaetetus": "plato:theaetetus",
    "Parmenides": "plato:parmenides",
    "Timaeus": "plato:timaeus",
    "Laws": "plato:laws",
    "Gorgias": "plato:gorgias",
    "Phaedo": "plato:phaedo",
    "Epinomis": "plato:epinomis",
    "Quadrature of the Parabola": "archimedes:quadrature-of-parabola",
    "On the Sphere and Cylinder": "archimedes:sphere-and-cylinder",
    "Sphere and Cylinder": "archimedes:sphere-and-cylinder",
    "On the equilibrium of planes": "archimedes:equilibrium-of-planes",
    "On Conoids and Spheroids": "archimedes:conoids-and-spheroids",
    "On Spirals": "archimedes:spirals",
    "Measurement of a circle": "archimedes:measurement-of-circle",
    "Sand-reckoner": "archimedes:sand-reckoner",
    "Sympos.": "plutarch:symposiaca",
    "Vita Marcelli": "plutarch:vita-marcelli",
    "Eclogae": "stobaeus:eclogae",
}

_CLASSICAL_TITLES_ALT = "|".join(
    re.escape(k) for k in sorted(_CLASSICAL_WORK_MAP, key=lambda x: -len(x))
)

# Matches e.g.:
# *Anal. post.* I. 5, 74 a 17
# *Anal. post.* **II.** 17, 99 a 13
# *Meteorologica* III. 5 (376 b 9)
# *Theaetetus* (147 E—148 B)
# *Timaeus*, 54 D, E
# *Eclogae*, I. 1, 8
_CLASSICAL_LOCUS_RE = re.compile(
    rf"\*({_CLASSICAL_TITLES_ALT})\*(?:,?\s+)("
    r"(?:\*\*[IVXLCDM]+\.\*\*\s*\d+(?:\s*,\s*\d+\s*[ab]\s*\d+(?:[—–-]\d+)?)?)"
    r"|(?:[IVXLCDM]+\.\s*\d+(?:\s*,\s*\d+(?:\s*[ab]\s*\d+(?:[—–-]\d+)?)?|\s*\(\d+\s*[ab]\s*\d+\))?)"
    r"|(?:\(\d+\s*[A-E](?:[—–-]\d+\s*[A-E])?\))"
    r"|(?:\d+\s*[ab]\s*\d+(?:[—–-]\d+(?:\s*[ab]\s*\d+)?)?)"
    r"|(?:\d+\s*[A-E](?:\s*sqq\.|\s*,\s*[A-E]|[—–-]\d+\s*[A-E])?)"
    r"|(?:p\.\s*\d+(?:\s*,\s*\d+)?)"
    r")"
)

# Proclus page/line citations: e.g. "Proclus, p. 185, 6", "Proclus (p. 211, 19)", "Proclus, pp. 301, 21—302, 13"
_PROCLUS_CITE_RE = re.compile(
    r"\b(Proclus(?:\s*\(|\s*,\s*))(pp?\.\s*\d+(?:\s*,\s*\d+)?(?:\s*[—–-]\s*(?:p\.\s*)?\d+(?:\s*,\s*\d+)?)?(?:\s*sqq\.)?)"
)

# Pappus Book/page citations: e.g. "Pappus, VII. p. 672", "Pappus (VII. p. 680)", "Pappus, IV. p. 250, 33"
_PAPPUS_CITE_RE = re.compile(
    r"\b(Pappus(?:\s*\(|\s*,\s*))((?:[IVXLCDM]+\.\s*)?pp?\.\s*\d+(?:\s*,\s*\d+)?(?:\s*[—–-]\s*\d+(?:\s*,\s*\d+)?)?)"
)

# Nicomachus citations: e.g. "Nicomachus, I. 8, 9", "Nicomachus (I. 19, 14)"
_NICOMACHUS_CITE_RE = re.compile(
    r"\b(Nicomachus(?:\s*\(|\s*,\s*))([IVXLCDM]+\.\s*\d+(?:\s*,\s*\d+)*)"
)

# Standalone italicized book / treatise titles
_ITALIC_WORK_CITATIONS: List[Tuple[str, str]] = [
    ("*Zur Geschichte der Mathematik in Alterthum und Mittelalter*", "hankel:zur-geschichte-der-mathematik"),
    ("*A defense of the treatise of the angle of contact*", "wallis:defense-of-angle-of-contact"),
    ("*De angulo contactus et semicirculi tractatus*", "wallis:de-angulo-contactus"),
    ("*Euclid und die sechs planimetrischen Bücher*", "simon:euclid-sechs-planimetrischen"),
    ("*In Platonis Timaeum commentaria*", "proclus:in-platonis-timaeum"),
    ("*Euclides ob omni naevo vindicatus*", "saccheri:euclides-vindicatus"),
    ("*Euclid and his Modern Rivals*", "dodgson:euclid-and-modern-rivals"),
    ("*On the equilibrium of planes*", "archimedes:equilibrium-of-planes"),
    ("*On the Sphere and Cylinder*", "archimedes:sphere-and-cylinder"),
    ("*Mathematisches zu Aristoteles*", "heiberg:mathematisches-zu-aristoteles"),
    ("*The Method of Archimedes*", "heath:method-of-archimedes"),
    ("*The Works of Archimedes*", "heath:works-of-archimedes"),
    ("*Die Algebra der Griechen*", "nesselmann:algebra-der-griechen"),
    ("*Geschichte der Mathematik*", "cantor:geschichte-der-mathematik"),
    ("*Bibliotheca Mathematica*", "enestrom:bibliotheca-mathematica"),
    ("*De institutione musica*", "boethius:de-institutione-musica"),
    ("*Lectiones Cantabrigienses*", "barrow:lectiones-cantabrigienses"),
    ("*Elementi di geometria*", "de-paolis:elementi-di-geometria"),
    ("*Éléments de Géométrie*", "legendre:elements-de-geometrie"),
    ("*De defectu oraculorum*", "plutarch:de-defectu-oraculorum"),
    ("*Lectiones Cantabrig.*", "barrow:lectiones-cantabrigienses"),
    ("*La Géométrie grecque*", "tannery:geometrie-grecque"),
    ("*De doctrina Platonis*", "alkinous:de-doctrina-platonis"),
    ("*Comm. on Nicomachus*", "iamblichus:in-nicomachi-arith"),
    ("*Apollonius of Perga*", "heath:apollonius-of-perga"),
    ("*Liber Assumptorum*", "archimedes:liber-assumptorum"),
    ("*Liber assumptorum*", "archimedes:liber-assumptorum"),
    ("*On Common Notions*", "plutarch:de-communibus-notitiis"),
    ("*Penny Cyclopaedia*", "de-morgan:penny-cyclopaedia"),
    ("*De sectione coni*", "serenus:de-sectione-coni"),
    ("*Gesch. d. Math.*", "cantor:geschichte-der-mathematik"),
    ("*Lect. Cantabr.*", "barrow:lectiones-cantabrigienses"),
    ("*Euklid-studien*", "knoche:euklid-studien"),
    ("*Euclid Revised*", "nixon:euclid-revised"),
    ("*Sectio Canonis*", "euclid:sectio-canonis"),
    ("*Sectio canonis*", "euclid:sectio-canonis"),
    ("*Formal Logic*", "de-morgan:formal-logic"),
    ("*On divisions*", "euclid:on-divisions"),
    ("*Cyclomathia*", "leotaud:cyclomathia"),
    ("*Plane Loci*", "apollonius:plane-loci"),
    ("*Tactiones*", "apollonius:tactiones"),
    ("*Syntaxis*", "ptolemy:syntaxis"),
    ("*Metrica*", "heron:metrica"),
    ("*Dioptra*", "heron:dioptra"),
    ("*Conics*", "apollonius:conics"),
    ("*Data*", "euclid:data"),
]


# ---------------------------------------------------------------------------
# 4. Historical Mathematicians, Commentators & Scholars (:person:)
# ---------------------------------------------------------------------------

_PERSONS_RAW: List[Tuple[str, str]] = [
    # Multi-word historical names first
    ("Theon of Smyrna", "theon-of-smyrna"),
    ("Theon of Alexandria", "theon-of-alexandria"),
    ("Hippocrates of Chios", "hippocrates-of-chios"),
    ("Archytas of Tarentum", "archytas"),
    ("Theodorus of Cyrene", "theodorus-of-cyrene"),
    ("Menaechmus", "menaechmus"),
    ("Dinostratus", "dinostratus"),
    ("Autolycus of Pitane", "autolycus"),
    ("Autolycus", "autolycus"),
    ("Aristaeus the Elder", "aristaeus"),
    ("Aristaeus", "aristaeus"),
    ("Apollonius of Perga", "apollonius"),
    ("Philo of Byzantium", "philo-of-byzantium"),
    ("Eudemus of Rhodes", "eudemus"),
    ("Diogenes Laertius", "diogenes-laertius"),
    ("Martianus Capella", "martianus-capella"),
    ("Maximus Planudes", "maximus-planudes"),
    ("George Pachymeres", "george-pachymeres"),
    ("Barlaam", "barlaam"),
    ("Johannes Pediasimus", "johannes-pediasimus"),
    ("Isaac Argyrus", "isaac-argyrus"),
    ("Thābit b. Qurra", "thabit-ibn-qurra"),
    ("al-Ḥajjāj", "al-hajjaj"),
    ("Isḥāq", "ishaq-ibn-hunayn"),
    ("an-Nairīzī", "an-nairizi"),
    ("Abū 'l-Wafā", "abu-l-wafa"),
    ("Ibn al-Haitham", "ibn-al-haytham"),
    ("Naṣīraddīn aṭ-Ṭūsī", "nasir-al-din-al-tusi"),
    ("Gherard of Cremona", "gerard-of-cremona"),
    ("Adelard of Bath", "adelard-of-bath"),
    ("Leonardo of Pisa", "leonardo-of-pisa"),
    ("Jordanus Nemorarius", "jordanus-nemorarius"),
    ("Campanus", "campanus"),
    ("Regiomontanus", "regiomontanus"),
    ("Lucas Paciuolo", "luca-pacioli"),
    ("Pacioli", "luca-pacioli"),
    ("Zamberti", "bartolomeo-zamberti"),
    ("Commandino", "federico-commandino"),
    ("Billingsley", "henry-billingsley"),
    ("Clavius", "christopher-clavius"),
    ("Peletier", "jacques-peletier"),
    ("Peletarius", "jacques-peletier"),
    ("Candalla", "francois-de-foix-candalle"),
    ("Borelli", "giovanni-alfonso-borelli"),
    ("Tacquet", "andreas-tacquet"),
    ("Savile", "henry-savile"),
    ("John Wallis", "john-wallis"),
    ("Wallis", "john-wallis"),
    ("Isaac Barrow", "isaac-barrow"),
    ("Barrow", "isaac-barrow"),
    ("Gerolamo Saccheri", "girolamo-saccheri"),
    ("Saccheri", "girolamo-saccheri"),
    ("Robert Simson", "robert-simson"),
    ("Simson", "robert-simson"),
    ("Playfair", "john-playfair"),
    ("Todhunter", "isaac-todhunter"),
    ("De Morgan", "augustus-de-morgan"),
    ("Peyrard", "francois-peyrard"),
    ("Camerer", "johann-wilhelm-camerer"),
    ("Heiberg", "johan-ludvig-heiberg"),
    ("Menge", "heinrich-menge"),
    ("Bretschneider", "carl-anton-bretschneider"),
    ("Hankel", "hermann-hankel"),
    ("Cantor", "moritz-cantor"),
    ("Zeuthen", "hieronymus-georg-zeuthen"),
    ("Tannery", "paul-tannery"),
    ("Hultsch", "friedrich-hultsch"),
    ("Allman", "george-johnston-allman"),
    ("Gow", "james-gow"),
    ("Loria", "gino-loria"),
    ("Enriques", "federigo-enriques"),
    ("Veronese", "giuseppe-veronese"),
    ("Ingrami", "giuseppe-ingrami"),
    ("De Paolis", "riccardo-de-paolis"),
    ("Duhamel", "jean-marie-duhamel"),
    ("Stolz", "otto-stolz"),
    ("Max Simon", "max-simon"),
    ("Nesselmann", "georg-heinrich-ferdinand-nesselmann"),
    ("Bürk", "albert-burk"),
    ("vieta", "francois-viete"),
    ("Vieta", "francois-viete"),
    ("Descartes", "rene-descartes"),
    ("Fermat", "pierre-de-fermat"),
    ("Pascal", "blaise-pascal"),
    ("Newton", "isaac-newton"),
    ("Leibniz", "gottfried-wilhelm-leibniz"),
    ("Euler", "leonhard-euler"),
    ("Lagrange", "joseph-louis-lagrange"),
    ("Legendre", "adrien-marie-legendre"),
    ("Gauss", "carl-friedrich-gauss"),
    ("Dedekind", "richard-dedekind"),
    ("Weierstrass", "karl-weierstrass"),
    ("Hilbert", "david-hilbert"),
    ("Ptolemy", "ptolemy"),
    ("Proclus", "proclus"),
    ("Pappus", "pappus"),
    ("Heron", "heron-of-alexandria"),
    ("Archimedes", "archimedes"),
    ("Apollonius", "apollonius"),
    ("Aristotle", "aristotle"),
    ("Plato", "plato"),
    ("Pythagoras", "pythagoras"),
    ("Thales", "thales"),
    ("Eudoxus", "eudoxus"),
    ("Theaetetus", "theaetetus"),
    ("Hippocrates", "hippocrates-of-chios"),
    ("Democritus", "democritus"),
    ("Zeno", "zeno-of-elea"),
    ("Oenopides", "oenopides"),
    ("Archytas", "archytas"),
    ("Theodorus", "theodorus-of-cyrene"),
    ("Eudemus", "eudemus"),
    ("Geminus", "geminus"),
    ("Posidonius", "posidonius"),
    ("Eratosthenes", "eratosthenes"),
    ("Nicomachus", "nicomachus"),
    ("Iamblichus", "iamblichus"),
    ("Boethius", "boethius"),
    ("Simplicius", "simplicius"),
    ("Philoponus", "john-philoponus"),
    ("Eutocius", "eutocius"),
    ("Porphyry", "porphyry"),
    ("Plutarch", "plutarch"),
    ("Psellus", "michael-psellus"),
    ("Stobaeus", "stobaeus"),
    ("Alcinous", "alkinous"),
    ("Moderatus", "moderatus-of-gades"),
    ("Thymaridas", "thymaridas"),
    ("Speusippus", "speusippus"),
    ("Xenocrates", "xenocrates"),
    ("Nicomedes", "nicomedes"),
    ("Diocles", "diocles"),
    ("Perseus", "perseus"),
    ("Zenodorus", "zenodorus"),
    ("Hypsicles", "hypsicles"),
    ("Serenus", "serenus"),
    ("Menelaus", "menelaus"),
    ("Diophantus", "diophantus"),
    ("Anatolius", "anatolius"),
    ("Domninus", "domninus"),
    ("Marinus", "marinus"),
    ("Asclepius", "asclepius-of-tralles"),
    ("Bessarion", "basilios-bessarion"),
    ("Grynäus", "simon-grynaeus"),
    ("viète", "francois-viete"),
    ("Tartaglia", "niccolo-tartaglia"),
    ("Cardan", "gerolamo-cardano"),
    ("Ramus", "petrus-ramus"),
    ("Léotaud", "vincent-leotaud"),
]

_PERSON_MAP: Dict[str, str] = {}
for _pname, _pslug in sorted(_PERSONS_RAW, key=lambda kv: (-len(kv[0]), kv[0])):
    if _pname not in _PERSON_MAP:
        _PERSON_MAP[_pname] = _pslug

_PERSON_PATTERN = re.compile(
    r"(?<![\w`])("
    + "|".join(re.escape(k) for k in _PERSON_MAP)
    + r")(?![\w`])"
)


# ---------------------------------------------------------------------------
# Safe Inline Transformer (Protects existing roles, code, math, links, emphasis)
# ---------------------------------------------------------------------------

_PROTECTED_INLINE_RE = re.compile(
    r"("
    r"``[^`\n]+``"
    r"|:[a-zA-Z0-9_.-]+:`[^`\n]+`"
    r"|`[^`\n]+`_"
    r"|`[^`\n]+`"
    r"|\$\$[\s\S]+?\$\$"
    r"|\$(?!\s)[^$\n]+?(?<!\s)\$"
    r"|\$[A-Za-z0-9]+\$"
    r"|\[#[a-zA-Z0-9_.-]+\]_"
    r"|\[\d+\]_"
    r"|\*\*[^*\n]+\*\*"
    r"|\*[^*\n]+\*"
    r")"
)

_DEFINITION_FILES = (
    "book_iii/definitions/0007.rst",
    "book_iii/definitions/0008.rst",
    "book_iv/definitions/0084.rst",
    "book_v/definitions/0119.rst",
    "book_v/definitions/0120.rst",
    "book_v/definitions/0121.rst",
    "book_vi/definitions/0194.rst",
    "book_vii/definitions/0283.rst",
    "book_vii/definitions/0284.rst",
)


def enrich_line(
    line: str,
    rel_path: str,
    stats: Dict[str, int],
) -> str:
    """Safely enrich a single non-heading, non-directive prose line with :term:, :cite:, and :person:."""
    if not line.strip():
        return line

    # Step A: In definition files, tag Euclid's bolded defined terms
    if any(k in rel_path for k in _DEFINITION_FILES):
        # Handle special case in 0194.rst: "[**2. Reciprocally related figures.** *See note.*]"
        if "[**2. Reciprocally related figures.**" in line:
            line = line.replace(
                "[**2. Reciprocally related figures.**",
                "[**2.** :term:`**Reciprocally related figures.** <reciprocally-related>`",
                1,
            )
            stats["term"] += 1
        elif re.match(r"^\[?\d+\.\s+", line.strip()):
            for bold_str, slug in _BOLD_DEF_TERMS:
                target_role = f":term:`{bold_str} <{slug}>`"
                if bold_str in line and target_role not in line:
                    line, n_sub = re.subn(
                        r"(?<!`)" + re.escape(bold_str) + r"(?!\s*<)",
                        target_role,
                        line,
                        count=1,
                    )
                    stats["term"] += n_sub

    # Step B: Tag Proclus, Pappus, and Nicomachus page/section citations before protecting segments
    def _repl_proclus(m: re.Match) -> str:
        prefix = m.group(1)
        loc_disp = m.group(2)
        num_part = re.sub(r"^pp?\.\s*", "", loc_disp)
        slug = _norm_locus_slug(num_part)
        stats["cite"] += 1
        return f"{prefix}:cite:`{loc_disp} <proclus:in-euclid:{slug}>`"

    if ":cite:`" not in line:
        line = _PROCLUS_CITE_RE.sub(_repl_proclus, line)

    def _repl_pappus(m: re.Match) -> str:
        prefix = m.group(1)
        loc_disp = m.group(2)
        slug = _norm_locus_slug(loc_disp)
        stats["cite"] += 1
        return f"{prefix}:cite:`{loc_disp} <pappus:collectio:{slug}>`"

    if "<pappus:collectio:" not in line:
        line = _PAPPUS_CITE_RE.sub(_repl_pappus, line)

    def _repl_nicomachus(m: re.Match) -> str:
        prefix = m.group(1)
        loc_disp = m.group(2)
        slug = _norm_locus_slug(loc_disp)
        stats["cite"] += 1
        return f"{prefix}:cite:`{loc_disp} <nicomachus:intro-arith:{slug}>`"

    if "<nicomachus:intro-arith:" not in line:
        line = _NICOMACHUS_CITE_RE.sub(_repl_nicomachus, line)

    # Step C: Tag Classical Locus Citations (*Anal. post.* I. 5, 74 a 17, *Theaetetus* 147 D, etc.)
    def _repl_classical_cite(m: re.Match) -> str:
        work_title = m.group(1)
        locus_raw = m.group(2).strip()
        # Normalize bolded Roman numerals inside locus so Docutils role text stays clean
        locus_clean = re.sub(r"\*\*([IVXLCDM]+\.)\*\*", r"\1", locus_raw)
        base_slug = _CLASSICAL_WORK_MAP[work_title]
        loc_slug = _norm_locus_slug(locus_clean)
        stats["cite"] += 1
        return f":cite:`*{work_title}* {locus_clean} <{base_slug}:{loc_slug}>`"

    line = re.sub(
        r"(?<!`)" + _CLASSICAL_LOCUS_RE.pattern,
        _repl_classical_cite,
        line,
    )

    # Step D: Tag standalone italicized treatise titles (*Mathematisches zu Aristoteles*, etc.)
    for it_title, cite_slug in _ITALIC_WORK_CITATIONS:
        role_str = f":cite:`{it_title} <{cite_slug}>`"
        if it_title in line and role_str not in line:
            line = re.sub(
                r"(?<![`*])" + re.escape(it_title) + r"(?![`*<])(?!\s*<)",
                lambda _: (stats.__setitem__("cite", stats["cite"] + 1) or role_str),
                line,
            )

    # Step E: Tag italicized Latin & English technical terms (*ex aequali*, *componendo*, etc.)
    if "indexofgreekwordsandforms" not in rel_path and "englishindex" not in rel_path:
        for it_term, term_slug in _ITALIC_TERMS:
            role_str = f":term:`{it_term} <{term_slug}>`"
            if it_term in line and role_str not in line:
                line = re.sub(
                    r"(?<![`*])" + re.escape(it_term) + r"(?![`*<])(?!\s*<)",
                    lambda _: (stats.__setitem__("term", stats["term"] + 1) or role_str),
                    line,
                )

    # Step F: Split by protected inline spans (roles, literals, math, bold, italic)
    # and apply Greek :term: and historical :person: tagging only to unprotected text segments!
    parts = _PROTECTED_INLINE_RE.split(line)
    for idx in range(0, len(parts), 2):
        seg = parts[idx]
        if not seg:
            continue

        # 1. Greek technical terms -> :term:
        if "indexofgreekwordsandforms" not in rel_path:
            def _repl_greek(m: re.Match) -> str:
                word = m.group(1)
                slug = _GREEK_MAP[word]
                stats["term"] += 1
                return f":term:`{word} <{slug}>`"

            seg = _GREEK_PATTERN.sub(_repl_greek, seg)

        # 2. Historical persons & scholars -> :person:
        if (
            "indexofgreekwordsandforms" not in rel_path
            and "englishindex" not in rel_path
            and "contents_of_volu_me_ii" not in rel_path
        ):
            sub_parts = _PROTECTED_INLINE_RE.split(seg)
            for s_idx in range(0, len(sub_parts), 2):
                s_seg = sub_parts[s_idx]
                if not s_seg:
                    continue

                def _repl_person(m: re.Match) -> str:
                    name = m.group(1)
                    slug = _PERSON_MAP[name]
                    stats["person"] += 1
                    return f":person:`{name} <{slug}>`"

                sub_parts[s_idx] = _PERSON_PATTERN.sub(_repl_person, s_seg)
            seg = "".join(sub_parts)

        parts[idx] = seg

    res_line = "".join(parts)
    # Ensure valid Docutils start/end boundaries around any newly inserted roles
    res_line = re.sub(r"(\.)(:(?:term|cite|person):`)", r"\1 \2", res_line)
    res_line = re.sub(r"(:(?:term|cite|person):`[^`\n]+`)(·)", r"\1 \2", res_line)
    return res_line


def process_folio(rst_path: Path, vol2_dir: Path, stats: Dict[str, int]) -> bool:
    """Process a single Volume II .rst folio file."""
    rel_path = str(rst_path.relative_to(vol2_dir))
    orig_text = rst_path.read_text(encoding="utf-8")
    lines = orig_text.splitlines()

    # 1. Normalize headings first
    lines, h_changed = normalize_headings(lines, rel_path)
    stats["headings_normalized"] += h_changed

    # Identify heading title lines and underline lines so we never tag inside headings
    heading_line_indices = set()
    for i in range(1, len(lines)):
        if _ADORNMENT_RE.match(lines[i].strip()):
            prev = lines[i - 1].strip()
            if prev and not prev.startswith("..") and not prev.startswith(":"):
                heading_line_indices.add(i - 1)
                heading_line_indices.add(i)

    # Identify metadata lines at top of file and directive/code blocks
    out_lines: List[str] = []
    in_code_block = False
    code_indent = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

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
    valid_openers = set(" \t([{\"“‘'—–-/:")
    valid_closers = set(" \t.,;:!?)]}\"”’'—–-/\\")

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
            if pre and pre not in valid_openers:
                warnings.append(f"Line {i}: Invalid char {pre!r} before role {role_tok}")
            if post and post not in valid_closers:
                warnings.append(f"Line {i}: Invalid char {post!r} after role {role_tok}")

    return warnings


def main() -> None:
    vol2_dir = _REPO_ROOT / "resources" / "heath" / "volume_II"
    rst_files = sorted(
        p for p in vol2_dir.rglob("*.rst") if not p.name.endswith(".notes.rst")
    )
    stats = {
        "files_modified": 0,
        "headings_normalized": 0,
        "term": 0,
        "cite": 0,
        "person": 0,
    }

    for rst_p in rst_files:
        if process_folio(rst_p, vol2_dir, stats):
            stats["files_modified"] += 1

    # Count total roles across all 442 folios
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

        # Render with photon_platform.publish.rst_renderer.render_rst_html
        try:
            rendered = render_rst_html(txt)
            if not rendered and txt.strip():
                errors.append((str(rst_p.relative_to(vol2_dir)), "Empty rendered HTML"))
        except Exception as exc:
            errors.append((str(rst_p.relative_to(vol2_dir)), str(exc)))

        w_list = validate_folio_rst_strict(txt)
        if w_list:
            errors.append((str(rst_p.relative_to(vol2_dir)), "; ".join(w_list)))

    print(
        f"Processed {len(rst_files)} folios in volume_II: "
        f"modified={stats['files_modified']}, "
        f"headings_normalized={stats['headings_normalized']}"
    )
    print(f"Heading level distribution across volume_II: {heading_levels}")
    print(f"Total semantic roles in volume_II: {totals}")
    print(f"Validation warnings/errors across {len(rst_files)} files: {len(errors)}")
    for rel, w in errors[:20]:
        print(f"  {rel}: {w}")


if __name__ == "__main__":
    main()
