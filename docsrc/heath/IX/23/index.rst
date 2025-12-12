:order: 23
:number: 360
:type: prop
:dependencies: IX.21, IX.22, VII.def.7




.. picture:: IX.23.graphic.inverted.png

.. _IX.23:

IX.23
=====

   If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.

For let as many odd numbers as we please, AB, BC, CD, the multitude of which is odd, be added together; I say that the whole AD is also odd.

Let the unit DE be subtracted from CD; therefore the remainder CE is even. [:ref:`VII.def.7 <VII.def.7>`]

But CA is also even; [:ref:`IX.22 <IX.22>`] therefore the whole AE is also even. [:ref:`IX.21 <IX.21>`]

And DE is an unit.

Therefore AD is odd. [:ref:`VII.def.7 <VII.def.7>`] Q. E. D.
3. Literally let there be as many numbers as we please, of which let the multitude be odd.
This form, natural in Greek, is awkward in English.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "IX.21" [fillcolor="#222244", URL="/heath/IX/21/", target="_top"];
     "VII.def.7" [fillcolor="#224422", URL="/heath/VII/def.7/", target="_top"];
     "IX.23" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/23/", target="_top"];
     "IX.22" [fillcolor="#222244", URL="/heath/IX/22/", target="_top"];
     "VII.def.6" [fillcolor="#224422", URL="/heath/VII/def.6/", target="_top"];
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.23" -> "IX.22";
     "IX.21" -> "VII.def.6";
   }



Required for
------------

:ref:`IX.29`, :ref:`IX.30`, :ref:`IX.31`