:canonical_id: III.11
:volume: II
:book: III
:proposition: 11
:type: proposition
:title: Proposition III.11
:folios: 0030, 0031
:pages: 24, 25
:dependencies: I.def.1, I.def.4, I.def.15, I.def.16, III.def.3

.. _III.11:

.. folio:: 0030
   :page: 24

PROPOSITION 11.
===============

.. enunciation::

   If two :term:`circles <circle>` :term:`touch one another <circles-touching>` internally, and their :term:`centres <centre>` be taken, the :term:`straight line <straight-line>` joining their centres,\ [#f1]_ if it be also produced, will fall on the :term:`point <point>` of contact\ [#f2]_ of the circles.

For let the two circles :g:`ABC <0030.g2:( A B C )>`, :g:`ADE <0030.g2:( A D E )>` touch one another internally at the point :g:`A <0030.g2:A>`, and let the centre :g:`F <0030.g2:F>` of the circle :g:`ABC <0030.g2:( A B C )>`, and the centre :g:`G <0030.g2:G>` of :g:`ADE <0030.g2:( A D E )>`, be taken;

I say that the straight line joined from :g:`G <0030.g2:G>` to :g:`F <0030.g2:F>` and produced will fall on :g:`A <0030.g2:A>`.

.. picture:: 0030.g2.svg
   :alt: Diagram for Proposition 11 showing circles ABC and ADE touching internally at A

For suppose it does not, but, if possible, let it fall as :g:`FGH <0030.g2:/ F G H />`, and let :g:`AF <0030.g2:/ A F />`, :g:`AG <0030.g2:/ A G />` be joined.

Then, since :g:`AG <0030.g2:/ A G />`, :g:`GF <0030.g2:/ G F />` are greater than :g:`FA <0030.g2:/ F A />`, that is, than :g:`FH <0030.g2:/ F H />`,

.. subclause::

   let :g:`FG <0030.g2:/ F G />` be subtracted from each;

.. assertion::

   therefore the remainder :g:`AG <0030.g2:/ A G />` is greater than the remainder :g:`GH <0030.g2:/ G H />`.

.. _folio-ii-0031:

.. folio:: 0031
   :page: 25

But :g:`AG <0030.g2:/ A G />` is :eq:`equal <0030.g2:/ A G / = 0030.g2:/ G D />` to :g:`GD <0030.g2:/ G D />`;

.. assertion::

   therefore :g:`GD <0030.g2:/ G D />` is also greater than :g:`GH <0030.g2:/ G H />`,

.. subclause::

   the less than the greater: which is impossible.

.. assertion::

   Therefore the straight line joined from :g:`F <0030.g2:F>` to :g:`G <0030.g2:G>` will not fall outside;

.. assertion::

   therefore it will fall at :g:`A <0030.g2:A>` on the point of contact.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **the straight line joining their centres**, literally "the straight line joined to their centres" (ἡ ἐπὶ τὰ κέντρα αὐτῶν ἐπιζευγνυμένη εὐθεῖα).

.. [#f2] **point of contact** is here συναφή, and in the enunciation of the next proposition ἐπαφή.

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
     "III.11" [label="III.11", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.11: If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the…", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.15" -> "I.def.1";
     "I.def.16" -> "I.def.1";
     "III.11" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.6" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.13" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.15" -> "I.def.4";
     "III.11" -> "I.def.4";
     "I.def.6" -> "I.def.5";
     "I.def.7" -> "I.def.5";
     "I.def.15" -> "I.def.6";
     "I.def.15" -> "I.def.7";
     "I.def.14" -> "I.def.13";
     "I.def.15" -> "I.def.14";
     "I.def.16" -> "I.def.15";
     "III.11" -> "I.def.15";
     "III.11" -> "I.def.16";
     "III.11" -> "III.def.3";
   }

Required for
------------

:ref:`III.13 <III.13>`

----

See :ref:`Commentary on Proposition III.11 <III.11.commentary>`.

.. toctree::
   :hidden:

   commentary
