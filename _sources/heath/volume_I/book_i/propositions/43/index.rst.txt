:canonical_id: I.43
:volume: I
:book: I
:proposition: 43
:type: proposition
:title: Proposition I.43
:folios: 0354, 0355
:pages: 340, 341
:dependencies: I.cn.2, I.cn.3, I.34

.. _I.43:

.. folio:: 0354
   :page: 340

PROPOSITION 43.
===============

.. enunciation::

   In any parallelogram the complements\ [#f1]_ of the parallelograms about the diameter are equal to one another.

Let :g:`$ABCD$ <0354.g1:< A B C D >>` be a parallelogram, and :g:`$AC$ <0354.g1:/ A C />` its diameter; and about :g:`$AC$ <0354.g1:/ A C />`\ [#f2]_ let :g:`$EH$ <0354.g1:< A E K H >>`, :g:`$FG$ <0354.g1:< K F C G >>` be parallelograms, and :g:`$BK$ <0354.g1:< E B F K >>`, :g:`$KD$ <0354.g1:< H K G D >>` the so-called complements;

I say that the complement :g:`$BK$ <0354.g1:< E B F K >>` is :eq:`equal <0354.g1:< E B F K > = 0354.g1:< H K G D >>` to the complement :g:`$KD$ <0354.g1:< H K G D >>`.

.. picture:: 0354.g1.svg
   :alt: Folio 0354 Figure 1 - Proposition 43

For, since :g:`$ABCD$ <0354.g1:< A B C D >>` is a parallelogram, and :g:`$AC$ <0354.g1:/ A C />` its diameter, the triangle :g:`$ABC$ <0354.g1:< A B C >>` is :eq:`equal <0354.g1:< A B C > = 0354.g1:< A C D >>` to the triangle :g:`$ACD$ <0354.g1:< A C D >>`. :just:`[I. 34] <I.34>`

Again, since :g:`$EH$ <0354.g1:< A E K H >>` is a parallelogram, and :g:`$AK$ <0354.g1:/ A K />` is its diameter, the triangle :g:`$AEK$ <0354.g1:< A E K >>` is :eq:`equal <0354.g1:< A E K > = 0354.g1:< A H K >>` to the triangle :g:`$AHK$ <0354.g1:< A H K >>`.

For the same reason the triangle :g:`$KFC$ <0354.g1:< K F C >>` is also :eq:`equal <0354.g1:< K F C > = 0354.g1:< K G C >>` to :g:`$KGC$ <0354.g1:< K G C >>`.

Now, since the triangle :g:`$AEK$ <0354.g1:< A E K >>` is :eq:`equal <0354.g1:< A E K > = 0354.g1:< A H K >; 0354.g1:< K F C > = 0354.g1:< K G C >>` to the triangle :g:`$AHK$ <0354.g1:< A H K >>`, and :g:`$KFC$ <0354.g1:< K F C >>` to :g:`$KGC$ <0354.g1:< K G C >>`,

.. assertion:: [C. N. 2] <I.cn.2>

   the triangle :g:`$AEK$ <0354.g1:< A E K >>` together with :g:`$KGC$ <0354.g1:< K G C >>` is equal to the triangle :g:`$AHK$ <0354.g1:< A H K >>` together with :g:`$KFC$ <0354.g1:< K F C >>`.

And the whole triangle :g:`$ABC$ <0354.g1:< A B C >>` is also :eq:`equal <0354.g1:< A B C > = 0354.g1:< A D C >>` to the whole :g:`$ADC$ <0354.g1:< A D C >>`;

.. assertion::

   therefore the complement :g:`$BK$ <0354.g1:< E B F K >>` which remains is :eq:`equal <0354.g1:< E B F K > = 0354.g1:< H K G D >>` to the complement :g:`$KD$ <0354.g1:< H K G D >>` which remains. :just:`[C. N. 3] <I.cn.3>`

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **complements**, :term:`παραπληρώματα <parapleroma>`, the figures put in to fill up (interstices).

.. [#f2] **and about** :g:`$AC$ <0354.g1:/ A C />`.... Euclid's phraseology here and in the next proposition implies that the complements as well as the other parallelograms are “about” the diagonal. The words are here περὶ δὲ τὴν ΑΓ παραλληλόγραμμα μὲν ἔστω τὰ ΕΘ, ΖΗ, τὰ δὲ λεγόμενα :term:`παραπληρώματα <parapleroma>` τὰ ΒΚ, ΚΔ. The expression “the so-called complements” indicates that this technical use of :term:`παραπληρώματα <parapleroma>` was not new, though it might not be universally known.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "I.def.10" [label="I.def.10", fillcolor="#224422", tooltip="I.def.10: When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is…", URL="../../definitions/index.html#i-def-10", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", tooltip="I.def.15: A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.", URL="../../definitions/index.html#i-def-15", target="_top"];
     "I.post.1" [label="I.post.1", fillcolor="#444422", tooltip="I.post.1: To draw a straight line from any point to any point.", URL="../../postulates/index.html#i-post-1", target="_top"];
     "I.post.2" [label="I.post.2", fillcolor="#444422", tooltip="I.post.2: To produce a finite straight line continuously in a straight line.", URL="../../postulates/index.html#i-post-2", target="_top"];
     "I.post.3" [label="I.post.3", fillcolor="#444422", tooltip="I.post.3: To describe a circle with any centre and distance.", URL="../../postulates/index.html#i-post-3", target="_top"];
     "I.post.4" [label="I.post.4", fillcolor="#444422", tooltip="I.post.4: That all right angles are equal to one another.", URL="../../postulates/index.html#i-post-4", target="_top"];
     "I.post.5" [label="I.post.5", fillcolor="#444422", tooltip="I.post.5: That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet…", URL="../../postulates/index.html#i-post-5", target="_top"];
     "I.cn.1" [label="I.cn.1", fillcolor="#442222", tooltip="I.cn.1: Things which are equal to the same thing are also equal to one another.", URL="../../common_notions/index.html#i-cn-1", target="_top"];
     "I.cn.2" [label="I.cn.2", fillcolor="#442222", tooltip="I.cn.2: If equals be added to equals, the wholes are equal.", URL="../../common_notions/index.html#i-cn-2", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", tooltip="I.cn.3: If equals be subtracted from equals, the remainders are equal.", URL="../../common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", tooltip="I.cn.4: Things which coincide with one another are equal to one another.", URL="../../common_notions/index.html#i-cn-4", target="_top"];
     "I.cn.5" [label="I.cn.5", fillcolor="#442222", tooltip="I.cn.5: The whole is greater than the part.", URL="../../common_notions/index.html#i-cn-5", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", tooltip="I.1: On a given finite straight line to construct an equilateral triangle.", URL="../01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", tooltip="I.2: To place at a given point (as an extremity) a straight line equal to a given straight line.", URL="../02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", tooltip="I.3: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", URL="../03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", tooltip="I.4: If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the…", URL="../04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", tooltip="I.5: In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one…", URL="../05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", tooltip="I.7: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its…", URL="../07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", tooltip="I.8: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the…", URL="../08/index.html", target="_top"];
     "I.9" [label="I.9", fillcolor="#222244", tooltip="I.9: To bisect a given rectilineal angle.", URL="../09/index.html", target="_top"];
     "I.10" [label="I.10", fillcolor="#222244", tooltip="I.10: To bisect a given finite straight line.", URL="../10/index.html", target="_top"];
     "I.11" [label="I.11", fillcolor="#222244", tooltip="I.11: To draw a straight line at right angles to a given straight line from a given point on it.", URL="../11/index.html", target="_top"];
     "I.13" [label="I.13", fillcolor="#222244", tooltip="I.13: If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", URL="../13/index.html", target="_top"];
     "I.15" [label="I.15", fillcolor="#222244", tooltip="I.15: If two straight lines cut one another, they make the vertical angles equal to one another.", URL="../15/index.html", target="_top"];
     "I.16" [label="I.16", fillcolor="#222244", tooltip="I.16: In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", URL="../16/index.html", target="_top"];
     "I.26" [label="I.26", fillcolor="#222244", tooltip="I.26: If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one…", URL="../26/index.html", target="_top"];
     "I.29" [label="I.29", fillcolor="#222244", tooltip="I.29: A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior…", URL="../29/index.html", target="_top"];
     "I.34" [label="I.34", fillcolor="#222244", tooltip="I.34: In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.", URL="../34/index.html", target="_top"];
     "I.43" [label="I.43", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="I.43: In any parallelogram the complements of the parallelograms about the diameter are equal to one another.", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.15" -> "I.post.4";
     "I.29" -> "I.post.5";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.43" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.16" -> "I.cn.5";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.7" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.26" -> "I.16";
     "I.34" -> "I.26";
     "I.34" -> "I.29";
     "I.43" -> "I.34";
   }

Required for
------------

:ref:`I.44 <I.44>`, :ref:`I.45 <I.45>`, :ref:`II.5 <II.5>`, :ref:`II.6 <II.6>`, :ref:`II.7 <II.7>`, :ref:`II.8 <II.8>`, :ref:`II.11 <II.11>`, :ref:`II.13 <II.13>`, :ref:`II.14 <II.14>`, :ref:`III.35 <III.35>`, :ref:`III.36 <III.36>`, :ref:`III.37 <III.37>`, :ref:`IV.10 <IV.10>`, :ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`, :ref:`VI.25 <VI.25>`, :ref:`VI.27 <VI.27>`, :ref:`VI.28 <VI.28>`, :ref:`VI.29 <VI.29>`, :ref:`VI.30 <VI.30>`, :ref:`X.17 <X.17>`, :ref:`X.18 <X.18>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.38 <X.38>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.44 <X.44>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.54 <X.54>`, :ref:`X.55 <X.55>`, :ref:`X.56 <X.56>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.61 <X.61>`, :ref:`X.62 <X.62>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.67 <X.67>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.73 <X.73>`, :ref:`X.74 <X.74>`, :ref:`X.75 <X.75>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.79 <X.79>`, :ref:`X.80 <X.80>`, :ref:`X.81 <X.81>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.92 <X.92>`, :ref:`X.93 <X.93>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.97 <X.97>`, :ref:`X.98 <X.98>`, :ref:`X.99 <X.99>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.103 <X.103>`, :ref:`X.104 <X.104>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`X.112 <X.112>`, :ref:`X.113 <X.113>`, :ref:`X.114 <X.114>`, :ref:`XI.32 <XI.32>`, :ref:`XI.33 <XI.33>`, :ref:`XI.34 <XI.34>`, :ref:`XI.37 <XI.37>`, :ref:`XII.8 <XII.8>`, :ref:`XII.9 <XII.9>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition I.43 <I.43.commentary>`.

.. toctree::
   :hidden:

   commentary
