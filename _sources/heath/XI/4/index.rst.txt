:order: 4
:number: 536
:type: prop
:tags: line
:dependencies: I.15, I.26, I.4, I.8, XI.def.3




.. picture:: XI.4.graphic.inverted.png

.. _XI.4:

XI.4
====

   If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through them.

For let a straight line EF be set up at right angles to the two straight lines AB, CD, which cut one another at the point E, from E; I say that EF is also at right angles to the plane through AB, CD.

For let AE, EB, CE, ED be cut off equal to one another, and let any straight line GEH be drawn across through E, at random; let AD, CB be joined, and further let FA, FG, FD, FC, FH, FB be joined from the point F taken at random <on EF>.

Now, since the two straight lines AE, ED are equal to the two straight lines CE, EB, and contain equal angles, [:ref:`I.15 <I.15>`] therefore the base AD is equal to the base CB, and the triangle AED will be equal to the triangle CEB; [:ref:`I.4 <I.4>`] so that the angle DAE is also equal to the angle EBC.

But the angle AEG is also equal to the angle BEH; [:ref:`I.15 <I.15>`] therefore AGE, BEH are two triangles which have two angles equal to two angles respectively, and one side equal to one side, namely that adjacent to the equal angles, that is to say, AE to EB; therefore they will also have the remaining sides equal to the remaining sides. [:ref:`I.26 <I.26>`]

Therefore GE is equal to EH, and AG to BH.

And, since AE is equal to EB, while FE is common and at right angles, therefore the base FA is equal to the base FB. [:ref:`I.4 <I.4>`]

For the same reason FC is also equal to FD.

And, since AD is equal to CB, and FA is also equal to FB, the two sides FA, AD are equal to the two sides FB, BC respectively; and the base FD was proved equal to the base FC; therefore the angle FAD is also equal to the angle FBC. [:ref:`I.8 <I.8>`]

And since, again, AG was proved equal to BH, and further FA also equal to FB, the two sides FA, AG are equal to the two sides FB, BH.

And the angle FAG was proved equal to the angle FBH; therefore the base FG is equal to the base FH. [:ref:`I.4 <I.4>`]

Now since, again, GE was proved equal to EH, and EF is common, the two sides GE, EF are equal to the two sides HE, EF; and the base FG is equal to the base FH; therefore the angle GEF is equal to the angle HEF. [:ref:`I.8 <I.8>`]

Therefore each of the angles GEF, HEF is right.

Therefore FE is at right angles to GH drawn at random through E.

Similarly we can prove that FE will also make right angles with all the straight lines which meet it and are in the plane of reference.

But a straight line is at right angles to a plane when it makes right angles with all the straight lines which meet it and are in that same plane; [:ref:`XI.def.3 <XI.def.3>`] therefore FE is at right angles to the plane of reference.

But the plane of reference is the plane through the straight lines AB, CD.

Therefore FE is at right angles to the plane through AB, CD.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "XI.def.3" [fillcolor="#224422", URL="/heath/XI/def.3/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "XI.4" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "XI.4" -> "XI.def.3";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "XI.4" -> "I.15";
     "I.13" -> "I.11";
     "I.26" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "XI.4" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "XI.4" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "XI.4" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`XI.10`, :ref:`XI.11`, :ref:`XI.12`, :ref:`XI.15`, :ref:`XI.18`, :ref:`XI.23`, :ref:`XI.24`, :ref:`XI.25`, :ref:`XI.26`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.35`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.38`, :ref:`XI.39`, :ref:`XI.5`, :ref:`XI.6`, :ref:`XI.8`, :ref:`XI.9`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`