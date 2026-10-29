:canonical_id: VII.16
:volume: II
:book: VII
:proposition: 16
:type: proposition
:title: Proposition VII.16
:folios: 0322
:pages: 316
:dependencies: VII.15

.. _VII.16:

.. _folio-ii-0322:

.. folio:: 0322
   :page: 316

PROPOSITION 16.
===============

.. enunciation::

   If two numbers by multiplying one another make certain numbers, the numbers so produced\ [#f1]_ will be equal to one another.

Let :g:`$A$ <0322.g1:A>`, :g:`$B$ <0322.g1:B>` be two numbers, and let :g:`$A$ <0322.g1:A>` by multiplying :g:`$B$ <0322.g1:B>` make :g:`$C$ <0322.g1:C>`, and :g:`$B$ <0322.g1:B>` by multiplying :g:`$A$ <0322.g1:A>` make :g:`$D$ <0322.g1:D>`;

I say that :g:`$C$ <0322.g1:C>` is :eq:`equal <0322.g1:C = 0322.g1:D>` to :g:`$D$ <0322.g1:D>`.

.. picture:: 0322.g1.svg
   :alt: Proposition 16 Diagram

.. subclause::

   For, since :g:`$A$ <0322.g1:A>` by multiplying :g:`$B$ <0322.g1:B>` has made :g:`$C$ <0322.g1:C>`,

.. assertion::

   therefore :g:`$B$ <0322.g1:B>` measures :g:`$C$ <0322.g1:C>` according to the units in :g:`$A$ <0322.g1:A>`.

.. subclause::

   But the unit :g:`$E$ <0322.g1:E>` also measures the number :g:`$A$ <0322.g1:A>` according to the units in it;

.. assertion::

   therefore the unit :g:`$E$ <0322.g1:E>` measures :g:`$A$ <0322.g1:A>` the same number of times that :g:`$B$ <0322.g1:B>` measures :g:`$C$ <0322.g1:C>`.

.. assertion::

   Therefore, alternately, the unit :g:`$E$ <0322.g1:E>` measures the number :g:`$B$ <0322.g1:B>` the same number of times that :g:`$A$ <0322.g1:A>` measures :g:`$C$ <0322.g1:C>`. :just:`[VII. 15] <VII.15>`

.. subclause::

   Again, since :g:`$B$ <0322.g1:B>` by multiplying :g:`$A$ <0322.g1:A>` has made :g:`$D$ <0322.g1:D>`,

.. assertion::

   therefore :g:`$A$ <0322.g1:A>` measures :g:`$D$ <0322.g1:D>` according to the units in :g:`$B$ <0322.g1:B>`.

.. subclause::

   But the unit :g:`$E$ <0322.g1:E>` also measures :g:`$B$ <0322.g1:B>` according to the units in it;

.. assertion::

   therefore the unit :g:`$E$ <0322.g1:E>` measures the number :g:`$B$ <0322.g1:B>` the same number of times that :g:`$A$ <0322.g1:A>` measures :g:`$D$ <0322.g1:D>`.

.. subclause::

   But the unit :g:`$E$ <0322.g1:E>` measured the number :g:`$B$ <0322.g1:B>` the same number of times that :g:`$A$ <0322.g1:A>` measures :g:`$C$ <0322.g1:C>`;

.. assertion::

   therefore :g:`$A$ <0322.g1:A>` measures each of the numbers :g:`$C$ <0322.g1:C>`, :g:`$D$ <0322.g1:D>` the same number of times.

.. assertion::

   Therefore :g:`$C$ <0322.g1:C>` is :eq:`equal <0322.g1:C = 0322.g1:D>` to :g:`$D$ <0322.g1:D>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **The numbers so produced.** The Greek has οἱ γενόμενοι ἐξ αὐτῶν, "the (numbers) produced *from them*." By "from them" Euclid means "from the original numbers," though this is not very clear even in the Greek. I think ambiguity is best avoided by leaving out the words.

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
     "VII.12" [label="VII.12", fillcolor="#222244", tooltip="VII.12: If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", URL="../12/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", tooltip="VII.15: If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of…", URL="../15/index.html", target="_top"];
     "VII.16" [label="VII.16", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.16: If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.", URL="index.html", target="_top"];
     "VII.12" -> "VII.def.20";
     "VII.6" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.6";
     "VII.15" -> "VII.12";
     "VII.16" -> "VII.15";
   }

Required for
------------

:ref:`VII.18 <VII.18>`, :ref:`VII.19 <VII.19>`, :ref:`VII.21 <VII.21>`, :ref:`VII.24 <VII.24>`, :ref:`VII.25 <VII.25>`, :ref:`VII.26 <VII.26>`, :ref:`VII.27 <VII.27>`, :ref:`VII.30 <VII.30>`, :ref:`VII.33 <VII.33>`, :ref:`VII.34 <VII.34>`, :ref:`VII.36 <VII.36>`, :ref:`VII.39 <VII.39>`, :ref:`VIII.1 <VIII.1>`, :ref:`VIII.2 <VIII.2>`, :ref:`VIII.3 <VIII.3>`, :ref:`VIII.4 <VIII.4>`, :ref:`VIII.5 <VIII.5>`, :ref:`VIII.6 <VIII.6>`, :ref:`VIII.7 <VIII.7>`, :ref:`VIII.8 <VIII.8>`, :ref:`VIII.9 <VIII.9>`, :ref:`VIII.10 <VIII.10>`, :ref:`VIII.11 <VIII.11>`, :ref:`VIII.12 <VIII.12>`, :ref:`VIII.14 <VIII.14>`, :ref:`VIII.15 <VIII.15>`, :ref:`VIII.16 <VIII.16>`, :ref:`VIII.17 <VIII.17>`, :ref:`VIII.19 <VIII.19>`, :ref:`VIII.20 <VIII.20>`, :ref:`VIII.21 <VIII.21>`, :ref:`VIII.22 <VIII.22>`, :ref:`VIII.23 <VIII.23>`, :ref:`VIII.24 <VIII.24>`, :ref:`VIII.25 <VIII.25>`, :ref:`VIII.26 <VIII.26>`, :ref:`VIII.27 <VIII.27>`, :ref:`IX.1 <IX.1>`, :ref:`IX.2 <IX.2>`, :ref:`IX.3 <IX.3>`, :ref:`IX.4 <IX.4>`, :ref:`IX.5 <IX.5>`, :ref:`IX.6 <IX.6>`, :ref:`IX.8 <IX.8>`, :ref:`IX.9 <IX.9>`, :ref:`IX.10 <IX.10>`, :ref:`IX.12 <IX.12>`, :ref:`IX.13 <IX.13>`, :ref:`IX.14 <IX.14>`, :ref:`IX.15 <IX.15>`, :ref:`IX.16 <IX.16>`, :ref:`IX.17 <IX.17>`, :ref:`IX.18 <IX.18>`, :ref:`IX.19 <IX.19>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`, :ref:`X.9 <X.9>`, :ref:`X.10 <X.10>`, :ref:`X.12 <X.12>`, :ref:`X.13 <X.13>`, :ref:`X.17 <X.17>`, :ref:`X.18 <X.18>`, :ref:`X.22 <X.22>`, :ref:`X.23 <X.23>`, :ref:`X.24 <X.24>`, :ref:`X.25 <X.25>`, :ref:`X.26 <X.26>`, :ref:`X.27 <X.27>`, :ref:`X.28 <X.28>`, :ref:`X.29 <X.29>`, :ref:`X.30 <X.30>`, :ref:`X.31 <X.31>`, :ref:`X.32 <X.32>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.36 <X.36>`, :ref:`X.37 <X.37>`, :ref:`X.38 <X.38>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.42 <X.42>`, :ref:`X.43 <X.43>`, :ref:`X.44 <X.44>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.47 <X.47>`, :ref:`X.48 <X.48>`, :ref:`X.49 <X.49>`, :ref:`X.50 <X.50>`, :ref:`X.51 <X.51>`, :ref:`X.52 <X.52>`, :ref:`X.53 <X.53>`, :ref:`X.54 <X.54>`, :ref:`X.55 <X.55>`, :ref:`X.56 <X.56>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.61 <X.61>`, :ref:`X.62 <X.62>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.66 <X.66>`, :ref:`X.67 <X.67>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.73 <X.73>`, :ref:`X.75 <X.75>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.79 <X.79>`, :ref:`X.80 <X.80>`, :ref:`X.81 <X.81>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.92 <X.92>`, :ref:`X.93 <X.93>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.97 <X.97>`, :ref:`X.98 <X.98>`, :ref:`X.99 <X.99>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.103 <X.103>`, :ref:`X.104 <X.104>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`X.112 <X.112>`, :ref:`X.113 <X.113>`, :ref:`X.114 <X.114>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition VII.16 <VII.16.commentary>`.

.. toctree::
   :hidden:

   commentary
