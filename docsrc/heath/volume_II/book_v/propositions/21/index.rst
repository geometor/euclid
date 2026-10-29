:canonical_id: V.21
:volume: II
:book: V
:proposition: 21
:type: proposition
:title: Proposition V.21
:folios: 0184, 0185
:pages: 178, 179
:dependencies: V.8, V.10, V.13

.. _V.21:

.. folio:: 0184
   :page: 178

PROPOSITION 21.
===============

.. enunciation::

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

Let there be three magnitudes :g:`$A$ <0184.g1:A>`, :g:`$B$ <0184.g1:B>`, :g:`$C$ <0184.g1:C>`, and others :g:`$D$ <0184.g1:D>`, :g:`$E$ <0184.g1:E>`, :g:`$F$ <0184.g1:F>` equal to them in multitude, which taken two and two are in the same ratio, and let the proportion of them be perturbed, so that,

.. assertion::

   as :g:`$A$ <0184.g1:A>` is to :g:`$B$ <0184.g1:B>`, so is :g:`$E$ <0184.g1:E>` to :g:`$F$ <0184.g1:F>`,

.. assertion::

   and, as :g:`$B$ <0184.g1:B>` is to :g:`$C$ <0184.g1:C>`, so is :g:`$D$ <0184.g1:D>` to :g:`$E$ <0184.g1:E>`,

and let :g:`$A$ <0184.g1:A>` be greater than :g:`$C$ <0184.g1:C>` :term:`*ex aequali* <ex-aequali>`;

I say that :g:`$D$ <0184.g1:D>` will also be greater than :g:`$F$ <0184.g1:F>`; if :g:`$A$ <0184.g1:A>` is :eq:`equal <0184.g1:A = 0184.g1:C>` to :g:`$C$ <0184.g1:C>`, :eq:`equal <0184.g1:D = 0184.g1:F>`; and if less, less.

.. picture:: 0184.g1.svg
   :alt: Proposition 21

For, since :g:`$A$ <0184.g1:A>` is greater than :g:`$C$ <0184.g1:C>`, and :g:`$B$ <0184.g1:B>` is some other magnitude,

.. assertion:: [V. 8] <V.8>

   therefore :g:`$A$ <0184.g1:A>` has to :g:`$B$ <0184.g1:B>` a greater ratio than :g:`$C$ <0184.g1:C>` has to :g:`$B$ <0184.g1:B>`.

But, as :g:`$A$ <0184.g1:A>` is to :g:`$B$ <0184.g1:B>`, so is :g:`$E$ <0184.g1:E>` to :g:`$F$ <0184.g1:F>`, and, as :g:`$C$ <0184.g1:C>` is to :g:`$B$ <0184.g1:B>`, inversely, so is :g:`$E$ <0184.g1:E>` to :g:`$D$ <0184.g1:D>`.

.. assertion:: [V. 13] <V.13>

   Therefore also :g:`$E$ <0184.g1:E>` has to :g:`$F$ <0184.g1:F>` a greater ratio than :g:`$E$ <0184.g1:E>` has to :g:`$D$ <0184.g1:D>`.

.. subclause:: [V. 10] <V.10>

   But that to which the same has a greater ratio is less;

.. assertion::

   therefore :g:`$F$ <0184.g1:F>` is less than :g:`$D$ <0184.g1:D>`;

.. assertion::

   therefore :g:`$D$ <0184.g1:D>` is greater than :g:`$F$ <0184.g1:F>`.

.. _folio-ii-0185:

.. folio:: 0185
   :page: 179

Similarly we can prove that, if :g:`$A$ <0184.g1:A>` be :eq:`equal <0184.g1:A = 0184.g1:C>` to :g:`$C$ <0184.g1:C>`, :g:`$D$ <0184.g1:D>` will also be :eq:`equal <0184.g1:D = 0184.g1:F>` to :g:`$F$ <0184.g1:F>`; and if less, less.

.. qed::

   Therefore etc. :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "V.def.4" [label="V.def.4", fillcolor="#224422", URL="../../definitions/index.html#v-def-4", target="_top"];
     "V.def.5" [label="V.def.5", fillcolor="#224422", URL="../../definitions/index.html#v-def-5", target="_top"];
     "V.def.7" [label="V.def.7", fillcolor="#224422", URL="../../definitions/index.html#v-def-7", target="_top"];
     "V.1" [label="V.1", fillcolor="#222244", URL="../01/index.html", target="_top"];
     "V.7" [label="V.7", fillcolor="#222244", URL="../07/index.html", target="_top"];
     "V.8" [label="V.8", fillcolor="#222244", URL="../08/index.html", target="_top"];
     "V.10" [label="V.10", fillcolor="#222244", URL="../10/index.html", target="_top"];
     "V.13" [label="V.13", fillcolor="#222244", URL="../13/index.html", target="_top"];
     "V.21" [label="V.21", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "V.8" -> "V.def.4";
     "V.7" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.8" -> "V.1";
     "V.10" -> "V.7";
     "V.10" -> "V.8";
     "V.21" -> "V.8";
     "V.21" -> "V.10";
     "V.21" -> "V.13";
   }

Required for
------------

:ref:`V.23 <V.23>`

----

See :ref:`Commentary on Proposition V.21 <V.21.commentary>`.

.. toctree::
   :hidden:

   commentary
