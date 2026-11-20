:canonical_id: IX.20
:volume: II
:book: IX
:proposition: 20
:type: proposition
:title: Proposition IX.20
:folios: 0418
:folio: 0418
:page: 412
:pages: 412
:dependencies: VII.def.11, VII.31

.. _IX.20:

.. folio:: 0418
   :page: 412

PROPOSITION 20.
===============

.. enunciation::

   :term:`Prime numbers <prime-number>` are more than any assigned multitude of prime numbers.

Let :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>` be the assigned prime numbers ;

I say that there are more prime numbers than :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>`.

For let the least :term:`number <number>` :term:`measured <part-aliquot>` by :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>` be taken, and let it be :g:`DE <0418.g1:/ D E />` ; let the :term:`unit <unit>` :g:`DF <0418.g1:/ D F />` be added to :g:`DE <0418.g1:/ D E />`.

.. picture:: 0418.g1.svg
   :alt: Book IX, Proposition 20

Then :g:`EF <0418.g1:/ E F />` is either prime or not.

First, let it be prime ;

.. assertion::

   then the prime numbers :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>`, :g:`EF <0418.g1:/ E F />` have been found which are more than :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>`.

Next, let :g:`EF <0418.g1:/ E F />` not be prime ;

.. assertion:: [VII. 31] <VII.31>

   therefore it is measured by some prime number.

Let it be measured by the prime number :g:`G <0418.g1:G>`.

I say that :g:`G <0418.g1:G>` is not the same with any of the numbers :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>`.

For, if possible, let it be so.

.. subclause::

   Now :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>` measure :g:`DE <0418.g1:/ D E />` ;

.. assertion::

   therefore :g:`G <0418.g1:G>` also will measure :g:`DE <0418.g1:/ D E />`.

.. subclause::

   But it also measures :g:`EF <0418.g1:/ E F />`.

.. assertion::

   Therefore :g:`G <0418.g1:G>`, being a number, will measure the remainder, the unit :g:`DF <0418.g1:/ D F />` : which is absurd.

.. assertion::

   Therefore :g:`G <0418.g1:G>` is not the same with any one of the numbers :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>`.

.. subclause::

   And by hypothesis it is prime.

.. assertion::

   Therefore the prime numbers :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>`, :g:`G <0418.g1:G>` have been found which are more than the assigned multitude of :g:`A <0418.g1:A>`, :g:`B <0418.g1:B>`, :g:`C <0418.g1:C>`.

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
     "VII.def.1" [label="VII.def.1", fillcolor="#224422", tooltip="VII.def.1: An unit is that by virtue of which each of the things that exist is called one.", URL="../../../book_vii/definitions/index.html#vii-def-1", target="_top"];
     "VII.def.2" [label="VII.def.2", fillcolor="#224422", tooltip="VII.def.2: A number is a multitude composed of units.", URL="../../../book_vii/definitions/index.html#vii-def-2", target="_top"];
     "VII.def.11" [label="VII.def.11", fillcolor="#224422", tooltip="VII.def.11: A prime number is that which is measured by an unit alone.", URL="../../../book_vii/definitions/index.html#vii-def-11", target="_top"];
     "VII.def.13" [label="VII.def.13", fillcolor="#224422", tooltip="VII.def.13: A composite number is that which is measured by some number.", URL="../../../book_vii/definitions/index.html#vii-def-13", target="_top"];
     "VII.31" [label="VII.31", fillcolor="#222244", tooltip="VII.31: Any composite number is measured by some prime number.", URL="../../../book_vii/propositions/31/index.html", target="_top"];
     "IX.20" [label="IX.20", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.20: Prime numbers are more than any assigned multitude of prime numbers.", URL="index.html", target="_top"];
     "VII.def.11" -> "V.def.1";
     "VII.def.13" -> "V.def.1";
     "VII.31" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.11" -> "VII.def.1";
     "VII.def.13" -> "VII.def.2";
     "VII.31" -> "VII.def.11";
     "IX.20" -> "VII.def.11";
     "VII.31" -> "VII.def.13";
     "IX.20" -> "VII.31";
   }

----

See :ref:`Commentary on Proposition IX.20 <IX.20.commentary>`.

.. toctree::
   :hidden:

   commentary
