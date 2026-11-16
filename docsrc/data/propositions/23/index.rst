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

Let the whole $AB$ have a given ratio to the whole $CD$, and let each of the parts $AE, EB$ of $AB$ have given ratios to the parts $CF, FD$ of $CD$ respectively, *but not the same ratios* (*μὴ τοὺς αὐτοὺς δέ*, so $AE : CF \neq EB : FD$). I say that all have given ratios to all.

Make $AE : CG = AB : CD$ (:just:`[Data Def. 2] <D.def.2>`). Since $AB : CD$ and $AE : CF$ are distinct ratios, $CG \neq CF$; suppose $G$ falls beyond $F$ on $CD$ (so $CG > CF$). Because $AE : CF$ is given and $AE : CG (= AB : CD)$ is given, the ratio $CF : CG$ is given (:just:`[Data 8] <D.8>`), whence *convertendo* $CF : FG$ is given (:just:`[Data 5] <D.5>`). Moreover, since whole $AB$ is to whole $CD$ as subtracted $AE$ is to subtracted $CG$, the remainder $EB$ is to the remainder $GD$ as $AB$ is to $CD$ (:just:`[V.19] <V.19>`), so $EB : GD$ is given. Yet $EB : FD$ is also given by hypothesis; hence $FD : GD$ is given (:just:`[Data 8] <D.8>`), and *separando* $FG : GD$ (and thus $FG : FD$) is given (:just:`[Data 5] <D.5>`). Combining $CF : FG$ and $FG : FD$ yields $CF : FD$ given (:just:`[Data 8] <D.8>`), whence $CD : CF$ and $CD : FD$ are given (:just:`[Data 6] <D.6>`). Chaining with the given ratios $AE : CF$ and $EB : FD$ gives $AE : EB$ and every pairwise ratio among $AB, AE, EB, CD, CF, FD$ (:just:`[Data 8] <D.8>`, :just:`[Data 9] <D.9>`).
