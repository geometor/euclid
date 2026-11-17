:navigation: header
:order: 14
:nav_title: Concordance
:type: apparatus
:title: Master Concordance & Dependency Matrix

.. _data-concordance:

============================================
Master Concordance & Dependency Matrix
============================================

Complete cross-reference of :person:`Euclid's <euclid>` *Data* across :person:`Heinrich Menge's <menge>` 1896 Teubner Greek text (`Vat. gr. 190`), :person:`Robert Simson's <simson>` 1762/1806 critical edition, the :doc:`Heath Elements <../heath/index>`, the ``geometor.elements`` **G-Index**, :person:`Pappus's <pappus>` *Synagoge* Book VII, and :person:`Julius Petersen's <petersen>` *Methods and Theories* (1879).

Definitions (`D.def.1` – `D.def.15`)
------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 12 10 14 22 42

   * - Menge ID
     - Page
     - Simson ID
     - Mode of Givenness
     - Functional Predicate
   * - :ref:`D.def.1 <D.def.1>` (:ref:`Greek <D.def.1.el>`)
     - p. 2
     - Def. I
     - Magnitude (μεγέθει)
     - ``GivenMagnitude(X) := exists constructible X' with X' = X``
   * - :ref:`D.def.2 <D.def.2>` (:ref:`Greek <D.def.2.el>`)
     - p. 2
     - Def. II
     - Ratio (λόγῳ)
     - ``GivenRatio(A : B) := exists GivenMagnitude(C, D) with A : B = C : D``
   * - :ref:`D.def.3 <D.def.3>` (:ref:`Greek <D.def.3.el>`)
     - p. 2
     - Def. III
     - Species (εἴδει)
     - ``GivenSpecies(P) := forall i,j: GivenAngle(ang_i(P)) and GivenRatio(s_i(P) : s_j(P))``
   * - :ref:`D.def.4 <D.def.4>` (:ref:`Greek <D.def.4.el>`)
     - p. 2
     - Def. IV (cf. Def. A)
     - Position (θέσει)
     - ``GivenPosition(X) := X is invariant in the fixed planar reference frame (and constructible)``
   * - :ref:`D.def.5 <D.def.5>` (:ref:`Greek <D.def.5.el>`)
     - p. 2
     - Def. V
     - Circle in Magnitude
     - ``GivenCircleMag(C) := GivenMagnitude(radius(C))``
   * - :ref:`D.def.6 <D.def.6>` (:ref:`Greek <D.def.6.el>`)
     - p. 2
     - Def. VI
     - Circle in Position & Magnitude
     - ``GivenCirclePosMag(C) := GivenPosition(center(C)) and GivenMagnitude(radius(C))``
   * - :ref:`D.def.7 <D.def.7>` (:ref:`Greek <D.def.7.el>`)
     - p. 2
     - Def. VII
     - Circular Segment in Magnitude
     - ``GivenSegmentMag(S) := GivenAngle(inscribed_angle(S)) and GivenMagnitude(base(S))``
   * - :ref:`D.def.8 <D.def.8>` (:ref:`Greek <D.def.8.el>`)
     - p. 2
     - Def. VIII
     - Circular Segment in Position & Magnitude
     - ``GivenSegmentPosMag(S) := GivenAngle(inscribed_angle(S)) and GivenPosMag(base(S))``
   * - :ref:`D.def.9 <D.def.9>` (:ref:`Greek <D.def.9.el>`)
     - p. 4
     - Def. IX
     - Affine Excess (δοθέντι μεῖζον)
     - ``ExceedsByGiven(A, B) := exists GivenMagnitude(D) with A - D = B``
   * - :ref:`D.def.10 <D.def.10>` (:ref:`Greek <D.def.10.el>`)
     - p. 4
     - Def. X
     - Affine Defect (δοθέντι ἔλασσον)
     - ``LessByGiven(A, B) := exists GivenMagnitude(D) with A + D = B``
   * - :ref:`D.def.11 <D.def.11>` (:ref:`Greek <D.def.11.el>`)
     - p. 4
     - Omitted (expanded verbally in Props. XIV–XXVII)
     - Affine-Ratio Excess (δοθέντι μεῖζον ἢ ἐν λόγῳ)
     - ``GreaterThanInRatio(A, B) := exists GivenMagnitude(D), GivenRatio(k) with (A - D) : B = k``
   * - :ref:`D.def.12 <D.def.12>` (:ref:`Greek <D.def.12.el>`)
     - p. 4
     - Omitted (expanded verbally in Props. XIV–XXVII)
     - Affine-Ratio Defect (δοθέντι ἔλασσον ἢ ἐν λόγῳ)
     - ``LessThanInRatio(A, B) := exists GivenMagnitude(D), GivenRatio(k) with (A + D) : B = k``
   * - :ref:`D.def.13 <D.def.13>` (:ref:`Greek <D.def.13.el>`)
     - p. 4
     - Omitted (late scholium; bracketed by Menge)
     - Directed Ordinate [Bracketed Scholium]
     - ``Kategmene(P, L, theta) := segment from GivenPoint(P) to GivenLine(L) at GivenAngle(theta)``
   * - :ref:`D.def.14 <D.def.14>` (:ref:`Greek <D.def.14.el>`)
     - p. 4
     - Omitted (late scholium; bracketed by Menge)
     - Erected Line [Bracketed Scholium]
     - ``Anegmene(P, L, theta) := ray from GivenPoint(P) on GivenLine(L) at GivenAngle(theta)``
   * - :ref:`D.def.15 <D.def.15>` (:ref:`Greek <D.def.15.el>`)
     - p. 4
     - Omitted (late scholium; bracketed by Menge)
     - Parallel to Position [Bracketed Scholium]
     - ``ParaThesei(P, L) := line through GivenPoint(P) parallel to GivenLine(L)``

Propositions (`D.1` – `D.94`)
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 8 12 34 22 14

   * - Menge ID
     - Page
     - Simson
     - Functional Signature
     - Data & Elements Deps
     - G-Index / Loci
   * - :ref:`D.1 <D.1>` (:ref:`Greek <D.1.el>`)
     - p. 4
     - Prop. I
     - ``Given(Mag(A), Mag(B)) -> Determined(Ratio(A : B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[V.7] <V.7>`, :just:`[V.16] <V.16>`
     - G.183, G.195, Synagoge VII.3
   * - :ref:`D.2 <D.2>` (:ref:`Greek <D.2.el>`)
     - p. 4
     - Prop. II
     - ``Given(Mag(A), Ratio(A : B)) -> Determined(Mag(B)) [Simson fourth-proportional diorismos]``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[V.11] <V.11>`, :just:`[V.9] <V.9>`, :just:`[VI.12] <VI.12>`
     - G.189, G.187, G.222, Synagoge VII.3
   * - :ref:`D.3 <D.3>` (:ref:`Greek <D.3.el>`)
     - p. 4
     - Prop. III
     - ``Given(Mag(AB), Mag(BC)) -> Determined(Mag(AB + BC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 2] <I.cn.2>`
     - G.36
   * - :ref:`D.4 <D.4>` (:ref:`Greek <D.4.el>`)
     - p. 4
     - Prop. IV
     - ``Given(Mag(AB), Mag(AC)) -> Determined(Mag(AB - AC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[C.N. 3] <I.cn.3>`
     - G.19
   * - :ref:`D.5 <D.5>` (:ref:`Greek <D.5.el>`)
     - p. 10
     - Prop. VI
     - ``Given(Ratio(AB : AC)) -> Determined(Ratio(AB : (AB - AC)))``
     - :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[V.19] <V.19>`
     - G.201, Synagoge VII.4
   * - :ref:`D.6 <D.6>` (:ref:`Greek <D.6.el>`)
     - p. 10
     - Prop. VII
     - ``Given(Ratio(AB : BC)) -> Determined(Ratio((AB+BC) : AB), Ratio((AB+BC) : BC))``
     - :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - G.199, G.201, Synagoge VII.4
   * - :ref:`D.7 <D.7>` (:ref:`Greek <D.7.el>`)
     - p. 12
     - Prop. VIII
     - ``Given(Mag(AB), Ratio(AC : CB)) -> Determined(Mag(AC), Mag(CB))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[VI.10] <VI.10>`
     - G.220, Synagoge VII.4
   * - :ref:`D.8 <D.8>` (:ref:`Greek <D.8.el>`)
     - p. 14
     - Prop. IX
     - ``Given(Ratio(A : B), Ratio(C : B)) -> Determined(Ratio(A : C))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[V.7] <V.7>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`
     - G.183, G.189, G.205, Synagoge VII.4
   * - :ref:`D.9 <D.9>` (:ref:`Greek <D.9.el>`)
     - p. 14
     - Prop. X
     - ``Given(Ratios(A:B:C), Ratio(A:D), Ratio(B:E), Ratio(C:F)) -> Determined(Ratios(D:E:F))``
     - :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.22] <V.22>`
     - G.189, G.205, Synagoge VII.4
   * - :ref:`D.10 <D.10>` (:ref:`Greek <D.10.el>`)
     - p. 16
     - Prop. XVI
     - ``Given((AB - D) : BC = k) <-> Determined(((AB+BC) - D) : BC = k+1 | (AB + BE = D where BC:BE given))``
     - :just:`[Data Def. 9] <D.def.9>`, :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 5] <D.5>`, :just:`[Data 6] <D.6>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - G.199, G.201, Synagoge VII.5
   * - :ref:`D.11 <D.11>` (:ref:`Greek <D.11.el>`)
     - p. 20
     - Prop. XVII
     - ``Given((AB - D) : BC = k) <-> Determined((AB - k/(k+1)*D) : (AB + BC) = k/(k+1))``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 6] <D.6>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[V.18] <V.18>`, :just:`[V.19] <V.19>`
     - G.190, G.195, G.199, Synagoge VII.5
   * - :ref:`D.12 <D.12>` (:ref:`Greek <D.12.el>`)
     - p. 22
     - Prop. V
     - ``Given(Mag(A + B), Mag(B + C)) -> Determined(A = C | ExceedsByGiven(A, C))``
     - :just:`[Data Def. 9] <D.def.9>`, :just:`[Data 4] <D.4>`, :just:`[C.N. 3] <I.cn.3>`
     - G.19
   * - :ref:`D.13 <D.13>` (:ref:`Greek <D.13.el>`)
     - p. 24
     - Prop. XXIV
     - ``Given(Ratio(A : B) = r, (B - F) : C = k) -> Determined((A - r*F) : C = r*k)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.19] <V.19>`
     - G.189, G.201, Synagoge VII.5
   * - :ref:`D.14 <D.14>` (:ref:`Greek <D.14.el>`)
     - p. 26
     - Prop. XVIII
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A+d1 : C+d2) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.12] <V.12>`, :just:`[V.18] <V.18>`
     - G.190, G.199, Synagoge VII.5
   * - :ref:`D.15 <D.15>` (:ref:`Greek <D.15.el>`)
     - p. 26
     - Prop. XIX
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A-d1 : C-d2) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`
     - G.201, Synagoge VII.5
   * - :ref:`D.16 <D.16>` (:ref:`Greek <D.16.el>`)
     - p. 30
     - Prop. XX
     - ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(((A+d2) - (r*d1+d2)) : (C-d1) = r)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[V.19] <V.19>`
     - G.201, Synagoge VII.5
   * - :ref:`D.17 <D.17>` (:ref:`Greek <D.17.el>`)
     - p. 32
     - Prop. XXV
     - ``Given((A - d1):B = k1, (C - d2):B = k2) -> Determined(Ratio(A:C) | GreaterThanInRatio(A, C))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 14] <D.14>`, :just:`[V.11] <V.11>`
     - G.189, Synagoge VII.5
   * - :ref:`D.18 <D.18>` (:ref:`Greek <D.18.el>`)
     - p. 32
     - Prop. XXVI
     - ``Given((C - d1):A = k1, (C - d2):E = k2) -> Determined(Ratio(A:E) | GreaterThanInRatio(A, E))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 15] <D.15>`, :just:`[V.11] <V.11>`
     - G.189, Synagoge VII.5
   * - :ref:`D.19 <D.19>` (:ref:`Greek <D.19.el>`)
     - p. 34
     - Prop. XXVII
     - ``Given((A - d1):B = k1, (B - d2):C = k2) -> Determined((A - (d1 + k1*d2)) : C = k1*k2)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 2] <D.2>`, :just:`[Data 3] <D.3>`, :just:`[Data 13] <D.13>`, :just:`[V.11] <V.11>`
     - G.189, Synagoge VII.5
   * - :ref:`D.20 <D.20>` (:ref:`Greek <D.20.el>`)
     - p. 34
     - Prop. XXIII
     - ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A-x : C-y) | GreaterThanInRatio)``
     - :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.19] <V.19>`
     - G.201, Synagoge VII.5
   * - :ref:`D.21 <D.21>` (:ref:`Greek <D.21.el>`)
     - p. 34
     - Omitted (cf. Prop. XVIII)
     - ``Given(Mag(A), Mag(C), Ratio(x : y) = r) -> Determined(Ratio(A+x : C+y) | GreaterThanInRatio)``
     - :just:`[Data 14] <D.14>`, :just:`[V.18] <V.18>`
     - G.199, Synagoge VII.5
   * - :ref:`D.22 <D.22>` (:ref:`Greek <D.22.el>`)
     - p. 34
     - Prop. XI
     - ``Given(Ratio(A : C) = r1, Ratio(B : C) = r2) -> Determined(Ratio((A + B) : C) = r1 + r2)``
     - :just:`[Data 3] <D.3>`, :just:`[Data 6] <D.6>`, :just:`[Data 8] <D.8>`, :just:`[V.24] <V.24>`
     - G.207, Synagoge VII.4
   * - :ref:`D.23 <D.23>` (:ref:`Greek <D.23.el>`)
     - p. 34
     - Prop. XII
     - ``Given(AB:CD = r0, AE:CF = r1 != r0, EB:FD = r2) -> Determined(All pairwise ratios)``
     - :just:`[Data 5] <D.5>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.19] <V.19>`
     - G.189, G.195, G.201, Synagoge VII.5
   * - :ref:`D.24 <D.24>` (:ref:`Greek <D.24.el>`)
     - p. 44
     - Prop. XIII
     - ``Given(A : B = B : C, Ratio(A : C)) -> Determined(Ratio(A : B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 2] <D.def.2>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[VI.13] <VI.13>`, :just:`[VI.17] <VI.17>`, :just:`[VI.22] <VI.22>`
     - G.223, G.228, G.234, Synagoge VII.5
   * - :ref:`D.25 <D.25>` (:ref:`Greek <D.25.el>`)
     - p. 46
     - Prop. XXVIII
     - ``Given(Pos(L1), Pos(L2), Meet(L1, L2) = E) -> Determined(Pos(E))``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[Post. 1] <I.post.1>`, :just:`[I Def. 4] <I.def.4>`
     - G.14, G.4, Synagoge VII.6
   * - :ref:`D.26 <D.26>` (:ref:`Greek <D.26.el>`)
     - p. 46
     - Prop. XXIX
     - ``Given(Pos(A), Pos(B)) -> Determined(Pos(AB), Mag(AB))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Post. 1] <I.post.1>`, :just:`[Post. 3] <I.post.3>`
     - G.14, G.15, Synagoge VII.6
   * - :ref:`D.27 <D.27>` (:ref:`Greek <D.27.el>`)
     - p. 48
     - Prop. XXX
     - ``Given(Pos(Ray A->), Mag(AB), Pos(A)) -> Determined(Pos(B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Post. 3] <I.post.3>`, :just:`[I Def. 15] <I.def.15>`
     - G.15, G.10, Synagoge VII.6
   * - :ref:`D.28 <D.28>` (:ref:`Greek <D.28.el>`)
     - p. 48
     - Prop. XXXI
     - ``Given(Pos(A), Pos(Line BC)) -> Determined(Pos(Parallel(A, BC)))``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[I.27] <I.27>`, :just:`[I.29] <I.29>`, :just:`[I.30] <I.30>`, :just:`[I.31] <I.31>`
     - G.53, G.56, G.57, Synagoge VII.6
   * - :ref:`D.29 <D.29>` (:ref:`Greek <D.29.el>`)
     - p. 50
     - Prop. XXXII
     - ``Given(Pos(Line AB), Pos(C in AB), Mag(Angle theta)) -> Determined(Pos(Ray CD))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[I.23] <I.23>`
     - G.48, Synagoge VII.6
   * - :ref:`D.30 <D.30>` (:ref:`Greek <D.30.el>`)
     - p. 50
     - Prop. XXXIII
     - ``Given(Pos(A), Pos(Line BC), Mag(Angle ADC)) -> Determined(Pos(Line AD))``
     - :just:`[Data 28] <D.28>`, :just:`[Data 29] <D.29>`, :just:`[I.23] <I.23>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`
     - G.48, G.56, G.58, Synagoge VII.6
   * - :ref:`D.31 <D.31>` (:ref:`Greek <D.31.el>`)
     - p. 50
     - Prop. XXXIV
     - ``Given(Pos(A), Pos(Line BC), Mag(AD >= dist(A, BC))) -> Determined(Pos(AD)) [2-root diorismos]``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[I.12] <I.12>`, :just:`[Post. 3] <I.post.3>`
     - G.35, G.15, Synagoge VII.6
   * - :ref:`D.32 <D.32>` (:ref:`Greek <D.32.el>`)
     - p. 54
     - Prop. XXXV
     - ``Given(Pos(AB || CD), Mag(Angle BEF)) -> Determined(Mag(EF))``
     - :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`
     - G.56, G.58, G.62, Synagoge VII.6
   * - :ref:`D.33 <D.33>` (:ref:`Greek <D.33.el>`)
     - p. 54
     - Prop. XXXVI
     - ``Given(Pos(AB || CD), Mag(EF >= strip_width)) -> Determined(Mag(Angle BEF))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data 28] <D.28>`, :just:`[Data 31] <D.31>`, :just:`[I.29] <I.29>`, :just:`[I.34] <I.34>`
     - G.56, G.62, Synagoge VII.6
   * - :ref:`D.34 <D.34>` (:ref:`Greek <D.34.el>`)
     - p. 54
     - Prop. XXXVIII
     - ``Given(Pos(AB || CD), Pos(Pole E)) -> Determined(Ratio(EF : FG))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.12] <I.12>`, :just:`[VI.2] <VI.2>`, :just:`[VI.4] <VI.4>`
     - G.35, G.211, G.213, Synagoge VII.6
   * - :ref:`D.35 <D.35>` (:ref:`Greek <D.35.el>`)
     - p. 54
     - Prop. XXXIX (pt. 1)
     - ``Given(Pos(Pole A), Pos(Line BC), InternalRatio(AE : ED)) -> Determined(Pos(Line FEG || BC))``
     - :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`
     - G.211, Synagoge VII.6
   * - :ref:`D.36 <D.36>` (:ref:`Greek <D.36.el>`)
     - p. 54
     - Prop. XXXIX (pt. 2)
     - ``Given(Pos(Pole A), Pos(Line BC), ExternalRatio(AD : DE)) -> Determined(Pos(Line FEG || BC))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`
     - G.211, Synagoge VII.6
   * - :ref:`D.37 <D.37>` (:ref:`Greek <D.37.el>`)
     - p. 62
     - Prop. XL (pt. 1)
     - ``Given(Pos(AB || CD), InternalRatio(EG : GF)) -> Determined(Pos(Line HK || AB))``
     - :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`
     - G.57, G.62, G.211, Synagoge VII.6
   * - :ref:`D.38 <D.38>` (:ref:`Greek <D.38.el>`)
     - p. 62
     - Prop. XL (pt. 2)
     - ``Given(Pos(AB || CD), ExternalRatio(EF : FG)) -> Determined(Pos(Line HK || AB))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`
     - G.57, G.62, G.211, Synagoge VII.6
   * - :ref:`D.39 <D.39>` (:ref:`Greek <D.39.el>`)
     - p. 66
     - Prop. XLII
     - ``Given(Mag(a), Mag(b), Mag(c)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 1] <D.1>`, :just:`[I.8] <I.8>`, :just:`[I.22] <I.22>`
     - G.29, G.47, Synagoge VII.7
   * - :ref:`D.40 <D.40>` (:ref:`Greek <D.40.el>`)
     - p. 66
     - Prop. XLIII
     - ``Given(Angle(A), Angle(B), Angle(C)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[I.32] <I.32>`, :just:`[VI.4] <VI.4>`
     - G.59, G.213, Synagoge VII.7
   * - :ref:`D.41 <D.41>` (:ref:`Greek <D.41.el>`)
     - p. 66
     - Prop. XLIV
     - ``Given(Angle(A), Ratio(c : b)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[VI.6] <VI.6>`
     - G.215, Synagoge VII.7
   * - :ref:`D.42 <D.42>` (:ref:`Greek <D.42.el>`)
     - p. 74
     - Prop. XLV
     - ``Given(Ratio(a : b), Ratio(b : c)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 39] <D.39>`, :just:`[I.20] <I.20>`, :just:`[I.22] <I.22>`, :just:`[VI.5] <VI.5>`
     - G.45, G.47, G.214, Synagoge VII.7
   * - :ref:`D.43 <D.43>` (:ref:`Greek <D.43.el>`)
     - p. 76
     - Prop. XLVI
     - ``Given(Angle(A) = pi/2, Ratio(hypotenuse c : leg b)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.47] <I.47>`, :just:`[VI.7] <VI.7>`
     - G.79, G.216, Synagoge VII.7
   * - :ref:`D.44 <D.44>` (:ref:`Greek <D.44.el>`)
     - p. 78
     - Prop. XLVII
     - ``Given(Angle(A), Ratio(AB : BC), Sign(cos C)) -> Determined(Species(Triangle ABC)) [SSA diorismos]``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.13] <I.13>`, :just:`[VI.7] <VI.7>`
     - G.37, G.216, Synagoge VII.7
   * - :ref:`D.45 <D.45>` (:ref:`Greek <D.45.el>`)
     - p. 82
     - Prop. XLVIII
     - ``Given(Angle(A), Ratio((b + c) : a)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data 40] <D.40>`, :just:`[Data 44] <D.44>`, :just:`[I.5] <I.5>`, :just:`[I.32] <I.32>`
     - G.25, G.59, Synagoge VII.7
   * - :ref:`D.46 <D.46>` (:ref:`Greek <D.46.el>`)
     - p. 84
     - Prop. XLIX
     - ``Given(Angle(B), Ratio((c + b) : a)) -> Determined(Species(Triangle ABC))``
     - :just:`[Data 40] <D.40>`, :just:`[Data 41] <D.41>`, :just:`[I.5] <I.5>`, :just:`[I.9] <I.9>`, :just:`[I.32] <I.32>`
     - G.25, G.31, G.59, Synagoge VII.7
   * - :ref:`D.47 <D.47>` (:ref:`Greek <D.47.el>`)
     - p. 84
     - Prop. LI
     - ``Given(Species(n-gon P)) -> Determined(Species(ear-triangulation T_1 .. T_{n-2}))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[Data 41] <D.41>`, :just:`[I.32] <I.32>`, :just:`[VI.20] <VI.20>`
     - G.59, G.232, Synagoge VII.7
   * - :ref:`D.48 <D.48>` (:ref:`Greek <D.48.el>`)
     - p. 84
     - Prop. LII
     - ``Given(Species(△ABC), Species(△ABD), SharedBase(AB)) -> Determined(Ratio(△ABC : △ABD))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.37] <I.37>`, :just:`[VI.1] <VI.1>`, :just:`[VI.4] <VI.4>`
     - G.66, G.210, G.213, Synagoge VII.7
   * - :ref:`D.49 <D.49>` (:ref:`Greek <D.49.el>`)
     - p. 88
     - Prop. LIII
     - ``Given(Species(P1 on AB), Species(P2 on AB)) -> Determined(Ratio(Area(P1) : Area(P2)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 22] <D.22>`, :just:`[Data 47] <D.47>`, :just:`[Data 48] <D.48>`, :just:`[VI.20] <VI.20>`
     - G.232, Synagoge VII.7
   * - :ref:`D.50 <D.50>` (:ref:`Greek <D.50.el>`)
     - p. 88
     - Prop. LIV
     - ``Given(Ratio(AB : CD) = r, Similar(E, F)) -> Determined(Ratio(Area(E) : Area(F)) = r^2)``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.11] <VI.11>`, :just:`[VI.19] <VI.19>`, :just:`[VI.20] <VI.20>`
     - G.221, G.231, G.232, Synagoge VII.7
   * - :ref:`D.51 <D.51>` (:ref:`Greek <D.51.el>`)
     - p. 92
     - Prop. LV
     - ``Given(Ratio(AB : CD), Species(E), Species(F)) -> Determined(Ratio(Area(E) : Area(F)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 49] <D.49>`, :just:`[Data 50] <D.50>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - G.229, G.232, Synagoge VII.7
   * - :ref:`D.52 <D.52>` (:ref:`Greek <D.52.el>`)
     - p. 94
     - Prop. LVI
     - ``Given(Mag(AB), Species(P on AB)) -> Determined(Mag(Area(P)))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`
     - G.75, Synagoge VII.7
   * - :ref:`D.53 <D.53>` (:ref:`Greek <D.53.el>`)
     - p. 94
     - Prop. LVII
     - ``Given(Species(A), Species(B), Ratio(s1(A) : s1(B))) -> Determined(Ratio(si(A) : sj(B)))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[V.22] <V.22>`
     - G.205, Synagoge VII.7
   * - :ref:`D.54 <D.54>` (:ref:`Greek <D.54.el>`)
     - p. 94
     - Prop. LIX
     - ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(si(A) : sj(B)))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 49] <D.49>`, :just:`[Data 53] <D.53>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - G.229, G.232, Synagoge VII.7
   * - :ref:`D.55 <D.55>` (:ref:`Greek <D.55.el>`)
     - p. 98
     - Prop. LX
     - ``Given(Species(A), Mag(Area(A))) -> Determined(Mag(sides(A)))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 52] <D.52>`, :just:`[Data 54] <D.54>`, :just:`[I.46] <I.46>`, :just:`[VI.18] <VI.18>`
     - G.75, G.229, Synagoge VII.7
   * - :ref:`D.56 <D.56>` (:ref:`Greek <D.56.el>`)
     - p. 100
     - Prop. LXIII
     - ``Given(Equiangular(P1, P2), Ratio(P1 : P2) = k) -> Determined(s1 : t1 = t2 : (s2 / k))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - G.210, G.225, Synagoge VII.8
   * - :ref:`D.57 <D.57>` (:ref:`Greek <D.57.el>`)
     - p. 102
     - Prop. LXI
     - ``Given(Mag(Area S), Mag(Base a), Mag(Angle theta)) -> Determined(Mag(Breadth x))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 52] <D.52>`, :just:`[I.31] <I.31>`, :just:`[I.46] <I.46>`, :just:`[VI.1] <VI.1>`
     - G.58, G.75, G.210, Synagoge VII.8
   * - :ref:`D.58 <D.58>` (:ref:`Greek <D.58.el>`)
     - p. 104
     - Prop. LXXXIII
     - ``Given(Mag(S), Mag(a), Species(Defect)) -> Determined(Roots of a*x - c*x^2 = S) [diorismos]``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.5] <II.5>`, :just:`[VI.24] <VI.24>`, :just:`[VI.27] <VI.27>`, :just:`[VI.28] <VI.28>`
     - G.87, G.236, G.239, Synagoge VII.8
   * - :ref:`D.59 <D.59>` (:ref:`Greek <D.59.el>`)
     - p. 106
     - Prop. LXXXIV
     - ``Given(Mag(S), Mag(a), Species(Excess)) -> Determined(Positive root of a*x + c*x^2 = S)``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 52] <D.52>`, :just:`[Data 55] <D.55>`, :just:`[II.6] <II.6>`, :just:`[VI.24] <VI.24>`, :just:`[VI.29] <VI.29>`
     - G.88, G.236, G.241, Synagoge VII.8
   * - :ref:`D.60 <D.60>` (:ref:`Greek <D.60.el>`)
     - p. 108
     - Prop. LXXXII
     - ``Given(Species(P), Mag(Area(P)), Mag(Gnomon G)) -> Determined(Mag(Sides of P +/- G))``
     - :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 55] <D.55>`, :just:`[VI.24] <VI.24>`
     - G.236, Synagoge VII.8
   * - :ref:`D.61 <D.61>` (:ref:`Greek <D.61.el>`)
     - p. 108
     - Prop. LXIX
     - ``Given(Species(P on CB), Angle(CD), Ratio(Area(P) : Area(CD))) -> Determined(Species(CD))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 49] <D.49>`, :just:`[I.13] <I.13>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`
     - G.37, G.56, G.58, Synagoge VII.8
   * - :ref:`D.62 <D.62>` (:ref:`Greek <D.62.el>`)
     - p. 112
     - Prop. LXX
     - ``Given(Ratio(AB : CD), Species(AEB on AB), Angle(DF), Ratio(AEB : DF)) -> Determined(Species(DF))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 50] <D.50>`, :just:`[Data 61] <D.61>`, :just:`[VI.18] <VI.18>`, :just:`[VI.20] <VI.20>`
     - G.229, G.232, Synagoge VII.8
   * - :ref:`D.63 <D.63>` (:ref:`Greek <D.63.el>`)
     - p. 114
     - Omitted (case of Prop. LIII)
     - ``Given(Species(△ABC)) -> Determined(Ratio(a^2 : △ABC), Ratio(b^2 : △ABC), Ratio(c^2 : △ABC))``
     - :just:`[Data 49] <D.49>`, :just:`[I.46] <I.46>`
     - G.75, Synagoge VII.8
   * - :ref:`D.64 <D.64>` (:ref:`Greek <D.64.el>`)
     - p. 114
     - Prop. LXXIV
     - ``Given(ObtuseAngle B) -> Determined(Ratio((b^2 - a^2 - c^2) : △ABC) = -4 cot B)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.12] <II.12>`, :just:`[VI.1] <VI.1>`
     - G.35, G.59, G.94, Synagoge VII.8
   * - :ref:`D.65 <D.65>` (:ref:`Greek <D.65.el>`)
     - p. 118
     - Prop. LXXV
     - ``Given(AcuteAngle B) -> Determined(Ratio((a^2 + c^2 - b^2) : △ABC) = 4 cot B)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.13] <II.13>`, :just:`[VI.1] <VI.1>`
     - G.35, G.59, G.95, Synagoge VII.8
   * - :ref:`D.66 <D.66>` (:ref:`Greek <D.66.el>`)
     - p. 120
     - Prop. LXII Cor.
     - ``Given(Angle A) -> Determined(Ratio((AB * AC) : Area(△ABC)) = 2 / sin A)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.1] <VI.1>`
     - G.35, G.70, G.210, Synagoge VII.8
   * - :ref:`D.67 <D.67>` (:ref:`Greek <D.67.el>`)
     - p. 120
     - Prop. LXXVI
     - ``Given(Angle A) -> Determined(Ratio(((b + c)^2 - a^2) : △ABC) = 4*(1 + cos A) / sin A)``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 50] <D.50>`, :just:`[Data 66] <D.66>`, :just:`[I.5] <I.5>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`, :just:`[I.32] <I.32>`, :just:`[II.6] <II.6>`, :just:`[VI.2] <VI.2>`, :just:`[VI.16] <VI.16>`
     - G.25, G.37, G.58, Synagoge VII.8
   * - :ref:`D.68 <D.68>` (:ref:`Greek <D.68.el>`)
     - p. 126
     - Prop. LXV
     - ``Given(Equiangular(P1, P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 56] <D.56>`, :just:`[I.31] <I.31>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - G.58, G.210, G.225, Synagoge VII.9
   * - :ref:`D.69 <D.69>` (:ref:`Greek <D.69.el>`)
     - p. 128
     - Prop. LXVI
     - ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.12] <I.12>`, :just:`[I.23] <I.23>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`
     - G.35, G.48, G.58, Synagoge VII.9
   * - :ref:`D.70 <D.70>` (:ref:`Greek <D.70.el>`)
     - p. 130
     - Props. LXVII–LXVIII
     - ``Given(Angle(P1), Angle(P2), Ratio(s1 : t1), Ratio(s2 : t2)) -> Determined(Ratio(P1 : P2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`, :just:`[VI.23] <VI.23>`
     - G.48, G.64, G.210, Synagoge VII.9
   * - :ref:`D.71 <D.71>` (:ref:`Greek <D.71.el>`)
     - p. 134
     - Prop. LXVIII Cor. 1
     - ``Given(Angle(A), Angle(D), Ratio(c1 : c2), Ratio(b1 : b2)) -> Determined(Ratio(△1 : △2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`
     - G.58, G.62, G.193, Synagoge VII.9
   * - :ref:`D.72 <D.72>` (:ref:`Greek <D.72.el>`)
     - p. 136
     - Prop. LXVIII Cor. 2
     - ``Given(Ratio(b1 : b2), Ratio(d1 : d2), Angle(phi1), Angle(phi2)) -> Determined(Ratio(△1 : △2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 70] <D.70>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`, :just:`[I.41] <I.41>`
     - G.56, G.58, G.62, Synagoge VII.9
   * - :ref:`D.73 <D.73>` (:ref:`Greek <D.73.el>`)
     - p. 138
     - Prop. LXIV (pt. 2)
     - ``Given(Angle(P1), Angle(P2), CB:FG = EF:CK, Ratio(AC:CK)) -> Determined(Ratio(P1 : P2))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[Data 70] <D.70>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - G.48, G.64, G.210, Synagoge VII.9
   * - :ref:`D.74 <D.74>` (:ref:`Greek <D.74.el>`)
     - p. 142
     - Prop. LXIV (pt. 1; cf. LXIII)
     - ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2)) -> Determined(CB : FG = EF : K with GivenRatio(AC : K))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 56] <D.56>`, :just:`[I.23] <I.23>`, :just:`[I.35] <I.35>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`
     - G.48, G.64, G.210, Synagoge VII.9
   * - :ref:`D.75 <D.75>` (:ref:`Greek <D.75.el>`)
     - p. 144
     - Prop. LXIV Cor.
     - ``Given(Angle(A), Angle(D), Ratio(△1 : △2)) -> Determined(AB : DE = DF : K with GivenRatio(AC : K))``
     - :just:`[Data 74] <D.74>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`
     - G.62, G.193, Synagoge VII.9
   * - :ref:`D.76 <D.76>` (:ref:`Greek <D.76.el>`)
     - p. 144
     - Prop. L
     - ``Given(Species(△ABC), AD perp BC) -> Determined(Ratio(AD : BC))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`
     - G.35, G.59, Synagoge VII.7
   * - :ref:`D.77 <D.77>` (:ref:`Greek <D.77.el>`)
     - p. 148
     - Omitted (dup. of Prop. LIX / D.54)
     - ``Given(Species(A), Species(B), Ratio(Area(A) : Area(B))) -> Determined(Ratio(s(A) : s(B)))``
     - :just:`[Data 54] <D.54>`, :just:`[VI.20] <VI.20>`
     - G.232
   * - :ref:`D.78 <D.78>` (:ref:`Greek <D.78.el>`)
     - p. 148
     - Omitted (case of Prop. LXX / D.62)
     - ``Given(Species(A), Ratio(A : B), Ratio(s(A) : s1(B)), Angle(B)) -> Determined(Species(B))``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 62] <D.62>`, :just:`[VI.14] <VI.14>`
     - G.225
   * - :ref:`D.79 <D.79>` (:ref:`Greek <D.79.el>`)
     - p. 152
     - Prop. LXXVII Cor. 1
     - ``Given(∠BAC = ∠EDF, BC : h_A = EF : h_D) -> Determined(△ABC ~ △DEF)``
     - :just:`[Data Def. 3] <D.def.3>`, :just:`[Data Def. 7] <D.def.7>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[III.21] <III.21>`, :just:`[VI.4] <VI.4>`
     - G.35, G.124, G.213, Synagoge VII.9
   * - :ref:`D.80 <D.80>` (:ref:`Greek <D.80.el>`)
     - p. 154
     - Prop. LXXVIII
     - ``Given(Angle A, Ratio((b*c) : a^2)) -> Determined(Species(△ABC))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 66] <D.66>`, :just:`[Data 68] <D.68>`, :just:`[Data 79] <D.79>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`
     - G.35, G.70, G.213, Synagoge VII.9
   * - :ref:`D.81 <D.81>` (:ref:`Greek <D.81.el>`)
     - p. 158
     - Prop. LXXI
     - ``Given(B^2 = A*C, E^2 = D*F) -> (Given(A:D, C:F) -> Given(B:E)) & (Given(A:D, B:E) -> Given(C:F))``
     - :just:`[Data 8] <D.8>`, :just:`[Data 24] <D.24>`, :just:`[Data 50] <D.50>`, :just:`[Data 54] <D.54>`, :just:`[Data 70] <D.70>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`
     - G.228, G.232, Synagoge VII.9
   * - :ref:`D.82 <D.82>` (:ref:`Greek <D.82.el>`)
     - p. 160
     - Prop. LXXII
     - ``Given(A : B = C : D, Ratio(B : E) = k) -> Determined(Ratio(D : F) = k when A : E = C : F)``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.22] <V.22>`
     - G.189, G.195, G.205, Synagoge VII.9
   * - :ref:`D.83 <D.83>` (:ref:`Greek <D.83.el>`)
     - p. 160
     - Prop. LXXIII
     - ``Given(A * D = B * E, Ratio(C : E) = k) -> Determined(D : C = B : (A / k))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 68] <D.68>`, :just:`[V.16] <V.16>`, :just:`[V.23] <V.23>`, :just:`[VI.16] <VI.16>`
     - G.195, G.206, G.227, Synagoge VII.9
   * - :ref:`D.84 <D.84>` (:ref:`Greek <D.84.el>`)
     - p. 164
     - Prop. LXXXV
     - ``Given(Angle B, Area(x, y) = S, y - x = d) -> Determined(Mag(x), Mag(y))``
     - :just:`[Data 3] <D.3>`, :just:`[Data 59] <D.59>`, :just:`[I.31] <I.31>`
     - G.58, Synagoge VII.10
   * - :ref:`D.85 <D.85>` (:ref:`Greek <D.85.el>`)
     - p. 166
     - Prop. LXXXVI
     - ``Given(Angle B, Area(x, y) = S, x + y = s) -> Determined(Mag(x), Mag(y)) [diorismos]``
     - :just:`[Data 4] <D.4>`, :just:`[Data 58] <D.58>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`
     - G.37, G.58, Synagoge VII.10
   * - :ref:`D.86 <D.86>` (:ref:`Greek <D.86.el>`)
     - p. 168
     - Prop. LXXXIX (cf. LXXXVII–LXXXVIII)
     - ``Given(Angle B, x*y*sin B = S, (y^2 - D) : x^2 = k) -> Determined(Mag(x), Mag(y))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 55] <D.55>`, :just:`[Data 57] <D.57>`, :just:`[Data 58] <D.58>`, :just:`[Data 59] <D.59>`, :just:`[Data 68] <D.68>`, :just:`[II.4] <II.4>`, :just:`[II.6] <II.6>`, :just:`[VI.1] <VI.1>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`
     - G.85, G.88, G.210, Synagoge VII.10
   * - :ref:`D.87 <D.87>` (:ref:`Greek <D.87.el>`)
     - p. 172
     - Prop. XCI
     - ``Given(CircleRadius R, InscribedAngle theta) -> Determined(Mag(Chord BC = 2*R*sin theta))``
     - :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`, :just:`[Data 40] <D.40>`, :just:`[Data 53] <D.53>`, :just:`[III.21] <III.21>`, :just:`[III.31] <III.31>`
     - G.124, G.139, Synagoge VII.11
   * - :ref:`D.88 <D.88>` (:ref:`Greek <D.88.el>`)
     - p. 172
     - Prop. XCII
     - ``Given(CircleRadius R, Mag(Chord BC <= 2R)) -> Determined(Mag(InscribedAngle BAC))``
     - :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 1] <D.1>`, :just:`[Data 3] <D.3>`, :just:`[Data 43] <D.43>`, :just:`[III.21] <III.21>`, :just:`[III.22] <III.22>`, :just:`[III.31] <III.31>`
     - G.124, G.125, G.139, Synagoge VII.11
   * - :ref:`D.89 <D.89>` (:ref:`Greek <D.89.el>`)
     - p. 172
     - Prop. XCIII
     - ``Given(PosMag(Circle(D, R)), Pos(B on circle), Mag(InscribedAngle BAC)) -> Determined(Pos(C))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 29] <D.29>`, :just:`[III.1] <III.1>`, :just:`[III.20] <III.20>`
     - G.98, G.123, Synagoge VII.11
   * - :ref:`D.90 <D.90>` (:ref:`Greek <D.90.el>`)
     - p. 176
     - Prop. XCIV
     - ``Given(PosMag(Circle(O, R)), Pos(D outside)) -> Determined(Pos(DA), Mag(DA = sqrt(OD^2 - R^2)))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 43] <D.43>`, :just:`[Data 53] <D.53>`, :just:`[III.17] <III.17>`, :just:`[III.18] <III.18>`, :just:`[III.31] <III.31>`
     - G.119, G.120, G.139, Synagoge VII.11
   * - :ref:`D.91 <D.91>` (:ref:`Greek <D.91.el>`)
     - p. 178
     - Prop. XCV
     - ``Given(PosMag(Circle(O, R)), Pos(External D)) -> Determined(Mag(DB * DC = OD^2 - R^2))``
     - :just:`[Data 52] <D.52>`, :just:`[Data 90] <D.90>`, :just:`[III.17] <III.17>`, :just:`[III.36] <III.36>`
     - G.119, G.144, Synagoge VII.11
   * - :ref:`D.92 <D.92>` (:ref:`Greek <D.92.el>`)
     - p. 178
     - Prop. XCVI
     - ``Given(PosMag(Circle(O, R)), Pos(Internal D)) -> Determined(Mag(BD * DC = R^2 - OD^2))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 52] <D.52>`, :just:`[III.1] <III.1>`, :just:`[III.35] <III.35>`
     - G.98, G.143, Synagoge VII.11
   * - :ref:`D.93 <D.93>` (:ref:`Greek <D.93.el>`)
     - p. 178
     - Prop. XCVII (cf. Prop. XCVIII [Stanhope])
     - ``Given(CircleRadius R, InscribedAngle A, Bisector AD cap BC = E) -> Determined(Ratio((AB+AC):AD), Mag((AB+AC)*ED))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 52] <D.52>`, :just:`[Data 87] <D.87>`, :just:`[III.21] <III.21>`, :just:`[III.26] <III.26>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[VI.3] <VI.3>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`
     - G.124, G.133, G.190, Synagoge VII.11
   * - :ref:`D.94 <D.94>` (:ref:`Greek <D.94.el>`)
     - p. 184
     - Prop. XCIX (cf. Prop. C [Stewart])
     - ``Given(PosMag(Circle(H, R)), Pos(D on diam BC), ∠DAE = 90°, EF || DA) -> Determined(Pos(F = 2H - D), Mag(AD * EF = |R^2 - HD^2|))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 91] <D.91>`, :just:`[Data 92] <D.92>`, :just:`[I.4] <I.4>`, :just:`[I.26] <I.26>`, :just:`[I.29] <I.29>`, :just:`[III.31] <III.31>`, :just:`[III.35] <III.35>`
     - G.24, G.51, G.56, Synagoge VII.11
