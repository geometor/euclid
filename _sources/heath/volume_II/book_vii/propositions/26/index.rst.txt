:canonical_id: VII.26
:volume: II
:book: VII
:proposition: 26
:type: proposition
:title: Proposition VII.26
:folios: 0333
:pages: 327
:dependencies: VII.24

.. _VII.26:

.. folio:: 0333
   :page: 327

PROPOSITION 26.
===============

.. enunciation::

   If two numbers be prime to two numbers, both to each, their products also will be prime to one another.

For let the two numbers :g:`A <0333.g1:A>`, :g:`B <0333.g1:B>` be prime to the two numbers :g:`C <0333.g1:C>`, :g:`D <0333.g1:D>` ; both to each, and let :g:`A <0333.g1:A>` by multiplying :g:`B <0333.g1:B>` make :g:`E <0333.g1:E>`, and let :g:`C <0333.g1:C>` by multiplying :g:`D <0333.g1:D>` make :g:`F <0333.g1:F>`;

I say that :g:`E <0333.g1:E>`, :g:`F <0333.g1:F>` are prime to one another.

.. picture:: 0333.g1.svg
   :alt: Book VII, Proposition 26

.. subclause::

   For, since each of the numbers :g:`A <0333.g1:A>`, :g:`B <0333.g1:B>` is prime to :g:`C <0333.g1:C>`,

.. assertion:: [VII. 24] <VII.24>

   therefore the product of :g:`A <0333.g1:A>`, :g:`B <0333.g1:B>` will also be prime to :g:`C <0333.g1:C>`.

.. subclause::

   But the product of :g:`A <0333.g1:A>`, :g:`B <0333.g1:B>` is :g:`E <0333.g1:E>` ;

.. assertion::

   therefore :g:`E <0333.g1:E>`, :g:`C <0333.g1:C>` are prime to one another.

.. subclause::

   For the same reason

.. assertion::

   :g:`E <0333.g1:E>`, :g:`D <0333.g1:D>` are also prime to one another.

.. assertion::

   Therefore each of the numbers :g:`C <0333.g1:C>`, :g:`D <0333.g1:D>` is prime to :g:`E <0333.g1:E>`.

.. assertion:: [VII. 24] <VII.24>

   Therefore the product of :g:`C <0333.g1:C>`, :g:`D <0333.g1:D>` will also be prime to :g:`E <0333.g1:E>`.

.. subclause::

   But the product of :g:`C <0333.g1:C>`, :g:`D <0333.g1:D>` is :g:`F <0333.g1:F>`.

.. assertion::

   Therefore :g:`E <0333.g1:E>`, :g:`F <0333.g1:F>` are prime to one another.

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
     "V.def.4" [label="V.def.4", fillcolor="#224422", tooltip="V.def.4: Magnitudes are said to have a ratio to one another which are capable, when multiplied, of exceeding one another.", URL="../../../book_v/definitions/index.html#v-def-4", target="_top"];
     "V.def.5" [label="V.def.5", fillcolor="#224422", tooltip="V.def.5: Magnitudes are said to be in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any…", URL="../../../book_v/definitions/index.html#v-def-5", target="_top"];
     "V.def.7" [label="V.def.7", fillcolor="#224422", tooltip="V.def.7: When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then…", URL="../../../book_v/definitions/index.html#v-def-7", target="_top"];
     "V.1" [label="V.1", fillcolor="#222244", tooltip="V.1: If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one…", URL="../../../book_v/propositions/01/index.html", target="_top"];
     "V.7" [label="V.7", fillcolor="#222244", tooltip="V.7: Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", URL="../../../book_v/propositions/07/index.html", target="_top"];
     "V.8" [label="V.8", fillcolor="#222244", tooltip="V.8: Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", URL="../../../book_v/propositions/08/index.html", target="_top"];
     "V.9" [label="V.9", fillcolor="#222244", tooltip="V.9: Magnitudes which have the same ratio to the same are equal to one another ; and magnitudes to which the same has the same ratio are equal.", URL="../../../book_v/propositions/09/index.html", target="_top"];
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../definitions/index.html#vii-def-12", target="_top"];
     "VII.def.15" [label="VII.def.15", fillcolor="#224422", tooltip="VII.def.15: A number is said to multiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", URL="../../definitions/index.html#vii-def-15", target="_top"];
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../definitions/index.html#vii-def-20", target="_top"];
     "VII.1" [label="VII.1", fillcolor="#222244", tooltip="VII.1: Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit…", URL="../01/index.html", target="_top"];
     "VII.2" [label="VII.2", fillcolor="#222244", tooltip="VII.2: Given two numbers not prime to one another, to find their greatest common measure.", URL="../02/index.html", target="_top"];
     "VII.4" [label="VII.4", fillcolor="#222244", tooltip="VII.4: Any number is either a part or parts of any number, the less of the greater.", URL="../04/index.html", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", tooltip="VII.6: If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", URL="../06/index.html", target="_top"];
     "VII.9" [label="VII.9", fillcolor="#222244", tooltip="VII.9: If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts…", URL="../09/index.html", target="_top"];
     "VII.10" [label="VII.10", fillcolor="#222244", tooltip="VII.10: If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part…", URL="../10/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", tooltip="VII.12: If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", URL="../12/index.html", target="_top"];
     "VII.13" [label="VII.13", fillcolor="#222244", tooltip="VII.13: If four numbers be proportional, they will also be proportional alternately.", URL="../13/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", tooltip="VII.15: If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of…", URL="../15/index.html", target="_top"];
     "VII.16" [label="VII.16", fillcolor="#222244", tooltip="VII.16: If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.", URL="../16/index.html", target="_top"];
     "VII.17" [label="VII.17", fillcolor="#222244", tooltip="VII.17: If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", URL="../17/index.html", target="_top"];
     "VII.18" [label="VII.18", fillcolor="#222244", tooltip="VII.18: If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", URL="../18/index.html", target="_top"];
     "VII.19" [label="VII.19", fillcolor="#222244", tooltip="VII.19: If four numbers be proportional, the number produced from the first and fourth will be equal to the number produced from the second and third; and, if the number produced from the…", URL="../19/index.html", target="_top"];
     "VII.20" [label="VII.20", fillcolor="#222244", tooltip="VII.20: The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", URL="../20/index.html", target="_top"];
     "VII.21" [label="VII.21", fillcolor="#222244", tooltip="VII.21: Numbers prime to one another are the least of those which have the same ratio with them.", URL="../21/index.html", target="_top"];
     "VII.23" [label="VII.23", fillcolor="#222244", tooltip="VII.23: If two numbers be prime to one another, the number which measures the one of them will be prime to the remaining number.", URL="../23/index.html", target="_top"];
     "VII.24" [label="VII.24", fillcolor="#222244", tooltip="VII.24: If two numbers be prime to any number, their product also will be prime to the same.", URL="../24/index.html", target="_top"];
     "VII.26" [label="VII.26", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.26: If two numbers be prime to two numbers, both to each, their products also will be prime to one another.", URL="index.html", target="_top"];
     "V.8" -> "V.def.4";
     "V.7" -> "V.def.5";
     "V.8" -> "V.def.7";
     "V.8" -> "V.1";
     "VII.19" -> "V.7";
     "V.9" -> "V.8";
     "VII.19" -> "V.9";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "VII.24" -> "VII.def.15";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
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
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VII.16" -> "VII.15";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.19" -> "VII.18";
     "VII.24" -> "VII.19";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VII.24" -> "VII.21";
     "VII.24" -> "VII.23";
     "VII.26" -> "VII.24";
   }

Required for
------------

:ref:`VII.27 <VII.27>`, :ref:`VIII.2 <VIII.2>`, :ref:`VIII.3 <VIII.3>`, :ref:`VIII.6 <VIII.6>`, :ref:`VIII.7 <VIII.7>`, :ref:`VIII.8 <VIII.8>`, :ref:`VIII.9 <VIII.9>`, :ref:`VIII.14 <VIII.14>`, :ref:`VIII.15 <VIII.15>`, :ref:`VIII.16 <VIII.16>`, :ref:`VIII.17 <VIII.17>`, :ref:`VIII.21 <VIII.21>`, :ref:`VIII.23 <VIII.23>`, :ref:`VIII.24 <VIII.24>`, :ref:`VIII.25 <VIII.25>`, :ref:`VIII.26 <VIII.26>`, :ref:`VIII.27 <VIII.27>`, :ref:`IX.1 <IX.1>`, :ref:`IX.2 <IX.2>`, :ref:`IX.3 <IX.3>`, :ref:`IX.4 <IX.4>`, :ref:`IX.5 <IX.5>`, :ref:`IX.6 <IX.6>`, :ref:`IX.8 <IX.8>`, :ref:`IX.9 <IX.9>`, :ref:`IX.10 <IX.10>`, :ref:`IX.12 <IX.12>`, :ref:`IX.13 <IX.13>`, :ref:`IX.15 <IX.15>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`, :ref:`X.9 <X.9>`, :ref:`X.10 <X.10>`, :ref:`X.29 <X.29>`, :ref:`X.30 <X.30>`, :ref:`X.31 <X.31>`, :ref:`X.32 <X.32>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.48 <X.48>`, :ref:`X.49 <X.49>`, :ref:`X.50 <X.50>`, :ref:`X.51 <X.51>`, :ref:`X.52 <X.52>`, :ref:`X.53 <X.53>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition VII.26 <VII.26.commentary>`.

.. toctree::
   :hidden:

   commentary
