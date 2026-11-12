:order: 43
:type: notes
:canonical_id: D.unit.4
:folio: Menge pp. 98–126
:book: Propositions 56–67: Areas, Quadratics & Cosines

.. _data-unit-4-notes:

==================================================================================================================
Unit 4: Application of Areas, Quadratics & Cosine Projections (Propositions 56–67) — Philological & Critical Notes
==================================================================================================================

1. Geometric Algebra of Application of Areas: Parabolē, Elleipsis, and Hyperbolē (D.57–D.60)
--------------------------------------------------------------------------------------------

Unit 4 (:ref:`D.56 <D.56>`–:ref:`D.67 <D.67>`) translates the constructive **application of areas** (*παραβολὴ τῶν χωρίων*, :cite:`Elements II.5–6 & VI.27–29 <heath:1926>`) into analytical root-determination theorems:

* **Parabolē** (:term:`παραβολή <parabole>`, :ref:`D.57 <D.57>`): Exact application $a \cdot x = S$ in a given angle $\\theta$ solves the linear equation $x = S / (a \sin\\theta)$.

* **Elleipsis** (:term:`ἔλλειψις <elleipsis>`, :ref:`D.58 <D.58>`): Elliptic application $(a - x)\cdot (\lambda x) = S$ solves the quadratic equation $\lambda x^2 - \lambda a x + S = 0$ by completing the gnomon on the half-segment $a/2$ (:just:`[II.5] <II.5>`, :just:`[VI.28] <VI.28>`), subject to the discriminant *diorismos* $S \le \lambda (a/2)^2$ (:just:`[VI.27] <VI.27>`).

* **Hyperbolē** (:term:`ὑπερβολή <hyperbole>`, :ref:`D.59 <D.59>`): Hyperbolic application $(a + x)\cdot (\lambda x) = S$ solves $\lambda x^2 + \lambda a x = S$ unconditionally via :just:`[II.6] <II.6>` and :just:`[VI.29] <VI.29>`. When $S = a^2$ and the excess is a square ($\lambda = 1$), $x(a + x) = a^2$ determines the **golden section** $x = a/\phi \in \mathbb{Q}(\phi)$ (:just:`[II.11] <II.11>`, :just:`[VI.30] <VI.30>`)!

As :person:`Proclus <proclus>` (:cite:`In Eucl. 419.15 <proclus:1873>`) and :person:`Pappus <pappus>` record, :person:`Apollonius of Perga <apollonius>` borrowed the very names *parabola*, *ellipse*, and *hyperbola* directly from this Pythagorean-Euclidean triad.

2. Area-to-Species Bridges (D.61–D.63) & Textual Notes
------------------------------------------------------

Propositions :ref:`D.61 <D.61>` and :ref:`D.62 <D.62>` bridge area-ratios back to species: if a parallelogram $CD$ in a given angle is applied either to a side of a species-given figure (:ref:`D.61 <D.61>`) or to a segment having a given ratio to a side of a species-given figure (:ref:`D.62 <D.62>`), and the area ratio is given, then $CD$ itself is given in species. :person:`Simson <simson>` (:cite:`Props. LXIX–LXX, p. 464 <simson:1762>`) retained both (`D.61–62`) while omitting :ref:`D.63 <D.63>` (*species-given figures on the three sides of a species-given triangle have given ratios to one another*) as an immediate corollary of :ref:`D.51 <D.51>`; :person:`Menge <menge>` preserved :ref:`D.63 <D.63>` from :cite:`Vat. gr. 190 <vat-gr-190>`.

3. The Euclidean Law of Cosines, Sine Area Formula & Half-Angle Excess (D.64–D.67)
----------------------------------------------------------------------------------

Propositions :ref:`D.64 <D.64>`–:ref:`D.67 <D.67>` form the trigonometric heart of Greek plane geometry (visualized in ``data_05_cosine_projection.svg``):

* **Obtuse & Acute Cosine Laws** (:ref:`D.64 <D.64>`–:ref:`D.65 <D.65>`): By combining :just:`[Elements II.12] <II.12>` and :just:`[II.13] <II.13>` with species-given right-triangle projections (:ref:`D.40 <D.40>`), Euclid proves that $|a^2 + c^2 - b^2| : (a c) = 2\, BD : AB = 2|\cos B|$ is **given** whenever $\angle B$ is given—without ever needing symbolic trigonometric tables!

* **Sine Area Law** (:ref:`D.66 <D.66>`): Proves $(AB \cdot BC) : \\triangle ABC = 2/\sin B$ is given whenever $\angle B$ is given.

* **Compound-Side Quadratic Excess** (:ref:`D.67 <D.67>`, `Simson Prop. LXXVI`): Proves $((b + c)^2 - a^2) : \\triangle ABC$ is given whenever $\angle A$ is given. Algebraically, $(b+c)^2 - a^2 = 2bc(1 + \cos A)$ while $\\triangle ABC = \frac{1}{2}bc\sin A$, so their constant ratio is $4(1+\cos A)/\sin A = 4\cot(A/2)$! In :cite:`Vat. gr. 190 <vat-gr-190>` (:cite:`Menge pp. 122–126 <menge:1896>`), Euclid establishes this synthetically without trigonometry by extending $BA$ to $D$ with $AD = AC$ and applying :just:`[II.6] <II.6>`.

Cross-Corpus Concordance (Pappus · Petersen · Altshiller-Court · G-Index)
-------------------------------------------------------------------------

* :ref:`D.56 <D.56>` (Prop. LXIII) — *Elements G-Index*: ``G.210, G.225`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Application of Areas
* :ref:`D.57 <D.57>` (Prop. LXI) — *Elements G-Index*: ``G.58, G.75, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Parabolic Application of Areas · *Altshiller-Court (1952)*: § 47 (Transformation of Areas)
* :ref:`D.58 <D.58>` (Prop. LXXXIII) — *Elements G-Index*: ``G.87, G.236, G.239, G.240`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Elliptic Application of Areas (Quadratic) · *Altshiller-Court (1952)*: § 50 (Elliptic Application)
* :ref:`D.59 <D.59>` (Prop. LXXXIV) — *Elements G-Index*: ``G.88, G.236, G.241`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Hyperbolic Application of Areas (Quadratic) · *Altshiller-Court (1952)*: § 51 (Hyperbolic Application / Golden Section)
* :ref:`D.60 <D.60>` (Prop. LXXXII) — *Elements G-Index*: ``G.236`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Gnomonic Scaling
* :ref:`D.61 <D.61>` (Prop. LXIX) — *Elements G-Index*: ``G.37, G.56, G.58, G.64, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Area-to-Aspect Conversion
* :ref:`D.62 <D.62>` (Prop. LXX) — *Elements G-Index*: ``G.229, G.232`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Area-to-Aspect Conversion
* :ref:`D.63 <D.63>` (Omitted (case of Prop. LIII)) — *Elements G-Index*: ``G.75`` · *Pappus*: Synagoge VII.8
* :ref:`D.64 <D.64>` (Prop. LXXIV) — *Elements G-Index*: ``G.35, G.59, G.94, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Cosine Projection Law
* :ref:`D.65 <D.65>` (Prop. LXXV) — *Elements G-Index*: ``G.35, G.59, G.95, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Cosine Projection Law
* :ref:`D.66 <D.66>` (Prop. LXII Cor.) — *Elements G-Index*: ``G.35, G.70, G.210`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Trigonometric Area Formula
* :ref:`D.67 <D.67>` (Prop. LXXVI) — *Elements G-Index*: ``G.25, G.37, G.58, G.59, G.88, G.211, G.227`` · *Pappus*: Synagoge VII.8 · *Petersen (1879)*: Isosceles Auxiliary Extension + Secant-Product
