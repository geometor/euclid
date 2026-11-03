:canonical_id: III.37
:volume: II
:book: III
:proposition: 37
:type: proposition
:title: Proposition III.37
:folios: 0081, 0082
:pages: 75, 76
:dependencies: I.def.1, I.def.4, I.def.15, I.8, II.def.1, III.16, III.18, III.36

.. _III.37:

.. folio:: 0081
   :page: 75

PROPOSITION 37.
===============

.. enunciation::

   If a :term:`point <point>` be taken outside a :term:`circle <circle>` and from the point there fall on the circle two :term:`straight lines <straight-line>`, if one of them cut the circle, and the other fall on it, and if further the :term:`rectangle contained <contained-rectangle>` by the whole of the straight line which cuts

.. _folio-ii-0082:

.. folio:: 0082
   :page: 76

.. enunciation::

   the circle and the straight line intercepted on it outside between the point and the convex circumference be equal to the :term:`square <square>` on the straight line which falls on the circle, the straight line which falls on it will :term:`touch the circle <tangent-to-circle>`.

For let a point :g:`D <0082.g1:D>` be taken outside the circle :g:`ABC <0082.g1:( A B C )>`;
from :g:`D <0082.g1:D>` let the two straight lines
:g:`DCA <0082.g1:/ D C A />`, :g:`DB <0082.g1:/ D B />` fall on the circle :g:`ACB <0082.g1:( A C B )>`;
let :g:`DCA <0082.g1:/ D C A />` cut the circle and :g:`DB <0082.g1:/ D B />`
fall on it; and let the rectangle :g:`AD <0082.g1:/ A D />`,
:g:`DC <0082.g1:/ D C />` be equal to the square on :g:`DB <0082.g1:/ D B />`.

.. picture:: 0082.g1.svg
   :alt: Proposition 37 diagram

I say that :g:`DB <0082.g1:/ D B />` touches the circle
:g:`ABC <0082.g1:( A B C )>`.

For let :g:`DE <0082.g1:/ D E />` be drawn touching
:g:`ABC <0082.g1:( A B C )>`; let the centre of the circle :g:`ABC <0082.g1:( A B C )>` be taken, and let it
be :g:`F <0082.g1:F>`; let :g:`FE <0082.g1:/ F E />`, :g:`FB <0082.g1:/ F B />`, :g:`FD <0082.g1:/ F D />` be joined.

Thus the :term:`angle <plane-angle>` :g:`FED <0082.g1:< F E D )>` is right. :just:`[III. 18] <III.18>`

Now, since :g:`DE <0082.g1:/ D E />` touches the circle :g:`ABC <0082.g1:( A B C )>`, and :g:`DCA <0082.g1:/ D C A />` cuts it,
the rectangle :g:`AD <0082.g1:/ A D />`, :g:`DC <0082.g1:/ D C />` is equal to the square on :g:`DE <0082.g1:/ D E />`. :just:`[III. 36] <III.36>`

But the rectangle :g:`AD <0082.g1:/ A D />`, :g:`DC <0082.g1:/ D C />` was also equal to the square
on :g:`DB <0082.g1:/ D B />`;
therefore the square on :g:`DE <0082.g1:/ D E />` is :eq:`equal <0082.g1:/ D E / = 0082.g1:/ D B />` to the square on :g:`DB <0082.g1:/ D B />`;

.. assertion::

   therefore :g:`DE <0082.g1:/ D E />` is :eq:`equal <0082.g1:/ D E / = 0082.g1:/ D B />` to :g:`DB <0082.g1:/ D B />`.

And :g:`FE <0082.g1:/ F E />` is :eq:`equal <0082.g1:/ F E / = 0082.g1:/ F B />` to :g:`FB <0082.g1:/ F B />`;
therefore the two sides :g:`DE <0082.g1:/ D E />`, :g:`EF <0082.g1:/ E F />` are :eq:`equal <0082.g1:/ D E / = 0082.g1:/ D B /; 0082.g1:/ E F / = 0082.g1:/ B F />` to the two sides
:g:`DB <0082.g1:/ D B />`, :g:`BF <0082.g1:/ B F />`;
and :g:`FD <0082.g1:/ F D />` is the common base of the :term:`triangles <trilateral>`;

.. assertion:: [I. 8] <I.8>

   therefore the angle :g:`DEF <0082.g1:< D E F )>` is :eq:`equal <0082.g1:< D E F ) = 0082.g1:< D B F )>` to the angle :g:`DBF <0082.g1:< D B F )>`.

But the angle :g:`DEF <0082.g1:< D E F )>` is right;

.. assertion::

   therefore the angle :g:`DBF <0082.g1:< D B F )>` is also right.

And :g:`FB <0082.g1:/ F B />` produced is a :term:`diameter <diameter>`;
and the straight line drawn :term:`at right angles <right-angle>` to the diameter
of a circle, from its :term:`extremity <extremity>`, touches the circle; :just:`[III. 16, Por.]`

.. assertion::

   therefore :g:`DB <0082.g1:/ D B />` touches the circle.

Similarly this can be proved to be the case even if the
:term:`centre <centre>` be on :g:`AC <0082.g1:/ A C />`.

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
     "I.def.1" [label="I.def.1", fillcolor="#224422", tooltip="I.def.1: A point is that which has no part.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-1", target="_top"];
     "I.def.2" [label="I.def.2", fillcolor="#224422", tooltip="I.def.2: A line is breadthless length.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-2", target="_top"];
     "I.def.3" [label="I.def.3", fillcolor="#224422", tooltip="I.def.3: The extremities of a line are points.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-3", target="_top"];
     "I.def.4" [label="I.def.4", fillcolor="#224422", tooltip="I.def.4: A straight line is a line which lies evenly with the points on itself.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-4", target="_top"];
     "I.def.5" [label="I.def.5", fillcolor="#224422", tooltip="I.def.5: A surface is that which has length and breadth only.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-5", target="_top"];
     "I.def.6" [label="I.def.6", fillcolor="#224422", tooltip="I.def.6: The extremities of a surface are lines.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-6", target="_top"];
     "I.def.7" [label="I.def.7", fillcolor="#224422", tooltip="I.def.7: A plane surface is a surface which lies evenly with the straight lines on itself.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-7", target="_top"];
     "I.def.8" [label="I.def.8", fillcolor="#224422", tooltip="I.def.8: A plane angle is the inclination to one another of two lines in a plane which meet one another and do not lie in a straight line.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-8", target="_top"];
     "I.def.9" [label="I.def.9", fillcolor="#224422", tooltip="I.def.9: And when the lines containing the angle are straight, the angle is called rectilineal.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-9", target="_top"];
     "I.def.10" [label="I.def.10", fillcolor="#224422", tooltip="I.def.10: When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-10", target="_top"];
     "I.def.11" [label="I.def.11", fillcolor="#224422", tooltip="I.def.11: An obtuse angle is an angle greater than a right angle.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-11", target="_top"];
     "I.def.12" [label="I.def.12", fillcolor="#224422", tooltip="I.def.12: An acute angle is an angle less than a right angle.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-12", target="_top"];
     "I.def.13" [label="I.def.13", fillcolor="#224422", tooltip="I.def.13: A boundary is that which is an extremity of anything.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-13", target="_top"];
     "I.def.14" [label="I.def.14", fillcolor="#224422", tooltip="I.def.14: A figure is that which is contained by any boundary or boundaries.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-14", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", tooltip="I.def.15: A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-15", target="_top"];
     "I.def.16" [label="I.def.16", fillcolor="#224422", tooltip="I.def.16: And the point is called the centre of the circle.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-16", target="_top"];
     "I.def.17" [label="I.def.17", fillcolor="#224422", tooltip="I.def.17: A diameter of the circle is any straight line drawn through the centre and terminated in both directions by the circumference of the circle, and such a straight line also bisects…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-17", target="_top"];
     "I.def.19" [label="I.def.19", fillcolor="#224422", tooltip="I.def.19: Rectilineal figures are those which are contained by straight lines, trilateral figures being those contained by three, quadrilateral those contained by four, and multilateral…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-19", target="_top"];
     "I.def.20" [label="I.def.20", fillcolor="#224422", tooltip="I.def.20: Of trilateral figures, an equilateral triangle is that which has its three sides equal, an isosceles triangle that which has two of its sides alone equal, and a scalene triangle…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-20", target="_top"];
     "I.def.21" [label="I.def.21", fillcolor="#224422", tooltip="I.def.21: Further, of trilateral figures, a right-angled triangle is that which has a right angle, an obtuse-angled triangle that which has an obtuse angle, and an acute-angled triangle…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-21", target="_top"];
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
     "I.14" [label="I.14", fillcolor="#222244", tooltip="I.14: If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be…", URL="../../../../volume_I/book_i/propositions/14/index.html", target="_top"];
     "I.15" [label="I.15", fillcolor="#222244", tooltip="I.15: If two straight lines cut one another, they make the vertical angles equal to one another.", URL="../../../../volume_I/book_i/propositions/15/index.html", target="_top"];
     "I.16" [label="I.16", fillcolor="#222244", tooltip="I.16: In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", URL="../../../../volume_I/book_i/propositions/16/index.html", target="_top"];
     "I.17" [label="I.17", fillcolor="#222244", tooltip="I.17: In any triangle two angles taken together in any manner are less than two right angles.", URL="../../../../volume_I/book_i/propositions/17/index.html", target="_top"];
     "I.18" [label="I.18", fillcolor="#222244", tooltip="I.18: In any triangle the greater side subtends the greater angle.", URL="../../../../volume_I/book_i/propositions/18/index.html", target="_top"];
     "I.19" [label="I.19", fillcolor="#222244", tooltip="I.19: In any triangle the greater angle is subtended by the greater side.", URL="../../../../volume_I/book_i/propositions/19/index.html", target="_top"];
     "I.20" [label="I.20", fillcolor="#222244", tooltip="I.20: In any triangle two sides taken together in any manner are greater than the remaining one.", URL="../../../../volume_I/book_i/propositions/20/index.html", target="_top"];
     "I.22" [label="I.22", fillcolor="#222244", tooltip="I.22: Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any…", URL="../../../../volume_I/book_i/propositions/22/index.html", target="_top"];
     "I.23" [label="I.23", fillcolor="#222244", tooltip="I.23: On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", URL="../../../../volume_I/book_i/propositions/23/index.html", target="_top"];
     "I.26" [label="I.26", fillcolor="#222244", tooltip="I.26: If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one…", URL="../../../../volume_I/book_i/propositions/26/index.html", target="_top"];
     "I.27" [label="I.27", fillcolor="#222244", tooltip="I.27: If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", URL="../../../../volume_I/book_i/propositions/27/index.html", target="_top"];
     "I.29" [label="I.29", fillcolor="#222244", tooltip="I.29: A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior…", URL="../../../../volume_I/book_i/propositions/29/index.html", target="_top"];
     "I.31" [label="I.31", fillcolor="#222244", tooltip="I.31: Through a given point to draw a straight line parallel to a given straight line.", URL="../../../../volume_I/book_i/propositions/31/index.html", target="_top"];
     "I.33" [label="I.33", fillcolor="#222244", tooltip="I.33: The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.", URL="../../../../volume_I/book_i/propositions/33/index.html", target="_top"];
     "I.34" [label="I.34", fillcolor="#222244", tooltip="I.34: In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.", URL="../../../../volume_I/book_i/propositions/34/index.html", target="_top"];
     "I.35" [label="I.35", fillcolor="#222244", tooltip="I.35: Parallelograms which are on the same base and in the same parallels are equal to one another.", URL="../../../../volume_I/book_i/propositions/35/index.html", target="_top"];
     "I.36" [label="I.36", fillcolor="#222244", tooltip="I.36: Parallelograms which are on equal bases and in the same parallels are equal to one another.", URL="../../../../volume_I/book_i/propositions/36/index.html", target="_top"];
     "I.37" [label="I.37", fillcolor="#222244", tooltip="I.37: Triangles which are on the same base and in the same parallels are equal to one another.", URL="../../../../volume_I/book_i/propositions/37/index.html", target="_top"];
     "I.41" [label="I.41", fillcolor="#222244", tooltip="I.41: If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.", URL="../../../../volume_I/book_i/propositions/41/index.html", target="_top"];
     "I.43" [label="I.43", fillcolor="#222244", tooltip="I.43: In any parallelogram the complements of the parallelograms about the diameter are equal to one another.", URL="../../../../volume_I/book_i/propositions/43/index.html", target="_top"];
     "I.46" [label="I.46", fillcolor="#222244", tooltip="I.46: On a given straight line to describe a square.", URL="../../../../volume_I/book_i/propositions/46/index.html", target="_top"];
     "I.47" [label="I.47", fillcolor="#222244", tooltip="I.47: In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.", URL="../../../../volume_I/book_i/propositions/47/index.html", target="_top"];
     "II.def.1" [label="II.def.1", fillcolor="#224422", tooltip="II.def.1: Any rectangular parallelogram is said to be contained by the two straight lines containing the right angle.", URL="../../../../volume_I/book_ii/definitions/index.html#ii-def-1", target="_top"];
     "II.def.2" [label="II.def.2", fillcolor="#224422", tooltip="II.def.2: And in any parallelogrammic area let any one whatever of the parallelograms about its diameter with the two complements be called a gnomon.", URL="../../../../volume_I/book_ii/definitions/index.html#ii-def-2", target="_top"];
     "II.6" [label="II.6", fillcolor="#222244", tooltip="II.6: If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line…", URL="../../../../volume_I/book_ii/propositions/06/index.html", target="_top"];
     "III.def.2" [label="III.def.2", fillcolor="#224422", tooltip="III.def.2: A straight line is said to touch a circle which, meeting the circle and being produced, does not cut the circle.", URL="../../definitions/index.html#iii-def-2", target="_top"];
     "III.def.7" [label="III.def.7", fillcolor="#224422", tooltip="III.def.7: An angle of a segment is that contained by a straight line and a circumference of a circle.", URL="../../definitions/index.html#iii-def-7", target="_top"];
     "III.3" [label="III.3", fillcolor="#222244", tooltip="III.3: If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects…", URL="../03/index.html", target="_top"];
     "III.16" [label="III.16", fillcolor="#222244", tooltip="III.16: The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the…", URL="../16/index.html", target="_top"];
     "III.18" [label="III.18", fillcolor="#222244", tooltip="III.18: If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.", URL="../18/index.html", target="_top"];
     "III.36" [label="III.36", fillcolor="#222244", tooltip="III.36: If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the circle and the other touch it, the rectangle contained by…", URL="../36/index.html", target="_top"];
     "III.37" [label="III.37", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.37: If a point be taken outside a circle and from the point there fall on the circle two straight lines, if one of them cut the circle, and the other fall on it, and if further the…", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.15" -> "I.def.1";
     "I.def.16" -> "I.def.1";
     "I.post.1" -> "I.def.1";
     "I.2" -> "I.def.1";
     "I.7" -> "I.def.1";
     "I.11" -> "I.def.1";
     "I.14" -> "I.def.1";
     "I.23" -> "I.def.1";
     "I.31" -> "I.def.1";
     "III.18" -> "I.def.1";
     "III.36" -> "I.def.1";
     "III.37" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.6" -> "I.def.2";
     "I.def.8" -> "I.def.2";
     "I.def.9" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.13" -> "I.def.3";
     "I.2" -> "I.def.3";
     "I.7" -> "I.def.3";
     "I.33" -> "I.def.3";
     "III.16" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.8" -> "I.def.4";
     "I.def.10" -> "I.def.4";
     "I.def.15" -> "I.def.4";
     "I.def.17" -> "I.def.4";
     "I.def.19" -> "I.def.4";
     "I.def.23" -> "I.def.4";
     "I.post.1" -> "I.def.4";
     "I.post.2" -> "I.def.4";
     "I.post.5" -> "I.def.4";
     "I.1" -> "I.def.4";
     "I.2" -> "I.def.4";
     "I.3" -> "I.def.4";
     "I.4" -> "I.def.4";
     "I.5" -> "I.def.4";
     "I.7" -> "I.def.4";
     "I.8" -> "I.def.4";
     "I.10" -> "I.def.4";
     "I.11" -> "I.def.4";
     "I.13" -> "I.def.4";
     "I.14" -> "I.def.4";
     "I.15" -> "I.def.4";
     "I.22" -> "I.def.4";
     "I.23" -> "I.def.4";
     "I.27" -> "I.def.4";
     "I.29" -> "I.def.4";
     "I.31" -> "I.def.4";
     "I.33" -> "I.def.4";
     "I.46" -> "I.def.4";
     "II.def.1" -> "I.def.4";
     "II.6" -> "I.def.4";
     "III.def.2" -> "I.def.4";
     "III.def.7" -> "I.def.4";
     "III.3" -> "I.def.4";
     "III.16" -> "I.def.4";
     "III.18" -> "I.def.4";
     "III.36" -> "I.def.4";
     "III.37" -> "I.def.4";
     "I.def.6" -> "I.def.5";
     "I.def.7" -> "I.def.5";
     "I.def.15" -> "I.def.6";
     "I.def.8" -> "I.def.7";
     "I.def.15" -> "I.def.7";
     "I.def.23" -> "I.def.7";
     "I.def.9" -> "I.def.8";
     "I.def.10" -> "I.def.8";
     "I.def.11" -> "I.def.8";
     "I.def.12" -> "I.def.8";
     "I.def.21" -> "I.def.8";
     "I.def.22" -> "I.def.8";
     "I.post.5" -> "I.def.8";
     "I.4" -> "I.def.8";
     "I.5" -> "I.def.8";
     "I.8" -> "I.def.8";
     "I.13" -> "I.def.8";
     "I.14" -> "I.def.8";
     "I.15" -> "I.def.8";
     "I.16" -> "I.def.8";
     "I.17" -> "I.def.8";
     "I.18" -> "I.def.8";
     "I.19" -> "I.def.8";
     "I.26" -> "I.def.8";
     "I.27" -> "I.def.8";
     "I.29" -> "I.def.8";
     "I.34" -> "I.def.8";
     "III.16" -> "I.def.8";
     "I.9" -> "I.def.9";
     "I.23" -> "I.def.9";
     "III.16" -> "I.def.9";
     "I.def.11" -> "I.def.10";
     "I.def.12" -> "I.def.10";
     "I.def.21" -> "I.def.10";
     "I.post.4" -> "I.def.10";
     "I.post.5" -> "I.def.10";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.14" -> "I.def.10";
     "I.17" -> "I.def.10";
     "I.29" -> "I.def.10";
     "I.47" -> "I.def.10";
     "II.def.1" -> "I.def.10";
     "III.3" -> "I.def.10";
     "III.16" -> "I.def.10";
     "III.18" -> "I.def.10";
     "I.def.21" -> "I.def.11";
     "I.def.21" -> "I.def.12";
     "III.16" -> "I.def.12";
     "III.18" -> "I.def.12";
     "I.def.14" -> "I.def.13";
     "I.def.15" -> "I.def.14";
     "I.4" -> "I.def.14";
     "I.def.16" -> "I.def.15";
     "I.def.17" -> "I.def.15";
     "I.post.3" -> "I.def.15";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.def.2" -> "I.def.15";
     "III.def.7" -> "I.def.15";
     "III.3" -> "I.def.15";
     "III.16" -> "I.def.15";
     "III.36" -> "I.def.15";
     "III.37" -> "I.def.15";
     "I.def.17" -> "I.def.16";
     "I.post.3" -> "I.def.16";
     "III.3" -> "I.def.16";
     "III.18" -> "I.def.16";
     "I.34" -> "I.def.17";
     "I.43" -> "I.def.17";
     "II.def.2" -> "I.def.17";
     "III.16" -> "I.def.17";
     "I.def.20" -> "I.def.19";
     "I.def.21" -> "I.def.19";
     "I.def.22" -> "I.def.19";
     "I.4" -> "I.def.19";
     "I.8" -> "I.def.19";
     "I.16" -> "I.def.19";
     "I.17" -> "I.def.19";
     "I.18" -> "I.def.19";
     "I.19" -> "I.def.19";
     "I.20" -> "I.def.19";
     "I.22" -> "I.def.19";
     "I.26" -> "I.def.19";
     "I.37" -> "I.def.19";
     "I.41" -> "I.def.19";
     "I.def.22" -> "I.def.20";
     "I.1" -> "I.def.20";
     "I.5" -> "I.def.20";
     "I.47" -> "I.def.21";
     "I.35" -> "I.def.22";
     "I.46" -> "I.def.22";
     "I.47" -> "I.def.22";
     "II.6" -> "I.def.22";
     "I.27" -> "I.def.23";
     "I.29" -> "I.def.23";
     "I.31" -> "I.def.23";
     "I.33" -> "I.def.23";
     "I.35" -> "I.def.23";
     "I.36" -> "I.def.23";
     "I.37" -> "I.def.23";
     "I.41" -> "I.def.23";
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
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.29" -> "I.post.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.43" -> "I.cn.3";
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
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.20" -> "I.5";
     "III.3" -> "I.5";
     "III.16" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.3" -> "I.8";
     "III.37" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.47" -> "I.14";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "III.16" -> "I.17";
     "III.18" -> "I.17";
     "I.19" -> "I.18";
     "I.20" -> "I.19";
     "III.16" -> "I.19";
     "III.18" -> "I.19";
     "I.22" -> "I.20";
     "I.23" -> "I.22";
     "I.31" -> "I.23";
     "I.34" -> "I.26";
     "III.3" -> "I.26";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "II.6" -> "I.31";
     "I.36" -> "I.33";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.43" -> "I.34";
     "I.46" -> "I.34";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "II.6" -> "I.36";
     "I.41" -> "I.37";
     "I.47" -> "I.41";
     "II.6" -> "I.43";
     "I.47" -> "I.46";
     "II.6" -> "I.46";
     "III.36" -> "I.47";
     "II.6" -> "II.def.1";
     "III.36" -> "II.def.1";
     "III.37" -> "II.def.1";
     "II.6" -> "II.def.2";
     "III.36" -> "II.6";
     "III.16" -> "III.def.2";
     "III.18" -> "III.def.2";
     "III.16" -> "III.def.7";
     "III.36" -> "III.3";
     "III.37" -> "III.16";
     "III.36" -> "III.18";
     "III.37" -> "III.18";
     "III.37" -> "III.36";
   }

Required for
------------

:ref:`IV.10 <IV.10>`, :ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`

----

See :ref:`Commentary on Proposition III.37 <III.37.commentary>`.

.. toctree::
   :hidden:

   commentary
