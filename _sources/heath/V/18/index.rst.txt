:order: 18
:number: 204
:type: prop
:dependencies: V.11, V.14, V.17




.. picture:: V.18.graphic.inverted.png

.. _V.18:

V.18
====

   If magnitudes be proportional
          separando, they will also be proportional
          componendo.

Let ``AE``, ``EB``, ``CF``, ``FD`` be magnitudes proportional separando, so that, as ``AE`` is to ``EB``, so is ``CF`` to ``FD``;

I say that they will also be proportional componendo, that is, as ``AB`` is to ``BE``, so is ``CD`` to ``FD``.

For, if ``CD`` be not to ``DF`` as ``AB`` to ``BE``, then, as ``AB`` is to ``BE``, so will ``CD`` be either to some magnitude less than ``DF`` or to a greater.

First, let it be in that ratio to a less magnitude ``DG``.

Then, since, as ``AB`` is to ``BE``, so is ``CD`` to ``DG``, they are magnitudes proportional componendo;


.. container:: center

   so that they will also be proportional separando. [:ref:`V.17 <V.17>`]


Therefore, as ``AE`` is to ``EB``, so is ``CG`` to ``GD``.

But also, by hypothesis,


.. container:: center

   as ``AE`` is to ``EB``, so is ``CF`` to ``FD``.


Therefore also, as ``CG`` is to ``GD``, so is ``CF`` to ``FD``. [:ref:`V.11 <V.11>`]

But the first ``CG`` is greater than the third ``CF``;


.. container:: center

   therefore the second ``GD`` is also greater than the fourth ``FD``. [:ref:`V.14 <V.14>`]


But it is also less: which is impossible.

Therefore, as ``AB`` is to ``BE``, so is not ``CD`` to a less magnitude than ``FD``.

Similarly we can prove that neither is it in that ratio to a greater;


.. container:: center

   it is therefore in that ratio to ``FD`` itself.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.11" [fillcolor="#222244", URL="/heath/V/11/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "V.18" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/V/18/", target="_top"];
     "V.13" [fillcolor="#222244", URL="/heath/V/13/", target="_top"];
     "V.14" [fillcolor="#222244", URL="/heath/V/14/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "V.17" [fillcolor="#222244", URL="/heath/V/17/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "V.17" -> "V.2";
     "V.8" -> "V.1";
     "V.17" -> "V.1";
     "V.7" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.18" -> "V.11";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.8" -> "V.def.4";
     "V.14" -> "V.13";
     "V.18" -> "V.14";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.10" -> "V.7";
     "V.18" -> "V.17";
     "V.14" -> "V.10";
   }



Required for
------------

:ref:`V.16`, :ref:`V.19`, :ref:`V.23`, :ref:`V.24`, :ref:`V.25`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`, :ref:`VIII.5`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.115`, :ref:`X.14`, :ref:`X.19`, :ref:`X.20`, :ref:`X.21`, :ref:`X.22`, :ref:`X.23`, :ref:`X.24`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XI.17`, :ref:`XI.23`, :ref:`XI.27`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.1`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.13`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.2`, :ref:`XIII.4`, :ref:`XIII.5`, :ref:`XIII.6`, :ref:`XIII.8`, :ref:`XIII.9`