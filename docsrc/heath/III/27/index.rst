:order: 27
:number: 135
:type: prop
:tags: circle
:dependencies: I.23, III.20, III.26




.. picture:: III.27.graphic.inverted.png

.. _III.27:

III.27
======

   In equal circles angles standing on equal circumferences are equal to one another, whether they stand at the centres or at the circumferences.

For in equal circles ``ABC``, ``DEF``, on equal circumferences ``BC``, ``EF``, let the angles ``BGC``, ``EHF`` stand at the centres ``G``, ``H``, and the angles ``BAC``, ``EDF`` at the circumferences; I say that the angle ``BGC`` is equal to the angle ``EHF``, and the angle ``BAC`` is equal to the angle ``EDF``.

For, if the angle ``BGC`` is unequal to the angle ``EHF``,


.. container:: center

   one of them is greater.


Let the angle ``BGC`` be greater : and on the straight line ``BG``, and at the point ``G`` on it, let the angle ``BGK`` be constructed equal to the angle ``EHF``. [:ref:`I.23 <I.23>`]

Now equal angles stand on equal circumferences, when they are at the centres; [:ref:`III.26 <III.26>`]


.. container:: center

   therefore the circumference ``BK`` is equal to the circumference ``EF``.


But ``EF`` is equal to ``BC``;


.. container:: center

   therefore ``BK`` is also equal to ``BC``, the less to the greater : which is impossible.


Therefore the angle ``BGC`` is not unequal to the angle ``EHF``;


.. container:: center

   therefore it is equal to it.


And the angle at ``A`` is half of the angle ``BGC``,


.. container:: center

   and the angle at ``D`` half of the angle ``EHF``; [:ref:`III.20 <III.20>`]


therefore the angle at ``A`` is also equal to the angle at ``D``.

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
     "III.24" [fillcolor="#222244", URL="/heath/III/24/", target="_top"];
     "III.27" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/27/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.26" [fillcolor="#222244", URL="/heath/III/26/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "III.10" [fillcolor="#222244", URL="/heath/III/10/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.20" [fillcolor="#222244", URL="/heath/III/20/", target="_top"];
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "III.def.11" [fillcolor="#224422", URL="/heath/III/def.11/", target="_top"];
     "I.32" -> "I.31";
     "III.20" -> "I.32";
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
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.15" -> "I.13";
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
     "III.27" -> "I.23";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.24" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "III.26" -> "I.4";
     "III.26" -> "III.24";
     "III.10" -> "III.1.p.1";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "III.27" -> "III.26";
     "I.16" -> "I.10";
     "III.24" -> "III.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.32" -> "I.29";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.27" -> "III.20";
     "III.10" -> "III.5";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "III.26" -> "III.def.11";
   }



Required for
------------

:ref:`III.29`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`VI.33`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.18`, :ref:`XIII.8`, :ref:`XIII.9`