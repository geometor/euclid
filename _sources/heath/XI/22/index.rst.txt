:order: 22
:number: 554
:type: prop
:categories: construct
:tags: line, triangle
:dependencies: I.24, I.4




.. picture:: XI.22.graphic.inverted.png

.. _XI.22:

XI.22
=====

   If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to construct a triangle out of the straight lines joining the extremities of the equal straight lines.

Let there be three plane angles ABC, DEF, GHK, of which two, taken together in any manner, are greater than the remaining one, namely


.. container:: center

   the angles ABC, DEF greater than the angle GHK, the angles DEF, GHK greater than the angle ABC,


and, further, the angles GHK, ABC greater than the angle DEF; let the straight lines AB, BC, DE, EF, GH, HK be equal, and let AC, DF, GK be joined; I say that it is possible to construct a triangle out of straight lines equal to AC, DF, GK, that is, that any two of the straight lines AC, DF, GK are greater than the remaining one.

Now, if the angles ABC, DEF, GHK are equal to one another, it is manifest that, AC, DF, GK being equal also, it is possible to construct a triangle out of straight lines equal to AC, DF, GK.

But, if not, let them be unequal, and on the straight line HK, and at the point H on it, let the angle KHL be constructed equal to the angle ABC; let HL be made equal to one of the straight lines AB, BC, DE, EF, GH, HK, and let KL, GL be joined.

Now, since the two sides AB, BC are equal to the two sides KH, HL, and the angle at B is equal to the angle KHL, therefore the base AC is equal to the base KL. [:ref:`I.4 <I.4>`]

And, since the angles ABC, GHK are greater than the angle DEF, while the angle ABC is equal to the angle KHL, therefore the angle GHL is greater than the angle DEF.

And, since the two sides GH, HL are equal to the two sides DE, EF, and the angle GHL is greater than the angle DEF, therefore the base GL is greater than the base DF. [:ref:`I.24 <I.24>`]

But GK, KL are greater than GL.

Therefore GK, KL are much greater than DF.

But KL is equal to AC; therefore AC, GK are greater than the remaining straight line DF.

Similarly we can prove that AC, DF are greater than GK, and further DF, GK are greater than AC.

Therefore it is possible to construct a triangle out of straight lines equal to AC, DF, GK. Q. E. D.


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
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.24" [fillcolor="#222244", URL="/heath/I/24/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "XI.22" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/22/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.24" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.13" -> "I.11";
     "I.18" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "XI.22" -> "I.24";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "I.24" -> "I.23";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.24" -> "I.4";
     "XI.22" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.19" -> "I.18";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.24" -> "I.5";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`XI.23`