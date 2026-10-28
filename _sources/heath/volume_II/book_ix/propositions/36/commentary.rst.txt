:canonical_id: IX.36.commentary
:volume: II
:book: IX
:proposition: 36
:type: commentary
:title: Commentary on Proposition IX.36
:folios: 0430, 0431, 0432
:pages: 424, 425, 426

.. _IX.36.commentary:

Commentary on Proposition IX.36
===============================

Back to :ref:`Proposition IX.36 <IX.36>`.

.. folio:: 0430
   :page: 424

If the sum of any number of terms of the series

$$1, 2, 2^2, \dots 2^{n-1}$$

be prime, and the said sum be multiplied by the last term, the product will be a “perfect” number, i.e. equal to the sum of all its factors.

Let $1 + 2 + 2^2 + \dots + 2^{n-1} (= S_n)$ be prime ; then shall $S_n \cdot 2^{n-1}$ be “perfect.”

Take $(n - 1)$ terms of the series

$$S_n, 2S_n, 2^2 S_n, \dots 2^{n-2} S_n.$$

These are then terms proportional to the terms

$$2, 2^2, 2^3, \dots 2^{n-1}.$$

Therefore, :term:`*ex aequali* <ex-aequali>`,

$$2 : 2^{n-1} = S_n : 2^{n-2} S_n, \tag{VII. 14}$$

or

$$2 \cdot 2^{n-2} S_n = 2^{n-1} \cdot S_n. \tag{VII. 19}$$

(This is of course obvious algebraically, but Euclid’s notation requires him to prove it.)

Now, by IX. 35, we can sum the series $S_n + 2S_n + \dots + 2^{n-2} S_n$, and

$$(2S_n - S_n) : S_n = (2^{n-1} S_n - S_n) : (S_n + 2S_n + \dots + 2^{n-2} S_n).$$

Therefore

$$S_n + 2S_n + 2^2 S_n + \dots + 2^{n-2} S_n = 2^{n-1} S_n - S_n,$$

or

$$\begin{aligned}
2^{n-1} S_n &= S_n + 2S_n + 2^2 S_n + \dots + 2^{n-2} S_n + S_n \\
&= S_n + 2S_n + \dots + 2^{n-2} S_n + (1 + 2 + 2^2 + \dots + 2^{n-1}),
\end{aligned}$$

and $2^{n-1} S_n$ is measured by every term of the right hand expression.

It is now necessary to prove that $2^{n-1} S_n$ cannot have any factor except those terms.

Suppose, if possible, that it has a factor $x$ different from all of them, and let

$$2^{n-1} S_n = x \cdot m.$$

Therefore

$$S_n : m = x : 2^{n-1}. \tag{VII. 19}$$

Now $2^{n-1}$ can only be measured by the preceding terms of the series

$$1, 2, 2^2, \dots 2^{n-1}, \tag{IX. 13}$$

and $x$ is different from all of these ; therefore $x$ does not measure $2^{n-1}$, so that $S_n$ does not measure $m$. :just:`[VII. Def. 20] <VII.def.20>`

And $S_n$ is prime ; therefore it is prime to $m$. :just:`[VII. 29] <VII.29>`

It follows :just:`[VII. 20, 21]` that

$$m\text{ measures }2^{n-1}.$$

.. _folio-ii-0431:

.. folio:: 0431
   :page: 425

Suppose that $m = 2^r$.

Now, :term:`*ex aequali* <ex-aequali>`,

$$2^r : 2^{n-1} = S_n : 2^{n-r-1} S_n.$$

Therefore

$$\begin{aligned}
2^r \cdot 2^{n-r-1} S_n &= 2^{n-1} S_n \tag{VII. 19} \\
&= x \cdot m\text{, from above.}
\end{aligned}$$

And $m = 2^r$ ; therefore $x = 2^{n-r-1} S_n$, one of the terms of the series $S_n, 2S_n, 2^2 S_n, \dots 2^{n-2} S_n$ : which contradicts the hypothesis.

There $2^{n-1} S_n$ has no factors except

$$S_n, 2S_n, 2^2 S_n, \dots 2^{n-2} S_n, 1, 2, 2^2, \dots 2^{n-1}.$$

:person:`Theon of Smyrna <theon-of-smyrna>` and :person:`Nicomachus <nicomachus>` both define a “perfect” number and give the law of its formation. :person:`Nicomachus <nicomachus>` gives four perfect numbers and no more, namely $6$, $28$, $496$, $8128$. He says they are formed in “ordered” fashion, there being one among the units (i.e. less than $10$), one among the tens (less than $100$), one among the hundreds (less than $1000$) and one among the thousands (less than $10000$) ; he adds that they terminate in $6$ or $8$ alternately. They do all terminate in $6$ or $8$, as can easily be proved by means of the formula $(2^n - 1) 2^{n-1}$ (cf. :person:`Loria <loria>`, *Le scienze esatte nell’ antica Grecia*, pp. 840–1), but not alternately, for the fifth and sixth perfect numbers both end in $6$, and the seventh and eighth both end in $8$. :person:`Iamblichus <iamblichus>` adds a tentative suggestion that perhaps there may be, in like manner, one perfect number among the “first myriads” (less than $10000^2$), one among the “second myriads” (less than $10000^3$), and so on. This is, as we shall see, incorrect.

It is natural that the subject of perfect numbers should, ever since Euclid’s time, have had a fascination for mathematicians. :person:`Fermat <fermat>` ($1601\text{–}1655$), in a letter to Mersenne (*Œuvres de Fermat*, ed. :person:`Tannery <tannery>` and Henry, Vol. II., $1894$, pp. 197–9), enunciated three propositions which much facilitate the investigation whether a given number of the form $2^n - 1$ is prime or not. If we write in one line the exponents $1, 2, 3, 4$, etc. of the successive powers of $2$ and underneath them respectively the numbers representing the corresponding powers of $2$ diminished by $1$, thus,

.. list-table::
   :header-rows: 1

   * - $1$
     - $2$
     - $3$
     - $4$
     - $5$
     - $6$
     - $7$
     - $8$
     - $9$
     - $10$
     - $11$
     - $\dots n$
   * - $1$
     - $3$
     - $7$
     - $15$
     - $31$
     - $63$
     - $127$
     - $255$
     - $511$
     - $1023$
     - $2047$
     - $\dots 2^n - 1$,

the following relations are found to subsist between the numbers in the first line and those directly below them in the second line.

1. If the exponent is not a prime number, the corresponding number is not a prime number either (since $a^{pq} - 1$ is always divisible by $a^p - 1$ as well as by $a^q - 1$).

2. If the exponent is a prime number, the corresponding number diminished by $1$ is divisible by twice the exponent. [$(2^n - 2)/2n = (2^{n-1} - 1)/n$ ; so that this is a special case of “:person:`Fermat <fermat>`’s theorem” that, if $p$ is a prime number and $a$ is prime to $p$, then $a^{p-1}$ is divisible by $p$.]

3. If the exponent $n$ is a prime number, the corresponding number is only divisible by numbers of the form $(2mn + 1)$. If therefore the corresponding number in the second line has no factors of this form, it has no integral factor.

The first and third of these propositions are those which are specially useful for the purpose in question. As usual, :person:`Fermat <fermat>` does not give his proofs but merely adds : “Voilà trois fort belles propositions que j’ay trouvées et prouvées non sans peine. Je les puis appeller les fondements de l’invention des nombres parfaits.”

.. _folio-ii-0432:

.. folio:: 0432
   :page: 426

I append a few details of discoveries of further perfect numbers after the first four. The next are as follows :

.. list-table::

   * -
     -
   * - fifth,
     - $2^{12} (2^{13} - 1) = 33\ 550\ 336$
   * - sixth,
     - $2^{16} (2^{17} - 1) = 8\ 589\ 869\ 056$
   * - seventh,
     - $2^{18} (2^{19} - 1) = 137\ 438\ 691\ 328$
   * - eighth,
     - $2^{30} (2^{31} - 1) = 2\ 305\ 843\ 008\ 139\ 952\ 128$
   * - ninth,
     - $2^{60} (2^{61} - 1) = 2\ 658\ 455\ 991\ 569\ 831\ 744\ 654\ 692\ 615\ 953\ 842\ 176$
   * - tenth,
     - $2^{88} (2^{89} - 1)$.

It has further been proved that $2^{107} - 1$ is prime, and so is $2^{127} - 1$. Hence $2^{106} (2^{107} - 1)$ and $2^{126} (2^{127} - 1)$ are two more perfect numbers.

The fifth perfect number may have been known to :person:`Iamblichus <iamblichus>`, though he does not give it ; it was however known, with all its factors, in the fifteenth century, as appears from a tract written in German which was discovered by Curtze (Cod. lat. Monac. 14908). The first eight perfect numbers were calculated by Jean Prestet (d. 1670). :person:`Fermat <fermat>` had stated, and :person:`Euler <euler>` proved, that $2^{31} - 1$ is prime. The ninth perfect number was found by P. Seelhoff (*Zeitschrift für Math. u. Physik*, XXXI., 1886, pp. 174–8) and verified by E. Lucas (*Mathésis*, VII., 1887, pp. 45–6). The tenth was discovered by R. E. Powers (see *Bulletin of the American Mathematical Society*, XVIII., 1912, p. 162). $2^{107} - 1$ was proved to be prime by E. Fauquembergue and R. E. Powers (1914), while Fauquembergue proved that $2^{127} - 1$ is prime.

There have been attempts, so far unsuccessful, to solve the question whether there exist other “perfect numbers” than those of Euclid, and, in particular, perfect numbers which are odd. (Cf. several notes by Sylvester in *Comptes rendus*, CVI., 1888 ; Catalan, “Mélanges mathématiques” in *Mém. de la Soc. de Liége*, $2^{\text{e}}$ Série, xv., 1888, pp. 205–7 ; C. Servais in *Mathésis*, VII., pp. 228–30 and VIII., pp. 92–93, 135 ; E. Cesàro in *Mathésis*, VII., pp. 245–6 ; E. Lucas in *Mathésis*, X., pp. 74–6).

For the detailed history of the whole subject see L. E. Dickson, *History of the Theory of Numbers*, Vol. I., 1919, pp. iii–iv, 3–33.
