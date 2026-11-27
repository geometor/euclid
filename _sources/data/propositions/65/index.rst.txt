:order: 65
:canonical_id: D.65
:breadcrumb_title: D.65
:book: Data
:proposition: 65
:type: proposition
:title: Proposition 65 [ξε΄ · Prop. Prop. LXXV]
:folio: Menge 118
:page: 118
:excerpt: If an acute-angled triangle have one acute angle given, then that area by which the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle will have a given ratio to the triangle.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.65:

Proposition 65 [ξε΄ · Prop. LXXV]
---------------------------------

.. folio:: Menge 118
   :page: 118

.. enunciation::

   If an acute-angled triangle have one acute angle given, then that area by which the square on the side subtending the acute angle is less than the squares on the sides containing the acute angle will have a given ratio to the triangle.

*Functional Signature*: ``Given(AcuteAngle B) -> Determined(Ratio((a^2 + c^2 - b^2) : △ABC) = 4 cot B)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.13] <II.13>`, :just:`[VI.1] <VI.1>`

Let :math:`\\triangle ABC` have the acute angle :math:`\angle ABC` given, and from :math:`A` let :math:`AD` be drawn perpendicular to :math:`BC` (:just:`[I.12] <I.12>`). I say that the defect :math:`((AB^2 + BC^2) - AC^2)` by which :math:`AC^2` falls short of :math:`AB^2 + BC^2` has a given ratio to the rectangle :math:`AB \cdot BC`.

In right-angled :math:`\\triangle ABD`, the acute angle :math:`\angle ABD` (:math:`= \angle ABC`) is given and :math:`\angle ADB = 1\\text{ rt.}`, so :math:`\\triangle ABD` is given in species (:just:`[Data 40] <D.40>`). Hence the ratio :math:`AB : BD` is given (:just:`[Data Def. 3] <D.def.3>`). Multiplying both terms by :math:`BC` (:just:`[VI.1] <VI.1>`), the ratio :math:`(AB \cdot BC) : (CB \cdot BD)` is given, and hence :math:`(2\, CB \cdot BD) : (AB \cdot BC)` is given (:just:`[Data 8] <D.8>`). Yet by the acute-triangle Pythagorean identity (:just:`[II.13] <II.13>`), :math:`AC^2 + 2\, CB \cdot BD = AB^2 + BC^2`, so the defect :math:`(AB^2 + BC^2) - AC^2` equals :math:`2\, CB \cdot BD`. Therefore that defect has a given ratio (:math:`= 2\, BD : AB = 2\cos\angle ABC`) to :math:`AB \cdot BC`.
