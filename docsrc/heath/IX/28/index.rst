:order: 28
:number: 365
:type: prop
:dependencies: IX.21, VII.def.15




.. picture:: IX.28.graphic.inverted.png

.. _IX.28:

IX.28
=====

   If an odd number by multiplying an even number make some number, the product will be even.

For let the odd number A by multiplying the even number B make C; I say that C is even.

For, since A by multiplying B has made C, therefore C is made up of as many numbers equal to B as there are units in A. [:ref:`VII.def.15 <VII.def.15>`]

And B is even; therefore C is made up of even numbers.

But, if as many even numbers as we please be added together, the whole is even. [:ref:`IX.21 <IX.21>`]

Therefore C is even. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "IX.21" [fillcolor="#222244", URL="/heath/IX/21/", target="_top"];
     "IX.28" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/28/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "VII.def.6" [fillcolor="#224422", URL="/heath/VII/def.6/", target="_top"];
     "IX.28" -> "IX.21";
     "IX.28" -> "VII.def.15";
     "IX.21" -> "VII.def.6";
   }
