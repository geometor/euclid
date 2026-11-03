:canonical_id: VII.11
:volume: II
:book: VII
:proposition: 11
:type: proposition
:title: Proposition VII.11
:folios: 0317
:pages: 311
:dependencies: VII.def.2, VII.def.20, VII.7, VII.8

.. _VII.11:

.. folio:: 0317
   :page: 311

PROPOSITION 11.
===============

.. enunciation::

   If, as whole is to whole, so is a :term:`number <number>` subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

As the whole :g:`AB <0317.g1:/ A B />` is to the whole :g:`CD <0317.g1:/ C D />`, so let :g:`AE <0317.g1:/ A E />` subtracted be to :g:`CF <0317.g1:/ C F />` subtracted;

I say that the remainder :g:`EB <0317.g1:/ E B />` is also to the remainder :g:`FD <0317.g1:/ F D />` as the whole :g:`AB <0317.g1:/ A B />` to the whole :g:`CD <0317.g1:/ C D />`.

.. picture:: 0317.g1.svg
   :alt: Book VII, Proposition 11

.. subclause::

   Since, as :g:`AB <0317.g1:/ A B />` is to :g:`CD <0317.g1:/ C D />`, so is :g:`AE <0317.g1:/ A E />` to :g:`CF <0317.g1:/ C F />`,

.. assertion::

   whatever part or parts :g:`AB <0317.g1:/ A B />` is of :g:`CD <0317.g1:/ C D />`, the :term:`same part <part-aliquot>` or the :term:`same parts <parts-non-aliquot>` is :g:`AE <0317.g1:/ A E />` of :g:`CF <0317.g1:/ C F />` also; :just:`[VII. Def. 20] <VII.def.20>`

.. assertion::

   Therefore also the remainder :g:`EB <0317.g1:/ E B />` is the same part or parts of :g:`FD <0317.g1:/ F D />` that :g:`AB <0317.g1:/ A B />` is of :g:`CD <0317.g1:/ C D />`. :just:`[VII. 7, 8]`

.. assertion:: [VII. Def. 20] <VII.def.20>

   Therefore, as :g:`EB <0317.g1:/ E B />` is to :g:`FD <0317.g1:/ F D />`, so is :g:`AB <0317.g1:/ A B />` to :g:`CD <0317.g1:/ C D />`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

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
     "VII.def.4" [label="VII.def.4", fillcolor="#224422", tooltip="VII.def.4: but parts when it does not measure it.", URL="../../definitions/index.html#vii-def-4", target="_top"];
     "VII.def.5" [label="VII.def.5", fillcolor="#224422", tooltip="VII.def.5: The greater number is a multiple of the less when it is measured by the less.", URL="../../definitions/index.html#vii-def-5", target="_top"];
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../definitions/index.html#vii-def-20", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../05/index.html", target="_top"];
     "VII.7" [label="VII.7", fillcolor="#222244", tooltip="VII.7: If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder will also be the same part of the remainder that the whole is of the whole.", URL="../07/index.html", target="_top"];
     "VII.8" [label="VII.8", fillcolor="#222244", tooltip="VII.8: If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder will also be the same parts of the remainder that the whole is of the…", URL="../08/index.html", target="_top"];
     "VII.11" [label="VII.11", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="VII.11: If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.", URL="index.html", target="_top"];
     "V.def.2" -> "V.def.1";
     "VII.def.3" -> "V.def.1";
     "VII.def.4" -> "V.def.1";
     "VII.def.5" -> "V.def.1";
     "VII.5" -> "V.def.2";
     "VII.def.2" -> "VII.def.1";
     "VII.def.3" -> "VII.def.2";
     "VII.def.5" -> "VII.def.2";
     "VII.5" -> "VII.def.2";
     "VII.7" -> "VII.def.2";
     "VII.8" -> "VII.def.2";
     "VII.11" -> "VII.def.2";
     "VII.def.20" -> "VII.def.3";
     "VII.5" -> "VII.def.3";
     "VII.7" -> "VII.def.3";
     "VII.def.20" -> "VII.def.4";
     "VII.8" -> "VII.def.4";
     "VII.def.20" -> "VII.def.5";
     "VII.5" -> "VII.def.5";
     "VII.11" -> "VII.def.20";
     "VII.7" -> "VII.5";
     "VII.8" -> "VII.7";
     "VII.11" -> "VII.7";
     "VII.11" -> "VII.8";
   }

Required for
------------

:ref:`IX.35 <IX.35>`, :ref:`IX.36 <IX.36>`

----

See :ref:`Commentary on Proposition VII.11 <VII.11.commentary>`.

.. toctree::
   :hidden:

   commentary
