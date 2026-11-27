:order: 70
:canonical_id: D.70
:breadcrumb_title: D.70
:book: Data
:proposition: 70
:type: proposition
:title: Proposition 70 [ο΄ · Prop. Props. LXVII–LXVIII]
:folio: Menge 130
:page: 130
:excerpt: If of two parallelograms about equal angles, or about unequal yet given angles, the sides have given ratios to one another, the parallelograms themselves will also have a given ratio to one another.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.70:

Proposition 70 [ο΄ · Props. LXVII–LXVIII]
-----------------------------------------

.. folio:: Menge 130
   :page: 130

.. enunciation::

   If of two parallelograms about equal angles, or about unequal yet given angles, the sides have given ratios to one another, the parallelograms themselves will also have a given ratio to one another.

*Functional Signature*: ``Given(Angle(P1), Angle(P2), Ratio(s1 : t1), Ratio(s2 : t2)) -> Determined(Ratio(P1 : P2))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`, :just:`[VI.23] <VI.23>`

Let two parallelograms :math:`AB` (about angle :math:`\angle CDB`) and :math:`EF` (about angle :math:`\angle GHF`) have their sides in given ratios—namely :math:`BD : FH` given and :math:`CD : GH` given—either when they are equiangular (:math:`\angle CDB = \angle GHF`), or when :math:`\angle CDB` and :math:`\angle GHF` are unequal given angles. I say that the area ratio :math:`AB : EF` is given.

First, let :math:`AB` and :math:`EF` be equiangular (:math:`\angle CDB = \angle GHF`). Take the fourth proportional :math:`K` so that :math:`BD : FH = K : CD` (:just:`[VI.12] <VI.12>`), and on :math:`FH` and :math:`FK = K` complete the parallelogram :math:`FHLK` equiangular with :math:`EF` (:just:`[I.31] <I.31>`). Because :math:`BD : FH = FK : CD` around equal angles, :math:`AB` and :math:`FHLK` have reciprocally proportional sides and are therefore equal: :math:`AB = FHLK` (:just:`[VI.14] <VI.14>`). Since :math:`FK : CD` (:math:`= BD : FH`) is given and :math:`CD : GH` is given, the ratio :math:`FK : GH` is given (:just:`[Data 8] <D.8>`). Yet on the common base :math:`FH`, :math:`FHLK : EF = FK : GH` (:just:`[VI.1] <VI.1>`), so :math:`AB : EF` is given.

Second, let :math:`\angle CDB` and :math:`\angle GHF` be unequal given angles. Shear :math:`AB` between the same parallels :math:`AC \parallel BD` into the parallelogram :math:`BDMN` having :math:`\angle BDM = \angle GHF` (:just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`). As in :just:`[Data 69] <D.69>`, :math:`\\triangle CDM` has given angles and is given in species (:just:`[Data 40] <D.40>`), so :math:`DM : CD` is given; combining with given :math:`CD : GH` yields :math:`DM : GH` given (:just:`[Data 8] <D.8>`). Since :math:`BDMN` and :math:`EF` are equiangular with :math:`BD : FH` and :math:`DM : GH` given, the first case gives :math:`BDMN : EF` given; and since :math:`AB = BDMN` (:just:`[I.35] <I.35>`), :math:`AB : EF` is given.
