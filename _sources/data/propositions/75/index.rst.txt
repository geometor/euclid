:order: 75
:canonical_id: D.75
:breadcrumb_title: D.75
:book: Data
:proposition: 75
:type: proposition
:title: Proposition 75 [οε΄ · Prop. Prop. LXIV Cor.]
:folio: Menge 144
:page: 144
:excerpt: If two triangles have a given ratio to one another, either in equal angles or in unequal yet given angles, as a side of the first is to a side of the second, so will the other side of the second be to that straight line to which the remaining side of the first has a given ratio.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.75:

Proposition 75 [οε΄ · Prop. LXIV Cor.]
--------------------------------------

.. folio:: Menge 144
   :page: 144

.. enunciation::

   If two triangles have a given ratio to one another, either in equal angles or in unequal yet given angles, as a side of the first is to a side of the second, so will the other side of the second be to that straight line to which the remaining side of the first has a given ratio.

*Functional Signature*: ``Given(Angle(A), Angle(D), Ratio(△1 : △2)) -> Determined(AB : DE = DF : K with GivenRatio(AC : K))`` · *Dependencies*: :just:`[Data 74] <D.74>`, :just:`[I.34] <I.34>`, :just:`[V.15] <V.15>`

Let two triangles $\\triangle ABC$ and $\\triangle DEF$ have a given area ratio $\\triangle ABC : \\triangle DEF$, and let the angles $\angle B$ and $\angle E$ either be equal, or be supplementary ($\angle B + \angle E = 2\\text{ rt.}$), or be unequal given angles. I say that as $BC$ is to $EF$, so is $DE$ to a straight line to which $AB$ has a given ratio.

Complete the parallelograms $ABCG$ and $DEFH$ (:just:`[I.31] <I.31>`). Since each parallelogram is double its triangle (:just:`[I.34] <I.34>`), $ABCG : DEFH = \\triangle ABC : \\triangle DEF$ (:just:`[V.15] <V.15>`) is given. If $\angle B = \angle E$, then $ABCG$ and $DEFH$ are equiangular; if $\angle B + \angle E = 2\\text{ rt.}$, then in parallelogram $ABCG$ the adjacent angle $\angle BAG = 2\\text{ rt.} - \angle B = \angle E$ (:just:`[I.29] <I.29>`), so $ABCG$ (viewed at $\angle A$ with sides $AG = BC$ and $AB$) is again equiangular with $DEFH$! And if $\angle B$ and $\angle E$ are both given, $ABCG$ and $DEFH$ have given angles. In every case, :just:`[Data 74] <D.74>` applies to $ABCG$ and $DEFH$, proving that $BC : EF = DE : K$ where $AB : K$ is given.
