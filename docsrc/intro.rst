**Digital reconstruction, semantic discovery, and critical edition of Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements*.**

``geometor.euclid`` is the primary textual and visual source of truth for Euclid's *Elements* in the GEOMETOR ecosystem. It transforms the three volumes of Sir Thomas L. Heath's 1926 Cambridge/Dover critical edition (1,416 archival folios and 831 recalibrated geometric SVGs) into a de-paginated, semantically tagged **Book Codex** edition powered by ``photon-platform/publish``.

----

Edition Highlights
------------------

* :doc:`The Heath Edition (Volumes I–III) <heath/index>` — Complete de-paginated text of Books I–XIII with marginal ``.. folio::`` markers, interactive SVG diagrams, and synchronized **Proposition** and **Commentary** tracks.
* **Scholarly Apparatus** — :doc:`Bibliography <heath/bibliography>` · :doc:`Index of Persons <heath/persons>` · :doc:`Technical Glossary <heath/glossary>` with interactive ``:cite:``, ``:person:``, and ``:term:`` hover cards.
* **Interactive Geometry & Justifications** — Bidirectional ``:g:`` highlighting between proof text and SVG primitives, plus ``:just:`` justification pills with live enunciation tooltips.
* **Downstream Symbolic Codex** — Feeds the compiled ``docsrc/heath/`` tree and ``objects.inv`` inventory into `GEOMETOR • elements <https://geometor.github.io/elements>`_ to generate the 525-node **G-Index** (`G.1`–`G.525`).