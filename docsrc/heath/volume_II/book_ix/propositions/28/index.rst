:canonical_id: IX.28
:volume: II
:book: IX
:proposition: 28
:type: proposition
:title: Proposition IX.28
:folios: 0422
:pages: 416
:dependencies: VII.def.15, IX.21

.. _IX.28:

.. folio:: 0422
   :page: 416

PROPOSITION 28.
===============

.. enunciation::

   If an odd number by multiplying an even number make some number, the product will be even.

For let the odd number :g:`$A$ <0422.g2:A>` by multiplying the even number :g:`$B$ <0422.g2:B>` make :g:`$C$ <0422.g2:C>` ;

I say that :g:`$C$ <0422.g2:C>` is even.

.. picture:: 0422.g2.svg
   :alt: Book IX, Proposition 28

.. subclause::

   For, since :g:`$A$ <0422.g2:A>` by multiplying :g:`$B$ <0422.g2:B>` has made :g:`$C$ <0422.g2:C>`,

.. assertion::

   therefore :g:`$C$ <0422.g2:C>` is made up of as many numbers equal to :g:`$B$ <0422.g2:B>` as there are units in :g:`$A$ <0422.g2:A>`. :just:`[VII. Def. 15] <VII.def.15>`

.. subclause::

   And :g:`$B$ <0422.g2:B>` is even ;

.. assertion::

   therefore :g:`$C$ <0422.g2:C>` is made up of even numbers.

.. subclause::

   But, if as many even numbers as we please be added together, the whole is even. :just:`[IX. 21] <IX.21>`

.. assertion::

   Therefore :g:`$C$ <0422.g2:C>` is even.

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
     "VII.def.6" [label="VII.def.6", fillcolor="#224422", URL="../../../book_vii/definitions/index.html#vii-def-6", target="_top"];
     "VII.def.15" [label="VII.def.15", fillcolor="#224422", URL="../../../book_vii/definitions/index.html#vii-def-15", target="_top"];
     "IX.21" [label="IX.21", fillcolor="#222244", URL="../21/index.html", target="_top"];
     "IX.28" [label="IX.28", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.28" -> "VII.def.15";
     "IX.28" -> "IX.21";
   }
