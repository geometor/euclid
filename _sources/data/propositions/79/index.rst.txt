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

Let two triangles $\\triangle ABC$ and $\\triangle DEF$ have one equal angle $\angle BAC = \angle EDF$, and from the vertices $A$ and $D$ let perpendiculars $AG \perp BC$ and $DH \perp EF$ be drawn; if $BC : AG = EF : DH$, I say that $\\triangle ABC$ and $\\triangle DEF$ are equiangular (and hence similar).

Circumscribe circles $ABC$ and $DEF$ about the two triangles (:just:`[IV.5] <IV.5>`), cutting off segments on $BC$ and $EF$ that contain the equal angles $\angle BAC = \angle EDF$ (:just:`[III.21] <III.21>`). Complete the cyclic symmetry by constructing on $EF$ a triangle $\\triangle EKF$ similar to $\\triangle ABC$ inscribed in circle $DEF$ (so $\angle EKF = \angle BAC = \angle EDF$, placing $K$ on arc $EDF$ by :just:`[III.21] <III.21>`), and drop perpendicular $KL \perp EF$. Since $\\triangle EKF \sim \\triangle ABC$, their base-to-altitude ratios match: $EF : KL = BC : AG$ (:just:`[VI.4] <VI.4>`). Yet $BC : AG = EF : DH$ by hypothesis; therefore $EF : KL = EF : DH$ (:just:`[V.11] <V.11>`), whence $KL = DH$ (:just:`[V.9] <V.9>`). Thus the line through $K$ and $D$ is parallel to $EF$ (:just:`[I.33] <I.33>`), cutting equal arcs $EK = DF$ (or $K = D$) in circle $DEF$, so the inscribed angles are equal (up to swapping $\angle E$ and $\angle F$), making $\\triangle ABC$ and $\\triangle DEF$ equiangular!
