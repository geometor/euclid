:order: 42
:type: summary
:canonical_id: D.unit.4
:folio: Menge pp. 98–126
:book: Propositions 56–67: Areas, Quadratics & Cosines

.. _data-unit-4-summary:

=======================================================================================================
Unit 4: Application of Areas, Quadratics & Cosine Projections (Propositions 56–67) — Analytical Summary
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
     - :ref:`EN <D.56>` · :ref:`EL <D.56.el>`
   * - :ref:`D.57 <D.57>`
     - Prop. LXI
     - ``Given(Mag(Area S), Mag(Base a), Mag(Angle theta)) -> Determined(Mag(Breadth x))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 52] <D.52>`, :just:`[I.31] <I.31>`, :just:`[I.46] <I.46>`, :just:`[VI.1] <VI.1>`
     - :ref:`EN <D.57>` · :ref:`EL <D.57.el>`
   * - :ref:`D.58 <D.58>`
     - Prop. LXXXIII
     - ``Given(Mag(S), Mag(a), Species(Defect)) -> Determined(Roots of a*x - c*x^2 = S) [diorismos]``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.5] <II.5>`, :just:`[VI.24] <VI.24>`, :just:`[VI.27] <VI.27>`, :just:`[VI.28] <VI.28>`
     - :ref:`EN <D.58>` · :ref:`EL <D.58.el>`
   * - :ref:`D.59 <D.59>`
     - Prop. LXXXIV
     - ``Given(Mag(S), Mag(a), Species(Excess)) -> Determined(Positive root of a*x + c*x^2 = S)``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.6] <II.6>`, :just:`[VI.24] <VI.24>`, :just:`[VI.29] <VI.29>`
     - :ref:`EN <D.59>` · :ref:`EL <D.59.el>`
   * - :ref:`D.60 <D.60>`
     - Prop. LXXXII
     - ``Given(Species(P), Mag(Area(P)), Mag(Gnomon G)) -> Determined(Mag(Sides of P +/- G))``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 55] <D.55>`, :just:`[VI.24] <VI.24>`
     - :ref:`EN <D.60>` · :ref:`EL <D.60.el>`
   * - :ref:`D.61 <D.61>`
     - Prop. LXIX
     - ``Given(Species(P on CB), Angle(CD), Ratio(Area(P) : Area(CD))) -> Determined(Species(CD))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 49] <D.49>`, :just:`[I.13] <I.13>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`
     - :ref:`EN <D.61>` · :ref:`EL <D.61.el>`
   * - :ref:`D.62 <D.62>`
     - Prop. LXX
     - ``Given(Ratio(AB : CD), Species(AEB on AB), Angle(DF), Ratio(AEB : DF)) -> Determined(Species(DF))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 50] <D.50>`, :just:`[Data 61] <D.61>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.62>` · :ref:`EL <D.62.el>`
   * - :ref:`D.63 <D.63>`
     - Omitted (case of Prop. LIII)
     - ``Given(Species(△ABC)) -> Determined(Ratio(a^2 : △ABC), Ratio(b^2 : △ABC), Ratio(c^2 : △ABC))``
     - :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`
     - :ref:`EN <D.63>` · :ref:`EL <D.63.el>`
   * - :ref:`D.64 <D.64>`
     - Prop. LXXIV
     - ``Given(ObtuseAngle B) -> Determined(Ratio((b^2 - a^2 - c^2) : △ABC) = -4 cot B)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.12] <II.12>`, :just:`[VI.1] <VI.1>`
     - :ref:`EN <D.64>` · :ref:`EL <D.64.el>`
   * - :ref:`D.65 <D.65>`
     - Prop. LXXV
     - ``Given(AcuteAngle B) -> Determined(Ratio((a^2 + c^2 - b^2) : △ABC) = 4 cot B)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.13] <II.13>`, :just:`[VI.1] <VI.1>`
     - :ref:`EN <D.65>` · :ref:`EL <D.65.el>`
   * - :ref:`D.66 <D.66>`
     - Prop. LXII Cor.
     - ``Given(Angle A) -> Determined(Ratio((AB * AC) : Area(△ABC)) = 2 / sin A)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.1] <VI.1>`
     - :ref:`EN <D.66>` · :ref:`EL <D.66.el>`
   * - :ref:`D.67 <D.67>`
     - Prop. LXXVI
     - ``Given(Angle A) -> Determined(Ratio(((b + c)^2 - a^2) : △ABC) = 4*(1 + cos A) / sin A)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 50] <D.50>`, :just:`[Data 66] <D.66>`, :just:`[I.5] <I.5>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`, :just:`[I.32] <I.32>`, :just:`[II.6] <II.6>`, :just:`[VI.2] <VI.2>`, :just:`[VI.16] <VI.16>`
     - :ref:`EN <D.67>` · :ref:`EL <D.67.el>`

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
