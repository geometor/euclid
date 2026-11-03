:canonical_id: IX.33
:volume: II
:book: IX
:proposition: 33
:type: proposition
:title: Proposition IX.33
:folios: 0425
:pages: 419
:dependencies: VII.def.2, VII.def.7, VII.def.8, VII.def.9

.. _IX.33:

.. folio:: 0425
   :page: 419

PROPOSITION 33.
===============

.. enunciation::

   If a :term:`number <number>` have its half :term:`odd <odd-number>`, it is :term:`even-times odd <even-times-odd-number>` only.

For let the number :g:`A <0425.g1:A>` have its half odd;

I say that :g:`A <0425.g1:A>` is even-times odd only.

.. picture:: 0425.g1.svg
   :alt: Proposition 33 Diagram

.. assertion::

   Now that it is even-times odd is manifest; for the half of it, being odd, :term:`measures <part-aliquot>` it an :term:`even number <even-number>` of times. :just:`[VII. Def. 9] <VII.def.9>`

I say next that it is also even-times odd only.

.. subclause::

   For, if :g:`A <0425.g1:A>` is :term:`even-times even <even-times-even-number>` also,

.. assertion::

   it will be measured by an even number according to an even number; :just:`[VII. Def. 8] <VII.def.8>`

.. assertion::

   so that the half of it will also be measured by an even number though it is odd: which is absurd.

.. assertion::

   Therefore :g:`A <0425.g1:A>` is even-times odd only.

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
     "V.def.1" [label="V.def.1", fillcolor="#224422", tooltip="V.def.1: A magnitude is a part of a magnitude, the less of the greater, when it measures the greater.", URL="../../../book_v/definitions/index.html#v-def-1", target="_top"];
     "VII.def.1" [label="VII.def.1", fillcolor="#224422", tooltip="VII.def.1: An unit is that by virtue of which each of the things that exist is called one.", URL="../../../book_vii/definitions/index.html#vii-def-1", target="_top"];
     "VII.def.2" [label="VII.def.2", fillcolor="#224422", tooltip="VII.def.2: A number is a multitude composed of units.", URL="../../../book_vii/definitions/index.html#vii-def-2", target="_top"];
     "VII.def.6" [label="VII.def.6", fillcolor="#224422", tooltip="VII.def.6: An even number is that which is divisible into two equal parts.", URL="../../../book_vii/definitions/index.html#vii-def-6", target="_top"];
     "VII.def.7" [label="VII.def.7", fillcolor="#224422", tooltip="VII.def.7: An odd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", URL="../../../book_vii/definitions/index.html#vii-def-7", target="_top"];
     "VII.def.8" [label="VII.def.8", fillcolor="#224422", tooltip="VII.def.8: An even-times even number is that which is measured by an even number according to an even number.", URL="../../../book_vii/definitions/index.html#vii-def-8", target="_top"];
     "VII.def.9" [label="VII.def.9", fillcolor="#224422", tooltip="VII.def.9: An even-times odd number is that which is measured by an even number according to an odd number.", URL="../../../book_vii/definitions/index.html#vii-def-9", target="_top"];
     "IX.33" [label="IX.33", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.33: If a number have its half odd, it is even-times odd only.", URL="index.html", target="_top"];
     "VII.def.8" -> "V.def.1";
     "VII.def.9" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.7" -> "VII.def.1";
     "IX.33" -> "VII.def.2";
     "VII.def.7" -> "VII.def.6";
     "VII.def.8" -> "VII.def.6";
     "VII.def.9" -> "VII.def.6";
     "VII.def.9" -> "VII.def.7";
     "IX.33" -> "VII.def.7";
     "IX.33" -> "VII.def.8";
     "IX.33" -> "VII.def.9";
   }
