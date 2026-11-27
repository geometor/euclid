:canonical_id: X.91.commentary
:volume: III
:book: X
:proposition: 91
:type: commentary
:title: Commentary on Proposition X.91
:folios: 0197, 0198
:folio: 0197
:page: 193
:pages: 193, 194

.. _X.91.commentary:

Commentary on Proposition X.91
==============================

Back to :ref:`Proposition X.91 <X.91>`.

.. folio:: 0197
   :page: 193

This proposition corresponds to x. 54, and the problem solved in it is to find and to classify the side of a square equal to the rectangle contained by a :term:`*first apotome* <first-apotome>` and :math:`\rho`, or (algebraically) to find

.. math::

   \sqrt{\rho(k\rho - k\rho\sqrt{1-\lambda^2})}.

First find :math:`u, v` from the equations

.. math::

   \left.\begin{aligned}
   u + v &= k\rho \\
   uv &= \frac{1}{4}k^2\rho^2(1 - \lambda^2)
   \end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(1).

If :math:`u, v` represent the values so found, put

.. math::

   \left.\begin{aligned}
   x^2 &= \rho u \\
   y^2 &= \rho v
   \end{aligned}\right\} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(2),

and :math:`(x - y)` shall be the square root required.

To prove this Euclid argues thus.

By (1),

.. math::

   u : \frac{1}{2}k\rho\sqrt{1-\lambda^2} = \frac{1}{2}k\rho\sqrt{1-\lambda^2} : v,

whence

.. math::

   \rho u : \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} = \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} : \rho v,

or

.. math::

   x^2 : \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} = \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} : y^2.

But [Lemma after x. 53]

.. math::

   x^2 : xy = xy : y^2,

so that

.. math::

   xy = \frac{1}{2}k\rho^2\sqrt{1-\lambda^2} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(3).

.. _folio-iii-0198:

.. folio:: 0198
   :page: 194

Therefore

.. math::

   \begin{aligned}
   (x - y)^2 &= x^2 + y^2 - 2xy \\
   &= \rho(u + v) - k\rho^2\sqrt{1-\lambda^2} \\
   &= k\rho^2 - k\rho^2\sqrt{1-\lambda^2}.
   \end{aligned}

Thus :math:`(x - y)` is equal to :math:`\sqrt{\rho(k\rho - k\rho\sqrt{1-\lambda^2})}`.

It has next to be proved that :math:`(x - y)` is an apotome.

From (1) it follows, by x. 17, that

.. math::

   u \mathbin{\frown} v;

thus :math:`u, v` are both commensurable with :math:`(u + v)` and therefore with :math:`\rho \dots\dots(4)`.

Hence :math:`u, v` are both rational,
so that :math:`\rho u, \rho v` are rational areas;
therefore, by (2), :math:`x^2, y^2` are rational and commensurable :math:`\dots\dots\dots\dots\dots(5)`,
whence also :math:`x, y` are rational straight lines :math:`\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots(6)`.

Next, :math:`k\rho\sqrt{1-\lambda^2}` is rational and :math:`\mathbin{\smile} \rho`;
therefore :math:`\frac{1}{2}k\rho^2\sqrt{1-\lambda^2}` is a medial area.

That is, by (3), :math:`xy` is a medial area.

But [(5)] :math:`y^2` is a rational area;
therefore

.. math::

   xy \mathbin{\smile} y^2,

or

.. math::

   x \mathbin{\smile} y.

But [(6)] :math:`x, y` are both rational.
Therefore :math:`x, y` are rational and :math:`\sim`;
so that :math:`(x - y)` is an apotome.

To find the form of :math:`(x - y)` algebraically, we have, by solving (1),

.. math::

   \begin{aligned}
   u &= \frac{1}{2}k\rho(1 + \lambda), \\
   v &= \frac{1}{2}k\rho(1 - \lambda),
   \end{aligned}

whence, from (2),

.. math::

   \begin{aligned}
   x &= \rho\sqrt{\frac{k}{2}(1 + \lambda)}, \\
   y &= \rho\sqrt{\frac{k}{2}(1 - \lambda)},
   \end{aligned}

and

.. math::

   x - y = \rho\sqrt{\frac{k}{2}(1 + \lambda)} - \rho\sqrt{\frac{k}{2}(1 - \lambda)}.

As explained in the note on x. 54, :math:`(x - y)` is the lesser positive root of the biquadratic equation

.. math::

   x^4 - 2k\rho^2 \cdot x^2 + \lambda^2 k^2\rho^4 = 0.

