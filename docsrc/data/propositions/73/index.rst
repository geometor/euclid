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

Let two parallelograms $ABCD$ and $EFGH$ be either equiangular ($\angle B = \angle F$) or in unequal given angles ($\angle B, \angle F$), and as $BC$ is to $FG$, so let $FE$ be to a straight line $K$ to which $BA$ has a given ratio $BA : K$. I say that the area ratio $ABCD : EFGH$ is given.

First, let $ABCD$ and $EFGH$ be equiangular. Along $BA$ (produced if necessary) cut off $BL = K$ (:just:`[I.3] <I.3>`), so $BA : BL$ is given, and complete the equiangular parallelogram $BLMC$ on $BL$ and $BC$ (:just:`[I.31] <I.31>`). Because $BC : FG = FE : BL$ around equal angles $\angle B = \angle F$, the parallelograms $BLMC$ and $EFGH$ have reciprocally proportional sides and are therefore equal: $BLMC = EFGH$ (:just:`[VI.14] <VI.14>`). Moreover, on the common base $BC$, $ABCD : BLMC = BA : BL$ (:just:`[VI.1] <VI.1>`), which is given! Substituting $BLMC = EFGH$ proves that $ABCD : EFGH$ is given.

Second, let $\angle B$ and $\angle F$ be unequal given angles. Shear $ABCD$ on base $BC$ between the same parallels into parallelogram $PBCQ$ having $\angle PBQ = \angle F$ (:just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`). As in :just:`[Data 69] <D.69>`, $\\triangle ABP$ is given in species (:just:`[Data 40] <D.40>`), so $BP : BA$ is given; combining with given $BA : K$ gives $BP : K$ given (:just:`[Data 8] <D.8>`). Applying the first case to equiangular $PBCQ$ and $EFGH$ gives $PBCQ : EFGH$ given; since $ABCD = PBCQ$ (:just:`[I.35] <I.35>`), $ABCD : EFGH$ is given.
