:canonical_id: III.13
:volume: II
:book: III
:proposition: 13
:type: proposition
:title: Proposition III.13
:folios: 0038, 0039
:pages: 32, 33
:dependencies: III.def.3, III.2, III.11

.. _III.13:

.. folio:: 0038
   :page: 32

PROPOSITION 13.
===============

.. enunciation::

   A circle does not touch a circle at more points than one, whether it touch it internally or externally.

For, if possible, let the circle :g:`$ABDC$ <0038.g3:( A B D C )>`\ [#f1]_ touch the circle
:g:`$EBFD$ <0038.g3:( E B F D )>`, first internally, at more
points than one, namely :g:`$D$ <0038.g3:D>`, :g:`$B$ <0038.g3:B>`.

.. picture:: 0038.g3.svg
   :alt: Proposition 13 diagram

Let the centre :g:`$G$ <0038.g3:G>` of the circle
:g:`$ABDC$ <0038.g3:( A B D C )>`, and the centre :g:`$H$ <0038.g3:H>` of
:g:`$EBFD$ <0038.g3:( E B F D )>`, be taken.

Therefore the straight line
joined from :g:`$G$ <0038.g3:G>` to :g:`$H$ <0038.g3:H>` will fall on
:g:`$B$ <0038.g3:B>`, :g:`$D$ <0038.g3:D>`. :just:`[III. 11] <III.11>`

Let it so fall, as :g:`$BGHD$ <0038.g3:/ B G H D />`.

Then, since the point :g:`$G$ <0038.g3:G>` is
the centre of the circle :g:`$ABCD$ <0038.g3:( A B C D )>`,

.. assertion::

   :g:`$BG$ <0038.g3:/ B G />` is :eq:`equal <0038.g3:/ B G / = 0038.g3:/ G D />` to :g:`$GD$ <0038.g3:/ G D />`;

.. _folio-ii-0039:

.. folio:: 0039
   :page: 33

.. assertion::

   therefore :g:`$BG$ <0038.g3:/ B G />` is greater than :g:`$HD$ <0038.g3:/ H D />`;

.. assertion::

   therefore :g:`$BH$ <0038.g3:/ B H />` is much greater than :g:`$HD$ <0038.g3:/ H D />`.

Again, since the point :g:`$H$ <0038.g3:H>` is the centre of the circle
:g:`$EBFD$ <0038.g3:( E B F D )>`,

.. assertion::

   :g:`$BH$ <0038.g3:/ B H />` is :eq:`equal <0038.g3:/ B H / = 0038.g3:/ H D />` to :g:`$HD$ <0038.g3:/ H D />`;

but it was also proved much greater than it: which is
impossible.

Therefore a circle does not touch a circle internally at
more points than one.

I say further that neither does it so touch it\ [#f2]_ externally.

For, if possible, let the circle :g:`$ACK$ <0038.g3:( A C K )>` touch the circle
:g:`$ABDC$ <0038.g3:( A B D C )>`\ [#f1]_ at more points than one, namely :g:`$A$ <0038.g3:A>`, :g:`$C$ <0038.g3:C>`,
and let :g:`$AC$ <0038.g3:/ A C />` be joined.

Then, since on the circumference of each of the circles
:g:`$ABDC$ <0038.g3:( A B D C )>`, :g:`$ACK$ <0038.g3:( A C K )>` two points :g:`$A$ <0038.g3:A>`, :g:`$C$ <0038.g3:C>` have been taken at random,
the straight line joining the points will fall within each
circle; :just:`[III. 2] <III.2>`
but it fell within the circle :g:`$ABCD$ <0038.g3:( A B C D )>` and outside :g:`$ACK$ <0038.g3:( A C K )>`
:just:`[III. Def. 3] <III.def.3>`: which is absurd.

Therefore a circle does not touch a circle externally at
more points than one.

And it was proved that neither does it so touch it
internally.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **ABDC.** Euclid writes :g:`$ABCD$ <0038.g3:( A B C D )>` (here and in the next proposition), notwithstanding the order in which the points are placed in the figure.

.. [#f2] **does it so touch it.** It is necessary to supply these words which the Greek ($\text{ὅτι οὐδὲ ἐκτός}$ and $\text{ὅτι οὐδὲ ἐντός}$) leaves to be understood.

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
     "III.def.3" [label="III.def.3", fillcolor="#224422", tooltip="III.def.3: Circles are said to touch one another which, meeting one another, do not cut one another.", URL="../../definitions/index.html#iii-def-3", target="_top"];
     "III.1" [label="III.1", fillcolor="#222244", tooltip="III.1: To find the centre of a given circle.", URL="../01/index.html", target="_top"];
     "III.2" [label="III.2", fillcolor="#222244", tooltip="III.2: If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.", URL="../02/index.html", target="_top"];
     "III.11" [label="III.11", fillcolor="#222244", tooltip="III.11: If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the…", URL="../11/index.html", target="_top"];
     "III.13" [label="III.13", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.13: A circle does not touch a circle at more points than one, whether it touch it internally or externally.", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.1" -> "I.def.10";
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
     "III.2" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "III.1" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.16" -> "I.15";
     "I.18" -> "I.16";
     "III.2" -> "I.16";
     "I.19" -> "I.18";
     "III.2" -> "I.19";
     "III.13" -> "III.def.3";
     "III.2" -> "III.1";
     "III.13" -> "III.2";
     "III.13" -> "III.11";
   }

----

See :ref:`Commentary on Proposition III.13 <III.13.commentary>`.

.. toctree::
   :hidden:

   commentary
