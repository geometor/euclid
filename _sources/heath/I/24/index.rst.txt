:order: 24
:number: 57
:type: prop
:tags: line, triangle
:dependencies: I.19, I.23, I.4, I.5




.. picture:: I.24.graphic.inverted.png

.. _I.24:

I.24
====

   If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.

Let ``ABC``, ``DEF`` be two triangles having the two sides ``AB``, ``AC`` equal to the two sides ``DE``, ``DF`` respectively, namely ``AB`` to ``DE``, and ``AC`` to ``DF``, and let the angle at ``A`` be greater than the angle at ``D``;

I say that the base ``BC`` is also greater than the base ``EF``. 

For, since the angle ``BAC`` is greater than the angle ``EDF``, let there be constructed, on the straight line ``DE``, and at the point ``D`` on it, the angle ``EDG``
        equal to the angle ``BAC``; [:ref:`I.23 <I.23>`] let ``DG`` be made equal to either of the two straight lines ``AC``, ``DF``, and let ``EG``, ``FG`` be joined. 
        

Then, since ``AB`` is equal to ``DE``, and ``AC`` to ``DG``, the two sides ``BA``, ``AC`` are equal to the two sides ``ED``, ``DG``, respectively; and the angle ``BAC`` is equal to the angle ``EDG``; therefore the base ``BC`` is equal to the base ``EG``. [:ref:`I.4 <I.4>`]

Again, since ``DF`` is equal to ``DG``, the angle ``DGF`` is also equal to the angle ``DFG``; [:ref:`I.5 <I.5>`] therefore the angle ``DFG`` is greater than the angle ``EGF``.

Therefore the angle ``EFG`` is much greater than the angle ``EGF``.

And, since ``EFG`` is a triangle having the angle ``EFG``
        greater than the angle ``EGF``, and the greater angle is subtended by the greater side, [:ref:`I.19 <I.19>`] the side ``EG`` is also greater than ``EF``.

But ``EG`` is equal to ``BC``. Therefore ``BC`` is also greater than ``EF``.
        

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **10**

   

   I have naturally left out the well-known words added by Simson in order to avoid the necessity of considering three cases: Of the two sides ``DE``, ``DF`` let ``DE`` be the side which is not greater than the other.

    I doubt whether Euclid could have been induced to insert the words himself, even if it had been represented to him that their omission meant leaving two possible cases out of consideration. His habit and that of the great Greek geometers was, not to set out all possible cases, but to give as a rule one case, generally the most difficult, as here, and to leave the others to the reader to work out for himself. We have already seen one instance in :ref:`I.7 <I.7>`.


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
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.24" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/24/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
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
     "I.24" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.13" -> "I.11";
     "I.18" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
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
     "I.24" -> "I.23";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.24" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.24" -> "I.5";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`I.25`, :ref:`III.15`, :ref:`III.7`, :ref:`III.8`, :ref:`XI.20`, :ref:`XI.21`, :ref:`XI.22`, :ref:`XI.23`, :ref:`XIII.18`