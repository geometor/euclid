GEOMETOR • euclid
=================

.. image:: https://img.shields.io/github/license/geometor/euclid.svg
   :target: https://github.com/geometor/euclid/blob/main/LICENSE

**Digital reconstruction, semantic discovery, and critical edition of Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements*.**

Overview
--------

``geometor.euclid`` is the primary textual and visual source of truth for Euclid's *Elements* in the GEOMETOR ecosystem. It transforms the three volumes of Sir Thomas L. Heath's 1926 Cambridge/Dover critical edition (1,416 archival folios and 831 geometric diagrams) into a de-paginated, semantically tagged **Book Codex** edition powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_.

While ``geometor.euclid`` performs **semantic discovery**—preserving Heath's complete translation, historical introductions, critical commentary, and folio provenance—its sister repository `geometor/elements <https://github.com/geometor/elements>`_ consumes the compiled ``docsrc/heath/`` tree to generate the symbolic **G-Index** (`G.1`–`G.525`).

Process & Pipeline
------------------

1. **Archival Folio Ingestion & Interactive Review (``resources/heath/``)**:
   - Each of the 1,416 printed pages across Volumes I–III is stored as a high-resolution scan (``<NNNN>.png``), diplomatic RST transcription (``<NNNN>.rst``), editorial note file (``<NNNN>.notes.rst``), and SVG diagram set (``<NNNN>.g1.svg``).
   - Reviewed side-by-side in the ``publish folio`` web workstation to verify Greek/Latin orthography, mathematical expressions, footnotes, and geometric primitive labels.

2. **SVG Bounding-Box Recalibration & Theme Normalization (``scripts/recalibrate_svgs.py``)**:
   - Computes tight vector bounding boxes (`viewBox`, `width`, `height`) across all 831 geometric SVGs and normalizes stroke/fill classes so diagrams adapt seamlessly between warm parchment light mode and obsidian dark mode.

3. **De-Pagination & Edition Compilation (``compile_edition.py``)**:
   - Merges folio-level transcriptions across page breaks into logical structural units—Introductory Chapters, Definitions, Postulates, Common Notions, and Propositions across Books I–XIII—while injecting marginal ``.. folio::`` markers to preserve exact page provenance.
   - Splits each proposition into a **2-track Book Codex**:
     - **Proposition Track (`index.rst`)**: Formal ``.. enunciation::``, interactive ``.. picture::`` SVG diagram, proof narrative with ``:g:`` geometric primitive roles and ``:just:`` justification pills, and Q.E.D./Q.E.F. conclusion.
     - **Commentary Track (`commentary.rst`)**: Heath's line-by-line philological, historical, and mathematical notes linked to the proposition via ``.. note_item::`` blocks.
   - Compiles the scholarly apparatus registries (`resources/citations.json`, `resources/persons.json`, `resources/glossary.json`) and generates `docsrc/heath/bibliography.rst`, `docsrc/heath/persons.rst`, and `docsrc/heath/glossary.rst`.

Feature Set & Coordination with ``publish``
-------------------------------------------

- **2-Track Book Codex (``:layout: book``)**: Synchronized **Proposition** and **Commentary** tabs in the sticky reading-pane header with track-preserving ``Prev`` / ``Next`` navigation across every book of the *Elements*.
- **Interactive Geometric Indications (``:g:``, ``:eq:``, ``:just:``)**:
  - Hovering or clicking any ``:g:`` reference in the proof text highlights the corresponding point, line, circle, angle, or polygon in the SVG figure (and vice versa).
  - ``:just:`` justification pills resolve to their target definition, postulate, common notion, or proposition and display its ``.. enunciation::`` text in a live hover tooltip.
- **Scholarly Apparatus (``:cite:``, ``:person:``, ``:term:``)**: Interactive citations, prosopographical entries (from Thales and Eudoxus to Heiberg and Heath), and Greek/English technical glossary terms.
- **Cross-Repository Intersphinx**: Exports ``docs/objects.inv`` so `geometor/elements <https://github.com/geometor/elements>`_, `geometor/pacioli <https://github.com/geometor/pacioli>`_, and `geometor/etc <https://github.com/geometor/etc>`_ can deep-link directly to any Euclidean definition, postulate, common notion, or proposition.

Usage
-----

.. code-block:: bash

   # Launch the side-by-side Folio Reviewer on resources/heath/
   publish folio

   # Compile the 3-volume Heath Edition from resources/heath/ into docsrc/heath/
   python3 -m geometor.euclid.compile_edition

   # Build and serve the Book Codex documentation locally
   publish test

Resources & Related Projects
----------------------------

- **Live Edition**: https://geometor.github.io/euclid
- **Source Code**: https://github.com/geometor/euclid
- `GEOMETOR • elements <https://github.com/geometor/elements>`_: Symbolic G-Index (`G.1`–`G.525`), formal pseudocode signatures, and composable constructions.
- `GEOMETOR • model <https://github.com/geometor/model>`_: Symbolic compass-and-straightedge construction engine.
- `PHOTON • publish <https://github.com/photon-platform/publish>`_: Sphinx Book Codex publishing engine and theme.
