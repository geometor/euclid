:order: 19
:number: 356
:type: prop
:dependencies: IX.17, VII.14, VII.19, VII.20, VII.21




.. picture:: IX.19.graphic.inverted.png

.. _IX.19:

IX.19
=====

   Given three numbers, to investigate when it is possible to find a fourth proportional to them.

Let A, B, C be the given three numbers, and let it be required to investigate when it is possible to find a fourth proportional to them.

Now either they are not in continued proportion, and the extremes of them are prime to one another; or they are in continued proportion, and the extremes of them are not prime to one another; or they are not in continued proportion, nor are the extremes of them prime to one another; or they are in continued proportion, and the extremes of them are prime to one another.

If then A, B, C are in continued proportion, and the extremes of them A, C are prime to one another, it has been proved that it is impossible to find a fourth proportional number to them. [:ref:`IX.17 <IX.17>`]

<*>Next, let A, B, C not be in continued proportion, the extremes being again prime to one another; I say that in this case also it is impossible to find a fourth proportional to them.

For, if possible, let D have been found, so that,


.. container:: center

   as A is to B, so is C to D,


and let it be contrived that, as B is to C, so is D to E.

Now, since, as A is to B, so is C to D, and, as B is to C, so is D to E, therefore, ex aequali, as A is to C, so is C to E. [:ref:`VII.14 <VII.14>`]

But A, C are prime, primes are also least, [:ref:`VII.21 <VII.21>`] and the least numbers measure those which have the same ratio, the antecedent the antecedent and the consequent the consequent. [:ref:`VII.20 <VII.20>`]

Therefore A measures C as antecedent antecedent.

But it also measures itself; therefore A measures A, C which are prime to one another: which is impossible.

Therefore it is not possible to find a fourth proportional to A, B, C.<*>

Next, let A, B, C be again in continued proportion, but let A, C not be prime to one another.

I say that it is possible to find a fourth proportional to them.

For let B by multiplying C make D; therefore A either measures D or does not measure it.

First, let it measure it according to E; therefore A by multiplying E has made D.

But, further, B has also by multiplying C made D; therefore the product of A, E is equal to the product of B, C; therefore, proportionally, as A is to B, so is C to E; [:ref:`VII.19 <VII.19>`] therefore E has been found a fourth proportional to A, B, C.

Next, let A not measure D; I say that it is impossible to find a fourth proportional number to A, B, C.

For, if possible, let E have been found; therefore the product of A, E is equal to the product of B, C. [:ref:`VII.19 <VII.19>`]

But the product of B, C is D; therefore the product of A, E is also equal to D.

Therefore A by multiplying E has made D; therefore A measures D according to E, so that A measures D.

But it also does not measure it: which is absurd.

Therefore it is not possible to find a fourth proportional number to A, B, C when A does not measure D.

Next, let A, B, C not be in continued proportion, nor the extremes prime to one another.

And let B by multiplying C make D.

Similarly then it can be proved that, if A measures D, it is possible to find a fourth proportional to them, but, if it does not measure it, impossible. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "IX.19" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IX/19/", target="_top"];
     "IX.17" [fillcolor="#222244", URL="/heath/IX/17/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.19" [fillcolor="#222244", URL="/heath/VII/19/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "VII.21" [fillcolor="#222244", URL="/heath/VII/21/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "VII.14" [fillcolor="#222244", URL="/heath/VII/14/", target="_top"];
     "V.7" -> "V.def.5";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "IX.17" -> "VII.20";
     "IX.19" -> "VII.20";
     "VII.19" -> "VII.18";
     "VII.4" -> "VII.2";
     "V.8" -> "V.def.4";
     "IX.19" -> "IX.17";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.2" -> "VII.1";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.16" -> "VII.15";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "IX.17" -> "VII.13";
     "V.8" -> "V.1";
     "VII.13" -> "VII.10";
     "VII.20" -> "VII.4";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "IX.19" -> "VII.19";
     "V.9" -> "V.8";
     "IX.17" -> "VII.21";
     "IX.19" -> "VII.21";
     "VII.10" -> "VII.9";
     "VII.19" -> "V.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.19" -> "V.9";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "IX.19" -> "VII.14";
   }
