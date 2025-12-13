:order: 12
:number: 389
:type: prop
:dependencies: V.11, V.22, VIII.4, X.5, X.6




.. picture:: X.12.graphic.inverted.png

.. _X.12:

X.12
====

   Magnitudes commensurable with the same magnitude are commensurable with one another also.

For let each of the magnitudes A, B be commensurable with C; I say that A is also commensurable with B.

For, since A is commensurable with C, therefore A has to C the ratio which a number has to a number. [:ref:`X.5 <X.5>`]

Let it have the ratio which D has to E.

Again, since C is commensurable with B, therefore C has to B the ratio which a number has to a number. [:ref:`X.5 <X.5>`]

Let it have the ratio which F has to G.

And, given any number of ratios we please, namely the ratio which D has to E and that which F has to G, let the numbers H, K, L be taken continuously in the given ratios; [cf. :ref:`VIII.4 <VIII.4>`] so that, as D is to E, so is H to K,


.. container:: center

   and, as F is to G, so is K to L.


Since, then, as A is to C, so is D to E, while, as D is to E, so is H to K, therefore also, as A is to C, so is H to K. [:ref:`V.11 <V.11>`]

Again, since, as C is to B, so is F to G, while, as F is to G, so is K to L, therefore also, as C is to B, so is K to L. [:ref:`V.11 <V.11>`]

But also, as A is to C, so is H to K; therefore, ex aequali, as A is to B, so is H to L. [:ref:`V.22 <V.22>`]

Therefore A has to B the ratio which a number has to a number; therefore A is commensurable with B. [:ref:`X.6 <X.6>`]

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.22" [fillcolor="#222244", URL="/heath/V/22/", target="_top"];
     "VII.33" [fillcolor="#222244", URL="/heath/VII/33/", target="_top"];
     "X.6" [fillcolor="#222244", URL="/heath/X/6/", target="_top"];
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "VI.19.p.1" [fillcolor="#333333"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "V.4" [fillcolor="#222244", URL="/heath/V/4/", target="_top"];
     "VII.21" [fillcolor="#222244", URL="/heath/VII/21/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "X.12" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/X/12/", target="_top"];
     "V.11" [fillcolor="#222244", URL="/heath/V/11/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "V.20" [fillcolor="#222244", URL="/heath/V/20/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "X.5" [fillcolor="#222244", URL="/heath/X/5/", target="_top"];
     "VII.34" [fillcolor="#222244", URL="/heath/VII/34/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "VII.2.p.1" [fillcolor="#333333"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "V.3" [fillcolor="#222244", URL="/heath/V/3/", target="_top"];
     "VIII.4" [fillcolor="#222244", URL="/heath/VIII/4/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.19" [fillcolor="#222244", URL="/heath/VII/19/", target="_top"];
     "V.13" [fillcolor="#222244", URL="/heath/V/13/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "V.7.p.1" [fillcolor="#333333"];
     "VII.3" [fillcolor="#222244", URL="/heath/VII/3/", target="_top"];
     "VII.35" [fillcolor="#222244", URL="/heath/VII/35/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.22" -> "V.def.5";
     "X.5" -> "V.22";
     "X.6" -> "V.22";
     "X.12" -> "V.22";
     "VII.34" -> "VII.33";
     "X.12" -> "X.6";
     "VII.19" -> "VII.18";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VIII.4" -> "VII.def.20";
     "X.5" -> "VII.def.20";
     "X.6" -> "VII.def.20";
     "VII.2" -> "VII.1";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VIII.4" -> "VII.13";
     "X.6" -> "VI.19.p.1";
     "VII.20" -> "VII.4";
     "V.22" -> "V.4";
     "VII.33" -> "VII.21";
     "VII.34" -> "VII.21";
     "VII.10" -> "VII.9";
     "V.10" -> "V.7";
     "VII.19" -> "V.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.19" -> "V.9";
     "X.6" -> "V.9";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.34" -> "VII.17";
     "X.6" -> "V.11";
     "X.12" -> "V.11";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.34" -> "VII.20";
     "VIII.4" -> "VII.20";
     "V.8" -> "V.def.4";
     "V.22" -> "V.20";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "X.12" -> "X.5";
     "VIII.4" -> "VII.34";
     "VII.33" -> "VII.def.15";
     "VII.34" -> "VII.def.15";
     "VII.3" -> "VII.2.p.1";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.34" -> "VII.16";
     "VII.16" -> "VII.15";
     "V.3" -> "V.2";
     "V.8" -> "V.1";
     "VII.13" -> "VII.10";
     "V.4" -> "V.3";
     "X.12" -> "VIII.4";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.33" -> "VII.19";
     "VII.34" -> "VII.19";
     "V.20" -> "V.13";
     "V.9" -> "V.8";
     "V.10" -> "V.8";
     "V.20" -> "V.8";
     "X.5" -> "V.7.p.1";
     "X.6" -> "V.7.p.1";
     "VII.33" -> "VII.3";
     "VIII.4" -> "VII.35";
     "V.20" -> "V.10";
   }



Required for
------------

:ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.13`, :ref:`X.17`, :ref:`X.18`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`