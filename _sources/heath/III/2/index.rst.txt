:order: 2
:number: 110
:type: prop
:tags: line, circle
:dependencies: I.16, I.19, I.5, III.1




.. picture:: III.2.graphic.inverted.png

.. _III.2:

III.2
=====

   If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

Let ``ABC`` be a circle, and let two points ``A``, ``B`` be taken at random on its circumference; I say that the straight line joined from ``A`` to ``B`` will fall within the circle.

For suppose it does not, but, if possible, let it fall outside, as ``AEB``; let the centre of the circle ``ABC`` be taken [:ref:`III.1 <III.1>`], and let it be ``D``; let ``DA``, ``DB`` be joined, and let ``DFE`` be drawn through.

Then, since ``DA`` is equal to ``DB``,


.. container:: center

   the angle ``DAE`` is also equal to the angle ``DBE``. [:ref:`I.5 <I.5>`]


And, since one side ``AEB`` of the triangle ``DAE`` is produced,


.. container:: center

   the angle ``DEB`` is greater than the angle ``DAE``. [:ref:`I.16 <I.16>`]


But the angle ``DAE`` is equal to the angle ``DBE``;


.. container:: center

   therefore the angle ``DEB`` is greater than the angle ``DBE``.


And the greater angle is subtended by the greater side; [:ref:`I.19 <I.19>`]


.. container:: center

   therefore ``DB`` is greater than ``DE``. But ``DB`` is equal to ``DF``;



.. container:: center

   therefore ``DF`` is greater than ``DE``,



.. container:: center

   the less than the greater : which is impossible.


Therefore the straight line joined from ``A`` to ``B`` will not fall outside the circle.

Similarly we can prove that neither will it fall on the circumference itself;


.. container:: center

   therefore it will fall within.


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
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "III.2" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/2/", target="_top"];
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
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "III.2" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "I.16" -> "I.15";
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



Required for
------------

:ref:`III.13`