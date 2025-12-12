:order: 19
:number: 551
:type: prop
:dependencies: XI.13, XI.def.4




.. picture:: XI.19.graphic.inverted.png

.. _XI.19:

XI.19
=====

   If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

For let the two planes AB, BC be at right angles to the plane of reference, and let BD be their common section; I say that BD is at right angles to the plane of reference.

For suppose it is not, and from the point D let DE be drawn in the plane AB at right angles to the straight line AD, and DF in the plane BC at right angles to CD.

Now, since the plane AB is at right angles to the plane of reference, and DE has been drawn in the plane AB at right angles to AD, their common section, therefore DE is at right angles to the plane of reference. [:ref:`XI.def.4 <XI.def.4>`]

Similarly we can prove that DF is also at right angles to the plane of reference.

Therefore from the same point D two straight lines have been set up at right angles to the plane of reference on the same side: which is impossible. [:ref:`XI.13 <XI.13>`]

Therefore no straight line except the common section DB of the planes AB, BC can be set up from the point D at right angles to the plane of reference.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "XI.19" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/19/", target="_top"];
     "XI.13" [fillcolor="#222244", URL="/heath/XI/13/", target="_top"];
     "XI.3" [fillcolor="#222244", URL="/heath/XI/3/", target="_top"];
     "XI.def.3" [fillcolor="#224422", URL="/heath/XI/def.3/", target="_top"];
     "XI.def.4" [fillcolor="#224422", URL="/heath/XI/def.4/", target="_top"];
     "XI.19" -> "XI.13";
     "XI.13" -> "XI.3";
     "XI.13" -> "XI.def.3";
     "XI.19" -> "XI.def.4";
   }
