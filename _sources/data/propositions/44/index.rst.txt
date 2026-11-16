:order: 44
:canonical_id: D.44
:breadcrumb_title: D.44
:book: Data
:proposition: 44
:type: proposition
:title: Proposition 44 [μδ΄ · Prop. Prop. XLVII]
:folio: Menge 78
:page: 78
:excerpt: If a triangle have one angle given, and the sides about another angle have a given ratio to one another, the triangle is given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.44:

Proposition 44 [μδ΄ · Prop. XLVII]
----------------------------------

.. folio:: Menge 78
   :page: 78

.. enunciation::

   If a triangle have one angle given, and the sides about another angle have a given ratio to one another, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Ratio(AB : BC), Sign(cos C)) -> Determined(Species(Triangle ABC)) [SSA diorismos]`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.13] <I.13>`, :just:`[VI.7] <VI.7>`

Let $\triangle ABC$ have one given angle $\angle ABC$, and let the sides $AB$ and $AC$ about another angle $\angle BAC$ have a given ratio $AB : AC$—*assuming the specification (diorismos) whether $\angle ACB$ is obtuse or acute is fixed*. I say that $\triangle ABC$ is given in species.

From $A$ drop $AD$ perpendicular to $BC$ (or $BC$ produced) (:just:`[I.12] <I.12>`). In right-angled $\triangle ABD$, $\angle ADB = 1\text{ rt.}$ and $\angle ABD$ (or its supplement) is given, so all angles of $\triangle ABD$ are given (:just:`[I.32] <I.32>`), whence $\triangle ABD$ is given in species (:just:`[Data 40] <D.40>`). Therefore the ratio $BA : AD$ is given (:just:`[Data Def. 3] <D.def.3>`). Yet the ratio $CA : AB$ is given by hypothesis; *ex aequali*, the ratio $CA : AD$ is given (:just:`[Data 8] <D.8>`). Now $\triangle ADC$ is right-angled at $D$ with the ratio of hypotenuse $CA$ to leg $AD$ given; hence $\triangle ADC$ is given in species (:just:`[Data 43] <D.43>`), so the acute angle $\angle ACD$ is given! Depending on the single branch specified (whether $D$ falls on $BC$ with $\angle ACB$ acute, or on $BC$ produced with $\angle ACB = 2\text{ rt.} - \angle ACD$ obtuse), $\angle ACB$ is uniquely given. Together with given $\angle ABC$, all angles of $\triangle ABC$ are given (:just:`[I.32] <I.32>`), so $\triangle ABC$ is given in species (:just:`[Data 40] <D.40>`).
