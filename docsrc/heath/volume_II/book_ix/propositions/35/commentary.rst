:canonical_id: IX.35.commentary
:volume: II
:book: IX
:proposition: 35
:type: commentary
:title: Commentary on Proposition IX.35
:folios: 0427
:pages: 421

.. _IX.35.commentary:

Commentary on Proposition IX.35
===============================

Back to :ref:`Proposition IX.35 <IX.35>`.

.. _folio-ii-0427:

.. folio:: 0427
   :page: 421

This proposition is perhaps the most interesting in the arithmetical Books, since it gives a method, and a very elegant one, of summing any series of *terms in geometrical progression*.

Let $a_1, a_2, a_3, \dots a_n, a_{n+1}$ be a series of terms in geometrical progression. Then Euclid's proposition proves that

$$(a_{n+1} - a_1) : (a_1 + a_2 + \dots + a_n) = (a_2 - a_1) : a_1.$$

For clearness' sake we will on this occasion use the fractional notation of algebra to represent proportions.

Euclid's method then comes to this.

Since

$$\frac{a_{n+1}}{a_n} = \frac{a_n}{a_{n-1}} = \dots = \frac{a_2}{a_1},$$

we have, :term:`*separando* <separando>`,

$$\frac{a_{n+1} - a_n}{a_n} = \frac{a_n - a_{n-1}}{a_{n-1}} = \dots = \frac{a_3 - a_2}{a_2} = \frac{a_2 - a_1}{a_1},$$

whence, since, as one of the antecedents is to one of the consequents, so is the sum of all the antecedents to the sum of all the consequents, :just:`[VII. 12] <VII.12>`

$$\frac{a_{n+1} - a_1}{a_n + a_{n-1} + \dots + a_1} = \frac{a_2 - a_1}{a_1},$$

which gives $a_1 + a_2 + \dots + a_n$, or $S_n$.

If, to compare the result with that arrived at in algebraical text-books, we write the series in the form

$$a,\ ar,\ ar^2, \dots ar^{n-1} \quad (n\text{ terms}),$$

we have

$$\frac{ar^n - a}{S_n} = \frac{ar - a}{a},$$

or

$$S_n = \frac{a(r^n - 1)}{r - 1}.$$
