:canonical_id: I.14
:volume: I
:book: I
:proposition: 14
:type: proposition
:title: Proposition I.14
:folios: 0290, 0291
:pages: 276, 277
:dependencies: I.post.4, I.cn.1, I.cn.3, I.13

.. _I.14:

.. folio:: 0290
   :page: 276

PROPOSITION 14.
===============

.. enunciation::

   If with any straight line,\ [#f1]_ and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

.. picture:: 0290.g1.svg
   :alt: Proposition 14 figure

For with any straight line :g:`AB <0290.g1:/ A B />`, and at the point :g:`B <0290.g1:B>` on it, let the two straight lines :g:`BC <0290.g1:/ B C />`, :g:`BD <0290.g1:/ B D />` not lying on the same side make the adjacent angles :g:`ABC <0290.g1:< A B C )>`, :g:`ABD <0290.g1:< A B D )>` equal to two right angles;

I say that :g:`BD <0290.g1:/ B D />` is in a straight line with :g:`CB <0290.g1:/ C B />`.

For, if :g:`BD <0290.g1:/ B D />` is not in a straight line with :g:`BC <0290.g1:/ B C />`, let :g:`BE <0290.g1:/ B E />` be in a straight line with :g:`CB <0290.g1:/ C B />`.

Then, since the straight line :g:`AB <0290.g1:/ A B />` stands on the straight line :g:`CBE <0290.g1:/ C B E />`,

.. assertion:: [I. 13] <I.13>

   the angles :g:`ABC <0290.g1:< A B C )>`, :g:`ABE <0290.g1:< A B E )>` are equal to two right angles.

But the angles :g:`ABC <0290.g1:< A B C )>`, :g:`ABD <0290.g1:< A B D )>` are also equal to two right angles;

.. assertion:: [Post. 4 and C. N. 1] <I.post.4, I.cn.1>

   therefore the angles :g:`CBA <0290.g1:< C B A )>`, :g:`ABE <0290.g1:< A B E )>` are equal to the angles :g:`CBA <0290.g1:< C B A )>`, :g:`ABD <0290.g1:< A B D )>`.\ [#f2]_

.. subclause::

   Let the angle :g:`CBA <0290.g1:< C B A )>` be subtracted from each;

therefore the remaining angle :g:`ABE <0290.g1:< A B E )>` is :eq:`equal <0290.g1:< A B E ) = 0290.g1:< A B D )>` to the remaining angle :g:`ABD <0290.g1:< A B D )>`, :just:`[C. N. 3] <I.cn.3>`

.. assertion::

   the less to the greater: which is impossible.

Therefore :g:`BE <0290.g1:/ B E />` is not in a straight line with :g:`CB <0290.g1:/ C B />`.

Similarly we can prove\ [#f3]_ that neither is any other straight line except :g:`BD <0290.g1:/ B D />`.

.. _folio-i-0291:

.. folio:: 0291
   :page: 277

Therefore :g:`CB <0290.g1:/ C B />` is in a straight line with :g:`BD <0290.g1:/ B D />`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **If with any straight line....** There is no greater difficulty in translating the works of the Greek geometers than that of accurately giving the force of prepositions. πρός, for instance, is used in all sorts of expressions with various shades of meaning. The present enunciation begins Ἐὰν πρός τινι εὐθείᾳ καὶ τῷ πρὸς αὐτῇ σημείῳ, and it is really necessary in this one sentence to translate πρός by three different words, *with*, *at*, and *on*. The first πρός must be translated by *with* because two straight lines “make” an angle *with* one another. On the other hand, where the similar expression πρὸς τῇ δοθείσῃ εὐθείᾳ occurs in I. 23, but it is a question of “constructing” an angle (συστήσασθαι), we have to say “to construct *on* a given straight line.” *Against* would perhaps be the English word coming nearest to expressing all these meanings of πρός, but it would be intolerable as a translation.

.. [#f2] :person:`Todhunter <todhunter>` points out that for the inference in this line Post. 4, that all right angles are equal, is necessary as well as the Common Notion that things which are equal to the same thing (or rather, here, to equal things) are equal. A similar remark applies to steps in the proofs of I. 15 and I. 28.

.. [#f3] **we can prove.** The Greek expresses this by the future of the verb, δείξομεν, “we shall prove,” which however would perhaps be misleading in English.

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
     "I.14" [label="I.14", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="I.14: If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be…", URL="index.html", target="_top"];
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
     "I.14" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
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
     "I.14" -> "I.13";
   }

Required for
------------

:ref:`I.45 <I.45>`, :ref:`I.47 <I.47>`, :ref:`I.48 <I.48>`, :ref:`II.9 <II.9>`, :ref:`II.10 <II.10>`, :ref:`II.11 <II.11>`, :ref:`II.12 <II.12>`, :ref:`II.13 <II.13>`, :ref:`II.14 <II.14>`, :ref:`III.14 <III.14>`, :ref:`III.15 <III.15>`, :ref:`III.35 <III.35>`, :ref:`III.36 <III.36>`, :ref:`III.37 <III.37>`, :ref:`IV.10 <IV.10>`, :ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`, :ref:`VI.14 <VI.14>`, :ref:`VI.15 <VI.15>`, :ref:`VI.16 <VI.16>`, :ref:`VI.17 <VI.17>`, :ref:`VI.19 <VI.19>`, :ref:`VI.20 <VI.20>`, :ref:`VI.22 <VI.22>`, :ref:`VI.25 <VI.25>`, :ref:`VI.28 <VI.28>`, :ref:`VI.29 <VI.29>`, :ref:`VI.30 <VI.30>`, :ref:`VI.31 <VI.31>`, :ref:`VI.32 <VI.32>`, :ref:`X.6 <X.6>`, :ref:`X.7 <X.7>`, :ref:`X.9 <X.9>`, :ref:`X.10 <X.10>`, :ref:`X.11 <X.11>`, :ref:`X.12 <X.12>`, :ref:`X.13 <X.13>`, :ref:`X.14 <X.14>`, :ref:`X.17 <X.17>`, :ref:`X.18 <X.18>`, :ref:`X.19 <X.19>`, :ref:`X.20 <X.20>`, :ref:`X.21 <X.21>`, :ref:`X.22 <X.22>`, :ref:`X.23 <X.23>`, :ref:`X.24 <X.24>`, :ref:`X.25 <X.25>`, :ref:`X.26 <X.26>`, :ref:`X.27 <X.27>`, :ref:`X.28 <X.28>`, :ref:`X.29 <X.29>`, :ref:`X.30 <X.30>`, :ref:`X.31 <X.31>`, :ref:`X.32 <X.32>`, :ref:`X.33 <X.33>`, :ref:`X.34 <X.34>`, :ref:`X.35 <X.35>`, :ref:`X.36 <X.36>`, :ref:`X.37 <X.37>`, :ref:`X.38 <X.38>`, :ref:`X.39 <X.39>`, :ref:`X.40 <X.40>`, :ref:`X.41 <X.41>`, :ref:`X.42 <X.42>`, :ref:`X.43 <X.43>`, :ref:`X.44 <X.44>`, :ref:`X.45 <X.45>`, :ref:`X.46 <X.46>`, :ref:`X.47 <X.47>`, :ref:`X.48 <X.48>`, :ref:`X.49 <X.49>`, :ref:`X.50 <X.50>`, :ref:`X.51 <X.51>`, :ref:`X.52 <X.52>`, :ref:`X.53 <X.53>`, :ref:`X.54 <X.54>`, :ref:`X.55 <X.55>`, :ref:`X.56 <X.56>`, :ref:`X.57 <X.57>`, :ref:`X.58 <X.58>`, :ref:`X.59 <X.59>`, :ref:`X.60 <X.60>`, :ref:`X.61 <X.61>`, :ref:`X.62 <X.62>`, :ref:`X.63 <X.63>`, :ref:`X.64 <X.64>`, :ref:`X.65 <X.65>`, :ref:`X.66 <X.66>`, :ref:`X.67 <X.67>`, :ref:`X.68 <X.68>`, :ref:`X.69 <X.69>`, :ref:`X.70 <X.70>`, :ref:`X.71 <X.71>`, :ref:`X.72 <X.72>`, :ref:`X.73 <X.73>`, :ref:`X.75 <X.75>`, :ref:`X.76 <X.76>`, :ref:`X.77 <X.77>`, :ref:`X.78 <X.78>`, :ref:`X.79 <X.79>`, :ref:`X.80 <X.80>`, :ref:`X.81 <X.81>`, :ref:`X.82 <X.82>`, :ref:`X.83 <X.83>`, :ref:`X.84 <X.84>`, :ref:`X.85 <X.85>`, :ref:`X.86 <X.86>`, :ref:`X.87 <X.87>`, :ref:`X.88 <X.88>`, :ref:`X.89 <X.89>`, :ref:`X.90 <X.90>`, :ref:`X.91 <X.91>`, :ref:`X.92 <X.92>`, :ref:`X.93 <X.93>`, :ref:`X.94 <X.94>`, :ref:`X.95 <X.95>`, :ref:`X.96 <X.96>`, :ref:`X.97 <X.97>`, :ref:`X.98 <X.98>`, :ref:`X.99 <X.99>`, :ref:`X.100 <X.100>`, :ref:`X.101 <X.101>`, :ref:`X.102 <X.102>`, :ref:`X.103 <X.103>`, :ref:`X.104 <X.104>`, :ref:`X.105 <X.105>`, :ref:`X.106 <X.106>`, :ref:`X.107 <X.107>`, :ref:`X.108 <X.108>`, :ref:`X.109 <X.109>`, :ref:`X.110 <X.110>`, :ref:`X.111 <X.111>`, :ref:`X.112 <X.112>`, :ref:`X.113 <X.113>`, :ref:`X.114 <X.114>`, :ref:`X.115 <X.115>`, :ref:`XI.23 <XI.23>`, :ref:`XI.32 <XI.32>`, :ref:`XI.33 <XI.33>`, :ref:`XI.34 <XI.34>`, :ref:`XI.35 <XI.35>`, :ref:`XI.36 <XI.36>`, :ref:`XI.37 <XI.37>`, :ref:`XI.38 <XI.38>`, :ref:`XII.1 <XII.1>`, :ref:`XII.2 <XII.2>`, :ref:`XII.4 <XII.4>`, :ref:`XII.5 <XII.5>`, :ref:`XII.6 <XII.6>`, :ref:`XII.7 <XII.7>`, :ref:`XII.8 <XII.8>`, :ref:`XII.9 <XII.9>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.1 <XIII.1>`, :ref:`XIII.4 <XIII.4>`, :ref:`XIII.5 <XIII.5>`, :ref:`XIII.6 <XIII.6>`, :ref:`XIII.10 <XIII.10>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.12 <XIII.12>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.14 <XIII.14>`, :ref:`XIII.15 <XIII.15>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.17 <XIII.17>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition I.14 <I.14.commentary>`.

.. toctree::
   :hidden:

   commentary
