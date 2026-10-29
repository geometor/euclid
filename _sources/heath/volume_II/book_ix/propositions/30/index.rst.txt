:canonical_id: IX.30
:volume: II
:book: IX
:proposition: 30
:type: proposition
:title: Proposition IX.30
:folios: 0423
:pages: 417
:dependencies: IX.23

.. _IX.30:

.. folio:: 0423
   :page: 417

PROPOSITION 30.
===============

.. enunciation::

   If an odd number measure an even number, it will also measure the half of it.

For let the odd number :g:`$A$ <0423.g1:A>` measure the even number :g:`$B$ <0423.g1:B>`;

I say that it will also measure the half of it.

.. picture:: 0423.g1.svg
   :alt: Book IX, Proposition 30

.. subclause::

   For, since :g:`$A$ <0423.g1:A>` measures :g:`$B$ <0423.g1:B>`, let it measure it according to :g:`$C$ <0423.g1:C>`;

I say that :g:`$C$ <0423.g1:C>` is not odd.

For, if possible, let it be so.

.. subclause::

   Then, since :g:`$A$ <0423.g1:A>` measures :g:`$B$ <0423.g1:B>` according to :g:`$C$ <0423.g1:C>`,

.. assertion::

   therefore :g:`$A$ <0423.g1:A>` by multiplying :g:`$C$ <0423.g1:C>` has made :g:`$B$ <0423.g1:B>`.

.. assertion::

   Therefore :g:`$B$ <0423.g1:B>` is made up of odd numbers the multitude of which is odd.

.. assertion::

   Therefore :g:`$B$ <0423.g1:B>` is odd: :just:`[IX. 23] <IX.23>` which is absurd, for by hypothesis it is even.

.. assertion::

   Therefore :g:`$C$ <0423.g1:C>` is not odd; therefore :g:`$C$ <0423.g1:C>` is even.

.. assertion::

   Thus :g:`$A$ <0423.g1:A>` measures :g:`$B$ <0423.g1:B>` an even number of times.

.. assertion::

   For this reason then it also measures the half of it.

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
     "VII.def.7" [label="VII.def.7", fillcolor="#224422", URL="../../../book_vii/definitions/index.html#vii-def-7", target="_top"];
     "IX.21" [label="IX.21", fillcolor="#222244", URL="../21/index.html", target="_top"];
     "IX.22" [label="IX.22", fillcolor="#222244", URL="../22/index.html", target="_top"];
     "IX.23" [label="IX.23", fillcolor="#222244", URL="../23/index.html", target="_top"];
     "IX.30" [label="IX.30", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
     "IX.23" -> "IX.22";
     "IX.30" -> "IX.23";
   }

Required for
------------

:ref:`IX.31 <IX.31>`
