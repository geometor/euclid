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

Let two parallelograms $ABCD$ and $EFGH$ have a given area ratio $ABCD : EFGH$, either in equal angles ($\angle B = \angle F$) or in unequal given angles ($\angle B, \angle F$). I say that as $BC$ is to $FG$, so is $FE$ to a straight line to which $BA$ has a given ratio.

First, if $\angle B = \angle F$, the proposition coincides directly with :just:`[Data 56] <D.56>`: setting $BA : BL = ABCD : EFGH$ and completing $BLMC$ yields $BLMC = EFGH$ (:just:`[VI.1] <VI.1>`, :just:`[V.9] <V.9>`), whence $BC : FG = FE : BL$ (:just:`[VI.14] <VI.14>`) with $BA : BL$ given.

Second, let $\angle B$ and $\angle F$ be unequal given angles. Shear $ABCD$ on base $BC$ into $PBCQ$ with $\angle PBQ = \angle F$ (:just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`). Then $PBCQ = ABCD$, so $PBCQ : EFGH$ is given, while $\\triangle ABP$ is given in species (:just:`[Data 40] <D.40>`), so $BA : BP$ is given. By the first case applied to equiangular $PBCQ$ and $EFGH$, $BC : FG = FE : L$ where $BP : L$ is given; combining $BA : BP$ with $BP : L$ yields $BA : L$ given (:just:`[Data 8] <D.8>`).
