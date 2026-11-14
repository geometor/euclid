:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive GEOMETOR Digital Edition

Welcome to the GEOMETOR digital critical edition of Euclid's *Elements* and *Data*. This site offers an immersive, multifaceted reading environment bridging historical print editions, polytonic Greek witnesses, and modern computational geometry.

Reader's Guide
--------------

Synchronized Reading Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every unit and proposition in the Book Codices provides synchronized tracks selectable from the book header bar:

* **Elements Tracks**: Switch between **Proposition** (clean mathematical statement and proof with recalibrated SVG figures) and **Commentary** (Heath's extensive historical and philosophical annotations).
* **Data Tracks**: Select among four synchronized views:
  
  1. **Proposition (English)**: Complete literal translation of Marinus's *Protheoria* and Euclid's Propositions `D.1`–`D.94` with interactive SVG diagrams.
  2. **Greek (Menge 1896)**: Polytonic Greek critical text established by Heinrich Menge from Codex Vaticanus Graecus 190.
  3. **Summary**: Formal functional signatures ``Given(...) -> Determined(...)`` and dependency summaries for computational modeling.
  4. **Notes**: Manuscript variations (`Vat. gr. 190` vs. Theonine recension), *diorismoi*, and ancient scholia.

Primary-Source Folio Milestones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Over **1,416 archival folio scans** are indexed across this edition:

* Click any marginal **[p. N]** or **[f. N]** link in the text to reveal the corresponding archival page milestone.
* Click the **Folio** badge in the chapter header bar to inspect high-resolution scans of the primary witness (Heath 1926 or Menge 1896 Teubner edition).

Interactive Diagrams & Deductive Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The geometric figures are rendered as live, responsive SVGs linked to the proof text:

* **Geometric Elements (``:g:``)**: Hovering over or clicking a geometric label (such as :g:`AB`) highlights the corresponding line, vertex, or polygon in the SVG diagram.
* **Symbolic Equations (``:eq:``)**: Equational assertions cross-illuminate the relevant components of the geometric figure.
* **Justification Pills (``:just:``)**: In *Data*, justification pills like :just:`[I.47] <I.47>` link directly to the corresponding proposition in the *Elements*.

Full-Text Search with In-Page Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The site-wide search index enables deep query across English translations, Greek terms, and commentary:

* Use the search bar in the sidebar or navigation menu to locate specific terms or Greek keywords.
* Search results automatically pass the ``?highlight=`` parameter to highlight matched terms directly within chapters and proposition pages.

Categories, Tags, Document Types & Collection Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Explore the corpus through multifaceted taxonomy views:

* **Sidebar Facets**: Browse documents filtered by category, topic tag, or document type.
* **Collection View Toggles**: On collection index pages, switch seamlessly between **Cards**, **Banners**, and **List** views using the interactive layout buttons.

People, Bibliography & Apparatus Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scholarly entities throughout the text feature rich interactive cards:

* Hover over any :person:`person link` to see dates, roles, and historical significance.
* Hover over any :cite:`citation` to preview bibliographic details.
* Hover over any :term:`glossary term` for Greek definitions and etymology.
* Toggle the **Light/Dark theme** switch in the upper corner for comfortable reading in any lighting condition.

Workflow Commands
-----------------

For contributors and researchers developing or building ``geometor.euclid`` locally:

.. code-block:: bash

   # Launch the side-by-side Folio Review web UI
   uv run folio-review

   # Compile folio-reviewed RST sources into docsrc/heath/
   python3 -m geometor.euclid.compile_edition

   # Recalibrate SVG bounding boxes and light/dark theme classes
   python3 scripts/recalibrate_svgs.py

   # Build the HTML documentation into docs/
   publish build

Guides & Reference
------------------

.. collection::
   :sort: order
