:canonical_id: X.91.commentary
:volume: III
:book: X
:proposition: 91
:type: commentary
:title: Commentary on Proposition X.91
:folios: 0197, 0198
:pages: 193, 194

.. _X.91.commentary:

Commentary on Proposition X.91
==============================

Back to :ref:`Proposition X.91 <X.91>`.

.. folio:: 0197
   :page: 193

This proposition corresponds to x. 54, and the problem solved in it is to find and to classify the side of a square equal to the rectangle contained by a :term:`*first apotome* <first-apotome>` and $\rho$, or (algebraically) to find

$$\sqrt{\rho(k\rho - k\rho\sqrt{1-\lambda^2})}.$$

First find $u, v$ from the equations

$$\left.\begin{aligned}
u + v &= k\rho \\
uv &= \frac{1}{4}k^2\rho^2(1 - \lambda^2)
\end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(1).$$

If $u, v$ represent the values so found, put

$$\left.\begin{aligned}
x^2 &= \rho u \\
y^2 &= \rho v
\end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(2),$$

and $(x - y)$ shall be the square root required.

To prove this Euclid argues thus.

By (1),

$$u : \frac{1}{2}k\rho\sqrt{1-\lambda^2} = \frac{1}{2}k\rho\sqrt{1-\lambda^2} : v,$$

whence

$$\rho u : \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} = \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} : \rho v,$$

or

$$x^2 : \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} = \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} : y^2.$$

But [Lemma after x. 53]

$$x^2 : xy = xy : y^2,$$

so that

$$xy = \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(3).$$

.. _folio-iii-0198:

.. folio:: 0198
   :page: 194

Therefore

$$\begin{aligned}
(x - y)^2 &= x^2 + y^2 - 2xy \\
&= \rho(u + v) - k\rho^2\sqrt{1-\lambda^2} \\
&= k\rho^2 - k\rho^2\sqrt{1-\lambda^2}.
\end{aligned}$$

Thus $(x - y)$ is equal to $\sqrt{\rho(k\rho - k\rho\sqrt{1-\lambda^2})}$.

It has next to be proved that $(x - y)$ is an apotome.

From (1) it follows, by x. 17, that

$$u \mathbin{\frown} v;$$

thus $u, v$ are both commensurable with $(u + v)$ and therefore with $\rho \dots\dots(4)$.

Hence $u, v$ are both rational,
so that $\rho u, \rho v$ are rational areas;
therefore, by (2), $x^2, y^2$ are rational and commensurable $\dots\dots\dots\dots\dots(5)$,
whence also $x, y$ are rational straight lines $\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(6)$.

Next, $k\rho\sqrt{1-\lambda^2}$ is rational and $\mathbin{\smile} \rho$;
therefore $\frac{1}{2}k\rho^2\sqrt{1-\lambda^2}$ is a medial area.

That is, by (3), $xy$ is a medial area.

But [(5)] $y^2$ is a rational area;
therefore

$$xy \mathbin{\smile} y^2,$$

or

$$x \mathbin{\smile} y.$$

But [(6)] $x, y$ are both rational.
Therefore $x, y$ are rational and $\sim$;
so that $(x - y)$ is an apotome.

To find the form of $(x - y)$ algebraically, we have, by solving (1),

$$\begin{aligned}
u &= \frac{1}{2}k\rho(1 + \lambda), \\
v &= \frac{1}{2}k\rho(1 - \lambda),
\end{aligned}$$

whence, from (2),

$$\begin{aligned}
x &= \rho\sqrt{\frac{k}{2}(1 + \lambda)}, \\
y &= \rho\sqrt{\frac{k}{2}(1 - \lambda)},
\end{aligned}$$

and

$$x - y = \rho\sqrt{\frac{k}{2}(1 + \lambda)} - \rho\sqrt{\frac{k}{2}(1 - \lambda)}.$$

As explained in the note on x. 54, $(x - y)$ is the lesser positive root of the biquadratic equation

$$x^4 - 2k\rho^2 \cdot x^2 + \lambda^2 k^2\rho^4 = 0.$$
