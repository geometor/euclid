:order: 78
:canonical_id: D.78
:breadcrumb_title: D.78
:book: Data
:proposition: 78
:type: proposition
:title: Proposition 78 [οη΄ · Prop. Omitted (case of Prop. LXX / D.62)]
:folio: Menge 148
:page: 148
:excerpt: If a given figure have a given ratio to some parallelogram, and one side have a given ratio to one side of the figure, while the parallelogram is in a given angle, the parallelogram will be given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.78:

Proposition 78 [οη΄ · Omitted (case of Prop. LXX / D.62)]
---------------------------------------------------------

.. enunciation::

   If a given figure have a given ratio to some parallelogram, and one side have a given ratio to one side of the figure, while the parallelogram is in a given angle, the parallelogram will be given in species.

*Functional Signature*: ``Given(Species(A), Ratio(A : B), Ratio(s(A) : s1(B)), Angle(B)) -> Determined(Species(B))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 62] <D.62>`, :just:`[VI.14] <VI.14>`

Let a rectilinear figure :math:`AFEB` given in species have a given area ratio to a rectangle :math:`BC \cdot CD`, and let one side :math:`AB` of :math:`AFEB` have a given ratio to :math:`BC`. I say that :math:`CD` has a given ratio to :math:`BC` (and :math:`AB`), so the rectangle :math:`BC \cdot CD` is given in species.

Construct the square :math:`ABGH` on :math:`AB` (:just:`[I.46] <I.46>`). Since both :math:`AFEB` and :math:`ABGH` are given in species on :math:`AB`, the ratio :math:`ABGH : AFEB` is given (:just:`[Data 49] <D.49>`). Combining with the given ratio :math:`AFEB : (BC \cdot CD)` yields :math:`AB^2 : (BC \cdot CD)` given (:just:`[Data 8] <D.8>`). Moreover, since :math:`AB : BC` is given, the ratio :math:`AB^2 : (AB \cdot BC)` (:math:`= AB : BC` by :just:`[VI.1] <VI.1>`) is given, whence :math:`(AB \cdot BC) : (BC \cdot CD)` is given (:just:`[Data 8] <D.8>`). Canceling the common side :math:`BC` (:just:`[VI.1] <VI.1>`) gives :math:`AB : CD` (and hence :math:`BC : CD`) given, so the rectangle :math:`BC \cdot CD` is given in species (:just:`[Data Def. 3] <D.def.3>`).
