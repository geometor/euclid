:navigation: header
:order: 20

=====
usage
=====

``geometor.euclid`` provides tools for folio-by-folio transcription review, SVG diagram recalibration, and compiling the 3-volume Heath Edition into a ``photon-platform/publish`` Book Codex.

Workflow Commands
-----------------

.. code-block:: bash

   # Launch the side-by-side Folio Review web UI
   uv run folio-review

   # Compile folio-reviewed RST sources into docsrc/heath/
   python3 -m geometor.euclid.compile_edition

   # Recalibrate SVG bounding boxes and light/dark theme classes
   python3 scripts/recalibrate_svgs.py

   # Build the HTML documentation into docs/
   publish build

Guides
------

.. collection::
   :sort: order
