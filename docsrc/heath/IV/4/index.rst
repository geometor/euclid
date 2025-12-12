:order: 4
:number: 156
:type: prop
:tags: circle, triangle
:dependencies: I.26, I.9, III.16, IV.13, IV.def.5




.. picture:: IV.4.graphic.inverted.png

.. _IV.4:

IV.4
====

   In a given triangle to inscribe a circle.

Let ``ABC`` be the given triangle; thus it is required to inscribe a circle in the triangle ``ABC``.

Let the angles ``ABC``, ``ACB``
be bisected by the straight lines ``BD``, ``CD`` [:ref:`I.9 <I.9>`], and let these meet one another at the point ``D``; from ``D`` let ``DE``, ``DF``, ``DG`` be drawn perpendicular to the straight lines ``AB``, ``BC``, ``CA``.

Now, since the angle ``ABD`` is equal to the angle ``CBD``, and the right angle ``BED`` is also equal to the right angle ``BFD``, ``EBD``, ``FBD`` are two triangles having two angles equal to two angles and one side equal to one side, namely that subtending one of the equal angles, which is ``BD`` common to the triangles;


.. container:: center

   therefore they will also have the remaining sides equal to the remaining sides; [:ref:`I.26 <I.26>`]



.. container:: center

   therefore ``DE`` is equal to ``DF``.


For the same reason


.. container:: center

   ``DG`` is also equal to ``DF``.


Therefore the three straight lines ``DE``, ``DF``, ``DG`` are equal to one another;


.. container:: center

   therefore the circle described with centre ``D`` and distance one of the straight lines ``DE``, ``DF``, ``DG`` will pass also through the remaining points, and will touch the straight lines ``AB``, ``BC``, ``CA``, because the angles at the points ``E``, ``F``, ``G``
           are right.


For, if it cuts them, the straight line drawn at right angles to the diameter of the circle from its extremity will be found to fall within the circle : which was proved absurd; [:ref:`III.16 <III.16>`]


.. container:: center

   therefore the circle described with centre ``D`` and distance one of the straight lines ``DE``, ``DF``, ``DG`` will not cut the straight lines ``AB``, ``BC``, ``CA``;



.. container:: center

   therefore it will touch them, and will be the circle inscribed in the triangle ``ABC``. [:ref:`IV.def.5 <IV.def.5>`]


Let it be inscribed, as ``FGE``.

Therefore in the given triangle ``ABC`` the circle ``EFG`` has been inscribed. Q. E. F.
and distance one of the (straight lines D)E, (D)F, (D)G. The words and letters here shown in brackets are put in to fill out the rather careless language of the Greek. Here and in several other places in Book IV. Euclid says literally and with distance one of the (points) ``E``, ``F``, ``G``
(καὶ διαστήματι ὲνὶ τῶν E, Z, H) and the like. In one case (:ref:`IV.13 <IV.13>`) he actually has with distance one of the ``points G``, ``H``, ``K``, ``L``, ``M``
(διαστήματι ὲνὶ τῶν Η, Θ, Κ, Λ, Μ σημείων). Heiberg notes Graecam locutionem satis miram et negligentem,
but, in view of its frequent occurrence in good MSS., does not venture to correct it.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "IV.def.5" [fillcolor="#224422", URL="/heath/IV/def.5/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "IV.4" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/4/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "IV.13" [fillcolor="#222244", URL="/heath/IV/13/", target="_top"];
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
     "IV.4" -> "IV.def.5";
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
     "IV.4" -> "IV.13";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "IV.4" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "IV.4" -> "III.16";
     "IV.13" -> "III.16";
     "I.15" -> "I.post.4";
     "IV.4" -> "I.26";
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
