:order: 33
:type: notes
:canonical_id: D.unit.3
:folio: Menge pp. 66–98
:book: Propositions 39–55: Triangles & Species

.. _data-unit-3-notes:

==================================================================================================
Unit 3: Triangles & Polygons Given in Species (Propositions 39–55) — Philological & Critical Notes
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
