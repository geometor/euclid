:order: 15
:number: 167
:type: prop
:tags: circle
:dependencies: I.15, I.32, I.5, III.26, III.27, III.29




.. picture:: IV.15.graphic.inverted.png

.. _IV.15:

IV.15
=====

   In a given circle to inscribe an equilateral and equiangular hexagon.

Let ``ABCDEF`` be the given circle; thus it is required to inscribe an equilateral and equiangular hexagon in the circle ``ABCDEF``.

Let the diameter ``AD`` of the circle ``ABCDEF`` be drawn; let the centre ``G`` of the circle be taken, and with centre ``D`` and distance ``DG`` let the circle ``EGCH`` be described;

let ``EG``, ``CG`` be joined and carried through to the points ``B``, ``F``, and let ``AB``, ``BC``, ``CD``, ``DE``, ``EF``, ``FA`` be joined.

I say that the hexagon ``ABCDEF`` is equilateral and equiangular.

For, since the point ``G`` is the centre of the circle ``ABCDEF``,


.. container:: center

   ``GE`` is equal to ``GD``.


Again, since the point ``D`` is the centre of the circle ``GCH``,


.. container:: center

   ``DE`` is equal to ``DG``.


But ``GE`` was proved equal to ``GD``;


.. container:: center

   therefore ``GE`` is also equal to ``ED``; therefore the triangle ``EGD`` is equilateral;


and therefore its three angles ``EGD``, ``GDE``, ``DEG`` are equal to one another, inasmuch as, in isosceles triangles, the angles at the base are equal to one another. [:ref:`I.5 <I.5>`]

And the three angles of the triangle are equal to two right angles; [:ref:`I.32 <I.32>`]


.. container:: center

   therefore the angle ``EGD`` is one-third of two right angles.


Similarly, the angle ``DGC`` can also be proved to be onethird of two right angles.

And, since the straight line ``CG`` standing on ``EB`` makes the adjacent angles ``EGC``, ``CGB`` equal to two right angles, therefore the remaining angle ``CGB`` is also one-third of two right angles.

Therefore the angles ``EGD``, ``DGC``, ``CGB`` are equal to one another; so that the angles vertical to them, the angles ``BGA``, ``AGF``, ``FGE`` are equal. [:ref:`I.15 <I.15>`]

Therefore the six angles ``EGD``, ``DGC``, ``CGB``, ``BGA``, ``AGF``, ``FGE`` are equal to one another.

But equal angles stand on equal circumferences; [:ref:`III.26 <III.26>`] therefore the six circumferences ``AB``, ``BC``, ``CD``, ``DE``, ``EF``, ``FA`` are equal to one another.

And equal circumferences are subtended by equal straight lines; [:ref:`III.29 <III.29>`]


.. container:: center

   therefore the six straight lines are equal to one another; therefore the hexagon ``ABCDEF`` is equilateral.


I say next that it is also equiangular.

For, since the circumference ``FA`` is equal to the circumference ``ED``,


.. container:: center

   let the circumference ``ABCD`` be added to each; therefore the whole ``FABCD`` is equal to the whole ``EDCBA``;


and the angle ``FED`` stands on the circumference ``FABCD``, and the angle ``AFE`` on the circumference ``EDCBA``;


.. container:: center

   therefore the angle ``AFE`` is equal to the angle ``DEF``. [:ref:`III.27 <III.27>`]


Similarly it can be proved that the remaining angles of the hexagon ``ABCDEF`` are also severally equal to each of the angles ``AFE``, ``FED``;


.. container:: center

   therefore the hexagon ``ABCDEF`` is equiangular.


But it was also proved equilateral; and it has been inscribed in the circle ``ABCDEF``.

Therefore in the given circle an equilateral and equiangular hexagon has been inscribed. Q. E. F.


.. _IV.15.p.1:


**IV.15.p.1**


From this it is manifest that the side of the hexagon is equal to the radius of the circle. 
And, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents to the circle, there will be circumscribed about the circle an equilateral and equiangular hexagon in conformity with what was explained in the case of the pentagon. 
And further by means similar to those explained in the case of the pentagon we can both inscribe a circle in a given hexagon and circumscribe one about it. Q. E. F.

PORISM.

From this it is manifest that the side of the hexagon is equal to the radius of the circle. 

And, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents to the circle, there will be circumscribed about the circle an equilateral and equiangular hexagon in conformity with what was explained in the case of the pentagon. 

And further by means similar to those explained in the case of the pentagon we can both inscribe a circle in a given hexagon and circumscribe one about it. Q. E. F.


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
     "III.24" [fillcolor="#222244", URL="/heath/III/24/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "III.27" [fillcolor="#222244", URL="/heath/III/27/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.26" [fillcolor="#222244", URL="/heath/III/26/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "III.29" [fillcolor="#222244", URL="/heath/III/29/", target="_top"];
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
     "IV.15" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/15/", target="_top"];
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "III.def.11" [fillcolor="#224422", URL="/heath/III/def.11/", target="_top"];
     "I.32" -> "I.31";
     "III.20" -> "I.32";
     "IV.15" -> "I.32";
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
     "IV.15" -> "I.15";
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
     "III.26" -> "III.24";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "III.26" -> "I.4";
     "III.29" -> "I.4";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.24" -> "I.8";
     "III.29" -> "III.27";
     "IV.15" -> "III.27";
     "III.10" -> "III.1.p.1";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "III.20" -> "I.5";
     "IV.15" -> "I.5";
     "III.27" -> "III.26";
     "IV.15" -> "III.26";
     "I.16" -> "I.10";
     "IV.15" -> "III.29";
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
