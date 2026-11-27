:order: 93
:canonical_id: D.93
:breadcrumb_title: D.93
:book: Data
:proposition: 93
:type: proposition
:title: Proposition 93 [ϙγ΄ · Prop. Prop. XCVII (cf. Prop. XCVIII [Stanhope])]
:folio: Menge 178
:page: 178
:excerpt: If into a circle given in magnitude a straight line be drawn cutting off a segment accepting a given angle, and the angle in the segment be bisected, both the straight lines containing the given angle taken together will have a given ratio to the bisecting chord, and the rectangle contained by both the straight lines containing the given angle taken together and the lower segment cut off from the bisector toward the circumference will be given.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. picture:: /_static/figures/data_07_prop93_bisector.svg
   :alt: Proposition 93 — Inscribed Angle Bisector & Harmonic-Cyclic Product

Interactive diagram for :ref:`Proposition 93 <D.93>` (:cite:`Menge pp. 180–184 <menge:1896>`): In magnitude-given circle :g:`(O, OA) <data_07_prop93_bisector:( O A )>`, chord :g:`BC <data_07_prop93_bisector:/ B C />` cuts off segment :g:`△ABC <data_07_prop93_bisector:< A B C >>`, and chord :g:`AD <data_07_prop93_bisector:/ A D />` bisects the inscribed angle into :eq:`equal half-angles <data_07_prop93_bisector:< B A D ) = data_07_prop93_bisector:< D A C )>` :g:`∠BAD <data_07_prop93_bisector:< B A D )>` and :g:`∠DAC <data_07_prop93_bisector:< D A C )>`, meeting :g:`BC <data_07_prop93_bisector:/ B C />` at :g:`E <data_07_prop93_bisector:E>` and the arc midpoint at :g:`D <data_07_prop93_bisector:D>` (:eq:`BD = CD <data_07_prop93_bisector:/ B D / = data_07_prop93_bisector:/ C D />`). Similarity of :g:`△ABD <data_07_prop93_bisector:< A B D >>` with :math:`AEC` and :math:`DEB` yields both :math:`(BA + AC) : AD = BC : BD` (:g:`AB <data_07_prop93_bisector:/ A B />` + :g:`AC <data_07_prop93_bisector:/ A C />`) and :math:`(BA + AC) \cdot ED = BC \cdot BD`.

.. _D.93:

Proposition 93 [ϙγ΄ · Prop. XCVII (cf. Prop. XCVIII [Stanhope])]
----------------------------------------------------------------

.. enunciation::

   If into a circle given in magnitude a straight line be drawn cutting off a segment accepting a given angle, and the angle in the segment be bisected, both the straight lines containing the given angle taken together will have a given ratio to the bisecting chord, and the rectangle contained by both the straight lines containing the given angle taken together and the lower segment cut off from the bisector toward the circumference will be given.

*Functional Signature*: ``Given(CircleRadius R, InscribedAngle A, Bisector AD cap BC = E) -> Determined(Ratio((AB+AC):AD), Mag((AB+AC)*ED))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 52] <D.52>`, :just:`[Data 87] <D.87>`, :just:`[III.21] <III.21>`, :just:`[III.26] <III.26>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[VI.3] <VI.3>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`

Into a circle :math:`ABC` given in magnitude, let a straight line :math:`BC` be drawn cutting off a segment :math:`BAC` that admits a given angle :math:`\angle BAC`, and let :math:`\angle BAC` be bisected by the chord :math:`AD` meeting :math:`BC` at :math:`E` and the opposite arc at :math:`D` (:just:`[I.9] <I.9>`). I say that :math:`(BA + AC)` has a given ratio to :math:`AD`, and that the rectangle :math:`(BA + AC) \cdot ED` is given in magnitude.

Join :math:`BD`. Since the circle :math:`ABC` is given in magnitude and the segment :math:`BAC` admits the given angle :math:`\angle BAC`, the chord :math:`BC` is given in magnitude (:just:`[Data 87] <D.87>`). Because :math:`\angle BAC` is given, its half :math:`\angle BAD` (:math:`= \angle EAC`) is given (:just:`[Data 7] <D.7>`), so in the same magnitude-given circle the chord :math:`BD` subtending :math:`\angle BAD` is also given in magnitude (:just:`[Data 87] <D.87>`). Hence the ratio :math:`BC : BD` is given (:just:`[Data 1] <D.1>`). Now since :math:`AE` bisects :math:`\angle BAC`, we have :math:`BA : AC = BE : EC` (:just:`[VI.3] <VI.3>`), whence *alternando* :math:`AB : BE = AC : CE` (:just:`[V.16] <V.16>`), and *componendo* :math:`(BA + AC) : BC = AC : CE` (:just:`[V.12] <V.12>`). Moreover, in :math:`\\triangle AEC` and :math:`\\triangle ABD`, :math:`\angle EAC = \angle BAD` and the inscribed angles :math:`\angle ACE = \angle ADB` subtend the same arc :math:`AB` (:just:`[III.21] <III.21>`), so :math:`\\triangle AEC \sim \\triangle ABD` (:just:`[VI.4] <VI.4>`), giving :math:`AC : CE = AD : BD`. Therefore :math:`(BA + AC) : BC = AD : BD` (:just:`[V.11] <V.11>`), and *alternando* :math:`(BA + AC) : AD = BC : BD` (:just:`[V.16] <V.16>`). Since :math:`BC : BD` is given, :math:`(BA + AC) : AD` is given.

Second, I say that the rectangle :math:`(BA + AC) \cdot ED` is given in magnitude. In :math:`\\triangle AEC` and :math:`\\triangle DEB`, the vertical angles at :math:`E` are equal (:just:`[I.15] <I.15>`) and :math:`\angle ACE = \angle EDB` (:just:`[III.21] <III.21>`), while :math:`\angle EAC = \angle BAD = \angle EBD` (subtending equal arcs :math:`DC` and :math:`BD`); thus :math:`\\triangle AEC \sim \\triangle DEB` (:just:`[VI.4] <VI.4>`), giving :math:`BD : DE = AC : CE`. Substituting :math:`(BA + AC) : CB = AC : CE` yields :math:`(BA + AC) : CB = BD : DE`, whence :math:`(BA + AC) \cdot ED = CB \cdot BD` (:just:`[VI.16] <VI.16>`). Because both :math:`CB` and :math:`BD` are given in magnitude, the rectangle :math:`CB \cdot BD` is given in magnitude, and therefore :math:`(BA + AC) \cdot ED` is given in magnitude.
