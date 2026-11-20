:canonical_id: XI.16
:volume: III
:book: XI
:proposition: 16
:type: proposition
:title: Proposition XI.16
:folios: 0304
:folio: 0304
:page: 300
:pages: 300
:dependencies: I.def.7, I.def.23, XI.def.8, XI.1

.. _XI.16:

.. _folio-iii-0304:

.. folio:: 0304
   :page: 300

PROPOSITION 16.
===============

.. enunciation::

   If two :term:`parallel planes <parallel-planes>` be cut by any :term:`plane <plane-surface>`, their common sections are :term:`parallel <parallel-straight-lines>`.

For let the two parallel planes :g:`AB <0304.g1:< A B >>`, :g:`CD <0304.g1:< C D >>` be cut by the plane :g:`EFGH <0304.g1:< E F G H >>`, and let :g:`EF <0304.g1:/ E F />`, :g:`GH <0304.g1:/ G H />` be their common sections ; I say that :g:`EF <0304.g1:/ E F />` is parallel to :g:`GH <0304.g1:/ G H />`.

.. picture:: 0304.g1.svg
   :alt: Book XI, Proposition 16

.. subclause::

   For, if not, :g:`EF <0304.g1:/ E F />`, :g:`GH <0304.g1:/ G H />` will, when produced, meet either in the direction of :g:`F <0304.g1:F>`, :g:`H <0304.g1:H>` or of :g:`E <0304.g1:E>`, :g:`G <0304.g1:G>`. Let them be produced, as in the direction of :g:`F <0304.g1:F>`, :g:`H <0304.g1:H>`, and let them, first, meet at :g:`K <0304.g1:K>`.

.. subclause::

   Now, since :g:`EFK <0304.g1:/ E F K />` is in the plane :g:`AB <0304.g1:< A B >>`,

.. assertion::

   therefore all the :term:`points <point>` on :g:`EFK <0304.g1:/ E F K />` are also in the plane :g:`AB <0304.g1:< A B >>`. :just:`[XI. 1] <XI.1>`

.. subclause::

   But :g:`K <0304.g1:K>` is one of the points on the :term:`straight line <straight-line>` :g:`EFK <0304.g1:/ E F K />`;

.. assertion::

   therefore :g:`K <0304.g1:K>` is in the plane :g:`AB <0304.g1:< A B >>`.

.. subclause::

   For the same reason :g:`K <0304.g1:K>` is also in the plane :g:`CD <0304.g1:< C D >>`;

.. assertion::

   therefore the planes :g:`AB <0304.g1:< A B >>`, :g:`CD <0304.g1:< C D >>` will meet when produced.

.. subclause::

   But they do not meet, because they are, by hypothesis, parallel;

.. assertion::

   therefore the straight lines :g:`EF <0304.g1:/ E F />`, :g:`GH <0304.g1:/ G H />` will not meet when produced in the direction of :g:`F <0304.g1:F>`, :g:`H <0304.g1:H>`.

.. assertion::

   Similarly we can prove that neither will the straight lines :g:`EF <0304.g1:/ E F />`, :g:`GH <0304.g1:/ G H />` meet when produced in the direction of :g:`E <0304.g1:E>`, :g:`G <0304.g1:G>`.

.. subclause::

   But straight lines which do not meet in either direction are parallel. :just:`[I. Def. 23] <I.def.23>`

.. assertion::

   Therefore :g:`EF <0304.g1:/ E F />` is parallel to :g:`GH <0304.g1:/ G H />`.

.. assertion::

   Therefore etc.

.. qed::

   :just:`Q. E. D.`

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
     "I.def.17" [label="I.def.17", fillcolor="#224422", tooltip="I.def.17: A diameter of the circle is any straight line drawn through the centre and terminated in both directions by the circumference of the circle, and such a straight line also bisects…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-17", target="_top"];
     "I.def.23" [label="I.def.23", fillcolor="#224422", tooltip="I.def.23: Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-23", target="_top"];
     "V.def.1" [label="V.def.1", fillcolor="#224422", tooltip="V.def.1: A magnitude is a part of a magnitude, the less of the greater, when it measures the greater.", URL="../../../../volume_II/book_v/definitions/index.html#v-def-1", target="_top"];
     "VII.def.1" [label="VII.def.1", fillcolor="#224422", tooltip="VII.def.1: An unit is that by virtue of which each of the things that exist is called one.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-1", target="_top"];
     "VII.def.2" [label="VII.def.2", fillcolor="#224422", tooltip="VII.def.2: A number is a multitude composed of units.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-2", target="_top"];
     "VII.def.3" [label="VII.def.3", fillcolor="#224422", tooltip="VII.def.3: A number is a part of a number, the less of the greater, when it measures the greater.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-3", target="_top"];
     "XI.def.8" [label="XI.def.8", fillcolor="#224422", tooltip="XI.def.8: Parallel planes are those which do not meet.", URL="../../definitions/index.html#xi-def-8", target="_top"];
     "XI.1" [label="XI.1", fillcolor="#222244", tooltip="XI.1: A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", URL="../01/index.html", target="_top"];
     "XI.16" [label="XI.16", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="XI.16: If two parallel planes be cut by any plane, their common sections are parallel.", URL="index.html", target="_top"];
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
     "I.def.17" -> "I.def.4";
     "I.def.23" -> "I.def.4";
     "XI.1" -> "I.def.4";
     "I.def.6" -> "I.def.5";
     "I.def.7" -> "I.def.5";
     "I.def.15" -> "I.def.6";
     "I.def.15" -> "I.def.7";
     "I.def.23" -> "I.def.7";
     "XI.1" -> "I.def.7";
     "XI.16" -> "I.def.7";
     "I.def.14" -> "I.def.13";
     "I.def.15" -> "I.def.14";
     "I.def.16" -> "I.def.15";
     "I.def.17" -> "I.def.15";
     "XI.1" -> "I.def.15";
     "I.def.17" -> "I.def.16";
     "XI.1" -> "I.def.16";
     "XI.1" -> "I.def.17";
     "XI.16" -> "I.def.23";
     "VII.def.3" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.3" -> "VII.def.2";
     "XI.1" -> "VII.def.3";
     "XI.16" -> "XI.def.8";
     "XI.16" -> "XI.1";
   }

Required for
------------

:ref:`XI.17 <XI.17>`, :ref:`XI.24 <XI.24>`, :ref:`XI.25 <XI.25>`, :ref:`XI.31 <XI.31>`, :ref:`XI.32 <XI.32>`, :ref:`XI.33 <XI.33>`, :ref:`XI.34 <XI.34>`, :ref:`XI.36 <XI.36>`, :ref:`XI.37 <XI.37>`, :ref:`XI.39 <XI.39>`, :ref:`XII.3 <XII.3>`, :ref:`XII.4 <XII.4>`, :ref:`XII.5 <XII.5>`, :ref:`XII.6 <XII.6>`, :ref:`XII.7 <XII.7>`, :ref:`XII.8 <XII.8>`, :ref:`XII.9 <XII.9>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`

----

See :ref:`Commentary on Proposition XI.16 <XI.16.commentary>`.

.. toctree::
   :hidden:

   commentary
