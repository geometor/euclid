:order: 30
:type: chapter
:canonical_id: D.unit.3
:folio: Menge pp. 66–98
:book: Propositions 39–55: Triangles & Species
:description: Constructive determination of triangles up to similarity (εἴδει) from SSS-ratios (D.39), AAA (D.40), SAS-ratio (D.41), side-ratios (D.42), right-SSA (D.43), general SSA bifurcation with obtuse/acute diorismos (D.44), sum/difference of sides (D.45–D.46), decomposing rectilinear polygons into triangles (D.47), and quadratic area-scaling of figures given in species (D.48–D.55).

.. _data-unit-3-en:

==================================================================
Unit 3: Triangles & Polygons Given in Species (Propositions 39–55)
==================================================================

*Similarity Invariants, Triangle Rigidity Criteria, and Area-to-Side Scaling* — **D.39–D.55 (Simson XLII–LX) · Menge (1896) pp. 66–98**

.. note::

   **Edition Track (English)**: Constructive determination of triangles up to similarity (εἴδει) from SSS-ratios (D.39), AAA (D.40), SAS-ratio (D.41), side-ratios (D.42), right-SSA (D.43), general SSA bifurcation with obtuse/acute diorismos (D.44), sum/difference of sides (D.45–D.46), decomposing rectilinear polygons into triangles (D.47), and quadratic area-scaling of figures given in species (D.48–D.55). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. picture:: /_static/figures/data_03_triangle_species.svg
   :alt: Triangle Species Determination (D.39–D.43) vs. SSA Two-Root Bifurcation (D.44)

Interactive species diagram (:cite:`Menge pp. 66–82 <menge:1896>`): Left panel illustrates unique species determination (:ref:`D.39 <D.39>`–:ref:`D.42 <D.42>`), pairing similar triangles :g:`DEF <data_03_triangle_species:< D E F >>` and :g:`GHK <data_03_triangle_species:< G H K >>` with :eq:`equal vertex angles <data_03_triangle_species:< E D F ) = data_03_triangle_species:< H G K )>` :g:`∠EDF <data_03_triangle_species:< E D F )>` and :g:`∠HGK <data_03_triangle_species:< H G K )>` and proportional sides :g:`DE <data_03_triangle_species:/ D E />` to :g:`GH <data_03_triangle_species:/ G H />`. Right panel illustrates the **SSA two-root bifurcation** (:ref:`D.44 <D.44>`): given angle :g:`∠CAB <data_03_triangle_species:< C2 A B )>` at :g:`A <data_03_triangle_species:A>` and side ratio :g:`AB <data_03_triangle_species:/ A B />` to radius :g:`BC₁ <data_03_triangle_species:/ B C1 />`, circle :g:`(B, BC₁) <data_03_triangle_species:( B C1 )>` cuts ray :g:`AC₂ <data_03_triangle_species:/ A C2 />` in :eq:`equal radii <data_03_triangle_species:/ B C1 / = data_03_triangle_species:/ B C2 />` at obtuse solution :g:`C₁ <data_03_triangle_species:C1>` and acute solution :g:`C₂ <data_03_triangle_species:C2>` symmetric across altitude :g:`BP <data_03_triangle_species:/ B P />` (foot :g:`P <data_03_triangle_species:P>`).

.. _D.39:

Proposition 39 [λθ΄ · Prop. XLII]
---------------------------------

.. folio:: Menge 66
   :page: 66

.. enunciation::

   If each of the sides of a triangle be given in magnitude, the triangle is given in species.

*Functional Signature*: ``Given(Mag(a), Mag(b), Mag(c)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 1] <D.1>`, :just:`[I.8] <I.8>`, :just:`[I.22] <I.22>`

Let each of the sides $AB, BC, CA$ of $\triangle ABC$ be given in magnitude. I say that $\triangle ABC$ is :term:`given in species <eidei>`.

Set out a straight line $DM$ given in position from a given endpoint $D$, and cut off $DE = AB$ (:just:`[I.3] <I.3>`), so $DE$ is given in magnitude and $E$ is given in position (:just:`[Data 27] <D.27>`). Similarly procure segments equal to $BC$ and $CA$, and on $DE$ construct $\triangle DEH$ with $EH = BC$ and $DH = CA$ (:just:`[I.22] <I.22>`): the circles $(E, BC)$ and $(D, CA)$ are both given in position (:just:`[Data Def. 6] <D.def.6>`), so their intersection $H$ (on an assigned side of $DE$) is given in position (:just:`[Data 25] <D.25>`), and the sides $DH, EH$ are given in position and magnitude (:just:`[Data 26] <D.26>`). Thus every angle and side-ratio of $\triangle DEH$ is given (:just:`[Data 1] <D.1>`). By :just:`[I.8] <I.8>` and :just:`[I.4] <I.4>`, $\triangle ABC \cong \triangle DEH$, whence all angles and side-ratios of $\triangle ABC$ are given; therefore $\triangle ABC$ is given in species (:just:`[Data Def. 3] <D.def.3>`).

.. _D.40:

Proposition 40 [μ΄ · Prop. XLIII]
---------------------------------

.. enunciation::

   If each of the angles of a triangle be given in magnitude, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Angle(B), Angle(C)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[I.32] <I.32>`, :just:`[VI.4] <VI.4>`

Let each of the angles $\angle ABC, \angle BCA, \angle CAB$ of $\triangle ABC$ be given in magnitude. I say that $\triangle ABC$ is given in species.

Set out a straight line $DE$ given in position and magnitude (:just:`[Data 26] <D.26>`). At the given points $D$ and $E$ on $DE$, draw straight lines $DF$ and $EF$ making $\angle EDF = \angle BAC$ and $\angle DEF = \angle ABC$ (:just:`[I.23] <I.23>`). Since $\angle EDF$ and $\angle DEF$ are given, the rays $DF$ and $EF$ are given in position (:just:`[Data 29] <D.29>`), so their intersection $F$ is given in position (:just:`[Data 25] <D.25>`). Therefore $DF$ and $EF$ are given in magnitude (:just:`[Data 26] <D.26>`), and $\triangle DEF$ has given pairwise side ratios (:just:`[Data 1] <D.1>`). By :just:`[I.32] <I.32>`, the remaining angle $\angle DFE = \angle ACB$, so $\triangle ABC$ is equiangular with $\triangle DEF$ and its sides are proportional to those of $\triangle DEF$ (:just:`[VI.4] <VI.4>`). Since all angles and side ratios of $\triangle ABC$ are given, $\triangle ABC$ is given in species (:just:`[Data Def. 3] <D.def.3>`).

.. _D.41:

Proposition 41 [μα΄ · Prop. XLIV]
---------------------------------

.. enunciation::

   If a triangle have one angle given, and the sides about the given angle have a given ratio to one another, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Ratio(c : b)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[VI.6] <VI.6>`

Let $\triangle ABC$ have one given angle $\angle BAC$, and let the sides $AB$ and $AC$ about the given angle have a given ratio $AB : AC$. I say that $\triangle ABC$ is given in species.

Set out a straight line $DE$ given in position and magnitude. At the given point $D$ on $DE$, draw $DF$ making $\angle EDF = \angle BAC$ (:just:`[I.23] <I.23>`); since $\angle BAC$ is given, $DF$ is given in position (:just:`[Data 29] <D.29>`). Make $DE : DF = AB : AC$ (:just:`[Data Def. 2] <D.def.2>`); since $DE$ is given and $AB : AC$ is given, $DF$ is given in magnitude (:just:`[Data 2] <D.2>`), whence $F$ is given in position (:just:`[Data 27] <D.27>`). Join $EF$: then $EF$ is given in position and magnitude (:just:`[Data 26] <D.26>`), so $\triangle DEF$ is given in species (:just:`[Data 39] <D.39>`). Because $\angle BAC = \angle EDF$ and $AB : AC = DE : DF$, $\triangle ABC \sim \triangle DEF$ (:just:`[VI.6] <VI.6>`). Therefore $\triangle ABC$ is also given in species (:just:`[Data Def. 3] <D.def.3>`).

.. _D.42:

Proposition 42 [μβ΄ · Prop. XLV]
--------------------------------

.. folio:: Menge 74
   :page: 74

.. enunciation::

   If the sides of a triangle have given ratios to one another, the triangle is given in species.

*Functional Signature*: ``Given(Ratio(a : b), Ratio(b : c)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 39] <D.39>`, :just:`[I.20] <I.20>`, :just:`[I.22] <I.22>`, :just:`[VI.5] <VI.5>`

Let the three sides $AB, BC, CA$ of $\triangle ABC$ have given ratios to one another. I say that $\triangle ABC$ is given in species.

Set out a given straight line $D$. Make $D : E = AB : BC$ and $D : F = AB : AC$ (:just:`[Data Def. 2] <D.def.2>`). Since $D$ is given and both ratios are given, $E$ and $F$ are given in magnitude (:just:`[Data 2] <D.2>`). Because $AB, BC, CA$ satisfy the triangle inequality (:just:`[I.20] <I.20>`) and $D, E, F$ are proportional to $AB, BC, CA$ (:just:`[Data 8] <D.8>`), any two of $D, E, F$ are greater than the remaining one; construct $\triangle GHK$ from sides $GH = D$, $HK = E$, $KG = F$ (:just:`[I.22] <I.22>`). Since each side of $\triangle GHK$ is given in magnitude, $\triangle GHK$ is given in species (:just:`[Data 39] <D.39>`). Because $AB : BC : CA = GH : HK : KG$, $\triangle ABC$ is equiangular and similar to $\triangle GHK$ (:just:`[VI.5] <VI.5>`), and therefore $\triangle ABC$ is given in species (:just:`[Data Def. 3] <D.def.3>`).

.. _D.43:

Proposition 43 [μγ΄ · Prop. XLVI]
---------------------------------

.. folio:: Menge 76
   :page: 76

.. enunciation::

   If of a right-angled triangle the sides about one of the acute angles have a given ratio to one another, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A) = pi/2, Ratio(hypotenuse c : leg b)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.47] <I.47>`, :just:`[VI.7] <VI.7>`

Let $\triangle ABC$ be right-angled at $A$ ($\angle BAC = 1\text{ rt.}$), and let the sides $BC$ and $BA$ about one of the other angles $\angle ABC$ have a given ratio $BC : BA$. I say that $\triangle ABC$ is given in species.

Set out a straight line $DE$ given in position and magnitude, and on diameter $DE$ describe the semicircle $DGE$ (:just:`[Post. 3] <I.post.3>`), whose centre (the midpoint of $DE$, :just:`[Data 7] <D.7>`, :just:`[Data 27] <D.27>`) and radius are given, so the semicircle $DGE$ is given in position (:just:`[Data Def. 6] <D.def.6>`). Make $DE : F = BC : BA$ (:just:`[Data Def. 2] <D.def.2>`); since $DE$ is given and $BC : BA$ is given (with $BC > BA$ by :just:`[I.19] <I.19>`), $F$ is given in magnitude (:just:`[Data 2] <D.2>`) and $F < DE$. With centre $D$ and radius $DG = F$, describe a circle meeting the semicircle $DGE$ at the unique point $G$ (:just:`[Data 25] <D.25>`), and join $DG, GE$ (:just:`[Data 26] <D.26>`). Then $\triangle DGE$ is given in species (:just:`[Data 39] <D.39>`) and $\angle DGE$ in the semicircle is right (:just:`[III.31] <III.31>`). In $\triangle ABC$ and $\triangle DGE$, $\angle BAC = \angle DGE = 1\text{ rt.}$, $BC : BA = DE : DG$, and the angles $\angle ACB, \angle DEG$ opposite $BA, DG$ are both acute (:just:`[I.17] <I.17>`); hence $\triangle ABC \sim \triangle DGE$ (:just:`[VI.7] <VI.7>`), so $\triangle ABC$ is given in species.

.. _D.44:

Proposition 44 [μδ΄ · Prop. XLVII]
----------------------------------

.. folio:: Menge 78
   :page: 78

.. enunciation::

   If a triangle have one angle given, and the sides about another angle have a given ratio to one another, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Ratio(AB : BC), Sign(cos C)) -> Determined(Species(Triangle ABC)) [SSA diorismos]`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.13] <I.13>`, :just:`[VI.7] <VI.7>`

Let $\triangle ABC$ have one given angle $\angle ABC$, and let the sides $AB$ and $AC$ about another angle $\angle BAC$ have a given ratio $AB : AC$—*assuming the specification (diorismos) whether $\angle ACB$ is obtuse or acute is fixed*. I say that $\triangle ABC$ is given in species.

From $A$ drop $AD$ perpendicular to $BC$ (or $BC$ produced) (:just:`[I.12] <I.12>`). In right-angled $\triangle ABD$, $\angle ADB = 1\text{ rt.}$ and $\angle ABD$ (or its supplement) is given, so all angles of $\triangle ABD$ are given (:just:`[I.32] <I.32>`), whence $\triangle ABD$ is given in species (:just:`[Data 40] <D.40>`). Therefore the ratio $BA : AD$ is given (:just:`[Data Def. 3] <D.def.3>`). Yet the ratio $CA : AB$ is given by hypothesis; *ex aequali*, the ratio $CA : AD$ is given (:just:`[Data 8] <D.8>`). Now $\triangle ADC$ is right-angled at $D$ with the ratio of hypotenuse $CA$ to leg $AD$ given; hence $\triangle ADC$ is given in species (:just:`[Data 43] <D.43>`), so the acute angle $\angle ACD$ is given! Depending on the single branch specified (whether $D$ falls on $BC$ with $\angle ACB$ acute, or on $BC$ produced with $\angle ACB = 2\text{ rt.} - \angle ACD$ obtuse), $\angle ACB$ is uniquely given. Together with given $\angle ABC$, all angles of $\triangle ABC$ are given (:just:`[I.32] <I.32>`), so $\triangle ABC$ is given in species (:just:`[Data 40] <D.40>`).

.. _D.45:

Proposition 45 [με΄ · Prop. XLVIII]
-----------------------------------

.. folio:: Menge 82
   :page: 82

.. enunciation::

   If a triangle have one angle given, and both the sides together about the given angle have a given ratio to the remaining side, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Ratio((b + c) : a)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data 40] <D.40>`, :just:`[Data 44] <D.44>`, :just:`[I.5] <I.5>`, :just:`[I.32] <I.32>`

Let $\triangle ABC$ have one given angle $\angle BAC$, and let the compound $(BA + AC)$ of the two sides about the given angle have a given ratio to the remaining side $BC$. I say that $\triangle ABC$ is given in species.

Bisect $\angle BAC$ by the straight line $AD$ meeting $BC$ at $D$ (:just:`[I.9] <I.9>`). Since $\angle BAC$ is given, its half $\angle BAD$ is given (:just:`[Data 7] <D.7>`). Because $AD$ bisects $\angle BAC$, $BA : AC = BD : DC$ (:just:`[VI.3] <VI.3>`). *Alternando* $BA : BD = AC : DC$ (:just:`[V.16] <V.16>`), and *componendo* $(BA + AC) : BC = BA : BD$ (:just:`[V.12] <V.12>`). Since $(BA + AC) : BC$ is given by hypothesis, the ratio $BA : BD$ is given. Applying :just:`[Data 44] <D.44>` to $\triangle ABD$ (with given angle $\angle BAD$ and given ratio $BA : BD$, up to the symmetric interchange of $AB$ and $AC$) determines $\triangle ABD$ in species, whence $\angle ABD$ is given; together with given $\angle BAC$, $\triangle ABC$ is given in species (:just:`[Data 40] <D.40>`).

.. _D.46:

Proposition 46 [μϛ΄ · Prop. XLIX]
---------------------------------

.. folio:: Menge 84
   :page: 84

.. enunciation::

   If a triangle have one angle given, and the sides together about another angle have a given ratio to the remaining side, the triangle is given in species.

*Functional Signature*: ``Given(Angle(B), Ratio((c + b) : a)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data 40] <D.40>`, :just:`[Data 41] <D.41>`, :just:`[I.5] <I.5>`, :just:`[I.9] <I.9>`, :just:`[I.32] <I.32>`

Let $\triangle ABC$ have one given angle $\angle ABC$, and let the compound $(BA + AC)$ of the sides about another angle $\angle BAC$ have a given ratio to the remaining side $BC$. I say that $\triangle ABC$ is given in species.

Bisect $\angle BAC$ by $AD$ meeting $BC$ at $D$ (:just:`[I.9] <I.9>`). Since $BA : AC = BD : DC$ (:just:`[VI.3] <VI.3>`), *alternando* and *componendo* $(BA + AC) : BC = AB : BD$ (:just:`[V.16] <V.16>`, :just:`[V.12] <V.12>`). Because $(BA + AC) : BC$ is given, the ratio $AB : BD$ is given. Now in $\triangle ABD$, the given angle $\angle ABD$ ($= \angle ABC$) is itself the included angle between $AB$ and $BD$; therefore $\triangle ABD$ is uniquely given in species (:just:`[Data 41] <D.41>`). Hence $\angle BAD$ is given, its double $\angle BAC$ is given (:just:`[Data 3] <D.3>`), and from given $\angle ABC$ and $\angle BAC$ the triangle $\triangle ABC$ is given in species (:just:`[Data 40] <D.40>`).

.. _D.47:

Proposition 47 [μζ΄ · Prop. LI]
-------------------------------

.. enunciation::

   Rectilineal figures given in species are divided into triangles given in species.

*Functional Signature*: ``Given(Species(n-gon P)) -> Determined(Species(ear-triangulation T_1 .. T_{n-2}))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[Data 41] <D.41>`, :just:`[I.32] <I.32>`, :just:`[VI.20] <VI.20>`

Rectilinear figures given in species are divided into triangles given in species. Let the polygon $ABCDE$ be given in species (:just:`[Data Def. 3] <D.def.3>`). I say that $ABCDE$ is divided into triangles given in species.

Join the diagonals $BE$ and $EC$ (:just:`[Post. 1] <I.post.1>`). Since $ABCDE$ is given in species, the angle $\angle BAE$ is given and the ratio $BA : AE$ is given (:just:`[Data Def. 3] <D.def.3>`). Therefore $\triangle BAE$ is given in species (:just:`[Data 41] <D.41>`), whence $\angle ABE$ is given and the ratio $AB : BE$ is given. Subtracting given $\angle ABE$ from the given polygon angle $\angle ABC$ leaves $\angle EBC$ given (:just:`[Data 4] <D.4>`). Moreover, since $EB : BA$ is given and $AB : BC$ is given (:just:`[Data Def. 3] <D.def.3>`), the ratio $EB : BC$ is given (:just:`[Data 8] <D.8>`). Thus $\triangle EBC$ has given angle $\angle EBC$ and given ratio $EB : BC$, so $\triangle EBC$ is given in species (:just:`[Data 41] <D.41>`). For the very same reason $\triangle ECD$ is also given in species; therefore $ABCDE$ has been partitioned into triangles given in species.

.. _D.48:

Proposition 48 [μη΄ · Prop. LII]
--------------------------------

.. enunciation::

   If on the same straight line two triangles given in species be described, they will have a given ratio to one another.

*Functional Signature*: ``Given(Species(△ABC), Species(△ABD), SharedBase(AB)) -> Determined(Ratio(△ABC : △ABD))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.37] <I.37>`, :just:`[VI.1] <VI.1>`, :just:`[VI.4] <VI.4>`

On the same straight line $AB$, let two triangles $\triangle ABC$ and $\triangle ABD$ given in species be described. I say that $\triangle ABC$ has a given ratio to $\triangle ABD$.

Through $A$ draw $AE$ perpendicular to $AB$ (:just:`[I.11] <I.11>`), and through $C$ and $D$ draw $CE$ and $DF$ parallel to $AB$ meeting the line $AE$ (produced as needed) at $E$ and $F$ (:just:`[I.31] <I.31>`). Since $\triangle ABC$ is given in species, dropping altitude $CG \perp AB$ (with $CG = AE$ by :just:`[I.34] <I.34>`) gives right-angled $\triangle AGC$ in species (:just:`[Data 40] <D.40>`), so the ratio $AE : AB$ ($= CG : AB$ via $CG : AC$ and $AC : AB$, :just:`[Data 8] <D.8>`) is given. For the same reason, since $\triangle ABD$ is given in species, the ratio $AB : AF$ is given. Combining $AE : AB$ and $AB : AF$ yields $AE : AF$ given (:just:`[Data 8] <D.8>`). Yet triangles $\triangle ABC$ and $\triangle ABD$ on the same base $AB$ are to one another as their altitudes $AE$ and $AF$ (specifically, completing parallelograms $ABHE$ and $ABKF$, $\triangle ABC : \triangle ABD = \square ABHE : \square ABKF = AE : AF$ by :just:`[I.41] <I.41>` and :just:`[VI.1] <VI.1>`). Therefore the ratio $\triangle ABC : \triangle ABD$ is given (:just:`[Data Def. 2] <D.def.2>`).

.. _D.49:

Proposition 49 [μθ΄ · Prop. LIII]
---------------------------------

.. folio:: Menge 88
   :page: 88

.. enunciation::

   If on the same straight line any two rectilineal figures given in species be described, they will have a given ratio to one another.

*Functional Signature*: ``Given(Species(P1 on AB), Species(P2 on AB)) -> Determined(Ratio(Area(P1) : Area(P2)))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 22] <D.22>`, :just:`[Data 47] <D.47>`, :just:`[Data 48] <D.48>`, :just:`[VI.20] <VI.20>`

On the same straight line $AB$, let any two rectilinear figures $ABCDE$ and $ABFG$ given in species be described. I say that $ABCDE$ has a given ratio to $ABFG$.

Divide each figure into triangles given in species by drawing diagonals from $A$ and $B$, say $ABCDE = \triangle ABE + \triangle EBC + \triangle ECD$ and $ABFG = \triangle ABF + \triangle AFG$ (:just:`[Data 47] <D.47>`). Because similar polygons and species-given sub-triangles on chained diagonals have given side-squared ratios (:just:`[VI.19] <VI.19>`), $\triangle ECD : \triangle EBC$ and $\triangle EBC : \triangle ABE$ are given, so by *componendo* (:just:`[Data 6] <D.6>`, :just:`[Data 22] <D.22>`) the whole polygon $ABCDE$ has a given ratio to the base triangle $\triangle ABE$. For the same reason $ABFG$ has a given ratio to $\triangle ABF$. Yet $\triangle ABE$ and $\triangle ABF$ are two species-given triangles on the *same* straight line $AB$, so $\triangle ABE : \triangle ABF$ is given (:just:`[Data 48] <D.48>`). Chaining $ABCDE : \triangle ABE$, $\triangle ABE : \triangle ABF$, and $\triangle ABF : ABFG$ via :just:`[Data 8] <D.8>` proves that $ABCDE : ABFG$ is given.

.. _D.50:

Proposition 50 [ν΄ · Prop. LIV]
-------------------------------

.. enunciation::

   If two straight lines have a given ratio to one another, the rectilineal figures similar and similarly described upon them will also have a given ratio to one another.

*Functional Signature*: ``Given(Ratio(AB : CD) = r, Similar(E, F)) -> Determined(Ratio(Area(E) : Area(F)) = r^2)`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.11] <VI.11>`, :just:`[VI.19] <VI.19>`, :just:`[VI.20] <VI.20>`

Let two straight lines $AB$ and $CD$ have a given ratio $AB : CD$, and on them let similar and similarly situated rectilinear figures $E$ and $F$ be described. I say that $E$ has a given ratio to $F$.

Take the third proportional $G$ to $AB$ and $CD$, so that $AB : CD = CD : G$ (:just:`[VI.11] <VI.11>`). Since $AB : CD$ is given, $CD : G$ is given; hence *ex aequali* $AB : G$ is given (:just:`[Data 8] <D.8>`). Yet because $E$ and $F$ are similar and similarly situated rectilinear figures on $AB$ and $CD$, $E$ has to $F$ the duplicate ratio of $AB$ to $CD$, namely $E : F = AB : G$ (:just:`[VI.19] <VI.19>` Cor., :just:`[VI.20] <VI.20>` Cor.). Since $AB : G$ is given, the ratio $E : F$ is given (:just:`[Data Def. 2] <D.def.2>`).

.. _D.51:

Proposition 51 [να΄ · Prop. LV]
-------------------------------

.. folio:: Menge 92
   :page: 92

.. enunciation::

   If two straight lines have a given ratio to one another, and upon them be described any rectilineal figures given in species, those figures will have a given ratio to one another.

*Functional Signature*: ``Given(Ratio(AB : CD), Species(E), Species(F)) -> Determined(Ratio(Area(E) : Area(F)))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 49] <D.49>`, :just:`[Data 50] <D.50>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`

Let two straight lines $AB$ and $CD$ have a given ratio $AB : CD$, and on them let *any* two rectilinear figures $E$ (on $AB$) and $F$ (on $CD$), each given in species, be described. I say that $E$ has a given ratio to $F$.

On $AB$ describe a rectilinear figure $G$ similar and similarly situated to $F$ (:just:`[VI.18] <VI.18>`). Because $F$ is given in species and $G \sim F$, $G$ is also given in species (:just:`[Data Def. 3] <D.def.3>`). Now $E$ and $G$ are two rectilinear figures given in species described on the *same* straight line $AB$; therefore the ratio $E : G$ is given (:just:`[Data 49] <D.49>`). Moreover, $G$ and $F$ are similar and similarly situated figures described on $AB$ and $CD$, which have the given ratio $AB : CD$; therefore the ratio $G : F$ is given (:just:`[Data 50] <D.50>`). Combining $E : G$ and $G : F$ yields $E : F$ given (:just:`[Data 8] <D.8>`).

.. _D.52:

Proposition 52 [νβ΄ · Prop. LVI]
--------------------------------

.. folio:: Menge 94
   :page: 94

.. enunciation::

   If on a straight line given in magnitude a rectilineal figure given in species be described, it is given in magnitude.

*Functional Signature*: ``Given(Mag(AB), Species(P on AB)) -> Determined(Mag(Area(P)))`` · *Dependencies*: :just:`[Data Def. 1] <D.def.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`

On a straight line $AB$ given in magnitude, let a rectilinear figure $ACDEB$ given in species be described. I say that $ACDEB$ is given in magnitude.

On $AB$ describe the square $AFGB$ (:just:`[I.46] <I.46>`). Because all angles of a square are right and all its sides are equal ($1:1$), the square $AFGB$ is given in species (:just:`[Data Def. 3] <D.def.3>`), and since $AB$ is given in magnitude, the square $AFGB$ is directly constructible equal to itself and so is given in magnitude (:just:`[Data Def. 1] <D.def.1>`). Now $ACDEB$ and $AFGB$ are two figures given in species on the same straight line $AB$; hence the ratio $ACDEB : AFGB$ is given (:just:`[Data 49] <D.49>`). Because $AFGB$ is given in magnitude, $ACDEB$ is also given in magnitude (:just:`[Data 2] <D.2>`).

.. _D.53:

Proposition 53 [νγ΄ · Prop. LVII]
---------------------------------

.. enunciation::

   If two figures be given in species, and one side of one have a given ratio to one side of the other, the remaining sides will also have given ratios to the remaining sides.

*Functional Signature*: ``Given(Species(A), Species(B), Ratio(s1(A) : s1(B))) -> Determined(Ratio(si(A) : sj(B)))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[V.22] <V.22>`

Let two rectilinear figures $A$ and $B$ be given in species, and let two sides—say $CD$ of $A$ and $EF$ of $B$—have a given ratio $CD : EF$. I say that the remaining sides also have given ratios to the remaining sides.

Let $GH$ be any other side of $A$ and $KL$ any other side of $B$. Since $A$ is given in species, the ratio of its own sides $GH : CD$ is given (:just:`[Data Def. 3] <D.def.3>`). By hypothesis, the ratio $CD : EF$ is given. And since $B$ is given in species, the ratio $EF : KL$ is given (:just:`[Data Def. 3] <D.def.3>`). Chaining $GH : CD$, $CD : EF$, and $EF : KL$ via :just:`[Data 8] <D.8>` proves that the ratio $GH : KL$ is given.

.. _D.54:

Proposition 54 [νδ΄ · Prop. LIX]
--------------------------------

.. enunciation::

   If two figures given in species have a given ratio to one another, their sides will also have a given ratio to one another.

*Functional Signature*: ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(si(A) : sj(B)))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 49] <D.49>`, :just:`[Data 53] <D.53>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`

Let two rectilinear figures $A$ (on side $CD$) and $B$ (on side $EF$) be given in species, and let the area ratio $A : B$ be given. I say that their sides also have given ratios to one another.

First, if $A$ and $B$ are similar, take the third proportional $G$ to $CD$ and $EF$ so $CD : EF = EF : G$ (:just:`[VI.11] <VI.11>`). Then $CD : G = A : B$ (:just:`[VI.20] <VI.20>` Cor.), which is given! Thus three straight lines $CD, EF, G$ are in continued proportion and the first $CD$ has a given ratio to the third $G$; by :just:`[Data 24] <D.24>`, $CD$ has a given ratio to the second $EF$. Next, if $A$ and $B$ are not similar, on $CD$ describe a figure $H$ similar and similarly situated to $B$ (:just:`[VI.18] <VI.18>`), so $H$ is given in species. On the same side $CD$, $A : H$ is given (:just:`[Data 49] <D.49>`); combining with given $A : B$ gives $H : B$ given (:just:`[Data 8] <D.8>`). Since $H \sim B$ on corresponding sides $CD$ and $EF$, the first case yields $CD : EF$ given, and :just:`[Data 53] <D.53>` gives the ratios of all remaining sides.

.. _D.55:

Proposition 55 [νε΄ · Prop. LX]
-------------------------------

.. folio:: Menge 98
   :page: 98

.. enunciation::

   If an area be given in species and in magnitude, its sides will also be given in magnitude.

*Functional Signature*: ``Given(Species(A), Mag(Area(A))) -> Determined(Mag(sides(A)))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 52] <D.52>`, :just:`[Data 54] <D.54>`, :just:`[I.46] <I.46>`, :just:`[VI.18] <VI.18>`

Let a rectilinear figure $A$ be given both in species and in magnitude. I say that its sides are also given in magnitude.

Let $BC$ be a side of $A$. Set out a straight line $DE$ given in magnitude, and on $DE$ describe a rectilinear figure $F$ similar and similarly situated to $A$ (:just:`[VI.18] <VI.18>`). Since $A$ is given in species, $F$ is also given in species (:just:`[Data Def. 3] <D.def.3>`); and since $F$ is described on the given straight line $DE$, $F$ is given in magnitude (:just:`[Data 52] <D.52>`). Because both $A$ and $F$ are given in magnitude, their ratio $A : F$ is given (:just:`[Data 1] <D.1>`). Therefore, by :just:`[Data 54] <D.54>`, their homologous sides have a given ratio $BC : DE$. Since $DE$ is given in magnitude, $BC$ is given in magnitude (:just:`[Data 2] <D.2>`), and since $A$ is given in species all remaining sides have given ratios to $BC$ and so are given in magnitude (:just:`[Data 2] <D.2>`).
