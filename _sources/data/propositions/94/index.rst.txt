:order: 94
:canonical_id: D.94
:breadcrumb_title: D.94
:book: Data
:proposition: 94
:type: proposition
:title: Proposition 94 [ϙδ΄ · Prop. Prop. XCIX (cf. Prop. C [Stewart])]
:folio: Menge 184
:page: 184
:excerpt: If in the diameter of a circle given in position a given point be taken, and from that point a straight line be drawn to the circle, and from the section a perpendicular be drawn to the drawn line, and through the point where the perpendicular meets the circumference again a parallel be drawn to the first drawn line, both the point at which the parallel meets the diameter is given, and the rectangle contained by the parallel chords is given.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

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
