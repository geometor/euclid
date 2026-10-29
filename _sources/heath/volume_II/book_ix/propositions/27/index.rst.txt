:canonical_id: IX.27
:volume: II
:book: IX
:proposition: 27
:type: proposition
:title: Proposition IX.27
:folios: 0422
:pages: 416
:dependencies: VII.def.7, IX.24

.. _IX.27:

.. _folio-ii-0422:

.. folio:: 0422
   :page: 416

PROPOSITION 27.
===============

.. enunciation::

   If from an odd number an even number be subtracted, the remainder will be odd.

For from the odd number :g:`$AB$ <0422.g1:/ A B />` let the even number :g:`$BC$ <0422.g1:/ B C />` be subtracted ;

I say that the remainder :g:`$CA$ <0422.g1:/ A C />` is odd.

.. picture:: 0422.g1.svg
   :alt: Book IX, Proposition 27

Let the unit :g:`$AD$ <0422.g1:/ A D />` be subtracted ;

.. assertion:: [VII. Def. 7] <VII.def.7>

   therefore :g:`$DB$ <0422.g1:/ B D />` is even.

.. subclause::

   But :g:`$BC$ <0422.g1:/ B C />` is also even ;

.. assertion:: [IX. 24] <IX.24>

   therefore the remainder :g:`$CD$ <0422.g1:/ C D />` is even.

.. assertion:: [VII. Def. 7] <VII.def.7>

   Therefore :g:`$CA$ <0422.g1:/ A C />` is odd.

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
     "VII.def.6" [label="VII.def.6", fillcolor="#224422", tooltip="VII.def.6: An even number is that which is divisible into two equal parts.", URL="../../../book_vii/definitions/index.html#vii-def-6", target="_top"];
     "VII.def.7" [label="VII.def.7", fillcolor="#224422", tooltip="VII.def.7: An odd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", URL="../../../book_vii/definitions/index.html#vii-def-7", target="_top"];
     "IX.24" [label="IX.24", fillcolor="#222244", tooltip="IX.24: If from an even number an even number be subtracted, the remainder will be even.", URL="../24/index.html", target="_top"];
     "IX.27" [label="IX.27", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.27: If from an odd number an even number be subtracted, the remainder will be odd.", URL="index.html", target="_top"];
     "IX.24" -> "VII.def.6";
     "IX.27" -> "VII.def.7";
     "IX.27" -> "IX.24";
   }
