:order: 42
:number: 75
:type: prop
:categories: construct
:tags: line, triangle
:dependencies: I.23, I.31, I.38, I.41




.. picture:: I.42.graphic.inverted.png

.. _I.42:

I.42
====

   To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

Let ``ABC`` be the given triangle, and ``D`` the given rectilineal angle; thus it is required to construct in the rectilineal angle ``D`` a parallelogram equal to the triangle ``ABC``. 

Let ``BC`` be bisected at ``E``, and let ``AE`` be joined; on the straight line ``EC``, and at the point ``E`` on it, let the angle ``CEF`` be constructed equal to the angle ``D``; [:ref:`I.23 <I.23>`] through ``A`` let ``AG`` be drawn parallel to ``EC``, and [:ref:`I.31 <I.31>`] through ``C`` let ``CG`` be drawn parallel to ``EF``.

Then ``FECG`` is a parallelogram.

And, since ``BE`` is equal to ``EC``, the triangle ``ABE`` is also equal to the triangle ``AEC``, for they are on equal bases ``BE``, ``EC`` and in the same parallels ``BC``, ``AG``; [:ref:`I.38 <I.38>`] therefore the triangle ``ABC`` is double of the triangle ``AEC``.
        

But the parallelogram ``FECG`` is also double of the triangle ``AEC``, for it has the same base with it and is in the same parallels with it; [:ref:`I.41 <I.41>`] therefore the parallelogram ``FECG`` is equal to the triangle ``ABC``.

And it has the angle ``CEF`` equal to the given angle ``D``.

Therefore the parallelogram ``FECG`` has been constructed equal to the given triangle ``ABC``, in the angle ``CEF`` which is equal to ``D``. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.42" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/I/42/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "I.38" [fillcolor="#222244", URL="/heath/I/38/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.42" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.3" -> "I.2";
     "I.42" -> "I.41";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "I.15" -> "I.post.4";
     "I.31" -> "I.23";
     "I.42" -> "I.23";
     "I.34" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.13" -> "I.11";
     "I.41" -> "I.37";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.38" -> "I.36";
     "I.42" -> "I.38";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.4" -> "I.cn.4";
     "I.27" -> "I.def.23";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.36" -> "I.33";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
   }



Required for
------------

:ref:`I.44`, :ref:`I.45`, :ref:`II.14`, :ref:`VI.25`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`X.100`, :ref:`X.101`, :ref:`X.105`, :ref:`X.106`, :ref:`X.108`, :ref:`X.109`, :ref:`X.33`, :ref:`X.34`, :ref:`X.38`, :ref:`X.39`, :ref:`X.40`, :ref:`X.44`, :ref:`X.45`, :ref:`X.46`, :ref:`X.54`, :ref:`X.56`, :ref:`X.57`, :ref:`X.58`, :ref:`X.62`, :ref:`X.63`, :ref:`X.64`, :ref:`X.67`, :ref:`X.68`, :ref:`X.69`, :ref:`X.71`, :ref:`X.72`, :ref:`X.76`, :ref:`X.77`, :ref:`X.82`, :ref:`X.83`, :ref:`X.94`, :ref:`X.95`, :ref:`XI.32`, :ref:`XI.33`, :ref:`XI.34`, :ref:`XI.37`, :ref:`XII.10`, :ref:`XII.11`, :ref:`XII.12`, :ref:`XII.13`, :ref:`XII.14`, :ref:`XII.15`, :ref:`XII.4`, :ref:`XII.5`, :ref:`XII.6`, :ref:`XII.7`, :ref:`XII.8`, :ref:`XII.9`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.18`