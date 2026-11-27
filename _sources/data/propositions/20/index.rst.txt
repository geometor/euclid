:order: 20
:canonical_id: D.20
:breadcrumb_title: D.20
:book: Data
:proposition: 20
:type: proposition
:title: Proposition 20 [κ΄ · Prop. Prop. XXIII]
:folio: Menge 34
:page: 34
:excerpt: If there be two given magnitudes, and from them be subtracted magnitudes having a given ratio to one another, either the remainders will have a given ratio to one another, or one is greater than the other by a given magnitude than in ratio.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.20:

Proposition 20 [κ΄ · Prop. XXIII]
---------------------------------

.. enunciation::

   If there be two given magnitudes, and from them be subtracted magnitudes having a given ratio to one another, either the remainders will have a given ratio to one another, or one is greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A-x : C-y) | GreaterThanInRatio)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`

Let there be two given magnitudes :math:`AB` and :math:`CD`, and from them let magnitudes :math:`AE` and :math:`CF`, having a given ratio :math:`AE : CF` to one another, be subtracted. I say that the remainders :math:`EB` and :math:`FD` either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

Since :math:`AB` is given and the ratio :math:`AE : CF` is given, make :math:`AB : CG = AE : CF` (:just:`[Data Def. 2] <D.def.2>`). Because :math:`AB` is given and :math:`AB : CG` is given, :math:`CG` is given (:just:`[Data 2] <D.2>`). Now :math:`CD` is also given, so :math:`CG` is either equal to :math:`CD` or unequal to it. If :math:`CG = CD`, then since whole :math:`AB` is to whole :math:`CD` as subtracted :math:`AE` is to subtracted :math:`CF`, the remainder :math:`EB` is to the remainder :math:`FD` as :math:`AB` is to :math:`CD` (:just:`[V.19] <V.19>`), which is a given ratio (:just:`[Data 1] <D.1>`). If :math:`CG \neq CD`, suppose :math:`CG > CD` (or :math:`CD > CG`): when :math:`CD > CG`, the difference :math:`GD = CD - CG` is given (:just:`[Data 4] <D.4>`), while :math:`EB : FG = AB : CG` is given (:just:`[V.19] <V.19>`), so :math:`FD = FG + GD` is greater by the given magnitude :math:`GD` than in ratio to :math:`EB` (:just:`[Data Def. 11] <D.def.11>`); symmetrically, if :math:`CG > CD`, making :math:`AH : CD = AE : CF` gives :math:`HB` given and :math:`EB = EH + HB` greater by :math:`HB` than in ratio to :math:`FD`.
