:order: 23
:canonical_id: D.23
:breadcrumb_title: D.23
:book: Data
:proposition: 23
:type: proposition
:title: Proposition 23 [κγ΄ · Prop. Prop. XII]
:folio: Menge 34
:page: 34
:excerpt: If a whole have to a whole a given ratio, and the parts have to the parts given ratios, yet not the same ratios, all the parts will have given ratios to all.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.23:

Proposition 23 [κγ΄ · Prop. XII]
--------------------------------

.. enunciation::

   If a whole have to a whole a given ratio, and the parts have to the parts given ratios, yet not the same ratios, all the parts will have given ratios to all.

*Functional Signature*: ``Given(AB:CD = r0, AE:CF = r1 != r0, EB:FD = r2) -> Determined(All pairwise ratios)`` · *Dependencies*: :just:`[Data 5] <D.5>`, :just:`[Data 8] <D.8>`, :just:`[V.11] <V.11>`, :just:`[V.16] <V.16>`, :just:`[V.19] <V.19>`

Let the whole :math:`AB` have a given ratio to the whole :math:`CD`, and let each of the parts :math:`AE, EB` of :math:`AB` have given ratios to the parts :math:`CF, FD` of :math:`CD` respectively, *but not the same ratios* (*μὴ τοὺς αὐτοὺς δέ*, so :math:`AE : CF \neq EB : FD`). I say that all have given ratios to all.

Make :math:`AE : CG = AB : CD` (:just:`[Data Def. 2] <D.def.2>`). Since :math:`AB : CD` and :math:`AE : CF` are distinct ratios, :math:`CG \neq CF`; suppose :math:`G` falls beyond :math:`F` on :math:`CD` (so :math:`CG > CF`). Because :math:`AE : CF` is given and :math:`AE : CG (= AB : CD)` is given, the ratio :math:`CF : CG` is given (:just:`[Data 8] <D.8>`), whence *convertendo* :math:`CF : FG` is given (:just:`[Data 5] <D.5>`). Moreover, since whole :math:`AB` is to whole :math:`CD` as subtracted :math:`AE` is to subtracted :math:`CG`, the remainder :math:`EB` is to the remainder :math:`GD` as :math:`AB` is to :math:`CD` (:just:`[V.19] <V.19>`), so :math:`EB : GD` is given. Yet :math:`EB : FD` is also given by hypothesis; hence :math:`FD : GD` is given (:just:`[Data 8] <D.8>`), and *separando* :math:`FG : GD` (and thus :math:`FG : FD`) is given (:just:`[Data 5] <D.5>`). Combining :math:`CF : FG` and :math:`FG : FD` yields :math:`CF : FD` given (:just:`[Data 8] <D.8>`), whence :math:`CD : CF` and :math:`CD : FD` are given (:just:`[Data 6] <D.6>`). Chaining with the given ratios :math:`AE : CF` and :math:`EB : FD` gives :math:`AE : EB` and every pairwise ratio among :math:`AB, AE, EB, CD, CF, FD` (:just:`[Data 8] <D.8>`, :just:`[Data 9] <D.9>`).
