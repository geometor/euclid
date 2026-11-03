:canonical_id: VII.7
:volume: II
:book: VII
:proposition: 7
:type: proposition
:title: Proposition VII.7
:folios: 0312, 0313
:pages: 306, 307
:dependencies: VII.def.2, VII.def.3, VII.5

.. _VII.7:

.. folio:: 0312
   :page: 306

PROPOSITION 7.
==============

.. enunciation::

   If a :term:`number <number>` be that :term:`part of <part-aliquot>` a number, which a number subtracted is of a number subtracted, the remainder will also be the same part of the remainder that the whole is of the whole.

For let the number :g:`AB <0312.g1:/ A B />` be that part of the number :g:`CD <0312.g1:/ C D />` which :g:`AE <0312.g1:/ A E />` subtracted is of :g:`CF <0312.g1:/ C F />` subtracted;

I say that the remainder :g:`EB <0312.g1:/ E B />` is also the same part of the remainder :g:`FD <0312.g1:/ F D />` that the whole :g:`AB <0312.g1:/ A B />` is of the whole :g:`CD <0312.g1:/ C D />`.

.. picture:: 0312.g1.svg
   :alt: Book VII, Proposition 7

For, whatever part :g:`AE <0312.g1:/ A E />` is of :g:`CF <0312.g1:/ C F />`, the same part also let :g:`EB <0312.g1:/ E B />` be of :g:`CG <0312.g1:/ G C />`.

.. subclause::

   Now since, whatever part :g:`AE <0312.g1:/ A E />` is of :g:`CF <0312.g1:/ C F />`, the same part also is :g:`EB <0312.g1:/ E B />` of :g:`CG <0312.g1:/ G C />`,

.. assertion::

   therefore, whatever part :g:`AE <0312.g1:/ A E />` is of :g:`CF <0312.g1:/ C F />`, the same part also is :g:`AB <0312.g1:/ A B />` of :g:`GF <0312.g1:/ G F />`. :just:`[VII. 5] <VII.5>`

.. subclause::

   But, whatever part :g:`AE <0312.g1:/ A E />` is of :g:`CF <0312.g1:/ C F />`, the same part also, by hypothesis, is :g:`AB <0312.g1:/ A B />` of :g:`CD <0312.g1:/ C D />`;

.. assertion::

   therefore, whatever part :g:`AB <0312.g1:/ A B />` is of :g:`GF <0312.g1:/ G F />`, the same part is it of :g:`CD <0312.g1:/ C D />` also;

.. assertion::

   therefore :g:`GF <0312.g1:/ G F />` is :eq:`equal <0312.g1:/ G F / = 0312.g1:/ C D />` to :g:`CD <0312.g1:/ C D />`.

Let :g:`CF <0312.g1:/ C F />` be subtracted from each;

.. assertion::

   therefore the remainder :g:`GC <0312.g1:/ G C />` is :eq:`equal <0312.g1:/ G C / = 0312.g1:/ F D />` to the remainder :g:`FD <0312.g1:/ F D />`.

.. subclause::

   Now since, whatever part :g:`AE <0312.g1:/ A E />` is of :g:`CF <0312.g1:/ C F />`, the same part also is :g:`EB <0312.g1:/ E B />` of :g:`GC <0312.g1:/ G C />`, while :g:`GC <0312.g1:/ G C />` is :eq:`equal <0312.g1:/ G C / = 0312.g1:/ F D />` to :g:`FD <0312.g1:/ F D />`,

.. assertion::

   therefore, whatever part :g:`AE <0312.g1:/ A E />` is of :g:`CF <0312.g1:/ C F />`, the same part also is :g:`EB <0312.g1:/ E B />` of :g:`FD <0312.g1:/ F D />`.

.. subclause::

   But, whatever part :g:`AE <0312.g1:/ A E />` is of :g:`CF <0312.g1:/ C F />`, the same part also is :g:`AB <0312.g1:/ A B />` of :g:`CD <0312.g1:/ C D />`;

.. _folio-ii-0313:

.. folio:: 0313
   :page: 307

.. assertion::

   therefore also the remainder :g:`EB <0312.g1:/ E B />` is the same part of the remainder :g:`FD <0312.g1:/ F D />` that the whole :g:`AB <0312.g1:/ A B />` is of the whole :g:`CD <0312.g1:/ C D />`.

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
     "V.def.2" [label="V.def.2", fillcolor="#224422", tooltip="V.def.2: The greater is a multiple of the less when it is measured by the less.", URL="../../../book_v/definitions/index.html#v-def-2", target="_top"];
     "VII.def.1" [label="VII.def.1", fillcolor="#224422", tooltip="VII.def.1: An unit is that by virtue of which each of the things that exist is called one.", URL="../../definitions/index.html#vii-def-1", target="_top"];
     "VII.def.2" [label="VII.def.2", fillcolor="#224422", tooltip="VII.def.2: A number is a multitude composed of units.", URL="../../definitions/index.html#vii-def-2", target="_top"];
     "VII.def.3" [label="VII.def.3", fillcolor="#224422", tooltip="VII.def.3: A number is a part of a number, the less of the greater, when it measures the greater.", URL="../../definitions/index.html#vii-def-3", target="_top"];
     "VII.def.5" [label="VII.def.5", fillcolor="#224422", tooltip="VII.def.5: The greater number is a multiple of the less when it is measured by the less.", URL="../../definitions/index.html#vii-def-5", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../05/index.html", target="_top"];
     "VII.7" [label="VII.7", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.7: If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder will also be the same part of the remainder that the whole is of the whole.", URL="index.html", target="_top"];
     "V.def.2" -> "V.def.1";
     "VII.def.3" -> "V.def.1";
     "VII.def.5" -> "V.def.1";
     "VII.5" -> "V.def.2";
     "VII.def.2" -> "VII.def.1";
     "VII.def.3" -> "VII.def.2";
     "VII.def.5" -> "VII.def.2";
     "VII.5" -> "VII.def.2";
     "VII.7" -> "VII.def.2";
     "VII.5" -> "VII.def.3";
     "VII.7" -> "VII.def.3";
     "VII.5" -> "VII.def.5";
     "VII.7" -> "VII.5";
   }

Required for
------------

:ref:`VII.8 <VII.8>`, :ref:`VII.11 <VII.11>`, :ref:`IX.35 <IX.35>`, :ref:`IX.36 <IX.36>`

----

See :ref:`Commentary on Proposition VII.7 <VII.7.commentary>`.

.. toctree::
   :hidden:

   commentary
