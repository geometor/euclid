:order: 23
:number: 555
:type: prop
:categories: construct
:dependencies: I.25, I.29, I.4, I.47, I.8, III.31, IV.1, V.16, VI.2, VI.4, XI.12, XI.22




.. picture:: XI.23.graphic.inverted.png

.. _XI.23:

XI.23
=====

   To construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

Let the angles ABC, DEF, GHK be the three given plane angles, and let two of these, taken together in any manner, be greater than the remaining one, while, further, the three are less than four right angles; thus it is required to construct a solid angle out of angles equal to the angles ABC, DEF, GHK.

Let AB, BC, DE, EF, GH, HK be cut off equal to one another, and let AC, DF, GK be joined; it is therefore possible to construct a triangle out of straight lines equal to AC, DF, GK. [:ref:`XI.22 <XI.22>`]

Let LMN be so constructed that AC is equal to LM, DF to MN, and further GK to NL, let the circle LMN be described about the triangle LMN, let its centre be taken, and let it be O; let LO, MO, NO be joined; I say that AB is greater than LO.

For, if not, AB is either equal to LO, or less.

First, let it be equal.

Then, since AB is equal to LO, while AB is equal to BC, and OL to OM, the two sides AB, BC are equal to the two sides LO, OM respectively; and, by hypothesis, the base AC is equal to the base LM; therefore the angle ABC is equal to the angle LOM. [:ref:`I.8 <I.8>`]

For the same reason the angle DEF is also equal to the angle MON, and further the angle GHK to the angle NOL; therefore the three angles ABC, DEF, GHK are equal to the three angles LOM, MON, NOL.

But the three angles LOM, MON, NOL are equal to four right angles; therefore the angles ABC, DEF, GHK are equal to four right angles.

But they are also, by hypothesis, less than four right angles: which is absurd.

Therefore AB is not equal to LO.

I say next that neither is AB less than LO.

For, if possible, let it be so, and let OP be made equal to AB, and OQ equal to BC, and let PQ be joined.

Then, since AB is equal to BC, OP is also equal to OQ, so that the remainder LP is equal to QM.

Therefore LM is parallel to PQ, [:ref:`VI.2 <VI.2>`] and LMO is equiangular with PQO; [:ref:`I.29 <I.29>`] therefore, as OL is to LM, so is OP to PQ; [:ref:`VI.4 <VI.4>`] and alternately, as LO is to OP, so is LM to PQ. [:ref:`V.16 <V.16>`]

But LO is greater than OP; therefore LM is also greater than PQ.

But LM was made equal to AC; therefore AC is also greater than PQ.

Since, then, the two sides AB, BC are equal to the two sides PO, OQ, and the base AC is greater than the base PQ, therefore the angle ABC is greater than the angle POQ. [:ref:`I.25 <I.25>`]

Similarly we can prove that the angle DEF is also greater than the angle MON, and the angle GHK greater than the angle NOL.

Therefore the three angles ABC, DEF, GHK are greater than the three angles LOM, MON, NOL.

But, by hypothesis, the angles ABC, DEF, GHK are less than four right angles; therefore the angles LOM, MON, NOL are much less than four right angles.

But they are also equal to four right angles: which is absurd.

Therefore AB is not less than LO.

And it was proved that neither is it equal; therefore AB is greater than LO.

Let then OR be set up from the point O at right angles to the plane of the circle LMN, [:ref:`XI.12 <XI.12>`] and let the square on OR be equal to that area by which the square on AB is greater than the square on LO; [Lemma] let RL, RM, RN be joined.

Then, since RO is at right angles to the plane of the circle LMN, therefore RO is also at right angles to each of the straight lines LO, MO, NO.

And, since LO is equal to OM, while OR is common and at right angles, therefore the base RL is equal to the base RM. [:ref:`I.4 <I.4>`]

For the same reason RN is also equal to each of the straight lines RL, RM; therefore the three straight lines RL, RM, RN are equal to one another.

Next, since by hypothesis the square on OR is equal to that area by which the square on AB is greater than the square on LO, therefore the square on AB is equal to the squares on LO, OR.

But the square on LR is equal to the squares on LO, OR, for the angle LOR is right; [:ref:`I.47 <I.47>`] therefore the square on AB is equal to the square on RL; therefore AB is equal to RL.

But each of the straight lines BC, DE, EF, GH, HK is equal to AB, while each of the straight lines RM, RN is equal to RL; therefore each of the straight lines AB, BC, DE, EF, GH, HK is equal to each of the straight lines RL, RM, RN.

And, since the two sides LR, RM are equal to the two sides AB, BC, and the base LM is by hypothesis equal to the base AC, therefore the angle LRM is equal to the angle ABC. [:ref:`I.8 <I.8>`]

For the same reason the angle MRN is also equal to the angle DEF, and the angle LRN to the angle GHK.

Therefore, out of the three plane angles LRM, MRN, LRN, which are equal to the three given angles ABC, DEF, GHK, the solid angle at R has been constructed, which is contained by the angles LRM, MRN, LRN. Q. E. F.


.. _XI.23.l.1:


**XI.23.l.1**


But how it is possible to take the square on OR equal to that area by which the square on AB is greater than the square on LO, we can show as follows. 
       
Let the straight lines AB, LO be set out, and let AB be the greater; let the semicircle ABC be described on AB, and into the semicircle ABC let AC be fitted equal to the straight line LO, not being greater than the diameter AB; [:ref:`IV.1 <IV.1>`] let CB be joined 
Since then the angle ACB is an angle in the semicircle ACB, therefore the angle ACB is right. [:ref:`III.31 <III.31>`] 
Therefore the square on AB is equal to the squares on AC, CB. [:ref:`I.47 <I.47>`] 
Hence the square on AB is greater than the square on AC by the square on CB. 
But AC is equal to LO. 
Therefore the square on AB is greater than the square on LO by the square on CB. 
If then we cut off OR equal to BC, the square on AB will be greater than the square on LO by the square on OR. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "V.15" [fillcolor="#222244", URL="/heath/V/15/", target="_top"];
     "I.12" [fillcolor="#222244", URL="/heath/I/12/", target="_top"];
     "XI.7" [fillcolor="#222244", URL="/heath/XI/7/", target="_top"];
     "XI.8" [fillcolor="#222244", URL="/heath/XI/8/", target="_top"];
     "I.32" [fillcolor="#222244", URL="/heath/I/32/", target="_top"];
     "I.cn.1" [fillcolor="#442222", URL="/heath/I/cn.1/", target="_top"];
     "I.25" [fillcolor="#222244", URL="/heath/I/25/", target="_top"];
     "V.18" [fillcolor="#222244", URL="/heath/V/18/", target="_top"];
     "V.14" [fillcolor="#222244", URL="/heath/V/14/", target="_top"];
     "I.28" [fillcolor="#222244", URL="/heath/I/28/", target="_top"];
     "I.27" [fillcolor="#222244", URL="/heath/I/27/", target="_top"];
     "V.23" [fillcolor="#222244", URL="/heath/V/23/", target="_top"];
     "I.2" [fillcolor="#222244", URL="/heath/I/2/", target="_top"];
     "I.41" [fillcolor="#222244", URL="/heath/I/41/", target="_top"];
     "XI.22" [fillcolor="#222244", URL="/heath/XI/22/", target="_top"];
     "XI.11" [fillcolor="#222244", URL="/heath/XI/11/", target="_top"];
     "I.post.4" [fillcolor="#444422", URL="/heath/I/post.4/", target="_top"];
     "I.26" [fillcolor="#222244", URL="/heath/I/26/", target="_top"];
     "I.8" [fillcolor="#222244", URL="/heath/I/8/", target="_top"];
     "V.4" [fillcolor="#222244", URL="/heath/V/4/", target="_top"];
     "V.16" [fillcolor="#222244", URL="/heath/V/16/", target="_top"];
     "VI.2" [fillcolor="#222244", URL="/heath/VI/2/", target="_top"];
     "I.7" [fillcolor="#222244", URL="/heath/I/7/", target="_top"];
     "I.5" [fillcolor="#222244", URL="/heath/I/5/", target="_top"];
     "V.11" [fillcolor="#222244", URL="/heath/V/11/", target="_top"];
     "V.def.4" [fillcolor="#224422", URL="/heath/V/def.4/", target="_top"];
     "V.20" [fillcolor="#222244", URL="/heath/V/20/", target="_top"];
     "I.11" [fillcolor="#222244", URL="/heath/I/11/", target="_top"];
     "I.37" [fillcolor="#222244", URL="/heath/I/37/", target="_top"];
     "I.cn.3" [fillcolor="#442222", URL="/heath/I/cn.3/", target="_top"];
     "III.21" [fillcolor="#222244", URL="/heath/III/21/", target="_top"];
     "I.36" [fillcolor="#222244", URL="/heath/I/36/", target="_top"];
     "I.38" [fillcolor="#222244", URL="/heath/I/38/", target="_top"];
     "I.post.2" [fillcolor="#444422", URL="/heath/I/post.2/", target="_top"];
     "I.def.23" [fillcolor="#224422", URL="/heath/I/def.23/", target="_top"];
     "I.35" [fillcolor="#222244", URL="/heath/I/35/", target="_top"];
     "III.31" [fillcolor="#222244", URL="/heath/III/31/", target="_top"];
     "I.post.3" [fillcolor="#444422", URL="/heath/I/post.3/", target="_top"];
     "V.13" [fillcolor="#222244", URL="/heath/V/13/", target="_top"];
     "V.8" [fillcolor="#222244", URL="/heath/V/8/", target="_top"];
     "I.33" [fillcolor="#222244", URL="/heath/I/33/", target="_top"];
     "III.20" [fillcolor="#222244", URL="/heath/III/20/", target="_top"];
     "V.10" [fillcolor="#222244", URL="/heath/V/10/", target="_top"];
     "I.17" [fillcolor="#222244", URL="/heath/I/17/", target="_top"];
     "V.def.5" [fillcolor="#224422", URL="/heath/V/def.5/", target="_top"];
     "V.22" [fillcolor="#222244", URL="/heath/V/22/", target="_top"];
     "I.31" [fillcolor="#222244", URL="/heath/I/31/", target="_top"];
     "I.3" [fillcolor="#222244", URL="/heath/I/3/", target="_top"];
     "V.12" [fillcolor="#222244", URL="/heath/V/12/", target="_top"];
     "I.19" [fillcolor="#222244", URL="/heath/I/19/", target="_top"];
     "I.def.10" [fillcolor="#224422", URL="/heath/I/def.10/", target="_top"];
     "XI.def.3" [fillcolor="#224422", URL="/heath/XI/def.3/", target="_top"];
     "I.15" [fillcolor="#222244", URL="/heath/I/15/", target="_top"];
     "I.39" [fillcolor="#222244", URL="/heath/I/39/", target="_top"];
     "I.13" [fillcolor="#222244", URL="/heath/I/13/", target="_top"];
     "XI.3" [fillcolor="#222244", URL="/heath/XI/3/", target="_top"];
     "I.cn.2" [fillcolor="#442222", URL="/heath/I/cn.2/", target="_top"];
     "I.24" [fillcolor="#222244", URL="/heath/I/24/", target="_top"];
     "XI.1" [fillcolor="#222244", URL="/heath/XI/1/", target="_top"];
     "I.9" [fillcolor="#222244", URL="/heath/I/9/", target="_top"];
     "I.1" [fillcolor="#222244", URL="/heath/I/1/", target="_top"];
     "I.post.5" [fillcolor="#444422", URL="/heath/I/post.5/", target="_top"];
     "I.23" [fillcolor="#222244", URL="/heath/I/23/", target="_top"];
     "I.4" [fillcolor="#222244", URL="/heath/I/4/", target="_top"];
     "VI.4" [fillcolor="#222244", URL="/heath/VI/4/", target="_top"];
     "V.7" [fillcolor="#222244", URL="/heath/V/7/", target="_top"];
     "V.9" [fillcolor="#222244", URL="/heath/V/9/", target="_top"];
     "VI.1" [fillcolor="#222244", URL="/heath/VI/1/", target="_top"];
     "I.10" [fillcolor="#222244", URL="/heath/I/10/", target="_top"];
     "III.22" [fillcolor="#222244", URL="/heath/III/22/", target="_top"];
     "I.46" [fillcolor="#222244", URL="/heath/I/46/", target="_top"];
     "V.def.7" [fillcolor="#224422", URL="/heath/V/def.7/", target="_top"];
     "I.post.1" [fillcolor="#444422", URL="/heath/I/post.1/", target="_top"];
     "IV.1" [fillcolor="#222244", URL="/heath/IV/1/", target="_top"];
     "I.16" [fillcolor="#222244", URL="/heath/I/16/", target="_top"];
     "I.29" [fillcolor="#222244", URL="/heath/I/29/", target="_top"];
     "I.cn.4" [fillcolor="#442222", URL="/heath/I/cn.4/", target="_top"];
     "I.47" [fillcolor="#222244", URL="/heath/I/47/", target="_top"];
     "I.14" [fillcolor="#222244", URL="/heath/I/14/", target="_top"];
     "XI.12" [fillcolor="#222244", URL="/heath/XI/12/", target="_top"];
     "V.1" [fillcolor="#222244", URL="/heath/V/1/", target="_top"];
     "V.2" [fillcolor="#222244", URL="/heath/V/2/", target="_top"];
     "V.3" [fillcolor="#222244", URL="/heath/V/3/", target="_top"];
     "XI.23" [penwidth=3, color="white", fillcolor="#555555", URL="/heath/XI/23/", target="_top"];
     "I.18" [fillcolor="#222244", URL="/heath/I/18/", target="_top"];
     "V.21" [fillcolor="#222244", URL="/heath/V/21/", target="_top"];
     "I.34" [fillcolor="#222244", URL="/heath/I/34/", target="_top"];
     "I.def.15" [fillcolor="#224422", URL="/heath/I/def.15/", target="_top"];
     "XI.4" [fillcolor="#222244", URL="/heath/XI/4/", target="_top"];
     "V.17" [fillcolor="#222244", URL="/heath/V/17/", target="_top"];
     "XI.2" [fillcolor="#222244", URL="/heath/XI/2/", target="_top"];
     "V.16" -> "V.15";
     "V.23" -> "V.15";
     "VI.1" -> "V.15";
     "XI.11" -> "I.12";
     "XI.8" -> "XI.7";
     "XI.11" -> "XI.8";
     "XI.12" -> "XI.8";
     "III.20" -> "I.32";
     "III.22" -> "I.32";
     "III.31" -> "I.32";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.14" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.39" -> "I.cn.1";
     "XI.23" -> "I.25";
     "V.16" -> "V.18";
     "V.16" -> "V.14";
     "V.18" -> "V.14";
     "VI.4" -> "I.28";
     "I.28" -> "I.27";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "V.16" -> "V.23";
     "I.3" -> "I.2";
     "I.47" -> "I.41";
     "VI.1" -> "I.41";
     "XI.23" -> "XI.22";
     "XI.12" -> "XI.11";
     "I.14" -> "I.post.4";
     "I.15" -> "I.post.4";
     "I.34" -> "I.26";
     "XI.4" -> "I.26";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.12" -> "I.8";
     "I.23" -> "I.8";
     "XI.4" -> "I.8";
     "XI.23" -> "I.8";
     "V.22" -> "V.4";
     "V.23" -> "V.16";
     "VI.1" -> "V.16";
     "VI.4" -> "V.16";
     "XI.23" -> "V.16";
     "VI.4" -> "VI.2";
     "XI.23" -> "VI.2";
     "I.8" -> "I.7";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "I.24" -> "I.5";
     "III.20" -> "I.5";
     "III.31" -> "I.5";
     "V.16" -> "V.11";
     "V.18" -> "V.11";
     "V.23" -> "V.11";
     "VI.1" -> "V.11";
     "VI.2" -> "V.11";
     "V.8" -> "V.def.4";
     "V.16" -> "V.20";
     "V.22" -> "V.20";
     "I.13" -> "I.11";
     "I.46" -> "I.11";
     "XI.11" -> "I.11";
     "I.39" -> "I.37";
     "I.41" -> "I.37";
     "I.2" -> "I.cn.3";
     "I.14" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "III.22" -> "III.21";
     "I.38" -> "I.36";
     "VI.1" -> "I.38";
     "VI.2" -> "I.38";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
     "I.27" -> "I.def.23";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "XI.23" -> "III.31";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.12" -> "I.post.3";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.9" -> "V.8";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "I.36" -> "I.33";
     "III.21" -> "III.20";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "III.31" -> "I.17";
     "VI.4" -> "I.17";
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.22" -> "V.def.5";
     "VI.1" -> "V.def.5";
     "V.16" -> "V.22";
     "VI.4" -> "V.22";
     "I.32" -> "I.31";
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.39" -> "I.31";
     "I.46" -> "I.31";
     "XI.11" -> "I.31";
     "XI.12" -> "I.31";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "V.15" -> "V.12";
     "I.24" -> "I.19";
     "I.11" -> "I.def.10";
     "I.12" -> "I.def.10";
     "I.13" -> "I.def.10";
     "III.31" -> "I.def.10";
     "XI.4" -> "XI.def.3";
     "XI.8" -> "XI.def.3";
     "XI.11" -> "XI.def.3";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "XI.4" -> "I.15";
     "VI.2" -> "I.39";
     "I.14" -> "I.13";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.32" -> "I.13";
     "XI.7" -> "XI.3";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.47" -> "I.cn.2";
     "I.25" -> "I.24";
     "XI.22" -> "I.24";
     "XI.2" -> "XI.1";
     "I.10" -> "I.9";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.post.5";
     "VI.4" -> "I.post.5";
     "I.24" -> "I.23";
     "I.31" -> "I.23";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.24" -> "I.4";
     "I.25" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.47" -> "I.4";
     "XI.4" -> "I.4";
     "XI.22" -> "I.4";
     "XI.23" -> "I.4";
     "XI.23" -> "VI.4";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "VI.2" -> "V.7";
     "VI.2" -> "V.9";
     "VI.2" -> "VI.1";
     "I.12" -> "I.10";
     "I.16" -> "I.10";
     "III.31" -> "III.22";
     "I.47" -> "I.46";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.12" -> "I.post.1";
     "I.16" -> "I.post.1";
     "XI.23" -> "IV.1";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.32" -> "I.29";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.46" -> "I.29";
     "XI.8" -> "I.29";
     "XI.23" -> "I.29";
     "I.4" -> "I.cn.4";
     "XI.23" -> "I.47";
     "I.47" -> "I.14";
     "XI.23" -> "XI.12";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.17" -> "V.1";
     "V.3" -> "V.2";
     "V.17" -> "V.2";
     "V.4" -> "V.3";
     "I.19" -> "I.18";
     "V.16" -> "V.21";
     "V.23" -> "V.21";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "I.46" -> "I.34";
     "VI.4" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "XI.8" -> "XI.4";
     "XI.11" -> "XI.4";
     "V.16" -> "V.17";
     "V.18" -> "V.17";
     "XI.8" -> "XI.2";
   }
