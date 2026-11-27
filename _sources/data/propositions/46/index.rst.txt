:order: 46
:canonical_id: D.46
:breadcrumb_title: D.46
:book: Data
:proposition: 46
:type: proposition
:title: Proposition 46 [μϛ΄ · Prop. Prop. XLIX]
:folio: Menge 84
:page: 84
:excerpt: If a triangle have one angle given, and the sides together about another angle have a given ratio to the remaining side, the triangle is given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.46:

Proposition 46 [μϛ΄ · Prop. XLIX]
---------------------------------

.. folio:: Menge 84
   :page: 84

.. enunciation::

   If a triangle have one angle given, and the sides together about another angle have a given ratio to the remaining side, the triangle is given in species.

*Functional Signature*: ``Given(Angle(B), Ratio((c + b) : a)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data 40] <D.40>`, :just:`[Data 41] <D.41>`, :just:`[I.5] <I.5>`, :just:`[I.9] <I.9>`, :just:`[I.32] <I.32>`

Let :math:`\triangle ABC` have one given angle :math:`\angle ABC`, and let the compound :math:`(BA + AC)` of the sides about another angle :math:`\angle BAC` have a given ratio to the remaining side :math:`BC`. I say that :math:`\triangle ABC` is given in species.

Bisect :math:`\angle BAC` by :math:`AD` meeting :math:`BC` at :math:`D` (:just:`[I.9] <I.9>`). Since :math:`BA : AC = BD : DC` (:just:`[VI.3] <VI.3>`), *alternando* and *componendo* :math:`(BA + AC) : BC = AB : BD` (:just:`[V.16] <V.16>`, :just:`[V.12] <V.12>`). Because :math:`(BA + AC) : BC` is given, the ratio :math:`AB : BD` is given. Now in :math:`\triangle ABD`, the given angle :math:`\angle ABD` (:math:`= \angle ABC`) is itself the included angle between :math:`AB` and :math:`BD`; therefore :math:`\triangle ABD` is uniquely given in species (:just:`[Data 41] <D.41>`). Hence :math:`\angle BAD` is given, its double :math:`\angle BAC` is given (:just:`[Data 3] <D.3>`), and from given :math:`\angle ABC` and :math:`\angle BAC` the triangle :math:`\triangle ABC` is given in species (:just:`[Data 40] <D.40>`).
