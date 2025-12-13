:order: 27
:number: 60
:type: prop
:tags: line
:dependencies: I.16, I.def.23




.. picture:: I.27.graphic.inverted.png

.. _I.27:

I.27
====

   If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

For let the straight line ``EF`` falling on the two straight lines ``AB``, ``CD`` make the alternate angles ``AEF``, ``EFD`` equal to one another;

I say that ``AB`` is parallel to ``CD``.

For, if not, ``AB``, ``CD`` when produced will meet either in the direction of ``B``, ``D`` or towards ``A``, ``C``. 

Let them be produced and meet, in the direction of ``B``, ``D``, at ``G``.

Then, in the triangle ``GEF``, the exterior angle ``AEF`` is equal to the interior and opposite angle ``EFG``: which is impossible. [:ref:`I.16 <I.16>`]

Therefore ``AB``, ``CD`` when produced will not meet in the direction of ``B``, ``D``.

Similarly it can be proved that neither will they meet towards ``A``, ``C``. 

But straight lines which do not meet in either direction are parallel; [:ref:`I.def.23 <I.def.23>`] therefore ``AB`` is parallel to ``CD``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. falling on two straight lines,**

   

   εὶς δύο εὐθείας ἐμπίπτουσα, the phrase being the same as that used in :ref:`I.post.5 <I.post.5>`, meaning a ``transversal``.


.. note::


   **2. the alternate angles,**

   

   αἱ ἐναλλὰξ γωνίαι. Proclus (p. 357, 9) explains that Euclid uses the word ``alternate`` (or, more exactly, ``alternately``, ἐναλλάξ) in two connexions, (1) of a certain transformation of a proportion, as in Book V. and the arithmetical Books, (2) as here, of certain of the angles formed by parallels with a straight line crossing them. Alternate angles are, according to Euclid as interpreted by Proclus, those which are not on the same side of the transversal, and are not adjacent, but are separated by the transversal, both being within the parallels but one above

    and the other below.

    The meaning is natural enough if we imagine the four internal angles to be taken in cyclic order and ``alternate`` angles to be any two of them not successive but separated by one angle of the four.


.. note::


   **9. in the direction of B, D or towards A, C,**

   

   literally towards the ``parts B``, ``D`` or towards ``A``, ``C``,

    ἐπὶ τὰ Β, Δ μέρη ἢ ἐπὶ τὰ Α Γ.


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
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
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
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.13" -> "I.11";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.15" -> "I.post.4";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
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

:ref:`I.28`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.27`, :ref:`III.29`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`IX.15`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`, :ref:`VIII.5`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.115`, :ref:`X.13`, :ref:`X.14`, :ref:`X.17`, :ref:`X.18`, :ref:`X.19`, :ref:`X.20`, :ref:`X.21`, :ref:`X.22`, :ref:`X.23`, :ref:`X.24`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.29`, :ref:`X.30`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.74`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XI.10`, :ref:`XI.11`, :ref:`XI.12`, :ref:`XI.15`, :ref:`XI.17`, :ref:`XI.18`, :ref:`XI.21`, :ref:`XI.23`, :ref:`XI.24`, :ref:`XI.25`, :ref:`XI.26`, :ref:`XI.27`, :ref:`XI.29`, :ref:`XI.30`, :ref:`XI.31`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.35`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.38`, :ref:`XI.39`, :ref:`XI.6`, :ref:`XI.9`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XII.3`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.1`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.12`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.15`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.2`, :ref:`XIII.4`, :ref:`XIII.5`, :ref:`XIII.6`, :ref:`XIII.8`, :ref:`XIII.9`