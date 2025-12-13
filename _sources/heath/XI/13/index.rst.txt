:order: 13
:number: 545
:type: prop
:tags: line
:dependencies: XI.3, XI.def.3




.. picture:: XI.13.graphic.inverted.png

.. _XI.13:

XI.13
=====

   From the same point two straight lines cannot be set up at right angles to the same plane on the same side.

For, if possible, from the same point A let the two straight lines AB, AC be set up at right angles to the plane of reference and on the same side, and let a plane be drawn through BA, AC; it will then make, as section through A in the plane of reference, a straight line. [:ref:`XI.3 <XI.3>`]

Let it make DAE; therefore the straight lines AB, AC, DAE are in one plane.

And, since CA is at right angles to the plane of reference, it will also make right angles with all the straight lines which meet it and are in the plane of reference. [:ref:`XI.def.3 <XI.def.3>`]

But DAE meets it and is in the plane of reference; therefore the angle CAE is right.

For the same reason the angle BAE is also right; therefore the angle CAE is equal to the angle BAE.

And they are in one plane: which is impossible.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "XI.3" [fillcolor="#222244", URL="/heath/XI/3/", target="_top"];
     "XI.def.3" [fillcolor="#224422", URL="/heath/XI/def.3/", target="_top"];
     "XI.13" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/13/", target="_top"];
     "XI.13" -> "XI.3";
     "XI.13" -> "XI.def.3";
   }



Required for
------------

:ref:`XI.19`