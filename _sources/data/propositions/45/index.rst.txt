:order: 45
:canonical_id: D.45
:breadcrumb_title: D.45
:book: Data
:proposition: 45
:type: proposition
:title: Proposition 45 [με΄ · Prop. Prop. XLVIII]
:folio: Menge 82
:page: 82
:excerpt: If a triangle have one angle given, and both the sides together about the given angle have a given ratio to the remaining side, the triangle is given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.45:

Proposition 45 [με΄ · Prop. XLVIII]
-----------------------------------

.. folio:: Menge 82
   :page: 82

.. enunciation::

   If a triangle have one angle given, and both the sides together about the given angle have a given ratio to the remaining side, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Ratio((b + c) : a)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data 40] <D.40>`, :just:`[Data 44] <D.44>`, :just:`[I.5] <I.5>`, :just:`[I.32] <I.32>`

Let $\triangle ABC$ have one given angle $\angle BAC$, and let the compound $(BA + AC)$ of the two sides about the given angle have a given ratio to the remaining side $BC$. I say that $\triangle ABC$ is given in species.

Bisect $\angle BAC$ by the straight line $AD$ meeting $BC$ at $D$ (:just:`[I.9] <I.9>`). Since $\angle BAC$ is given, its half $\angle BAD$ is given (:just:`[Data 7] <D.7>`). Because $AD$ bisects $\angle BAC$, $BA : AC = BD : DC$ (:just:`[VI.3] <VI.3>`). *Alternando* $BA : BD = AC : DC$ (:just:`[V.16] <V.16>`), and *componendo* $(BA + AC) : BC = BA : BD$ (:just:`[V.12] <V.12>`). Since $(BA + AC) : BC$ is given by hypothesis, the ratio $BA : BD$ is given. Applying :just:`[Data 44] <D.44>` to $\triangle ABD$ (with given angle $\angle BAD$ and given ratio $BA : BD$, up to the symmetric interchange of $AB$ and $AC$) determines $\triangle ABD$ in species, whence $\angle ABD$ is given; together with given $\angle BAC$, $\triangle ABC$ is given in species (:just:`[Data 40] <D.40>`).
