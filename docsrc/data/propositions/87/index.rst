:order: 87
:canonical_id: D.87
:breadcrumb_title: D.87
:book: Data
:proposition: 87
:type: proposition
:title: Proposition 87 [πζ΄ · Prop. Prop. XCI]
:folio: Menge 172
:page: 172
:excerpt: If in a circle given in magnitude a straight line be drawn cutting off a segment that accepts a given angle, the straight line drawn is given in magnitude.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. picture:: /_static/figures/data_06_circle_angle_locus.svg
   :alt: Circle Chords, Inscribed Angles, and Tangent-Secant Power (D.87–D.91)

Interactive circle-locus diagram (:cite:`Menge pp. 168–178 <menge:1896>`): In circle :g:`(O, OA) <data_06_circle_angle_locus:( O A )>` with centre :g:`O <data_06_circle_angle_locus:O>` and diameter :g:`CE <data_06_circle_angle_locus:/ C E />`, chord :g:`BC <data_06_circle_angle_locus:/ B C />` subtends given inscribed angle :g:`∠BAC <data_06_circle_angle_locus:< B A C )>` in :g:`△ABC <data_06_circle_angle_locus:< A B C >>`, calibrated via right-angled triangle on :g:`BE <data_06_circle_angle_locus:/ B E />` (:ref:`D.87 <D.87>`–:ref:`D.88 <D.88>`). From external given point :g:`P <data_06_circle_angle_locus:P>`, tangent :g:`PT <data_06_circle_angle_locus:/ P T />` (perpendicular to radius :g:`OT <data_06_circle_angle_locus:/ O T />` at :g:`T <data_06_circle_angle_locus:T>`, :ref:`D.90 <D.90>`) fixes the secant power along :g:`CP <data_06_circle_angle_locus:/ C P />` (:ref:`D.91 <D.91>`).

.. _D.87:

Proposition 87 [πζ΄ · Prop. XCI]
--------------------------------

.. folio:: Menge 172
   :page: 172

.. enunciation::

   If in a circle given in magnitude a straight line be drawn cutting off a segment that accepts a given angle, the straight line drawn is given in magnitude.

*Functional Signature*: ``Given(CircleRadius R, InscribedAngle theta) -> Determined(Mag(Chord BC = 2*R*sin theta))`` · *Dependencies*: :just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`, :just:`[Data 40] <D.40>`, :just:`[Data 53] <D.53>`, :just:`[III.21] <III.21>`, :just:`[III.31] <III.31>`

In a circle $ABC$ :term:`given in magnitude <megethei>` (:just:`[Data Def. 5] <D.def.5>`), let a straight line $AC$ be drawn cutting off a segment $ABC$ that admits a given angle $\angle ABC$ (:just:`[Data Def. 7] <D.def.7>`). I say that the chord $AC$ is given in magnitude.

Take the centre $D$ of circle $ABC$ (:just:`[III.1] <III.1>`), draw the diameter $ADE$ through $A$ and $D$, and join $EC$. Since the circle $ABC$ is given in magnitude, its radius $AD$ and diameter $AE = 2\,AD$ are given in magnitude (:just:`[Data Def. 5] <D.def.5>`, :just:`[Data 3] <D.3>`). In the semicircle $ACE$, the angle $\angle ACE$ is right (:just:`[III.31] <III.31>`). Moreover, either $B$ and $E$ lie in the same segment on $AC$ so $\angle AEC = \angle ABC$ (:just:`[III.21] <III.21>`), or they lie in opposite segments of the cyclic quadrilateral $ABCE$ so $\angle AEC = 2\\text{ rt.} - \angle ABC$ (:just:`[III.22] <III.22>`, :just:`[Data 4] <D.4>`); in either case $\angle AEC$ is given. Therefore right-angled $\\triangle ACE$ has all angles given and is given in species (:just:`[Data 40] <D.40>`), so the ratio $AC : AE$ is given (:just:`[Data Def. 3] <D.def.3>`). Since the diameter $AE$ is given in magnitude, the chord $AC$ is given in magnitude (:just:`[Data 2] <D.2>`).
