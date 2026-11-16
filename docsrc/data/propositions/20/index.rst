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

Let there be two given magnitudes $AB$ and $CD$, and from them let magnitudes $AE$ and $CF$, having a given ratio $AE : CF$ to one another, be subtracted. I say that the remainders $EB$ and $FD$ either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

Since $AB$ is given and the ratio $AE : CF$ is given, make $AB : CG = AE : CF$ (:just:`[Data Def. 2] <D.def.2>`). Because $AB$ is given and $AB : CG$ is given, $CG$ is given (:just:`[Data 2] <D.2>`). Now $CD$ is also given, so $CG$ is either equal to $CD$ or unequal to it. If $CG = CD$, then since whole $AB$ is to whole $CD$ as subtracted $AE$ is to subtracted $CF$, the remainder $EB$ is to the remainder $FD$ as $AB$ is to $CD$ (:just:`[V.19] <V.19>`), which is a given ratio (:just:`[Data 1] <D.1>`). If $CG \neq CD$, suppose $CG > CD$ (or $CD > CG$): when $CD > CG$, the difference $GD = CD - CG$ is given (:just:`[Data 4] <D.4>`), while $EB : FG = AB : CG$ is given (:just:`[V.19] <V.19>`), so $FD = FG + GD$ is greater by the given magnitude $GD$ than in ratio to $EB$ (:just:`[Data Def. 11] <D.def.11>`); symmetrically, if $CG > CD$, making $AH : CD = AE : CF$ gives $HB$ given and $EB = EH + HB$ greater by $HB$ than in ratio to $FD$.
