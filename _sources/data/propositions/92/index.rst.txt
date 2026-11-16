:order: 92
:canonical_id: D.92
:breadcrumb_title: D.92
:book: Data
:proposition: 92
:type: proposition
:title: Proposition 92 [ϙβ΄ · Prop. Prop. XCVI]
:folio: Menge 178
:page: 178
:excerpt: If a point be taken inside a circle given in position, and through the point some straight line be drawn across the circle, the rectangle contained by the segments of the drawn straight line is given.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

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
