:order: 3
:number: 219
:type: prop
:categories: bisect
:tags: line, triangle
:dependencies: I.29, I.5, I.6, V.11, V.9, VI.2




.. picture:: VI.3.graphic.inverted.png

.. _VI.3:

VI.3
====

   If an angle of a triangle be bisected and the straight line cutting the angle cut the base also, the segments of the base will have the same ratio as the remaining sides of the triangle; and, if the segments of the base have the same ratio as the remaining sides of the triangle, the straight line joined from the vertex to the point of section will bisect the angle of the triangle.

Let ``ABC`` be a triangle, and let the angle ``BAC`` be bisected by the straight line ``AD``; I say that, as ``BD`` is to ``CD``, so is ``BA`` to ``AC``.

For let ``CE`` be drawn through ``C`` parallel to ``DA``, and let ``BA``

be carried through and meet it at ``E``.

Then, since the straight line ``AC`` falls upon the parallels ``AD``, ``EC``,


.. container:: center

   the angle ``ACE`` is equal to the angle ``CAD``. [:ref:`I.29 <I.29>`]


But the angle ``CAD`` is by hypothesis equal to the angle ``BAD``; therefore the angle ``BAD`` is also equal to the angle ``ACE``.

Again, since the straight line ``BAE`` falls upon the parallels ``AD``, ``EC``,


.. container:: center

   the exterior angle ``BAD`` is equal to the interior angle ``AEC``. [:ref:`I.29 <I.29>`]


But the angle ``ACE`` was also proved equal to the angle ``BAD``;


.. container:: center

   therefore the angle ``ACE`` is also equal to the angle ``AEC``, so that the side ``AE`` is also equal to the side ``AC``. [:ref:`I.6 <I.6>`]


And, since ``AD`` has been drawn parallel to ``EC``, one of the sides of the triangle ``BCE``, therefore, proportionally, as ``BD`` is to ``DC``, so is ``BA`` to ``AE``.

But ``AE`` is equal to ``AC``; [:ref:`VI.2 <VI.2>`] therefore, as ``BD`` is to ``DC``, so is ``BA`` to ``AC``.

Again, let ``BA`` be to ``AC`` as ``BD`` to ``DC``, and let ``AD`` be joined; I say that the angle ``BAC`` has been bisected by the straight line A.D.

For, with the same construction, since, as ``BD`` is to ``DC``, so is ``BA`` to ``AC``, and also, as ``BD`` is to ``DC``, so is ``BA`` to ``AE`` : for ``AD`` has been drawn parallel to ``EC``, one of the sides of the triangle ``BCE``: [:ref:`VI.2 <VI.2>`] therefore also, as ``BA`` is to ``AC``, so is ``BA`` to ``AE``. [:ref:`V.11 <V.11>`]

Therefore ``AC`` is equal to ``AE``, [:ref:`V.9 <V.9>`] so that the angle ``AEC`` is also equal to the angle ``ACE``. [:ref:`I.5 <I.5>`]

But the angle ``AEC`` is equal to the exterior angle ``BAD``, [:ref:`I.29 <I.29>`] and the angle ``ACE`` is equal to the alternate angle ``CAD``; [``id``.]


.. container:: center

   therefore the angle ``BAD`` is also equal to the angle ``CAD``.


Therefore the angle ``BAC`` has been bisected by the straight line ``AD``.

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
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "V.18" [fillcolor="#222244", URL="/heath/V/18/", target="_top"];
     "V.14" [fillcolor="#222244", URL="/heath/V/14/", target="_top"];
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
     "VI.3" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VI/3/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.22" [fillcolor="#222244", URL="/heath/V/22/", target="_top"];
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
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
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VI.1" [fillcolor="#222244", URL="/heath/VI/1/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
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
     "VI.3" -> "VI.2";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "VI.3" -> "I.5";
     "V.16" -> "V.11";
     "V.18" -> "V.11";
     "V.23" -> "V.11";
     "VI.1" -> "V.11";
     "VI.2" -> "V.11";
     "VI.3" -> "V.11";
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
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.22" -> "V.def.5";
     "VI.1" -> "V.def.5";
     "V.16" -> "V.22";
     "VI.3" -> "I.6";
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
     "I.29" -> "I.15";
     "VI.2" -> "I.39";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.31" -> "I.23";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "VI.2" -> "V.7";
     "VI.2" -> "V.9";
     "VI.3" -> "V.9";
     "VI.2" -> "VI.1";
     "I.16" -> "I.10";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "VI.3" -> "I.29";
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
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "V.4" -> "V.3";
     "V.16" -> "V.17";
     "V.18" -> "V.17";
   }
