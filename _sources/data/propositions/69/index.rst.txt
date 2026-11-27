:order: 69
:canonical_id: D.69
:breadcrumb_title: D.69
:book: Data
:proposition: 69
:type: proposition
:title: Proposition 69 [ξθ΄ · Prop. Prop. LXVI]
:folio: Menge 128
:page: 128
:excerpt: If two parallelograms have given angles, and have a given ratio to one another, and one side have to one side a given ratio, the remaining side will also have a given ratio to the remaining side.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.69:

Proposition 69 [ξθ΄ · Prop. LXVI]
---------------------------------

.. folio:: Menge 128
   :page: 128

.. enunciation::

   If two parallelograms have given angles, and have a given ratio to one another, and one side have to one side a given ratio, the remaining side will also have a given ratio to the remaining side.

*Functional Signature*: ``Given(Angle(P1), Angle(P2), Ratio(P1 : P2), Ratio(s1 : t1)) -> Determined(Ratio(s2 : t2))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 40] <D.40>`, :just:`[Data 68] <D.68>`, :just:`[I.12] <I.12>`, :just:`[I.23] <I.23>`, :just:`[I.31] <I.31>`, :just:`[I.35] <I.35>`

Let two parallelograms :math:`AB` (with given angle :math:`\angle CDB`) and :math:`EF` (with given angle :math:`\angle GHF`, not necessarily equal to :math:`\angle CDB`) have a given area ratio :math:`AB : EF`, and let one side :math:`BD` have a given ratio to one side :math:`FH`. I say that the remaining side :math:`CD` also has a given ratio to the remaining side :math:`GH`.

If :math:`AB` and :math:`EF` are equiangular, the conclusion holds immediately by :just:`[Data 68] <D.68>`. Suppose :math:`\angle CDB \neq \angle GHF`: at :math:`D` on :math:`BD`, draw :math:`DK` making :math:`\angle BDK = \angle GHF` (:just:`[I.23] <I.23>`), meeting the line of the opposite side :math:`AC` (produced) at :math:`K`, and complete the parallelogram :math:`BDKL` (:just:`[I.31] <I.31>`). In :math:`\\triangle CDK`, :math:`\angle CDK` is the difference (or supplement difference) of the two given angles :math:`\angle CDB` and :math:`\angle BDK`, so :math:`\angle CDK` is given (:just:`[Data 4] <D.4>`), and :math:`\angle CKD` equals the interior/alternate angle with :math:`BD` (:just:`[I.29] <I.29>`), which is given; hence :math:`\\triangle CDK` is given in species (:just:`[Data 40] <D.40>`), so the ratio :math:`CD : DK` is given! Because :math:`AB` and :math:`BDKL` lie between the same parallels :math:`AC` and :math:`BD` on the same base :math:`BD`, :math:`AB = BDKL` (:just:`[I.35] <I.35>`). Thus :math:`BDKL` is equiangular with :math:`EF`, :math:`BDKL : EF = AB : EF` is given, and :math:`BD : FH` is given; by :just:`[Data 68] <D.68>`, the ratio :math:`DK : GH` is given. Combining :math:`CD : DK` and :math:`DK : GH` gives :math:`CD : GH` given (:just:`[Data 8] <D.8>`).
