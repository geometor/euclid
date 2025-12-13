:order: 32
:number: 303
:type: prop
:dependencies: VII.31




.. picture:: VII.32.graphic.inverted.png

.. _VII.32:

VII.32
======

   Any number either is prime or is measured by some prime number.

Let A be a number; I say that A either is prime or is measured by some prime number.

If now A is prime, that which was enjoined will have been done.

But if it is composite, some prime number will measure it. [:ref:`VII.31 <VII.31>`]

Therefore any number either is prime or is measured by some prime number. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.32" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/32/", target="_top"];
     "VII.31" [fillcolor="#222244", URL="/heath/VII/31/", target="_top"];
     "VII.32" -> "VII.31";
   }
