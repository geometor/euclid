:order: 8
:number: 160
:type: prop
:tags: circle
:dependencies: I.10, I.31, I.34, III.16




.. picture:: IV.8.graphic.inverted.png

.. _IV.8:

IV.8
====

   In a given square to inscribe a circle.

``In a given square to inscribe a circle``.

Let ``ABCD`` be the given square; thus it is required to inscribe a circle in the given square ``ABCD``.

Let the straight lines ``AD``, ``AB`` be bisected at the points ``E``, ``F`` respectively [:ref:`I.10 <I.10>`], through ``E`` let ``EH`` be drawn parallel to either ``AB`` or ``CD``, and through ``F`` let ``FK`` be drawn parallel to either ``AD`` or ``BC``; [:ref:`I.31 <I.31>`] therefore each of the figures ``AK``, ``KB``, ``AH``, ``HD``, ``AG``, ``GC``, ``BG``, ``GD`` is a parallelogram, and their opposite sides are evidently equal. [:ref:`I.34 <I.34>`]

Now, since ``AD`` is equal to ``AB``, and ``AE`` is half of ``AD``, and ``AF`` half of ``AB``,


.. container:: center

   therefore ``AE`` is equal to ``AF``, so that the opposite sides are also equal;



.. container:: center

   therefore ``FG`` is equal to ``GE``.


Similarly we can prove that each of the straight lines ``GH``, ``GK`` is equal to each of the straight lines ``FG``, ``GE``;


.. container:: center

   therefore the four straight lines ``GE``, ``GF``, ``GH``, ``GK`` are equal to one another.


Therefore the circle described with centre ``G`` and distance one of the straight lines ``GE``, ``GF``, ``GH``, ``GK`` will pass also through the remaining points.

And it will touch the straight lines ``AB``, ``BC``, ``CD``, ``DA``, because the angles at ``E``, ``F``, ``H``, ``K`` are right.

For, if the circle cuts ``AB``, ``BC``, ``CD``, ``DA``, the straight line drawn at right angles to the diameter of the circle from its extremity will fall within the circle : which was proved absurd; [:ref:`III.16 <III.16>`] therefore the circle described with centre ``G`` and distance one of the straight lines ``GE``, ``GF``, ``GH``, ``GK`` will not cut the straight lines ``AB``, ``BC``, ``CD``, ``DA``.

Therefore it will touch them, and will have been inscribed in the square ``ABCD``.

Therefore in the given square a circle has been inscribed. Q. E. F.


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
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "III.16" [fillcolor="#222244", URL="/heath/III/16/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "IV.8" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/8/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "IV.8" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "III.16" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "IV.8" -> "III.16";
     "I.31" -> "I.23";
     "I.15" -> "I.post.4";
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
     "I.19" -> "I.5";
     "III.16" -> "I.5";
     "I.16" -> "I.10";
     "IV.8" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.34" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "IV.8" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.16" -> "I.17";
   }
