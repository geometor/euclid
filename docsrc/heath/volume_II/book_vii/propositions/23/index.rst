:canonical_id: VII.23
:volume: II
:book: VII
:proposition: 23
:type: proposition
:title: Proposition VII.23
:folios: 0330, 0331
:pages: 324, 325
:dependencies: VII.def.12

.. _VII.23:

.. folio:: 0330
   :page: 324

PROPOSITION 23.
===============

.. enunciation::

   If two numbers be prime to one another, the number which measures the one of them will be prime to the remaining number.

Let :g:`A <0330.g1:A>`, :g:`B <0330.g1:B>` be two numbers prime to one another, and let any number :g:`C <0330.g1:C>` measure :g:`A <0330.g1:A>`;

I say that :g:`C <0330.g1:C>`, :g:`B <0330.g1:B>` are also prime to one another.

.. picture:: 0330.g1.svg
   :alt: Book VII, Proposition 23

.. subclause::

   For, if :g:`C <0330.g1:C>`, :g:`B <0330.g1:B>` are not prime to one another, some number will measure :g:`C <0330.g1:C>`, :g:`B <0330.g1:B>`.

Let a number measure them, and let it be :g:`D <0330.g1:D>`.

.. subclause::

   Since :g:`D <0330.g1:D>` measures :g:`C <0330.g1:C>`, and :g:`C <0330.g1:C>` measures :g:`A <0330.g1:A>`,

.. assertion::

   therefore :g:`D <0330.g1:D>` also measures :g:`A <0330.g1:A>`.

.. subclause::

   But it also measures :g:`B <0330.g1:B>` ;

.. _folio-ii-0331:

.. folio:: 0331
   :page: 325

.. assertion::

   therefore :g:`D <0330.g1:D>` measures :g:`A <0330.g1:A>`, :g:`B <0330.g1:B>` which are prime to one another : which is impossible. :just:`[VII. Def. 12] <VII.def.12>`

.. assertion::

   Therefore no number will measure the numbers :g:`C <0330.g1:C>`, :g:`B <0330.g1:B>`.

.. assertion::

   Therefore :g:`C <0330.g1:C>`, :g:`B <0330.g1:B>` are prime to one another.

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
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../definitions/index.html#vii-def-12", target="_top"];
     "VII.23" [label="VII.23", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.23: If two numbers be prime to one another, the number which measures the one of them will be prime to the remaining number.", URL="index.html", target="_top"];
     "VII.23" -> "VII.def.12";
   }

Required for
------------

:ref:`VII.24 <VII.24>`, :ref:`VII.25 <VII.25>`, :ref:`VII.26 <VII.26>`, :ref:`VII.27 <VII.27>`, :ref:`VIII.2 <VIII.2>`, :ref:`VIII.3 <VIII.3>`, :ref:`VIII.6 <VIII.6>`, :ref:`VIII.7 <VIII.7>`, :ref:`VIII.8 <VIII.8>`, :ref:`VIII.9 <VIII.9>`, :ref:`VIII.14 <VIII.14>`, :ref:`VIII.15 <VIII.15>`, :ref:`VIII.16 <VIII.16>`, :ref:`VIII.17 <VIII.17>`, :ref:`VIII.21 <VIII.21>`, :ref:`VIII.23 <VIII.23>`, :ref:`VIII.24 <VIII.24>`, :ref:`VIII.25 <VIII.25>`, :ref:`VIII.26 <VIII.26>`, :ref:`VIII.27 <VIII.27>`, :ref:`IX.1 <IX.1>`, :ref:`IX.2 <IX.2>`, :ref:`IX.3 <IX.3>`, :ref:`IX.4 <IX.4>`, :ref:`IX.5 <IX.5>`, :ref:`IX.6 <IX.6>`, :ref:`IX.8 <IX.8>`, :ref:`IX.9 <IX.9>`, :ref:`IX.10 <IX.10>`, :ref:`IX.12 <IX.12>`, :ref:`IX.13 <IX.13>`, :ref:`IX.15 <IX.15>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`, :ref:`X.9 <X.9>`, :ref:`X.10 <X.10>`, :ref:`X.29 <X.29>`, :ref:`X.30 <X.30>`, :ref:`X.31 <X.31>`, :ref:`X.32 <X.32>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.48 <X.48>`, :ref:`X.49 <X.49>`, :ref:`X.50 <X.50>`, :ref:`X.51 <X.51>`, :ref:`X.52 <X.52>`, :ref:`X.53 <X.53>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition VII.23 <VII.23.commentary>`.

.. toctree::
   :hidden:

   commentary
