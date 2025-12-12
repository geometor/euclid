:order: 3
:number: 380
:type: prop
:dependencies: X.2




.. picture:: X.3.graphic.inverted.png

.. _X.3:

X.3
===

   Given two commensurable magnitudes, to find their greatest common measure.

Let the two given commensurable magnitudes be AB, CD of which AB is the less; thus it is required to find the greatest common measure of AB, CD.

Now the magnitude AB either measures CD or it does not.

If then it measures it—and it measures itself also—AB is a common measure of AB, CD.

And it is manifest that it is also the greatest; for a greater magnitude than the magnitude AB will not measure AB.

Next, let AB not measure CD.

Then, if the less be continually subtracted in turn from the greater, that which is left over will sometime measure the one before it, because AB, CD are not incommensurable; [cf. :ref:`X.2 <X.2>`] let AB, measuring ED, leave EC less than itself, let EC, measuring FB, leave AF less than itself, and let AF measure CE.

Since, then, AF measures CE, while CE measures FB, therefore AF will also measure FB.

But it measures itself also; therefore AF will also measure the whole AB.

But AB measures DE; therefore AF will also measure ED.

But it measures CE also; therefore it also measures the whole CD.

Therefore AF is a common measure of AB, CD.

I say next that it is also the greatest.

For, if not, there will be some magnitude greater than AF which will measure AB, CD.

Let it be G.

Since then G measures AB, while AB measures ED, therefore G will also measure ED.

But it measures the whole CD also; therefore G will also measure the remainder CE.

But CE measures FB; therefore G will also measure FB.

But it measures the whole AB also, and it will therefore measure the remainder AF, the greater the less: which is impossible.

Therefore no magnitude greater than AF will measure AB, CD; therefore AF is the greatest common measure of AB, CD.

Therefore the greatest common measure of the two given commensurable magnitudes AB, CD has been found. Q. E. D.


.. _X.3.p.1:


**X.3.p.1**


From this it is manifest that, if a magnitude measure two magnitudes, it will also measure their greatest common measure.

PORISM.

From this it is manifest that, if a magnitude measure two magnitudes, it will also measure their greatest common measure.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "X.2" [fillcolor="#222244", URL="/heath/X/2/", target="_top"];
     "X.def.1" [fillcolor="#224422", URL="/heath/X/def.1/", target="_top"];
     "X.3" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/X/3/", target="_top"];
     "X.3" -> "X.2";
     "X.2" -> "X.def.1";
   }



Required for
------------

:ref:`X.4`