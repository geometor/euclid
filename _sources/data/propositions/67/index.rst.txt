:order: 67
:canonical_id: D.67
:breadcrumb_title: D.67
:book: Data
:proposition: 67
:type: proposition
:title: Proposition 67 [ξζ΄ · Prop. Prop. LXXVI]
:folio: Menge 120
:page: 120
:excerpt: If a triangle have a given angle, then that area by which the square on both the sides containing the given angle taken together as one exceeds the square on the remaining side will have a given ratio to the triangle.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.67:

Proposition 67 [ξζ΄ · Prop. LXXVI]
----------------------------------

.. enunciation::

   If a triangle have a given angle, then that area by which the square on both the sides containing the given angle taken together as one exceeds the square on the remaining side will have a given ratio to the triangle.

*Functional Signature*: ``Given(Angle A) -> Determined(Ratio(((b + c)^2 - a^2) : △ABC) = 4*(1 + cos A) / sin A)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 50] <D.50>`, :just:`[Data 66] <D.66>`, :just:`[I.5] <I.5>`, :just:`[I.13] <I.13>`, :just:`[I.31] <I.31>`, :just:`[I.32] <I.32>`, :just:`[II.6] <II.6>`, :just:`[VI.2] <VI.2>`, :just:`[VI.16] <VI.16>`

Let $\\triangle ABC$ have a given angle $\angle BAC$. I say that the excess $((BA + AC)^2 - BC^2)$ by which the square on the compound $(BA + AC)$ exceeds the square on $BC$ has a given ratio to the area of $\\triangle ABC$.

Produce $BA$ to $D$ so that $AD = AC$ (:just:`[I.3] <I.3>`), making $BD = BA + AC$; join $DC$, and through $B$ draw $BE$ parallel to $DC$ meeting $CA$ produced at $E$ (:just:`[I.31] <I.31>`). Because $AD = AC$ and $DC \parallel BE$, by parallels $BA : AD = EA : AC$ (:just:`[VI.2] <VI.2>`), whence $EA = BA$ and $EC = BA + AC = BD$, while in $\\triangle BDC$ and $\\triangle BCE$ the secant-product and cosine relations (:just:`[II.6] <II.6>`, :just:`[Data 64] <D.64>`–:just:`[Data 65] <D.65>`) express $(BA + AC)^2 - BC^2 = (AB^2 + AC^2 - BC^2) + 2\, AB \cdot AC$ in a given ratio to the rectangle $AB \cdot AC$. Yet since $\angle BAC$ is given, the rectangle $AB \cdot AC$ has a given ratio to $\\triangle ABC$ (:just:`[Data 66] <D.66>`). *Ex aequali*, the excess $((BA + AC)^2 - BC^2)$ has a given ratio ($= 4\cot\frac{1}{2}\angle BAC$) to $\\triangle ABC$ (:just:`[Data 8] <D.8>`).
