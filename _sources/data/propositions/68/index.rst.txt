:order: 68
:canonical_id: D.68
:breadcrumb_title: D.68
:book: Data
:proposition: 68
:type: proposition
:title: Proposition 68 [ξη΄ · Prop. Prop. LXV]
:folio: Menge 126
:page: 126
:excerpt: If two equiangular parallelograms have a given ratio to one another, and one side have to one side a given ratio, the remaining side will also have to the remaining side a given ratio.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _data-unit-5-en:

.. _D.68:

Proposition 68 [ξη΄ · Prop. LXV]
--------------------------------

.. folio:: Menge 126
   :page: 126

.. enunciation::

   If two equiangular parallelograms have a given ratio to one another, and one side have to one side a given ratio, the remaining side will also have to the remaining side a given ratio.

*Functional Signature*: ``Given(Equiangular(P1, P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))`` · *Dependencies*: :just:`[Data 2] <D.2>`, :just:`[Data 8] <D.8>`, :just:`[Data 56] <D.56>`, :just:`[I.31] <I.31>`, :just:`[VI.1] <VI.1>`, :just:`[VI.14] <VI.14>`

Let two equiangular parallelograms :math:`AB` (:math:`= ACDB`) and :math:`EF` (:math:`= EGHF`) have a given area ratio :math:`AB : EF`, and let one side :math:`BD` have a given ratio to one side :math:`FH`. I say that the remaining side :math:`CD` also has a given ratio to the remaining side :math:`GH`.

Along :math:`CD` (produced if necessary) apply to :math:`BD` the equiangular parallelogram :math:`BDKL` equal in area to :math:`EF` (:just:`[I.44] <I.44>`). Because :math:`AB : EF` is given and :math:`BDKL = EF`, the ratio :math:`AB : BDKL` is given; since :math:`AB` and :math:`BDKL` share the base :math:`BD` in the same angle, :math:`CD : DK = AB : BDKL` (:just:`[VI.1] <VI.1>`), so :math:`CD : DK` is given. Moreover, because :math:`BDKL` and :math:`EF` are equal and equiangular, their sides about the equal angles are reciprocally proportional: :math:`BD : FH = GH : DK` (:just:`[VI.14] <VI.14>`). Since :math:`BD : FH` is given, :math:`GH : DK` is given; combining :math:`CD : DK` with :math:`DK : GH` yields :math:`CD : GH` given (:just:`[Data 8] <D.8>`).
