:order: 74
:canonical_id: D.74
:breadcrumb_title: D.74
:book: Data
:proposition: 74
:type: proposition
:title: Proposition 74 [οδ΄ · Prop. Prop. LXIV (pt. 1; cf. LXIII)]
:folio: Menge 142
:page: 142
:excerpt: If two parallelograms have a given ratio, either in equal angles or in unequal yet given angles, as a side of the first is to a side of the second, so will the other side of the second be to that straight line to which the remaining side of the first has a given ratio.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.74:

Proposition 74 [οδ΄ · Prop. LXIV (pt. 1; cf. LXIII)]
----------------------------------------------------

.. folio:: Menge 142
   :page: 142

.. enunciation::

   If two parallelograms have a given ratio, either in equal angles or in unequal yet given angles, as a side of the first is to a side of the second, so will the other side of the second be to that straight line to which the remaining side of the first has a given ratio.

*Functional Signature*: ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2)) -> Determined(CB : FG = EF : K with GivenRatio(AC : K))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`

Let two parallelograms :math:`ABCD` and :math:`EFGH` have a given area ratio :math:`ABCD : EFGH`, either in equal angles (:math:`\angle B = \angle F`) or in unequal given angles (:math:`\angle B, \angle F`). I say that as :math:`BC` is to :math:`FG`, so is :math:`FE` to a straight line to which :math:`BA` has a given ratio.

First, if :math:`\angle B = \angle F`, the proposition coincides directly with :just:`[Data 56] <D.56>`: setting :math:`BA : BL = ABCD : EFGH` and completing :math:`BLMC` yields :math:`BLMC = EFGH` (:just:`[VI.1] <VI.1>`, :just:`[V.9] <V.9>`), whence :math:`BC : FG = FE : BL` (:just:`[VI.14] <VI.14>`) with :math:`BA : BL` given.

Second, let :math:`\angle B` and :math:`\angle F` be unequal given angles. Shear :math:`ABCD` on base :math:`BC` into :math:`PBCQ` with :math:`\angle PBQ = \angle F` (:just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`). Then :math:`PBCQ = ABCD`, so :math:`PBCQ : EFGH` is given, while :math:`\\triangle ABP` is given in species (:just:`[Data 40] <D.40>`), so :math:`BA : BP` is given. By the first case applied to equiangular :math:`PBCQ` and :math:`EFGH`, :math:`BC : FG = FE : L` where :math:`BP : L` is given; combining :math:`BA : BP` with :math:`BP : L` yields :math:`BA : L` given (:just:`[Data 8] <D.8>`).
