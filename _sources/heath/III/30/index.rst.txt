:order: 30
:number: 138
:type: prop
:categories: bisect
:dependencies: I.4, III.28




.. picture:: III.30.graphic.inverted.png

.. _III.30:

III.30
======

   To bisect a given circumference.

Let ``ADB`` be the given circumference; thus it is required to bisect the circumference ``ADB``.

Let ``AB`` be joined and bisected at ``C``; from the point ``C`` let ``CD`` be drawn at right angles to the straight line ``AB``,

and let ``AD``, ``DB`` be joined.

Then, since ``AC`` is equal to ``CB``, and ``CD`` is common,


.. container:: center

   the two sides ``AC``, ``CD`` are equal to the two sides ``BC``, ``CD``;


and the angle ``ACD`` is equal to the angle ``BCD``, for each is right;


.. container:: center

   therefore the base ``AD`` is equal to the base ``DB``. [:ref:`I.4 <I.4>`]


But equal straight lines cut off equal circumferences, the greater equal to the greater, and the less to the less; [:ref:`III.28 <III.28>`]


.. container:: center

   and each of the circumferences ``AD``, ``DB`` is less than a semicircle; therefore the circumference ``AD`` is equal to the circumference ``DB``.


Therefore the given circumference has been bisected at the point ``D``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "III.10" [fillcolor="#222244", URL="/heath/III/10/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "III.30" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/30/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "III.24" [fillcolor="#222244", URL="/heath/III/24/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.28" [fillcolor="#222244", URL="/heath/III/28/", target="_top"];
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.26" [fillcolor="#222244", URL="/heath/III/26/", target="_top"];
     "III.def.11" [fillcolor="#224422", URL="/heath/III/def.11/", target="_top"];
     "III.24" -> "III.10";
     "I.5" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "III.24" -> "I.8";
     "III.28" -> "I.8";
     "I.5" -> "I.4";
     "III.26" -> "I.4";
     "III.30" -> "I.4";
     "III.26" -> "III.24";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.30" -> "III.28";
     "III.10" -> "III.5";
     "III.10" -> "III.1.p.1";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "I.7" -> "I.5";
     "III.28" -> "III.26";
     "III.26" -> "III.def.11";
   }



Required for
------------

:ref:`IV.16`