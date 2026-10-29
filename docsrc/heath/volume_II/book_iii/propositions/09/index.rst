:canonical_id: III.9
:volume: II
:book: III
:proposition: 9
:type: proposition
:title: Proposition III.9
:folios: 0027, 0028
:pages: 21, 22
:dependencies: I.def.10, I.8, III.1

.. _III.9:

.. folio:: 0027
   :page: 21

PROPOSITION 9.
==============

.. enunciation::

   If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.

Let :g:`$ABC$ <0027.g1:( A B C )>` be a circle and :g:`$D$ <0027.g1:D>` a point within it, and from :g:`$D$ <0027.g1:D>` let more than two :eq:`equal <0027.g1:/ D A / = 0027.g1:/ D B / = 0027.g1:/ D C />` straight lines, namely :g:`$DA$ <0027.g1:/ D A />`, :g:`$DB$ <0027.g1:/ D B />`, :g:`$DC$ <0027.g1:/ D C />`, fall on the circle :g:`$ABC$ <0027.g1:( A B C )>`;

I say that the point :g:`$D$ <0027.g1:D>` is the centre of the circle :g:`$ABC$ <0027.g1:( A B C )>`.

.. picture:: 0027.g1.svg
   :alt: Diagram for Proposition 9

For let :g:`$AB$ <0027.g1:/ A B />`, :g:`$BC$ <0027.g1:/ B C />` be joined and :eq:`bisected <0027.g1:/ A E / = 0027.g1:/ E B /; 0027.g1:/ B F / = 0027.g1:/ F C />` at the points :g:`$E$ <0027.g1:E>`, :g:`$F$ <0027.g1:F>`, and let :g:`$ED$ <0027.g1:/ E D />`, :g:`$FD$ <0027.g1:/ F D />` be joined and drawn through to the points :g:`$G$ <0027.g1:G>`, :g:`$K$ <0027.g1:K>`, :g:`$H$ <0027.g1:H>`, :g:`$L$ <0027.g1:L>`.

Then, since :g:`$AE$ <0027.g1:/ A E />` is :eq:`equal <0027.g1:/ A E / = 0027.g1:/ E B />` to :g:`$EB$ <0027.g1:/ E B />`, and :g:`$ED$ <0027.g1:/ E D />` is common,

.. subclause::

   the two sides :g:`$AE$ <0027.g1:/ A E />`, :g:`$ED$ <0027.g1:/ E D />` are :eq:`equal <0027.g1:/ A E / = 0027.g1:/ B E />` to the two sides :g:`$BE$ <0027.g1:/ B E />`, :g:`$ED$ <0027.g1:/ E D />`;

and the base :g:`$DA$ <0027.g1:/ D A />` is :eq:`equal <0027.g1:/ D A / = 0027.g1:/ D B />` to the base :g:`$DB$ <0027.g1:/ D B />`;

.. assertion:: [I. 8] <I.8>

   therefore the angle :g:`$AED$ <0027.g1:< A E D )>` is :eq:`equal <0027.g1:< A E D ) = 0027.g1:< B E D )>` to the angle :g:`$BED$ <0027.g1:< B E D )>`.

.. assertion:: [I. Def. 10] <I.def.10>

   Therefore each of the angles :g:`$AED$ <0027.g1:< A E D )>`, :g:`$BED$ <0027.g1:< B E D )>` is :eq:`right <0027.g1:< A E D ) = 0027.g1:< B E D )>`;

therefore :g:`$GK$ <0027.g1:/ G K />` cuts :g:`$AB$ <0027.g1:/ A B />` into two :eq:`equal <0027.g1:/ A E / = 0027.g1:/ E B />` parts and at :eq:`right angles <0027.g1:< A E D ) = 0027.g1:< B E D )>`.

And since, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line, :just:`[III. 1, Por.]`

.. assertion::

   the centre of the circle is on :g:`$GK$ <0027.g1:/ G K />`.

.. _folio-ii-0028:

.. folio:: 0028
   :page: 22

For the same reason

.. assertion::

   the centre of the circle :g:`$ABC$ <0027.g1:( A B C )>` is also on :g:`$HL$ <0027.g1:/ H L />`.

And the straight lines :g:`$GK$ <0027.g1:/ G K />`, :g:`$HL$ <0027.g1:/ H L />` have no other point common but the point :g:`$D$ <0027.g1:D>`;

.. assertion::

   therefore the point :g:`$D$ <0027.g1:D>` is the centre of the circle :g:`$ABC$ <0027.g1:( A B C )>`.

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
     "I.def.10" [label="I.def.10", fillcolor="#224422", URL="../../../../volume_I/book_i/definitions/index.html#i-def-10", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", URL="../../../../volume_I/book_i/definitions/index.html#i-def-15", target="_top"];
     "I.post.1" [label="I.post.1", fillcolor="#444422", URL="../../../../volume_I/book_i/postulates/index.html#i-post-1", target="_top"];
     "I.post.2" [label="I.post.2", fillcolor="#444422", URL="../../../../volume_I/book_i/postulates/index.html#i-post-2", target="_top"];
     "I.post.3" [label="I.post.3", fillcolor="#444422", URL="../../../../volume_I/book_i/postulates/index.html#i-post-3", target="_top"];
     "I.cn.1" [label="I.cn.1", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-1", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-4", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "III.1" [label="III.1", fillcolor="#222244", URL="../01/index.html", target="_top"];
     "III.9" [label="III.9", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "III.1" -> "I.def.10";
     "III.9" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.5" -> "I.4";
     "I.7" -> "I.5";
     "I.8" -> "I.7";
     "III.1" -> "I.8";
     "III.9" -> "I.8";
     "III.9" -> "III.1";
   }

Required for
------------

:ref:`III.25 <III.25>`

----

See :ref:`Commentary on Proposition III.9 <III.9.commentary>`.

.. toctree::
   :hidden:

   commentary
