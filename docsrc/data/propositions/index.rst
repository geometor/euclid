:order: 2
:type: book
:layout: book
:canonical_id: D.prop
:breadcrumb_title: Propositions
:book: Propositions
:title: Propositions 1–94 of Euclid's Data
:folio: Menge 4–184

.. _data-propositions:

=========================================
Propositions 1–94 of Euclid's *Data*
=========================================

The ninety-four propositions of Euclid's *Data* establish the constructive closure of Greek geometric analysis, progressing systematically across magnitudes, ratios, position loci, triangle species, area application with defect and excess, proportional figures, and circular chords.

.. rubric:: Section 1

:order: 10
:type: chapter
:canonical_id: D.unit.1
:folio: Menge pp. 4–42
:book: Propositions 1–24: Magnitudes & Ratios
:description: Deductive closure of given magnitudes and ratios over Elements Book V: addition, subtraction, inversion, composition, division, ex aequali chains, affine-linear offset relations (δοθέντι μεῖζον ἢ ἐν λόγῳ), non-singular linear combinations (D.22–D.23), and geometric mean proportions (D.24).

.. _data-unit-1-en:

===============================================
Magnitudes & Ratios (Propositions 1–24)
===============================================

*Pure Algebraic Closure of Given Magnitudes, Ratios, and Affine-Ratio Equations* — **D.1–D.24 (Simson I–XXVII) · Menge (1896) pp. 4–42**

.. note::

   **Edition Track (English)**: Deductive closure of given magnitudes and ratios over Elements Book V: addition, subtraction, inversion, composition, division, ex aequali chains, affine-linear offset relations (δοθέντι μεῖζον ἢ ἐν λόγῳ), non-singular linear combinations (D.22–D.23), and geometric mean proportions (D.24). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

:order: 12
:type: summary
:canonical_id: D.unit.1
:folio: Menge pp. 4–42
:book: Propositions 1–24: Magnitudes & Ratios

.. _data-unit-1-summary:

====================================================================
Magnitudes & Ratios (Propositions 1–24) — Analytical Summary
====================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Deductive closure of given magnitudes and ratios over Elements Book V: addition, subtraction, inversion, composition, division, ex aequali chains, affine-linear offset relations (δοθέντι μεῖζον ἢ ἐν λόγῳ), non-singular linear combinations (D.22–D.23), and geometric mean proportions (D.24).

* **Scope**: 24 propositions (D.1–D.24 (Simson I–XXVII), *Menge* pp. 4–42).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Overview (D.1–D.24 (Simson I–XXVII))
------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 12 38 28 12

   * - ID
     - Simson
     - Functional Signature
     - Key Dependencies
     - Tracks
   * - :ref:`D.1 <D.1>`
     - Prop. I
     - ``Given(Mag(A), Mag(B)) -> Determined(Ratio(A : B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[V.7] <V.7>`, :just:`[V.16] <V.16>`
     - :ref:`English <D.1>` · :ref:`Greek <D.1.el>`
   * - :ref:`D.2 <D.2>`
     - Prop. II
     - ``Given(Mag(A), Ratio(A : B)) -> Determined(Mag(B)) [Simson fourth-proportional diorismos]``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[V.11] <V.11>`, :just:`[V.9] <V.9>`, :just:`[VI.12] <VI.12>`
     - :ref:`English <D.2>` · :ref:`Greek <D.2.el>`
   * - :ref:`D.3 <D.3>`
     - Prop. III
     - ``Given(Mag(AB), Mag(BC)) -> Determined(Mag(AB + BC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 2] <I.cn.2>`
     - :ref:`English <D.3>` · :ref:`Greek <D.3.el>`
   * - :ref:`D.4 <D.4>`
     - Prop. IV
     - ``Given(Mag(AB), Mag(AC)) -> Determined(Mag(AB - AC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 3] <I.cn.3>`
     - :ref:`English <D.4>` · :ref:`Greek <D.4.el>`
   * - :ref:`D.5 <D.5>`
     - Prop. VI
     - ``Given(Ratio(AB : AC)) -> Determined(Ratio(AB : (AB - AC)))``
     - :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.5>` · :ref:`Greek <D.5.el>`
   * - :ref:`D.6 <D.6>`
     - Prop. VII
     - ``Given(Ratio(AB : BC)) -> Determined(Ratio((AB+BC) : AB), Ratio((AB+BC) : BC))``
     - :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.6>` · :ref:`Greek <D.6.el>`
   * - :ref:`D.7 <D.7>`
     - Prop. VIII
     - ``Given(Mag(AB), Ratio(AC : CB)) -> Determined(Mag(AC), Mag(CB))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[VI.10] <VI.10>`
     - :ref:`English <D.7>` · :ref:`Greek <D.7.el>`
   * - :ref:`D.8 <D.8>`
     - Prop. IX
     - ``Given(Ratio(A : B), Ratio(C : B)) -> Determined(Ratio(A : C))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[V.7] <V.7>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`
     - :ref:`English <D.8>` · :ref:`Greek <D.8.el>`
   * - :ref:`D.9 <D.9>`
     - Prop. X
     - ``Given(Ratios(A:B:C), Ratio(A:D), Ratio(B:E), Ratio(C:F)) -> Determined(Ratios(D:E:F))``
     - :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`
     - :ref:`English <D.9>` · :ref:`Greek <D.9.el>`
   * - :ref:`D.10 <D.10>`
     - Prop. XVI
     - ``Given((AB - D) : BC = k) <-> Determined(((AB+BC) - D) : BC = k+1 | (AB + BE = D where BC:BE given))``
     - :just:`[Data Def. 9] <D.def.9>`, :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 5] <D.5>`, :just:`[Data 6] <D.6>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.10>` · :ref:`Greek <D.10.el>`
   * - :ref:`D.11 <D.11>`
     - Prop. XVII
     - ``Given((AB - D) : BC = k) <-> Determined((AB - k/(k+1)*D) : (AB + BC) = k/(k+1))``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 6] <D.6>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.11>` · :ref:`Greek <D.11.el>`
   * - :ref:`D.12 <D.12>`
     - Prop. V
     - ``Given(Mag(A + B), Mag(B + C)) -> Determined(A = C | ExceedsByGiven(A, C))``
     - :just:`[Data Def. 9] <D.def.9>`, :just:`[Data 4] <D.4>`, :just:`[C.N. 3] <I.cn.3>`
     - :ref:`English <D.12>` · :ref:`Greek <D.12.el>`
   * - :ref:`D.13 <D.13>`
     - Prop. XXIV
     - ``Given(Ratio(A : B) = r, (B - F) : C = k) -> Determined((A - r*F) : C = r*k)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.13>` · :ref:`Greek <D.13.el>`
   * - :ref:`D.14 <D.14>`
     - Prop. XVIII
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A+d1 : C+d2) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.12] <V.12>`, :just:`[V.18] <V.18>`
     - :ref:`English <D.14>` · :ref:`Greek <D.14.el>`
   * - :ref:`D.15 <D.15>`
     - Prop. XIX
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A-d1 : C-d2) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.15>` · :ref:`Greek <D.15.el>`
   * - :ref:`D.16 <D.16>`
     - Prop. XX
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(((A+d2) - (r*d1+d2)) : (C-d1) = r)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.16>` · :ref:`Greek <D.16.el>`
   * - :ref:`D.17 <D.17>`
     - Prop. XXV
     - ``Given((A - d1):B = k1, (C - d2):B = k2) -> Determined(Ratio(A:C) | GreaterThanInRatio(A, C))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 14] <D.14>`, :just:`[V.11] <V.11>`
     - :ref:`English <D.17>` · :ref:`Greek <D.17.el>`
   * - :ref:`D.18 <D.18>`
     - Prop. XXVI
     - ``Given((C - d1):A = k1, (C - d2):E = k2) -> Determined(Ratio(A:E) | GreaterThanInRatio(A, E))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 15] <D.15>`, :just:`[V.11] <V.11>`
     - :ref:`English <D.18>` · :ref:`Greek <D.18.el>`
   * - :ref:`D.19 <D.19>`
     - Prop. XXVII
     - ``Given((A - d1):B = k1, (B - d2):C = k2) -> Determined((A - (d1 + k1*d2)) : C = k1*k2)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[Data 13] <D.13>`, :just:`[V.11] <V.11>`
     - :ref:`English <D.19>` · :ref:`Greek <D.19.el>`
   * - :ref:`D.20 <D.20>`
     - Prop. XXIII
     - ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A-x : C-y) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.20>` · :ref:`Greek <D.20.el>`
   * - :ref:`D.21 <D.21>`
     - Omitted (cf. Prop. XVIII)
     - ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A+x : C+y) | GreaterThanInRatio)``
     - :just:`[Data 14] <D.14>`, :just:`[V.18] <V.18>`
     - :ref:`English <D.21>` · :ref:`Greek <D.21.el>`
   * - :ref:`D.22 <D.22>`
     - Prop. XI
     - ``Given(Ratio(A : C) = r1, Ratio(B : C) = r2) -> Determined(Ratio((A + B) : C) = r1 + r2)``
     - :just:`[Data 3] <D.3>`, :just:`[Data 6] <D.6>`, :just:`[Data 8] <D.8>`, :just:`[V.24] <V.24>`
     - :ref:`English <D.22>` · :ref:`Greek <D.22.el>`
   * - :ref:`D.23 <D.23>`
     - Prop. XII
     - ``Given(AB:CD = r0, AE:CF = r1 != r0, EB:FD = r2) -> Determined(All pairwise ratios)``
     - :just:`[Data 5] <D.5>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.19] <V.19>`
     - :ref:`English <D.23>` · :ref:`Greek <D.23.el>`
   * - :ref:`D.24 <D.24>`
     - Prop. XIII
     - ``Given(A : B = B : C, Ratio(A : C)) -> Determined(Ratio(A : B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[VI.13] <VI.13>`, :just:`[VI.17] <VI.17>`, :just:`[VI.22] <VI.22>`
     - :ref:`English <D.24>` · :ref:`Greek <D.24.el>`

Computational Primitives (``geometor.model`` & SymPy)
-----------------------------------------------------

* :ref:`D.1 <D.1>` (*Prop. I*): Exact symbolic ratio evaluation sp.simplify(A / B) from known magnitudes.
* :ref:`D.2 <D.2>` (*Prop. II*): Fourth-proportional solver B = A * (D / C) when homogeneous constructibility holds.
* :ref:`D.3 <D.3>` (*Prop. III*): Additive closure X + Y of constructible symbolic quantities.
* :ref:`D.4 <D.4>` (*Prop. IV*): Subtractive closure X - Y (with X > Y) of constructible symbolic quantities.
* :ref:`D.5 <D.5>` (*Prop. VI*): Conversio rationis closure: r = A/C -> A/(A-C) = r/(r-1).
* :ref:`D.6 <D.6>` (*Prop. VII*): Compositio rationis closure: r = A/B -> (A+B)/B = r+1 and (A+B)/A = (r+1)/r.
* :ref:`D.7 <D.7>` (*Prop. VIII*): Barycentric / internal ratio partition AC = r/(r+1)*AB, CB = 1/(r+1)*AB.
* :ref:`D.8 <D.8>` (*Prop. IX*): Transitive elimination of shared reference magnitude B via ex aequali (A/C = (A/B)/(C/B)).
* :ref:`D.9 <D.9>` (*Prop. X*): Diagonal scaling of a projective tuple (D, E, F) = (A/k1, B/k2, C/k3).
* :ref:`D.10 <D.10>` (*Prop. XVI*): Affine-ratio composition and converse bifurcation depending on whether given offset D < AB or D > AB.
* :ref:`D.11 <D.11>` (*Prop. XVII*): Bidirectional affine-linear substitution solving BC = (AB - D)/k into AB + BC and back.
* :ref:`D.12 <D.12>` (*Prop. V*): Elimination of common summand B: A - C = (A + B) - (B + C).
* :ref:`D.13 <D.13>` (*Prop. XXIV*): Scalar multiplication of an affine-ratio relation A = r*B = r*F + (r*k)*C.
* :ref:`D.14 <D.14>` (*Prop. XVIII*): Affine shift of proportional variables: (A+d1) - r*(C+d2) = d1 - r*d2.
* :ref:`D.15 <D.15>` (*Prop. XIX*): Subtractive affine shift: (A-d1) - r*(C-d2) = r*d2 - d1.
* :ref:`D.16 <D.16>` (*Prop. XX*): Mixed affine shift: A + d2 = r*(C - d1) + (r*d1 + d2), offset strictly positive.
* :ref:`D.17 <D.17>` (*Prop. XXV*): Elimination of parameter B between two affine-linear equations A = d1 + k1*B, C = d2 + k2*B.
* :ref:`D.18 <D.18>` (*Prop. XXVI*): Elimination of shared dominant variable C = d1 + k1*A = d2 + k2*E.
* :ref:`D.19 <D.19>` (*Prop. XXVII*): Composition of 1D affine maps f(g(C)) = d1 + k1*(d2 + k2*C) = (d1 + k1*d2) + (k1*k2)*C.
* :ref:`D.20 <D.20>` (*Prop. XXIII*): Parametric line segment difference: (A - x) + r*y = A, eliminating x = r*y.
* :ref:`D.21 <D.21>` (*Omitted (cf. Prop. XVIII)*): Dual of D.20 and symmetric restatement of D.14 (omitted as redundant by Simson).
* :ref:`D.22 <D.22>` (*Prop. XI*): Linearity of ratios over common denominator: (A + B)/C = A/C + B/C.
* :ref:`D.23 <D.23>` (*Prop. XII*): Non-singular 2x2 homogeneous linear solver (det = r1 - r2 != 0; Zamberti/Simson condition).
* :ref:`D.24 <D.24>` (*Prop. XIII*): Quadratic/mean-proportional root extraction over Q(sqrt(r)): A/B = sqrt(A/C).


:order: 13
:type: notes
:canonical_id: D.unit.1
:folio: Menge pp. 4–42
:book: Propositions 1–24: Magnitudes & Ratios

.. _data-unit-1-notes:

===============================================================================
Magnitudes & Ratios (Propositions 1–24) — Philological & Critical Notes
===============================================================================

1. Inhomogeneous Magnitudes & Simson's Diorismos on D.2, D.7, and D.8
---------------------------------------------------------------------

Unit 1 (:ref:`D.1 <D.1>`–:ref:`D.24 <D.24>`) operates at the universal level of :cite:`Elements Book V <heath:1926>` magnitudes (*μεγέθη*): lines, plane areas, solids, and angles. In his critical notes on :ref:`D.2 <D.2>` (:cite:`pp. 456–457 <simson:1762>`), :person:`Robert Simson <simson>` pointed out a subtle foundational boundary that :person:`Euclid <euclid>` leaves tacit: in the *Elements*, constructing a fourth proportional $C : D = A : B$ is proved constructively only for **straight lines** (:just:`[VI.12] <VI.12>`), not directly for arbitrary solids or inhomogeneous magnitudes.

Simson observed that whenever a given ratio between two homogeneous magnitudes can be exhibited as the ratio of two *given straight lines* $L_1 : L_2$ (as is always the case for constructible plane and solid problems in geometry), :just:`[VI.12] <VI.12>` supplies the required fourth proportional rigorously. Similarly, in :ref:`D.8 <D.8>` (*magnitudes having given ratios to the same magnitude have a given ratio to one another*), $A$ and $C$ must be **homogeneous** with one another (both lines, or both areas, etc.) in order to stand in a Eudoxian ratio (:just:`[V.def.3] <V.def.3>`).

2. The Affine-Linear Calculus (Defs. 11–12 & D.10–D.21) and Simson's Additions
------------------------------------------------------------------------------

Propositions :ref:`D.10 <D.10>`–:ref:`D.21 <D.21>` constitute an extraordinary piece of Greek **symbolic compression**. By packaging the two-parameter affine relation $y = k x + c$ ($c > 0$ given in magnitude, $k > 0$ given in ratio) into the single predicate :term:`δοθέντι μεῖζον ἢ ἐν λόγῳ <dothenti-meizon-e-en-logo>` (:just:`[Data Def. 11] <D.def.11>`) and $y = k x - c$ into :just:`[Data Def. 12] <D.def.12>`, Euclid proves that affine functions of an unknown magnitude form a **closed algebraic groupoid**:

* **Additive & Subtractive Shifts** (:ref:`D.10 <D.10>`–:ref:`D.11 <D.11>`): Notice that in :person:`Heinrich Menge's <menge>` non-Theonine text (:cite:`1896, pp. 16–22 <menge:1896>`), both :ref:`D.10 <D.10>` and :ref:`D.11 <D.11>` contain **two parts**—a direct theorem and its converse! In the converse of :ref:`D.10 <D.10>`, subtracting the given offset $c$ from $x + y = c + k y$ splits into two cases according as $c < x$ (leaving $x = c + (k-1)y$) or $c > x$ (producing $x + (c - x) = c$ where $y : (c - x)$ is given, i.e., $x = c - k' y$). Because Euclid in `Vat. gr. 190` avoided phrasing the second branch via Def. 12 directly, :person:`Simson <simson>` (:cite:`Props. XIV–XXIV <simson:1762>`) split and expanded the entire suite symmetrically across all sign combinations (`Props. XIV–XV` and `Props. XXI–XXII`).

* **Composition & Elimination** (:ref:`D.13 <D.13>`, :ref:`D.17 <D.17>`–:ref:`D.19 <D.19>`): :ref:`D.19 <D.19>` proves closure under composition ($A = k_1 B + c_1$ and $B = k_2 C + c_2 \implies A = (k_1 k_2) C + (c_1 + k_1 c_2)$), while :ref:`D.17 <D.17>` and :ref:`D.18 <D.18>` eliminate a shared variable between two affine equations.

* **The Doublet D.21**: As :person:`Simson <simson>` noted (:cite:`p. 458 <simson:1762>`), :ref:`D.21 <D.21>` (*adding magnitudes in a given ratio to two given magnitudes*) is mathematically identical to the first part of :ref:`D.14 <D.14>` (*adding two given magnitudes to magnitudes in a given ratio*) with the roles of the summands swapped; Simson therefore omitted `D.21`, whereas Menge retained it on the manuscript authority of :cite:`Vat. gr. 190 <vat-gr-190>`.

3. Non-Singularity in D.23 (det != 0) & Simson's Critique of Newton on D.24
---------------------------------------------------------------------------

Two philological gems crown the close of * **Determinant Non-Singularity in D.23**: In :ref:`D.23 <D.23>`, if whole $AB = AE + EB$ has a given ratio $r$ to whole $CD = CF + FD$, while $AE : CF = r_1$ and $EB : FD = r_2$ are given, the crucial Greek proviso **μὴ τοὺς αὐτοὺς δέ** (*\"yet not the same ratios\"*, $r_1 \neq r_2$) is the exact classical statement of **matrix non-singularity**! Algebraically, $(r_1 - r) CF + (r_2 - r) FD = 0$; if $r_1 = r_2 = r$, the two equations collapse into one ($0 = 0$) and $CF : FD$ is indeterminate (`ἄτακτον`), whereas $r_1 \neq r_2$ forces $CF : FD = (r - r_2) : (r_1 - r)$ uniquely. :person:`Bartolomeo Zamberti's <zamberti>` 1505 Latin translation omitted the negation *non*, rendering the theorem false until :person:`Claude Hardy <hardy>` (:cite:`1625 <hardy:1625>`) and :person:`David Gregory <gregory>` (:cite:`1703 <gregory:1703>`) restored the Greek condition.

* **Continued Proportion & Quadratic Root Extraction in D.24**: :ref:`D.24 <D.24>` proves that if $A : B = B : C$ and $A : C$ is given, then $A : B$ is given ($A/B = \sqrt{A/C}$). Notably, Unit 1 here steps from general magnitudes to **straight lines** (*εὐθεῖαι*) so that :just:`[VI.13] <VI.13>` can construct the geometric mean $E = \sqrt{D \cdot F}$. Late Byzantine manuscripts appended an alternative proof (*Ἄλλως*, relegated by Menge to the Appendix) that tried to dispense with squares, and :person:`Isaac Newton <newton>` cited a similar shortcut in :cite:`Principia Book I, Lemma XVII <newton:1713>`; :person:`Simson <simson>` (:cite:`pp. 459–460 <simson:1762>`) demonstrated that the scholiast's *Ἄλλως* tacitly begged the question, vindicating Euclid's authentic proof.

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.1 <D.1>` (Prop. I) — *Elements G-Index*: ``G.183, G.195`` · *Pappus*: Synagoge VII.3
* :ref:`D.2 <D.2>` (Prop. II) — *Elements G-Index*: ``G.189, G.187, G.222`` · *Pappus*: Synagoge VII.3 · *Petersen (1879)*: Similarity / Scaling · *Altshiller-Court (1952)*: § 18 (Fourth Proportional)
* :ref:`D.3 <D.3>` (Prop. III) — *Elements G-Index*: ``G.36`` · *Petersen (1879)*: Algebraic Method · *Altshiller-Court (1952)*: § 6 (Sum of Segments)
* :ref:`D.4 <D.4>` (Prop. IV) — *Elements G-Index*: ``G.19`` · *Petersen (1879)*: Algebraic Method · *Altshiller-Court (1952)*: § 6 (Difference of Segments)
* :ref:`D.5 <D.5>` (Prop. VI) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.4
* :ref:`D.6 <D.6>` (Prop. VII) — *Elements G-Index*: ``G.199, G.201`` · *Pappus*: Synagoge VII.4
* :ref:`D.7 <D.7>` (Prop. VIII) — *Elements G-Index*: ``G.220`` · *Pappus*: Synagoge VII.4 · *Petersen (1879)*: Similarity / Ratio Division · *Altshiller-Court (1952)*: § 19 (Internal Division)
* :ref:`D.8 <D.8>` (Prop. IX) — *Elements G-Index*: ``G.183, G.189, G.205`` · *Pappus*: Synagoge VII.4
* :ref:`D.9 <D.9>` (Prop. X) — *Elements G-Index*: ``G.189, G.205`` · *Pappus*: Synagoge VII.4
* :ref:`D.10 <D.10>` (Prop. XVI) — *Elements G-Index*: ``G.199, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.11 <D.11>` (Prop. XVII) — *Elements G-Index*: ``G.190, G.195, G.199, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.12 <D.12>` (Prop. V) — *Elements G-Index*: ``G.19`` · *Petersen (1879)*: Algebraic Method
* :ref:`D.13 <D.13>` (Prop. XXIV) — *Elements G-Index*: ``G.189, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.14 <D.14>` (Prop. XVIII) — *Elements G-Index*: ``G.190, G.199`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.15 <D.15>` (Prop. XIX) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.16 <D.16>` (Prop. XX) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.17 <D.17>` (Prop. XXV) — *Elements G-Index*: ``G.189`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.18 <D.18>` (Prop. XXVI) — *Elements G-Index*: ``G.189`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.19 <D.19>` (Prop. XXVII) — *Elements G-Index*: ``G.189`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.20 <D.20>` (Prop. XXIII) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.21 <D.21>` (Omitted (cf. Prop. XVIII)) — *Elements G-Index*: ``G.199`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.22 <D.22>` (Prop. XI) — *Elements G-Index*: ``G.207`` · *Pappus*: Synagoge VII.4
* :ref:`D.23 <D.23>` (Prop. XII) — *Elements G-Index*: ``G.189, G.195, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.24 <D.24>` (Prop. XIII) — *Elements G-Index*: ``G.223, G.228, G.234`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Mean Proportional · *Altshiller-Court (1952)*: § 21 (Mean Proportional)


----


.. rubric:: Section 2

:order: 20
:type: chapter
:canonical_id: D.unit.2
:folio: Menge pp. 42–66
:book: Propositions 25–38: Position & Parallels
:description: Transition from abstract magnitudes to planar geometry: uniqueness of line-line intersections (D.25), endpoints and directions of segments (D.26–D.30), neusis/circle distance meets (D.31), inclined transversals across parallels (D.32–D.33), and parallel ratio-division loci through a fixed pole (D.34–D.38).

.. _data-unit-2-en:

=============================================================
Position, Angles & Parallel Loci (Propositions 25–38)
=============================================================

*Straight Lines Given in Position, Angular Rays, and Parallel Locus Determination* — **D.25–D.38 (Simson XXVIII–XL) · Menge (1896) pp. 42–66**

.. note::

   **Edition Track (English)**: Transition from abstract magnitudes to planar geometry: uniqueness of line-line intersections (D.25), endpoints and directions of segments (D.26–D.30), neusis/circle distance meets (D.31), inclined transversals across parallels (D.32–D.33), and parallel ratio-division loci through a fixed pole (D.34–D.38). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. picture:: /_static/figures/data_02_position_loci.svg
   :alt: Position, Intersections, and Parallel Ratio Loci (Data Props. 25, 28–30, 34–38)

Interactive locus diagram (:cite:`Menge pp. 46–66 <menge:1896>`): From given external pole :g:`P <data_02_position_loci:P>`, secants :g:`PF <data_02_position_loci:/ P F />` (cutting :g:`AB <data_02_position_loci:/ A B />` at :g:`E <data_02_position_loci:E>` and :g:`CD <data_02_position_loci:/ C D />` at :g:`F <data_02_position_loci:F>`) and :g:`PH <data_02_position_loci:/ P H />` (cutting at :g:`G <data_02_position_loci:G>` and :g:`H <data_02_position_loci:H>`) are divided in a constant given ratio (:ref:`D.34 <D.34>`), while internal division points :g:`M <data_02_position_loci:M>`, :g:`N <data_02_position_loci:N>`, and :g:`S <data_02_position_loci:S>` trace the parallel locus :g:`MN <data_02_position_loci:/ M N />` (:ref:`D.35 <D.35>`–:ref:`D.38 <D.38>`). Ray :g:`KQ <data_02_position_loci:/ K Q />` from given point :g:`K <data_02_position_loci:K>` at given angle :g:`∠BKQ <data_02_position_loci:< B K Q )>` (:ref:`D.29 <D.29>`) meets :g:`CD <data_02_position_loci:/ C D />` at unique point :g:`Q <data_02_position_loci:Q>` (:ref:`D.25 <D.25>`).

:order: 22
:type: summary
:canonical_id: D.unit.2
:folio: Menge pp. 42–66
:book: Propositions 25–38: Position & Parallels

.. _data-unit-2-summary:

==================================================================================
Position, Angles & Parallel Loci (Propositions 25–38) — Analytical Summary
==================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Transition from abstract magnitudes to planar geometry: uniqueness of line-line intersections (D.25), endpoints and directions of segments (D.26–D.30), neusis/circle distance meets (D.31), inclined transversals across parallels (D.32–D.33), and parallel ratio-division loci through a fixed pole (D.34–D.38).

* **Scope**: 14 propositions (D.25–D.38 (Simson XXVIII–XL), *Menge* pp. 42–66).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Overview (D.25–D.38 (Simson XXVIII–XL))
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 12 38 28 12

   * - ID
     - Simson
     - Functional Signature
     - Key Dependencies
     - Tracks
   * - :ref:`D.25 <D.25>`
     - Prop. XXVIII
     - ``Given(Pos(L1), Pos(L2), Meet(L1, L2) = E) -> Determined(Pos(E))``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[Post. 1] <I.post.1>`, :just:`[I Def. 4] <I.def.4>`
     - :ref:`English <D.25>` · :ref:`Greek <D.25.el>`
   * - :ref:`D.26 <D.26>`
     - Prop. XXIX
     - ``Given(Pos(A), Pos(B)) -> Determined(Pos(AB), Mag(AB))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Post. 1] <I.post.1>`, :just:`[Post. 3] <I.post.3>`
     - :ref:`English <D.26>` · :ref:`Greek <D.26.el>`
   * - :ref:`D.27 <D.27>`
     - Prop. XXX
     - ``Given(Pos(Ray A->), Mag(AB), Pos(A)) -> Determined(Pos(B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Post. 3] <I.post.3>`, :just:`[I Def. 15] <I.def.15>`
     - :ref:`English <D.27>` · :ref:`Greek <D.27.el>`
   * - :ref:`D.28 <D.28>`
     - Prop. XXXI
     - ``Given(Pos(A), Pos(Line BC)) -> Determined(Pos(Parallel(A, BC)))``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[I.27] <I.27>`, :just:`[I.29] <I.29>`, :just:`[I.30] <I.30>`, :just:`[I.31] <I.31>`
     - :ref:`English <D.28>` · :ref:`Greek <D.28.el>`
   * - :ref:`D.29 <D.29>`
     - Prop. XXXII
     - ``Given(Pos(Line AB), Pos(C in AB), Mag(Angle theta)) -> Determined(Pos(Ray CD))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[I.23] <I.23>`
     - :ref:`English <D.29>` · :ref:`Greek <D.29.el>`
   * - :ref:`D.30 <D.30>`
     - Prop. XXXIII
     - ``Given(Pos(A), Pos(Line BC), Mag(Angle ADC)) -> Determined(Pos(Line AD))``
     - :just:`[Data 28] <D.28>`, :just:`[Data 29] <D.29>`, :just:`[I.23] <I.23>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`
     - :ref:`English <D.30>` · :ref:`Greek <D.30.el>`
   * - :ref:`D.31 <D.31>`
     - Prop. XXXIV
     - ``Given(Pos(A), Pos(Line BC), Mag(AD >= dist(A, BC))) -> Determined(Pos(AD)) [2-root diorismos]``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[I.12] <I.12>`, :just:`[Post. 3] <I.post.3>`
     - :ref:`English <D.31>` · :ref:`Greek <D.31.el>`
   * - :ref:`D.32 <D.32>`
     - Prop. XXXV
     - ``Given(Pos(AB || CD), Mag(Angle BEF)) -> Determined(Mag(EF))``
     - :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`
     - :ref:`English <D.32>` · :ref:`Greek <D.32.el>`
   * - :ref:`D.33 <D.33>`
     - Prop. XXXVI
     - ``Given(Pos(AB || CD), Mag(EF >= strip_width)) -> Determined(Mag(Angle BEF))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data 28] <D.28>`, :just:`[Data 31] <D.31>`, :just:`[I.29] <I.29>`, :just:`[I.34] <I.34>`
     - :ref:`English <D.33>` · :ref:`Greek <D.33.el>`
   * - :ref:`D.34 <D.34>`
     - Prop. XXXVIII
     - ``Given(Pos(AB || CD), Pos(Pole E)) -> Determined(Ratio(EF : FG))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.12] <I.12>`, :just:`[VI.2] <VI.2>`, :just:`[VI.4] <VI.4>`
     - :ref:`English <D.34>` · :ref:`Greek <D.34.el>`
   * - :ref:`D.35 <D.35>`
     - Prop. XXXIX (pt. 1)
     - ``Given(Pos(Pole A), Pos(Line BC), InternalRatio(AE : ED)) -> Determined(Pos(Line FEG || BC))``
     - :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`
     - :ref:`English <D.35>` · :ref:`Greek <D.35.el>`
   * - :ref:`D.36 <D.36>`
     - Prop. XXXIX (pt. 2)
     - ``Given(Pos(Pole A), Pos(Line BC), ExternalRatio(AD : DE)) -> Determined(Pos(Line FEG || BC))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`
     - :ref:`English <D.36>` · :ref:`Greek <D.36.el>`
   * - :ref:`D.37 <D.37>`
     - Prop. XL (pt. 1)
     - ``Given(Pos(AB || CD), InternalRatio(EG : GF)) -> Determined(Pos(Line HK || AB))``
     - :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`
     - :ref:`English <D.37>` · :ref:`Greek <D.37.el>`
   * - :ref:`D.38 <D.38>`
     - Prop. XL (pt. 2)
     - ``Given(Pos(AB || CD), ExternalRatio(EF : FG)) -> Determined(Pos(Line HK || AB))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`
     - :ref:`English <D.38>` · :ref:`Greek <D.38.el>`

Computational Primitives (``geometor.model`` & SymPy)
-----------------------------------------------------

* :ref:`D.25 <D.25>` (*Prop. XXVIII*): Fundamental `model.intersect(L1, L2)` primitive in geometor.model.
* :ref:`D.26 <D.26>` (*Prop. XXIX*): Fundamental `model.set_line(A, B)` and Euclidean metric norm :math:`|B - A|`.
* :ref:`D.27 <D.27>` (*Prop. XXX*): Line-circle intersection `model.intersect(line, Circle(A, r))` fixing endpoint B on a given ray.
* :ref:`D.28 <D.28>` (*Prop. XXXI*): Euclidean parallel constructor through P along direction vector of BC (`Elements I.31`).
* :ref:`D.29 <D.29>` (*Prop. XXXII*): Angular ray constructor `Elements I.23` rotating line direction at vertex C by given angle.
* :ref:`D.30 <D.30>` (*Prop. XXXIII*): Auxiliary angle construction at A on parallel through A (`D.28` + `D.29`), yielding dropped oblique/altitude.
* :ref:`D.31 <D.31>` (*Prop. XXXIV*): Circle-line intersection `Circle(A, r) cap Line(BC)` (1 tangent or 2 symmetric chords; Simson diorismos).
* :ref:`D.32 <D.32>` (*Prop. XXXV*): Translational invariance of oblique transversal length across a fixed parallel strip (`I.34`).
* :ref:`D.33 <D.33>` (*Prop. XXXVI*): Converse of D.32 reducing free transversal of given length to pinned circle-line meet (`D.31`).
* :ref:`D.34 <D.34>` (*Prop. XXXVIII*): Thales projection invariant: collinear segments from fixed pole E cut parallel lines in constant ratio.
* :ref:`D.35 <D.35>` (*Prop. XXXIX (pt. 1)*): Internal homothetic dilation H(A, k) with 0 < k < 1 mapping given line BC to parallel locus FEG.
* :ref:`D.36 <D.36>` (*Prop. XXXIX (pt. 2)*): External homothetic dilation H(A, 1 + r) or H(A, -r) mapping line BC to parallel locus FEG.
* :ref:`D.37 <D.37>` (*Prop. XL (pt. 1)*): Affine convex combination (1 - t)*L1 + t*L2 of two parallel lines given in position.
* :ref:`D.38 <D.38>` (*Prop. XL (pt. 2)*): Extrapolated affine combination (1 + r)*L2 - r*L1 outside the parallel strip.


:order: 23
:type: notes
:canonical_id: D.unit.2
:folio: Menge pp. 42–66
:book: Propositions 25–38: Position & Parallels

.. _data-unit-2-notes:

=============================================================================================
Position, Angles & Parallel Loci (Propositions 25–38) — Philological & Critical Notes
=============================================================================================

1. Shifting Proofs (Μεταπεσεῖται) vs. Constructive Proofs in D.25–D.30
----------------------------------------------------------------------

The opening propositions of Unit 2 (:ref:`D.25 <D.25>`–:ref:`D.30 <D.30>`) exhibit a striking stylistic feature in the Greek manuscripts: instead of constructing an auxiliary copy, they argue by *reductio ad absurdum* using the kinematic verb **μεταπεσεῖται** (*\"it will shift / fall elsewhere\"*), appealing directly to :just:`[Data Def. 4] <D.def.4>` (*\"always occupying the same place\"*).

:person:`Robert Simson <simson>` (:cite:`pp. 460–462 <simson:1762>`), consistent with his repair of Definition 4 (requiring *procurability* alongside *uniqueness*), replaced several shifting arguments with explicit straightedge-and-compass constructions (:just:`[Post. 1] <I.post.1>`, :just:`[Post. 3] <I.post.3>`, :just:`[I.23] <I.23>`, :just:`[I.31] <I.31>`) and inserted a companion converse (`Simson Prop. XXVII`: *if one extremity of a straight line given in magnitude be given, and the line also pass through another given point, or be given in position...*). Modern foundational scholarship (:person:`Taisbak <taisbak>` (:cite:`2003 <taisbak:2003>`)) recognizes that Euclid's `μεταπεσεῖται` idiom intentionally isolates topological/incidence invariance once elementary constructibility is already guaranteed by Books I and III.

2. Multi-Valued Intersections & Diorismos in D.31 and D.33
----------------------------------------------------------

In :ref:`D.31 <D.31>` (*drawing a segment of given length $r$ from a given point $A$ to a position-given line $CD$*), the circle $(A, r)$ (:just:`[Data Def. 6] <D.def.6>`) meets $CD$ in:

* **Zero points** if $r < d(A, CD)$ (requiring the *diorismos* $r \ge d(A, CD)$);

* **One point** (tangent foot of the perpendicular) if $r = d(A, CD)$; or

* **Two symmetric points** $B_1, B_2$ on $CD$ if $r > d(A, CD)$.

As :person:`Marinus <marinus>` already explained in :ref:`Protheoria § 4 <marinus-p04>`, Greek analysis treats a *finitely bifurcated* intersection—unique on each side of the perpendicular axis of symmetry—as genuinely **ordered and given** (*μοναχῶς ἐφʼ ἑκάτερα*), in sharp contrast to an *indeterminate* (`ἄτακτον`) continuum of solutions. Exactly the same two-branch symmetry governs :ref:`D.33 <D.33>`.

3. Petersen's Two-Locus & Parallel-Translation Paradigm (D.25–D.38)
-------------------------------------------------------------------

Nearly twenty-two centuries after Euclid, :person:`Julius Petersen <petersen>` opened his celebrated Danish problem-solving classic :cite:`Methods and Theories for the Solution of Problems of Geometrical Constructions (1879) <petersen:1879>` by distilling Unit 2 of Euclid's *Data* into two master heuristics:

1. **Method of Loci (Chapter I)**: Drop one constraint on an unknown point $X$; its locus is a position-given line (:ref:`D.28 <D.28>`–:ref:`D.30 <D.30>`, :ref:`D.35 <D.35>`–:ref:`D.38 <D.38>`) or circle (:just:`[Data Def. 6] <D.def.6>`). Restore the second constraint to obtain a second position-given locus; :ref:`D.25 <D.25>` then determines $X$ as their intersection.

2. **Parallel Translation & Homothety (Chapters II–III)**: Propositions :ref:`D.32 <D.32>`–:ref:`D.33 <D.33>` translate a floating segment $EF$ between parallel lines $AB \parallel CD$ to a chosen anchor point $G \in AB$, while :ref:`D.35 <D.35>`–:ref:`D.38 <D.38>` apply central dilation (*homothety*) from a fixed centre $A$ (or transversal dilation between parallels) to transform a position-given line into a parallel position-given locus. Note also that :person:`Simson <simson>` (:cite:`Props. XXXIX–XL <simson:1762>`) consolidated Euclid's external/internal pairs :ref:`D.35 <D.35>` + :ref:`D.36 <D.36>` into `Prop. XXXIX` and :ref:`D.37 <D.37>` + :ref:`D.38 <D.38>` into `Prop. XL`.

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.25 <D.25>` (Prop. XXVIII) — *Elements G-Index*: ``G.14, G.4`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Method of Loci (Two-Locus Intersection) · *Altshiller-Court (1952)*: § 1 (Intersection of Loci)
* :ref:`D.26 <D.26>` (Prop. XXIX) — *Elements G-Index*: ``G.14, G.15`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Method of Loci · *Altshiller-Court (1952)*: § 2
* :ref:`D.27 <D.27>` (Prop. XXX) — *Elements G-Index*: ``G.15, G.10`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Method of Loci (Line + Circle) · *Altshiller-Court (1952)*: § 3
* :ref:`D.28 <D.28>` (Prop. XXXI) — *Elements G-Index*: ``G.53, G.56, G.57, G.58`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Parallel Translation · *Altshiller-Court (1952)*: § 8 (Parallel Locus)
* :ref:`D.29 <D.29>` (Prop. XXXII) — *Elements G-Index*: ``G.48`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Rotation / Angular Locus · *Altshiller-Court (1952)*: § 5 (Given Angle Ray)
* :ref:`D.30 <D.30>` (Prop. XXXIII) — *Elements G-Index*: ``G.48, G.56, G.58`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Parallel Translation · *Altshiller-Court (1952)*: § 8
* :ref:`D.31 <D.31>` (Prop. XXXIV) — *Elements G-Index*: ``G.35, G.15`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Method of Loci (Circle + Line) · *Altshiller-Court (1952)*: § 11 (Circle-Line Intersection)
* :ref:`D.32 <D.32>` (Prop. XXXV) — *Elements G-Index*: ``G.56, G.58, G.62`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Parallel Translation · *Altshiller-Court (1952)*: § 31 (Translation between Parallels)
* :ref:`D.33 <D.33>` (Prop. XXXVI) — *Elements G-Index*: ``G.56, G.62`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Parallel Translation · *Altshiller-Court (1952)*: § 31
* :ref:`D.34 <D.34>` (Prop. XXXVIII) — *Elements G-Index*: ``G.35, G.211, G.213`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Homothecy / Multiplication of Curves · *Altshiller-Court (1952)*: § 39 (Homothetic Ratio across Parallels)
* :ref:`D.35 <D.35>` (Prop. XXXIX (pt. 1)) — *Elements G-Index*: ``G.211`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Homothecy / Multiplication of Curves · *Altshiller-Court (1952)*: § 40 (Homothetic Line Locus)
* :ref:`D.36 <D.36>` (Prop. XXXIX (pt. 2)) — *Elements G-Index*: ``G.211`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Homothecy / Multiplication of Curves · *Altshiller-Court (1952)*: § 40 (Homothetic Line Locus)
* :ref:`D.37 <D.37>` (Prop. XL (pt. 1)) — *Elements G-Index*: ``G.57, G.62, G.211`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Method of Loci · *Altshiller-Court (1952)*: § 9 (Parallel Intermediate Locus)
* :ref:`D.38 <D.38>` (Prop. XL (pt. 2)) — *Elements G-Index*: ``G.57, G.62, G.211`` · *Pappus*: Synagoge VII.6 · *Petersen (1879)*: Method of Loci · *Altshiller-Court (1952)*: § 9


----


.. rubric:: Section 3

:order: 30
:type: chapter
:canonical_id: D.unit.3
:folio: Menge pp. 66–98
:book: Propositions 39–55: Triangles & Species
:description: Constructive determination of triangles up to similarity (εἴδει) from SSS-ratios (D.39), AAA (D.40), SAS-ratio (D.41), side-ratios (D.42), right-SSA (D.43), general SSA bifurcation with obtuse/acute diorismos (D.44), sum/difference of sides (D.45–D.46), decomposing rectilinear polygons into triangles (D.47), and quadratic area-scaling of figures given in species (D.48–D.55).

.. _data-unit-3-en:

==================================================================
Triangles & Polygons Given in Species (Propositions 39–55)
==================================================================

*Similarity Invariants, Triangle Rigidity Criteria, and Area-to-Side Scaling* — **D.39–D.55 (Simson XLII–LX) · Menge (1896) pp. 66–98**

.. note::

   **Edition Track (English)**: Constructive determination of triangles up to similarity (εἴδει) from SSS-ratios (D.39), AAA (D.40), SAS-ratio (D.41), side-ratios (D.42), right-SSA (D.43), general SSA bifurcation with obtuse/acute diorismos (D.44), sum/difference of sides (D.45–D.46), decomposing rectilinear polygons into triangles (D.47), and quadratic area-scaling of figures given in species (D.48–D.55). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

.. picture:: /_static/figures/data_03_triangle_species.svg
   :alt: Triangle Species Determination (D.39–D.43) vs. SSA Two-Root Bifurcation (D.44)

Interactive species diagram (:cite:`Menge pp. 66–82 <menge:1896>`): Left panel illustrates unique species determination (:ref:`D.39 <D.39>`–:ref:`D.42 <D.42>`), pairing similar triangles :g:`DEF <data_03_triangle_species:< D E F >>` and :g:`GHK <data_03_triangle_species:< G H K >>` with :eq:`equal vertex angles <data_03_triangle_species:< E D F ) = data_03_triangle_species:< H G K )>` :g:`∠EDF <data_03_triangle_species:< E D F )>` and :g:`∠HGK <data_03_triangle_species:< H G K )>` and proportional sides :g:`DE <data_03_triangle_species:/ D E />` to :g:`GH <data_03_triangle_species:/ G H />`. Right panel illustrates the **SSA two-root bifurcation** (:ref:`D.44 <D.44>`): given angle :g:`∠CAB <data_03_triangle_species:< C2 A B )>` at :g:`A <data_03_triangle_species:A>` and side ratio :g:`AB <data_03_triangle_species:/ A B />` to radius :g:`BC₁ <data_03_triangle_species:/ B C1 />`, circle :g:`(B, BC₁) <data_03_triangle_species:( B C1 )>` cuts ray :g:`AC₂ <data_03_triangle_species:/ A C2 />` in :eq:`equal radii <data_03_triangle_species:/ B C1 / = data_03_triangle_species:/ B C2 />` at obtuse solution :g:`C₁ <data_03_triangle_species:C1>` and acute solution :g:`C₂ <data_03_triangle_species:C2>` symmetric across altitude :g:`BP <data_03_triangle_species:/ B P />` (foot :g:`P <data_03_triangle_species:P>`).

:order: 32
:type: summary
:canonical_id: D.unit.3
:folio: Menge pp. 66–98
:book: Propositions 39–55: Triangles & Species

.. _data-unit-3-summary:

=======================================================================================
Triangles & Polygons Given in Species (Propositions 39–55) — Analytical Summary
=======================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Constructive determination of triangles up to similarity (εἴδει) from SSS-ratios (D.39), AAA (D.40), SAS-ratio (D.41), side-ratios (D.42), right-SSA (D.43), general SSA bifurcation with obtuse/acute diorismos (D.44), sum/difference of sides (D.45–D.46), decomposing rectilinear polygons into triangles (D.47), and quadratic area-scaling of figures given in species (D.48–D.55).

* **Scope**: 17 propositions (D.39–D.55 (Simson XLII–LX), *Menge* pp. 66–98).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Overview (D.39–D.55 (Simson XLII–LX))
-------------------------------------------------

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
     - :ref:`English <D.39>` · :ref:`Greek <D.39.el>`
   * - :ref:`D.40 <D.40>`
     - Prop. XLIII
     - ``Given(Angle(A), Angle(B), Angle(C)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[I.32] <I.32>`, :just:`[VI.4] <VI.4>`
     - :ref:`English <D.40>` · :ref:`Greek <D.40.el>`
   * - :ref:`D.41 <D.41>`
     - Prop. XLIV
     - ``Given(Angle(A), Ratio(c : b)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[VI.6] <VI.6>`
     - :ref:`English <D.41>` · :ref:`Greek <D.41.el>`
   * - :ref:`D.42 <D.42>`
     - Prop. XLV
     - ``Given(Ratio(a : b), Ratio(b : c)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 39] <D.39>`, :just:`[I.20] <I.20>`, :just:`[I.22] <I.22>`, :just:`[VI.5] <VI.5>`
     - :ref:`English <D.42>` · :ref:`Greek <D.42.el>`
   * - :ref:`D.43 <D.43>`
     - Prop. XLVI
     - ``Given(Angle(A) = pi/2, Ratio(hypotenuse c : leg b)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.47] <I.47>`, :just:`[VI.7] <VI.7>`
     - :ref:`English <D.43>` · :ref:`Greek <D.43.el>`
   * - :ref:`D.44 <D.44>`
     - Prop. XLVII
     - ``Given(Angle(A), Ratio(AB : BC), Sign(cos C)) -> Determined(Species(Triangle ABC)) [SSA diorismos]``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.13] <I.13>`, :just:`[VI.7] <VI.7>`
     - :ref:`English <D.44>` · :ref:`Greek <D.44.el>`
   * - :ref:`D.45 <D.45>`
     - Prop. XLVIII
     - ``Given(Angle(A), Ratio((b + c) : a)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data 40] <D.40>`, :just:`[Data 44] <D.44>`, :just:`[I.5] <I.5>`, :just:`[I.32] <I.32>`
     - :ref:`English <D.45>` · :ref:`Greek <D.45.el>`
   * - :ref:`D.46 <D.46>`
     - Prop. XLIX
     - ``Given(Angle(B), Ratio((c + b) : a)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data 40] <D.40>`, :just:`[Data 41] <D.41>`, :just:`[I.5] <I.5>`, :just:`[I.9] <I.9>`, :just:`[I.32] <I.32>`
     - :ref:`English <D.46>` · :ref:`Greek <D.46.el>`
   * - :ref:`D.47 <D.47>`
     - Prop. LI
     - ``Given(Species(n-gon P)) -> Determined(Species(ear-triangulation T_1 .. T_{n-2}))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[Data 41] <D.41>`, :just:`[I.32] <I.32>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.47>` · :ref:`Greek <D.47.el>`
   * - :ref:`D.48 <D.48>`
     - Prop. LII
     - ``Given(Species(△ABC), Species(△ABD), SharedBase(AB)) -> Determined(Ratio(△ABC : △ABD))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.37] <I.37>`, :just:`[VI.1] <VI.1>`, :just:`[VI.4] <VI.4>`
     - :ref:`English <D.48>` · :ref:`Greek <D.48.el>`
   * - :ref:`D.49 <D.49>`
     - Prop. LIII
     - ``Given(Species(P1 on AB), Species(P2 on AB)) -> Determined(Ratio(Area(P1) : Area(P2)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 22] <D.22>`, :just:`[Data 47] <D.47>`, :just:`[Data 48] <D.48>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.49>` · :ref:`Greek <D.49.el>`
   * - :ref:`D.50 <D.50>`
     - Prop. LIV
     - ``Given(Ratio(AB : CD) = r, Similar(E, F)) -> Determined(Ratio(Area(E) : Area(F)) = r^2)``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.11] <VI.11>`, :just:`[VI.19] <VI.19>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.50>` · :ref:`Greek <D.50.el>`
   * - :ref:`D.51 <D.51>`
     - Prop. LV
     - ``Given(Ratio(AB : CD), Species(E), Species(F)) -> Determined(Ratio(Area(E) : Area(F)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 49] <D.49>`, :just:`[Data 50] <D.50>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.51>` · :ref:`Greek <D.51.el>`
   * - :ref:`D.52 <D.52>`
     - Prop. LVI
     - ``Given(Mag(AB), Species(P on AB)) -> Determined(Mag(Area(P)))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`
     - :ref:`English <D.52>` · :ref:`Greek <D.52.el>`
   * - :ref:`D.53 <D.53>`
     - Prop. LVII
     - ``Given(Species(A), Species(B), Ratio(s1(A) : s1(B))) -> Determined(Ratio(si(A) : sj(B)))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[V.22] <V.22>`
     - :ref:`English <D.53>` · :ref:`Greek <D.53.el>`
   * - :ref:`D.54 <D.54>`
     - Prop. LIX
     - ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(si(A) : sj(B)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 49] <D.49>`, :just:`[Data 53] <D.53>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.54>` · :ref:`Greek <D.54.el>`
   * - :ref:`D.55 <D.55>`
     - Prop. LX
     - ``Given(Species(A), Mag(Area(A))) -> Determined(Mag(sides(A)))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 52] <D.52>`, :just:`[Data 54] <D.54>`, :just:`[I.46] <I.46>`, :just:`[VI.18] <VI.18>`
     - :ref:`English <D.55>` · :ref:`Greek <D.55.el>`

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


:order: 33
:type: notes
:canonical_id: D.unit.3
:folio: Menge pp. 66–98
:book: Propositions 39–55: Triangles & Species

.. _data-unit-3-notes:

==================================================================================================
Triangles & Polygons Given in Species (Propositions 39–55) — Philological & Critical Notes
==================================================================================================

1. Triangle Rigidity modulo Similarity & Petersen's Method of Similarity (D.39–D.42)
------------------------------------------------------------------------------------

Unit 3 shifts from *position* in the plane to **intrinsic shape**—figures :term:`given in species <eidei>` (:just:`[Data Def. 3] <D.def.3>`), i.e., determined up to similarity (angles given and pairwise side-ratios given). Propositions :ref:`D.39 <D.39>`–:ref:`D.42 <D.42>` lift the congruence and similarity theorems of Books I and VI into constructive shape-determination operators:

* :ref:`D.39 <D.39>` (**SSS** $\to$ species, via :just:`[I.22] <I.22>` & :just:`[I.8] <I.8>`);

* :ref:`D.40 <D.40>` (**AAA / AA** $\to$ species, via :just:`[I.32] <I.32>` & :just:`[VI.4] <VI.4>`);

* :ref:`D.41 <D.41>` (**SAS-ratio** $\to$ species, via :just:`[VI.6] <VI.6>`);

* :ref:`D.42 <D.42>` (**SSS-ratios** $\to$ species, via :just:`[VI.5] <VI.5>`).

Notice Euclid's constructive technique throughout: he sets out an arbitrary *reference segment* $DE$ given in position and magnitude, builds a concrete prototype $\triangle DEF$ whose vertices are determined in position by Unit 2, reads off its given angles and ratios, and transfers species to $\triangle ABC$ by Book VI similarity. This is the exact archetype of :person:`Petersen's <petersen>` **Method of Similarity** (:cite:`1879, Chapter II <petersen:1879>`).

2. Unambiguous Right-Triangle HL (D.43) vs. General SSA Bifurcation (D.44)
--------------------------------------------------------------------------

The contrast between :ref:`D.43 <D.43>` and :ref:`D.44 <D.44>` (illustrated interactively in ``data_03_triangle_species.svg``) showcases Euclid's command of :term:`diorismos <diorismos>`:

* In :ref:`D.43 <D.43>`, $\angle BAC = 90^\circ$ is opposite the hypotenuse $BC$, while the ratio $BC : BA$ ($> 1$ by :just:`[I.19] <I.19>`) is given. Since the remaining angle $\angle ACB$ is *necessarily acute* (:just:`[I.17] <I.17>`), inscribing $DG$ in the Thales semicircle $DGE$ (:just:`[III.31] <III.31>`) yields a **single, unambiguous** species (:just:`[VI.7] <VI.7>`).

* In :ref:`D.44 <D.44>`, $\angle ABC$ is given while the ratio $AB : AC$ of the sides about *another* angle $\angle BAC$ is given (**SSA**). When $AC < AB$ ($AC \ge AB \sin B$), the circle $(A, AC)$ cuts ray $BC$ in **two distinct points** $C_1, C_2$ symmetric across the altitude foot $P$, with $\angle AC_1 B + \angle AC_2 B = 180^\circ$! Euclid's proof drops the altitude $AD \perp BC$, reduces $\triangle ADC$ to :ref:`D.43 <D.43>`, and handles the acute and obtuse branches separately (`χωρὶς δὲ τοῦ συμπτώματος`), matching :just:`[VI.7] <VI.7>`.

3. Angle-Bisector Harmonic Reduction (D.45–D.46) vs. Simson's Construction
--------------------------------------------------------------------------

Propositions :ref:`D.45 <D.45>` and :ref:`D.46 <D.46>` determine the species of $\triangle ABC$ from one angle and the ratio $(BA + AC) : BC$ of the sum of two sides to the third side:

* **Euclid's Proof via Elements VI.3**: Bisecting $\angle BAC$ by $AD$ gives $BA : AC = BD : DC$ (:just:`[VI.3] <VI.3>`), whence *alternando* and *componendo* $(BA + AC) : BC = BA : BD$! In :ref:`D.46 <D.46>` (where $\angle ABC$ is given), $\angle ABD$ lies *between* $BA$ and $BD$, so :ref:`D.41 <D.41>` applies immediately without ambiguity. In :ref:`D.45 <D.45>` (where $\angle BAC$ is given), $\angle BAD = \frac{1}{2}\angle BAC$ is opposite $BD$; since $BD < BC$ and $\angle ADB = \angle DAC + \angle C > \angle BAD$, $\angle ABD$ can actually take two supplementary-like configurations only up to swapping $AB$ and $AC$!

* **Simson's Isosceles-Extension Proof & Added Prop. L**: :person:`Simson <simson>` (:cite:`Props. XLVIII–L, pp. 394–397, 463 <simson:1762>`) noted that extending $CA$ to $E$ with $AE = AB$ makes $EC = BA + AC$ directly and $\angle AEB = \frac{1}{2}\angle BAC$, reducing :ref:`D.45 <D.45>` (`Simson XLVIII`) cleanly to :ref:`D.44 <D.44>` on $\triangle EBC$ and inspiring Simson's companion `Prop. L` for the **difference** of the sides $(BA - AC) : BC$ (via cutting off $AE' = AB$ internally).

4. Polygon Triangulation & Quadratic Area-to-Side Extraction (D.47–D.55)
------------------------------------------------------------------------

The second half of Unit 3 (:ref:`D.47 <D.47>`–:ref:`D.55 <D.55>`) links **1D linear segments** to **2D rectilinear areas**:

* :ref:`D.47 <D.47>` proves that every species-given $n$-gon triangulates into $(n-2)$ species-given triangles by ear-clipping diagonals (:ref:`D.41 <D.41>`).

* :ref:`D.48 <D.48>`–:ref:`D.51 <D.51>` establish that any two species-given figures on the same or ratio-given segments have a **given area ratio**, culminating in :ref:`D.52 <D.52>` (*species-given figure on a magnitude-given segment is given in area*, calibrated against the unit square $AB^2$).

* :ref:`D.54 <D.54>` and :ref:`D.55 <D.55>` invert the quadratic scaling map $S \propto x^2$! Using :ref:`D.24 <D.24>` (which extracted the square root of a ratio via the geometric mean :just:`[VI.13] <VI.13>`), :ref:`D.54 <D.54>` deduces linear side-ratios from area-ratios, and :ref:`D.55 <D.55>` proves the grand converse of :ref:`D.52 <D.52>`: **any figure given both in species and in magnitude has all its sides given in magnitude**—the exact analytical counterpart of :just:`[Elements VI.25] <VI.25>` (*constructing a figure similar to one given figure and equal in area to another*).

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.39 <D.39>` (Prop. XLII) — *Elements G-Index*: ``G.29, G.47`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Construction of Triangles (SSS) · *Altshiller-Court (1952)*: § 13 (SSS Construction)
* :ref:`D.40 <D.40>` (Prop. XLIII) — *Elements G-Index*: ``G.59, G.213`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Method of Similarity (AAA) · *Altshiller-Court (1952)*: § 44 (Method of Similitude)
* :ref:`D.41 <D.41>` (Prop. XLIV) — *Elements G-Index*: ``G.215`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Method of Similarity (SAS) · *Altshiller-Court (1952)*: § 44 (Method of Similitude)
* :ref:`D.42 <D.42>` (Prop. XLV) — *Elements G-Index*: ``G.45, G.47, G.214`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Method of Similarity (SSS-Ratio) · *Altshiller-Court (1952)*: § 45
* :ref:`D.43 <D.43>` (Prop. XLVI) — *Elements G-Index*: ``G.79, G.216`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Method of Similarity (Right-HL) · *Altshiller-Court (1952)*: § 14 (Right Triangle HL)
* :ref:`D.44 <D.44>` (Prop. XLVII) — *Elements G-Index*: ``G.37, G.216`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Method of Similarity (SSA Bifurcation) · *Altshiller-Court (1952)*: § 15 (Ambiguous Case SSA)
* :ref:`D.45 <D.45>` (Prop. XLVIII) — *Elements G-Index*: ``G.25, G.59`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Auxiliary Isosceles Extension · *Altshiller-Court (1952)*: § 53 (Sum of Two Sides)
* :ref:`D.46 <D.46>` (Prop. XLIX) — *Elements G-Index*: ``G.25, G.31, G.59`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Auxiliary Isosceles Extension · *Altshiller-Court (1952)*: § 53 (Sum of Two Sides)
* :ref:`D.47 <D.47>` (Prop. LI) — *Elements G-Index*: ``G.59, G.232`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Polygon Triangulation
* :ref:`D.48 <D.48>` (Prop. LII) — *Elements G-Index*: ``G.66, G.210, G.213`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Ratio of Altitudes
* :ref:`D.49 <D.49>` (Prop. LIII) — *Elements G-Index*: ``G.232`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Polygon Triangulation
* :ref:`D.50 <D.50>` (Prop. LIV) — *Elements G-Index*: ``G.221, G.231, G.232`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Duplicate Ratio Scaling
* :ref:`D.51 <D.51>` (Prop. LV) — *Elements G-Index*: ``G.229, G.232`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Similarity Bridge
* :ref:`D.52 <D.52>` (Prop. LVI) — *Elements G-Index*: ``G.75`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Square Reference Unit
* :ref:`D.53 <D.53>` (Prop. LVII) — *Elements G-Index*: ``G.205`` · *Pappus*: Synagoge VII.7
* :ref:`D.54 <D.54>` (Prop. LIX) — *Elements G-Index*: ``G.229, G.232`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Mean Proportional Extraction
* :ref:`D.55 <D.55>` (Prop. LX) — *Elements G-Index*: ``G.75, G.229`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Similarity + Quadratic Scaling · *Altshiller-Court (1952)*: § 49 (Constructing a Figure of Given Species & Area)


----


.. rubric:: Section 4

:order: 40
:type: chapter
:canonical_id: D.unit.4
:folio: Menge pp. 98–126
:book: Propositions 56–67: Areas, Quadratics & Cosines
:description: Equiangular parallelograms and parabolic division of areas (D.56–D.57), quadratic root extraction via elliptic and hyperbolic application of areas (D.58–D.59) and gnomons (D.60), altitude-to-base ratios (D.61–D.63), generalized Law of Cosines projections in obtuse and acute triangles (D.64–D.65), area-product law BD·BC : △ABC (D.66), and the algebraic identity (a+b)² − c² (D.67).

.. _data-unit-4-en:

==================================================================================
Application of Areas, Quadratics & Cosine Projections (Propositions 56–67)
==================================================================================

*Geometric Algebra of Parabolic, Elliptic & Hyperbolic Areas and Oblique Triangle Projections* — **D.56–D.67 (Simson LXI–LXXXIV) · Menge (1896) pp. 98–126**

.. note::

   **Edition Track (English)**: Equiangular parallelograms and parabolic division of areas (D.56–D.57), quadratic root extraction via elliptic and hyperbolic application of areas (D.58–D.59) and gnomons (D.60), altitude-to-base ratios (D.61–D.63), generalized Law of Cosines projections in obtuse and acute triangles (D.64–D.65), area-product law BD·BC : △ABC (D.66), and the algebraic identity (a+b)² − c² (D.67). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

:order: 42
:type: summary
:canonical_id: D.unit.4
:folio: Menge pp. 98–126
:book: Propositions 56–67: Areas, Quadratics & Cosines

.. _data-unit-4-summary:

=======================================================================================================
Application of Areas, Quadratics & Cosine Projections (Propositions 56–67) — Analytical Summary
=======================================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Equiangular parallelograms and parabolic division of areas (D.56–D.57), quadratic root extraction via elliptic and hyperbolic application of areas (D.58–D.59) and gnomons (D.60), altitude-to-base ratios (D.61–D.63), generalized Law of Cosines projections in obtuse and acute triangles (D.64–D.65), area-product law BD·BC : △ABC (D.66), and the algebraic identity (a+b)² − c² (D.67).

* **Scope**: 12 propositions (D.56–D.67 (Simson LXI–LXXXIV), *Menge* pp. 98–126).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Overview (D.56–D.67 (Simson LXI–LXXXIV))
----------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 12 38 28 12

   * - ID
     - Simson
     - Functional Signature
     - Key Dependencies
     - Tracks
   * - :ref:`D.56 <D.56>`
     - Prop. LXIII
     - ``Given(Equiangular(P1, P2), Ratio(P1 : P2) = k) -> Determined(s1 : t1 = t2 : (s2 / k))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - :ref:`English <D.56>` · :ref:`Greek <D.56.el>`
   * - :ref:`D.57 <D.57>`
     - Prop. LXI
     - ``Given(Mag(Area S), Mag(Base a), Mag(Angle theta)) -> Determined(Mag(Breadth x))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 52] <D.52>`, :just:`[I.31] <I.31>`, :just:`[I.46] <I.46>`, :just:`[VI.1] <VI.1>`
     - :ref:`English <D.57>` · :ref:`Greek <D.57.el>`
   * - :ref:`D.58 <D.58>`
     - Prop. LXXXIII
     - ``Given(Mag(S), Mag(a), Species(Defect)) -> Determined(Roots of a*x - c*x^2 = S) [diorismos]``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.5] <II.5>`, :just:`[VI.24] <VI.24>`, :just:`[VI.27] <VI.27>`, :just:`[VI.28] <VI.28>`
     - :ref:`English <D.58>` · :ref:`Greek <D.58.el>`
   * - :ref:`D.59 <D.59>`
     - Prop. LXXXIV
     - ``Given(Mag(S), Mag(a), Species(Excess)) -> Determined(Positive root of a*x + c*x^2 = S)``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.6] <II.6>`, :just:`[VI.24] <VI.24>`, :just:`[VI.29] <VI.29>`
     - :ref:`English <D.59>` · :ref:`Greek <D.59.el>`
   * - :ref:`D.60 <D.60>`
     - Prop. LXXXII
     - ``Given(Species(P), Mag(Area(P)), Mag(Gnomon G)) -> Determined(Mag(Sides of P +/- G))``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 55] <D.55>`, :just:`[VI.24] <VI.24>`
     - :ref:`English <D.60>` · :ref:`Greek <D.60.el>`
   * - :ref:`D.61 <D.61>`
     - Prop. LXIX
     - ``Given(Species(P on CB), Angle(CD), Ratio(Area(P) : Area(CD))) -> Determined(Species(CD))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 49] <D.49>`, :just:`[I.13] <I.13>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`
     - :ref:`English <D.61>` · :ref:`Greek <D.61.el>`
   * - :ref:`D.62 <D.62>`
     - Prop. LXX
     - ``Given(Ratio(AB : CD), Species(AEB on AB), Angle(DF), Ratio(AEB : DF)) -> Determined(Species(DF))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 50] <D.50>`, :just:`[Data 61] <D.61>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.62>` · :ref:`Greek <D.62.el>`
   * - :ref:`D.63 <D.63>`
     - Omitted (case of Prop. LIII)
     - ``Given(Species(△ABC)) -> Determined(Ratio(a^2 : △ABC), Ratio(b^2 : △ABC), Ratio(c^2 : △ABC))``
     - :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`
     - :ref:`English <D.63>` · :ref:`Greek <D.63.el>`
   * - :ref:`D.64 <D.64>`
     - Prop. LXXIV
     - ``Given(ObtuseAngle B) -> Determined(Ratio((b^2 - a^2 - c^2) : △ABC) = -4 cot B)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.12] <II.12>`, :just:`[VI.1] <VI.1>`
     - :ref:`English <D.64>` · :ref:`Greek <D.64.el>`
   * - :ref:`D.65 <D.65>`
     - Prop. LXXV
     - ``Given(AcuteAngle B) -> Determined(Ratio((a^2 + c^2 - b^2) : △ABC) = 4 cot B)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.13] <II.13>`, :just:`[VI.1] <VI.1>`
     - :ref:`English <D.65>` · :ref:`Greek <D.65.el>`
   * - :ref:`D.66 <D.66>`
     - Prop. LXII Cor.
     - ``Given(Angle A) -> Determined(Ratio((AB * AC) : Area(△ABC)) = 2 / sin A)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.1] <VI.1>`
     - :ref:`English <D.66>` · :ref:`Greek <D.66.el>`
   * - :ref:`D.67 <D.67>`
     - Prop. LXXVI
     - ``Given(Angle A) -> Determined(Ratio(((b + c)^2 - a^2) : △ABC) = 4*(1 + cos A) / sin A)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 50] <D.50>`, :just:`[Data 66] <D.66>`, :just:`[I.5] <I.5>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`, :just:`[I.32] <I.32>`, :just:`[II.6] <II.6>`, :just:`[VI.2] <VI.2>`, :just:`[VI.16] <VI.16>`
     - :ref:`English <D.67>` · :ref:`Greek <D.67.el>`

Computational Primitives (``geometor.model`` & SymPy)
-----------------------------------------------------

* :ref:`D.56 <D.56>` (*Prop. LXIII*): Reduction of non-equal equiangular parallelogram areas to reciprocal sides (`Elements VI.14`) by scaling side BC -> BG.
* :ref:`D.57 <D.57>` (*Prop. LXI*): Linear division of area (`parabolē`, `Elements I.44`): x = S / (a * sin(theta)).
* :ref:`D.58 <D.58>` (*Prop. LXXXIII*): Quadratic solver for elliptic application (`Elements VI.28` + `II.5` gnomon completion) over Q(sqrt((a/2)^2 - S/c)).
* :ref:`D.59 <D.59>` (*Prop. LXXXIV*): Unconditional quadratic solver (`Elements VI.29` + `II.6`) yielding exact radical / Q(phi) positive root.
* :ref:`D.60 <D.60>` (*Prop. LXXXII*): Since P +/- G preserves species (`Elements VI.24`) and has given area (`D.3`/`D.4`), `D.55` gives new sides, `D.4` gives gnomon widths.
* :ref:`D.61 <D.61>` (*Prop. LXIX*): Compare AFCB with auxiliary parallelogram FB (`D.49`), shear CD to equal-base KB (`I.35`, `VI.1`), then solve △LCK (`D.40`) for LC : CB.
* :ref:`D.62 <D.62>` (*Prop. LXX*): Describe parallelogram AG ~ DF on AB (`VI.18`); `D.50` + `D.8` give Area(AEB) : Area(AG), reducing directly to `D.61`!
* :ref:`D.63 <D.63>` (*Omitted (case of Prop. LIII)*): Direct specialization of `D.49` pairing △ABC with the squares on its sides (omitted as corollarial by Simson).
* :ref:`D.64 <D.64>` (*Prop. LXXIV*): Elements II.12 gives AC^2 - (AB^2 + BC^2) = 2*BC*BD; right △ABD is given in species (`D.40`), fixing 2*BC*BD : (1/2*BC*AD) = 4*BD : AD!
* :ref:`D.65 <D.65>` (*Prop. LXXV*): Elements II.13 gives (AB^2 + BC^2) - AC^2 = 2*BC*BD; right △ABD has given ratio BD : AD (`D.40`), fixing 4*BD : AD!
* :ref:`D.66 <D.66>` (*Prop. LXII Cor.*): Drop altitude BD perp AC: right △ABD has given AB : BD (`D.40`), and Rect(AB, AC) : △ABC = 2*AB : BD.
* :ref:`D.67 <D.67>` (*Prop. LXXVI*): Extend BA to AD = AC and BE || AC: `(BA+AC)^2 - BC^2 = Rect(DC, CE)` (`II.6`), whose ratio to `Rect(BA, AC)` (`D.50`) and `△ABC` (`D.66`) is given!


:order: 43
:type: notes
:canonical_id: D.unit.4
:folio: Menge pp. 98–126
:book: Propositions 56–67: Areas, Quadratics & Cosines

.. _data-unit-4-notes:

==================================================================================================================
Application of Areas, Quadratics & Cosine Projections (Propositions 56–67) — Philological & Critical Notes
==================================================================================================================

1. Geometric Algebra of Application of Areas: Parabolē, Elleipsis, and Hyperbolē (D.57–D.60)
--------------------------------------------------------------------------------------------

Unit 4 (:ref:`D.56 <D.56>`–:ref:`D.67 <D.67>`) translates the constructive **application of areas** (*παραβολὴ τῶν χωρίων*, :cite:`Elements II.5–6 & VI.27–29 <heath:1926>`) into analytical root-determination theorems:

* **Parabolē** (:term:`παραβολή <parabole>`, :ref:`D.57 <D.57>`): Exact application $a \cdot x = S$ in a given angle $\\theta$ solves the linear equation $x = S / (a \sin\\theta)$.

* **Elleipsis** (:term:`ἔλλειψις <elleipsis>`, :ref:`D.58 <D.58>`): Elliptic application $(a - x)\cdot (\lambda x) = S$ solves the quadratic equation $\lambda x^2 - \lambda a x + S = 0$ by completing the gnomon on the half-segment $a/2$ (:just:`[II.5] <II.5>`, :just:`[VI.28] <VI.28>`), subject to the discriminant *diorismos* $S \le \lambda (a/2)^2$ (:just:`[VI.27] <VI.27>`).

* **Hyperbolē** (:term:`ὑπερβολή <hyperbole>`, :ref:`D.59 <D.59>`): Hyperbolic application $(a + x)\cdot (\lambda x) = S$ solves $\lambda x^2 + \lambda a x = S$ unconditionally via :just:`[II.6] <II.6>` and :just:`[VI.29] <VI.29>`. When $S = a^2$ and the excess is a square ($\lambda = 1$), $x(a + x) = a^2$ determines the **golden section** $x = a/\phi \in \mathbb{Q}(\phi)$ (:just:`[II.11] <II.11>`, :just:`[VI.30] <VI.30>`)!

As :person:`Proclus <proclus>` (:cite:`In Eucl. 419.15 <proclus:1873>`) and :person:`Pappus <pappus>` record, :person:`Apollonius of Perga <apollonius>` borrowed the very names *parabola*, *ellipse*, and *hyperbola* directly from this Pythagorean-Euclidean triad.

2. Area-to-Species Bridges (D.61–D.63) & Textual Notes
------------------------------------------------------

Propositions :ref:`D.61 <D.61>` and :ref:`D.62 <D.62>` bridge area-ratios back to species: if a parallelogram $CD$ in a given angle is applied either to a side of a species-given figure (:ref:`D.61 <D.61>`) or to a segment having a given ratio to a side of a species-given figure (:ref:`D.62 <D.62>`), and the area ratio is given, then $CD$ itself is given in species. :person:`Simson <simson>` (:cite:`Props. LXIX–LXX, p. 464 <simson:1762>`) retained both (`D.61–62`) while omitting :ref:`D.63 <D.63>` (*species-given figures on the three sides of a species-given triangle have given ratios to one another*) as an immediate corollary of :ref:`D.51 <D.51>`; :person:`Menge <menge>` preserved :ref:`D.63 <D.63>` from :cite:`Vat. gr. 190 <vat-gr-190>`.

3. The Euclidean Law of Cosines, Sine Area Formula & Half-Angle Excess (D.64–D.67)
----------------------------------------------------------------------------------

Propositions :ref:`D.64 <D.64>`–:ref:`D.67 <D.67>` form the trigonometric heart of Greek plane geometry (visualized in ``data_05_cosine_projection.svg``):

* **Obtuse & Acute Cosine Laws** (:ref:`D.64 <D.64>`–:ref:`D.65 <D.65>`): By combining :just:`[Elements II.12] <II.12>` and :just:`[II.13] <II.13>` with species-given right-triangle projections (:ref:`D.40 <D.40>`), Euclid proves that $|a^2 + c^2 - b^2| : (a c) = 2\, BD : AB = 2|\cos B|$ is **given** whenever $\angle B$ is given—without ever needing symbolic trigonometric tables!

* **Sine Area Law** (:ref:`D.66 <D.66>`): Proves $(AB \cdot BC) : \\triangle ABC = 2/\sin B$ is given whenever $\angle B$ is given.

* **Compound-Side Quadratic Excess** (:ref:`D.67 <D.67>`, `Simson Prop. LXXVI`): Proves $((b + c)^2 - a^2) : \\triangle ABC$ is given whenever $\angle A$ is given. Algebraically, $(b+c)^2 - a^2 = 2bc(1 + \cos A)$ while $\\triangle ABC = \frac{1}{2}bc\sin A$, so their constant ratio is $4(1+\cos A)/\sin A = 4\cot(A/2)$! In :cite:`Vat. gr. 190 <vat-gr-190>` (:cite:`Menge pp. 122–126 <menge:1896>`), Euclid establishes this synthetically without trigonometry by extending $BA$ to $D$ with $AD = AC$ and applying :just:`[II.6] <II.6>`.

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.56 <D.56>` (Prop. LXIII) — *Elements G-Index*: ``G.210, G.225`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Application of Areas
* :ref:`D.57 <D.57>` (Prop. LXI) — *Elements G-Index*: ``G.58, G.75, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Parabolic Application of Areas · *Altshiller-Court (1952)*: § 47 (Transformation of Areas)
* :ref:`D.58 <D.58>` (Prop. LXXXIII) — *Elements G-Index*: ``G.87, G.236, G.239, G.240`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Elliptic Application of Areas (Quadratic) · *Altshiller-Court (1952)*: § 50 (Elliptic Application)
* :ref:`D.59 <D.59>` (Prop. LXXXIV) — *Elements G-Index*: ``G.88, G.236, G.241`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Hyperbolic Application of Areas (Quadratic) · *Altshiller-Court (1952)*: § 51 (Hyperbolic Application / Golden Section)
* :ref:`D.60 <D.60>` (Prop. LXXXII) — *Elements G-Index*: ``G.236`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Gnomonic Scaling
* :ref:`D.61 <D.61>` (Prop. LXIX) — *Elements G-Index*: ``G.37, G.56, G.58, G.64, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Area-to-Aspect Conversion
* :ref:`D.62 <D.62>` (Prop. LXX) — *Elements G-Index*: ``G.229, G.232`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Area-to-Aspect Conversion
* :ref:`D.63 <D.63>` (Omitted (case of Prop. LIII)) — *Elements G-Index*: ``G.75`` · *Pappus*: Synagoge VII.8
* :ref:`D.64 <D.64>` (Prop. LXXIV) — *Elements G-Index*: ``G.35, G.59, G.94, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Cosine Projection Law
* :ref:`D.65 <D.65>` (Prop. LXXV) — *Elements G-Index*: ``G.35, G.59, G.95, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Cosine Projection Law
* :ref:`D.66 <D.66>` (Prop. LXII Cor.) — *Elements G-Index*: ``G.35, G.70, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Trigonometric Area Formula
* :ref:`D.67 <D.67>` (Prop. LXXVI) — *Elements G-Index*: ``G.25, G.37, G.58, G.59, G.88, G.211, G.227`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Isosceles Auxiliary Extension + Secant-Product


----


.. rubric:: Section 5

:order: 50
:type: chapter
:canonical_id: D.unit.5
:folio: Menge pp. 126–164
:book: Propositions 68–83: Proportional Figures
:description: Compound ratio calculus for equiangular and supplementary-angle parallelograms and triangles (D.68–D.75), dropped-altitude ratios in species-given triangles (D.76), duplicated/corollarial area-species bridges (D.77–D.78), inscribed circle-triangle similarity lemmas and area-product determination (D.79–D.80), and four-line proportional transformations (D.81–D.83).

.. _data-unit-5-en:

=========================================================================================
Proportional Parallelograms, Triangles & Four-Line Relations (Propositions 68–83)
=========================================================================================

*Compound Side-Ratios, Reciprocal Proportions, Simson's Lemma, and Four-Line Cross-Multiplications* — **D.68–D.83 (Simson L–LXXVIII) · Menge (1896) pp. 126–164**

.. note::

   **Edition Track (English)**: Compound ratio calculus for equiangular and supplementary-angle parallelograms and triangles (D.68–D.75), dropped-altitude ratios in species-given triangles (D.76), duplicated/corollarial area-species bridges (D.77–D.78), inscribed circle-triangle similarity lemmas and area-product determination (D.79–D.80), and four-line proportional transformations (D.81–D.83). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

:order: 52
:type: summary
:canonical_id: D.unit.5
:folio: Menge pp. 126–164
:book: Propositions 68–83: Proportional Figures

.. _data-unit-5-summary:

==============================================================================================================
Proportional Parallelograms, Triangles & Four-Line Relations (Propositions 68–83) — Analytical Summary
==============================================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Compound ratio calculus for equiangular and supplementary-angle parallelograms and triangles (D.68–D.75), dropped-altitude ratios in species-given triangles (D.76), duplicated/corollarial area-species bridges (D.77–D.78), inscribed circle-triangle similarity lemmas and area-product determination (D.79–D.80), and four-line proportional transformations (D.81–D.83).

* **Scope**: 16 propositions (D.68–D.83 (Simson L–LXXVIII), *Menge* pp. 126–164).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Overview (D.68–D.83 (Simson L–LXXVIII))
---------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 12 38 28 12

   * - ID
     - Simson
     - Functional Signature
     - Key Dependencies
     - Tracks
   * - :ref:`D.68 <D.68>`
     - Prop. LXV
     - ``Given(Equiangular(P1, P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 56] <D.56>`, :just:`[I.31] <I.31>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - :ref:`English <D.68>` · :ref:`Greek <D.68.el>`
   * - :ref:`D.69 <D.69>`
     - Prop. LXVI
     - ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.12] <I.12>`, :just:`[I.23] <I.23>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`
     - :ref:`English <D.69>` · :ref:`Greek <D.69.el>`
   * - :ref:`D.70 <D.70>`
     - Props. LXVII–LXVIII
     - ``Given(Angle(P1), Angle(P2), Ratio(s1 : t1), Ratio(s2 : t2)) -> Determined(Ratio(P1 : P2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`, :just:`[VI.23] <VI.23>`
     - :ref:`English <D.70>` · :ref:`Greek <D.70.el>`
   * - :ref:`D.71 <D.71>`
     - Prop. LXVIII Cor. 1
     - ``Given(Angle(A), Angle(D), Ratio(c1 : c2), Ratio(b1 : b2)) -> Determined(Ratio(△1 : △2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`
     - :ref:`English <D.71>` · :ref:`Greek <D.71.el>`
   * - :ref:`D.72 <D.72>`
     - Prop. LXVIII Cor. 2
     - ``Given(Ratio(b1 : b2), Ratio(d1 : d2), Angle(phi1), Angle(phi2)) -> Determined(Ratio(△1 : △2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[I.41] <I.41>`
     - :ref:`English <D.72>` · :ref:`Greek <D.72.el>`
   * - :ref:`D.73 <D.73>`
     - Prop. LXIV (pt. 2)
     - ``Given(Angle(P1), Angle(P2), CB:FG = EF:CK, Ratio(AC:CK)) -> Determined(Ratio(P1 : P2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[Data 70] <D.70>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - :ref:`English <D.73>` · :ref:`Greek <D.73.el>`
   * - :ref:`D.74 <D.74>`
     - Prop. LXIV (pt. 1; cf. LXIII)
     - ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2)) -> Determined(CB : FG = EF : K with GivenRatio(AC : K))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - :ref:`English <D.74>` · :ref:`Greek <D.74.el>`
   * - :ref:`D.75 <D.75>`
     - Prop. LXIV Cor.
     - ``Given(Angle(A), Angle(D), Ratio(△1 : △2)) -> Determined(AB : DE = DF : K with GivenRatio(AC : K))``
     - :just:`[Data 74] <D.74>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`
     - :ref:`English <D.75>` · :ref:`Greek <D.75.el>`
   * - :ref:`D.76 <D.76>`
     - Prop. L
     - ``Given(Species(△ABC), AD perp BC) -> Determined(Ratio(AD : BC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`
     - :ref:`English <D.76>` · :ref:`Greek <D.76.el>`
   * - :ref:`D.77 <D.77>`
     - Omitted (dup. of Prop. LIX / D.54)
     - ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(s(A) : s(B)))``
     - :just:`[Data 54] <D.54>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.77>` · :ref:`Greek <D.77.el>`
   * - :ref:`D.78 <D.78>`
     - Omitted (case of Prop. LXX / D.62)
     - ``Given(Species(A), Ratio(A : B), Ratio(s(A) : s1(B)), Angle(B)) -> Determined(Species(B))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 62] <D.62>`, :just:`[VI.14] <VI.14>`
     - :ref:`English <D.78>` · :ref:`Greek <D.78.el>`
   * - :ref:`D.79 <D.79>`
     - Prop. LXXVII Cor. 1
     - ``Given(∠BAC = ∠EDF, BC : h_A = EF : h_D) -> Determined(△ABC ~ △DEF)``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data Def. 7] <D.def.7>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[III.21] <III.21>`, :just:`[VI.4] <VI.4>`
     - :ref:`English <D.79>` · :ref:`Greek <D.79.el>`
   * - :ref:`D.80 <D.80>`
     - Prop. LXXVIII
     - ``Given(Angle A, Ratio((b*c) : a^2)) -> Determined(Species(△ABC))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 66] <D.66>`, :just:`[Data 68] <D.68>`, :just:`[Data 79] <D.79>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`
     - :ref:`English <D.80>` · :ref:`Greek <D.80.el>`
   * - :ref:`D.81 <D.81>`
     - Prop. LXXI
     - ``Given(B^2 = A*C, E^2 = D*F) -> (Given(A:D, C:F) -> Given(B:E)) & (Given(A:D, B:E) -> Given(C:F))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 50] <D.50>`, :just:`[Data 54] <D.54>`, :just:`[Data 70] <D.70>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.81>` · :ref:`Greek <D.81.el>`
   * - :ref:`D.82 <D.82>`
     - Prop. LXXII
     - ``Given(A : B = C : D, Ratio(B : E) = k) -> Determined(Ratio(D : F) = k when A : E = C : F)``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.22] <V.22>`
     - :ref:`English <D.82>` · :ref:`Greek <D.82.el>`
   * - :ref:`D.83 <D.83>`
     - Prop. LXXIII
     - ``Given(A * D = B * E, Ratio(C : E) = k) -> Determined(D : C = B : (A / k))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 68] <D.68>`, :just:`[V.16] <V.16>`, :just:`[V.23] <V.23>`, :just:`[VI.16] <VI.16>`
     - :ref:`English <D.83>` · :ref:`Greek <D.83.el>`

Computational Primitives (``geometor.model`` & SymPy)
-----------------------------------------------------

* :ref:`D.68 <D.68>` (*Prop. LXV*): Apply auxiliary parallelogram EG on EB equal to CD (`VI.1`), then cancel shared angle via reciprocal sides (`Elements VI.14`).
* :ref:`D.69 <D.69>` (*Prop. LXVI*): Shear P1 at constant base & height (`Elements I.35`) to match Angle(P2); `D.40` gives oblique-side ratio, reducing to `D.68`.
* :ref:`D.70 <D.70>` (*Props. LXVII–LXVIII*): Equiangular compound-ratio case (`Elements VI.14`/`VI.23`), generalized to arbitrary given angles by shearing (`I.35` + `D.40`).
* :ref:`D.71 <D.71>` (*Prop. LXVIII Cor. 1*): Complete each triangle into its double parallelogram (`I.34`, `V.15`) and invoke `D.70`.
* :ref:`D.72 <D.72>` (*Prop. LXVIII Cor. 2*): Construct parallelograms along the oblique direction `AG`/`DH` equal to twice each triangle (`I.34`/`I.41`) and apply `D.70`.
* :ref:`D.73 <D.73>` (*Prop. LXIV (pt. 2)*): Converse of `D.74` linking reciprocal-side fourth proportionals (`VI.14`) to parallelogram area ratios (text repaired by Simson Prop. LXIV).
* :ref:`D.74 <D.74>` (*Prop. LXIV (pt. 1; cf. LXIII)*): Generalization of `D.56` from equiangular parallelograms to arbitrary given angles via equal-area shear (`I.35` + `D.40`).
* :ref:`D.75 <D.75>` (*Prop. LXIV Cor.*): Half-parallelogram specialization of `D.74` (`Elements I.34`, `V.15`).
* :ref:`D.76 <D.76>` (*Prop. L*): Right △ABD has given Angle B (`Def. 3`), hence Species(△ABD) by `D.40`, giving AD : AB; compose with AB : BC via `D.8`.
* :ref:`D.77 <D.77>` (*Omitted (dup. of Prop. LIX / D.54)*): Textual doublet of `D.54` preserved in the Greek archetype (`Vat. gr. 190`) and omitted by Simson.
* :ref:`D.78 <D.78>` (*Omitted (case of Prop. LXX / D.62)*): Immediate corollary of `D.62` (once both side ratios and angle of parallelogram B are given, B is given in species).
* :ref:`D.79 <D.79>` (*Prop. LXXVII Cor. 1*): Pure similarity lemma for `D.80`: inscribe △EDF in equal-angle segment on EF (`III.21`), cut at equal altitude, establish congruence/similarity.
* :ref:`D.80 <D.80>` (*Prop. LXXVIII*): Since AB*AC : △ABC is given (`D.66`) and △ABC = 1/2*BC*h_A, BC^2 : BC*h_A = BC : h_A is given; prototype triangle matches by Lemma `D.79`!
* :ref:`D.81 <D.81>` (*Prop. LXXI*): Rectangles A*C = B^2 and D*F = E^2 (`VI.17`): `D.70` gives B^2 : E^2, `D.54` extracts B : E (and `D.50` + `D.68` gives converse).
* :ref:`D.82 <D.82>` (*Prop. LXXII*): Projective rescaling of second and fourth proportionals: A/(B/k) = C/(D/k) (`Elements V.22`).
* :ref:`D.83 <D.83>` (*Prop. LXXIII*): Perturbed four-line proportion (`Elements V.23` / `VI.16`): A*D = B*(C/k) <-> D*k*A... -> D : C = B : (k*A).


:order: 53
:type: notes
:canonical_id: D.unit.5
:folio: Menge pp. 126–164
:book: Propositions 68–83: Proportional Figures

.. _data-unit-5-notes:

=========================================================================================================================
Proportional Parallelograms, Triangles & Four-Line Relations (Propositions 68–83) — Philological & Critical Notes
=========================================================================================================================

1. Compound Ratios & Oblique Shear Invariance (D.68–D.75)
---------------------------------------------------------

Unit 5 (:ref:`D.68 <D.68>`–:ref:`D.83 <D.83>`) lifts the theory of equiangular parallelograms (:just:`[Elements VI.14] <VI.14>`, :just:`[VI.23] <VI.23>`) to **arbitrary given angles**. Euclid's key geometric operator in :ref:`D.69 <D.69>`, :ref:`D.70 <D.70>`, :ref:`D.73 <D.73>`, and :ref:`D.74 <D.74>` is an area-preserving **Cavalieri shear** (:just:`[I.35] <I.35>`) on a fixed base $BC$: shearing a parallelogram from given angle $\\theta_1$ to given angle $\\theta_2$ introduces a corner triangle $\\triangle ABP$ whose angles are given, so its slant-side ratio $BA : BP = \sin\\theta_2 / \sin\\theta_1$ is given by :ref:`D.40 <D.40>`!

In his philological commentary (:cite:`pp. 464–466 <simson:1762>`), :person:`Robert Simson <simson>` showed that late Greek scribes had slightly garbled the reciprocally-proportional clauses of :ref:`D.73 <D.73>` and :ref:`D.74 <D.74>`, and consolidated them cleanly in `Simson Props. LXIII–LXVII`.

2. Manuscript Doublets (D.77–D.78) & the Inscribed-Angle Locus Theorem (D.79–D.80)
----------------------------------------------------------------------------------

* **Doublets in Codex P**: :ref:`D.77 <D.77>` repeats the enunciation of :ref:`D.54 <D.54>` with an alternative square-calibration proof, and :ref:`D.78 <D.78>` specializes :ref:`D.62 <D.62>` to rectangles; :person:`Simson <simson>` omitted both as scholiastic doublets, whereas :person:`Menge <menge>` (:cite:`pp. 148–152 <menge:1896>`) printed them in their traditional numbering so all ancient citations from :person:`Pappus <pappus>` remain intact.

* **The Inscribed-Angle & Parallel-Chord Masterpiece (D.79–D.80)**: :ref:`D.80 <D.80>` (`Simson Prop. LXXVIII`) proves that $\\triangle ABC$ is given in species if $\angle A$ and the ratio $(AB \cdot AC) : BC^2$ are given. Euclid prepares this via the pure locus lemma :ref:`D.79 <D.79>`: two triangles with equal vertex angles $\angle A = \angle D$ and equal base-to-altitude ratios $BC : AG = EF : DH$ can be superposed onto the same circular segment (:just:`[III.21] <III.21>`, :just:`[III.33] <III.33>`), where equal altitudes cut the arc in a parallel line symmetric across the perpendicular bisector! :person:`Simson <simson>` admired this cluster so deeply that he added four companion theorems (`Props. LXXVII, LXXIX–LXXXI`).

3. Four-Line Proportional Permutations & Apollonian Analysis (D.81–D.83)
------------------------------------------------------------------------

Propositions :ref:`D.81 <D.81>`–:ref:`D.83 <D.83>` provide the algebraic rewrite rules for proportions $A : B = C : D$ when one or more terms are replaced by lines having *given ratios* to them. As :person:`Pappus <pappus>` (:cite:`Synagoge Book VII <pappus:synagoge>`) demonstrates across his lemmas to :person:`Apollonius's <apollonius>` *Cutting off of a Ratio* (*Λόγου ἀποτομή*), *Cutting off of an Area* (*Χωρίου ἀποτομή*), and *Determinate Section* (*Διωρισμένη τομή*), :ref:`D.82 <D.82>` and :ref:`D.83 <D.83>` allow an analyst to absorb arbitrary given multiplicative constants into auxiliary segments without breaking a four-term proportion.

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.68 <D.68>` (Prop. LXV) — *Elements G-Index*: ``G.58, G.210, G.225`` · *Pappus*: Synagoge VII.9
* :ref:`D.69 <D.69>` (Prop. LXVI) — *Elements G-Index*: ``G.35, G.48, G.58, G.64`` · *Pappus*: Synagoge VII.9 · *Petersen (1879)*: Shear Transformation
* :ref:`D.70 <D.70>` (Props. LXVII–LXVIII) — *Elements G-Index*: ``G.48, G.64, G.210, G.225, G.235`` · *Pappus*: Synagoge VII.9 · *Petersen (1879)*: Compound Ratio of Sides
* :ref:`D.71 <D.71>` (Prop. LXVIII Cor. 1) — *Elements G-Index*: ``G.58, G.62, G.193`` · *Pappus*: Synagoge VII.9
* :ref:`D.72 <D.72>` (Prop. LXVIII Cor. 2) — *Elements G-Index*: ``G.56, G.58, G.62, G.70`` · *Pappus*: Synagoge VII.9
* :ref:`D.73 <D.73>` (Prop. LXIV (pt. 2)) — *Elements G-Index*: ``G.48, G.64, G.210, G.225`` · *Pappus*: Synagoge VII.9
* :ref:`D.74 <D.74>` (Prop. LXIV (pt. 1; cf. LXIII)) — *Elements G-Index*: ``G.48, G.64, G.210, G.225`` · *Pappus*: Synagoge VII.9
* :ref:`D.75 <D.75>` (Prop. LXIV Cor.) — *Elements G-Index*: ``G.62, G.193`` · *Pappus*: Synagoge VII.9
* :ref:`D.76 <D.76>` (Prop. L) — *Elements G-Index*: ``G.35, G.59`` · *Pappus*: Synagoge VII.7 · *Petersen (1879)*: Altitude-to-Base Invariant
* :ref:`D.77 <D.77>` (Omitted (dup. of Prop. LIX / D.54)) — *Elements G-Index*: ``G.232``
* :ref:`D.78 <D.78>` (Omitted (case of Prop. LXX / D.62)) — *Elements G-Index*: ``G.225``
* :ref:`D.79 <D.79>` (Prop. LXXVII Cor. 1) — *Elements G-Index*: ``G.35, G.124, G.213`` · *Pappus*: Synagoge VII.9 · *Petersen (1879)*: Circumscribed Segment Locus + Parallel Chord · *Altshiller-Court (1952)*: § 10 (Capable Arc Locus)
* :ref:`D.80 <D.80>` (Prop. LXXVIII) — *Elements G-Index*: ``G.35, G.70, G.213, G.227`` · *Pappus*: Synagoge VII.9 · *Petersen (1879)*: Capable Arc + Parallel Strip Locus · *Altshiller-Court (1952)*: § 55 (Given Angle, Base & Product/Altitude)
* :ref:`D.81 <D.81>` (Prop. LXXI) — *Elements G-Index*: ``G.228, G.232`` · *Pappus*: Synagoge VII.9
* :ref:`D.82 <D.82>` (Prop. LXXII) — *Elements G-Index*: ``G.189, G.195, G.205`` · *Pappus*: Synagoge VII.9
* :ref:`D.83 <D.83>` (Prop. LXXIII) — *Elements G-Index*: ``G.195, G.206, G.227`` · *Pappus*: Synagoge VII.9


----


.. rubric:: Section 6

:order: 60
:type: chapter
:canonical_id: D.unit.6
:folio: Menge pp. 164–186
:book: Propositions 84–94: Circles, Chords & Angle Bisectors
:description: Canonical two-line systems xy = A² with x − y = d (D.84), x + y = s (D.85), and x² − y² = C² (D.86); circles given in magnitude and position, inscribed angle loci, and chord/arc determination (D.87–D.89); secant/chord power of a point (D.90–D.92); the celebrated Prop. 93 interior angle-bisector theorem; and its orthogonal chord-reflection corollary (D.94).

.. _data-unit-6-en:

===========================================================================================
Hyperbolic/Elliptic Systems, Circles, Chords & Angle Bisectors (Propositions 84–94)
===========================================================================================

*Canonical Two-Segment Quadratic Systems, Circular Loci, Chord Power, and the Prop. 93 Bisector Theorem* — **D.84–D.94 (Simson LXXXV–C) · Menge (1896) pp. 164–186**

.. note::

   **Edition Track (English)**: Canonical two-line systems xy = A² with x − y = d (D.84), x + y = s (D.85), and x² − y² = C² (D.86); circles given in magnitude and position, inscribed angle loci, and chord/arc determination (D.87–D.89); secant/chord power of a point (D.90–D.92); the celebrated Prop. 93 interior angle-bisector theorem; and its orthogonal chord-reflection corollary (D.94). Switch tabs above for **Greek (Menge 1896)**, **Summary**, or **Notes**.

:order: 62
:type: summary
:canonical_id: D.unit.6
:folio: Menge pp. 164–186
:book: Propositions 84–94: Circles, Chords & Angle Bisectors

.. _data-unit-6-summary:

================================================================================================================
Hyperbolic/Elliptic Systems, Circles, Chords & Angle Bisectors (Propositions 84–94) — Analytical Summary
================================================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Canonical two-line systems xy = A² with x − y = d (D.84), x + y = s (D.85), and x² − y² = C² (D.86); circles given in magnitude and position, inscribed angle loci, and chord/arc determination (D.87–D.89); secant/chord power of a point (D.90–D.92); the celebrated Prop. 93 interior angle-bisector theorem; and its orthogonal chord-reflection corollary (D.94).

* **Scope**: 11 propositions (D.84–D.94 (Simson LXXXV–C), *Menge* pp. 164–186).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Overview (D.84–D.94 (Simson LXXXV–C))
-------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 12 38 28 12

   * - ID
     - Simson
     - Functional Signature
     - Key Dependencies
     - Tracks
   * - :ref:`D.84 <D.84>`
     - Prop. LXXXV
     - ``Given(Angle B, Area(x, y) = S, y - x = d) -> Determined(Mag(x), Mag(y))``
     - :just:`[Data 3] <D.3>`, :just:`[Data 59] <D.59>`, :just:`[I.31] <I.31>`
     - :ref:`English <D.84>` · :ref:`Greek <D.84.el>`
   * - :ref:`D.85 <D.85>`
     - Prop. LXXXVI
     - ``Given(Angle B, Area(x, y) = S, x + y = s) -> Determined(Mag(x), Mag(y)) [diorismos]``
     - :just:`[Data 4] <D.4>`, :just:`[Data 58] <D.58>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`
     - :ref:`English <D.85>` · :ref:`Greek <D.85.el>`
   * - :ref:`D.86 <D.86>`
     - Prop. LXXXIX (cf. LXXXVII–LXXXVIII)
     - ``Given(Angle B, x*y*sin B = S, (y^2 - D) : x^2 = k) -> Determined(Mag(x), Mag(y))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 55] <D.55>`, :just:`[Data 57] <D.57>`, :just:`[Data 58] <D.58>`, :just:`[Data 59] <D.59>`, :just:`[Data 68] <D.68>`, :just:`[II.4] <II.4>`, :just:`[II.6] <II.6>`, :just:`[VI.1] <VI.1>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`
     - :ref:`English <D.86>` · :ref:`Greek <D.86.el>`
   * - :ref:`D.87 <D.87>`
     - Prop. XCI
     - ``Given(CircleRadius R, InscribedAngle theta) -> Determined(Mag(Chord BC = 2*R*sin theta))``
     - :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`, :just:`[Data 40] <D.40>`, :just:`[Data 53] <D.53>`, :just:`[III.21] <III.21>`, :just:`[III.31] <III.31>`
     - :ref:`English <D.87>` · :ref:`Greek <D.87.el>`
   * - :ref:`D.88 <D.88>`
     - Prop. XCII
     - ``Given(CircleRadius R, Mag(Chord BC <= 2R)) -> Determined(Mag(InscribedAngle BAC))``
     - :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 1] <D.1>`, :just:`[Data 3] <D.3>`, :just:`[Data 43] <D.43>`, :just:`[III.21] <III.21>`, :just:`[III.22] <III.22>`, :just:`[III.31] <III.31>`
     - :ref:`English <D.88>` · :ref:`Greek <D.88.el>`
   * - :ref:`D.89 <D.89>`
     - Prop. XCIII
     - ``Given(PosMag(Circle(D, R)), Pos(B on circle), Mag(InscribedAngle BAC)) -> Determined(Pos(C))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 29] <D.29>`, :just:`[III.1] <III.1>`, :just:`[III.20] <III.20>`
     - :ref:`English <D.89>` · :ref:`Greek <D.89.el>`
   * - :ref:`D.90 <D.90>`
     - Prop. XCIV
     - ``Given(PosMag(Circle(O, R)), Pos(D outside)) -> Determined(Pos(DA), Mag(DA = sqrt(OD^2 - R^2)))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 43] <D.43>`, :just:`[Data 53] <D.53>`, :just:`[III.17] <III.17>`, :just:`[III.18] <III.18>`, :just:`[III.31] <III.31>`
     - :ref:`English <D.90>` · :ref:`Greek <D.90.el>`
   * - :ref:`D.91 <D.91>`
     - Prop. XCV
     - ``Given(PosMag(Circle(O, R)), Pos(External D)) -> Determined(Mag(DB * DC = OD^2 - R^2))``
     - :just:`[Data 52] <D.52>`, :just:`[Data 90] <D.90>`, :just:`[III.17] <III.17>`, :just:`[III.36] <III.36>`
     - :ref:`English <D.91>` · :ref:`Greek <D.91.el>`
   * - :ref:`D.92 <D.92>`
     - Prop. XCVI
     - ``Given(PosMag(Circle(O, R)), Pos(Internal D)) -> Determined(Mag(BD * DC = R^2 - OD^2))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 52] <D.52>`, :just:`[III.1] <III.1>`, :just:`[III.35] <III.35>`
     - :ref:`English <D.92>` · :ref:`Greek <D.92.el>`
   * - :ref:`D.93 <D.93>`
     - Prop. XCVII (cf. Prop. XCVIII [Stanhope])
     - ``Given(CircleRadius R, InscribedAngle A, Bisector AD cap BC = E) -> Determined(Ratio((AB+AC):AD), Mag((AB+AC)*ED))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 52] <D.52>`, :just:`[Data 87] <D.87>`, :just:`[III.21] <III.21>`, :just:`[III.26] <III.26>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[VI.3] <VI.3>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`
     - :ref:`English <D.93>` · :ref:`Greek <D.93.el>`
   * - :ref:`D.94 <D.94>`
     - Prop. XCIX (cf. Prop. C [Stewart])
     - ``Given(PosMag(Circle(H, R)), Pos(D on diam BC), ∠DAE = 90°, EF || DA) -> Determined(Pos(F = 2H - D), Mag(AD * EF = |R^2 - HD^2|))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 91] <D.91>`, :just:`[Data 92] <D.92>`, :just:`[I.4] <I.4>`, :just:`[I.26] <I.26>`, :just:`[I.29] <I.29>`, :just:`[III.31] <III.31>`, :just:`[III.35] <III.35>`
     - :ref:`English <D.94>` · :ref:`Greek <D.94.el>`

Computational Primitives (``geometor.model`` & SymPy)
-----------------------------------------------------

* :ref:`D.84 <D.84>` (*Prop. LXXXV*): Canonical difference-and-product solver: x*(x + d)*sin B = S reduces directly to hyperbolic application `D.59`!
* :ref:`D.85 <D.85>` (*Prop. LXXXVI*): Canonical sum-and-product (Vieta) solver: x*(s - x)*sin B = S reduces directly to elliptic application `D.58`!
* :ref:`D.86 <D.86>` (*Prop. LXXXIX (cf. LXXXVII–LXXXVIII)*): Biquadratic system x*y = S', y^2 - k*x^2 = D -> k*x^4 + D*x^2 - S'^2 = 0 solved in radicals via quadratic substitution (`D.59`/`D.58` + `D.55`)!
* :ref:`D.87 <D.87>` (*Prop. XCI*): Draw diameter BD (`Mag(BD) = 2R` by `Def. 5`); join DC (`∠BCD = 90°` by `III.31`, `∠BDC = ∠BAC` by `III.21`); right △BCD given by `D.40` + `D.53`!
* :ref:`D.88 <D.88>` (*Prop. XCII*): Converse of `D.87`: diameter BD = 2R (`Def. 5`), ratio BC : BD given (`D.1`), right △BCD given in species by `D.43`, fixing ∠BDC and supplementary arc angle (`III.22`)!
* :ref:`D.89 <D.89>` (*Prop. XCIII*): Join centre D to B (`D.26`); central ∠BDC = 2·∠BAC (`Elements III.20`) is given, so ray DC (`D.29`) meets Circle(D, R) (`D.25`) at given point C!
* :ref:`D.90 <D.90>` (*Prop. XCIV*): Join centre E to D (`D.26`); semicircle on ED cuts Circle(E, R) at A (`∠EAD = 90°` by `III.31`/`III.18`), fixing Pos(A) and Mag(DA)!
* :ref:`D.91 <D.91>` (*Prop. XCV*): Draw tangent DA (`Mag(DA)` given by `D.90`, `DA^2` given by `D.52`); by `Elements III.36`, Rect(DB, DC) = DA^2 is invariant across all secants!
* :ref:`D.92 <D.92>` (*Prop. XCVI*): Draw diameter FEG through centre E and D: FD = R + ED (`D.3`) and DG = R - ED (`D.4`) are given; by `Elements III.35`, BD*DC = FD*DG!
* :ref:`D.93 <D.93>` (*Prop. XCVII (cf. Prop. XCVIII [Stanhope])*): Masterpiece of Data: chords BC and BD = DC are given (`D.87`); `VI.3` + `V.12` + `△ACE ~ △ADB ~ △BDE` yield (AB+AC):AD = BC:BD and (AB+AC)*ED = BC*BD!
* :ref:`D.94 <D.94>` (*Prop. XCIX (cf. Prop. C [Stewart])*): Produce EF to G on circle: since ∠GAE = ∠DAE = 90° (`I.29`), GE... wait: ∠AEG = 90° -> AG is a diameter through centre H (`III.31`), so △AHD ~= △GHF (`I.26`), fixing HF = HD (`Pos(F)`) and AD*EF = GF*EF (`D.92`/`D.91`)!


:order: 63
:type: notes
:canonical_id: D.unit.6
:folio: Menge pp. 164–186
:book: Propositions 84–94: Circles, Chords & Angle Bisectors

.. _data-unit-6-notes:

===========================================================================================================================
Hyperbolic/Elliptic Systems, Circles, Chords & Angle Bisectors (Propositions 84–94) — Philological & Critical Notes
===========================================================================================================================

1. Canonical Vieta Systems (D.84–D.85) & the Biquadratic Theorem (D.86)
-----------------------------------------------------------------------

Unit 6 opens (:ref:`D.84 <D.84>`–:ref:`D.86 <D.86>`) with the three most famous algebraic propositions in the *Data*—solving simultaneous two-variable quadratic systems:

1. **Product & Difference** (:ref:`D.84 <D.84>`): $x y \sin\\theta = S$ and $y - x = d \implies$ apply $S$ to $d$ with species-given rhombus excess (:ref:`D.59 <D.59>`). When $\\theta = 90^\circ$ and $S = d^2$, $x(x + d) = d^2$ yields the **golden ratio** $y/x = \phi$!

2. **Product & Sum** (:ref:`D.85 <D.85>`): $x y \sin\\theta = S$ and $x + y = s \implies$ apply $S$ to $s$ with species-given rhombus defect (:ref:`D.58 <D.58>`), subject to $S \le \frac{1}{4}s^2 \sin\\theta$.

3. **Product & Affine Ratio of Squares** (:ref:`D.86 <D.86>`): $x y \sin\\theta = S$ and $y^2 - C = k x^2$. In 1703 :person:`David Gregory <gregory>` (:cite:`Praefatio <gregory:1703>`) suspected the Greek text of :ref:`D.86 <D.86>` might be corrupt; :person:`Robert Simson <simson>` (:cite:`pp. 467–468 <simson:1762>`) brilliantly vindicated the integrity of Euclid's biquadratic proof (which completes the square via $y^2 - C = y(y - d)$ and $(2y - d)^2 = 4y(y - d) + d^2$, :just:`[II.8] <II.8>`) and added `Simson Prop. LXXXVIII` covering the sum-of-squares system $x y = S,\; x^2 + y^2 = C$.

2. Chord Trigonometry (D.87–D.89) & Power of a Point (D.90–D.92)
----------------------------------------------------------------

Propositions :ref:`D.87 <D.87>`–:ref:`D.89 <D.89>` establish the constructive equivalence between **inscribed angles** and **chord lengths** in circles given in magnitude or position (see ``data_06_circle_angle_locus.svg``). In Book I of the :cite:`Syntaxis (Almagest) <ptolemy:syntaxis>`, :person:`Claudius Ptolemy <ptolemy>` builds his entire table of chords (*Πραγματεία τῶν ἐν κύκλῳ εὐθειῶν*) on this foundation alongside :ref:`D.93 <D.93>`.

Propositions :ref:`D.90 <D.90>`–:ref:`D.92 <D.92>` reformulate :just:`[Elements III.17] <III.17>`, :just:`[III.35] <III.35>`, and :just:`[III.36] <III.36>` as the invariance of the **power of a given point** $|OP^2 - R^2|$ with respect to a position-given circle: every secant from an external given point (:ref:`D.91 <D.91>`) or chord through an internal given point (:ref:`D.92 <D.92>`) cuts off segments whose rectangle $PA \cdot PB$ is **given in magnitude**—the invariant engine behind :person:`Apollonius's <apollonius>` *Tangencies* and *Plane Loci* as well as modern radical-axis geometry (:cite:`Altshiller-Court 1952 <altshiller-court:1952>`).

3. The Crown Jewels (D.93–D.94) & Earl Stanhope's and Matthew Stewart's Theorems
--------------------------------------------------------------------------------

The treatise culminates in two virtuoso cyclic-similarity theorems (:ref:`D.93 <D.93>`–:ref:`D.94 <D.94>`, with :ref:`D.93 <D.93>` rendered interactively in ``data_07_prop93_bisector.svg``):

* **Euclid's D.93 & Earl Stanhope's Exterior-Bisector Theorem (`Simson Prop. XCVIII [F]`)**: When a given chord $BC$ cuts off a segment admitting given $\angle BAC$ in a magnitude-given circle, and the **interior** bisector $AD$ of $\angle BAC$ meets $BC$ at $E$ and the opposite arc at $D$, Euclid proves both that $(BA + AC) : AD = BC : BD$ is **given in ratio** and that $(BA + AC) \cdot ED = BD^2$ is **given in magnitude**! In his 1762/1806 edition (:cite:`Prop. XCVIII & p. 469 <simson:1762>`), :person:`Simson <simson>` paired :ref:`D.93 <D.93>` with its dual communicated to him by **Philip Stanhope, 2nd Earl Stanhope** (:person:`Earl Stanhope <stanhope>`): if instead the **exterior** angle at $A$ is bisected by chord $AD'$ meeting $BC$ produced at $E'$ and the circle at $D'$, then the *difference* $|BA - AC|$ has a given ratio to $AD'$, and $|BA - AC| \cdot E'D' = BD'^2$ is given in magnitude!

* **Euclid's D.94 & Matthew Stewart's Generalization (`Simson Prop. C`)**: Immediately following :ref:`D.94 <D.94>`, :person:`Simson <simson>` (:cite:`Prop. C & pp. 469–470 <simson:1762>`) published a remarkable generalization discovered by his pupil and colleague :person:`Matthew Stewart <stewart>` (author of *Some General Theorems of Considerable Use in the Higher Parts of Mathematics*, 1746), showing how fixed lines and chords inflected in a given circle preserve given combinations of products and squares—a direct bridge from Alexandrian *Data* to eighteenth-century Scottish synthetic geometry.

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.84 <D.84>` (Prop. LXXXV) — *Elements G-Index*: ``G.58`` · *Pappus*: Synagoge VII.10 · *Petersen (1879)*: Hyperbolic Application of Areas · *Altshiller-Court (1952)*: § 51
* :ref:`D.85 <D.85>` (Prop. LXXXVI) — *Elements G-Index*: ``G.37, G.58`` · *Pappus*: Synagoge VII.10 · *Petersen (1879)*: Elliptic Application of Areas · *Altshiller-Court (1952)*: § 50 (Sum & Product of Segments)
* :ref:`D.86 <D.86>` (Prop. LXXXIX (cf. LXXXVII–LXXXVIII)) — *Elements G-Index*: ``G.85, G.88, G.210, G.228, G.232`` · *Pappus*: Synagoge VII.10 · *Petersen (1879)*: Biquadratic Reduction (Hyperbola cap Hyperbola)
* :ref:`D.87 <D.87>` (Prop. XCI) — *Elements G-Index*: ``G.124, G.139`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Chord Table / Law of Sines · *Altshiller-Court (1952)*: § 10
* :ref:`D.88 <D.88>` (Prop. XCII) — *Elements G-Index*: ``G.124, G.125, G.139`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Inverse Chord Lookup
* :ref:`D.89 <D.89>` (Prop. XCIII) — *Elements G-Index*: ``G.98, G.123`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Central-Inscribed Angle Rotation · *Altshiller-Court (1952)*: § 10 (Inscribed Angle Arc)
* :ref:`D.90 <D.90>` (Prop. XCIV) — *Elements G-Index*: ``G.119, G.120, G.139`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Thales Semicircle Tangent · *Altshiller-Court (1952)*: § 12 (Tangent from External Point)
* :ref:`D.91 <D.91>` (Prop. XCV) — *Elements G-Index*: ``G.119, G.144`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Exterior Power of a Point · *Altshiller-Court (1952)*: § 310 (Power of a Point)
* :ref:`D.92 <D.92>` (Prop. XCVI) — *Elements G-Index*: ``G.98, G.143`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Interior Power of a Point · *Altshiller-Court (1952)*: § 310 (Intersecting Chords / Power of a Point)
* :ref:`D.93 <D.93>` (Prop. XCVII (cf. Prop. XCVIII [Stanhope])) — *Elements G-Index*: ``G.124, G.133, G.190, G.195, G.212, G.213, G.227`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Angle-Bisector Circumcircle Similarity · *Altshiller-Court (1952)*: § 134 (Inscribed Angle Bisector)
* :ref:`D.94 <D.94>` (Prop. XCIX (cf. Prop. C [Stewart])) — *Elements G-Index*: ``G.24, G.51, G.56, G.139, G.143`` · *Pappus*: Synagoge VII.11 · *Petersen (1879)*: Central Point Reflection + Chord Power · *Altshiller-Court (1952)*: § 310


----


Table of Propositions
---------------------

.. collection::
   :type: proposition
   :sort: order

.. toctree::
   :hidden:

   01/index
   02/index
   03/index
   04/index
   05/index
   06/index
   07/index
   08/index
   09/index
   10/index
   11/index
   12/index
   13/index
   14/index
   15/index
   16/index
   17/index
   18/index
   19/index
   20/index
   21/index
   22/index
   23/index
   24/index
   25/index
   26/index
   27/index
   28/index
   29/index
   30/index
   31/index
   32/index
   33/index
   34/index
   35/index
   36/index
   37/index
   38/index
   39/index
   40/index
   41/index
   42/index
   43/index
   44/index
   45/index
   46/index
   47/index
   48/index
   49/index
   50/index
   51/index
   52/index
   53/index
   54/index
   55/index
   56/index
   57/index
   58/index
   59/index
   60/index
   61/index
   62/index
   63/index
   64/index
   65/index
   66/index
   67/index
   68/index
   69/index
   70/index
   71/index
   72/index
   73/index
   74/index
   75/index
   76/index
   77/index
   78/index
   79/index
   80/index
   81/index
   82/index
   83/index
   84/index
   85/index
   86/index
   87/index
   88/index
   89/index
   90/index
   91/index
   92/index
   93/index
   94/index
