:order: 80
:canonical_id: D.80
:breadcrumb_title: D.80
:book: Data
:proposition: 80
:type: proposition
:title: Proposition 80 [π΄ · Prop. Prop. LXXVIII]
:folio: Menge 154
:page: 154
:excerpt: If a triangle have one angle given, and the rectangle contained by the sides about the given angle have a given ratio to the square on the remaining side, the triangle is given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.80:

Proposition 80 [π΄ · Prop. LXXVIII]
-----------------------------------

.. folio:: Menge 154
   :page: 154

.. enunciation::

   If a triangle have one angle given, and the rectangle contained by the sides about the given angle have a given ratio to the square on the remaining side, the triangle is given in species.

*Functional Signature*: ``Given(Angle A, Ratio((b*c) : a^2)) -> Determined(Species(△ABC))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 66] <D.66>`, :just:`[Data 68] <D.68>`, :just:`[Data 79] <D.79>`, :just:`[I.12] <I.12>`, :just:`[I.41] <I.41>`, :just:`[VI.4] <VI.4>`, :just:`[VI.16] <VI.16>`

Let :math:`\\triangle ABC` have a given angle :math:`\angle BAC`, and let the rectangle :math:`BA \cdot AC` contained by the sides about the given angle have a given ratio to the square :math:`BC^2` on the remaining side. I say that :math:`\\triangle ABC` is given in species.

Drop the altitude :math:`AD \perp BC` (:just:`[I.12] <I.12>`). Because :math:`\\triangle ABC` has given angle :math:`\angle BAC`, the ratio :math:`(BA \cdot AC) : \\triangle ABC` is given (:just:`[Data 66] <D.66>`). Combining this with the given ratio :math:`(BA \cdot AC) : BC^2` yields :math:`BC^2 : \\triangle ABC` given (:just:`[Data 8] <D.8>`), and since :math:`BC \cdot AD = 2\,\\triangle ABC` (:just:`[I.41] <I.41>`), the ratio :math:`BC^2 : (BC \cdot AD) = BC : AD` is given (:just:`[VI.1] <VI.1>`). Now set out a straight line :math:`FG` given in position and magnitude, and on :math:`FG` describe the circular segment :math:`FHG` admitting an angle equal to given :math:`\angle BAC` (:just:`[III.33] <III.33>`), whose arc is given in position. Take :math:`L` so that :math:`FG : L = BC : AD` (:just:`[Data 2] <D.2>`), erect :math:`FK = L` perpendicular to :math:`FG`, and draw :math:`KH \parallel FG` meeting the arc :math:`FHG` at :math:`H` (:just:`[Data 28] <D.28>`, :just:`[Data 25] <D.25>`). Joining :math:`FH` and :math:`HG` gives :math:`\\triangle FHG` in species (:just:`[Data 39] <D.39>`) with :math:`\angle FHG = \angle BAC` and base-to-altitude ratio :math:`FG : L = BC : AD`. By :just:`[Data 79] <D.79>`, :math:`\\triangle ABC` is equiangular with :math:`\\triangle FHG`, and therefore :math:`\\triangle ABC` is given in species (:just:`[Data 40] <D.40>`).
