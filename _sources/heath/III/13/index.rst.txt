:order: 13
:number: 121
:type: prop
:tags: circle
:dependencies: III.11, III.2, III.def.3




.. picture:: III.13.graphic.inverted.png

.. _III.13:

III.13
======

   A circle does not touch a circle at more points than one, whether it touch it internally or externally.

For, if possible, let the circle ``ABDC`` touch the circle ``EBFD``, first internally, at more points than one, namely ``D``, ``B``.

Let the centre ``G`` of the circle ``ABDC``, and the centre ``H`` of ``EBFD``, be taken.

Therefore the straight line

joined from ``G`` to ``H`` will fall on ``B``, ``D``. [:ref:`III.11 <III.11>`]

Let it so fall, as ``BGHD``.

Then, since the point ``G`` is the centre of the circle ``ABCD``,


.. container:: center

   ``BG`` is equal to ``GD``;



.. container:: center

   therefore ``BG`` is greater than ``HD``; therefore ``BH`` is much greater than ``HD``.


Again, since the point ``H`` is the centre of the circle ``EBFD``,


.. container:: center

   ``BH`` is equal to ``HD``;



.. container:: center

   but it was also proved much greater than it: which is impossible.


Therefore a circle does not touch a circle internally at more points than one.

I say further that neither does it so touch it externally.

For, if possible, let the circle ``ACK`` touch the circle ``ABDC`` at more points than one, namely ``A``, ``C``, and let ``AC`` be joined.

Then, since on the circumference of each of the circles ``ABDC``, ``ACK`` two points ``A``, ``C`` have been taken at random, the straight line joining the points will fall within each circle; [:ref:`III.2 <III.2>`]


.. container:: center

   but it fell within the circle ``ABCD`` and outside ``ACK`` [:ref:`III.def.3 <III.def.3>`]: which is absurd.


Therefore a circle does not touch a circle externally at more points than one.

And it was proved that neither does it so touch it internally.

Therefore etc. Q. E. D.
ABDC. Euclid writes ``ABCD`` (here and in the next proposition), notwithstanding the order in which the points are placed in the figure.
does it so touch it. It is necessary to supply these words which the Greek (ὅτι οὐδὲ ἐκτός and ὅτι οὐδὲ ἐντός) leaves to be understood.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "III.13" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/13/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "III.2" [fillcolor="#222244", URL="/heath/III/2/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "III.11" [fillcolor="#222244", URL="/heath/III/11/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "III.1" [fillcolor="#222244", URL="/heath/III/1/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "III.def.3" [fillcolor="#224422", URL="/heath/III/def.3/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "III.13" -> "III.2";
     "III.2" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "I.16" -> "I.15";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "III.13" -> "III.11";
     "I.13" -> "I.11";
     "I.18" -> "I.16";
     "III.2" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "III.2" -> "III.1";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.1" -> "I.8";
     "III.13" -> "III.def.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.2" -> "I.5";
     "I.16" -> "I.10";
   }
