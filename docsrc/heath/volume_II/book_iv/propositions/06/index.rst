:canonical_id: IV.6
:volume: II
:book: IV
:proposition: 6
:type: proposition
:title: Proposition IV.6
:folios: 0097
:pages: 91
:dependencies: I.def.22, I.4, III.31

.. _IV.6:

.. _folio-ii-0097:

.. folio:: 0097
   :page: 91

PROPOSITION 6.
==============

.. enunciation::

   In a given circle to inscribe a square.

Let :g:`ABCD <0097.g1:( A B C D )>` be the given circle;
thus it is required to inscribe a square in the circle :g:`ABCD <0097.g1:( A B C D )>`.

Let two diameters :g:`AC <0097.g1:/ A C />`, :g:`BD <0097.g1:/ B D />` of the
circle :g:`ABCD <0097.g1:( A B C D )>` be drawn at right angles
to one another, and let :g:`AB <0097.g1:/ A B />`, :g:`BC <0097.g1:/ B C />`, :g:`CD <0097.g1:/ C D />`,
:g:`DA <0097.g1:/ D A />` be joined.

.. picture:: 0097.g1.svg
   :alt: Proposition 6 diagram

Then, since :g:`BE <0097.g1:/ B E />` is :eq:`equal <0097.g1:/ B E / = 0097.g1:/ E D />` to :g:`ED <0097.g1:/ E D />`, for
:g:`E <0097.g1:E>` is the centre,
and :g:`EA <0097.g1:/ E A />` is common and at right angles,
therefore the base :g:`AB <0097.g1:/ A B />` is :eq:`equal <0097.g1:/ A B / = 0097.g1:/ A D />` to the
base :g:`AD <0097.g1:/ A D />`. :just:`[I. 4] <I.4>`

For the same reason
each of the straight lines :g:`BC <0097.g1:/ B C />`, :g:`CD <0097.g1:/ C D />` is also :eq:`equal <0097.g1:/ B C / = 0097.g1:/ C D / = 0097.g1:/ A B / = 0097.g1:/ A D />` to each of
the straight lines :g:`AB <0097.g1:/ A B />`, :g:`AD <0097.g1:/ A D />`;

.. assertion::

   therefore the quadrilateral :g:`ABCD <0097.g1:< A B C D >>` is :eq:`equilateral <0097.g1:/ A B / = 0097.g1:/ B C / = 0097.g1:/ C D / = 0097.g1:/ D A />`.

I say next that it is also right-angled.

For, since the straight line :g:`BD <0097.g1:/ B D />` is a diameter of the circle
:g:`ABCD <0097.g1:( A B C D )>`,
therefore :g:`BAD <0097.g1:( B A D )>` is a semicircle;

.. assertion:: [III. 31] <III.31>

   therefore the angle :g:`BAD <0097.g1:< B A D )>` is right.

For the same reason
each of the angles :g:`ABC <0097.g1:< A B C )>`, :g:`BCD <0097.g1:< B C D )>`, :g:`CDA <0097.g1:< C D A )>` is also :eq:`right <0097.g1:< A B C ) = 0097.g1:< B C D ) = 0097.g1:< C D A ) = 0097.g1:< B A D )>`;

.. assertion::

   therefore the quadrilateral :g:`ABCD <0097.g1:< A B C D >>` is right-angled.

But it was also proved :eq:`equilateral <0097.g1:/ A B / = 0097.g1:/ B C / = 0097.g1:/ C D / = 0097.g1:/ D A />`;
therefore it is a square; :just:`[I. Def. 22] <I.def.22>`
and it has been inscribed in the circle :g:`ABCD <0097.g1:( A B C D )>`.

Therefore in the given circle the square :g:`ABCD <0097.g1:< A B C D >>` has been
inscribed.

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
     "I.def.10" [label="I.def.10", fillcolor="#224422", tooltip="I.def.10: When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-10", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", tooltip="I.def.15: A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-15", target="_top"];
     "I.def.22" [label="I.def.22", fillcolor="#224422", tooltip="I.def.22: Of quadrilateral figures, a square is that which is both equilateral and right-angled ; an oblong that which is right-angled but not equilateral ; a rhombus that which is…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-22", target="_top"];
     "I.def.23" [label="I.def.23", fillcolor="#224422", tooltip="I.def.23: Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-23", target="_top"];
     "I.post.1" [label="I.post.1", fillcolor="#444422", tooltip="I.post.1: To draw a straight line from any point to any point.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-1", target="_top"];
     "I.post.2" [label="I.post.2", fillcolor="#444422", tooltip="I.post.2: To produce a finite straight line continuously in a straight line.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-2", target="_top"];
     "I.post.3" [label="I.post.3", fillcolor="#444422", tooltip="I.post.3: To describe a circle with any centre and distance.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-3", target="_top"];
     "I.post.4" [label="I.post.4", fillcolor="#444422", tooltip="I.post.4: That all right angles are equal to one another.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-4", target="_top"];
     "I.post.5" [label="I.post.5", fillcolor="#444422", tooltip="I.post.5: That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet…", URL="../../../../volume_I/book_i/postulates/index.html#i-post-5", target="_top"];
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
     "I.17" [label="I.17", fillcolor="#222244", tooltip="I.17: In any triangle two angles taken together in any manner are less than two right angles.", URL="../../../../volume_I/book_i/propositions/17/index.html", target="_top"];
     "I.18" [label="I.18", fillcolor="#222244", tooltip="I.18: In any triangle the greater side subtends the greater angle.", URL="../../../../volume_I/book_i/propositions/18/index.html", target="_top"];
     "I.19" [label="I.19", fillcolor="#222244", tooltip="I.19: In any triangle the greater angle is subtended by the greater side.", URL="../../../../volume_I/book_i/propositions/19/index.html", target="_top"];
     "I.20" [label="I.20", fillcolor="#222244", tooltip="I.20: In any triangle two sides taken together in any manner are greater than the remaining one.", URL="../../../../volume_I/book_i/propositions/20/index.html", target="_top"];
     "I.22" [label="I.22", fillcolor="#222244", tooltip="I.22: Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any…", URL="../../../../volume_I/book_i/propositions/22/index.html", target="_top"];
     "I.23" [label="I.23", fillcolor="#222244", tooltip="I.23: On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", URL="../../../../volume_I/book_i/propositions/23/index.html", target="_top"];
     "I.27" [label="I.27", fillcolor="#222244", tooltip="I.27: If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", URL="../../../../volume_I/book_i/propositions/27/index.html", target="_top"];
     "I.29" [label="I.29", fillcolor="#222244", tooltip="I.29: A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior…", URL="../../../../volume_I/book_i/propositions/29/index.html", target="_top"];
     "I.31" [label="I.31", fillcolor="#222244", tooltip="I.31: Through a given point to draw a straight line parallel to a given straight line.", URL="../../../../volume_I/book_i/propositions/31/index.html", target="_top"];
     "I.32" [label="I.32", fillcolor="#222244", tooltip="I.32: In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to…", URL="../../../../volume_I/book_i/propositions/32/index.html", target="_top"];
     "III.20" [label="III.20", fillcolor="#222244", tooltip="III.20: In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", URL="../../../book_iii/propositions/20/index.html", target="_top"];
     "III.21" [label="III.21", fillcolor="#222244", tooltip="III.21: In a circle the angles in the same segment are equal to one another.", URL="../../../book_iii/propositions/21/index.html", target="_top"];
     "III.22" [label="III.22", fillcolor="#222244", tooltip="III.22: The opposite angles of quadrilaterals in circles are equal to two right angles.", URL="../../../book_iii/propositions/22/index.html", target="_top"];
     "III.31" [label="III.31", fillcolor="#222244", tooltip="III.31: In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle…", URL="../../../book_iii/propositions/31/index.html", target="_top"];
     "IV.6" [label="IV.6", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IV.6: In a given circle to inscribe a square.", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "IV.6" -> "I.def.22";
     "I.27" -> "I.def.23";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.15" -> "I.post.4";
     "I.29" -> "I.post.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.29" -> "I.cn.2";
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
     "I.22" -> "I.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "IV.6" -> "I.4";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.18" -> "I.16";
     "I.27" -> "I.16";
     "III.31" -> "I.17";
     "I.19" -> "I.18";
     "I.20" -> "I.19";
     "I.22" -> "I.20";
     "I.23" -> "I.22";
     "I.31" -> "I.23";
     "I.31" -> "I.27";
     "I.32" -> "I.29";
     "I.32" -> "I.31";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "III.21" -> "III.20";
     "III.22" -> "III.21";
     "III.31" -> "III.22";
     "IV.6" -> "III.31";
   }

Required for
------------

:ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`

----

See :ref:`Commentary on Proposition IV.6 <IV.6.commentary>`.

.. toctree::
   :hidden:

   commentary
