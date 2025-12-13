:order: 14
:number: 47
:type: prop
:tags: line
:dependencies: I.13, I.cn.1, I.cn.3, I.post.4




.. picture:: I.14.graphic.inverted.png

.. _I.14:

I.14
====

   If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

For with any straight line ``AB``, and at the point ``B`` on it, let the two straight lines ``BC``, ``BD`` not lying on the same side make the adjacent angles ``ABC``, ``ABD`` equal to two right angles;

I say that ``BD`` is in a straight line with ``CB``. 

For, if ``BD`` is not in a straight line with ``BC``, let ``BE`` be in a straight line with ``CB``.

Then, since the straight line ``AB`` stands on the straight line ``CBE``, 
        the angles ``ABC``, ``ABE`` are equal to two right angles. [:ref:`I.13 <I.13>`] But the angles ``ABC``, ``ABD`` are also equal to two right angles; therefore the angles ``CBA``, ``ABE`` are equal to the angles ``CBA``, ``ABD``. [:ref:`I.post.4 <I.post.4>` and :ref:`I.cn.1 <I.cn.1>`]

Let the angle ``CBA`` be subtracted from each; therefore the remaining angle ``ABE`` is equal to the remaining angle ``ABD``, [:ref:`I.cn.3 <I.cn.3>`] the less to the greater: which is impossible. Therefore ``BE`` is not in a straight line with ``CB``.

Similarly we can prove that neither is any other straight line except ``BD``. Therefore ``CB`` is in a straight line with ``BD``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. If with any straight line....**

   

   There is no greater difficulty in translating the works of the Greek geometers than that of accurately giving the force of prepositions. πρός, for instance, is used in all sorts of expressions with various shades of meaning. The present enunciation begins ἐὰν πρός τινι εὐθείᾳ καὶ τῷ πρὸς αὐτῆ σημείῳ, and it is really necessary in this one sentence to translate πρός by three different words, ``with``, ``at``, and ``on``. The first πρός must be translated by ``with`` because two straight lines make

    an angle ``with`` one another. On the other hand, where the similar expression πρὸς τῇ δοθείση εὐθείᾳ occurs in :ref:`I.23 <I.23>`, but it is a question of constructing

    an angle (συστἡσασθαι), we have to say to construct ``on`` a given straight line.

    Against would perhaps be the English word coming nearest to expressing all these meanings of πρός, but it would be intolerable as a translation.


.. note::


   **17**

   

   Todhunter points out that for the inference in this line :ref:`I.post.4 <I.post.4>`, that all right angles are equal, is necessary as well as the Common Notion that things which are equal to the same thing (or rather, here, to ``equal things``) are equal. A similar remark applies to steps in the proofs of :ref:`I.15 <I.15>` and :ref:`I.28 <I.28>`.


.. note::


   **24. we can prove.**

   

   The Greek expresses this by the future of the verb, δείξομεν, we shall prove,

    which however would perhaps be misleading in English.


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
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.14" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/14/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.5" -> "I.3";
     "I.11" -> "I.3";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.14" -> "I.13";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.3" -> "I.2";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.1";
     "I.11" -> "I.1";
     "I.14" -> "I.post.4";
     "I.11" -> "I.8";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.5" -> "I.4";
     "I.8" -> "I.7";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.7" -> "I.5";
   }



Required for
------------

:ref:`I.45`, :ref:`I.47`, :ref:`I.48`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.19`, :ref:`VI.20`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`VI.32`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.13`, :ref:`X.18`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.29`, :ref:`X.30`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XI.23`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.35`, :ref:`XI.36`, :ref:`XI.37`, :ref:`XI.38`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.1`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.12`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.15`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.4`, :ref:`XIII.5`, :ref:`XIII.6`