:canonical_id: X.113.commentary
:volume: III
:book: X
:proposition: 113
:type: commentary
:title: Commentary on Proposition X.113
:folios: 0254, 0255, 0256
:folio: 0254
:page: 250
:pages: 250, 251, 252

.. _X.113.commentary:

Commentary on Proposition X.113
===============================

Back to :ref:`Proposition X.113 <X.113>`.

.. folio:: 0254
   :page: 250

This proposition, which is companion to the preceding, gives us the equivalent of the rationalisation of the denominator of

.. math::

   \frac{c^2}{\sqrt A - \sqrt B} \quad\text{or}\quad \frac{c^2}{a \sim \sqrt B}.

.. _folio-iii-0255:

.. folio:: 0255
   :page: 251

Euclid (or the writer) proves that

.. math::

   \frac{\sigma^2}{\rho - \sqrt k \cdot \rho} = \lambda\rho + \lambda\sqrt k \cdot \rho, \qquad (k < 1)

and his method enables us to see that :math:`\lambda = \sigma^2/(\rho^2 - k\rho^2)`.

Let

.. math::

   \frac{\sigma^2}{\rho - \sqrt k \cdot \rho} = u;

and it is proved that :math:`u` is the binomial straight line :math:`(u - w) + w`, where :math:`w` is determined as shown below.

.. math::

   \left.\begin{aligned}
   u\, (\rho - \sqrt k \cdot \rho) &= \sigma^2 = \rho x\text{, say,} \\
   \text{whence}\quad \rho : (\rho - \sqrt k \cdot \rho) &= u : x
   \end{aligned}\right\}\dots\dots\dots\dots\dots\dots(1),

so that :math:`x < u`.

Let then

.. math::

   x = u - v.

Since :math:`(u - v)\,\rho = \sigma^2`, a rational area,

.. math::

   (u - v) \text{ is rational and } \mathbin{\cap} \rho \dots\dots\dots\dots\dots\dots(2).

And [(1)]

.. math::

   \rho : (\rho - \sqrt k \cdot \rho) = u : (u - v),

so that, :term:`*convertendo* <convertendo>`,

.. math::

   \rho : \sqrt k \cdot \rho = u : v.

Suppose that

.. math::

   u : v = w : (v - w),

so that [V. 19]

.. math::

   (u - w) : w = u : v = w : (v - w).

Thus, :math:`w` being a mean proportional between :math:`(u - w)`, :math:`(v - w)`,

.. math::

   (u - w)^2 : w^2 = (u - w) : (v - w).

But

.. math::

   \begin{aligned}
   (u - w)^2 : w^2 &= u^2 : v^2 \\
   &= \rho^2 : k\rho^2 \dots\dots\dots\dots\dots\dots(3),
   \end{aligned}

so that :math:`(u - w)^2 \mathbin{\cap} u^2.`

Therefore

.. math::

   \begin{aligned}
   (u - w) &\mathbin{\cap} (v - w) \\
   &\mathbin{\cap} \{(u - w) - (v - w)\} \\
   &\mathbin{\cap} (u - v).
   \end{aligned}

Therefore [(2)] :math:`(u - w)` is rational and :math:`\mathbin{\cap} \rho \dots\dots\dots\dots\dots\dots(4).`

And, since

.. math::

   \rho : \sqrt k \cdot \rho = (u - w) : w,

:math:`w` is rational and :math:`\mathbin{\cap} \sqrt k \cdot \rho \dots\dots\dots\dots\dots\dots(5).`

Hence [(4), (5)] :math:`(u - w)`, :math:`w` are rational and :math:`\mathbin{\sim}`,
so that :math:`(u - w) + w` is a binomial straight line.

Now either

.. math::

   \begin{aligned}
   \text{(I)} &\quad \sqrt{\rho^2 - k\rho^2} \mathbin{\cap} \rho, \\
   \text{or (II)} &\quad \sqrt{\rho^2 - k\rho^2} \mathbin{\cup} \rho.
   \end{aligned}

In case (I)

.. math::

   \sqrt{(u - w)^2 - w^2} \mathbin{\cap} (u - w),

and in case (II)

.. math::

   \sqrt{(u - w)^2 - w^2} \mathbin{\cup} (u - w). \qquad \text{[(3) and X. 14]}

And, if :math:`\rho \mathbin{\cap} \sigma`, :math:`(u - w) \mathbin{\cap} \sigma`; [(4)]
if :math:`\sqrt k \cdot \rho \mathbin{\cap} \sigma`, :math:`w \mathbin{\cap} \sigma`; [5]
while, if neither :math:`\rho` nor :math:`\sqrt k \cdot \rho` is :math:`\mathbin{\cap} \sigma`, neither :math:`(u - w)` nor :math:`w` is :math:`\mathbin{\cap} \sigma`.

Hence :math:`(u - w) + w` is a binomial straight line of the same order as the apotome :math:`\rho - \sqrt k \cdot \rho`, its terms are proportional to those of the apotome [(3)], and commensurable with them respectively [(4), (5)].

.. _folio-iii-0256:

.. folio:: 0256
   :page: 252

To find :math:`(u - w)`, :math:`w` algebraically we have

.. math::

   u = \frac{\sigma^2}{\rho - \sqrt{k} \cdot \rho},

.. math::

   \frac{u - w}{w} = \frac{\rho}{\sqrt{k} \cdot \rho}.

From the latter

.. math::

   \begin{aligned}
   w &= \frac{u \cdot \sqrt{k} \cdot \rho}{\rho + \sqrt{k} \cdot \rho} \\
   &= \frac{\sigma^2 \cdot \sqrt{k} \cdot \rho}{\rho^2 - k\rho^2}.
   \end{aligned}

Thus

.. math::

   u - w = w \cdot \frac{1}{\sqrt{k}} = \frac{\sigma^2\rho}{\rho^2 - k\rho^2}.

Therefore

.. math::

   (u - w) + w = \sigma^2 \cdot \frac{\rho + \sqrt{k} \cdot \rho}{\rho^2 - k\rho^2}.

