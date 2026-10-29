:canonical_id: IX.7
:volume: II
:book: IX
:proposition: 7
:type: proposition
:title: Proposition IX.7
:folios: 0395, 0396
:pages: 389, 390
:dependencies: VII.def.13, VII.def.15

.. _IX.7:

.. folio:: 0395
   :page: 389

PROPOSITION 7.
==============

.. enunciation::

   If a composite number by multiplying any number make some number, the product will be solid.

For let the composite number :g:`$A$ <0395.g1:A>` by multiplying any number :g:`$B$ <0395.g1:B>` make :g:`$C$ <0395.g1:C>`;

I say that :g:`$C$ <0395.g1:C>` is solid.

.. picture:: 0395.g1.svg
   :alt: Proposition 7 Diagram

.. subclause::

   For, since :g:`$A$ <0395.g1:A>` is composite,

.. assertion::

   it will be measured by some number. :just:`[VII. Def. 13] <VII.def.13>`

Let it be measured by :g:`$D$ <0395.g1:D>`; and, as many times as :g:`$D$ <0395.g1:D>` measures :g:`$A$ <0395.g1:A>`, so many units let there be in :g:`$E$ <0395.g1:E>`.

.. _folio-ii-0396:

.. folio:: 0396
   :page: 390

.. subclause::

   Since then :g:`$D$ <0395.g1:D>` measures :g:`$A$ <0395.g1:A>` according to the units in :g:`$E$ <0395.g1:E>`,

.. assertion:: [VII. Def. 15] <VII.def.15>

   therefore :g:`$E$ <0395.g1:E>` by multiplying :g:`$D$ <0395.g1:D>` has made :g:`$A$ <0395.g1:A>`.

.. subclause::

   And, since :g:`$A$ <0395.g1:A>` by multiplying :g:`$B$ <0395.g1:B>` has made :g:`$C$ <0395.g1:C>`, and :g:`$A$ <0395.g1:A>` is the product of :g:`$D$ <0395.g1:D>`, :g:`$E$ <0395.g1:E>`,

.. assertion::

   therefore the product of :g:`$D$ <0395.g1:D>`, :g:`$E$ <0395.g1:E>` by multiplying :g:`$B$ <0395.g1:B>` has made :g:`$C$ <0395.g1:C>`.

.. assertion::

   Therefore :g:`$C$ <0395.g1:C>` is solid, and :g:`$D$ <0395.g1:D>`, :g:`$E$ <0395.g1:E>`, :g:`$B$ <0395.g1:B>` are its sides.

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
     "VII.def.13" [label="VII.def.13", fillcolor="#224422", URL="../../../book_vii/definitions/index.html#vii-def-13", target="_top"];
     "VII.def.15" [label="VII.def.15", fillcolor="#224422", URL="../../../book_vii/definitions/index.html#vii-def-15", target="_top"];
     "IX.7" [label="IX.7", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "IX.7" -> "VII.def.13";
     "IX.7" -> "VII.def.15";
   }

----

See :ref:`Commentary on Proposition IX.7 <IX.7.commentary>`.

.. toctree::
   :hidden:

   commentary
