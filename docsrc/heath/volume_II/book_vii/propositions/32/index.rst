:canonical_id: VII.32
:volume: II
:book: VII
:proposition: 32
:type: proposition
:title: Proposition VII.32
:folios: 0339
:pages: 333
:dependencies: VII.31

.. _VII.32:

.. folio:: 0339
   :page: 333

PROPOSITION 32.
===============

.. enunciation::

   Any number either is prime or is measured by some prime number.

Let :g:`A <0339.g1:A>` be a number;

I say that :g:`A <0339.g1:A>` either is prime or is measured by some prime number.

.. subclause::

   If now :g:`A <0339.g1:A>` is prime, that which was enjoined will have been done.

.. picture:: 0339.g1.svg
   :alt: Proposition 32 diagram

.. subclause:: [VII. 31] <VII.31>

   But if it is composite, some prime number will measure it.

.. assertion::

   Therefore any number either is prime or is measured by some prime number.

.. qed::

   :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "VII.31" [label="VII.31", fillcolor="#222244", tooltip="VII.31: Any composite number is measured by some prime number.", URL="../31/index.html", target="_top"];
     "VII.32" [label="VII.32", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.32: Any number either is prime or is measured by some prime number.", URL="index.html", target="_top"];
     "VII.32" -> "VII.31";
   }
