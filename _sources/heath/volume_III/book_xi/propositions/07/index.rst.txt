:canonical_id: XI.7
:volume: III
:book: XI
:proposition: 7
:type: proposition
:title: Proposition XI.7
:folios: 0289, 0290
:pages: 285, 286
:dependencies: I.def.1, I.def.4, I.def.7, I.def.23, XI.3

.. _XI.7:

.. folio:: 0289
   :page: 285

PROPOSITION 7.
==============

.. enunciation::

   If two :term:`straight lines <straight-line>` be :term:`parallel <parallel-straight-lines>` and :term:`points <point>` be taken at random on each of them, the straight line joining the points is in the same :term:`plane <plane-surface>` with the parallel straight lines.

Let :g:`AB <0289.g1:/ A B />`, :g:`CD <0289.g1:/ C D />` be two parallel straight lines, and let points :g:`E <0289.g1:E>`, :g:`F <0289.g1:F>` be taken at random on them respectively; I say that the straight line joining the points :g:`E <0289.g1:E>`, :g:`F <0289.g1:F>` is in the same plane with the parallel straight lines.

.. picture:: 0289.g1.svg
   :alt: Book XI - Proposition 7

For suppose it is not, but, if possible, let it be in a more elevated plane as :g:`EGF <0289.g1:( E G F )>`, and let a plane be drawn through :g:`EGF <0289.g1:( E G F )>`;

.. assertion::

   it will then make, as section in the plane of reference, a straight line. :just:`[XI. 3] <XI.3>`

.. _folio-iii-0290:

.. folio:: 0290
   :page: 286

Let it make it, as :g:`EF <0289.g1:/ E F />`;

.. assertion::

   therefore the two straight lines :g:`EGF <0289.g1:( E G F )>`, :g:`EF <0289.g1:/ E F />` will enclose an area: which is impossible.

.. assertion::

   Therefore the straight line joined from :g:`E <0289.g1:E>` to :g:`F <0289.g1:F>` is not in a plane more elevated; therefore the straight line joined from :g:`E <0289.g1:E>` to :g:`F <0289.g1:F>` is in the plane through the parallel straight lines :g:`AB <0289.g1:/ A B />`, :g:`CD <0289.g1:/ C D />`.

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
     "I.def.23" [label="I.def.23", fillcolor="#224422", tooltip="I.def.23: Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-23", target="_top"];
     "XI.3" [label="XI.3", fillcolor="#222244", tooltip="XI.3: If two planes cut one another, their common section is a straight line.", URL="../03/index.html", target="_top"];
     "XI.7" [label="XI.7", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="XI.7: If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "XI.7" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.23" -> "I.def.4";
     "XI.3" -> "I.def.4";
     "XI.7" -> "I.def.4";
     "I.def.7" -> "I.def.5";
     "I.def.23" -> "I.def.7";
     "XI.3" -> "I.def.7";
     "XI.7" -> "I.def.7";
     "XI.7" -> "I.def.23";
     "XI.7" -> "XI.3";
   }

Required for
------------

:ref:`XI.8 <XI.8>`, :ref:`XI.9 <XI.9>`, :ref:`XI.10 <XI.10>`, :ref:`XI.11 <XI.11>`, :ref:`XI.12 <XI.12>`, :ref:`XI.15 <XI.15>`, :ref:`XI.18 <XI.18>`, :ref:`XI.23 <XI.23>`, :ref:`XI.24 <XI.24>`, :ref:`XI.25 <XI.25>`, :ref:`XI.26 <XI.26>`, :ref:`XI.31 <XI.31>`, :ref:`XI.32 <XI.32>`, :ref:`XI.33 <XI.33>`, :ref:`XI.34 <XI.34>`, :ref:`XI.35 <XI.35>`, :ref:`XI.36 <XI.36>`, :ref:`XI.37 <XI.37>`, :ref:`XI.38 <XI.38>`, :ref:`XI.39 <XI.39>`, :ref:`XII.3 <XII.3>`, :ref:`XII.4 <XII.4>`, :ref:`XII.5 <XII.5>`, :ref:`XII.6 <XII.6>`, :ref:`XII.7 <XII.7>`, :ref:`XII.8 <XII.8>`, :ref:`XII.9 <XII.9>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.14 <XIII.14>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition XI.7 <XI.7.commentary>`.

.. toctree::
   :hidden:

   commentary
