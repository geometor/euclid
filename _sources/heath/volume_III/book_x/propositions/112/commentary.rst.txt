:canonical_id: X.112.commentary
:volume: III
:book: X
:proposition: 112
:type: commentary
:title: Commentary on Proposition X.112
:folios: 0250, 0251, 0252
:folio: 0250
:page: 246
:pages: 246, 247, 248

.. _X.112.commentary:

Commentary on Proposition X.112
===============================

Back to :ref:`Proposition X.112 <X.112>`.

.. folio:: 0250
   :page: 246

:person:`Heiberg <heiberg>` considers that this proposition and the succeeding ones are interpolated, though the interpolation must have taken place before :person:`Theon <theon-of-alexandria>`'s time. His argument is that X. 112—115 are nowhere used, but that X. 111 rounds off the complete discussion of the 13 irrationals (as indicated in the recapitulation), thereby giving what was necessary for use in connexion with the investigation of the five regular solids. For besides X. 73 (used in XIII. 6, 11) X. 94 and 97 are used in XIII. 11, 6 respectively; and Euclid could not have stopped at X. 97 without leaving the discussion of irrationals imperfect, for X. 98—102 are closely connected with X. 97, and X. 103—111 add, as it were, the coping-stone to the whole doctrine. On the other hand, X. 112—115 are not connected with the rest of the treatise on the 13 irrationals and are not used in the stereometric books. They are rather the germ of a new study and a more abstruse investigation of irrationals *in themselves*. Prop. 115 in particular extends the number of the different kinds of irrationals. As however X. 112—115 are old and serviceable theorems, :person:`Heiberg <heiberg>` thinks that, though Euclid did not give them, they may have been taken from :person:`Apollonius <apollonius>`.

I will only point out what seems to me open to doubt in the above, namely that X. 112—114 (excluding 115) are not connected with the rest of the exposition of the 13 irrationals. It seems to me that they *are* so connected. X. 111 has shown us that a *binomial straight line cannot also be an apotome*. But X. 112—114 show us *how either of them can be used to rationalise the other*, thus giving what is surely an important relation between them.

X. 112 is the equivalent of rationalising the denominators of the fractions

.. math::

   \frac{c^2}{\sqrt A + \sqrt B},\quad \frac{c^2}{a + \sqrt B},

by multiplying numerator and denominator by :math:`\sqrt A - \sqrt B` and :math:`a - \sqrt B` respectively.

Euclid proves that

.. math::

   \frac{\sigma^2}{\rho + \sqrt k \cdot \rho} = \lambda\rho - \sqrt k \cdot \lambda\rho \quad (k < 1),

and his method enables us to see that :math:`\lambda = \sigma^2/(\rho^2 - k\rho^2)`.

The proof is a remarkable instance of the dexterity of the Greeks in using geometry as the equivalent of our algebra. Like so many proofs in :person:`Archimedes <archimedes>` and :person:`Apollonius <apollonius>`, it leaves us completely in the dark as to how it was evolved. That the Greeks must have had some analytical method which suggested the steps of such proofs seems certain; but *what* it was must remain apparently an insoluble mystery.

I will reproduce by means of algebraical symbols the exact course of Euclid's proof.

He has to prove that :math:`\frac{\sigma^2}{\rho + \sqrt k \cdot \rho}` is an apotome related in a certain way to
the binomial straight line :math:`\rho + \sqrt k \cdot \rho`. If :math:`u` be the straight line required, :math:`(u + w) - w` is shown to be an apotome of the kind described, where :math:`w` is determined in the following manner.

.. _folio-iii-0251:

.. folio:: 0251
   :page: 247

We have

.. math::

   \left.\begin{aligned}
   (\rho + \sqrt k \cdot \rho)\, u &= \sigma^2 = \sqrt k \cdot \rho \cdot x\text{, say,} \\
   \text{whence}\quad x &> u.
   \end{aligned}\right\} \dots\dots\dots\dots\dots\dots(1).

Let

.. math::

   x = u + v.

Then

.. math::

   (\rho + \sqrt k \cdot \rho) : \sqrt k \cdot \rho = (u + v) : u,

and hence

.. math::

   \rho : \sqrt k \cdot \rho = v : u \dots\dots\dots\dots\dots\dots(2).

Let :math:`w` be taken such that

.. math::

   v : u = (u + w) : w \dots\dots\dots\dots\dots\dots(3).

Thus

.. math::

   v : u = (u + v + w) : (u + w) \dots\dots\dots\dots\dots\dots(4),

and therefore

.. math::

   \rho : \sqrt k \cdot \rho = (u + v + w) : (u + w).

From the last proportion,

.. math::

   (u + v + w)^2 \mathbin{\cap} (u + w)^2,

and, from the two preceding, :math:`(u + w)` is a mean proportional between :math:`(u + v + w)`, :math:`w`, so that

.. math::

   (u + v + w)^2 : (u + w)^2 = (u + v + w) : w.

Therefore

.. math::

   (u + v + w) \mathbin{\cap} w,

whence

.. math::

   (u + v) \mathbin{\cap} w.

Now :math:`\sqrt k \cdot \rho\, (u + v) = \sigma^2`, which is rational; therefore :math:`(u + v)` is rational and :math:`\mathbin{\cap} \sqrt k \cdot \rho`; hence

.. math::

   w \text{ is also rational and } \mathbin{\cap} \sqrt k \cdot \rho \dots\dots\dots\dots\dots\dots(5).

Next, by (2), (3), since :math:`\rho`, :math:`\sqrt k \cdot \rho` are :math:`\mathbin{\sim}`,

.. math::

   (u + w) \mathbin{\sim} w,

and :math:`w` is rational; therefore :math:`(u + w)` is rational, and :math:`(u + w)`, :math:`w` are rational and :math:`\mathbin{\sim}`. Hence :math:`(u + w) - w` is an apotome.

Now either

.. math::

   \begin{aligned}
   \text{(I)} &\quad \sqrt{\rho^2 - k\rho^2} \mathbin{\cap} \rho, \\
   \text{or (II)} &\quad \sqrt{\rho^2 - k\rho^2} \mathbin{\cup} \rho.
   \end{aligned}

In case (I)

.. math::

   \sqrt{(u + w)^2 - w^2} \mathbin{\cap} (u + w), \qquad \text{[(2), (3) and X. 14]}

and in case (II)

.. math::

   \sqrt{(u + w)^2 - w^2} \mathbin{\cup} (u + w). \qquad \text{[*id*.]}

Then, since [(5)] :math:`w \mathbin{\cap} \sqrt k \cdot \rho`, by X. 11 and (2), (3),

.. math::

   (u + w) \mathbin{\cap} \rho \dots\dots\dots\dots\dots\dots(6).

[This step is omitted in Euclid, but the result is assumed.]

If therefore :math:`\rho \mathbin{\cap} \sigma`, :math:`(u + w) \mathbin{\cap} \sigma`; if :math:`\sqrt k \cdot \rho \mathbin{\cap} \sigma`, :math:`w \mathbin{\cap} \sigma`; [(5)] and, if neither :math:`\rho` nor :math:`\sqrt k \cdot \rho` is :math:`\mathbin{\cap} \sigma`, neither :math:`(u + w)` nor :math:`w` will be :math:`\mathbin{\cap} \sigma`.

Thus the order of the apotome :math:`(u + w) - w` is the same as that of the binomial straight line :math:`\rho + \sqrt k \cdot \rho`; while [(2), (3)] the terms are proportional and [(5), (6)] commensurable respectively.

.. _folio-iii-0252:

.. folio:: 0252
   :page: 248

We find :math:`(u + w)`, :math:`w` algebraically thus.

By (1),

.. math::

   u = \frac{\sigma^2}{\rho + \sqrt k \cdot \rho};

and, by (2), (3),

.. math::

   \frac{u + w}{w} = \frac{\rho}{\sqrt k \cdot \rho},

whence

.. math::

   \begin{aligned}
   w &= \frac{u \cdot \sqrt k \cdot \rho}{\rho - \sqrt k \cdot \rho} \\
   &= \frac{\sigma^2 \cdot \sqrt k \cdot \rho}{\rho^2 - k\rho^2}.
   \end{aligned}

Thus

.. math::

   u + w = w \cdot \frac{1}{\sqrt k} = \frac{\sigma^2 \cdot \rho}{\rho^2 - k\rho^2}.

Therefore

.. math::

   (u + w) - w = \sigma^2 \cdot \frac{\rho - \sqrt k \cdot \rho}{\rho^2 - k\rho^2}.

