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

Let two parallelograms $AB$ (with given angle $\angle CDB$) and $EF$ (with given angle $\angle GHF$, not necessarily equal to $\angle CDB$) have a given area ratio $AB : EF$, and let one side $BD$ have a given ratio to one side $FH$. I say that the remaining side $CD$ also has a given ratio to the remaining side $GH$.

If $AB$ and $EF$ are equiangular, the conclusion holds immediately by :just:`[Data 68] <D.68>`. Suppose $\angle CDB \neq \angle GHF$: at $D$ on $BD$, draw $DK$ making $\angle BDK = \angle GHF$ (:just:`[I.23] <I.23>`), meeting the line of the opposite side $AC$ (produced) at $K$, and complete the parallelogram $BDKL$ (:just:`[I.31] <I.31>`). In $\\triangle CDK$, $\angle CDK$ is the difference (or supplement difference) of the two given angles $\angle CDB$ and $\angle BDK$, so $\angle CDK$ is given (:just:`[Data 4] <D.4>`), and $\angle CKD$ equals the interior/alternate angle with $BD$ (:just:`[I.29] <I.29>`), which is given; hence $\\triangle CDK$ is given in species (:just:`[Data 40] <D.40>`), so the ratio $CD : DK$ is given! Because $AB$ and $BDKL$ lie between the same parallels $AC$ and $BD$ on the same base $BD$, $AB = BDKL$ (:just:`[I.35] <I.35>`). Thus $BDKL$ is equiangular with $EF$, $BDKL : EF = AB : EF$ is given, and $BD : FH$ is given; by :just:`[Data 68] <D.68>`, the ratio $DK : GH$ is given. Combining $CD : DK$ and $DK : GH$ gives $CD : GH$ given (:just:`[Data 8] <D.8>`).
