:order: 30
:number: 367
:type: prop
:dependencies: IX.23




.. picture:: IX.30.graphic.inverted.png

.. _IX.30:

IX.30
=====

   If an odd number measure an even number, it will also measure the half of it.

For let the odd number A measure the even number B; I say that it will also measure the half of it.

For, since A measures B, let it measure it according to C; I say that C is not odd.

For, if possible, let it be so.

Then, since A measures B according to C, therefore A by multiplying C has made B.

Therefore B is made up of odd numbers the multitude of which is odd.

Therefore B is odd: [:ref:`IX.23 <IX.23>`] which is absurd, for by hypothesis it is even.

Therefore C is not odd; therefore C is even.

Thus A measures B an even number of times.

For this reason then it also measures the half of it. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "IX.21" [fillcolor="#222244", URL="/heath/IX/21/", target="_top"];
     "IX.30" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/30/", target="_top"];
     "VII.def.7" [fillcolor="#224422", URL="/heath/VII/def.7/", target="_top"];
     "IX.23" [fillcolor="#222244", URL="/heath/IX/23/", target="_top"];
     "IX.22" [fillcolor="#222244", URL="/heath/IX/22/", target="_top"];
     "VII.def.6" [fillcolor="#224422", URL="/heath/VII/def.6/", target="_top"];
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.30" -> "IX.23";
     "IX.23" -> "IX.22";
     "IX.21" -> "VII.def.6";
   }



Required for
------------

:ref:`IX.31`