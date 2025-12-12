:order: 4
:number: 220
:type: prop
:tags: triangle
:dependencies: I.17, I.28, I.34, I.post.5, V.16, V.22, VI.2




.. picture:: VI.4.graphic.inverted.png

.. _VI.4:

VI.4
====

   In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

Let ``ABC``, ``DCE`` be equiangular triangles having the angle ``ABC`` equal to the angle ``DCE``, the angle ``BAC`` to the angle ``CDE``, and further the angle ``ACB`` to the angle ``CED``; I say that in the triangles ``ABC``, ``DCE`` the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

For let ``BC`` be placed in a straight line with ``CE``.

Then, since the angles ``ABC``, ``ACB`` are less than two right angles, [:ref:`I.17 <I.17>`] and the angle ``ACB`` is equal to the angle ``DEC``, therefore the angles ``ABC``, ``DEC`` are less than two right angles; therefore ``BA``, ``ED``, when produced, will meet. [:ref:`I.post.5 <I.post.5>`]

Let them be produced and meet at ``F``.

Now, since the angle ``DCE`` is equal to the angle ``ABC``,


.. container:: center

   ``BF`` is parallel to ``CD``. [:ref:`I.28 <I.28>`]


Again, since the angle ``ACB`` is equal to the angle ``DEC``,


.. container:: center

   ``AC`` is parallel to ``FE``. [:ref:`I.28 <I.28>`]


Therefore ``FACD`` is a parallelogram; therefore ``FA`` is equal to ``DC``, and ``AC`` to ``FD``. [:ref:`I.34 <I.34>`]

And, since ``AC`` has been drawn parallel to ``FE``, one side of the triangle ``FBE``, therefore, as ``BA`` is to ``AF``, so is ``BC`` to ``CE``. [:ref:`VI.2 <VI.2>`]

But ``AF`` is equal to ``CD``;


.. container:: center

   therefore, as ``BA`` is to ``CD``, so is ``BC`` to ``CE``,


and alternately, as ``AB`` is to ``BC``, so is ``DC`` to ``CE``. [:ref:`V.16 <V.16>`]

Again, since ``CD`` is parallel to ``BF``, therefore, as ``BC`` is to ``CE``, so is ``FD`` to ``DE``. [:ref:`VI.2 <VI.2>`]

But ``FD`` is equal to ``AC``;


.. container:: center

   therefore, as ``BC`` is to ``CE``, so is ``AC`` to ``DE``,


and alternately, as ``BC`` is to ``CA``, so is ``CE`` to ``ED``. [:ref:`V.16 <V.16>`]

Since then it was proved that,


.. container:: center

   as ``AB`` is to ``BC``, so is ``DC`` to ``CE``,


and, as ``BC`` is to ``CA``, so is ``CE`` to ``ED``; therefore, ``ex aequali``, as ``BA`` is to ``AC``, so is ``CD`` to ``DE``. [:ref:`V.22 <V.22>`]

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
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "V.18" [fillcolor="#222244", URL="/heath/V/18/", target="_top"];
     "V.14" [fillcolor="#222244", URL="/heath/V/14/", target="_top"];
     "I.28" [fillcolor="#222244", URL="/heath/I/28/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "V.23" [fillcolor="#222244", URL="/heath/V/23/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "V.4" [fillcolor="#222244", URL="/heath/V/4/", target="_top"];
     "V.16" [fillcolor="#222244", URL="/heath/V/16/", target="_top"];
     "VI.2" [fillcolor="#222244", URL="/heath/VI/2/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "V.11" [fillcolor="#222244", URL="/heath/V/11/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "V.20" [fillcolor="#222244", URL="/heath/V/20/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "I.38" [fillcolor="#222244", URL="/heath/I/38/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "V.13" [fillcolor="#222244", URL="/heath/V/13/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.22" [fillcolor="#222244", URL="/heath/V/22/", target="_top"];
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "V.12" [fillcolor="#222244", URL="/heath/V/12/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.39" [fillcolor="#222244", URL="/heath/I/39/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "VI.4" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VI/4/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VI.1" [fillcolor="#222244", URL="/heath/VI/1/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "V.21" [fillcolor="#222244", URL="/heath/V/21/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "V.3" [fillcolor="#222244", URL="/heath/V/3/", target="_top"];
     "V.17" [fillcolor="#222244", URL="/heath/V/17/", target="_top"];
     "V.16" -> "V.15";
     "V.23" -> "V.15";
     "VI.1" -> "V.15";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.39" -> "I.cn.1";
     "V.16" -> "V.18";
     "V.16" -> "V.14";
     "V.18" -> "V.14";
     "VI.4" -> "I.28";
     "I.28" -> "I.27";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "V.16" -> "V.23";
     "I.3" -> "I.2";
     "VI.1" -> "I.41";
     "I.15" -> "I.post.4";
     "I.34" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "V.22" -> "V.4";
     "V.23" -> "V.16";
     "VI.1" -> "V.16";
     "VI.4" -> "V.16";
     "VI.4" -> "VI.2";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "V.16" -> "V.11";
     "V.18" -> "V.11";
     "V.23" -> "V.11";
     "VI.1" -> "V.11";
     "VI.2" -> "V.11";
     "V.8" -> "V.def.4";
     "V.16" -> "V.20";
     "V.22" -> "V.20";
     "I.13" -> "I.11";
     "I.39" -> "I.37";
     "I.41" -> "I.37";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.38" -> "I.36";
     "VI.1" -> "I.38";
     "VI.2" -> "I.38";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.27" -> "I.def.23";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.9" -> "V.8";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "I.36" -> "I.33";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "VI.4" -> "I.17";
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.22" -> "V.def.5";
     "VI.1" -> "V.def.5";
     "V.16" -> "V.22";
     "VI.4" -> "V.22";
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.39" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "V.15" -> "V.12";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "VI.2" -> "I.39";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "VI.4" -> "I.post.5";
     "I.31" -> "I.23";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "VI.2" -> "V.7";
     "VI.2" -> "V.9";
     "VI.2" -> "VI.1";
     "I.16" -> "I.10";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.17" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.4" -> "I.cn.4";
     "V.3" -> "V.2";
     "V.17" -> "V.2";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.17" -> "V.1";
     "V.16" -> "V.21";
     "V.23" -> "V.21";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "VI.4" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "V.4" -> "V.3";
     "V.16" -> "V.17";
     "V.18" -> "V.17";
   }



Required for
------------

:ref:`VI.18`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.14`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XI.23`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.13`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`, :ref:`XIII.8`, :ref:`XIII.9`