:order: 24
:number: 210
:type: prop
:dependencies: V.18, V.22




.. picture:: V.24.graphic.inverted.png

.. _V.24:

V.24
====

   If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

Let a first magnitude ``AB`` have to a second ``C`` the same ratio as a third ``DE`` has to a fourth ``F``; and let also a fifth ``BG`` have to

the second ``C`` the same ratio as a sixth ``EH`` has to the fourth ``F``; I say that the first and fifth added together, ``AG``, will have to the second ``C`` the same ratio as the third and sixth, ``DH``, has to the fourth ``F``.

For since, as ``BG`` is to ``C``, so is ``EH`` to ``F``, inversely, as ``C`` is to ``BG``, so is ``F`` to ``EH``.

Since, then, as ``AB`` is to ``C``, so is ``DE`` to ``F``,


.. container:: center

   and, as ``C`` is to ``BG``, so is ``F`` to ``EH``,


therefore, ex aequali, as ``AB`` is to ``BG``, so is ``DE`` to ``EH``. [:ref:`V.22 <V.22>`]

And, since the magnitudes are proportional separando, they will also be proportional componendo; [:ref:`V.18 <V.18>`]


.. container:: center

   therefore, as ``AG`` is to ``GB``, so is ``DH`` to ``HE``.


But also, as ``BG`` is to ``C``, so is ``EH`` to ``F``; therefore, ex aequali, as ``AG`` is to ``C``, so is ``DH`` to ``F``. [:ref:`V.22 <V.22>`]

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.22" [fillcolor="#222244", URL="/heath/V/22/", target="_top"];
     "V.11" [fillcolor="#222244", URL="/heath/V/11/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "V.20" [fillcolor="#222244", URL="/heath/V/20/", target="_top"];
     "V.24" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/V/24/", target="_top"];
     "V.18" [fillcolor="#222244", URL="/heath/V/18/", target="_top"];
     "V.14" [fillcolor="#222244", URL="/heath/V/14/", target="_top"];
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "V.4" [fillcolor="#222244", URL="/heath/V/4/", target="_top"];
     "V.13" [fillcolor="#222244", URL="/heath/V/13/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "V.3" [fillcolor="#222244", URL="/heath/V/3/", target="_top"];
     "V.17" [fillcolor="#222244", URL="/heath/V/17/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.22" -> "V.def.5";
     "V.24" -> "V.22";
     "V.18" -> "V.11";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.8" -> "V.def.4";
     "V.22" -> "V.20";
     "V.24" -> "V.18";
     "V.18" -> "V.14";
     "V.3" -> "V.2";
     "V.17" -> "V.2";
     "V.8" -> "V.1";
     "V.17" -> "V.1";
     "V.22" -> "V.4";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.10" -> "V.7";
     "V.4" -> "V.3";
     "V.18" -> "V.17";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
   }
