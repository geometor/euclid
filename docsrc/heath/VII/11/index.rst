:order: 11
:number: 282
:type: prop
:dependencies: VII.7, VII.8, VII.def.20




.. picture:: VII.11.graphic.inverted.png

.. _VII.11:

VII.11
======

   If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

As the whole AB is to the whole CD, so let AE subtracted be to CF subtracted; I say that the remainder EB is also to the remainder FD as the whole AB to the whole CD.

Since, as AB is to CD, so is AE to CF, whatever part or parts AB is of CD, the same part or the same parts is AE of CF also; [:ref:`VII.def.20 <VII.def.20>`]

Therefore also the remainder EB is the same part or parts of FD that AB is of CD. [:ref:`VII.7 <VII.7>` :ref:`VII.8 <VII.8>`]

Therefore, as EB is to FD, so is AB to CD. [:ref:`VII.def.20 <VII.def.20>`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.11" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/11/", target="_top"];
     "VII.7" [fillcolor="#222244", URL="/heath/VII/7/", target="_top"];
     "VII.8" [fillcolor="#222244", URL="/heath/VII/8/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.11" -> "VII.def.20";
     "VII.8" -> "VII.7";
     "VII.11" -> "VII.7";
     "VII.11" -> "VII.8";
     "VII.7" -> "VII.5";
   }



Required for
------------

:ref:`IX.35`, :ref:`IX.36`