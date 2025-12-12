:order: 10
:number: 320
:type: prop
:dependencies: VII.17, VII.18, VII.def.20




.. picture:: VIII.10.graphic.inverted.png

.. _VIII.10:

VIII.10
=======

   If numbers fall between each of two numbers and an unit in continued proportion, however many numbers fall between each of them and an unit in continued proportion, so many also will fall between the numbers themselves in continued proportion.

For let the numbers D, E and F, G respectively fall between the two numbers A, B and the unit C in continued proportion; I say that, as many numbers as have fallen between each of the numbers A, B and the unit C in continued proportion, so many numbers will also fall between A, B in continued proportion.

For let D by multiplying F make H, and let the numbers D, F by multiplying H make K, L respectively.

Now, since, as the unit C is to the number D, so is D to E, therefore the unit C measures the number D the same number of times as D measures E. [:ref:`VII.def.20 <VII.def.20>`]

But the unit C measures the number D according to the units in D; therefore the number D also measures E according to the units in D; therefore D by multiplying itself has made E.

Again, since, as C is to the number D, so is E to A, therefore the unit C measures the number D the same number of times as E measures A.

But the unit C measures the number D according to the units in D; therefore E also measures A according to the units in D; therefore D by multiplying E has made A.

For the same reason also F by multiplying itself has made G, and by multiplying G has made B.

And, since D by multiplying itself has made E and by multiplying F has made H, therefore, as D is to F, so is E to H. [:ref:`VII.17 <VII.17>`]

For the same reason also,


.. container:: center

   as D is to F, so is H to G. [:ref:`VII.18 <VII.18>`]


Therefore also, as E is to H, so is H to G.

Again, since D by multiplying the numbers E, H has made A, K respectively, therefore, as E is to H, so is A to K. [:ref:`VII.17 <VII.17>`]

But, as E is to H, so is D to F; therefore also, as D is to F, so is A to K.

Again, since the numbers D, F by multiplying H have made K, L respectively, therefore, as D is to F, so is K to L. [:ref:`VII.18 <VII.18>`]

But, as D is to F, so is A to K; therefore also, as A is to K, so is K to L.

Further, since F by multiplying the numbers H, G has made L, B respectively, therefore, as H is to G, so is L to B. [:ref:`VII.17 <VII.17>`]

But, as H is to G, so is D to F; therefore also, as D is to F, so is L to B.

But it was also proved that,


.. container:: center

   as D is to F, so is A to K and K to L;


therefore also, as A is to K, so is K to L and L to B.

Therefore A, K, L, B are in continued proportion.

Therefore, as many numbers as fall between each of the numbers A, B and the unit C in continued proportion, so many also will fall between A, B in continued proportion. Q. E. D.


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
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "VIII.10" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VIII/10/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "VII.17" -> "VII.13";
     "VII.13" -> "VII.10";
     "VIII.10" -> "VII.18";
     "VII.18" -> "VII.17";
     "VIII.10" -> "VII.17";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VIII.10" -> "VII.def.20";
     "VII.10" -> "VII.9";
     "VII.15" -> "VII.12";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.16" -> "VII.15";
   }
