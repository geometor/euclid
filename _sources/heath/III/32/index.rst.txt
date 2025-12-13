:order: 32
:number: 140
:type: prop
:tags: line, circle
:dependencies: I.32, III.19, III.22, III.31




.. picture:: III.32.graphic.inverted.png

.. _III.32:

III.32
======

   If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

For let a straight line ``EF`` touch the circle ``ABCD`` at the point ``B``, and from the point ``B`` let there be drawn across, in the circle ``ABCD``, a straight line ``BD`` cutting it; I say that the angles which ``BD`` makes with the tangent ``EF`` will be equal to the angles in the alternate segments of the circle, that is, that the angle ``FBD`` is equal to the angle constructed in the segment ``BAD``, and the angle ``EBD`` is equal to the angle constructed in the segment ``DCB``.

For let ``BA`` be drawn from ``B`` at right angles to ``EF``, let a point ``C`` be taken at random on the circumference ``BD``,

and let ``AD``, ``DC``, ``CB`` be joined.

Then, since a straight line ``EF`` touches the circle ``ABCD`` at ``B``, and ``BA`` has been drawn from the point of contact at right angles to the tangent, the centre of the circle ``ABCD`` is on ``BA``. [:ref:`III.19 <III.19>`]

Therefore ``BA`` is a diameter of the circle ``ABCD``;


.. container:: center

   therefore the angle ``ADB``, being an angle in a semicircle, is right. [:ref:`III.31 <III.31>`]


Therefore the remaining angles ``BAD``, ``ABD`` are equal to one right angle. [:ref:`I.32 <I.32>`]

But the angle ``ABF`` is also right; therefore the angle ``ABF`` is equal to the angles ``BAD``, ``ABD``.

Let the angle ``ABD`` be subtracted from each; therefore the angle ``DBF`` which remains is equal to the angle ``BAD`` in the alternate segment of the circle.

Next, since ``ABCD`` is a quadrilateral in a circle, its opposite angles are equal to two right angles. [:ref:`III.22 <III.22>`]

But the angles ``DBF``, ``DBE`` are also equal to two right angles; therefore the angles ``DBF``, ``DBE`` are equal to the angles ``BAD``, ``BCD``,


.. container:: center

   of which the angle ``BAD`` was proved equal to the angle ``DBF``; therefore the angle ``DBE`` which remains is equal to the angle ``DCB`` in the alternate segment ``DCB`` of the circle.


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
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "III.32" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/32/", target="_top"];
     "III.18" [fillcolor="#222244", URL="/heath/III/18/", target="_top"];
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
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "III.22" [fillcolor="#222244", URL="/heath/III/22/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "III.21" [fillcolor="#222244", URL="/heath/III/21/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "III.19" [fillcolor="#222244", URL="/heath/III/19/", target="_top"];
     "III.31" [fillcolor="#222244", URL="/heath/III/31/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "III.20" [fillcolor="#222244", URL="/heath/III/20/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "I.32" -> "I.31";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "III.32" -> "I.32";
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
     "III.18" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "III.19" -> "III.18";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
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
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "I.16" -> "I.10";
     "III.31" -> "III.22";
     "III.32" -> "III.22";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "III.22" -> "III.21";
     "I.32" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "III.32" -> "III.19";
     "III.32" -> "III.31";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "III.21" -> "III.20";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.18" -> "I.17";
     "III.31" -> "I.17";
   }



Required for
------------

:ref:`III.33`, :ref:`III.34`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.2`, :ref:`XIII.13`, :ref:`XIII.18`