:order: 3
:number: 111
:type: prop
:categories: bisect
:tags: line, circle
:dependencies: I.26, I.5, I.8, I.def.10




.. picture:: III.3.graphic.inverted.png

.. _III.3:

III.3
=====

   If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects it.

Let ``ABC`` be a circle, and in it let a straight line ``CD``
through the centre bisect a straight line ``AB`` not through the centre at the point ``F``;

I say that it also cuts it at right angles.

For let the centre of the circle ``ABC``
be taken, and let it be ``E``; let ``EA``, ``EB`` be joined.

Then, since ``AF`` is equal to ``FB``, and ``FE`` is common,


.. container:: center

   two sides are equal to two sides;



.. container:: center

   and the base ``EA`` is equal to the base ``EB``; therefore the angle ``AFE`` is equal to the angle ``BFE``. [:ref:`I.8 <I.8>`]


But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; [:ref:`I.def.10 <I.def.10>`]


.. container:: center

   therefore each of the angles ``AFE``, ``BFE`` is right.


Therefore ``CD``, which is through the centre, and bisects ``AB`` which is not through the centre, also cuts it at right angles.

Again, let ``CD`` cut ``AB`` at right angles; I say that it also bisects it. that is, that ``AF`` is equal to ``FB``.

For, with the same construction,


.. container:: center

   since ``EA`` is equal to ``EB``,


the angle ``EAF`` is also equal to the angle ``EBF``. [:ref:`I.5 <I.5>`]

But the right angle ``AFE`` is equal to the right angle ``BFE``, therefore ``EAF``, ``EBF`` are two triangles having two angles equal to two angles and one side equal to one side, namely ``EF``, which is common to them, and subtends one of the equal angles;


.. container:: center

   therefore they will also have the remaining sides equal to the remaining sides; [:ref:`I.26 <I.26>`] therefore ``AF`` is equal to ``FB``.


Therefore etc. Q. E. D.
with the same construction, τῶν αὐτῶν κατασκευασθέντων.


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
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "III.3" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/3/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.3" -> "I.def.10";
     "I.16" -> "I.15";
     "I.13" -> "I.11";
     "I.26" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "III.3" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.3" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "III.3" -> "I.5";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`III.14`, :ref:`III.15`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.4`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`XII.16`