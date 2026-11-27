:order: 66
:canonical_id: D.66
:breadcrumb_title: D.66
:book: Data
:proposition: 66
:type: proposition
:title: Proposition 66 [ξϛ΄ · Prop. Prop. LXII Cor.]
:folio: Menge 120
:page: 120
:excerpt: If a triangle have a given angle, the rectangle contained by the straight lines containing the given angle has a given ratio to the triangle.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.66:

Proposition 66 [ξϛ΄ · Prop. LXII Cor.]
--------------------------------------

.. folio:: Menge 120
   :page: 120

.. enunciation::

   If a triangle have a given angle, the rectangle contained by the straight lines containing the given angle has a given ratio to the triangle.

*Functional Signature*: ``Given(Angle A) -> Determined(Ratio((AB * AC) : Area(△ABC)) = 2 / sin A)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.1] <VI.1>`

Let :math:`\\triangle ABC` have a given angle :math:`\angle ABC`. I say that the rectangle :math:`AB \cdot BC` contained by the sides about the given angle has a given ratio to the area of :math:`\\triangle ABC`.

From :math:`A` drop :math:`AD` perpendicular to :math:`BC` (or :math:`BC` produced) (:just:`[I.12] <I.12>`). Because :math:`\angle ABC` is given, :math:`\angle ABD` is given (either directly if acute, or as :math:`2\\text{ rt.} - \angle ABC` if obtuse by :just:`[Data 4] <D.4>`; if :math:`\angle ABC` is right, :math:`AD = AB` immediately). Hence right-angled :math:`\\triangle ABD` is given in species (:just:`[Data 40] <D.40>`), so the ratio :math:`AB : AD` is given (:just:`[Data Def. 3] <D.def.3>`). Multiplying both terms by :math:`BC` (:just:`[VI.1] <VI.1>`), :math:`(AB \cdot BC) : (AD \cdot BC)` is given. Yet the rectangle :math:`AD \cdot BC` is double the area of :math:`\\triangle ABC` (:just:`[I.41] <I.41>`), so :math:`(AD \cdot BC) : \\triangle ABC = 2 : 1` is given. *Ex aequali*, the ratio :math:`(AB \cdot BC) : \\triangle ABC` (:math:`= 2/\sin\angle ABC`) is given (:just:`[Data 8] <D.8>`).
