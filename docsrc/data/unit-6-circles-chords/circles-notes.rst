:order: 63
:type: notes
:canonical_id: D.unit.6
:folio: Menge pp. 164–186
:book: Propositions 84–94: Circles, Chords & Angle Bisectors

.. _data-unit-6-notes:

===========================================================================================================================
Unit 6: Hyperbolic/Elliptic Systems, Circles, Chords & Angle Bisectors (Propositions 84–94) — Philological & Critical Notes
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
