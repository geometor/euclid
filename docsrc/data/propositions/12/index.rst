:order: 12
:canonical_id: D.12
:breadcrumb_title: D.12
:book: Data
:proposition: 12
:type: proposition
:title: Proposition 12 [ιβ΄ · Prop. Prop. V]
:folio: Menge 22
:page: 22
:excerpt: If there be three magnitudes, and the first together with the second be given, and the second together with the third be also given, then either the first is equal to the third, or one exceeds the other by a given magnitude.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.12:

Proposition 12 [ιβ΄ · Prop. V]
------------------------------

.. folio:: Menge 22
   :page: 22

.. enunciation::

   If there be three magnitudes, and the first together with the second be given, and the second together with the third be also given, then either the first is equal to the third, or one exceeds the other by a given magnitude.

*Functional Signature*: ``Given(Mag(A + B), Mag(B + C)) -> Determined(A = C | ExceedsByGiven(A, C))`` · *Dependencies*: :just:`[Data Def. 9] <D.def.9>`, :just:`[Data 4] <D.4>`, :just:`[C.N. 3] <I.cn.3>`

Let there be three magnitudes :math:`AB, BC, CD`, and let :math:`AB + BC = AC` be given, and let :math:`BC + CD = BD` also be given. I say that either :math:`AB` is equal to :math:`CD`, or one exceeds the other by a given magnitude.

Since each of :math:`AC` and :math:`BD` is given, :math:`AC` and :math:`BD` are either equal or unequal. First, let them be equal: since :math:`AC = BD`, subtract the common magnitude :math:`BC`; then the remainder :math:`AB` is equal to the remainder :math:`CD` (:just:`[C.N. 3] <I.cn.3>`). Next, let them be unequal, and let :math:`AC` be greater than :math:`BD`: cut off :math:`EC = BD` from :math:`AC` (:just:`[Data Def. 1] <D.def.1>`); since both :math:`AC` and :math:`EC` are given, the remainder :math:`AE` is given (:just:`[Data 4] <D.4>`). Subtracting the common part :math:`BC` from :math:`EC = BD` gives :math:`EB = CD` (:just:`[C.N. 3] <I.cn.3>`), so :math:`AB = AE + EB` exceeds :math:`CD` by the given magnitude :math:`AE`.
