:canonical_id: III.4
:volume: II
:book: III
:proposition: 4
:type: proposition
:title: Proposition III.4
:folios: 0017, 0018
:folio: 0017
:page: 11
:pages: 11, 12
:dependencies: I.def.4, I.def.15, I.def.16, III.1, III.3

.. _III.4:

.. folio:: 0017
   :page: 11

PROPOSITION 4.
==============

.. enunciation::

   If in a :term:`circle <circle>` two :term:`straight lines <straight-line>` cut one another which are not through the :term:`centre <centre>`, they do not bisect one another.

Let :g:`ABCD <0017.g1:( A B C D )>` be a circle, and in it let the two straight lines :g:`AC <0017.g1:/ A C />`, :g:`BD <0017.g1:/ B D />`, which are not through the centre, cut one another at :g:`E <0017.g1:E>`;

I say that they do not bisect one another.

.. picture:: 0017.g1.svg
   :alt: Proposition 4

For, if possible, let them :eq:`bisect <0017.g1:/ A E / = 0017.g1:/ E C /; 0017.g1:/ B E / = 0017.g1:/ E D />` one another, so that :g:`AE <0017.g1:/ A E />` is :eq:`equal <0017.g1:/ A E / = 0017.g1:/ E C /; 0017.g1:/ B E / = 0017.g1:/ E D />` to :g:`EC <0017.g1:/ E C />`, and :g:`BE <0017.g1:/ B E />` to :g:`ED <0017.g1:/ E D />`; let the centre of the circle :g:`ABCD <0017.g1:( A B C D )>` be taken :just:`[III. 1] <III.1>`, and let it be :g:`F <0017.g1:F>`; let :g:`FE <0017.g1:/ F E />` be joined.

Then, since a straight line :g:`FE <0017.g1:/ F E />` through the centre :eq:`bisects <0017.g1:/ A E / = 0017.g1:/ E C />` a straight line :g:`AC <0017.g1:/ A C />` not through the centre,

.. subclause:: [III. 3] <III.3>

   it also cuts it :term:`at right angles <right-angle>`;

.. assertion::

   therefore the :term:`angle <plane-angle>` :g:`FEA <0017.g1:< F E A )>` is right.

Again, since a straight line :g:`FE <0017.g1:/ F E />` :eq:`bisects <0017.g1:/ B E / = 0017.g1:/ E D />` a straight line :g:`BD <0017.g1:/ B D />`,

.. subclause:: [III. 3] <III.3>

   it also cuts it at right angles;

.. assertion::

   therefore the angle :g:`FEB <0017.g1:< F E B )>` is right.

.. _folio-ii-0018:

.. folio:: 0018
   :page: 12

But the angle :g:`FEA <0017.g1:< F E A )>` was also proved right; therefore the angle :g:`FEA <0017.g1:< F E A )>` is :eq:`equal <0017.g1:< F E A ) = 0017.g1:< F E B )>` to the angle :g:`FEB <0017.g1:< F E B )>`, the less to the greater: which is impossible.

.. assertion::

   Therefore :g:`AC <0017.g1:/ A C />`, :g:`BD <0017.g1:/ B D />` do not bisect one another.

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
     "I.def.13" [label="I.def.13", fillcolor="#224422", tooltip="I.def.13: A boundary is that which is an extremity of anything.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-13", target="_top"];
     "I.def.14" [label="I.def.14", fillcolor="#224422", tooltip="I.def.14: A figure is that which is contained by any boundary or boundaries.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-14", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", tooltip="I.def.15: A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-15", target="_top"];
     "I.def.16" [label="I.def.16", fillcolor="#224422", tooltip="I.def.16: And the point is called the centre of the circle.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-16", target="_top"];
     "I.def.19" [label="I.def.19", fillcolor="#224422", tooltip="I.def.19: Rectilineal figures are those which are contained by straight lines, trilateral figures being those contained by three, quadrilateral those contained by four, and multilateral…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-19", target="_top"];
     "I.def.20" [label="I.def.20", fillcolor="#224422", tooltip="I.def.20: Of trilateral figures, an equilateral triangle is that which has its three sides equal, an isosceles triangle that which has two of its sides alone equal, and a scalene triangle…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-20", target="_top"];
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
     "I.26" [label="I.26", fillcolor="#222244", tooltip="I.26: If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one…", URL="../../../../volume_I/book_i/propositions/26/index.html", target="_top"];
     "III.1" [label="III.1", fillcolor="#222244", tooltip="III.1: To find the centre of a given circle.", URL="../01/index.html", target="_top"];
     "III.3" [label="III.3", fillcolor="#222244", tooltip="III.3: If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects…", URL="../03/index.html", target="_top"];
     "III.4" [label="III.4", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.4: If in a circle two straight lines cut one another which are not through the centre, they do not bisect one another.", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.15" -> "I.def.1";
     "I.def.16" -> "I.def.1";
     "I.post.1" -> "I.def.1";
     "I.2" -> "I.def.1";
     "I.7" -> "I.def.1";
     "I.11" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.6" -> "I.def.2";
     "I.def.8" -> "I.def.2";
     "I.def.9" -> "I.def.2";
     "I.def.4" -> "I.def.3";
     "I.def.13" -> "I.def.3";
     "I.2" -> "I.def.3";
     "I.7" -> "I.def.3";
     "I.def.7" -> "I.def.4";
     "I.def.8" -> "I.def.4";
     "I.def.10" -> "I.def.4";
     "I.def.15" -> "I.def.4";
     "I.def.19" -> "I.def.4";
     "I.post.1" -> "I.def.4";
     "I.post.2" -> "I.def.4";
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
     "I.15" -> "I.def.4";
     "III.3" -> "I.def.4";
     "III.4" -> "I.def.4";
     "I.def.6" -> "I.def.5";
     "I.def.7" -> "I.def.5";
     "I.def.15" -> "I.def.6";
     "I.def.8" -> "I.def.7";
     "I.def.15" -> "I.def.7";
     "I.def.9" -> "I.def.8";
     "I.def.10" -> "I.def.8";
     "I.4" -> "I.def.8";
     "I.5" -> "I.def.8";
     "I.8" -> "I.def.8";
     "I.13" -> "I.def.8";
     "I.15" -> "I.def.8";
     "I.16" -> "I.def.8";
     "I.26" -> "I.def.8";
     "I.9" -> "I.def.9";
     "I.post.4" -> "I.def.10";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
     "III.3" -> "I.def.10";
     "I.def.14" -> "I.def.13";
     "I.def.15" -> "I.def.14";
     "I.4" -> "I.def.14";
     "I.def.16" -> "I.def.15";
     "I.post.3" -> "I.def.15";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.1" -> "I.def.15";
     "III.3" -> "I.def.15";
     "III.4" -> "I.def.15";
     "I.post.3" -> "I.def.16";
     "III.1" -> "I.def.16";
     "III.3" -> "I.def.16";
     "III.4" -> "I.def.16";
     "I.def.20" -> "I.def.19";
     "I.4" -> "I.def.19";
     "I.8" -> "I.def.19";
     "I.16" -> "I.def.19";
     "I.26" -> "I.def.19";
     "I.1" -> "I.def.20";
     "I.5" -> "I.def.20";
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
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.7" -> "I.5";
     "III.3" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.1" -> "I.8";
     "III.3" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.16" -> "I.15";
     "I.26" -> "I.16";
     "III.3" -> "I.26";
     "III.4" -> "III.1";
     "III.4" -> "III.3";
   }
