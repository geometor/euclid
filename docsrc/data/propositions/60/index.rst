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

First, let a parallelogram :math:`ABCD`, given both in species and in magnitude, be increased by a given :term:`gnomon <gnomon>` :math:`ECBDFG` so as to form a larger similar parallelogram :math:`AEFG`. I say that the breadths :math:`CE` and :math:`DF` of the gnomon are given in magnitude.

Since :math:`ABCD` is given in magnitude and the gnomon :math:`ECBDFG` is given in magnitude, the whole parallelogram :math:`AEFG = ABCD + ECBDFG` is given in magnitude (:just:`[Data 3] <D.3>`). Moreover, because a gnomon adjoined around the diagonal preserves similarity (:just:`[VI.24] <VI.24>`), :math:`AEFG` is similar to :math:`ABCD` and hence given in species (:just:`[Data Def. 3] <D.def.3>`). Therefore the side :math:`AE` of :math:`AEFG` is given in magnitude (:just:`[Data 55] <D.55>`), while the side :math:`AC` of :math:`ABCD` is likewise given in magnitude (:just:`[Data 55] <D.55>`). Subtracting :math:`AC` from :math:`AE` yields the gnomon breadth :math:`CE` given in magnitude (:just:`[Data 4] <D.4>`), and similarly :math:`DF` is given.

Second, let the species-and-magnitude-given parallelogram :math:`AEFG` be diminished by a given gnomon :math:`ECBDFG` leaving :math:`ABCD`: then the remainder :math:`ABCD = AEFG - ECBDFG` is given in magnitude (:just:`[Data 4] <D.4>`) and in species (:math:`\sim AEFG`), so both :math:`AE` and :math:`AC` are given in magnitude (:just:`[Data 55] <D.55>`), whence their difference :math:`CE` (and :math:`DF`) is given in magnitude (:just:`[Data 4] <D.4>`).
