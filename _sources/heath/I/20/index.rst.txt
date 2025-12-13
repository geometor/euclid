:order: 20
:number: 53
:type: prop
:tags: triangle
:dependencies: I.19, I.5, I.cn.5




.. picture:: I.20.graphic.inverted.png

.. _I.20:

I.20
====

   In any triangle two sides taken together in any manner are greater than the remaining one.

For let ``ABC`` be a triangle; I say that in the triangle ``ABC`` two sides taken together in any manner are greater than the remaining one, namely ``BA``, ``AC`` greater than ``BC``, ``AB``, ``BC`` greater than ``AC``, ``BC``, ``CA`` greater than ``AB``.

For let ``BA`` be drawn through to the point ``D``, let ``DA`` be made equal to ``CA``, and let ``DC`` be joined.

Then, since ``DA`` is equal to ``AC``, the angle ``ADC`` is also equal to the angle ``ACD``; [:ref:`I.5 <I.5>`] 
        therefore the angle ``BCD`` is greater than the angle ``ADC``. [:ref:`I.cn.5 <I.cn.5>`]

And, since ``DCB`` is a triangle having the angle ``BCD`` greater than the angle ``BDC``, and the greater angle is subtended by the greater side, [:ref:`I.19 <I.19>`] therefore ``DB`` is greater than ``BC``.
        

But ``DA`` is equal to ``AC``; therefore ``BA``, ``AC`` are greater than ``BC``.

Similarly we can prove that ``AB``, ``BC`` are also greater than ``CA``, and ``BC``, ``CA`` than ``AB``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   It was the habit of the Epicureans, says Proclus (p. 322), to ridicule this theorem as being evident even to an ass and requiring no proof, and their allegation that the theorem was known

    (γνώριμον) even to an ass was based on the fact that, if fodder is placed at one angular point and the ass at another, he does not, in order to get to his food, traverse the two sides of the triangle but only the one side separating them (an argument which makes Savile exclaim that its authors were digni ipsi, qui cum Asino foenum essent,

    p. 78). Proclus replies truly that a mere perception of the truth of the theorem is a different thing from a scientific proof of it and a knowledge of the reason ``why`` it is true. Moreover, as Simson says, the number of axioms should not be increased without necessity.


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
     "I.cn.5" [fillcolor="#442222", URL="/heath/I/cn.5/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.20" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/20/", target="_top"];
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
     "I.20" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.13" -> "I.11";
     "I.18" -> "I.16";
     "I.20" -> "I.cn.5";
     "I.15" -> "I.13";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`I.21`, :ref:`I.22`, :ref:`III.12`, :ref:`III.15`, :ref:`III.7`, :ref:`III.8`, :ref:`XI.20`, :ref:`XI.21`, :ref:`XIII.18`