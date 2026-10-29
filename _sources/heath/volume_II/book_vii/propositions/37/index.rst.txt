:canonical_id: VII.37
:volume: II
:book: VII
:proposition: 37
:type: proposition
:title: Proposition VII.37
:folios: 0347, 0348
:pages: 341, 342
:dependencies: VII.15

.. _VII.37:

.. folio:: 0347
   :page: 341

PROPOSITION 37.
===============

.. enunciation::

   If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

For let the number :g:`A <0347.g1:A>` be measured by any number :g:`B <0347.g1:B>`;

I say that :g:`A <0347.g1:A>` has a part called by the same name as :g:`B <0347.g1:B>`.

.. picture:: 0347.g1.svg
   :alt: Proposition 37

For, as many times as :g:`B <0347.g1:B>` measures :g:`A <0347.g1:A>`, so many units let there be in :g:`C <0347.g1:C>`.

.. subclause::

   Since :g:`B <0347.g1:B>` measures :g:`A <0347.g1:A>` according to the units in :g:`C <0347.g1:C>`, and the unit :g:`D <0347.g1:D>` also measures the number :g:`C <0347.g1:C>` according to the units in it,

.. _folio-ii-0348:

.. folio:: 0348
   :page: 342

.. assertion::

   therefore the unit :g:`D <0347.g1:D>` measures the number :g:`C <0347.g1:C>` the same number of times as :g:`B <0347.g1:B>` measures :g:`A <0347.g1:A>`.

.. assertion::

   Therefore, alternately, the unit :g:`D <0347.g1:D>` measures the number :g:`B <0347.g1:B>` the same number of times as :g:`C <0347.g1:C>` measures :g:`A <0347.g1:A>`; :just:`[VII. 15] <VII.15>` therefore, whatever part the unit :g:`D <0347.g1:D>` is of the number :g:`B <0347.g1:B>`, the same part is :g:`C <0347.g1:C>` of :g:`A <0347.g1:A>` also.

.. subclause::

   But the unit :g:`D <0347.g1:D>` is a part of the number :g:`B <0347.g1:B>` called by the same name as it;

.. assertion::

   therefore :g:`C <0347.g1:C>` is also a part of :g:`A <0347.g1:A>` called by the same name as :g:`B <0347.g1:B>`, so that :g:`A <0347.g1:A>` has a part :g:`C <0347.g1:C>` which is called by the same name as :g:`B <0347.g1:B>`.

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
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../definitions/index.html#vii-def-20", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", tooltip="VII.6: If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", URL="../06/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", tooltip="VII.12: If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", URL="../12/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", tooltip="VII.15: If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of…", URL="../15/index.html", target="_top"];
     "VII.37" [label="VII.37", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.37: If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.", URL="index.html", target="_top"];
     "VII.12" -> "VII.def.20";
     "VII.6" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.6";
     "VII.15" -> "VII.12";
     "VII.37" -> "VII.15";
   }

Required for
------------

:ref:`VII.39 <VII.39>`

----

See :ref:`Commentary on Proposition VII.37 <VII.37.commentary>`.

.. toctree::
   :hidden:

   commentary
