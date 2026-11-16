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

Let two parallelograms $AB$ (about angle $\angle CDB$) and $EF$ (about angle $\angle GHF$) have their sides in given ratios—namely $BD : FH$ given and $CD : GH$ given—either when they are equiangular ($\angle CDB = \angle GHF$), or when $\angle CDB$ and $\angle GHF$ are unequal given angles. I say that the area ratio $AB : EF$ is given.

First, let $AB$ and $EF$ be equiangular ($\angle CDB = \angle GHF$). Take the fourth proportional $K$ so that $BD : FH = K : CD$ (:just:`[VI.12] <VI.12>`), and on $FH$ and $FK = K$ complete the parallelogram $FHLK$ equiangular with $EF$ (:just:`[I.31] <I.31>`). Because $BD : FH = FK : CD$ around equal angles, $AB$ and $FHLK$ have reciprocally proportional sides and are therefore equal: $AB = FHLK$ (:just:`[VI.14] <VI.14>`). Since $FK : CD$ ($= BD : FH$) is given and $CD : GH$ is given, the ratio $FK : GH$ is given (:just:`[Data 8] <D.8>`). Yet on the common base $FH$, $FHLK : EF = FK : GH$ (:just:`[VI.1] <VI.1>`), so $AB : EF$ is given.

Second, let $\angle CDB$ and $\angle GHF$ be unequal given angles. Shear $AB$ between the same parallels $AC \parallel BD$ into the parallelogram $BDMN$ having $\angle BDM = \angle GHF$ (:just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`). As in :just:`[Data 69] <D.69>`, $\\triangle CDM$ has given angles and is given in species (:just:`[Data 40] <D.40>`), so $DM : CD$ is given; combining with given $CD : GH$ yields $DM : GH$ given (:just:`[Data 8] <D.8>`). Since $BDMN$ and $EF$ are equiangular with $BD : FH$ and $DM : GH$ given, the first case gives $BDMN : EF$ given; and since $AB = BDMN$ (:just:`[I.35] <I.35>`), $AB : EF$ is given.
