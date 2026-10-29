:canonical_id: IX.24
:volume: II
:book: IX
:proposition: 24
:type: proposition
:title: Proposition IX.24
:folios: 0420, 0421
:pages: 414, 415
:dependencies: VII.def.6

.. _IX.24:

.. folio:: 0420
   :page: 414

PROPOSITION 24.
===============

.. enunciation::

   If from an even number an even number be subtracted, the remainder will be even.

For from the even number :g:`$AB$ <0420.g3:/ A B />` let the even number :g:`$BC$ <0420.g3:/ B C />` be subtracted :

I say that the remainder :g:`$CA$ <0420.g3:/ A C />` is even.

.. picture:: 0420.g3.svg
   :alt: Book IX, Proposition 24

.. subclause::

   For, since :g:`$AB$ <0420.g3:/ A B />` is even, it has a half part. :just:`[VII. Def. 6] <VII.def.6>`

.. _folio-ii-0421:

.. folio:: 0421
   :page: 415

.. subclause::

   For the same reason :g:`$BC$ <0420.g3:/ B C />` also has a half part ;

.. assertion::

   so that the remainder [:g:`$CA$ <0420.g3:/ A C />` also has a half part, and] :g:`$AC$ <0420.g3:/ A C />` is therefore even.

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
     "VII.def.6" [label="VII.def.6", fillcolor="#224422", tooltip="VII.def.6: An even number is that which is divisible into two equal parts.", URL="../../../book_vii/definitions/index.html#vii-def-6", target="_top"];
     "IX.24" [label="IX.24", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.24: If from an even number an even number be subtracted, the remainder will be even.", URL="index.html", target="_top"];
     "IX.24" -> "VII.def.6";
   }

Required for
------------

:ref:`IX.25 <IX.25>`, :ref:`IX.26 <IX.26>`, :ref:`IX.27 <IX.27>`
