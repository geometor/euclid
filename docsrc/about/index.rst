:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-euclid:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

**GEOMETOR • euclid** is the primary textual, archival, and visual source of truth for **Euclid of Alexandria** (c. 300 BCE) within the GEOMETOR Digital Scriptorium. Created and curated by **phi ARCHITECT**, the edition unites the monumental scholarship of Sir Thomas L. Heath's definitive three-volume critical edition of *The Thirteen Books of Euclid's Elements* (Cambridge University Press, 1908; 2nd ed. 1926) with a synchronized four-track bilingual **Book Codex** of Euclid's *Data* (*Δεδομένα*), based on Heinrich Menge's 1896 Teubner Greek critical text and Robert Simson's historical edition. Spanning **1,416 archival folios and 831 calibrated geometric vector diagrams**, this edition establishes an authoritative digital repository preserving the foundational canon of Western mathematics.

Every unit across the *Elements* and *Data* has been extracted into machine-addressable semantic structures. Historical prose is de-paginated and anchored by exact archival folio markers (``publish folio``), while enunciations, proofs, and critical commentaries are presented through synchronized multi-track interfaces. Demonstrations feature bidirectional visual indications (``:g:`` and ``:eq:``) linking mathematical expressions directly to primitives in calibrated ``.euclid-graphic`` SVGs, alongside explicit justification indicators (``:just:``) that expose the underlying deductive dependency chain connecting propositions across all thirteen books.

Within the GEOMETOR ecosystem, ``geometor.euclid`` provides the textual and geometric foundation for the entire computational library. It supplies the formal propositions, definitions, and citations compiled into the computable G-Index directed acyclic graph (``G.1``–``G.601``) in ``geometor.elements``. It establishes the primary axiomatic source for the extreme and mean ratio theorems verified in ``geometor.divine``, supports the ancient analytical frameworks of ``geometor.pappus`` (*Collection*, Book VII), and connects directly with Renaissance renewals in Luca Pacioli's ``geometor.pacioli`` (*De Divina Proportione*, 1509) and Albrecht Dürer's ``geometor.durer`` (*Underweysung der Messung*, 1525).

The GEOMETOR Mission
--------------------

Founded by **phi ARCHITECT**, the GEOMETOR project is dedicated to three foundational pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. GEOMETOR elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Anchoring geometric constructions in 100% exact symbolic algebra (`SymPy <https://www.sympy.org>`_) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than floating-point approximations. Every geometric theorem and construction is mathematically verified and permanently reproducible.

Repurposing Knowledge Across Mediums
    Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

The Digital Scriptorium edition of *The Thirteen Books of the Elements* and *Data* is established on authoritative critical editions and primary archival witnesses:

- **Sir Thomas Little Heath**: *The Thirteen Books of Euclid's Elements, translated from the text of Heiberg with introduction and commentary*, 3 vols. (Cambridge University Press, 1908; 2nd revised ed., 1926; Dover Publications reprint).
- **Johan Ludvig Heiberg**: *Euclidis Elementa*, 5 vols. in *Euclidis Opera Omnia* (Leipzig: B.G. Teubner, 1883–1888), establishing the standard modern Greek critical text.
- **Heinrich Menge**: *Euclidis Data cum Commentario Marini et Scholiis Antiquis*, vol. VI in *Euclidis Opera Omnia* (Leipzig: B.G. Teubner, 1896).
- **Robert Simson**: *The Elements of Euclid, viz. The First Six Books, together with the Eleventh and Twelfth... Also the Book of Euclid's Data* (Glasgow: Robert and Andrew Foulis, 1756).
- **Primary Manuscript Witnesses**: Collation against *Codex Vaticanus Graecus 190* (10th c., Vatican Library) and *Codex Bodleianus MS. D'Orville 301* (copied 888 CE by Stephen the Clerk, Bodleian Library, Oxford).
- **Digital Scriptorium Methodology**: Reconstructing historical typography, apparatus criticus, and mathematical diagrams into high-resolution vector assets and structured reStructuredText codices compiled via the Photon Publisher framework.
