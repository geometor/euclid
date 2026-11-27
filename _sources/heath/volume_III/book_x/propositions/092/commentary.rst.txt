:canonical_id: X.92.commentary
:volume: III
:book: X
:proposition: 92
:type: commentary
:title: Commentary on Proposition X.92
:folios: 0201, 0202
:folio: 0201
:page: 197
:pages: 197, 198

.. _X.92.commentary:

Commentary on Proposition X.92
==============================

Back to :ref:`Proposition X.92 <X.92>`.

.. folio:: 0201
   :page: 197

There is an evident flaw in the text in the place (:person:`Heiberg <heiberg>`, p. 282, ll. 17—20: translation p. 196 above) where it is said that "since then :g:`AI <0199.g1:< A I >>`, :g:`FK <0199.g1:< F K >>` are medial and are equal to the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />`, the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are also medial; *therefore :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are also medial straight lines commensurable in square only.*" It is not till the last lines of the proposition (:person:`Heiberg <heiberg>`, p. 284, ll. 17, 18) that it is proved that :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are :term:`*incommensurable in length* <incommensurable-in-length>`. What should have been proved in the former passage is that the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are commensurable, so that :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are commensurable in square (not commensurable in square *only*). I have supplied the step in the note below: "Also :math:`x^2 \mathbin{\frown} y^2`, since :math:`u \mathbin{\frown} v`." :person:`Theon <theon-of-alexandria>` seems to have observed the omission and to have put "and commensurable with one another" after "medial" in the passage quoted, though even this does not show *why* the squares on :g:`LP <0199.g1:/ L P />`, :g:`PN <0199.g1:/ P N />` are commensurable. One MS. (V) also has "only" (:math:`\mu\acute{o}\nu\omicron\nu`) erased after "commensurable in square."

----

This proposition amounts to finding and classifying

.. math::

   \sqrt{\rho\left(\frac{k\rho}{\sqrt{1-\lambda^2}} - k\rho\right)}.

The method is that of the last proposition. Euclid solves, first, the equations

.. math::

   \left.\begin{aligned}
   u + v &= \frac{k\rho}{\sqrt{1-\lambda^2}} \\
   uv &= \frac{1}{4}k^2\rho^2
   \end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(1).

.. _folio-iii-0202:

.. folio:: 0202
   :page: 198

Then, using the values of :math:`u, v` so found, he puts

.. math::

   \left.\begin{aligned}
   x^2 &= \rho u \\
   y^2 &= \rho v
   \end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(2),

and :math:`(x - y)` is the square root required.

That

.. math::

   (x - y) = \sqrt{\rho\left(\frac{k\rho}{\sqrt{1-\lambda^2}} - k\rho\right)}

is proved in the same way as is the corresponding fact in x. 91.

From (1)

.. math::

   u : \frac{1}{2}k\rho = \frac{1}{2}k\rho : v,

so that

.. math::

   \rho u : \frac{1}{2}k\rho^2 = \frac{1}{2}k\rho^2 : \rho v.

But

.. math::

   x^2 : xy = xy : y^2,

whence, by (2),

.. math::

   xy = \frac{1}{2}k\rho^2 \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(3).

Therefore

.. math::

   \begin{aligned}
   (x - y)^2 &= x^2 + y^2 - 2xy \\
   &= \rho(u + v) - k\rho^2 \\
   &= \rho\left(\frac{k\rho}{\sqrt{1-\lambda^2}} - k\rho\right).
   \end{aligned}

Next, we have to prove that :math:`(x - y)` is a *first apotome of a medial straight line*.

From (1) it follows, by x. 17, that

.. math::

   u \mathbin{\frown} v, \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(4),

therefore :math:`u, v` are both :math:`\mathbin{\frown} (u + v)`.

But [(1)] :math:`(u + v)` is rational and :math:`\mathbin{\smile} \rho`; therefore :math:`u, v` are both rational and :math:`\mathbin{\smile} \rho \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(5)`.

Therefore :math:`\rho u, \rho v`, or :math:`x^2, y^2`, are both *medial* areas, and :math:`x, y` are medial straight lines :math:`\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(6)`.

Also :math:`x^2 \mathbin{\frown} y^2`, since :math:`u \mathbin{\frown} v` [(4)] :math:`\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(7)`.

Now :math:`xy`, or :math:`\frac{1}{2}k\rho^2`, is a rational area; therefore

.. math::

   xy \mathbin{\smile} y^2,

and

.. math::

   x \mathbin{\smile} y.

Hence [(6), (7), (3)] :math:`x, y` are medial straight lines commensurable in square only and containing a rational rectangle; therefore :math:`(x - y)` is a :term:`*first apotome of a medial straight line* <first-apotome-of-a-medial-straight-line>`.

Algebraical solution of the equations gives

.. math::

   \begin{aligned}
   u &= \frac{1}{2}\frac{1+\lambda}{\sqrt{1-\lambda^2}}k\rho, \\
   v &= \frac{1}{2}\frac{1-\lambda}{\sqrt{1-\lambda^2}}k\rho,
   \end{aligned}

and

.. math::

   x - y = \rho\sqrt{\frac{k}{2}\left(\frac{1+\lambda}{1-\lambda}\right)^{\frac{1}{2}}} - \rho\sqrt{\frac{k}{2}\left(\frac{1-\lambda}{1+\lambda}\right)^{\frac{1}{2}}}.

As explained in the note on x. 55, this is the lesser positive root of the equation

.. math::

   x^4 - \frac{2k\rho^2}{\sqrt{1-\lambda^2}}x^2 + \frac{\lambda^2}{1-\lambda^2}k^2\rho^4 = 0.

