:order: 20
:type: chapter
:canonical_id: D.unit.2
:folio: Menge pp. 42–66
:book: Propositions 25–38: Position & Parallels
:description: Transition from abstract magnitudes to planar geometry: uniqueness of line-line intersections (D.25), endpoints and directions of segments (D.26–D.30), neusis/circle distance meets (D.31), inclined transversals across parallels (D.32–D.33), and parallel ratio-division loci through a fixed pole (D.34–D.38).

.. _data-unit-2-en:

=============================================================
Unit 2: Position, Angles & Parallel Loci (Propositions 25–38)
=============================================================

*Straight Lines Given in Position, Angular Rays, and Parallel Locus Determination* — **D.25–D.38 (Simson XXVIII–XL) · Menge (1896) pp. 42–66**

.. note::

   **Edition Track (English)**: Transition from abstract magnitudes to planar geometry: uniqueness of line-line intersections (D.25), endpoints and directions of segments (D.26–D.30), neusis/circle distance meets (D.31), inclined transversals across parallels (D.32–D.33), and parallel ratio-division loci through a fixed pole (D.34–D.38). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. picture:: /_static/figures/data_02_position_loci.svg
   :alt: Position, Intersections, and Parallel Ratio Loci (Data Props. 25, 28–30, 34–38)

Interactive locus diagram (:cite:`Menge pp. 46–66 <menge:1896>`): From given external pole :g:`P <data_02_position_loci:P>`, secants :g:`PF <data_02_position_loci:/ P F />` (cutting :g:`AB <data_02_position_loci:/ A B />` at :g:`E <data_02_position_loci:E>` and :g:`CD <data_02_position_loci:/ C D />` at :g:`F <data_02_position_loci:F>`) and :g:`PH <data_02_position_loci:/ P H />` (cutting at :g:`G <data_02_position_loci:G>` and :g:`H <data_02_position_loci:H>`) are divided in a constant given ratio (:ref:`D.34 <D.34>`), while internal division points :g:`M <data_02_position_loci:M>`, :g:`N <data_02_position_loci:N>`, and :g:`S <data_02_position_loci:S>` trace the parallel locus :g:`MN <data_02_position_loci:/ M N />` (:ref:`D.35 <D.35>`–:ref:`D.38 <D.38>`). Ray :g:`KQ <data_02_position_loci:/ K Q />` from given point :g:`K <data_02_position_loci:K>` at given angle :g:`∠BKQ <data_02_position_loci:< B K Q )>` (:ref:`D.29 <D.29>`) meets :g:`CD <data_02_position_loci:/ C D />` at unique point :g:`Q <data_02_position_loci:Q>` (:ref:`D.25 <D.25>`).

.. _D.25:

Proposition 25 [κε΄ · Prop. XXVIII]
-----------------------------------

.. folio:: Menge 46
   :page: 46

.. enunciation::

   If two lines given in position cut one another, the point at which they cut one another is given in position.

*Functional Signature*: ``Given(Pos(L1), Pos(L2), Meet(L1, L2) = E) -> Determined(Pos(E))`` · *Dependencies*: :just:`[Data Def. 4] <D.def.4>`, :just:`[Post. 1] <I.post.1>`, :just:`[I Def. 4] <I.def.4>`

Let two lines $AB$ and $CD$, :term:`given in position <thesei>`, intersect one another at the point $E$. I say that the point $E$ is given in position.

For if $E$ is not given in position, it will shift its place (*μεταπεσεῖται*, :just:`[Data Def. 4] <D.def.4>`), while $AB$ and $CD$ remain fixed in position. Consequently at least one of the lines $AB$ or $CD$ passing through $E$ would also shift its position; yet both were assumed given in position—which is absurd. Therefore the intersection point $E$ does not shift, and so is given in position (:just:`[Data Def. 4] <D.def.4>`).

.. _D.26:

Proposition 26 [κϛ΄ · Prop. XXIX]
---------------------------------

.. enunciation::

   If the extremities of a straight line be given in position, the straight line is given in position and in magnitude.

*Functional Signature*: ``Given(Pos(A), Pos(B)) -> Determined(Pos(AB), Mag(AB))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Post. 1] <I.post.1>`, :just:`[Post. 3] <I.post.3>`

Let the extremities $A$ and $B$ of a straight line $AB$ be given in position. I say that the straight line $AB$ is given in position and in magnitude.

For if the straight line $AB$ did not retain the same place while $A$ and $B$ remain fixed, or if its length varied, two distinct straight lines could be drawn between the same two fixed points $A$ and $B$, enclosing a space—contrary to :just:`[Post. 1] <I.post.1>`. Therefore $AB$ always occupies the same place and has an invariant equal constructible on it (:just:`[I.2] <I.2>`), so $AB$ is given both in position (:just:`[Data Def. 4] <D.def.4>`) and in magnitude (:just:`[Data Def. 1] <D.def.1>`).

.. _D.27:

Proposition 27 [κζ΄ · Prop. XXX]
--------------------------------

.. folio:: Menge 48
   :page: 48

.. enunciation::

   If one extremity of a straight line given in position and in magnitude be given, the other extremity will also be given.

*Functional Signature*: ``Given(Pos(Ray A->), Mag(AB), Pos(A)) -> Determined(Pos(B))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Post. 3] <I.post.3>`, :just:`[I Def. 15] <I.def.15>`

Let one extremity $A$ of a straight line $AB$, given in position and in magnitude, be given. I say that the other extremity $B$ is also given.

For if $B$ were not given in position while $A$ remains fixed and the line $AB$ remains fixed in position, then either the straight line $AB$ would shift its position or its length $AB$ would change (falling at some distinct point $C$ on the same ray with $AC \neq AB$). Yet $AB$ is given both in position and in magnitude—or constructively, describing the circle with given centre $A$ and given radius $AB$ (:just:`[Post. 3] <I.post.3>`, :just:`[Data Def. 6] <D.def.6>`) cuts the position-given ray at $B$ (:just:`[Data 25] <D.25>`). Therefore $B$ is given in position.

.. _D.28:

Proposition 28 [κη΄ · Prop. XXXI]
---------------------------------

.. enunciation::

   If through a given point a straight line be drawn parallel to a straight line given in position, the straight line drawn is given in position.

*Functional Signature*: ``Given(Pos(A), Pos(Line BC)) -> Determined(Pos(Parallel(A, BC)))`` · *Dependencies*: :just:`[Data Def. 4] <D.def.4>`, :just:`[I.27] <I.27>`, :just:`[I.29] <I.29>`, :just:`[I.30] <I.30>`, :just:`[I.31] <I.31>`

Through a given point $A$, let the straight line $DAE$ be drawn parallel to a straight line $BC$ given in position (:just:`[I.31] <I.31>`). I say that $DAE$ is given in position.

For if $DAE$ were not given in position while passing through the fixed point $A$, it could shift into another straight line $FAE$ through $A$ still parallel to $BC$. Then $BC$ would be parallel simultaneously to two intersecting straight lines $DAE$ and $FAE$—which is impossible by :just:`[I.29] <I.29>` and :just:`[I.30] <I.30>` (Playfair's / Euclid's Fifth Postulate :just:`[Post. 5] <I.post.5>`). Therefore $DAE$ always occupies the same place and is given in position (:just:`[Data Def. 4] <D.def.4>`).

.. _D.29:

Proposition 29 [κθ΄ · Prop. XXXII]
----------------------------------

.. folio:: Menge 50
   :page: 50

.. enunciation::

   If to a straight line given in position, and at a given point upon it, a straight line be drawn making a given angle, the straight line drawn is given in position.

*Functional Signature*: ``Given(Pos(Line AB), Pos(C in AB), Mag(Angle theta)) -> Determined(Pos(Ray CD))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[I.23] <I.23>`

To a straight line $AB$ given in position, and at a given point $C$ on it, let a straight line $CD$ be drawn making a given angle $\angle BCD$ (:just:`[I.23] <I.23>`). I say that $CD$ is given in position.

For if $CD$ did not retain the same place (on the assigned side of $AB$) while $AB$ and $C$ remain fixed, it would shift to another ray $CE$ through $C$ making $\angle BCE = \angle BCD$, the lesser equal to the greater—which is impossible (:just:`[C.N. 5] <I.cn.5>`). Therefore $CD$ is given in position (:just:`[Data Def. 4] <D.def.4>`).

.. _D.30:

Proposition 30 [λ΄ · Prop. XXXIII]
----------------------------------

.. enunciation::

   If from a given point a straight line be drawn onto a straight line given in position making a given angle, the straight line drawn is given in position.

*Functional Signature*: ``Given(Pos(A), Pos(Line BC), Mag(Angle ADC)) -> Determined(Pos(Line AD))`` · *Dependencies*: :just:`[Data 28] <D.28>`, :just:`[Data 29] <D.29>`, :just:`[I.23] <I.23>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`

From a given point $A$ outside a straight line $BC$ given in position, let a straight line $AD$ be drawn making a given angle $\angle ADC$ with $BC$. I say that $AD$ is given in position.

Through the given point $A$ draw $EAF$ parallel to $BC$ (:just:`[I.31] <I.31>`); then $EAF$ is given in position (:just:`[Data 28] <D.28>`). Because $EAF \parallel BC$, the alternate angle $\angle EAD$ is equal to $\angle ADC$ (:just:`[I.29] <I.29>`). Yet $\angle ADC$ is given; therefore $\angle EAD$ is given. Thus to the position-given line $EAF$ and at the given point $A$ on it, the straight line $AD$ has been drawn making the given angle $\angle EAD$; therefore $AD$ is given in position (:just:`[Data 29] <D.29>`).

.. _D.31:

Proposition 31 [λα΄ · Prop. XXXIV]
----------------------------------

.. enunciation::

   If from a given point onto a straight line given in position a straight line given in magnitude be drawn, it is also given in position.

*Functional Signature*: ``Given(Pos(A), Pos(Line BC), Mag(AD >= dist(A, BC))) -> Determined(Pos(AD)) [2-root diorismos]`` · *Dependencies*: :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[I.12] <I.12>`, :just:`[Post. 3] <I.post.3>`

From a given point $A$, let a straight line $AB$ of given magnitude be drawn to meet a straight line $CD$ given in position at $B$. I say that $AB$ is given in position (up to the two symmetric intersections on $CD$).

With given centre $A$ and given distance $AB$, describe the circle $EBF$ (:just:`[Post. 3] <I.post.3>`). Since the centre $A$ is given in position and the radius $AB$ is given in magnitude, the circle $EBF$ is given in position (:just:`[Data Def. 6] <D.def.6>`). Moreover, the straight line $CD$ is given in position; therefore their intersection $B$ is given in position (:just:`[Data 25] <D.25>`). Since $A$ is also given in position, the straight line $AB$ joining $A$ and $B$ is given in position (:just:`[Data 26] <D.26>`).

.. _D.32:

Proposition 32 [λβ΄ · Prop. XXXV]
---------------------------------

.. folio:: Menge 54
   :page: 54

.. enunciation::

   If onto parallel straight lines given in position a straight line be drawn making given angles, the straight line cut off between the parallels is given in magnitude.

*Functional Signature*: ``Given(Pos(AB || CD), Mag(Angle BEF)) -> Determined(Mag(EF))`` · *Dependencies*: :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`

Between two parallel straight lines $AB$ and $CD$ given in position, let a straight line $EF$ be drawn making given angles $\angle BEF$ and $\angle EFD$. I say that $EF$ is given in magnitude.

Take any given point $G$ on $AB$, and through $G$ draw $GH$ parallel to $EF$ meeting $CD$ at $H$ (:just:`[I.31] <I.31>`). Because $GH \parallel EF$, the interior angle $\angle AGH$ (or $\angle BGH$) equals the corresponding angle $\angle BEF$ (:just:`[I.29] <I.29>`), which is given; hence $GH$ is drawn from the given point $G$ on position-given $AB$ at a given angle, so $GH$ is given in position (:just:`[Data 29] <D.29>`). Since $CD$ is also given in position, their intersection $H$ is given (:just:`[Data 25] <D.25>`). Because both $G$ and $H$ are given, $GH$ is given in magnitude (:just:`[Data 26] <D.26>`). Finally, $GEFH$ is a parallelogram, so $EF = GH$ (:just:`[I.34] <I.34>`); therefore $EF$ is given in magnitude (:just:`[Data Def. 1] <D.def.1>`).

.. _D.33:

Proposition 33 [λγ΄ · Prop. XXXVI]
----------------------------------

.. enunciation::

   If onto parallel straight lines given in position a straight line given in magnitude be drawn, it will make given angles with the parallels.

*Functional Signature*: ``Given(Pos(AB || CD), Mag(EF >= strip_width)) -> Determined(Mag(Angle BEF))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data 28] <D.28>`, :just:`[Data 31] <D.31>`, :just:`[I.29] <I.29>`, :just:`[I.34] <I.34>`

Between two parallel straight lines $AB$ and $CD$ given in position, let a straight line $EF$ of given magnitude be drawn. I say that $EF$ makes given angles $\angle BEF$ and $\angle EFD$ with the parallels.

Take a given point $G$ on $AB$, and through $G$ draw $GH$ parallel to $EF$ meeting $CD$ at $H$ (:just:`[I.31] <I.31>`). Then $GEFH$ is a parallelogram, so $GH = EF$ (:just:`[I.34] <I.34>`); since $EF$ is given in magnitude, $GH$ is given in magnitude. With given centre $G$ and given distance $GH$, describe the circle $KHL$ (:just:`[Post. 3] <I.post.3>`), which is given in position (:just:`[Data Def. 6] <D.def.6>`). Since $CD$ is given in position, the intersection $H$ is given in position (:just:`[Data 25] <D.25>`), whence the straight line $GH$ is given in position (:just:`[Data 26] <D.26>`). Because both $AB$ and $GH$ are given in position, the angle $\angle BGH$ is given; and by parallels $\angle BEF = \angle BGH$ and $\angle EFD = 2\text{ rt.} - \angle BEF$ (:just:`[I.29] <I.29>`), so $\angle BEF$ and $\angle EFD$ are given (:just:`[Data 4] <D.4>`).

.. _D.34:

Proposition 34 [λδ΄ · Prop. XXXVIII]
------------------------------------

.. enunciation::

   If to parallel straight lines given in position a straight line be drawn from a given point, it will be cut in a given ratio.

*Functional Signature*: ``Given(Pos(AB || CD), Pos(Pole E)) -> Determined(Ratio(EF : FG))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.12] <I.12>`, :just:`[VI.2] <VI.2>`, :just:`[VI.4] <VI.4>`

From a given point $E$, let a straight line $EFG$ be drawn across two parallel straight lines $AB$ and $CD$ given in position, meeting them at $F$ and $G$. I say that $EFG$ is cut in a given ratio $EF : FG$.

From the given point $E$, draw $EHK$ perpendicular to $AB$ (and hence also to $CD$), meeting $AB$ at $H$ and $CD$ at $K$ (:just:`[I.12] <I.12>`). Since $EHK$ makes a given (right) angle with position-given $AB$ from given $E$, $EHK$ is given in position (:just:`[Data 30] <D.30>`). Because $AB$ and $CD$ are given in position, the intersections $H$ and $K$ are given in position (:just:`[Data 25] <D.25>`). Since $E, H, K$ are all given in position, the segments $EH$ and $HK$ are given in magnitude (:just:`[Data 26] <D.26>`), so the ratio $EH : HK$ is given (:just:`[Data 1] <D.1>`). Yet in $\triangle EKG$, since $FH \parallel GK$, we have $EF : FG = EH : HK$ (:just:`[VI.2] <VI.2>`). Therefore the ratio $EF : FG$ is given (:just:`[Data Def. 2] <D.def.2>`).

.. _D.35:

Proposition 35 [λε΄ · Prop. XXXIX (pt. 1)]
------------------------------------------

.. enunciation::

   If from a given point onto a straight line given in position a straight line be drawn and cut in a given ratio, and through the point of section a parallel be drawn to the straight line given in position, that parallel is given in position.

*Functional Signature*: ``Given(Pos(Pole A), Pos(Line BC), InternalRatio(AE : ED)) -> Determined(Pos(Line FEG || BC))`` · *Dependencies*: :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`

From a given point $A$ outside a straight line $BC$ given in position, let a straight line $AD$ be drawn to $BC$ and produced to $E$ so that the ratio $DE : AD$ is given. I say that $E$ lies on a straight line given in position.

From $A$ draw $AF$ perpendicular to $BC$ meeting $BC$ at $F$ (:just:`[I.12] <I.12>`), and produce $AF$ to $G$ so that $FG : AF = DE : AD$ (:just:`[VI.12] <VI.12>`). Because $AF$ is drawn at a right angle from given $A$ to position-given $BC$, $AF$ is given in position (:just:`[Data 30] <D.30>`), $F$ is given (:just:`[Data 25] <D.25>`), and $AF$ is given in magnitude (:just:`[Data 26] <D.26>`). Since $FG : AF = DE : AD$ is given, $FG$ is given in magnitude (:just:`[Data 2] <D.2>`), so the extremity $G$ on the position-given ray $AFG$ is given in position (:just:`[Data 27] <D.27>`). Through $G$ draw $HGK$ parallel to $BC$ (:just:`[I.31] <I.31>`), which is given in position (:just:`[Data 28] <D.28>`). Because $AD : DE = AF : FG$, the line through $G$ and $E$ is parallel to $FD$ (:just:`[VI.2] <VI.2>`) and therefore coincides with $HGK$; hence $E$ lies on a straight line given in position.

.. _D.36:

Proposition 36 [λϛ΄ · Prop. XXXIX (pt. 2)]
------------------------------------------

.. enunciation::

   If from a given point onto a straight line given in position a straight line be drawn, and there be added to it a straight line having a given ratio to it, and through the extremity a parallel be drawn to the straight line given in position, that parallel is given in position.

*Functional Signature*: ``Given(Pos(Pole A), Pos(Line BC), ExternalRatio(AD : DE)) -> Determined(Pos(Line FEG || BC))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`

From a given point $A$ to a straight line $BC$ given in position, let $AD$ be drawn, and on $AD$ (or its opposite ray through $D$) let $DE$ be cut off toward $A$ having a given ratio $DE : AD$. I say that $E$ lies on a straight line given in position.

Draw $AF$ perpendicular to $BC$ (:just:`[I.12] <I.12>`), so $AF$ is given in position (:just:`[Data 30] <D.30>`), $F$ is given (:just:`[Data 25] <D.25>`), and $AF$ is given in magnitude (:just:`[Data 26] <D.26>`). Cut off $FG$ toward $A$ (or beyond $A$ if $DE > AD$) such that $FG : FA = DE : DA$ (:just:`[Data Def. 2] <D.def.2>`). Since $FA$ is given and $FG : FA$ is given, $FG$ is given in magnitude (:just:`[Data 2] <D.2>`), whence $G$ is given in position (:just:`[Data 27] <D.27>`). Because $FD \parallel GE$ follows from $DA : DE = FA : FG$ (and *separando* $AE : ED = AG : GF$, :just:`[V.17] <V.17>`, :just:`[VI.2] <VI.2>`), the straight line $GE$ passes through the given point $G$ parallel to position-given $BC$, and so is given in position (:just:`[Data 28] <D.28>`).

.. _D.37:

Proposition 37 [λζ΄ · Prop. XL (pt. 1)]
---------------------------------------

.. folio:: Menge 62
   :page: 62

.. enunciation::

   If onto parallel straight lines given in position a straight line be drawn and cut in a given ratio, and through the point of section a parallel be drawn to the parallels given in position, that parallel is given in position.

*Functional Signature*: ``Given(Pos(AB || CD), InternalRatio(EG : GF)) -> Determined(Pos(Line HK || AB))`` · *Dependencies*: :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`

Between two parallel straight lines $AB$ and $CD$ given in position, let any straight line $EF$ be drawn, and let $EF$ be produced to $G$ in a given ratio $EF : FG$. I say that $G$ lies on a straight line given in position parallel to $AB$ and $CD$.

Take a given point $H$ on $AB$, draw $HK$ perpendicular to $CD$ meeting $CD$ at $K$ (:just:`[I.12] <I.12>`), and produce $HK$ to $L$ so that $HK : KL = EF : FG$. By :just:`[Data 30] <D.30>`, :just:`[Data 25] <D.25>`, and :just:`[Data 26] <D.26>`, $HK$ is given in position and magnitude; since $HK : KL$ is given, $KL$ is given in magnitude (:just:`[Data 2] <D.2>`), so $L$ is given in position (:just:`[Data 27] <D.27>`). Through $L$ draw $MLN$ parallel to $CD$ (:just:`[I.31] <I.31>`), which is given in position (:just:`[Data 28] <D.28>`). Produce $EF$ to meet $MLN$ at $G'$: by parallel transversals (:just:`[VI.2] <VI.2>` via the auxiliary parallel from $H$ to $EF$), $EF : FG' = HK : KL = EF : FG$, whence $FG' = FG$ (:just:`[V.9] <V.9>`) and $G$ coincides with $G'$ on the position-given line $MLN$.

.. _D.38:

Proposition 38 [λη΄ · Prop. XL (pt. 2)]
---------------------------------------

.. enunciation::

   If onto parallel straight lines given in position a straight line be drawn, and there be added to it a straight line having a given ratio to it, and through the extremity a parallel be drawn to the parallels given in position, that parallel is given in position.

*Functional Signature*: ``Given(Pos(AB || CD), ExternalRatio(EF : FG)) -> Determined(Pos(Line HK || AB))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`

Between two parallel straight lines $AB$ and $CD$ given in position, let a straight line $EF$ be drawn and divided internally at $G$ in a given ratio $EG : GF$. I say that $G$ lies on a straight line given in position.

Take a given point $N$ on $AB$ and draw $NM$ perpendicular to $CD$ meeting $CD$ at $M$ (:just:`[I.12] <I.12>`), so $NM$ is given in position and magnitude (:just:`[Data 30] <D.30>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`). Divide $NM$ at $L$ so that $NL : LM = EG : GF$ (:just:`[VI.10] <VI.10>`); since $NM$ is given and $NL : LM$ is given, $NL$ is given in magnitude (:just:`[Data 7] <D.7>`), so $L$ is given in position (:just:`[Data 27] <D.27>`). Draw $KLH$ through $L$ parallel to $CD$, which is given in position (:just:`[Data 28] <D.28>`). Since $AB \parallel KLH \parallel CD$ cuts $NM$ and $EF$ proportionally (:just:`[VI.2] <VI.2>`), $KLH$ divides $EF$ in the ratio $NL : LM = EG : GF$, and therefore passes through $G$.
