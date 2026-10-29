:canonical_id: X.92.commentary
:volume: III
:book: X
:proposition: 92
:type: commentary
:title: Commentary on Proposition X.92
:folios: 0201, 0202
:pages: 197, 198

.. _X.92.commentary:

Commentary on Proposition X.92
==============================

Back to :ref:`Proposition X.92 <X.92>`.

.. folio:: 0201
   :page: 197

There is an evident flaw in the text in the place (:person:`Heiberg <heiberg>`, p. 282, ll. 17—20: translation p. 196 above) where it is said that "since then :g:`AI <0199.g1:< A I >>`, :g:`FK <0199.g1:< F K >>` are medial and are equal to the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />`, the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are also medial; *therefore :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are also medial straight lines commensurable in square only.*" It is not till the last lines of the proposition (:person:`Heiberg <heiberg>`, p. 284, ll. 17, 18) that it is proved that :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are :term:`*incommensurable in length* <incommensurable-in-length>`. What should have been proved in the former passage is that the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are commensurable, so that :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are commensurable in square (not commensurable in square *only*). I have supplied the step in the note below: "Also $x^2 \mathbin{\frown} y^2$, since $u \mathbin{\frown} v$." :person:`Theon <theon-of-alexandria>` seems to have observed the omission and to have put "and commensurable with one another" after "medial" in the passage quoted, though even this does not show *why* the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are commensurable. One MS. (V) also has "only" ($\mu\acute{o}\nu\omicron\nu$) erased after "commensurable in square."

----

This proposition amounts to finding and classifying

$$\sqrt{\rho\left(\frac{k\rho}{\sqrt{1-\lambda^2}} - k\rho\right)}.$$

The method is that of the last proposition. Euclid solves, first, the equations

$$\left.\begin{aligned}
u + v &= \frac{k\rho}{\sqrt{1-\lambda^2}} \\
uv &= \frac{1}{4}k^2\rho^2
\end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(1).$$

.. _folio-iii-0202:

.. folio:: 0202
   :page: 198

Then, using the values of $u, v$ so found, he puts

$$\left.\begin{aligned}
x^2 &= \rho u \\
y^2 &= \rho v
\end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(2),$$

and $(x - y)$ is the square root required.

That

$$(x - y) = \sqrt{\rho\left(\frac{k\rho}{\sqrt{1-\lambda^2}} - k\rho\right)}$$

is proved in the same way as is the corresponding fact in x. 91.

From (1)

$$u : \frac{1}{2}k\rho = \frac{1}{2}k\rho : v,$$

so that

$$\rho u : \frac{1}{2}k\rho^2 = \frac{1}{2}k\rho^2 : \rho v.$$

But

$$x^2 : xy = xy : y^2,$$

whence, by (2),

$$xy = \frac{1}{2}k\rho^2 \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(3).$$

Therefore

$$\begin{aligned}
(x - y)^2 &= x^2 + y^2 - 2xy \\
&= \rho(u + v) - k\rho^2 \\
&= \rho\left(\frac{k\rho}{\sqrt{1-\lambda^2}} - k\rho\right).
\end{aligned}$$

Next, we have to prove that $(x - y)$ is a *first apotome of a medial straight line*.

From (1) it follows, by x. 17, that

$$u \mathbin{\frown} v, \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(4),$$

therefore $u, v$ are both $\mathbin{\frown} (u + v)$.

But [(1)] $(u + v)$ is rational and $\mathbin{\smile} \rho$; therefore $u, v$ are both rational and $\mathbin{\smile} \rho \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(5)$.

Therefore $\rho u, \rho v$, or $x^2, y^2$, are both *medial* areas, and $x, y$ are medial straight lines $\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(6)$.

Also $x^2 \mathbin{\frown} y^2$, since $u \mathbin{\frown} v$ [(4)] $\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(7)$.

Now $xy$, or $\frac{1}{2}k\rho^2$, is a rational area; therefore

$$xy \mathbin{\smile} y^2,$$

and

$$x \mathbin{\smile} y.$$

Hence [(6), (7), (3)] $x, y$ are medial straight lines commensurable in square only and containing a rational rectangle; therefore $(x - y)$ is a :term:`*first apotome of a medial straight line* <first-apotome-of-a-medial-straight-line>`.

Algebraical solution of the equations gives

$$\begin{aligned}
u &= \frac{1}{2}\frac{1+\lambda}{\sqrt{1-\lambda^2}}k\rho, \\
v &= \frac{1}{2}\frac{1-\lambda}{\sqrt{1-\lambda^2}}k\rho,
\end{aligned}$$

and

$$x - y = \rho\sqrt{\frac{k}{2}\left(\frac{1+\lambda}{1-\lambda}\right)^{\frac{1}{2}}} - \rho\sqrt{\frac{k}{2}\left(\frac{1-\lambda}{1+\lambda}\right)^{\frac{1}{2}}}.$$

As explained in the note on x. 55, this is the lesser positive root of the equation

$$x^4 - \frac{2k\rho^2}{\sqrt{1-\lambda^2}}x^2 + \frac{\lambda^2}{1-\lambda^2}k^2\rho^4 = 0.$$
