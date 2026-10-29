:canonical_id: IX.16
:volume: II
:book: IX
:proposition: 16
:type: proposition
:title: Proposition IX.16
:folios: 0412
:pages: 406
:dependencies: VII.20, VII.21

.. _IX.16:

.. _folio-ii-0412:

.. folio:: 0412
   :page: 406

PROPOSITION 16.
===============

.. enunciation::

   If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

For let the two numbers :g:`A <0412.g1:A>`, :g:`B <0412.g1:B>` be prime to one another ;

I say that :g:`B <0412.g1:B>` is not to any other number as :g:`A <0412.g1:A>` is to :g:`B <0412.g1:B>`.

.. picture:: 0412.g1.svg
   :alt: Proposition 16

For, if possible, as :g:`A <0412.g1:A>` is to :g:`B <0412.g1:B>`, so let :g:`B <0412.g1:B>` be to :g:`C <0412.g1:C>`.

.. subclause::

   Now :g:`A <0412.g1:A>`, :g:`B <0412.g1:B>` are prime, primes are also least, :just:`[VII. 21] <VII.21>` and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent ; :just:`[VII. 20] <VII.20>`

.. assertion::

   therefore :g:`A <0412.g1:A>` measures :g:`B <0412.g1:B>` as antecedent antecedent.

.. subclause::

   But it also measures itself ;

.. assertion::

   therefore :g:`A <0412.g1:A>` measures :g:`A <0412.g1:A>`, :g:`B <0412.g1:B>` which are prime to one another : which is absurd.

.. assertion::

   Therefore :g:`B <0412.g1:B>` will not be to :g:`C <0412.g1:C>`, as :g:`A <0412.g1:A>` is to :g:`B <0412.g1:B>`.

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
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../../book_vii/definitions/index.html#vii-def-12", target="_top"];
     "VII.def.20" [label="VII.def.20", fillcolor="#224422", tooltip="VII.def.20: Numbers are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", URL="../../../book_vii/definitions/index.html#vii-def-20", target="_top"];
     "VII.1" [label="VII.1", fillcolor="#222244", tooltip="VII.1: Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit…", URL="../../../book_vii/propositions/01/index.html", target="_top"];
     "VII.2" [label="VII.2", fillcolor="#222244", tooltip="VII.2: Given two numbers not prime to one another, to find their greatest common measure.", URL="../../../book_vii/propositions/02/index.html", target="_top"];
     "VII.4" [label="VII.4", fillcolor="#222244", tooltip="VII.4: Any number is either a part or parts of any number, the less of the greater.", URL="../../../book_vii/propositions/04/index.html", target="_top"];
     "VII.5" [label="VII.5", fillcolor="#222244", tooltip="VII.5: If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", URL="../../../book_vii/propositions/05/index.html", target="_top"];
     "VII.6" [label="VII.6", fillcolor="#222244", tooltip="VII.6: If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", URL="../../../book_vii/propositions/06/index.html", target="_top"];
     "VII.9" [label="VII.9", fillcolor="#222244", tooltip="VII.9: If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts…", URL="../../../book_vii/propositions/09/index.html", target="_top"];
     "VII.10" [label="VII.10", fillcolor="#222244", tooltip="VII.10: If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part…", URL="../../../book_vii/propositions/10/index.html", target="_top"];
     "VII.12" [label="VII.12", fillcolor="#222244", tooltip="VII.12: If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", URL="../../../book_vii/propositions/12/index.html", target="_top"];
     "VII.13" [label="VII.13", fillcolor="#222244", tooltip="VII.13: If four numbers be proportional, they will also be proportional alternately.", URL="../../../book_vii/propositions/13/index.html", target="_top"];
     "VII.15" [label="VII.15", fillcolor="#222244", tooltip="VII.15: If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of…", URL="../../../book_vii/propositions/15/index.html", target="_top"];
     "VII.16" [label="VII.16", fillcolor="#222244", tooltip="VII.16: If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.", URL="../../../book_vii/propositions/16/index.html", target="_top"];
     "VII.20" [label="VII.20", fillcolor="#222244", tooltip="VII.20: The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", URL="../../../book_vii/propositions/20/index.html", target="_top"];
     "VII.21" [label="VII.21", fillcolor="#222244", tooltip="VII.21: Numbers prime to one another are the least of those which have the same ratio with them.", URL="../../../book_vii/propositions/21/index.html", target="_top"];
     "IX.16" [label="IX.16", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.16: If two numbers be prime to one another, the second will not be to any other number as the first is to the second.", URL="index.html", target="_top"];
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.2" -> "VII.1";
     "VII.4" -> "VII.2";
     "VII.20" -> "VII.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.10" -> "VII.9";
     "VII.13" -> "VII.10";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.20" -> "VII.13";
     "VII.16" -> "VII.15";
     "VII.21" -> "VII.16";
     "VII.21" -> "VII.20";
     "IX.16" -> "VII.20";
     "IX.16" -> "VII.21";
   }

Required for
------------

:ref:`IX.18 <IX.18>`

----

See :ref:`Commentary on Proposition IX.16 <IX.16.commentary>`.

.. toctree::
   :hidden:

   commentary
