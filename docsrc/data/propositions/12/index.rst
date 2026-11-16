:order: 12
:canonical_id: D.12
:breadcrumb_title: D.12
:book: Data
:proposition: 12
:type: proposition
:title: Proposition 12 [ιβ΄ · Prop. Prop. V]
:folio: Menge 22
:page: 22
:excerpt: If there be three magnitudes, and the first together with the second be given, and the second together with the third be also given, then either the first is equal to the third, or one exceeds the other by a given magnitude.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.12:

Proposition 12 [ιβ΄ · Prop. V]
------------------------------

.. folio:: Menge 22
   :page: 22

.. enunciation::

   If there be three magnitudes, and the first together with the second be given, and the second together with the third be also given, then either the first is equal to the third, or one exceeds the other by a given magnitude.

*Functional Signature*: ``Given(Mag(A + B), Mag(B + C)) -> Determined(A = C | ExceedsByGiven(A, C))`` · *Dependencies*: :just:`[Data Def. 9] <D.def.9>`, :just:`[Data 4] <D.4>`, :just:`[C.N. 3] <I.cn.3>`

Let there be three magnitudes $AB, BC, CD$, and let $AB + BC = AC$ be given, and let $BC + CD = BD$ also be given. I say that either $AB$ is equal to $CD$, or one exceeds the other by a given magnitude.

Since each of $AC$ and $BD$ is given, $AC$ and $BD$ are either equal or unequal. First, let them be equal: since $AC = BD$, subtract the common magnitude $BC$; then the remainder $AB$ is equal to the remainder $CD$ (:just:`[C.N. 3] <I.cn.3>`). Next, let them be unequal, and let $AC$ be greater than $BD$: cut off $EC = BD$ from $AC$ (:just:`[Data Def. 1] <D.def.1>`); since both $AC$ and $EC$ are given, the remainder $AE$ is given (:just:`[Data 4] <D.4>`). Subtracting the common part $BC$ from $EC = BD$ gives $EB = CD$ (:just:`[C.N. 3] <I.cn.3>`), so $AB = AE + EB$ exceeds $CD$ by the given magnitude $AE$.
