:order: 39
:number: 310
:type: prop
:dependencies: VII.36, VII.37, VII.38




.. picture:: VII.39.graphic.inverted.png

.. _VII.39:

VII.39
======

   To find the number which is the least that will have given parts.

Let A, B, C be the given parts; thus it is required to find the number which is the least that will have the parts A, B, C.

Let D, E, F be numbers called by the same name as the parts A, B, C, and let G, the least number measured by D, E, F, be taken. [:ref:`VII.36 <VII.36>`]

Therefore G has parts called by the same name as D, E, F. [:ref:`VII.37 <VII.37>`]

But A, B, C are parts called by the same name as D, E, F; therefore G has the parts A, B, C.

I say next that it is also the least number that has.

For, if not, there will be some number less than G which will have the parts A, B, C.

Let it be H.

Since H has the parts A, B, C, therefore H will be measured by numbers called by the same name as the parts A, B, C. [:ref:`VII.38 <VII.38>`]

But D, E, F are numbers called by the same name as the parts A, B, C; therefore H is measured by D, E, F.

And it is less than G : which is impossible.

Therefore there will be no number less than G that will have the parts A, B, C. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "VII.33" [fillcolor="#222244", URL="/heath/VII/33/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "VII.36" [fillcolor="#222244", URL="/heath/VII/36/", target="_top"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "VII.37" [fillcolor="#222244", URL="/heath/VII/37/", target="_top"];
     "VII.21" [fillcolor="#222244", URL="/heath/VII/21/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "VII.39" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/39/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.34" [fillcolor="#222244", URL="/heath/VII/34/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "VII.2.p.1" [fillcolor="#333333"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.19" [fillcolor="#222244", URL="/heath/VII/19/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "VII.3" [fillcolor="#222244", URL="/heath/VII/3/", target="_top"];
     "VII.38" [fillcolor="#222244", URL="/heath/VII/38/", target="_top"];
     "VII.35" [fillcolor="#222244", URL="/heath/VII/35/", target="_top"];
     "VII.34" -> "VII.33";
     "V.7" -> "V.def.5";
     "VII.19" -> "VII.18";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VII.2" -> "VII.1";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VII.39" -> "VII.36";
     "VII.20" -> "VII.4";
     "VII.39" -> "VII.37";
     "VII.33" -> "VII.21";
     "VII.34" -> "VII.21";
     "VII.10" -> "VII.9";
     "VII.19" -> "V.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.19" -> "V.9";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.34" -> "VII.17";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.34" -> "VII.20";
     "V.8" -> "V.def.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.36" -> "VII.34";
     "VII.33" -> "VII.def.15";
     "VII.34" -> "VII.def.15";
     "VII.3" -> "VII.2.p.1";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.34" -> "VII.16";
     "VII.16" -> "VII.15";
     "VII.37" -> "VII.15";
     "VII.38" -> "VII.15";
     "V.8" -> "V.1";
     "VII.13" -> "VII.10";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.33" -> "VII.19";
     "VII.34" -> "VII.19";
     "V.9" -> "V.8";
     "VII.33" -> "VII.3";
     "VII.39" -> "VII.38";
     "VII.36" -> "VII.35";
   }
