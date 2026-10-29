:canonical_id: VII.2
:volume: II
:book: VII
:proposition: 2
:type: proposition
:title: Proposition VII.2
:folios: 0304, 0305
:pages: 298, 299
:dependencies: VII.1

.. _VII.2:

.. _folio-ii-0304:

.. folio:: 0304
   :page: 298

PROPOSITION 2.
==============

.. enunciation::

   Given two numbers not prime to one another, to find their greatest common measure.

Let :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />` be the two given numbers not prime to one another.

Thus it is required to find the greatest common measure of :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />`.

If now :g:`CD <0304.g1:/ C D />` measures :g:`AB <0304.g1:/ A B />`—and it also measures itself—:g:`CD <0304.g1:/ C D />` is a common measure of :g:`CD <0304.g1:/ C D />`, :g:`AB <0304.g1:/ A B />`.

And it is manifest that it is also the greatest; for no greater number than :g:`CD <0304.g1:/ C D />` will measure :g:`CD <0304.g1:/ C D />`.

.. picture:: 0304.g1.svg
   :alt: Proposition 2 Diagram

But, if :g:`CD <0304.g1:/ C D />` does not measure :g:`AB <0304.g1:/ A B />`, then, the less of the numbers :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />` being continually subtracted from the greater, some number will be left which will measure the one before it.

.. subclause::

   For an unit will not be left; otherwise :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />` will be prime to one another :just:`[VII. 1] <VII.1>`, which is contrary to the hypothesis.

.. assertion::

   Therefore some number will be left which will measure the one before it.

Now let :g:`CD <0304.g1:/ C D />`, measuring :g:`BE <0304.g1:/ E B />`, leave :g:`EA <0304.g1:/ A E />` less than itself, let :g:`EA <0304.g1:/ A E />`, measuring :g:`DF <0304.g1:/ F D />`, leave :g:`FC <0304.g1:/ C F />` less than itself, and let :g:`CF <0304.g1:/ C F />` measure :g:`AE <0304.g1:/ A E />`.

.. subclause::

   Since then, :g:`CF <0304.g1:/ C F />` measures :g:`AE <0304.g1:/ A E />`, and :g:`AE <0304.g1:/ A E />` measures :g:`DF <0304.g1:/ F D />`,

.. assertion::

   therefore :g:`CF <0304.g1:/ C F />` will also measure :g:`DF <0304.g1:/ F D />`.

.. subclause::

   But it also measures itself;

.. assertion::

   therefore it will also measure the whole :g:`CD <0304.g1:/ C D />`.

.. subclause::

   But :g:`CD <0304.g1:/ C D />` measures :g:`BE <0304.g1:/ E B />`;

.. assertion::

   therefore :g:`CF <0304.g1:/ C F />` also measures :g:`BE <0304.g1:/ E B />`.

.. subclause::

   But it also measures :g:`EA <0304.g1:/ A E />`;

.. assertion::

   therefore it will also measure the whole :g:`BA <0304.g1:/ A B />`.

.. subclause::

   But it also measures :g:`CD <0304.g1:/ C D />`;

.. assertion::

   therefore :g:`CF <0304.g1:/ C F />` measures :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />`.

.. assertion::

   Therefore :g:`CF <0304.g1:/ C F />` is a common measure of :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />`.

.. _folio-ii-0305:

.. folio:: 0305
   :page: 299

I say next that it is also the greatest.

For, if :g:`CF <0304.g1:/ C F />` is not the greatest common measure of :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />`, some number which is greater than :g:`CF <0304.g1:/ C F />` will measure the numbers :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />`.

Let such a number measure them, and let it be :g:`G <0304.g1:G>`.

.. subclause::

   Now, since :g:`G <0304.g1:G>` measures :g:`CD <0304.g1:/ C D />`, while :g:`CD <0304.g1:/ C D />` measures :g:`BE <0304.g1:/ E B />`,

.. assertion::

   :g:`G <0304.g1:G>` also measures :g:`BE <0304.g1:/ E B />`.

.. subclause::

   But it also measures the whole :g:`BA <0304.g1:/ A B />`;

.. assertion::

   therefore it will also measure the remainder :g:`AE <0304.g1:/ A E />`.

.. subclause::

   But :g:`AE <0304.g1:/ A E />` measures :g:`DF <0304.g1:/ F D />`;

.. assertion::

   therefore :g:`G <0304.g1:G>` will also measure :g:`DF <0304.g1:/ F D />`.

.. subclause::

   But it also measures the whole :g:`DC <0304.g1:/ C D />`;

.. assertion::

   therefore it will also measure the remainder :g:`CF <0304.g1:/ C F />`, that is, the greater will measure the less: which is impossible.

.. assertion::

   Therefore no number which is greater than :g:`CF <0304.g1:/ C F />` will measure the numbers :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />`; therefore :g:`CF <0304.g1:/ C F />` is the greatest common measure of :g:`AB <0304.g1:/ A B />`, :g:`CD <0304.g1:/ C D />`.

.. assertion::

   PORISM. From this it is manifest that, if a number measure two numbers, it will also measure their greatest common measure.

.. qed::

   Q. E. D.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../definitions/index.html#vii-def-12", target="_top"];
     "VII.1" [label="VII.1", fillcolor="#222244", tooltip="VII.1: Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit…", URL="../01/index.html", target="_top"];
     "VII.2" [label="VII.2", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.2: Given two numbers not prime to one another, to find their greatest common measure.", URL="index.html", target="_top"];
     "VII.1" -> "VII.def.12";
     "VII.2" -> "VII.1";
   }

Required for
------------

:ref:`VII.3 <VII.3>`, :ref:`VII.4 <VII.4>`, :ref:`VII.20 <VII.20>`, :ref:`VII.21 <VII.21>`, :ref:`VII.24 <VII.24>`, :ref:`VII.25 <VII.25>`, :ref:`VII.26 <VII.26>`, :ref:`VII.27 <VII.27>`, :ref:`VII.30 <VII.30>`, :ref:`VII.33 <VII.33>`, :ref:`VII.34 <VII.34>`, :ref:`VII.36 <VII.36>`, :ref:`VII.39 <VII.39>`, :ref:`VIII.1 <VIII.1>`, :ref:`VIII.2 <VIII.2>`, :ref:`VIII.3 <VIII.3>`, :ref:`VIII.4 <VIII.4>`, :ref:`VIII.5 <VIII.5>`, :ref:`VIII.6 <VIII.6>`, :ref:`VIII.7 <VIII.7>`, :ref:`VIII.8 <VIII.8>`, :ref:`VIII.9 <VIII.9>`, :ref:`VIII.14 <VIII.14>`, :ref:`VIII.15 <VIII.15>`, :ref:`VIII.16 <VIII.16>`, :ref:`VIII.17 <VIII.17>`, :ref:`VIII.20 <VIII.20>`, :ref:`VIII.21 <VIII.21>`, :ref:`VIII.22 <VIII.22>`, :ref:`VIII.23 <VIII.23>`, :ref:`VIII.24 <VIII.24>`, :ref:`VIII.25 <VIII.25>`, :ref:`VIII.26 <VIII.26>`, :ref:`VIII.27 <VIII.27>`, :ref:`IX.1 <IX.1>`, :ref:`IX.2 <IX.2>`, :ref:`IX.3 <IX.3>`, :ref:`IX.4 <IX.4>`, :ref:`IX.5 <IX.5>`, :ref:`IX.6 <IX.6>`, :ref:`IX.8 <IX.8>`, :ref:`IX.9 <IX.9>`, :ref:`IX.10 <IX.10>`, :ref:`IX.12 <IX.12>`, :ref:`IX.13 <IX.13>`, :ref:`IX.14 <IX.14>`, :ref:`IX.15 <IX.15>`, :ref:`IX.16 <IX.16>`, :ref:`IX.17 <IX.17>`, :ref:`IX.18 <IX.18>`, :ref:`IX.19 <IX.19>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`, :ref:`X.9 <X.9>`, :ref:`X.10 <X.10>`, :ref:`X.12 <X.12>`, :ref:`X.13 <X.13>`, :ref:`X.17 <X.17>`, :ref:`X.18 <X.18>`, :ref:`X.22 <X.22>`, :ref:`X.23 <X.23>`, :ref:`X.24 <X.24>`, :ref:`X.25 <X.25>`, :ref:`X.26 <X.26>`, :ref:`X.27 <X.27>`, :ref:`X.28 <X.28>`, :ref:`X.29 <X.29>`, :ref:`X.30 <X.30>`, :ref:`X.31 <X.31>`, :ref:`X.32 <X.32>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.36 <X.36>`, :ref:`X.37 <X.37>`, :ref:`X.38 <X.38>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.42 <X.42>`, :ref:`X.43 <X.43>`, :ref:`X.44 <X.44>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.47 <X.47>`, :ref:`X.48 <X.48>`, :ref:`X.49 <X.49>`, :ref:`X.50 <X.50>`, :ref:`X.51 <X.51>`, :ref:`X.52 <X.52>`, :ref:`X.53 <X.53>`, :ref:`X.54 <X.54>`, :ref:`X.55 <X.55>`, :ref:`X.56 <X.56>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.61 <X.61>`, :ref:`X.62 <X.62>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.66 <X.66>`, :ref:`X.67 <X.67>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.73 <X.73>`, :ref:`X.75 <X.75>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.79 <X.79>`, :ref:`X.80 <X.80>`, :ref:`X.81 <X.81>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.92 <X.92>`, :ref:`X.93 <X.93>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.97 <X.97>`, :ref:`X.98 <X.98>`, :ref:`X.99 <X.99>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.103 <X.103>`, :ref:`X.104 <X.104>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`X.112 <X.112>`, :ref:`X.113 <X.113>`, :ref:`X.114 <X.114>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition VII.2 <VII.2.commentary>`.

.. toctree::
   :hidden:

   commentary
