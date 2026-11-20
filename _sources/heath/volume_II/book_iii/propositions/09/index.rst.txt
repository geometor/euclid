:canonical_id: III.9
:volume: II
:book: III
:proposition: 9
:type: proposition
:title: Proposition III.9
:folios: 0027, 0028
:folio: 0027
:page: 21
:pages: 21, 22
:dependencies: I.def.1, I.def.4, I.def.10, I.def.15, I.def.16, I.8, III.1

.. _III.9:

.. folio:: 0027
   :page: 21

PROPOSITION 9.
==============

.. enunciation::

   If a :term:`point <point>` be taken within a :term:`circle <circle>`, and more than two equal :term:`straight lines <straight-line>` fall from the point on the circle, the point taken is the :term:`centre <centre>` of the circle.

Let :g:`ABC <0027.g1:( A B C )>` be a circle and :g:`D <0027.g1:D>` a point within it, and from :g:`D <0027.g1:D>` let more than two :eq:`equal <0027.g1:/ D A / = 0027.g1:/ D B / = 0027.g1:/ D C />` straight lines, namely :g:`DA <0027.g1:/ D A />`, :g:`DB <0027.g1:/ D B />`, :g:`DC <0027.g1:/ D C />`, fall on the circle :g:`ABC <0027.g1:( A B C )>`;

I say that the point :g:`D <0027.g1:D>` is the centre of the circle :g:`ABC <0027.g1:( A B C )>`.

.. picture:: 0027.g1.svg
   :alt: Diagram for Proposition 9

For let :g:`AB <0027.g1:/ A B />`, :g:`BC <0027.g1:/ B C />` be joined and :eq:`bisected <0027.g1:/ A E / = 0027.g1:/ E B /; 0027.g1:/ B F / = 0027.g1:/ F C />` at the points :g:`E <0027.g1:E>`, :g:`F <0027.g1:F>`, and let :g:`ED <0027.g1:/ E D />`, :g:`FD <0027.g1:/ F D />` be joined and drawn through to the points :g:`G <0027.g1:G>`, :g:`K <0027.g1:K>`, :g:`H <0027.g1:H>`, :g:`L <0027.g1:L>`.

Then, since :g:`AE <0027.g1:/ A E />` is :eq:`equal <0027.g1:/ A E / = 0027.g1:/ E B />` to :g:`EB <0027.g1:/ E B />`, and :g:`ED <0027.g1:/ E D />` is common,

.. subclause::

   the two sides :g:`AE <0027.g1:/ A E />`, :g:`ED <0027.g1:/ E D />` are :eq:`equal <0027.g1:/ A E / = 0027.g1:/ B E />` to the two sides :g:`BE <0027.g1:/ B E />`, :g:`ED <0027.g1:/ E D />`;

and the base :g:`DA <0027.g1:/ D A />` is :eq:`equal <0027.g1:/ D A / = 0027.g1:/ D B />` to the base :g:`DB <0027.g1:/ D B />`;

.. assertion:: [I. 8] <I.8>

   therefore the :term:`angle <plane-angle>` :g:`AED <0027.g1:< A E D )>` is :eq:`equal <0027.g1:< A E D ) = 0027.g1:< B E D )>` to the angle :g:`BED <0027.g1:< B E D )>`.

.. assertion:: [I. Def. 10] <I.def.10>

   Therefore each of the angles :g:`AED <0027.g1:< A E D )>`, :g:`BED <0027.g1:< B E D )>` is :eq:`right <0027.g1:< A E D ) = 0027.g1:< B E D )>`;

therefore :g:`GK <0027.g1:/ G K />` cuts :g:`AB <0027.g1:/ A B />` into two :eq:`equal <0027.g1:/ A E / = 0027.g1:/ E B />` parts and at :eq:`right angles <0027.g1:< A E D ) = 0027.g1:< B E D )>`.

And since, if in a circle a straight line cut a straight line into two equal parts and :term:`at right angles <right-angle>`, the centre of the circle is on the cutting straight line, :just:`[III. 1, Por.]`

.. assertion::

   the centre of the circle is on :g:`GK <0027.g1:/ G K />`.

.. _folio-ii-0028:

.. folio:: 0028
   :page: 22

For the same reason

.. assertion::

   the centre of the circle :g:`ABC <0027.g1:( A B C )>` is also on :g:`HL <0027.g1:/ H L />`.

And the straight lines :g:`GK <0027.g1:/ G K />`, :g:`HL <0027.g1:/ H L />` have no other point common but the point :g:`D <0027.g1:D>`;

.. assertion::

   therefore the point :g:`D <0027.g1:D>` is the centre of the circle :g:`ABC <0027.g1:( A B C )>`.

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
     "III.1" [label="III.1", fillcolor="#222244", tooltip="III.1: To find the centre of a given circle.", URL="../01/index.html", target="_top"];
     "III.9" [label="III.9", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.9: If a point be taken within a circle, and more than two equal straight lines fall from the point on the circle, the point taken is the centre of the circle.", URL="index.html", target="_top"];
     "I.def.3" -> "I.def.1";
     "I.def.4" -> "I.def.1";
     "I.def.15" -> "I.def.1";
     "I.def.16" -> "I.def.1";
     "I.post.1" -> "I.def.1";
     "I.2" -> "I.def.1";
     "I.7" -> "I.def.1";
     "III.9" -> "I.def.1";
     "I.def.3" -> "I.def.2";
     "I.def.4" -> "I.def.2";
     "I.def.6" -> "I.def.2";
     "I.def.8" -> "I.def.2";
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
     "III.9" -> "I.def.4";
     "I.def.6" -> "I.def.5";
     "I.def.7" -> "I.def.5";
     "I.def.15" -> "I.def.6";
     "I.def.8" -> "I.def.7";
     "I.def.15" -> "I.def.7";
     "I.def.10" -> "I.def.8";
     "I.4" -> "I.def.8";
     "I.5" -> "I.def.8";
     "I.8" -> "I.def.8";
     "III.1" -> "I.def.10";
     "III.9" -> "I.def.10";
     "I.def.14" -> "I.def.13";
     "I.def.15" -> "I.def.14";
     "I.4" -> "I.def.14";
     "I.def.16" -> "I.def.15";
     "I.post.3" -> "I.def.15";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.1" -> "I.def.15";
     "III.9" -> "I.def.15";
     "I.post.3" -> "I.def.16";
     "III.1" -> "I.def.16";
     "III.9" -> "I.def.16";
     "I.def.20" -> "I.def.19";
     "I.4" -> "I.def.19";
     "I.8" -> "I.def.19";
     "I.1" -> "I.def.20";
     "I.5" -> "I.def.20";
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
     "III.9" -> "I.8";
     "III.9" -> "III.1";
   }

Required for
------------

:ref:`III.25 <III.25>`

----

See :ref:`Commentary on Proposition III.9 <III.9.commentary>`.

.. toctree::
   :hidden:

   commentary
