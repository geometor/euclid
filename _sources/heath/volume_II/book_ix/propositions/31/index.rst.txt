:canonical_id: IX.31
:volume: II
:book: IX
:proposition: 31
:type: proposition
:title: Proposition IX.31
:folios: 0423, 0424
:pages: 417, 418
:dependencies: IX.30

.. _IX.31:

.. folio:: 0423
   :page: 417

PROPOSITION 31.
===============

.. enunciation::

   If an odd number be prime to any number, it will also be prime to the double of it.

For let the odd number :g:`A <0423.g2:A>` be prime to any number :g:`B <0423.g2:B>`, and let :g:`C <0423.g2:C>` be double of :g:`B <0423.g2:B>`;

I say that :g:`A <0423.g2:A>` is prime to :g:`C <0423.g2:C>`.

.. picture:: 0423.g2.svg
   :alt: Book IX, Proposition 31

For, if they are not prime to one another, some number will measure them.

.. _folio-ii-0424:

.. folio:: 0424
   :page: 418

Let a number measure them, and let it be :g:`D <0423.g2:D>`.

.. subclause::

   Now :g:`A <0423.g2:A>` is odd;

.. assertion::

   therefore :g:`D <0423.g2:D>` is also odd.

.. subclause::

   And since :g:`D <0423.g2:D>` which is odd measures :g:`C <0423.g2:C>`, and :g:`C <0423.g2:C>` is even,

.. assertion:: [IX. 30] <IX.30>

   therefore [:g:`D <0423.g2:D>`] will measure the half of :g:`C <0423.g2:C>` also.

.. subclause::

   But :g:`B <0423.g2:B>` is half of :g:`C <0423.g2:C>`;

.. assertion::

   therefore :g:`D <0423.g2:D>` measures :g:`B <0423.g2:B>`.

.. subclause::

   But it also measures :g:`A <0423.g2:A>`;

.. assertion::

   therefore :g:`D <0423.g2:D>` measures :g:`A <0423.g2:A>`, :g:`B <0423.g2:B>` which are prime to one another: which is impossible.

.. assertion::

   Therefore :g:`A <0423.g2:A>` cannot but be prime to :g:`C <0423.g2:C>`.

.. assertion::

   Therefore :g:`A <0423.g2:A>`, :g:`C <0423.g2:C>` are prime to one another.

.. qed::

   :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "VII.def.6" [label="VII.def.6", fillcolor="#224422", tooltip="VII.def.6: An even number is that which is divisible into two equal parts.", URL="../../../book_vii/definitions/index.html#vii-def-6", target="_top"];
     "VII.def.7" [label="VII.def.7", fillcolor="#224422", tooltip="VII.def.7: An odd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", URL="../../../book_vii/definitions/index.html#vii-def-7", target="_top"];
     "IX.21" [label="IX.21", fillcolor="#222244", tooltip="IX.21: If as many even numbers as we please be added together, the whole is even.", URL="../21/index.html", target="_top"];
     "IX.22" [label="IX.22", fillcolor="#222244", tooltip="IX.22: If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.", URL="../22/index.html", target="_top"];
     "IX.23" [label="IX.23", fillcolor="#222244", tooltip="IX.23: If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.", URL="../23/index.html", target="_top"];
     "IX.30" [label="IX.30", fillcolor="#222244", tooltip="IX.30: If an odd number measure an even number, it will also measure the half of it.", URL="../30/index.html", target="_top"];
     "IX.31" [label="IX.31", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.31: If an odd number be prime to any number, it will also be prime to the double of it.", URL="index.html", target="_top"];
     "IX.21" -> "VII.def.6";
     "IX.22" -> "VII.def.7";
     "IX.23" -> "VII.def.7";
     "IX.22" -> "IX.21";
     "IX.23" -> "IX.21";
     "IX.23" -> "IX.22";
     "IX.30" -> "IX.23";
     "IX.31" -> "IX.30";
   }
