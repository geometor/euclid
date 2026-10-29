:canonical_id: IX.11
:volume: II
:book: IX
:proposition: 11
:type: proposition
:title: Proposition IX.11
:folios: 0401, 0402
:pages: 395, 396
:dependencies: VII.15

.. _IX.11:

.. folio:: 0401
   :page: 395

PROPOSITION 11.
===============

.. enunciation::

   If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

.. _folio-ii-0402:

.. folio:: 0402
   :page: 396

Let there be as many numbers as we please, :g:`$B$ <0402.g1:B>`, :g:`$C$ <0402.g1:C>`, :g:`$D$ <0402.g1:D>`, :g:`$E$ <0402.g1:E>`, beginning from the unit :g:`$A$ <0402.g1:A>` and in continued proportion ;

I say that :g:`$B$ <0402.g1:B>`, the least of the numbers :g:`$B$ <0402.g1:B>`, :g:`$C$ <0402.g1:C>`, :g:`$D$ <0402.g1:D>`, :g:`$E$ <0402.g1:E>`, measures :g:`$E$ <0402.g1:E>` according to some one of the numbers :g:`$C$ <0402.g1:C>`, :g:`$D$ <0402.g1:D>`.

.. picture:: 0402.g1.svg
   :alt: Proposition 11 Diagram

.. subclause::

   For since, as the unit :g:`$A$ <0402.g1:A>` is to :g:`$B$ <0402.g1:B>`, so is :g:`$D$ <0402.g1:D>` to :g:`$E$ <0402.g1:E>`,

.. assertion::

   therefore the unit :g:`$A$ <0402.g1:A>` measures the number :g:`$B$ <0402.g1:B>` the same number of times as :g:`$D$ <0402.g1:D>` measures :g:`$E$ <0402.g1:E>`;

.. assertion::

   therefore, alternately, the unit :g:`$A$ <0402.g1:A>` measures :g:`$D$ <0402.g1:D>` the same number of times as :g:`$B$ <0402.g1:B>` measures :g:`$E$ <0402.g1:E>`. :just:`[VII. 15] <VII.15>`

.. subclause::

   But the unit :g:`$A$ <0402.g1:A>` measures :g:`$D$ <0402.g1:D>` according to the units in it;

.. assertion::

   therefore :g:`$B$ <0402.g1:B>` also measures :g:`$E$ <0402.g1:E>` according to the units in :g:`$D$ <0402.g1:D>`;

.. assertion::

   so that :g:`$B$ <0402.g1:B>` the less measures :g:`$E$ <0402.g1:E>` the greater according to some number of those which have place among the proportional numbers.—

.. assertion::

   PORISM. And it is manifest that, whatever place the measuring number has, reckoned from the unit, the same place also has the number according to which it measures, reckoned from the number measured, in the direction of the number before it.—

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
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../../book_vii/definitions/index.html#vii-def-20", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../../../book_vii/propositions/05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", tooltip="VII.6: If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", URL="../../../book_vii/propositions/06/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", tooltip="VII.12: If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", URL="../../../book_vii/propositions/12/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", tooltip="VII.15: If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of…", URL="../../../book_vii/propositions/15/index.html", target="_top"];
     "IX.11" [label="IX.11", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.11: If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the…", URL="index.html", target="_top"];
     "VII.12" -> "VII.def.20";
     "VII.6" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.6";
     "VII.15" -> "VII.12";
     "IX.11" -> "VII.15";
   }

Required for
------------

:ref:`IX.12 <IX.12>`, :ref:`IX.13 <IX.13>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`

----

See :ref:`Commentary on Proposition IX.11 <IX.11.commentary>`.

.. toctree::
   :hidden:

   commentary
