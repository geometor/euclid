:canonical_id: X.16
:volume: III
:book: X
:proposition: 16
:type: proposition
:title: Proposition X.16
:folios: 0044, 0045
:pages: 40, 41
:dependencies: I.def.4, I.def.14, I.def.22, II.def.1, X.def.1

.. _X.16:

.. _folio-iii-0044:

.. folio:: 0044
   :page: 40

PROPOSITION 16.
===============

.. enunciation::

   If two :term:`incommensurable <incommensurable>` magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes will also be incommensurable.

For let the two incommensurable magnitudes :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />` be added together; I say that the whole :g:`AC <0044.g1:/ A C />` is also incommensurable with each of the magnitudes :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />`.

.. picture:: 0044.g1.svg
   :alt: Proposition 16 Diagram

For, if :g:`CA <0044.g1:/ A C />`, :g:`AB <0044.g1:/ A B />` are not incommensurable, some magnitude will :term:`measure <part-aliquot>` them. Let it measure them, if possible, and let it be :g:`D <0044.g1:D>`.

.. subclause::

   Since then :g:`D <0044.g1:D>` measures :g:`CA <0044.g1:/ A C />`, :g:`AB <0044.g1:/ A B />`,

.. assertion::

   therefore it will also measure the remainder :g:`BC <0044.g1:/ B C />`.

.. subclause::

   But it measures :g:`AB <0044.g1:/ A B />` also;

.. assertion::

   therefore :g:`D <0044.g1:D>` measures :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />`.

.. assertion::

   Therefore :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />` are commensurable;

.. subclause::

   but they were also, by hypothesis, incommensurable:

.. assertion::

   which is impossible.

.. assertion::

   Therefore no magnitude will measure :g:`CA <0044.g1:/ A C />`, :g:`AB <0044.g1:/ A B />`; therefore :g:`CA <0044.g1:/ A C />`, :g:`AB <0044.g1:/ A B />` are incommensurable. :just:`[X. Def. 1] <X.def.1>`

.. assertion::

   Similarly we can prove that :g:`AC <0044.g1:/ A C />`, :g:`CB <0044.g1:/ B C />` are also incommensurable.

.. assertion::

   Therefore :g:`AC <0044.g1:/ A C />` is incommensurable with each of the magnitudes :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />`.

Next, let :g:`AC <0044.g1:/ A C />` be incommensurable with one of the magnitudes :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />`.

First, let it be incommensurable with :g:`AB <0044.g1:/ A B />`; I say that :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />` are also incommensurable.

For, if they are commensurable, some magnitude will measure them. Let it measure them, and let it be :g:`D <0044.g1:D>`.

.. subclause::

   Since then :g:`D <0044.g1:D>` measures :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />`,

.. assertion::

   therefore it will also measure the whole :g:`AC <0044.g1:/ A C />`.

.. subclause::

   But it measures :g:`AB <0044.g1:/ A B />` also;

.. assertion::

   therefore :g:`D <0044.g1:D>` measures :g:`CA <0044.g1:/ A C />`, :g:`AB <0044.g1:/ A B />`.

.. _folio-iii-0045:

.. folio:: 0045
   :page: 41

.. assertion::

   Therefore :g:`CA <0044.g1:/ A C />`, :g:`AB <0044.g1:/ A B />` are commensurable;

.. subclause::

   but they were also, by hypothesis, incommensurable:

.. assertion::

   which is impossible.

.. assertion::

   Therefore no magnitude will measure :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />`; therefore :g:`AB <0044.g1:/ A B />`, :g:`BC <0044.g1:/ B C />` are incommensurable. :just:`[X. Def. 1] <X.def.1>`

.. qed::

   Therefore etc.

LEMMA.
~~~~~~

.. enunciation::

   If to any :term:`straight line <straight-line>` there be applied a parallelogram deficient by a :term:`square <square>` :term:`figure <figure>`, the applied parallelogram is equal to the :term:`rectangle contained <contained-rectangle>` by the segments of the straight line resulting from the application.

For let there be applied to the straight line :g:`AB <0045.g1:/ A B />` the parallelogram :g:`AD <0045.g1:< A C D E >>` deficient by the square figure :g:`DB <0045.g1:< C B F D >>`; I say that :g:`AD <0045.g1:< A C D E >>` is equal to the rectangle contained by :g:`AC <0045.g1:/ A C />`, :g:`CB <0045.g1:/ C B />`.

.. picture:: 0045.g1.svg
   :alt: Lemma Diagram

This is indeed at once manifest;

.. subclause::

   for, since :g:`DB <0045.g1:< C B F D >>` is a square,

.. assertion::

   :g:`DC <0045.g1:/ C D />` is :eq:`equal <0045.g1:/ C D / = 0045.g1:/ C B />` to :g:`CB <0045.g1:/ C B />`;

.. assertion::

   and :g:`AD <0045.g1:< A C D E >>` is the rectangle :g:`AC <0045.g1:/ A C />`, :g:`CD <0045.g1:/ C D />`, that is, the rectangle :g:`AC <0045.g1:/ A C />`, :g:`CB <0045.g1:/ C B />`.

.. qed::

   Therefore etc.

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
     "I.def.13" [label="I.def.13", fillcolor="#224422", tooltip="I.def.13: A boundary is that which is an extremity of anything.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-13", target="_top"];
     "I.def.14" [label="I.def.14", fillcolor="#224422", tooltip="I.def.14: A figure is that which is contained by any boundary or boundaries.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-14", target="_top"];
     "I.def.19" [label="I.def.19", fillcolor="#224422", tooltip="I.def.19: Rectilineal figures are those which are contained by straight lines, trilateral figures being those contained by three, quadrilateral those contained by four, and multilateral…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-19", target="_top"];
     "I.def.20" [label="I.def.20", fillcolor="#224422", tooltip="I.def.20: Of trilateral figures, an equilateral triangle is that which has its three sides equal, an isosceles triangle that which has two of its sides alone equal, and a scalene triangle…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-20", target="_top"];
     "I.def.22" [label="I.def.22", fillcolor="#224422", tooltip="I.def.22: Of quadrilateral figures, a square is that which is both equilateral and right-angled ; an oblong that which is right-angled but not equilateral ; a rhombus that which is…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-22", target="_top"];
     "II.def.1" [label="II.def.1", fillcolor="#224422", tooltip="II.def.1: Any rectangular parallelogram is said to be contained by the two straight lines containing the right angle.", URL="../../../../volume_I/book_ii/definitions/index.html#ii-def-1", target="_top"];
     "V.def.1" [label="V.def.1", fillcolor="#224422", tooltip="V.def.1: A magnitude is a part of a magnitude, the less of the greater, when it measures the greater.", URL="../../../../volume_II/book_v/definitions/index.html#v-def-1", target="_top"];
     "X.def.1" [label="X.def.1", fillcolor="#224422", tooltip="X.def.1: Those magnitudes are said to be commensurable which are measured by the same measure, and those incommensurable which cannot have any common measure.", URL="../../definitions/index.html#x-def-1", target="_top"];
     "X.16" [label="X.16", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="X.16: If two incommensurable magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original…", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.8" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.13" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.8" -> "I.def.4";
     "I.def.10" -> "I.def.4";
     "I.def.19" -> "I.def.4";
     "II.def.1" -> "I.def.4";
     "X.16" -> "I.def.4";
     "I.def.7" -> "I.def.5";
     "I.def.8" -> "I.def.7";
     "I.def.10" -> "I.def.8";
     "I.def.22" -> "I.def.8";
     "II.def.1" -> "I.def.10";
     "I.def.14" -> "I.def.13";
     "X.16" -> "I.def.14";
     "I.def.20" -> "I.def.19";
     "I.def.22" -> "I.def.19";
     "I.def.22" -> "I.def.20";
     "X.16" -> "I.def.22";
     "X.16" -> "II.def.1";
     "X.def.1" -> "V.def.1";
     "X.16" -> "X.def.1";
   }

Required for
------------

:ref:`X.18 <X.18>`, :ref:`X.26 <X.26>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.36 <X.36>`, :ref:`X.37 <X.37>`, :ref:`X.38 <X.38>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.42 <X.42>`, :ref:`X.43 <X.43>`, :ref:`X.44 <X.44>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.47 <X.47>`, :ref:`X.48 <X.48>`, :ref:`X.49 <X.49>`, :ref:`X.50 <X.50>`, :ref:`X.52 <X.52>`, :ref:`X.53 <X.53>`, :ref:`X.54 <X.54>`, :ref:`X.55 <X.55>`, :ref:`X.56 <X.56>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.61 <X.61>`, :ref:`X.62 <X.62>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.66 <X.66>`, :ref:`X.67 <X.67>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.73 <X.73>`, :ref:`X.74 <X.74>`, :ref:`X.75 <X.75>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.79 <X.79>`, :ref:`X.80 <X.80>`, :ref:`X.81 <X.81>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.92 <X.92>`, :ref:`X.93 <X.93>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.97 <X.97>`, :ref:`X.98 <X.98>`, :ref:`X.99 <X.99>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.103 <X.103>`, :ref:`X.104 <X.104>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`X.112 <X.112>`, :ref:`X.113 <X.113>`, :ref:`X.114 <X.114>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition X.16 <X.16.commentary>`.

.. toctree::
   :hidden:

   commentary
