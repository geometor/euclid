#!/usr/bin/env python3
"""Enrich Volume I (.rst folios) with normalized 4-level headings and :term:, :cite:, and :person: roles."""

from __future__ import annotations

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
# 1. Fixed 4-Level Heading Hierarchy (=, -, ~, ^) for Volume I
# ---------------------------------------------------------------------------

_LEVEL_1_EXACT = {
    "THE THIRTEEN BOOKS OF EUCLID'S ELEMENTS",
    "FRONTISPIECE: BODLEIAN MS. D'ORVILLE 301",
    "PREFACE",
    "PREFACE TO THE SECOND EDITION",
    "CONTENTS",
    "INTRODUCTION.",
    "BOOK I.",
    "BOOK I. PROPOSITIONS.",
    "BOOK II.",
    "BOOK II. PROPOSITIONS.",
    "EXCURSUS I.",
    "EXCURSUS II.",
    "INDEX OF GREEK WORDS AND FORMS.",
    "ENGLISH INDEX.",
    "ENGLISH INDEX",
}

_LEVEL_2_EXACT = {
    "VOLUME I.",
    "DEFINITIONS.",
    "POSTULATES.",
    "COMMON NOTIONS.",
    "AXIOMS OR *COMMON NOTIONS*.",
    "OTHER AXIOMS INTRODUCED AFTER EUCLID'S TIME.",
    "GEOMETRICAL ALGEBRA.",
    "PYTHAGORAS AND THE PYTHAGOREANS.",
    "POPULAR NAMES FOR EUCLIDEAN PROPOSITIONS.",
}

_LEVEL_2_PATTERNS = [
    re.compile(r"^CHAPTER\s+[IVXLCDM]+\.$"),
    re.compile(r"^DEFINITIONS?\s+\d+(?:\s*,\s*\d+)*\.$"),
    re.compile(r"^POSTULATES?\s+\d+(?:\s*,\s*\d+)*\.$"),
    re.compile(r"^COMMON\s+NOTIONS?\s+\d+(?:\s*,\s*\d+)*\.$"),
    re.compile(r"^PROPOSITIONS?\s+\d+(?:\s*,\s*\d+)*\.$"),
]

_LEVEL_4_PATTERNS = [
    # Sub-items under Chapter II ("EUCLID'S OTHER WORKS.") and Chapter VII ("EUCLID IN ARABIA.")
    re.compile(r"^[1-5]\.\s+(?:The\s+\*|\*[A-Z])"),
    # Sub-items under "Notes on classes of “lines” and on particular curves." (0176-0178)
    re.compile(r"^[1-5]\.\s+(?:Homoeomeric|Mixed|Spiric|The cissoid|“Single-turn)"),
    # Sub-items under "Noteworthy attempts to prove the Postulate." (0218-0227)
    re.compile(
        r"^(?:\*\*Ptolemy\.\*\*|Proclus\.|Naṣīraddīn aṭ-Ṭūsī\.|John Wallis\.|Gerolamo Saccheri\.|Lambert\.|Legendre\.)$"
    ),
    # Sub-items under "Intersections of two circles." (0252-0253)
    re.compile(r"^\*(?:Lemma|Proof of theorem)\.\*$"),
    # Sub-items under "Trisection of an angle." (0280-0281)
    re.compile(r"^\([abc]\)\s+"),
]


def classify_heading_char(title: str, rel_path: str) -> str:
    """Return the canonical underline character ('=', '-', '~', '^') for a heading title."""
    t = title.strip()
    if t == "INTRODUCTION." and "contents/" in rel_path:
        return "~"
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
# 2. Defined Terms & Greek Technical Terms (:term:)
# ---------------------------------------------------------------------------

# Explicit bolded defined terms in Book I Definitions (0167, 0168) and Book II Definitions (0384)
_BOLD_DEF_TERMS: List[Tuple[str, str]] = [
    ("**parallel straight lines**", "parallel-straight-lines"),
    ("**equilateral triangle**", "equilateral-triangle"),
    ("**isosceles triangle**", "isosceles-triangle"),
    ("**scalene triangle**", "scalene-triangle"),
    ("**right-angled triangle**", "right-angled-triangle"),
    ("**obtuse-angled triangle**", "obtuse-angled-triangle"),
    ("**acute-angled triangle**", "acute-angled-triangle"),
    ("**Rectilineal figures**", "rectilineal-figure"),
    ("**rectilineal figures**", "rectilineal-figure"),
    ("**trilateral figures**", "trilateral"),
    ("**plane surface**", "plane-surface"),
    ("**straight line**", "straight-line"),
    ("**plane angle**", "plane-angle"),
    ("**obtuse angle**", "obtuse-angle"),
    ("**acute angle**", "acute-angle"),
    ("**perpendicular**", "perpendicular"),
    ("**quadrilateral**", "quadrilateral"),
    ("**multilateral**", "multilateral"),
    ("**rectilineal**", "rectilineal-angle"),
    ("**extremities**", "extremity"),
    ("**semicircle**", "semicircle"),
    ("**contained**", "contained-rectangle"),
    ("**boundary**", "boundary"),
    ("**diameter**", "diameter"),
    ("**Parallel**", "parallel-straight-lines"),
    ("**rhomboid**", "rhomboid"),
    ("**trapezia**", "trapezium"),
    ("**surface**", "surface"),
    ("**rhombus**", "rhombus"),
    ("**figure**", "figure"),
    ("**circle**", "circle"),
    ("**centre**", "centre"),
    ("**square**", "square"),
    ("**oblong**", "oblong"),
    ("**gnomon**", "gnomon"),
    ("**point**", "point"),
    ("**right**", "right-angle"),
    ("**line**", "line"),
]

# Greek technical phrases & terms (sorted longest-first at compile time)
_GREEK_TERMS_RAW: List[Tuple[str, str]] = [
    ("ὅπερ ἔδει δεῖξαι", "hoper-edei-deixai"),
    ("ὅπερ ἔδει ποιῆσαι", "hoper-edei-poiesai"),
    ("παραβολὴ τῶν χωρίων", "parabole-ton-chorion"),
    ("τόπος ἀναλυόμενος", "topos-analyomenos"),
    ("παράδοξος τόπος", "paradoxos-topos"),
    ("εἰς τὸ ἀδύνατον", "eis-to-adynaton"),
    ("ἡ εἰς τὸ ἀδύνατον ἀπαγωγή", "apagoge-eis-to-adynaton"),
    ("κοιναὶ ἔννοιαι", "koinai-ennoiai"),
    ("κοιναὶ δόξαι", "koinai-doxai"),
    ("ἐπίπεδος ἐπιφάνεια", "epipedos-epiphaneia"),
    ("κάθετος εὐθεῖα γραμμή", "kathetos"),
    ("εὐθεῖα γραμμή", "eutheia-gramme"),
    ("μονόστροφος ἕλιξ", "monostrophos-helix"),
    ("μονὰς προσλαβοῦσα θέσιν", "monas-proslabousa-thesin"),
    ("πέρας συγκλεῖον", "peras-synkleion"),
    ("τοπικὸν θεώρημα", "topikon-theorema"),
    ("γαμήλιον διάγραμμα", "gamelion-diagramma"),
    ("θεώρημα τῆς νύμφης", "theorema-tes-nymphes"),
    ("ἵππου πέδη", "hippou-pede"),
    ("ἄτομοι γραμμαί", "atomoi-grammai"),
    ("σημεῖον", "semeion"),
    ("Σημεῖόν", "semeion"),
    ("στιγμή", "stigme"),
    ("γραμμή", "gramme"),
    ("γραμμῆς", "gramme"),
    ("γραμμὴν", "gramme"),
    ("γραμμαί", "gramme"),
    ("γραμμῶν", "gramme"),
    ("εὐθεῖα", "eutheia-gramme"),
    ("εὐθεῖαι", "eutheia-gramme"),
    ("εὐθειῶν", "eutheia-gramme"),
    ("ἐπιφάνεια", "epiphaneia"),
    ("ἐπιφανείας", "epiphaneia"),
    ("ἐπιφάνειαι", "epiphaneia"),
    ("ἐπίπεδον", "epipedon"),
    ("ἐπιπέδου", "epipedon"),
    ("γωνία", "gonia"),
    ("γωνίας", "gonia"),
    ("γωνίαν", "gonia"),
    ("γωνίαι", "gonia"),
    ("ἀμβλεῖα", "ambleia"),
    ("ὀξεῖα", "oxeia"),
    ("κάθετος", "kathetos"),
    ("πέρας", "peras"),
    ("πέρατα", "peras"),
    ("σχῆμα", "schema"),
    ("σχήματος", "schema"),
    ("σχήματα", "schema"),
    ("κύκλος", "kyklos"),
    ("κύκλου", "kyklos"),
    ("κέντρον", "kentron"),
    ("κέντρου", "kentron"),
    ("διάμετρος", "diametros"),
    ("διαμέτρου", "diametros"),
    ("διάμετρον", "diametros"),
    ("περιφέρεια", "periphereia"),
    ("περιφερείας", "periphereia"),
    ("ἡμικύκλιον", "hemikyklion"),
    ("τρίπλευρον", "tripleuron"),
    ("τρίπλευρα", "tripleuron"),
    ("τετράπλευρον", "tetrapleuron"),
    ("τετράπλευρα", "tetrapleuron"),
    ("πολύπλευρον", "polypleuron"),
    ("πολύπλευρα", "polypleuron"),
    ("ἰσόπλευρον", "isopleuron"),
    ("ἰσοσκελές", "isoskeles"),
    ("σκαληνόν", "skalenon"),
    ("ὀρθογώνιον", "orthogonion"),
    ("ὀρθογώνιος", "orthogonion"),
    ("ἀμβλυγώνιον", "amblygonion"),
    ("ἀμβλυγώνιος", "amblygonion"),
    ("ὀξυγώνιον", "oxygonion"),
    ("ὀξυγώνιος", "oxygonion"),
    ("τετράγωνον", "tetragonon"),
    ("ἑτερόμηκες", "heteromekes"),
    ("ῥόμβος", "rhombos"),
    ("ῥομβοειδές", "rhomboeides"),
    ("τραπέζιον", "trapezion"),
    ("τραπέζια", "trapezion"),
    ("παράλληλοι", "paralleloi"),
    ("παραλληλόγραμμον", "parallelogrammon"),
    ("παραλληλογράμμου", "parallelogrammon"),
    ("παραπλήρωμα", "parapleroma"),
    ("παραπληρώμασι", "parapleroma"),
    ("παραπληρώματα", "parapleroma"),
    ("γνώμων", "gnomon"),
    ("γνώμονος", "gnomon"),
    ("ὁρισμός", "horos"),
    ("ὁρισμοί", "horos"),
    ("ὅρος", "horos"),
    ("ὅροι", "horos"),
    ("αἴτημα", "aitema"),
    ("αἰτήματα", "aitema"),
    ("αἰτημάτων", "aitema"),
    ("ἀξίωμα", "axioma"),
    ("ἀξιώματα", "axioma"),
    ("ἀξιωμάτων", "axioma"),
    ("ὑπόθεσις", "hypothesis"),
    ("ὑποθέσεις", "hypothesis"),
    ("πρότασις", "protasis"),
    ("ἔκθεσις", "ekthesis"),
    ("διορισμός", "diorismos"),
    ("διορισμοί", "diorismos"),
    ("κατασκευή", "kataskeue"),
    ("ἀπόδειξις", "apodeixis"),
    ("συμπέρασμα", "symperasma"),
    ("πόρισμα", "porisma"),
    ("πορίσματα", "porisma"),
    ("λῆμμα", "lemma"),
    ("λήμματα", "lemma"),
    ("πτῶσις", "ptosis"),
    ("πτώσεις", "ptosis"),
    ("ἔνστασις", "enstasis"),
    ("ἀπαγωγή", "apagoge"),
    ("ἀντιστροφή", "antistrophe"),
    ("νεύσεις", "neuseis"),
    ("νεῦσις", "neuseis"),
    ("παραβολή", "parabole"),
    ("ὑπερβολή", "hyperbole"),
    ("ἔλλειψις", "elleipsis"),
    ("ἐφαρμόζειν", "epharmozein"),
    ("ἐφαρμόζεσθαι", "epharmozein"),
    ("κερατοειδής", "keratoeides"),
    ("μηνοειδής", "menoeides"),
    ("μηνοειδές", "menoeides"),
    ("ὁμοιομερής", "homoiomeres"),
    ("ὁμοιομερεῖς", "homoiomeres"),
    ("ἀνομοιομερής", "anomoiomeres"),
    ("ἀσύμπτωτος", "asymptotos"),
    ("ἀσύμπτωτοι", "asymptotos"),
    ("ἀσσύμμετρος", "asymmetros"),
    ("ἀσύμμετρος", "asymmetros"),
    ("ἄλογος", "alogos"),
    ("ἄλογοι", "alogos"),
    ("ῥητός", "rhetos"),
    ("ἄρρητος", "arrhetos"),
    ("στοιχεῖον", "stoicheion"),
    ("στοιχεῖα", "stoicheion"),
    ("θεώρημα", "theorema"),
    ("θεωρήματα", "theorema"),
    ("πρόβλημα", "problema"),
    ("προβλήματα", "problema"),
    ("διάστημα", "diastema"),
    ("διαστάσεις", "diastaseis"),
    ("μῆκος", "mekos"),
    ("πλάτος", "platos"),
    ("βάθος", "bathos"),
    ("κλίσις", "klisis"),
    ("κορυφή", "koryphe"),
    ("βάσις", "basis"),
    ("τομή", "tome"),
    ("τόπος", "topos"),
    ("τόποι", "topos"),
    ("τετραγωνισμός", "tetragonismos"),
]

_GREEK_TERMS = sorted(_GREEK_TERMS_RAW, key=lambda x: len(x[0]), reverse=True)
_GREEK_MAP: Dict[str, str] = {k: v for k, v in _GREEK_TERMS}
_GREEK_PATTERN = re.compile(
    r"(?<![\w\u0370-\u03ff\u1f00-\u1fff*`])("
    + "|".join(re.escape(k) for k, _ in _GREEK_TERMS)
    + r")(?![\w\u0370-\u03ff\u1f00-\u1fff*`])"
)


# ---------------------------------------------------------------------------
# 3. Bibliographic & Classical Locus Citations (:cite:)
# ---------------------------------------------------------------------------

# Italicized treatise titles -> canonical author:work slug
_ITALIC_WORK_CITATIONS: List[Tuple[str, str]] = [
    ("*Euclid und die sechs planimetrischen Bücher*", "simon:euclid-1901"),
    ("*Die Theorie der Parallellinien von Euklid bis auf Gauss*", "staeckel-engel:parallellinien"),
    ("*Die Mathematiker und Astronomen der Araber und ihre Werke*", "suter:mathematiker-araber"),
    ("*Zur Geschichte der Mathematik im Alterthum und Mittelalter*", "hankel:geschichte"),
    ("*Die Geometrie und die Geometer vor Euklides*", "bretschneider:geometrie"),
    ("*Die Lehre von den Kegelschnitten im Altertum*", "zeuthen:kegelschnitte"),
    ("*Questioni riguardanti la geometria elementare*", "enriques:questioni"),
    ("*Vorlesungen über Geschichte der Mathematik*", "cantor:vorlesungen"),
    ("*Vorlesungen über Gesch. d. Math.*", "cantor:vorlesungen"),
    ("*Litterargeschichtliche Studien über Euklid*", "heiberg:studien"),
    ("*Greek Geometry from Thales to Euclid*", "allman:greek-geometry"),
    ("*Le scienze esatte nell' antica Grecia*", "loria:scienze-esatte"),
    ("*A Short History of Greek Mathematics*", "gow:short-history"),
    ("*Euclides ab omni naevo vindicatus*", "saccheri:euclides"),
    ("*Vorlesungen über neuere Geometrie*", "pasch:neuere-geometrie"),
    ("*The Principles of Mathematics*", "russell:principles"),
    ("*Theorie der Parallellinien*", "lambert:parallellinien"),
    ("*Grundlagen der Geometrie*", "hilbert:grundlagen"),
    ("*Grundzüge der Geometrie*", "veronese:grundzuege"),
    ("*La Geometria non-euclidea*", "bonola:non-euclidea"),
    ("*La Géométrie grecque*", "tannery:geometrie-grecque"),
    ("*Éléments de Géométrie*", "legendre:elements"),
    ("*Elemente der Geometrie*", "legendre:elements"),
    ("*Synagoge*", "pappus:synagoge"),
    ("*Fihrist*", "ibn-al-nadim:fihrist"),
]

# Classical work + locus regexes (Aristotle, Plato)
_ARISTOTLE_WORKS = {
    "Metaph.": "aristotle:met",
    "Anal. Post.": "aristotle:anal-post",
    "Anal. post.": "aristotle:anal-post",
    "Anal. Prior.": "aristotle:anal-prior",
    "Anal. prior.": "aristotle:anal-prior",
    "Topics": "aristotle:topics",
    "Top.": "aristotle:topics",
    "Phys.": "aristotle:phys",
    "Physics": "aristotle:phys",
    "De caelo": "aristotle:de-caelo",
    "De Caelo": "aristotle:de-caelo",
    "De anima": "aristotle:de-anima",
    "De Anima": "aristotle:de-anima",
    "Eth. Nic.": "aristotle:eth-nic",
    "Soph. El.": "aristotle:soph-el",
    "Meteor.": "aristotle:meteor",
    "De lin. insec.": "aristotle:de-lin-insec",
    "Mechanica": "aristotle:mech",
}

_PLATO_WORKS = {
    "Republic": "plato:rep",
    "Meno": "plato:meno",
    "Theaetetus": "plato:theaet",
    "Timaeus": "plato:tim",
    "Laws": "plato:laws",
    "Parmenides": "plato:parm",
    "Phaedo": "plato:phaedo",
    "Gorgias": "plato:gorgias",
    "Euthydemus": "plato:euthydemus",
}

_CLASSICAL_WORK_NAMES = sorted(
    list(_ARISTOTLE_WORKS.keys()) + list(_PLATO_WORKS.keys()),
    key=len,
    reverse=True,
)
_CLASSICAL_WORK_MAP = {**_ARISTOTLE_WORKS, **_PLATO_WORKS}

# Matches e.g. `*Metaph.* 1035 b 32` or `*Anal. Post.* I. 10, 76 a 31–77 a 4` or `*Republic* VII. 526 C`
_CLASSICAL_LOCUS_RE = re.compile(
    r"(?<![\w*`])\*("
    + "|".join(re.escape(w) for w in _CLASSICAL_WORK_NAMES)
    + r")\*[ \t]+"
    r"("
    r"(?:[IVXLCDM]+\.\s*\d+(?:\s*,\s*)?)?"
    r"\d{1,4}\s*[abABcCdDeE]?(?:\s*\d{1,2})?"
    r"(?:\s*[–—-]\s*(?:\d{1,4}\s*)?[abABcCdDeE]?\s*\d{0,2})?"
    r")(?=[.,;:!?)\]}\"”’\s]|$)"
)

# Proclus page/line citations after "Proclus, " or "Proclus ("
_PROCLUS_CITE_RE = re.compile(
    r"(Proclus(?:,\s*|\s+\())(pp?\.\s*\d+(?:\s*,\s*\d+)?(?:\s*[–—-]+\s*\d+(?:\s*,\s*\d+)?)?)"
)


def _norm_locus_slug(raw_locus: str) -> str:
    s = re.sub(r"[–—]+", "-", raw_locus.strip())
    s = re.sub(r"\s*,\s*", ".", s)
    s = re.sub(r"\.\s+", ".", s)
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[^A-Za-z0-9._-]+", "", s)
    return s.strip(".")


# ---------------------------------------------------------------------------
# 4. Historical Mathematicians, Philosophers, Commentators & Scholars (:person:)
# ---------------------------------------------------------------------------

_PERSONS_RAW: List[Tuple[str, str]] = [
    # Multi-word names first
    ("Hippocrates of Chios", "hippocrates-of-chios"),
    ("Theon of Alexandria", "theon-of-alexandria"),
    ("Theon of Smyrna", "theon-of-smyrna"),
    ("Diogenes Laertius", "diogenes-laertius"),
    ("Martianus Capella", "martianus-capella"),
    ("Naṣīraddīn aṭ-Ṭūsī", "nasiraddin-at-tusi"),
    ("Naṣīraddīn at-Ṭūsī", "nasiraddin-at-tusi"),
    ("Isḥāq b. Ḥunain", "ishaq-ibn-hunain"),
    ("Thābit b. Qurra", "thabit-ibn-qurra"),
    ("Ibn al-Haitham", "ibn-al-haitham"),
    ("Omar Khayyām", "omar-khayyam"),
    ("Adelard of Bath", "adelard-of-bath"),
    ("Gherard of Cremona", "gherard-of-cremona"),
    ("Leonardo of Pisa", "fibonacci"),
    ("Jordanus Nemorarius", "jordanus-nemorarius"),
    ("Roger Bacon", "roger-bacon"),
    ("Luca Pacioli", "pacioli"),
    ("John Wallis", "wallis"),
    ("Gerolamo Saccheri", "saccheri"),
    ("Max Simon", "max-simon"),
    ("De Morgan", "de-morgan"),
    ("W. Bolyai", "wolfgang-bolyai"),
    ("J. Bolyai", "janos-bolyai"),
    # Ancient
    ("Euclid", "euclid"),
    ("Plato", "plato"),
    ("Aristotle", "aristotle"),
    ("Proclus", "proclus"),
    ("Pappus", "pappus"),
    ("Archimedes", "archimedes"),
    ("Apollonius", "apollonius"),
    ("Pythagoras", "pythagoras"),
    ("Thales", "thales"),
    ("Eudoxus", "eudoxus"),
    ("Theaetetus", "theaetetus"),
    ("Hippocrates", "hippocrates-of-chios"),
    ("Archytas", "archytas"),
    ("Menaechmus", "menaechmus"),
    ("Dinostratus", "dinostratus"),
    ("Eudemus", "eudemus"),
    ("Theophrastus", "theophrastus"),
    ("Autolycus", "autolycus"),
    ("Aristaeus", "aristaeus"),
    ("Conon", "conon"),
    ("Eratosthenes", "eratosthenes"),
    ("Posidonius", "posidonius"),
    ("Geminus", "geminus"),
    ("Heron", "heron"),
    ("Ptolemy", "ptolemy"),
    ("Menelaus", "menelaus"),
    ("Nicomachus", "nicomachus"),
    ("Diophantus", "diophantus"),
    ("Theon", "theon-of-alexandria"),
    ("Hypatia", "hypatia"),
    ("Simplicius", "simplicius"),
    ("Philoponus", "philoponus"),
    ("Eutocius", "eutocius"),
    ("Marinus", "marinus"),
    ("Zeno", "zeno"),
    ("Democritus", "democritus"),
    ("Xenocrates", "xenocrates"),
    ("Speusippus", "speusippus"),
    ("Oenopides", "oenopides"),
    ("Zenodorus", "zenodorus"),
    ("Serenus", "serenus"),
    ("Porphyry", "porphyry"),
    ("Iamblichus", "iamblichus"),
    ("Plutarch", "plutarch"),
    ("Vitruvius", "vitruvius"),
    ("Cicero", "cicero"),
    ("Boethius", "boethius"),
    ("Cassiodorus", "cassiodorus"),
    ("Stobaeus", "stobaeus"),
    ("Suidas", "suidas"),
    ("Anaximander", "anaximander"),
    ("Herodotus", "herodotus"),
    ("Carpus", "carpus"),
    ("Cleonides", "cleonides"),
    ("Aganis", "aganis"),
    # Medieval Arabic / Latin / Renaissance
    ("an-Nairīzī", "an-nairizi"),
    ("Nairīzī", "an-nairizi"),
    ("al-Ḥajjāj", "al-hajjaj"),
    ("Isḥāq", "ishaq-ibn-hunain"),
    ("Alhazen", "ibn-al-haitham"),
    ("Naṣīraddīn", "nasiraddin-at-tusi"),
    ("al-Kindī", "al-kindi"),
    ("al-Fārābī", "al-farabi"),
    ("al-Bīrūnī", "al-biruni"),
    ("Gerbert", "gerbert"),
    ("Adelard", "adelard-of-bath"),
    ("Fibonacci", "fibonacci"),
    ("Campanus", "campanus"),
    ("Regiomontanus", "regiomontanus"),
    ("Pacioli", "pacioli"),
    ("Zamberti", "zamberti"),
    ("Tartaglia", "tartaglia"),
    ("Cardan", "cardano"),
    ("Ramus", "ramus"),
    ("Commandino", "commandino"),
    ("Billingsley", "billingsley"),
    ("Clavius", "clavius"),
    ("Cataldi", "cataldi"),
    ("Borelli", "borelli"),
    ("Savile", "savile"),
    ("Wallis", "wallis"),
    ("Barrow", "barrow"),
    # Modern Geometers, Mathematicians & Historian-Editors
    ("Simson", "simson"),
    ("Playfair", "playfair"),
    ("Saccheri", "saccheri"),
    ("Lambert", "lambert"),
    ("Lagrange", "lagrange"),
    ("Laplace", "laplace"),
    ("Fourier", "fourier"),
    ("Legendre", "legendre"),
    ("Carnot", "carnot"),
    ("Poncelet", "poncelet"),
    ("Chasles", "chasles"),
    ("Thibaut", "thibaut"),
    ("Gauss", "gauss"),
    ("Schweikart", "schweikart"),
    ("Taurinus", "taurinus"),
    ("Lobachewsky", "lobachevsky"),
    ("Bolyai", "bolyai"),
    ("Riemann", "riemann"),
    ("Helmholtz", "helmholtz"),
    ("Beltrami", "beltrami"),
    ("Hoüel", "houel"),
    ("Cayley", "cayley"),
    ("Klein", "klein"),
    ("Poincaré", "poincare"),
    ("Grassmann", "grassmann"),
    ("Todhunter", "todhunter"),
    ("Dodgson", "dodgson"),
    ("Henrici", "henrici"),
    ("Pasch", "pasch"),
    ("Pieri", "pieri"),
    ("Peano", "peano"),
    ("Veronese", "veronese"),
    ("Ingrami", "ingrami"),
    ("Hilbert", "hilbert"),
    ("Enriques", "enriques"),
    ("Amaldi", "amaldi"),
    ("Bonola", "bonola"),
    ("Stäckel", "staeckel"),
    ("Killing", "killing"),
    ("Schur", "schur"),
    ("Dehn", "dehn"),
    ("Veblen", "veblen"),
    ("Russell", "russell"),
    ("Whitehead", "whitehead"),
    ("Dedekind", "dedekind"),
    ("Weierstrass", "weierstrass"),
    ("Peyrard", "peyrard"),
    ("Camérer", "camerer"),
    ("Heiberg", "heiberg"),
    ("Menge", "menge"),
    ("Friedlein", "friedlein"),
    ("Hultsch", "hultsch"),
    ("Schöne", "schoene"),
    ("Besthorn", "besthorn"),
    ("Curtze", "curtze"),
    ("Bonitz", "bonitz"),
    ("Waitz", "waitz"),
    ("Zeller", "zeller"),
    ("Cantor", "cantor"),
    ("Hankel", "hankel"),
    ("Bretschneider", "bretschneider"),
    ("Allman", "allman"),
    ("Gow", "gow"),
    ("Zeuthen", "zeuthen"),
    ("Tannery", "tannery"),
    ("Loria", "loria"),
    ("Suter", "suter"),
    ("Steinschneider", "steinschneider"),
    ("Woepcke", "woepcke"),
    ("Klamroth", "klamroth"),
]

_PERSONS = sorted(_PERSONS_RAW, key=lambda x: len(x[0]), reverse=True)
_PERSON_MAP: Dict[str, str] = {k: v for k, v in _PERSONS}
_PERSON_PATTERN = re.compile(
    r"(?<![\w\u0370-\u03ff\u1f00-\u1fff*`-])("
    + "|".join(re.escape(k) for k, _ in _PERSONS)
    + r")(?![\w\u0370-\u03ff\u1f00-\u1fff*`'-]|’s|'s)"
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


def enrich_line(
    line: str,
    rel_path: str,
    stats: Dict[str, int],
) -> str:
    """Safely enrich a single non-heading, non-directive prose line with :term:, :cite:, and :person:."""
    if not line.strip():
        return line

    # Step A: In definition files (0167.rst, 0168.rst, 0384.rst), tag Euclid's bolded defined terms
    if any(k in rel_path for k in ("book_i/definitions/0167.rst", "book_i/postulates/0168.rst", "book_ii/definitions/0384.rst")):
        if re.match(r"^\d+\.\s+", line.strip()):
            for bold_str, slug in _BOLD_DEF_TERMS:
                target_role = f":term:`{bold_str} <{slug}>`"
                if bold_str in line and target_role not in line:
                    line = line.replace(bold_str, target_role, 1)
                    stats["term"] += 1

    # Step B: Tag Proclus page/line citations before protecting segments
    def _repl_proclus(m: re.Match) -> str:
        prefix = m.group(1)
        loc_disp = m.group(2)
        num_part = re.sub(r"^pp?\.\s*", "", loc_disp)
        slug = _norm_locus_slug(num_part)
        stats["cite"] += 1
        return f"{prefix}:cite:`{loc_disp} <proclus:in-euclid:{slug}>`"

    line = _PROCLUS_CITE_RE.sub(_repl_proclus, line)

    # Step C: Tag Classical Locus Citations (*Metaph.* 1035 b 32, *Topics* VI. 4, 141 b 20, etc.)
    def _repl_classical_cite(m: re.Match) -> str:
        work_title = m.group(1)
        locus = m.group(2).strip()
        base_slug = _CLASSICAL_WORK_MAP[work_title]
        loc_slug = _norm_locus_slug(locus)
        stats["cite"] += 1
        return f":cite:`*{work_title}* {locus} <{base_slug}:{loc_slug}>`"

    line = _CLASSICAL_LOCUS_RE.sub(_repl_classical_cite, line)

    # Step D: Tag standalone italicized treatise titles (*Grundlagen der Geometrie*, etc.)
    for it_title, cite_slug in _ITALIC_WORK_CITATIONS:
        role_str = f":cite:`{it_title} <{cite_slug}>`"
        if it_title in line and role_str not in line:
            # Make sure it_title is not already inside a role
            line = re.sub(
                r"(?<!`)" + re.escape(it_title) + r"(?!\s*<)",
                lambda _: (stats.__setitem__("cite", stats["cite"] + 1) or role_str),
                line,
            )

    # Step E: Split by protected inline spans (roles, literals, math, bold, italic)
    # and apply Greek :term: and historical :person: tagging only to unprotected text segments!
    parts = _PROTECTED_INLINE_RE.split(line)
    for idx in range(0, len(parts), 2):
        seg = parts[idx]
        if not seg:
            continue

        # 1. Greek technical terms -> :term:
        if "index_of_greek_words_and_forms" not in rel_path:
            def _repl_greek(m: re.Match) -> str:
                word = m.group(1)
                slug = _GREEK_MAP[word]
                stats["term"] += 1
                return f":term:`{word} <{slug}>`"

            seg = _GREEK_PATTERN.sub(_repl_greek, seg)

        # 2. Historical persons & scholars -> :person:
        if "index_of_greek_words_and_forms" not in rel_path and "english_index" not in rel_path and "contents/" not in rel_path:
            # Re-split seg so newly created :term:`...` spans are protected
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


def process_folio(rst_path: Path, vol1_dir: Path, stats: Dict[str, int]) -> bool:
    """Process a single Volume I .rst folio file."""
    rel_path = str(rst_path.relative_to(vol1_dir))
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
    vol1_dir = _REPO_ROOT / "resources" / "heath" / "volume_I"
    rst_files = sorted(
        p for p in vol1_dir.rglob("*.rst") if not p.name.endswith(".notes.rst")
    )
    stats = {
        "files_modified": 0,
        "headings_normalized": 0,
        "term": 0,
        "cite": 0,
        "person": 0,
    }

    for rst_p in rst_files:
        if process_folio(rst_p, vol1_dir, stats):
            stats["files_modified"] += 1

    # Count total roles across all 446 folios
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
                errors.append((str(rst_p.relative_to(vol1_dir)), "Empty rendered HTML"))
        except Exception as exc:
            errors.append((str(rst_p.relative_to(vol1_dir)), str(exc)))

        w_list = validate_folio_rst_strict(txt)
        if w_list:
            errors.append((str(rst_p.relative_to(vol1_dir)), "; ".join(w_list)))

    print(
        f"Processed {len(rst_files)} folios in volume_I: "
        f"modified={stats['files_modified']}, "
        f"headings_normalized={stats['headings_normalized']}"
    )
    print(f"Heading level distribution across volume_I: {heading_levels}")
    print(f"Total semantic roles in volume_I: {totals}")
    print(f"Validation warnings/errors across {len(rst_files)} files: {len(errors)}")
    for rel, w in errors[:20]:
        print(f"  {rel}: {w}")


if __name__ == "__main__":
    main()

