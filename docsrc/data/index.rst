:navigation: header
:order: 2
:nav_title: Data
:layout: book
:book_title: Euclid's Data
:book_subtitle: Δεδομένα — Bilingual Critical Edition (Menge 1896 & Simson 1806)
:author: Euclid of Alexandria · Protheoria by Marinus of Neapolis
:publisher: GEOMETOR Digital Scriptorium
:year: c. 300 BCE / 1896

.. _euclid-data-codex:

====
Data
====

.. rubric:: *Δεδομένα* — Bilingual Critical Edition (Menge 1896 & Simson 1806)

.. container:: title-page

   | **Author:** :person:`Euclid of Alexandria <euclid>` (fl. c. 300 BCE)
   | **Protheoria:** :person:`Marinus of Neapolis <marinus>` (c. 440 – c. 495 CE)
   | **Critical Greek Edition:** :person:`Heinrich Menge <menge>` (*Euclidis Opera Omnia*, Vol. VI, Leipzig: B. G. Teubner, 1896)
   | **Critical Reconstruction:** :person:`Robert Simson <simson>` (Glasgow 1762 / London 1806)
   | **Mathematical Analysis:** :person:`Sir Thomas Little Heath <heath>` (Oxford 1921 / Cambridge 1926)
   | **GEOMETOR Edition:** Synchronized 4-Track Bilingual Codex · English · Greek · Summary · Notes

*A Synchronized Four-Track Bilingual Book Codex of the Foundation of the Ancient Treasury of Analysis (*:term:`ὁ ἀναλυόμενος τόπος <analyomenos-topos>`*)*

Composed by :person:`Euclid of Alexandria <euclid>` alongside the thirteen books of the :doc:`Elements <../heath/index>`, the **Data** (*Δεδομένα*, *Dedomena*) is the algorithmic and epistemological grammar of Greek geometric problem-solving. Where the *Elements* proceeds by :term:`synthesis <synthesis>` to construct figures and demonstrate static properties, the *Data* establishes **functional determinacy**: given certain magnitudes, ratios, angles, or loci in hypothesis, what further geometric entities are thereby uniquely *procurable* (:term:`πόριμον <porimon>`)?

This GEOMETOR Digital Scriptorium edition presents the complete non-Theonine Greek text established by :person:`Heinrich Menge <menge>` from the ninth-century Vatican archetype :cite:`Vat. gr. 190 (Codex P) <vat-gr-190>` (:cite:`Euclidis Opera Omnia, Vol. VI, 1896 <menge:1896>`), prefaced by the fifth-century philosophical commentary (*Protheoria*) of :person:`Marinus of Neapolis <marinus>`, and collated throughout with :person:`Robert Simson's <simson>` landmark critical reconstruction (:cite:`1762 / 1806 <simson:1762>`) and :person:`Sir Thomas Heath's <heath>` mathematical analysis (:cite:`1921 <heath:1921>`, :cite:`1926 <heath:1926>`).

Each thematic unit is organized into **four synchronized tracks** selectable from the Book Codex header bar:

1. **Proposition (English)** — Complete literal translation of Marinus's *Protheoria* (§§ 1–18), Definitions 1–15, and Propositions 1–94 (`D.1`–`D.94`), wired with interactive ``.euclid-graphic`` SVGs, ``:g:`` geometric highlights, and live ``:just:`` justification pills linking directly into the :doc:`Heath Elements <../heath/index>`.
2. **Greek (Menge 1896)** — Complete polytonic Greek text of Marinus and Euclid with marginal ``.. folio::`` milestones keyed to Menge's 1896 Teubner pagination.
3. **Summary** — Functional ``Given(...) -> Determined(...)`` signatures, constructive dependency tables, and computational primitives for ``geometor.model``.
4. **Notes** — Textual criticism (`Vat. gr. 190` vs. Theonine recension vs. Simson), *diorismoi*, and cross-corpus links to :person:`Pappus <pappus>` (*Synagoge* VII), :person:`Julius Petersen <petersen>` (*Methods and Theories*, 1879), and :person:`Nathan Altshiller-Court <altshiller-court>` (*College Geometry*, 1952).

Functional Architecture of the *Data*
-------------------------------------

.. picture:: /_static/figures/data_08_functional_dag.svg
   :alt: Functional Dependency Architecture of Euclid's Data (Units 0–6)

Interactive architecture map: :g:`Unit 0 (Protheoria & Defs. 1–15) <data_08_functional_dag:U0>` grounds the modes of givenness alongside :g:`Euclid's Elements I–VI <data_08_functional_dag:ELM>`. From these rise :g:`Unit 1 (Magnitudes & Ratios, D.1–24) <data_08_functional_dag:U1>` and :g:`Unit 2 (Position & Parallel Loci, D.25–38) <data_08_functional_dag:U2>`, converging in :g:`Unit 3 (Triangle & Polygon Species, D.39–55) <data_08_functional_dag:U3>`, branching through :g:`Unit 4 (Area Application & Cosine Metric, D.56–67) <data_08_functional_dag:U4>` and :g:`Unit 5 (Proportional Figures, D.68–83) <data_08_functional_dag:U5>`, and culminating in :g:`Unit 6 (Quadratic Systems & Circle Loci, D.84–94) <data_08_functional_dag:U6>`—powering :g:`Pappus's Treasury of Analysis (Synagoge VII) <data_08_functional_dag:SYN>`.

Table of Contents
-----------------

.. collection::
   :type: chapter
   :sort: order

.. toctree::
   :hidden:

   unit-0-protheoria-definitions/protheoria-el
   unit-0-protheoria-definitions/protheoria-summary
   unit-0-protheoria-definitions/protheoria-notes
   unit-1-magnitudes-ratios/magnitudes-el
   unit-1-magnitudes-ratios/magnitudes-summary
   unit-1-magnitudes-ratios/magnitudes-notes
   unit-2-position-parallels/position-el
   unit-2-position-parallels/position-summary
   unit-2-position-parallels/position-notes
   unit-3-triangles-species/triangles-el
   unit-3-triangles-species/triangles-summary
   unit-3-triangles-species/triangles-notes
   unit-4-areas-quadratics/areas-el
   unit-4-areas-quadratics/areas-summary
   unit-4-areas-quadratics/areas-notes
   unit-5-proportional-figures/proportional-el
   unit-5-proportional-figures/proportional-summary
   unit-5-proportional-figures/proportional-notes
   unit-6-circles-chords/circles-el
   unit-6-circles-chords/circles-summary
   unit-6-circles-chords/circles-notes

Scholarly Apparatus
-------------------

.. toctree::
   :maxdepth: 1

   concordance
   bibliography
   persons
   glossary
