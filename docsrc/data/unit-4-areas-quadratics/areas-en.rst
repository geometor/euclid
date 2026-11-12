:order: 40
:type: chapter
:canonical_id: D.unit.4
:folio: Menge pp. 98–126
:book: Propositions 56–67: Areas, Quadratics & Cosines
:description: Equiangular parallelograms and parabolic division of areas (D.56–D.57), quadratic root extraction via elliptic and hyperbolic application of areas (D.58–D.59) and gnomons (D.60), altitude-to-base ratios (D.61–D.63), generalized Law of Cosines projections in obtuse and acute triangles (D.64–D.65), area-product law BD·BC : △ABC (D.66), and the algebraic identity (a+b)² − c² (D.67).

.. _data-unit-4-en:

==================================================================================
Unit 4: Application of Areas, Quadratics & Cosine Projections (Propositions 56–67)
==================================================================================

*Geometric Algebra of Parabolic, Elliptic & Hyperbolic Areas and Oblique Triangle Projections* — **D.56–D.67 (Simson LXI–LXXXIV) · Menge (1896) pp. 98–126**

.. note::

   **Edition Track (English)**: Equiangular parallelograms and parabolic division of areas (D.56–D.57), quadratic root extraction via elliptic and hyperbolic application of areas (D.58–D.59) and gnomons (D.60), altitude-to-base ratios (D.61–D.63), generalized Law of Cosines projections in obtuse and acute triangles (D.64–D.65), area-product law BD·BC : △ABC (D.66), and the algebraic identity (a+b)² − c² (D.67). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. _D.56:

Proposition 56 [νϛ΄ · Prop. LXIII]
----------------------------------

.. folio:: Menge 100
   :page: 100

.. enunciation::

   If two equiangular parallelograms have a given ratio to one another, as a side of the first is to a side of the second, so is the remaining side of the second to that straight line to which the remaining side of the first has the given ratio that the parallelogram has to the parallelogram.

*Functional Signature*: ``Given(Equiangular(P1, P2), Ratio(P1 : P2) = k) -> Determined(s1 : t1 = t2 : (s2 / k))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`

Let two equiangular parallelograms $ABCD$ and $EFGH$ have a given area ratio $ABCD : EFGH$. I say that as $CD$ (a side of the first) is to $FG$ (a side of the second), so is the remaining side $GH$ of the second to a straight line to which the remaining side $BC$ of the first has a given ratio.

Produce $BC$ to $K$ so that the ratio $BC : CK$ is equal to the given area ratio $ABCD : EFGH$ (:just:`[Data Def. 2] <D.def.2>`), and complete the equiangular parallelogram $CDLK$ on $CD$ and $CK$ (:just:`[I.31] <I.31>`). Because $ABCD$ and $CDLK$ share the base $CD$ and have the same altitude, $ABCD : CDLK = BC : CK$ (:just:`[VI.1] <VI.1>`). Yet $BC : CK = ABCD : EFGH$ by construction; therefore $CDLK = EFGH$ (:just:`[V.9] <V.9>`). Now $CDLK$ and $EFGH$ are equal and equiangular parallelograms, so their sides about the equal angles are reciprocally proportional: $CD : FG = GH : CK$ (:just:`[VI.14] <VI.14>`). And since $BC : CK$ is given, $CD$ is to $FG$ as $GH$ is to $CK$, a straight line to which $BC$ has a given ratio.

.. _D.57:

Proposition 57 [νζ΄ · Prop. LXI]
--------------------------------

.. folio:: Menge 102
   :page: 102

.. enunciation::

   If a given area be applied to a given straight line in a given angle, the breadth of the application is given.

*Functional Signature*: ``Given(Mag(Area S), Mag(Base a), Mag(Angle theta)) -> Determined(Mag(Breadth x))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 52] <D.52>`, :just:`[I.31] <I.31>`, :just:`[I.46] <I.46>`, :just:`[VI.1] <VI.1>`

Let a given area $AC$ (a parallelogram in a given angle $\angle CAB$) be :term:`applied <parabole>` to a straight line $AB$ given in magnitude (:just:`[I.44] <I.44>`). I say that its breadth $CB$ (or $AD$) is given in magnitude.

On the given straight line $AB$, describe the square $AEFB$ (:just:`[I.46] <I.46>`), which is given in magnitude (:just:`[Data 52] <D.52>`), and produce $EA$ to meet the opposite side $CD$ (or complete the equiangular auxiliary parallelogram $AGHB$ on $AB$ with $AG = AB$). Since $AC$ is given in magnitude and $AEFB$ is given in magnitude, the ratio $AC : AEFB$ is given (:just:`[Data 1] <D.1>`). Moreover, comparing $AC$ with the rhombus $AGHB$ on $AB$ in the given angle $\angle CAB$ (whose species is given by :just:`[Data Def. 3] <D.def.3>`, so $AGHB : AEFB$ is given by :just:`[Data 49] <D.49>`), the ratio $AC : AGHB$ is given (:just:`[Data 8] <D.8>`). Yet on the common side $AB$ in the same angle, $AC : AGHB = AD : AG = AD : AB$ (:just:`[VI.1] <VI.1>`). Since $AD : AB$ is given and $AB$ is given in magnitude, the breadth $AD$ ($= CB$) is given in magnitude (:just:`[Data 2] <D.2>`).

.. picture:: /_static/figures/data_04_area_application.svg
   :alt: Elliptic (D.58) and Hyperbolic (D.59) Application of Areas

Interactive geometric-algebra diagram (:cite:`Menge pp. 104–110 <menge:1896>`): Left panel shows **elliptic application** (:term:`ἔλλειψις <elleipsis>`, :ref:`D.58 <D.58>`), applying given area :g:`AHKE <data_04_area_application:< A H K E >>` to given line :g:`AB <data_04_area_application:/ A B />` (midpoint :g:`M <data_04_area_application:M>`) deficient by species-given figure :g:`EKBG <data_04_area_application:< E K B G >>` of breadth :g:`EK <data_04_area_application:/ E K />`. Right panel shows **hyperbolic application** (:term:`ὑπερβολή <hyperbole>`, :ref:`D.59 <D.59>`), applying given area :g:`PRST <data_04_area_application:< P R S T >>` along extended base :g:`PR <data_04_area_application:/ P R />` (from given segment endpoint :g:`Q <data_04_area_application:Q>` bisected at :g:`W <data_04_area_application:W>`, crossbar :g:`QW <data_04_area_application:/ Q W />`) exceeding by species-given figure on :g:`RS <data_04_area_application:/ R S />` enclosed within gnomon square :g:`PQUV <data_04_area_application:< P Q U V >>`.

.. _D.58:

Proposition 58 [νη΄ · Prop. LXXXIII]
------------------------------------

.. folio:: Menge 104
   :page: 104

.. enunciation::

   If a given area be applied to a given straight line, falling short by a figure given in species, the breadths of the defect are given.

*Functional Signature*: ``Given(Mag(S), Mag(a), Species(Defect)) -> Determined(Roots of a*x - c*x^2 = S) [diorismos]`` · *Dependencies*: :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.5] <II.5>`, :just:`[VI.24] <VI.24>`, :just:`[VI.27] <VI.27>`, :just:`[VI.28] <VI.28>`

Let a given area $AC$ be applied to a straight line $AB$ given in magnitude, :term:`deficient <elleipsis>` by a parallelogram $CDFB$ given in species (:just:`[VI.28] <VI.28>`). I say that both the breadths and bases of the deficiency ($BD, DF$ and $AD$) are given in magnitude.

Bisect $AB$ at $E$ (:just:`[I.10] <I.10>`). Since $AB$ is given in magnitude, its half $EB$ ($= AE$) is given in magnitude (:just:`[Data 7] <D.7>`). On $EB$ describe the parallelogram $EFGH$ similar and similarly situated to the species-given defect $CDFB$ (:just:`[VI.18] <VI.18>`), and complete the diagram of :just:`[VI.28] <VI.28>`. Because $EFGH$ is given in species and described on the given segment $EB$, $EFGH$ is given in magnitude (:just:`[Data 52] <D.52>`). By the gnomon identity (:just:`[II.5] <II.5>` generalized to equiangular parallelograms in :just:`[VI.27] <VI.27>`–:just:`[VI.28] <VI.28>`), $EFGH$ equals the applied area $AC$ together with the inner parallelogram $KHLN$ (which is similar and similarly situated to $EFGH$ on segment $ED = EB - BD$). Since both $EFGH$ and $AC$ are given in magnitude (with $AC \le EFGH$ by the *diorismos* of :just:`[VI.27] <VI.27>`), the difference $KHLN = EFGH - AC$ is given in magnitude (:just:`[Data 4] <D.4>`). Because $KHLN \sim CDFB$ is also given in species, its side $KH$ ($= ED$) is given in magnitude (:just:`[Data 55] <D.55>`). Subtracting $ED$ from given $EB$ gives $BD$ (:just:`[Data 4] <D.4>`), adding $ED$ to given $AE$ gives $AD$ (:just:`[Data 3] <D.3>`), and from species-given $CDFB$ on $BD$ its breadth $DF$ ($= CB$) is given in magnitude (:just:`[Data 2] <D.2>`).

.. _D.59:

Proposition 59 [νθ΄ · Prop. LXXXIV]
-----------------------------------

.. folio:: Menge 106
   :page: 106

.. enunciation::

   If a given area be applied to a given straight line, exceeding by a figure given in species, the breadths of the excess are given.

*Functional Signature*: ``Given(Mag(S), Mag(a), Species(Excess)) -> Determined(Positive root of a*x + c*x^2 = S)`` · *Dependencies*: :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.6] <II.6>`, :just:`[VI.24] <VI.24>`, :just:`[VI.29] <VI.29>`

Let a given area $AB$ (i.e., parallelogram $ACDB$ applied along $AC$ produced to $B$) be applied to a straight line $AC$ given in magnitude, :term:`exceeding <hyperbole>` by a parallelogram $CBEF$ given in species (:just:`[VI.29] <VI.29>`). I say that the sides of the excess ($CB$ and $BE$) are given in magnitude.

Bisect the given straight line $AC$ at $D$ (:just:`[I.10] <I.10>`), so $DC$ is given in magnitude (:just:`[Data 7] <D.7>`). On $DC$ describe the parallelogram $DGHC$ similar and similarly situated to the species-given excess $CBEF$ (:just:`[VI.18] <VI.18>`), so $DGHC$ is given in magnitude (:just:`[Data 52] <D.52>`). Completing the gnomon around the diagonal $BHF$ (:just:`[II.6] <II.6>`, :just:`[VI.29] <VI.29>`), the large parallelogram $DBEK$ described on $DB = DC + CB$ (similar and similarly situated to $CBEF$) is equal to the sum of the given applied area $AB$ and the given parallelogram $DGHC$. Therefore $DBEK$ is given in magnitude (:just:`[Data 3] <D.3>`). Since $DBEK$ is also given in species ($\sim CBEF$), its side $DB$ is given in magnitude (:just:`[Data 55] <D.55>`). Subtracting given $DC$ from $DB$ leaves $CB$ given in magnitude (:just:`[Data 4] <D.4>`), and because $CBEF$ is given in species its adjacent side $BE$ (and the total base $AB = AC + CB$) is given in magnitude (:just:`[Data 2] <D.2>`).

.. _D.60:

Proposition 60 [ξ΄ · Prop. LXXXII]
----------------------------------

.. folio:: Menge 108
   :page: 108

.. enunciation::

   If a parallelogram given in species and in magnitude be increased or diminished by a gnomon given in magnitude, the breadths of the gnomon are given.

*Functional Signature*: ``Given(Species(P), Mag(Area(P)), Mag(Gnomon G)) -> Determined(Mag(Sides of P +/- G))`` · *Dependencies*: :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 55] <D.55>`, :just:`[VI.24] <VI.24>`

First, let a parallelogram $ABCD$, given both in species and in magnitude, be increased by a given :term:`gnomon <gnomon>` $ECBDFG$ so as to form a larger similar parallelogram $AEFG$. I say that the breadths $CE$ and $DF$ of the gnomon are given in magnitude.

Since $ABCD$ is given in magnitude and the gnomon $ECBDFG$ is given in magnitude, the whole parallelogram $AEFG = ABCD + ECBDFG$ is given in magnitude (:just:`[Data 3] <D.3>`). Moreover, because a gnomon adjoined around the diagonal preserves similarity (:just:`[VI.24] <VI.24>`), $AEFG$ is similar to $ABCD$ and hence given in species (:just:`[Data Def. 3] <D.def.3>`). Therefore the side $AE$ of $AEFG$ is given in magnitude (:just:`[Data 55] <D.55>`), while the side $AC$ of $ABCD$ is likewise given in magnitude (:just:`[Data 55] <D.55>`). Subtracting $AC$ from $AE$ yields the gnomon breadth $CE$ given in magnitude (:just:`[Data 4] <D.4>`), and similarly $DF$ is given.

Second, let the species-and-magnitude-given parallelogram $AEFG$ be diminished by a given gnomon $ECBDFG$ leaving $ABCD$: then the remainder $ABCD = AEFG - ECBDFG$ is given in magnitude (:just:`[Data 4] <D.4>`) and in species ($\sim AEFG$), so both $AE$ and $AC$ are given in magnitude (:just:`[Data 55] <D.55>`), whence their difference $CE$ (and $DF$) is given in magnitude (:just:`[Data 4] <D.4>`).

.. _D.61:

Proposition 61 [ξα΄ · Prop. LXIX]
---------------------------------

.. enunciation::

   If along one of the sides of a figure given in species a parallelogrammic area be applied in a given angle, and the figure have a given ratio to the parallelogram, the parallelogram is given in species.

*Functional Signature*: ``Given(Species(P on CB), Angle(CD), Ratio(Area(P) : Area(CD))) -> Determined(Species(CD))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 49] <D.49>`, :just:`[I.13] <I.13>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`

To a specified side $CB$ of a rectilinear figure $AFCB$ given in species, let a parallelogram $CD$ ($= CBKL$) be applied in a given angle $\angle LCB$, and let the figure $AFCB$ have a given ratio to the parallelogram $CD$. I say that the parallelogram $CD$ is given in species.

On $CB$ construct the square $CBEG$ (or a reference parallelogram $CBHM$ in the given angle $\angle LCB$ with $CM = CB$, whose species is given by :just:`[Data Def. 3] <D.def.3>`). Specifically, in Menge's proof, draw $CK = CB$ along $CL$ (or construct square $CBHM$ on $CB$ and compare): since both $AFCB$ and the unit-ratio parallelogram $CBHM$ (with $\angle MCB = \angle LCB$ and $CM = CB$) are given in species on the same straight line $CB$, the area ratio $AFCB : CBHM$ is given (:just:`[Data 49] <D.49>`). Combining this with the given hypothesis $AFCB : CD$ via :just:`[Data 8] <D.8>`, the ratio $CBHM : CD$ is given. Yet $CBHM$ and $CD$ share base $CB$ in the same angle $\angle LCB$, so $CBHM : CD = CM : CL = CB : CL$ (:just:`[VI.1] <VI.1>`). Thus the side ratio $CB : CL$ is given together with the angle $\angle LCB$ (and hence all four angles of $CD$ by :just:`[I.29] <I.29>`, :just:`[I.34] <I.34>`); therefore the parallelogram $CD$ is given in species (:just:`[Data Def. 3] <D.def.3>`).

.. _D.62:

Proposition 62 [ξβ΄ · Prop. LXX]
--------------------------------

.. folio:: Menge 112
   :page: 112

.. enunciation::

   If two straight lines have a given ratio to one another, and on one of them be described a figure given in species, and on the other a parallelogrammic area in a given angle, and the figure have a given ratio to the parallelogram, the parallelogram is given in species.

*Functional Signature*: ``Given(Ratio(AB : CD), Species(AEB on AB), Angle(DF), Ratio(AEB : DF)) -> Determined(Species(DF))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 50] <D.50>`, :just:`[Data 61] <D.61>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`

Let two straight lines $AB$ and $BC$ have a given ratio $AB : BC$; on $AB$ let a rectilinear figure $AEB$ given in species be described, and on $BC$ let a parallelogram $BD$ ($= BCGD$) be described in a given angle $\angle GBC$. If the area ratio $AEB : BD$ is given, I say that the parallelogram $BD$ is given in species.

On $BC$ describe a rectilinear figure $BHC$ similar and similarly situated to $AEB$ (:just:`[VI.18] <VI.18>`), so $BHC$ is given in species. Since $AB : BC$ is given and $AEB \sim BHC$, the area ratio $AEB : BHC$ is given (:just:`[Data 50] <D.50>`). Yet $AEB : BD$ is given by hypothesis; therefore the ratio $BHC : BD$ is given (:just:`[Data 8] <D.8>`). Because the parallelogram $BD$ is applied in the given angle $\angle GBC$ to the side $BC$ of the species-given figure $BHC$ and $BHC : BD$ is given, the parallelogram $BD$ is given in species (:just:`[Data 61] <D.61>`).

.. _D.63:

Proposition 63 [ξγ΄ · Omitted (case of Prop. LIII)]
---------------------------------------------------

.. folio:: Menge 114
   :page: 114

.. enunciation::

   If a triangle be given in species, the square on each of its sides will have a given ratio to the triangle.

*Functional Signature*: ``Given(Species(△ABC)) -> Determined(Ratio(a^2 : △ABC), Ratio(b^2 : △ABC), Ratio(c^2 : △ABC))`` · *Dependencies*: :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`

Let $\\triangle ABC$ be given in species, and on its three sides $AB, BC, CA$ let rectilinear figures $ABDE, BCFG, CAHK$ given in species be described respectively. I say that each of those figures has a given ratio to each of the others.

Since $\\triangle ABC$ is given in species, the pairwise ratios of its sides $AB : BC$, $BC : CA$, and $CA : AB$ are all given (:just:`[Data Def. 3] <D.def.3>`). Moreover, on the two straight lines $AB$ and $BC$ having the given ratio $AB : BC$, the rectilinear figures $ABDE$ and $BCFG$ are each given in species; therefore the ratio $ABDE : BCFG$ is given (:just:`[Data 51] <D.51>`). For the very same reason the ratios $BCFG : CAHK$ and $CAHK : ABDE$ are also given (:just:`[Data 51] <D.51>`).

.. picture:: /_static/figures/data_05_cosine_projection.svg
   :alt: Obtuse (D.64) and Acute (D.65) Altitude Projections & Euclidean Law of Cosines

Interactive cosine-projection diagram (:cite:`Menge pp. 116–122 <menge:1896>`): Left panel (:ref:`D.64 <D.64>`, obtuse :g:`∠CBA <data_05_cosine_projection:< C B A )>`) drops exterior altitude :g:`AD <data_05_cosine_projection:/ A D />` onto :g:`BC <data_05_cosine_projection:/ B C />` produced at :g:`D <data_05_cosine_projection:D>` in :g:`△ABC <data_05_cosine_projection:< A B C >>`, making projection ratio :g:`DB <data_05_cosine_projection:/ D B />` to :g:`AB <data_05_cosine_projection:/ A B />` given and fixing the excess of :g:`AC <data_05_cosine_projection:/ A C />` squared (:just:`[II.12] <II.12>`). Right panel (:ref:`D.65 <D.65>`, acute :g:`∠GFE <data_05_cosine_projection:< G F E )>`) drops interior altitude :g:`EH <data_05_cosine_projection:/ E H />` onto :g:`FG <data_05_cosine_projection:/ F G />` at :g:`H <data_05_cosine_projection:H>` in :g:`△EFG <data_05_cosine_projection:< E F G >>`, making :g:`FH <data_05_cosine_projection:/ F H />` to :g:`EF <data_05_cosine_projection:/ E F />` given and fixing the defect of :g:`EG <data_05_cosine_projection:/ E G />` squared (:just:`[II.13] <II.13>`).

.. _D.64:

Proposition 64 [ξδ΄ · Prop. LXXIV]
----------------------------------

.. enunciation::

   If an obtuse-angled triangle have the obtuse angle given, then that area by which the square on the side subtending the obtuse angle exceeds the squares on the sides containing the obtuse angle will have a given ratio to the triangle.

*Functional Signature*: ``Given(ObtuseAngle B) -> Determined(Ratio((b^2 - a^2 - c^2) : △ABC) = -4 cot B)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.12] <II.12>`, :just:`[VI.1] <VI.1>`

Let $\\triangle ABC$ have the obtuse angle $\angle ABC$ given, and from $A$ let $AD$ be drawn perpendicular to $CB$ produced at $D$ (:just:`[I.12] <I.12>`). I say that the excess $(AC^2 - (AB^2 + BC^2))$ by which $AC^2$ exceeds $AB^2 + BC^2$ has a given ratio to the rectangle $AB \cdot BC$.

Since the obtuse angle $\angle ABC$ is given, its adjacent supplementary angle $\angle ABD$ is given (:just:`[I.13] <I.13>`, :just:`[Data 4] <D.4>`). In right-angled $\\triangle ABD$, $\angle ADB = 1\\text{ rt.}$ and $\angle ABD$ is given, so $\\triangle ABD$ is given in species (:just:`[Data 40] <D.40>`). Therefore the projection ratio $AB : BD$ is given (:just:`[Data Def. 3] <D.def.3>`). Now under the common altitude $BC$, as $AB$ is to $BD$, so is the rectangle $AB \cdot BC$ to the rectangle $CB \cdot BD$ (:just:`[VI.1] <VI.1>`), whence $(AB \cdot BC) : (CB \cdot BD)$ is given, and doubling the consequent gives $(AB \cdot BC) : (2\, CB \cdot BD)$ given (:just:`[Data 8] <D.8>`). Yet because $\angle ABC$ is obtuse, by the obtuse-triangle Pythagorean identity (:just:`[II.12] <II.12>`), $AC^2 = AB^2 + BC^2 + 2\, CB \cdot BD$, so the excess $AC^2 - (AB^2 + BC^2)$ equals $2\, CB \cdot BD$. Therefore that excess has a given ratio ($= 2\, BD : AB = -2\cos\angle ABC$) to $AB \cdot BC$.

.. _D.65:

Proposition 65 [ξε΄ · Prop. LXXV]
---------------------------------

.. folio:: Menge 118
   :page: 118

.. enunciation::

   If an acute-angled triangle have one acute angle given, then that area by which the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle will have a given ratio to the triangle.

*Functional Signature*: ``Given(AcuteAngle B) -> Determined(Ratio((a^2 + c^2 - b^2) : △ABC) = 4 cot B)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.13] <II.13>`, :just:`[VI.1] <VI.1>`

Let $\\triangle ABC$ have the acute angle $\angle ABC$ given, and from $A$ let $AD$ be drawn perpendicular to $BC$ (:just:`[I.12] <I.12>`). I say that the defect $((AB^2 + BC^2) - AC^2)$ by which $AC^2$ falls short of $AB^2 + BC^2$ has a given ratio to the rectangle $AB \cdot BC$.

In right-angled $\\triangle ABD$, the acute angle $\angle ABD$ ($= \angle ABC$) is given and $\angle ADB = 1\\text{ rt.}$, so $\\triangle ABD$ is given in species (:just:`[Data 40] <D.40>`). Hence the ratio $AB : BD$ is given (:just:`[Data Def. 3] <D.def.3>`). Multiplying both terms by $BC$ (:just:`[VI.1] <VI.1>`), the ratio $(AB \cdot BC) : (CB \cdot BD)$ is given, and hence $(2\, CB \cdot BD) : (AB \cdot BC)$ is given (:just:`[Data 8] <D.8>`). Yet by the acute-triangle Pythagorean identity (:just:`[II.13] <II.13>`), $AC^2 + 2\, CB \cdot BD = AB^2 + BC^2$, so the defect $(AB^2 + BC^2) - AC^2$ equals $2\, CB \cdot BD$. Therefore that defect has a given ratio ($= 2\, BD : AB = 2\cos\angle ABC$) to $AB \cdot BC$.

.. _D.66:

Proposition 66 [ξϛ΄ · Prop. LXII Cor.]
--------------------------------------

.. folio:: Menge 120
   :page: 120

.. enunciation::

   If a triangle have a given angle, the rectangle contained by the straight lines containing the given angle has a given ratio to the triangle.

*Functional Signature*: ``Given(Angle A) -> Determined(Ratio((AB * AC) : Area(△ABC)) = 2 / sin A)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.1] <VI.1>`

Let $\\triangle ABC$ have a given angle $\angle ABC$. I say that the rectangle $AB \cdot BC$ contained by the sides about the given angle has a given ratio to the area of $\\triangle ABC$.

From $A$ drop $AD$ perpendicular to $BC$ (or $BC$ produced) (:just:`[I.12] <I.12>`). Because $\angle ABC$ is given, $\angle ABD$ is given (either directly if acute, or as $2\\text{ rt.} - \angle ABC$ if obtuse by :just:`[Data 4] <D.4>`; if $\angle ABC$ is right, $AD = AB$ immediately). Hence right-angled $\\triangle ABD$ is given in species (:just:`[Data 40] <D.40>`), so the ratio $AB : AD$ is given (:just:`[Data Def. 3] <D.def.3>`). Multiplying both terms by $BC$ (:just:`[VI.1] <VI.1>`), $(AB \cdot BC) : (AD \cdot BC)$ is given. Yet the rectangle $AD \cdot BC$ is double the area of $\\triangle ABC$ (:just:`[I.41] <I.41>`), so $(AD \cdot BC) : \\triangle ABC = 2 : 1$ is given. *Ex aequali*, the ratio $(AB \cdot BC) : \\triangle ABC$ ($= 2/\sin\angle ABC$) is given (:just:`[Data 8] <D.8>`).

.. _D.67:

Proposition 67 [ξζ΄ · Prop. LXXVI]
----------------------------------

.. enunciation::

   If a triangle have a given angle, then that area by which the square on both the sides containing the given angle taken together as one exceeds the square on the remaining side will have a given ratio to the triangle.

*Functional Signature*: ``Given(Angle A) -> Determined(Ratio(((b + c)^2 - a^2) : △ABC) = 4*(1 + cos A) / sin A)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 50] <D.50>`, :just:`[Data 66] <D.66>`, :just:`[I.5] <I.5>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`, :just:`[I.32] <I.32>`, :just:`[II.6] <II.6>`, :just:`[VI.2] <VI.2>`, :just:`[VI.16] <VI.16>`

Let $\\triangle ABC$ have a given angle $\angle BAC$. I say that the excess $((BA + AC)^2 - BC^2)$ by which the square on the compound $(BA + AC)$ exceeds the square on $BC$ has a given ratio to the area of $\\triangle ABC$.

Produce $BA$ to $D$ so that $AD = AC$ (:just:`[I.3] <I.3>`), making $BD = BA + AC$; join $DC$, and through $B$ draw $BE$ parallel to $DC$ meeting $CA$ produced at $E$ (:just:`[I.31] <I.31>`). Because $AD = AC$ and $DC \parallel BE$, by parallels $BA : AD = EA : AC$ (:just:`[VI.2] <VI.2>`), whence $EA = BA$ and $EC = BA + AC = BD$, while in $\\triangle BDC$ and $\\triangle BCE$ the secant-product and cosine relations (:just:`[II.6] <II.6>`, :just:`[Data 64] <D.64>`–:just:`[Data 65] <D.65>`) express $(BA + AC)^2 - BC^2 = (AB^2 + AC^2 - BC^2) + 2\, AB \cdot AC$ in a given ratio to the rectangle $AB \cdot AC$. Yet since $\angle BAC$ is given, the rectangle $AB \cdot AC$ has a given ratio to $\\triangle ABC$ (:just:`[Data 66] <D.66>`). *Ex aequali*, the excess $((BA + AC)^2 - BC^2)$ has a given ratio ($= 4\cot\frac{1}{2}\angle BAC$) to $\\triangle ABC$ (:just:`[Data 8] <D.8>`).
