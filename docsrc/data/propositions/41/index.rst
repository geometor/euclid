:order: 41
:canonical_id: D.41
:breadcrumb_title: D.41
:book: Data
:proposition: 41
:type: proposition
:title: Proposition 41 [μα΄ · Prop. Prop. XLIV]
:folio: Menge 66
:page: 66
:excerpt: If a triangle have one angle given, and the sides about the given angle have a given ratio to one another, the triangle is given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.41:

Proposition 41 [μα΄ · Prop. XLIV]
---------------------------------

.. enunciation::

   If a triangle have one angle given, and the sides about the given angle have a given ratio to one another, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Ratio(c : b)) -> Determined(Species(Triangle ABC))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[VI.6] <VI.6>`

Let :math:`\triangle ABC` have one given angle :math:`\angle BAC`, and let the sides :math:`AB` and :math:`AC` about the given angle have a given ratio :math:`AB : AC`. I say that :math:`\triangle ABC` is given in species.

Set out a straight line :math:`DE` given in position and magnitude. At the given point :math:`D` on :math:`DE`, draw :math:`DF` making :math:`\angle EDF = \angle BAC` (:just:`[I.23] <I.23>`); since :math:`\angle BAC` is given, :math:`DF` is given in position (:just:`[Data 29] <D.29>`). Make :math:`DE : DF = AB : AC` (:just:`[Data Def. 2] <D.def.2>`); since :math:`DE` is given and :math:`AB : AC` is given, :math:`DF` is given in magnitude (:just:`[Data 2] <D.2>`), whence :math:`F` is given in position (:just:`[Data 27] <D.27>`). Join :math:`EF`: then :math:`EF` is given in position and magnitude (:just:`[Data 26] <D.26>`), so :math:`\triangle DEF` is given in species (:just:`[Data 39] <D.39>`). Because :math:`\angle BAC = \angle EDF` and :math:`AB : AC = DE : DF`, :math:`\triangle ABC \sim \triangle DEF` (:just:`[VI.6] <VI.6>`). Therefore :math:`\triangle ABC` is also given in species (:just:`[Data Def. 3] <D.def.3>`).
