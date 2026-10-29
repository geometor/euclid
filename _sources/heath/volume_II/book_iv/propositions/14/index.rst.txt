:canonical_id: IV.14
:volume: II
:book: IV
:proposition: 14
:type: proposition
:title: Proposition IV.14
:folios: 0112, 0113
:pages: 106, 107
:dependencies: I.6

.. _IV.14:

.. folio:: 0112
   :page: 106

PROPOSITION 14.
===============

.. enunciation::

   About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.

Let :g:`$ABCDE$ <0112.g1:< A B C D E >>` be the given pentagon, which is equilateral
and equiangular;
thus it is required to circumscribe a circle
about the pentagon :g:`$ABCDE$ <0112.g1:< A B C D E >>`.

Let the angles :g:`$BCD$ <0112.g1:< B C D )>`, :g:`$CDE$ <0112.g1:< C D E )>` be bisected
by the straight lines :g:`$CF$ <0112.g1:/ F C />`, :g:`$DF$ <0112.g1:/ F D />` respectively,
and from the point :g:`$F$ <0112.g1:F>`, at which the straight
lines meet, let the straight lines :g:`$FB$ <0112.g1:/ F B />`, :g:`$FA$ <0112.g1:/ F A />`,
:g:`$FE$ <0112.g1:/ F E />` be joined to the points :g:`$B$ <0112.g1:B>`, :g:`$A$ <0112.g1:A>`, :g:`$E$ <0112.g1:E>`.

.. picture:: 0112.g1.svg
   :alt: Book IV Proposition 14: Circle circumscribed about regular pentagon ABCDE

Then in manner similar to the preceding
it can be proved that the angles
:g:`$CBA$ <0112.g1:< C B A )>`, :g:`$BAE$ <0112.g1:< B A E )>`, :g:`$AED$ <0112.g1:< A E D )>` have also been bisected by the straight
lines :g:`$FB$ <0112.g1:/ F B />`, :g:`$FA$ <0112.g1:/ F A />`, :g:`$FE$ <0112.g1:/ F E />` respectively.

.. _folio-ii-0113:

.. folio:: 0113
   :page: 107

Now, since the angle :g:`$BCD$ <0112.g1:< B C D )>` is :eq:`equal <0112.g1:< B C D ) = 0112.g1:< C D E )>` to the angle :g:`$CDE$ <0112.g1:< C D E )>`,
and the angle :g:`$FCD$ <0112.g1:< F C D )>` is half of the angle :g:`$BCD$ <0112.g1:< B C D )>`,
and the angle :g:`$CDF$ <0112.g1:< C D F )>` half of the angle :g:`$CDE$ <0112.g1:< C D E )>`,

.. assertion::

   therefore the angle :g:`$FCD$ <0112.g1:< F C D )>` is also :eq:`equal <0112.g1:< F C D ) = 0112.g1:< C D F )>` to the angle :g:`$CDF$ <0112.g1:< C D F )>`,

.. assertion:: [I. 6] <I.6>

   so that the side :g:`$FC$ <0112.g1:/ F C />` is also :eq:`equal <0112.g1:/ F C / = 0112.g1:/ F D />` to the side :g:`$FD$ <0112.g1:/ F D />`.

Similarly it can be proved that
each of the straight lines :g:`$FB$ <0112.g1:/ F B />`, :g:`$FA$ <0112.g1:/ F A />`, :g:`$FE$ <0112.g1:/ F E />` is also :eq:`equal <0112.g1:/ F B / = 0112.g1:/ F A / = 0112.g1:/ F E / = 0112.g1:/ F C / = 0112.g1:/ F D />` to each
of the straight lines :g:`$FC$ <0112.g1:/ F C />`, :g:`$FD$ <0112.g1:/ F D />`;

.. assertion::

   therefore the five straight lines :g:`$FA$ <0112.g1:/ F A />`, :g:`$FB$ <0112.g1:/ F B />`, :g:`$FC$ <0112.g1:/ F C />`, :g:`$FD$ <0112.g1:/ F D />`, :g:`$FE$ <0112.g1:/ F E />` are :eq:`equal <0112.g1:/ F A / = 0112.g1:/ F B / = 0112.g1:/ F C / = 0112.g1:/ F D / = 0112.g1:/ F E />` to one another.

Therefore the circle described with centre :g:`$F$ <0112.g1:F>` and distance
one of the straight lines :g:`$FA$ <0112.g1:/ F A />`, :g:`$FB$ <0112.g1:/ F B />`, :g:`$FC$ <0112.g1:/ F C />`, :g:`$FD$ <0112.g1:/ F D />`, :g:`$FE$ <0112.g1:/ F E />` will pass
also through the remaining points, and will have been
circumscribed.

Let it be circumscribed, and let it be :g:`$ABCDE$ <0112.g1:( A B C D E )>`.

.. qed::

   Therefore about the given pentagon, which is equilateral and equiangular, a circle has been circumscribed. :just:`Q. E. F.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "I.6" [label="I.6", fillcolor="#222244", tooltip="I.6: If in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another.", URL="../../../../volume_I/book_i/propositions/06/index.html", target="_top"];
     "IV.14" [label="IV.14", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IV.14: About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.", URL="index.html", target="_top"];
     "IV.14" -> "I.6";
   }

Required for
------------

:ref:`XIII.8 <XIII.8>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.18 <XIII.18>`
