:order: 60
:type: chapter
:canonical_id: D.unit.6
:folio: Menge pp. 164–186
:book: Propositions 84–94: Circles, Chords & Angle Bisectors
:description: Canonical two-line systems xy = A² with x − y = d (D.84), x + y = s (D.85), and x² − y² = C² (D.86); circles given in magnitude and position, inscribed angle loci, and chord/arc determination (D.87–D.89); secant/chord power of a point (D.90–D.92); the celebrated Prop. 93 interior angle-bisector theorem; and its orthogonal chord-reflection corollary (D.94).

.. _data-unit-6-en:

===========================================================================================
Unit 6: Hyperbolic/Elliptic Systems, Circles, Chords & Angle Bisectors (Propositions 84–94)
===========================================================================================

*Canonical Two-Segment Quadratic Systems, Circular Loci, Chord Power, and the Prop. 93 Bisector Theorem* — **D.84–D.94 (Simson LXXXV–C) · Menge (1896) pp. 164–186**

.. note::

   **Edition Track (English)**: Canonical two-line systems xy = A² with x − y = d (D.84), x + y = s (D.85), and x² − y² = C² (D.86); circles given in magnitude and position, inscribed angle loci, and chord/arc determination (D.87–D.89); secant/chord power of a point (D.90–D.92); the celebrated Prop. 93 interior angle-bisector theorem; and its orthogonal chord-reflection corollary (D.94). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. _D.84:

Proposition 84 [πδ΄ · Prop. LXXXV]
----------------------------------

.. folio:: Menge 164
   :page: 164

.. enunciation::

   If two straight lines contain a given area in a given angle, and one exceed the other by a given straight line, each of them will also be given.

*Functional Signature*: ``Given(Angle B, Area(x, y) = S, y - x = d) -> Determined(Mag(x), Mag(y))`` · *Dependencies*: :just:`[Data 3] <D.3>`, :just:`[Data 59] <D.59>`, :just:`[I.31] <I.31>`

Let two straight lines $AB$ and $BC$ contain a given area $AB \cdot BC$ in a given angle $\angle ABC$, and let $BC$ exceed $AB$ by a given straight line. I say that each of $AB$ and $BC$ is given in magnitude.

On $BC$ cut off $BD = AB$ (:just:`[I.3] <I.3>`). Since $BC$ exceeds $AB$ ($= BD$) by a given magnitude, the remainder $DC = BC - BD$ is given in magnitude! Complete the parallelogram $ABCE$ in the given angle $\angle ABC$ (whose area is given by hypothesis), and draw $DF$ parallel to $AB$ meeting $AE$ at $F$ (:just:`[I.31] <I.31>`), splitting $ABCE$ into $ABDF$ and $FDCE$. Because $BD = AB$ and $\angle ABD$ is given, the rhombus $ABDF$ has all sides equal ($1:1$) and all angles given, so $ABDF$ is given in species (:just:`[Data Def. 3] <D.def.3>`). Thus the given parallelogram $ABCE$ has been applied to the given straight line $DC$, :term:`exceeding <hyperbole>` by the parallelogram $ABDF$ given in species! By :just:`[Data 59] <D.59>`, the sides of the excess—namely $BD$ ($= AB$)—are given in magnitude; and adding given $DC$ to $BD$ yields $BC$ given in magnitude (:just:`[Data 3] <D.3>`).

.. _D.85:

Proposition 85 [πε΄ · Prop. LXXXVI]
-----------------------------------

.. folio:: Menge 166
   :page: 166

.. enunciation::

   If two straight lines contain a given area in a given angle, and both taken together be given, each of them will also be given.

*Functional Signature*: ``Given(Angle B, Area(x, y) = S, x + y = s) -> Determined(Mag(x), Mag(y)) [diorismos]`` · *Dependencies*: :just:`[Data 4] <D.4>`, :just:`[Data 58] <D.58>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`

Let two straight lines $AB$ and $BC$ contain a given area $AB \cdot BC$ in a given angle $\angle ABC$, and let the sum $AB + BC$ be given in magnitude. I say that each of $AB$ and $BC$ is given in magnitude.

Produce $CB$ to $D$ so that $BD = AB$ (:just:`[I.3] <I.3>`). Since the compound $AB + BC$ is given, the whole straight line $DC = DB + BC$ is given in magnitude. Complete the given parallelogram $ABCE$ in the given angle $\angle ABC$, and complete the supplementary rhombus $ABDF$ on $BD = AB$ between the same parallels $DC$ and $FE$ (:just:`[I.31] <I.31>`). Because $BD = AB$ and the adjacent angle $\angle ABD = 2\\text{ rt.} - \angle ABC$ is given (:just:`[I.13] <I.13>`, :just:`[Data 4] <D.4>`), the rhombus $ABDF$ is given in species (:just:`[Data Def. 3] <D.def.3>`). Thus the given area $ABCE$ has been applied to the given straight line $DC$, :term:`deficient <elleipsis>` by the species-given figure $ABDF$! By :just:`[Data 58] <D.58>`, the segments $BD$ ($= AB$) and $BC$ are both given in magnitude.

.. _D.86:

Proposition 86 [πϛ΄ · Prop. LXXXIX (cf. LXXXVII–LXXXVIII)]
----------------------------------------------------------

.. folio:: Menge 168
   :page: 168

.. enunciation::

   If two straight lines contain a given area in a given angle, and the square on one be greater than the square on the other by a given area than in ratio, each of them will also be given.

*Functional Signature*: ``Given(Angle B, x*y*sin B = S, (y^2 - D) : x^2 = k) -> Determined(Mag(x), Mag(y))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 55] <D.55>`, :just:`[Data 57] <D.57>`, :just:`[Data 58] <D.58>`, :just:`[Data 59] <D.59>`, :just:`[Data 68] <D.68>`, :just:`[II.4] <II.4>`, :just:`[II.6] <II.6>`, :just:`[VI.1] <VI.1>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`

Let two straight lines $AB$ and $BC$ contain a given area $AB \cdot BC$ in a given angle $\angle ABC$, and let the square $BC^2$ be :term:`greater by a given area than in ratio <dothenti-meizon-e-en-logo>` to the square $AB^2$. I say that each of $AB$ and $BC$ is given in magnitude.

Since $BC^2$ is greater by a given area than in ratio to $AB^2$, subtract the given area—expressed as a rectangle $BC \cdot BD$ applied to $BC$ (:just:`[I.44] <I.44>`), so $BC^2 - BC \cdot BD = BC \cdot DC$ (:just:`[II.2] <II.2>`) has a given ratio to $AB^2$ (:just:`[Data Def. 11] <D.def.11>`). Moreover, since the parallelogram $ABEC$ in the given angle $\angle ABC$ is given in magnitude, the rectangle $AB \cdot BC$ also is given in magnitude (having a given ratio to $ABEC$ by :just:`[Data 66] <D.66>` and :just:`[Data 2] <D.2>`), while $BC \cdot BD$ is given in magnitude! Therefore the ratio $(BC \cdot BD) : (AB \cdot BC) = BD : AB$ (:just:`[Data 1] <D.1>`, :just:`[VI.1] <VI.1>`) is given, whence $BD^2 : AB^2$ is given (:just:`[Data 50] <D.50>`). Combining $(BC \cdot DC) : AB^2$ with $AB^2 : BD^2$ gives $(BC \cdot DC) : BD^2$ given (:just:`[Data 8] <D.8>`), so $4\,(BC \cdot DC) : BD^2$ is given. Yet by :just:`[II.8] <II.8>` (taking $E$ with $BE = BD$, or directly $(BC + DC)^2 = (2\,BC - BD)^2 = 4\,BC \cdot DC + BD^2$!), adding $BD^2$ *componendo* (:just:`[Data 6] <D.6>`) gives $(2\,BC - BD)^2 : BD^2$ given! Extracting the square root via :just:`[Data 54] <D.54>` yields $(2\,BC - BD) : BD$ given, whence *componendo* $2\,BC : BD$ and $BC : BD$ are given (:just:`[Data 6] <D.6>`). Combining $BC : BD$ with $BD : AB$ gives $BC : AB$ given (:just:`[Data 8] <D.8>`). Thus the given parallelogram $ABEC$ has given angles and given side ratio $BC : AB$, so $ABEC$ is given in species (:just:`[Data Def. 3] <D.def.3>`) as well as in magnitude; therefore $AB$ and $BC$ are given in magnitude (:just:`[Data 55] <D.55>`).

.. picture:: /_static/figures/data_06_circle_angle_locus.svg
   :alt: Circle Chords, Inscribed Angles, and Tangent-Secant Power (D.87–D.91)

Interactive circle-locus diagram (:cite:`Menge pp. 168–178 <menge:1896>`): In circle :g:`(O, OA) <data_06_circle_angle_locus:( O A )>` with centre :g:`O <data_06_circle_angle_locus:O>` and diameter :g:`CE <data_06_circle_angle_locus:/ C E />`, chord :g:`BC <data_06_circle_angle_locus:/ B C />` subtends given inscribed angle :g:`∠BAC <data_06_circle_angle_locus:< B A C )>` in :g:`△ABC <data_06_circle_angle_locus:< A B C >>`, calibrated via right-angled triangle on :g:`BE <data_06_circle_angle_locus:/ B E />` (:ref:`D.87 <D.87>`–:ref:`D.88 <D.88>`). From external given point :g:`P <data_06_circle_angle_locus:P>`, tangent :g:`PT <data_06_circle_angle_locus:/ P T />` (perpendicular to radius :g:`OT <data_06_circle_angle_locus:/ O T />` at :g:`T <data_06_circle_angle_locus:T>`, :ref:`D.90 <D.90>`) fixes the secant power along :g:`CP <data_06_circle_angle_locus:/ C P />` (:ref:`D.91 <D.91>`).

.. _D.87:

Proposition 87 [πζ΄ · Prop. XCI]
--------------------------------

.. folio:: Menge 172
   :page: 172

.. enunciation::

   If in a circle given in magnitude a straight line be drawn cutting off a segment that accepts a given angle, the straight line drawn is given in magnitude.

*Functional Signature*: ``Given(CircleRadius R, InscribedAngle theta) -> Determined(Mag(Chord BC = 2*R*sin theta))`` · *Dependencies*: :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`, :just:`[Data 40] <D.40>`, :just:`[Data 53] <D.53>`, :just:`[III.21] <III.21>`, :just:`[III.31] <III.31>`

In a circle $ABC$ :term:`given in magnitude <megethei>` (:just:`[Data Def. 5] <D.def.5>`), let a straight line $AC$ be drawn cutting off a segment $ABC$ that admits a given angle $\angle ABC$ (:just:`[Data Def. 7] <D.def.7>`). I say that the chord $AC$ is given in magnitude.

Take the centre $D$ of circle $ABC$ (:just:`[III.1] <III.1>`), draw the diameter $ADE$ through $A$ and $D$, and join $EC$. Since the circle $ABC$ is given in magnitude, its radius $AD$ and diameter $AE = 2\,AD$ are given in magnitude (:just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`). In the semicircle $ACE$, the angle $\angle ACE$ is right (:just:`[III.31] <III.31>`). Moreover, either $B$ and $E$ lie in the same segment on $AC$ so $\angle AEC = \angle ABC$ (:just:`[III.21] <III.21>`), or they lie in opposite segments of the cyclic quadrilateral $ABCE$ so $\angle AEC = 2\\text{ rt.} - \angle ABC$ (:just:`[III.22] <III.22>`, :just:`[Data 4] <D.4>`); in either case $\angle AEC$ is given. Therefore right-angled $\\triangle ACE$ has all angles given and is given in species (:just:`[Data 40] <D.40>`), so the ratio $AC : AE$ is given (:just:`[Data Def. 3] <D.def.3>`). Since the diameter $AE$ is given in magnitude, the chord $AC$ is given in magnitude (:just:`[Data 2] <D.2>`).

.. _D.88:

Proposition 88 [πη΄ · Prop. XCII]
---------------------------------

.. enunciation::

   If in a circle given in magnitude a straight line given in magnitude be drawn, it will cut off a segment accepting a given angle.

*Functional Signature*: ``Given(CircleRadius R, Mag(Chord BC <= 2R)) -> Determined(Mag(InscribedAngle BAC))`` · *Dependencies*: :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 1] <D.1>`, :just:`[Data 3] <D.3>`, :just:`[Data 43] <D.43>`, :just:`[III.21] <III.21>`, :just:`[III.22] <III.22>`, :just:`[III.31] <III.31>`

In a circle $ABC$ given in magnitude, let a chord $AC$ given in magnitude be drawn. I say that $AC$ cuts off a segment $ABC$ admitting a given angle $\angle ABC$.

Take the centre $D$ (:just:`[III.1] <III.1>`), draw the diameter $ADE$, and join $EC$. Since the circle is given in magnitude, its diameter $AE$ is given in magnitude (:just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`). Because $AC$ is also given in magnitude, the ratio $AE : AC$ is given (:just:`[Data 1] <D.1>`). Now $\\triangle ACE$ is right-angled at $C$ (:just:`[III.31] <III.31>`) with the ratio of hypotenuse $AE$ to leg $AC$ given; hence $\\triangle ACE$ is uniquely given in species (:just:`[Data 43] <D.43>`). Therefore the angle $\angle AEC$ is given, whence the inscribed angle $\angle ABC$ (equal to $\angle AEC$ by :just:`[III.21] <III.21>`, or supplementary to it in the opposite arc by :just:`[III.22] <III.22>` and :just:`[Data 4] <D.4>`) is given, so segment $ABC$ admits a given angle (:just:`[Data Def. 8] <D.def.8>`).

.. _D.89:

Proposition 89 [πθ΄ · Prop. XCIII]
----------------------------------

.. enunciation::

   If on the circumference of a circle given in position a given point be taken, and from it a straight line be inflected to the circumference of the circle making a given angle, the other extremity of the inflected line is given.

*Functional Signature*: ``Given(PosMag(Circle(D, R)), Pos(B on circle), Mag(InscribedAngle BAC)) -> Determined(Pos(C))`` · *Dependencies*: :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 29] <D.29>`, :just:`[III.1] <III.1>`, :just:`[III.20] <III.20>`

Let a point $B$ be given on the circumference of a circle $ABC$ :term:`given in position <thesei>` (:just:`[Data Def. 6] <D.def.6>`), and from $B$ to another point $C$ on the circumference let two straight lines $BA, AC$ be inflected at a variable point $A$ on the circumference so as to contain a given angle $\angle BAC$ (with $C$ on a specified side of $B$). I say that the point $C$ is given in position.

Take the centre $D$ of the position-given circle $ABC$ (:just:`[III.1] <III.1>`); then $D$ is given in position (:just:`[Data Def. 6] <D.def.6>`). Join $DB$ and $DC$. Since both $D$ and $B$ are given in position, the radius $DB$ is given in position (:just:`[Data 26] <D.26>`). Moreover, the central angle $\angle BDC$ is double the inscribed angle $\angle BAC$ (:just:`[III.20] <III.20>`, or $2\,(2\\text{ rt.} - \angle BAC)$ if $\angle BAC$ stands in the minor segment). Because $\angle BAC$ is given, its double $\angle BDC$ is given (:just:`[Data 3] <D.3>`). Thus at the given point $D$ on the position-given line $DB$, the ray $DC$ is drawn making a given angle $\angle BDC$; therefore $DC$ is given in position (:just:`[Data 29] <D.29>`). Since the circumference $ABC$ is also given in position, their intersection $C$ is given in position (:just:`[Data 25] <D.25>`).

.. _D.90:

Proposition 90 [ϙ΄ · Prop. XCIV]
--------------------------------

.. folio:: Menge 176
   :page: 176

.. enunciation::

   If from a given point a straight line be drawn touching a circle given in position, the straight line drawn is given in position and in magnitude.

*Functional Signature*: ``Given(PosMag(Circle(O, R)), Pos(D outside)) -> Determined(Pos(DA), Mag(DA = sqrt(OD^2 - R^2)))`` · *Dependencies*: :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 43] <D.43>`, :just:`[Data 53] <D.53>`, :just:`[III.17] <III.17>`, :just:`[III.18] <III.18>`, :just:`[III.31] <III.31>`

From a given point $C$ outside a circle $AB$ given in position, let a straight line $CA$ be drawn touching the circle at $A$ (:just:`[III.17] <III.17>`). I say that the tangent $CA$ is given both in position and in magnitude.

Take the centre $D$ of the position-given circle $AB$ (:just:`[III.1] <III.1>`), so $D$ is given in position (:just:`[Data Def. 6] <D.def.6>`), and join $DA$ and $DC$. Since both $D$ and $C$ are given in position, $DC$ is given in position and magnitude (:just:`[Data 26] <D.26>`). Because $CA$ touches the circle at $A$, the angle $\angle DAC$ is right (:just:`[III.18] <III.18>`); therefore the semicircle $DAC$ described on diameter $DC$ passes through $A$ (:just:`[III.31] <III.31>`). Since $DC$ is given in position and magnitude, the semicircle $DAC$ is given in position (:just:`[Data Def. 6] <D.def.6>`). Because the circle $AB$ is also given in position, their intersection $A$ is given in position (:just:`[Data 25] <D.25>`). Joining $A$ to the given point $C$, the tangent $CA$ is given both in position and in magnitude (:just:`[Data 26] <D.26>`).

.. _D.91:

Proposition 91 [ϙα΄ · Prop. XCV]
--------------------------------

.. folio:: Menge 178
   :page: 178

.. enunciation::

   If a point be taken outside a circle given in position, and from the point some straight line be drawn across the circle, the rectangle contained by the whole drawn straight line and the segment intercepted outside between the point and the convex circumference is given.

*Functional Signature*: ``Given(PosMag(Circle(O, R)), Pos(External D)) -> Determined(Mag(DB * DC = OD^2 - R^2))`` · *Dependencies*: :just:`[Data 52] <D.52>`, :just:`[Data 90] <D.90>`, :just:`[III.17] <III.17>`, :just:`[III.36] <III.36>`

Outside a circle $ABC$ given in position let a given point $D$ be taken, and from $D$ let any secant straight line $DCB$ be drawn cutting the circle at $C$ and $B$. I say that the rectangle $BD \cdot DC$ contained by the whole secant and its external segment is given in magnitude.

From the given point $D$ draw the tangent $DA$ touching the circle $ABC$ at $A$ (:just:`[III.17] <III.17>`). By :just:`[Data 90] <D.90>`, the tangent $DA$ is given in position and in magnitude. Because $DA$ is given in magnitude, the square $DA^2$ described on it is given in magnitude (:just:`[Data 52] <D.52>`). Yet by the tangent-secant theorem (:just:`[III.36] <III.36>`), $BD \cdot DC = DA^2$. Therefore the rectangle $BD \cdot DC$ is given in magnitude.

.. _D.92:

Proposition 92 [ϙβ΄ · Prop. XCVI]
---------------------------------

.. enunciation::

   If a point be taken inside a circle given in position, and through the point some straight line be drawn across the circle, the rectangle contained by the segments of the drawn straight line is given.

*Functional Signature*: ``Given(PosMag(Circle(O, R)), Pos(Internal D)) -> Determined(Mag(BD * DC = R^2 - OD^2))`` · *Dependencies*: :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 52] <D.52>`, :just:`[III.1] <III.1>`, :just:`[III.35] <III.35>`

Inside a circle $BC$ given in position let a given point $A$ be taken, and through $A$ let any chord $CB$ be drawn across the circle. I say that the rectangle $CA \cdot AB$ contained by its segments is given in magnitude.

Take the centre $D$ of the circle (:just:`[III.1] <III.1>`), which is given in position (:just:`[Data Def. 6] <D.def.6>`), and join $AD$ and produce it in both directions to meet the circumference at $F$ and $E$ (if $A$ coincides with $D$, every chord through $A$ is a diameter and $CA \cdot AB = R^2$ immediately). Since both $D$ and $A$ are given in position, the line $FAE$ is given in position (:just:`[Data 26] <D.26>`), and its intersections $F$ and $E$ with the position-given circle are given in position (:just:`[Data 25] <D.25>`). Therefore the segments $FA$ and $AE$ are both given in magnitude (:just:`[Data 26] <D.26>`), whence the rectangle $FA \cdot AE$ is given in magnitude. By the intersecting-chords theorem (:just:`[III.35] <III.35>`), $CA \cdot AB = FA \cdot AE$; therefore $CA \cdot AB$ is given in magnitude.

.. picture:: /_static/figures/data_07_prop93_bisector.svg
   :alt: Proposition 93 — Inscribed Angle Bisector & Harmonic-Cyclic Product

Interactive diagram for :ref:`Proposition 93 <D.93>` (:cite:`Menge pp. 180–184 <menge:1896>`): In magnitude-given circle :g:`(O, OA) <data_07_prop93_bisector:( O A )>`, chord :g:`BC <data_07_prop93_bisector:/ B C />` cuts off segment :g:`△ABC <data_07_prop93_bisector:< A B C >>`, and chord :g:`AD <data_07_prop93_bisector:/ A D />` bisects the inscribed angle into :eq:`equal half-angles <data_07_prop93_bisector:< B A D ) = data_07_prop93_bisector:< D A C )>` :g:`∠BAD <data_07_prop93_bisector:< B A D )>` and :g:`∠DAC <data_07_prop93_bisector:< D A C )>`, meeting :g:`BC <data_07_prop93_bisector:/ B C />` at :g:`E <data_07_prop93_bisector:E>` and the arc midpoint at :g:`D <data_07_prop93_bisector:D>` (:eq:`BD = CD <data_07_prop93_bisector:/ B D / = data_07_prop93_bisector:/ C D />`). Similarity of :g:`△ABD <data_07_prop93_bisector:< A B D >>` with $AEC$ and $DEB$ yields both $(BA + AC) : AD = BC : BD$ (:g:`AB <data_07_prop93_bisector:/ A B />` + :g:`AC <data_07_prop93_bisector:/ A C />`) and $(BA + AC) \cdot ED = BC \cdot BD$.

.. _D.93:

Proposition 93 [ϙγ΄ · Prop. XCVII (cf. Prop. XCVIII [Stanhope])]
----------------------------------------------------------------

.. enunciation::

   If into a circle given in magnitude a straight line be drawn cutting off a segment accepting a given angle, and the angle in the segment be bisected, both the straight lines containing the given angle taken together will have a given ratio to the bisecting chord, and the rectangle contained by both the straight lines containing the given angle taken together and the lower segment cut off from the bisector toward the circumference will be given.

*Functional Signature*: ``Given(CircleRadius R, InscribedAngle A, Bisector AD cap BC = E) -> Determined(Ratio((AB+AC):AD), Mag((AB+AC)*ED))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 52] <D.52>`, :just:`[Data 87] <D.87>`, :just:`[III.21] <III.21>`, :just:`[III.26] <III.26>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[VI.3] <VI.3>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`

Into a circle $ABC$ given in magnitude, let a straight line $BC$ be drawn cutting off a segment $BAC$ that admits a given angle $\angle BAC$, and let $\angle BAC$ be bisected by the chord $AD$ meeting $BC$ at $E$ and the opposite arc at $D$ (:just:`[I.9] <I.9>`). I say that $(BA + AC)$ has a given ratio to $AD$, and that the rectangle $(BA + AC) \cdot ED$ is given in magnitude.

Join $BD$. Since the circle $ABC$ is given in magnitude and the segment $BAC$ admits the given angle $\angle BAC$, the chord $BC$ is given in magnitude (:just:`[Data 87] <D.87>`). Because $\angle BAC$ is given, its half $\angle BAD$ ($= \angle EAC$) is given (:just:`[Data 7] <D.7>`), so in the same magnitude-given circle the chord $BD$ subtending $\angle BAD$ is also given in magnitude (:just:`[Data 87] <D.87>`). Hence the ratio $BC : BD$ is given (:just:`[Data 1] <D.1>`). Now since $AE$ bisects $\angle BAC$, we have $BA : AC = BE : EC$ (:just:`[VI.3] <VI.3>`), whence *alternando* $AB : BE = AC : CE$ (:just:`[V.16] <V.16>`), and *componendo* $(BA + AC) : BC = AC : CE$ (:just:`[V.12] <V.12>`). Moreover, in $\\triangle AEC$ and $\\triangle ABD$, $\angle EAC = \angle BAD$ and the inscribed angles $\angle ACE = \angle ADB$ subtend the same arc $AB$ (:just:`[III.21] <III.21>`), so $\\triangle AEC \sim \\triangle ABD$ (:just:`[VI.4] <VI.4>`), giving $AC : CE = AD : BD$. Therefore $(BA + AC) : BC = AD : BD$ (:just:`[V.11] <V.11>`), and *alternando* $(BA + AC) : AD = BC : BD$ (:just:`[V.16] <V.16>`). Since $BC : BD$ is given, $(BA + AC) : AD$ is given.

Second, I say that the rectangle $(BA + AC) \cdot ED$ is given in magnitude. In $\\triangle AEC$ and $\\triangle DEB$, the vertical angles at $E$ are equal (:just:`[I.15] <I.15>`) and $\angle ACE = \angle EDB$ (:just:`[III.21] <III.21>`), while $\angle EAC = \angle BAD = \angle EBD$ (subtending equal arcs $DC$ and $BD$); thus $\\triangle AEC \sim \\triangle DEB$ (:just:`[VI.4] <VI.4>`), giving $BD : DE = AC : CE$. Substituting $(BA + AC) : CB = AC : CE$ yields $(BA + AC) : CB = BD : DE$, whence $(BA + AC) \cdot ED = CB \cdot BD$ (:just:`[VI.16] <VI.16>`). Because both $CB$ and $BD$ are given in magnitude, the rectangle $CB \cdot BD$ is given in magnitude, and therefore $(BA + AC) \cdot ED$ is given in magnitude.

.. _D.94:

Proposition 94 [ϙδ΄ · Prop. XCIX (cf. Prop. C [Stewart])]
---------------------------------------------------------

.. folio:: Menge 184
   :page: 184

.. enunciation::

   If in the diameter of a circle given in position a given point be taken, and from that point a straight line be drawn to the circle, and from the section a perpendicular be drawn to the drawn line, and through the point where the perpendicular meets the circumference again a parallel be drawn to the first drawn line, both the point at which the parallel meets the diameter is given, and the rectangle contained by the parallel chords is given.

*Functional Signature*: ``Given(PosMag(Circle(H, R)), Pos(D on diam BC), ∠DAE = 90°, EF || DA) -> Determined(Pos(F = 2H - D), Mag(AD * EF = |R^2 - HD^2|))`` · *Dependencies*: :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 91] <D.91>`, :just:`[Data 92] <D.92>`, :just:`[I.4] <I.4>`, :just:`[I.26] <I.26>`, :just:`[I.29] <I.29>`, :just:`[III.31] <III.31>`, :just:`[III.35] <III.35>`

In a circle $ABC$ given in position, on its diameter $BC$ let a given point $D$ be taken; through $D$ let any straight line $DA$ be drawn to the circumference at $A$, from $A$ let $AE$ be drawn at right angles to $DA$ meeting the circumference at $E$ (:just:`[I.11] <I.11>`), and through $E$ let $EF$ be drawn parallel to $AD$ meeting the diameter $BC$ at $F$ (:just:`[I.31] <I.31>`). I say that the point $F$ is given in position, and that the rectangle $AD \cdot EF$ is given in magnitude.

Produce $EF$ to meet the circumference again at $H$, and join $AH$. Because $AD \parallel EH$ and $\angle DAE$ is right, the interior alternate angle $\angle HEA$ is also right (:just:`[I.29] <I.29>`); therefore $HA$ is a diameter of the circle $ABC$ (:just:`[III.31] <III.31>`). Since $BC$ is also a diameter, their intersection $G$ is the centre of the position-given circle $ABC$, so $G$ is given in position (:just:`[Data Def. 6] <D.def.6>`). Because $D$ is also given in position, $DG$ is given in magnitude (:just:`[Data 26] <D.26>`). Now in $\\triangle AGD$ and $\\triangle HGF$, the radii $AG$ and $HG$ are equal, the vertical angles at $G$ are equal (:just:`[I.15] <I.15>`), and the alternate angles $\angle GAD = \angle GHF$ (from $AD \parallel EH$) are equal (:just:`[I.29] <I.29>`); hence $\\triangle AGD \cong \\triangle HGF$ (:just:`[I.26] <I.26>`), so $FG = DG$ and $FH = AD$. Since $DG$ is given in magnitude, $FG$ is given in magnitude along the position-given diameter $BC$ from given $G$, whence $F$ is given in position (:just:`[Data 27] <D.27>`). Finally, because the chord $EFH$ passes through the given interior point $F$ of the position-given circle $ABC$, the rectangle $EF \cdot FH$ is given in magnitude (:just:`[Data 92] <D.92>`); substituting $FH = AD$ proves that $AD \cdot EF$ is given in magnitude.
