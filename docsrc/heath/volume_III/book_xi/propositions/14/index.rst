:canonical_id: XI.14
:volume: III
:book: XI
:proposition: 14
:type: proposition
:title: Proposition XI.14
:folios: 0300
:pages: 296
:dependencies: I.17, XI.def.3, XI.def.8, XI.3

.. _XI.14:

.. _folio-iii-0300:

.. folio:: 0300
   :page: 296

PROPOSITION 14.
===============

.. enunciation::

   Planes to which the same straight line is at right angles will be parallel.

For let any straight line :g:`$AB$ <0300.g1:/ A B />` be at right angles to each of the planes :g:`$CD$ <0300.g1:< C D >>`, :g:`$EF$ <0300.g1:< E F >>`; I say that the planes are parallel.

.. picture:: 0300.g1.svg
   :alt: Book XI, Proposition 14

For, if not, they will meet when produced. Let them meet; they will then make, as common section, a straight line. :just:`[XI. 3] <XI.3>` Let them make :g:`$GH$ <0300.g1:/ G H />`; let a point :g:`$K$ <0300.g1:K>` be taken at random on :g:`$GH$ <0300.g1:/ G H />`, and let :g:`$AK$ <0300.g1:/ A K />`, :g:`$BK$ <0300.g1:/ B K />` be joined.

Now, since :g:`$AB$ <0300.g1:/ A B />` is at right angles to the plane :g:`$EF$ <0300.g1:< E F >>`, therefore :g:`$AB$ <0300.g1:/ A B />` is also at right angles to :g:`$BK$ <0300.g1:/ B K />` which is a straight line in the plane :g:`$EF$ <0300.g1:< E F >>` produced; :just:`[XI. Def. 3] <XI.def.3>`

.. assertion::

   therefore the angle :g:`$ABK$ <0300.g1:< A B K )>` is right.

.. subclause::

   For the same reason the angle :g:`$BAK$ <0300.g1:< B A K )>` is also right.

Thus, in the triangle :g:`$ABK$ <0300.g1:< A B K >>`, the two angles :g:`$ABK$ <0300.g1:< A B K )>`, :g:`$BAK$ <0300.g1:< B A K )>` are equal to two right angles:

.. assertion:: [I. 17] <I.17>

   which is impossible.

Therefore the planes :g:`$CD$ <0300.g1:< C D >>`, :g:`$EF$ <0300.g1:< E F >>` will not meet when produced;

.. assertion:: [XI. Def. 8] <XI.def.8>

   therefore the planes :g:`$CD$ <0300.g1:< C D >>`, :g:`$EF$ <0300.g1:< E F >>` are parallel.

.. assertion::

   Therefore planes to which the same straight line is at right angles are parallel.

.. qed::

   Q. E. D.

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
     "I.cn.2" [label="I.cn.2", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-2", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-4", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "I.11" [label="I.11", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/11/index.html", target="_top"];
     "I.13" [label="I.13", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/13/index.html", target="_top"];
     "I.17" [label="I.17", fillcolor="#222244", URL="../../../../volume_I/book_i/propositions/17/index.html", target="_top"];
     "XI.def.3" [label="XI.def.3", fillcolor="#224422", URL="../../definitions/index.html#xi-def-3", target="_top"];
     "XI.def.8" [label="XI.def.8", fillcolor="#224422", URL="../../definitions/index.html#xi-def-8", target="_top"];
     "XI.3" [label="XI.3", fillcolor="#222244", URL="../03/index.html", target="_top"];
     "XI.14" [label="XI.14", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.2" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "I.11" -> "I.1";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.11" -> "I.3";
     "I.5" -> "I.4";
     "I.7" -> "I.5";
     "I.8" -> "I.7";
     "I.11" -> "I.8";
     "I.13" -> "I.11";
     "I.17" -> "I.13";
     "XI.14" -> "I.17";
     "XI.14" -> "XI.def.3";
     "XI.14" -> "XI.def.8";
     "XI.14" -> "XI.3";
   }

Required for
------------

:ref:`XI.15 <XI.15>`
