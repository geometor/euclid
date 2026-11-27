:order: 73
:canonical_id: D.73
:breadcrumb_title: D.73
:book: Data
:proposition: 73
:type: proposition
:title: Proposition 73 [ογ΄ · Prop. Prop. LXIV (pt. 2)]
:folio: Menge 138
:page: 138
:excerpt: If of two parallelograms about equal angles, or about unequal yet given angles, the sides stand so that as a side of the first is to a side of the second, so is the remaining side of the second to some other straight line, and the remaining side of the first have a given ratio to that straight line, the parallelograms themselves will also have a given ratio to one another.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.73:

Proposition 73 [ογ΄ · Prop. LXIV (pt. 2)]
-----------------------------------------

.. folio:: Menge 138
   :page: 138

.. enunciation::

   If of two parallelograms about equal angles, or about unequal yet given angles, the sides stand so that as a side of the first is to a side of the second, so is the remaining side of the second to some other straight line, and the remaining side of the first have a given ratio to that straight line, the parallelograms themselves will also have a given ratio to one another.

*Functional Signature*: ``Given(Angle(P1), Angle(P2), CB:FG = EF:CK, Ratio(AC:CK)) -> Determined(Ratio(P1 : P2))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[Data 70] <D.70>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`

Let two parallelograms :math:`ABCD` and :math:`EFGH` be either equiangular (:math:`\angle B = \angle F`) or in unequal given angles (:math:`\angle B, \angle F`), and as :math:`BC` is to :math:`FG`, so let :math:`FE` be to a straight line :math:`K` to which :math:`BA` has a given ratio :math:`BA : K`. I say that the area ratio :math:`ABCD : EFGH` is given.

First, let :math:`ABCD` and :math:`EFGH` be equiangular. Along :math:`BA` (produced if necessary) cut off :math:`BL = K` (:just:`[I.3] <I.3>`), so :math:`BA : BL` is given, and complete the equiangular parallelogram :math:`BLMC` on :math:`BL` and :math:`BC` (:just:`[I.31] <I.31>`). Because :math:`BC : FG = FE : BL` around equal angles :math:`\angle B = \angle F`, the parallelograms :math:`BLMC` and :math:`EFGH` have reciprocally proportional sides and are therefore equal: :math:`BLMC = EFGH` (:just:`[VI.14] <VI.14>`). Moreover, on the common base :math:`BC`, :math:`ABCD : BLMC = BA : BL` (:just:`[VI.1] <VI.1>`), which is given! Substituting :math:`BLMC = EFGH` proves that :math:`ABCD : EFGH` is given.

Second, let :math:`\angle B` and :math:`\angle F` be unequal given angles. Shear :math:`ABCD` on base :math:`BC` between the same parallels into parallelogram :math:`PBCQ` having :math:`\angle PBQ = \angle F` (:just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`). As in :just:`[Data 69] <D.69>`, :math:`\\triangle ABP` is given in species (:just:`[Data 40] <D.40>`), so :math:`BP : BA` is given; combining with given :math:`BA : K` gives :math:`BP : K` given (:just:`[Data 8] <D.8>`). Applying the first case to equiangular :math:`PBCQ` and :math:`EFGH` gives :math:`PBCQ : EFGH` given; since :math:`ABCD = PBCQ` (:just:`[I.35] <I.35>`), :math:`ABCD : EFGH` is given.
