:canonical_id: IX.14
:volume: II
:book: IX
:proposition: 14
:type: proposition
:title: Proposition IX.14
:folios: 0408, 0409
:pages: 402, 403
:dependencies: VII.30

.. _IX.14:

.. folio:: 0408
   :page: 402

PROPOSITION 14.
===============

.. enunciation::

   If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

For let the number :g:`A <0409.g1:A>` be the least that is measured by the prime numbers :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>` ;

.. _folio-ii-0409:

.. folio:: 0409
   :page: 403

I say that :g:`A <0409.g1:A>` will not be measured by any other prime number except :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>`.

For, if possible, let it be measured by the prime number :g:`E <0409.g1:E>`, and let :g:`E <0409.g1:E>` not be the same with any one of the numbers :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>`.

.. picture:: 0409.g1.svg
   :alt: Proposition 14 diagram

.. subclause::

   Now, since :g:`E <0409.g1:E>` measures :g:`A <0409.g1:A>`, let it measure it according to :g:`F <0409.g1:F>` ;

.. assertion::

   therefore :g:`E <0409.g1:E>` by multiplying :g:`F <0409.g1:F>` has made :g:`A <0409.g1:A>`.

.. subclause::

   And :g:`A <0409.g1:A>` is measured by the prime numbers :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>`.

.. subclause::

   But, if two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers ; :just:`[VII. 30] <VII.30>`

.. assertion::

   therefore :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>` will measure one of the numbers :g:`E <0409.g1:E>`, :g:`F <0409.g1:F>`.

.. subclause::

   Now they will not measure :g:`E <0409.g1:E>` ; for :g:`E <0409.g1:E>` is prime and not the same with any one of the numbers :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>`.

.. assertion::

   Therefore they will measure :g:`F <0409.g1:F>`, which is less than :g:`A <0409.g1:A>` : which is impossible, for :g:`A <0409.g1:A>` is by hypothesis the least number measured by :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>`.

.. assertion::

   Therefore no prime number will measure :g:`A <0409.g1:A>` except :g:`B <0409.g1:B>`, :g:`C <0409.g1:C>`, :g:`D <0409.g1:D>`.

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
     "V.def.4" [label="V.def.4", fillcolor="#224422", tooltip="V.def.4: Magnitudes are said to have a ratio to one another which are capable, when multiplied, of exceeding one another.", URL="../../../book_v/definitions/index.html#v-def-4", target="_top"];
     "V.def.5" [label="V.def.5", fillcolor="#224422", tooltip="V.def.5: Magnitudes are said to be in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any…", URL="../../../book_v/definitions/index.html#v-def-5", target="_top"];
     "V.def.7" [label="V.def.7", fillcolor="#224422", tooltip="V.def.7: When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then…", URL="../../../book_v/definitions/index.html#v-def-7", target="_top"];
     "V.1" [label="V.1", fillcolor="#222244", tooltip="V.1: If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one…", URL="../../../book_v/propositions/01/index.html", target="_top"];
     "V.7" [label="V.7", fillcolor="#222244", tooltip="V.7: Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", URL="../../../book_v/propositions/07/index.html", target="_top"];
     "V.8" [label="V.8", fillcolor="#222244", tooltip="V.8: Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", URL="../../../book_v/propositions/08/index.html", target="_top"];
     "V.9" [label="V.9", fillcolor="#222244", tooltip="V.9: Magnitudes which have the same ratio to the same are equal to one another ; and magnitudes to which the same has the same ratio are equal.", URL="../../../book_v/propositions/09/index.html", target="_top"];
     "VII.def.12" [label="VII.def.12", fillcolor="#224422", tooltip="VII.def.12: Numbers prime to one another are those which are measured by an unit alone as a common measure.", URL="../../../book_vii/definitions/index.html#vii-def-12", target="_top"];
     "VII.def.15" [label="VII.def.15", fillcolor="#224422", tooltip="VII.def.15: A number is said to multiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", URL="../../../book_vii/definitions/index.html#vii-def-15", target="_top"];
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
     "VII.17" [label="VII.17", fillcolor="#222244", tooltip="VII.17: If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", URL="../../../book_vii/propositions/17/index.html", target="_top"];
     "VII.18" [label="VII.18", fillcolor="#222244", tooltip="VII.18: If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", URL="../../../book_vii/propositions/18/index.html", target="_top"];
     "VII.19" [label="VII.19", fillcolor="#222244", tooltip="VII.19: If four numbers be proportional, the number produced from the first and fourth will be equal to the number produced from the second and third; and, if the number produced from the…", URL="../../../book_vii/propositions/19/index.html", target="_top"];
     "VII.20" [label="VII.20", fillcolor="#222244", tooltip="VII.20: The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", URL="../../../book_vii/propositions/20/index.html", target="_top"];
     "VII.21" [label="VII.21", fillcolor="#222244", tooltip="VII.21: Numbers prime to one another are the least of those which have the same ratio with them.", URL="../../../book_vii/propositions/21/index.html", target="_top"];
     "VII.29" [label="VII.29", fillcolor="#222244", tooltip="VII.29: Any prime number is prime to any number which it does not measure.", URL="../../../book_vii/propositions/29/index.html", target="_top"];
     "VII.30" [label="VII.30", fillcolor="#222244", tooltip="VII.30: If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.", URL="../../../book_vii/propositions/30/index.html", target="_top"];
     "IX.14" [label="IX.14", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="IX.14: If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.", URL="index.html", target="_top"];
     "V.8" -> "V.def.4";
     "V.7" -> "V.def.5";
     "V.8" -> "V.def.7";
     "V.8" -> "V.1";
     "VII.19" -> "V.7";
     "V.9" -> "V.8";
     "VII.19" -> "V.9";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.30" -> "VII.def.15";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
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
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VII.16" -> "VII.15";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.19" -> "VII.18";
     "VII.30" -> "VII.19";
     "VII.21" -> "VII.20";
     "VII.30" -> "VII.20";
     "VII.30" -> "VII.21";
     "VII.30" -> "VII.29";
     "IX.14" -> "VII.30";
   }

----

See :ref:`Commentary on Proposition IX.14 <IX.14.commentary>`.

.. toctree::
   :hidden:

   commentary
