:canonical_id: X.59.commentary
:volume: III
:book: X
:proposition: 59
:type: commentary
:title: Commentary on Proposition X.59
:folios: 0135, 0136
:pages: 131, 132

.. _X.59.commentary:

Commentary on Proposition X.59
==============================

Back to :ref:`Proposition X.59 <X.59>`.

.. folio:: 0135
   :page: 131

Euclid here finds the square root of the expression [cf. X. 53]

$$\rho(\sqrt{k}\cdot\rho + \sqrt{\lambda}\cdot\rho).$$

As usual, we solve the equations

$$\left.\begin{aligned} u+v &= \sqrt{k}\cdot\rho \\ uv &= \frac{1}{4}\lambda\rho^2 \end{aligned}\right\}\quad\quad\quad\quad\dots\dots(1);$$

then, $u$, $v$ being found, we put

$$\left.\begin{aligned} x^2 &= \rho u \\ y^2 &= \rho v \end{aligned}\right\}\quad\quad\quad\quad\dots\dots(2),$$

and $(x+y)$ is the square root required.

Euclid proves that $(x+y)$ is the *side of (the sum of) two medial areas*, as follows.

As in the last two propositions, $x$, $y$ are proved to be incommensurable in square.

Now $\sqrt{k}\cdot\rho$, $\rho$ are commensurable in square only;
therefore $\rho(u+v)$, or $(x^2+y^2)$, is a medial area $\dots\dots(3).$

Next, $xy = \frac{1}{2}\sqrt{\lambda}\cdot\rho^2$, which is again a medial area $\dots\dots(4).$

Lastly,

$$\sqrt{k}\cdot\rho \smile \frac{1}{2}\sqrt{\lambda}\cdot\rho,$$

$$\sqrt{k}\cdot\rho^2 \smile \frac{1}{2}\sqrt{\lambda}\cdot\rho^2;$$

that is,

$$(x^2+y^2) \smile xy \dots\dots(5).$$

Hence [(3), (4), (5)] $(x+y)$ is the *side of the sum of two medial areas*.

Solving the equations algebraically, we have

$$\begin{aligned} u &= \frac{\rho}{2}(\sqrt{k} + \sqrt{k-\lambda}), \\ v &= \frac{\rho}{2}(\sqrt{k} - \sqrt{k-\lambda}), \end{aligned}$$

and

$$x+y = \rho\sqrt{\frac{1}{2}(\sqrt{k}+\sqrt{k-\lambda})} + \rho\sqrt{\frac{1}{2}(\sqrt{k}-\sqrt{k-\lambda})}.$$

The corresponding square root found in X. 96 is $x-y$, where $x$, $y$ are the same as here.

The two square roots are (cf. note on X. 53) the roots of the biquadratic equation

$$x^4 - 2\sqrt{k}\cdot\rho^2 x^2 + (k-\lambda)\rho^4 = 0.$$

----

[LEMMA.
~~~~~~~

.. enunciation::

   If a straight line be cut into unequal parts, the squares on the unequal parts are greater than twice the rectangle contained by the unequal parts.

.. picture:: 0135.g1.svg
   :alt: Lemma after Proposition 59

Let :g:`AB <0135.g1:/ A B />` be a straight line, and let it be cut into unequal parts at :g:`C <0135.g1:C>`, and let :g:`AC <0135.g1:/ A C />` be the greater ; I say that the squares on :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />` are greater than twice the rectangle :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />`.

.. _folio-iii-0136:

.. folio:: 0136
   :page: 132

For let :g:`AB <0135.g1:/ A B />` be :eq:`bisected <0135.g1:/ A D / = 0135.g1:/ D B />` at :g:`D <0135.g1:D>`.

.. subclause::

   Since then a straight line has been cut into :eq:`equal <0135.g1:/ A D / = 0135.g1:/ D B />` parts at :g:`D <0135.g1:D>`, and into unequal parts at :g:`C <0135.g1:C>`,

.. assertion::

   therefore the rectangle :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />` together with the square on :g:`CD <0135.g1:/ C D />` is equal to the square on :g:`AD <0135.g1:/ A D />`, :just:`[II. 5] <II.5>` so that the rectangle :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />` is less than the square on :g:`AD <0135.g1:/ A D />` ; therefore twice the rectangle :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />` is less than double of the square on :g:`AD <0135.g1:/ A D />`.

.. subclause::

   But the squares on :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />` are double of the squares on :g:`AD <0135.g1:/ A D />`, :g:`DC <0135.g1:/ D C />` ; :just:`[II. 9] <II.9>`

.. qed::

   therefore the squares on :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />` are greater than twice the rectangle :g:`AC <0135.g1:/ A C />`, :g:`CB <0135.g1:/ C B />`. :just:`Q. E. D.]`

We have already remarked (note on X. 44) that the Lemma here proving that

$$x^2 + y^2 > 2xy$$

can hardly be genuine, since the result is used in X. 44.
