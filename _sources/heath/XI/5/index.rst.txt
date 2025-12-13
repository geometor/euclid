:order: 5
:number: 537
:type: prop
:tags: line
:dependencies: XI.3, XI.4, XI.def.3




.. picture:: XI.5.graphic.inverted.png

.. _XI.5:

XI.5
====

   If a straight line be set up at right angles to three straight lines which meet one another, at their common point of section, the three straight lines are in one plane.

For let a straight line AB be set up at right angles to the three straight lines BC, BD, BE, at their point of meeting at B; I say that BC, BD, BE are in one plane.

For suppose they are not, but, if possible, let BD, BE be in the plane of reference and BC in one more elevated; let the plane through AB, BC be produced; it will thus make, as common section in the plane of reference, a straight line. [:ref:`XI.3 <XI.3>`]

Let it make BF.

Therefore the three straight lines AB, BC, BF are in one plane, namely that drawn through AB, BC.

Now, since AB is at right angles to each of the straight lines BD, BE, therefore AB is also at right angles to the plane through BD, BE. [:ref:`XI.4 <XI.4>`]

But the plane through BD, BE is the plane of reference; therefore AB is at right angles to the plane of reference.

Thus AB will also make right angles with all the straight lines which meet it and are in the plane of reference. [:ref:`XI.def.3 <XI.def.3>`]

But BF which is in the plane of reference meets it; therefore the angle ABF is right.

But, by hypothesis, the angle ABC is also right; therefore the angle ABF is equal to the angle ABC.

And they are in one plane: which is impossible.

Therefore the straight line BC is not in a more elevated plane; therefore the three straight lines BC, BD, BE are in one plane.

Therefore, if a straight line be set up at right angles to three straight lines, at their point of meeting, the three straight lines are in one plane. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "XI.def.3" [fillcolor="#224422", URL="/heath/XI/def.3/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "XI.5" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/5/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "XI.3" [fillcolor="#222244", URL="/heath/XI/3/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "XI.4" [fillcolor="#222244", URL="/heath/XI/4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "XI.4" -> "XI.def.3";
     "XI.5" -> "XI.def.3";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "XI.4" -> "I.15";
     "I.13" -> "I.11";
     "I.26" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "XI.5" -> "XI.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "XI.5" -> "XI.4";
     "XI.4" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "XI.4" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XI.4" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`XI.10`, :ref:`XI.15`, :ref:`XI.24`, :ref:`XI.25`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.38`, :ref:`XI.39`, :ref:`XI.6`, :ref:`XI.9`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`