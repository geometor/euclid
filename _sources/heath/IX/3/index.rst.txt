:order: 3
:number: 340
:type: prop
:dependencies: VII.def.20, VIII.23, VIII.8




.. picture:: IX.3.graphic.inverted.png

.. _IX.3:

IX.3
====

   If a cube number by multiplying itself make some number, the product will be cube.

For let the cube number A by multiplying itself make B; I say that B is cube.

For let C, the side of A, be taken, and let C by multiplying itself make D.

It is then manifest that C by multiplying D has made A.

Now, since C by multiplying itself has made D, therefore C measures D according to the units in itself.

But further the unit also measures C according to the units in it; therefore, as the unit is to C, so is C to D. [:ref:`VII.def.20 <VII.def.20>`]

Again, since C by multiplying D has made A, therefore D measures A according to the units in C.

But the unit also measures C according to the units in it; therefore, as the unit is to C, so is D to A.

But, as the unit is to C, so is C to D; therefore also, as the unit is to C, so is C to D, and D to A.

Therefore between the unit and the number A two mean proportional numbers C, D have fallen in continued proportion.

Again, since A by multiplying itself has made B, therefore A measures B according to the units in itself.

But the unit also measures A according to the units in it; therefore, as the unit is to A, so is A to B. [:ref:`VII.def.20 <VII.def.20>`]

But between the unit and A two mean proportional numbers have fallen; therefore two mean proportional numbers will also fall between A, B. [:ref:`VIII.8 <VIII.8>`]

But, if two mean proportional numbers fall between two numbers, and the first be cube, the second will also be cube. [:ref:`VIII.23 <VIII.23>`]

And A is cube; therefore B is also cube. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.33" [fillcolor="#222244", URL="/heath/VII/33/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VIII.8" [fillcolor="#222244", URL="/heath/VIII/8/", target="_top"];
     "VIII.21" [fillcolor="#222244", URL="/heath/VIII/21/", target="_top"];
     "VII.26" [fillcolor="#222244", URL="/heath/VII/26/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "VIII.2.p.1" [fillcolor="#333333"];
     "VII.27" [fillcolor="#222244", URL="/heath/VII/27/", target="_top"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "VII.25" [fillcolor="#222244", URL="/heath/VII/25/", target="_top"];
     "IX.3" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/3/", target="_top"];
     "VIII.20" [fillcolor="#222244", URL="/heath/VIII/20/", target="_top"];
     "VII.21" [fillcolor="#222244", URL="/heath/VII/21/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "VII.24" [fillcolor="#222244", URL="/heath/VII/24/", target="_top"];
     "VII.22" [fillcolor="#222244", URL="/heath/VII/22/", target="_top"];
     "VIII.2" [fillcolor="#222244", URL="/heath/VIII/2/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VIII.23" [fillcolor="#222244", URL="/heath/VIII/23/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "VIII.3" [fillcolor="#222244", URL="/heath/VIII/3/", target="_top"];
     "VII.2.p.1" [fillcolor="#333333"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VII.23" [fillcolor="#222244", URL="/heath/VII/23/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.19" [fillcolor="#222244", URL="/heath/VII/19/", target="_top"];
     "VIII.1" [fillcolor="#222244", URL="/heath/VIII/1/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "VII.3" [fillcolor="#222244", URL="/heath/VII/3/", target="_top"];
     "VII.14" [fillcolor="#222244", URL="/heath/VII/14/", target="_top"];
     "VIII.3" -> "VII.33";
     "VIII.8" -> "VII.33";
     "VIII.20" -> "VII.33";
     "VIII.21" -> "VII.33";
     "V.7" -> "V.def.5";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "VIII.21" -> "VII.18";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VIII.8" -> "VII.def.20";
     "IX.3" -> "VII.def.20";
     "IX.3" -> "VIII.8";
     "VIII.23" -> "VIII.21";
     "VII.27" -> "VII.26";
     "VII.2" -> "VII.1";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VIII.20" -> "VII.13";
     "VIII.3" -> "VIII.2.p.1";
     "VIII.2" -> "VII.27";
     "VIII.3" -> "VII.27";
     "VII.20" -> "VII.4";
     "VII.27" -> "VII.25";
     "VIII.21" -> "VIII.20";
     "VII.24" -> "VII.21";
     "VII.33" -> "VII.21";
     "VIII.1" -> "VII.21";
     "VIII.8" -> "VII.21";
     "VIII.21" -> "VII.21";
     "VII.10" -> "VII.9";
     "VII.19" -> "V.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.19" -> "V.9";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VIII.20" -> "VII.17";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VIII.2" -> "VII.22";
     "VIII.3" -> "VII.22";
     "VIII.3" -> "VIII.2";
     "VIII.21" -> "VIII.2";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
     "VIII.8" -> "VII.20";
     "VIII.20" -> "VII.20";
     "VIII.21" -> "VII.20";
     "V.8" -> "V.def.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "IX.3" -> "VIII.23";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.33" -> "VII.def.15";
     "VIII.8" -> "VIII.3";
     "VIII.21" -> "VIII.3";
     "VII.3" -> "VII.2.p.1";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.16" -> "VII.15";
     "V.8" -> "V.1";
     "VII.13" -> "VII.10";
     "VII.24" -> "VII.23";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
     "VIII.2" -> "VIII.1";
     "V.9" -> "V.8";
     "VII.33" -> "VII.3";
     "VIII.1" -> "VII.14";
     "VIII.8" -> "VII.14";
     "VIII.21" -> "VII.14";
   }



Required for
------------

:ref:`IX.4`, :ref:`IX.5`, :ref:`IX.9`