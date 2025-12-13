:order: 7
:number: 90
:type: prop
:tags: line
:dependencies: I.43, I.46




.. picture:: II.7.graphic.inverted.png

.. _II.7:

II.7
====

   If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment and the square on the remaining segment.

For let a straight line ``AB`` be cut at random at the point ``C``;

I say that the squares on ``AB``, ``BC`` are equal to twice the rectangle contained by ``AB``, ``BC`` and the square on ``CA``.

For let the square ``ADEB`` be described on ``AB``, [:ref:`I.46 <I.46>`] and let the figure be drawn.

Then, since ``AG`` is equal to ``GE``, [:ref:`I.43 <I.43>`] let ``CF`` be added to each;


.. container:: center

   therefore the whole ``AF`` is equal to the whole ``CE``.


Therefore ``AF``, ``CE`` are double of ``AF``.

But ``AF``, ``CE`` are the gnomon ``KLM`` and the square ``CF``; therefore the gnomon ``KLM`` and the square ``CF`` are double of ``AF``.

But twice the rectangle ``AB``, ``BC`` is also double of ``AF``; for ``BF`` is equal to ``BC``; therefore the gnomon ``KLM`` and the square ``CF`` are equal to twice the rectangle ``AB``, ``BC``.

Let ``DG``, which is the square on ``AC``, be added to each; therefore the gnomon ``KLM`` and the squares ``BG``, ``GD`` are equal to twice the rectangle contained by ``AB``, ``BC`` and the square on ``AC``.

But the gnomon ``KLM`` and the squares ``BG``, ``GD`` are the whole ``ADEB`` and ``CF``,


.. container:: center

   which are squares described on ``AB``, ``BC``;


therefore the squares on ``AB``, ``BC`` are equal to twice the rectangle contained by ``AB``, ``BC`` together with the square on ``AC``.

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
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.43" [fillcolor="#222244", URL="/heath/I/43/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "II.7" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/II/7/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.46" -> "I.31";
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
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.10" -> "I.9";
     "II.7" -> "I.43";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
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
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
     "II.7" -> "I.46";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.43" -> "I.cn.3";
     "I.34" -> "I.29";
     "I.46" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.43" -> "I.34";
     "I.46" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
   }



Required for
------------

:ref:`II.13`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.73`, :ref:`X.74`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`