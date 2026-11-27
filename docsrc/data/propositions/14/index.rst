:order: 14
:canonical_id: D.14
:breadcrumb_title: D.14
:book: Data
:proposition: 14
:type: proposition
:title: Proposition 14 [ιδ΄ · Prop. Prop. XVIII]
:folio: Menge 26
:page: 26
:excerpt: If two magnitudes have a given ratio to one another, and a given magnitude be added to each of them, either the wholes will still have a given ratio to one another, or one will be greater than the other by a given magnitude than in ratio.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.14:

Proposition 14 [ιδ΄ · Prop. XVIII]
----------------------------------

.. folio:: Menge 26
   :page: 26

.. enunciation::

   If two magnitudes have a given ratio to one another, and a given magnitude be added to each of them, either the wholes will still have a given ratio to one another, or one will be greater than the other by a given magnitude than in ratio.

*Functional Signature*: ``Given(Ratio(A : C) = r, Mag(d1), Mag(d2)) -> Determined(Ratio(A+d1 : C+d2) | GreaterThanInRatio)`` · *Dependencies*: :just:`[Data Def. 11] <D.def.11>`, :just:`[Data 1] <D.1>`, :just:`[Data 2] <D.2>`, :just:`[Data 4] <D.4>`, :just:`[Data 8] <D.8>`, :just:`[V.12] <V.12>`, :just:`[V.18] <V.18>`

Let two magnitudes :math:`AB` and :math:`CD` have a given ratio to one another. First, let the given magnitudes :math:`BE` and :math:`DF` be added to them respectively. I say that the wholes :math:`AE` and :math:`CF` either have a given ratio to one another, or one is greater by a given magnitude than in ratio to the other.

Since each of :math:`BE` and :math:`DF` is given, make :math:`BG : DF = AB : CD` (:just:`[Data Def. 2] <D.def.2>`). Because :math:`AB : CD` is given and :math:`DF` is given, :math:`BG` is given (:just:`[Data 2] <D.2>`). Now :math:`BG` is either equal to :math:`BE` or unequal to it. If :math:`BG = BE`, then since :math:`AB : CD = BG : DF`, *componendo* the whole :math:`AE = AB + BE` is to the whole :math:`CF = CD + DF` as :math:`AB` is to :math:`CD` (:just:`[V.12] <V.12>`), so the ratio :math:`AE : CF` is given. If :math:`BG \neq BE`, suppose :math:`BE > BG`: since both :math:`BE` and :math:`BG` are given, the excess :math:`GE` is given (:just:`[Data 4] <D.4>`). Because :math:`AB : CD = BG : DF`, the compound :math:`AG : CF = AB : CD` (:just:`[V.12] <V.12>`) is given, and :math:`AE = AG + GE` exceeds :math:`AG` by the given magnitude :math:`GE`; therefore :math:`AE` is greater by a given magnitude than in ratio to :math:`CF` (:just:`[Data Def. 11] <D.def.11>`).

Second, let the given magnitudes :math:`EB` and :math:`FD` be subtracted from :math:`AB` and :math:`CD` respectively. Again make :math:`GB : FD = AB : CD`, so :math:`GB` is given (:just:`[Data 2] <D.2>`). If :math:`GB = EB`, then by :just:`[V.19] <V.19>` the remainders :math:`AE` and :math:`CF` have the given ratio :math:`AB : CD`. If :math:`GB > EB`, the difference :math:`GE` is given (:just:`[Data 4] <D.4>`), :math:`AG : CF = AB : CD` is given (:just:`[V.19] <V.19>`), and :math:`AE = AG + GE` is greater by the given magnitude :math:`GE` than in ratio to :math:`CF` (:just:`[Data Def. 11] <D.def.11>`).
