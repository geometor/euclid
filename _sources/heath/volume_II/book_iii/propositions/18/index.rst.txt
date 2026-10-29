:canonical_id: III.18
:volume: II
:book: III
:proposition: 18
:type: proposition
:title: Proposition III.18
:folios: 0050, 0051
:pages: 44, 45
:dependencies: I.17, I.19

.. _III.18:

.. folio:: 0050
   :page: 44

PROPOSITION 18.
===============

.. enunciation::

   If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.\ [#f1]_

For let a straight line :g:`DE <0050.g1:/ D E />` touch the circle :g:`ABC <0050.g1:( A B C )>` at the
point :g:`C <0050.g1:C>`, let the centre :g:`F <0050.g1:F>` of the
circle :g:`ABC <0050.g1:( A B C )>` be taken, and let :g:`FC <0050.g1:/ F C />`
be joined from :g:`F <0050.g1:F>` to :g:`C <0050.g1:C>`;
I say that :g:`FC <0050.g1:/ F C />` is perpendicular to
:g:`DE <0050.g1:/ D E />`.

.. picture:: 0050.g1.svg
   :alt: Diagram for Proposition 18

For, if not, let :g:`FG <0050.g1:/ F G />` be drawn
from :g:`F <0050.g1:F>` perpendicular to :g:`DE <0050.g1:/ D E />`.

Then, since the angle :g:`FGC <0050.g1:< F G C )>` is
right,

.. assertion:: [I. 17] <I.17>

   the angle :g:`FCG <0050.g1:< F C G )>` is acute;

and the greater angle is subtended
by the greater side; :just:`[I. 19] <I.19>`

.. assertion::

   therefore :g:`FC <0050.g1:/ F C />` is greater than :g:`FG <0050.g1:/ F G />`.

But :g:`FC <0050.g1:/ F C />` is :eq:`equal <0050.g1:/ F C / = 0050.g1:/ F B />` to :g:`FB <0050.g1:/ F B />`;

.. assertion::

   therefore :g:`FB <0050.g1:/ F B />` is also greater than :g:`FG <0050.g1:/ F G />`, the less than the greater: which is impossible.

Therefore :g:`FG <0050.g1:/ F G />` is not perpendicular to :g:`DE <0050.g1:/ D E />`.

Similarly we can prove that neither is any other straight
line except :g:`FC <0050.g1:/ F C />`;

.. assertion::

   therefore :g:`FC <0050.g1:/ F C />` is perpendicular to :g:`DE <0050.g1:/ D E />`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **the tangent**, $\text{ἡ ἐφαπτομένη}$.

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
     "I.post.4" [label="I.post.4", fillcolor="#444422", tooltip="I.post.4: That all right angles are equal to one another.", URL="../../../../volume_I/book_i/postulates/index.html#i-post-4", target="_top"];
     "I.cn.1" [label="I.cn.1", fillcolor="#442222", tooltip="I.cn.1: Things which are equal to the same thing are also equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-1", target="_top"];
     "I.cn.2" [label="I.cn.2", fillcolor="#442222", tooltip="I.cn.2: If equals be added to equals, the wholes are equal.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-2", target="_top"];
     "I.cn.3" [label="I.cn.3", fillcolor="#442222", tooltip="I.cn.3: If equals be subtracted from equals, the remainders are equal.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-3", target="_top"];
     "I.cn.4" [label="I.cn.4", fillcolor="#442222", tooltip="I.cn.4: Things which coincide with one another are equal to one another.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-4", target="_top"];
     "I.cn.5" [label="I.cn.5", fillcolor="#442222", tooltip="I.cn.5: The whole is greater than the part.", URL="../../../../volume_I/book_i/common_notions/index.html#i-cn-5", target="_top"];
     "I.1" [label="I.1", fillcolor="#222244", tooltip="I.1: On a given finite straight line to construct an equilateral triangle.", URL="../../../../volume_I/book_i/propositions/01/index.html", target="_top"];
     "I.2" [label="I.2", fillcolor="#222244", tooltip="I.2: To place at a given point (as an extremity) a straight line equal to a given straight line.", URL="../../../../volume_I/book_i/propositions/02/index.html", target="_top"];
     "I.3" [label="I.3", fillcolor="#222244", tooltip="I.3: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", URL="../../../../volume_I/book_i/propositions/03/index.html", target="_top"];
     "I.4" [label="I.4", fillcolor="#222244", tooltip="I.4: If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the…", URL="../../../../volume_I/book_i/propositions/04/index.html", target="_top"];
     "I.5" [label="I.5", fillcolor="#222244", tooltip="I.5: In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one…", URL="../../../../volume_I/book_i/propositions/05/index.html", target="_top"];
     "I.7" [label="I.7", fillcolor="#222244", tooltip="I.7: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its…", URL="../../../../volume_I/book_i/propositions/07/index.html", target="_top"];
     "I.8" [label="I.8", fillcolor="#222244", tooltip="I.8: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the…", URL="../../../../volume_I/book_i/propositions/08/index.html", target="_top"];
     "I.9" [label="I.9", fillcolor="#222244", tooltip="I.9: To bisect a given rectilineal angle.", URL="../../../../volume_I/book_i/propositions/09/index.html", target="_top"];
     "I.10" [label="I.10", fillcolor="#222244", tooltip="I.10: To bisect a given finite straight line.", URL="../../../../volume_I/book_i/propositions/10/index.html", target="_top"];
     "I.11" [label="I.11", fillcolor="#222244", tooltip="I.11: To draw a straight line at right angles to a given straight line from a given point on it.", URL="../../../../volume_I/book_i/propositions/11/index.html", target="_top"];
     "I.13" [label="I.13", fillcolor="#222244", tooltip="I.13: If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", URL="../../../../volume_I/book_i/propositions/13/index.html", target="_top"];
     "I.15" [label="I.15", fillcolor="#222244", tooltip="I.15: If two straight lines cut one another, they make the vertical angles equal to one another.", URL="../../../../volume_I/book_i/propositions/15/index.html", target="_top"];
     "I.16" [label="I.16", fillcolor="#222244", tooltip="I.16: In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", URL="../../../../volume_I/book_i/propositions/16/index.html", target="_top"];
     "I.17" [label="I.17", fillcolor="#222244", tooltip="I.17: In any triangle two angles taken together in any manner are less than two right angles.", URL="../../../../volume_I/book_i/propositions/17/index.html", target="_top"];
     "I.18" [label="I.18", fillcolor="#222244", tooltip="I.18: In any triangle the greater side subtends the greater angle.", URL="../../../../volume_I/book_i/propositions/18/index.html", target="_top"];
     "I.19" [label="I.19", fillcolor="#222244", tooltip="I.19: In any triangle the greater angle is subtended by the greater side.", URL="../../../../volume_I/book_i/propositions/19/index.html", target="_top"];
     "III.18" [label="III.18", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="III.18: If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.", URL="index.html", target="_top"];
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
     "I.17" -> "I.post.2";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.13" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.13" -> "I.cn.2";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
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
     "I.18" -> "I.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.8" -> "I.7";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.10" -> "I.9";
     "I.16" -> "I.10";
     "I.13" -> "I.11";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.16" -> "I.15";
     "I.18" -> "I.16";
     "III.18" -> "I.17";
     "I.19" -> "I.18";
     "III.18" -> "I.19";
   }

Required for
------------

:ref:`III.19 <III.19>`, :ref:`III.32 <III.32>`, :ref:`III.33 <III.33>`, :ref:`III.34 <III.34>`, :ref:`III.36 <III.36>`, :ref:`III.37 <III.37>`, :ref:`IV.2 <IV.2>`, :ref:`IV.3 <IV.3>`, :ref:`IV.7 <IV.7>`, :ref:`IV.10 <IV.10>`, :ref:`IV.11 <IV.11>`, :ref:`IV.12 <IV.12>`, :ref:`XII.10 <XII.10>`, :ref:`XII.11 <XII.11>`, :ref:`XII.12 <XII.12>`, :ref:`XII.13 <XII.13>`, :ref:`XII.14 <XII.14>`, :ref:`XII.15 <XII.15>`, :ref:`XIII.13 <XIII.13>`, :ref:`XIII.18 <XIII.18>`

----

See :ref:`Commentary on Proposition III.18 <III.18.commentary>`.

.. toctree::
   :hidden:

   commentary
