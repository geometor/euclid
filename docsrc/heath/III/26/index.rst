:order: 26
:number: 134
:type: prop
:tags: circle
:dependencies: I.4, III.24, III.def.11




.. picture:: III.26.graphic.inverted.png

.. _III.26:

III.26
======

   In equal circles equal angles stand on equal circumferences, whether they stand at the centres or at the circumferences.

Let ``ABC``, ``DEF`` be equal circles, and in them let there be equal angles, namely at the centres the angles ``BGC``, ``EHF``, and at the circumferences the angles ``BAC``, ``EDF``; I say that the circumference ``BKC`` is equal to the circumference ``ELF``.

For let ``BC``, ``EF`` be joined.

Now, since the circles ``ABC``, ``DEF`` are equal,


.. container:: center

   the radii are equal.


Thus the two straight lines ``BG``, ``GC`` are equal to the two straight lines ``EH``, ``HF``;


.. container:: center

   and the angle at ``G`` is equal to the angle at ``H``; therefore the base ``BC`` is equal to the base ``EF``. [:ref:`I.4 <I.4>`]


And, since the angle at ``A`` is equal to the angle at ``D``,


.. container:: center

   the segment ``BAC`` is similar to the segment ``EDF``; [:ref:`III.def.11 <III.def.11>`]


and they are upon equal straight lines.

But similar segments of circles on equal straight lines are equal to one another; [:ref:`III.24 <III.24>`]


.. container:: center

   therefore the segment ``BAC`` is equal to ``EDF``.


But the whole circle ``ABC`` is also equal to the whole circle ``DEF``; therefore the circumference ``BKC`` which remains is equal to the circumference ``ELF``.

Therefore etc. Q. E. D.


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
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "III.24" [fillcolor="#222244", URL="/heath/III/24/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.26" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/26/", target="_top"];
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
     "III.26" -> "III.24";
     "I.5" -> "I.4";
     "III.26" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.10" -> "III.5";
     "III.10" -> "III.1.p.1";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "I.7" -> "I.5";
     "III.26" -> "III.def.11";
   }



Required for
------------

:ref:`III.27`, :ref:`III.28`, :ref:`III.29`, :ref:`III.30`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.16`, :ref:`VI.33`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.18`, :ref:`XIII.8`, :ref:`XIII.9`