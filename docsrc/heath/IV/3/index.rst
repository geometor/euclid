:order: 3
:number: 155
:type: prop
:tags: circle, triangle
:dependencies: I.13, I.23, I.32, III.1, III.16.p.1, III.18




.. picture:: IV.3.graphic.inverted.png

.. _IV.3:

IV.3
====

   About a given circle to circumscribe a triangle equiangular with a given triangle.

Let ``ABC`` be the given circle, and ``DEF`` the given triangle; thus it is required to circumscribe about the circle ``ABC`` a triangle equiangular with the triangle ``DEF``.

Let ``EF`` be produced in both directions to the points ``G``, ``H``, let the centre ``K`` of the circle ``ABC`` be taken [:ref:`III.1 <III.1>`], and let the straight line ``KB`` be drawn across at random; on the straight line ``KB``, and at the point ``K`` on it, let the angle ``BKA`` be constructed equal to the angle ``DEG``, and the angle ``BKC`` equal to the angle ``DFH``; [:ref:`I.23 <I.23>`] and through the points ``A``, ``B``, ``C`` let ``LAM``, ``MBN``, ``NCL`` be drawn touching the circle ``ABC``. [:ref:`III.16.p.1 <III.16.p.1>`]

Now, since ``LM``, ``MN``, ``NL`` touch the circle ``ABC`` at the points ``A``, ``B``, ``C``, and ``KA``, ``KB``, ``KC`` have been joined from the centre ``K`` to the points ``A``, ``B``, ``C``, therefore the angles at the points ``A``, ``B``, ``C`` are right. [:ref:`III.18 <III.18>`]

And, since the four angles of the quadrilateral ``AMBK`` are equal to four right angles, inasmuch as ``AMBK`` is in fact divisible into two triangles,


.. container:: center

   and the angles ``KAM``, ``KBM`` are right,


therefore the remaining angles ``AKB``, ``AMB`` are equal to two right angles.

But the angles ``DEG``, ``DEF`` are also equal to two right angles; [:ref:`I.13 <I.13>`] therefore the angles ``AKB``, ``AMB`` are equal to the angles ``DEG``, ``DEF``, of which the angle ``AKB`` is equal to the angle ``DEG``;


.. container:: center

   therefore the angle ``AMB`` which remains is equal to the angle ``DEF`` which remains.


Similarly it can be proved that the angle ``LNB`` is also equal to the angle ``DFE``;


.. container:: center

   therefore the remaining angle ``MLN`` is equal to the angle ``EDF``. [:ref:`I.32 <I.32>`]


Therefore the triangle ``LMN`` is equiangular with the triangle ``DEF``; and it has been circumscribed about the circle ``ABC``.

Therefore about a given circle there has been circumscribed a triangle equiangular with the given triangle. Q. E. F.
at random, literally as it may chance,
ὡς ἕτυχεν. The same expression is used in :ref:`III.1 <III.1>` and commonly.
is in fact divisible, καὶ διαιρεῖται, literally is actually divided.


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
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "III.18" [fillcolor="#222244", URL="/heath/III/18/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
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
     "IV.3" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/3/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "III.1" [fillcolor="#222244", URL="/heath/III/1/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "III.16.p.1" [fillcolor="#333333"];
     "I.32" -> "I.31";
     "IV.3" -> "I.32";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "III.18" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "IV.3" -> "III.18";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "IV.3" -> "I.13";
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "I.29" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "IV.3" -> "I.23";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.1" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.32" -> "I.29";
     "IV.3" -> "III.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.18" -> "I.17";
     "IV.3" -> "III.16.p.1";
   }
