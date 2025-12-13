:order: 31
:number: 368
:type: prop
:dependencies: IX.30




.. picture:: IX.31.graphic.inverted.png

.. _IX.31:

IX.31
=====

   If an odd number be prime to any number, it will also be prime to the double of it.

For let the odd number A be prime to any number B, and let C be double of B; I say that A is prime to C.

For, if they are not prime to one another, some number will measure them.

Let a number measure them, and let it be D.

Now A is odd; therefore D is also odd.

And since D which is odd measures C, and C is even, therefore [D] will measure the half of C also. [:ref:`IX.30 <IX.30>`]

But B is half of C; therefore D measures B.

But it also measures A; therefore D measures A, B which are prime to one another: which is impossible.

Therefore A cannot but be prime to C.

Therefore A, C are prime to one another. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "IX.21" [fillcolor="#222244", URL="/heath/IX/21/", target="_top"];
     "IX.30" [fillcolor="#222244", URL="/heath/IX/30/", target="_top"];
     "IX.31" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/31/", target="_top"];
     "VII.def.7" [fillcolor="#224422", URL="/heath/VII/def.7/", target="_top"];
     "IX.23" [fillcolor="#222244", URL="/heath/IX/23/", target="_top"];
     "IX.22" [fillcolor="#222244", URL="/heath/IX/22/", target="_top"];
     "VII.def.6" [fillcolor="#224422", URL="/heath/VII/def.6/", target="_top"];
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
     "IX.31" -> "IX.30";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.30" -> "IX.23";
     "IX.23" -> "IX.22";
     "IX.21" -> "VII.def.6";
   }
