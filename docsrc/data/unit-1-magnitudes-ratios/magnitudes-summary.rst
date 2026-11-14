:order: 12
:type: summary
:canonical_id: D.unit.1
:folio: Menge pp. 4–42
:book: Propositions 1–24: Magnitudes & Ratios

.. _data-unit-1-summary:

====================================================================
Unit 1: Magnitudes & Ratios (Propositions 1–24) — Analytical Summary
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
     - :ref:`EN <D.1>` · :ref:`EL <D.1.el>`
   * - :ref:`D.2 <D.2>`
     - Prop. II
     - ``Given(Mag(A), Ratio(A : B)) -> Determined(Mag(B)) [Simson fourth-proportional diorismos]``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[V.11] <V.11>`, :just:`[V.9] <V.9>`, :just:`[VI.12] <VI.12>`
     - :ref:`EN <D.2>` · :ref:`EL <D.2.el>`
   * - :ref:`D.3 <D.3>`
     - Prop. III
     - ``Given(Mag(AB), Mag(BC)) -> Determined(Mag(AB + BC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 2] <I.cn.2>`
     - :ref:`EN <D.3>` · :ref:`EL <D.3.el>`
   * - :ref:`D.4 <D.4>`
     - Prop. IV
     - ``Given(Mag(AB), Mag(AC)) -> Determined(Mag(AB - AC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 3] <I.cn.3>`
     - :ref:`EN <D.4>` · :ref:`EL <D.4.el>`
   * - :ref:`D.5 <D.5>`
     - Prop. VI
     - ``Given(Ratio(AB : AC)) -> Determined(Ratio(AB : (AB - AC)))``
     - :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.5>` · :ref:`EL <D.5.el>`
   * - :ref:`D.6 <D.6>`
     - Prop. VII
     - ``Given(Ratio(AB : BC)) -> Determined(Ratio((AB+BC) : AB), Ratio((AB+BC) : BC))``
     - :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.6>` · :ref:`EL <D.6.el>`
   * - :ref:`D.7 <D.7>`
     - Prop. VIII
     - ``Given(Mag(AB), Ratio(AC : CB)) -> Determined(Mag(AC), Mag(CB))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[VI.10] <VI.10>`
     - :ref:`EN <D.7>` · :ref:`EL <D.7.el>`
   * - :ref:`D.8 <D.8>`
     - Prop. IX
     - ``Given(Ratio(A : B), Ratio(C : B)) -> Determined(Ratio(A : C))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[V.7] <V.7>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`
     - :ref:`EN <D.8>` · :ref:`EL <D.8.el>`
   * - :ref:`D.9 <D.9>`
     - Prop. X
     - ``Given(Ratios(A:B:C), Ratio(A:D), Ratio(B:E), Ratio(C:F)) -> Determined(Ratios(D:E:F))``
     - :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`
     - :ref:`EN <D.9>` · :ref:`EL <D.9.el>`
   * - :ref:`D.10 <D.10>`
     - Prop. XVI
     - ``Given((AB - D) : BC = k) <-> Determined(((AB+BC) - D) : BC = k+1 | (AB + BE = D where BC:BE given))``
     - :just:`[Data Def. 9] <D.def.9>`, :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 5] <D.5>`, :just:`[Data 6] <D.6>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.10>` · :ref:`EL <D.10.el>`
   * - :ref:`D.11 <D.11>`
     - Prop. XVII
     - ``Given((AB - D) : BC = k) <-> Determined((AB - k/(k+1)*D) : (AB + BC) = k/(k+1))``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 6] <D.6>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.11>` · :ref:`EL <D.11.el>`
   * - :ref:`D.12 <D.12>`
     - Prop. V
     - ``Given(Mag(A + B), Mag(B + C)) -> Determined(A = C | ExceedsByGiven(A, C))``
     - :just:`[Data Def. 9] <D.def.9>`, :just:`[Data 4] <D.4>`, :just:`[C.N. 3] <I.cn.3>`
     - :ref:`EN <D.12>` · :ref:`EL <D.12.el>`
   * - :ref:`D.13 <D.13>`
     - Prop. XXIV
     - ``Given(Ratio(A : B) = r, (B - F) : C = k) -> Determined((A - r*F) : C = r*k)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.13>` · :ref:`EL <D.13.el>`
   * - :ref:`D.14 <D.14>`
     - Prop. XVIII
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A+d1 : C+d2) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.12] <V.12>`, :just:`[V.18] <V.18>`
     - :ref:`EN <D.14>` · :ref:`EL <D.14.el>`
   * - :ref:`D.15 <D.15>`
     - Prop. XIX
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A-d1 : C-d2) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.15>` · :ref:`EL <D.15.el>`
   * - :ref:`D.16 <D.16>`
     - Prop. XX
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(((A+d2) - (r*d1+d2)) : (C-d1) = r)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.16>` · :ref:`EL <D.16.el>`
   * - :ref:`D.17 <D.17>`
     - Prop. XXV
     - ``Given((A - d1):B = k1, (C - d2):B = k2) -> Determined(Ratio(A:C) | GreaterThanInRatio(A, C))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 14] <D.14>`, :just:`[V.11] <V.11>`
     - :ref:`EN <D.17>` · :ref:`EL <D.17.el>`
   * - :ref:`D.18 <D.18>`
     - Prop. XXVI
     - ``Given((C - d1):A = k1, (C - d2):E = k2) -> Determined(Ratio(A:E) | GreaterThanInRatio(A, E))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 15] <D.15>`, :just:`[V.11] <V.11>`
     - :ref:`EN <D.18>` · :ref:`EL <D.18.el>`
   * - :ref:`D.19 <D.19>`
     - Prop. XXVII
     - ``Given((A - d1):B = k1, (B - d2):C = k2) -> Determined((A - (d1 + k1*d2)) : C = k1*k2)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[Data 13] <D.13>`, :just:`[V.11] <V.11>`
     - :ref:`EN <D.19>` · :ref:`EL <D.19.el>`
   * - :ref:`D.20 <D.20>`
     - Prop. XXIII
     - ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A-x : C-y) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.20>` · :ref:`EL <D.20.el>`
   * - :ref:`D.21 <D.21>`
     - Omitted (cf. Prop. XVIII)
     - ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A+x : C+y) | GreaterThanInRatio)``
     - :just:`[Data 14] <D.14>`, :just:`[V.18] <V.18>`
     - :ref:`EN <D.21>` · :ref:`EL <D.21.el>`
   * - :ref:`D.22 <D.22>`
     - Prop. XI
     - ``Given(Ratio(A : C) = r1, Ratio(B : C) = r2) -> Determined(Ratio((A + B) : C) = r1 + r2)``
     - :just:`[Data 3] <D.3>`, :just:`[Data 6] <D.6>`, :just:`[Data 8] <D.8>`, :just:`[V.24] <V.24>`
     - :ref:`EN <D.22>` · :ref:`EL <D.22.el>`
   * - :ref:`D.23 <D.23>`
     - Prop. XII
     - ``Given(AB:CD = r0, AE:CF = r1 != r0, EB:FD = r2) -> Determined(All pairwise ratios)``
     - :just:`[Data 5] <D.5>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.19] <V.19>`
     - :ref:`EN <D.23>` · :ref:`EL <D.23.el>`
   * - :ref:`D.24 <D.24>`
     - Prop. XIII
     - ``Given(A : B = B : C, Ratio(A : C)) -> Determined(Ratio(A : B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[VI.13] <VI.13>`, :just:`[VI.17] <VI.17>`, :just:`[VI.22] <VI.22>`
     - :ref:`EN <D.24>` · :ref:`EL <D.24.el>`

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
