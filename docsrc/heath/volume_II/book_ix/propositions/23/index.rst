:canonical_id: IX.23
:volume: II
:book: IX
:proposition: 23
:type: proposition
:title: Proposition IX.23
:folios: 0420
:pages: 414
:dependencies: VII.def.7, IX.21, IX.22

.. _IX.23:

.. folio:: 0420
   :page: 414

PROPOSITION 23.
===============

.. enunciation::

   If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.

For let as many odd numbers as we please, :g:`$AB$ <0420.g2:/ A B />`, :g:`$BC$ <0420.g2:/ B C />`, :g:`$CD$ <0420.g2:/ C D />`, the multitude of which is odd,\ [#f1]_ be added together ;

I say that the whole :g:`$AD$ <0420.g2:/ A D />` is also odd.

.. picture:: 0420.g2.svg
   :alt: Book IX, Proposition 23

Let the unit :g:`$DE$ <0420.g2:/ D E />` be subtracted from :g:`$CD$ <0420.g2:/ C D />` ;

.. assertion:: [VII. Def. 7] <VII.def.7>

   therefore the remainder :g:`$CE$ <0420.g2:/ C E />` is even.

.. subclause:: [IX. 22] <IX.22>

   But :g:`$CA$ <0420.g2:/ A C />` is also even ;

.. assertion:: [IX. 21] <IX.21>

   therefore the whole :g:`$AE$ <0420.g2:/ A E />` is also even.

.. subclause::

   And :g:`$DE$ <0420.g2:/ D E />` is an unit.

.. assertion:: [VII. Def. 7] <VII.def.7>

   Therefore :g:`$AD$ <0420.g2:/ A D />` is odd.

.. qed::

   :just:`Q. E. D.`

.. [#f1] Literally “let there be as many numbers as we please, of which *let the multitude be odd*.” This form, natural in Greek, is awkward in English.

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
     "IX.21" [label="IX.21", fillcolor="#222244", tooltip="IX.21: If as many even numbers as we please be added together, the whole is even.", URL="../21/index.html", target="_top"];
     "IX.22" [label="IX.22", fillcolor="#222244", tooltip="IX.22: If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.", URL="../22/index.html", target="_top"];
     "IX.23" [label="IX.23", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.23: If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.", URL="index.html", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
     "IX.23" -> "IX.22";
   }

Required for
------------

:ref:`IX.29 <IX.29>`, :ref:`IX.30 <IX.30>`, :ref:`IX.31 <IX.31>`
