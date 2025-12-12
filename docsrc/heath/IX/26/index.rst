:order: 26
:number: 363
:type: prop
:dependencies: IX.24, VII.def.7




.. picture:: IX.26.graphic.inverted.png

.. _IX.26:

IX.26
=====

   If from an odd number an odd number be subtracted, the remainder will be even.

For from the odd number AB let the odd number BC be subtracted; I say that the remainder CA is even.

For, since AB is odd, let the unit BD be subtracted; therefore the remainder AD is even. [:ref:`VII.def.7 <VII.def.7>`]

For the same reason CD is also even; [:ref:`VII.def.7 <VII.def.7>`] so that the remainder CA is also even. [:ref:`IX.24 <IX.24>`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "IX.24" [fillcolor="#222244", URL="/heath/IX/24/", target="_top"];
     "IX.26" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/26/", target="_top"];
     "VII.def.7" [fillcolor="#224422", URL="/heath/VII/def.7/", target="_top"];
     "VII.def.6" [fillcolor="#224422", URL="/heath/VII/def.6/", target="_top"];
     "IX.26" -> "IX.24";
     "IX.26" -> "VII.def.7";
     "IX.24" -> "VII.def.6";
   }



Required for
------------

:ref:`X.104`, :ref:`X.110`, :ref:`X.28`, :ref:`X.75`, :ref:`X.81`, :ref:`X.93`, :ref:`X.99`