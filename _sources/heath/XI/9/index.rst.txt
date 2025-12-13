:order: 9
:number: 541
:type: prop
:tags: line
:dependencies: XI.4, XI.6, XI.8




.. picture:: XI.9.graphic.inverted.png

.. _XI.9:

XI.9
====

   Straight lines which are parallel to the same straight line and are not in the same plane with it are also parallel to one another.

For let each of the straight lines AB, CD be parallel to EF, not being in the same plane with it; I say that AB is parallel to CD.

For let a point G be taken at random on EF, and from it let there be drawn GH, in the plane through EF, AB, at right angles to EF, and GK in the plane through FE, CD again at right angles to EF.

Now, since EF is at right angles to each of the straight lines GH, GK, therefore EF is also at right angles to the plane through GH, GK. [:ref:`XI.4 <XI.4>`]

And EF is parallel to AB; therefore AB is also at right angles to the plane through HG, GK. [:ref:`XI.8 <XI.8>`]

For the same reason CD is also at right angles to the plane through HG, GK; therefore each of the straight lines AB, CD is at right angles to the plane through HG, GK.

But if two straight lines be at right angles to the same plane, the straight lines are parallel; [:ref:`XI.6 <XI.6>`] therefore AB is parallel to CD.


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
     "XI.5" [fillcolor="#222244", URL="/heath/XI/5/", target="_top"];
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
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "XI.9" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/9/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "XI.4" [fillcolor="#222244", URL="/heath/XI/4/", target="_top"];
     "XI.2" [fillcolor="#222244", URL="/heath/XI/2/", target="_top"];
     "XI.6" [fillcolor="#222244", URL="/heath/XI/6/", target="_top"];
     "XI.8" -> "XI.7";
     "XI.9" -> "XI.8";
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
     "XI.5" -> "XI.def.3";
     "XI.6" -> "XI.def.3";
     "XI.8" -> "XI.def.3";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "XI.4" -> "I.15";
     "XI.6" -> "XI.5";
     "XI.6" -> "I.28";
     "I.15" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.28" -> "I.27";
     "I.3" -> "I.2";
     "XI.5" -> "XI.3";
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
     "XI.6" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XI.4" -> "I.4";
     "XI.6" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
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
     "XI.5" -> "XI.4";
     "XI.8" -> "XI.4";
     "XI.9" -> "XI.4";
     "XI.6" -> "XI.2";
     "XI.8" -> "XI.2";
     "XI.9" -> "XI.6";
   }



Required for
------------

:ref:`XI.10`, :ref:`XI.15`, :ref:`XI.24`, :ref:`XI.25`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.38`, :ref:`XI.39`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.17`, :ref:`XIII.18`