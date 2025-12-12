:order: 25
:number: 362
:type: prop
:dependencies: IX.24, VII.def.7




.. picture:: IX.25.graphic.inverted.png

.. _IX.25:

IX.25
=====

   If from an even number an odd number be subtracted, the remainder will be odd.

For from the even number AB let the odd number BC be subtracted; I say that the remainder CA is odd.

For let the unit CD be subtracted from BC; therefore DB is even. [:ref:`VII.def.7 <VII.def.7>`]

But AB is also even; therefore the remainder AD is also even. [:ref:`IX.24 <IX.24>`]

And CD is an unit; therefore CA is odd. [:ref:`VII.def.7 <VII.def.7>`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "IX.24" [fillcolor="#222244", URL="/heath/IX/24/", target="_top"];
     "VII.def.7" [fillcolor="#224422", URL="/heath/VII/def.7/", target="_top"];
     "IX.25" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/25/", target="_top"];
     "VII.def.6" [fillcolor="#224422", URL="/heath/VII/def.6/", target="_top"];
     "IX.25" -> "IX.24";
     "IX.25" -> "VII.def.7";
     "IX.24" -> "VII.def.6";
   }
