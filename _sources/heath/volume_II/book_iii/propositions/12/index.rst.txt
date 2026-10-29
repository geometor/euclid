:canonical_id: III.12
:volume: II
:book: III
:proposition: 12
:type: proposition
:title: Proposition III.12
:folios: 0033, 0034
:pages: 27, 28
:dependencies: I.20

.. _III.12:

.. folio:: 0033
   :page: 27

PROPOSITION 12.
===============

.. enunciation::

   If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

For let the two circles :g:`ABC <0034.g1:( A B C )>`, :g:`ADE <0034.g1:( A D E )>` touch one another externally at the point :g:`A <0034.g1:A>`, and let the centre :g:`F <0034.g1:F>` of :g:`ABC <0034.g1:( A B C )>`, and the centre :g:`G <0034.g1:G>` of :g:`ADE <0034.g1:( A D E )>`, be taken;

.. _folio-ii-0034:

.. folio:: 0034
   :page: 28

I say that the straight line joined from :g:`F <0034.g1:F>` to :g:`G <0034.g1:G>` will pass through the point of contact at :g:`A <0034.g1:A>`.

.. picture:: 0034.g1.svg
   :alt: Diagram for Proposition 12 showing two circles ABC and ADE touching externally at A

For suppose it does not, but, if possible, let it pass as :g:`FCDG <0034.g1:/ F C D G />`, and let :g:`AF <0034.g1:/ A F />`, :g:`AG <0034.g1:/ A G />` be joined.

Then, since the point :g:`F <0034.g1:F>` is the centre of the circle :g:`ABC <0034.g1:( A B C )>`,

.. assertion::

   :g:`FA <0034.g1:/ F A />` is :eq:`equal <0034.g1:/ F A / = 0034.g1:/ F C />` to :g:`FC <0034.g1:/ F C />`.

Again, since the point :g:`G <0034.g1:G>` is the centre of the circle :g:`ADE <0034.g1:( A D E )>`,

.. assertion::

   :g:`GA <0034.g1:/ G A />` is :eq:`equal <0034.g1:/ G A / = 0034.g1:/ G D />` to :g:`GD <0034.g1:/ G D />`.

But :g:`FA <0034.g1:/ F A />` was also proved :eq:`equal <0034.g1:/ F A / = 0034.g1:/ F C />` to :g:`FC <0034.g1:/ F C />`;

.. assertion::

   therefore :g:`FA <0034.g1:/ F A />`, :g:`AG <0034.g1:/ A G />` are equal to :g:`FC <0034.g1:/ F C />`, :g:`GD <0034.g1:/ G D />`,

.. assertion::

   so that the whole :g:`FG <0034.g1:/ F G />` is greater than :g:`FA <0034.g1:/ F A />`, :g:`AG <0034.g1:/ A G />`;

but it is also less :just:`[I. 20] <I.20>`: which is impossible.

Therefore the straight line joined from :g:`F <0034.g1:F>` to :g:`G <0034.g1:G>` will not fail to pass\ [#f1]_ through the point of contact at :g:`A <0034.g1:A>`;

.. assertion::

   therefore it will pass through it.

.. qed::

   Therefore etc. :just:`Q. E. D.]`

.. [#f1] **will not fail to pass.** The Greek has the double negative, οὐκ ἄρα ἡ...εὐθεῖα...οὐκ ἐλεύσεται, literally "the straight line...will not *not*-pass...."

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
     "I.post.4" [label="I.post.4", fillcolor="#444422", tooltip="I.post.4: That all right angles are equal to one another.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-4", target="_top"];
     "I.cn.1" [label="I.cn.1", fillcolor="#442222", tooltip="I.cn.1: Things which are equal to the same thing are also equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-1", target="_top"];
     "I.cn.2" [label="I.cn.2", fillcolor="#442222", tooltip="I.cn.2: If equals be added to equals, the wholes are equal.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-2", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", tooltip="I.cn.3: If equals be subtracted from equals, the remainders are equal.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", tooltip="I.cn.4: Things which coincide with one another are equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-4", target="_top"];
     "I.cn.5" [label="I.cn.5", fillcolor="#442222", tooltip="I.cn.5: The whole is greater than the part.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-5", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", tooltip="I.1: On a given finite straight line to construct an equilateral triangle.", URL="../../../../volume_I/book_i/propositions/01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", tooltip="I.2: To place at a given point (as an extremity) a straight line equal to a given straight line.", URL="../../../../volume_I/book_i/propositions/02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", tooltip="I.3: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", URL="../../../../volume_I/book_i/propositions/03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", tooltip="I.4: If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the…", URL="../../../../volume_I/book_i/propositions/04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", tooltip="I.5: In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one…", URL="../../../../volume_I/book_i/propositions/05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", tooltip="I.7: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its…", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", tooltip="I.8: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the…", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "I.9" [label="I.9", fillcolor="#222244", tooltip="I.9: To bisect a given rectilineal angle.", URL="../../../../volume_I/book_i/propositions/09/index.html", target="_top"];
     "I.10" [label="I.10", fillcolor="#222244", tooltip="I.10: To bisect a given finite straight line.", URL="../../../../volume_I/book_i/propositions/10/index.html", target="_top"];
     "I.11" [label="I.11", fillcolor="#222244", tooltip="I.11: To draw a straight line at right angles to a given straight line from a given point on it.", URL="../../../../volume_I/book_i/propositions/11/index.html", target="_top"];
     "I.13" [label="I.13", fillcolor="#222244", tooltip="I.13: If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", URL="../../../../volume_I/book_i/propositions/13/index.html", target="_top"];
     "I.15" [label="I.15", fillcolor="#222244", tooltip="I.15: If two straight lines cut one another, they make the vertical angles equal to one another.", URL="../../../../volume_I/book_i/propositions/15/index.html", target="_top"];
     "I.16" [label="I.16", fillcolor="#222244", tooltip="I.16: In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", URL="../../../../volume_I/book_i/propositions/16/index.html", target="_top"];
     "I.18" [label="I.18", fillcolor="#222244", tooltip="I.18: In any triangle the greater side subtends the greater angle.", URL="../../../../volume_I/book_i/propositions/18/index.html", target="_top"];
     "I.19" [label="I.19", fillcolor="#222244", tooltip="I.19: In any triangle the greater angle is subtended by the greater side.", URL="../../../../volume_I/book_i/propositions/19/index.html", target="_top"];
     "I.20" [label="I.20", fillcolor="#222244", tooltip="I.20: In any triangle two sides taken together in any manner are greater than the remaining one.", URL="../../../../volume_I/book_i/propositions/20/index.html", target="_top"];
     "III.12" [label="III.12", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.12: If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
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
     "I.20" -> "I.cn.5";
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
     "I.20" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.16" -> "I.15";
     "I.18" -> "I.16";
     "I.19" -> "I.18";
     "I.20" -> "I.19";
     "III.12" -> "I.20";
   }

----

See :ref:`Commentary on Proposition III.12 <III.12.commentary>`.

.. toctree::
   :hidden:

   commentary
