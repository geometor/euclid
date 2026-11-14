:order: 22
:type: summary
:canonical_id: D.unit.2
:folio: Menge pp. 42–66
:book: Propositions 25–38: Position & Parallels

.. _data-unit-2-summary:

==================================================================================
Unit 2: Position, Angles & Parallel Loci (Propositions 25–38) — Analytical Summary
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
     - :ref:`EN <D.25>` · :ref:`EL <D.25.el>`
   * - :ref:`D.26 <D.26>`
     - Prop. XXIX
     - ``Given(Pos(A), Pos(B)) -> Determined(Pos(AB), Mag(AB))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Post. 1] <I.post.1>`, :just:`[Post. 3] <I.post.3>`
     - :ref:`EN <D.26>` · :ref:`EL <D.26.el>`
   * - :ref:`D.27 <D.27>`
     - Prop. XXX
     - ``Given(Pos(Ray A->), Mag(AB), Pos(A)) -> Determined(Pos(B))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Post. 3] <I.post.3>`, :just:`[I Def. 15] <I.def.15>`
     - :ref:`EN <D.27>` · :ref:`EL <D.27.el>`
   * - :ref:`D.28 <D.28>`
     - Prop. XXXI
     - ``Given(Pos(A), Pos(Line BC)) -> Determined(Pos(Parallel(A, BC)))``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[I.27] <I.27>`, :just:`[I.29] <I.29>`, :just:`[I.30] <I.30>`, :just:`[I.31] <I.31>`
     - :ref:`EN <D.28>` · :ref:`EL <D.28.el>`
   * - :ref:`D.29 <D.29>`
     - Prop. XXXII
     - ``Given(Pos(Line AB), Pos(C in AB), Mag(Angle theta)) -> Determined(Pos(Ray CD))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[I.23] <I.23>`
     - :ref:`EN <D.29>` · :ref:`EL <D.29.el>`
   * - :ref:`D.30 <D.30>`
     - Prop. XXXIII
     - ``Given(Pos(A), Pos(Line BC), Mag(Angle ADC)) -> Determined(Pos(Line AD))``
     - :just:`[Data 28] <D.28>`, :just:`[Data 29] <D.29>`, :just:`[I.23] <I.23>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`
     - :ref:`EN <D.30>` · :ref:`EL <D.30.el>`
   * - :ref:`D.31 <D.31>`
     - Prop. XXXIV
     - ``Given(Pos(A), Pos(Line BC), Mag(AD >= dist(A, BC))) -> Determined(Pos(AD)) [2-root diorismos]``
     - :just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[I.12] <I.12>`, :just:`[Post. 3] <I.post.3>`
     - :ref:`EN <D.31>` · :ref:`EL <D.31.el>`
   * - :ref:`D.32 <D.32>`
     - Prop. XXXV
     - ``Given(Pos(AB || CD), Mag(Angle BEF)) -> Determined(Mag(EF))``
     - :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.29] <I.29>`, :just:`[I.31] <I.31>`, :just:`[I.34] <I.34>`
     - :ref:`EN <D.32>` · :ref:`EL <D.32.el>`
   * - :ref:`D.33 <D.33>`
     - Prop. XXXVI
     - ``Given(Pos(AB || CD), Mag(EF >= strip_width)) -> Determined(Mag(Angle BEF))``
     - :just:`[Data Def. 1] <D.def.1>`, :just:`[Data Def. 4] <D.def.4>`, :just:`[Data 28] <D.28>`, :just:`[Data 31] <D.31>`, :just:`[I.29] <I.29>`, :just:`[I.34] <I.34>`
     - :ref:`EN <D.33>` · :ref:`EL <D.33.el>`
   * - :ref:`D.34 <D.34>`
     - Prop. XXXVIII
     - ``Given(Pos(AB || CD), Pos(Pole E)) -> Determined(Ratio(EF : FG))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 30] <D.30>`, :just:`[I.12] <I.12>`, :just:`[VI.2] <VI.2>`, :just:`[VI.4] <VI.4>`
     - :ref:`EN <D.34>` · :ref:`EL <D.34.el>`
   * - :ref:`D.35 <D.35>`
     - Prop. XXXIX (pt. 1)
     - ``Given(Pos(Pole A), Pos(Line BC), InternalRatio(AE : ED)) -> Determined(Pos(Line FEG || BC))``
     - :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`
     - :ref:`EN <D.35>` · :ref:`EL <D.35.el>`
   * - :ref:`D.36 <D.36>`
     - Prop. XXXIX (pt. 2)
     - ``Given(Pos(Pole A), Pos(Line BC), ExternalRatio(AD : DE)) -> Determined(Pos(Line FEG || BC))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 6] <D.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[VI.2] <VI.2>`
     - :ref:`EN <D.36>` · :ref:`EL <D.36.el>`
   * - :ref:`D.37 <D.37>`
     - Prop. XL (pt. 1)
     - ``Given(Pos(AB || CD), InternalRatio(EG : GF)) -> Determined(Pos(Line HK || AB))``
     - :just:`[Data 7] <D.7>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`
     - :ref:`EN <D.37>` · :ref:`EL <D.37.el>`
   * - :ref:`D.38 <D.38>`
     - Prop. XL (pt. 2)
     - ``Given(Pos(AB || CD), ExternalRatio(EF : FG)) -> Determined(Pos(Line HK || AB))``
     - :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 28] <D.28>`, :just:`[Data 30] <D.30>`, :just:`[I.30] <I.30>`, :just:`[I.34] <I.34>`, :just:`[VI.2] <VI.2>`
     - :ref:`EN <D.38>` · :ref:`EL <D.38.el>`

Computational Primitives (``geometor.model`` & SymPy)
-----------------------------------------------------

* :ref:`D.25 <D.25>` (*Prop. XXVIII*): Fundamental `model.intersect(L1, L2)` primitive in geometor.model.
* :ref:`D.26 <D.26>` (*Prop. XXIX*): Fundamental `model.set_line(A, B)` and Euclidean metric norm |B - A|.
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
