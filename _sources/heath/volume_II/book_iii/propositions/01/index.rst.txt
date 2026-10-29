:canonical_id: III.1
:volume: II
:book: III
:proposition: 1
:type: proposition
:title: Proposition III.1
:folios: 0012, 0013
:pages: 6, 7
:dependencies: I.def.10, I.8

.. _III.1:

.. _folio-ii-0012:

.. folio:: 0012
   :page: 6

PROPOSITION 1.
==============

.. enunciation::

   To find the centre of a given circle.

Let :g:`$ABC$ <0012.g1:( A B C )>` be the given circle;

thus it is required to find the centre of the circle :g:`$ABC$ <0012.g1:( A B C )>`.

Let a straight line :g:`$AB$ <0012.g1:/ A B />` be drawn through it at random, and let it be :eq:`bisected <0012.g1:/ A D / = 0012.g1:/ D B />` at the point :g:`$D$ <0012.g1:D>`; from :g:`$D$ <0012.g1:D>` let :g:`$DC$ <0012.g1:/ D C />` be drawn at right angles to :g:`$AB$ <0012.g1:/ A B />` and let it be drawn through to :g:`$E$ <0012.g1:E>`; let :g:`$CE$ <0012.g1:/ C E />` be :eq:`bisected <0012.g1:/ C F / = 0012.g1:/ F E />` at :g:`$F$ <0012.g1:F>`;

I say that :g:`$F$ <0012.g1:F>` is the centre of the circle :g:`$ABC$ <0012.g1:( A B C )>`.

.. picture:: 0012.g1.svg
   :alt: Proposition 1

For suppose it is not,\ [#f1]_ but, if possible, let :g:`$G$ <0012.g1:G>` be the centre, and let :g:`$GA$ <0012.g1:/ G A />`, :g:`$GD$ <0012.g1:/ G D />`, :g:`$GB$ <0012.g1:/ G B />` be joined.

Then, since :g:`$AD$ <0012.g1:/ A D />` is :eq:`equal <0012.g1:/ A D / = 0012.g1:/ D B />` to :g:`$DB$ <0012.g1:/ D B />`, and :g:`$DG$ <0012.g1:/ D G />` is common,

.. subclause::

   the two sides :g:`$AD$ <0012.g1:/ A D />`, :g:`$DG$ <0012.g1:/ D G />` are :eq:`equal <0012.g1:/ A D / = 0012.g1:/ B D />` to the two sides :g:`$BD$ <0012.g1:/ B D />`, :g:`$DG$ <0012.g1:/ D G />` respectively;\ [#f2]_

and the base :g:`$GA$ <0012.g1:/ G A />` is :eq:`equal <0012.g1:/ G A / = 0012.g1:/ G B />` to the base :g:`$GB$ <0012.g1:/ G B />`, for they are radii;

.. assertion:: [I. 8] <I.8>

   therefore the angle :g:`$ADG$ <0012.g1:< A D G )>` is :eq:`equal <0012.g1:< A D G ) = 0012.g1:< G D B )>` to the angle :g:`$GDB$ <0012.g1:< G D B )>`.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; :just:`[I. Def. 10] <I.def.10>`

.. assertion::

   therefore the angle :g:`$GDB$ <0012.g1:< G D B )>` is right.

.. _folio-ii-0013:

.. folio:: 0013
   :page: 7

But the angle :g:`$FDB$ <0012.g1:< F D B )>` is also right; therefore the angle :g:`$FDB$ <0012.g1:< F D B )>` is :eq:`equal <0012.g1:< F D B ) = 0012.g1:< G D B )>` to the angle :g:`$GDB$ <0012.g1:< G D B )>`, the greater to the less: which is impossible.

.. assertion::

   Therefore :g:`$G$ <0012.g1:G>` is not the centre of the circle :g:`$ABC$ <0012.g1:( A B C )>`.

Similarly we can prove that neither is any other point except :g:`$F$ <0012.g1:F>`.

.. assertion::

   Therefore the point :g:`$F$ <0012.g1:F>` is the centre of the circle :g:`$ABC$ <0012.g1:( A B C )>`.

.. enunciation::

   PORISM. From this it is manifest that, if in a circle a straight line cut a straight line into two equal parts and at right angles, the centre of the circle is on the cutting straight line.

.. qed::

   Q. E. F.

.. [#f1] **For suppose it is not.** This is expressed in the Greek by the two words Μὴ γάρ, but such an elliptical phrase is impossible in English.

.. [#f2] **the two sides AD, DG are equal to the two sides BD, DG respectively.** As before observed, Euclid is not always careful to put the equals in corresponding order. The text here has ":g:`$GD$ <0012.g1:/ G D />`, :g:`$DB$ <0012.g1:/ D B />`."

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "I.def.10" [label="I.def.10", fillcolor="#224422", tooltip="I.def.10: When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-10", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", tooltip="I.def.15: A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-15", target="_top"];
     "I.post.1" [label="I.post.1", fillcolor="#444422", tooltip="I.post.1: To draw a straight line from any point to any point.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-1", target="_top"];
     "I.post.2" [label="I.post.2", fillcolor="#444422", tooltip="I.post.2: To produce a finite straight line continuously in a straight line.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-2", target="_top"];
     "I.post.3" [label="I.post.3", fillcolor="#444422", tooltip="I.post.3: To describe a circle with any centre and distance.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-3", target="_top"];
     "I.cn.1" [label="I.cn.1", fillcolor="#442222", tooltip="I.cn.1: Things which are equal to the same thing are also equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-1", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", tooltip="I.cn.3: If equals be subtracted from equals, the remainders are equal.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", tooltip="I.cn.4: Things which coincide with one another are equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-4", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", tooltip="I.1: On a given finite straight line to construct an equilateral triangle.", URL="../../../../volume_I/book_i/propositions/01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", tooltip="I.2: To place at a given point (as an extremity) a straight line equal to a given straight line.", URL="../../../../volume_I/book_i/propositions/02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", tooltip="I.3: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", URL="../../../../volume_I/book_i/propositions/03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", tooltip="I.4: If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the…", URL="../../../../volume_I/book_i/propositions/04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", tooltip="I.5: In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one…", URL="../../../../volume_I/book_i/propositions/05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", tooltip="I.7: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its…", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", tooltip="I.8: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the…", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "III.1" [label="III.1", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.1: To find the centre of a given circle.", URL="index.html", target="_top"];
     "III.1" -> "I.def.10";
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
   }

Required for
------------

:ref:`III.2 <III.2>`, :ref:`III.4 <III.4>`, :ref:`III.8 <III.8>`, :ref:`III.9 <III.9>`, :ref:`III.10 <III.10>`, :ref:`III.13 <III.13>`, :ref:`III.14 <III.14>`, :ref:`III.15 <III.15>`, :ref:`III.17 <III.17>`, :ref:`III.24 <III.24>`, :ref:`III.25 <III.25>`, :ref:`III.26 <III.26>`, :ref:`III.27 <III.27>`, :ref:`III.28 <III.28>`, :ref:`III.29 <III.29>`, :ref:`III.30 <III.30>`, :ref:`IV.3 <IV.3>`, :ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`, :ref:`IV.15 <IV.15>`, :ref:`IV.16 <IV.16>`, :ref:`VI.33 <VI.33>`, :ref:`XII.1 <XII.1>`, :ref:`XII.2 <XII.2>`, :ref:`XII.5 <XII.5>`, :ref:`XII.6 <XII.6>`, :ref:`XII.7 <XII.7>`, :ref:`XII.8 <XII.8>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.8 <XIII.8>`, :ref:`XIII.9 <XIII.9>`, :ref:`XIII.10 <XIII.10>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.12 <XIII.12>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition III.1 <III.1.commentary>`.

.. toctree::
   :hidden:

   commentary
