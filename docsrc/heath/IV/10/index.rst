:order: 10
:number: 162
:type: prop
:categories: construct
:tags: triangle
:dependencies: I.32, I.5, I.6, II.11, III.32, III.37, IV.1, IV.5




.. picture:: IV.10.graphic.inverted.png

.. _IV.10:

IV.10
=====

   To construct an isosceles triangle having each of the angles at the base double of the remaining one.

``To construct an isosceles triangle having each of the angles at the base double of the remaining one``.

Let any straight line ``AB`` be set out, and let it be cut at the point ``C`` so that the rectangle contained by ``AB``, ``BC`` is equal to the square on ``CA``; [:ref:`II.11 <II.11>`] with centre ``A`` and distance ``AB`` let the circle ``BDE`` be described, and let there be fitted in the circle ``BDE`` the straight line ``BD`` equal to the straight line ``AC`` which is not greater than the diameter of the circle ``BDE``. [:ref:`IV.1 <IV.1>`]

Let ``AD``, ``DC`` be joined, and let the circle ``ACD`` be circumscribed about the triangle ``ACD``. [:ref:`IV.5 <IV.5>`]

Then, since the rectangle ``AB``, ``BC`` is equal to the square on ``AC``, and ``AC`` is equal to ``BD``, therefore the rectangle ``AB``, ``BC`` is equal to the square on ``BD``.

And, since a point ``B`` has been taken outside the circle ``ACD``, and from ``B`` the two straight lines ``BA``, ``BD`` have fallen on the circle ``ACD``, and one of them cuts it, while the other falls on it, and the rectangle ``AB``, ``BC`` is equal to the square on ``BD``,


.. container:: center

   therefore ``BD`` touches the circle ``ACD``. [:ref:`III.37 <III.37>`]


Since, then, ``BD`` touches it, and ``DC`` is drawn across from the point of contact at ``D``, therefore the angle ``BDC`` is equal to the angle ``DAC`` in the alternate segment of the circle. [:ref:`III.32 <III.32>`]

Since, then, the angle ``BDC`` is equal to the angle ``DAC``, let the angle ``CDA`` be added to each; therefore the whole angle ``BDA`` is equal to the two angles ``CDA``, ``DAC``.

But the exterior angle ``BCD`` is equal to the angles ``CDA``, ``DAC``; [:ref:`I.32 <I.32>`] therefore the angle ``BDA`` is also equal to the angle ``BCD``.

But the angle ``BDA`` is equal to the angle ``CBD``, since the side ``AD`` is also equal to ``AB``; [:ref:`I.5 <I.5>`] so that the angle ``DBA`` is also equal to the angle ``BCD``.

Therefore the three angles ``BDA``, ``DBA``, ``BCD`` are equal to one another.

And, since the angle ``DBC`` is equal to the angle ``BCD``,


.. container:: center

   the side ``BD`` is also equal to the side ``DC``. [:ref:`I.6 <I.6>`]


But ``BD`` is by hypothesis equal to ``CA``; therefore ``CA`` is also equal to ``CD``,


.. container:: center

   so that the angle ``CDA`` is also equal to the angle ``DAC``; [:ref:`I.5 <I.5>`]


therefore the angles ``CDA``, ``DAC`` are double of the angle ``DAC``.

But the angle ``BCD`` is equal to the angles ``CDA``, ``DAC``; therefore the angle ``BCD`` is also double of the angle ``CAD``.

But the angle ``BCD`` is equal to each of the angles ``BDA``, ``DBA``; therefore each of the angles ``BDA``, ``DBA`` is also double of the angle ``DAB``.

Therefore the isosceles triangle ``ABD`` has been constructed having each of the angles at the base ``DB`` double of the remaining one. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "III.37" [fillcolor="#222244", URL="/heath/III/37/", target="_top"];
     "I.32" [fillcolor="#222244", URL="/heath/I/32/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "III.32" [fillcolor="#222244", URL="/heath/III/32/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "IV.10" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/IV/10/", target="_top"];
     "III.18" [fillcolor="#222244", URL="/heath/III/18/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.43" [fillcolor="#222244", URL="/heath/I/43/", target="_top"];
     "II.6" [fillcolor="#222244", URL="/heath/II/6/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "II.11" [fillcolor="#222244", URL="/heath/II/11/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "IV.5" [fillcolor="#222244", URL="/heath/IV/5/", target="_top"];
     "III.22" [fillcolor="#222244", URL="/heath/III/22/", target="_top"];
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "III.36" [fillcolor="#222244", URL="/heath/III/36/", target="_top"];
     "IV.1" [fillcolor="#222244", URL="/heath/IV/1/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "III.21" [fillcolor="#222244", URL="/heath/III/21/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.47" [fillcolor="#222244", URL="/heath/I/47/", target="_top"];
     "I.14" [fillcolor="#222244", URL="/heath/I/14/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "III.3" [fillcolor="#222244", URL="/heath/III/3/", target="_top"];
     "III.19" [fillcolor="#222244", URL="/heath/III/19/", target="_top"];
     "III.31" [fillcolor="#222244", URL="/heath/III/31/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "III.20" [fillcolor="#222244", URL="/heath/III/20/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "III.16.p.1" [fillcolor="#333333"];
     "IV.10" -> "I.6";
     "I.32" -> "I.31";
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "II.6" -> "I.31";
     "IV.10" -> "III.37";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "III.32" -> "I.32";
     "IV.10" -> "I.32";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "III.18" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.3" -> "I.def.10";
     "III.31" -> "I.def.10";
     "IV.10" -> "III.32";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "III.19" -> "III.18";
     "III.36" -> "III.18";
     "III.37" -> "III.18";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.3" -> "I.2";
     "I.47" -> "I.41";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.10" -> "I.9";
     "II.6" -> "I.43";
     "II.11" -> "II.6";
     "III.36" -> "II.6";
     "I.29" -> "I.post.5";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "I.34" -> "I.26";
     "III.3" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "III.3" -> "I.8";
     "III.37" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "IV.5" -> "I.4";
     "I.8" -> "I.7";
     "IV.10" -> "II.11";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.3" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "IV.10" -> "I.5";
     "I.16" -> "I.10";
     "IV.5" -> "I.10";
     "IV.10" -> "IV.5";
     "III.31" -> "III.22";
     "III.32" -> "III.22";
     "I.47" -> "I.46";
     "II.6" -> "I.46";
     "II.11" -> "I.46";
     "III.37" -> "III.36";
     "IV.10" -> "IV.1";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.41" -> "I.37";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.43" -> "I.cn.3";
     "III.22" -> "III.21";
     "II.6" -> "I.36";
     "I.32" -> "I.29";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "II.11" -> "I.47";
     "III.36" -> "I.47";
     "I.47" -> "I.14";
     "I.27" -> "I.def.23";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "III.36" -> "III.3";
     "III.32" -> "III.19";
     "III.32" -> "III.31";
     "IV.5" -> "III.31";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.36" -> "I.33";
     "I.19" -> "I.18";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.43" -> "I.34";
     "I.46" -> "I.34";
     "III.21" -> "III.20";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.18" -> "I.17";
     "III.31" -> "I.17";
     "III.37" -> "III.16.p.1";
   }



Required for
------------

:ref:`IV.11`, :ref:`IV.12`