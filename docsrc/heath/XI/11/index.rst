:order: 11
:number: 543
:type: prop
:tags: line
:dependencies: I.11, I.12, I.31, XI.4, XI.8, XI.def.3




.. picture:: XI.11.graphic.inverted.png

.. _XI.11:

XI.11
=====

   From a given elevated point to draw a straight line perpendicular to a given plane.

Let A be the given elevated point, and the plane of reference the given plane; thus it is required to draw from the point A a straight line perpendicular to the plane of reference.

Let any straight line BC be drawn, at random, in the plane of reference, and let AD be drawn from the point A perpendicular to BC. [:ref:`I.12 <I.12>`]

If then AD is also perpendicular to the plane of reference, that which was enjoined will have been done.

But, if not, let DE be drawn from the point D at right angles to BC and in the plane of reference, [:ref:`I.11 <I.11>`] let AF be drawn from A perpendicular to DE, [:ref:`I.12 <I.12>`] and let GH be drawn through the point F parallel to BC. [:ref:`I.31 <I.31>`]

Now, since BC is at right angles to each of the straight lines DA, DE, therefore BC is also at right angles to the plane through ED, DA. [:ref:`XI.4 <XI.4>`]

And GH is parallel to it; but, if two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane; [:ref:`XI.8 <XI.8>`] therefore GH is also at right angles to the plane through ED, DA.

Therefore GH is also at right angles to all the straight lines which meet it and are in the plane through ED, DA. [:ref:`XI.def.3 <XI.def.3>`]

But AF meets it and is in the plane through ED, DA; therefore GH is at right angles to FA, so that FA is also at right angles to GH.

But AF is also at right angles to DE; therefore AF is at right angles to each of the straight lines GH, DE.

But, if a straight line be set up at right angles to two straight lines which cut one another, at the point of section, it will also be at right angles to the plane through them; [:ref:`XI.4 <XI.4>`] therefore FA is at right angles to the plane through ED, GH.

But the plane through ED, GH is the plane of reference; therefore AF is at right angles to the plane of reference.

Therefore from the given elevated point A the straight line AF has been drawn perpendicular to the plane of reference. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.12" [fillcolor="#222244", URL="/heath/I/12/", target="_top"];
     "XI.8" [fillcolor="#222244", URL="/heath/XI/8/", target="_top"];
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "XI.7" [fillcolor="#222244", URL="/heath/XI/7/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "XI.def.3" [fillcolor="#224422", URL="/heath/XI/def.3/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "XI.3" [fillcolor="#222244", URL="/heath/XI/3/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "XI.1" [fillcolor="#222244", URL="/heath/XI/1/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "XI.11" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/11/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "XI.4" [fillcolor="#222244", URL="/heath/XI/4/", target="_top"];
     "XI.2" [fillcolor="#222244", URL="/heath/XI/2/", target="_top"];
     "XI.11" -> "I.12";
     "XI.11" -> "XI.8";
     "XI.11" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "XI.8" -> "XI.7";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "XI.4" -> "XI.def.3";
     "XI.8" -> "XI.def.3";
     "XI.11" -> "XI.def.3";
     "I.11" -> "I.def.10";
     "I.12" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "XI.4" -> "I.15";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "XI.7" -> "XI.3";
     "I.29" -> "I.cn.2";
     "XI.2" -> "XI.1";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "XI.4" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.12" -> "I.8";
     "I.23" -> "I.8";
     "XI.4" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XI.4" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.12" -> "I.10";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.12" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "XI.11" -> "I.11";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "XI.8" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.12" -> "I.post.3";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "XI.8" -> "XI.4";
     "XI.11" -> "XI.4";
     "XI.8" -> "XI.2";
   }



Required for
------------

:ref:`XI.12`, :ref:`XI.15`, :ref:`XI.23`, :ref:`XI.26`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.18`