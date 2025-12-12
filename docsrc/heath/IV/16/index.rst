:order: 16
:number: 168
:type: prop
:tags: circle
:dependencies: III.30




.. picture:: IV.16.graphic.inverted.png

.. _IV.16:

IV.16
=====

   In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular.

``In a given circle to inscribe a fifteen-angled figure which shall be both equilateral and equiangular``.

Let ``ABCD`` be the given circle; thus it is required to inscribe in the circle ``ABCD`` a fifteenangled figure which shall be both equilateral and equiangular.

In the circle ``ABCD`` let there be inscribed a side ``AC`` of the equilateral triangle inscribed in it, and a side ``AB`` of an equilateral pentagon; therefore, of the equal segments of which there are fifteen in the circle ``ABCD``, there will be five in the circumference ``ABC`` which is one-third of the circle, and there will be three in the circumference ``AB`` which is one-fifth of the circle;


.. container:: center

   therefore in the remainder ``BC`` there will be two of the equal segments.


Let ``BC`` be bisected at ``E``; [:ref:`III.30 <III.30>`] therefore each of the circumferences ``BE``, ``EC`` is a fifteenth of the circle ``ABCD``.

If therefore we join ``BE``, ``EC`` and fit into the circle ``ABCD`` straight lines equal to them and in contiguity, a fifteen-angled figure which is both equilateral and equiangular will have been inscribed in it. Q. E. F.

And, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents to the circle, there will be circumscribed about the circle a fifteen-angled figure which is equilateral and equiangular.

And further, by proofs similar to those in the case of the pentagon, we can both inscribe a circle in the given fifteenangled figure and circumscribe one about it. Q. E. F.


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
     "III.30" [fillcolor="#222244", URL="/heath/III/30/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "IV.16" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "III.24" [fillcolor="#222244", URL="/heath/III/24/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.28" [fillcolor="#222244", URL="/heath/III/28/", target="_top"];
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.26" [fillcolor="#222244", URL="/heath/III/26/", target="_top"];
     "III.def.11" [fillcolor="#224422", URL="/heath/III/def.11/", target="_top"];
     "III.24" -> "III.10";
     "I.5" -> "I.3";
     "IV.16" -> "III.30";
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
     "III.28" -> "I.8";
     "I.5" -> "I.4";
     "III.26" -> "I.4";
     "III.30" -> "I.4";
     "III.26" -> "III.24";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "III.30" -> "III.28";
     "III.10" -> "III.5";
     "III.10" -> "III.1.p.1";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "I.7" -> "I.5";
     "III.28" -> "III.26";
     "III.26" -> "III.def.11";
   }
