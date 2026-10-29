:canonical_id: IX.29
:volume: II
:book: IX
:proposition: 29
:type: proposition
:title: Proposition IX.29
:folios: 0422, 0423
:pages: 416, 417
:dependencies: VII.def.15, IX.23

.. _IX.29:

.. folio:: 0422
   :page: 416

PROPOSITION 29.
===============

.. enunciation::

   If an odd number by multiplying an odd number make some number, the product will be odd.

For let the odd number :g:`A <0422.g3:A>` by multiplying the odd number :g:`B <0422.g3:B>` make :g:`C <0422.g3:C>` ;

I say that :g:`C <0422.g3:C>` is odd.

.. picture:: 0422.g3.svg
   :alt: Book IX, Proposition 29

.. subclause::

   For, since :g:`A <0422.g3:A>` by multiplying :g:`B <0422.g3:B>` has made :g:`C <0422.g3:C>`,

.. _folio-ii-0423:

.. folio:: 0423
   :page: 417

.. assertion::

   therefore :g:`C <0422.g3:C>` is made up of as many numbers equal to :g:`B <0422.g3:B>` as there are units in :g:`A <0422.g3:A>`. :just:`[VII. Def. 15] <VII.def.15>`

.. subclause::

   And each of the numbers :g:`A <0422.g3:A>`, :g:`B <0422.g3:B>` is odd;

.. assertion::

   therefore :g:`C <0422.g3:C>` is made up of odd numbers the multitude of which is odd.

.. assertion:: [IX. 23] <IX.23>

   Thus :g:`C <0422.g3:C>` is odd.

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
     "VII.def.15" [label="VII.def.15", fillcolor="#224422", tooltip="VII.def.15: A number is said to multiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", URL="../../../book_vii/definitions/index.html#vii-def-15", target="_top"];
     "IX.21" [label="IX.21", fillcolor="#222244", tooltip="IX.21: If as many even numbers as we please be added together, the whole is even.", URL="../21/index.html", target="_top"];
     "IX.22" [label="IX.22", fillcolor="#222244", tooltip="IX.22: If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.", URL="../22/index.html", target="_top"];
     "IX.23" [label="IX.23", fillcolor="#222244", tooltip="IX.23: If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.", URL="../23/index.html", target="_top"];
     "IX.29" [label="IX.29", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.29: If an odd number by multiplying an odd number make some number, the product will be odd.", URL="index.html", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.29" -> "VII.def.15";
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
     "IX.23" -> "IX.22";
     "IX.29" -> "IX.23";
   }
