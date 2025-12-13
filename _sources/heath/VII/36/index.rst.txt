:order: 36
:number: 307
:type: prop
:dependencies: VII.34, VII.35




.. picture:: VII.36.graphic.inverted.png

.. _VII.36:

VII.36
======

   Given three numbers, to find the least number which they measure.

Let A, B, C be the three given numbers; thus it is required to find the least number which they measure.

Let D, the least number measured by the two numbers A, B, be taken. [:ref:`VII.34 <VII.34>`]

Then C either measures, or does not measure, D.

First, let it measure it.

But A, B also measure D; therefore A, B, C measure D.

I say next that it is also the least that they measure.

For, if not, A, B, C will measure some number which is less than D.

Let them measure E.

Since A, B, C measure E, therefore also A, B measure E.

Therefore the least number measured by A, B will also measure E. [:ref:`VII.35 <VII.35>`]

But D is the least number measured by A, B; therefore D will measure E, the greater the less: which is impossible.

Therefore A, B, C will not measure any number which is less than D;


.. container:: center

   therefore D is the least that A, B, C measure.


Again, let C not measure D, and let E, the least number measured by C, D, be taken. [:ref:`VII.34 <VII.34>`]

Since A, B measure D, and D measures E, therefore also A, B measure E.

But C also measures E; therefore also A, B, C measure E.

I say next that it is also the least that they measure.

For, if not, A, B, C will measure some number which is less than E.

Let them measure F.

Since A, B, C measure F, therefore also A, B measure F; therefore the least number measured by A, B will also measure F. [:ref:`VII.35 <VII.35>`]

But D is the least number measured by A, B; therefore D measures F.

But C also measures F; therefore D, C measure F, so that the least number measured by D, C will also measure F.

But E is the least number measured by C, D; therefore E measures F, the greater the less: which is impossible.

Therefore A, B, C will not measure any number which is less than E.

Therefore E is the least that is measured by A, B, C. Q. E. D.


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
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "VII.20" [fillcolor="#222244", URL="/heath/VII/20/", target="_top"];
     "VII.18" [fillcolor="#222244", URL="/heath/VII/18/", target="_top"];
     "VII.2" [fillcolor="#222244", URL="/heath/VII/2/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "VII.5" [fillcolor="#222244", URL="/heath/VII/5/", target="_top"];
     "VII.34" [fillcolor="#222244", URL="/heath/VII/34/", target="_top"];
     "VII.def.20" [fillcolor="#224422", URL="/heath/VII/def.20/", target="_top"];
     "VII.def.15" [fillcolor="#224422", URL="/heath/VII/def.15/", target="_top"];
     "VII.2.p.1" [fillcolor="#333333"];
     "VII.1" [fillcolor="#222244", URL="/heath/VII/1/", target="_top"];
     "VII.6" [fillcolor="#222244", URL="/heath/VII/6/", target="_top"];
     "VII.16" [fillcolor="#222244", URL="/heath/VII/16/", target="_top"];
     "VII.15" [fillcolor="#222244", URL="/heath/VII/15/", target="_top"];
     "VII.13" [fillcolor="#222244", URL="/heath/VII/13/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "VII.10" [fillcolor="#222244", URL="/heath/VII/10/", target="_top"];
     "VII.36" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/VII/36/", target="_top"];
     "VII.4" [fillcolor="#222244", URL="/heath/VII/4/", target="_top"];
     "VII.def.12" [fillcolor="#224422", URL="/heath/VII/def.12/", target="_top"];
     "VII.19" [fillcolor="#222244", URL="/heath/VII/19/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "VII.21" [fillcolor="#222244", URL="/heath/VII/21/", target="_top"];
     "VII.9" [fillcolor="#222244", URL="/heath/VII/9/", target="_top"];
     "VII.3" [fillcolor="#222244", URL="/heath/VII/3/", target="_top"];
     "VII.35" [fillcolor="#222244", URL="/heath/VII/35/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "VII.12" [fillcolor="#222244", URL="/heath/VII/12/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VII.17" [fillcolor="#222244", URL="/heath/VII/17/", target="_top"];
     "VII.34" -> "VII.33";
     "V.7" -> "V.def.5";
     "V.8" -> "V.def.7";
     "VII.21" -> "VII.20";
     "VII.34" -> "VII.20";
     "VII.19" -> "VII.18";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "V.8" -> "V.def.4";
     "VII.6" -> "VII.5";
     "VII.9" -> "VII.5";
     "VII.10" -> "VII.5";
     "VII.12" -> "VII.5";
     "VII.36" -> "VII.34";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VII.33" -> "VII.def.15";
     "VII.34" -> "VII.def.15";
     "VII.3" -> "VII.2.p.1";
     "VII.2" -> "VII.1";
     "VII.9" -> "VII.6";
     "VII.10" -> "VII.6";
     "VII.12" -> "VII.6";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.34" -> "VII.16";
     "VII.16" -> "VII.15";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "V.8" -> "V.1";
     "VII.13" -> "VII.10";
     "VII.20" -> "VII.4";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.33" -> "VII.19";
     "VII.34" -> "VII.19";
     "V.9" -> "V.8";
     "VII.33" -> "VII.21";
     "VII.34" -> "VII.21";
     "VII.10" -> "VII.9";
     "VII.33" -> "VII.3";
     "VII.36" -> "VII.35";
     "VII.19" -> "V.7";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.19" -> "V.9";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.34" -> "VII.17";
   }



Required for
------------

:ref:`VII.39`