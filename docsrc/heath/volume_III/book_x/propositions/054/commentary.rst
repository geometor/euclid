:canonical_id: X.54.commentary
:volume: III
:book: X
:proposition: 54
:type: commentary
:title: Commentary on Proposition X.54
:folios: 0123, 0124
:folio: 0123
:page: 119
:pages: 119, 120

.. _X.54.commentary:

Commentary on Proposition X.54
==============================

Back to :ref:`Proposition X.54 <X.54>`.

.. folio:: 0123
   :page: 119

A :term:`*first binomial* <first-binomial>` straight line being, as we have seen in x. 48, of the form

.. math::

   k\rho + k\rho\sqrt{1 - \lambda^2},

the problem solved in this proposition is the equivalent of *finding the square root of this expression multiplied by* :math:`\rho`, *or of*

.. math::

   \rho(k\rho + k\rho\sqrt{1 - \lambda^2}),

and of proving that the said square root represents a *binomial* straight line as defined in x. 36.

The geometrical method corresponds sufficiently closely to the algebraical one which we should use.

First solve the equations

.. math::

   \left. \begin{aligned} u + v &= k\rho \\ uv &= \frac{1}{4}k^2\rho^2(1 - \lambda^2) \end{aligned} \right\} \ldots\ldots\ldots\ldots\ldots\ldots(1).

Then, if :math:`u`, :math:`v` represent the straight lines so found, put

.. math::

   \left. \begin{aligned} x^2 &= \rho u \\ y^2 &= \rho v \end{aligned} \right\} \ldots\ldots\ldots\ldots\ldots\ldots(2);

and the straight line :math:`(x + y)` is the square root required.

The actual algebraical solution of (1) gives

.. math::

   u - v = k\rho \cdot \lambda,

so that

.. math::

   \begin{aligned} u &= \frac{1}{2}k\rho(1 + \lambda), \\ v &= \frac{1}{2}k\rho(1 - \lambda), \end{aligned}

and therefore

.. math::

   \begin{aligned} x &= \rho \sqrt{\frac{k}{2}(1 + \lambda)}, \\ y &= \rho \sqrt{\frac{k}{2}(1 - \lambda)}, \end{aligned}

and

.. math::

   x + y = \rho \sqrt{\frac{k}{2}(1 + \lambda)} + \rho \sqrt{\frac{k}{2}(1 - \lambda)}.

This is clearly a binomial straight line as defined in x. 36.

Since Euclid has to express his results by straight lines in his figure, and has no symbols to make the result obvious by inspection, he is obliged to prove (1) that :math:`(x + y)` is the square root of :math:`\rho(k\rho + k\rho\sqrt{1 - \lambda^2})`, and (2) that :math:`(x + y)` is a binomial straight line, in the following manner.

First, he proves, by means of the preceding Lemma, that

.. math::

   xy = \frac{k}{2}\rho^2\sqrt{1 - \lambda^2} \ldots\ldots\ldots\ldots\ldots\ldots(3);

therefore

.. math::

   \begin{aligned} (x + y)^2 &= x^2 + y^2 + 2xy \\ &= \rho(u + v) + 2xy \\ &= k\rho^2 + k\rho^2\sqrt{1 - \lambda^2}\text{, by (1) and (3),} \end{aligned}

so that

.. math::

   x + y = \sqrt{\rho(k\rho + k\rho\sqrt{1 - \lambda^2})}.

.. _folio-iii-0124:

.. folio:: 0124
   :page: 120

Secondly, it results from (1), [by x. 17], that

.. math::

   u \sim v,

so that :math:`u`, :math:`v` are both :math:`\cap (u + v)`, and therefore :math:`\cap \rho \ldots\ldots\ldots\ldots\ldots\ldots(4);` thus :math:`u`, :math:`v` are rational, whence :math:`\rho u`, :math:`\rho v` are both rational, and

.. math::

   \rho u \cap \rho v.

Therefore :math:`x^2`, :math:`y^2` are rational and commensurable :math:`\ldots\ldots\ldots\ldots\ldots\ldots(5).` Next, :math:`k\rho \cup k\rho\sqrt{1 - \lambda^2},` and :math:`k\rho \cap u`, while :math:`k\rho\sqrt{1 - \lambda^2} \cap \frac{1}{2}k\rho\sqrt{1 - \lambda^2};` therefore

.. math::

   u \cup \frac{1}{2}k\rho\sqrt{1 - \lambda^2},

whence

.. math::

   \rho u \cup \frac{1}{2}k\rho^2\sqrt{1 - \lambda^2},

or

.. math::

   x^2 \cup xy,

so that

.. math::

   x \cup y.

By this and (5), :math:`x`, :math:`y` are rational and :math:`\sim`, so that :math:`(x + y)` is a binomial straight line. :just:`[X. 36] <X.36>`

x. 91 will prove in like manner that a like theorem holds for *apotomes*, viz. that

.. math::

   \rho\sqrt{\frac{k}{2}(1 + \lambda)} - \rho\sqrt{\frac{k}{2}(1 - \lambda)} = \sqrt{\rho(k\rho - k\rho\sqrt{1 - \lambda^2})}.

Since the :term:`*first binomial* <first-binomial>` straight line and the :term:`*first apotome* <first-apotome>` are the roots of the equation

.. math::

   x^2 - 2k\rho \cdot x + \lambda^2 k^2 \rho^2 = 0,

this proposition and x. 91 give us the solution of the biquadratic equation

.. math::

   x^4 - 2k\rho^2 \cdot x^2 + \lambda^2 k^2 \rho^4 = 0.

