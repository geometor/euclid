:canonical_id: VII.38
:volume: II
:book: VII
:proposition: 38
:type: proposition
:title: Proposition VII.38
:folios: 0348, 0349
:pages: 342, 343
:dependencies: VII.15

.. _VII.38:

.. folio:: 0348
   :page: 342

PROPOSITION 38.
===============

.. enunciation::

   If a number have any part whatever, it will be measured by a number called by the same name as the part.

For let the number :g:`$A$ <0348.g1:A>` have any part whatever, :g:`$B$ <0348.g1:B>`, and let :g:`$C$ <0348.g1:C>` be a number called by the same name as the part :g:`$B$ <0348.g1:B>`;

I say that :g:`$C$ <0348.g1:C>` measures :g:`$A$ <0348.g1:A>`.

.. picture:: 0348.g1.svg
   :alt: Proposition 38

.. subclause::

   For, since :g:`$B$ <0348.g1:B>` is a part of :g:`$A$ <0348.g1:A>` called by the same name as :g:`$C$ <0348.g1:C>`, and the unit :g:`$D$ <0348.g1:D>` is also a part of :g:`$C$ <0348.g1:C>` called by the same name as it,

.. assertion::

   therefore, whatever part the unit :g:`$D$ <0348.g1:D>` is of the number :g:`$C$ <0348.g1:C>`, the same part is :g:`$B$ <0348.g1:B>` of :g:`$A$ <0348.g1:A>` also;

.. assertion::

   therefore the unit :g:`$D$ <0348.g1:D>` measures the number :g:`$C$ <0348.g1:C>` the same number of times that :g:`$B$ <0348.g1:B>` measures :g:`$A$ <0348.g1:A>`.

.. _folio-ii-0349:

.. folio:: 0349
   :page: 343

.. assertion::

   Therefore, alternately, the unit :g:`$D$ <0348.g1:D>` measures the number :g:`$B$ <0348.g1:B>` the same number of times that :g:`$C$ <0348.g1:C>` measures :g:`$A$ <0348.g1:A>`. :just:`[VII. 15] <VII.15>`

.. assertion::

   Therefore :g:`$C$ <0348.g1:C>` measures :g:`$A$ <0348.g1:A>`.

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
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", URL="../../definitions/index.html#vii-def-20", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", URL="../05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", URL="../06/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", URL="../12/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", URL="../15/index.html", target="_top"];
     "VII.38" [label="VII.38", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "VII.12" -> "VII.def.20";
     "VII.6" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.6";
     "VII.15" -> "VII.12";
     "VII.38" -> "VII.15";
   }

Required for
------------

:ref:`VII.39 <VII.39>`

----

See :ref:`Commentary on Proposition VII.38 <VII.38.commentary>`.

.. toctree::
   :hidden:

   commentary
