:canonical_id: VI.28.commentary
:volume: II
:book: VI
:proposition: 28
:type: commentary
:title: Commentary on Proposition VI.28
:folios: 0268, 0269, 0270, 0271
:pages: 262, 263, 264, 265

.. _VI.28.commentary:

Commentary on Proposition VI.28
===============================

Back to :ref:`Proposition VI.28 <VI.28>`.

.. folio:: 0268
   :page: 262

The second part of the enunciation of this proposition which states the :term:`διορισμός <diorismos>` appears to have been considerably amplified, but not improved in the process, by Theon. His version would read as follows. "But the given rectilineal figure, that namely to which the applied parallelogram must be equal (ᾧ δεῖ ἴσον παραβαλεῖν), must not be greater than that applied to the half (παραβαλλομένου instead of ἀναγραφομένου), the defects being similar, (namely) that (of the parallelogram applied) to the half and that (of the required parallelogram) which must have a similar defect" (ὁμοίων ὄντων τῶν ἐλλειμμάτων τοῦ τε ἀπὸ τῆς ἡμισείας καὶ ᾧ δεῖ ὅμοιον ἐλλείπειν). The first amplification "that to which the applied parallelogram must be equal" is quite unnecessary, since "the given rectilineal figure" could mean nothing else. The above attempt at a translation will show how difficult it is to make sense of the words at the end; they speak of *two* defects apparently and, while one may well be the "defect on the half," the other can hardly be *the given parallelogram* "to which the defect (of the required parallelogram) must be similar." Clearly the reading given above (from $P$) is by far the better.

In this proposition and the next there occurs the tacit assumption (already alluded to in the note on VI. 22) that *if, of two similar parallelograms, one is greater than the other, either side of the greater is greater than the corresponding side of the less.*
As already remarked, VI. 28 is the geometrical equivalent of the solution of the quadratic equation

.. _folio-ii-0269:

.. folio:: 0269
   :page: 263

$$ax - \frac{b}{c} x^2 = S,$$

subject to the condition necessary to admit of a real solution, namely that

$$S \ngtr \frac{c}{b} \cdot \frac{a^2}{4}.$$

The corresponding proposition in the :cite:`*Data* <euclid:data>` is (Prop. 58), *If a given (area) be applied (i.e. in the form of a parallelogram) to a given straight line and be deficient by a figure (i.e. a parallelogram) given in species, the breadths of the defect are given.*

To exhibit the exact correspondence between Euclid's geometrical and the ordinary algebraical method of solving the equation we will, as before (in order to avoid bringing in a constant dependent on the sine of the angle of the parallelograms), suppose the parallelograms to be rectangles. To solve the equation algebraically we change the signs and write it

$$\frac{b}{c} x^2 - ax = - S.$$

We may now complete the square by adding $\frac{c}{b} \cdot \frac{a^2}{4}$.
Thus

$$\frac{b}{c} x^2 - ax + \frac{c}{b} \cdot \frac{a^2}{4} = \frac{c}{b} \cdot \frac{a^2}{4} - S;$$

and, extracting the square root, we have

$$\sqrt{\frac{b}{c}} \cdot x - \sqrt{\frac{c}{b}} \cdot \frac{a}{2} = \pm \sqrt{\frac{c}{b} \cdot \frac{a^2}{4} - S},$$

and

$$x = \frac{c}{b} \cdot \frac{a}{2} \pm \sqrt{\frac{c}{b} \left(\frac{c}{b} \cdot \frac{a^2}{4} - S\right)}.$$

Now let us observe Euclid's method.

.. picture:: 0269.g1.svg
   :alt: Book VI Proposition 28, Heath commentary diagram

He first describes :g:`$GEBF$ <0269.g1:< G E B F >>` on :g:`$EB$ <0269.g1:/ E B />` (half of :g:`$AB$ <0269.g1:/ A B />`) similar to the given parallelogram :g:`$D$ <0269.g1:< D >>`.
He then places in one angle :g:`$FGE$ <0269.g1:< F G E )>` of :g:`$GEBF$ <0269.g1:< G E B F >>` a similar and similarly situated parallelogram :g:`$GQ$ <0269.g1:< G Q >>`, equal to the difference between the parallelogram :g:`$GB$ <0269.g1:< G B >>` and the area :g:`$C$ <0269.g1:< C >>`.

With our notation,

.. container:: center

   :g:`$GO$ <0269.g1:/ G O />` $:$ :g:`$OQ$ <0269.g1:/ O Q />` $= c : b$,

whence

.. container:: center

   :g:`$OQ$ <0269.g1:/ O Q />` $=$ :g:`$GO$ <0269.g1:/ G O />` $\cdot \frac{b}{c}$.

.. _folio-ii-0270:

.. folio:: 0270
   :page: 264

Similarly

.. container:: center

   $\frac{a}{2} =$ :g:`$EB$ <0270.g1:/ E B />` $=$ :g:`$GE$ <0270.g1:/ G E />` $\cdot \frac{b}{c}$,

so that

.. container:: center

   :g:`$GE$ <0270.g1:/ G E />` $= \frac{c}{b} \cdot \frac{a}{2}$.

Therefore the parallelogram :g:`$GQ$ <0270.g1:< G Q >>` $=$ :g:`$GO^2$ <0270.g1:/ G O />` $\cdot \frac{b}{c}$,
and the parallelogram :g:`$GB$ <0270.g1:< G B >>` $= \frac{c}{b} \cdot \frac{a^2}{4}$.

Thus, in taking the parallelogram :g:`$GQ$ <0270.g1:< G Q >>` equal to $(GB - S)$, Euclid really finds :g:`$GO$ <0270.g1:/ G O />` from the equation

.. container:: center

   :g:`$GO^2$ <0270.g1:/ G O />` $\cdot \frac{b}{c} = \frac{c}{b} \cdot \frac{a^2}{4} - S$.

The value which he finds is

.. container:: center

   :g:`$GO$ <0270.g1:/ G O />` $= \sqrt{\frac{c}{b} \left(\frac{c}{b} \cdot \frac{a^2}{4} - S\right)}$,

and he finds :g:`$QS$ <0270.g1:/ Q S />` (or $x$) by subtracting :g:`$GO$ <0270.g1:/ G O />` from :g:`$GE$ <0270.g1:/ G E />`; whence

$$x = \frac{c}{b} \cdot \frac{a}{2} - \sqrt{\frac{c}{b} \left(\frac{c}{b} \cdot \frac{a^2}{4} - S\right)}.$$

It will be observed that Euclid only gives one solution, that corresponding to the *negative* sign before the radical. But the reason must be the same as that for which he only gives one "case" in VI. 27. He cannot have failed to see how to *add* :g:`$GO$ <0270.g1:/ G O />` to :g:`$GE$ <0270.g1:/ G E />` would give another solution. As shown under the last proposition, the other solution can be arrived at

(1) by placing the parallelogram :g:`$GOQP$ <0270.g1:< G O Q P >>` in the angle vertically opposite to :g:`$FGE$ <0270.g1:< F G E )>` so that :g:`$GQ'$ <0270.g1:< G Q' >>` lies along :g:`$BG$ <0270.g1:[ B G ]>` produced. The parallelogram :g:`$AQ'$ <0270.g1:< A Q' >>` then gives the second solution. The side of this parallelogram lying along :g:`$AB$ <0270.g1:/ A B />` is equal to :g:`$SB$ <0270.g1:/ S B />`. The other side is what we have called $x$, and in this case

.. container:: center

   $x =$ :g:`$EG$ <0270.g1:/ G E />` $+$ :g:`$GO$ <0270.g1:/ G O />` $= \frac{c}{b} \cdot \frac{a}{2} + \sqrt{\frac{c}{b} \left(\frac{c}{b} \cdot \frac{a^2}{4} - S\right)}$.

.. picture:: 0270.g1.svg
   :alt: Book VI Proposition 28, Heath commentary diagram (alternative solution)

(2) A parallelogram similar and equal to :g:`$AQ'$ <0270.g1:< A Q' >>` can also be obtained by producing :g:`$BG$ <0270.g1:[ B G ]>` till it meets :g:`$AT$ <0270.g1:[ A T ]>` produced and completing the parallelogram :g:`$B'ABA'$ <0270.g1:< B' A B A' >>`, whence it is seen that the complement :g:`$QA'$ <0270.g1:< Q A' >>` is equal to the complement :g:`$AQ$ <0270.g1:< A Q >>`, besides being equal and similar and similarly situated to :g:`$AQ'$ <0270.g1:< A Q' >>`.

A particular case of this proposition, indicated in Prop. 85 of the :cite:`*Data* <euclid:data>`, is that in which the sides of the defect are equal, so that the defect is a *rhombus* with a given angle. Prop. 85 proves that, *If two straight lines contain a given area in a given angle, and the sum of the straight lines be given, each of them will be given also.* :g:`$AB$ <0270.g2:/ A B />`, :g:`$BC$ <0270.g2:/ B C />` being the given straight lines "containing a given area :g:`$AC$ <0270.g2:< A C >>` in a given angle :g:`$ABC$ <0270.g2:< A B C )>`," one side :g:`$CB$ <0270.g2:[ C B ]>` is produced to :g:`$D$ <0270.g2:D>` so that :g:`$BD$ <0270.g2:/ B D />` is equal to :g:`$AB$ <0270.g2:/ A B />`, and the parallelograms are completed. Then, by hypothesis, :g:`$CD$ <0270.g2:/ C D />` is of given length, and :g:`$AC$ <0270.g2:< A C >>` is a parallelo-

.. picture:: 0270.g2.svg
   :alt: Book VI Proposition 28, Heath commentary diagram (Data Prop. 85)

.. _folio-ii-0271:

.. folio:: 0271
   :page: 265

gram applied to :g:`$CD$ <0270.g2:/ C D />` falling short by a rhombus (:g:`$AD$ <0270.g2:< A D >>`) with a given angle :g:`$EDB$ <0270.g2:< E D B )>`. The case is thus a particular case of Prop. 58 of the $Data$ quoted above (p. 263) as corresponding to VI. 28.

A particular case of the last, that namely in which the defect is a *square*, corresponding to the equation

$$ax - x^2 = b^2,$$

is important. This is the problem of *applying to a given straight line a* *rectangle equal to a given area and falling short by a square*; and it can be solved, without the aid of Book VI., as shown above under II. 5 (Vol. I. pp. 383—4).
