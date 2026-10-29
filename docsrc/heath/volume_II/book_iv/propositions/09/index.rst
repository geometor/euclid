:canonical_id: IV.9
:volume: II
:book: IV
:proposition: 9
:type: proposition
:title: Proposition IV.9
:folios: 0101
:pages: 95
:dependencies: I.6, I.8

.. _IV.9:

.. folio:: 0101
   :page: 95

PROPOSITION 9.
==============

.. enunciation::

   About a given square to circumscribe a circle.

Let :g:`ABCD <0101.g1:< A B C D >>` be the given square;
thus it is required to circumscribe a circle about the square
:g:`ABCD <0101.g1:< A B C D >>`.

For let :g:`AC <0101.g1:/ A C />`, :g:`BD <0101.g1:/ B D />` be joined, and let them
cut one another at :g:`E <0101.g1:E>`.

.. picture:: 0101.g1.svg
   :alt: Proposition IV. 9 Diagram

Then, since :g:`DA <0101.g1:/ D A />` is :eq:`equal <0101.g1:/ D A / = 0101.g1:/ A B />` to :g:`AB <0101.g1:/ A B />`,
and :g:`AC <0101.g1:/ A C />` is common,
therefore the two sides :g:`DA <0101.g1:/ D A />`, :g:`AC <0101.g1:/ A C />` are :eq:`equal <0101.g1:/ D A / = 0101.g1:/ B A /; 0101.g1:/ A C / = 0101.g1:/ A C />`
to the two sides :g:`BA <0101.g1:/ B A />`, :g:`AC <0101.g1:/ A C />`;
and the base :g:`DC <0101.g1:/ D C />` is :eq:`equal <0101.g1:/ D C / = 0101.g1:/ B C />` to the base :g:`BC <0101.g1:/ B C />`;

.. assertion::

   therefore the angle :g:`DAC <0101.g1:< D A C )>` is :eq:`equal <0101.g1:< D A C ) = 0101.g1:< B A C )>` to the angle :g:`BAC <0101.g1:< B A C )>`. :just:`[I. 8] <I.8>`

Therefore the angle :g:`DAB <0101.g1:< D A B )>` is :eq:`bisected <0101.g1:< D A C ) = 0101.g1:< B A C )>` by :g:`AC <0101.g1:/ A C />`.

Similarly we can prove that each of the angles :g:`ABC <0101.g1:< A B C )>`,
:g:`BCD <0101.g1:< B C D )>`, :g:`CDA <0101.g1:< C D A )>` is bisected by the straight lines :g:`AC <0101.g1:/ A C />`, :g:`DB <0101.g1:/ D B />`.

Now, since the angle :g:`DAB <0101.g1:< D A B )>` is :eq:`equal <0101.g1:< D A B ) = 0101.g1:< A B C )>` to the angle :g:`ABC <0101.g1:< A B C )>`,
and the angle :g:`EAB <0101.g1:< E A B )>` is half the angle :g:`DAB <0101.g1:< D A B )>`,
and the angle :g:`EBA <0101.g1:< E B A )>` half the angle :g:`ABC <0101.g1:< A B C )>`,
therefore the angle :g:`EAB <0101.g1:< E A B )>` is also :eq:`equal <0101.g1:< E A B ) = 0101.g1:< E B A )>` to the angle :g:`EBA <0101.g1:< E B A )>`;
so that the side :g:`EA <0101.g1:/ E A />` is also :eq:`equal <0101.g1:/ E A / = 0101.g1:/ E B />` to :g:`EB <0101.g1:/ E B />`. :just:`[I. 6] <I.6>`

Similarly we can prove that each of the straight lines
:g:`EA <0101.g1:/ E A />`, :g:`EB <0101.g1:/ E B />` is :eq:`equal <0101.g1:/ E A / = 0101.g1:/ E B / = 0101.g1:/ E C / = 0101.g1:/ E D />` to each of the straight lines :g:`EC <0101.g1:/ E C />`, :g:`ED <0101.g1:/ E D />`.

Therefore the four straight lines :g:`EA <0101.g1:/ E A />`, :g:`EB <0101.g1:/ E B />`, :g:`EC <0101.g1:/ E C />`, :g:`ED <0101.g1:/ E D />` are
:eq:`equal <0101.g1:/ E A / = 0101.g1:/ E B / = 0101.g1:/ E C / = 0101.g1:/ E D />` to one another.

Therefore the circle described with centre :g:`E <0101.g1:E>` and distance
one of the straight lines :g:`EA <0101.g1:/ E A />`, :g:`EB <0101.g1:/ E B />`, :g:`EC <0101.g1:/ E C />`, :g:`ED <0101.g1:/ E D />` will pass also
through the remaining points;
and it will have been circumscribed about the square :g:`ABCD <0101.g1:< A B C D >>`.

Let it be circumscribed, as :g:`ABCD <0101.g1:( A B C D )>`.

Therefore about the given square a circle has been
circumscribed.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
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
     "I.6" [label="I.6", fillcolor="#222244", tooltip="I.6: If in a triangle two angles be equal to one another, the sides which subtend the equal angles will also be equal to one another.", URL="../../../../volume_I/book_i/propositions/06/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", tooltip="I.7: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its…", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", tooltip="I.8: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the…", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "IV.9" [label="IV.9", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IV.9: About a given square to circumscribe a circle.", URL="index.html", target="_top"];
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
     "IV.9" -> "I.6";
     "I.8" -> "I.7";
     "IV.9" -> "I.8";
   }
