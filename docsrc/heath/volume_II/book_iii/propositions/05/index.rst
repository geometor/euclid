:canonical_id: III.5
:volume: II
:book: III
:proposition: 5
:type: proposition
:title: Proposition III.5
:folios: 0018
:folio: 0018
:page: 12
:pages: 12
:dependencies: I.def.15, I.def.16

.. _III.5:

.. folio:: 0018
   :page: 12

PROPOSITION 5.
==============

.. enunciation::

   If two :term:`circles <circle>` cut one another, they will not have the same :term:`centre <centre>`.

For let the circles :g:`ABC <0018.g1:( A B C )>`, :g:`CDG <0018.g1:( C D G )>` cut one another at the :term:`points <point>` :g:`B <0018.g1:B>`, :g:`C <0018.g1:C>`;

I say that they will not have the same centre.

.. picture:: 0018.g1.svg
   :alt: Proposition 5 Diagram

For, if possible, let it be :g:`E <0018.g1:E>`; let :g:`EC <0018.g1:/ E C />` be joined, and let :g:`EFG <0018.g1:/ E F G />` be drawn through at random.

Then, since the point :g:`E <0018.g1:E>` is the centre of the circle :g:`ABC <0018.g1:( A B C )>`,

.. assertion:: [I. Def. 15] <I.def.15>

   :g:`EC <0018.g1:/ E C />` is :eq:`equal <0018.g1:/ E C / = 0018.g1:/ E F />` to :g:`EF <0018.g1:/ E F />`.

Again, since the point :g:`E <0018.g1:E>` is the centre of the circle :g:`CDG <0018.g1:( C D G )>`,

.. assertion::

   :g:`EC <0018.g1:/ E C />` is :eq:`equal <0018.g1:/ E C / = 0018.g1:/ E G />` to :g:`EG <0018.g1:/ E G />`.

But :g:`EC <0018.g1:/ E C />` was proved :eq:`equal <0018.g1:/ E C / = 0018.g1:/ E F />` to :g:`EF <0018.g1:/ E F />` also; therefore :g:`EF <0018.g1:/ E F />` is also :eq:`equal <0018.g1:/ E F / = 0018.g1:/ E G />` to :g:`EG <0018.g1:/ E G />`, the less to the greater: which is impossible.

.. assertion::

   Therefore the point :g:`E <0018.g1:E>` is not the centre of the circles :g:`ABC <0018.g1:( A B C )>`, :g:`CDG <0018.g1:( C D G )>`.

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
     "I.def.6" [label="I.def.6", fillcolor="#224422", tooltip="I.def.6: The extremities of a surface are lines.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-6", target="_top"];
     "I.def.7" [label="I.def.7", fillcolor="#224422", tooltip="I.def.7: A plane surface is a surface which lies evenly with the straight lines on itself.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-7", target="_top"];
     "I.def.13" [label="I.def.13", fillcolor="#224422", tooltip="I.def.13: A boundary is that which is an extremity of anything.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-13", target="_top"];
     "I.def.14" [label="I.def.14", fillcolor="#224422", tooltip="I.def.14: A figure is that which is contained by any boundary or boundaries.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-14", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", tooltip="I.def.15: A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-15", target="_top"];
     "I.def.16" [label="I.def.16", fillcolor="#224422", tooltip="I.def.16: And the point is called the centre of the circle.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-16", target="_top"];
     "III.5" [label="III.5", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.5: If two circles cut one another, they will not have the same centre.", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.15" -> "I.def.1";
     "I.def.16" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.6" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.13" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.15" -> "I.def.4";
     "I.def.6" -> "I.def.5";
     "I.def.7" -> "I.def.5";
     "I.def.15" -> "I.def.6";
     "I.def.15" -> "I.def.7";
     "I.def.14" -> "I.def.13";
     "I.def.15" -> "I.def.14";
     "I.def.16" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.5" -> "I.def.16";
   }

Required for
------------

:ref:`III.10 <III.10>`, :ref:`III.24 <III.24>`, :ref:`III.26 <III.26>`, :ref:`III.27 <III.27>`, :ref:`III.28 <III.28>`, :ref:`III.29 <III.29>`, :ref:`III.30 <III.30>`, :ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`, :ref:`IV.15 <IV.15>`, :ref:`IV.16 <IV.16>`, :ref:`VI.33 <VI.33>`, :ref:`XII.1 <XII.1>`, :ref:`XII.2 <XII.2>`, :ref:`XII.5 <XII.5>`, :ref:`XII.6 <XII.6>`, :ref:`XII.7 <XII.7>`, :ref:`XII.8 <XII.8>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.8 <XIII.8>`, :ref:`XIII.9 <XIII.9>`, :ref:`XIII.10 <XIII.10>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.12 <XIII.12>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition III.5 <III.5.commentary>`.

.. toctree::
   :hidden:

   commentary
