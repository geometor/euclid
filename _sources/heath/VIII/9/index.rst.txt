:order: 9
:number: 319
:type: prop
:dependencies: VII.def.20, VIII.1, VIII.2, VIII.2.p.1




.. picture:: VIII.9.graphic.inverted.png

.. _VIII.9:

VIII.9
======

   If two numbers be prime to one another, and numbers fall between them in continued proportion, then, however many numbers fall between them in continued proportion, so many will also fall between each of them and an unit in continued proportion.

Let A, B be two numbers prime to one another, and let C, D fall between them in continued proportion, and let the unit E be set out; I say that, as many numbers as fall between A, B in continued proportion, so many will also fall between either of the numbers A, B and the unit in continued proportion.

For let two numbers F, G, the least that are in the ratio of A, C, D, B, be taken, three numbers H, K, L with the same property, and others more by one continually, until their multitude is equal to the multitude of A, C, D, B. [:ref:`VIII.2 <VIII.2>`]

Let them be taken, and let them be M, N, O, P.

It is now manifest that F by multiplying itself has made H and by multiplying H has made M, while G by multiplying itself has made L and by multiplying L has made P. [:ref:`VIII.2.p.1 <VIII.2.p.1>`]

And, since M, N, O, P are the least of those which have the same ratio with F, G, and A, C, D, B are also the least of those which have the same ratio with F, G, [:ref:`VIII.1 <VIII.1>`] while the multitude of the numbers M, N, O, P is equal to the multitude of the numbers A, C, D, B, therefore M, N, O, P are equal to A, C, D, B respectively; therefore M is equal to A, and P to B.

Now, since F by multiplying itself has made H, therefore F measures H according to the units in F.

But the unit E also measures F according to the units in it; therefore the unit E measures the number F the same number of times as F measures H.

Therefore, as the unit E is to the number F, so is F to H. [:ref:`VII.def.20 <VII.def.20>`]

Again, since F by multiplying H has made M, therefore H measures M according to the units in F.

But the unit E also measures the number F according to the units in it; therefore the unit E measures the number F the same number of times as H measures M.

Therefore, as the unit E is to the number F, so is H to M.

But it was also proved that, as the unit E is to the number F, so is F to H; therefore also, as the unit E is to the number F, so is F to H, and H to M.

But M is equal to A; therefore, as the unit E is to the number F, so is F to H, and H to A.

For the same reason also, as the unit E is to the number G, so is G to L and L to B.

Therefore, as many numbers as have fallen between A, B in continued proportion, so many numbers also have fallen between each of the numbers A, B and the unit E in continued proportion. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "VIII.9" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VIII/9/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.26" [fillcolor="#222244", URL="/heath/VII/26/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "VIII.2.p.1" [fillcolor="#333333"];
     "VII.27" [fillcolor="#222244", URL="/heath/VII/27/", target="_top"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "VII.25" [fillcolor="#222244", URL="/heath/VII/25/", target="_top"];
     "VII.21" [fillcolor="#222244", URL="/heath/VII/21/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "VII.24" [fillcolor="#222244", URL="/heath/VII/24/", target="_top"];
     "VII.22" [fillcolor="#222244", URL="/heath/VII/22/", target="_top"];
     "VIII.2" [fillcolor="#222244", URL="/heath/VIII/2/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VII.23" [fillcolor="#222244", URL="/heath/VII/23/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VIII.1" [fillcolor="#222244", URL="/heath/VIII/1/", target="_top"];
     "VII.19" [fillcolor="#222244", URL="/heath/VII/19/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "VII.14" [fillcolor="#222244", URL="/heath/VII/14/", target="_top"];
     "V.7" -> "V.def.5";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "VII.4" -> "VII.2";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VIII.9" -> "VII.def.20";
     "VII.27" -> "VII.26";
     "VII.2" -> "VII.1";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VIII.9" -> "VIII.2.p.1";
     "VIII.2" -> "VII.27";
     "VII.20" -> "VII.4";
     "VII.27" -> "VII.25";
     "VII.24" -> "VII.21";
     "VIII.1" -> "VII.21";
     "VII.10" -> "VII.9";
     "VII.19" -> "V.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.19" -> "V.9";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VIII.2" -> "VII.22";
     "VIII.9" -> "VIII.2";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
     "V.8" -> "V.def.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.16" -> "VII.15";
     "V.8" -> "V.1";
     "VII.13" -> "VII.10";
     "VII.24" -> "VII.23";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "VIII.2" -> "VIII.1";
     "VIII.9" -> "VIII.1";
     "VII.24" -> "VII.19";
     "V.9" -> "V.8";
     "VIII.1" -> "VII.14";
   }
