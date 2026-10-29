:canonical_id: III.30
:volume: II
:book: III
:proposition: 30
:type: proposition
:title: Proposition III.30
:folios: 0067
:pages: 61
:dependencies: I.4, III.28

.. _III.30:

.. folio:: 0067
   :page: 61

PROPOSITION 30.
===============

.. enunciation::

   To bisect a given circumference.

Let :g:`$ADB$ <0067.g1:( A D B )>` be the given circumference;
thus it is required to bisect the circumference :g:`$ADB$ <0067.g1:( A D B )>`.

Let :g:`$AB$ <0067.g1:/ A B />` be joined and bisected at
:g:`$C$ <0067.g1:C>`; from the point :g:`$C$ <0067.g1:C>` let :g:`$CD$ <0067.g1:/ C D />` be drawn
at right angles to the straight line :g:`$AB$ <0067.g1:/ A B />`,
and let :g:`$AD$ <0067.g1:/ A D />`, :g:`$DB$ <0067.g1:/ D B />` be joined.

.. picture:: 0067.g1.svg
   :alt: Diagram

Then, since :g:`$AC$ <0067.g1:/ A C />` is :eq:`equal <0067.g1:/ A C / = 0067.g1:/ C B />` to :g:`$CB$ <0067.g1:/ C B />`,
and :g:`$CD$ <0067.g1:/ C D />` is common,
the two sides :g:`$AC$ <0067.g1:/ A C />`, :g:`$CD$ <0067.g1:/ C D />` are :eq:`equal <0067.g1:/ A C / = 0067.g1:/ B C /; 0067.g1:/ C D / = 0067.g1:/ C D />` to the two sides :g:`$BC$ <0067.g1:/ B C />`, :g:`$CD$ <0067.g1:/ C D />`;
and the angle :g:`$ACD$ <0067.g1:< A C D )>` is :eq:`equal <0067.g1:< A C D ) = 0067.g1:< B C D )>` to the angle :g:`$BCD$ <0067.g1:< B C D )>`, for each is
right;

.. assertion:: [I. 4] <I.4>

   therefore the base :g:`$AD$ <0067.g1:/ A D />` is :eq:`equal <0067.g1:/ A D / = 0067.g1:/ D B />` to the base :g:`$DB$ <0067.g1:/ D B />`.

But equal straight lines cut off equal circumferences, the
greater equal to the greater, and the less to the less; :just:`[III. 28] <III.28>`

.. subclause::

   and each of the circumferences :g:`$AD$ <0067.g1:( A D )>`, :g:`$DB$ <0067.g1:( D B )>` is less than a semicircle;

.. assertion::

   therefore the circumference :g:`$AD$ <0067.g1:( A D )>` is :eq:`equal <0067.g1:( A D ) = 0067.g1:( D B )>` to the circumference :g:`$DB$ <0067.g1:( D B )>`.

Therefore the given circumference has been bisected at
the point :g:`$D$ <0067.g1:D>`.

.. qed::

   :just:`Q. E. F.`

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
     "III.def.11" [label="III.def.11", fillcolor="#224422", URL="../../definitions/index.html#iii-def-11", target="_top"];
     "III.1" [label="III.1", fillcolor="#222244", URL="../01/index.html", target="_top"];
     "III.5" [label="III.5", fillcolor="#222244", URL="../05/index.html", target="_top"];
     "III.10" [label="III.10", fillcolor="#222244", URL="../10/index.html", target="_top"];
     "III.24" [label="III.24", fillcolor="#222244", URL="../24/index.html", target="_top"];
     "III.26" [label="III.26", fillcolor="#222244", URL="../26/index.html", target="_top"];
     "III.28" [label="III.28", fillcolor="#222244", URL="../28/index.html", target="_top"];
     "III.30" [label="III.30", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "III.1" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
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
     "III.26" -> "I.4";
     "III.30" -> "I.4";
     "I.7" -> "I.5";
     "I.8" -> "I.7";
     "III.1" -> "I.8";
     "III.28" -> "I.8";
     "III.26" -> "III.def.11";
     "III.10" -> "III.1";
     "III.10" -> "III.5";
     "III.24" -> "III.10";
     "III.26" -> "III.24";
     "III.28" -> "III.26";
     "III.30" -> "III.28";
   }

Required for
------------

:ref:`IV.16 <IV.16>`
