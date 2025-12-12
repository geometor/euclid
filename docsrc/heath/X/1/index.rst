:order: 1
:number: 378
:type: prop
:dependencies: V.def.4




.. picture:: X.1.graphic.inverted.png

.. _X.1:

X.1
===

   Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

Let AB, C be two unequal magnitudes of which AB is the greater: I say that, if from AB there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the magnitude C.

For C if multiplied will sometime be greater than AB. [cf. :ref:`V.def.4 <V.def.4>`]

Let it be multiplied, and let DE be a multiple of C, and greater than. AB; let DE be divided into the parts DF, FG, GE equal to C, from AB let there be subtracted BH greater than its half, and, from AH, HK greater than its half, and let this process be repeated continually until the divisions in AB are equal in multitude with the divisions in DE.

Let, then, AK, KH, HB be divisions which are equal in multitude with DF, FG, GE.

Now, since DE is greater than AB, and from DE there has been subtracted EG less than its half, and, from AB, BH greater than its half, therefore the remainder GD is greater than the remainder HA.

And, since GD is greater than HA, and there has been subtracted, from GD, the half GF, and, from HA, HK greater than its half, therefore the remainder DF is greater than the remainder AK.

But DF is equal to C; therefore C is also greater than AK.

Therefore AK is less than C.

Therefore there is left of the magnitude AB the magnitude AK which is less than the lesser magnitude set out, namely C. Q. E. D.

And the theorem can be similarly proved even if the parts subtracted be halves.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "X.1" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/X/1/", target="_top"];
     "X.1" -> "V.def.4";
   }



Required for
------------

:ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.16`