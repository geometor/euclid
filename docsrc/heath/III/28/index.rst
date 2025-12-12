:order: 28
:number: 136
:type: prop
:tags: line, circle
:dependencies: I.8, III.26




.. picture:: III.28.graphic.inverted.png

.. _III.28:

III.28
======

   In equal circles equal straight lines cut off equal circumferences, the greater equal to the greater and the less to the less.

Let ``ABC``, ``DEF`` be equal circles, and in the circles let ``AB``, ``DE`` be equal straight lines cutting off ``ACB``, ``DFE`` as greater circumferences and ``AGB``, ``DHE`` as lesser; I say that the greater circumference ``ACB`` is equal to the greater circumference ``DFE``, and the less circumference ``AGB`` to ``DHE``.

For let the centres ``K``, ``L`` of the circles be taken, and let ``AK``, ``KB``, ``DL``, ``LE`` be joined.

Now, since the circles are equal,


.. container:: center

   the radii are also equal; therefore the two sides ``AK``, ``KB`` are equal to the two sides ``DL``, ``LE``;


and the base ``AB`` is equal to the base ``DE``;


.. container:: center

   therefore the angle ``AKB`` is equal to the angle ``DLE``. [:ref:`I.8 <I.8>`]


But equal angles stand on equal circumferences, when they are at the centres; [:ref:`III.26 <III.26>`]


.. container:: center

   therefore the circumference ``AGB`` is equal to ``DHE``.


And the whole circle ``ABC`` is also equal to the whole circle ``DEF``; therefore the circumference ``ACB`` which remains is also equal to the circumference ``DFE`` which remains.

Therefore etc. Q. E. D.


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
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "III.24" [fillcolor="#222244", URL="/heath/III/24/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "III.28" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/28/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "III.26" [fillcolor="#222244", URL="/heath/III/26/", target="_top"];
     "III.def.11" [fillcolor="#224422", URL="/heath/III/def.11/", target="_top"];
     "III.24" -> "III.10";
     "I.5" -> "I.3";
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
     "III.26" -> "III.24";
     "III.24" -> "I.8";
     "III.28" -> "I.8";
     "I.5" -> "I.4";
     "III.26" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
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



Required for
------------

:ref:`III.30`, :ref:`IV.16`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.18`, :ref:`XIII.8`