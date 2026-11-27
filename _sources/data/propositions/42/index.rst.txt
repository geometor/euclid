:order: 42
:canonical_id: D.42
:breadcrumb_title: D.42
:book: Data
:proposition: 42
:type: proposition
:title: Proposition 42 [μβ΄ · Prop. Prop. XLV]
:folio: Menge 74
:page: 74
:excerpt: If the sides of a triangle have given ratios to one another, the triangle is given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.42:

Proposition 42 [μβ΄ · Prop. XLV]
--------------------------------

.. folio:: Menge 74
   :page: 74

.. enunciation::

   If the sides of a triangle have given ratios to one another, the triangle is given in species.

*Functional Signature*: ``Given(Ratio(a : b), Ratio(b : c)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 39] <D.39>`, :just:`[I.20] <I.20>`, :just:`[I.22] <I.22>`, :just:`[VI.5] <VI.5>`

Let the three sides :math:`AB, BC, CA` of :math:`\triangle ABC` have given ratios to one another. I say that :math:`\triangle ABC` is given in species.

Set out a given straight line :math:`D`. Make :math:`D : E = AB : BC` and :math:`D : F = AB : AC` (:just:`[Data Def. 2] <D.def.2>`). Since :math:`D` is given and both ratios are given, :math:`E` and :math:`F` are given in magnitude (:just:`[Data 2] <D.2>`). Because :math:`AB, BC, CA` satisfy the triangle inequality (:just:`[I.20] <I.20>`) and :math:`D, E, F` are proportional to :math:`AB, BC, CA` (:just:`[Data 8] <D.8>`), any two of :math:`D, E, F` are greater than the remaining one; construct :math:`\triangle GHK` from sides :math:`GH = D`, :math:`HK = E`, :math:`KG = F` (:just:`[I.22] <I.22>`). Since each side of :math:`\triangle GHK` is given in magnitude, :math:`\triangle GHK` is given in species (:just:`[Data 39] <D.39>`). Because :math:`AB : BC : CA = GH : HK : KG`, :math:`\triangle ABC` is equiangular and similar to :math:`\triangle GHK` (:just:`[VI.5] <VI.5>`), and therefore :math:`\triangle ABC` is given in species (:just:`[Data Def. 3] <D.def.3>`).
