:order: 3
:number: 274
:type: prop
:dependencies: VII.2, VII.2.p.1




.. picture:: VII.3.graphic.inverted.png

.. _VII.3:

VII.3
=====

   Given three numbers not prime to one another, to find their greatest common measure.

Let A, B, C be the three given numbers not prime to one another; thus it is required to find the greatest common measure of A, B, C.

For let the greatest common measure, D, of the two numbers A, B be taken; [:ref:`VII.2 <VII.2>`] then D either measures, or does not measure, C.

First, let it measure it.

But it measures A, B also; therefore D measures A, B, C; therefore D is a common measure of A, B, C.

I say that it is also the greatest.

For, if D is not the greatest common measure of A, B, C, some number which is greater than D will measure the numbers A, B, C.

Let such a number measure them, and let it be E.

Since then E measures A, B, C, it will also measure A, B; therefore it will also measure the greatest common measure of A, B. [:ref:`VII.2.p.1 <VII.2.p.1>`]

But the greatest common measure of A, B is D; therefore E measures D, the greater the less: which is impossible.

Therefore no number which is greater than D will measure the numbers A, B, C;


.. container:: center

   therefore D is the greatest common measure of A, B, C.


Next, let D not measure C; I say first that C, D are not prime to one another.

For, since A, B, C are not prime to one another, some number will measure them.

Now that which measures A, B, C will also measure A, B, and will measure D, the greatest common measure of A, B. [:ref:`VII.2.p.1 <VII.2.p.1>`]

But it measures C also; therefore some number will measure the numbers D, C; therefore D, C are not prime to one another.

Let then their greatest common measure E be taken. [:ref:`VII.2 <VII.2>`]

Then, since E measures D, and D measures A, B, therefore E also measures A, B.

But it measures C also; therefore E measures A, B, C; therefore E is a common measure of A, B, C.

I say next that it is also the greatest.

For, if E is not the greatest common measure of A, B, C, some number which is greater than E will measure the numbers A, B, C.

Let such a number measure them, and let it be F.

Now, since F measures A, B, C, it also measures A, B; therefore it will also measure the greatest common measure of A, B. [:ref:`VII.2.p.1 <VII.2.p.1>`]

But the greatest common measure of A, B is D; therefore F measures D.

And it measures C also; therefore F measures D, C; therefore it will also measure the greatest common measure of D, C. [:ref:`VII.2.p.1 <VII.2.p.1>`]

But the greatest common measure of D, C is E; therefore F measures E, the greater the less: which is impossible.

Therefore no number which is greater than E will measure the numbers A, B, C; therefore E is the greatest common measure of A, B, C. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.3" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/3/", target="_top"];
     "VII.2.p.1" [fillcolor="#333333"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.3" -> "VII.2.p.1";
     "VII.3" -> "VII.2";
     "VII.2" -> "VII.1";
     "VII.1" -> "VII.def.12";
   }



Required for
------------

:ref:`IX.1`, :ref:`IX.10`, :ref:`IX.12`, :ref:`IX.13`, :ref:`IX.2`, :ref:`IX.3`, :ref:`IX.32`, :ref:`IX.36`, :ref:`IX.4`, :ref:`IX.5`, :ref:`IX.6`, :ref:`IX.8`, :ref:`IX.9`, :ref:`VII.33`, :ref:`VII.34`, :ref:`VII.36`, :ref:`VII.39`, :ref:`VIII.14`, :ref:`VIII.15`, :ref:`VIII.16`, :ref:`VIII.17`, :ref:`VIII.20`, :ref:`VIII.21`, :ref:`VIII.22`, :ref:`VIII.23`, :ref:`VIII.24`, :ref:`VIII.25`, :ref:`VIII.26`, :ref:`VIII.27`, :ref:`VIII.3`, :ref:`VIII.4`, :ref:`VIII.5`, :ref:`VIII.6`, :ref:`VIII.7`, :ref:`VIII.8`, :ref:`X.10`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.12`, :ref:`X.13`, :ref:`X.17`, :ref:`X.18`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.29`, :ref:`X.30`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.51`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.9`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`