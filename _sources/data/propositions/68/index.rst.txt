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

Let two equiangular parallelograms $AB$ ($= ACDB$) and $EF$ ($= EGHF$) have a given area ratio $AB : EF$, and let one side $BD$ have a given ratio to one side $FH$. I say that the remaining side $CD$ also has a given ratio to the remaining side $GH$.

Along $CD$ (produced if necessary) apply to $BD$ the equiangular parallelogram $BDKL$ equal in area to $EF$ (:just:`[I.44] <I.44>`). Because $AB : EF$ is given and $BDKL = EF$, the ratio $AB : BDKL$ is given; since $AB$ and $BDKL$ share the base $BD$ in the same angle, $CD : DK = AB : BDKL$ (:just:`[VI.1] <VI.1>`), so $CD : DK$ is given. Moreover, because $BDKL$ and $EF$ are equal and equiangular, their sides about the equal angles are reciprocally proportional: $BD : FH = GH : DK$ (:just:`[VI.14] <VI.14>`). Since $BD : FH$ is given, $GH : DK$ is given; combining $CD : DK$ with $DK : GH$ yields $CD : GH$ given (:just:`[Data 8] <D.8>`).
