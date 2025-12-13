:order: 21
:number: 292
:type: prop
:dependencies: VII.16, VII.20, VII.def.12




.. picture:: VII.21.graphic.inverted.png

.. _VII.21:

VII.21
======

   Numbers prime to one another are the least of those which have the same ratio with them.

Let A, B be numbers prime to one another; I say that A, B are the least of those which have the same ratio with them.

For, if not, there will be some numbers less than A, B which are in the same ratio with A, B.

Let them be C, D.

Since, then, the least numbers of those which have the same ratio measure those which have the same ratio the same number of times, the greater the greater and the less the less, that is, the antecedent the antecedent and the consequent the consequent, [:ref:`VII.20 <VII.20>`] therefore C measures A the same number of times that D measures B.

Now, as many times as C measures A, so many units let there be in E.

Therefore D also measures B according to the units in E.

And, since C measures A according to the units in E, therefore E also measures A according to the units in C. [:ref:`VII.16 <VII.16>`]

For the same reason E also measures B according to the units in D. [:ref:`VII.16 <VII.16>`]

Therefore E measures A, B which are prime to one another: which is impossible. [:ref:`VII.def.12 <VII.def.12>`]

Therefore there will be no numbers less than A, B which are in the same ratio with A, B.

Therefore A, B are the least of those which have the same ratio with them. Q. E. D.


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
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "VII.21" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/21/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "VII.20" -> "VII.13";
     "VII.13" -> "VII.10";
     "VII.21" -> "VII.20";
     "VII.2" -> "VII.1";
     "VII.20" -> "VII.4";
     "VII.4" -> "VII.2";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.10" -> "VII.9";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.21" -> "VII.16";
     "VII.16" -> "VII.15";
   }



Required for
------------

:ref:`IX.1`, :ref:`IX.10`, :ref:`IX.12`, :ref:`IX.13`, :ref:`IX.14`, :ref:`IX.15`, :ref:`IX.16`, :ref:`IX.17`, :ref:`IX.18`, :ref:`IX.19`, :ref:`IX.2`, :ref:`IX.3`, :ref:`IX.32`, :ref:`IX.36`, :ref:`IX.4`, :ref:`IX.5`, :ref:`IX.6`, :ref:`IX.8`, :ref:`IX.9`, :ref:`VII.24`, :ref:`VII.25`, :ref:`VII.26`, :ref:`VII.27`, :ref:`VII.30`, :ref:`VII.33`, :ref:`VII.34`, :ref:`VII.36`, :ref:`VII.39`, :ref:`VIII.1`, :ref:`VIII.14`, :ref:`VIII.15`, :ref:`VIII.16`, :ref:`VIII.17`, :ref:`VIII.2`, :ref:`VIII.20`, :ref:`VIII.21`, :ref:`VIII.22`, :ref:`VIII.23`, :ref:`VIII.24`, :ref:`VIII.25`, :ref:`VIII.26`, :ref:`VIII.27`, :ref:`VIII.3`, :ref:`VIII.4`, :ref:`VIII.5`, :ref:`VIII.6`, :ref:`VIII.7`, :ref:`VIII.8`, :ref:`VIII.9`, :ref:`X.10`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.12`, :ref:`X.13`, :ref:`X.17`, :ref:`X.18`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.29`, :ref:`X.30`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.51`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.9`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`