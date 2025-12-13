:order: 10
:number: 118
:type: prop
:tags: circle
:dependencies: I.def.15, III.1.p.1, III.5




.. picture:: III.10.graphic.inverted.png

.. _III.10:

III.10
======

   A circle does not cut a circle at more points than two.

``A circle does not cut a circle at more points than two``.

For, if possible, let the circle ``ABC`` cut the circle ``DEF`` at more points than two, namely ``B``, ``C``, ``F``, ``H``;

let ``BH``, ``BG`` be joined and bisected at the points ``K``, ``L``, and from ``K``, ``L`` let ``KC``, ``LM`` be drawn at right angles to ``BH``, ``BG`` and carried through to the points ``A``, ``E``.

Then, since in the circle ``ABC`` a straight line ``AC`` cuts a straight line ``BH`` into two equal parts and at right angles,


.. container:: center

   the centre of the circle ``ABC`` is on ``AC``. [:ref:`III.1.p.1 <III.1.p.1>`]


Again, since in the same circle ``ABC`` a straight line ``NO`` cuts a straight line ``BG`` into two equal parts and at right angles,


.. container:: center

   the centre of the circle ``ABC`` is on ``NO``.


But it was also proved to be on ``AC``, and the straight lines ``AC``, ``NO`` meet at no point except at ``P``;


.. container:: center

   therefore the point ``P`` is the centre of the circle ``ABC``.


Similarly we can prove that ``P`` is also the centre of the circle ``DEF``;


.. container:: center

   therefore the two circles ``ABC``, ``DEF`` which cut one another have the same centre ``P``: which is impossible. [:ref:`III.5 <III.5>`]


Therefore etc. Q. E. D.
The word circle (κύκλος) is here employed in the unusual sense of the ``circumference`` (περιφέρεια) of a circle. Cf. note on :ref:`I.def.15 <I.def.15>`.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "III.5" [fillcolor="#222244", URL="/heath/III/5/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "III.10" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/III/10/", target="_top"];
     "III.1.p.1" [fillcolor="#333333"];
     "III.10" -> "III.5";
     "III.5" -> "I.def.15";
     "III.10" -> "I.def.15";
     "III.10" -> "III.1.p.1";
   }



Required for
------------

:ref:`III.24`, :ref:`III.26`, :ref:`III.27`, :ref:`III.28`, :ref:`III.29`, :ref:`III.30`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.16`, :ref:`VI.33`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.18`, :ref:`XIII.8`, :ref:`XIII.9`