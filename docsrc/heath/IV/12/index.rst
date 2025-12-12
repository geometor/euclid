:order: 12
:number: 164
:type: prop
:tags: circle
:dependencies: I.26, I.47, I.8, III.1, III.16.p.1, III.18, III.27, IV.11




.. picture:: IV.12.graphic.inverted.png

.. _IV.12:

IV.12
=====

   About a given circle to circumscribe an equilateral and equiangular pentagon.

Let ``ABCDE`` be the given circle; thus it is required to circumscribe an equilateral and equiangular pentagon about the circle ``ABCDE``.

Let ``A``, ``B``, ``C``, ``D``, ``E`` be conceived to be the angular points of the inscribed pentagon, so that the circumferences ``AB``, ``BC``, ``CD``, ``DE``, ``EA`` are equal; [:ref:`IV.11 <IV.11>`]

through ``A``, ``B``, ``C``, ``D``, ``E`` let ``GH``, ``HK``, ``KL``, ``LM``, ``MG`` be drawn touching the circle; [:ref:`III.16.p.1 <III.16.p.1>`] let the centre ``F`` of the circle ``ABCDE`` be taken [:ref:`III.1 <III.1>`], and let ``FB``, ``FK``, ``FC``, ``FL``, ``FD`` be joined.

Then, since the straight line ``KL`` touches the circle ``ABCDE`` at ``C``, and ``FC`` has been joined from the centre ``F`` to the point of contact at ``C``,


.. container:: center

   therefore ``FC`` is perpendicular to ``KL``; [:ref:`III.18 <III.18>`] therefore each of the angles at ``C`` is right.


For the same reason


.. container:: center

   the angles at the points ``B``, ``D`` are also right.


And, since the angle ``FCK`` is right, therefore the square on ``FK`` is equal to the squares on ``FC``, ``CK``.

For the same reason [:ref:`I.47 <I.47>`]


.. container:: center

   the square on ``FK`` is also equal to the squares on ``FB``, ``BK``; so that the squares on ``FC``, ``CK`` are equal to the squares on ``FB``, ``BK``, of which the square on ``FC`` is equal to the square on ``FB``;


therefore the square on ``CK`` which remains is equal to the square on ``BK``.

Therefore ``BK`` is equal to ``CK``.

And, since ``FB`` is equal to ``FC``, and ``FK`` common,


.. container:: center

   the two sides ``BF``, ``FK`` are equal to the two sides ``CF``, ``FK``; and the base ``BK`` equal to the base ``CK``; therefore the angle ``BFK`` is equal to the angle ``KFC``, [:ref:`I.8 <I.8>`] and the angle ``BKF`` to the angle ``FKC``.


Therefore the angle ``BFC`` is double of the angle ``KFC``,


.. container:: center

   and the angle ``BKC`` of the angle ``FKC``.


For the same reason


.. container:: center

   the angle ``CFD`` is also double of the angle ``CFL``, and the angle ``DLC`` of the angle ``FLC``.


Now, since the circumference ``BC`` is equal to ``CD``, the angle ``BFC`` is also equal to the angle ``CFD``. [:ref:`III.27 <III.27>`]

And the angle ``BFC`` is double of the angle ``KFC``, and the angle ``DFC`` of the angle ``LFC``;


.. container:: center

   therefore the angle ``KFC`` is also equal to the angle ``LFC``.


But the angle ``FCK`` is also equal to the angle ``FCL``; therefore ``FKC``, ``FLC`` are two triangles having two angles equal to two angles and one side equal to one side, namely ``FC`` which is common to them; therefore they will also have the remaining sides equal to the remaining sides, and the remaining angle to the remaining angle; [:ref:`I.26 <I.26>`]


.. container:: center

   therefore the straight line ``KC`` is equal to ``CL``, and the angle ``FKC`` to the angle ``FLC``.


And, since ``KC`` is equal to ``CL``, therefore ``KL`` is double of ``KC``.

For the same reason it can be proved that


.. container:: center

   ``HK`` is also double of ``BK``.


And ``BK`` is equal to ``KC``;


.. container:: center

   therefore ``HK`` is also equal to ``KL``.


Similarly each of the straight lines ``HG``, ``GM``, ``ML`` can also be proved equal to each of the straight lines ``HK``, ``KL``;


.. container:: center

   therefore the pentagon ``GHKLM`` is equilateral.


I say next that it is also equiangular.

For, since the angle ``FKC`` is equal to the angle ``FLC``, and the angle ``HKL`` was proved double of the angle ``FKC``,


.. container:: center

   and the angle ``KLM`` double of the angle ``FLC``, therefore the angle ``HKL`` is also equal to the angle ``KLM``.


Similarly each of the angles ``KHG``, ``HGM``, ``GML`` can also be proved equal to each of the angles ``HKL``, ``KLM``; therefore the five angles ``GHK``, ``HKL``, ``KLM``, ``LMG``, ``MGH`` are equal to one another.

Therefore the pentagon ``GHKLM`` is equiangular.

And it was also proved equilateral; and it has been circumscribed about the circle ``ABCDE``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.32" [fillcolor="#222244", URL="/heath/I/32/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "III.32" [fillcolor="#222244", URL="/heath/III/32/", target="_top"];
     "IV.10" [fillcolor="#222244", URL="/heath/IV/10/", target="_top"];
     "III.18" [fillcolor="#222244", URL="/heath/III/18/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.43" [fillcolor="#222244", URL="/heath/I/43/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "III.27" [fillcolor="#222244", URL="/heath/III/27/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.26" [fillcolor="#222244", URL="/heath/III/26/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "III.21" [fillcolor="#222244", URL="/heath/III/21/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "III.1" [fillcolor="#222244", URL="/heath/III/1/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "III.31" [fillcolor="#222244", URL="/heath/III/31/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "III.20" [fillcolor="#222244", URL="/heath/III/20/", target="_top"];
     "III.def.11" [fillcolor="#224422", URL="/heath/III/def.11/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "III.37" [fillcolor="#222244", URL="/heath/III/37/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "IV.12" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/12/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "II.6" [fillcolor="#222244", URL="/heath/II/6/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "III.24" [fillcolor="#222244", URL="/heath/III/24/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "IV.11" [fillcolor="#222244", URL="/heath/IV/11/", target="_top"];
     "II.11" [fillcolor="#222244", URL="/heath/II/11/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "III.29" [fillcolor="#222244", URL="/heath/III/29/", target="_top"];
     "IV.5" [fillcolor="#222244", URL="/heath/IV/5/", target="_top"];
     "III.22" [fillcolor="#222244", URL="/heath/III/22/", target="_top"];
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "III.10" [fillcolor="#222244", URL="/heath/III/10/", target="_top"];
     "III.36" [fillcolor="#222244", URL="/heath/III/36/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "IV.1" [fillcolor="#222244", URL="/heath/IV/1/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.47" [fillcolor="#222244", URL="/heath/I/47/", target="_top"];
     "I.14" [fillcolor="#222244", URL="/heath/I/14/", target="_top"];
     "IV.2" [fillcolor="#222244", URL="/heath/IV/2/", target="_top"];
     "III.3" [fillcolor="#222244", URL="/heath/III/3/", target="_top"];
     "III.19" [fillcolor="#222244", URL="/heath/III/19/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "III.16.p.1" [fillcolor="#333333"];
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "III.32" -> "I.32";
     "IV.2" -> "I.32";
     "IV.10" -> "I.32";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "IV.2" -> "III.32";
     "IV.10" -> "III.32";
     "IV.11" -> "IV.10";
     "III.19" -> "III.18";
     "III.36" -> "III.18";
     "III.37" -> "III.18";
     "IV.12" -> "III.18";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.3" -> "I.2";
     "I.47" -> "I.41";
     "II.6" -> "I.43";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.34" -> "I.26";
     "III.3" -> "I.26";
     "IV.12" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.1" -> "I.8";
     "III.3" -> "I.8";
     "III.24" -> "I.8";
     "III.37" -> "I.8";
     "IV.12" -> "I.8";
     "III.29" -> "III.27";
     "IV.11" -> "III.27";
     "IV.12" -> "III.27";
     "III.10" -> "III.1.p.1";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.3" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "IV.10" -> "I.5";
     "III.27" -> "III.26";
     "IV.11" -> "III.26";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.41" -> "I.37";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.43" -> "I.cn.3";
     "III.22" -> "III.21";
     "II.6" -> "I.36";
     "IV.12" -> "III.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.27" -> "I.def.23";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "III.32" -> "III.31";
     "IV.5" -> "III.31";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.36" -> "I.33";
     "III.21" -> "III.20";
     "III.27" -> "III.20";
     "III.26" -> "III.def.11";
     "III.18" -> "I.17";
     "III.31" -> "I.17";
     "I.32" -> "I.31";
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "II.6" -> "I.31";
     "IV.10" -> "I.6";
     "IV.10" -> "III.37";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "III.18" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "III.3" -> "I.def.10";
     "III.31" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.10" -> "I.9";
     "IV.11" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "II.11" -> "II.6";
     "III.36" -> "II.6";
     "I.31" -> "I.23";
     "III.27" -> "I.23";
     "IV.2" -> "I.23";
     "III.26" -> "III.24";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "III.26" -> "I.4";
     "III.29" -> "I.4";
     "IV.5" -> "I.4";
     "IV.12" -> "IV.11";
     "IV.10" -> "II.11";
     "I.16" -> "I.10";
     "IV.5" -> "I.10";
     "IV.11" -> "III.29";
     "IV.10" -> "IV.5";
     "III.31" -> "III.22";
     "III.32" -> "III.22";
     "I.47" -> "I.46";
     "II.6" -> "I.46";
     "II.11" -> "I.46";
     "III.24" -> "III.10";
     "III.37" -> "III.36";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "IV.10" -> "IV.1";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.32" -> "I.29";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "I.4" -> "I.cn.4";
     "II.11" -> "I.47";
     "III.36" -> "I.47";
     "IV.12" -> "I.47";
     "I.47" -> "I.14";
     "IV.11" -> "IV.2";
     "III.36" -> "III.3";
     "III.32" -> "III.19";
     "I.19" -> "I.18";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.43" -> "I.34";
     "I.46" -> "I.34";
     "III.10" -> "III.5";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "III.37" -> "III.16.p.1";
     "IV.2" -> "III.16.p.1";
     "IV.12" -> "III.16.p.1";
   }
