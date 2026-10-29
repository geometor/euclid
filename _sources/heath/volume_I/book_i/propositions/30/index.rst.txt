:canonical_id: I.30
:volume: I
:book: I
:proposition: 30
:type: proposition
:title: Proposition I.30
:folios: 0328
:pages: 314
:dependencies: I.cn.1, I.29

.. _I.30:

.. folio:: 0328
   :page: 314

PROPOSITION 30.
===============

.. enunciation::

   Straight lines parallel to the same straight line are also parallel to one another.

.. picture:: 0328.g1.svg
   :alt: Folio 0328 Figure 1 - Proposition 30

Let each of the straight lines :g:`$AB$ <0328.g1:/ A B />`, :g:`$CD$ <0328.g1:/ C D />` be parallel to :g:`$EF$ <0328.g1:/ E F />`;

I say that :g:`$AB$ <0328.g1:/ A B />` is also parallel to :g:`$CD$ <0328.g1:/ C D />`.

For let the straight line :g:`$GK$ <0328.g1:/ G K />` fall upon them;

Then, since the straight line :g:`$GK$ <0328.g1:/ G K />` has fallen on the parallel straight lines :g:`$AB$ <0328.g1:/ A B />`, :g:`$EF$ <0328.g1:/ E F />`,

.. assertion:: [I. 29] <I.29>

   the angle :g:`$AGK$ <0328.g1:< A G K )>` is :eq:`equal <0328.g1:< A G K ) = 0328.g1:< G H F )>` to the angle :g:`$GHF$ <0328.g1:< G H F )>`.

Again, since the straight line :g:`$GK$ <0328.g1:/ G K />` has fallen on the parallel straight lines :g:`$EF$ <0328.g1:/ E F />`, :g:`$CD$ <0328.g1:/ C D />`,

.. assertion:: [I. 29] <I.29>

   the angle :g:`$GHF$ <0328.g1:< G H F )>` is :eq:`equal <0328.g1:< G H F ) = 0328.g1:< G K D )>` to the angle :g:`$GKD$ <0328.g1:< G K D )>`.

But the angle :g:`$AGK$ <0328.g1:< A G K )>` was also proved :eq:`equal <0328.g1:< A G K ) = 0328.g1:< G H F )>` to the angle :g:`$GHF$ <0328.g1:< G H F )>`;

.. assertion:: [C. N. 1] <I.cn.1>

   therefore the angle :g:`$AGK$ <0328.g1:< A G K )>` is also :eq:`equal <0328.g1:< A G K ) = 0328.g1:< G K D )>` to the angle :g:`$GKD$ <0328.g1:< G K D )>`;

.. subclause::

   and they are alternate.

.. assertion::

   Therefore :g:`$AB$ <0328.g1:/ A B />` is parallel to :g:`$CD$ <0328.g1:/ C D />`.\ [#f1]_

.. qed::

   Q. E. D.

.. [#f1] The usual conclusion in general terms ("Therefore etc.") repeating the enunciation is, curiously enough, wanting at the end of this proposition.

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
     "I.1" [label="I.1", fillcolor="#222244", tooltip="I.1: On a given finite straight line to construct an equilateral triangle.", URL="../01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", tooltip="I.2: To place at a given point (as an extremity) a straight line equal to a given straight line.", URL="../02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", tooltip="I.3: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", URL="../03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", tooltip="I.4: If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the…", URL="../04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", tooltip="I.5: In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one…", URL="../05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", tooltip="I.7: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its…", URL="../07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", tooltip="I.8: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the…", URL="../08/index.html", target="_top"];
     "I.11" [label="I.11", fillcolor="#222244", tooltip="I.11: To draw a straight line at right angles to a given straight line from a given point on it.", URL="../11/index.html", target="_top"];
     "I.13" [label="I.13", fillcolor="#222244", tooltip="I.13: If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", URL="../13/index.html", target="_top"];
     "I.15" [label="I.15", fillcolor="#222244", tooltip="I.15: If two straight lines cut one another, they make the vertical angles equal to one another.", URL="../15/index.html", target="_top"];
     "I.29" [label="I.29", fillcolor="#222244", tooltip="I.29: A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior…", URL="../29/index.html", target="_top"];
     "I.30" [label="I.30", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="I.30: Straight lines parallel to the same straight line are also parallel to one another.", URL="index.html", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
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
     "I.30" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.29" -> "I.cn.2";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "I.11" -> "I.1";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.11" -> "I.3";
     "I.5" -> "I.4";
     "I.7" -> "I.5";
     "I.8" -> "I.7";
     "I.11" -> "I.8";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.29" -> "I.15";
     "I.30" -> "I.29";
   }

Required for
------------

:ref:`I.45 <I.45>`, :ref:`II.14 <II.14>`, :ref:`IV.7 <IV.7>`, :ref:`VI.25 <VI.25>`, :ref:`VI.28 <VI.28>`, :ref:`VI.29 <VI.29>`, :ref:`VI.30 <VI.30>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.54 <X.54>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.71 <X.71>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`XI.32 <XI.32>`, :ref:`XI.33 <XI.33>`, :ref:`XI.34 <XI.34>`, :ref:`XI.37 <XI.37>`, :ref:`XII.8 <XII.8>`, :ref:`XII.9 <XII.9>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition I.30 <I.30.commentary>`.

.. toctree::
   :hidden:

   commentary
