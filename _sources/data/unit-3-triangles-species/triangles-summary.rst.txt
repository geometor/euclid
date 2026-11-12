:order: 32
:type: summary
:canonical_id: D.unit.3
:folio: Menge pp. 66–98
:book: Propositions 39–55: Triangles & Species

.. _data-unit-3-summary:

=======================================================================================
Unit 3: Triangles & Polygons Given in Species (Propositions 39–55) — Analytical Summary
=======================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Constructive determination of triangles up to similarity (εἴδει) from SSS-ratios (D.39), AAA (D.40), SAS-ratio (D.41), side-ratios (D.42), right-SSA (D.43), general SSA bifurcation with obtuse/acute diorismos (D.44), sum/difference of sides (D.45–D.46), decomposing rectilinear polygons into triangles (D.47), and quadratic area-scaling of figures given in species (D.48–D.55).

* **Scope**: 17 propositions (D.39–D.55 (Simson XLII–LX), *Menge* pp. 66–98).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Conspectus (D.39–D.55 (Simson XLII–LX))
--------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 12 38 28 12

   * - ID
     - Simson
     - Functional Signature
     - Key Dependencies
     - Tracks
   * - :ref:`D.39 <D.39>`
     - Prop. XLII
     - ``Given(Mag(a), Mag(b), Mag(c)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 1] <D.1>`, :just:`[I.8] <I.8>`, :just:`[I.22] <I.22>`
     - :ref:`EN <D.39>` · :ref:`EL <D.39.el>`
   * - :ref:`D.40 <D.40>`
     - Prop. XLIII
     - ``Given(Angle(A), Angle(B), Angle(C)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[I.32] <I.32>`, :just:`[VI.4] <VI.4>`
     - :ref:`EN <D.40>` · :ref:`EL <D.40.el>`
   * - :ref:`D.41 <D.41>`
     - Prop. XLIV
     - ``Given(Angle(A), Ratio(c : b)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[VI.6] <VI.6>`
     - :ref:`EN <D.41>` · :ref:`EL <D.41.el>`
   * - :ref:`D.42 <D.42>`
     - Prop. XLV
     - ``Given(Ratio(a : b), Ratio(b : c)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 39] <D.39>`, :just:`[I.20] <I.20>`, :just:`[I.22] <I.22>`, :just:`[VI.5] <VI.5>`
     - :ref:`EN <D.42>` · :ref:`EL <D.42.el>`
   * - :ref:`D.43 <D.43>`
     - Prop. XLVI
     - ``Given(Angle(A) = pi/2, Ratio(hypotenuse c : leg b)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.47] <I.47>`, :just:`[VI.7] <VI.7>`
     - :ref:`EN <D.43>` · :ref:`EL <D.43.el>`
   * - :ref:`D.44 <D.44>`
     - Prop. XLVII
     - ``Given(Angle(A), Ratio(AB : BC), Sign(cos C)) -> Determined(Species(Triangle ABC)) [SSA diorismos]``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.13] <I.13>`, :just:`[VI.7] <VI.7>`
     - :ref:`EN <D.44>` · :ref:`EL <D.44.el>`
   * - :ref:`D.45 <D.45>`
     - Prop. XLVIII
     - ``Given(Angle(A), Ratio((b + c) : a)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data 40] <D.40>`, :just:`[Data 44] <D.44>`, :just:`[I.5] <I.5>`, :just:`[I.32] <I.32>`
     - :ref:`EN <D.45>` · :ref:`EL <D.45.el>`
   * - :ref:`D.46 <D.46>`
     - Prop. XLIX
     - ``Given(Angle(B), Ratio((c + b) : a)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data 40] <D.40>`, :just:`[Data 41] <D.41>`, :just:`[I.5] <I.5>`, :just:`[I.9] <I.9>`, :just:`[I.32] <I.32>`
     - :ref:`EN <D.46>` · :ref:`EL <D.46.el>`
   * - :ref:`D.47 <D.47>`
     - Prop. LI
     - ``Given(Species(n-gon P)) -> Determined(Species(ear-triangulation T_1 .. T_{n-2}))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[Data 41] <D.41>`, :just:`[I.32] <I.32>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.47>` · :ref:`EL <D.47.el>`
   * - :ref:`D.48 <D.48>`
     - Prop. LII
     - ``Given(Species(△ABC), Species(△ABD), SharedBase(AB)) -> Determined(Ratio(△ABC : △ABD))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.37] <I.37>`, :just:`[VI.1] <VI.1>`, :just:`[VI.4] <VI.4>`
     - :ref:`EN <D.48>` · :ref:`EL <D.48.el>`
   * - :ref:`D.49 <D.49>`
     - Prop. LIII
     - ``Given(Species(P1 on AB), Species(P2 on AB)) -> Determined(Ratio(Area(P1) : Area(P2)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 22] <D.22>`, :just:`[Data 47] <D.47>`, :just:`[Data 48] <D.48>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.49>` · :ref:`EL <D.49.el>`
   * - :ref:`D.50 <D.50>`
     - Prop. LIV
     - ``Given(Ratio(AB : CD) = r, Similar(E, F)) -> Determined(Ratio(Area(E) : Area(F)) = r^2)``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.11] <VI.11>`, :just:`[VI.19] <VI.19>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.50>` · :ref:`EL <D.50.el>`
   * - :ref:`D.51 <D.51>`
     - Prop. LV
     - ``Given(Ratio(AB : CD), Species(E), Species(F)) -> Determined(Ratio(Area(E) : Area(F)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 49] <D.49>`, :just:`[Data 50] <D.50>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.51>` · :ref:`EL <D.51.el>`
   * - :ref:`D.52 <D.52>`
     - Prop. LVI
     - ``Given(Mag(AB), Species(P on AB)) -> Determined(Mag(Area(P)))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`
     - :ref:`EN <D.52>` · :ref:`EL <D.52.el>`
   * - :ref:`D.53 <D.53>`
     - Prop. LVII
     - ``Given(Species(A), Species(B), Ratio(s1(A) : s1(B))) -> Determined(Ratio(si(A) : sj(B)))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[V.22] <V.22>`
     - :ref:`EN <D.53>` · :ref:`EL <D.53.el>`
   * - :ref:`D.54 <D.54>`
     - Prop. LIX
     - ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(si(A) : sj(B)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 49] <D.49>`, :just:`[Data 53] <D.53>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.54>` · :ref:`EL <D.54.el>`
   * - :ref:`D.55 <D.55>`
     - Prop. LX
     - ``Given(Species(A), Mag(Area(A))) -> Determined(Mag(sides(A)))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 52] <D.52>`, :just:`[Data 54] <D.54>`, :just:`[I.46] <I.46>`, :just:`[VI.18] <VI.18>`
     - :ref:`EN <D.55>` · :ref:`EL <D.55.el>`

Computational Primitives (``geometor.model`` & SymPy)
-----------------------------------------------------

* :ref:`D.39 <D.39>` (*Prop. XLII*): Constructive SSS rigidity (`Elements I.22` + `I.8`) determining all angles and side-ratios.
* :ref:`D.40 <D.40>` (*Prop. XLIII*): Prototype unit-base construction (`D.27` + `D.29`) + equiangular similarity (`Elements VI.4`).
* :ref:`D.41 <D.41>` (*Prop. XLIV*): SAS similarity (`Elements VI.6`) on an auxiliary model triangle with fixed side D and E = (b/c)*D.
* :ref:`D.42 <D.42>` (*Prop. XLV*): Scale-free SSS similarity (`Elements VI.5` + `D.39`) instantiating segments F, G, H in given ratios.
* :ref:`D.43 <D.43>` (*Prop. XLVI*): Unambiguous right-triangle HL similarity (semicircle intersection fixes unique acute complement).
* :ref:`D.44 <D.44>` (*Prop. XLVII*): Elements VI.7 SSA similarity split into acute and obtuse roots C1, C2 of Circle(B, r) cap Ray(AC).
* :ref:`D.45 <D.45>` (*Prop. XLVIII*): Produce BA to D with AD = AC: angle BDC = A/2 is given, reducing (b+c):a to SSA (`D.44`) on △DBC!
* :ref:`D.46 <D.46>` (*Prop. XLIX*): Produce BA to D with AD = AC: △DBC has given Angle B and given ratio BD : BC (`D.41`), then CD bisector fixes A!
* :ref:`D.47 <D.47>` (*Prop. LI*): Inductive diagonal ear-clipping (`D.41` peels △ABC, subtracts ∠ACB from ∠BCD via `D.4`, scales ratio via `D.8`).
* :ref:`D.48 <D.48>` (*Prop. LII*): Common-base area ratio equals ratio of altitudes h1 : h2, determined by species angles and side ratios.
* :ref:`D.49 <D.49>` (*Prop. LIII*): Triangulate both polygons (`D.47`), relate sub-triangles via `D.48` and `VI.20`, sum via `D.22`.
* :ref:`D.50 <D.50>` (*Prop. LIV*): Duplicate-ratio scaling (`Elements VI.20` cor.): Area(E) : Area(F) = AB : third_proportional(AB, CD) = r^2.
* :ref:`D.51 <D.51>` (*Prop. LV*): Copy figure G ~ E onto AB or CD (`VI.18`), bridge Area(E):Area(G) by `D.50` and Area(G):Area(F) by `D.49`, compose via `D.8`.
* :ref:`D.52 <D.52>` (*Prop. LVI*): Construct square ABFG on given AB (`I.46`, given in magnitude and species); Area(P) : AB^2 is given by `D.49`, hence Area(P) by `D.2`.
* :ref:`D.53 <D.53>` (*Prop. LVII*): Chain internal side ratios from `Def. 3` across the cross-figure bridge ratio via `D.8`.
* :ref:`D.54 <D.54>` (*Prop. LIX*): Reduce Area(A):Area(B) to similar figures via `D.49`, then extract square-root side ratio from duplicate ratio via `D.24`!
* :ref:`D.55 <D.55>` (*Prop. LX*): Instantiate unit-side prototype B ~ A (`D.52` gives Area(B)); `D.1` gives Area(A):Area(B); `D.54` + `D.2` yield exact sides (`Elements VI.25`!
