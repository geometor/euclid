:canonical_id: IX.17
:volume: II
:book: IX
:proposition: 17
:type: proposition
:title: Proposition IX.17
:folios: 0412, 0413
:pages: 406, 407
:dependencies: VII.13, VII.20, VII.21

.. _IX.17:

.. folio:: 0412
   :page: 406

PROPOSITION 17.
===============

.. enunciation::

   If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the second.

For let there be as many numbers as we please, :g:`$A$ <0412.g2:A>`, :g:`$B$ <0412.g2:B>`, :g:`$C$ <0412.g2:C>`, :g:`$D$ <0412.g2:D>`, in continued proportion, and let the extremes of them, :g:`$A$ <0412.g2:A>`, :g:`$D$ <0412.g2:D>`, be prime to one another ;

I say that :g:`$D$ <0412.g2:D>` is not to any other number as :g:`$A$ <0412.g2:A>` is to :g:`$B$ <0412.g2:B>`.

.. picture:: 0412.g2.svg
   :alt: Proposition 17

For, if possible, as :g:`$A$ <0412.g2:A>` is to :g:`$B$ <0412.g2:B>`, so let :g:`$D$ <0412.g2:D>` be to :g:`$E$ <0412.g2:E>` ;

.. assertion:: [VII. 13] <VII.13>

   therefore, alternately, as :g:`$A$ <0412.g2:A>` is to :g:`$D$ <0412.g2:D>`, so is :g:`$B$ <0412.g2:B>` to :g:`$E$ <0412.g2:E>`.

.. _folio-ii-0413:

.. folio:: 0413
   :page: 407

.. subclause::

   But :g:`$A$ <0412.g2:A>`, :g:`$D$ <0412.g2:D>` are prime, primes are also least, :just:`[VII. 21] <VII.21>` and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent. :just:`[VII. 20] <VII.20>`

.. assertion::

   Therefore :g:`$A$ <0412.g2:A>` measures :g:`$B$ <0412.g2:B>`.

.. subclause::

   And, as :g:`$A$ <0412.g2:A>` is to :g:`$B$ <0412.g2:B>`, so is :g:`$B$ <0412.g2:B>` to :g:`$C$ <0412.g2:C>`.

.. assertion::

   Therefore :g:`$B$ <0412.g2:B>` also measures :g:`$C$ <0412.g2:C>` ; so that :g:`$A$ <0412.g2:A>` also measures :g:`$C$ <0412.g2:C>`.

.. subclause::

   And since, as :g:`$B$ <0412.g2:B>` is to :g:`$C$ <0412.g2:C>`, so is :g:`$C$ <0412.g2:C>` to :g:`$D$ <0412.g2:D>`, and :g:`$B$ <0412.g2:B>` measures :g:`$C$ <0412.g2:C>`,

.. assertion::

   therefore :g:`$C$ <0412.g2:C>` also measures :g:`$D$ <0412.g2:D>`.

.. subclause::

   But :g:`$A$ <0412.g2:A>` measured :g:`$C$ <0412.g2:C>` ;

.. assertion::

   so that :g:`$A$ <0412.g2:A>` also measures :g:`$D$ <0412.g2:D>`.

.. subclause::

   But it also measures itself ;

.. assertion::

   therefore :g:`$A$ <0412.g2:A>` measures :g:`$A$ <0412.g2:A>`, :g:`$D$ <0412.g2:D>` which are prime to one another : which is impossible.

.. assertion::

   Therefore :g:`$D$ <0412.g2:D>` will not be to any other number as :g:`$A$ <0412.g2:A>` is to :g:`$B$ <0412.g2:B>`.

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
     "IX.17" [label="IX.17", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.17: If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the…", URL="index.html", target="_top"];
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
     "IX.17" -> "VII.13";
     "VII.16" -> "VII.15";
     "VII.21" -> "VII.16";
     "VII.21" -> "VII.20";
     "IX.17" -> "VII.20";
     "IX.17" -> "VII.21";
   }

Required for
------------

:ref:`IX.19 <IX.19>`

----

See :ref:`Commentary on Proposition IX.17 <IX.17.commentary>`.

.. toctree::
   :hidden:

   commentary
