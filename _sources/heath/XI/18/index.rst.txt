:order: 18
:number: 550
:type: prop
:tags: line
:dependencies: I.11, I.28, XI.8, XI.def.3, XI.def.4




.. picture:: XI.18.graphic.inverted.png

.. _XI.18:

XI.18
=====

   If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

For let any straight line AB be at right angles to the plane of reference; I say that all the planes through AB are also at right angles to the plane of reference.

For let the plane DE be drawn through AB, let CE be the common section of the plane DE and the plane of reference, let a point F be taken at random on CE, and from F let FG be drawn in the plane DE at right angles to CE. [:ref:`I.11 <I.11>`]

Now, since AB is at right angles to the plane of reference, AB is also at right angles to all the straight lines which meet it and are in the plane of reference; [:ref:`XI.def.3 <XI.def.3>`] so that it is also at right angles to CE; therefore the angle ABF is right.

But the angle GFB is also right; therefore AB is parallel to FG. [:ref:`I.28 <I.28>`]

But AB is at right angles to the plane of reference; therefore FG is also at right angles to the plane of reference. [:ref:`XI.8 <XI.8>`]

Now a plane is at right angles to a plane, when the straight lines drawn, in one of the planes, at right angles to the common section of the planes are at right angles to the remaining plane. [:ref:`XI.def.4 <XI.def.4>`]

And FG, drawn in one of the planes DE at right angles to CE, the common section of the planes, was proved to be at right angles to the plane of reference; therefore the plane DE is at right angles to the plane of reference.

Similarly also it can be proved that all the planes through AB are at right angles to the plane of reference.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "XI.7" [fillcolor="#222244", URL="/heath/XI/7/", target="_top"];
     "XI.8" [fillcolor="#222244", URL="/heath/XI/8/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "XI.def.3" [fillcolor="#224422", URL="/heath/XI/def.3/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.28" [fillcolor="#222244", URL="/heath/I/28/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "XI.3" [fillcolor="#222244", URL="/heath/XI/3/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "XI.1" [fillcolor="#222244", URL="/heath/XI/1/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "XI.def.4" [fillcolor="#224422", URL="/heath/XI/def.4/", target="_top"];
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
     "XI.18" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/18/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "XI.4" [fillcolor="#222244", URL="/heath/XI/4/", target="_top"];
     "XI.2" [fillcolor="#222244", URL="/heath/XI/2/", target="_top"];
     "XI.8" -> "XI.7";
     "XI.18" -> "XI.8";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "XI.4" -> "XI.def.3";
     "XI.8" -> "XI.def.3";
     "XI.18" -> "XI.def.3";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "XI.4" -> "I.15";
     "XI.18" -> "I.28";
     "I.15" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.28" -> "I.27";
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
     "XI.4" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "XI.4" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XI.4" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "XI.18" -> "XI.def.4";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "XI.18" -> "I.11";
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
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "XI.8" -> "XI.4";
     "XI.8" -> "XI.2";
   }



Required for
------------

:ref:`XII.17`, :ref:`XII.18`