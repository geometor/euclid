:canonical_id: VII.32
:volume: II
:book: VII
:proposition: 32
:type: proposition
:title: Proposition VII.32
:folios: 0339
:pages: 333
:dependencies: V.def.1, VII.def.2, VII.def.11, VII.31

.. _VII.32:

.. folio:: 0339
   :page: 333

PROPOSITION 32.
===============

.. enunciation::

   Any :term:`number <number>` either is :term:`prime <prime-number>` or is :term:`measured <part-aliquot>` by some prime number.

Let :g:`A <0339.g1:A>` be a number;

I say that :g:`A <0339.g1:A>` either is prime or is measured by some prime number.

.. subclause::

   If now :g:`A <0339.g1:A>` is prime, that which was enjoined will have been done.

.. picture:: 0339.g1.svg
   :alt: Proposition 32 diagram

.. subclause:: [VII. 31] <VII.31>

   But if it is :term:`composite <composite-number>`, some prime number will measure it.

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
     "V.def.1" [label="V.def.1", fillcolor="#224422", tooltip="V.def.1: A magnitude is a part of a magnitude, the less of the greater, when it measures the greater.", URL="../../../book_v/definitions/index.html#v-def-1", target="_top"];
     "VII.def.1" [label="VII.def.1", fillcolor="#224422", tooltip="VII.def.1: An unit is that by virtue of which each of the things that exist is called one.", URL="../../definitions/index.html#vii-def-1", target="_top"];
     "VII.def.2" [label="VII.def.2", fillcolor="#224422", tooltip="VII.def.2: A number is a multitude composed of units.", URL="../../definitions/index.html#vii-def-2", target="_top"];
     "VII.def.11" [label="VII.def.11", fillcolor="#224422", tooltip="VII.def.11: A prime number is that which is measured by an unit alone.", URL="../../definitions/index.html#vii-def-11", target="_top"];
     "VII.def.13" [label="VII.def.13", fillcolor="#224422", tooltip="VII.def.13: A composite number is that which is measured by some number.", URL="../../definitions/index.html#vii-def-13", target="_top"];
     "VII.31" [label="VII.31", fillcolor="#222244", tooltip="VII.31: Any composite number is measured by some prime number.", URL="../31/index.html", target="_top"];
     "VII.32" [label="VII.32", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.32: Any number either is prime or is measured by some prime number.", URL="index.html", target="_top"];
     "VII.def.11" -> "V.def.1";
     "VII.def.13" -> "V.def.1";
     "VII.31" -> "V.def.1";
     "VII.32" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.11" -> "VII.def.1";
     "VII.def.13" -> "VII.def.2";
     "VII.32" -> "VII.def.2";
     "VII.31" -> "VII.def.11";
     "VII.32" -> "VII.def.11";
     "VII.31" -> "VII.def.13";
     "VII.32" -> "VII.31";
   }
