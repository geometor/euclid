:order: 5
:number: 157
:type: prop
:tags: circle, triangle
:dependencies: I.10, I.4, III.31




.. picture:: IV.5.graphic.inverted.png

.. _IV.5:

IV.5
====

   About a given triangle to circumscribe a circle.

Let ``ABC`` be the given triangle; thus it is required to circumscribe a circle about the given triangle ``ABC``.

Let the straight lines ``AB``, ``AC`` be bisected at the points ``D``, ``E`` [:ref:`I.10 <I.10>`], and from the points ``D``, ``E`` let ``DF``, ``EF`` be drawn at right angles to ``AB``, ``AC``; they will then meet within the triangle ``ABC``, or on the straight line ``BC``, or outside ``BC``.

First let them meet within at ``F``, and let ``FB``, ``FC``, ``FA`` be joined.

Then, since ``AD`` is equal to ``DB``, and ``DF`` is common and at right angles, therefore the base ``AF`` is equal to the base ``FB``. [:ref:`I.4 <I.4>`]

Similarly we can prove that


.. container:: center

   ``CF`` is also equal to ``AF``;


so that ``FB`` is also equal to ``FC``;


.. container:: center

   therefore the three straight lines ``FA``, ``FB``, ``FC`` are equal to one another.


Therefore the circle described with centre ``F`` and distance one of the straight lines ``FA``, ``FB``, ``FC`` will pass also through the remaining points, and the circle will have been circumscribed about the triangle ``ABC``.

Let it be circumscribed, as ``ABC``.

Next, let ``DF``, ``EF`` meet on the straight line ``BC`` at ``F``, as is the case in the second figure; and let ``AF`` be joined.

Then, similarly, we shall prove that the point ``F`` is the centre of the circle circumscribed about the triangle ``ABC``.

Again, let ``DF``, ``EF`` meet outside the triangle ``ABC`` at ``F``, as is the case in the third figure, and let ``AF``, ``BF``, ``CF`` be joined.

Then again, since ``AD`` is equal to ``DB``, and ``DF`` is common and at right angles, therefore the base ``AF`` is equal to the base ``BF``. [:ref:`I.4 <I.4>`]

Similarly we can prove that


.. container:: center

   ``CF`` is also equal to ``AF``;


so that ``BF`` is also equal to ``FC``; therefore the circle described with centre ``F`` and distance one of the straight lines ``FA``, ``FB``, ``FC`` will pass also through the remaining points, and will have been circumscribed about the triangle ``ABC``.

Therefore about the given triangle a circle has been circumscribed. Q. E. F.

And it is manifest that, when the centre of the circle falls within the triangle, the angle ``BAC``, being in a segment greater than the semicircle, is less than a right angle; when the centre falls on the straight line ``BC``, the angle ``BAC``, being in a semicircle, is right; and when the centre of the circle falls outside the triangle, the angle ``BAC``, being in a segment less than the semicircle, is greater than a right angle. [:ref:`III.31 <III.31>`]


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
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
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
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "IV.5" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/5/", target="_top"];
     "III.22" [fillcolor="#222244", URL="/heath/III/22/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "III.21" [fillcolor="#222244", URL="/heath/III/21/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "III.31" [fillcolor="#222244", URL="/heath/III/31/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.20" [fillcolor="#222244", URL="/heath/III/20/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "I.32" -> "I.31";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
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
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "IV.5" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "I.16" -> "I.10";
     "IV.5" -> "I.10";
     "III.31" -> "III.22";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.17" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "III.22" -> "III.21";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.32" -> "I.29";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "IV.5" -> "III.31";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.21" -> "III.20";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.31" -> "I.17";
   }



Required for
------------

:ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`