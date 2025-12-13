:order: 17
:number: 50
:type: prop
:tags: triangle
:dependencies: I.13, I.16, I.post.2




.. picture:: I.17.graphic.inverted.png

.. _I.17:

I.17
====

   In any triangle two angles taken together in any manner are less than two right angles.

Let ``ABC`` be a triangle; I say that two angles of the triangle ``ABC`` taken together in any manner are less than two right angles.

For let ``BC`` be produced to ``D``. [:ref:`I.post.2 <I.post.2>`]

Then, since the angle ``ACD`` is an exterior angle of the triangle ``ABC``,

it is greater than the interior and opposite angle ``ABC``. [:ref:`I.16 <I.16>`] Let the angle ``ACB`` be added to each; therefore the angles ``ACD``, ``ACB`` are greater than the angles ``ABC``, ``BCA``.  But the angles ``ACD``, ``ACB`` are equal to two right angles. [:ref:`I.13 <I.13>`]

Therefore the angles ``ABC``, ``BCA`` are less than two right angles.

Similarly we can prove that the angles ``BAC``, ``ACB`` are also less than two right angles, and so are the angles ``CAB``, ``ABC`` as well.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. taken together in any manner,**

   

   πάντη μεταλαμβανόμεναι, i.e. any pair added together.


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
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.17" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/17/", target="_top"];
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
     "I.17" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.3" -> "I.2";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.4" -> "I.cn.4";
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

:ref:`III.16`, :ref:`III.18`, :ref:`III.19`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`VI.13`, :ref:`VI.18`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`X.100`, :ref:`X.101`, :ref:`X.102`, :ref:`X.103`, :ref:`X.104`, :ref:`X.105`, :ref:`X.106`, :ref:`X.107`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.111`, :ref:`X.112`, :ref:`X.113`, :ref:`X.114`, :ref:`X.13`, :ref:`X.14`, :ref:`X.18`, :ref:`X.22`, :ref:`X.23`, :ref:`X.25`, :ref:`X.26`, :ref:`X.27`, :ref:`X.28`, :ref:`X.29`, :ref:`X.30`, :ref:`X.31`, :ref:`X.32`, :ref:`X.33`, :ref:`X.34`, :ref:`X.35`, :ref:`X.36`, :ref:`X.37`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.41`, :ref:`X.42`, :ref:`X.43`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.47`, :ref:`X.48`, :ref:`X.49`, :ref:`X.50`, :ref:`X.52`, :ref:`X.53`, :ref:`X.54`, :ref:`X.55`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.59`, :ref:`X.60`, :ref:`X.61`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.65`, :ref:`X.66`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.70`, :ref:`X.71`, :ref:`X.72`, :ref:`X.73`, :ref:`X.75`, :ref:`X.76`, :ref:`X.77`, :ref:`X.78`, :ref:`X.79`, :ref:`X.80`, :ref:`X.81`, :ref:`X.82`, :ref:`X.83`, :ref:`X.84`, :ref:`X.85`, :ref:`X.86`, :ref:`X.87`, :ref:`X.88`, :ref:`X.89`, :ref:`X.90`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`X.97`, :ref:`X.98`, :ref:`X.99`, :ref:`XI.14`, :ref:`XI.15`, :ref:`XI.23`, :ref:`XII.1`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.17`, :ref:`XII.18`, :ref:`XII.2`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XIII.10`, :ref:`XIII.11`, :ref:`XIII.12`, :ref:`XIII.13`, :ref:`XIII.14`, :ref:`XIII.16`, :ref:`XIII.17`, :ref:`XIII.18`, :ref:`XIII.6`, :ref:`XIII.8`, :ref:`XIII.9`