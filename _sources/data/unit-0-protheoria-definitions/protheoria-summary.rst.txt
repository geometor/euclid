:order: 2
:type: summary
:canonical_id: D.unit.0
:folio: Menge 234–256, 2–4
:book: Protheoria & Definitions

.. _data-unit-0-summary:

=======================================================================
Unit 0: Marinus's Protheoria & Definitions 1–15 — Analytical Summary
=======================================================================

Marinus's Fourfold Epistemic Classification (*Menge pp. 234–252*)
-----------------------------------------------------------------

:person:`Marinus of Neapolis <marinus>` organizes ancient definitions of the :term:`given <dedomenon>` (*δεδομένον*) across four fundamental binary predicates and three relational standpoints:

.. list-table::
   :header-rows: 1
   :widths: 22 18 22 38

   * - Predicate Pair
     - Standpoint
     - Ancient Authority
     - Diagnostic Geometric Criterion & Counterexample
   * - :term:`τεταγμένον <tetagmenon>` / :term:`ἄτακτον <atakton>` (*Ordered / Unordered*)
     - Nature itself (*πρὸς τὴν φύσιν*)
     - :person:`Apollonius of Perga <apollonius>` (*On Vergings*)
     - Unique invariance. Line through 2 points or circle through 3 is *ordered*; circle through 2 points or general scalene triangle is *unordered*. Quadrature of the circle is *ordered* yet *unprocurable*.
   * - :term:`γνώριμον <gnorimon>` / *ἄγνωστον* (*Known / Unknown*)
     - Relative to us (*πρὸς ἡμᾶς*)
     - :person:`Diodorus of Alexandria <diodorus>`
     - Cognitive grasp (**Genus** of *given*). Uniqueness of tangent to :person:`Archimedes' <archimedes>` spiral is *known* by *reductio* before its construction is *procurable*.
   * - :term:`πόριμον <porimon>` / :term:`ἄπορον <aporon>` (*Procurable / Unprocurable*)
     - Constructive power (*ἐν πόρῳ*)
     - :person:`Euclid <euclid>` (*Data* Defs. 1–2)
     - Constructive exhibibility from elementary postulates (**Specific Differentia** of *given*). Converts coextensively with *comprehensible* (*καταληπτόν*).
   * - :term:`ῥητόν <rheton>` / :term:`ἄλογον <alogon>` (*Rational / Irrational*)
     - Unit measure (*πρὸς τὸ μέτρον*)
     - :person:`Claudius Ptolemy <ptolemy>` (*Syntaxis*)
     - Numerical commensurability. Strictly narrower than *given*: $\sqrt{2}$ and Book X binomials (:just:`[X.36] <X.36>`) are *irrational* yet completely *given*.

**Marinus's Canon (§ 15)**: $\text{Δεδομένον} \iff \text{Γνώριμον (Genus)} \land \text{Πόριμον (Differentia)}$.

Conspectus of the Fifteen Definitions (*Menge pp. 2–4*)
-------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 12 16 24 38 10

   * - Menge ID
     - Simson ID
     - Mode of Givenness
     - Functional Predicate
     - Tracks
   * - :ref:`D.def.1 <D.def.1>`
     - Def. I
     - Magnitude (μεγέθει)
     - ``GivenMagnitude(X) := exists constructible X' with X' = X``
     - :ref:`EN <D.def.1>` · :ref:`EL <D.def.1.el>`
   * - :ref:`D.def.2 <D.def.2>`
     - Def. II
     - Ratio (λόγῳ)
     - ``GivenRatio(A : B) := exists GivenMagnitude(C, D) with A : B = C : D``
     - :ref:`EN <D.def.2>` · :ref:`EL <D.def.2.el>`
   * - :ref:`D.def.3 <D.def.3>`
     - Def. III
     - Species (εἴδει)
     - ``GivenSpecies(P) := forall i,j: GivenAngle(ang_i(P)) and GivenRatio(s_i(P) : s_j(P))``
     - :ref:`EN <D.def.3>` · :ref:`EL <D.def.3.el>`
   * - :ref:`D.def.4 <D.def.4>`
     - Def. IV (cf. Def. A)
     - Position (θέσει)
     - ``GivenPosition(X) := X is invariant in the fixed planar reference frame (and constructible)``
     - :ref:`EN <D.def.4>` · :ref:`EL <D.def.4.el>`
   * - :ref:`D.def.5 <D.def.5>`
     - Def. V
     - Circle in Magnitude
     - ``GivenCircleMag(C) := GivenMagnitude(radius(C))``
     - :ref:`EN <D.def.5>` · :ref:`EL <D.def.5.el>`
   * - :ref:`D.def.6 <D.def.6>`
     - Def. VI
     - Circle in Position & Magnitude
     - ``GivenCirclePosMag(C) := GivenPosition(center(C)) and GivenMagnitude(radius(C))``
     - :ref:`EN <D.def.6>` · :ref:`EL <D.def.6.el>`
   * - :ref:`D.def.7 <D.def.7>`
     - Def. VII
     - Circular Segment in Magnitude
     - ``GivenSegmentMag(S) := GivenAngle(inscribed_angle(S)) and GivenMagnitude(base(S))``
     - :ref:`EN <D.def.7>` · :ref:`EL <D.def.7.el>`
   * - :ref:`D.def.8 <D.def.8>`
     - Def. VIII
     - Circular Segment in Position & Magnitude
     - ``GivenSegmentPosMag(S) := GivenAngle(inscribed_angle(S)) and GivenPosMag(base(S))``
     - :ref:`EN <D.def.8>` · :ref:`EL <D.def.8.el>`
   * - :ref:`D.def.9 <D.def.9>`
     - Def. IX
     - Affine Excess (δοθέντι μεῖζον)
     - ``ExceedsByGiven(A, B) := exists GivenMagnitude(D) with A - D = B``
     - :ref:`EN <D.def.9>` · :ref:`EL <D.def.9.el>`
   * - :ref:`D.def.10 <D.def.10>`
     - Def. X
     - Affine Defect (δοθέντι ἔλασσον)
     - ``LessByGiven(A, B) := exists GivenMagnitude(D) with A + D = B``
     - :ref:`EN <D.def.10>` · :ref:`EL <D.def.10.el>`
   * - :ref:`D.def.11 <D.def.11>`
     - Omitted (expanded verbally in Props. XIV–XXVII)
     - Affine-Ratio Excess (δοθέντι μεῖζον ἢ ἐν λόγῳ)
     - ``GreaterThanInRatio(A, B) := exists GivenMagnitude(D), GivenRatio(k) with (A - D) : B = k``
     - :ref:`EN <D.def.11>` · :ref:`EL <D.def.11.el>`
   * - :ref:`D.def.12 <D.def.12>`
     - Omitted (expanded verbally in Props. XIV–XXVII)
     - Affine-Ratio Defect (δοθέντι ἔλασσον ἢ ἐν λόγῳ)
     - ``LessThanInRatio(A, B) := exists GivenMagnitude(D), GivenRatio(k) with (A + D) : B = k``
     - :ref:`EN <D.def.12>` · :ref:`EL <D.def.12.el>`
   * - :ref:`D.def.13 <D.def.13>`
     - Omitted (late scholium; bracketed by Menge)
     - Directed Ordinate [Bracketed Scholium]
     - ``Kategmene(P, L, theta) := segment from GivenPoint(P) to GivenLine(L) at GivenAngle(theta)``
     - :ref:`EN <D.def.13>` · :ref:`EL <D.def.13.el>`
   * - :ref:`D.def.14 <D.def.14>`
     - Omitted (late scholium; bracketed by Menge)
     - Erected Line [Bracketed Scholium]
     - ``Anegmene(P, L, theta) := ray from GivenPoint(P) on GivenLine(L) at GivenAngle(theta)``
     - :ref:`EN <D.def.14>` · :ref:`EL <D.def.14.el>`
   * - :ref:`D.def.15 <D.def.15>`
     - Omitted (late scholium; bracketed by Menge)
     - Parallel to Position [Bracketed Scholium]
     - ``ParaThesei(P, L) := line through GivenPoint(P) parallel to GivenLine(L)``
     - :ref:`EN <D.def.15>` · :ref:`EL <D.def.15.el>`
