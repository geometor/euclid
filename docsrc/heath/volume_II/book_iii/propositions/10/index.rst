:canonical_id: III.10
:volume: II
:book: III
:proposition: 10
:type: proposition
:title: Proposition III.10
:folios: 0029
:pages: 23
:dependencies: III.1, III.5

.. _III.10:

.. _folio-ii-0029:

.. folio:: 0029
   :page: 23

PROPOSITION 10.
===============

.. enunciation::

   A circle\ [#f1]_ does not cut a circle at more points than two.

For, if possible, let the circle :g:`ABC <0029.g1:( A B C )>` cut the circle :g:`DEF <0029.g1:( D E F )>` at more points than two, namely :g:`B <0029.g1:B>`, :g:`G <0029.g1:G>`, :g:`F <0029.g1:F>`, :g:`H <0029.g1:H>`; let :g:`BH <0029.g1:/ B H />`, :g:`BG <0029.g1:/ B G />` be joined and :eq:`bisected <0029.g1:/ B K / = 0029.g1:/ K H /; 0029.g1:/ B L / = 0029.g1:/ L G />` at the points :g:`K <0029.g1:K>`, :g:`L <0029.g1:L>`, and from :g:`K <0029.g1:K>`, :g:`L <0029.g1:L>` let :g:`KC <0029.g1:/ K C />`, :g:`LM <0029.g1:/ L M />` be drawn at right angles to :g:`BH <0029.g1:/ B H />`, :g:`BG <0029.g1:/ B G />` and carried through to the points :g:`A <0029.g1:A>`, :g:`E <0029.g1:E>`.

.. picture:: 0029.g1.svg
   :alt: Diagram for Proposition 10

Then, since in the circle :g:`ABC <0029.g1:( A B C )>` a straight line :g:`AC <0029.g1:/ A C />` cuts a straight line :g:`BH <0029.g1:/ B H />` into two :eq:`equal <0029.g1:/ B K / = 0029.g1:/ K H />` parts and at right angles,

.. assertion:: [III. 1, Por.]

   the centre of the circle :g:`ABC <0029.g1:( A B C )>` is on :g:`AC <0029.g1:/ A C />`.

Again, since in the same circle :g:`ABC <0029.g1:( A B C )>` a straight line :g:`NO <0029.g1:/ N O />` cuts a straight line :g:`BG <0029.g1:/ B G />` into two :eq:`equal <0029.g1:/ B L / = 0029.g1:/ L G />` parts and at right angles,

.. assertion::

   the centre of the circle :g:`ABC <0029.g1:( A B C )>` is on :g:`NO <0029.g1:/ N O />`.

But it was also proved to be on :g:`AC <0029.g1:/ A C />`, and the straight lines :g:`AC <0029.g1:/ A C />`, :g:`NO <0029.g1:/ N O />` meet at no point except at :g:`P <0029.g1:P>`;

.. assertion::

   therefore the point :g:`P <0029.g1:P>` is the centre of the circle :g:`ABC <0029.g1:( A B C )>`.

Similarly we can prove that :g:`P <0029.g1:P>` is also the centre of the circle :g:`DEF <0029.g1:( D E F )>`;

.. assertion::

   therefore the two circles :g:`ABC <0029.g1:( A B C )>`, :g:`DEF <0029.g1:( D E F )>` which cut one another have the same centre :g:`P <0029.g1:P>`: which is impossible. :just:`[III. 5] <III.5>`

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] The word **circle** ($\kappa\acute{\upsilon}\kappa\lambda\omicron\varsigma$) is here employed in the unusual sense of the *circumference* ($\pi\epsilon\rho\iota\phi\acute{\epsilon}\rho\epsilon\iota\alpha$) of a circle. Cf. note on I. Def. 15.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "I.def.10" [label="I.def.10", fillcolor="#224422", tooltip="I.def.10: When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is…", URL="../../../../volume_I/book_i/definitions/index.html#i-def-10", target="_top"];
     "I.def.15" [label="I.def.15", fillcolor="#224422", tooltip="I.def.15: A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another.", URL="../../../../volume_I/book_i/definitions/index.html#i-def-15", target="_top"];
     "I.post.1" [label="I.post.1", fillcolor="#444422", tooltip="I.post.1: To draw a straight line from any point to any point.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-1", target="_top"];
     "I.post.2" [label="I.post.2", fillcolor="#444422", tooltip="I.post.2: To produce a finite straight line continuously in a straight line.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-2", target="_top"];
     "I.post.3" [label="I.post.3", fillcolor="#444422", tooltip="I.post.3: To describe a circle with any centre and distance.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-3", target="_top"];
     "I.cn.1" [label="I.cn.1", fillcolor="#442222", tooltip="I.cn.1: Things which are equal to the same thing are also equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-1", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", tooltip="I.cn.3: If equals be subtracted from equals, the remainders are equal.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", tooltip="I.cn.4: Things which coincide with one another are equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-4", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", tooltip="I.1: On a given finite straight line to construct an equilateral triangle.", URL="../../../../volume_I/book_i/propositions/01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", tooltip="I.2: To place at a given point (as an extremity) a straight line equal to a given straight line.", URL="../../../../volume_I/book_i/propositions/02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", tooltip="I.3: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", URL="../../../../volume_I/book_i/propositions/03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", tooltip="I.4: If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the…", URL="../../../../volume_I/book_i/propositions/04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", tooltip="I.5: In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one…", URL="../../../../volume_I/book_i/propositions/05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", tooltip="I.7: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its…", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", tooltip="I.8: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the…", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "III.1" [label="III.1", fillcolor="#222244", tooltip="III.1: To find the centre of a given circle.", URL="../01/index.html", target="_top"];
     "III.5" [label="III.5", fillcolor="#222244", tooltip="III.5: If two circles cut one another, they will not have the same centre.", URL="../05/index.html", target="_top"];
     "III.10" [label="III.10", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.10: A circle does not cut a circle at more points than two.", URL="index.html", target="_top"];
     "III.1" -> "I.def.10";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.5" -> "I.def.15";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.7" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.2" -> "I.cn.3";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "I.3" -> "I.2";
     "I.5" -> "I.3";
     "I.5" -> "I.4";
     "I.7" -> "I.5";
     "I.8" -> "I.7";
     "III.1" -> "I.8";
     "III.10" -> "III.1";
     "III.10" -> "III.5";
   }

Required for
------------

:ref:`III.24 <III.24>`, :ref:`III.26 <III.26>`, :ref:`III.27 <III.27>`, :ref:`III.28 <III.28>`, :ref:`III.29 <III.29>`, :ref:`III.30 <III.30>`, :ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`, :ref:`IV.15 <IV.15>`, :ref:`IV.16 <IV.16>`, :ref:`VI.33 <VI.33>`, :ref:`XII.1 <XII.1>`, :ref:`XII.2 <XII.2>`, :ref:`XII.5 <XII.5>`, :ref:`XII.6 <XII.6>`, :ref:`XII.7 <XII.7>`, :ref:`XII.8 <XII.8>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XII.17 <XII.17>`, :ref:`XII.18 <XII.18>`, :ref:`XIII.8 <XIII.8>`, :ref:`XIII.9 <XIII.9>`, :ref:`XIII.10 <XIII.10>`, :ref:`XIII.11 <XIII.11>`, :ref:`XIII.12 <XIII.12>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.16 <XIII.16>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition III.10 <III.10.commentary>`.

.. toctree::
   :hidden:

   commentary
