:order: 50
:type: chapter
:canonical_id: D.unit.5
:folio: Menge pp. 126–164
:book: Propositions 68–83: Proportional Figures
:description: Compound ratio calculus for equiangular and supplementary-angle parallelograms and triangles (D.68–D.75), dropped-altitude ratios in species-given triangles (D.76), duplicated/corollarial area-species bridges (D.77–D.78), inscribed circle-triangle similarity lemmas and area-product determination (D.79–D.80), and four-line proportional transformations (D.81–D.83).

.. _data-unit-5-en:

=========================================================================================
Unit 5: Proportional Parallelograms, Triangles & Four-Line Relations (Propositions 68–83)
=========================================================================================

*Compound Side-Ratios, Reciprocal Proportions, Simson's Lemma, and Four-Line Cross-Multiplications* — **D.68–D.83 (Simson L–LXXVIII) · Menge (1896) pp. 126–164**

.. note::

   **Edition Track (English)**: Compound ratio calculus for equiangular and supplementary-angle parallelograms and triangles (D.68–D.75), dropped-altitude ratios in species-given triangles (D.76), duplicated/corollarial area-species bridges (D.77–D.78), inscribed circle-triangle similarity lemmas and area-product determination (D.79–D.80), and four-line proportional transformations (D.81–D.83). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. _D.68:

Proposition 68 [ξη΄ · Prop. LXV]
--------------------------------

.. folio:: Menge 126
   :page: 126

.. enunciation::

   If two equiangular parallelograms have a given ratio to one another, and one side have to one side a given ratio, the remaining side will also have to the remaining side a given ratio.

*Functional Signature*: ``Given(Equiangular(P1, P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 56] <D.56>`, :just:`[I.31] <I.31>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`

Let two equiangular parallelograms $AB$ ($= ACDB$) and $EF$ ($= EGHF$) have a given area ratio $AB : EF$, and let one side $BD$ have a given ratio to one side $FH$. I say that the remaining side $CD$ also has a given ratio to the remaining side $GH$.

Along $CD$ (produced if necessary) apply to $BD$ the equiangular parallelogram $BDKL$ equal in area to $EF$ (:just:`[I.44] <I.44>`). Because $AB : EF$ is given and $BDKL = EF$, the ratio $AB : BDKL$ is given; since $AB$ and $BDKL$ share the base $BD$ in the same angle, $CD : DK = AB : BDKL$ (:just:`[VI.1] <VI.1>`), so $CD : DK$ is given. Moreover, because $BDKL$ and $EF$ are equal and equiangular, their sides about the equal angles are reciprocally proportional: $BD : FH = GH : DK$ (:just:`[VI.14] <VI.14>`). Since $BD : FH$ is given, $GH : DK$ is given; combining $CD : DK$ with $DK : GH$ yields $CD : GH$ given (:just:`[Data 8] <D.8>`).

.. _D.69:

Proposition 69 [ξθ΄ · Prop. LXVI]
---------------------------------

.. folio:: Menge 128
   :page: 128

.. enunciation::

   If two parallelograms have given angles, and have a given ratio to one another, and one side have to one side a given ratio, the remaining side will also have a given ratio to the remaining side.

*Functional Signature*: ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.12] <I.12>`, :just:`[I.23] <I.23>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`

Let two parallelograms $AB$ (with given angle $\angle CDB$) and $EF$ (with given angle $\angle GHF$, not necessarily equal to $\angle CDB$) have a given area ratio $AB : EF$, and let one side $BD$ have a given ratio to one side $FH$. I say that the remaining side $CD$ also has a given ratio to the remaining side $GH$.

If $AB$ and $EF$ are equiangular, the conclusion holds immediately by :just:`[Data 68] <D.68>`. Suppose $\angle CDB \neq \angle GHF$: at $D$ on $BD$, draw $DK$ making $\angle BDK = \angle GHF$ (:just:`[I.23] <I.23>`), meeting the line of the opposite side $AC$ (produced) at $K$, and complete the parallelogram $BDKL$ (:just:`[I.31] <I.31>`). In $\\triangle CDK$, $\angle CDK$ is the difference (or supplement difference) of the two given angles $\angle CDB$ and $\angle BDK$, so $\angle CDK$ is given (:just:`[Data 4] <D.4>`), and $\angle CKD$ equals the interior/alternate angle with $BD$ (:just:`[I.29] <I.29>`), which is given; hence $\\triangle CDK$ is given in species (:just:`[Data 40] <D.40>`), so the ratio $CD : DK$ is given! Because $AB$ and $BDKL$ lie between the same parallels $AC$ and $BD$ on the same base $BD$, $AB = BDKL$ (:just:`[I.35] <I.35>`). Thus $BDKL$ is equiangular with $EF$, $BDKL : EF = AB : EF$ is given, and $BD : FH$ is given; by :just:`[Data 68] <D.68>`, the ratio $DK : GH$ is given. Combining $CD : DK$ and $DK : GH$ gives $CD : GH$ given (:just:`[Data 8] <D.8>`).

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

.. _D.71:

Proposition 71 [οα΄ · Prop. LXVIII Cor. 1]
------------------------------------------

.. folio:: Menge 134
   :page: 134

.. enunciation::

   If of two triangles the sides about equal angles, or about unequal yet given angles, have given ratios to one another, the triangles themselves also have a given ratio to one another.

*Functional Signature*: ``Given(Angle(A), Angle(D), Ratio(c1 : c2), Ratio(b1 : b2)) -> Determined(Ratio(△1 : △2))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`

Let two triangles $\\triangle ABC$ and $\\triangle DEF$ have their sides about either equal angles ($\angle B = \angle E$) or given unequal angles ($\angle B, \angle E$) in given ratios ($AB : DE$ given and $BC : EF$ given). I say that the area ratio $\\triangle ABC : \\triangle DEF$ is given.

Complete the parallelograms $ABCG$ and $DEFH$ by drawing parallels to the opposite sides (:just:`[I.31] <I.31>`). Then $ABCG$ and $DEFH$ are parallelograms having either equal angles $\angle B = \angle E$ or given angles $\angle B, \angle E$, with $AB : DE$ and $BC : EF$ given; therefore by :just:`[Data 70] <D.70>`, the ratio $ABCG : DEFH$ is given. Since each parallelogram is double its triangle (:just:`[I.34] <I.34>`), $\\triangle ABC : \\triangle DEF = ABCG : DEFH$ (:just:`[V.15] <V.15>`), so $\\triangle ABC : \\triangle DEF$ is given.

.. _D.72:

Proposition 72 [οβ΄ · Prop. LXVIII Cor. 2]
------------------------------------------

.. folio:: Menge 136
   :page: 136

.. enunciation::

   If of two triangles both the bases be in a given ratio, and the straight lines drawn onto them from the vertices making either equal angles or unequal yet given angles with the bases be in a given ratio, the triangles themselves will also have a given ratio to one another.

*Functional Signature*: ``Given(Ratio(b1 : b2), Ratio(d1 : d2), Angle(phi1), Angle(phi2)) -> Determined(Ratio(△1 : △2))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[I.41] <I.41>`

Let two triangles $\\triangle ABC$ and $\\triangle DEF$ have their bases in a given ratio $BC : EF$, and let the altitudes $AG$ and $DH$ drawn to the bases from the opposite vertices also have a given ratio $AG : DH$. I say that the area ratio $\\triangle ABC : \\triangle DEF$ is given.

Complete the rectangles (or right-angled parallelograms) $KBCG$ of altitude $AG$ on base $BC$ and $LEFH$ of altitude $DH$ on base $EF$ (:just:`[I.31] <I.31>`). Because all right angles are equal (:just:`[Post. 4] <I.post.4>`), $KBCG$ and $LEFH$ are equiangular parallelograms with side ratios $BC : EF$ given and $BG : EH$ ($= AG : DH$) given; hence $KBCG : LEFH$ is given (:just:`[Data 70] <D.70>`). Since each rectangle is double its triangle (:just:`[I.41] <I.41>`), $\\triangle ABC : \\triangle DEF = KBCG : LEFH$ (:just:`[V.15] <V.15>`) is given.

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

.. _D.75:

Proposition 75 [οε΄ · Prop. LXIV Cor.]
--------------------------------------

.. folio:: Menge 144
   :page: 144

.. enunciation::

   If two triangles have a given ratio to one another, either in equal angles or in unequal yet given angles, as a side of the first is to a side of the second, so will the other side of the second be to that straight line to which the remaining side of the first has a given ratio.

*Functional Signature*: ``Given(Angle(A), Angle(D), Ratio(△1 : △2)) -> Determined(AB : DE = DF : K with GivenRatio(AC : K))`` · *Dependencies*: :just:`[Data 74] <D.74>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`

Let two triangles $\\triangle ABC$ and $\\triangle DEF$ have a given area ratio $\\triangle ABC : \\triangle DEF$, and let the angles $\angle B$ and $\angle E$ either be equal, or be supplementary ($\angle B + \angle E = 2\\text{ rt.}$), or be unequal given angles. I say that as $BC$ is to $EF$, so is $DE$ to a straight line to which $AB$ has a given ratio.

Complete the parallelograms $ABCG$ and $DEFH$ (:just:`[I.31] <I.31>`). Since each parallelogram is double its triangle (:just:`[I.34] <I.34>`), $ABCG : DEFH = \\triangle ABC : \\triangle DEF$ (:just:`[V.15] <V.15>`) is given. If $\angle B = \angle E$, then $ABCG$ and $DEFH$ are equiangular; if $\angle B + \angle E = 2\\text{ rt.}$, then in parallelogram $ABCG$ the adjacent angle $\angle BAG = 2\\text{ rt.} - \angle B = \angle E$ (:just:`[I.29] <I.29>`), so $ABCG$ (viewed at $\angle A$ with sides $AG = BC$ and $AB$) is again equiangular with $DEFH$! And if $\angle B$ and $\angle E$ are both given, $ABCG$ and $DEFH$ have given angles. In every case, :just:`[Data 74] <D.74>` applies to $ABCG$ and $DEFH$, proving that $BC : EF = DE : K$ where $AB : K$ is given.

.. _D.76:

Proposition 76 [οϚ΄ · Prop. L]
------------------------------

.. enunciation::

   If in a triangle given in species a perpendicular be drawn from the vertex onto the base, the drawn perpendicular has a given ratio to the base.

*Functional Signature*: ``Given(Species(△ABC), AD perp BC) -> Determined(Ratio(AD : BC))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`

In a triangle $\\triangle ABC$ given in species, let the perpendicular $AD$ be drawn from the vertex $A$ to the base $BC$ (:just:`[I.12] <I.12>`). I say that the perpendicular $AD$ has a given ratio to the base $BC$.

Since $\\triangle ABC$ is given in species, the angle $\angle ABD$ (or its supplement if $\angle ABC$ is obtuse) is given (:just:`[Data Def. 3] <D.def.3>`), and the side ratio $AB : BC$ is also given. In right-angled $\\triangle ABD$, $\angle ADB = 1\\text{ rt.}$ and $\angle ABD$ is given, so $\\triangle ABD$ is given in species (:just:`[Data 40] <D.40>`), whence the ratio $AD : AB$ is given. Combining $AD : AB$ with $AB : BC$ yields $AD : BC$ given (:just:`[Data 8] <D.8>`).

.. _D.77:

Proposition 77 [οζ΄ · Omitted (dup. of Prop. LIX / D.54)]
---------------------------------------------------------

.. folio:: Menge 148
   :page: 148

.. enunciation::

   If two figures given in species have a given ratio to one another, any side of one of the figures will also have a given ratio to any side of the other.

*Functional Signature*: ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(s(A) : s(B)))`` · *Dependencies*: :just:`[Data 54] <D.54>`, :just:`[VI.20] <VI.20>`

Let two rectilinear figures $ABC$ and $DEF$, given in species, have a given area ratio $ABC : DEF$. I say that any side of one has a given ratio to any side of the other.

Exactly as in :just:`[Data 54] <D.54>` (of which this proposition in :cite:`Vat. gr. 190 <vat-gr-190>` is an alternative doublet using auxiliary squares on a side of each figure): construct squares $BG$ on $BC$ and $EH$ on $EF$ (:just:`[I.46] <I.46>`). Since $ABC$ and $BG$ are both given in species on $BC$, $BG : ABC$ is given (:just:`[Data 49] <D.49>`); similarly $DEF : EH$ is given (:just:`[Data 49] <D.49>`). Combining with given $ABC : DEF$ gives $BG : EH$ given (:just:`[Data 8] <D.8>`). Taking the third proportional $K$ to $BC$ and $EF$ so $BC : EF = EF : K$, we have $BC : K = BG : EH$ given (:just:`[VI.20] <VI.20>` Cor.), whence $BC : EF$ is given (:just:`[Data 24] <D.24>`), and all remaining side ratios follow by :just:`[Data 53] <D.53>`.

.. _D.78:

Proposition 78 [οη΄ · Omitted (case of Prop. LXX / D.62)]
---------------------------------------------------------

.. enunciation::

   If a given figure have a given ratio to some parallelogram, and one side have a given ratio to one side of the figure, while the parallelogram is in a given angle, the parallelogram will be given in species.

*Functional Signature*: ``Given(Species(A), Ratio(A : B), Ratio(s(A) : s1(B)), Angle(B)) -> Determined(Species(B))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 62] <D.62>`, :just:`[VI.14] <VI.14>`

Let a rectilinear figure $AFEB$ given in species have a given area ratio to a rectangle $BC \cdot CD$, and let one side $AB$ of $AFEB$ have a given ratio to $BC$. I say that $CD$ has a given ratio to $BC$ (and $AB$), so the rectangle $BC \cdot CD$ is given in species.

Construct the square $ABGH$ on $AB$ (:just:`[I.46] <I.46>`). Since both $AFEB$ and $ABGH$ are given in species on $AB$, the ratio $ABGH : AFEB$ is given (:just:`[Data 49] <D.49>`). Combining with the given ratio $AFEB : (BC \cdot CD)$ yields $AB^2 : (BC \cdot CD)$ given (:just:`[Data 8] <D.8>`). Moreover, since $AB : BC$ is given, the ratio $AB^2 : (AB \cdot BC)$ ($= AB : BC$ by :just:`[VI.1] <VI.1>`) is given, whence $(AB \cdot BC) : (BC \cdot CD)$ is given (:just:`[Data 8] <D.8>`). Canceling the common side $BC$ (:just:`[VI.1] <VI.1>`) gives $AB : CD$ (and hence $BC : CD$) given, so the rectangle $BC \cdot CD$ is given in species (:just:`[Data Def. 3] <D.def.3>`).

.. _D.79:

Proposition 79 [οθ΄ · Prop. LXXVII Cor. 1]
------------------------------------------

.. folio:: Menge 152
   :page: 152

.. enunciation::

   If there be two triangles having one angle equal to one angle, and from the vertices perpendiculars be drawn to the bases, and as the base of the first triangle is to its perpendicular, so be the base of the second triangle to its perpendicular, the triangles are equiangular.

*Functional Signature*: ``Given(∠BAC = ∠EDF, BC : h_A = EF : h_D) -> Determined(△ABC ~ △DEF)`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data Def. 7] <D.def.7>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[III.21] <III.21>`, :just:`[VI.4] <VI.4>`

Let two triangles $\\triangle ABC$ and $\\triangle DEF$ have one equal angle $\angle BAC = \angle EDF$, and from the vertices $A$ and $D$ let perpendiculars $AG \perp BC$ and $DH \perp EF$ be drawn; if $BC : AG = EF : DH$, I say that $\\triangle ABC$ and $\\triangle DEF$ are equiangular (and hence similar).

Circumscribe circles $ABC$ and $DEF$ about the two triangles (:just:`[IV.5] <IV.5>`), cutting off segments on $BC$ and $EF$ that contain the equal angles $\angle BAC = \angle EDF$ (:just:`[III.21] <III.21>`). Complete the cyclic symmetry by constructing on $EF$ a triangle $\\triangle EKF$ similar to $\\triangle ABC$ inscribed in circle $DEF$ (so $\angle EKF = \angle BAC = \angle EDF$, placing $K$ on arc $EDF$ by :just:`[III.21] <III.21>`), and drop perpendicular $KL \perp EF$. Since $\\triangle EKF \sim \\triangle ABC$, their base-to-altitude ratios match: $EF : KL = BC : AG$ (:just:`[VI.4] <VI.4>`). Yet $BC : AG = EF : DH$ by hypothesis; therefore $EF : KL = EF : DH$ (:just:`[V.11] <V.11>`), whence $KL = DH$ (:just:`[V.9] <V.9>`). Thus the line through $K$ and $D$ is parallel to $EF$ (:just:`[I.33] <I.33>`), cutting equal arcs $EK = DF$ (or $K = D$) in circle $DEF$, so the inscribed angles are equal (up to swapping $\angle E$ and $\angle F$), making $\\triangle ABC$ and $\\triangle DEF$ equiangular!

.. _D.80:

Proposition 80 [π΄ · Prop. LXXVIII]
-----------------------------------

.. folio:: Menge 154
   :page: 154

.. enunciation::

   If a triangle have one angle given, and the rectangle contained by the sides about the given angle have a given ratio to the square on the remaining side, the triangle is given in species.

*Functional Signature*: ``Given(Angle A, Ratio((b*c) : a^2)) -> Determined(Species(△ABC))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 66] <D.66>`, :just:`[Data 68] <D.68>`, :just:`[Data 79] <D.79>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`

Let $\\triangle ABC$ have a given angle $\angle BAC$, and let the rectangle $BA \cdot AC$ contained by the sides about the given angle have a given ratio to the square $BC^2$ on the remaining side. I say that $\\triangle ABC$ is given in species.

Drop the altitude $AD \perp BC$ (:just:`[I.12] <I.12>`). Because $\\triangle ABC$ has given angle $\angle BAC$, the ratio $(BA \cdot AC) : \\triangle ABC$ is given (:just:`[Data 66] <D.66>`). Combining this with the given ratio $(BA \cdot AC) : BC^2$ yields $BC^2 : \\triangle ABC$ given (:just:`[Data 8] <D.8>`), and since $BC \cdot AD = 2\,\\triangle ABC$ (:just:`[I.41] <I.41>`), the ratio $BC^2 : (BC \cdot AD) = BC : AD$ is given (:just:`[VI.1] <VI.1>`). Now set out a straight line $FG$ given in position and magnitude, and on $FG$ describe the circular segment $FHG$ admitting an angle equal to given $\angle BAC$ (:just:`[III.33] <III.33>`), whose arc is given in position. Take $L$ so that $FG : L = BC : AD$ (:just:`[Data 2] <D.2>`), erect $FK = L$ perpendicular to $FG$, and draw $KH \parallel FG$ meeting the arc $FHG$ at $H$ (:just:`[Data 28] <D.28>`, :just:`[Data 25] <D.25>`). Joining $FH$ and $HG$ gives $\\triangle FHG$ in species (:just:`[Data 39] <D.39>`) with $\angle FHG = \angle BAC$ and base-to-altitude ratio $FG : L = BC : AD$. By :just:`[Data 79] <D.79>`, $\\triangle ABC$ is equiangular with $\\triangle FHG$, and therefore $\\triangle ABC$ is given in species (:just:`[Data 40] <D.40>`).

.. _D.81:

Proposition 81 [πα΄ · Prop. LXXI]
---------------------------------

.. folio:: Menge 158
   :page: 158

.. enunciation::

   If of three proportional straight lines the extremes have given ratios to the extremes of three proportional straight lines, the means will also have a given ratio to one another; and if an extreme have a given ratio to an extreme and the mean to the mean, the remaining extreme will also have a given ratio to the remaining extreme.

*Functional Signature*: ``Given(B^2 = A*C, E^2 = D*F) -> (Given(A:D, C:F) -> Given(B:E)) & (Given(A:D, B:E) -> Given(C:F))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 50] <D.50>`, :just:`[Data 54] <D.54>`, :just:`[Data 70] <D.70>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`

First, let three straight lines $A, B, C$ in continued proportion ($A : B = B : C$) and three straight lines $D, E, F$ in continued proportion ($D : E = E : F$) have their extremes in given ratios—namely $A : D$ given and $C : F$ given. I say that their means $B$ and $E$ also have a given ratio $B : E$.

Since $A : D$ is given and $C : F$ is given, the ratio of the rectangles $(A \cdot C) : (D \cdot F)$ is given (:just:`[Data 70] <D.70>`). Yet $A \cdot C = B^2$ and $D \cdot F = E^2$ (:just:`[VI.17] <VI.17>`). Therefore $B^2 : E^2$ is given, whence the ratio of the means $B : E$ is given (:just:`[Data 54] <D.54>`).

Second, let one extreme have a given ratio to one extreme ($A : D$ given) and the mean to the mean ($B : E$ given). I say that the remaining extreme $C$ also has a given ratio to $F$.

Since $B : E$ is given, $B^2 : E^2$ is given (:just:`[Data 50] <D.50>`), and therefore $(A \cdot C) : (D \cdot F)$ is given (:just:`[VI.17] <VI.17>`). Because the equiangular rectangles $A \cdot C$ and $D \cdot F$ have a given area ratio while one side $A$ has a given ratio to $D$, the remaining side $C$ has a given ratio to $F$ (:just:`[Data 68] <D.68>`).

.. _D.82:

Proposition 82 [πβ΄ · Prop. LXXII]
----------------------------------

.. folio:: Menge 160
   :page: 160

.. enunciation::

   If four straight lines be proportional, as the first is to that straight line to which the second has a given ratio, so will the third be to that straight line to which the fourth has a given ratio.

*Functional Signature*: ``Given(A : B = C : D, Ratio(B : E) = k) -> Determined(Ratio(D : F) = k when A : E = C : F)`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.22] <V.22>`

Let four straight lines $A, B, C, D$ be proportional ($A : B = C : D$). I say that as the first $A$ is to the line $E$ to which the second $B$ has a given ratio, so is the third $C$ to a line $F$ to which the fourth $D$ has a given ratio.

Let $E$ be any straight line to which $B$ has a given ratio $B : E$. Make $D : F = B : E$ (:just:`[Data Def. 2] <D.def.2>`), so $D$ has the same given ratio to $F$. Now since $A : B = C : D$, *alternando* $A : C = B : D$ (:just:`[V.16] <V.16>`), while from $B : E = D : F$ *alternando* $B : D = E : F$ (:just:`[V.16] <V.16>`). Therefore $A : C = E : F$ (:just:`[V.11] <V.11>`), and *alternando* $A : E = C : F$ (:just:`[V.16] <V.16>`), where $D : F$ is given.

.. _D.83:

Proposition 83 [πγ΄ · Prop. LXXIII]
-----------------------------------

.. enunciation::

   If four straight lines be so related to one another that, when three of them are taken and a fourth is assumed to them to which the remaining one of the original four has a given ratio, the four straight lines are proportional, then as the fourth is to the third, so is the second to that straight line to which the first has a given ratio.

*Functional Signature*: ``Given(A * D = B * E, Ratio(C : E) = k) -> Determined(D : C = B : (A / k))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 68] <D.68>`, :just:`[V.16] <V.16>`, :just:`[V.23] <V.23>`, :just:`[VI.16] <VI.16>`

Let four straight lines $A, B, C, D$ be so related to one another that when any three of them ($A, B, C$) are taken, and a fourth $E$ is taken to which the remaining line $D$ has a given ratio $D : E$ such that $A : B = C : E$, I say that $D$ is to $C$ as $B$ is to a straight line $F$ to which $A$ has a given ratio (and similarly for every permutation of the four lines).

Since $A : B = C : E$ and the ratio $D : E$ is given, make $A : F = D : E$ (:just:`[Data Def. 2] <D.def.2>`), so $A$ has a given ratio to $F$. From $A : F = D : E$, *alternando* $A : D = F : E$ (:just:`[V.16] <V.16>`); and from $A : B = C : E$, *invertendo* and *ex aequali* (:just:`[V.7] <V.7>` Cor., :just:`[V.22] <V.22>`), since $D : E = A : F$ while $E : C = B : A$, multiplying/chaining *ex aequali perturbed* (:just:`[V.23] <V.23>`) gives $D : C = B : F$! Because $A : F$ is given, $D$ is to $C$ as $B$ is to $F$, a straight line to which $A$ has a given ratio.
