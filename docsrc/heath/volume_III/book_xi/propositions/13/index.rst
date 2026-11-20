:canonical_id: XI.13
:volume: III
:book: XI
:proposition: 13
:type: proposition
:title: Proposition XI.13
:folios: 0299
:folio: 0299
:page: 295
:pages: 295
:dependencies: I.def.1, I.def.4, XI.def.3, XI.3

.. _XI.13:

.. _folio-iii-0299:

.. folio:: 0299
   :page: 295

PROPOSITION 13.
===============

.. enunciation::

   From the same :term:`point <point>` two :term:`straight lines <straight-line>` cannot be set up :term:`at right angles to the same plane <right-angles-to-plane>` on the same side.

For, if possible, from the same point :g:`A <0299.g1:A>` let the two straight lines :g:`AB <0299.g1:/ A B />`, :g:`AC <0299.g1:/ A C />` be set up at right angles to the plane of reference and on the same side, and let a :term:`plane <plane-surface>` be drawn through :g:`BA <0299.g1:/ B A />`, :g:`AC <0299.g1:/ A C />`; it will then make, as section through :g:`A <0299.g1:A>` in the plane of reference, a straight line. :just:`[XI. 3] <XI.3>`

.. picture:: 0299.g1.svg
   :alt: Proposition 13

Let it make :g:`DAE <0299.g1:/ D A E />`;

.. assertion::

   therefore the straight lines :g:`AB <0299.g1:/ A B />`, :g:`AC <0299.g1:/ A C />`, :g:`DAE <0299.g1:/ D A E />` are in one plane.

And, since :g:`CA <0299.g1:/ C A />` is at right angles to the plane of reference, it will also make :term:`right angles <right-angle>` with all the straight lines which meet it and are in the plane of reference. :just:`[XI. Def. 3] <XI.def.3>`

.. subclause::

   But :g:`DAE <0299.g1:/ D A E />` meets it and is in the plane of reference;

.. assertion::

   therefore the :term:`angle <plane-angle>` :g:`CAE <0299.g1:< C A E )>` is right.

.. subclause::

   For the same reason the angle :g:`BAE <0299.g1:< B A E )>` is also right;

.. assertion::

   therefore the angle :g:`CAE <0299.g1:< C A E )>` is :eq:`equal <0299.g1:< C A E ) = 0299.g1:< B A E )>` to the angle :g:`BAE <0299.g1:< B A E )>`.

.. assertion::

   And they are in one plane: which is impossible.

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
     "I.def.8" [label="I.def.8", fillcolor="#224422", tooltip="I.def.8: A plane angle is the inclination to one another of two lines in a plane which meet one another and do not lie in a straight line.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-8", target="_top"];
     "I.def.10" [label="I.def.10", fillcolor="#224422", tooltip="I.def.10: When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-10", target="_top"];
     "XI.def.3" [label="XI.def.3", fillcolor="#224422", tooltip="XI.def.3: A straight line is at right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", URL="../../definitions/index.html#xi-def-3", target="_top"];
     "XI.3" [label="XI.3", fillcolor="#222244", tooltip="XI.3: If two planes cut one another, their common section is a straight line.", URL="../03/index.html", target="_top"];
     "XI.13" [label="XI.13", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="XI.13: From the same point two straight lines cannot be set up at right angles to the same plane on the same side.", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "XI.13" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.8" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.8" -> "I.def.4";
     "I.def.10" -> "I.def.4";
     "XI.def.3" -> "I.def.4";
     "XI.3" -> "I.def.4";
     "XI.13" -> "I.def.4";
     "I.def.7" -> "I.def.5";
     "I.def.8" -> "I.def.7";
     "XI.def.3" -> "I.def.7";
     "XI.3" -> "I.def.7";
     "I.def.10" -> "I.def.8";
     "XI.def.3" -> "I.def.10";
     "XI.13" -> "XI.def.3";
     "XI.13" -> "XI.3";
   }

Required for
------------

:ref:`XI.19 <XI.19>`

----

See :ref:`Commentary on Proposition XI.13 <XI.13.commentary>`.

.. toctree::
   :hidden:

   commentary
