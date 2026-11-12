:order: 10
:type: chapter
:canonical_id: D.unit.1
:folio: Menge pp. 4–42
:book: Propositions 1–24: Magnitudes & Ratios
:description: Deductive closure of given magnitudes and ratios over Elements Book V: addition, subtraction, inversion, composition, division, ex aequali chains, affine-linear offset relations (δοθέντι μεῖζον ἢ ἐν λόγῳ), non-singular linear combinations (D.22–D.23), and geometric mean proportions (D.24).

.. _data-unit-1-en:

===============================================
Unit 1: Magnitudes & Ratios (Propositions 1–24)
===============================================

*Pure Algebraic Closure of Given Magnitudes, Ratios, and Affine-Ratio Equations* — **D.1–D.24 (Simson I–XXVII) · Menge (1896) pp. 4–42**

.. note::

   **Edition Track (English)**: Deductive closure of given magnitudes and ratios over Elements Book V: addition, subtraction, inversion, composition, division, ex aequali chains, affine-linear offset relations (δοθέντι μεῖζον ἢ ἐν λόγῳ), non-singular linear combinations (D.22–D.23), and geometric mean proportions (D.24). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. _D.1:

Proposition 1 [α΄ · Prop. I]
----------------------------

.. folio:: Menge 4
   :page: 4

.. enunciation::

   The ratio of given magnitudes to one another is given.

*Functional Signature*: ``Given(Mag(A), Mag(B)) -> Determined(Ratio(A : B))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[V.7] <V.7>`, :just:`[V.16] <V.16>`

Let $A$ and $B$ be given magnitudes. I say that the ratio of $A$ to $B$ is given.

Since $A$ is given, it is possible to procure a magnitude equal to it (:just:`[Data Def. 1] <D.def.1>`); let it be procured and let it be $C$. Again, since $B$ is given, let $D$ be procured equal to $B$ (:just:`[Data Def. 1] <D.def.1>`). Because $A = C$ and $B = D$, as $A$ is to $C$, so is $B$ to $D$ (:just:`[V.7] <V.7>`); and *alternando*, as $A$ is to $B$, so is $C$ to $D$ (:just:`[V.16] <V.16>`). Therefore the ratio of $A$ to $B$ is given, for the same ratio $C : D$ has been procured for it (:just:`[Data Def. 2] <D.def.2>`).

.. _D.2:

Proposition 2 [β΄ · Prop. II]
-----------------------------

.. enunciation::

   If a given magnitude have a given ratio to some other magnitude, that other is also given in magnitude.

*Functional Signature*: ``Given(Mag(A), Ratio(A : B)) -> Determined(Mag(B)) [Simson fourth-proportional diorismos]`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[V.11] <V.11>`, :just:`[V.9] <V.9>`, :just:`[VI.12] <VI.12>`

Let the given magnitude $A$ have a given ratio to $B$. I say that $B$ is also given in magnitude.

Since $A$ is given, let a magnitude $C$ be procured equal to it (:just:`[Data Def. 1] <D.def.1>`). And since the ratio of $A$ to $B$ is given—for so it was assumed—let the ratio of $C$ to $D$ be made the same with it (:just:`[Data Def. 2] <D.def.2>`). Then as $A$ is to $B$, so is $C$ to $D$ (:just:`[V.11] <V.11>`); and *alternando*, as $A$ is to $C$, so is $B$ to $D$ (:just:`[V.16] <V.16>`). Yet $A = C$; therefore $B = D$ (:just:`[V.14] <V.14>`). Hence the magnitude $B$ is given, for $D$ has been procured equal to it (:just:`[Data Def. 1] <D.def.1>`).

.. _D.3:

Proposition 3 [γ΄ · Prop. III]
------------------------------

.. enunciation::

   If any multitude of given magnitudes be compounded together, the magnitude compounded out of them will also be given.

*Functional Signature*: ``Given(Mag(AB), Mag(BC)) -> Determined(Mag(AB + BC))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 2] <I.cn.2>`

Let any multitude of given magnitudes $AB$ and $BC$ be compounded. I say that the whole $AC$ compounded out of them is given.

Since $AB$ is given, it is possible to procure a magnitude equal to it (:just:`[Data Def. 1] <D.def.1>`); let it be procured and be $DE$. Again, since $BC$ is given, let $EF$ be procured equal to $BC$ (:just:`[Data Def. 1] <D.def.1>`). Because $AB = DE$ and $BC = EF$, the whole $AC$ is equal to the whole $DF$ (:just:`[C.N. 2] <I.cn.2>`). Therefore $AC$ is given, since $DF$ has been procured equal to it (:just:`[Data Def. 1] <D.def.1>`).

.. _D.4:

Proposition 4 [δ΄ · Prop. IV]
-----------------------------

.. enunciation::

   If from a given magnitude a given magnitude be subtracted, the remainder will also be given.

*Functional Signature*: ``Given(Mag(AB), Mag(AC)) -> Determined(Mag(AB - AC))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 3] <I.cn.3>`

From the given magnitude $AB$ let the given magnitude $AG$ be subtracted. I say that the remainder $GB$ is given.

Since $AB$ is given, let $DF$ be procured equal to it (:just:`[Data Def. 1] <D.def.1>`); and since $AG$ is given, let $DE$ be cut off equal to $AG$ (:just:`[Data Def. 1] <D.def.1>`). Because the whole $AB = DF$, of which the subtracted parts $AG$ and $DE$ are equal, the remainder $GB$ is equal to the remainder $EF$ (:just:`[C.N. 3] <I.cn.3>`). Therefore $GB$ is given, since $EF$ has been procured equal to it (:just:`[Data Def. 1] <D.def.1>`).

.. _D.5:

Proposition 5 [ε΄ · Prop. VI]
-----------------------------

.. folio:: Menge 10
   :page: 10

.. enunciation::

   If a magnitude have a given ratio to a part of itself, it will also have a given ratio to the remainder.

*Functional Signature*: ``Given(Ratio(AB : AC)) -> Determined(Ratio(AB : (AB - AC)))`` · *Dependencies*: :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[V.19] <V.19>`

Let the magnitude $AB$ have a given ratio to its part $AG$. I say that $AB$ also has a given ratio to the remaining part $GB$.

Let $DF$ be set out as a given magnitude; since the ratio $BA : AG$ is given, let the ratio $FD : DE$ be made the same with it (:just:`[Data Def. 2] <D.def.2>`). Then $FD : DE$ is given, and $FD$ is given, so $DE$ is given (:just:`[Data 2] <D.2>`), whence the remainder $EF$ is given (:just:`[Data 4] <D.4>`). Since $FD$ is also given, the ratio $DF : FE$ is given (:just:`[Data 1] <D.1>`). Moreover, since $AB : AG = DF : DE$, *convertendo* as $AB$ is to $BG$, so is $DF$ to $FE$ (:just:`[V.19] <V.19>` Cor.). Because $DF : FE$ is given, the ratio $AB : BG$ is also given (:just:`[Data Def. 2] <D.def.2>`).

.. _D.6:

Proposition 6 [Ϛ΄ · Prop. VII]
------------------------------

.. enunciation::

   If two magnitudes having a given ratio to one another be compounded together, the whole magnitude will also have a given ratio to each of them.

*Functional Signature*: ``Given(Ratio(AB : BC)) -> Determined(Ratio((AB+BC) : AB), Ratio((AB+BC) : BC))`` · *Dependencies*: :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`

Let the two magnitudes $AB$ and $BC$, having a given ratio to one another, be compounded into $AC$. I say that the whole $AC$ has a given ratio to each of $AB$ and $BC$.

Let a given magnitude $DE$ be set out; since the ratio $AB : BC$ is given, let the same ratio $DE : EF$ be procured (:just:`[Data Def. 2] <D.def.2>`). Because $DE$ is given and $DE : EF$ is given, $EF$ is given (:just:`[Data 2] <D.2>`), so the whole $DF$ is given (:just:`[Data 3] <D.3>`). Since each of $DE$ and $EF$ is given, the ratios $DF : DE$ and $DF : EF$ are both given (:just:`[Data 1] <D.1>`). Now since $AB : BC = DE : EF$, *componendo* $AC : BC = DF : EF$ (:just:`[V.18] <V.18>`), and by inversion and *componendo* $AC : AB = DF : DE$. Since $DF$ has a given ratio to each of $DE$ and $EF$, $AC$ likewise has a given ratio to each of $AB$ and $BC$ (:just:`[Data Def. 2] <D.def.2>`).

.. _D.7:

Proposition 7 [ζ΄ · Prop. VIII]
-------------------------------

.. folio:: Menge 12
   :page: 12

.. enunciation::

   If a given magnitude be divided in a given ratio, each of the segments is given.

*Functional Signature*: ``Given(Mag(AB), Ratio(AC : CB)) -> Determined(Mag(AC), Mag(CB))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[VI.10] <VI.10>`

Let the given magnitude $AC$ be divided into $AB$ and $BC$ in a given ratio $AB : BC$. I say that each of $AB$ and $BC$ is given.

Since the ratio $AB : BC$ is given, the whole $AC$ has a given ratio to each of $AB$ and $BC$ (:just:`[Data 6] <D.6>`). Yet $AC$ is given in magnitude; therefore each of $AB$ and $BC$ is given in magnitude (:just:`[Data 2] <D.2>`).

.. _D.8:

Proposition 8 [η΄ · Prop. IX]
-----------------------------

.. folio:: Menge 14
   :page: 14

.. enunciation::

   Magnitudes that have given ratios to the same magnitude will also have a given ratio to one another.

*Functional Signature*: ``Given(Ratio(A : B), Ratio(C : B)) -> Determined(Ratio(A : C))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[V.7] <V.7>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`

Let $A$ have a given ratio to $B$, and let $C$ have a given ratio to the same $B$. I say that $A$ also has a given ratio to $C$.

Let a given magnitude $D$ be set out. Since the ratio $A : B$ is given, let $D : E$ be made the same with it (:just:`[Data Def. 2] <D.def.2>`); because $D$ is given, $E$ is also given (:just:`[Data 2] <D.2>`). Again, since the ratio $C : B$ is given, let $F : E$ be made the same with $C : B$, so that *invertendo* $B : C = E : F$ (:just:`[V.7] <V.7>` Cor.); because $E$ is given, $F$ is also given (:just:`[Data 2] <D.2>`). Since both $D$ and $F$ are given, the ratio $D : F$ is given (:just:`[Data 1] <D.1>`). And since $A : B = D : E$ while $B : C = E : F$, *ex aequali* $A : C = D : F$ (:just:`[V.22] <V.22>`). Therefore the ratio $A : C$ is given (:just:`[Data Def. 2] <D.def.2>`).

.. _D.9:

Proposition 9 [θ΄ · Prop. X]
----------------------------

.. enunciation::

   If two or more magnitudes have given ratios to one another, and the same magnitudes have given ratios—even if not the same—to certain other magnitudes, those other magnitudes will also have given ratios to one another.

*Functional Signature*: ``Given(Ratios(A:B:C), Ratio(A:D), Ratio(B:E), Ratio(C:F)) -> Determined(Ratios(D:E:F))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`

Let two or more magnitudes $A, B, C$ have given ratios to one another, and let those same magnitudes have given ratios (even if not the same ones) to other magnitudes $D, E, F$ respectively. I say that $D, E, F$ also have given ratios to one another.

Since the ratio $A : B$ is given and the ratio $A : D$ is given, the ratio $D : B$ is given (:just:`[Data 8] <D.8>`). Again, since the ratio $B : E$ is given, the ratio $D : E$ is given (:just:`[Data 8] <D.8>`). For the very same reason, since $B : C$ is given together with $B : E$ and $C : F$, the ratio $E : F$ is given (:just:`[Data 8] <D.8>`), whence $D : F$ is also given (:just:`[Data 8] <D.8>`). Therefore $D, E, F$ have given ratios to one another.

.. _D.10:

Proposition 10 [ι΄ · Prop. XVI]
-------------------------------

.. folio:: Menge 16
   :page: 16

.. enunciation::

   If a magnitude be greater than a magnitude by a given magnitude than in ratio, the compounded magnitude will also be greater than the same by a given magnitude than in ratio; and if the compounded magnitude be greater than the same by a given magnitude than in ratio, either the remainder is also greater than the same by a given magnitude than in ratio, or the remainder together with the following magnitude to which the other has a given ratio is given.

*Functional Signature*: ``Given((AB - D) : BC = k) <-> Determined(((AB+BC) - D) : BC = k+1 | (AB + BE = D where BC:BE given))`` · *Dependencies*: :just:`[Data Def. 9] <D.def.9>`, :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 5] <D.5>`, :just:`[Data 6] <D.6>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`

First, let the magnitude $AB$ be :term:`greater by a given magnitude than in ratio <dothenti-meizon-e-en-logo>` to $BC$. I say that the compound $AC$ is also greater by a given magnitude than in ratio to the same $BC$.

From $AB$ let the given magnitude $AD$ be subtracted (:just:`[Data Def. 11] <D.def.11>`); then the ratio of the remainder $DB$ to $BC$ is given. *Componendo*, the ratio $DC : BC$ is given (:just:`[Data 6] <D.6>`, :just:`[V.18] <V.18>`). And since $AD$ is given, the whole $CA$ is greater than $DC$ by the given magnitude $AD$, and hence $AC$ is greater by a given magnitude than in ratio to $BC$ (:just:`[Data Def. 11] <D.def.11>`).

Conversely, let the compound $AC$ be greater by a given magnitude than in ratio to $BC$. I say that the remaining part $AB$ is either greater by a given magnitude than in ratio to $BC$, or else $AB$ together with a magnitude to which $BC$ has a given ratio is given.

Subtract the given excess from $AC$ (:just:`[Data Def. 11] <D.def.11>`). This given magnitude is either less than $AB$ or greater than $AB$ (if equal to $AB$, then $BC$ itself is in a given ratio to $BC$, a boundary case). First let it be less than $AB$, and let it be $AD$: then $DC : CB$ is given, so *separando* $DB : BC$ is given (:just:`[Data 5] <D.5>`, :just:`[V.17] <V.17>`); and $AD$ is given, so $AB$ is greater by a given magnitude than in ratio to $BC$ (:just:`[Data Def. 11] <D.def.11>`). Next let the given magnitude be greater than $AB$, and let $AE$ be set equal to it (with $E$ falling between $B$ and $C$): then the remainder $EC$ has a given ratio to $CB$, so *invertendo* $BC : EC$ is given, and *convertendo* $BC : BE$ is given (:just:`[Data 5] <D.5>`). Yet $AE = AB + BE$ is given; therefore $AB$ together with $BE$—to which $BC$ has a given ratio—is given.

.. _D.11:

Proposition 11 [ια΄ · Prop. XVII]
---------------------------------

.. folio:: Menge 20
   :page: 20

.. enunciation::

   If a magnitude be greater than a magnitude by a given magnitude than in ratio, the same will also be greater than the compounded magnitude by a given magnitude than in ratio; and if the same be greater than the compounded magnitude by a given magnitude than in ratio, the same will also be greater than the remainder by a given magnitude than in ratio.

*Functional Signature*: ``Given((AB - D) : BC = k) <-> Determined((AB - k/(k+1)*D) : (AB + BC) = k/(k+1))`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 6] <D.6>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`

First, let the magnitude $AB$ be greater by a given magnitude than in ratio to $BC$. I say that $AB$ is also greater by a given magnitude than in ratio to the compound $AC$.

Subtract the given magnitude $AD$ from $AB$ (:just:`[Data Def. 11] <D.def.11>`); then the ratio $DB : BC$ is given. *Invertendo* and *componendo*, the ratio $DC : DB$ is given (:just:`[Data 6] <D.6>`), so *invertendo* $DB : DC$ is given. Let the ratio $AD : DE$ be made the same with $DB : DC$ (:just:`[Data Def. 2] <D.def.2>`); since $DB : DC$ is given and $AD$ is given, $DE$ is given (:just:`[Data 2] <D.2>`), whence the whole $AE = AD + DE$ is given (:just:`[Data 3] <D.3>`). Moreover, since $AD : DE = DB : DC$, it follows by proportion manipulation (:just:`[V.12] <V.12>`, :just:`[V.19] <V.19>`) that the remainder $EB$ is to the compound $AC$ as $DB$ is to $DC$. Thus the ratio $EB : AC$ is given while $AE$ is given; therefore $AB$ is greater by a given magnitude than in ratio to $AC$ (:just:`[Data Def. 11] <D.def.11>`).

Conversely, let $AB$ be greater by a given magnitude than in ratio to the compound $AC$. I say that $AB$ is also greater by a given magnitude than in ratio to the remainder $BC$.

Subtract from $AB$ the given magnitude $AE$ (:just:`[Data Def. 11] <D.def.11>`), so that the ratio $EB : AC$ is given, whence *invertendo* $AC : EB$ is given. Make $AE : ED$ have the same ratio as $AC : EB$ (:just:`[Data Def. 2] <D.def.2>`). Because $AE$ is given, $ED$ is given (:just:`[Data 2] <D.2>`), and therefore the remainder $AD$ is given (:just:`[Data 4] <D.4>`). Since $AC : EB = AE : ED$, *convertendo*, *alternando*, and *separando* (:just:`[V.19] <V.19>`, :just:`[V.17] <V.17>`), the ratio $BC : DB$ (and hence $DB : BC$) is given while $AD$ is given. Therefore $AB$ is greater by a given magnitude than in ratio to $BC$ (:just:`[Data Def. 11] <D.def.11>`).

.. _D.12:

Proposition 12 [ιβ΄ · Prop. V]
------------------------------

.. folio:: Menge 22
   :page: 22

.. enunciation::

   If there be three magnitudes, and the first together with the second be given, and the second together with the third be also given, then either the first is equal to the third, or one exceeds the other by a given magnitude.

*Functional Signature*: ``Given(Mag(A + B), Mag(B + C)) -> Determined(A = C | ExceedsByGiven(A, C))`` · *Dependencies*: :just:`[Data Def. 9] <D.def.9>`, :just:`[Data 4] <D.4>`, :just:`[C.N. 3] <I.cn.3>`

Let there be three magnitudes $AB, BC, CD$, and let $AB + BC = AC$ be given, and let $BC + CD = BD$ also be given. I say that either $AB$ is equal to $CD$, or one exceeds the other by a given magnitude.

Since each of $AC$ and $BD$ is given, $AC$ and $BD$ are either equal or unequal. First, let them be equal: since $AC = BD$, subtract the common magnitude $BC$; then the remainder $AB$ is equal to the remainder $CD$ (:just:`[C.N. 3] <I.cn.3>`). Next, let them be unequal, and let $AC$ be greater than $BD$: cut off $EC = BD$ from $AC$ (:just:`[Data Def. 1] <D.def.1>`); since both $AC$ and $EC$ are given, the remainder $AE$ is given (:just:`[Data 4] <D.4>`). Subtracting the common part $BC$ from $EC = BD$ gives $EB = CD$ (:just:`[C.N. 3] <I.cn.3>`), so $AB = AE + EB$ exceeds $CD$ by the given magnitude $AE$.

.. _D.13:

Proposition 13 [ιγ΄ · Prop. XXIV]
---------------------------------

.. folio:: Menge 24
   :page: 24

.. enunciation::

   If there be three magnitudes, and the first have to the second a given ratio, while the second is greater than the third by a given magnitude than in ratio, the first will also be greater than the third by a given magnitude than in ratio.

*Functional Signature*: ``Given(Ratio(A : B) = r, (B - F) : C = k) -> Determined((A - r*F) : C = r*k)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.19] <V.19>`

Let there be three magnitudes $A, B, C$; let the ratio $A : B$ be given, and let $B$ be :term:`greater by a given magnitude than in ratio <dothenti-meizon-e-en-logo>` to $C$. I say that $A$ is also greater by a given magnitude than in ratio to $C$.

Since $B$ is greater by a given magnitude than in ratio to $C$, subtract the given magnitude $BD$ from $B$ (writing $B = BD + DC'$ or dividing $B$ into given $D$ and remainder $E$): specifically, in Menge's lettering, represent the three magnitudes as $AB, CD, E$, where $AB : CD$ is given and $CD$ is greater by a given magnitude $CF$ than in ratio to $E$ (:just:`[Data Def. 11] <D.def.11>`). Make $AG : CF = AB : CD$ (:just:`[Data Def. 2] <D.def.2>`). Since $AB : CD$ is given and $CF$ is given, $AG$ is given (:just:`[Data 2] <D.2>`). Moreover, since whole $AB$ is to whole $CD$ as subtracted $AG$ is to subtracted $CF$, the remainder $GB$ is to the remainder $FD$ as $AB$ is to $CD$ (:just:`[V.19] <V.19>`), so $GB : FD$ is given. Yet $FD : E$ is given; therefore $GB : E$ is given (:just:`[Data 8] <D.8>`). Since $AG$ is given, $AB$ is greater by the given magnitude $AG$ than in ratio to $E$ (:just:`[Data Def. 11] <D.def.11>`).

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

.. _D.15:

Proposition 15 [ιε΄ · Prop. XIX]
--------------------------------

.. enunciation::

   If two magnitudes have a given ratio to one another, and a given magnitude be subtracted from each of them, either the remainders will have a given ratio to one another, or one will be greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A-d1 : C-d2) | GreaterThanInRatio)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`

Let two magnitudes $AB$ and $CD$ have a given ratio to one another; from $AB$ let the given magnitude $AE$ be subtracted, and to $CD$ let the given magnitude $DF$ be added, forming $EB$ and $CF$. I say that the whole $CF$ is greater by a given magnitude than in ratio to the remainder $EB$.

Since $AE$ is given and the ratio $AB : CD$ is given, make $AE : CG = AB : CD$ (:just:`[Data Def. 2] <D.def.2>`). Because $AE$ is given and $AE : CG$ is given, $CG$ is given (:just:`[Data 2] <D.2>`); and since $DF$ is also given, the sum $CG + DF$ is given (:just:`[Data 3] <D.3>`). Moreover, since whole $AB$ is to whole $CD$ as subtracted $AE$ is to subtracted $CG$, the remainder $EB$ is to the remainder $GD$ as $AB$ is to $CD$ (:just:`[V.19] <V.19>`), so the ratio $GD : EB$ is given (and if $CG \ge CD$, adjoining the auxiliary proportional beyond $C$ gives the identical sum of given offsets). Since $CF = GD + (CG + DF)$ exceeds $GD$ by the given magnitude $CG + DF$, the whole $CF$ is greater by a given magnitude than in ratio to $EB$ (:just:`[Data Def. 11] <D.def.11>`).

.. _D.16:

Proposition 16 [ιϛ΄ · Prop. XX]
-------------------------------

.. folio:: Menge 30
   :page: 30

.. enunciation::

   If two magnitudes have a given ratio to one another, and from one of them a given magnitude be subtracted while to the other a given magnitude be added, the whole will be greater than the remainder by a given magnitude than in ratio.

*Functional Signature*: ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(((A+d2) - (r*d1+d2)) : (C-d1) = r)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.19] <V.19>`

Let two magnitudes $AB$ and $CD$ have a given ratio to one another; from $AB$ let the given magnitude $AE$ be subtracted, and to $CD$ let the given magnitude $DF$ be added. I say that the remainder $EB$ is :term:`less by a given magnitude than in ratio <dothenti-meizon-e-en-logo>` to the whole $CF$.

Since the ratio $AB : CD$ is given, make $GB : DF = AB : CD$, adjoining $GB$ to $AB$ at $B$ (:just:`[Data Def. 2] <D.def.2>`). Because $DF$ is given and $GB : DF$ is given, $GB$ is given (:just:`[Data 2] <D.2>`). Since $AE$ is also given, the sum $AE + GB$ is given (:just:`[Data 3] <D.3>`). Now since $AB : CD = GB : DF$, the compound $AG = AB + GB$ is to the compound $CF = CD + DF$ in the given ratio $AB : CD$ (:just:`[V.12] <V.12>`). Yet $AG = EB + (AE + GB)$ exceeds the remainder $EB$ by the given magnitude $AE + GB$. Therefore $EB$, together with the given magnitude $AE + GB$, has a given ratio to $CF$; that is, $EB$ is less by a given magnitude than in ratio to $CF$ (:just:`[Data Def. 12] <D.def.12>`).

.. _D.17:

Proposition 17 [ιζ΄ · Prop. XXV]
--------------------------------

.. folio:: Menge 32
   :page: 32

.. enunciation::

   If there be three magnitudes, and the first be greater than the second by a given magnitude than in ratio, and the third be also greater than the same second by a given magnitude than in ratio, then either the first has a given ratio to the third, or one is greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given((A - d1):B = k1, (C - d2):B = k2) -> Determined(Ratio(A:C) | GreaterThanInRatio(A, C))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 14] <D.14>`, :just:`[V.11] <V.11>`

Let there be three magnitudes $AB, CD, E$, and let each of $AB$ and $E$ be greater by a given magnitude than in ratio to $CD$ (in Menge's order: first and third each greater by a given magnitude than in ratio to the second, or first and second to the third). Specifically, let $AB$ and $CD$ each be greater by a given magnitude than in ratio to $E$. I say that $AB$ and $CD$ either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

From $AB$ subtract the given magnitude $AF$ (:just:`[Data Def. 11] <D.def.11>`), so that $FB : E$ is given; and from $CD$ subtract the given magnitude $CG$, so that $GD : E$ is given. Since both $FB$ and $GD$ have given ratios to $E$, the ratio $FB : GD$ is given (:just:`[Data 8] <D.8>`). And to the two magnitudes $FB$ and $GD$, having a given ratio to one another, the given magnitudes $AF$ and $CG$ have been added; therefore the wholes $AB$ and $CD$ either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other (:just:`[Data 14] <D.14>`).

.. _D.18:

Proposition 18 [ιη΄ · Prop. XXVI]
---------------------------------

.. enunciation::

   If there be three magnitudes, and one of them be greater than each of the remaining two by a given magnitude than in ratio, the remaining two will either have a given ratio to one another, or one is greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given((C - d1):A = k1, (C - d2):E = k2) -> Determined(Ratio(A:E) | GreaterThanInRatio(A, E))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 15] <D.15>`, :just:`[V.11] <V.11>`

Let there be three magnitudes $AB, CD, EF$, and let the middle one $CD$ be greater by a given magnitude than in ratio to each of $AB$ and $EF$. I say that $AB$ and $EF$ either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

Since $CD$ is greater by a given magnitude than in ratio to $AB$, subtract the given magnitude $CG$ from $CD$ (:just:`[Data Def. 11] <D.def.11>`), so that $GD : AB$ is given. Again, since $CD$ is greater by a given magnitude than in ratio to $EF$, subtract the given magnitude $CH$ from $CD$, so that $HD : EF$ is given. Now the two given magnitudes $CG$ and $CH$ are either equal or unequal. First let $CG = CH$: then the remainders $GD$ and $HD$ are identical, so $GD$ has a given ratio both to $AB$ and to $EF$; hence $AB : EF$ is given (:just:`[Data 8] <D.8>`). Next let $CG < CH$: then $H$ falls between $G$ and $D$, and the difference $GH$ is given (:just:`[Data 4] <D.4>`). Since $GD : AB$ is given, make $GH : AK = GD : AB$ (:just:`[Data Def. 2] <D.def.2>`); because $GH$ is given, $AK$ is given (:just:`[Data 2] <D.2>`), and the remainder $HD : KB = GD : AB$ is given (:just:`[V.19] <V.19>`). Since $HD : EF$ is also given, $KB : EF$ is given (:just:`[Data 8] <D.8>`), while $AB = AK + KB$ exceeds $KB$ by the given magnitude $AK$; therefore $AB$ is greater by a given magnitude than in ratio to $EF$ (:just:`[Data Def. 11] <D.def.11>`).

.. _D.19:

Proposition 19 [ιθ΄ · Prop. XXVII]
----------------------------------

.. folio:: Menge 34
   :page: 34

.. enunciation::

   If there be three magnitudes, and the first be greater than the second by a given magnitude than in ratio, and the second be greater than the third by a given magnitude than in ratio, the first will also be greater than the third by a given magnitude than in ratio.

*Functional Signature*: ``Given((A - d1):B = k1, (B - d2):C = k2) -> Determined((A - (d1 + k1*d2)) : C = k1*k2)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[Data 13] <D.13>`, :just:`[V.11] <V.11>`

Let there be three magnitudes $AB, CD, E$; let $AB$ be greater by a given magnitude than in ratio to $CD$, and let $CD$ be greater by a given magnitude than in ratio to $E$. I say that $AB$ is also greater by a given magnitude than in ratio to $E$.

Since $AB$ is greater by a given magnitude than in ratio to $CD$, subtract the given magnitude $AF$ from $AB$ (:just:`[Data Def. 11] <D.def.11>`), so that the remainder $FB$ has a given ratio to $CD$. Because $FB : CD$ is given and $CD$ is greater by a given magnitude than in ratio to $E$, $FB$ is also greater by a given magnitude than in ratio to $E$ (:just:`[Data 13] <D.13>`). Subtract that given magnitude $FG$ from $FB$, leaving $GB : E$ given. Since both $AF$ and $FG$ are given, the whole $AG = AF + FG$ is given (:just:`[Data 3] <D.3>`), and the remainder $GB$ has a given ratio to $E$. Therefore $AB$ is greater by the given magnitude $AG$ than in ratio to $E$ (:just:`[Data Def. 11] <D.def.11>`).

.. _D.20:

Proposition 20 [κ΄ · Prop. XXIII]
---------------------------------

.. enunciation::

   If there be two given magnitudes, and from them be subtracted magnitudes having a given ratio to one another, either the remainders will have a given ratio to one another, or one is greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A-x : C-y) | GreaterThanInRatio)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`

Let there be two given magnitudes $AB$ and $CD$, and from them let magnitudes $AE$ and $CF$, having a given ratio $AE : CF$ to one another, be subtracted. I say that the remainders $EB$ and $FD$ either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

Since $AB$ is given and the ratio $AE : CF$ is given, make $AB : CG = AE : CF$ (:just:`[Data Def. 2] <D.def.2>`). Because $AB$ is given and $AB : CG$ is given, $CG$ is given (:just:`[Data 2] <D.2>`). Now $CD$ is also given, so $CG$ is either equal to $CD$ or unequal to it. If $CG = CD$, then since whole $AB$ is to whole $CD$ as subtracted $AE$ is to subtracted $CF$, the remainder $EB$ is to the remainder $FD$ as $AB$ is to $CD$ (:just:`[V.19] <V.19>`), which is a given ratio (:just:`[Data 1] <D.1>`). If $CG \neq CD$, suppose $CG > CD$ (or $CD > CG$): when $CD > CG$, the difference $GD = CD - CG$ is given (:just:`[Data 4] <D.4>`), while $EB : FG = AB : CG$ is given (:just:`[V.19] <V.19>`), so $FD = FG + GD$ is greater by the given magnitude $GD$ than in ratio to $EB$ (:just:`[Data Def. 11] <D.def.11>`); symmetrically, if $CG > CD$, making $AH : CD = AE : CF$ gives $HB$ given and $EB = EH + HB$ greater by $HB$ than in ratio to $FD$.

.. _D.21:

Proposition 21 [κα΄ · Omitted (cf. Prop. XVIII)]
------------------------------------------------

.. enunciation::

   If there be two given magnitudes, and there be added to them magnitudes having a given ratio to one another, either the wholes have a given ratio to one another, or one is greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A+x : C+y) | GreaterThanInRatio)`` · *Dependencies*: :just:`[Data 14] <D.14>`, :just:`[V.18] <V.18>`

Let there be two given magnitudes $AB$ and $CD$, and to them let magnitudes $BE$ and $DF$, having a given ratio $BE : DF$ to one another, be added. I say that the wholes $AE$ and $CF$ either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

Since $BE : DF$ is given, and to the two magnitudes $BE$ and $DF$ having a given ratio to one another the given magnitudes $AB$ and $CD$ have been added, the wholes $AE$ and $CF$ either have a given ratio to one another or one is greater by a given magnitude than in ratio to the other (proved identically to :just:`[Data 14] <D.14>` by making $BG : CD = BE : DF$, so $BG$ is given by :just:`[Data 2] <D.2>`; if $BG = AB$ then $AE : CF = BE : DF$ by :just:`[V.12] <V.12>`, while if $AB > BG$ then $AG$ is given by :just:`[Data 4] <D.4>` and $AE = AG + GE$ exceeds $GE$ by given $AG$ with $GE : CF = BE : DF$).

.. _D.22:

Proposition 22 [κβ΄ · Prop. XI]
-------------------------------

.. enunciation::

   If two magnitudes have a given ratio to some magnitude, the magnitude compounded out of both will also have a given ratio to that same magnitude.

*Functional Signature*: ``Given(Ratio(A : C) = r1, Ratio(B : C) = r2) -> Determined(Ratio((A + B) : C) = r1 + r2)`` · *Dependencies*: :just:`[Data 3] <D.3>`, :just:`[Data 6] <D.6>`, :just:`[Data 8] <D.8>`, :just:`[V.24] <V.24>`

Let two magnitudes $A$ and $B$ each have a given ratio to $C$. I say that the compound $A + B$ also has a given ratio to $C$.

Since the ratio $A : C$ is given and the ratio $B : C$ is given, the ratio $A : B$ is given (:just:`[Data 8] <D.8>`). Therefore the compound $A + B$ has a given ratio to $A$ (:just:`[Data 6] <D.6>`). Yet $A$ has a given ratio to $C$; *ex aequali*, the compound $A + B$ also has a given ratio to $C$ (:just:`[Data 8] <D.8>`).

.. _D.23:

Proposition 23 [κγ΄ · Prop. XII]
--------------------------------

.. enunciation::

   If a whole have to a whole a given ratio, and the parts have to the parts given ratios, yet not the same ratios, all the parts will have given ratios to all.

*Functional Signature*: ``Given(AB:CD = r0, AE:CF = r1 != r0, EB:FD = r2) -> Determined(All pairwise ratios)`` · *Dependencies*: :just:`[Data 5] <D.5>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.19] <V.19>`

Let the whole $AB$ have a given ratio to the whole $CD$, and let each of the parts $AE, EB$ of $AB$ have given ratios to the parts $CF, FD$ of $CD$ respectively, *but not the same ratios* (*μὴ τοὺς αὐτοὺς δέ*, so $AE : CF \neq EB : FD$). I say that all have given ratios to all.

Make $AE : CG = AB : CD$ (:just:`[Data Def. 2] <D.def.2>`). Since $AB : CD$ and $AE : CF$ are distinct ratios, $CG \neq CF$; suppose $G$ falls beyond $F$ on $CD$ (so $CG > CF$). Because $AE : CF$ is given and $AE : CG (= AB : CD)$ is given, the ratio $CF : CG$ is given (:just:`[Data 8] <D.8>`), whence *convertendo* $CF : FG$ is given (:just:`[Data 5] <D.5>`). Moreover, since whole $AB$ is to whole $CD$ as subtracted $AE$ is to subtracted $CG$, the remainder $EB$ is to the remainder $GD$ as $AB$ is to $CD$ (:just:`[V.19] <V.19>`), so $EB : GD$ is given. Yet $EB : FD$ is also given by hypothesis; hence $FD : GD$ is given (:just:`[Data 8] <D.8>`), and *separando* $FG : GD$ (and thus $FG : FD$) is given (:just:`[Data 5] <D.5>`). Combining $CF : FG$ and $FG : FD$ yields $CF : FD$ given (:just:`[Data 8] <D.8>`), whence $CD : CF$ and $CD : FD$ are given (:just:`[Data 6] <D.6>`). Chaining with the given ratios $AE : CF$ and $EB : FD$ gives $AE : EB$ and every pairwise ratio among $AB, AE, EB, CD, CF, FD$ (:just:`[Data 8] <D.8>`, :just:`[Data 9] <D.9>`).

.. _D.24:

Proposition 24 [κδ΄ · Prop. XIII]
---------------------------------

.. folio:: Menge 44
   :page: 44

.. enunciation::

   If three straight lines be proportional, and the first have to the third a given ratio, it will also have to the second a given ratio.

*Functional Signature*: ``Given(A : B = B : C, Ratio(A : C)) -> Determined(Ratio(A : B))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[VI.13] <VI.13>`, :just:`[VI.17] <VI.17>`, :just:`[VI.22] <VI.22>`

Let three straight lines $A, B, C$ be in continued proportion ($A : B = B : C$), and let the first $A$ have a given ratio to the third $C$. I say that $A$ also has a given ratio to the second $B$.

Let a given straight line $D$ be set out. Since the ratio $A : C$ is given, let the ratio $D : F$ be made the same with it (:just:`[Data Def. 2] <D.def.2>`); because $D$ is given, $F$ is also given (:just:`[Data 2] <D.2>`). Let the mean proportional $E$ be taken between $D$ and $F$ (:just:`[VI.13] <VI.13>`), so that the rectangle $D \cdot F$ is equal to the square $E^2$ (:just:`[VI.17] <VI.17>`). Since both $D$ and $F$ are given in magnitude, the rectangle $D \cdot F$ is given—and therefore $E^2$ is given, whence the straight line $E$ is given in magnitude (compare :just:`[Data 52] <D.52>` / :just:`[Data Def. 1] <D.def.1>`). Because $D$ is also given, the ratio $D : E$ is given (:just:`[Data 1] <D.1>`). Now since $A : C = D : F$, while $A : C = A^2 : (A \cdot C)$ and $D : F = D^2 : (D \cdot F)$ (:just:`[VI.1] <VI.1>`), it follows that $A^2 : (A \cdot C) = D^2 : (D \cdot F)$ (:just:`[V.11] <V.11>`). Substituting $B^2 = A \cdot C$ (from $A : B = B : C$, :just:`[VI.17] <VI.17>`) and $E^2 = D \cdot F$ gives $A^2 : B^2 = D^2 : E^2$, whence for the sides themselves $A : B = D : E$ (:just:`[VI.22] <VI.22>`). Since $D : E$ is given, the ratio $A : B$ is also given (:just:`[Data Def. 2] <D.def.2>`).
