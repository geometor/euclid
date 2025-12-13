:order: 23
:number: 209
:type: prop
:dependencies: V.11, V.15, V.16, V.21




.. picture:: V.23.graphic.inverted.png

.. _V.23:

V.23
====

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio
          ex aequali.

Let there be three magnitudes ``A``, ``B``, ``C``, and others equal to them in multitude, which, taken two and two together, are in the same proportion, namely ``D``, ``E``, ``F``; and let the proportion of them be perturbed, so that,


.. container:: center

   as ``A`` is to ``B``, so is ``E`` to ``F``,


and, as ``B`` is to ``C``, so is ``D`` to ``E``; I say that, as ``A`` is to ``C``, so is ``D`` to ``F``.

Of ``A``, ``B``, ``D`` let equimultiples ``G``, ``H``, ``K`` be taken, and of ``C``, ``E``, ``F`` other, chance, equimultiples ``L``, ``M``, ``N``.

Then, since ``G``, ``H`` are equimultiples of ``A``, ``B``, and parts have the same ratio as the same multiples of them, [:ref:`V.15 <V.15>`]


.. container:: center

   therefore, as ``A`` is to ``B``, so is ``G`` to ``H``.


For the same reason also,


.. container:: center

   as ``E`` is to ``F``, so is ``M`` to ``N``.


And, as ``A`` is to ``B``, so is ``E`` to ``F``;


.. container:: center

   therefore also, as ``G`` is to ``H``, so is ``M`` to ``N``. [:ref:`V.11 <V.11>`]


Next, since, as ``B`` is to ``C``, so is ``D`` to ``E``, alternately, also, as ``B`` is to ``D``, so is ``C`` to ``E``. [:ref:`V.16 <V.16>`]

And, since ``H``, ``K`` are equimultiples of ``B``, ``D``, and parts have the same ratio as their equimultiples,


.. container:: center

   therefore, as ``B`` is to ``D``, so is ``H`` to ``K``. [:ref:`V.15 <V.15>`]


But, as ``B`` is to ``D``, so is ``C`` to ``E``;


.. container:: center

   therefore also, as ``H`` is to ``K``, so is ``C`` to ``E``. [:ref:`V.11 <V.11>`]


Again, since ``L``, ``M`` are equimultiples of ``C``, ``E``,


.. container:: center

   therefore, as ``C`` is to ``E``, so is ``L`` to ``M``. [:ref:`V.15 <V.15>`]


But, as ``C`` is to ``E``, so is ``H`` to ``K``;


.. container:: center

   therefore also, as ``H`` is to ``K``, so is ``L`` to ``M``, [:ref:`V.11 <V.11>`]


and, alternately, as ``H`` is to ``L``, so is ``K`` to ``M``. [:ref:`V.16 <V.16>`]

But it was also proved that,


.. container:: center

   as ``G`` is to ``H``, so is ``M`` to ``N``.


Since, then, there are three magnitudes ``G``, ``H``, ``L``, and others equal to them in multitude ``K``, ``M``, ``N``, which taken two and two together are in the same ratio, and the proportion of them is perturbed, therefore, ex aequali, if ``G`` is in excess of ``L``, ``K`` is also in excess of ``N``; if equal, equal; and if less, less. [:ref:`V.21 <V.21>`]

And ``G``, ``K`` are equimultiples of ``A``, ``D``, and ``L``, ``N`` of ``C``, ``F``.

Therefore, as ``A`` is to ``C``, so is ``D`` to ``F``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.15" [fillcolor="#222244", URL="/heath/V/15/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.22" [fillcolor="#222244", URL="/heath/V/22/", target="_top"];
     "V.11" [fillcolor="#222244", URL="/heath/V/11/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "V.12" [fillcolor="#222244", URL="/heath/V/12/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "V.20" [fillcolor="#222244", URL="/heath/V/20/", target="_top"];
     "V.18" [fillcolor="#222244", URL="/heath/V/18/", target="_top"];
     "V.14" [fillcolor="#222244", URL="/heath/V/14/", target="_top"];
     "V.23" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/V/23/", target="_top"];
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "V.4" [fillcolor="#222244", URL="/heath/V/4/", target="_top"];
     "V.13" [fillcolor="#222244", URL="/heath/V/13/", target="_top"];
     "V.16" [fillcolor="#222244", URL="/heath/V/16/", target="_top"];
     "V.21" [fillcolor="#222244", URL="/heath/V/21/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "V.3" [fillcolor="#222244", URL="/heath/V/3/", target="_top"];
     "V.17" [fillcolor="#222244", URL="/heath/V/17/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "V.16" -> "V.15";
     "V.23" -> "V.15";
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.22" -> "V.def.5";
     "V.16" -> "V.22";
     "V.16" -> "V.11";
     "V.18" -> "V.11";
     "V.23" -> "V.11";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.15" -> "V.12";
     "V.8" -> "V.def.4";
     "V.16" -> "V.20";
     "V.22" -> "V.20";
     "V.16" -> "V.18";
     "V.16" -> "V.14";
     "V.18" -> "V.14";
     "V.16" -> "V.23";
     "V.3" -> "V.2";
     "V.17" -> "V.2";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.17" -> "V.1";
     "V.22" -> "V.4";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.23" -> "V.16";
     "V.16" -> "V.21";
     "V.23" -> "V.21";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "V.4" -> "V.3";
     "V.16" -> "V.17";
     "V.18" -> "V.17";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
   }



Required for
------------

:ref:`V.16`, :ref:`V.19`, :ref:`V.25`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`, :ref:`VIII.5`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.115`, :ref:`X.14`, :ref:`X.19`, :ref:`X.20`, :ref:`X.21`, :ref:`X.22`, :ref:`X.23`, :ref:`X.24`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XI.17`, :ref:`XI.23`, :ref:`XI.27`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.1`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.13`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.2`, :ref:`XIII.4`, :ref:`XIII.5`, :ref:`XIII.6`, :ref:`XIII.8`, :ref:`XIII.9`