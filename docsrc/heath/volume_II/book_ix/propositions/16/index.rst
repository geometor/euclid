:canonical_id: IX.16
:volume: II
:book: IX
:proposition: 16
:type: proposition
:title: Proposition IX.16
:folios: 0412
:pages: 406
:dependencies: VII.20, VII.21

.. _IX.16:

.. _folio-ii-0412:

.. folio:: 0412
   :page: 406

PROPOSITION 16.
===============

.. enunciation::

   If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

For let the two numbers :g:`$A$ <0412.g1:A>`, :g:`$B$ <0412.g1:B>` be prime to one another ;

I say that :g:`$B$ <0412.g1:B>` is not to any other number as :g:`$A$ <0412.g1:A>` is to :g:`$B$ <0412.g1:B>`.

.. picture:: 0412.g1.svg
   :alt: Proposition 16

For, if possible, as :g:`$A$ <0412.g1:A>` is to :g:`$B$ <0412.g1:B>`, so let :g:`$B$ <0412.g1:B>` be to :g:`$C$ <0412.g1:C>`.

.. subclause::

   Now :g:`$A$ <0412.g1:A>`, :g:`$B$ <0412.g1:B>` are prime, primes are also least, :just:`[VII. 21] <VII.21>` and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent ; :just:`[VII. 20] <VII.20>`

.. assertion::

   therefore :g:`$A$ <0412.g1:A>` measures :g:`$B$ <0412.g1:B>` as antecedent antecedent.

.. subclause::

   But it also measures itself ;

.. assertion::

   therefore :g:`$A$ <0412.g1:A>` measures :g:`$A$ <0412.g1:A>`, :g:`$B$ <0412.g1:B>` which are prime to one another : which is absurd.

.. assertion::

   Therefore :g:`$B$ <0412.g1:B>` will not be to :g:`$C$ <0412.g1:C>`, as :g:`$A$ <0412.g1:A>` is to :g:`$B$ <0412.g1:B>`.

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
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", URL="../../../book_vii/definitions/index.html#vii-def-12", target="_top"];
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", URL="../../../book_vii/definitions/index.html#vii-def-20", target="_top"];
     "VII.1" [label="VII.1", fillcolor="#222244", URL="../../../book_vii/propositions/01/index.html", target="_top"];
     "VII.2" [label="VII.2", fillcolor="#222244", URL="../../../book_vii/propositions/02/index.html", target="_top"];
     "VII.4" [label="VII.4", fillcolor="#222244", URL="../../../book_vii/propositions/04/index.html", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", URL="../../../book_vii/propositions/05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", URL="../../../book_vii/propositions/06/index.html", target="_top"];
     "VII.9" [label="VII.9", fillcolor="#222244", URL="../../../book_vii/propositions/09/index.html", target="_top"];
     "VII.10" [label="VII.10", fillcolor="#222244", URL="../../../book_vii/propositions/10/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", URL="../../../book_vii/propositions/12/index.html", target="_top"];
     "VII.13" [label="VII.13", fillcolor="#222244", URL="../../../book_vii/propositions/13/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", URL="../../../book_vii/propositions/15/index.html", target="_top"];
     "VII.16" [label="VII.16", fillcolor="#222244", URL="../../../book_vii/propositions/16/index.html", target="_top"];
     "VII.20" [label="VII.20", fillcolor="#222244", URL="../../../book_vii/propositions/20/index.html", target="_top"];
     "VII.21" [label="VII.21", fillcolor="#222244", URL="../../../book_vii/propositions/21/index.html", target="_top"];
     "IX.16" [label="IX.16", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.2" -> "VII.1";
     "VII.4" -> "VII.2";
     "VII.20" -> "VII.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.10" -> "VII.9";
     "VII.13" -> "VII.10";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.20" -> "VII.13";
     "VII.16" -> "VII.15";
     "VII.21" -> "VII.16";
     "VII.21" -> "VII.20";
     "IX.16" -> "VII.20";
     "IX.16" -> "VII.21";
   }

Required for
------------

:ref:`IX.18 <IX.18>`

----

See :ref:`Commentary on Proposition IX.16 <IX.16.commentary>`.

.. toctree::
   :hidden:

   commentary
