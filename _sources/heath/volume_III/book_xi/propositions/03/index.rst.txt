:canonical_id: XI.3
:volume: III
:book: XI
:proposition: 3
:type: proposition
:title: Proposition XI.3
:folios: 0280
:pages: 276
:dependencies: I.def.4, I.def.7

.. _XI.3:

.. folio:: 0280
   :page: 276

PROPOSITION 3.
==============

.. enunciation::

   If two :term:`planes <plane-surface>` cut one another, their common section is a :term:`straight line <straight-line>`.

For let the two planes :g:`AB <0280.g1:< A B >>`, :g:`BC <0280.g1:< B C >>` cut one another, and let the :term:`line <line>` :g:`DB <0280.g1:/ D B />` be their common section; I say that the line :g:`DB <0280.g1:/ D B />` is a straight line.

.. picture:: 0280.g1.svg
   :alt: Book XI, Proposition 3

For, if not, from :g:`D <0280.g1:D>` to :g:`B <0280.g1:B>` let the straight line :g:`DEB <0280.g1:/ D E B />` be joined in the plane :g:`AB <0280.g1:< A B >>`, and in the plane :g:`BC <0280.g1:< B C >>` the straight line :g:`DFB <0280.g1:/ D F B />`.

.. assertion::

   Then the two straight lines :g:`DEB <0280.g1:/ D E B />`, :g:`DFB <0280.g1:/ D F B />` will have the same :term:`extremities <extremity>`, and will clearly enclose an area:

.. assertion::

   which is absurd.

.. assertion::

   Therefore :g:`DEB <0280.g1:/ D E B />`, :g:`DFB <0280.g1:/ D F B />` are not straight lines.

.. assertion::

   Similarly we can prove that neither will there be any other straight line joined from :g:`D <0280.g1:D>` to :g:`B <0280.g1:B>` except :g:`DB <0280.g1:/ D B />` the common section of the planes :g:`AB <0280.g1:< A B >>`, :g:`BC <0280.g1:< B C >>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "I.def.1" [label="I.def.1", fillcolor="#224422", tooltip="I.def.1: A point is that which has no part.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-1", target="_top"];
     "I.def.2" [label="I.def.2", fillcolor="#224422", tooltip="I.def.2: A line is breadthless length.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-2", target="_top"];
     "I.def.3" [label="I.def.3", fillcolor="#224422", tooltip="I.def.3: The extremities of a line are points.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-3", target="_top"];
     "I.def.4" [label="I.def.4", fillcolor="#224422", tooltip="I.def.4: A straight line is a line which lies evenly with the points on itself.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-4", target="_top"];
     "I.def.5" [label="I.def.5", fillcolor="#224422", tooltip="I.def.5: A surface is that which has length and breadth only.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-5", target="_top"];
     "I.def.7" [label="I.def.7", fillcolor="#224422", tooltip="I.def.7: A plane surface is a surface which lies evenly with the straight lines on itself.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-7", target="_top"];
     "XI.3" [label="XI.3", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="XI.3: If two planes cut one another, their common section is a straight line.", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "XI.3" -> "I.def.4";
     "I.def.7" -> "I.def.5";
     "XI.3" -> "I.def.7";
   }

Required for
------------

:ref:`XI.5 <XI.5>`, :ref:`XI.6 <XI.6>`, :ref:`XI.7 <XI.7>`, :ref:`XI.8 <XI.8>`, :ref:`XI.9 <XI.9>`, :ref:`XI.10 <XI.10>`, :ref:`XI.11 <XI.11>`, :ref:`XI.12 <XI.12>`, :ref:`XI.13 <XI.13>`, :ref:`XI.14 <XI.14>`, :ref:`XI.15 <XI.15>`, :ref:`XI.18 <XI.18>`, :ref:`XI.19 <XI.19>`, :ref:`XI.23 <XI.23>`, :ref:`XI.24 <XI.24>`, :ref:`XI.25 <XI.25>`, :ref:`XI.26 <XI.26>`, :ref:`XI.31 <XI.31>`, :ref:`XI.32 <XI.32>`, :ref:`XI.33 <XI.33>`, :ref:`XI.34 <XI.34>`, :ref:`XI.35 <XI.35>`, :ref:`XI.36 <XI.36>`, :ref:`XI.37 <XI.37>`, :ref:`XI.38 <XI.38>`, :ref:`XI.39 <XI.39>`, :ref:`XII.3 <XII.3>`, :ref:`XII.4 <XII.4>`, :ref:`XII.5 <XII.5>`, :ref:`XII.6 <XII.6>`, :ref:`XII.7 <XII.7>`, :ref:`XII.8 <XII.8>`, :ref:`XII.9 <XII.9>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.14 <XIII.14>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition XI.3 <XI.3.commentary>`.

.. toctree::
   :hidden:

   commentary
