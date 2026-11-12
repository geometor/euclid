:order: 62
:type: summary
:canonical_id: D.unit.6
:folio: Menge pp. 164–186
:book: Propositions 84–94: Circles, Chords & Angle Bisectors

.. _data-unit-6-summary:

================================================================================================================
Unit 6: Hyperbolic/Elliptic Systems, Circles, Chords & Angle Bisectors (Propositions 84–94) — Analytical Summary
================================================================================================================

Unit Overview & Role in Greek Geometric Analysis
------------------------------------------------

Canonical two-line systems xy = A² with x − y = d (D.84), x + y = s (D.85), and x² − y² = C² (D.86); circles given in magnitude and position, inscribed angle loci, and chord/arc determination (D.87–D.89); secant/chord power of a point (D.90–D.92); the celebrated Prop. 93 interior angle-bisector theorem; and its orthogonal chord-reflection corollary (D.94).

* **Scope**: 11 propositions (D.84–D.94 (Simson LXXXV–C), *Menge* pp. 164–186).
* **Analytical Function**: Each proposition below compiles into a forward-chaining inference rule ``Given(...) -> Determined(...)`` within :person:`Pappus's <pappus>` :term:`Treasury of Analysis <analyomenos-topos>` (:cite:`Synagoge Book VII <pappus:synagoge>`) and ``geometor.model`` symbolic DAGs.

Functional Conspectus (D.84–D.94 (Simson LXXXV–C))
--------------------------------------------------

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
     - :ref:`EN <D.84>` · :ref:`EL <D.84.el>`
   * - :ref:`D.85 <D.85>`
     - Prop. LXXXVI
     - ``Given(Angle B, Area(x, y) = S, x + y = s) -> Determined(Mag(x), Mag(y)) [diorismos]``
     - :just:`[Data 4] <D.4>`, :just:`[Data 58] <D.58>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`
     - :ref:`EN <D.85>` · :ref:`EL <D.85.el>`
   * - :ref:`D.86 <D.86>`
     - Prop. LXXXIX (cf. LXXXVII–LXXXVIII)
     - ``Given(Angle B, x*y*sin B = S, (y^2 - D) : x^2 = k) -> Determined(Mag(x), Mag(y))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 55] <D.55>`, :just:`[Data 57] <D.57>`, :just:`[Data 58] <D.58>`, :just:`[Data 59] <D.59>`, :just:`[Data 68] <D.68>`, :just:`[II.4] <II.4>`, :just:`[II.6] <II.6>`, :just:`[VI.1] <VI.1>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`
     - :ref:`EN <D.86>` · :ref:`EL <D.86.el>`
   * - :ref:`D.87 <D.87>`
     - Prop. XCI
     - ``Given(CircleRadius R, InscribedAngle theta) -> Determined(Mag(Chord BC = 2*R*sin theta))``
     - :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`, :just:`[Data 40] <D.40>`, :just:`[Data 53] <D.53>`, :just:`[III.21] <III.21>`, :just:`[III.31] <III.31>`
     - :ref:`EN <D.87>` · :ref:`EL <D.87.el>`
   * - :ref:`D.88 <D.88>`
     - Prop. XCII
     - ``Given(CircleRadius R, Mag(Chord BC <= 2R)) -> Determined(Mag(InscribedAngle BAC))``
     - :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 1] <D.1>`, :just:`[Data 3] <D.3>`, :just:`[Data 43] <D.43>`, :just:`[III.21] <III.21>`, :just:`[III.22] <III.22>`, :just:`[III.31] <III.31>`
     - :ref:`EN <D.88>` · :ref:`EL <D.88.el>`
   * - :ref:`D.89 <D.89>`
     - Prop. XCIII
     - ``Given(PosMag(Circle(D, R)), Pos(B on circle), Mag(InscribedAngle BAC)) -> Determined(Pos(C))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 29] <D.29>`, :just:`[III.1] <III.1>`, :just:`[III.20] <III.20>`
     - :ref:`EN <D.89>` · :ref:`EL <D.89.el>`
   * - :ref:`D.90 <D.90>`
     - Prop. XCIV
     - ``Given(PosMag(Circle(O, R)), Pos(D outside)) -> Determined(Pos(DA), Mag(DA = sqrt(OD^2 - R^2)))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 43] <D.43>`, :just:`[Data 53] <D.53>`, :just:`[III.17] <III.17>`, :just:`[III.18] <III.18>`, :just:`[III.31] <III.31>`
     - :ref:`EN <D.90>` · :ref:`EL <D.90.el>`
   * - :ref:`D.91 <D.91>`
     - Prop. XCV
     - ``Given(PosMag(Circle(O, R)), Pos(External D)) -> Determined(Mag(DB * DC = OD^2 - R^2))``
     - :just:`[Data 52] <D.52>`, :just:`[Data 90] <D.90>`, :just:`[III.17] <III.17>`, :just:`[III.36] <III.36>`
     - :ref:`EN <D.91>` · :ref:`EL <D.91.el>`
   * - :ref:`D.92 <D.92>`
     - Prop. XCVI
     - ``Given(PosMag(Circle(O, R)), Pos(Internal D)) -> Determined(Mag(BD * DC = R^2 - OD^2))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 52] <D.52>`, :just:`[III.1] <III.1>`, :just:`[III.35] <III.35>`
     - :ref:`EN <D.92>` · :ref:`EL <D.92.el>`
   * - :ref:`D.93 <D.93>`
     - Prop. XCVII (cf. Prop. XCVIII [Stanhope])
     - ``Given(CircleRadius R, InscribedAngle A, Bisector AD cap BC = E) -> Determined(Ratio((AB+AC):AD), Mag((AB+AC)*ED))``
     - :just:`[Data 1] <D.1>`, :just:`[Data 52] <D.52>`, :just:`[Data 87] <D.87>`, :just:`[III.21] <III.21>`, :just:`[III.26] <III.26>`, :just:`[V.12] <V.12>`, :just:`[V.16] <V.16>`, :just:`[VI.3] <VI.3>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`
     - :ref:`EN <D.93>` · :ref:`EL <D.93.el>`
   * - :ref:`D.94 <D.94>`
     - Prop. XCIX (cf. Prop. C [Stewart])
     - ``Given(PosMag(Circle(H, R)), Pos(D on diam BC), ∠DAE = 90°, EF || DA) -> Determined(Pos(F = 2H - D), Mag(AD * EF = |R^2 - HD^2|))``
     - :just:`[Data Def. 6] <D.def.6>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 91] <D.91>`, :just:`[Data 92] <D.92>`, :just:`[I.4] <I.4>`, :just:`[I.26] <I.26>`, :just:`[I.29] <I.29>`, :just:`[III.31] <III.31>`, :just:`[III.35] <III.35>`
     - :ref:`EN <D.94>` · :ref:`EL <D.94.el>`

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
