:canonical_id: IX.25
:volume: II
:book: IX
:proposition: 25
:type: proposition
:title: Proposition IX.25
:folios: 0421
:pages: 415
:dependencies: VII.def.7, IX.24

.. _IX.25:

.. folio:: 0421
   :page: 415

PROPOSITION 25.
===============

.. enunciation::

   If from an even number an odd number be subtracted, the remainder will be odd.

For from the even number :g:`$AB$ <0421.g1:/ A B />` let the odd number :g:`$BC$ <0421.g1:/ B C />` be subtracted ;

I say that the remainder :g:`$CA$ <0421.g1:/ A C />` is odd.

.. picture:: 0421.g1.svg
   :alt: Book IX, Proposition 25

For let the unit :g:`$CD$ <0421.g1:/ C D />` be subtracted from :g:`$BC$ <0421.g1:/ B C />` ;

.. assertion:: [VII. Def. 7] <VII.def.7>

   therefore :g:`$DB$ <0421.g1:/ B D />` is even.

.. subclause::

   But :g:`$AB$ <0421.g1:/ A B />` is also even ;

.. assertion:: [IX. 24] <IX.24>

   therefore the remainder :g:`$AD$ <0421.g1:/ A D />` is also even.

.. subclause::

   And :g:`$CD$ <0421.g1:/ C D />` is an unit ;

.. assertion:: [VII. Def. 7] <VII.def.7>

   therefore :g:`$CA$ <0421.g1:/ A C />` is odd.

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
     "IX.25" [label="IX.25", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.25: If from an even number an odd number be subtracted, the remainder will be odd.", URL="index.html", target="_top"];
     "IX.24" -> "VII.def.6";
     "IX.25" -> "VII.def.7";
     "IX.25" -> "IX.24";
   }
