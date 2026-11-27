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

Let :math:`\triangle ABC` have one given angle :math:`\angle BAC`, and let the compound :math:`(BA + AC)` of the two sides about the given angle have a given ratio to the remaining side :math:`BC`. I say that :math:`\triangle ABC` is given in species.

Bisect :math:`\angle BAC` by the straight line :math:`AD` meeting :math:`BC` at :math:`D` (:just:`[I.9] <I.9>`). Since :math:`\angle BAC` is given, its half :math:`\angle BAD` is given (:just:`[Data 7] <D.7>`). Because :math:`AD` bisects :math:`\angle BAC`, :math:`BA : AC = BD : DC` (:just:`[VI.3] <VI.3>`). *Alternando* :math:`BA : BD = AC : DC` (:just:`[V.16] <V.16>`), and *componendo* :math:`(BA + AC) : BC = BA : BD` (:just:`[V.12] <V.12>`). Since :math:`(BA + AC) : BC` is given by hypothesis, the ratio :math:`BA : BD` is given. Applying :just:`[Data 44] <D.44>` to :math:`\triangle ABD` (with given angle :math:`\angle BAD` and given ratio :math:`BA : BD`, up to the symmetric interchange of :math:`AB` and :math:`AC`) determines :math:`\triangle ABD` in species, whence :math:`\angle ABD` is given; together with given :math:`\angle BAC`, :math:`\triangle ABC` is given in species (:just:`[Data 40] <D.40>`).
