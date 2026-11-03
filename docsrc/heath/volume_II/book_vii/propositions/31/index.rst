:canonical_id: VII.31
:volume: II
:book: VII
:proposition: 31
:type: proposition
:title: Proposition VII.31
:folios: 0338, 0339
:pages: 332, 333
:dependencies: V.def.1, VII.def.11, VII.def.13

.. _VII.31:

.. folio:: 0338
   :page: 332

PROPOSITION 31.
===============

.. enunciation::

   Any :term:`composite number <composite-number>` is :term:`measured <part-aliquot>` by some :term:`prime number <prime-number>`.

Let :g:`A <0338.g1:A>` be a composite number;

I say that :g:`A <0338.g1:A>` is measured by some prime number.

.. subclause::

   For, since :g:`A <0338.g1:A>` is composite, some :term:`number <number>` will measure it.

Let a number measure it, and let it be :g:`B <0338.g1:B>`.

.. picture:: 0338.g1.svg
   :alt: Proposition 31 diagram

.. subclause::

   Now, if :g:`B <0338.g1:B>` is prime, what was enjoined will have been done.\ [#f1]_

.. subclause::

   But if it is composite, some number will measure it.

Let a number measure it, and let it be :g:`C <0338.g1:C>`.

.. subclause::

   Then, since :g:`C <0338.g1:C>` measures :g:`B <0338.g1:B>`, and :g:`B <0338.g1:B>` measures :g:`A <0338.g1:A>`,

.. assertion::

   therefore :g:`C <0338.g1:C>` also measures :g:`A <0338.g1:A>`.

.. subclause::

   And, if :g:`C <0338.g1:C>` is prime, what was enjoined will have been done.

.. subclause::

   But if it is composite, some number will measure it.

.. assertion::

   Thus, if the investigation be continued in this way, some prime number will be found which will measure\ [#f2]_ the number before it, which will also measure :g:`A <0338.g1:A>`.

.. subclause::

   For, if it is not found, an infinite series of numbers will measure the number :g:`A <0338.g1:A>`, each of which is less than the other: which is impossible in numbers.

.. assertion::

   Therefore some prime number will be found which will measure the one before it, which will also measure :g:`A <0338.g1:A>`.

.. assertion::

   Therefore any composite number is measured by some prime number.

.. [#f1] **if** :g:`B <0338.g1:B>` **is prime, what was enjoined will have been done**, *i.e.* the implied *problem* of finding a prime number which measures :g:`A <0338.g1:A>`.

.. [#f2] **some prime number will be found which will measure.** In the Greek the sentence stops here, but it is necessary to add the words "the number before it, which will also measure :g:`A <0338.g1:A>`," which are found a few lines further down. It is possible that the words may have fallen out of P here by a simple mistake due to ὁμοιοτέλευτον (:person:`Heiberg <heiberg>`).

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
     "VII.31" [label="VII.31", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.31: Any composite number is measured by some prime number.", URL="index.html", target="_top"];
     "VII.def.11" -> "V.def.1";
     "VII.def.13" -> "V.def.1";
     "VII.31" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.11" -> "VII.def.1";
     "VII.def.13" -> "VII.def.2";
     "VII.31" -> "VII.def.11";
     "VII.31" -> "VII.def.13";
   }

Required for
------------

:ref:`VII.32 <VII.32>`, :ref:`IX.13 <IX.13>`, :ref:`IX.20 <IX.20>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`

----

See :ref:`Commentary on Proposition VII.31 <VII.31.commentary>`.

.. toctree::
   :hidden:

   commentary
