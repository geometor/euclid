:canonical_id: VII.14
:volume: II
:book: VII
:proposition: 14
:type: proposition
:title: Proposition VII.14
:folios: 0319, 0320
:pages: 313, 314
:dependencies: VII.13

.. _VII.14:

.. folio:: 0319
   :page: 313

PROPOSITION 14.
===============

.. enunciation::

   If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they will also be in the same ratio ex aequali.

Let there be as many numbers as we please :g:`A <0319.g2:A>`, :g:`B <0319.g2:B>`, :g:`C <0319.g2:C>`, and others equal to them in multitude :g:`D <0319.g2:D>`, :g:`E <0319.g2:E>`, :g:`F <0319.g2:F>`, which taken two and two are in the same ratio, so that, as :g:`A <0319.g2:A>` is to :g:`B <0319.g2:B>`, so is :g:`D <0319.g2:D>` to :g:`E <0319.g2:E>`, and, as :g:`B <0319.g2:B>` is to :g:`C <0319.g2:C>`, so is :g:`E <0319.g2:E>` to :g:`F <0319.g2:F>`;

I say that, :term:`*ex aequali* <ex-aequali>`, as :g:`A <0319.g2:A>` is to :g:`C <0319.g2:C>`, so also is :g:`D <0319.g2:D>` to :g:`F <0319.g2:F>`.

.. picture:: 0319.g2.svg
   :alt: Proposition 14 Diagram

.. subclause::

   For, since, as :g:`A <0319.g2:A>` is to :g:`B <0319.g2:B>`, so is :g:`D <0319.g2:D>` to :g:`E <0319.g2:E>`,

.. assertion::

   therefore, alternately, as :g:`A <0319.g2:A>` is to :g:`D <0319.g2:D>`, so is :g:`B <0319.g2:B>` to :g:`E <0319.g2:E>`. :just:`[VII. 13] <VII.13>`

.. _folio-ii-0320:

.. folio:: 0320
   :page: 314

.. subclause::

   Again, since, as :g:`B <0319.g2:B>` is to :g:`C <0319.g2:C>`, so is :g:`E <0319.g2:E>` to :g:`F <0319.g2:F>`,

.. assertion::

   therefore, alternately, as :g:`B <0319.g2:B>` is to :g:`E <0319.g2:E>`, so is :g:`C <0319.g2:C>` to :g:`F <0319.g2:F>`. :just:`[VII. 13] <VII.13>`

.. subclause::

   But, as :g:`B <0319.g2:B>` is to :g:`E <0319.g2:E>`, so is :g:`A <0319.g2:A>` to :g:`D <0319.g2:D>`;

.. assertion::

   therefore also, as :g:`A <0319.g2:A>` is to :g:`D <0319.g2:D>`, so is :g:`C <0319.g2:C>` to :g:`F <0319.g2:F>`.

.. assertion::

   Therefore, alternately, as :g:`A <0319.g2:A>` is to :g:`C <0319.g2:C>`, so is :g:`D <0319.g2:D>` to :g:`F <0319.g2:F>`. :just:`[id.]`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../definitions/index.html#vii-def-20", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", tooltip="VII.6: If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", URL="../06/index.html", target="_top"];
     "VII.9" [label="VII.9", fillcolor="#222244", tooltip="VII.9: If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts…", URL="../09/index.html", target="_top"];
     "VII.10" [label="VII.10", fillcolor="#222244", tooltip="VII.10: If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part…", URL="../10/index.html", target="_top"];
     "VII.13" [label="VII.13", fillcolor="#222244", tooltip="VII.13: If four numbers be proportional, they will also be proportional alternately.", URL="../13/index.html", target="_top"];
     "VII.14" [label="VII.14", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.14: If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they will also be in the same ratio ex aequali.", URL="index.html", target="_top"];
     "VII.13" -> "VII.def.20";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.10" -> "VII.9";
     "VII.13" -> "VII.10";
     "VII.14" -> "VII.13";
   }

Required for
------------

:ref:`VIII.1 <VIII.1>`, :ref:`VIII.2 <VIII.2>`, :ref:`VIII.3 <VIII.3>`, :ref:`VIII.5 <VIII.5>`, :ref:`VIII.6 <VIII.6>`, :ref:`VIII.7 <VIII.7>`, :ref:`VIII.8 <VIII.8>`, :ref:`VIII.9 <VIII.9>`, :ref:`VIII.13 <VIII.13>`, :ref:`VIII.14 <VIII.14>`, :ref:`VIII.15 <VIII.15>`, :ref:`VIII.16 <VIII.16>`, :ref:`VIII.17 <VIII.17>`, :ref:`VIII.21 <VIII.21>`, :ref:`VIII.23 <VIII.23>`, :ref:`VIII.24 <VIII.24>`, :ref:`VIII.25 <VIII.25>`, :ref:`VIII.26 <VIII.26>`, :ref:`VIII.27 <VIII.27>`, :ref:`IX.1 <IX.1>`, :ref:`IX.2 <IX.2>`, :ref:`IX.3 <IX.3>`, :ref:`IX.4 <IX.4>`, :ref:`IX.5 <IX.5>`, :ref:`IX.6 <IX.6>`, :ref:`IX.8 <IX.8>`, :ref:`IX.9 <IX.9>`, :ref:`IX.10 <IX.10>`, :ref:`IX.12 <IX.12>`, :ref:`IX.13 <IX.13>`, :ref:`IX.15 <IX.15>`, :ref:`IX.19 <IX.19>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`, :ref:`X.9 <X.9>`, :ref:`X.10 <X.10>`, :ref:`X.29 <X.29>`, :ref:`X.30 <X.30>`, :ref:`X.31 <X.31>`, :ref:`X.32 <X.32>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.48 <X.48>`, :ref:`X.49 <X.49>`, :ref:`X.50 <X.50>`, :ref:`X.51 <X.51>`, :ref:`X.52 <X.52>`, :ref:`X.53 <X.53>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition VII.14 <VII.14.commentary>`.

.. toctree::
   :hidden:

   commentary
