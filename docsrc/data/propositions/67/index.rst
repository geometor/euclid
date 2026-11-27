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

Let :math:`\\triangle ABC` have a given angle :math:`\angle BAC`. I say that the excess :math:`((BA + AC)^2 - BC^2)` by which the square on the compound :math:`(BA + AC)` exceeds the square on :math:`BC` has a given ratio to the area of :math:`\\triangle ABC`.

Produce :math:`BA` to :math:`D` so that :math:`AD = AC` (:just:`[I.3] <I.3>`), making :math:`BD = BA + AC`; join :math:`DC`, and through :math:`B` draw :math:`BE` parallel to :math:`DC` meeting :math:`CA` produced at :math:`E` (:just:`[I.31] <I.31>`). Because :math:`AD = AC` and :math:`DC \parallel BE`, by parallels :math:`BA : AD = EA : AC` (:just:`[VI.2] <VI.2>`), whence :math:`EA = BA` and :math:`EC = BA + AC = BD`, while in :math:`\\triangle BDC` and :math:`\\triangle BCE` the secant-product and cosine relations (:just:`[II.6] <II.6>`, :just:`[Data 64] <D.64>`–:just:`[Data 65] <D.65>`) express :math:`(BA + AC)^2 - BC^2 = (AB^2 + AC^2 - BC^2) + 2\, AB \cdot AC` in a given ratio to the rectangle :math:`AB \cdot AC`. Yet since :math:`\angle BAC` is given, the rectangle :math:`AB \cdot AC` has a given ratio to :math:`\\triangle ABC` (:just:`[Data 66] <D.66>`). *Ex aequali*, the excess :math:`((BA + AC)^2 - BC^2)` has a given ratio (:math:`= 4\cot\frac{1}{2}\angle BAC`) to :math:`\\triangle ABC` (:just:`[Data 8] <D.8>`).
