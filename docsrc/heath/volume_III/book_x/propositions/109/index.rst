:canonical_id: X.109
:volume: III
:book: X
:proposition: 109
:type: proposition
:title: Proposition X.109
:folios: 0240, 0241, 0242
:pages: 236, 237, 238
:dependencies: X.def.iii.2, X.def.iii.5, X.13, X.73, X.92, X.95

.. _X.109:

.. folio:: 0240
   :page: 236

PROPOSITION 109.
================

.. enunciation::

   If from a medial area a rational area be subtracted, there arise two other irrational straight lines, either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole.

For from the medial area :g:`$BC$ <0241.g1:< B C >>` let the rational area :g:`$BD$ <0241.g1:< B D >>` be subtracted.

.. _folio-iii-0241:

.. folio:: 0241
   :page: 237

I say that the “side” of the remainder :g:`$EC$ <0241.g1:< E C >>` becomes one of two irrational straight lines, either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole.

.. picture:: 0241.g1.svg
   :alt: Propositions 108, 109

For let a rational straight line :g:`$FG$ <0241.g1:/ F G />` be set out, and let the areas be similarly applied.

.. subclause::

   It follows then that :g:`$FH$ <0241.g1:/ F H />` is rational and incommensurable in length with :g:`$FG$ <0241.g1:/ F G />`, while :g:`$KF$ <0241.g1:/ K F />` is rational and commensurable in length with :g:`$FG$ <0241.g1:/ F G />`;

.. assertion::

   therefore :g:`$FH$ <0241.g1:/ F H />`, :g:`$FK$ <0241.g1:/ F K />` are rational straight lines commensurable in square only; :just:`[x. 13]` therefore :g:`$KH$ <0241.g1:/ K H />` is an apotome, and :g:`$FK$ <0241.g1:/ F K />` the annex to it. :just:`[x. 73]`

Now the square on :g:`$HF$ <0241.g1:/ H F />` is greater than the square on :g:`$FK$ <0241.g1:/ F K />` either by the square on a straight line commensurable with :g:`$HF$ <0241.g1:/ H F />` or by the square on a straight line incommensurable with it.

.. subclause::

   If then the square on :g:`$HF$ <0241.g1:/ H F />` is greater than the square on :g:`$FK$ <0241.g1:/ F K />` by the square on a straight line commensurable with :g:`$HF$ <0241.g1:/ H F />`, while the annex :g:`$FK$ <0241.g1:/ F K />` is commensurable in length with the rational straight line :g:`$FG$ <0241.g1:/ F G />` set out,

.. assertion:: [x. Deff. III. 2]

   :g:`$KH$ <0241.g1:/ K H />` is a second apotome.

.. subclause::

   But :g:`$FG$ <0241.g1:/ F G />` is rational;

.. assertion::

   so that the “side” of :g:`$LH$ <0241.g1:< L H >>`, that is, of :g:`$EC$ <0241.g1:< E C >>`, is a first apotome of a medial straight line. :just:`[x. 92]`

.. subclause::

   But, if the square on :g:`$HF$ <0241.g1:/ H F />` is greater than the square on :g:`$FK$ <0241.g1:/ F K />` by the square on a straight line incommensurable with :g:`$HF$ <0241.g1:/ H F />`, while the annex :g:`$FK$ <0241.g1:/ F K />` is commensurable in length with the rational straight line :g:`$FG$ <0241.g1:/ F G />` set out,

.. assertion::

   :g:`$KH$ <0241.g1:/ K H />` is a fifth apotome; :just:`[x. Deff. III. 5]` so that the “side” of :g:`$EC$ <0241.g1:< E C >>` is a straight line which produces with a rational area a medial whole. :just:`[x. 95]`

.. _folio-iii-0242:

.. folio:: 0242
   :page: 238

In this case we have to classify

$$\sqrt{\sqrt{k} \cdot \rho^2 - \lambda\rho^2}.$$

Suppose that

$$\sigma u = \sqrt{k} \cdot \rho^2,$$

$$\sigma v = \lambda\rho^2.$$

Thus, $\sigma u$ being medial and $\sigma v$ rational, $u$ is rational and $\smile \sigma$, while $v$ is rational and $\mathbin{\Cap} \sigma$.

Thus, as before, $u, v$ are rational and $\sim$, so that $(u - v)$ is an apotome.

Now either

(1) $\sqrt{u^2 - v^2} \mathbin{\Cap} u$, or (2) $\sqrt{u^2 - v^2} \smile u$, while in both cases $v$ is commensurable with $\sigma$.

Therefore $(u - v)$ is either (1) a second apotome, or (2) a fifth apotome, and hence in case (1) $\sqrt{\sigma (u - v)}$ is the :term:`*first apotome of a medial straight line* <first-apotome-of-a-medial-straight-line>`, :just:`[x. 92]` and in case (2) $\sqrt{\sigma (u - v)}$ is the "*side" of a medial, minus a rational, area*. :just:`[x. 95]`

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
     "I.28" [label="I.28", fillcolor="#222244", tooltip="I.28: If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal…", URL="../../../../volume_I/book_i/propositions/28/index.html", target="_top"];
     "I.29" [label="I.29", fillcolor="#222244", tooltip="I.29: A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior…", URL="../../../../volume_I/book_i/propositions/29/index.html", target="_top"];
     "I.30" [label="I.30", fillcolor="#222244", tooltip="I.30: Straight lines parallel to the same straight line are also parallel to one another.", URL="../../../../volume_I/book_i/propositions/30/index.html", target="_top"];
     "I.31" [label="I.31", fillcolor="#222244", tooltip="I.31: Through a given point to draw a straight line parallel to a given straight line.", URL="../../../../volume_I/book_i/propositions/31/index.html", target="_top"];
     "I.32" [label="I.32", fillcolor="#222244", tooltip="I.32: In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to…", URL="../../../../volume_I/book_i/propositions/32/index.html", target="_top"];
     "I.33" [label="I.33", fillcolor="#222244", tooltip="I.33: The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.", URL="../../../../volume_I/book_i/propositions/33/index.html", target="_top"];
     "I.34" [label="I.34", fillcolor="#222244", tooltip="I.34: In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.", URL="../../../../volume_I/book_i/propositions/34/index.html", target="_top"];
     "I.35" [label="I.35", fillcolor="#222244", tooltip="I.35: Parallelograms which are on the same base and in the same parallels are equal to one another.", URL="../../../../volume_I/book_i/propositions/35/index.html", target="_top"];
     "I.36" [label="I.36", fillcolor="#222244", tooltip="I.36: Parallelograms which are on equal bases and in the same parallels are equal to one another.", URL="../../../../volume_I/book_i/propositions/36/index.html", target="_top"];
     "I.37" [label="I.37", fillcolor="#222244", tooltip="I.37: Triangles which are on the same base and in the same parallels are equal to one another.", URL="../../../../volume_I/book_i/propositions/37/index.html", target="_top"];
     "I.38" [label="I.38", fillcolor="#222244", tooltip="I.38: Triangles which are on equal bases and in the same parallels are equal to one another.", URL="../../../../volume_I/book_i/propositions/38/index.html", target="_top"];
     "I.39" [label="I.39", fillcolor="#222244", tooltip="I.39: Equal triangles which are on the same base and on the same side are also in the same parallels.", URL="../../../../volume_I/book_i/propositions/39/index.html", target="_top"];
     "I.41" [label="I.41", fillcolor="#222244", tooltip="I.41: If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.", URL="../../../../volume_I/book_i/propositions/41/index.html", target="_top"];
     "I.42" [label="I.42", fillcolor="#222244", tooltip="I.42: To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.", URL="../../../../volume_I/book_i/propositions/42/index.html", target="_top"];
     "I.43" [label="I.43", fillcolor="#222244", tooltip="I.43: In any parallelogram the complements of the parallelograms about the diameter are equal to one another.", URL="../../../../volume_I/book_i/propositions/43/index.html", target="_top"];
     "I.44" [label="I.44", fillcolor="#222244", tooltip="I.44: To a given straight line to apply, in a given rectilineal angle, a parallelogram equal to a given triangle.", URL="../../../../volume_I/book_i/propositions/44/index.html", target="_top"];
     "I.45" [label="I.45", fillcolor="#222244", tooltip="I.45: To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.", URL="../../../../volume_I/book_i/propositions/45/index.html", target="_top"];
     "I.46" [label="I.46", fillcolor="#222244", tooltip="I.46: On a given straight line to describe a square.", URL="../../../../volume_I/book_i/propositions/46/index.html", target="_top"];
     "I.47" [label="I.47", fillcolor="#222244", tooltip="I.47: In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.", URL="../../../../volume_I/book_i/propositions/47/index.html", target="_top"];
     "II.5" [label="II.5", fillcolor="#222244", tooltip="II.5: If a straight line be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the straight line between the…", URL="../../../../volume_I/book_ii/propositions/05/index.html", target="_top"];
     "II.7" [label="II.7", fillcolor="#222244", tooltip="II.7: If a straight line be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said…", URL="../../../../volume_I/book_ii/propositions/07/index.html", target="_top"];
     "III.20" [label="III.20", fillcolor="#222244", tooltip="III.20: In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", URL="../../../../volume_II/book_iii/propositions/20/index.html", target="_top"];
     "III.21" [label="III.21", fillcolor="#222244", tooltip="III.21: In a circle the angles in the same segment are equal to one another.", URL="../../../../volume_II/book_iii/propositions/21/index.html", target="_top"];
     "III.22" [label="III.22", fillcolor="#222244", tooltip="III.22: The opposite angles of quadrilaterals in circles are equal to two right angles.", URL="../../../../volume_II/book_iii/propositions/22/index.html", target="_top"];
     "III.31" [label="III.31", fillcolor="#222244", tooltip="III.31: In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle…", URL="../../../../volume_II/book_iii/propositions/31/index.html", target="_top"];
     "IV.1" [label="IV.1", fillcolor="#222244", tooltip="IV.1: Into a given circle to fit a straight line equal to a given straight line which is not greater than the diameter of the circle.", URL="../../../../volume_II/book_iv/propositions/01/index.html", target="_top"];
     "V.def.4" [label="V.def.4", fillcolor="#224422", tooltip="V.def.4: Magnitudes are said to have a ratio to one another which are capable, when multiplied, of exceeding one another.", URL="../../../../volume_II/book_v/definitions/index.html#v-def-4", target="_top"];
     "V.def.5" [label="V.def.5", fillcolor="#224422", tooltip="V.def.5: Magnitudes are said to be in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any…", URL="../../../../volume_II/book_v/definitions/index.html#v-def-5", target="_top"];
     "V.def.7" [label="V.def.7", fillcolor="#224422", tooltip="V.def.7: When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then…", URL="../../../../volume_II/book_v/definitions/index.html#v-def-7", target="_top"];
     "V.def.9" [label="V.def.9", fillcolor="#224422", tooltip="V.def.9: When three magnitudes are proportional, the first is said to have to the third the duplicate ratio of that which it has to the second.", URL="../../../../volume_II/book_v/definitions/index.html#v-def-9", target="_top"];
     "V.def.11" [label="V.def.11", fillcolor="#224422", tooltip="V.def.11: The term corresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", URL="../../../../volume_II/book_v/definitions/index.html#v-def-11", target="_top"];
     "V.1" [label="V.1", fillcolor="#222244", tooltip="V.1: If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one…", URL="../../../../volume_II/book_v/propositions/01/index.html", target="_top"];
     "V.2" [label="V.2", fillcolor="#222244", tooltip="V.2: If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of…", URL="../../../../volume_II/book_v/propositions/02/index.html", target="_top"];
     "V.3" [label="V.3", fillcolor="#222244", tooltip="V.3: If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken…", URL="../../../../volume_II/book_v/propositions/03/index.html", target="_top"];
     "V.4" [label="V.4", fillcolor="#222244", tooltip="V.4: If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples…", URL="../../../../volume_II/book_v/propositions/04/index.html", target="_top"];
     "V.7" [label="V.7", fillcolor="#222244", tooltip="V.7: Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", URL="../../../../volume_II/book_v/propositions/07/index.html", target="_top"];
     "V.8" [label="V.8", fillcolor="#222244", tooltip="V.8: Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", URL="../../../../volume_II/book_v/propositions/08/index.html", target="_top"];
     "V.9" [label="V.9", fillcolor="#222244", tooltip="V.9: Magnitudes which have the same ratio to the same are equal to one another ; and magnitudes to which the same has the same ratio are equal.", URL="../../../../volume_II/book_v/propositions/09/index.html", target="_top"];
     "V.10" [label="V.10", fillcolor="#222244", tooltip="V.10: Of magnitudes which have a ratio to the same, that which has a greater ratio is greater ; and that to which the same has a greater ratio is less.", URL="../../../../volume_II/book_v/propositions/10/index.html", target="_top"];
     "V.11" [label="V.11", fillcolor="#222244", tooltip="V.11: Ratios which are the same with the same ratio are also the same with one another.", URL="../../../../volume_II/book_v/propositions/11/index.html", target="_top"];
     "V.12" [label="V.12", fillcolor="#222244", tooltip="V.12: If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", URL="../../../../volume_II/book_v/propositions/12/index.html", target="_top"];
     "V.13" [label="V.13", fillcolor="#222244", tooltip="V.13: If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have…", URL="../../../../volume_II/book_v/propositions/13/index.html", target="_top"];
     "V.14" [label="V.14", fillcolor="#222244", tooltip="V.14: If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second will also be greater than the fourth ; if…", URL="../../../../volume_II/book_v/propositions/14/index.html", target="_top"];
     "V.15" [label="V.15", fillcolor="#222244", tooltip="V.15: Parts have the same ratio as the same multiples of them taken in corresponding order.", URL="../../../../volume_II/book_v/propositions/15/index.html", target="_top"];
     "V.16" [label="V.16", fillcolor="#222244", tooltip="V.16: If four magnitudes be proportional, they will also be proportional alternately.", URL="../../../../volume_II/book_v/propositions/16/index.html", target="_top"];
     "V.17" [label="V.17", fillcolor="#222244", tooltip="V.17: If magnitudes be proportional componendo, they will also be proportional separando.", URL="../../../../volume_II/book_v/propositions/17/index.html", target="_top"];
     "V.18" [label="V.18", fillcolor="#222244", tooltip="V.18: If magnitudes be proportional separando, they will also be proportional componendo.", URL="../../../../volume_II/book_v/propositions/18/index.html", target="_top"];
     "V.19" [label="V.19", fillcolor="#222244", tooltip="V.19: If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder will also be to the remainder as whole to whole.", URL="../../../../volume_II/book_v/propositions/19/index.html", target="_top"];
     "V.20" [label="V.20", fillcolor="#222244", tooltip="V.20: If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and if ex aequali the first be greater than the third, the…", URL="../../../../volume_II/book_v/propositions/20/index.html", target="_top"];
     "V.22" [label="V.22", fillcolor="#222244", tooltip="V.22: If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they will also be in the same ratio…", URL="../../../../volume_II/book_v/propositions/22/index.html", target="_top"];
     "VI.def.1" [label="VI.def.1", fillcolor="#224422", tooltip="VI.def.1: Similar rectilineal figures are such as have their angles severally equal and the sides about the equal angles proportional.", URL="../../../../volume_II/book_vi/definitions/index.html#vi-def-1", target="_top"];
     "VI.1" [label="VI.1", fillcolor="#222244", tooltip="VI.1: Triangles and parallelograms which are under the same height are to one another as their bases.", URL="../../../../volume_II/book_vi/propositions/01/index.html", target="_top"];
     "VI.2" [label="VI.2", fillcolor="#222244", tooltip="VI.2: If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut…", URL="../../../../volume_II/book_vi/propositions/02/index.html", target="_top"];
     "VI.4" [label="VI.4", fillcolor="#222244", tooltip="VI.4: In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", URL="../../../../volume_II/book_vi/propositions/04/index.html", target="_top"];
     "VI.6" [label="VI.6", fillcolor="#222244", tooltip="VI.6: If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular and will have those angles equal which the…", URL="../../../../volume_II/book_vi/propositions/06/index.html", target="_top"];
     "VI.8" [label="VI.8", fillcolor="#222244", tooltip="VI.8: If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.", URL="../../../../volume_II/book_vi/propositions/08/index.html", target="_top"];
     "VI.11" [label="VI.11", fillcolor="#222244", tooltip="VI.11: To two given straight lines to find a third proportional.", URL="../../../../volume_II/book_vi/propositions/11/index.html", target="_top"];
     "VI.12" [label="VI.12", fillcolor="#222244", tooltip="VI.12: To three given straight lines to find a fourth proportional.", URL="../../../../volume_II/book_vi/propositions/12/index.html", target="_top"];
     "VI.13" [label="VI.13", fillcolor="#222244", tooltip="VI.13: To two given straight lines to find a mean proportional.", URL="../../../../volume_II/book_vi/propositions/13/index.html", target="_top"];
     "VI.14" [label="VI.14", fillcolor="#222244", tooltip="VI.14: In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles…", URL="../../../../volume_II/book_vi/propositions/14/index.html", target="_top"];
     "VI.15" [label="VI.15", fillcolor="#222244", tooltip="VI.15: In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one…", URL="../../../../volume_II/book_vi/propositions/15/index.html", target="_top"];
     "VI.16" [label="VI.16", fillcolor="#222244", tooltip="VI.16: If four straight lines be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes…", URL="../../../../volume_II/book_vi/propositions/16/index.html", target="_top"];
     "VI.17" [label="VI.17", fillcolor="#222244", tooltip="VI.17: If three straight lines be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes be equal to…", URL="../../../../volume_II/book_vi/propositions/17/index.html", target="_top"];
     "VI.18" [label="VI.18", fillcolor="#222244", tooltip="VI.18: On a given straight line to describe a rectilinear figure similar and similarly situated to a given rectilinear figure.", URL="../../../../volume_II/book_vi/propositions/18/index.html", target="_top"];
     "VI.19" [label="VI.19", fillcolor="#222244", tooltip="VI.19: Similar triangles are to one another in the duplicate ratio of the corresponding sides.", URL="../../../../volume_II/book_vi/propositions/19/index.html", target="_top"];
     "VI.20" [label="VI.20", fillcolor="#222244", tooltip="VI.20: Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio…", URL="../../../../volume_II/book_vi/propositions/20/index.html", target="_top"];
     "VI.21" [label="VI.21", fillcolor="#222244", tooltip="VI.21: Figures which are similar to the same rectilineal figure are also similar to one another.", URL="../../../../volume_II/book_vi/propositions/21/index.html", target="_top"];
     "VI.22" [label="VI.22", fillcolor="#222244", tooltip="VI.22: If four straight lines be proportional, the rectilineal figures similar and similarly described upon them will also be proportional; and, if the rectilineal figures similar and…", URL="../../../../volume_II/book_vi/propositions/22/index.html", target="_top"];
     "VI.24" [label="VI.24", fillcolor="#222244", tooltip="VI.24: In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.", URL="../../../../volume_II/book_vi/propositions/24/index.html", target="_top"];
     "VI.25" [label="VI.25", fillcolor="#222244", tooltip="VI.25: To construct one and the same figure similar to a given rectilineal figure and equal to another given rectilineal figure.", URL="../../../../volume_II/book_vi/propositions/25/index.html", target="_top"];
     "VI.26" [label="VI.26", fillcolor="#222244", tooltip="VI.26: If from a parallelogram there be taken away a parallelogram similar and similarly situated to the whole and having a common angle with it, it is about the same diameter with the…", URL="../../../../volume_II/book_vi/propositions/26/index.html", target="_top"];
     "VI.28" [label="VI.28", fillcolor="#222244", tooltip="VI.28: To a given straight line to apply a parallelogram equal to a given rectilineal figure and deficient by a parallelogrammic figure similar to a given one : thus the given…", URL="../../../../volume_II/book_vi/propositions/28/index.html", target="_top"];
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-12", target="_top"];
     "VII.def.15" [label="VII.def.15", fillcolor="#224422", tooltip="VII.def.15: A number is said to multiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-15", target="_top"];
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-20", target="_top"];
     "VII.def.21" [label="VII.def.21", fillcolor="#224422", tooltip="VII.def.21: Similar plane and solid numbers are those which have their sides proportional.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-21", target="_top"];
     "VII.1" [label="VII.1", fillcolor="#222244", tooltip="VII.1: Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit…", URL="../../../../volume_II/book_vii/propositions/01/index.html", target="_top"];
     "VII.2" [label="VII.2", fillcolor="#222244", tooltip="VII.2: Given two numbers not prime to one another, to find their greatest common measure.", URL="../../../../volume_II/book_vii/propositions/02/index.html", target="_top"];
     "VII.3" [label="VII.3", fillcolor="#222244", tooltip="VII.3: Given three numbers not prime to one another, to find their greatest common measure.", URL="../../../../volume_II/book_vii/propositions/03/index.html", target="_top"];
     "VII.4" [label="VII.4", fillcolor="#222244", tooltip="VII.4: Any number is either a part or parts of any number, the less of the greater.", URL="../../../../volume_II/book_vii/propositions/04/index.html", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../../../../volume_II/book_vii/propositions/05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", tooltip="VII.6: If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", URL="../../../../volume_II/book_vii/propositions/06/index.html", target="_top"];
     "VII.9" [label="VII.9", fillcolor="#222244", tooltip="VII.9: If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts…", URL="../../../../volume_II/book_vii/propositions/09/index.html", target="_top"];
     "VII.10" [label="VII.10", fillcolor="#222244", tooltip="VII.10: If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part…", URL="../../../../volume_II/book_vii/propositions/10/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", tooltip="VII.12: If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", URL="../../../../volume_II/book_vii/propositions/12/index.html", target="_top"];
     "VII.13" [label="VII.13", fillcolor="#222244", tooltip="VII.13: If four numbers be proportional, they will also be proportional alternately.", URL="../../../../volume_II/book_vii/propositions/13/index.html", target="_top"];
     "VII.14" [label="VII.14", fillcolor="#222244", tooltip="VII.14: If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they will also be in the same ratio ex aequali.", URL="../../../../volume_II/book_vii/propositions/14/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", tooltip="VII.15: If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of…", URL="../../../../volume_II/book_vii/propositions/15/index.html", target="_top"];
     "VII.16" [label="VII.16", fillcolor="#222244", tooltip="VII.16: If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.", URL="../../../../volume_II/book_vii/propositions/16/index.html", target="_top"];
     "VII.17" [label="VII.17", fillcolor="#222244", tooltip="VII.17: If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", URL="../../../../volume_II/book_vii/propositions/17/index.html", target="_top"];
     "VII.18" [label="VII.18", fillcolor="#222244", tooltip="VII.18: If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", URL="../../../../volume_II/book_vii/propositions/18/index.html", target="_top"];
     "VII.19" [label="VII.19", fillcolor="#222244", tooltip="VII.19: If four numbers be proportional, the number produced from the first and fourth will be equal to the number produced from the second and third; and, if the number produced from the…", URL="../../../../volume_II/book_vii/propositions/19/index.html", target="_top"];
     "VII.20" [label="VII.20", fillcolor="#222244", tooltip="VII.20: The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", URL="../../../../volume_II/book_vii/propositions/20/index.html", target="_top"];
     "VII.21" [label="VII.21", fillcolor="#222244", tooltip="VII.21: Numbers prime to one another are the least of those which have the same ratio with them.", URL="../../../../volume_II/book_vii/propositions/21/index.html", target="_top"];
     "VII.22" [label="VII.22", fillcolor="#222244", tooltip="VII.22: The least numbers of those which have the same ratio with them are prime to one another.", URL="../../../../volume_II/book_vii/propositions/22/index.html", target="_top"];
     "VII.23" [label="VII.23", fillcolor="#222244", tooltip="VII.23: If two numbers be prime to one another, the number which measures the one of them will be prime to the remaining number.", URL="../../../../volume_II/book_vii/propositions/23/index.html", target="_top"];
     "VII.24" [label="VII.24", fillcolor="#222244", tooltip="VII.24: If two numbers be prime to any number, their product also will be prime to the same.", URL="../../../../volume_II/book_vii/propositions/24/index.html", target="_top"];
     "VII.25" [label="VII.25", fillcolor="#222244", tooltip="VII.25: If two numbers be prime to one another, the product of one of them into itself will be prime to the remaining one.", URL="../../../../volume_II/book_vii/propositions/25/index.html", target="_top"];
     "VII.26" [label="VII.26", fillcolor="#222244", tooltip="VII.26: If two numbers be prime to two numbers, both to each, their products also will be prime to one another.", URL="../../../../volume_II/book_vii/propositions/26/index.html", target="_top"];
     "VII.27" [label="VII.27", fillcolor="#222244", tooltip="VII.27: If two numbers be prime to one another, and each by multiplying itself make a certain number, the products will be prime to one another ; and, if the original numbers by…", URL="../../../../volume_II/book_vii/propositions/27/index.html", target="_top"];
     "VII.33" [label="VII.33", fillcolor="#222244", tooltip="VII.33: Given as many numbers as we please, to find the least of those which have the same ratio with them.", URL="../../../../volume_II/book_vii/propositions/33/index.html", target="_top"];
     "VII.34" [label="VII.34", fillcolor="#222244", tooltip="VII.34: Given two numbers, to find the least number which they measure.", URL="../../../../volume_II/book_vii/propositions/34/index.html", target="_top"];
     "VII.35" [label="VII.35", fillcolor="#222244", tooltip="VII.35: If two numbers measure any number, the least number measured by them will also measure the same.", URL="../../../../volume_II/book_vii/propositions/35/index.html", target="_top"];
     "VIII.def.20" [label="VIII.def.20", fillcolor="#224422", tooltip="VIII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../../../volume_II/book_vii/definitions/index.html#vii-def-20", target="_top"];
     "VIII.1" [label="VIII.1", fillcolor="#222244", tooltip="VIII.1: If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio…", URL="../../../../volume_II/book_viii/propositions/01/index.html", target="_top"];
     "VIII.2" [label="VIII.2", fillcolor="#222244", tooltip="VIII.2: To find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.", URL="../../../../volume_II/book_viii/propositions/02/index.html", target="_top"];
     "VIII.4" [label="VIII.4", fillcolor="#222244", tooltip="VIII.4: Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.", URL="../../../../volume_II/book_viii/propositions/04/index.html", target="_top"];
     "VIII.11" [label="VIII.11", fillcolor="#222244", tooltip="VIII.11: Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.", URL="../../../../volume_II/book_viii/propositions/11/index.html", target="_top"];
     "VIII.18" [label="VIII.18", fillcolor="#222244", tooltip="VIII.18: Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has…", URL="../../../../volume_II/book_viii/propositions/18/index.html", target="_top"];
     "VIII.26" [label="VIII.26", fillcolor="#222244", tooltip="VIII.26: Similar plane numbers have to one another the ratio which a square number has to a square number.", URL="../../../../volume_II/book_viii/propositions/26/index.html", target="_top"];
     "X.def.1" [label="X.def.1", fillcolor="#224422", tooltip="X.def.1: Those magnitudes are said to be commensurable which are measured by the same measure, and those incommensurable which cannot have any common measure.", URL="../../definitions/index.html#x-def-1", target="_top"];
     "X.def.3" [label="X.def.3", fillcolor="#224422", tooltip="X.def.3: With these hypotheses, it is proved that there exist straight lines infinite in multitude which are commensurable and incommensurable respectively, some in length only, and others…", URL="../../definitions/index.html#x-def-3", target="_top"];
     "X.def.4" [label="X.def.4", fillcolor="#224422", tooltip="X.def.4: And let the square on the assigned straight line be called rational and those areas which are commensurable with it rational, but those which are incommensurable with it…", URL="../../definitions/index.html#x-def-4", target="_top"];
     "X.def.iii.2" [label="X.def.iii.2", fillcolor="#224422", tooltip="X.def.iii.2: But if the annex be commensurable in length with the rational straight line set out, and the square on the whole be greater than that on the annex by the square on a straight line…", URL="../../definitions_iii/index.html#x-def-iii-2", target="_top"];
     "X.def.iii.5" [label="X.def.iii.5", fillcolor="#224422", tooltip="X.def.iii.5: if the annex be so commensurable, a fifth.", URL="../../definitions_iii/index.html#x-def-iii-5", target="_top"];
     "X.5" [label="X.5", fillcolor="#222244", tooltip="X.5: Commensurable magnitudes have to one another the ratio which a number has to a number.", URL="../005/index.html", target="_top"];
     "X.6" [label="X.6", fillcolor="#222244", tooltip="X.6: If two magnitudes have to one another the ratio which a number has to a number, the magnitudes will be commensurable.", URL="../006/index.html", target="_top"];
     "X.7" [label="X.7", fillcolor="#222244", tooltip="X.7: Incommensurable magnitudes have not to one another the ratio which a number has to a number.", URL="../007/index.html", target="_top"];
     "X.8" [label="X.8", fillcolor="#222244", tooltip="X.8: If two magnitudes have not to one another the ratio which a number has to a number, the magnitudes will be incommensurable.", URL="../008/index.html", target="_top"];
     "X.9" [label="X.9", fillcolor="#222244", tooltip="X.9: The squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which have to one another the ratio…", URL="../009/index.html", target="_top"];
     "X.11" [label="X.11", fillcolor="#222244", tooltip="X.11: If four magnitudes be proportional, and the first be commensurable with the second, the third will also be commensurable with the fourth ; and, if the first be incommensurable…", URL="../011/index.html", target="_top"];
     "X.12" [label="X.12", fillcolor="#222244", tooltip="X.12: Magnitudes commensurable with the same magnitude are commensurable with one another also.", URL="../012/index.html", target="_top"];
     "X.13" [label="X.13", fillcolor="#222244", tooltip="X.13: If two magnitudes be commensurable, and the one of them be incommensurable with any magnitude, the remaining one will also be incommensurable with the same.", URL="../013/index.html", target="_top"];
     "X.14" [label="X.14", fillcolor="#222244", tooltip="X.14: If four straight lines be proportional, and the square on the first be greater than the square on the second by the square on a straight line commensurable with the first, the…", URL="../014/index.html", target="_top"];
     "X.15" [label="X.15", fillcolor="#222244", tooltip="X.15: If two commensurable magnitudes be added together, the whole will also be commensurable with each of them; and, if the whole be commensurable with one of them, the original…", URL="../015/index.html", target="_top"];
     "X.16" [label="X.16", fillcolor="#222244", tooltip="X.16: If two incommensurable magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original…", URL="../016/index.html", target="_top"];
     "X.17" [label="X.17", fillcolor="#222244", tooltip="X.17: If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure…", URL="../017/index.html", target="_top"];
     "X.18" [label="X.18", fillcolor="#222244", tooltip="X.18: If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure…", URL="../018/index.html", target="_top"];
     "X.19" [label="X.19", fillcolor="#222244", tooltip="X.19: The rectangle contained by rational straight lines commensurable in length is rational.", URL="../019/index.html", target="_top"];
     "X.21" [label="X.21", fillcolor="#222244", tooltip="X.21: The rectangle contained by rational straight lines commensurable in square only is irrational, and the side of the square equal to it is irrational. Let the latter be called…", URL="../021/index.html", target="_top"];
     "X.22" [label="X.22", fillcolor="#222244", tooltip="X.22: The square on a medial straight line, if applied to a rational straight line, produces as breadth a straight line rational and incommensurable in length with that to which it is…", URL="../022/index.html", target="_top"];
     "X.23" [label="X.23", fillcolor="#222244", tooltip="X.23: A straight line commensurable with a medial straight line is medial.", URL="../023/index.html", target="_top"];
     "X.29" [label="X.29", fillcolor="#222244", tooltip="X.29: To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line…", URL="../029/index.html", target="_top"];
     "X.30" [label="X.30", fillcolor="#222244", tooltip="X.30: To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line…", URL="../030/index.html", target="_top"];
     "X.31" [label="X.31", fillcolor="#222244", tooltip="X.31: To find two medial straight lines commensurable in square only, containing a rational rectangle, and such that the square on the greater is greater than the square on the less by…", URL="../031/index.html", target="_top"];
     "X.34" [label="X.34", fillcolor="#222244", tooltip="X.34: To find two straight lines incommensurable in square which make the sum of the squares on them medial but the rectangle contained by them rational.", URL="../034/index.html", target="_top"];
     "X.73" [label="X.73", fillcolor="#222244", tooltip="X.73: If from a rational straight line there be subtracted a rational straight line commensurable with the whole in square only, the remainder is irrational ; and let it be called an…", URL="../073/index.html", target="_top"];
     "X.74" [label="X.74", fillcolor="#222244", tooltip="X.74: If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a rational…", URL="../074/index.html", target="_top"];
     "X.77" [label="X.77", fillcolor="#222244", tooltip="X.77: If from a straight line there be subtracted a straight line which is incommensurable in square with the whole, and which with the whole makes the sum of the squares on them…", URL="../077/index.html", target="_top"];
     "X.92" [label="X.92", fillcolor="#222244", tooltip="X.92: If an area be contained by a rational straight line and a second apotome, the \"side\" of the area is a first apotome of a medial straight line.", URL="../092/index.html", target="_top"];
     "X.95" [label="X.95", fillcolor="#222244", tooltip="X.95: If an area be contained by a rational straight line and a fifth apotome, the “side” of the area is a straight line which produces with a rational area a medial whole.", URL="../095/index.html", target="_top"];
     "X.109" [label="X.109", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="X.109: If from a medial area a rational area be subtracted, there arise two other irrational straight lines, either a first apotome of a medial straight line or a straight line which…", URL="index.html", target="_top"];
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
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.29" -> "I.post.5";
     "I.44" -> "I.post.5";
     "VI.4" -> "I.post.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.30" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.39" -> "I.cn.1";
     "I.44" -> "I.cn.1";
     "I.45" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.45" -> "I.cn.2";
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
     "VI.11" -> "I.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "VI.6" -> "I.4";
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
     "I.46" -> "I.11";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.45" -> "I.14";
     "I.47" -> "I.14";
     "VI.14" -> "I.14";
     "VI.15" -> "I.14";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "I.44" -> "I.15";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "III.31" -> "I.17";
     "VI.4" -> "I.17";
     "I.19" -> "I.18";
     "I.20" -> "I.19";
     "I.22" -> "I.20";
     "I.23" -> "I.22";
     "I.31" -> "I.23";
     "I.42" -> "I.23";
     "VI.6" -> "I.23";
     "VI.18" -> "I.23";
     "I.34" -> "I.26";
     "I.28" -> "I.27";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "VI.4" -> "I.28";
     "I.30" -> "I.29";
     "I.32" -> "I.29";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.44" -> "I.29";
     "I.45" -> "I.29";
     "I.46" -> "I.29";
     "I.45" -> "I.30";
     "I.32" -> "I.31";
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.39" -> "I.31";
     "I.42" -> "I.31";
     "I.44" -> "I.31";
     "I.46" -> "I.31";
     "II.5" -> "I.31";
     "VI.11" -> "I.31";
     "VI.12" -> "I.31";
     "VI.26" -> "I.31";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "VI.6" -> "I.32";
     "VI.8" -> "I.32";
     "VI.18" -> "I.32";
     "VI.20" -> "I.32";
     "I.36" -> "I.33";
     "I.45" -> "I.33";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "I.43" -> "I.34";
     "I.45" -> "I.34";
     "I.46" -> "I.34";
     "VI.4" -> "I.34";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.38" -> "I.36";
     "II.5" -> "I.36";
     "VI.28" -> "I.36";
     "I.39" -> "I.37";
     "I.41" -> "I.37";
     "I.42" -> "I.38";
     "VI.1" -> "I.38";
     "VI.2" -> "I.38";
     "VI.2" -> "I.39";
     "I.42" -> "I.41";
     "I.47" -> "I.41";
     "VI.1" -> "I.41";
     "I.44" -> "I.42";
     "I.45" -> "I.42";
     "I.44" -> "I.43";
     "II.5" -> "I.43";
     "II.7" -> "I.43";
     "I.45" -> "I.44";
     "VI.25" -> "I.44";
     "VI.25" -> "I.45";
     "I.47" -> "I.46";
     "II.5" -> "I.46";
     "II.7" -> "I.46";
     "X.13" -> "I.47";
     "X.29" -> "I.47";
     "X.30" -> "I.47";
     "X.34" -> "I.47";
     "X.17" -> "II.5";
     "X.73" -> "II.7";
     "X.74" -> "II.7";
     "X.77" -> "II.7";
     "III.21" -> "III.20";
     "III.22" -> "III.21";
     "III.31" -> "III.22";
     "VI.13" -> "III.31";
     "X.13" -> "III.31";
     "X.29" -> "III.31";
     "X.30" -> "III.31";
     "X.34" -> "III.31";
     "X.13" -> "IV.1";
     "V.8" -> "V.def.4";
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.22" -> "V.def.5";
     "VI.1" -> "V.def.5";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "VI.19" -> "V.def.9";
     "VIII.11" -> "V.def.9";
     "VIII.18" -> "V.def.9";
     "VI.19" -> "V.def.11";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.17" -> "V.1";
     "V.3" -> "V.2";
     "V.17" -> "V.2";
     "V.4" -> "V.3";
     "V.22" -> "V.4";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "VI.2" -> "V.7";
     "VI.14" -> "V.7";
     "VI.15" -> "V.7";
     "VII.19" -> "V.7";
     "X.5" -> "V.7";
     "X.6" -> "V.7";
     "V.9" -> "V.8";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "VI.2" -> "V.9";
     "VI.6" -> "V.9";
     "VI.14" -> "V.9";
     "VI.15" -> "V.9";
     "VI.22" -> "V.9";
     "VI.26" -> "V.9";
     "VII.19" -> "V.9";
     "X.6" -> "V.9";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.16" -> "V.11";
     "V.18" -> "V.11";
     "V.19" -> "V.11";
     "VI.1" -> "V.11";
     "VI.2" -> "V.11";
     "VI.6" -> "V.11";
     "VI.14" -> "V.11";
     "VI.15" -> "V.11";
     "VI.19" -> "V.11";
     "VI.22" -> "V.11";
     "VI.26" -> "V.11";
     "X.6" -> "V.11";
     "X.12" -> "V.11";
     "X.92" -> "V.11";
     "V.15" -> "V.12";
     "VI.20" -> "V.12";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.16" -> "V.14";
     "V.18" -> "V.14";
     "V.16" -> "V.15";
     "VI.1" -> "V.15";
     "V.19" -> "V.16";
     "VI.4" -> "V.16";
     "VI.19" -> "V.16";
     "VI.24" -> "V.16";
     "VI.25" -> "V.16";
     "V.18" -> "V.17";
     "V.19" -> "V.17";
     "X.14" -> "V.17";
     "VI.24" -> "V.18";
     "X.29" -> "V.19";
     "X.30" -> "V.19";
     "V.22" -> "V.20";
     "VI.4" -> "V.22";
     "VI.20" -> "V.22";
     "VI.22" -> "V.22";
     "VI.24" -> "V.22";
     "X.5" -> "V.22";
     "X.6" -> "V.22";
     "X.12" -> "V.22";
     "X.14" -> "V.22";
     "VI.8" -> "VI.def.1";
     "VI.18" -> "VI.def.1";
     "VI.20" -> "VI.def.1";
     "VI.21" -> "VI.def.1";
     "VI.24" -> "VI.def.1";
     "VI.2" -> "VI.1";
     "VI.14" -> "VI.1";
     "VI.15" -> "VI.1";
     "VI.19" -> "VI.1";
     "VI.20" -> "VI.1";
     "VI.25" -> "VI.1";
     "X.19" -> "VI.1";
     "X.21" -> "VI.1";
     "X.23" -> "VI.1";
     "X.92" -> "VI.1";
     "VI.4" -> "VI.2";
     "VI.11" -> "VI.2";
     "VI.12" -> "VI.2";
     "VI.24" -> "VI.2";
     "VI.6" -> "VI.4";
     "VI.8" -> "VI.4";
     "VI.18" -> "VI.4";
     "VI.20" -> "VI.4";
     "VI.20" -> "VI.6";
     "VI.13" -> "VI.8";
     "VI.19" -> "VI.11";
     "VI.22" -> "VI.11";
     "VI.22" -> "VI.12";
     "VI.25" -> "VI.13";
     "VI.16" -> "VI.14";
     "X.22" -> "VI.14";
     "VI.19" -> "VI.15";
     "VI.17" -> "VI.16";
     "X.92" -> "VI.17";
     "VI.22" -> "VI.18";
     "VI.25" -> "VI.18";
     "VI.28" -> "VI.18";
     "VI.20" -> "VI.19";
     "VI.22" -> "VI.19";
     "VI.25" -> "VI.19";
     "X.6" -> "VI.19";
     "X.9" -> "VI.20";
     "VI.24" -> "VI.21";
     "VI.28" -> "VI.21";
     "X.14" -> "VI.22";
     "X.22" -> "VI.22";
     "VI.26" -> "VI.24";
     "VI.28" -> "VI.25";
     "VI.28" -> "VI.26";
     "X.92" -> "VI.26";
     "X.95" -> "VI.26";
     "X.34" -> "VI.28";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.33" -> "VII.def.15";
     "VII.34" -> "VII.def.15";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VIII.4" -> "VII.def.20";
     "X.5" -> "VII.def.20";
     "X.6" -> "VII.def.20";
     "VIII.18" -> "VII.def.21";
     "VII.2" -> "VII.1";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VII.33" -> "VII.3";
     "VII.20" -> "VII.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.10" -> "VII.9";
     "VII.13" -> "VII.10";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VIII.4" -> "VII.13";
     "VIII.18" -> "VII.13";
     "VIII.1" -> "VII.14";
     "VII.16" -> "VII.15";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.34" -> "VII.16";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VII.34" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VIII.11" -> "VII.17";
     "VIII.18" -> "VII.17";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "VIII.11" -> "VII.18";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
     "VII.34" -> "VII.19";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VII.34" -> "VII.20";
     "VIII.1" -> "VII.20";
     "VIII.4" -> "VII.20";
     "VII.24" -> "VII.21";
     "VII.33" -> "VII.21";
     "VII.34" -> "VII.21";
     "VIII.1" -> "VII.21";
     "VIII.2" -> "VII.22";
     "VII.24" -> "VII.23";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VII.27" -> "VII.25";
     "VII.27" -> "VII.26";
     "VIII.2" -> "VII.27";
     "VII.34" -> "VII.33";
     "VIII.26" -> "VII.33";
     "VIII.4" -> "VII.34";
     "VIII.4" -> "VII.35";
     "VIII.4" -> "VIII.def.20";
     "VIII.2" -> "VIII.1";
     "VIII.26" -> "VIII.2";
     "X.12" -> "VIII.4";
     "X.9" -> "VIII.11";
     "VIII.26" -> "VIII.18";
     "X.9" -> "VIII.26";
     "X.15" -> "X.def.1";
     "X.16" -> "X.def.1";
     "X.23" -> "X.def.3";
     "X.19" -> "X.def.4";
     "X.21" -> "X.def.4";
     "X.22" -> "X.def.4";
     "X.29" -> "X.def.4";
     "X.73" -> "X.def.4";
     "X.74" -> "X.def.4";
     "X.92" -> "X.def.iii.2";
     "X.109" -> "X.def.iii.2";
     "X.95" -> "X.def.iii.5";
     "X.109" -> "X.def.iii.5";
     "X.8" -> "X.5";
     "X.9" -> "X.5";
     "X.11" -> "X.5";
     "X.12" -> "X.5";
     "X.7" -> "X.6";
     "X.9" -> "X.6";
     "X.11" -> "X.6";
     "X.12" -> "X.6";
     "X.17" -> "X.6";
     "X.18" -> "X.6";
     "X.29" -> "X.6";
     "X.30" -> "X.6";
     "X.34" -> "X.6";
     "X.73" -> "X.6";
     "X.11" -> "X.7";
     "X.11" -> "X.8";
     "X.29" -> "X.9";
     "X.30" -> "X.9";
     "X.14" -> "X.11";
     "X.19" -> "X.11";
     "X.21" -> "X.11";
     "X.22" -> "X.11";
     "X.23" -> "X.11";
     "X.31" -> "X.11";
     "X.34" -> "X.11";
     "X.73" -> "X.11";
     "X.92" -> "X.11";
     "X.13" -> "X.12";
     "X.17" -> "X.12";
     "X.18" -> "X.13";
     "X.22" -> "X.13";
     "X.23" -> "X.13";
     "X.73" -> "X.13";
     "X.92" -> "X.13";
     "X.109" -> "X.13";
     "X.31" -> "X.14";
     "X.17" -> "X.15";
     "X.73" -> "X.15";
     "X.92" -> "X.15";
     "X.18" -> "X.16";
     "X.73" -> "X.16";
     "X.74" -> "X.16";
     "X.77" -> "X.16";
     "X.18" -> "X.17";
     "X.92" -> "X.17";
     "X.34" -> "X.18";
     "X.95" -> "X.18";
     "X.92" -> "X.19";
     "X.95" -> "X.19";
     "X.22" -> "X.21";
     "X.23" -> "X.21";
     "X.31" -> "X.21";
     "X.92" -> "X.21";
     "X.95" -> "X.21";
     "X.23" -> "X.22";
     "X.31" -> "X.23";
     "X.31" -> "X.29";
     "X.31" -> "X.30";
     "X.34" -> "X.31";
     "X.77" -> "X.34";
     "X.92" -> "X.73";
     "X.109" -> "X.73";
     "X.92" -> "X.74";
     "X.95" -> "X.77";
     "X.109" -> "X.92";
     "X.109" -> "X.95";
   }
