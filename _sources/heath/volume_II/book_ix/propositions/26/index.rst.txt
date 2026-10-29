:canonical_id: IX.26
:volume: II
:book: IX
:proposition: 26
:type: proposition
:title: Proposition IX.26
:folios: 0421
:pages: 415
:dependencies: VII.def.7, IX.24

.. _IX.26:

.. folio:: 0421
   :page: 415

PROPOSITION 26.
===============

.. enunciation::

   If from an odd number an odd number be subtracted, the remainder will be even.

For from the odd number :g:`$AB$ <0421.g2:/ A B />` let the odd number :g:`$BC$ <0421.g2:/ B C />` be subtracted ;

I say that the remainder :g:`$CA$ <0421.g2:/ A C />` is even.

.. picture:: 0421.g2.svg
   :alt: Book IX, Proposition 26

.. subclause::

   For, since :g:`$AB$ <0421.g2:/ A B />` is odd, let the unit :g:`$BD$ <0421.g2:/ B D />` be subtracted ;

.. assertion:: [VII. Def. 7] <VII.def.7>

   therefore the remainder :g:`$AD$ <0421.g2:/ A D />` is even.

.. subclause:: [VII. Def. 7] <VII.def.7>

   For the same reason :g:`$CD$ <0421.g2:/ C D />` is also even ;

.. assertion:: [IX. 24] <IX.24>

   so that the remainder :g:`$CA$ <0421.g2:/ A C />` is also even.

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
     "IX.26" [label="IX.26", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.26: If from an odd number an odd number be subtracted, the remainder will be even.", URL="index.html", target="_top"];
     "IX.24" -> "VII.def.6";
     "IX.26" -> "VII.def.7";
     "IX.26" -> "IX.24";
   }
