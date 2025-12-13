:order: 10
:number: 93
:type: prop
:categories: describe, bisect
:tags: line
:dependencies: I.11, I.15, I.29, I.3, I.31, I.32, I.34, I.47, I.5, I.6, I.cn.1, I.post.5




.. picture:: II.10.graphic.inverted.png

.. _II.10:

II.10
=====

   If a straight line be bisected, and a straight line be added to it in a straight line, the square on the whole with the added straight line and the square on the added straight line both together are double of the square on the half and of the square described on the straight line made up of the half and the added straight line as on one straight line.

For let a straight line ``AB`` be bisected at ``C``, and let a straight line ``BD`` be added to it in a straight line;

I say that the squares on ``AD``, ``DB`` are double of the squares on ``AC``, ``CD``.

For let ``CE`` be drawn from the point ``C`` at right angles to ``AB`` [:ref:`I.11 <I.11>`], and let it be made equal to either ``AC`` or ``CB`` [:ref:`I.3 <I.3>`]; let ``EA``, ``EB`` be joined; through ``E`` let ``EF`` be drawn parallel to ``AD``, and through ``D`` let ``FD`` be drawn parallel to ``CE``. [:ref:`I.31 <I.31>`]

Then, since a straight line ``EF`` falls on the parallel straight lines ``EC``, ``FD``,


.. container:: center

   the angles ``CEF``, ``EFD`` are equal to two right angles; [:ref:`I.29 <I.29>`] therefore the angles ``FEB``, ``EFD`` are less than two right angles.


But straight lines produced from angles less than two right angles meet; [:ref:`I.post.5 <I.post.5>`]


.. container:: center

   therefore ``EB``, ``FD``, if produced in the direction ``B``, ``D``, will meet.


Let them be produced and meet at ``G``, and let ``AG`` be joined.

Then, since ``AC`` is equal to ``CE``, the angle ``EAC`` is also equal to the angle ``AEC``; [:ref:`I.5 <I.5>`] and the angle at ``C`` is right;


.. container:: center

   therefore each of the angles ``EAC``, ``AEC`` is half a right angle. [:ref:`I.32 <I.32>`]


For the same reason


.. container:: center

   each of the angles ``CEB``, ``EBC`` is also half a right angle; therefore the angle ``AEB`` is right.


And, since the angle ``EBC`` is half a right angle, the angle ``DBG`` is also half a right angle. [:ref:`I.15 <I.15>`]


.. container:: center

   But the angle ``BDG`` is also right,


for it is equal to the angle ``DCE``, they being alternate; [:ref:`I.29 <I.29>`]


.. container:: center

   therefore the remaining angle ``DGB`` is half a right angle; [:ref:`I.32 <I.32>`]


therefore the angle ``DGB`` is equal to the angle ``DBG``,


.. container:: center

   so that the side ``BD`` is also equal to the side ``GD``. [:ref:`I.6 <I.6>`]


Again, since the angle ``EGF`` is half a right angle, and the angle at ``F`` is right, for it is equal to the opposite angle, the angle at ``C``, [:ref:`I.34 <I.34>`]


.. container:: center

   the remaining angle ``FEG`` is half a right angle; [:ref:`I.32 <I.32>`] therefore the angle ``EGF`` is equal to the angle ``FEG``, so that the side ``GF`` is also equal to the side ``EF``. [:ref:`I.6 <I.6>`]


Now, since the square on ``EC`` is equal to the square on ``CA``, the squares on ``EC``, ``CA`` are double of the square on ``CA``.

But the square on ``EA`` is equal to the squares on ``EC``, ``CA``; [:ref:`I.47 <I.47>`] therefore the square on ``EA`` is double of the square on ``AC``. [:ref:`I.cn.1 <I.cn.1>`]

Again, since ``FG`` is equal to ``EF``, the square on ``FG`` is also equal to the square on ``FE``; therefore the squares on ``GF``, ``FE`` are double of the square on ``EF``.

But the square on ``EG`` is equal to the squares on ``GF``, ``FE``; [:ref:`I.47 <I.47>`] therefore the square on ``EG`` is double of the square on ``EF``.

And ``EF`` is equal to ``CD``; [:ref:`I.34 <I.34>`]


.. container:: center

   therefore the square on ``EG`` is double of the square on ``CD``.


But the square on ``EA`` was also proved double of the square on ``AC``; therefore the squares on ``AE``, ``EG`` are double of the squares on ``AC``, ``CD``.

And the square on ``AG`` is equal to the squares on ``AE``, ``EG``; [:ref:`I.47 <I.47>`] therefore the square on ``AG`` is double of the squares on ``AC``, ``CD``. But the squares on ``AD``, ``DG`` are equal to the square on ``AG``; [:ref:`I.47 <I.47>`] therefore the squares on ``AD``, ``DG`` are double of the squares on ``AC``, ``CD``.

And ``DG`` is equal to ``DB``; therefore the squares on ``AD``, ``DB`` are double of the squares on ``AC``, ``CD``.

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
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.32" [fillcolor="#222244", URL="/heath/I/32/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "II.10" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/II/10/", target="_top"];
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
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.47" [fillcolor="#222244", URL="/heath/I/47/", target="_top"];
     "I.14" [fillcolor="#222244", URL="/heath/I/14/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.32" -> "I.31";
     "I.37" -> "I.31";
     "I.46" -> "I.31";
     "II.10" -> "I.31";
     "II.10" -> "I.6";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "II.10" -> "I.3";
     "II.10" -> "I.32";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "II.10" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "II.10" -> "I.15";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "I.31" -> "I.27";
     "I.3" -> "I.2";
     "I.47" -> "I.41";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "II.10" -> "I.post.5";
     "I.14" -> "I.post.4";
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
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "II.10" -> "I.5";
     "I.16" -> "I.10";
     "I.47" -> "I.46";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "II.10" -> "I.11";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.41" -> "I.37";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.32" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "II.10" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "II.10" -> "I.47";
     "I.47" -> "I.14";
     "I.27" -> "I.def.23";
     "I.37" -> "I.35";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.35" -> "I.34";
     "I.37" -> "I.34";
     "I.41" -> "I.34";
     "I.46" -> "I.34";
     "II.10" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
   }
