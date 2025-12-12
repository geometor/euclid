:order: 21
:number: 54
:type: prop
:categories: construct
:tags: line, triangle
:dependencies: I.16, I.20




.. picture:: I.21.graphic.inverted.png

.. _I.21:

I.21
====

   If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greater angle.

On ``BC``, one of the sides of the triangle ``ABC``, from its extremities ``B``, ``C``, let the two straight lines ``BD``, ``DC`` be constructed meeting within the triangle;

I say that ``BD``, ``DC`` are less than the remaining two sides of the triangle ``BA``, ``AC``, but contain an angle ``BDC`` greater than the angle ``BAC``. 

For let ``BD`` be drawn through to ``E``.

Then, since in any triangle two sides are greater than the remaining one, [:ref:`I.20 <I.20>`] therefore, in the triangle ``ABE``, the two sides ``AB``, ``AE`` are greater than ``BE``.

Let ``EC`` be added to each; therefore ``BA``, ``AC`` are greater than ``BE``, ``EC``.
        

Again, since, in the triangle ``CED``, the two sides ``CE``, ``ED`` are greater than ``CD``, let ``DB`` be added to each; therefore ``CE``, ``EB`` are greater than ``CD``, ``DB``.

But ``BA``, ``AC`` were proved greater than ``BE``, ``EC``; therefore ``BA``, ``AC`` are much greater than ``BD``, ``DC``.

Again, since in any triangle the exterior angle is greater than the interior and opposite angle, [:ref:`I.16 <I.16>`] therefore, in the triangle ``CDE``, the exterior angle ``BDC`` is greater than the angle ``CED``.
        

For the same reason, moreover, in the triangle ``ABE`` also, the exterior angle ``CEB`` is greater than the angle ``BAC``. But the angle ``BDC`` was proved greater than the angle ``CEB``; therefore the angle ``BDC`` is much greater than the angle ``BAC``.
        

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **2. be constructed...meeting within the triangle.**

   

   The word meeting

    is not in the Greek, where the words are ἐντὸς συσταθῶσιν. συνίστασθαι is the word used of constructing two straight lines ``to a point`` (cf. :ref:`I.7 <I.7>`) or so as to form a triangle; but it is necessary in English to indicate that they ``meet``.


.. note::


   **3. the straight lines so constructed.**

   

   Observe the elegant brevity of the Greek αἱ συσταθεῖσαι.


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
     "I.21" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/21/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
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
     "I.21" -> "I.16";
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
     "I.21" -> "I.20";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`III.8`