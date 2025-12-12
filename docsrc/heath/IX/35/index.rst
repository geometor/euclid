:order: 35
:number: 372
:type: prop
:dependencies: VII.11, VII.12, VII.13




.. picture:: IX.35.graphic.inverted.png

.. _IX.35:

IX.35
=====

   If as many numbers as we please be in continued proportion, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to the first, so will the excess of the last be to all those before it.

Let there be as many numbers as we please in continued proportion, A, BC, D, EF, beginning from A as least, and let there be subtracted from BC and EF the numbers BG, FH, each equal to A; I say that, as GC is to A, so is EH to A, BC, D.

For let FK be made equal to BC, and FL equal to D.

Then, since FK is equal to BC, and of these the part FH is equal to the part BG, therefore the remainder HK is equal to the remainder GC.

And since, as EF is to D, so is D to BC, and BC to A, while D is equal to FL, BC to FK, and A to FH, therefore, as EF is to FL, so is LF to FK, and FK to FH.

Separando, as EL is to LF, so is LK to FK, and KH to FH. [:ref:`VII.11 <VII.11>` :ref:`VII.13 <VII.13>`]

Therefore also, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents; [:ref:`VII.12 <VII.12>`] therefore, as KH is to FH, so are EL, LK. KH to LF, FK, HF.

But KH is equal to CG, FH to A, and LF, FK, HF to D, BC, A; therefore, as CG is to A, so is EH to D, BC, A.

Therefore, as the excess of the second is to the first, so is the excess of the last to all those before it. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VII.11" [fillcolor="#222244", URL="/heath/VII/11/", target="_top"];
     "VII.8" [fillcolor="#222244", URL="/heath/VII/8/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "IX.35" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/35/", target="_top"];
     "VII.7" [fillcolor="#222244", URL="/heath/VII/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "IX.35" -> "VII.13";
     "VII.13" -> "VII.10";
     "IX.35" -> "VII.11";
     "VII.11" -> "VII.8";
     "VII.6" -> "VII.5";
     "VII.7" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.11" -> "VII.def.20";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.10" -> "VII.9";
     "VII.8" -> "VII.7";
     "VII.11" -> "VII.7";
     "IX.35" -> "VII.12";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
   }



Required for
------------

:ref:`IX.36`