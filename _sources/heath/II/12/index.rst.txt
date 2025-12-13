:order: 12
:number: 95
:type: prop
:tags: line, triangle
:dependencies: I.47, II.4




.. picture:: II.12.graphic.inverted.png

.. _II.12:

II.12
=====

   In obtuse-angled triangles the square on the side subtending the obtuse angle is greater than the squares on the sides containing the obtuse angle by twice the rectangle contained by one of the sides about the obtuse angle, namely that on which the
          perpendicular falls, and the straight line cut off outside by the perpendicular towards the obtuse angle.

Let ``ABC`` be an obtuse-angled triangle having the angle ``BAC`` obtuse, and let ``BD`` be drawn from the point ``B`` perpendicular to ``CA`` produced;

I say that the square on ``BC`` is greater than the squares on ``BA``, ``AC`` by twice the rectangle contained by ``CA``, ``AD``.

For, since the straight line ``CD`` has been cut at random at the point ``A``, the square on ``DC`` is equal to the squares on ``CA``, ``AD`` and twice the rectangle contained by ``CA``, ``AD``. [:ref:`II.4 <II.4>`]

Let the square on ``DB`` be added to each; therefore the squares on ``CD``, ``DB`` are equal to the squares on ``CA``, ``AD``, ``DB`` and twice the rectangle ``CA``, ``AD``.

But the square on ``CB`` is equal to the squares on ``CD``, ``DB``, for the angle at ``D`` is right; [:ref:`I.47 <I.47>`]


.. container:: center

   and the square on ``AB`` is equal to the squares on ``AD``, ``DB``; [:ref:`I.47 <I.47>`]


therefore the square on ``CB`` is equal to the squares on ``CA``, ``AB`` and twice the rectangle contained by ``CA``, ``AD``;


.. container:: center

   so that the square on ``CB`` is greater than the squares on ``CA``, ``AB`` by twice the rectangle contained by ``CA``, ``AD``.


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
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
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
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.47" [fillcolor="#222244", URL="/heath/I/47/", target="_top"];
     "I.14" [fillcolor="#222244", URL="/heath/I/14/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "II.12" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/II/12/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "II.4" [fillcolor="#222244", URL="/heath/II/4/", target="_top"];
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "II.4" -> "I.31";
     "II.4" -> "I.6";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "I.47" -> "I.41";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "I.34" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "II.4" -> "I.5";
     "I.16" -> "I.10";
     "I.47" -> "I.46";
     "II.4" -> "I.46";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.41" -> "I.37";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "II.4" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "II.12" -> "I.47";
     "I.47" -> "I.14";
     "I.37" -> "I.35";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.35" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.46" -> "I.34";
     "II.4" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "II.12" -> "II.4";
   }
