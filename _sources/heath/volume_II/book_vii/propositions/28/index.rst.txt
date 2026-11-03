:canonical_id: VII.28
:volume: II
:book: VII
:proposition: 28
:type: proposition
:title: Proposition VII.28
:folios: 0335, 0336
:pages: 329, 330
:dependencies: VII.def.2, VII.def.12

.. _VII.28:

.. folio:: 0335
   :page: 329

PROPOSITION 28.
===============

.. enunciation::

   If two :term:`numbers <number>` be :term:`prime to one another <prime-to-one-another>`, the sum will also be prime to each of them ; and, if the sum of two numbers be prime to any one of them, the original numbers will also be prime to one another.

For let two numbers :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />` prime to one another be added ;

I say that the sum :g:`AC <0335.g1:/ A C />` is also prime to each of the numbers :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />`.

.. picture:: 0335.g1.svg
   :alt: Book VII, Proposition 28

.. subclause::

   For, if :g:`CA <0335.g1:/ A C />`, :g:`AB <0335.g1:/ A B />` are not prime to one another, some number will :term:`measure <part-aliquot>` :g:`CA <0335.g1:/ A C />`, :g:`AB <0335.g1:/ A B />`.

Let a number measure them, and let it be :g:`D <0335.g1:D>`.

.. subclause::

   Since then :g:`D <0335.g1:D>` measures :g:`CA <0335.g1:/ A C />`, :g:`AB <0335.g1:/ A B />`,

.. assertion::

   therefore it will also measure the remainder :g:`BC <0335.g1:/ B C />`.

.. subclause::

   But it also measures :g:`BA <0335.g1:/ A B />` ;

.. assertion::

   therefore :g:`D <0335.g1:D>` measures :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />` which are prime to one another : which is impossible. :just:`[VII. Def. 12] <VII.def.12>`

.. assertion::

   Therefore no number will measure the numbers :g:`CA <0335.g1:/ A C />`, :g:`AB <0335.g1:/ A B />` ; therefore :g:`CA <0335.g1:/ A C />`, :g:`AB <0335.g1:/ A B />` are prime to one another.

.. subclause::

   For the same reason

.. assertion::

   :g:`AC <0335.g1:/ A C />`, :g:`CB <0335.g1:/ B C />` are also prime to one another.

.. assertion::

   Therefore :g:`CA <0335.g1:/ A C />` is prime to each of the numbers :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />`.

Again, let :g:`CA <0335.g1:/ A C />`, :g:`AB <0335.g1:/ A B />` be prime to one another ;

I say that :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />` are also prime to one another.

.. subclause::

   For, if :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />` are not prime to one another, some number will measure :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />`.

.. _folio-ii-0336:

.. folio:: 0336
   :page: 330

Let a number measure them, and let it be :g:`D <0335.g1:D>`.

.. subclause::

   Now, since :g:`D <0335.g1:D>` measures each of the numbers :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />`,

.. assertion::

   it will also measure the whole :g:`CA <0335.g1:/ A C />`.

.. subclause::

   But it also measures :g:`AB <0335.g1:/ A B />` ;

.. assertion::

   therefore :g:`D <0335.g1:D>` measures :g:`CA <0335.g1:/ A C />`, :g:`AB <0335.g1:/ A B />` which are prime to one another : which is impossible. :just:`[VII. Def. 12] <VII.def.12>`

.. assertion::

   Therefore no number will measure the numbers :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />`.

.. assertion::

   Therefore :g:`AB <0335.g1:/ A B />`, :g:`BC <0335.g1:/ B C />` are prime to one another.

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
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../definitions/index.html#vii-def-12", target="_top"];
     "VII.28" [label="VII.28", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.28: If two numbers be prime to one another, the sum will also be prime to each of them ; and, if the sum of two numbers be prime to any one of them, the original numbers will also be…", URL="index.html", target="_top"];
     "VII.def.12" -> "V.def.1";
     "VII.def.2" -> "VII.def.1";
     "VII.def.12" -> "VII.def.1";
     "VII.28" -> "VII.def.2";
     "VII.28" -> "VII.def.12";
   }

Required for
------------

:ref:`IX.15 <IX.15>`

----

See :ref:`Commentary on Proposition VII.28 <VII.28.commentary>`.

.. toctree::
   :hidden:

   commentary
