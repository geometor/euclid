:order: 52
:type: summary
:canonical_id: D.unit.5
:folio: Menge pp. 126–164
:book: Propositions 68–83: Proportional Figures

.. _data-unit-5-summary:

==============================================================================================================
Unit 5: Proportional Parallelograms, Triangles & Four-Line Relations (Propositions 68–83) — Analytical Summary
==============================================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Compound ratio calculus for equiangular and supplementary-angle parallelograms and triangles (D.68–D.75), dropped-altitude ratios in species-given triangles (D.76), duplicated/corollarial area-species bridges (D.77–D.78), inscribed circle-triangle similarity lemmas and area-product determination (D.79–D.80), and four-line proportional transformations (D.81–D.83).

* **Scope**: 16 propositions (D.68–D.83 (Simson L–LXXVIII), *Menge* pp. 126–164).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Conspectus (D.68–D.83 (Simson L–LXXVIII))
----------------------------------------------------

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
     - :ref:`EN <D.68>` · :ref:`EL <D.68.el>`
   * - :ref:`D.69 <D.69>`
     - Prop. LXVI
     - ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.12] <I.12>`, :just:`[I.23] <I.23>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`
     - :ref:`EN <D.69>` · :ref:`EL <D.69.el>`
   * - :ref:`D.70 <D.70>`
     - Props. LXVII–LXVIII
     - ``Given(Angle(P1), Angle(P2), Ratio(s1 : t1), Ratio(s2 : t2)) -> Determined(Ratio(P1 : P2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`, :just:`[VI.23] <VI.23>`
     - :ref:`EN <D.70>` · :ref:`EL <D.70.el>`
   * - :ref:`D.71 <D.71>`
     - Prop. LXVIII Cor. 1
     - ``Given(Angle(A), Angle(D), Ratio(c1 : c2), Ratio(b1 : b2)) -> Determined(Ratio(△1 : △2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`
     - :ref:`EN <D.71>` · :ref:`EL <D.71.el>`
   * - :ref:`D.72 <D.72>`
     - Prop. LXVIII Cor. 2
     - ``Given(Ratio(b1 : b2), Ratio(d1 : d2), Angle(phi1), Angle(phi2)) -> Determined(Ratio(△1 : △2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[I.41] <I.41>`
     - :ref:`EN <D.72>` · :ref:`EL <D.72.el>`
   * - :ref:`D.73 <D.73>`
     - Prop. LXIV (pt. 2)
     - ``Given(Angle(P1), Angle(P2), CB:FG = EF:CK, Ratio(AC:CK)) -> Determined(Ratio(P1 : P2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[Data 70] <D.70>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - :ref:`EN <D.73>` · :ref:`EL <D.73.el>`
   * - :ref:`D.74 <D.74>`
     - Prop. LXIV (pt. 1; cf. LXIII)
     - ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2)) -> Determined(CB : FG = EF : K with GivenRatio(AC : K))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - :ref:`EN <D.74>` · :ref:`EL <D.74.el>`
   * - :ref:`D.75 <D.75>`
     - Prop. LXIV Cor.
     - ``Given(Angle(A), Angle(D), Ratio(△1 : △2)) -> Determined(AB : DE = DF : K with GivenRatio(AC : K))``
     - :just:`[Data 74] <D.74>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`
     - :ref:`EN <D.75>` · :ref:`EL <D.75.el>`
   * - :ref:`D.76 <D.76>`
     - Prop. L
     - ``Given(Species(△ABC), AD perp BC) -> Determined(Ratio(AD : BC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`
     - :ref:`EN <D.76>` · :ref:`EL <D.76.el>`
   * - :ref:`D.77 <D.77>`
     - Omitted (dup. of Prop. LIX / D.54)
     - ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(s(A) : s(B)))``
     - :just:`[Data 54] <D.54>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.77>` · :ref:`EL <D.77.el>`
   * - :ref:`D.78 <D.78>`
     - Omitted (case of Prop. LXX / D.62)
     - ``Given(Species(A), Ratio(A : B), Ratio(s(A) : s1(B)), Angle(B)) -> Determined(Species(B))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 62] <D.62>`, :just:`[VI.14] <VI.14>`
     - :ref:`EN <D.78>` · :ref:`EL <D.78.el>`
   * - :ref:`D.79 <D.79>`
     - Prop. LXXVII Cor. 1
     - ``Given(∠BAC = ∠EDF, BC : h_A = EF : h_D) -> Determined(△ABC ~ △DEF)``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data Def. 7] <D.def.7>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[III.21] <III.21>`, :just:`[VI.4] <VI.4>`
     - :ref:`EN <D.79>` · :ref:`EL <D.79.el>`
   * - :ref:`D.80 <D.80>`
     - Prop. LXXVIII
     - ``Given(Angle A, Ratio((b*c) : a^2)) -> Determined(Species(△ABC))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 66] <D.66>`, :just:`[Data 68] <D.68>`, :just:`[Data 79] <D.79>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`
     - :ref:`EN <D.80>` · :ref:`EL <D.80.el>`
   * - :ref:`D.81 <D.81>`
     - Prop. LXXI
     - ``Given(B^2 = A*C, E^2 = D*F) -> (Given(A:D, C:F) -> Given(B:E)) & (Given(A:D, B:E) -> Given(C:F))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 50] <D.50>`, :just:`[Data 54] <D.54>`, :just:`[Data 70] <D.70>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.81>` · :ref:`EL <D.81.el>`
   * - :ref:`D.82 <D.82>`
     - Prop. LXXII
     - ``Given(A : B = C : D, Ratio(B : E) = k) -> Determined(Ratio(D : F) = k when A : E = C : F)``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.22] <V.22>`
     - :ref:`EN <D.82>` · :ref:`EL <D.82.el>`
   * - :ref:`D.83 <D.83>`
     - Prop. LXXIII
     - ``Given(A * D = B * E, Ratio(C : E) = k) -> Determined(D : C = B : (A / k))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 68] <D.68>`, :just:`[V.16] <V.16>`, :just:`[V.23] <V.23>`, :just:`[VI.16] <VI.16>`
     - :ref:`EN <D.83>` · :ref:`EL <D.83.el>`

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
