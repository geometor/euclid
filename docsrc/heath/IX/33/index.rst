:order: 33
:number: 370
:type: prop
:dependencies: VII.def.8, VII.def.9




.. picture:: IX.33.graphic.inverted.png

.. _IX.33:

IX.33
=====

   If a number have its half odd, it is even-times odd only.

For let the number A have its half odd; I say that A is even-times odd only.

Now that it is even-times odd is manifest; for the half of it, being odd, measures it an even number of times. [:ref:`VII.def.9 <VII.def.9>`]

I say next that it is also even-times odd only.

For, if A is even-times even also, it will be measured by an even number according to an even number; [:ref:`VII.def.8 <VII.def.8>`] so that the half of it will also be measured by an even number though it is odd: which is absurd.

Therefore A is even-times odd only. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.def.9" [fillcolor="#224422", URL="/heath/VII/def.9/", target="_top"];
     "VII.def.8" [fillcolor="#224422", URL="/heath/VII/def.8/", target="_top"];
     "IX.33" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/33/", target="_top"];
     "IX.33" -> "VII.def.9";
     "IX.33" -> "VII.def.8";
   }
