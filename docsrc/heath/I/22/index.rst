:order: 22
:number: 55
:type: prop
:categories: construct
:tags: line, triangle
:dependencies: I.20, I.3




.. picture:: I.22.graphic.inverted.png

.. _I.22:

I.22
====

   Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manner should be greater than the remaining one.

Let the three given straight lines be ``A``, ``B``, ``C``, and of these let two taken together in any manner be greater than the remaining one, namely ``A``, ``B`` greater than ``C``, ``A``, ``C`` greater than ``B``, and ``B``, ``C`` greater than ``A``; thus it is required to construct a triangle out of straight lines equal to ``A``, ``B``, ``C``. [:ref:`I.20 <I.20>`]

Let there be set out a straight line ``DE``, terminated at ``D`` but of infinite length in the direction of ``E``, and let ``DF`` be made equal to ``A``, ``FG`` equal to ``B``, and ``GH`` equal to ``C``. [:ref:`I.3 <I.3>`]

With centre ``F`` and distance ``FD`` let the circle ``DKL`` be described; again, with centre ``G`` and distance ``GH`` let the circle ``KLH`` be described; and let ``KF``, ``KG`` be joined;

I say that the triangle ``KFG`` has been constructed out of three straight lines equal to ``A``, ``B``, ``C``. 

For, since the point ``F`` is the centre of the circle ``DKL``, ``FD`` is equal to ``FK``.

But ``FD`` is equal to ``A``; therefore ``KF`` is also equal to ``A``.

Again, since the point ``G`` is the centre of the circle ``LKH``, ``GH`` is equal to ``GK``.

But ``GH`` is equal to ``C``; therefore ``KG`` is also equal to ``C``. And ``FG`` is also equal to ``B``; therefore the three straight lines ``KF``, ``FG``, ``GK`` are equal to the three straight lines ``A``, ``B``, ``C``.

Therefore out of the three straight lines ``KF``, ``FG``, ``GK``, which are equal to the three given straight lines ``A``, ``B``, ``C``, the triangle ``KFG`` has been constructed.


**Q. E. D.**


Q. E. F.


.. note::


   **2-4**

   

   This is the first case in the Elements of a διορισμός to a problem in the sense of a statement of the conditions or limits of the possibility of a solution. The criterion is of course supplied by the preceding proposition.


.. note::


   **2. thus it is necessary.**

   

   This is usually translated (e.g. by Williamson and Simson) But it is necessary,

    which is however inaccurate, since the Greek is not δεῖ δέ but δεῖ δή. The words are the same as those used to introduce the διορισμός in the other sense of the definition

    or particular statement

    of a construction to be effected. Hence, as in the latter case we say thus it is required

    (e.g. to bisect the finite straight line ``AB``, :ref:`I.10 <I.10>`), we should here translate ``thus`` it is necessary.


.. note::


   **4**

   

   To this enunciation all the MSS. and Boethius add, after the διορισμός, the words because in any triangle two sides taken together in any manner are greater than the remaining one.

    But this explanation has the appearance of a gloss, and it is omitted by Proclus and Campanus. Moreover there is no corresponding addition to the διορισμός of :ref:`VI.28 <VI.28>`.


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
     "I.22" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/22/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.20" [fillcolor="#222244", URL="/heath/I/20/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.22" -> "I.3";
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
     "I.22" -> "I.20";
     "I.16" -> "I.10";
   }
