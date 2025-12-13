:order: 21
:number: 553
:type: prop
:dependencies: I.32, XI.20




.. picture:: XI.21.graphic.inverted.png

.. _XI.21:

XI.21
=====

   Any solid angle is contained by plane angles less than four right angles.

Let the angle at A be a solid angle contained by the plane angles BAC, CAD, DAB; I say that the angles BAC, CAD, DAB are less than four right angles.

For let points B, C, D be taken at random on the straight lines AB, AC, AD respectively, and let BC, CD, DB be joined.

Now, since the solid angle at B is contained by the three plane angles CBA, ABD, CBD, any two are greater than the remaining one; [:ref:`XI.20 <XI.20>`] therefore the angles CBA, ABD are greater than the angle CBD.

For the same reason the angles BCA, ACD are also greater than the angle BCD, and the angles CDA, ADB are greater than the angle CDB; therefore the six angles CBA, ABD, BCA, ACD, CDA, ADB are greater than the three angles CBD, BCD, CDB.

But the three angles CBD, BDC, BCD are equal to two right angles; [:ref:`I.32 <I.32>`] therefore the six angles CBA, ABD, BCA, ACD, CDA, ADB are greater than two right angles.

And, since the three angles of each of the triangles ABC, ACD, ADB are equal to two right angles, therefore the nine angles of the three triangles, the angles CBA, ACB, BAC, ACD, CDA, CAD, ADB, DBA, BAD are equal to six right angles; and of them the six angles ABC, BCA, ACD, CDA, ADB, DBA are greater than two right angles; therefore the remaining three angles BAC, CAD, DAB containing the solid angle are less than four right angles.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "I.32" [fillcolor="#222244", URL="/heath/I/32/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.25" [fillcolor="#222244", URL="/heath/I/25/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.24" [fillcolor="#222244", URL="/heath/I/24/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "XI.21" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/21/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.5" [fillcolor="#442222", URL="/heath/I/cn.5/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "XI.20" [fillcolor="#222244", URL="/heath/XI/20/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.20" [fillcolor="#222244", URL="/heath/I/20/", target="_top"];
     "I.32" -> "I.31";
     "XI.21" -> "I.32";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "XI.20" -> "I.25";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.20" -> "I.19";
     "I.24" -> "I.19";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "I.25" -> "I.24";
     "I.29" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.15" -> "I.post.4";
     "I.24" -> "I.23";
     "I.31" -> "I.23";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.24" -> "I.4";
     "I.25" -> "I.4";
     "XI.20" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "I.24" -> "I.5";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.18" -> "I.16";
     "I.27" -> "I.16";
     "I.20" -> "I.cn.5";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.32" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "XI.21" -> "XI.20";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "XI.20" -> "I.20";
   }



Required for
------------

:ref:`XIII.18`