:order: 6
:number: 538
:type: prop
:tags: line
:dependencies: I.28, I.4, I.8, XI.2, XI.5, XI.def.3




.. picture:: XI.6.graphic.inverted.png

.. _XI.6:

XI.6
====

   If two straight lines be at right angles to the same plane, the straight lines will be parallel.

For let the two straight lines AB, CD be at right angles to the plane of reference; I say that AB is parallel to CD.

For let them meet the plane of reference at the points B, D, let the straight line BD be joined, let DE be drawn, in the plane of reference, at right angles to BD, let DE be made equal to AB, and let BE, AE, AD be joined.

Now, since AB is at right angles to the plane of reference, it will also make right angles with all the straight lines which meet it and are in the plane of reference. [:ref:`XI.def.3 <XI.def.3>`]

But each of the straight lines BD, BE is in the plane of reference and meets AB; therefore each of the angles ABD, ABE is right.

For the same reason each of the angles CDB, CDE is also right.

And, since AB is equal to DE, and BD is common, the two sides AB, BD are equal to the two sides ED, DB; and they include right angles; therefore the base AD is equal to the base BE. [:ref:`I.4 <I.4>`]

And, since AB is equal to DE, while AD is also equal to BE, the two sides AB, BE are equal to the two sides ED, DA; and AE is their common base; therefore the angle ABE is equal to the angle EDA. [:ref:`I.8 <I.8>`]

But the angle ABE is right; therefore the angle EDA is also right; therefore ED is at right angles to DA.

But it is also at right angles to each of the straight lines BD, DC; therefore ED is set up at right angles to the three straight lines BD, DA, DC at their point of meeting; therefore the three straight lines BD, DA, DC are in one plane. [:ref:`XI.5 <XI.5>`]

But, in whatever plane DB, DA are, in that plane is AB also, for every triangle is in one plane; [:ref:`XI.2 <XI.2>`] therefore the straight lines AB, BD, DC are in one plane.

And each of the angles ABD, BDC is right; therefore AB is parallel to CD. [:ref:`I.28 <I.28>`]

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
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
     "XI.1" [fillcolor="#222244", URL="/heath/XI/1/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
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
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "XI.4" [fillcolor="#222244", URL="/heath/XI/4/", target="_top"];
     "XI.2" [fillcolor="#222244", URL="/heath/XI/2/", target="_top"];
     "XI.6" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/6/", target="_top"];
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "XI.4" -> "XI.def.3";
     "XI.5" -> "XI.def.3";
     "XI.6" -> "XI.def.3";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "XI.4" -> "I.15";
     "XI.6" -> "XI.5";
     "XI.6" -> "I.28";
     "I.15" -> "I.13";
     "I.28" -> "I.13";
     "I.28" -> "I.27";
     "I.3" -> "I.2";
     "XI.5" -> "XI.3";
     "XI.2" -> "XI.1";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
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
     "XI.6" -> "XI.2";
   }



Required for
------------

:ref:`XI.10`, :ref:`XI.15`, :ref:`XI.24`, :ref:`XI.25`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.38`, :ref:`XI.39`, :ref:`XI.9`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`