:order: 49
:canonical_id: D.49
:breadcrumb_title: D.49
:book: Data
:proposition: 49
:type: proposition
:title: Proposition 49 [μθ΄ · Prop. Prop. LIII]
:folio: Menge 88
:page: 88
:excerpt: If on the same straight line any two rectilineal figures given in species be described, they will have a given ratio to one another.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.49:

Proposition 49 [μθ΄ · Prop. LIII]
---------------------------------

.. folio:: Menge 88
   :page: 88

.. enunciation::

   If on the same straight line any two rectilineal figures given in species be described, they will have a given ratio to one another.

*Functional Signature*: ``Given(Species(P1 on AB), Species(P2 on AB)) -> Determined(Ratio(Area(P1) : Area(P2)))`` · *Dependencies*: :just:`[Data 8] <D.8>`, :just:`[Data 22] <D.22>`, :just:`[Data 47] <D.47>`, :just:`[Data 48] <D.48>`, :just:`[VI.20] <VI.20>`

On the same straight line :math:`AB`, let any two rectilinear figures :math:`ABCDE` and :math:`ABFG` given in species be described. I say that :math:`ABCDE` has a given ratio to :math:`ABFG`.

Divide each figure into triangles given in species by drawing diagonals from :math:`A` and :math:`B`, say :math:`ABCDE = \triangle ABE + \triangle EBC + \triangle ECD` and :math:`ABFG = \triangle ABF + \triangle AFG` (:just:`[Data 47] <D.47>`). Because similar polygons and species-given sub-triangles on chained diagonals have given side-squared ratios (:just:`[VI.19] <VI.19>`), :math:`\triangle ECD : \triangle EBC` and :math:`\triangle EBC : \triangle ABE` are given, so by *componendo* (:just:`[Data 6] <D.6>`, :just:`[Data 22] <D.22>`) the whole polygon :math:`ABCDE` has a given ratio to the base triangle :math:`\triangle ABE`. For the same reason :math:`ABFG` has a given ratio to :math:`\triangle ABF`. Yet :math:`\triangle ABE` and :math:`\triangle ABF` are two species-given triangles on the *same* straight line :math:`AB`, so :math:`\triangle ABE : \triangle ABF` is given (:just:`[Data 48] <D.48>`). Chaining :math:`ABCDE : \triangle ABE`, :math:`\triangle ABE : \triangle ABF`, and :math:`\triangle ABF : ABFG` via :just:`[Data 8] <D.8>` proves that :math:`ABCDE : ABFG` is given.
