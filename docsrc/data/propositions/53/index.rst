:order: 53
:canonical_id: D.53
:breadcrumb_title: D.53
:book: Data
:proposition: 53
:type: proposition
:title: Proposition 53 [νγ΄ · Prop. Prop. LVII]
:folio: Menge 94
:page: 94
:excerpt: If two figures be given in species, and one side of one have a given ratio to one side of the other, the remaining sides will also have given ratios to the remaining sides.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.53:

Proposition 53 [νγ΄ · Prop. LVII]
---------------------------------

.. enunciation::

   If two figures be given in species, and one side of one have a given ratio to one side of the other, the remaining sides will also have given ratios to the remaining sides.

*Functional Signature*: ``Given(Species(A), Species(B), Ratio(s1(A) : s1(B))) -> Determined(Ratio(si(A) : sj(B)))`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 8] <D.8>`, :just:`[V.22] <V.22>`

Let two rectilinear figures $A$ and $B$ be given in species, and let two sides—say $CD$ of $A$ and $EF$ of $B$—have a given ratio $CD : EF$. I say that the remaining sides also have given ratios to the remaining sides.

Let $GH$ be any other side of $A$ and $KL$ any other side of $B$. Since $A$ is given in species, the ratio of its own sides $GH : CD$ is given (:just:`[Data Def. 3] <D.def.3>`). By hypothesis, the ratio $CD : EF$ is given. And since $B$ is given in species, the ratio $EF : KL$ is given (:just:`[Data Def. 3] <D.def.3>`). Chaining $GH : CD$, $CD : EF$, and $EF : KL$ via :just:`[Data 8] <D.8>` proves that the ratio $GH : KL$ is given.
