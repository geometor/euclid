:order: 2
:number: 273
:type: prop
:dependencies: VII.1




.. picture:: VII.2.graphic.inverted.png

.. _VII.2:

VII.2
=====

   Given two numbers not prime to one another, to find their greatest common measure.

Let AB, CD be the two given numbers not prime to one another.

Thus it is required to find the greatest common measure of AB, CD.

If now CD measures AB—and it also measures itself—CD is a common measure of CD, AB.

And it is manifest that it is also the greatest; for no greater number than CD will measure CD.

But, if CD does not measure AB, then, the less of the numbers AB, CD being continually subtracted from the greater, some number will be left which will measure the one before it.

For an unit will not be left; otherwise AB, CD will be prime to one another [:ref:`VII.1 <VII.1>`], which is contrary to the hypothesis.

Therefore some number will be left which will measure the one before it.

Now let CD, measuring BE, leave EA less than itself, let EA, measuring DF, leave FC less than itself, and let CF measure AE.

Since then, CF measures AE, and AE measures DF, therefore CF will also measure DF.

But it also measures itself; therefore it will also measure the whole CD.

But CD measures BE; therefore CF also measures BE.

But it also measures EA; therefore it will also measure the whole BA.

But it also measures CD; therefore CF measures AB, CD.

Therefore CF is a common measure of AB, CD.

I say next that it is also the greatest.

For, if CF is not the greatest common measure of AB, CD, some number which is greater than CF will measure the numbers AB, CD.

Let such a number measure them, and let it be G.

Now, since G measures CD, while CD measures BE, G also measures BE.

But it also measures the whole BA; therefore it will also measure the remainder AE.

But AE measures DF; therefore G will also measure DF.

But it also measures the whole DC; therefore it will also measure the remainder CF, that is, the greater will measure the less: which is impossible.

Therefore no number which is greater than CF will measure the numbers AB, CD;


.. container:: center

   therefore CF is the greatest common measure of AB, CD.



.. _VII.2.p.1:


**VII.2.p.1**


From this it is manifest that, if a number measure two numbers, it will also measure their greatest common measure.

PORISM.

From this it is manifest that, if a number measure two numbers, it will also measure their greatest common measure.

Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.2" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/2/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.2" -> "VII.1";
     "VII.1" -> "VII.def.12";
   }



Required for
------------

:ref:`IX.1`, :ref:`IX.10`, :ref:`IX.12`, :ref:`IX.13`, :ref:`IX.14`, :ref:`IX.15`, :ref:`IX.16`, :ref:`IX.17`, :ref:`IX.18`, :ref:`IX.19`, :ref:`IX.2`, :ref:`IX.3`, :ref:`IX.32`, :ref:`IX.36`, :ref:`IX.4`, :ref:`IX.5`, :ref:`IX.6`, :ref:`IX.8`, :ref:`IX.9`, :ref:`VII.20`, :ref:`VII.21`, :ref:`VII.24`, :ref:`VII.25`, :ref:`VII.26`, :ref:`VII.27`, :ref:`VII.3`, :ref:`VII.30`, :ref:`VII.33`, :ref:`VII.34`, :ref:`VII.36`, :ref:`VII.39`, :ref:`VII.4`, :ref:`VIII.1`, :ref:`VIII.14`, :ref:`VIII.15`, :ref:`VIII.16`, :ref:`VIII.17`, :ref:`VIII.2`, :ref:`VIII.20`, :ref:`VIII.21`, :ref:`VIII.22`, :ref:`VIII.23`, :ref:`VIII.24`, :ref:`VIII.25`, :ref:`VIII.26`, :ref:`VIII.27`, :ref:`VIII.3`, :ref:`VIII.4`, :ref:`VIII.5`, :ref:`VIII.6`, :ref:`VIII.7`, :ref:`VIII.8`, :ref:`VIII.9`, :ref:`X.10`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.12`, :ref:`X.13`, :ref:`X.17`, :ref:`X.18`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.29`, :ref:`X.30`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.51`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.9`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`