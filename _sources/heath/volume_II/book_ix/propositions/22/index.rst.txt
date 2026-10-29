:canonical_id: IX.22
:volume: II
:book: IX
:proposition: 22
:type: proposition
:title: Proposition IX.22
:folios: 0419, 0420
:pages: 413, 414
:dependencies: VII.def.7, IX.21

.. _IX.22:

.. folio:: 0419
   :page: 413

PROPOSITION 22.
===============

.. enunciation::

   If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.

For let as many odd numbers as we please, :g:`AB <0420.g1:/ A B />`, :g:`BC <0420.g1:/ B C />`, :g:`CD <0420.g1:/ C D />`, :g:`DE <0420.g1:/ D E />`, even in multitude, be added together ;

I say that the whole :g:`AE <0420.g1:/ A E />` is even.

.. _folio-ii-0420:

.. folio:: 0420
   :page: 414

.. subclause::

   For, since each of the numbers :g:`AB <0420.g1:/ A B />`, :g:`BC <0420.g1:/ B C />`, :g:`CD <0420.g1:/ C D />`, :g:`DE <0420.g1:/ D E />` is odd, if an unit be subtracted from each, each of the remainders will be even ; :just:`[VII. Def. 7] <VII.def.7>`

.. assertion:: [IX. 21] <IX.21>

   so that the sum of them will be even.

.. picture:: 0420.g1.svg
   :alt: Book IX, Proposition 22

.. subclause::

   But the multitude of the units is also even.

.. assertion:: [IX. 21] <IX.21>

   Therefore the whole :g:`AE <0420.g1:/ A E />` is also even.

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
     "IX.21" [label="IX.21", fillcolor="#222244", tooltip="IX.21: If as many even numbers as we please be added together, the whole is even.", URL="../21/index.html", target="_top"];
     "IX.22" [label="IX.22", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.22: If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.", URL="index.html", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.22" -> "VII.def.7";
     "IX.22" -> "IX.21";
   }

Required for
------------

:ref:`IX.23 <IX.23>`, :ref:`IX.29 <IX.29>`, :ref:`IX.30 <IX.30>`, :ref:`IX.31 <IX.31>`
