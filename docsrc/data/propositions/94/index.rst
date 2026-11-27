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

In a circle :math:`ABC` given in position, on its diameter :math:`BC` let a given point :math:`D` be taken; through :math:`D` let any straight line :math:`DA` be drawn to the circumference at :math:`A`, from :math:`A` let :math:`AE` be drawn at right angles to :math:`DA` meeting the circumference at :math:`E` (:just:`[I.11] <I.11>`), and through :math:`E` let :math:`EF` be drawn parallel to :math:`AD` meeting the diameter :math:`BC` at :math:`F` (:just:`[I.31] <I.31>`). I say that the point :math:`F` is given in position, and that the rectangle :math:`AD \cdot EF` is given in magnitude.

Produce :math:`EF` to meet the circumference again at :math:`H`, and join :math:`AH`. Because :math:`AD \parallel EH` and :math:`\angle DAE` is right, the interior alternate angle :math:`\angle HEA` is also right (:just:`[I.29] <I.29>`); therefore :math:`HA` is a diameter of the circle :math:`ABC` (:just:`[III.31] <III.31>`). Since :math:`BC` is also a diameter, their intersection :math:`G` is the centre of the position-given circle :math:`ABC`, so :math:`G` is given in position (:just:`[Data Def. 6] <D.def.6>`). Because :math:`D` is also given in position, :math:`DG` is given in magnitude (:just:`[Data 26] <D.26>`). Now in :math:`\\triangle AGD` and :math:`\\triangle HGF`, the radii :math:`AG` and :math:`HG` are equal, the vertical angles at :math:`G` are equal (:just:`[I.15] <I.15>`), and the alternate angles :math:`\angle GAD = \angle GHF` (from :math:`AD \parallel EH`) are equal (:just:`[I.29] <I.29>`); hence :math:`\\triangle AGD \cong \\triangle HGF` (:just:`[I.26] <I.26>`), so :math:`FG = DG` and :math:`FH = AD`. Since :math:`DG` is given in magnitude, :math:`FG` is given in magnitude along the position-given diameter :math:`BC` from given :math:`G`, whence :math:`F` is given in position (:just:`[Data 27] <D.27>`). Finally, because the chord :math:`EFH` passes through the given interior point :math:`F` of the position-given circle :math:`ABC`, the rectangle :math:`EF \cdot FH` is given in magnitude (:just:`[Data 92] <D.92>`); substituting :math:`FH = AD` proves that :math:`AD \cdot EF` is given in magnitude.
