:order: 13
:number: 165
:type: prop
:tags: circle
:dependencies: I.26, I.4, III.16




.. picture:: IV.13.graphic.inverted.png

.. _IV.13:

IV.13
=====

   In a given pentagon, which is equilateral and equiangular, to inscribe a circle.

Let ``ABCDE`` be the given equilateral and equiangular pentagon; thus it is required to inscribe a circle in the pentagon ``ABCDE``.

For let the angles ``BCD``, ``CDE`` be bisected by the straight lines ``CF``, ``DF`` respectively; and from the point ``F``, at which the straight lines ``CF``, ``DF`` meet one another, let the straight lines ``FB``, ``FA``, ``FE`` be joined.

Then, since ``BC`` is equal to ``CD``, and ``CF`` common, the two sides ``BC``, ``CF`` are equal to the two sides ``DC``, ``CF``;

and the angle ``BCF`` is equal to the angle ``DCF``;


.. container:: center

   therefore the base ``BF`` is equal to the base ``DF``,


and the triangle ``BCF`` is equal to the triangle ``DCF``, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend. [:ref:`I.4 <I.4>`]

Therefore the angle ``CBF`` is equal to the angle ``CDF``.

And, since the angle ``CDE`` is double of the angle ``CDF``, and the angle ``CDE`` is equal to the angle ``ABC``, while the angle ``CDF`` is equal to the angle ``CBF``; therefore the angle ``CBA`` is also double of the angle ``CBF``;


.. container:: center

   therefore the angle ``ABF`` is equal to the angle ``FBC``;


therefore the angle ``ABC`` has been bisected by the straight line ``BF``.

Similarly it can be proved that the angles ``BAE``, ``AED`` have also been bisected by the straight lines ``FA``, ``FE`` respectively.

Now let ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` be drawn from the point ``F`` perpendicular to the straight lines ``AB``, ``BC``, ``CD``, ``DE``, ``EA``.

Then, since the angle ``HCF`` is equal to the angle ``KCF``, and the right angle ``FHC`` is also equal to the angle ``FKC``, ``FHC``, ``FKC`` are two triangles having two angles equal to two angles and one side equal to one side, namely ``FC`` which is common to them and subtends one of the equal angles; therefore they will also have the remaining sides equal to the remaining sides; [:ref:`I.26 <I.26>`] therefore the perpendicular ``FH`` is equal to the perpendicular ``FK``.

Similarly it can be proved that each of the straight lines ``FL``, ``FM``, ``FG`` is also equal to each of the straight lines ``FH``, ``FK``; therefore the five straight lines ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` are equal to one another.

Therefore the circle described with centre ``F`` and distance one of the straight lines ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` will pass also through the remaining points; and it will touch the straight lines ``AB``, ``BC``, ``CD``, ``DE``, ``EA``, because the angles at the points ``G``, ``H``, ``K``, ``L``, ``M`` are right.

For, if it does not touch them. but cuts them, it will result that the straight line drawn at right angles to the diameter of the circle from its extremity falls within the circle: which was proved absurd. [:ref:`III.16 <III.16>`]

Therefore the circle described with centre ``F`` and distance one of the straight lines ``FG``, ``FH``, ``FK``, ``FL``, ``FM`` will not cut the straight lines ``AB``, ``BC``, ``CD``, ``DE``, ``EA``;


.. container:: center

   therefore it will touch them.


Let it be described, as ``GHKLM``.

Therefore in the given pentagon, which is equilateral and equiangular, a circle has been inscribed. Q. E. F.


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
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "IV.13" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/13/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "III.16" [fillcolor="#222244", URL="/heath/III/16/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
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
     "III.16" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.13" -> "I.11";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "IV.13" -> "III.16";
     "I.15" -> "I.post.4";
     "IV.13" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "IV.13" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.16" -> "I.5";
     "III.16" -> "I.17";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`IV.4`