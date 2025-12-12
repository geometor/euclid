:order: 11
:number: 348
:type: prop
:dependencies: VII.15




.. picture:: IX.11.graphic.inverted.png

.. _IX.11:

IX.11
=====

   If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

Let there be as many numbers as we please, B, C, D, E, beginning from the unit A and in continued proportion; I say that B, the least of the numbers B, C, D, E, measures E according to some one of the numbers C, D.

For since, as the unit A is to B, so is D to E, therefore the unit A measures the number B the same number of times as D measures E; therefore, alternately, the unit A measures D the same number of times as B measures E. [:ref:`VII.15 <VII.15>`]

But the unit A measures D according to the units in it; therefore B also measures E according to the units in D; so that B the less measures E the greater according to some number of those which have place among the proportional numbers.—


.. _IX.11.p.1:


**IX.11.p.1**


And it is manifest that, whatever place the measuring number has, reckoned from the unit, the same place also has the number according to which it measures, reckoned from the number measured, in the direction of the number before it.—

PORISM.

And it is manifest that, whatever place the measuring number has, reckoned from the unit, the same place also has the number according to which it measures, reckoned from the number measured, in the direction of the number before it.—

Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "IX.11" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/11/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.12" -> "VII.def.20";
     "VII.15" -> "VII.12";
     "VII.12" -> "VII.6";
     "IX.11" -> "VII.15";
     "VII.6" -> "VII.5";
     "VII.12" -> "VII.5";
   }



Required for
------------

:ref:`IX.12`, :ref:`IX.13`, :ref:`IX.32`, :ref:`IX.36`