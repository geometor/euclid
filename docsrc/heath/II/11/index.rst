:order: 11
:number: 94
:type: prop
:tags: line
:dependencies: I.46, I.47, II.6




.. picture:: II.11.graphic.inverted.png

.. _II.11:

II.11
=====

   To cut a given straight line so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.

Let ``AB`` be the given straight line; thus it is required to cut ``AB`` so that the rectangle contained by the whole and one of the segments is equal to the square on the remaining segment.

For let the square ``ABDC`` be described on ``AB``; [:ref:`I.46 <I.46>`] let ``AC`` be bisected at the point ``E``, and let ``BE`` be joined; let ``CA`` be drawn through to ``F``, and let ``EF`` be made equal to ``BE``; let the square ``FH`` be described on ``AF``, and let ``GH`` be drawn through to ``K``.

I say that ``AB`` has been cut at ``H`` so as to make the rectangle contained by ``AB``, ``BH`` equal to the square on ``AH``.

For, since the straight line ``AC`` has been bisected at ``E``, and ``FA`` is added to it,


.. container:: center

   the rectangle contained by ``CF``, ``FA`` together with the square on ``AE`` is equal to the square on ``EF``. [:ref:`II.6 <II.6>`]


But ``EF`` is equal to ``EB``;


.. container:: center

   therefore the rectangle ``CF``, ``FA`` together with the square on ``AE`` is equal to the square on ``EB``.


But the squares on ``BA``, ``AE`` are equal to the square on ``EB``, for the angle at ``A`` is right; [:ref:`I.47 <I.47>`]


.. container:: center

   therefore the rectangle ``CF``, ``FA`` together with the square on ``AE`` is equal to the squares on ``BA``, ``AE``.


Let the square on ``AE`` be subtracted from each;


.. container:: center

   therefore the rectangle ``CF``, ``FA`` which remains is equal to the square on ``AB``.


Now the rectangle ``CF``, ``FA`` is ``FK``, for ``AF`` is equal to ``FG``; and the square on ``AB`` is ``AD``;


.. container:: center

   therefore ``FK`` is equal to ``AD``.


Let ``AK`` be subtracted from each;


.. container:: center

   therefore ``FH`` which remains is equal to ``HD``.


And ``HD`` is the rectangle ``AB``, ``BH``, for ``AB`` is equal to ``BD``; and ``FH`` is the square on ``AH``;


.. container:: center

   therefore the rectangle contained by ``AB``, ``BH`` is equal to the square on ``HA``. therefore the given straight line ``AB`` has been cut at ``H`` so as to make the rectangle contained by ``AB``, ``BH`` equal to the square on ``HA``. Q. E. F.



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
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.43" [fillcolor="#222244", URL="/heath/I/43/", target="_top"];
     "II.6" [fillcolor="#222244", URL="/heath/II/6/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "II.11" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/II/11/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.47" [fillcolor="#222244", URL="/heath/I/47/", target="_top"];
     "I.14" [fillcolor="#222244", URL="/heath/I/14/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "II.6" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.3" -> "I.2";
     "I.47" -> "I.41";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.10" -> "I.9";
     "II.6" -> "I.43";
     "II.11" -> "II.6";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "I.34" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
     "I.47" -> "I.46";
     "II.6" -> "I.46";
     "II.11" -> "I.46";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.41" -> "I.37";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.43" -> "I.cn.3";
     "II.6" -> "I.36";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "II.11" -> "I.47";
     "I.47" -> "I.14";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.36" -> "I.33";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.43" -> "I.34";
     "I.46" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
   }



Required for
------------

:ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`