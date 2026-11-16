:order: 60
:canonical_id: D.60
:breadcrumb_title: D.60
:book: Data
:proposition: 60
:type: proposition
:title: Proposition 60 [ξ΄ · Prop. Prop. LXXXII]
:folio: Menge 108
:page: 108
:excerpt: If a parallelogram given in species and in magnitude be increased or diminished by a gnomon given in magnitude, the breadths of the gnomon are given.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.60:

Proposition 60 [ξ΄ · Prop. LXXXII]
----------------------------------

.. folio:: Menge 108
   :page: 108

.. enunciation::

   If a parallelogram given in species and in magnitude be increased or diminished by a gnomon given in magnitude, the breadths of the gnomon are given.

*Functional Signature*: ``Given(Species(P), Mag(Area(P)), Mag(Gnomon G)) -> Determined(Mag(Sides of P +/- G))`` · *Dependencies*: :just:`[Data 3] <D.3>`, :just:`[Data 4] <D.4>`, :just:`[Data 55] <D.55>`, :just:`[VI.24] <VI.24>`

First, let a parallelogram $ABCD$, given both in species and in magnitude, be increased by a given :term:`gnomon <gnomon>` $ECBDFG$ so as to form a larger similar parallelogram $AEFG$. I say that the breadths $CE$ and $DF$ of the gnomon are given in magnitude.

Since $ABCD$ is given in magnitude and the gnomon $ECBDFG$ is given in magnitude, the whole parallelogram $AEFG = ABCD + ECBDFG$ is given in magnitude (:just:`[Data 3] <D.3>`). Moreover, because a gnomon adjoined around the diagonal preserves similarity (:just:`[VI.24] <VI.24>`), $AEFG$ is similar to $ABCD$ and hence given in species (:just:`[Data Def. 3] <D.def.3>`). Therefore the side $AE$ of $AEFG$ is given in magnitude (:just:`[Data 55] <D.55>`), while the side $AC$ of $ABCD$ is likewise given in magnitude (:just:`[Data 55] <D.55>`). Subtracting $AC$ from $AE$ yields the gnomon breadth $CE$ given in magnitude (:just:`[Data 4] <D.4>`), and similarly $DF$ is given.

Second, let the species-and-magnitude-given parallelogram $AEFG$ be diminished by a given gnomon $ECBDFG$ leaving $ABCD$: then the remainder $ABCD = AEFG - ECBDFG$ is given in magnitude (:just:`[Data 4] <D.4>`) and in species ($\sim AEFG$), so both $AE$ and $AC$ are given in magnitude (:just:`[Data 55] <D.55>`), whence their difference $CE$ (and $DF$) is given in magnitude (:just:`[Data 4] <D.4>`).
