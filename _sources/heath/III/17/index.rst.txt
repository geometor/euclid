:order: 17
:number: 125
:type: prop
:tags: line, circle
:dependencies: I.4, III.1, III.16.p.1




.. picture:: III.17.graphic.inverted.png

.. _III.17:

III.17
======

   From a given point to draw a straight line touching a given circle.

Let ``A`` be the given point, and ``BCD`` the given circle; thus it is required to draw from the point ``A`` a straight line touching the circle ``BCD``.

For let the centre ``E`` of the circle be taken; [:ref:`III.1 <III.1>`] let ``AE`` be joined, and with centre ``E`` and distance ``EA`` let the circle ``AFG`` be described;

from ``D`` let ``DF`` be drawn at right angles to ``EA``, and let ``EF``, ``AB`` be joined; I say that ``AB`` has been drawn from the point ``A`` touching the circle ``BCD``.

For, since ``E`` is the centre of the circles ``BCD``, ``AFG``,


.. container:: center

   ``EA`` is equal to ``EF``, and ``ED`` to ``EB``;


therefore the two sides ``AE``, ``EB`` are equal to the two sides ``FE``, ``ED``: and they contain a common angle, the angle at ``E``;


.. container:: center

   therefore the base ``DF`` is equal to the base ``AB``, and the triangle ``DEF`` is equal to the triangle ``BEA``, and the remaining angles to the remaining angles; [:ref:`I.4 <I.4>`] therefore the angle ``EDF`` is equal to the angle ``EBA``.


But the angle ``EDF`` is right;


.. container:: center

   therefore the angle ``EBA`` is also right.


Now ``EB`` is a radius; and the straight line drawn at right angles to the diameter of a circle, from its extremity, touches the circle; [:ref:`III.16.p.1 <III.16.p.1>`]


.. container:: center

   therefore ``AB`` touches the circle ``BCD``.


Therefore from the given point ``A`` the straight line ``AB`` has been drawn touching the circle ``BCD``.


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
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "III.17" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/17/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "III.1" [fillcolor="#222244", URL="/heath/III/1/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.16.p.1" [fillcolor="#333333"];
     "I.5" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "III.1" -> "I.def.10";
     "I.2" -> "I.cn.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.3" -> "I.2";
     "III.17" -> "III.1";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "III.1" -> "I.8";
     "I.5" -> "I.4";
     "III.17" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "III.17" -> "III.16.p.1";
   }
