:order: 6
:number: 89
:type: prop
:categories: bisect
:tags: line
:dependencies: I.31, I.36, I.43, I.46




.. picture:: II.6.graphic.inverted.png

.. _II.6:

II.6
====

   If a straight line be bisected and a straight line be added to it in a straight line, the rectangle contained by the whole with the added straight line and the added straight line together with the square on the half is equal to the square on the straight line made up of the half and the added straight line.

For let a straight line ``AB`` be bisected at the point ``C``, and let a straight line ``BD`` be added to it in a straight line;

I say that the rectangle contained by ``AD``, ``DB`` together with the square on ``CB`` is equal to the square on ``CD``.

For let the square ``CEFD`` be described on ``CD``, [:ref:`I.46 <I.46>`] and let ``DE`` be joined; through the point ``B`` let ``BG`` be drawn parallel to either ``EC`` or ``DF``, through the point ``H`` let ``KM`` be drawn parallel to either ``AB`` or ``EF``, and further through ``A`` let ``AK`` be drawn parallel to either ``CL`` or ``DM``. [:ref:`I.31 <I.31>`]


.. container:: center

   Then, since ``AC`` is equal to ``CB``, ``AL`` is also equal to ``CH``. [:ref:`I.36 <I.36>`]


But ``CH`` is equal to ``HF``. [:ref:`I.43 <I.43>`]


.. container:: center

   Therefore ``AL`` is also equal to ``HF``.


Let ``CM`` be added to each;


.. container:: center

   therefore the whole ``AM`` is equal to the gnomon ``NOP``.


But ``AM`` is the rectangle ``AD``, ``DB``,


.. container:: center

   for ``DM`` is equal to ``DB``; therefore the gnomon ``NOP`` is also equal to the rectangle ``AD``, ``DB``.


Let ``LG``, which is equal to the square on ``BC``, be added to each;


.. container:: center

   therefore the rectangle contained by ``AD``, ``DB`` together with the square on ``CB`` is equal to the gnomon ``NOP`` and ``LG``.


But the gnomon ``NOP`` and ``LG`` are the whole square ``CEFD``, which is described on ``CD``;


.. container:: center

   therefore the rectangle contained by ``AD``, ``DB`` together with the square on ``CB`` is equal to the square on ``CD``.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.43" [fillcolor="#222244", URL="/heath/I/43/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "II.6" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/II/6/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.46" -> "I.31";
     "II.6" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.3" -> "I.2";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.10" -> "I.9";
     "II.6" -> "I.43";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "I.34" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
     "II.6" -> "I.46";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.43" -> "I.cn.3";
     "II.6" -> "I.36";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.36" -> "I.35";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.36" -> "I.33";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.43" -> "I.34";
     "I.46" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
   }



Required for
------------

:ref:`II.11`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`X.104`, :ref:`X.110`, :ref:`X.28`, :ref:`X.75`, :ref:`X.81`, :ref:`X.93`, :ref:`X.99`