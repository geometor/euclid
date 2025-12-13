:order: 6
:number: 192
:type: prop
:dependencies: V.2




.. picture:: V.6.graphic.inverted.png

.. _V.6:

V.6
===

   If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

For let two magnitudes ``AB``, ``CD`` be equimultiples of two magnitudes ``E``, ``F``, and let ``AG``, ``CH`` subtracted from them be equimultiples of the same two ``E``, ``F``;

I say that the remainders also, ``GB``, ``HD``, are either equal to ``E``, ``F`` or equimultiples of them.

For, first, let ``GB`` be equal to ``E``; I say that ``HD`` is also equal to ``F``.

For let ``CK`` be made equal to ``F``.

Since ``AG`` is the same multiple of ``E`` that ``CH`` is of ``F``, while ``GB`` is equal to ``E`` and ``KC`` to ``F``, therefore ``AB`` is the same multiple of ``E`` that ``KH`` is of ``F``. [:ref:`V.2 <V.2>`]

But, by hypothesis, ``AB`` is the same multiple of ``E`` that ``CD`` is of ``F``; therefore ``KH`` is the same multiple of ``F`` that ``CD`` is of ``F``.

Since then each of the magnitudes ``KH``, ``CD`` is the same multiple of ``F``,


.. container:: center

   therefore ``KH`` is equal to ``CD``.


Let ``CH`` be subtracted from each; therefore the remainder ``KC`` is equal to the remainder ``HD``.

But ``F`` is equal to ``KC``; therefore ``HD`` is also equal to ``F``.

Hence, if ``GB`` is equal to ``E``, ``HD`` is also equal to ``F``.

Similarly we can prove that, even if ``GB`` be a multiple of ``E``, ``HD`` is also the same multiple of ``F``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.6" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/V/6/", target="_top"];
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.6" -> "V.2";
   }
