:canonical_id: XII.2.commentary
:volume: III
:book: XII
:proposition: 2
:type: commentary
:title: Commentary on Proposition XII.2
:folios: 0378, 0379, 0380, 0381, 0382
:pages: 374, 375, 376, 377, 378

.. _XII.2.commentary:

Commentary on Proposition XII.2
===============================

Back to :ref:`Proposition XII.2 <XII.2>`.

.. folio:: 0378
   :page: 374

Though this theorem is said to have been proved by :person:`Hippocrates <hippocrates-of-chios>`, we may with tolerable certainty attribute the proof of it given by Euclid to :person:`Eudoxus <eudoxus>`, to whom XII. 7 Por. and XII. 10 (which Euclid proves in exactly the same manner) are specifically attributed by :person:`Archimedes <archimedes>`. As regards the lemma used herein (Eucl. X. 1) and the somewhat different lemma by means of which :person:`Archimedes <archimedes>` says that the theorems of XII. 2, XII. 7 Por. and XII. 18 were proved, see my note on X. 1 above.

The first essential in this proposition is to prove that we can *exhaust* a circle, in the sense of X. 1, by successively inscribing in it regular polygons, each of which has twice as many sides as the preceding one. We take first an inscribed square, then bisect the arcs subtended by the sides and so form an equilateral polygon of eight sides, then do the same with the latter, forming a polygon of 16 sides, and so on. And we have to prove that what is left over when any one of these polygons is taken away from the circle is *more than half exhausted* when the next polygon is made and subtracted from the circle.

Euclid proves that the inscribed square is greater than half the circle and that the regular octagon when subtracted takes away more than half of what was left by the square. He then infers that the same thing will happen whenever the number of sides is doubled.

This can be seen generally by taking *any* arc of a circle cut off by a chord :g:`AB <0378.g1:/ A B />`. :eq:`Bisect <0378.g1:/ A C / = 0378.g1:/ C B />` the arc in :g:`C <0378.g1:C>`. Draw a tangent to the circle at :g:`C <0378.g1:C>`, and let :g:`AD <0378.g1:/ A D />`, :g:`BE <0378.g1:/ B E />` be drawn perpendicular to the tangent. Join :g:`AC <0378.g1:/ A C />`, :g:`CB <0378.g1:/ C B />`. Then :g:`DE <0378.g1:/ D E />` is parallel to :g:`AB <0378.g1:/ A B />`, since $\angle$ :g:`ECB <0378.g1:< E C B )>` $= \angle$ :g:`CAB <0378.g1:< C A B )>`, in alternate segment, :just:`[III. 32] <III.32>` $= \angle$ :g:`CBA <0378.g1:< C B A )>`. :just:`[III. 29, I. 5] <III.29, I.5>` Thus :g:`ABED <0378.g1:< A B E D >>` is a $\square$; and it is greater than the segment :g:`ACB <0378.g1:( A C B )>`. Therefore its half, the $\triangle$ :g:`ACB <0378.g1:< A C B >>`, is greater than half the segment.

.. picture:: 0378.g1.svg
   :alt: Exhaustion of circular segment

Thus, by X. 1, Euclid's construction of successive regular polygons in a circle, if continued far enough, will at length leave segments which are together less than any given area.

Now let $X$, $X'$ be the areas of the circles, $d$, $d'$ their diameters, respectively. Then, if

$$X : X' \ne d^2 : {d'}^2,$$

$$d^2 : {d'}^2 = X : S,$$

where $S$ is some area either greater or less than $X'$.

**I.** Suppose $S < X'$. Continue the construction of polygons in $X'$ until we arrive at one which
leaves over segments together less than the excess of $X'$ over $S$, i.e. a polygon such that

.. _folio-iii-0379:

.. folio:: 0379
   :page: 375

$$X' > (\text{polygon in } X') > S.$$

Inscribe in the circle $X$ a polygon similar to that in $X'$. Then

$$(\text{polygon in } X) : (\text{polygon in } X') = d^2 : {d'}^2$$

:just:`[XII. 1] <XII.1>`

$$= X : S\text{, by hypothesis;}$$

and, alternately,

$$(\text{polygon in } X) : X = (\text{polygon in } X') : S.$$

But

$$(\text{polygon in } X) < X;$$

therefore

$$(\text{polygon in } X') < S.$$

But, by construction,

$$(\text{polygon in } X') > S:$$

which is impossible.

Hence $S$ cannot be *less* than $X'$ as supposed.

**II.** Suppose $S > X'$. Since

$$d^2 : {d'}^2 = X : S,$$

we have, inversely,

$${d'}^2 : d^2 = S : X.$$

Suppose that

$$S : X = X' : T,$$

whence, since $S > X'$,

$$X > T.$$

:just:`[v. 14]`
Consequently

$${d'}^2 : d^2 = X' : T,$$

where $T < X$.

This can be proved impossible in exactly the same way as shown in Part I. Hence $S$ cannot be *greater* than $X'$ as supposed. Since then $S$ is neither greater nor less than $X'$,

$$S = X',$$

and therefore

$$d^2 : {d'}^2 = X : X'.$$

With reference to the assumption that *there is some space $S$ such that*

$$d^2 : {d'}^2 = X : S,$$

i.e. that there is a fourth proportional to the areas $d^2$, ${d'}^2$, $X$, :person:`Simson <simson>` observes that it is sufficient, in this and the like cases, that a thing made use of in the reasoning can possibly *exist*, though it cannot be exhibited by a geometrical construction. As regards the assumption see note on v. 18 above.

There is grave reason for suspecting the genuineness of the Lemma at the end of the proposition; though, if it be rejected, it will be necessary to delete the words "as was before proved" in corresponding places in XII. 5, 18.

It will be observed that Euclid proves the impossibility in the second case by reducing it to the first. If it is desired to prove the second case independently, we must *circumscribe* successive polygons to the circles instead of inscribing them, in the way shown by :person:`Archimedes <archimedes>` in his first proposition on the *Measurement of a circle*. Of course we require, as a preliminary, the proposition corresponding to XII. 1, that

.. enunciation::

   Similar polygons circumscribed about circles are to one another as the squares on the diameters.

Let :g:`AB <0379.g1:/ A B />`, :g:`A'B' <0379.g1:/ A' B' />` be corresponding sides of the two similar polygons. Then $\angle\text{s}$ :g:`OAB <0379.g1:< O A B )>`, :g:`O'A'B' <0379.g1:< O' A' B' )>` are :eq:`equal <0379.g1:< O A B ) = 0379.g1:< O' A' B' )>`, since :g:`AO <0379.g1:/ A O />`, :g:`A'O' <0379.g1:/ A' O' />` bisect equal angles.

.. picture:: 0379.g1.svg
   :alt: Similar circumscribed polygons about two circles

.. _folio-iii-0380:

.. folio:: 0380
   :page: 376

Similarly $\angle$ :g:`ABO <0379.g1:< A B O )>` $= \angle$ :g:`A'B'O' <0379.g1:< A' B' O' )>`. Therefore $\triangle\text{s}$ :g:`AOB <0379.g1:< A O B >>`, :g:`A'O'B' <0379.g1:< A' O' B' >>` are similar, so that their areas are in the duplicate ratio of :g:`AB <0379.g1:/ A B />` to :g:`A'B' <0379.g1:/ A' B' />`. The radii :g:`OC <0379.g1:/ O C />`, :g:`O'C' <0379.g1:/ O' C' />` drawn to the points of contact are perpendicular to :g:`AB <0379.g1:/ A B />`, :g:`A'B' <0379.g1:/ A' B' />`, and it follows that

$$AB : A'B' = CO : C'O'.$$

Thus the polygons are to one another in the duplicate ratio of the radii, and therefore of the diameters.

Now suppose a square :g:`ABCD <0380.g1:< A B C D >>` described about a circle. Make an octagon described about the circle by drawing tangents at the points :g:`E <0380.g1:E>` etc., where :g:`OA <0380.g1:/ O A />` etc. meet the circle. Then shall the tangent at :g:`E <0380.g1:E>` cut off more than half of the area between :g:`AK <0380.g1:/ A K />`, :g:`AH <0380.g1:/ A H />` and the arc :g:`HEK <0380.g1:( H E K )>`. For the angle :g:`AEG <0380.g1:< A E G )>` is right, and is therefore $> \angle$ :g:`EAG <0380.g1:< E A G )>`.

.. picture:: 0380.g1.svg
   :alt: Circumscribed square and octagon about circle

'Therefore

$$\begin{aligned}
AG &> EG \\
&> GK.
\end{aligned}$$

Therefore

$$\triangle\text{">$AGE} > \triangle\text{">$EGK.}$$

Similarly

$$\triangle\text{">$AFE} > \triangle\text{">$EFH.}$$

Hence

$$\triangle\text{">$AFG} > \tfrac{1}{2}\text{ (re-entrant quadrilateral ">$AHEK),}$$

and :term:`*a fortiori* <a-fortiori>`,

$$\triangle\text{">$AFG} > \tfrac{1}{2}\text{ (area between AH, AK and the arc).}$$

Thus the octagon takes from the square more than half the space between the square and the circle. Similarly, if a figure of 16 equal sides be circumscribed by cutting off symmetrically the corners of the octagon, it will take away more than half of the space between the octagon and circle.

Suppose now, with the original notation, that

$$d^2 : {d'}^2 = X : S,$$

where $S$ is greater than $X'$.

Continue the construction of circumscribed polygons about $X'$ until the total area between the polygon and the circle is less than the difference between $S$ and $X'$, i.e. till

$$S > (\text{polygon about } X') > X'.$$

Circumscribe a similar polygon about $X$. Then

$$(\text{polygon about } X) : (\text{polygon about } X') = d^2 : {d'}^2$$

$$= X : S\text{, by hypothesis,}$$

and, alternately,

$$(\text{polygon about } X) : X = (\text{polygon about } X') : S.$$

But

$$(\text{polygon about } X) > X.$$

Therefore

$$(\text{polygon about } X') > S.$$

But

$$S > (\text{polygon about } X'):$$

:just:`[above]`
which is impossible.

Hence $S$ cannot be *greater* than $X'$.

.. _folio-iii-0381:

.. folio:: 0381
   :page: 377

:person:`Legendre <legendre>` proves this proposition by a method equally rigorous but not, I think, possessing any advantages over Euclid's. It depends on a lemma corresponding to Eucl. XII. 16, but with another part added to it.

.. enunciation::

   Two concentric circles being given, we can always inscribe in the greater a regular polygon such that its sides do not meet the circumference of the lesser, and we can also circumscribe about the lesser a regular polygon such that its sides do not meet the circumference of the greater.

Let :g:`CA <0381.g1:/ C A />`, :g:`CB <0381.g1:/ C B />` be the radii of the circles.

**I.** At :g:`A <0381.g1:A>` on the inner circle draw the tangent :g:`DE <0381.g1:/ D E />` meeting the outer circle in :g:`D <0381.g1:D>`, :g:`E <0381.g1:E>`. Inscribe in the outer circle any of the regular polygons which we can inscribe, e.g. a square. Bisect the arc subtended by a side, bisect the half, bisect that again, and so on, until we arrive at an arc less than the arc :g:`DBE <0381.g1:( D B E )>`. Let this arc be :g:`MN <0381.g1:( M N )>`, and suppose it so placed that :g:`B <0381.g1:B>` is its middle point. Then the chord :g:`MN <0381.g1:/ M N />` is clearly more distant from the centre :g:`C <0381.g1:C>` than :g:`DE <0381.g1:/ D E />` is; and the regular polygon, of which :g:`MN <0381.g1:/ M N />` is a side, does not anywhere meet the circumference of the inner circle.

.. picture:: 0381.g1.svg
   :alt: Concentric circles and tangent DE

**II.** Join :g:`CM <0381.g1:/ C M />`, :g:`CN <0381.g1:/ C N />`, meeting :g:`DE <0381.g1:/ D E />` in :g:`P <0381.g1:P>`, :g:`Q <0381.g1:Q>`. Then :g:`PQ <0381.g1:/ P Q />` will be the side of a polygon circumscribed about the inner circle and similar to the polygon inscribed in the outer; and the circumscribed polygon of which :g:`PQ <0381.g1:/ P Q />` is a side will not anywhere meet the outer circle.

:person:`Legendre <legendre>` now proves XII. 2 after the following manner. For brevity, let us denote the area of the circle with radius :g:`CA <0381.g2:/ C A />` by $(\text{circ. }$ :g:`CA <0381.g2:( C A )>` $)$. Then it is required to prove that, if :g:`OB <0381.g2:/ O B />` be the radius of a second circle, $(\text{circ. }$ :g:`CA <0381.g2:( C A )>` $) : (\text{circ. }$ :g:`OB <0381.g2:( O B )>` $) =$ :g:`CA^2 <0381.g2:/ C A />` $:$ :g:`OB^2 <0381.g2:/ O B />`.

.. picture:: 0381.g2.svg
   :alt: Legendre's two circles

Suppose, if possible, that this relation is not true. Then :g:`CA^2 <0381.g2:/ C A />` will be to :g:`OB^2 <0381.g2:/ O B />` as $(\text{circ. }$ :g:`CA <0381.g2:( C A )>` $)$ is to an area greater or less than $(\text{circ. }$ :g:`OB <0381.g2:( O B )>`)$. **I.** Suppose, first, that :g:`CA^2 <0381.g2:/ C A />` $:$ :g:`OB^2 <0381.g2:/ O B />` $= (\text{circ. }$ :g:`CA <0381.g2:( C A )>` $) : (\text{circ. }$ :g:`OD <0381.g2:( O D )>` $)$, where :g:`OD <0381.g2:/ O D />` is less than :g:`OB <0381.g2:/ O B />`.

.. _folio-iii-0382:

.. folio:: 0382
   :page: 378

Inscribe in the circle with radius :g:`OB <0381.g2:/ O B />` a regular polygon such that its sides do not anywhere meet the circumference of the circle with centre :g:`OD <0381.g2:/ O D />`; :just:`[Lemma]` and inscribe a similar polygon in the other circle. The areas of the polygons will then be in the duplicate ratio of :g:`CA <0381.g2:/ C A />` to :g:`OB <0381.g2:/ O B />`, or :just:`[XII. 1] <XII.1>` $(\text{polygon in circ. }$ :g:`CA <0381.g2:( C A )>` $) : (\text{polygon in circ. }$ :g:`OB <0381.g2:( O B )>` $)$ $=$ :g:`CA^2 <0381.g2:/ C A />` $:$ :g:`OB^2 <0381.g2:/ O B />` $= (\text{circ. }$ :g:`CA <0381.g2:( C A )>` $) : (\text{circ. }$ :g:`OD <0381.g2:( O D )>` $)$, by hypothesis.

But this is impossible, because the polygon in $(\text{circ. }$ :g:`CA <0381.g2:( C A )>` $)$ is less than $(\text{circ. }$ :g:`CA <0381.g2:( C A )>` $)$, but the polygon in $(\text{circ. }$ :g:`OB <0381.g2:( O B )>` $)$ is *greater* than $(\text{circ. }$ :g:`OD <0381.g2:( O D )>`)$. 'Therefore :g:`CA^2 <0381.g2:/ C A />` cannot be to :g:`OB^2 <0381.g2:/ O B />` as $(\text{circ. }$ :g:`CA <0381.g2:( C A )>` $)$ is to a *less* circle than $(\text{circ. }$ :g:`OB <0381.g2:( O B )>` $)$.

**II.** Suppose, if possible, that :g:`CA^2 <0381.g2:/ C A />` $:$ :g:`OB^2 <0381.g2:/ O B />` $= (\text{circ. }$ :g:`CA <0381.g2:( C A )>` $) : (\text{some circle} > \text{circ. }$ :g:`OB <0381.g2:( O B )>`)$. Then inversely :g:`OB^2 <0381.g2:/ O B />` $:$ :g:`CA^2 <0381.g2:/ C A />` $= (\text{circ. }$ :g:`OB <0381.g2:( O B )>` $) : (\text{some circle} < \text{circ. }$ :g:`CA <0381.g2:( C A )>` $), and this is proved impossible exactly as in Part I. Therefore :g:`CA^2 <0381.g2:/ C A />` $:$ :g:`OB^2 <0381.g2:/ O B />` $= (\text{circ. }$ :g:`CA <0381.g2:( C A )>` $) : (\text{circ. }$ :g:`OB <0381.g2:( O B )>` $)$.
