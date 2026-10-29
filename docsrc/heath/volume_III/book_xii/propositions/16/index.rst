:canonical_id: XII.16
:volume: III
:book: XII
:proposition: 16
:type: proposition
:title: Proposition XII.16
:folios: 0427, 0428
:pages: 423, 424
:dependencies: I.4, III.3, III.16, X.1

.. _XII.16:

.. folio:: 0427
   :page: 423

PROPOSITION 16.
===============

.. enunciation::

   Given two circles about the same centre, to inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle.

.. _folio-iii-0428:

.. folio:: 0428
   :page: 424

Let :g:`ABCD <0428.g1:( A B C D )>`, :g:`EFGH <0428.g1:( E F G H )>` be the two given circles about the same centre :g:`K <0428.g1:K>` ; thus it is required to inscribe in the greater circle :g:`ABCD <0428.g1:( A B C D )>` an equilateral polygon with an even number of sides which does not touch the circle :g:`EFGH <0428.g1:( E F G H )>`.

.. picture:: 0428.g1.svg
   :alt: Proposition 16

For let the straight line :g:`BKD <0428.g1:/ B K D />` be drawn through the centre :g:`K <0428.g1:K>`, and from the point :g:`G <0428.g1:G>` let :g:`GA <0428.g1:/ G A />` be drawn at right angles to the straight line :g:`BD <0428.g1:/ B D />` and carried through to :g:`C <0428.g1:C>` ;

.. assertion:: [III. 16, Por.]

   therefore :g:`AC <0428.g1:/ A C />` touches the circle :g:`EFGH <0428.g1:( E F G H )>`.

Then, bisecting the circumference :g:`BAD <0428.g1:( B A D )>`, bisecting the half of it, and doing this continually, we shall leave a circumference less than :g:`AD <0428.g1:( A D )>`. :just:`[X. 1] <X.1>` Let such be left, and let it be :g:`LD <0428.g1:( L D )>` ; from :g:`L <0428.g1:L>` let :g:`LM <0428.g1:/ L M />` be drawn perpendicular to :g:`BD <0428.g1:/ B D />` and carried through to :g:`N <0428.g1:N>`, and let :g:`LD <0428.g1:/ L D />`, :g:`DN <0428.g1:/ D N />` be joined ;

.. assertion:: [III. 3, I. 4] <III.3, I.4>

   therefore :g:`LD <0428.g1:/ L D />` is :eq:`equal <0428.g1:/ L D / = 0428.g1:/ D N />` to :g:`DN <0428.g1:/ D N />`.

.. subclause::

   Now, since :g:`LN <0428.g1:/ L N />` is parallel to :g:`AC <0428.g1:/ A C />`, and :g:`AC <0428.g1:/ A C />` touches the circle :g:`EFGH <0428.g1:( E F G H )>`,

.. assertion::

   therefore :g:`LN <0428.g1:/ L N />` does not touch the circle :g:`EFGH <0428.g1:( E F G H )>` ; therefore :g:`LD <0428.g1:/ L D />`, :g:`DN <0428.g1:/ D N />` are far from touching the circle :g:`EFGH <0428.g1:( E F G H )>`.

.. qed::

   If then we fit into the circle :g:`ABCD <0428.g1:( A B C D )>` straight lines equal to the straight line :g:`LD <0428.g1:/ L D />` and placed continuously, there will be inscribed in the circle :g:`ABCD <0428.g1:( A B C D )>` an equilateral polygon with an even number of sides which does not touch the lesser circle :g:`EFGH <0428.g1:( E F G H )>`. :just:`Q. E. F.`

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
     "I.17" [label="I.17", fillcolor="#222244", tooltip="I.17: In any triangle two angles taken together in any manner are less than two right angles.", URL="../../../../volume_I/book_i/propositions/17/index.html", target="_top"];
     "I.18" [label="I.18", fillcolor="#222244", tooltip="I.18: In any triangle the greater side subtends the greater angle.", URL="../../../../volume_I/book_i/propositions/18/index.html", target="_top"];
     "I.19" [label="I.19", fillcolor="#222244", tooltip="I.19: In any triangle the greater angle is subtended by the greater side.", URL="../../../../volume_I/book_i/propositions/19/index.html", target="_top"];
     "I.26" [label="I.26", fillcolor="#222244", tooltip="I.26: If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one…", URL="../../../../volume_I/book_i/propositions/26/index.html", target="_top"];
     "III.3" [label="III.3", fillcolor="#222244", tooltip="III.3: If in a circle a straight line through the centre bisect a straight line not through the centre, it also cuts it at right angles; and if it cut it at right angles, it also bisects…", URL="../../../../volume_II/book_iii/propositions/03/index.html", target="_top"];
     "III.16" [label="III.16", fillcolor="#222244", tooltip="III.16: The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the…", URL="../../../../volume_II/book_iii/propositions/16/index.html", target="_top"];
     "V.def.4" [label="V.def.4", fillcolor="#224422", tooltip="V.def.4: Magnitudes are said to have a ratio to one another which are capable, when multiplied, of exceeding one another.", URL="../../../../volume_II/book_v/definitions/index.html#v-def-4", target="_top"];
     "X.1" [label="X.1", fillcolor="#222244", tooltip="X.1: Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and…", URL="../../../book_x/propositions/001/index.html", target="_top"];
     "XII.16" [label="XII.16", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="XII.16: Given two circles about the same centre, to inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle.", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.3" -> "I.def.10";
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
     "I.17" -> "I.post.2";
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
     "I.26" -> "I.4";
     "XII.16" -> "I.4";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.3" -> "I.5";
     "III.16" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.3" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.16" -> "I.15";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "III.16" -> "I.17";
     "I.19" -> "I.18";
     "III.16" -> "I.19";
     "III.3" -> "I.26";
     "XII.16" -> "III.3";
     "XII.16" -> "III.16";
     "X.1" -> "V.def.4";
     "XII.16" -> "X.1";
   }

----

See :ref:`Commentary on Proposition XII.16 <XII.16.commentary>`.

.. toctree::
   :hidden:

   commentary
