:order: 7
:number: 596
:type: prop
:dependencies: I.4, I.5, I.6, I.8




.. picture:: XIII.7.graphic.inverted.png

.. _XIII.7:

XIII.7
======

   If three angles of an equilateral pentagon, taken either in order or not in order, be equal, the pentagon will be equiangular.

For in the equilateral pentagon ABCDE let, first, three angles taken in order, those at A, B, C, be equal to one another; I say that the pentagon ABCDE is equiangular.

For let AC, BE, FD be joined.

Now, since the two sides CB, BA are equal to the two sides BA, AE respectively, and the angle CBA is equal to the angle BAE, therefore the base AC is equal to the base BE, the triangle ABC is equal to the triangle ABE, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend, [:ref:`I.4 <I.4>`] that is, the angle BCA to the angle BEA, and the angle ABE to the angle CAB; hence the side AF is also equal to the side BF. [:ref:`I.6 <I.6>`]

But the whole AC was also proved equal to the whole BE; therefore the remainder FC is also equal to the remainder FE.

But CD is also equal to DE.

Therefore the two sides FC, CD are equal to the two sides FE, ED; and the base FD is common to them; therefore the angle FCD is equal to the angle FED. [:ref:`I.8 <I.8>`]

But the angle BCA was also proved equal to the angle AEB; therefore the whole angle BCD is also equal to the whole angle AED.

But, by hypothesis, the angle BCD is equal to the angles at A, B; therefore the angle AED is also equal to the angles at A, B.

Similarly we can prove that the angle CDE is also equal to the angles at A, B, C; therefore the pentagon ABCDE is equiangular.

Next, let the given equal angles not be angles taken in order, but let the angles at the points A, C, D be equal; I say that in this case too the pentagon ABCDE is equiangular.

For let BD be joined.

Then, since the two sides BA, AE are equal to the two sides BC, CD, and they contain equal angles, therefore the base BE is equal to the base BD, the triangle ABE is equal to the triangle BCD, and the remaining angles will be equal to the remaining angles, namely those which the equal sides subtend; [:ref:`I.4 <I.4>`] therefore the angle AEB is equal to the angle CDB.

But the angle BED is also equal to the angle BDE, since the side BE is also equal to the side BD. [:ref:`I.5 <I.5>`]

Therefore the whole angle AED is equal to the whole angle CDE.

But the angle CDE is, by hypothesis, equal to the angles at A, C; therefore the angle AED is also equal to the angles at A, C.

For the same reason the angle ABC is also equal to the angles at A, C, D.

Therefore the pentagon ABCDE is equiangular. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.6" [fillcolor="#222244", URL="/heath/I/6/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "XIII.7" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XIII/7/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "XIII.7" -> "I.6";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.2" -> "I.1";
     "I.5" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "XIII.7" -> "I.8";
     "I.5" -> "I.4";
     "XIII.7" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.cn.3";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "XIII.7" -> "I.5";
     "I.3" -> "I.2";
     "I.4" -> "I.cn.4";
   }



Required for
------------

:ref:`XIII.17`, :ref:`XIII.18`