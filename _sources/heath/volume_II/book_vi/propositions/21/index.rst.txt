:canonical_id: VI.21
:volume: II
:book: VI
:proposition: 21
:type: proposition
:title: Proposition VI.21
:folios: 0245, 0246
:pages: 239, 240
:dependencies: I.def.14, I.def.19, VI.def.1

.. _VI.21:

.. folio:: 0245
   :page: 239

PROPOSITION 21.
===============

.. enunciation::

   :term:`Figures <figure>` which are similar to the same :term:`rectilineal figure <rectilineal-figure>` are also similar to one another.

For let each of the rectilineal figures :g:`A <0246.g1:A>`, :g:`B <0246.g1:B>` be similar to :g:`C <0246.g1:C>`;

I say that :g:`A <0246.g1:A>` is also similar to :g:`B <0246.g1:B>`.

.. _folio-ii-0246:

.. folio:: 0246
   :page: 240

.. subclause::

   For, since :g:`A <0246.g1:A>` is similar to :g:`C <0246.g1:C>`,

.. assertion::

   it is equiangular with it and has the sides about the equal :term:`angles <plane-angle>` :term:`proportional <proportional>`. :just:`[VI. Def. 1] <VI.def.1>`

.. picture:: 0246.g1.svg
   :alt: Book VI, Proposition 21

.. subclause::

   Again, since :g:`B <0246.g1:B>` is similar to :g:`C <0246.g1:C>`,

.. assertion::

   it is equiangular with it and has the sides about the equal angles proportional.

.. assertion::

   Therefore each of the figures :g:`A <0246.g1:A>`, :g:`B <0246.g1:B>` is equiangular with :g:`C <0246.g1:C>` and with :g:`C <0246.g1:C>` has the sides about the equal angles proportional;

.. assertion::

   therefore :g:`A <0246.g1:A>` is similar to :g:`B <0246.g1:B>`.

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
     "I.def.7" [label="I.def.7", fillcolor="#224422", tooltip="I.def.7: A plane surface is a surface which lies evenly with the straight lines on itself.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-7", target="_top"];
     "I.def.8" [label="I.def.8", fillcolor="#224422", tooltip="I.def.8: A plane angle is the inclination to one another of two lines in a plane which meet one another and do not lie in a straight line.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-8", target="_top"];
     "I.def.13" [label="I.def.13", fillcolor="#224422", tooltip="I.def.13: A boundary is that which is an extremity of anything.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-13", target="_top"];
     "I.def.14" [label="I.def.14", fillcolor="#224422", tooltip="I.def.14: A figure is that which is contained by any boundary or boundaries.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-14", target="_top"];
     "I.def.19" [label="I.def.19", fillcolor="#224422", tooltip="I.def.19: Rectilineal figures are those which are contained by straight lines, trilateral figures being those contained by three, quadrilateral those contained by four, and multilateral…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-19", target="_top"];
     "V.def.1" [label="V.def.1", fillcolor="#224422", tooltip="V.def.1: A magnitude is a part of a magnitude, the less of the greater, when it measures the greater.", URL="../../../book_v/definitions/index.html#v-def-1", target="_top"];
     "V.def.2" [label="V.def.2", fillcolor="#224422", tooltip="V.def.2: The greater is a multiple of the less when it is measured by the less.", URL="../../../book_v/definitions/index.html#v-def-2", target="_top"];
     "V.def.5" [label="V.def.5", fillcolor="#224422", tooltip="V.def.5: Magnitudes are said to be in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any…", URL="../../../book_v/definitions/index.html#v-def-5", target="_top"];
     "V.def.6" [label="V.def.6", fillcolor="#224422", tooltip="V.def.6: Let magnitudes which have the same ratio be called proportional.", URL="../../../book_v/definitions/index.html#v-def-6", target="_top"];
     "VI.def.1" [label="VI.def.1", fillcolor="#224422", tooltip="VI.def.1: Similar rectilineal figures are such as have their angles severally equal and the sides about the equal angles proportional.", URL="../../definitions/index.html#vi-def-1", target="_top"];
     "VI.21" [label="VI.21", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VI.21: Figures which are similar to the same rectilineal figure are also similar to one another.", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.8" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.13" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.8" -> "I.def.4";
     "I.def.19" -> "I.def.4";
     "I.def.7" -> "I.def.5";
     "I.def.8" -> "I.def.7";
     "VI.def.1" -> "I.def.8";
     "I.def.14" -> "I.def.13";
     "VI.21" -> "I.def.14";
     "VI.21" -> "I.def.19";
     "V.def.2" -> "V.def.1";
     "V.def.5" -> "V.def.2";
     "V.def.6" -> "V.def.5";
     "VI.def.1" -> "V.def.6";
     "VI.21" -> "VI.def.1";
   }

Required for
------------

:ref:`VI.24 <VI.24>`, :ref:`VI.26 <VI.26>`, :ref:`VI.27 <VI.27>`, :ref:`VI.28 <VI.28>`, :ref:`VI.29 <VI.29>`, :ref:`VI.30 <VI.30>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.71 <X.71>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.91 <X.91>`, :ref:`X.92 <X.92>`, :ref:`X.93 <X.93>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition VI.21 <VI.21.commentary>`.

.. toctree::
   :hidden:

   commentary
