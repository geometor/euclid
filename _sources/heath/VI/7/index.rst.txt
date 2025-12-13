:order: 7
:number: 223
:type: prop
:tags: triangle
:dependencies: I.13, I.17, I.23, I.32, I.5, V.11, V.9, VI.4




.. picture:: VI.7.graphic.inverted.png

.. _VI.7:

VI.7
====

   If two triangles have one angle equal to one angle, the sides about other angles proportional, and the remaining angles either both less or both not less than a right angle, the triangles will be equiangular and will have those angles equal, the sides about which are proportional.

``If two triangles have one angle equal to one angle``, ``the sides about other angles proportional``, ``and the remaining angles either both less or both not less than a right angle``, ``the triangles will be equiangular and will have those angles equal``, ``the sides about which are proportional``.

Let ``ABC``, ``DEF`` be two triangles having one angle equal to one angle, the angle ``BAC`` to the angle ``EDF``, the sides about other angles ``ABC``, ``DEF`` proportional, so that, as ``AB`` is to ``BC``, so is ``DE`` to ``EF``, and, first, each of the remaining angles at ``C``, ``F`` less than a right angle;

I say that the triangle ``ABC`` is equiangular with the triangle ``DEF``, the angle ``ABC`` will be equal to the angle ``DEF``, and the remaining angle, namely the angle at ``C``, equal to the remaining angle, the angle at ``F``.

For, if the angle ``ABC`` is unequal to the angle ``DEF``, one of them is greater.

Let the angle ``ABC`` be greater; and on the straight line ``AB``, and at the point ``B`` on it, let the angle ``ABG`` be constructed equal to the angle ``DEF``. [:ref:`I.23 <I.23>`]

Then, since the angle ``A`` is equal to ``D``, and the angle ``ABG`` to the angle ``DEF``, therefore the remaining angle ``AGB`` is equal to the remaining angle ``DFE``. [:ref:`I.32 <I.32>`]

Therefore the triangle ``ABG`` is equiangular with the triangle ``DEF``.

Therefore, as ``AB`` is to ``BG``, so is ``DE`` to ``EF`` [:ref:`VI.4 <VI.4>`]

But, as ``DE`` is to ``EF``, so by hypothesis is ``AB`` to ``BC``; therefore ``AB`` has the same ratio to each of the straight lines ``BC``, ``BG``; [:ref:`V.11 <V.11>`]


.. container:: center

   therefore ``BC`` is equal to ``BG``, [:ref:`V.9 <V.9>`]


so that the angle at ``C`` is also equal to the angle ``BGC``. [:ref:`I.5 <I.5>`]

But, by hypothesis, the angle at ``C`` is less than a right angle; therefore the angle ``BGC`` is also less than a right angle; so that the angle ``AGB`` adjacent to it is greater than a right angle. [:ref:`I.13 <I.13>`]

And it was proved equal to the angle at ``F``; therefore the angle at ``F`` is also greater than a right angle.

But it is by hypothesis less than a right angle : which is absurd.

Therefore the angle ``ABC`` is not unequal to the angle ``DEF``; therefore it is equal to it.

But the angle at ``A`` is also equal to the angle at ``D``; therefore the remaining angle at ``C`` is equal to the remaining angle at ``F``. [:ref:`I.32 <I.32>`]

Therefore the triangle ``ABC`` is equiangular with the triangle ``DEF``.

But, again, let each of the angles at ``C``, ``F`` be supposed not less than a right angle; I say again that, in this case too, the triangle ``ABC`` is equiangular with the triangle ``DEF``.

For, with the same construction, we can prove similarly that


.. container:: center

   ``BC`` is equal to ``BG``;


so that the angle at ``C`` is also equal to the angle ``BGC``. [:ref:`I.5 <I.5>`]

But the angle at ``C`` is not less than a right angle; therefore neither is the angle ``BGC`` less than a right angle.

Thus in the triangle ``BGC`` the two angles are not less than two right angles: which is impossible. [:ref:`I.17 <I.17>`]

Therefore, once more, the angle ``ABC`` is not unequal to the angle ``DEF``; therefore it is equal to it.

But the angle at ``A`` is also equal to the angle at ``D``; therefore the remaining angle at ``C`` is equal to the remaining angle at ``F``. [:ref:`I.32 <I.32>`]

Therefore the triangle ``ABC`` is equiangular with the triangle ``DEF``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.15" [fillcolor="#222244", URL="/heath/V/15/", target="_top"];
     "I.32" [fillcolor="#222244", URL="/heath/I/32/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "V.18" [fillcolor="#222244", URL="/heath/V/18/", target="_top"];
     "V.14" [fillcolor="#222244", URL="/heath/V/14/", target="_top"];
     "I.28" [fillcolor="#222244", URL="/heath/I/28/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "V.23" [fillcolor="#222244", URL="/heath/V/23/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "V.4" [fillcolor="#222244", URL="/heath/V/4/", target="_top"];
     "V.16" [fillcolor="#222244", URL="/heath/V/16/", target="_top"];
     "VI.2" [fillcolor="#222244", URL="/heath/VI/2/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "V.11" [fillcolor="#222244", URL="/heath/V/11/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "V.20" [fillcolor="#222244", URL="/heath/V/20/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "I.38" [fillcolor="#222244", URL="/heath/I/38/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "V.13" [fillcolor="#222244", URL="/heath/V/13/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.22" [fillcolor="#222244", URL="/heath/V/22/", target="_top"];
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "VI.7" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VI/7/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "V.12" [fillcolor="#222244", URL="/heath/V/12/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.39" [fillcolor="#222244", URL="/heath/I/39/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "VI.4" [fillcolor="#222244", URL="/heath/VI/4/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "VI.1" [fillcolor="#222244", URL="/heath/VI/1/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "V.21" [fillcolor="#222244", URL="/heath/V/21/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "V.3" [fillcolor="#222244", URL="/heath/V/3/", target="_top"];
     "V.17" [fillcolor="#222244", URL="/heath/V/17/", target="_top"];
     "V.16" -> "V.15";
     "V.23" -> "V.15";
     "VI.1" -> "V.15";
     "VI.7" -> "I.32";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.39" -> "I.cn.1";
     "V.16" -> "V.18";
     "V.16" -> "V.14";
     "V.18" -> "V.14";
     "VI.4" -> "I.28";
     "I.28" -> "I.27";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "V.16" -> "V.23";
     "I.3" -> "I.2";
     "VI.1" -> "I.41";
     "I.15" -> "I.post.4";
     "I.34" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "V.22" -> "V.4";
     "V.23" -> "V.16";
     "VI.1" -> "V.16";
     "VI.4" -> "V.16";
     "VI.4" -> "VI.2";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "VI.7" -> "I.5";
     "V.16" -> "V.11";
     "V.18" -> "V.11";
     "V.23" -> "V.11";
     "VI.1" -> "V.11";
     "VI.2" -> "V.11";
     "VI.7" -> "V.11";
     "V.8" -> "V.def.4";
     "V.16" -> "V.20";
     "V.22" -> "V.20";
     "I.13" -> "I.11";
     "I.39" -> "I.37";
     "I.41" -> "I.37";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.38" -> "I.36";
     "VI.1" -> "I.38";
     "VI.2" -> "I.38";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.27" -> "I.def.23";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.9" -> "V.8";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "I.36" -> "I.33";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "VI.4" -> "I.17";
     "VI.7" -> "I.17";
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.22" -> "V.def.5";
     "VI.1" -> "V.def.5";
     "V.16" -> "V.22";
     "VI.4" -> "V.22";
     "I.32" -> "I.31";
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.39" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "V.15" -> "V.12";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "VI.2" -> "I.39";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "VI.7" -> "I.13";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "VI.4" -> "I.post.5";
     "I.31" -> "I.23";
     "VI.7" -> "I.23";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "VI.7" -> "VI.4";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "VI.2" -> "V.7";
     "VI.2" -> "V.9";
     "VI.7" -> "V.9";
     "I.16" -> "I.10";
     "VI.2" -> "VI.1";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.17" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.32" -> "I.29";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.4" -> "I.cn.4";
     "V.3" -> "V.2";
     "V.17" -> "V.2";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.17" -> "V.1";
     "V.16" -> "V.21";
     "V.23" -> "V.21";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "VI.4" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "V.4" -> "V.3";
     "V.16" -> "V.17";
     "V.18" -> "V.17";
   }
