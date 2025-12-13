:order: 9
:number: 117
:type: prop
:tags: line, circle
:dependencies: I.8, I.def.10, III.1.p.1




.. picture:: III.9.graphic.inverted.png

.. _III.9:

III.9
=====

   If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

Let ``ABC`` be a circle and ``D`` a point within it, and from ``D`` let more than two equal straight lines, namely ``DA``, ``DB``, ``DC``, fall on the circle ``ABC``; I say that the point ``D`` is the centre of the circle ``ABC``.

For let ``AB``, ``BC`` be joined and bisected at the points ``E``, ``F``, and let ``ED``, ``FD`` be joined and drawn through to the points ``G``, ``K``, ``H``, ``L``.

Then, since ``AE`` is equal to ``EB``, and ``ED`` is common,


.. container:: center

   the two sides ``AE``, ``ED`` are equal to the two sides ``BE``, ``ED``;


and the base ``DA`` is equal to the base ``DB``;


.. container:: center

   therefore the angle ``AED`` is equal to the angle ``BED``. [:ref:`I.8 <I.8>`]


Therefore each of the angles ``AED``, ``BED`` is right; [:ref:`I.def.10 <I.def.10>`] therefore ``GK`` cuts ``AB`` into two equal parts and at right angles.

And since, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line, [:ref:`III.1.p.1 <III.1.p.1>`]


.. container:: center

   the centre of the circle is on ``GK``.


For the same reason


.. container:: center

   the centre of the circle ``ABC`` is also on ``HL``.


And the straight lines ``GK``, ``HL`` have no other point common but the point ``D``;


.. container:: center

   therefore the point ``D`` is the centre of the circle ``ABC``.


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
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "III.9" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/9/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.5" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "III.9" -> "I.def.10";
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



Required for
------------

:ref:`III.25`