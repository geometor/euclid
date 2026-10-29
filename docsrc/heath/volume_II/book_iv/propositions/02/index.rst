:canonical_id: IV.2
:volume: II
:book: IV
:proposition: 2
:type: proposition
:title: Proposition IV.2
:folios: 0087, 0088
:pages: 81, 82
:dependencies: I.23, I.32, III.16, III.32

.. _IV.2:

.. folio:: 0087
   :page: 81

PROPOSITION 2.
==============

.. enunciation::

   In a given circle to inscribe a triangle equiangular with a given triangle.

Let :g:`$ABC$ <0088.g1:( A B C )>` be the given circle, and :g:`$DEF$ <0088.g1:< D E F >>` the given
triangle;
thus it is required to inscribe in the circle :g:`$ABC$ <0088.g1:( A B C )>` a triangle
equiangular with the triangle :g:`$DEF$ <0088.g1:< D E F >>`.

Let :g:`$GH$ <0088.g1:/ G H />` be drawn touching the circle :g:`$ABC$ <0088.g1:( A B C )>` at :g:`$A$ <0088.g1:A>` :just:`[III. 16, Por.]`;

.. _folio-ii-0088:

.. folio:: 0088
   :page: 82

on the straight line :g:`$AH$ <0088.g1:/ A H />`, and at the point :g:`$A$ <0088.g1:A>` on it, let the
angle :g:`$HAC$ <0088.g1:< H A C )>` be constructed :eq:`equal <0088.g1:< H A C ) = 0088.g1:< D E F )>` to the angle :g:`$DEF$ <0088.g1:< D E F )>`,
and on the straight line :g:`$AG$ <0088.g1:/ A G />`, and at the point :g:`$A$ <0088.g1:A>` on it, let
the angle :g:`$GAB$ <0088.g1:< G A B )>` be constructed :eq:`equal <0088.g1:< G A B ) = 0088.g1:< D F E )>` to the angle :g:`$DFE$ <0088.g1:< D F E )>`;
:just:`[I. 23] <I.23>`
let :g:`$BC$ <0088.g1:/ B C />` be joined.

.. picture:: 0088.g1.svg
   :alt: Diagram for Proposition 2

Then, since a straight line :g:`$AH$ <0088.g1:/ A H />` touches the circle :g:`$ABC$ <0088.g1:( A B C )>`,
and from the point of contact at :g:`$A$ <0088.g1:A>` the straight line :g:`$AC$ <0088.g1:/ A C />` is
drawn across in the circle,
therefore the angle :g:`$HAC$ <0088.g1:< H A C )>` is :eq:`equal <0088.g1:< H A C ) = 0088.g1:< A B C )>` to the angle :g:`$ABC$ <0088.g1:< A B C )>` in the
alternate segment of the circle. :just:`[III. 32] <III.32>`

But the angle :g:`$HAC$ <0088.g1:< H A C )>` is :eq:`equal <0088.g1:< H A C ) = 0088.g1:< D E F )>` to the angle :g:`$DEF$ <0088.g1:< D E F )>`;
therefore the angle :g:`$ABC$ <0088.g1:< A B C )>` is also :eq:`equal <0088.g1:< A B C ) = 0088.g1:< D E F )>` to the angle :g:`$DEF$ <0088.g1:< D E F )>`.

For the same reason

.. assertion::

   the angle :g:`$ACB$ <0088.g1:< A C B )>` is also :eq:`equal <0088.g1:< A C B ) = 0088.g1:< D F E )>` to the angle :g:`$DFE$ <0088.g1:< D F E )>`;

therefore the remaining angle :g:`$BAC$ <0088.g1:< B A C )>` is also :eq:`equal <0088.g1:< B A C ) = 0088.g1:< E D F )>` to the
remaining angle :g:`$EDF$ <0088.g1:< E D F )>`. :just:`[I. 32] <I.32>`

.. qed::

   Therefore in the given circle there has been inscribed a triangle equiangular with the given triangle. :just:`Q. E. F.`

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
     "III.16" [label="III.16", fillcolor="#222244", tooltip="III.16: The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the…", URL="../../../book_iii/propositions/16/index.html", target="_top"];
     "III.18" [label="III.18", fillcolor="#222244", tooltip="III.18: If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.", URL="../../../book_iii/propositions/18/index.html", target="_top"];
     "III.19" [label="III.19", fillcolor="#222244", tooltip="III.19: If a straight line touch a circle, and from the point of contact a straight line be drawn at right angles to the tangent, the centre of the circle will be on the straight line so…", URL="../../../book_iii/propositions/19/index.html", target="_top"];
     "III.20" [label="III.20", fillcolor="#222244", tooltip="III.20: In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", URL="../../../book_iii/propositions/20/index.html", target="_top"];
     "III.21" [label="III.21", fillcolor="#222244", tooltip="III.21: In a circle the angles in the same segment are equal to one another.", URL="../../../book_iii/propositions/21/index.html", target="_top"];
     "III.22" [label="III.22", fillcolor="#222244", tooltip="III.22: The opposite angles of quadrilaterals in circles are equal to two right angles.", URL="../../../book_iii/propositions/22/index.html", target="_top"];
     "III.31" [label="III.31", fillcolor="#222244", tooltip="III.31: In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle…", URL="../../../book_iii/propositions/31/index.html", target="_top"];
     "III.32" [label="III.32", fillcolor="#222244", tooltip="III.32: If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the…", URL="../../../book_iii/propositions/32/index.html", target="_top"];
     "IV.2" [label="IV.2", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IV.2: In a given circle to inscribe a triangle equiangular with a given triangle.", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
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
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "III.16" -> "I.5";
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
     "III.16" -> "I.17";
     "III.18" -> "I.17";
     "III.31" -> "I.17";
     "I.19" -> "I.18";
     "I.20" -> "I.19";
     "III.16" -> "I.19";
     "III.18" -> "I.19";
     "I.22" -> "I.20";
     "I.23" -> "I.22";
     "I.31" -> "I.23";
     "IV.2" -> "I.23";
     "I.31" -> "I.27";
     "I.32" -> "I.29";
     "I.32" -> "I.31";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "III.32" -> "I.32";
     "IV.2" -> "I.32";
     "IV.2" -> "III.16";
     "III.19" -> "III.18";
     "III.32" -> "III.19";
     "III.21" -> "III.20";
     "III.22" -> "III.21";
     "III.31" -> "III.22";
     "III.32" -> "III.22";
     "III.32" -> "III.31";
     "IV.2" -> "III.32";
   }

Required for
------------

:ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition IV.2 <IV.2.commentary>`.

.. toctree::
   :hidden:

   commentary
