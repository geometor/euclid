:canonical_id: VII.29
:volume: II
:book: VII
:proposition: 29
:type: proposition
:title: Proposition VII.29
:folios: 0336, 0337
:folio: 0336
:page: 330
:pages: 330, 331
:dependencies: V.def.1, VII.def.2, VII.def.11, VII.def.12

.. _VII.29:

.. folio:: 0336
   :page: 330

PROPOSITION 29.
===============

.. enunciation::

   Any :term:`prime number <prime-number>` is :term:`prime to <prime-to-one-another>` any :term:`number <number>` which it does not :term:`measure <part-aliquot>`.

Let :g:`A <0336.g1:A>` be a prime number, and let it not measure :g:`B <0336.g1:B>`;

I say that :g:`B <0336.g1:B>`, :g:`A <0336.g1:A>` are prime to one another.

.. picture:: 0336.g1.svg
   :alt: Book VII, Proposition 29

.. subclause::

   For, if :g:`B <0336.g1:B>`, :g:`A <0336.g1:A>` are not prime to one another, some number will measure them.

Let :g:`C <0336.g1:C>` measure them.

.. subclause::

   Since :g:`C <0336.g1:C>` measures :g:`B <0336.g1:B>`, and :g:`A <0336.g1:A>` does not measure :g:`B <0336.g1:B>`,

.. assertion::

   therefore :g:`C <0336.g1:C>` is not the same with :g:`A <0336.g1:A>`.

.. subclause::

   Now, since :g:`C <0336.g1:C>` measures :g:`B <0336.g1:B>`, :g:`A <0336.g1:A>`,

.. assertion::

   therefore it also measures :g:`A <0336.g1:A>` which is prime, though it is not the same with it : which is impossible.

.. _folio-ii-0337:

.. folio:: 0337
   :page: 331

.. assertion::

   Therefore no number will measure :g:`B <0336.g1:B>`, :g:`A <0336.g1:A>`.

.. assertion::

   Therefore :g:`A <0336.g1:A>`, :g:`B <0336.g1:B>` are prime to one another.

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
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../definitions/index.html#vii-def-12", target="_top"];
     "VII.29" [label="VII.29", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.29: Any prime number is prime to any number which it does not measure.", URL="index.html", target="_top"];
     "VII.def.11" -> "V.def.1";
     "VII.def.12" -> "V.def.1";
     "VII.29" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.11" -> "VII.def.1";
     "VII.def.12" -> "VII.def.1";
     "VII.29" -> "VII.def.2";
     "VII.29" -> "VII.def.11";
     "VII.29" -> "VII.def.12";
   }

Required for
------------

:ref:`VII.30 <VII.30>`, :ref:`IX.12 <IX.12>`, :ref:`IX.13 <IX.13>`, :ref:`IX.14 <IX.14>`, :ref:`IX.32 <IX.32>`, :ref:`IX.36 <IX.36>`

----

See :ref:`Commentary on Proposition VII.29 <VII.29.commentary>`.

.. toctree::
   :hidden:

   commentary
