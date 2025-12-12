:order: 37
:number: 308
:type: prop
:dependencies: VII.15




.. picture:: VII.37.graphic.inverted.png

.. _VII.37:

VII.37
======

   If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

For let the number A be measured by any number B; I say that A has a part called by the same name as B.

For, as many times as B measures A, so many units let there be in C.

Since B measures A according to the units in C, and the unit D also measures the number C according to the units in it, therefore the unit D measures the number C the same number of times as B measures A.

Therefore, alternately, the unit D measures the number B the same number of times as C measures A; [:ref:`VII.15 <VII.15>`] therefore, whatever part the unit D is of the number B, the same part is C of A also.

But the unit D is a part of the number B called by the same name as it; therefore C is also a part of A called by the same name as B, so that A has a part C which is called by the same name as B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.37" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/37/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.12" -> "VII.def.20";
     "VII.15" -> "VII.12";
     "VII.12" -> "VII.6";
     "VII.37" -> "VII.15";
     "VII.6" -> "VII.5";
     "VII.12" -> "VII.5";
   }



Required for
------------

:ref:`VII.39`