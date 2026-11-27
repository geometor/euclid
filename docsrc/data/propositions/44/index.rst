:order: 44
:canonical_id: D.44
:breadcrumb_title: D.44
:book: Data
:proposition: 44
:type: proposition
:title: Proposition 44 [μδ΄ · Prop. Prop. XLVII]
:folio: Menge 78
:page: 78
:excerpt: If a triangle have one angle given, and the sides about another angle have a given ratio to one another, the triangle is given in species.
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _D.44:

Proposition 44 [μδ΄ · Prop. XLVII]
----------------------------------

.. folio:: Menge 78
   :page: 78

.. enunciation::

   If a triangle have one angle given, and the sides about another angle have a given ratio to one another, the triangle is given in species.

*Functional Signature*: ``Given(Angle(A), Ratio(AB : BC), Sign(cos C)) -> Determined(Species(Triangle ABC)) [SSA diorismos]`` · *Dependencies*: :just:`[Data Def. 3] <D.def.3>`, :just:`[Data 2] <D.2>`, :just:`[Data 25] <D.25>`, :just:`[Data 26] <D.26>`, :just:`[Data 27] <D.27>`, :just:`[Data 29] <D.29>`, :just:`[Data 31] <D.31>`, :just:`[I.13] <I.13>`, :just:`[VI.7] <VI.7>`

Let :math:`\triangle ABC` have one given angle :math:`\angle ABC`, and let the sides :math:`AB` and :math:`AC` about another angle :math:`\angle BAC` have a given ratio :math:`AB : AC`—*assuming the specification (diorismos) whether* :math:`\angle ACB` *is obtuse or acute is fixed*. I say that :math:`\triangle ABC` is given in species.

From :math:`A` drop :math:`AD` perpendicular to :math:`BC` (or :math:`BC` produced) (:just:`[I.12] <I.12>`). In right-angled :math:`\triangle ABD`, :math:`\angle ADB = 1\text{ rt.}` and :math:`\angle ABD` (or its supplement) is given, so all angles of :math:`\triangle ABD` are given (:just:`[I.32] <I.32>`), whence :math:`\triangle ABD` is given in species (:just:`[Data 40] <D.40>`). Therefore the ratio :math:`BA : AD` is given (:just:`[Data Def. 3] <D.def.3>`). Yet the ratio :math:`CA : AB` is given by hypothesis; *ex aequali*, the ratio :math:`CA : AD` is given (:just:`[Data 8] <D.8>`). Now :math:`\triangle ADC` is right-angled at :math:`D` with the ratio of hypotenuse :math:`CA` to leg :math:`AD` given; hence :math:`\triangle ADC` is given in species (:just:`[Data 43] <D.43>`), so the acute angle :math:`\angle ACD` is given! Depending on the single branch specified (whether :math:`D` falls on :math:`BC` with :math:`\angle ACB` acute, or on :math:`BC` produced with :math:`\angle ACB = 2\text{ rt.} - \angle ACD` obtuse), :math:`\angle ACB` is uniquely given. Together with given :math:`\angle ABC`, all angles of :math:`\triangle ABC` are given (:just:`[I.32] <I.32>`), so :math:`\triangle ABC` is given in species (:just:`[Data 40] <D.40>`).
