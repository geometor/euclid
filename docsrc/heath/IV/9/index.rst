:order: 9
:number: 161
:type: prop
:tags: circle
:dependencies: I.6, I.8




.. picture:: IV.9.graphic.inverted.png

.. _IV.9:

IV.9
====

   About a given square to circumscribe a circle.

Let ``ABCD`` be the given square; thus it is required to circumscribe a circle about the square ``ABCD``.

For let ``AC``, ``BD`` be joined, and let them cut one another at ``E``.

Then, since ``DA`` is equal to ``AB``, and ``AC`` is common, therefore the two sides ``DA``, ``AC`` are equal to the two sides ``BA``, ``AC``; and the base ``DC`` is equal to the base ``BC``;


.. container:: center

   therefore the angle ``DAC`` is equal to the angle ``BAC``. [:ref:`I.8 <I.8>`]


Therefore the angle ``DAB`` is bisected by ``AC``.

Similarly we can prove that each of the angles ``ABC``, ``BCD``, ``CDA`` is bisected by the straight lines ``AC``, ``DB``.

Now, since the angle ``DAB`` is equal to the angle ``ABC``, and the angle ``EAB`` is half the angle ``DAB``, and the angle ``EBA`` half the angle ``ABC``, therefore the angle ``EAB`` is also equal to the angle ``EBA``; so that the side ``EA`` is also equal to ``EB``. [:ref:`I.6 <I.6>`]

Similarly we can prove that each of the straight lines ``EA``, ``EB`` is equal to each of the straight lines ``EC``, ``ED``.

Therefore the four straight lines ``EA``, ``EB``, ``EC``, ``ED`` are equal to one another.

Therefore the circle described with centre ``E`` and distance one of the straight lines ``EA``, ``EB``, ``EC``, ``ED`` will pass also through the remaining points; and it will have been circumscribed about the square ``ABCD``.

Let it be circumscribed, as ``ABCD``.

Therefore about the given square a circle has been circumscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "IV.9" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/9/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "IV.9" -> "I.6";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.2" -> "I.1";
     "I.5" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "IV.9" -> "I.8";
     "I.5" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.cn.3";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.3" -> "I.2";
     "I.4" -> "I.cn.4";
   }
