:order: 1
:type: definitions
:canonical_id: D.def
:breadcrumb_title: Definitions
:book: Definitions
:layout: book
:title: Definitions of Euclid's Data
:folio: Menge 2–4
:page: 2

.. _data-definitions:
.. _data-definitions-el:

========================================
Definitions (*Ὅροι*) of Euclid's *Data*
========================================

.. picture:: /_static/figures/data_01_taxonomy.svg
   :alt: Taxonomy of Givenness: Magnitude (Def. 1), Species (Def. 3), and Position (Defs. 4 & 6)

Interactive diagram key (:cite:`Menge pp. 2–4 <menge:1896>`): Panel 1 illustrates **Magnitude** (:just:`[Data Def. 1] <D.def.1>`), constructing segment :g:`CD <data_01_taxonomy:/ C D />` :eq:`equal <data_01_taxonomy:/ A B / = data_01_taxonomy:/ C D />` to given :g:`AB <data_01_taxonomy:/ A B />`. Panel 2 illustrates **Species** (:just:`[Data Def. 3] <D.def.3>`), pairing homothetic triangles :g:`EFG <data_01_taxonomy:< E F G >>` and :g:`HKL <data_01_taxonomy:< H K L >>` with equal angles :g:`∠FEG <data_01_taxonomy:< F E G )>` and :g:`∠KHL <data_01_taxonomy:< K H L )>` and given side ratios (:math:`2:3`). Panel 3 illustrates **Position** (:just:`[Data Def. 4] <D.def.4>`, :just:`[Data Def. 6] <D.def.6>`), where fixed circle :g:`(O, OM) <data_01_taxonomy:( O M )>` with centre :g:`O <data_01_taxonomy:O>` and radius :g:`OM <data_01_taxonomy:/ O M />` meets fixed straight line :g:`PQ <data_01_taxonomy:/ P Q />` at uniquely determined points :g:`M <data_01_taxonomy:M>` and :g:`N <data_01_taxonomy:N>`.

Overview of the Fifteen Definitions (*Menge pp. 2–4*)
-----------------------------------------------------

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
     - :ref:`English <D.def.1>` · :ref:`Greek <D.def.1.el>`
   * - :ref:`D.def.2 <D.def.2>`
     - Def. II
     - Ratio (λόγῳ)
     - ``GivenRatio(A : B) := exists GivenMagnitude(C, D) with A : B = C : D``
     - :ref:`English <D.def.2>` · :ref:`Greek <D.def.2.el>`
   * - :ref:`D.def.3 <D.def.3>`
     - Def. III
     - Species (εἴδει)
     - ``GivenSpecies(P) := forall i,j: GivenAngle(ang_i(P)) and GivenRatio(s_i(P) : s_j(P))``
     - :ref:`English <D.def.3>` · :ref:`Greek <D.def.3.el>`
   * - :ref:`D.def.4 <D.def.4>`
     - Def. IV (cf. Def. A)
     - Position (θέσει)
     - ``GivenPosition(X) := X is invariant in the fixed planar reference frame (and constructible)``
     - :ref:`English <D.def.4>` · :ref:`Greek <D.def.4.el>`
   * - :ref:`D.def.5 <D.def.5>`
     - Def. V
     - Circle in Magnitude
     - ``GivenCircleMag(C) := GivenMagnitude(radius(C))``
     - :ref:`English <D.def.5>` · :ref:`Greek <D.def.5.el>`
   * - :ref:`D.def.6 <D.def.6>`
     - Def. VI
     - Circle in Position & Magnitude
     - ``GivenCirclePosMag(C) := GivenPosition(center(C)) and GivenMagnitude(radius(C))``
     - :ref:`English <D.def.6>` · :ref:`Greek <D.def.6.el>`
   * - :ref:`D.def.7 <D.def.7>`
     - Def. VII
     - Circular Segment in Magnitude
     - ``GivenSegmentMag(S) := GivenAngle(inscribed_angle(S)) and GivenMagnitude(base(S))``
     - :ref:`English <D.def.7>` · :ref:`Greek <D.def.7.el>`
   * - :ref:`D.def.8 <D.def.8>`
     - Def. VIII
     - Circular Segment in Position & Magnitude
     - ``GivenSegmentPosMag(S) := GivenAngle(inscribed_angle(S)) and GivenPosMag(base(S))``
     - :ref:`English <D.def.8>` · :ref:`Greek <D.def.8.el>`
   * - :ref:`D.def.9 <D.def.9>`
     - Def. IX
     - Affine Excess (δοθέντι μεῖζον)
     - ``ExceedsByGiven(A, B) := exists GivenMagnitude(D) with A - D = B``
     - :ref:`English <D.def.9>` · :ref:`Greek <D.def.9.el>`
   * - :ref:`D.def.10 <D.def.10>`
     - Def. X
     - Affine Defect (δοθέντι ἔλασσον)
     - ``LessByGiven(A, B) := exists GivenMagnitude(D) with A + D = B``
     - :ref:`English <D.def.10>` · :ref:`Greek <D.def.10.el>`
   * - :ref:`D.def.11 <D.def.11>`
     - Omitted (expanded verbally in Props. XIV–XXVII)
     - Affine-Ratio Excess (δοθέντι μεῖζον ἢ ἐν λόγῳ)
     - ``GreaterThanInRatio(A, B) := exists GivenMagnitude(D), GivenRatio(k) with (A - D) : B = k``
     - :ref:`English <D.def.11>` · :ref:`Greek <D.def.11.el>`
   * - :ref:`D.def.12 <D.def.12>`
     - Omitted (expanded verbally in Props. XIV–XXVII)
     - Affine-Ratio Defect (δοθέντι ἔλασσον ἢ ἐν λόγῳ)
     - ``LessThanInRatio(A, B) := exists GivenMagnitude(D), GivenRatio(k) with (A + D) : B = k``
     - :ref:`English <D.def.12>` · :ref:`Greek <D.def.12.el>`
   * - :ref:`D.def.13 <D.def.13>`
     - Omitted (late scholium; bracketed by Menge)
     - Directed Ordinate [Bracketed Scholium]
     - ``Kategmene(P, L, theta) := segment from GivenPoint(P) to GivenLine(L) at GivenAngle(theta)``
     - :ref:`English <D.def.13>` · :ref:`Greek <D.def.13.el>`
   * - :ref:`D.def.14 <D.def.14>`
     - Omitted (late scholium; bracketed by Menge)
     - Erected Line [Bracketed Scholium]
     - ``Anegmene(P, L, theta) := ray from GivenPoint(P) on GivenLine(L) at GivenAngle(theta)``
     - :ref:`English <D.def.14>` · :ref:`Greek <D.def.14.el>`
   * - :ref:`D.def.15 <D.def.15>`
     - Omitted (late scholium; bracketed by Menge)
     - Parallel to Position [Bracketed Scholium]
     - ``ParaThesei(P, L) := line through GivenPoint(P) parallel to GivenLine(L)``
     - :ref:`English <D.def.15>` · :ref:`Greek <D.def.15.el>`

2. Simson's Regular-Heptagon Critique of Definition 4 (*Position*)
------------------------------------------------------------------

:just:`[Data Def. 4] <D.def.4>` defines points, lines, and angles as :term:`given in position <thesei>` when they *"always occupy the same place"* (*ἃ τὸν αὐτὸν ἀεὶ τόπον ἐπέχει*). In his critical note on Def. IV (:cite:`p. 455 <simson:1762>`), :person:`Simson <simson>` observed that Euclid's wording captures :person:`Apollonius's <apollonius>` :term:`τεταγμένον <tetagmenon>` (*uniquely determined in nature*) while omitting :term:`πόριμον <porimon>` (*constructible by elementary means*): if :math:`\triangle ABC` is given in position, a ray :math:`BD` cutting off :math:`\angle DBC = \frac{1}{7} \angle ABC` occupies an invariant, unique place, yet **cannot be constructed by straightedge and compass** (since angle septisection / the regular heptagon requires a cubic *neusis* or conic intersection, outside the quadratic closure of the *Elements*). Simson therefore appended *"and which are either actually exhibited, or can be found"*—confirming in detail :person:`Marinus's <marinus>` diagnosis in :ref:`§ 15 <marinus-p15>` that *givenness* requires **procurability** (*πόριμον*), not mere uniqueness (*τεταγμένον*).

3. Affine-Ratio Idiom in Definitions 11–12 (*Δοθέντι μεῖζον ἢ ἐν λόγῳ*)
-----------------------------------------------------------------------

:just:`[Data Def. 11] <D.def.11>` and :just:`[Data Def. 12] <D.def.12>` introduce Euclid's remarkably compact Greek idiom :term:`δοθέντι μεῖζον ἢ ἐν λόγῳ <dothenti-meizon-e-en-logo>` (*"greater [or less] by a given magnitude than in ratio"*):

.. math::

   (A - D) : B = k \iff A = k \cdot B + D, \qquad (A + D) : B = k \iff A = k \cdot B - D,

where offset :math:`D` is given in magnitude and slope :math:`k` is given in ratio. This turns 1D **affine-linear transformations** into a single syntactic predicate closed under composition (:ref:`D.19 <D.19>`) and Gaussian elimination (:ref:`D.17 <D.17>`–:ref:`D.18 <D.18>`). :person:`Simson <simson>` (:cite:`p. 456 <simson:1762>`) omitted Defs. 11–12 only because literal English sounded obscure, expanding the phrase verbally as *"the excess of one magnitude above a given magnitude has a given ratio to the other"* across his Props. XIV–XXVII.

4. Manuscript Authority & Bracketing of Definitions 13–15
---------------------------------------------------------

In the ninth-century non-Theonine Vatican archetype :cite:`Vat. gr. 190 (Codex P) <vat-gr-190>` collated by :person:`Heinrich Menge <menge>` (:cite:`1896, p. 4 <menge:1896>`), Definitions 1–12 form the authentic Euclidean core, whereas :just:`[Data Def. 13] <D.def.13>` (:term:`κατηγμένη <kategmene>`), :just:`[Data Def. 14] <D.def.14>` (:term:`ἀνηγμένη <anegmene>`), and :just:`[Data Def. 15] <D.def.15>` (:term:`παρὰ θέσει <para-thesei>`) are enclosed in editorial brackets ``[...]`` as post-Euclidean scholia imported from Alexandrian locus and conic terminology (their terms never appear in the proofs of :ref:`D.28 <D.28>`–:ref:`D.30 <D.30>`, where Euclid writes out the full geometric descriptions). :person:`Simson <simson>` (:cite:`p. 456 <simson:1762>`) had already rejected all three on internal mathematical grounds.

Table of Definitions
--------------------

.. collection::
   :type: definition
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
