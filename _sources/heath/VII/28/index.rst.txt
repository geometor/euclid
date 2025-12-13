:order: 28
:number: 299
:type: prop
:dependencies: VII.def.12




.. picture:: VII.28.graphic.inverted.png

.. _VII.28:

VII.28
======

   If two numbers be prime to one another, the sum will also be prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers will also be prime to one another.

For let two numbers AB, BC prime to one another be added; I say that the sum AC is also prime to each of the numbers AB, BC.

For, if CA, AB are not prime to one another, some number will measure CA, AB.

Let a number measure them, and let it be D.

Since then D measures CA, AB, therefore it will also measure the remainder BC.

But it also measures BA; therefore D measures AB, BC which are prime to one another: which is impossible. [:ref:`VII.def.12 <VII.def.12>`]

Therefore no number will measure the numbers CA, AB; therefore CA, AB are prime to one another.

For the same reason AC, CB are also prime to one another.

Therefore CA is prime to each of the numbers AB, BC.

Again, let CA, AB be prime to one another; I say that AB, BC are also prime to one another.

For, if AB, BC are not prime to one another, some number will measure AB, BC.

Let a number measure them, and let it be D.

Now, since D measures each of the numbers AB, BC, it will also measure the whole CA.

But it also measures AB; therefore D measures CA, AB which are prime to one another: which is impossible. [:ref:`VII.def.12 <VII.def.12>`]

Therefore no number will measure the numbers AB, BC.

Therefore AB, BC are prime to one another. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.28" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/28/", target="_top"];
     "VII.28" -> "VII.def.12";
   }



Required for
------------

:ref:`IX.15`