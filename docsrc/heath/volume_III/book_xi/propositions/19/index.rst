:canonical_id: XI.19
:volume: III
:book: XI
:proposition: 19
:type: proposition
:title: Proposition XI.19
:folios: 0308, 0309
:pages: 304, 305
:dependencies: XI.def.4, XI.13

.. _XI.19:

.. folio:: 0308
   :page: 304

PROPOSITION 19.
===============

.. enunciation::

   If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.

For let the two planes :g:`AB <0308.g2:< A B >>`, :g:`BC <0308.g2:< B C >>` be at right angles to the plane of reference, and let :g:`BD <0308.g2:/ B D />` be their common section; I say that :g:`BD <0308.g2:/ B D />` is at right angles to the plane of reference.

.. picture:: 0308.g2.svg
   :alt: Book XI, Proposition 19

For suppose it is not, and from the point :g:`D <0308.g2:D>` let :g:`DE <0308.g2:/ D E />` be drawn in the plane :g:`AB <0308.g2:< A B >>` at right angles to the straight line :g:`AD <0308.g2:/ A D />`, and :g:`DF <0308.g2:/ D F />` in the plane :g:`BC <0308.g2:< B C >>` at right angles to :g:`CD <0308.g2:/ C D />`.

.. subclause::

   Now, since the plane :g:`AB <0308.g2:< A B >>` is at right angles to the plane of reference, and :g:`DE <0308.g2:/ D E />` has been drawn in the plane :g:`AB <0308.g2:< A B >>` at right angles to :g:`AD <0308.g2:/ A D />`, their common section,

.. assertion:: [XI. Def. 4] <XI.def.4>

   therefore :g:`DE <0308.g2:/ D E />` is at right angles to the plane of reference.

.. _folio-iii-0309:

.. folio:: 0309
   :page: 305

.. assertion::

   Similarly we can prove that :g:`DF <0308.g2:/ D F />` is also at right angles to the plane of reference.

.. assertion::

   Therefore from the same point :g:`D <0308.g2:D>` two straight lines have been set up at right angles to the plane of reference on the same side: which is impossible. :just:`[XI. 13] <XI.13>`

.. assertion::

   Therefore no straight line except the common section :g:`DB <0308.g2:/ D B />` of the planes :g:`AB <0308.g2:< A B >>`, :g:`BC <0308.g2:< B C >>` can be set up from the point :g:`D <0308.g2:D>` at right angles to the plane of reference.

.. qed::

   Therefore etc. :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "XI.def.3" [label="XI.def.3", fillcolor="#224422", tooltip="XI.def.3: A straight line is at right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", URL="../../definitions/index.html#xi-def-3", target="_top"];
     "XI.def.4" [label="XI.def.4", fillcolor="#224422", tooltip="XI.def.4: A plane is at right angles to a plane when the straight lines drawn, in one of the planes, at right angles to the common section of the planes are at right angles to the remaining…", URL="../../definitions/index.html#xi-def-4", target="_top"];
     "XI.3" [label="XI.3", fillcolor="#222244", tooltip="XI.3: If two planes cut one another, their common section is a straight line.", URL="../03/index.html", target="_top"];
     "XI.13" [label="XI.13", fillcolor="#222244", tooltip="XI.13: From the same point two straight lines cannot be set up at right angles to the same plane on the same side.", URL="../13/index.html", target="_top"];
     "XI.19" [label="XI.19", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="XI.19: If two planes which cut one another be at right angles to any plane, their common section will also be at right angles to the same plane.", URL="index.html", target="_top"];
     "XI.13" -> "XI.def.3";
     "XI.19" -> "XI.def.4";
     "XI.13" -> "XI.3";
     "XI.19" -> "XI.13";
   }

----

See :ref:`Commentary on Proposition XI.19 <XI.19.commentary>`.

.. toctree::
   :hidden:

   commentary
