:order: 1
:number: 84
:type: prop
:tags: line
:dependencies: I.11, I.3, I.31, I.34




.. picture:: II.1.graphic.inverted.png

.. _II.1:

II.1
====

   If there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments.

Let ``A``, ``BC`` be two straight lines, and let ``BC`` be cut at random at the points ``D``, ``E``; I say that the rectangle contained by ``A``, ``BC`` is equal to the rectangle contained by ``A``, ``BD``, that contained by ``A``, ``DE`` and that contained by ``A``, ``EC``.

For let ``BF`` be drawn from ``B`` at right angles to ``BC``; [:ref:`I.11 <I.11>`] let ``BG`` be made equal to ``A``, [:ref:`I.3 <I.3>`] through ``G`` let ``GH`` be drawn parallel to ``BC``, [:ref:`I.31 <I.31>`] and through ``D``, ``E``, ``C`` let ``DK``, ``EL``, ``CH`` be drawn parallel to ``BG``.

Then ``BH`` is equal to ``BK``, ``DL``, ``EH``.

Now ``BH`` is the rectangle ``A``, ``BC``, for it is contained by ``GB``, ``BC``, and ``BG`` is equal to ``A``;

``BK`` is the rectangle ``A``, ``BD``, for it is contained by ``GB``, ``BD``, and ``BG`` is equal to ``A``;


.. container:: center

   and ``DL`` is the rectangle ``A``, ``DE``, for ``DK``, that is ``BG`` [:ref:`I.34 <I.34>`], is equal to ``A``.


Similarly also ``EH`` is the rectangle ``A``, ``EC``.

Therefore the rectangle ``A``, ``BC`` is equal to the rectangle ``A``, ``BD``, the rectangle ``A``, ``DE`` and the rectangle ``A``, ``EC``.

Therefore etc. Q. E. D.
the rectangle A, BC. From this point onward I shall translate thus in cases where Euclid leaves out the word ``contained`` (περιεχόμενον). Though the word rectangle
is also omitted in the Greek (the neuter article being sufficient to show that the rectangle is meant), it cannot be dispensed with in English. De Morgan advises the use of the expression the rectangle ``under`` two lines.
This does not seem to me a very good expression, and, if used in a translation from the Greek, it might suggest that ὑπό in τὸ ὑπό meant ``under``, which it does not.


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
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "II.1" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/II/1/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "II.1" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "II.1" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.13" -> "I.11";
     "II.1" -> "I.11";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "I.34" -> "I.29";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
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
     "I.34" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "II.1" -> "I.34";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
   }
