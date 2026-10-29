:canonical_id: III.2
:volume: II
:book: III
:proposition: 2
:type: proposition
:title: Proposition III.2
:folios: 0014, 0015
:pages: 8, 9
:dependencies: I.5, I.16, I.19, III.1

.. _III.2:

.. folio:: 0014
   :page: 8

PROPOSITION 2.
==============

.. enunciation::

   If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

Let :g:`$ABC$ <0014.g1:( A B C )>` be a circle, and let two points :g:`$A$ <0014.g1:A>`, :g:`$B$ <0014.g1:B>` be taken at random on its circumference;

I say that the straight line joined from :g:`$A$ <0014.g1:A>` to :g:`$B$ <0014.g1:B>` will fall within the circle.

.. picture:: 0014.g1.svg
   :alt: Proposition 2

For suppose it does not, but, if possible, let it fall outside, as :g:`$AEB$ <0014.g1:/ A E B />`; let the centre of the circle :g:`$ABC$ <0014.g1:( A B C )>` be taken :just:`[III. 1] <III.1>`, and let it be :g:`$D$ <0014.g1:D>`; let :g:`$DA$ <0014.g1:/ D A />`, :g:`$DB$ <0014.g1:/ D B />` be joined, and let :g:`$DFE$ <0014.g1:/ D F E />` be drawn through.

.. _folio-ii-0015:

.. folio:: 0015
   :page: 9

Then, since :g:`$DA$ <0014.g1:/ D A />` is :eq:`equal <0014.g1:/ D A / = 0014.g1:/ D B />` to :g:`$DB$ <0014.g1:/ D B />`,

.. subclause:: [I. 5] <I.5>

   the angle :g:`$DAE$ <0014.g1:< D A E )>` is also :eq:`equal <0014.g1:< D A E ) = 0014.g1:< D B E )>` to the angle :g:`$DBE$ <0014.g1:< D B E )>`.

And, since one side :g:`$AEB$ <0014.g1:/ A E B />` of the triangle :g:`$DAE$ <0014.g1:< D A E >>` is produced,

.. subclause:: [I. 16] <I.16>

   the angle :g:`$DEB$ <0014.g1:< D E B )>` is greater than the angle :g:`$DAE$ <0014.g1:< D A E )>`.

But the angle :g:`$DAE$ <0014.g1:< D A E )>` is :eq:`equal <0014.g1:< D A E ) = 0014.g1:< D B E )>` to the angle :g:`$DBE$ <0014.g1:< D B E )>`;

.. assertion::

   therefore the angle :g:`$DEB$ <0014.g1:< D E B )>` is greater than the angle :g:`$DBE$ <0014.g1:< D B E )>`.

And the greater angle is subtended by the greater side; :just:`[I. 19] <I.19>`

.. assertion::

   therefore :g:`$DB$ <0014.g1:/ D B />` is greater than :g:`$DE$ <0014.g1:/ D E />`.

But :g:`$DB$ <0014.g1:/ D B />` is :eq:`equal <0014.g1:/ D B / = 0014.g1:/ D F />` to :g:`$DF$ <0014.g1:/ D F />`;

.. assertion::

   therefore :g:`$DF$ <0014.g1:/ D F />` is greater than :g:`$DE$ <0014.g1:/ D E />`,

.. subclause::

   the less than the greater: which is impossible.

.. assertion::

   Therefore the straight line joined from :g:`$A$ <0014.g1:A>` to :g:`$B$ <0014.g1:B>` will not fall outside the circle.

Similarly we can prove that neither will it fall on the circumference itself;

.. assertion::

   therefore it will fall within.

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
     "I.post.4" [label="I.post.4", fillcolor="#444422", URL="../../../../volume_I/book_i/postulates/index.html#i-post-4", target="_top"];
     "I.cn.1" [label="I.cn.1", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-1", target="_top"];
     "I.cn.2" [label="I.cn.2", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-2", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-4", target="_top"];
     "I.cn.5" [label="I.cn.5", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-5", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "I.9" [label="I.9", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/09/index.html", target="_top"];
     "I.10" [label="I.10", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/10/index.html", target="_top"];
     "I.11" [label="I.11", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/11/index.html", target="_top"];
     "I.13" [label="I.13", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/13/index.html", target="_top"];
     "I.15" [label="I.15", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/15/index.html", target="_top"];
     "I.16" [label="I.16", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/16/index.html", target="_top"];
     "I.18" [label="I.18", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/18/index.html", target="_top"];
     "I.19" [label="I.19", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/19/index.html", target="_top"];
     "III.1" [label="III.1", fillcolor="#222244", URL="../01/index.html", target="_top"];
     "III.2" [label="III.2", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.16" -> "I.cn.5";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.2" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.1" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.16" -> "I.15";
     "I.18" -> "I.16";
     "III.2" -> "I.16";
     "I.19" -> "I.18";
     "III.2" -> "I.19";
     "III.2" -> "III.1";
   }

Required for
------------

:ref:`III.13 <III.13>`

----

See :ref:`Commentary on Proposition III.2 <III.2.commentary>`.

.. toctree::
   :hidden:

   commentary
