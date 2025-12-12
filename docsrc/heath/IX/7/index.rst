:order: 7
:number: 344
:type: prop
:dependencies: VII.def.13, VII.def.15




.. picture:: IX.7.graphic.inverted.png

.. _IX.7:

IX.7
====

   If a composite number by multiplying any number make some number, the product will be solid.

For let the composite number A by multiplying any number B make C; I say that C is solid.

For, since A is composite, it will be measured by some number. [:ref:`VII.def.13 <VII.def.13>`]

Let it be measured by D; and, as many times as D measures A, so many units let there be in E.

Since then D measures A according to the units in E, therefore E by multiplying D has made A. [:ref:`VII.def.15 <VII.def.15>`]

And, since A by multiplying B has made C, and A is the product of D, E, therefore the product of D, E by multiplying B has made C.

Therefore C is solid, and D, E, B are its sides. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.def.13" [fillcolor="#224422", URL="/heath/VII/def.13/", target="_top"];
     "IX.7" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/7/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "IX.7" -> "VII.def.13";
     "IX.7" -> "VII.def.15";
   }
