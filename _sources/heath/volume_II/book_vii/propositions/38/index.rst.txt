:canonical_id: VII.38
:volume: II
:book: VII
:proposition: 38
:type: proposition
:title: Proposition VII.38
:folios: 0348, 0349
:folio: 0348
:page: 342
:pages: 342, 343
:dependencies: V.def.1, VII.def.2, VII.15

.. _VII.38:

.. folio:: 0348
   :page: 342

PROPOSITION 38.
===============

.. enunciation::

   If a :term:`number <number>` have any part whatever, it will be :term:`measured <part-aliquot>` by a number called by the same name as the part.

For let the number :g:`A <0348.g1:A>` have any part whatever, :g:`B <0348.g1:B>`, and let :g:`C <0348.g1:C>` be a number called by the same name as the part :g:`B <0348.g1:B>`;

I say that :g:`C <0348.g1:C>` measures :g:`A <0348.g1:A>`.

.. picture:: 0348.g1.svg
   :alt: Proposition 38

.. subclause::

   For, since :g:`B <0348.g1:B>` is a :term:`part of <part-aliquot>` :g:`A <0348.g1:A>` called by the same name as :g:`C <0348.g1:C>`, and the :term:`unit <unit>` :g:`D <0348.g1:D>` is also a part of :g:`C <0348.g1:C>` called by the same name as it,

.. assertion::

   therefore, whatever part the unit :g:`D <0348.g1:D>` is of the number :g:`C <0348.g1:C>`, the same part is :g:`B <0348.g1:B>` of :g:`A <0348.g1:A>` also;

.. assertion::

   therefore the unit :g:`D <0348.g1:D>` measures the number :g:`C <0348.g1:C>` the same number of times that :g:`B <0348.g1:B>` measures :g:`A <0348.g1:A>`.

.. _folio-ii-0349:

.. folio:: 0349
   :page: 343

.. assertion::

   Therefore, :term:`alternately <alternando>`, the unit :g:`D <0348.g1:D>` measures the number :g:`B <0348.g1:B>` the same number of times that :g:`C <0348.g1:C>` measures :g:`A <0348.g1:A>`. :just:`[VII. 15] <VII.15>`

.. assertion::

   Therefore :g:`C <0348.g1:C>` measures :g:`A <0348.g1:A>`.

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
     "V.def.1" [label="V.def.1", fillcolor="#224422", tooltip="V.def.1: A magnitude is a part of a magnitude, the less of the greater, when it measures the greater.", URL="../../../book_v/definitions/index.html#v-def-1", target="_top"];
     "V.def.2" [label="V.def.2", fillcolor="#224422", tooltip="V.def.2: The greater is a multiple of the less when it is measured by the less.", URL="../../../book_v/definitions/index.html#v-def-2", target="_top"];
     "V.def.11" [label="V.def.11", fillcolor="#224422", tooltip="V.def.11: The term corresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", URL="../../../book_v/definitions/index.html#v-def-11", target="_top"];
     "V.def.12" [label="V.def.12", fillcolor="#224422", tooltip="V.def.12: Alternate ratio means taking the antecedent in relation to the antecedent and the consequent in relation to the consequent.", URL="../../../book_v/definitions/index.html#v-def-12", target="_top"];
     "VII.def.1" [label="VII.def.1", fillcolor="#224422", tooltip="VII.def.1: An unit is that by virtue of which each of the things that exist is called one.", URL="../../definitions/index.html#vii-def-1", target="_top"];
     "VII.def.2" [label="VII.def.2", fillcolor="#224422", tooltip="VII.def.2: A number is a multitude composed of units.", URL="../../definitions/index.html#vii-def-2", target="_top"];
     "VII.def.3" [label="VII.def.3", fillcolor="#224422", tooltip="VII.def.3: A number is a part of a number, the less of the greater, when it measures the greater.", URL="../../definitions/index.html#vii-def-3", target="_top"];
     "VII.def.4" [label="VII.def.4", fillcolor="#224422", tooltip="VII.def.4: but parts when it does not measure it.", URL="../../definitions/index.html#vii-def-4", target="_top"];
     "VII.def.5" [label="VII.def.5", fillcolor="#224422", tooltip="VII.def.5: The greater number is a multiple of the less when it is measured by the less.", URL="../../definitions/index.html#vii-def-5", target="_top"];
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../definitions/index.html#vii-def-20", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", tooltip="VII.6: If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", URL="../06/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", tooltip="VII.12: If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", URL="../12/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", tooltip="VII.15: If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of…", URL="../15/index.html", target="_top"];
     "VII.38" [label="VII.38", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.38: If a number have any part whatever, it will be measured by a number called by the same name as the part.", URL="index.html", target="_top"];
     "V.def.2" -> "V.def.1";
     "VII.def.3" -> "V.def.1";
     "VII.def.4" -> "V.def.1";
     "VII.def.5" -> "V.def.1";
     "VII.15" -> "V.def.1";
     "VII.38" -> "V.def.1";
     "VII.5" -> "V.def.2";
     "V.def.12" -> "V.def.11";
     "VII.12" -> "V.def.11";
     "VII.15" -> "V.def.12";
     "VII.def.2" -> "VII.def.1";
     "VII.15" -> "VII.def.1";
     "VII.def.3" -> "VII.def.2";
     "VII.def.5" -> "VII.def.2";
     "VII.5" -> "VII.def.2";
     "VII.6" -> "VII.def.2";
     "VII.12" -> "VII.def.2";
     "VII.15" -> "VII.def.2";
     "VII.38" -> "VII.def.2";
     "VII.def.20" -> "VII.def.3";
     "VII.5" -> "VII.def.3";
     "VII.def.20" -> "VII.def.4";
     "VII.6" -> "VII.def.4";
     "VII.def.20" -> "VII.def.5";
     "VII.5" -> "VII.def.5";
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
