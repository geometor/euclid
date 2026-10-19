#!/usr/bin/env python3
"""Normalize :cite:, :term:, and :person: keys across all 3 volumes of Heath's Euclid
and generate the master scholarly apparatus registries:
  - resources/heath/citations.json
  - resources/heath/glossary.json
  - resources/heath/persons.json
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

EDITION_ROOT = Path("/home/phi/PROJECTS/geometor/euclid/resources/heath")
VOLUMES = ["volume_I", "volume_II", "volume_III"]

# ---------------------------------------------------------------------------
# 1. Person Normalization & Prosopographical Catalog
# ---------------------------------------------------------------------------

PERSON_ALIAS_MAP: Dict[str, str] = {
    "adrien-marie-legendre": "legendre",
    "augustus-de-morgan": "de-morgan",
    "carl-anton-bretschneider": "bretschneider",
    "christopher-clavius": "clavius",
    "federico-commandino": "commandino",
    "federigo-enriques": "enriques",
    "francois-viete": "vieta",
    "georg-heinrich-ferdinand-nesselmann": "nesselmann",
    "gino-loria": "loria",
    "giovanni-alfonso-borelli": "borelli",
    "girolamo-saccheri": "saccheri",
    "giuseppe-ingrami": "ingrami",
    "giuseppe-veronese": "veronese",
    "henry-billingsley": "billingsley",
    "henry-savile": "savile",
    "hermann-hankel": "hankel",
    "heron-of-alexandria": "heron",
    "hieronymus-georg-zeuthen": "zeuthen",
    "isaac-barrow": "barrow",
    "isaac-todhunter": "todhunter",
    "johan-ludvig-heiberg": "heiberg",
    "john-philoponus": "philoponus",
    "john-playfair": "playfair",
    "john-wallis": "wallis",
    "karl-weierstrass": "weierstrass",
    "leonhard-euler": "euler",
    "moritz-cantor": "cantor",
    "nasir-al-din-al-tusi": "nasiraddin",
    "nasiraddin-at-tusi": "nasiraddin",
    "niccolo-tartaglia": "tartaglia",
    "paul-tannery": "tannery",
    "petrus-ramus": "ramus",
    "pierre-de-fermat": "fermat",
    "richard-dedekind": "dedekind",
    "robert-simson": "simson",
    "hippocrates": "hippocrates-of-chios",
    "theon": "theon-of-alexandria",
    "max-simon": "simon",
    "wolfgang-bolyai": "farkas-bolyai",
    "janos-bolyai": "bolyai",
}

PERSON_CATALOG: Dict[str, Dict[str, Any]] = {
    "euclid": {
        "name": "Euclid of Alexandria",
        "dates": "fl. c. 300 BC",
        "role": "Alexandrian Geometer; Author of the Elements",
        "bio": "Compiled and systematized the Thirteen Books of the Elements at Alexandria under Ptolemy I Soter, integrating the discoveries of the Pythagoreans, Hippocrates of Chios, Eudoxus of Cnidus, and Theaetetus of Athens into a rigorous deductive canon.",
        "works": ["Elements (Στοιχεῖα)", "Data", "Porisms", "On Divisions of Figures", "Optics", "Phaenomena"],
    },
    "plato": {
        "name": "Plato",
        "dates": "428/427 – 348/347 BC",
        "role": "Founder of the Athenian Academy",
        "bio": "Placed geometry at the threshold of philosophical education and dialectical ascent (Republic VI–VII, Meno, Theaetetus, Timaeus); associated the five regular polyhedra with the cosmic elements.",
        "works": ["Republic", "Meno", "Theaetetus", "Timaeus", "Parmenides", "Laws"],
    },
    "aristotle": {
        "name": "Aristotle of Stagira",
        "dates": "384 – 322 BC",
        "role": "Founder of the Peripatetic School",
        "bio": "Codified the logic of demonstrative science (Analytica Posteriora), distinguishing definitions, hypotheses, postulates, and common axioms, and preserving key pre-Euclidean geometric proofs and definitions.",
        "works": ["Analytica Posteriora", "Analytica Priora", "Metaphysica", "Physica", "De Caelo", "De Anima", "Topics"],
    },
    "proclus": {
        "name": "Proclus Lycius Diadochus",
        "dates": "412 – 485 AD",
        "role": "Neoplatonic Philosopher & Commentator on Euclid Book I",
        "bio": "Head of the Athenian Academy whose Commentary on Book I of Euclid's Elements preserves the Eudemian Summary of early Greek geometry alongside the critiques and alternative proofs of Geminus, Posidonius, Heron, Ptolemy, and Pappus.",
        "works": ["In Primum Euclidis Elementorum Librum Commentarii (ed. Friedlein, 1873)"],
    },
    "pappus": {
        "name": "Pappus of Alexandria",
        "dates": "fl. c. 320 AD",
        "role": "Alexandrian Geometer & Commentator",
        "bio": "Author of the Mathematical Collection (Synagoge) and a commentary on Euclid Book X (surviving in Arabic), preserving the Treasury of Analysis and advanced lemmas on projective and solid geometry.",
        "works": ["Mathematical Collection (Συναγωγή, ed. Hultsch)", "Commentary on Euclid's Elements Book X"],
    },
    "archimedes": {
        "name": "Archimedes of Syracuse",
        "dates": "c. 287 – 212 BC",
        "role": "Greek Geometer, Physicist & Engineer",
        "bio": "Perfected Eudoxus's method of exhaustion and mechanical heuristic discovery to determine areas, volumes, and centers of gravity of curvilinear and solid figures.",
        "works": ["On the Sphere and Cylinder", "Measurement of a Circle", "On Conoids and Spheroids", "On Spirals", "Quadrature of the Parabola", "The Method"],
    },
    "apollonius": {
        "name": "Apollonius of Perga",
        "dates": "c. 240 – c. 190 BC",
        "role": "The 'Great Geometer' of Antiquity",
        "bio": "Author of the monumental treatise on Conics (introducing the terms parabola, hyperbola, and ellipse from the Pythagorean application of areas) as well as works on Plane Loci, Tangencies, and Unordered Irrationals.",
        "works": ["Conics (Κωνικά)", "Plane Loci", "Tangencies", "On Unordered Irrationals"],
    },
    "pythagoras": {
        "name": "Pythagoras of Samos",
        "dates": "c. 570 – c. 495 BC",
        "role": "Founder of the Pythagorean Brotherhood",
        "bio": "Transformed geometry into a liberal philosophical science; credited with the discovery of the theory of proportions, the application of areas (Book II), the theorem on the right-angled triangle (I.47), and the construction of the cosmic figures.",
        "works": [],
    },
    "thales": {
        "name": "Thales of Miletus",
        "dates": "c. 624 – c. 546 BC",
        "role": "Ionion Natural Philosopher & Pioneer of Greek Geometry",
        "bio": "Introduced geometry from Egypt into Greece; credited by Eudemus and Proclus with propositions I.5, I.15, I.26, and the theorem that the angle in a semicircle is a right angle (III.31).",
        "works": [],
    },
    "eudoxus": {
        "name": "Eudoxus of Cnidus",
        "dates": "c. 408 – c. 355 BC",
        "role": "Mathematician & Astronomer of the Academy",
        "bio": "Creator of the general theory of proportion in Book V (applicable equally to commensurable and incommensurable magnitudes) and the method of exhaustion in Book XII (proving the volume ratios of pyramid, prism, cone, and cylinder).",
        "works": ["General Theory of Proportion (Elements Book V)", "Method of Exhaustion (Elements Book XII)"],
    },
    "theaetetus": {
        "name": "Theaetetus of Athens",
        "dates": "c. 417 – c. 369 BC",
        "role": "Geometer of the Platonic Academy",
        "bio": "Developed the general classification of incommensurable magnitudes (medial, binomial, apotome) codified in Book X and completed the theoretical construction of the five regular solids (octahedron and icosahedron) in Book XIII.",
        "works": ["Theory of Irrationals (Elements Book X)", "Regular Solids (Elements Book XIII)"],
    },
    "hippocrates-of-chios": {
        "name": "Hippocrates of Chios",
        "dates": "fl. c. 440 BC",
        "role": "Early Greek Geometer; First Author of an Elements",
        "bio": "First to compose a treatise of Elements (Στοιχεῖα); squared the lunes (menoeide) and reduced the duplication of the cube to finding two mean proportionals between two straight lines.",
        "works": ["Elements (lost)", "Quadrature of Lunes"],
    },
    "archytas": {
        "name": "Archytas of Tarentum",
        "dates": "428 – 347 BC",
        "role": "Pythagorean Mathematician, Statesman & Friend of Plato",
        "bio": "Solved the duplication of the cube via the intersection of a cylinder, a cone, and a torus in three dimensions, and proved key propositions in harmonic number theory (that no mean proportional exists in a superparticular ratio, VIII.8).",
        "works": [],
    },
    "theodorus-of-cyrene": {
        "name": "Theodorus of Cyrene",
        "dates": "c. 465 – c. 398 BC",
        "role": "Pythagorean Geometer; Teacher of Plato and Theaetetus",
        "bio": "Proved the irrationality of the square roots of non-square integers from 3 up to 17 (Plato, Theaetetus 147D).",
        "works": [],
    },
    "eudemus": {
        "name": "Eudemus of Rhodes",
        "dates": "c. 370 – c. 300 BC",
        "role": "Peripatetic Philosopher & First Historian of Mathematics",
        "bio": "Disciple of Aristotle whose History of Geometry (Γεωμετρικὴ Ἱστορία) is the primary source for Proclus's Eudemian Summary and Simplicius's account of Hippocrates' quadrature of lunes.",
        "works": ["History of Geometry (Γεωμετρικὴ Ἱστορία)"],
    },
    "heron": {
        "name": "Heron of Alexandria",
        "dates": "fl. 1st century AD",
        "role": "Alexandrian Geometer, Engineer & Commentator on Euclid",
        "bio": "Wrote an extensive commentary on Euclid's Elements (extant in Proclus and an-Nairīzī's Arabic commentary) introducing alternative direct proofs, semi-algebraical methods for Book II, and the formula for the area of a triangle in terms of its sides.",
        "works": ["Commentary on Euclid's Elements", "Metrica", "Definitiones", "Dioptra", "Pneumatica"],
    },
    "geminus": {
        "name": "Geminus of Rhodes",
        "dates": "fl. 1st century BC",
        "role": "Stoic Mathematician & Philosopher of Mathematics",
        "bio": "Author of a comprehensive philosophical encyclopaedia on the classification and foundations of the mathematical sciences, extensively excerpted by Proclus and an-Nairīzī.",
        "works": ["Doctrine/Theory of the Mathematical Sciences (Φιλοκαλία)"],
    },
    "posidonius": {
        "name": "Posidonius of Apamea",
        "dates": "c. 135 – c. 51 BC",
        "role": "Stoic Polymath & Geometer",
        "bio": "Defended geometry against the Epicurean critiques of Zeno of Sidon and proposed defining parallel lines as equidistant coplanar straight lines.",
        "works": ["Against Zeno of Sidon"],
    },
    "ptolemy": {
        "name": "Claudius Ptolemy",
        "dates": "c. 100 – c. 170 AD",
        "role": "Alexandrian Astronomer & Geometer",
        "bio": "Author of the Almagest (Syntaxis Mathematica) and a treatise attempting to prove Euclid's Fifth Postulate, preserved and critiqued by Proclus.",
        "works": ["Syntaxis Mathematica (Almagest)", "On the Parallel Postulate"],
    },
    "simplicius": {
        "name": "Simplicius of Cilicia",
        "dates": "c. 490 – c. 560 AD",
        "role": "Neoplatonic Commentator on Aristotle & Euclid",
        "bio": "Preserved Eudemus's verbatim account of the quadrature of lunes by Hippocrates of Chios (in his Commentary on Aristotle's Physics) and ancient proofs of the Parallel Postulate (in an-Nairīzī).",
        "works": ["In Aristotelis Physicorum Libros Commentaria", "In Aristotelis De Caelo Commentaria", "Commentary on the Premises of Euclid's Elements"],
    },
    "eutocius": {
        "name": "Eutocius of Ascalon",
        "dates": "c. 480 – c. 540 AD",
        "role": "Commentator on Archimedes and Apollonius",
        "bio": "Preserved priceless historical solutions to the duplication of the cube, trisection of the angle, and ancient commentaries on Archimedes' Sphere and Cylinder and Apollonius's Conics.",
        "works": ["Commentaries on Archimedes", "Commentary on Apollonius's Conics"],
    },
    "theon-of-alexandria": {
        "name": "Theon of Alexandria",
        "dates": "c. 335 – c. 405 AD",
        "role": "Alexandrian Editor of Euclid's Elements; Father of Hypatia",
        "bio": "Produced the standard late-antique recension of Euclid's Elements that dominated all Greek manuscripts until Peyrard's discovery of the non-Theonine Vatican manuscript (P = Vat. gr. 190).",
        "works": ["Recension of Euclid's Elements", "Commentary on Ptolemy's Syntaxis"],
    },
    "theon-of-smyrna": {
        "name": "Theon of Smyrna",
        "dates": "fl. c. 115 – 140 AD",
        "role": "Middle Platonic Mathematician",
        "bio": "Author of an exposition of arithmetic, music, and astronomy useful for reading Plato, preserving the theory of side and diameter numbers (rational approximations to √2).",
        "works": ["Expositio rerum mathematicarum ad legendum Platonem utilium"],
    },
    "nicomachus": {
        "name": "Nicomachus of Gerasa",
        "dates": "c. 60 – c. 120 AD",
        "role": "Neopythagorean Mathematician",
        "bio": "Author of the Introductio Arithmetica, presenting Greek number theory (prime, composite, plane, solid, and perfect numbers) in an inductive, non-geometric style.",
        "works": ["Introductio Arithmetica (Ἀριθμητικὴ Εἰσαγωγή)"],
    },
    "diophantus": {
        "name": "Diophantus of Alexandria",
        "dates": "fl. c. 250 AD",
        "role": "Alexandrian Algebraist & Number Theorist",
        "bio": "Author of the Arithmetica and On Polygonal Numbers, pioneering syncopated algebraic notation and indeterminate analysis.",
        "works": ["Arithmetica", "On Polygonal Numbers"],
    },
    "hypsicles": {
        "name": "Hypsicles of Alexandria",
        "dates": "fl. c. 175 BC",
        "role": "Alexandrian Mathematician & Astronomer",
        "bio": "Author of the treatise on regular polyhedra appended to Euclid's Elements as 'Book XIV', building on Aristaeus and Apollonius on the dodecahedron and icosahedron inscribed in the same sphere.",
        "works": ["Book XIV of the Elements", "Anaphorikos"],
    },
    "boethius": {
        "name": "Anicius Manlius Severinus Boethius",
        "dates": "c. 480 – 524 AD",
        "role": "Roman Philosopher & Transmitter of the Quadrivium",
        "bio": "Translated Euclid's definitions, postulates, and enunciations into Latin and authored the De Institutione Arithmetica and De Institutione Musica.",
        "works": ["De Institutione Arithmetica", "De Institutione Musica", "Ars Geometriae"],
    },
    "an-nairizi": {
        "name": "al-Faḍl ibn Ḥātim an-Nairīzī (Anaritius)",
        "dates": "c. 865 – c. 922 AD",
        "role": "Persian Mathematician, Astronomer & Commentator on Euclid",
        "bio": "Authored a major Arabic commentary on Euclid's Elements (translated into Latin by Gherard of Cremona) that uniquely preserves large lost portions of the commentaries of Heron of Alexandria and Simplicius.",
        "works": ["Commentary on Euclid's Elements (ed. Besthorn & Heiberg; Latin tr. ed. Curtze)"],
    },
    "nasiraddin": {
        "name": "Naṣīr al-Dīn al-Ṭūsī",
        "dates": "1201 – 1274",
        "role": "Persian Polymath, Astronomer & Geometer",
        "bio": "Composed influential Arabic recensions (Taḥrīr) of Euclid's Elements and attempted a proof of the Parallel Postulate that directly influenced John Wallis and Girolamo Saccheri.",
        "works": ["Taḥrīr Uṣūl Uqlīdis"],
    },
    "campanus": {
        "name": "Campanus of Novara",
        "dates": "c. 1220 – 1296",
        "role": "Medieval Italian Mathematician & Editor of the Latin Euclid",
        "bio": "Prepared the authoritative medieval Latin edition and commentary of the Elements (based on Adelard of Bath and Arabic sources), which was the first printed edition of Euclid (Ratdolt, Venice, 1482) and the basis of Pacioli's 1509 edition.",
        "works": ["Elementa Geometriae (printed Venice, 1482)"],
    },
    "pacioli": {
        "name": "Fra Luca Bartolomeo de Pacioli",
        "dates": "c. 1447 – 1517",
        "role": "Renaissance Franciscan Mathematician",
        "bio": "Author of the Summa de arithmetica (1494) and De Divina Proportione (1509, illustrated by Leonardo da Vinci), and editor of a 1509 Venice Latin edition of Euclid's Elements.",
        "works": ["Summa de arithmetica, geometria, proportioni et proportionalita (1494)", "De Divina Proportione (1509)", "Euclidis Opera (1509)"],
    },
    "commandino": {
        "name": "Federico Commandino",
        "dates": "1509 – 1575",
        "role": "Renaissance Humanist Mathematician & Translator",
        "bio": "Produced the landmark 1572 Latin translation and commentary of Euclid's Elements directly from the Greek text alongside editions of Archimedes, Apollonius, Pappus, Aristarchus, and Heron.",
        "works": ["Euclidis Elementorum Libri XV (Pesaro, 1572)"],
    },
    "clavius": {
        "name": "Christopher Clavius, S.J.",
        "dates": "1538 – 1612",
        "role": "Jesuit Mathematician & Architect of the Gregorian Calendar",
        "bio": "Published an encyclopedic Latin edition and commentary on Euclid's Elements (1574) containing extensive scholia, critiques of Peletier on the angle of contact, and an attempted proof of the Parallel Postulate.",
        "works": ["Euclidis Elementorum Libri XV (Rome, 1574)"],
    },
    "wallis": {
        "name": "John Wallis",
        "dates": "1616 – 1703",
        "role": "Savilian Professor of Geometry at Oxford",
        "bio": "Pioneered infinitesimal analysis, defended Euclid's treatment of the horn-like angle of contact against Clavius, and showed that the Parallel Postulate is equivalent to the existence of similar non-congruent triangles of arbitrary size.",
        "works": ["De Postulato Quinto (1663 / 1693)", "De Angulo Contactus et Semicirculi (1656)", "Arithmetica Infinitorum (1656)"],
    },
    "barrow": {
        "name": "Isaac Barrow",
        "dates": "1630 – 1677",
        "role": "First Lucasian Professor of Mathematics at Cambridge; Teacher of Newton",
        "bio": "Published widely used Latin and English editions of Euclid's Elements (1655, 1660) and defended the philosophical rigor of Euclid's definitions and Book V theory of proportion in his Lectiones Mathematicae.",
        "works": ["Euclidis Elementorum Libri XV Breviter Demonstrati (1655)", "Lectiones Mathematicae (1683)"],
    },
    "saccheri": {
        "name": "Girolamo Saccheri, S.J.",
        "dates": "1667 – 1733",
        "role": "Jesuit Logician & Precursor of Non-Euclidean Geometry",
        "bio": "Author of Euclides ab omni naevo vindicatus (1733), investigating the summit angles of the Saccheri quadrilateral under the hypotheses of the obtuse, acute, and right angle, unwittingly establishing dozens of theorems of non-Euclidean geometry.",
        "works": ["Euclides ab omni naevo vindicatus (1733)", "Logica Demonstrativa (1697)"],
    },
    "simson": {
        "name": "Robert Simson",
        "dates": "1687 – 1768",
        "role": "Professor of Mathematics at the University of Glasgow",
        "bio": "Published the critical Latin and English edition of Books I–VI, XI, and XII of Euclid's Elements (1756) that served as the standard textbook in the English-speaking world for over a century.",
        "works": ["The Elements of Euclid (1756)"],
    },
    "lambert": {
        "name": "Johann Heinrich Lambert",
        "dates": "1728 – 1777",
        "role": "Swiss-German Mathematician, Physicist & Philosopher",
        "bio": "Proved the irrationality of π (1761) and wrote Die Theorie der Parallellinien (1766), discovering that under the hypothesis of the acute angle the area of a triangle is proportional to its angular defect and would hold on a sphere of imaginary radius.",
        "works": ["Die Theorie der Parallellinien (1766)"],
    },
    "playfair": {
        "name": "John Playfair",
        "dates": "1748 – 1819",
        "role": "Scottish Mathematician & Geologist",
        "bio": "Popularized 'Playfair's Axiom' (already stated by Proclus) as a modern substitute for Euclid's Fifth Postulate in his Elements of Geometry (1795).",
        "works": ["Elements of Geometry (1795)"],
    },
    "legendre": {
        "name": "Adrien-Marie Legendre",
        "dates": "1752 – 1833",
        "role": "French Mathematician",
        "bio": "Author of Éléments de géométrie (1794), who reshaped elementary geometry instruction and proved fundamental theorems relating the Parallel Postulate to the angle-sum of a triangle.",
        "works": ["Éléments de géométrie (1794)", "Théorie des nombres"],
    },
    "gauss": {
        "name": "Carl Friedrich Gauss",
        "dates": "1777 – 1855",
        "role": "German Mathematician ('Princeps Mathematicorum')",
        "bio": "Proved the constructibility of the regular 17-gon (extending Euclid Book IV) and was the first to recognize the logical consistency and possible physical validity of non-Euclidean (hyperbolic) geometry.",
        "works": ["Disquisitiones Arithmeticae (1801)"],
    },
    "lobachevsky": {
        "name": "Nikolai Ivanovich Lobachevsky",
        "dates": "1792 – 1856",
        "role": "Co-Founder of Hyperbolic Non-Euclidean Geometry",
        "bio": "Published the first complete, self-consistent system of hyperbolic geometry ('Imaginary' or 'Pangeometry', 1829–1855) replacing Euclid's Fifth Postulate with its negation.",
        "works": ["Geometrische Untersuchungen zur Theorie der Parallellinien (1840)", "Pangeometry (1855)"],
    },
    "bolyai": {
        "name": "János Bolyai",
        "dates": "1802 – 1860",
        "role": "Co-Founder of Hyperbolic Non-Euclidean Geometry",
        "bio": "Independently discovered non-Euclidean geometry and published the celebrated Appendix scientiam spatii absolute veram exhibens (1832) in his father Farkas Bolyai's Tentamen.",
        "works": ["Appendix scientiam spatii absolute veram exhibens (1832)"],
    },
    "riemann": {
        "name": "Bernhard Riemann",
        "dates": "1826 – 1866",
        "role": "German Mathematician; Founder of Riemannian Geometry",
        "bio": "In his 1854 Habilitationsschrift, generalized geometry to n-dimensional manifolds of variable curvature, distinguishing unboundedness from infinitude and introducing spherical/elliptic non-Euclidean geometry.",
        "works": ["Über die Hypothesen, welche der Geometrie zu Grunde liegen (1854 / 1867)"],
    },
    "de-morgan": {
        "name": "Augustus De Morgan",
        "dates": "1806 – 1871",
        "role": "British Mathematician & Logician",
        "bio": "Wrote penetrating critical analyses of Euclid's logic, Book V theory of proportion, and Book X theory of irrationals in the Companion to the Almanac and the Penny Cyclopaedia.",
        "works": ["Study and Difficulties of Mathematics (1831)", "Connexion of Number and Magnitude (1836)", "Formal Logic (1847)"],
    },
    "todhunter": {
        "name": "Isaac Todhunter",
        "dates": "1820 – 1884",
        "role": "Cambridge Mathematician & Historian of Mathematics",
        "bio": "Author of the classic Cambridge school and university edition of The Elements of Euclid (1862) with insightful pedagogical and logical notes.",
        "works": ["The Elements of Euclid (1862)"],
    },
    "dedekind": {
        "name": "Richard Dedekind",
        "dates": "1831 – 1916",
        "role": "German Mathematician",
        "bio": "Formulated the rigorous arithmetic theory of irrational numbers via Dedekind cuts (Stetigkeit und irrationale Zahlen, 1872), which strictly mirrors Eudoxus's Definition 5 of Book V.",
        "works": ["Stetigkeit und irrationale Zahlen (1872)", "Was sind und was sollen die Zahlen? (1888)"],
    },
    "heiberg": {
        "name": "Johan Ludvig Heiberg",
        "dates": "1854 – 1928",
        "role": "Danish Classical Philologist & Editor of the Critical Greek Text of Euclid",
        "bio": "Edited the definitive Teubner critical Greek edition of Euclid's Elements (Vols. I–V, 1883–1888) based on the non-Theonine Vatican manuscript P, as well as the critical editions of Archimedes, Apollonius, Ptolemy, and Simplicius.",
        "works": ["Euclidis Elementa (5 vols., Teubner, 1883–1888)", "Litterargeschichtliche Studien über Euklid (1882)", "Mathematisches zu Aristoteles (1904)"],
    },
    "cantor": {
        "name": "Moritz Benedikt Cantor",
        "dates": "1829 – 1920",
        "role": "German Historian of Mathematics",
        "bio": "Author of the monumental four-volume Vorlesungen über Geschichte der Mathematik (1880–1908).",
        "works": ["Vorlesungen über Geschichte der Mathematik"],
    },
    "zeuthen": {
        "name": "Hieronymus Georg Zeuthen",
        "dates": "1839 – 1920",
        "role": "Danish Mathematician & Historian of Greek Geometry",
        "bio": "Demonstrated the geometric-algebraic content of Euclid Book II and Book VI and the constructive existence role of Greek geometric problems.",
        "works": ["Die Lehre von den Kegelschnitten im Altertum (1886)", "Geschichte der Mathematik im Altertum und Mittelalter (1896)"],
    },
    "tannery": {
        "name": "Paul Tannery",
        "dates": "1843 – 1904",
        "role": "French Historian of Ancient Science & Mathematics",
        "bio": "Pioneered the critical reconstruction of pre-Euclidean Greek geometry, the history of the terms axiom and common notion, and the edition of Diophantus.",
        "works": ["La Géométrie grecque (1887)", "Pour l'histoire de la science hellène (1887)"],
    },
    "hankel": {
        "name": "Hermann Hankel",
        "dates": "1839 – 1873",
        "role": "German Mathematician & Historian of Mathematics",
        "bio": "Author of Zur Geschichte der Mathematik in Alterthum und Mittelalter (1874), analyzing the Greek method of analysis, synthesis, and diorismos.",
        "works": ["Zur Geschichte der Mathematik in Alterthum und Mittelalter (1874)"],
    },
    "allman": {
        "name": "George Johnston Allman",
        "dates": "1824 – 1904",
        "role": "Irish Mathematician & Historian of Greek Geometry",
        "bio": "Author of Greek Geometry from Thales to Euclid (1889), tracing the contributions of the Pythagoreans, Hippocrates, Archytas, Eudoxus, and Theaetetus.",
        "works": ["Greek Geometry from Thales to Euclid (1889)"],
    },
    "bretschneider": {
        "name": "Carl Anton Bretschneider",
        "dates": "1808 – 1878",
        "role": "German Geometer & Historian of Mathematics",
        "bio": "Author of Die Geometrie und die Geometer vor Euklides (1870).",
        "works": ["Die Geometrie und die Geometer vor Euklides (1870)"],
    },
    "loria": {
        "name": "Gino Loria",
        "dates": "1862 – 1954",
        "role": "Italian Historian of Mathematics",
        "bio": "Author of Le scienze esatte nell' antica Grecia (1893–1902; 2nd ed. 1914).",
        "works": ["Le scienze esatte nell' antica Grecia"],
    },
    "simon": {
        "name": "Max Simon",
        "dates": "1844 – 1918",
        "role": "German Historian of Mathematics",
        "bio": "Author of Euclid und die sechs planimetrischen Bücher (1901) and Über die Entwicklung der Elementar-Geometrie im XIX. Jahrhundert (1906).",
        "works": ["Euclid und die sechs planimetrischen Bücher (1901)"],
    },
    "pasch": {
        "name": "Moritz Pasch",
        "dates": "1843 – 1930",
        "role": "Pioneer of Modern Axiomatic Geometry",
        "bio": "In Vorlesungen über neuere Geometrie (1882), identified the unstated order and betweenness assumptions in Euclid ('Pasch's Axiom') and initiated rigorous modern axiomatics.",
        "works": ["Vorlesungen über neuere Geometrie (1882)"],
    },
    "veronese": {
        "name": "Giuseppe Veronese",
        "dates": "1854 – 1917",
        "role": "Italian Geometer; Pioneer of Non-Archimedean Geometry",
        "bio": "Author of Fondamenti di geometria (1891) and Elementi di geometria (with Ingrami), developing rigorous synthetic foundations of geometry.",
        "works": ["Fondamenti di geometria (1891)", "Elementi di geometria"],
    },
    "hilbert": {
        "name": "David Hilbert",
        "dates": "1862 – 1943",
        "role": "German Mathematician",
        "bio": "Author of Grundlagen der Geometrie (1899), reorganizing Euclidean geometry into five rigorous axiom groups (incidence, order, congruence, parallels, continuity) and proving the theory of plane area independent of continuity.",
        "works": ["Grundlagen der Geometrie (1899)"],
    },
    "enriques": {
        "name": "Federigo Enriques",
        "dates": "1871 – 1946",
        "role": "Italian Geometer & Philosopher of Science",
        "bio": "Editor of Questioni riguardanti la geometria elementare (1900) and co-author (with Ugo Amaldi) of Elementi di geometria.",
        "works": ["Questioni riguardanti la geometria elementare (1900)", "Elementi di geometria"],
    },
    "russell": {
        "name": "Bertrand Russell",
        "dates": "1872 – 1970",
        "role": "British Philosopher, Logician & Mathematician",
        "bio": "Author of An Essay on the Foundations of Geometry (1897) and The Principles of Mathematics (1903).",
        "works": ["An Essay on the Foundations of Geometry (1897)", "The Principles of Mathematics (1903)"],
    },
    "heath": {
        "name": "Sir Thomas Little Heath",
        "dates": "1861 – 1940",
        "role": "Translator & Commentator of The Thirteen Books of Euclid's Elements",
        "bio": "Foremost English historian of Greek mathematics; translated and annotated Euclid's Elements (1908; 2nd ed. 1926) from Heiberg's critical Greek text, as well as the works of Archimedes, Apollonius, Diophantus, and Aristarchus.",
        "works": ["The Thirteen Books of Euclid's Elements (1908 / 1926)", "The Works of Archimedes (1897)", "Apollonius of Perga (1896)", "A History of Greek Mathematics (1921)"],
    },
}

# ---------------------------------------------------------------------------
# 2. Citation Work Normalization & Catalog
# ---------------------------------------------------------------------------

CITE_PREFIX_MAP: Dict[str, str] = {
    "allman:greek_geometry": "allman:greek-geometry",
    "apollonius:comparison_dodecahedron_icosahedron": "apollonius:comparison-solids",
    "apollonius:plane_loci": "apollonius:plane-loci",
    "archimedes:de_conoidibus": "archimedes:conoids-and-spheroids",
    "archimedes:de_sphaera_et_cylindro": "archimedes:sphere-and-cylinder",
    "archimedes:quadratura_parabolae": "archimedes:quadrature-of-parabola",
    "aristaeus:comparison_five_solids": "aristaeus:comparison-five-solids",
    "aristaeus:solid_loci": "aristaeus:solid-loci",
    "aristotle:de_caelo": "aristotle:de-caelo",
    "aristotle:metaphysica": "aristotle:met",
    "aristotle:metaphysics": "aristotle:met",
    "aristotle:physica": "aristotle:phys",
    "aristotle:physics": "aristotle:phys",
    "aristotle:topica": "aristotle:topics",
    "cantor:geschichte-der-mathematik": "cantor:vorlesungen",
    "christensen:zeitschrift_math_phys": "christensen:zeitschrift-math-phys",
    "chrystal:textbook_of_algebra": "chrystal:textbook-of-algebra",
    "cossali:origine_algebra": "cossali:origine-algebra",
    "de_morgan:penny_cyclopaedia": "de-morgan:penny-cyclopaedia",
    "democritus:peri_alogon_grammon": "democritus:peri-alogon-grammon",
    "diogenes_laertius:vitae": "diogenes-laertius:vitae",
    "euclid:de_divisionibus": "euclid:on-divisions",
    "euclid:sectio_canonis": "euclid:sectio-canonis",
    "euclid:surface_loci": "euclid:surface-loci",
    "eudemus:history_of_geometry": "eudemus:history-of-geometry",
    "eutocius:in_archimedem": "eutocius:in-archimedem",
    "fibonacci:liber_abaci": "fibonacci:liber-abaci",
    "hankel:zur-geschichte-der-mathematik": "hankel:geschichte",
    "heath:method_of_archimedes": "heath:method-of-archimedes",
    "heath:works_of_archimedes": "heath:works-of-archimedes",
    "heiberg:archimedis_opera": "heiberg:archimedis-opera",
    "heiberg:euklid_studien": "heiberg:euklid-studien",
    "heiberg:studien": "heiberg:euklid-studien",
    "hirsch:algebraischer_commentar": "hirsch:algebraischer-commentar",
    "hultsch:neue_jahrbuecher": "hultsch:neue-jahrbuecher",
    "kluge:de_euclidis_xiv_xv": "kluge:de-euclidis-xiv-xv",
    "legendre:elements": "legendre:elements-de-geometrie",
    "legendre:elements_de_geometrie": "legendre:elements-de-geometrie",
    "loria:scienze_esatte": "loria:scienze-esatte",
    "nesselmann:algebra_der_griechen": "nesselmann:algebra-der-griechen",
    "pappus:synagoge": "pappus:collectio",
    "pauly_wissowa:real_encyclopaedie": "pauly-wissowa:real-encyclopaedie",
    "plato:republic": "plato:rep",
    "plato:theaet": "plato:theaetetus",
    "plutarch:de_communibus_notitiis": "plutarch:de-communibus-notitiis",
    "poselger:zehnte_buch": "poselger:zehnte-buch",
    "proclus:in_euclidem": "proclus:in-euclid",
    "saccheri:euclides": "saccheri:euclides-vindicatus",
    "simon:euclid-sechs-planimetrischen": "simon:euclid-1901",
    "simplicius:in_physica": "simplicius:in-physica",
    "stevin:appendice_incommensurables": "stevin:appendice-incommensurables",
    "stevin:oeuvres_mathematiques": "stevin:oeuvres-mathematiques",
    "stifel:arithmetica_integra": "stifel:arithmetica-integra",
    "suter:mathematiker_araber": "suter:mathematiker-araber",
    "tannery:memoires_bordeaux": "tannery:memoires-bordeaux",
    "wallis:defense-of-angle-of-contact": "wallis:de-angulo-contactus",
    "woepcke:memoires_academie": "woepcke:memoires-academie",
    "zeuthen:geschichte_altertum": "zeuthen:geschichte-altertum",
}

WORK_TITLES: Dict[str, Tuple[str, str]] = {
    "allman:greek-geometry": ("George Johnston Allman", "Greek Geometry from Thales to Euclid (1889)"),
    "apollonius:conics": ("Apollonius of Perga", "Conics (Κωνικά)"),
    "apollonius:plane-loci": ("Apollonius of Perga", "Plane Loci (Τόποι ἐπίπεδοι)"),
    "apollonius:comparison-solids": ("Apollonius of Perga", "Comparison of the Dodecahedron and the Icosahedron"),
    "archimedes:sphere-and-cylinder": ("Archimedes of Syracuse", "On the Sphere and Cylinder (Περὶ σφαίρας καὶ κυλίνδρου)"),
    "archimedes:quadrature-of-parabola": ("Archimedes of Syracuse", "Quadrature of the Parabola"),
    "archimedes:conoids-and-spheroids": ("Archimedes of Syracuse", "On Conoids and Spheroids"),
    "archimedes:equilibrium-of-planes": ("Archimedes of Syracuse", "On the Equilibrium of Planes"),
    "archimedes:liber-assumptorum": ("Archimedes of Syracuse", "Liber Assumptorum (Book of Lemmas)"),
    "archimedes:methodus": ("Archimedes of Syracuse", "The Method of Mechanical Theorems (Ἐφόδιον)"),
    "aristaeus:solid-loci": ("Aristaeus the Elder", "Solid Loci (Τόποι στερεοί)"),
    "aristaeus:comparison-five-solids": ("Aristaeus the Elder", "Comparison of the Five Regular Solids"),
    "aristotle:anal-post": ("Aristotle", "Analytica Posteriora (Posterior Analytics)"),
    "aristotle:anal-prior": ("Aristotle", "Analytica Priora (Prior Analytics)"),
    "aristotle:met": ("Aristotle", "Metaphysica (Metaphysics)"),
    "aristotle:phys": ("Aristotle", "Physica (Physics)"),
    "aristotle:de-caelo": ("Aristotle", "De Caelo (On the Heavens)"),
    "aristotle:de-anima": ("Aristotle", "De Anima (On the Soul)"),
    "aristotle:topics": ("Aristotle", "Topica (Topics)"),
    "aristotle:eth-nic": ("Aristotle", "Ethica Nicomachea (Nicomachean Ethics)"),
    "aristotle:meteorologica": ("Aristotle", "Meteorologica"),
    "aristotle:soph-el": ("Aristotle", "Sophistici Elenchi"),
    "aristotle:mechanica": ("Pseudo-Aristotle", "Mechanica"),
    "barrow:lectiones-cantabrigienses": ("Isaac Barrow", "Lectiones Mathematicae Cantabrigienses (1683)"),
    "boethius:de-institutione-musica": ("Boethius", "De Institutione Musica"),
    "cantor:vorlesungen": ("Moritz Cantor", "Vorlesungen über Geschichte der Mathematik (1880–1908)"),
    "de-morgan:penny-cyclopaedia": ("Augustus De Morgan", "Articles in The Penny Cyclopaedia"),
    "de-morgan:formal-logic": ("Augustus De Morgan", "Formal Logic (1847)"),
    "diogenes-laertius:vitae": ("Diogenes Laertius", "Lives and Opinions of Eminent Philosophers"),
    "dodgson:euclid-and-modern-rivals": ("Charles Lutwidge Dodgson (Lewis Carroll)", "Euclid and His Modern Rivals (1879)"),
    "euclid:elements": ("Euclid of Alexandria", "Elements (Στοιχεῖα)"),
    "euclid:data": ("Euclid of Alexandria", "Data (Δεδομένα)"),
    "euclid:porisms": ("Euclid of Alexandria", "Porisms (Πορίσματα)"),
    "euclid:on-divisions": ("Euclid of Alexandria", "On Divisions of Figures (Περὶ διαιρέσεων βιβλίον)"),
    "euclid:optics": ("Euclid of Alexandria", "Optics (Ὀπτικά)"),
    "euclid:phaenomena": ("Euclid of Alexandria", "Phaenomena (Φαινόμενα)"),
    "euclid:sectio-canonis": ("Euclid of Alexandria", "Sectio Canonis (Κατατομὴ κανόνος)"),
    "euclid:surface-loci": ("Euclid of Alexandria", "Surface Loci (Τόποι πρὸς ἐπιφανείᾳ)"),
    "eudemus:history-of-geometry": ("Eudemus of Rhodes", "History of Geometry (Γεωμετρικὴ Ἱστορία)"),
    "eutocius:in-archimedem": ("Eutocius of Ascalon", "Commentaries on Archimedes' On the Sphere and Cylinder"),
    "fibonacci:liber-abaci": ("Leonardo of Pisa (Fibonacci)", "Liber Abaci (1202 / 1228)"),
    "hankel:geschichte": ("Hermann Hankel", "Zur Geschichte der Mathematik in Alterthum und Mittelalter (1874)"),
    "heath:works-of-archimedes": ("Sir Thomas Little Heath", "The Works of Archimedes (1897)"),
    "heath:method-of-archimedes": ("Sir Thomas Little Heath", "The Method of Archimedes (1912)"),
    "heath:apollonius-of-perga": ("Sir Thomas Little Heath", "Apollonius of Perga: Treatise on Conic Sections (1896)"),
    "heiberg:euklid-studien": ("Johan Ludvig Heiberg", "Litterargeschichtliche Studien über Euklid (1882)"),
    "heiberg:mathematisches-zu-aristoteles": ("Johan Ludvig Heiberg", "Mathematisches zu Aristoteles (1904)"),
    "heiberg:archimedis-opera": ("Johan Ludvig Heiberg", "Archimedis Opera Omnia (Teubner)"),
    "heron:metrica": ("Heron of Alexandria", "Metrica (Μετρικά)"),
    "heron:dioptra": ("Heron of Alexandria", "Dioptra (Περὶ διόπτρας)"),
    "hilbert:grundlagen": ("David Hilbert", "Grundlagen der Geometrie (Foundations of Geometry, 1899)"),
    "iamblichus:in-nicomachi-arith": ("Iamblichus", "In Nicomachi Arithmeticam Introductionem"),
    "ibn-al-nadim:fihrist": ("Ibn al-Nadīm", "Kitāb al-Fihrist (987 AD)"),
    "lambert:parallellinien": ("Johann Heinrich Lambert", "Die Theorie der Parallellinien (1766)"),
    "legendre:elements-de-geometrie": ("Adrien-Marie Legendre", "Éléments de géométrie (1794)"),
    "loria:scienze-esatte": ("Gino Loria", "Le scienze esatte nell' antica Grecia (1893–1902 / 1914)"),
    "nesselmann:algebra-der-griechen": ("G. H. F. Nesselmann", "Die Algebra der Griechen (1842)"),
    "nicomachus:intro-arith": ("Nicomachus of Gerasa", "Introductio Arithmetica"),
    "pappus:collectio": ("Pappus of Alexandria", "Mathematical Collection (Συναγωγή, ed. Hultsch)"),
    "pasch:neuere-geometrie": ("Moritz Pasch", "Vorlesungen über neuere Geometrie (1882)"),
    "plato:rep": ("Plato", "Republic (Πολιτεία)"),
    "plato:meno": ("Plato", "Meno (Μένων)"),
    "plato:theaetetus": ("Plato", "Theaetetus (Θεαίτητος)"),
    "plato:timaeus": ("Plato", "Timaeus (Τίμαιος)"),
    "plato:laws": ("Plato", "Laws (Νόμοι)"),
    "plato:parm": ("Plato", "Parmenides (Παρμενίδης)"),
    "plato:sophist": ("Plato", "Sophist (Σοφιστής)"),
    "plato:phaedo": ("Plato", "Phaedo (Φαίδων)"),
    "plato:gorgias": ("Plato", "Gorgias (Γοργίας)"),
    "plutarch:de-communibus-notitiis": ("Plutarch", "De Communibus Notitiis adversus Stoicos"),
    "proclus:in-euclid": ("Proclus Diadochus", "In Primum Euclidis Elementorum Librum Commentarii (ed. Friedlein, 1873)"),
    "proclus:in-platonis-timaeum": ("Proclus Diadochus", "In Platonis Timaeum Commentaria"),
    "ptolemy:syntaxis": ("Claudius Ptolemy", "Syntaxis Mathematica (Almagest)"),
    "russell:principles-of-mathematics": ("Bertrand Russell", "The Principles of Mathematics (1903)"),
    "saccheri:euclides-vindicatus": ("Girolamo Saccheri", "Euclides ab omni naevo vindicatus (1733)"),
    "serenus:de-sectione-coni": ("Serenus of Antinoeia", "On the Section of a Cone"),
    "simon:euclid-1901": ("Max Simon", "Euclid und die sechs planimetrischen Bücher (1901)"),
    "simplicius:in-physica": ("Simplicius of Cilicia", "In Aristotelis Physicorum Libros Commentaria (ed. Diels)"),
    "staeckel-engel:parallellinien": ("Paul Stäckel & Friedrich Engel", "Die Theorie der Parallellinien von Euklid bis auf Gauss (1895)"),
    "stevin:oeuvres-mathematiques": ("Simon Stevin", "Les Œuvres Mathématiques (1634)"),
    "stifel:arithmetica-integra": ("Michael Stifel", "Arithmetica Integra (1544)"),
    "stobaeus:eclogae": ("Ioannes Stobaeus", "Eclogae Physicae et Ethicae"),
    "suter:mathematiker-araber": ("Heinrich Suter", "Die Mathematiker und Astronomen der Araber und ihre Werke (1900)"),
    "tannery:geometrie-grecque": ("Paul Tannery", "La Géométrie grecque (1887)"),
    "theodosius:sphaerica": ("Theodosius of Bithynia", "Sphaerica (Σφαιρικά)"),
    "wallis:de-angulo-contactus": ("John Wallis", "De Angulo Contactus et Semicirculi Disquisitio Geometrica (1656)"),
    "zeuthen:kegelschnitte": ("Hieronymus Georg Zeuthen", "Die Lehre von den Kegelschnitten im Altertum (1886)"),
    "zeuthen:geschichte-altertum": ("Hieronymus Georg Zeuthen", "Geschichte der Mathematik im Altertum und Mittelalter (1896)"),
}

# ---------------------------------------------------------------------------
# 3. Term Normalization & Glossary Catalog
# ---------------------------------------------------------------------------

TERM_ALIAS_MAP: Dict[str, str] = {
    "ratio-ex-aequali": "ex-aequali",
    "rhetos": "rational",
    "alogos": "irrational",
    "mekos": "length",
    "platos": "breadth",
    "bathos": "depth",
    "diastaseis": "dimensions",
    "semeion": "point",
    "gramme": "line",
    "eutheia-gramme": "straight-line",
    "epiphaneia": "surface",
    "epipedos-epiphaneia": "plane-surface",
    "gonia": "angle",
    "kyklos": "circle",
    "kentron": "centre",
    "diametros": "diameter",
    "dividendo": "separando",
    "dirimendo": "separando",
    "permutando": "alternando",
    "alternate-ratio": "alternando",
    "inverse-ratio": "invertendo",
    "composition-of-a-ratio": "componendo",
    "separation-of-a-ratio": "separando",
    "conversion-of-a-ratio": "convertendo",
    "first-bimedial-straight-line": "first-bimedial",
    "second-bimedial-straight-line": "second-bimedial",
    "apagoge-eis-to-adynaton": "eis-to-adynaton",
}

TERM_CATALOG: Dict[str, Dict[str, str]] = {
    "point": {
        "headword": "Point (σημεῖον)",
        "language": "Euclidean Definition (Book I, Def. 1)",
        "translation": "Σημεῖόν ἐστιν, οὗ μέρος οὐθέν",
        "definition": "Book I, Def. 1: 'A point is that which has no part.' Earlier Pythagoreans defined it as a 'monad having position' (μονὰς προσλαβοῦσα θέσιν).",
    },
    "line": {
        "headword": "Line (γραμμή)",
        "language": "Euclidean Definition (Book I, Def. 2)",
        "translation": "Γραμμὴ δὲ μῆκος ἀπλατές",
        "definition": "Book I, Def. 2: 'A line is breadthless length.' Book I, Def. 3: 'The extremities of a line are points.'",
    },
    "straight-line": {
        "headword": "Straight line (εὐθεῖα γραμμή)",
        "language": "Euclidean Definition (Book I, Def. 4)",
        "translation": "Εὐθεῖα γραμμή ἐστιν, ἥτις ἐξ ἴσου τοῖς ἐφ' ἑαυτῆς σημείοις κεῖται",
        "definition": "Book I, Def. 4: 'A straight line is a line which lies evenly with the points on itself.'",
    },
    "surface": {
        "headword": "Surface (ἐπιφάνεια)",
        "language": "Euclidean Definition (Book I, Def. 5)",
        "translation": "Ἐπιφάνεια δέ ἐστιν, ὃ μῆκος καὶ πλάτος μόνον ἔχει",
        "definition": "Book I, Def. 5: 'A surface is that which has length and breadth only.' Book I, Def. 6: 'The extremities of a surface are lines.'",
    },
    "plane-surface": {
        "headword": "Plane surface (ἐπίπεδος ἐπιφάνεια)",
        "language": "Euclidean Definition (Book I, Def. 7)",
        "translation": "Ἐπίπεδος ἐπιφάνειά ἐστιν, ἥτις ἐξ ἴσου ταῖς ἐφ' ἑαυτῆς εὐθείαις κεῖται",
        "definition": "Book I, Def. 7: 'A plane surface is a surface which lies evenly with the straight lines on itself.'",
    },
    "plane-angle": {
        "headword": "Plane angle (ἐπίπεδος γωνία)",
        "language": "Euclidean Definition (Book I, Def. 8)",
        "translation": "Ἐπίπεδος δὲ γωνία ἐστὶν ἡ ἐν ἐπιπέδῳ δύο γραμμῶν ἁπτομένων ἀλλήλων κλίσις",
        "definition": "Book I, Def. 8: 'A plane angle is the inclination to one another of two lines in a plane which meet one another and do not lie in a straight line.'",
    },
    "angle": {
        "headword": "Angle (γωνία)",
        "language": "Euclidean Definition (Book I, Def. 8–12)",
        "translation": "γωνία",
        "definition": "The inclination to one another of two lines in a plane which meet one another and do not lie in a straight line (classified by Aristotle, Syrianus, and Proclus under quality, quantity, or relation).",
    },
    "right-angle": {
        "headword": "Right angle (ὀρθὴ γωνία) & Perpendicular (κάθετος)",
        "language": "Euclidean Definition (Book I, Def. 10)",
        "translation": "ὀρθὴ γωνία / κάθετος",
        "definition": "Book I, Def. 10: 'When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is called a perpendicular to that on which it stands.'",
    },
    "circle": {
        "headword": "Circle (κύκλος)",
        "language": "Euclidean Definition (Book I, Def. 15)",
        "translation": "Κύκλος ἐστὶ σχῆμα ἐπίπεδον ὑπὸ μιᾶς γραμμῆς περιεχόμενον...",
        "definition": "Book I, Def. 15: 'A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.'",
    },
    "centre": {
        "headword": "Centre of the circle (κέντρον τοῦ κύκλου)",
        "language": "Euclidean Definition (Book I, Def. 16)",
        "translation": "Κέντρον δὲ τοῦ κύκλου τὸ σημεῖον καλεῖται",
        "definition": "Book I, Def. 16: 'And the point is called the centre of the circle.'",
    },
    "diameter": {
        "headword": "Diameter of the circle (διάμετρος τοῦ κύκλου)",
        "language": "Euclidean Definition (Book I, Def. 17)",
        "translation": "Διάμετρος δὲ τοῦ κύκλου ἐστὶν εὐθεῖά τις διὰ τοῦ κέντρου ἠγμένη...",
        "definition": "Book I, Def. 17: 'A diameter of the circle is any straight line drawn through the centre and terminated in both directions by the circumference of the circle, and such a straight line also bisects the circle.'",
    },
    "parallel-straight-lines": {
        "headword": "Parallel straight lines (παράλληλοι εὐθεῖαι)",
        "language": "Euclidean Definition (Book I, Def. 23)",
        "translation": "Παράλληλοί εἰσιν εὐθεῖαι, αἵτινες ἐν τῷ αὐτῷ ἐπιπέδῳ οὖσαι καὶ ἐκβαλλόμεναι εἰς ἄπειρον ἐφ' ἑκάτερα τὰ μέρη ἐπὶ μηδέτερα συμπίπτουσιν ἀλλήλαις",
        "definition": "Book I, Def. 23: 'Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.'",
    },
    "gnomon": {
        "headword": "Gnomon (γνώμων)",
        "language": "Euclidean Definition (Book II, Def. 2)",
        "translation": "γνώμων",
        "definition": "Book II, Def. 2: 'In any parallelogrammic area let any one whatever of the parallelograms about its diameter with the two complements be called a gnomon.'",
    },
    "ratio": {
        "headword": "Ratio (λόγος)",
        "language": "Euclidean Definition (Book V, Def. 3 & 4)",
        "translation": "Λόγος ἐστὶ δύο μεγεθῶν ὁμογενῶν ἡ κατὰ πηλικότητα ποιὰ σχέσις",
        "definition": "Book V, Def. 3: 'A ratio is a sort of relation in respect of size between two magnitudes of the same kind.' Def. 4 requires that the magnitudes, when multiplied, are capable of exceeding one another.",
    },
    "same-ratio": {
        "headword": "In the same ratio / Proportion (ἐν τῷ αὐτῷ λόγῳ / ἀναλογία)",
        "language": "Euclidean Definition (Book V, Def. 5 & 6)",
        "translation": "Ἐν τῷ αὐτῷ λόγῳ μεγέθη λέγεται εἶναι...",
        "definition": "Eudoxus's celebrated equimultiple criterion (Book V, Def. 5) defining equality of ratios for both commensurable and incommensurable magnitudes.",
    },
    "alternando": {
        "headword": "Alternando (ἐναλλάξ)",
        "language": "Euclidean Proportion Operation (Book V, Def. 12)",
        "translation": "Alternate ratio (taking antecedent to antecedent as consequent to consequent)",
        "definition": "Book V, Def. 12: If A : B = C : D, then alternando A : C = B : D (proved in V.16).",
    },
    "invertendo": {
        "headword": "Invertendo (ἀνάπαλιν)",
        "language": "Euclidean Proportion Operation (Book V, Def. 13)",
        "translation": "Inverse ratio (taking consequent to antecedent)",
        "definition": "Book V, Def. 13: If A : B = C : D, then invertendo B : A = D : C (V.7 Porism).",
    },
    "componendo": {
        "headword": "Componendo (σύνθεσις λόγου / συνθέντι)",
        "language": "Euclidean Proportion Operation (Book V, Def. 14)",
        "translation": "Composition of a ratio (antecedent + consequent to consequent)",
        "definition": "Book V, Def. 14: If A : B = C : D, then componendo (A + B) : B = (C + D) : D (proved in V.18).",
    },
    "separando": {
        "headword": "Separando / Dividendo (διαίρεσις λόγου / διελόντι)",
        "language": "Euclidean Proportion Operation (Book V, Def. 15)",
        "translation": "Separation of a ratio (antecedent − consequent to consequent)",
        "definition": "Book V, Def. 15: If A : B = C : D, then separando (A − B) : B = (C − D) : D (proved in V.17).",
    },
    "convertendo": {
        "headword": "Convertendo (ἀναστροφὴ λόγου / ἀναστρέψαντι)",
        "language": "Euclidean Proportion Operation (Book V, Def. 16)",
        "translation": "Conversion of a ratio (antecedent to antecedent − consequent)",
        "definition": "Book V, Def. 16: If A : B = C : D, then convertendo A : (A − B) = C : (C − D) (V.19 Porism).",
    },
    "ex-aequali": {
        "headword": "Ex aequali (δι' ἴσου λόγος)",
        "language": "Euclidean Proportion Operation (Book V, Def. 17)",
        "translation": "Ratio ex aequali (taking extreme to extreme across ordered series of ratios)",
        "definition": "Book V, Def. 17: If A : B = D : E and B : C = E : F, then ex aequali A : C = D : F (proved in V.22; perturbed proportion in V.23).",
    },
    "extreme-and-mean-ratio": {
        "headword": "Extreme and mean ratio (ἄκρος καὶ μέσος λόγος)",
        "language": "Euclidean Definition (Book VI, Def. 3)",
        "translation": "Golden Section / Divine Proportion",
        "definition": "Book VI, Def. 3: 'A straight line is said to have been cut in extreme and mean ratio when, as the whole line is to the greater segment, so is the greater to the less.' (Constructed in II.11 and VI.30; applied to the pentagon, icosahedron, and dodecahedron in Book XIII).",
    },
    "unit": {
        "headword": "Unit (μονάς)",
        "language": "Euclidean Definition (Book VII, Def. 1)",
        "translation": "Μονάς ἐστιν, καθ' ἣν ἕκαστον τῶν ὄντων ἓν λέγεται",
        "definition": "Book VII, Def. 1: 'A unit is that by virtue of which each of the things that exist is called one.'",
    },
    "number": {
        "headword": "Number (ἀριθμός)",
        "language": "Euclidean Definition (Book VII, Def. 2)",
        "translation": "Ἀριθμὸς δὲ τὸ ἐκ μονάδων συγκείμενον πλῆθος",
        "definition": "Book VII, Def. 2: 'A number is a multitude composed of units.'",
    },
    "prime-number": {
        "headword": "Prime number (πρῶτος ἀριθμός)",
        "language": "Euclidean Definition (Book VII, Def. 11)",
        "translation": "Πρῶτος ἀριθμός ἐστιν ὁ μονάδι μόνῃ μετρούμενος",
        "definition": "Book VII, Def. 11: 'A prime number is that which is measured by a unit alone.' (Proved infinite in multitude in IX.20).",
    },
    "perfect-number": {
        "headword": "Perfect number (τέλειος ἀριθμός)",
        "language": "Euclidean Definition (Book VII, Def. 22)",
        "translation": "Τέλειος ἀριθμός ἐστιν ὁ τοῖς ἑαυτοῦ μέρεσιν ἴσος ὤν",
        "definition": "Book VII, Def. 22: 'A perfect number is that which is equal to its own parts.' (Constructed from prime sums of powers of two in IX.36).",
    },
    "commensurable": {
        "headword": "Commensurable (σύμμετρος)",
        "language": "Euclidean Definition (Book X, Def. 1)",
        "translation": "Σύμμετρα μεγέθη λέγεται τὰ τῷ αὐτῷ μέτρῳ μετρούμενα",
        "definition": "Book X, Def. 1: 'Those magnitudes are said to be commensurable which are measured by the same measure, and those incommensurable which cannot have any common measure.'",
    },
    "incommensurable": {
        "headword": "Incommensurable (ἀσύμμετρος)",
        "language": "Euclidean Definition (Book X, Def. 1)",
        "translation": "ἀσύμμετρα μεγέθη",
        "definition": "Book X, Def. 1: Magnitudes which cannot have any common measure.",
    },
    "rational": {
        "headword": "Rational straight line (ῥητή)",
        "language": "Euclidean Definition (Book X, Def. 3)",
        "translation": "ῥητὴ εὐθεῖα",
        "definition": "Book X, Def. 3: A straight line commensurable either in length and in square, or in square only, with the assigned straight line.",
    },
    "irrational": {
        "headword": "Irrational straight line (ἄλογος)",
        "language": "Euclidean Definition (Book X, Def. 3)",
        "translation": "ἄλογος εὐθεῖα",
        "definition": "Book X, Def. 3: A straight line incommensurable both in length and in square with the assigned rational straight line.",
    },
    "medial": {
        "headword": "Medial straight line (μέση)",
        "language": "Euclidean Definition (Book X. 21)",
        "translation": "μέση εὐθεῖα",
        "definition": "Book X.21: The side of an irrational rectangle contained by two rational straight lines commensurable in square only (equivalent to ⁴√k · ρ).",
    },
    "binomial": {
        "headword": "Binomial straight line (ἐκ δύο ὀνομάτων)",
        "language": "Euclidean Definition (Book X. 36)",
        "translation": "ἐκ δύο ὀνομάτων",
        "definition": "Book X.36: The irrational sum of two rational straight lines commensurable in square only; classified into six species in Book X Defs. II.",
    },
    "apotome": {
        "headword": "Apotome (ἀποτομή)",
        "language": "Euclidean Definition (Book X. 73)",
        "translation": "ἀποτομή",
        "definition": "Book X.73: The irrational remainder when a rational straight line commensurable in square only with the whole is subtracted from a rational straight line; classified into six species in Book X Defs. III.",
    },
    "protasis": {
        "headword": "Protasis (πρότασις)",
        "language": "Greek (Formal Division of a Proposition)",
        "translation": "Enunciation",
        "definition": "The first of the six formal divisions of a Euclidean proposition (Proclus, p. 203), stating in general terms what is given and what is sought.",
    },
    "ekthesis": {
        "headword": "Ekthesis (ἔκθεσις)",
        "language": "Greek (Formal Division of a Proposition)",
        "translation": "Setting-out",
        "definition": "The second formal division of a Euclidean proposition, instantiating the given data in a concrete geometric figure with lettered elements.",
    },
    "diorismos": {
        "headword": "Diorismos (διορισμός)",
        "language": "Greek (Formal Division of a Proposition)",
        "translation": "Definition / Specification (or Condition of Possibility)",
        "definition": "Either (1) the third formal division of a proposition restating the goal in terms of the particular figure, or (2) the determination of the limits/conditions under which a problem admits of a solution.",
    },
    "kataskeue": {
        "headword": "Kataskeue (κατασκευή)",
        "language": "Greek (Formal Division of a Proposition)",
        "translation": "Construction / Machinery",
        "definition": "The fourth formal division of a Euclidean proposition, adding auxiliary lines and circles justified by the Postulates or prior problems.",
    },
    "apodeixis": {
        "headword": "Apodeixis (ἀπόδειξις)",
        "language": "Greek (Formal Division of a Proposition)",
        "translation": "Proof / Demonstration",
        "definition": "The fifth formal division of a Euclidean proposition, drawing the deductive chain of assertions from the hypotheses, constructions, axioms, and prior propositions.",
    },
    "symperasma": {
        "headword": "Symperasma (συμπέρασμα)",
        "language": "Greek (Formal Division of a Proposition)",
        "translation": "Conclusion",
        "definition": "The sixth formal division of a Euclidean proposition, reverting to the general or particular statement and closing with Q.E.D. (ὅπερ ἔδει δεῖξαι) or Q.E.F. (ὅπερ ἔδει ποιῆσαι).",
    },
    "hoper-edei-deixai": {
        "headword": "ὅπερ ἔδει δεῖξαι (Q.E.D.)",
        "language": "Greek",
        "translation": "Being what it was required to prove (Quod erat demonstrandum)",
        "definition": "Euclid's canonical closing formula for every theorem.",
    },
    "hoper-edei-poiesai": {
        "headword": "ὅπερ ἔδει ποιῆσαι (Q.E.F.)",
        "language": "Greek",
        "translation": "Being what it was required to do (Quod erat faciendum)",
        "definition": "Euclid's canonical closing formula for every construction problem.",
    },
    "parabole-ton-chorion": {
        "headword": "παραβολὴ τῶν χωρίων",
        "language": "Greek",
        "translation": "Application of areas",
        "definition": "The Pythagorean geometric-algebraic method (Book I.44–45, Book II, Book VI.27–29) of applying a parallelogram equal to a given area along a given straight line—either exactly (παραβολή), in defect (ἔλλειψις), or in excess (ὑπερβολή).",
    },
    "koinai-ennoiai": {
        "headword": "κοιναὶ ἔννοιαι",
        "language": "Greek",
        "translation": "Common Notions (Axioms)",
        "definition": "Euclid's title for universal, self-evident axioms shared across sciences (called τὰ κοινά or ἀξιώματα by Aristotle).",
    },
    "aitema": {
        "headword": "αἴτημα (αἰτήματα)",
        "language": "Greek",
        "translation": "Postulate (Postulates)",
        "definition": "First principles specific to geometry requesting the constructibility of straight lines and circles and the properties of right angles and intersecting lines.",
    },
    "horos": {
        "headword": "ὅρος (ὅροι)",
        "language": "Greek",
        "translation": "Definition / Boundary",
        "definition": "A definition delimiting the meaning of a geometric or arithmetic term.",
    },
    "eis-to-adynaton": {
        "headword": "ἡ εἰς τὸ ἀδύνατον ἀπαγωγή",
        "language": "Greek",
        "translation": "Reduction to the impossible (reductio ad absurdum)",
        "definition": "Indirect demonstration proving a proposition by showing that its contradiction leads to an impossibility.",
    },
    "reductio-ad-absurdum": {
        "headword": "reductio ad absurdum",
        "language": "Latin (Logical)",
        "translation": "Reduction to absurdity / the impossible (ἡ εἰς τὸ ἀδύνατον ἀπαγωγή)",
        "definition": "Indirect proof establishing a truth by deducing a contradiction from the denial of the conclusion.",
    },
    "method-of-exhaustion": {
        "headword": "Method of exhaustion",
        "language": "Mathematical Method (Book XII)",
        "translation": "Exhaustion by inscribed/circumscribed polygons or polyhedra (Eudoxus & Archimedes)",
        "definition": "Rigorous Greek limiting method grounded in Book X.1 (and Book V Def. 4) avoiding actual infinitesimals via double reductio ad absurdum.",
    },
}


def normalize_person_slug(slug: str) -> str:
    s = slug.strip().lower().replace("_", "-")
    extra = {
        "francois-peyrard": "peyrard",
        "friedrich-hultsch": "hultsch",
        "johann-wilhelm-camerer": "camerer",
        "jacques-peletier": "peletier",
        "andreas-tacquet": "tacquet",
        "francois-de-foix-candalle": "candalle",
    }
    s = PERSON_ALIAS_MAP.get(s, s)
    return extra.get(s, s)


def normalize_cite_target(target: str) -> str:
    t = target.strip()
    parts = t.split(":")
    if len(parts) >= 2:
        raw_prefix = f"{parts[0]}:{parts[1]}"
        norm_prefix = CITE_PREFIX_MAP.get(raw_prefix, raw_prefix.replace("_", "-"))
        locus = ":".join(parts[2:])
        return f"{norm_prefix}:{locus}" if locus else norm_prefix
    return CITE_PREFIX_MAP.get(t, t.replace("_", "-"))


def normalize_term_slug(slug: str) -> str:
    s = slug.strip().lower().replace("_", "-")
    return TERM_ALIAS_MAP.get(s, s)


def infer_term_language(headword: str, slug: str, raw_displays: List[str]) -> str:
    if slug in TERM_CATALOG:
        return TERM_CATALOG[slug]["language"]
    if any(d.startswith("**") and d.endswith("**") for d in raw_displays):
        return "Euclidean Definition"
    if any("\u0370" <= ch <= "\u03ff" or "\u1f00" <= ch <= "\u1fff" for ch in headword):
        return "Greek"
    if slug in ("a-fortiori", "ad-infinitum", "ex-aequali", "mutatis-mutandis", "reductio-ad-absurdum", "alternando", "invertendo", "componendo", "separando", "convertendo", "dirimendo", "dividendo", "permutando"):
        return "Latin (Mathematical)"
    return "Mathematical Term"


def strip_inline_markup(s: str) -> str:
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    return s.strip()


def harvest_euclid_definitions() -> Dict[str, str]:
    """Extract verbatim definition sentences from all Euclid folios where `:term:`**...** <slug>`` appears."""
    defs: Dict[str, str] = {}
    for vol in VOLUMES:
        for p in sorted((EDITION_ROOT / vol).rglob("*.rst")):
            if p.name.endswith(".notes.rst"):
                continue
            text = p.read_text(encoding="utf-8")
            if ":term:`**" not in text:
                continue
            book = ""
            for line in text.splitlines():
                if not line.strip():
                    break
                m = re.match(r"^:book:\s*(.+)$", line)
                if m:
                    book = m.group(1).strip()
            for para in re.split(r"\n\s*\n", text):
                if ":term:`**" in para:
                    clean_para = re.sub(
                        r":(?:term|cite|person|g|just|line):`([^`<]+?)(?:\s*<[^>]+>)?`",
                        lambda m: strip_inline_markup(m.group(1)),
                        para,
                    )
                    clean_para = re.sub(r"^\|\s*", "", clean_para, flags=re.MULTILINE)
                    clean_para = re.sub(r"\s+", " ", clean_para).strip()
                    for tm in re.finditer(r":term:`\*\*[^`]+\*\*\s*<([^>]+)>`", para):
                        slug = normalize_term_slug(tm.group(1))
                        prefix = f"Book {book}: " if book else ""
                        if slug not in defs:
                            defs[slug] = f"{prefix}{clean_para}"
    return defs


def harvest_greek_indices() -> Dict[str, Tuple[str, str]]:
    """Harvest Greek headwords and Heath's index glosses from the Greek Indices of Vols. I–III."""
    greek_glosses: Dict[str, Tuple[str, str]] = {}
    index_dirs = [
        EDITION_ROOT / "volume_I" / "index_of_greek_words_and_forms",
        EDITION_ROOT / "volume_II" / "indexofgreekwordsandforms",
        EDITION_ROOT / "volume_III" / "general_index_of_greek_words",
    ]
    for d in index_dirs:
        if not d.exists():
            continue
        for p in sorted(d.glob("*.rst")):
            if p.name.endswith(".notes.rst"):
                continue
            for line in p.read_text(encoding="utf-8").splitlines():
                m = re.match(r"^-\s+([^\s,:]+(?:\s+[^\s,:]+)?)\s*[,:]\s*(.+)$", line.strip())
                if m:
                    gw = strip_inline_markup(m.group(1)).strip("()")
                    gloss = strip_inline_markup(m.group(2))
                    greek_glosses[gw] = (gw, f"Heath Greek Index: {gw} — {gloss}")
    return greek_glosses


def main() -> None:
    euclid_defs = harvest_euclid_definitions()
    greek_glosses = harvest_greek_indices()

    citations_registry: Dict[str, Dict[str, Any]] = {}
    glossary_registry: Dict[str, Dict[str, Any]] = {}
    persons_registry: Dict[str, Dict[str, Any]] = {}
    term_raw_displays: Dict[str, List[str]] = {}

    normalized_files = 0

    for vol in VOLUMES:
        vol_dir = EDITION_ROOT / vol
        rst_files = sorted([p for p in vol_dir.rglob("*.rst") if not p.name.endswith(".notes.rst")])

        for p in rst_files:
            text = p.read_text(encoding="utf-8")
            orig_text = text

            meta: Dict[str, str] = {}
            for line in text.splitlines():
                if not line.strip():
                    break
                m = re.match(r"^:([A-Za-z0-9_.-]+):\s*(.*)$", line)
                if m:
                    meta[m.group(1)] = m.group(2).strip()

            folio = meta.get("folio", p.stem)
            page = meta.get("page", folio)
            book = meta.get("book", "")
            section = meta.get("section", p.parent.name)

            # Normalize :cite:
            def _norm_cite(m: re.Match) -> str:
                c = m.group(1)
                cm = re.match(r"^(.*?)\s*<([^>]+)>$", c)
                if cm:
                    disp, key = cm.group(1).strip(), normalize_cite_target(cm.group(2))
                else:
                    disp, key = c.strip(), normalize_cite_target(c.strip().lower())
                return f":cite:`{disp} <{key}>`"

            # Normalize :term:
            def _norm_term(m: re.Match) -> str:
                c = m.group(1)
                tm = re.match(r"^(.*?)\s*<([^>]+)>$", c)
                if tm:
                    disp, key = tm.group(1).strip(), normalize_term_slug(tm.group(2))
                else:
                    disp, key = c.strip(), normalize_term_slug(c.strip().lower())
                return f":term:`{disp} <{key}>`"

            # Normalize :person:
            def _norm_person(m: re.Match) -> str:
                c = m.group(1)
                pm = re.match(r"^(.*?)\s*<([^>]+)>$", c)
                if pm:
                    disp, key = pm.group(1).strip(), normalize_person_slug(pm.group(2))
                else:
                    disp, key = c.strip(), normalize_person_slug(c.strip().lower())
                return f":person:`{disp} <{key}>`"

            text = re.sub(r":cite:`([^`]+)`", _norm_cite, text)
            text = re.sub(r":term:`([^`]+)`", _norm_term, text)
            text = re.sub(r":person:`([^`]+)`", _norm_person, text)

            if text != orig_text:
                p.write_text(text, encoding="utf-8")
                normalized_files += 1

            # Extract body after metadata
            lines = text.splitlines()
            idx = 0
            while idx < len(lines) and lines[idx].strip():
                idx += 1
            body = "\n".join(lines[idx:])

            # Collect :cite:
            for m in re.finditer(r":cite:`([^`]+)`", body):
                cm = re.match(r"^(.*?)\s*<([^>]+)>$", m.group(1))
                if not cm:
                    continue
                disp, target = cm.group(1).strip(), cm.group(2).strip()
                parts = target.split(":")
                author_key = normalize_person_slug(parts[0])
                work_prefix = ":".join(parts[:2]) if len(parts) >= 2 else author_key
                locus = ":".join(parts[2:]) if len(parts) > 2 else ""

                if work_prefix in WORK_TITLES:
                    author_name, work_title = WORK_TITLES[work_prefix]
                elif author_key in PERSON_CATALOG:
                    author_name = PERSON_CATALOG[author_key]["name"]
                    work_title = parts[1].replace("-", " ").title() if len(parts) >= 2 else target
                else:
                    author_name = author_key.replace("-", " ").title()
                    work_title = parts[1].replace("-", " ").title() if len(parts) >= 2 else target

                c_entry = citations_registry.setdefault(
                    target,
                    {
                        "key": target,
                        "author_key": author_key,
                        "work_key": work_prefix,
                        "locus": locus,
                        "author": author_name,
                        "work": work_title,
                        "occurrences": [],
                    },
                )
                c_entry["occurrences"].append(
                    {
                        "volume": vol,
                        "folio": folio,
                        "page": page,
                        "book": book,
                        "section": section,
                        "display": strip_inline_markup(disp),
                    }
                )

            # Collect :term:
            for m in re.finditer(r":term:`([^`]+)`", body):
                tm = re.match(r"^(.*?)\s*<([^>]+)>$", m.group(1))
                if not tm:
                    continue
                disp, slug = tm.group(1).strip(), tm.group(2).strip()
                term_raw_displays.setdefault(slug, []).append(disp)
                clean_disp = strip_inline_markup(disp)
                cat = TERM_CATALOG.get(slug, {})
                headword = cat.get("headword", clean_disp)
                lang = infer_term_language(headword, slug, term_raw_displays[slug])
                translation = cat.get("translation", slug.replace("-", " "))
                if slug in TERM_CATALOG:
                    definition = TERM_CATALOG[slug]["definition"]
                elif slug in euclid_defs:
                    definition = euclid_defs[slug]
                elif clean_disp in greek_glosses:
                    definition = greek_glosses[clean_disp][1]
                else:
                    definition = f"Technical geometric or mathematical term in Heath's edition of Euclid's Elements ({lang})."

                t_entry = glossary_registry.setdefault(
                    slug,
                    {
                        "slug": slug,
                        "headword": headword,
                        "language": lang,
                        "translation": translation,
                        "definition": definition,
                        "occurrences": [],
                    },
                )
                if lang == "Euclidean Definition" and t_entry["language"] != "Euclidean Definition":
                    t_entry["language"] = lang
                if slug in euclid_defs and "Heath's edition" in t_entry["definition"]:
                    t_entry["definition"] = euclid_defs[slug]
                elif clean_disp in greek_glosses and "Heath's edition" in t_entry["definition"]:
                    t_entry["definition"] = greek_glosses[clean_disp][1]

                t_entry["occurrences"].append(
                    {
                        "volume": vol,
                        "folio": folio,
                        "page": page,
                        "book": book,
                        "section": section,
                        "display": clean_disp,
                    }
                )

            # Collect :person:
            for m in re.finditer(r":person:`([^`]+)`", body):
                pm = re.match(r"^(.*?)\s*<([^>]+)>$", m.group(1))
                if not pm:
                    continue
                disp, slug = pm.group(1).strip(), pm.group(2).strip()
                clean_disp = strip_inline_markup(disp)
                pcat = PERSON_CATALOG.get(slug, {})
                name = pcat.get("name", clean_disp if len(clean_disp) > 3 else slug.replace("-", " ").title())
                dates = pcat.get("dates", "")
                role = pcat.get("role", "Mathematician / Commentator / Scholar")
                bio = pcat.get(
                    "bio",
                    f"Historical mathematician, philosopher, commentator, or modern scholar cited in Heath's edition of Euclid's Elements.",
                )
                works = pcat.get("works", [])

                p_entry = persons_registry.setdefault(
                    slug,
                    {
                        "slug": slug,
                        "name": name,
                        "dates": dates,
                        "role": role,
                        "bio": bio,
                        "works": works,
                        "occurrences": [],
                    },
                )
                p_entry["occurrences"].append(
                    {
                        "volume": vol,
                        "folio": folio,
                        "page": page,
                        "book": book,
                        "section": section,
                        "display": clean_disp,
                    }
                )

    # Also merge citation-derived author occurrences into persons_registry
    for target, c_entry in citations_registry.items():
        ak = c_entry["author_key"]
        if ak in persons_registry:
            p_entry = persons_registry[ak]
            seen = {f"{o['volume']}:{o['folio']}" for o in p_entry["occurrences"]}
            for occ in c_entry["occurrences"]:
                vf = f"{occ['volume']}:{occ['folio']}"
                if vf not in seen:
                    p_entry["occurrences"].append(occ)
                    seen.add(vf)
            if c_entry["work"] and c_entry["work"] not in p_entry["works"]:
                p_entry["works"].append(c_entry["work"])

    # Populate work_occurrences for citations across all 3 volumes
    work_folios: Dict[str, List[Dict[str, str]]] = {}
    for target, entry in citations_registry.items():
        wk = entry["work_key"]
        seen = {f"{o['volume']}:{o['folio']}" for o in work_folios.get(wk, [])}
        for occ in entry["occurrences"]:
            vf = f"{occ['volume']}:{occ['folio']}"
            if vf not in seen:
                work_folios.setdefault(wk, []).append(occ)
                seen.add(vf)

    for target, entry in citations_registry.items():
        entry["work_occurrences"] = work_folios.get(entry["work_key"], entry["occurrences"])

    (EDITION_ROOT / "citations.json").write_text(
        json.dumps(dict(sorted(citations_registry.items())), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (EDITION_ROOT / "glossary.json").write_text(
        json.dumps(dict(sorted(glossary_registry.items())), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (EDITION_ROOT / "persons.json").write_text(
        json.dumps(dict(sorted(persons_registry.items())), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(
        f"Normalized {normalized_files} files across Volumes I–III. "
        f"Built citations.json ({len(citations_registry)} keys), "
        f"glossary.json ({len(glossary_registry)} terms), "
        f"persons.json ({len(persons_registry)} persons)."
    )


if __name__ == "__main__":
    main()
