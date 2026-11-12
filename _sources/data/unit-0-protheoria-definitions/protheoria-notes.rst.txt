:order: 3
:type: notes
:canonical_id: D.unit.0
:folio: Menge 234–256, 2–4
:book: Protheoria & Definitions

.. _data-unit-0-notes:

===============================================================================
Unit 0: Marinus's Protheoria & Definitions 1–15 — Philological & Critical Notes
===============================================================================

1. Marinus, Pappus, and Simson on Analysis vs. Synthesis in the *Data*
----------------------------------------------------------------------

At the close of the *Protheoria* (:ref:`§ 18 <marinus-p18>`, *Menge* p. 256), :person:`Marinus <marinus>` invokes :person:`Pappus's <pappus>` lost *Commentary on the Data* (:cite:`Synagoge VII <pappus:synagoge>`) to assert that :person:`Euclid <euclid>` followed the method of :term:`analysis <analysis>` rather than :term:`synthesis <synthesis>`. In the Preface to his 1762/1806 edition (:cite:`pp. 357–358 <simson:1762>`), :person:`Robert Simson <simson>` sharply objected:

   *"At the end of it, he [Marinus] says, that Euclid has not used the synthetical but the analytical method in delivering them; in which he is quite mistaken; for in the analysis of a theorem, the thing to be demonstrated is assumed in the analysis; but in the demonstrations of the Data, the thing to be demonstrated, which is, that something or other is given, is never once assumed in the demonstration, from which it is manifest, that every one of them is demonstrated synthetically; though indeed, if a proposition of the Data be turned into a problem, for example, the 84th or 85th ... the demonstration of the proposition becomes the analysis of the problem."*

Both thinkers illuminate complementary halves of the truth:

* **Logical Form of Each Proof (Simson)**: Every proposition ``D.k`` argues *forward* from ``Given(X)`` to ``Determined(Y)`` using definitions of ``πορίσασθαι`` and theorems of the *Elements*. None assumes ``Determined(Y)`` beforehand.
* **Architectonic Role in Problem-Solving (Pappus & Marinus)**: When a geometer analyzes a *problem* ('to construct $Y$ satisfying condition $X$'), assuming the figure drawn yields condition $X$ as *given*; chaining forward through the *Data* deduces that $Y$ is *given*—which **is** the :term:`analysis <analysis>` of the problem! Reversing the constructive witnesses inside Euclid's proofs (`πεπορίσθω`) then yields the :term:`synthesis <synthesis>` automatically.

2. Simson's Regular-Heptagon Critique of Definition 4 (*Position*)
------------------------------------------------------------------

:just:`[Data Def. 4] <D.def.4>` defines points, lines, and angles as :term:`given in position <thesei>` when they *"always occupy the same place"* (*ἃ τὸν αὐτὸν ἀεὶ τόπον ἐπέχει*). In his critical note on Def. IV (:cite:`p. 455 <simson:1762>`), :person:`Simson <simson>` observed that Euclid's wording captures :person:`Apollonius's <apollonius>` :term:`τεταγμένον <tetagmenon>` (*uniquely determined in nature*) while omitting :term:`πόριμον <porimon>` (*constructible by elementary means*): if $\triangle ABC$ is given in position, a ray $BD$ cutting off $\angle DBC = \frac{1}{7} \angle ABC$ occupies an invariant, unique place, yet **cannot be constructed by straightedge and compass** (since angle septisection / the regular heptagon requires a cubic *neusis* or conic intersection, outside the quadratic closure of the *Elements*). Simson therefore appended *"and which are either actually exhibited, or can be found"*—confirming in detail :person:`Marinus's <marinus>` diagnosis in :ref:`§ 15 <marinus-p15>` that *givenness* requires **procurability** (*πόριμον*), not mere uniqueness (*τεταγμένον*).

3. Affine-Ratio Idiom in Definitions 11–12 (*Δοθέντι μεῖζον ἢ ἐν λόγῳ*)
-----------------------------------------------------------------------

:just:`[Data Def. 11] <D.def.11>` and :just:`[Data Def. 12] <D.def.12>` introduce Euclid's remarkably compact Greek idiom :term:`δοθέντι μεῖζον ἢ ἐν λόγῳ <dothenti-meizon-e-en-logo>` (*"greater [or less] by a given magnitude than in ratio"*):

.. math::

   (A - D) : B = k \iff A = k \cdot B + D, \qquad (A + D) : B = k \iff A = k \cdot B - D,

where offset $D$ is given in magnitude and slope $k$ is given in ratio. This turns 1D **affine-linear transformations** into a single syntactic predicate closed under composition (:ref:`D.19 <D.19>`) and Gaussian elimination (:ref:`D.17 <D.17>`–:ref:`D.18 <D.18>`). :person:`Simson <simson>` (:cite:`p. 456 <simson:1762>`) omitted Defs. 11–12 only because literal English sounded obscure, expanding the phrase verbally as *"the excess of one magnitude above a given magnitude has a given ratio to the other"* across his Props. XIV–XXVII.

4. Manuscript Authority & Bracketing of Definitions 13–15
---------------------------------------------------------

In the ninth-century non-Theonine Vatican archetype :cite:`Vat. gr. 190 (Codex P) <vat-gr-190>` collated by :person:`Heinrich Menge <menge>` (:cite:`1896, p. 4 <menge:1896>`), Definitions 1–12 form the authentic Euclidean core, whereas :just:`[Data Def. 13] <D.def.13>` (:term:`κατηγμένη <kategmene>`), :just:`[Data Def. 14] <D.def.14>` (:term:`ἀνηγμένη <anegmene>`), and :just:`[Data Def. 15] <D.def.15>` (:term:`παρὰ θέσει <para-thesei>`) are enclosed in editorial brackets ``[...]`` as post-Euclidean scholia imported from Alexandrian locus and conic terminology (their terms never appear in the proofs of :ref:`D.28 <D.28>`–:ref:`D.30 <D.30>`, where Euclid writes out the full geometric descriptions). :person:`Simson <simson>` (:cite:`p. 456 <simson:1762>`) had already rejected all three on internal mathematical grounds.
