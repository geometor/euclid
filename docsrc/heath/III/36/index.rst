:order: 36
:number: 144
:type: prop
:tags: line, circle
:dependencies: I.47, II.6, III.18, III.3




.. picture:: III.36.graphic.inverted.png

.. _III.36:

III.36
======

   If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the circle and the other touch it, the rectangle contained by the whole of the straight line which cuts the circle and the straight line intercepted on it outside between the point and the convex circumference will be equal to the square on the tangent.

For let a point ``D`` be taken outside the circle ``ABC``, and from ``D`` let the two straight lines ``DCA``, ``DB`` fall on the circle ``ABC``; let ``DCA`` cut the circle ``ABC`` and let ``BD`` touch it; I say that the rectangle contained by ``AD``, ``DC`` is equal to the square on ``DB``.

Then ``DCA`` is either through the centre or not through the centre.

First let it be through the centre, and let ``F`` be the centre of the circle ``ABC``; let ``FB`` be joined;


.. container:: center

   therefore the angle ``FBD`` is right. [:ref:`III.18 <III.18>`]


And, since ``AC`` has been bisected at ``F``, and ``CD`` is added to it, the rectangle ``AD``, ``DC`` together with the square on ``FC`` is equal to the square on ``FD``. [:ref:`II.6 <II.6>`]

But ``FC`` is equal to ``FB``; therefore the rectangle ``AD``, ``DC`` together with the square on ``FB`` is equal to the square on ``FD``.

And the squares on ``FB``, ``BD`` are equal to the square on ``FD``; [:ref:`I.47 <I.47>`] therefore the rectangle ``AD``, ``DC`` together with the square on ``FB`` is equal to the squares on ``FB``, ``BD``.

Let the square on ``FB`` be subtracted from each; therefore the rectangle ``AD``, ``DC`` which remains is equal to the square on the tangent ``DB``.

Again, let ``DCA`` not be through the centre of the circle ``ABC``; let the centre ``E`` be taken, and from ``E`` let ``EF`` be drawn perpendicular to ``AC``; let ``EB``, ``EC``, ``ED`` be joined.

Then the angle ``EBD`` is right. [:ref:`III.18 <III.18>`]

And, since a straight line ``EF`` through the centre cuts a straight line ``AC`` not through the centre at right angles,


.. container:: center

   it also bisects it; [:ref:`III.3 <III.3>`] therefore ``AF`` is equal to ``FC``.


Now, since the straight line ``AC`` has been bisected at the point ``F``, and ``CD`` is added to it, the rectangle contained by ``AD``, ``DC`` together with the square on ``FC`` is equal to the square on ``FD``. [:ref:`II.6 <II.6>`]

Let the square on ``FE`` be added to each; therefore the rectangle ``AD``, ``DC`` together with the squares on ``CF``, ``FE`` is equal to the squares on ``FD``, ``FE``.

But the square on ``EC`` is equal to the squares on ``CF``, ``FE``, for the angle ``EFC`` is right; [:ref:`I.47 <I.47>`] and the square on ``ED`` is equal to the squares on ``DF``, ``FE``; therefore the rectangle ``AD``, ``DC`` together with the square on ``EC`` is equal to the square on ``ED``.

And ``EC`` is equal to ``EB``; therefore the rectangle ``AD``, ``DC`` together with the square on ``EB`` is equal to the square on ``ED``.

But the squares on ``EB``, ``BD`` are equal to the square on ``ED``, for the angle ``EBD`` is right; [:ref:`I.47 <I.47>`] therefore the rectangle ``AD``, ``DC`` together with the square on ``EB`` is equal to the squares on ``EB``, ``BD``.

Let the square on ``EB`` be subtracted from each; therefore the rectangle ``AD``, ``DC`` which remains is equal to the square on ``DB``.

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
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "III.18" [fillcolor="#222244", URL="/heath/III/18/", target="_top"];
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
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "III.36" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/36/", target="_top"];
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
     "III.3" [fillcolor="#222244", URL="/heath/III/3/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "II.6" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "III.18" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.3" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "III.36" -> "III.18";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
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
     "III.36" -> "II.6";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "I.34" -> "I.26";
     "III.3" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.3" -> "I.8";
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
     "I.19" -> "I.5";
     "III.3" -> "I.5";
     "I.16" -> "I.10";
     "I.47" -> "I.46";
     "II.6" -> "I.46";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.41" -> "I.37";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
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
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "III.36" -> "I.47";
     "I.47" -> "I.14";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.27" -> "I.def.23";
     "III.36" -> "III.3";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.36" -> "I.33";
     "I.19" -> "I.18";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.43" -> "I.34";
     "I.46" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.18" -> "I.17";
   }



Required for
------------

:ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`