:order: 64
:canonical_id: D.64
:breadcrumb_title: D.64
:book: Data
:proposition: 64
:type: proposition
:title: Proposition 64 [ξδ΄ · Prop. Prop. LXXIV]
:folio: Menge 114
:page: 114
:excerpt: If an obtuse-angled triangle have the obtuse angle given, then that area by which the square on the side subtending the obtuse angle exceeds the squares on the sides containing the obtuse angle will have a given ratio to the triangle.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. picture:: /_static/figures/data_05_cosine_projection.svg
   :alt: Obtuse (D.64) and Acute (D.65) Altitude Projections & Euclidean Law of Cosines

Interactive cosine-projection diagram (:cite:`Menge pp. 116–122 <menge:1896>`): Left panel (:ref:`D.64 <D.64>`, obtuse :g:`∠CBA <data_05_cosine_projection:< C B A )>`) drops exterior altitude :g:`AD <data_05_cosine_projection:/ A D />` onto :g:`BC <data_05_cosine_projection:/ B C />` produced at :g:`D <data_05_cosine_projection:D>` in :g:`△ABC <data_05_cosine_projection:< A B C >>`, making projection ratio :g:`DB <data_05_cosine_projection:/ D B />` to :g:`AB <data_05_cosine_projection:/ A B />` given and fixing the excess of :g:`AC <data_05_cosine_projection:/ A C />` squared (:just:`[II.12] <II.12>`). Right panel (:ref:`D.65 <D.65>`, acute :g:`∠GFE <data_05_cosine_projection:< G F E )>`) drops interior altitude :g:`EH <data_05_cosine_projection:/ E H />` onto :g:`FG <data_05_cosine_projection:/ F G />` at :g:`H <data_05_cosine_projection:H>` in :g:`△EFG <data_05_cosine_projection:< E F G >>`, making :g:`FH <data_05_cosine_projection:/ F H />` to :g:`EF <data_05_cosine_projection:/ E F />` given and fixing the defect of :g:`EG <data_05_cosine_projection:/ E G />` squared (:just:`[II.13] <II.13>`).

.. _D.64:

Proposition 64 [ξδ΄ · Prop. LXXIV]
----------------------------------

.. enunciation::

   If an obtuse-angled triangle have the obtuse angle given, then that area by which the square on the side subtending the obtuse angle exceeds the squares on the sides containing the obtuse angle will have a given ratio to the triangle.

*Functional Signature*: ``Given(ObtuseAngle B) -> Determined(Ratio((b^2 - a^2 - c^2) : △ABC) = -4 cot B)`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[I.32] <I.32>`, :just:`[II.12] <II.12>`, :just:`[VI.1] <VI.1>`

Let :math:`\\triangle ABC` have the obtuse angle :math:`\angle ABC` given, and from :math:`A` let :math:`AD` be drawn perpendicular to :math:`CB` produced at :math:`D` (:just:`[I.12] <I.12>`). I say that the excess :math:`(AC^2 - (AB^2 + BC^2))` by which :math:`AC^2` exceeds :math:`AB^2 + BC^2` has a given ratio to the rectangle :math:`AB \cdot BC`.

Since the obtuse angle :math:`\angle ABC` is given, its adjacent supplementary angle :math:`\angle ABD` is given (:just:`[I.13] <I.13>`, :just:`[Data 4] <D.4>`). In right-angled :math:`\\triangle ABD`, :math:`\angle ADB = 1\\text{ rt.}` and :math:`\angle ABD` is given, so :math:`\\triangle ABD` is given in species (:just:`[Data 40] <D.40>`). Therefore the projection ratio :math:`AB : BD` is given (:just:`[Data Def. 3] <D.def.3>`). Now under the common altitude :math:`BC`, as :math:`AB` is to :math:`BD`, so is the rectangle :math:`AB \cdot BC` to the rectangle :math:`CB \cdot BD` (:just:`[VI.1] <VI.1>`), whence :math:`(AB \cdot BC) : (CB \cdot BD)` is given, and doubling the consequent gives :math:`(AB \cdot BC) : (2\, CB \cdot BD)` given (:just:`[Data 8] <D.8>`). Yet because :math:`\angle ABC` is obtuse, by the obtuse-triangle Pythagorean identity (:just:`[II.12] <II.12>`), :math:`AC^2 = AB^2 + BC^2 + 2\, CB \cdot BD`, so the excess :math:`AC^2 - (AB^2 + BC^2)` equals :math:`2\, CB \cdot BD`. Therefore that excess has a given ratio (:math:`= 2\, BD : AB = -2\cos\angle ABC`) to :math:`AB \cdot BC`.
