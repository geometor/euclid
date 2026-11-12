:order: 13
:type: notes
:canonical_id: D.unit.1
:folio: Menge pp. 4–42
:book: Propositions 1–24: Magnitudes & Ratios

.. _data-unit-1-notes:

===============================================================================
Unit 1: Magnitudes & Ratios (Propositions 1–24) — Philological & Critical Notes
===============================================================================

1. Inhomogeneous Magnitudes & Simson's Diorismos on D.2, D.7, and D.8
---------------------------------------------------------------------

Unit 1 (:ref:`D.1 <D.1>`–:ref:`D.24 <D.24>`) operates at the universal level of :cite:`Elements Book V <heath:1926>` magnitudes (*μεγέθη*): lines, plane areas, solids, and angles. In his critical notes on :ref:`D.2 <D.2>` (:cite:`pp. 456–457 <simson:1762>`), :person:`Robert Simson <simson>` pointed out a subtle foundational boundary that :person:`Euclid <euclid>` leaves tacit: in the *Elements*, constructing a fourth proportional $C : D = A : B$ is proved constructively only for **straight lines** (:just:`[VI.12] <VI.12>`), not directly for arbitrary solids or inhomogeneous magnitudes.

Simson observed that whenever a given ratio between two homogeneous magnitudes can be exhibited as the ratio of two *given straight lines* $L_1 : L_2$ (as is always the case for constructible plane and solid problems in geometry), :just:`[VI.12] <VI.12>` supplies the required fourth proportional rigorously. Similarly, in :ref:`D.8 <D.8>` (*magnitudes having given ratios to the same magnitude have a given ratio to one another*), $A$ and $C$ must be **homogeneous** with one another (both lines, or both areas, etc.) in order to stand in a Eudoxian ratio (:just:`[V.def.3] <V.def.3>`).

2. The Affine-Linear Calculus (Defs. 11–12 & D.10–D.21) and Simson's Additions
------------------------------------------------------------------------------

Propositions :ref:`D.10 <D.10>`–:ref:`D.21 <D.21>` constitute an extraordinary piece of Greek **symbolic compression**. By packaging the two-parameter affine relation $y = k x + c$ ($c > 0$ given in magnitude, $k > 0$ given in ratio) into the single predicate :term:`δοθέντι μεῖζον ἢ ἐν λόγῳ <dothenti-meizon-e-en-logo>` (:just:`[Data Def. 11] <D.def.11>`) and $y = k x - c$ into :just:`[Data Def. 12] <D.def.12>`, Euclid proves that affine functions of an unknown magnitude form a **closed algebraic groupoid**:

* **Additive & Subtractive Shifts** (:ref:`D.10 <D.10>`–:ref:`D.11 <D.11>`): Notice that in :person:`Heinrich Menge's <menge>` non-Theonine text (:cite:`1896, pp. 16–22 <menge:1896>`), both :ref:`D.10 <D.10>` and :ref:`D.11 <D.11>` contain **two parts**—a direct theorem and its converse! In the converse of :ref:`D.10 <D.10>`, subtracting the given offset $c$ from $x + y = c + k y$ splits into two cases according as $c < x$ (leaving $x = c + (k-1)y$) or $c > x$ (producing $x + (c - x) = c$ where $y : (c - x)$ is given, i.e., $x = c - k' y$). Because Euclid in `Vat. gr. 190` avoided phrasing the second branch via Def. 12 directly, :person:`Simson <simson>` (:cite:`Props. XIV–XXIV <simson:1762>`) split and expanded the entire suite symmetrically across all sign combinations (`Props. XIV–XV` and `Props. XXI–XXII`).

* **Composition & Elimination** (:ref:`D.13 <D.13>`, :ref:`D.17 <D.17>`–:ref:`D.19 <D.19>`): :ref:`D.19 <D.19>` proves closure under composition ($A = k_1 B + c_1$ and $B = k_2 C + c_2 \implies A = (k_1 k_2) C + (c_1 + k_1 c_2)$), while :ref:`D.17 <D.17>` and :ref:`D.18 <D.18>` eliminate a shared variable between two affine equations.

* **The Doublet D.21**: As :person:`Simson <simson>` noted (:cite:`p. 458 <simson:1762>`), :ref:`D.21 <D.21>` (*adding magnitudes in a given ratio to two given magnitudes*) is mathematically identical to the first part of :ref:`D.14 <D.14>` (*adding two given magnitudes to magnitudes in a given ratio*) with the roles of the summands swapped; Simson therefore omitted `D.21`, whereas Menge retained it on the manuscript authority of :cite:`Vat. gr. 190 <vat-gr-190>`.

3. Non-Singularity in D.23 (det != 0) & Simson's Critique of Newton on D.24
---------------------------------------------------------------------------

Two philological gems crown the close of Unit 1:

* **Determinant Non-Singularity in D.23**: In :ref:`D.23 <D.23>`, if whole $AB = AE + EB$ has a given ratio $r$ to whole $CD = CF + FD$, while $AE : CF = r_1$ and $EB : FD = r_2$ are given, the crucial Greek proviso **μὴ τοὺς αὐτοὺς δέ** (*\"yet not the same ratios\"*, $r_1 \neq r_2$) is the exact classical statement of **matrix non-singularity**! Algebraically, $(r_1 - r) CF + (r_2 - r) FD = 0$; if $r_1 = r_2 = r$, the two equations collapse into one ($0 = 0$) and $CF : FD$ is indeterminate (`ἄτακτον`), whereas $r_1 \neq r_2$ forces $CF : FD = (r - r_2) : (r_1 - r)$ uniquely. :person:`Bartolomeo Zamberti's <zamberti>` 1505 Latin translation omitted the negation *non*, rendering the theorem false until :person:`Claude Hardy <hardy>` (:cite:`1625 <hardy:1625>`) and :person:`David Gregory <gregory>` (:cite:`1703 <gregory:1703>`) restored the Greek condition.

* **Continued Proportion & Quadratic Root Extraction in D.24**: :ref:`D.24 <D.24>` proves that if $A : B = B : C$ and $A : C$ is given, then $A : B$ is given ($A/B = \sqrt{A/C}$). Notably, Unit 1 here steps from general magnitudes to **straight lines** (*εὐθεῖαι*) so that :just:`[VI.13] <VI.13>` can construct the geometric mean $E = \sqrt{D \cdot F}$. Late Byzantine manuscripts appended an alternative proof (*Ἄλλως*, relegated by Menge to the Appendix) that tried to dispense with squares, and :person:`Isaac Newton <newton>` cited a similar shortcut in :cite:`Principia Book I, Lemma XVII <newton:1713>`; :person:`Simson <simson>` (:cite:`pp. 459–460 <simson:1762>`) demonstrated that the scholiast's *Ἄλλως* tacitly begged the question, vindicating Euclid's authentic proof.

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.1 <D.1>` (Prop. I) — *Elements G-Index*: ``G.183, G.195`` · *Pappus*: Synagoge VII.3
* :ref:`D.2 <D.2>` (Prop. II) — *Elements G-Index*: ``G.189, G.187, G.222`` · *Pappus*: Synagoge VII.3 · *Petersen (1879)*: Similarity / Scaling · *Altshiller-Court (1952)*: § 18 (Fourth Proportional)
* :ref:`D.3 <D.3>` (Prop. III) — *Elements G-Index*: ``G.36`` · *Petersen (1879)*: Algebraic Method · *Altshiller-Court (1952)*: § 6 (Sum of Segments)
* :ref:`D.4 <D.4>` (Prop. IV) — *Elements G-Index*: ``G.19`` · *Petersen (1879)*: Algebraic Method · *Altshiller-Court (1952)*: § 6 (Difference of Segments)
* :ref:`D.5 <D.5>` (Prop. VI) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.4
* :ref:`D.6 <D.6>` (Prop. VII) — *Elements G-Index*: ``G.199, G.201`` · *Pappus*: Synagoge VII.4
* :ref:`D.7 <D.7>` (Prop. VIII) — *Elements G-Index*: ``G.220`` · *Pappus*: Synagoge VII.4 · *Petersen (1879)*: Similarity / Ratio Division · *Altshiller-Court (1952)*: § 19 (Internal Division)
* :ref:`D.8 <D.8>` (Prop. IX) — *Elements G-Index*: ``G.183, G.189, G.205`` · *Pappus*: Synagoge VII.4
* :ref:`D.9 <D.9>` (Prop. X) — *Elements G-Index*: ``G.189, G.205`` · *Pappus*: Synagoge VII.4
* :ref:`D.10 <D.10>` (Prop. XVI) — *Elements G-Index*: ``G.199, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.11 <D.11>` (Prop. XVII) — *Elements G-Index*: ``G.190, G.195, G.199, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.12 <D.12>` (Prop. V) — *Elements G-Index*: ``G.19`` · *Petersen (1879)*: Algebraic Method
* :ref:`D.13 <D.13>` (Prop. XXIV) — *Elements G-Index*: ``G.189, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.14 <D.14>` (Prop. XVIII) — *Elements G-Index*: ``G.190, G.199`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.15 <D.15>` (Prop. XIX) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.16 <D.16>` (Prop. XX) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.17 <D.17>` (Prop. XXV) — *Elements G-Index*: ``G.189`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.18 <D.18>` (Prop. XXVI) — *Elements G-Index*: ``G.189`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.19 <D.19>` (Prop. XXVII) — *Elements G-Index*: ``G.189`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.20 <D.20>` (Prop. XXIII) — *Elements G-Index*: ``G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.21 <D.21>` (Omitted (cf. Prop. XVIII)) — *Elements G-Index*: ``G.199`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.22 <D.22>` (Prop. XI) — *Elements G-Index*: ``G.207`` · *Pappus*: Synagoge VII.4
* :ref:`D.23 <D.23>` (Prop. XII) — *Elements G-Index*: ``G.189, G.195, G.201`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Algebraic Method
* :ref:`D.24 <D.24>` (Prop. XIII) — *Elements G-Index*: ``G.223, G.228, G.234`` · *Pappus*: Synagoge VII.5 · *Petersen (1879)*: Mean Proportional · *Altshiller-Court (1952)*: § 21 (Mean Proportional)
