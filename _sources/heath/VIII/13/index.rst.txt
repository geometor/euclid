:order: 13
:number: 323
:type: prop
:dependencies: VII.14




.. picture:: VIII.13.graphic.inverted.png

.. _VIII.13:

VIII.13
=======

   If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products will be proportional; and, if the original numbers by multiplying the products make certain numbers, the latter will also be proportional.

Let there be as many numbers as we please, A, B, C, in continued proportion, so that, as A is to B, so is B to C; let A, B, C by multiplying themselves make D, E, F, and by multiplying D, E, F let them make G, H, K; I say that D, E, F and G, H, K are in continued proportion.

For let A by multiplying B make L, and let the numbers A, B by multiplying L make M. N respectively.

And again let B by multiplying C make O, and let the numbers B, C by multiplying O make P, Q respectively.

Then, in manner similar to the foregoing, we can prove that D, L, E and G, M, N, H are continuously proportional in the ratio of A to B, and further E, O, F and H, P, Q, K are continuously proportional in the ratio of B to C.

Now, as A is to B, so is B to C; therefore D, L, E are also in the same ratio with E, O, F, and further G, M, N, H in the same ratio with H, P, Q, K.

And the multitude of D, L, E is equal to the multitude of E, O, F, and that of G, M, N, H to that of H, P, Q, K; therefore, ex acquali,


.. container:: center

   as D is to E, so is E to F,


and, as G is to H, so is H to K. [:ref:`VII.14 <VII.14>`] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VIII.13" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VIII/13/", target="_top"];
     "VII.14" [fillcolor="#222244", URL="/heath/VII/14/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.14" -> "VII.13";
     "VII.13" -> "VII.def.20";
     "VII.10" -> "VII.9";
     "VII.13" -> "VII.10";
     "VIII.13" -> "VII.14";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
   }
