:canonical_id: III.6
:volume: II
:book: III
:proposition: 6
:type: proposition
:title: Proposition III.6
:folios: 0019
:folio: 0019
:page: 13
:pages: 13
:dependencies: I.def.15, I.def.16, III.def.3

.. _III.6:

.. _folio-ii-0019:

.. folio:: 0019
   :page: 13

PROPOSITION 6.
==============

.. enunciation::

   If two :term:`circles <circle>` :term:`touch one another <circles-touching>`, they will not have the same :term:`centre <centre>`.

For let the two circles :g:`ABC <0019.g1:( A B C )>`, :g:`CDE <0019.g1:( C D E )>` touch one another at the :term:`point <point>` :g:`C <0019.g1:C>`;

I say that they will not have the same centre.

.. picture:: 0019.g1.svg
   :alt: Proposition 6 Diagram

For, if possible, let it be :g:`F <0019.g1:F>`; let :g:`FC <0019.g1:/ F C />` be joined, and let :g:`FEB <0019.g1:/ F E B />` be drawn through at random.

Then, since the point :g:`F <0019.g1:F>` is the centre of the circle :g:`ABC <0019.g1:( A B C )>`,

.. assertion::

   :g:`FC <0019.g1:/ F C />` is :eq:`equal <0019.g1:/ F C / = 0019.g1:/ F B />` to :g:`FB <0019.g1:/ F B />`.

Again, since the point :g:`F <0019.g1:F>` is the centre of the circle :g:`CDE <0019.g1:( C D E )>`,

.. assertion::

   :g:`FC <0019.g1:/ F C />` is :eq:`equal <0019.g1:/ F C / = 0019.g1:/ F E />` to :g:`FE <0019.g1:/ F E />`.

But :g:`FC <0019.g1:/ F C />` was proved :eq:`equal <0019.g1:/ F C / = 0019.g1:/ F B />` to :g:`FB <0019.g1:/ F B />`; therefore :g:`FE <0019.g1:/ F E />` is also :eq:`equal <0019.g1:/ F E / = 0019.g1:/ F B />` to :g:`FB <0019.g1:/ F B />`, the less to the greater: which is impossible.

.. assertion::

   Therefore :g:`F <0019.g1:F>` is not the centre of the circles :g:`ABC <0019.g1:( A B C )>`, :g:`CDE <0019.g1:( C D E )>`.

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
     "III.def.3" [label="III.def.3", fillcolor="#224422", tooltip="III.def.3: Circles are said to touch one another which, meeting one another, do not cut one another.", URL="../../definitions/index.html#iii-def-3", target="_top"];
     "III.6" [label="III.6", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.6: If two circles touch one another, they will not have the same centre.", URL="index.html", target="_top"];
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
     "III.6" -> "I.def.15";
     "III.6" -> "I.def.16";
     "III.6" -> "III.def.3";
   }

----

See :ref:`Commentary on Proposition III.6 <III.6.commentary>`.

.. toctree::
   :hidden:

   commentary
