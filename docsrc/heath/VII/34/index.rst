:order: 34
:number: 305
:type: prop
:dependencies: VII.16, VII.17, VII.19, VII.20, VII.21, VII.33, VII.def.15




.. picture:: VII.34.graphic.inverted.png

.. _VII.34:

VII.34
======

   Given two numbers, to find the least number which they measure.

Let A, B be the two given numbers; thus it is required to find the least number which they measure.

Now A, B are either prime to one another or not.

First, let A, B be prime to one another, and let A by multiplying B make C; therefore also B by multiplying A has made C. [:ref:`VII.16 <VII.16>`]

Therefore A, B measure C

I say next that it is also the least number they measure.

For, if not, A, B will measure some number which is less than C.

Let them measure D.

Then, as many times as A measures D, so many units let there be in E, and, as many times as B measures D, so many units let there be in F; therefore A by multiplying E has made D, and B by multiplying F has made D; [:ref:`VII.def.15 <VII.def.15>`] therefore the product of A, E is equal to the product of B, F.

Therefore, as A is to B, so is F
E. [:ref:`VII.19 <VII.19>`]

But A, B are prime, primes are also least, [:ref:`VII.21 <VII.21>`] and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less; [:ref:`VII.20 <VII.20>`] therefore B measures E, as consequent consequent.

And, since A by multiplying B, E has made C, D, therefore, as B is to E, so is C to D. [:ref:`VII.17 <VII.17>`]

But B measures E; therefore C also measures D, the greater the less: which is impossible.

Therefore A, B do not measure any number less than C; therefore C is the least that is measured by A, B.

Next, let A, B not be prime to one another, and let F, E, the least numbers of those which have the same ratio with A, B, be taken; [:ref:`VII.33 <VII.33>`] therefore the product of A, E is equal to the product of B, F. [:ref:`VII.19 <VII.19>`]

And let A by multiplying E make C; therefore also B by multiplying F has made C; therefore A, B measure C.

I say next that it is also the least number that they measure.

For, if not, A, B will measure some number which is less than C.

Let them measure D.

And, as many times as A measures D, so many units let there be in G, and, as many times as B measures D, so many units let there be in H.

Therefore A by multiplying G has made D, and B by multiplying H has made D.

Therefore the product of A, G is equal to the product of B, H; therefore, as A is to B, so is H to G. [:ref:`VII.19 <VII.19>`]

But, as A is to B, so is F to E.

Therefore also, as F is to E, so is H to G.

But F, E are least, and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less; [:ref:`VII.20 <VII.20>`] therefore E measures G.

And, since A by multiplying E, G has made C, D, therefore, as E is to G, so is C to D. [:ref:`VII.17 <VII.17>`]

But E measures G; therefore C also measures D, the greater the less: which is impossible.

Therefore A, B will not measure any number which is less than C.

Therefore C is the least that is measured by A, B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.33" [fillcolor="#222244", URL="/heath/VII/33/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.34" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/34/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "VII.2.p.1" [fillcolor="#333333"];
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
     "VII.3" [fillcolor="#222244", URL="/heath/VII/3/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "VII.34" -> "VII.33";
     "V.7" -> "V.def.5";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.34" -> "VII.20";
     "VII.19" -> "VII.18";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "V.8" -> "V.def.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VII.33" -> "VII.def.15";
     "VII.34" -> "VII.def.15";
     "VII.3" -> "VII.2.p.1";
     "VII.2" -> "VII.1";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.34" -> "VII.16";
     "VII.16" -> "VII.15";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "V.8" -> "V.1";
     "VII.13" -> "VII.10";
     "VII.20" -> "VII.4";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.33" -> "VII.19";
     "VII.34" -> "VII.19";
     "V.9" -> "V.8";
     "VII.33" -> "VII.21";
     "VII.34" -> "VII.21";
     "VII.10" -> "VII.9";
     "VII.33" -> "VII.3";
     "VII.19" -> "V.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.19" -> "V.9";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.34" -> "VII.17";
   }



Required for
------------

:ref:`VII.36`, :ref:`VII.39`, :ref:`VIII.4`, :ref:`VIII.5`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.12`, :ref:`X.13`, :ref:`X.17`, :ref:`X.18`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`