:order: 18
:number: 51
:type: prop
:tags: triangle
:dependencies: I.16, I.3




.. picture:: I.18.graphic.inverted.png

.. _I.18:

I.18
====

   In any triangle the greater side subtends the greater angle.

For let ``ABC`` be a triangle having the side ``AC`` greater than ``AB``;

I say that the angle ``ABC`` is also greater than the angle ``BCA``.

For, since ``AC`` is greater than ``AB``, let ``AD`` be made equal to ``AB`` [:ref:`I.3 <I.3>`], and let ``BD`` bejoined.

Then, since the angle ``ADB`` is an exterior angle of the triangle ``BCD``, 

it is greater than the interior and opposite angle ``DCB``. [:ref:`I.16 <I.16>`]

But the angle ``ADB`` is equal to the angle ``ABD``, since the side ``AB`` is equal to ``AD``; therefore the angle ``ABD`` is also greater than the angle ``ACB``; therefore the angle ``ABC`` is much greater than the angle ``ACB``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   In the enunciation of this number we have ὑποτείνειν (subtend

   ) used with the simple accusative instead of the more usual ὑπό with accusative. The latter construction is used in the enunciation of :ref:`I.19 <I.19>`, which otherwise only differs from that of :ref:`I.18 <I.18>` in the order of the words. The point to remember in order to distinguish the two is that the datum comes first and the quaesitum second, the datum being in this proposition the greater ``side`` and in the next the greater ``angle``. Thus the enunciations are (:ref:`I.18 <I.18>`) παντὸς τριγώνου ἡ μείζων πλευρὰ τὴν μείζονα γωνίαν ὑποτείνει and (:ref:`I.19 <I.19>`) παντὸς τριγώνου ὑπὸ τὴν μείζονα γωνίαν ἡ μείζων πλευρὰ ὑποτείνει. In order to keep the proper order in English we must use the passive of the verb in :ref:`I.19 <I.19>`. Aristotle quotes the result of :ref:`I.19 <I.19>`, using the exact wording, ὑπὸ γὰρ τὴν μείζω γωνίαν ὑποτείνει (Meteorologica III. 5, 376 a 12).


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
     "I.18" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/18/", target="_top"];
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
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.13" -> "I.11";
     "I.18" -> "I.16";
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

:ref:`I.19`, :ref:`I.20`, :ref:`I.21`, :ref:`I.22`, :ref:`I.24`, :ref:`I.25`, :ref:`III.12`, :ref:`III.13`, :ref:`III.15`, :ref:`III.16`, :ref:`III.18`, :ref:`III.19`, :ref:`III.2`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.36`, :ref:`III.37`, :ref:`III.7`, :ref:`III.8`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.7`, :ref:`IV.8`, :ref:`X.55`, :ref:`X.71`, :ref:`XI.20`, :ref:`XI.21`, :ref:`XI.22`, :ref:`XI.23`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XIII.13`, :ref:`XIII.18`