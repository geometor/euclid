:order: 56
:canonical_id: D.56
:breadcrumb_title: D.56
:book: Data
:proposition: 56
:type: proposition
:title: Proposition 56 [νϛ΄ · Prop. Prop. LXIII]
:folio: Menge 100
:page: 100
:excerpt: If two equiangular parallelograms have a given ratio to one another, as a side of the first is to a side of the second, so is the remaining side of the second to that straight line to which the remaining side of the first has the given ratio that the parallelogram has to the parallelogram.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _data-unit-4-en:

.. _D.56:

Proposition 56 [νϛ΄ · Prop. LXIII]
----------------------------------

.. folio:: Menge 100
   :page: 100

.. enunciation::

   If two equiangular parallelograms have a given ratio to one another, as a side of the first is to a side of the second, so is the remaining side of the second to that straight line to which the remaining side of the first has the given ratio that the parallelogram has to the parallelogram.

*Functional Signature*: ``Given(Equiangular(P1, P2), Ratio(P1 : P2) = k) -> Determined(s1 : t1 = t2 : (s2 / k))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`

Let two equiangular parallelograms :math:`ABCD` and :math:`EFGH` have a given area ratio :math:`ABCD : EFGH`. I say that as :math:`CD` (a side of the first) is to :math:`FG` (a side of the second), so is the remaining side :math:`GH` of the second to a straight line to which the remaining side :math:`BC` of the first has a given ratio.

Produce :math:`BC` to :math:`K` so that the ratio :math:`BC : CK` is equal to the given area ratio :math:`ABCD : EFGH` (:just:`[Data Def. 2] <D.def.2>`), and complete the equiangular parallelogram :math:`CDLK` on :math:`CD` and :math:`CK` (:just:`[I.31] <I.31>`). Because :math:`ABCD` and :math:`CDLK` share the base :math:`CD` and have the same altitude, :math:`ABCD : CDLK = BC : CK` (:just:`[VI.1] <VI.1>`). Yet :math:`BC : CK = ABCD : EFGH` by construction; therefore :math:`CDLK = EFGH` (:just:`[V.9] <V.9>`). Now :math:`CDLK` and :math:`EFGH` are equal and equiangular parallelograms, so their sides about the equal angles are reciprocally proportional: :math:`CD : FG = GH : CK` (:just:`[VI.14] <VI.14>`). And since :math:`BC : CK` is given, :math:`CD` is to :math:`FG` as :math:`GH` is to :math:`CK`, a straight line to which :math:`BC` has a given ratio.
