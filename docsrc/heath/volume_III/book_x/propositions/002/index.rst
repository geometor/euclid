:canonical_id: X.2
:volume: III
:book: X
:proposition: 2
:type: proposition
:title: Proposition X.2
:folios: 0021
:pages: 17
:dependencies: X.def.1

.. _X.2:

.. _folio-iii-0021:

.. folio:: 0021
   :page: 17

PROPOSITION 2.
==============

.. enunciation::

   If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be incommensurable.

For, there being two unequal magnitudes :g:`AB <0021.g1:/ A B />`, :g:`CD <0021.g1:/ C D />`, and :g:`AB <0021.g1:/ A B />` being the less, when the less is continually subtracted in turn from the greater, let that which is left over never measure the one before it; I say that the magnitudes :g:`AB <0021.g1:/ A B />`, :g:`CD <0021.g1:/ C D />` are incommensurable.

.. picture:: 0021.g1.svg
   :alt: Book X, Proposition 2

For, if they are commensurable, some magnitude will measure them.

Let a magnitude measure them, if possible, and let it be :g:`E <0021.g1:E>`; let :g:`AB <0021.g1:/ A B />`, measuring :g:`FD <0021.g1:/ F D />`, leave :g:`CF <0021.g1:/ C F />` less than itself, let :g:`CF <0021.g1:/ C F />` measuring :g:`BG <0021.g1:/ B G />`, leave :g:`AG <0021.g1:/ A G />` less than itself, and let this process be repeated continually, until there is left some magnitude which is less than :g:`E <0021.g1:E>`.

Suppose this done, and let there be left :g:`AG <0021.g1:/ A G />` less than :g:`E <0021.g1:E>`.

.. subclause::

   Then, since :g:`E <0021.g1:E>` measures :g:`AB <0021.g1:/ A B />`, while :g:`AB <0021.g1:/ A B />` measures :g:`DF <0021.g1:/ D F />`,

.. assertion::

   therefore :g:`E <0021.g1:E>` will also measure :g:`FD <0021.g1:/ F D />`.

.. subclause::

   But it measures the whole :g:`CD <0021.g1:/ C D />` also;

.. assertion::

   therefore it will also measure the remainder :g:`CF <0021.g1:/ C F />`.

.. subclause::

   But :g:`CF <0021.g1:/ C F />` measures :g:`BG <0021.g1:/ B G />`;

.. assertion::

   therefore :g:`E <0021.g1:E>` also measures :g:`BG <0021.g1:/ B G />`.

.. subclause::

   But it measures the whole :g:`AB <0021.g1:/ A B />` also;

.. assertion::

   therefore it will also measure the remainder :g:`AG <0021.g1:/ A G />`, the greater the less :

.. assertion::

   which is impossible.

.. assertion::

   Therefore no magnitude will measure the magnitudes :g:`AB <0021.g1:/ A B />`, :g:`CD <0021.g1:/ C D />`; therefore the magnitudes :g:`AB <0021.g1:/ A B />`, :g:`CD <0021.g1:/ C D />` are incommensurable. :just:`[x. Def. 1] <X.def.1>`

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
     "X.def.1" [label="X.def.1", fillcolor="#224422", tooltip="X.def.1: Those magnitudes are said to be commensurable which are measured by the same measure, and those incommensurable which cannot have any common measure.", URL="../../definitions/index.html#x-def-1", target="_top"];
     "X.2" [label="X.2", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", tooltip="X.2: If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be…", URL="index.html", target="_top"];
     "X.2" -> "X.def.1";
   }

Required for
------------

:ref:`X.3 <X.3>`, :ref:`X.4 <X.4>`

----

See :ref:`Commentary on Proposition X.2 <X.2.commentary>`.

.. toctree::
   :hidden:

   commentary
