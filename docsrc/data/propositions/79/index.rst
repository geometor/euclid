:order: 79
:canonical_id: D.79
:breadcrumb_title: D.79
:book: Data
:proposition: 79
:type: proposition
:title: Proposition 79 [οθ΄ · Prop. Prop. LXXVII Cor. 1]
:folio: Menge 152
:page: 152
:excerpt: If there be two triangles having one angle equal to one angle, and from the vertices perpendiculars be drawn to the bases, and as the base of the first triangle is to its perpendicular, so be the base of the second triangle to its perpendicular, the triangles are equiangular.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.79:

Proposition 79 [οθ΄ · Prop. LXXVII Cor. 1]
------------------------------------------

.. folio:: Menge 152
   :page: 152

.. enunciation::

   If there be two triangles having one angle equal to one angle, and from the vertices perpendiculars be drawn to the bases, and as the base of the first triangle is to its perpendicular, so be the base of the second triangle to its perpendicular, the triangles are equiangular.

*Functional Signature*: ``Given(∠BAC = ∠EDF, BC : h_A = EF : h_D) -> Determined(△ABC ~ △DEF)`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data Def. 7] <D.def.7>`, :just:`[Data 40] <D.40>`, :just:`[I.12] <I.12>`, :just:`[III.21] <III.21>`, :just:`[VI.4] <VI.4>`

Let two triangles :math:`\\triangle ABC` and :math:`\\triangle DEF` have one equal angle :math:`\angle BAC = \angle EDF`, and from the vertices :math:`A` and :math:`D` let perpendiculars :math:`AG \perp BC` and :math:`DH \perp EF` be drawn; if :math:`BC : AG = EF : DH`, I say that :math:`\\triangle ABC` and :math:`\\triangle DEF` are equiangular (and hence similar).

Circumscribe circles :math:`ABC` and :math:`DEF` about the two triangles (:just:`[IV.5] <IV.5>`), cutting off segments on :math:`BC` and :math:`EF` that contain the equal angles :math:`\angle BAC = \angle EDF` (:just:`[III.21] <III.21>`). Complete the cyclic symmetry by constructing on :math:`EF` a triangle :math:`\\triangle EKF` similar to :math:`\\triangle ABC` inscribed in circle :math:`DEF` (so :math:`\angle EKF = \angle BAC = \angle EDF`, placing :math:`K` on arc :math:`EDF` by :just:`[III.21] <III.21>`), and drop perpendicular :math:`KL \perp EF`. Since :math:`\\triangle EKF \sim \\triangle ABC`, their base-to-altitude ratios match: :math:`EF : KL = BC : AG` (:just:`[VI.4] <VI.4>`). Yet :math:`BC : AG = EF : DH` by hypothesis; therefore :math:`EF : KL = EF : DH` (:just:`[V.11] <V.11>`), whence :math:`KL = DH` (:just:`[V.9] <V.9>`). Thus the line through :math:`K` and :math:`D` is parallel to :math:`EF` (:just:`[I.33] <I.33>`), cutting equal arcs :math:`EK = DF` (or :math:`K = D`) in circle :math:`DEF`, so the inscribed angles are equal (up to swapping :math:`\angle E` and :math:`\angle F`), making :math:`\\triangle ABC` and :math:`\\triangle DEF` equiangular!
