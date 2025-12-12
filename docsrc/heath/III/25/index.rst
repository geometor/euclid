:order: 25
:number: 133
:type: prop
:categories: describe
:tags: circle
:dependencies: I.6, III.9




.. picture:: III.25.graphic.inverted.png

.. _III.25:

III.25
======

   Given a segment of a circle, to describe the complete circle of which it is a segment.

Let ``ABC`` be the given segment of a circle; thus it is required to describe the complete circle belonging to the segment ``ABC``, that is, of which it is a segment.

For let ``AC`` be bisected at ``D``, let ``DB`` be drawn from the point ``D`` at right angles to ``AC``, and let ``AB``. be joined;


.. container:: center

   the angle ``ABD`` is then greater than, equal to, or less than the angle ``BAD``.


First let it be greater; and on the straight line ``BA``, and at the point ``A`` on it, let the angle ``BAE`` be constructed equal to the angle ``ABD``; let ``DB`` be drawn through to ``E``, and let ``EC`` be joined.

Then, since the angle ``ABE`` is equal to the angle ``BAE``,


.. container:: center

   the straight line ``EB`` is also equal to ``EA``. [:ref:`I.6 <I.6>`]


And, since ``AD`` is equal to ``DC``, and ``DE`` is common,


.. container:: center

   the two sides ``AD``, ``DE`` are equal to the two sides ``CD``, ``DE`` respectively;


and the angle ``ADE`` is equal to the angle ``CDE``, for each is right;


.. container:: center

   therefore the base ``AE`` is equal to the base ``CE``.


But ``AE`` was proved equal to ``BE``;


.. container:: center

   therefore ``BE`` is also equal to ``CE``;


therefore the three straight lines ``AE``, ``EB``, ``EC`` are equal to one another.

Therefore the circle drawn with centre ``E`` and distance one of the straight lines ``AE``, ``EB``, ``EC`` will also pass through the remaining points and will have been completed. [:ref:`III.9 <III.9>`]

Therefore, given a segment of a circle, the complete circle has been described.

And it is manifest that the segment ``ABC`` is less than a semicircle, because the centre ``E`` happens to be outside it.

Similarly, even if the angle ``ABD`` be equal to the angle ``BAD``, ``AD`` being equal to each of the two ``BD``, ``DC``,


.. container:: center

   the three straight lines ``DA``, ``DB``, ``DC`` will be equal to one another, 
           ``D`` will be the centre of the completed circle, and ``ABC`` will clearly be a semicircle.


But, if the angle ``ABD`` be less than the angle ``BAD``, and if we construct, on the straight line ``BA`` and at the point ``A`` on it, an angle equal to the angle ``ABD``, the centre will fall on ``DB`` within the segment ``ABC``, and the segment

``ABC`` will clearly be greater than a semicircle.

Therefore, given a segment of a circle, the complete circle has been described. Q. E. F.
to describe the complete circle, προσαναγράψαι τὸν κύκλον, literally “to describe the circle ``on to it``.’


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "III.9" [fillcolor="#222244", URL="/heath/III/9/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "III.25" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/25/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.25" -> "I.6";
     "I.5" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "III.9" -> "I.def.10";
     "III.25" -> "III.9";
     "I.2" -> "I.cn.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.3" -> "I.2";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "III.9" -> "I.8";
     "I.5" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.9" -> "III.1.p.1";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
   }
