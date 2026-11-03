:canonical_id: IX.34
:volume: II
:book: IX
:proposition: 34
:type: proposition
:title: Proposition IX.34
:folios: 0425, 0426
:pages: 419, 420
:dependencies: VII.def.2, VII.def.7, VII.def.8, VII.def.9

.. _IX.34:

.. folio:: 0425
   :page: 419

PROPOSITION 34.
===============

.. enunciation::

   If a :term:`number <number>` neither be one of those which are continually doubled from a dyad, nor have its half :term:`odd <odd-number>`, it is both :term:`even-times even <even-times-even-number>` and :term:`even-times odd <even-times-odd-number>`.

For let the number :g:`A <0425.g2:A>` neither be one of those doubled from a dyad, nor have its half odd;

I say that :g:`A <0425.g2:A>` is both even-times even and even-times odd.

.. picture:: 0425.g2.svg
   :alt: Proposition 34 Diagram

.. assertion::

   Now that :g:`A <0425.g2:A>` is even-times even is manifest; for it has not its half odd. :just:`[VII. Def. 8] <VII.def.8>`

I say next that it is also even-times odd.

.. subclause::

   For, if we bisect :g:`A <0425.g2:A>`, then bisect its half, and do this continually, we shall come upon some odd number which will :term:`measure <part-aliquot>` :g:`A <0425.g2:A>` according to an :term:`even number <even-number>`.

.. subclause::

   For, if not, we shall come upon a dyad, and :g:`A <0425.g2:A>` will be among those which are doubled from a dyad: which is contrary to the hypothesis.

.. _folio-ii-0426:

.. folio:: 0426
   :page: 420

.. assertion::

   Thus :g:`A <0425.g2:A>` is even-times odd.

.. subclause::

   But it was also proved even-times even.

.. assertion::

   Therefore :g:`A <0425.g2:A>` is both even-times even and even-times odd.

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
     "IX.34" [label="IX.34", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.34: If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.", URL="index.html", target="_top"];
     "VII.def.8" -> "V.def.1";
     "VII.def.9" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.7" -> "VII.def.1";
     "IX.34" -> "VII.def.2";
     "VII.def.7" -> "VII.def.6";
     "VII.def.8" -> "VII.def.6";
     "VII.def.9" -> "VII.def.6";
     "VII.def.9" -> "VII.def.7";
     "IX.34" -> "VII.def.7";
     "IX.34" -> "VII.def.8";
     "IX.34" -> "VII.def.9";
   }
