:canonical_id: VII.11
:volume: II
:book: VII
:proposition: 11
:type: proposition
:title: Proposition VII.11
:folios: 0317
:pages: 311
:dependencies: VII.def.20, VII.7, VII.8

.. _VII.11:

.. folio:: 0317
   :page: 311

PROPOSITION 11.
===============

.. enunciation::

   If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

As the whole :g:`$AB$ <0317.g1:/ A B />` is to the whole :g:`$CD$ <0317.g1:/ C D />`, so let :g:`$AE$ <0317.g1:/ A E />` subtracted be to :g:`$CF$ <0317.g1:/ C F />` subtracted;

I say that the remainder :g:`$EB$ <0317.g1:/ E B />` is also to the remainder :g:`$FD$ <0317.g1:/ F D />` as the whole :g:`$AB$ <0317.g1:/ A B />` to the whole :g:`$CD$ <0317.g1:/ C D />`.

.. picture:: 0317.g1.svg
   :alt: Book VII, Proposition 11

.. subclause::

   Since, as :g:`$AB$ <0317.g1:/ A B />` is to :g:`$CD$ <0317.g1:/ C D />`, so is :g:`$AE$ <0317.g1:/ A E />` to :g:`$CF$ <0317.g1:/ C F />`,

.. assertion::

   whatever part or parts :g:`$AB$ <0317.g1:/ A B />` is of :g:`$CD$ <0317.g1:/ C D />`, the same part or the same parts is :g:`$AE$ <0317.g1:/ A E />` of :g:`$CF$ <0317.g1:/ C F />` also; :just:`[VII. Def. 20] <VII.def.20>`

.. assertion::

   Therefore also the remainder :g:`$EB$ <0317.g1:/ E B />` is the same part or parts of :g:`$FD$ <0317.g1:/ F D />` that :g:`$AB$ <0317.g1:/ A B />` is of :g:`$CD$ <0317.g1:/ C D />`. :just:`[VII. 7, 8]`

.. assertion:: [VII. Def. 20] <VII.def.20>

   Therefore, as :g:`$EB$ <0317.g1:/ E B />` is to :g:`$FD$ <0317.g1:/ F D />`, so is :g:`$AB$ <0317.g1:/ A B />` to :g:`$CD$ <0317.g1:/ C D />`.

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
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", URL="../../definitions/index.html#vii-def-20", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", URL="../05/index.html", target="_top"];
     "VII.7" [label="VII.7", fillcolor="#222244", URL="../07/index.html", target="_top"];
     "VII.8" [label="VII.8", fillcolor="#222244", URL="../08/index.html", target="_top"];
     "VII.11" [label="VII.11", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
