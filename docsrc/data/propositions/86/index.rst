:order: 86
:canonical_id: D.86
:breadcrumb_title: D.86
:book: Data
:proposition: 86
:type: proposition
:title: Proposition 86 [πϛ΄ · Prop. Prop. LXXXIX (cf. LXXXVII–LXXXVIII)]
:folio: Menge 168
:page: 168
:excerpt: If two straight lines contain a given area in a given angle, and the square on one be greater than the square on the other by a given area than in ratio, each of them will also be given.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.86:

Proposition 86 [πϛ΄ · Prop. LXXXIX (cf. LXXXVII–LXXXVIII)]
----------------------------------------------------------

.. folio:: Menge 168
   :page: 168

.. enunciation::

   If two straight lines contain a given area in a given angle, and the square on one be greater than the square on the other by a given area than in ratio, each of them will also be given.

*Functional Signature*: ``Given(Angle B, x*y*sin B = S, (y^2 - D) : x^2 = k) -> Determined(Mag(x), Mag(y))`` · *Dependencies*: :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 55] <D.55>`, :just:`[Data 57] <D.57>`, :just:`[Data 58] <D.58>`, :just:`[Data 59] <D.59>`, :just:`[Data 68] <D.68>`, :just:`[II.4] <II.4>`, :just:`[II.6] <II.6>`, :just:`[VI.1] <VI.1>`, :just:`[VI.17] <VI.17>`, :just:`[VI.20] <VI.20>`

Let two straight lines :math:`AB` and :math:`BC` contain a given area :math:`AB \cdot BC` in a given angle :math:`\angle ABC`, and let the square :math:`BC^2` be :term:`greater by a given area than in ratio <dothenti-meizon-e-en-logo>` to the square :math:`AB^2`. I say that each of :math:`AB` and :math:`BC` is given in magnitude.

Since :math:`BC^2` is greater by a given area than in ratio to :math:`AB^2`, subtract the given area—expressed as a rectangle :math:`BC \cdot BD` applied to :math:`BC` (:just:`[I.44] <I.44>`), so :math:`BC^2 - BC \cdot BD = BC \cdot DC` (:just:`[II.2] <II.2>`) has a given ratio to :math:`AB^2` (:just:`[Data Def. 11] <D.def.11>`). Moreover, since the parallelogram :math:`ABEC` in the given angle :math:`\angle ABC` is given in magnitude, the rectangle :math:`AB \cdot BC` also is given in magnitude (having a given ratio to :math:`ABEC` by :just:`[Data 66] <D.66>` and :just:`[Data 2] <D.2>`), while :math:`BC \cdot BD` is given in magnitude! Therefore the ratio :math:`(BC \cdot BD) : (AB \cdot BC) = BD : AB` (:just:`[Data 1] <D.1>`, :just:`[VI.1] <VI.1>`) is given, whence :math:`BD^2 : AB^2` is given (:just:`[Data 50] <D.50>`). Combining :math:`(BC \cdot DC) : AB^2` with :math:`AB^2 : BD^2` gives :math:`(BC \cdot DC) : BD^2` given (:just:`[Data 8] <D.8>`), so :math:`4\,(BC \cdot DC) : BD^2` is given. Yet by :just:`[II.8] <II.8>` (taking :math:`E` with :math:`BE = BD`, or directly :math:`(BC + DC)^2 = (2\,BC - BD)^2 = 4\,BC \cdot DC + BD^2`!), adding :math:`BD^2` *componendo* (:just:`[Data 6] <D.6>`) gives :math:`(2\,BC - BD)^2 : BD^2` given! Extracting the square root via :just:`[Data 54] <D.54>` yields :math:`(2\,BC - BD) : BD` given, whence *componendo* :math:`2\,BC : BD` and :math:`BC : BD` are given (:just:`[Data 6] <D.6>`). Combining :math:`BC : BD` with :math:`BD : AB` gives :math:`BC : AB` given (:just:`[Data 8] <D.8>`). Thus the given parallelogram :math:`ABEC` has given angles and given side ratio :math:`BC : AB`, so :math:`ABEC` is given in species (:just:`[Data Def. 3] <D.def.3>`) as well as in magnitude; therefore :math:`AB` and :math:`BC` are given in magnitude (:just:`[Data 55] <D.55>`).

.. picture:: /_static/figures/data_06_circle_angle_locus.svg
   :alt: Circle Chords, Inscribed Angles, and Tangent-Secant Power (D.87–D.91)

Interactive circle-locus diagram (:cite:`Menge pp. 168–178 <menge:1896>`): In circle :g:`(O, OA) <data_06_circle_angle_locus:( O A )>` with centre :g:`O <data_06_circle_angle_locus:O>` and diameter :g:`CE <data_06_circle_angle_locus:/ C E />`, chord :g:`BC <data_06_circle_angle_locus:/ B C />` subtends given inscribed angle :g:`∠BAC <data_06_circle_angle_locus:< B A C )>` in :g:`△ABC <data_06_circle_angle_locus:< A B C >>`, calibrated via right-angled triangle on :g:`BE <data_06_circle_angle_locus:/ B E />` (:ref:`D.87 <D.87>`–:ref:`D.88 <D.88>`). From external given point :g:`P <data_06_circle_angle_locus:P>`, tangent :g:`PT <data_06_circle_angle_locus:/ P T />` (perpendicular to radius :g:`OT <data_06_circle_angle_locus:/ O T />` at :g:`T <data_06_circle_angle_locus:T>`, :ref:`D.90 <D.90>`) fixes the secant power along :g:`CP <data_06_circle_angle_locus:/ C P />` (:ref:`D.91 <D.91>`).
