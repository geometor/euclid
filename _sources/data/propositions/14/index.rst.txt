:order: 14
:canonical_id: D.14
:breadcrumb_title: D.14
:book: Data
:proposition: 14
:type: proposition
:title: Proposition 14 [ιδ΄ · Prop. Prop. XVIII]
:folio: Menge 26
:page: 26
:excerpt: If two magnitudes have a given ratio to one another, and a given magnitude be added to each of them, either the wholes will still have a given ratio to one another, or one will be greater than the other by a given magnitude than in ratio.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.14:

Proposition 14 [ιδ΄ · Prop. XVIII]
----------------------------------

.. folio:: Menge 26
   :page: 26

.. enunciation::

   If two magnitudes have a given ratio to one another, and a given magnitude be added to each of them, either the wholes will still have a given ratio to one another, or one will be greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A+d1 : C+d2) | GreaterThanInRatio)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.12] <V.12>`, :just:`[V.18] <V.18>`

Let two magnitudes $AB$ and $CD$ have a given ratio to one another. First, let the given magnitudes $BE$ and $DF$ be added to them respectively. I say that the wholes $AE$ and $CF$ either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

Since each of $BE$ and $DF$ is given, make $BG : DF = AB : CD$ (:just:`[Data Def. 2] <D.def.2>`). Because $AB : CD$ is given and $DF$ is given, $BG$ is given (:just:`[Data 2] <D.2>`). Now $BG$ is either equal to $BE$ or unequal to it. If $BG = BE$, then since $AB : CD = BG : DF$, *componendo* the whole $AE = AB + BE$ is to the whole $CF = CD + DF$ as $AB$ is to $CD$ (:just:`[V.12] <V.12>`), so the ratio $AE : CF$ is given. If $BG \neq BE$, suppose $BE > BG$: since both $BE$ and $BG$ are given, the excess $GE$ is given (:just:`[Data 4] <D.4>`). Because $AB : CD = BG : DF$, the compound $AG : CF = AB : CD$ (:just:`[V.12] <V.12>`) is given, and $AE = AG + GE$ exceeds $AG$ by the given magnitude $GE$; therefore $AE$ is greater by a given magnitude than in ratio to $CF$ (:just:`[Data Def. 11] <D.def.11>`).

Second, let the given magnitudes $EB$ and $FD$ be subtracted from $AB$ and $CD$ respectively. Again make $GB : FD = AB : CD$, so $GB$ is given (:just:`[Data 2] <D.2>`). If $GB = EB$, then by :just:`[V.19] <V.19>` the remainders $AE$ and $CF$ have the given ratio $AB : CD$. If $GB > EB$, the difference $GE$ is given (:just:`[Data 4] <D.4>`), $AG : CF = AB : CD$ is given (:just:`[V.19] <V.19>`), and $AE = AG + GE$ is greater by the given magnitude $GE$ than in ratio to $CF$ (:just:`[Data Def. 11] <D.def.11>`).
