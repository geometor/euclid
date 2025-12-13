:order: 16
:number: 353
:type: prop
:dependencies: VII.20, VII.21




.. picture:: IX.16.graphic.inverted.png

.. _IX.16:

IX.16
=====

   If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

For let the two numbers A, B be prime to one another; I say that B is not to any other number as A is to B.

For, if possible, as A is to B, so let B be to C.

Now A, B are prime, primes are also least, [:ref:`VII.21 <VII.21>`] and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent; [:ref:`VII.20 <VII.20>`] therefore A measures B as antecedent antecedent.

But it also measures itself; therefore A measures A, B which are prime to one another: which is absurd.

Therefore B will not be to C, as A is to B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.21" [fillcolor="#222244", URL="/heath/VII/21/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "IX.16" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/16/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "VII.20" -> "VII.13";
     "VII.13" -> "VII.10";
     "VII.21" -> "VII.20";
     "IX.16" -> "VII.20";
     "VII.2" -> "VII.1";
     "VII.20" -> "VII.4";
     "VII.4" -> "VII.2";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "IX.16" -> "VII.21";
     "VII.10" -> "VII.9";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.21" -> "VII.16";
     "VII.16" -> "VII.15";
   }



Required for
------------

:ref:`IX.18`