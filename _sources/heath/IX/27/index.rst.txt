:order: 27
:number: 364
:type: prop
:dependencies: IX.24, VII.def.7




.. picture:: IX.27.graphic.inverted.png

.. _IX.27:

IX.27
=====

   If from an odd number an even number be subtracted, the remainder will be odd.

For from the odd number AB let the even number BC be subtracted; I say that the remainder CA is odd.

Let the unit AD be subtracted; therefore DB is even. [:ref:`VII.def.7 <VII.def.7>`]

But BC is also even; therefore the remainder CD is even. [:ref:`IX.24 <IX.24>`]

Therefore CA is odd. [:ref:`VII.def.7 <VII.def.7>`] Q. E. D.


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
     "IX.27" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/27/", target="_top"];
     "VII.def.6" [fillcolor="#224422", URL="/heath/VII/def.6/", target="_top"];
     "IX.27" -> "IX.24";
     "IX.27" -> "VII.def.7";
     "IX.24" -> "VII.def.6";
   }
