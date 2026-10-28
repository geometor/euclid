#!/usr/bin/env python3
"""Wire line-keyed proposition notes across Volume II to RST footnotes ([#f1]_ / .. [#f1])."""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

_REPO_ROOT = Path(__file__).resolve().parents[1]
_VOL2_DIR = _REPO_ROOT / "resources" / "heath" / "volume_II"

# List of (relative_path, old_substring, new_substring)
_REPLACEMENTS: List[Tuple[str, str, str]] = [
    # 1. Book III Prop. 1 (0012.rst & 0013.rst)
    (
        "book_iii/propositions/0012.rst",
        "For suppose it is not, but, if possible, let :g:`$G$ <0012.g1:G>` be the centre,",
        r"For suppose it is not,\ [#f1]_ but, if possible, let :g:`$G$ <0012.g1:G>` be the centre,",
    ),
    (
        "book_iii/propositions/0012.rst",
        "   the two sides :g:`$AD$ <0012.g1:/ A D />`, :g:`$DG$ <0012.g1:/ D G />` are equal to the two sides :g:`$BD$ <0012.g1:/ B D />`, :g:`$DG$ <0012.g1:/ D G />` respectively;",
        r"   the two sides :g:`$AD$ <0012.g1:/ A D />`, :g:`$DG$ <0012.g1:/ D G />` are equal to the two sides :g:`$BD$ <0012.g1:/ B D />`, :g:`$DG$ <0012.g1:/ D G />` respectively;\ [#f2]_",
    ),
    (
        "book_iii/propositions/0013.rst",
        "**12. For suppose it is not.** This is expressed in the Greek by the two words Μὴ γάρ, but such an elliptical phrase is impossible in English.\n\n**17. the two sides AD, DG are equal to the two sides BD, DG respectively.**",
        ".. [#f1] **For suppose it is not.** This is expressed in the Greek by the two words Μὴ γάρ, but such an elliptical phrase is impossible in English.\n\n.. [#f2] **the two sides AD, DG are equal to the two sides BD, DG respectively.**",
    ),
    # 2. Book III Prop. 3 (0017.rst)
    (
        "book_iii/propositions/0017.rst",
        "For, with the same construction,",
        r"For, with the same construction,\ [#f1]_",
    ),
    (
        "book_iii/propositions/0017.rst",
        "**26. with the same construction**, τῶν αὐτῶν κατασκευασθέντων.",
        ".. [#f1] **with the same construction**, τῶν αὐτῶν κατασκευασθέντων.",
    ),
    # 3. Book III Prop. 7 (0020.rst & 0021.rst)
    (
        "book_iii/propositions/0020.rst",
        "the remainder of the same diameter will be least, and of the rest the nearer to the straight line through the centre is always greater than the more remote, and only two equal straight lines will fall from the point on the circle, one on each side of the least straight line.",
        r"the remainder of the same diameter\ [#f1]_ will be least, and of the rest the nearer to the straight line through the centre is always greater than the more remote, and only two equal straight lines will fall from the point on the circle, one on each side\ [#f2]_ of the least straight line.",
    ),
    (
        "book_iii/propositions/0021.rst",
        "I say also that from the point :g:`$F$ <0020.g1:F>` only two equal straight lines will fall on the circle :g:`$ABCD$ <0020.g1:( A B C D )>`, one on each side of the least :g:`$FD$ <0020.g1:/ F D />`.",
        r"I say also that from the point :g:`$F$ <0020.g1:F>` only two equal straight lines will fall on the circle :g:`$ABCD$ <0020.g1:( A B C D )>`, one on each side\ [#f2]_ of the least :g:`$FD$ <0020.g1:/ F D />`.",
    ),
    (
        "book_iii/propositions/0021.rst",
        "**4. of the same diameter.** I have inserted these words for clearness' sake. The text has simply ἐλαχίστη δὲ ἡ λοιπή, \"and the remaining (straight line) least.\"\n\n**7, 39. one on each side.**",
        ".. [#f1] **of the same diameter.** I have inserted these words for clearness' sake. The text has simply ἐλαχίστη δὲ ἡ λοιπή, \"and the remaining (straight line) least.\"\n\n.. [#f2] **one on each side.**",
    ),
    # 4. Book III Prop. 10 (0029.rst)
    (
        "book_iii/propositions/0029.rst",
        "   A circle does not cut a circle at more points than two.",
        r"   A circle\ [#f1]_ does not cut a circle at more points than two.",
    ),
    (
        "book_iii/propositions/0029.rst",
        r"**1.** The word **circle** ($\kappa\acute{\upsilon}\kappa\lambda\omicron\varsigma$)",
        r".. [#f1] The word **circle** ($\kappa\acute{\upsilon}\kappa\lambda\omicron\varsigma$)",
    ),
    # 5. Book III Prop. 11 (0030.rst & 0031.rst)
    (
        "book_iii/propositions/0030.rst",
        "   If two circles touch one another internally, and their centres be taken, the straight line joining their centres, if it be also produced, will fall on the point of contact of the circles.",
        r"   If two circles touch one another internally, and their centres be taken, the straight line joining their centres,\ [#f1]_ if it be also produced, will fall on the point of contact\ [#f2]_ of the circles.",
    ),
    (
        "book_iii/propositions/0031.rst",
        "**2. the straight line joining their centres**, literally \"the straight line joined to their centres\" (ἡ ἐπὶ τὰ κέντρα αὐτῶν ἐπιζευγνυμένη εὐθεῖα).\n\n**3. point of contact**",
        ".. [#f1] **the straight line joining their centres**, literally \"the straight line joined to their centres\" (ἡ ἐπὶ τὰ κέντρα αὐτῶν ἐπιζευγνυμένη εὐθεῖα).\n\n.. [#f2] **point of contact**",
    ),
    # 6. Book III Prop. 12 (0034.rst)
    (
        "book_iii/propositions/0034.rst",
        "Therefore the straight line joined from :g:`$F$ <0034.g1:F>` to :g:`$G$ <0034.g1:G>` will not fail to pass through the point of contact at :g:`$A$ <0034.g1:A>`;",
        r"Therefore the straight line joined from :g:`$F$ <0034.g1:F>` to :g:`$G$ <0034.g1:G>` will not fail to pass\ [#f1]_ through the point of contact at :g:`$A$ <0034.g1:A>`;",
    ),
    (
        "book_iii/propositions/0034.rst",
        "**23. will not fail to pass.**",
        ".. [#f1] **will not fail to pass.**",
    ),
    # 7. Book III Prop. 13 (0038.rst & 0039.rst)
    (
        "book_iii/propositions/0038.rst",
        "For, if possible, let the circle :g:`$ABDC$ <0038.g3:( A B D C )>` touch the circle",
        r"For, if possible, let the circle :g:`$ABDC$ <0038.g3:( A B D C )>`\ [#f1]_ touch the circle",
    ),
    (
        "book_iii/propositions/0039.rst",
        "I say further that neither does it so touch it externally.\n\nFor, if possible, let the circle :g:`$ACK$ <0038.g3:( A C K )>` touch the circle\n:g:`$ABDC$ <0038.g3:( A B D C )>` at more points than one,",
        r"I say further that neither does it so touch it\ [#f2]_ externally." + "\n\nFor, if possible, let the circle :g:`$ACK$ <0038.g3:( A C K )>` touch the circle\n" + r":g:`$ABDC$ <0038.g3:( A B D C )>`\ [#f1]_ at more points than one,",
    ),
    (
        "book_iii/propositions/0039.rst",
        "**3, 7, 14, 27, 30, 33. ABDC.** Euclid writes :g:`$ABCD$ <0038.g3:( A B C D )>` (here and in the next proposition), notwithstanding the order in which the points are placed in the figure.\n\n**25, 37. does it so touch it.** It is necessary to supply these words which the Greek ($\\text{ὅτι οὐδὲ ἐκτός}$ and $\\text{ὅτι οὐδὲ ἐντός}$) leaves to be understood.\n\n----",
        ".. [#f1] **ABDC.** Euclid writes :g:`$ABCD$ <0038.g3:( A B C D )>` (here and in the next proposition), notwithstanding the order in which the points are placed in the figure.\n\n.. [#f2] **does it so touch it.** It is necessary to supply these words which the Greek ($\\text{ὅτι οὐδὲ ἐκτός}$ and $\\text{ὅτι οὐδὲ ἐντός}$) leaves to be understood.",
    ),
    # 8. Book III Prop. 15 (0042.rst & 0043.rst)
    (
        "book_iii/propositions/0042.rst",
        "   Of straight lines in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote.\n\nLet :g:`$ABCD$ <0042.g1:( A B C D )>` be a circle, let :g:`$AD$ <0042.g1:/ A D />` be its diameter and :g:`$E$ <0042.g1:E>`\nthe centre; and let :g:`$BC$ <0042.g1:/ B C />` be nearer to the\ndiameter :g:`$AD$ <0042.g1:/ A D />`, and :g:`$FG$ <0042.g1:/ F G />` more remote;",
        r"   Of straight lines\ [#f1]_ in a circle the diameter is greatest, and of the rest the nearer to the centre is always greater than the more remote." + "\n\nLet :g:`$ABCD$ <0042.g1:( A B C D )>` be a circle, let :g:`$AD$ <0042.g1:/ A D />` be its diameter and :g:`$E$ <0042.g1:E>`\nthe centre; and let :g:`$BC$ <0042.g1:/ B C />` be nearer to the\n" + r"diameter :g:`$AD$ <0042.g1:/ A D />`,\ [#f2]_ and :g:`$FG$ <0042.g1:/ F G />` more remote;",
    ),
    (
        "book_iii/propositions/0043.rst",
        "**1. Of straight lines.** The Greek leaves these words to be understood.\n\n**5. Nearer to the diameter AD.** As :g:`$BC$ <0042.g1:/ B C />`, :g:`$FG$ <0042.g1:/ F G />` are not in general parallel to :g:`$AD$ <0042.g1:/ A D />`, Euclid should have said \"nearer to the centre.\"\n\n----",
        ".. [#f1] **Of straight lines.** The Greek leaves these words to be understood.\n\n.. [#f2] **Nearer to the diameter AD.** As :g:`$BC$ <0042.g1:/ B C />`, :g:`$FG$ <0042.g1:/ F G />` are not in general parallel to :g:`$AD$ <0042.g1:/ A D />`, Euclid should have said \"nearer to the centre.\"",
    ),
    # 9. Book III Prop. 16 (0043.rst & 0045.rst)
    (
        "book_iii/propositions/0043.rst",
        "   The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed; further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.",
        r"   The straight line drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the straight line and the circumference another straight line cannot be interposed;\ [#f1]_ further the angle of the semicircle is greater, and the remaining angle less, than any acute rectilineal angle.",
    ),
    (
        "book_iii/propositions/0045.rst",
        "But such a straight line cannot be interposed;",
        r"But such a straight line cannot be interposed;\ [#f1]_",
    ),
    (
        "book_iii/propositions/0045.rst",
        "**4. cannot be interposed**, literally \"will not fall in between\" ($\\text{οὐ παρεμπεσεῖται}$).\n\n----",
        ".. [#f1] **cannot be interposed**, literally \"will not fall in between\" ($\\text{οὐ παρεμπεσεῖται}$).",
    ),
    # 10. Book III Prop. 18 (0050.rst & 0051.rst)
    (
        "book_iii/propositions/0050.rst",
        "   If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.",
        r"   If a straight line touch a circle, and a straight line be joined from the centre to the point of contact, the straight line so joined will be perpendicular to the tangent.\ [#f1]_",
    ),
    (
        "book_iii/propositions/0051.rst",
        "**3. the tangent**, $\\text{ἡ ἐφαπτομένη}$.\n\n----",
        "----\n\n.. [#f1] **the tangent**, $\\text{ἡ ἐφαπτομένη}$.",
    ),
    # 11. Book III Prop. 20 (0052.rst & 0053.rst)
    (
        "book_iii/propositions/0052.rst",
        "Again let another straight line be inflected, and let there",
        r"Again let another straight line be inflected,\ [#f1]_ and let there",
    ),
    (
        "book_iii/propositions/0053.rst",
        "**25. let another straight line be inflected**, $\\text{κεκλάσθω δὴ πάλιν}$ (without $\\text{εὐθεῖα}$). The verb $\\text{κλάω}$ (to *break off*) was the regular technical term for drawing from a point a (broken) straight line which first meets another straight line or curve and is then *bent back* from it to another point, or (in other words) for drawing straight lines from two points meeting at a point on a curve or another straight line. $\\text{κεκλάσθαι}$ is one of the geometrical terms the definition of which must according to :person:`Aristotle <aristotle>` be assumed (:cite:`*Anal. Post.* I. 10, 76 b 9 <aristotle:anal-post:i-10-76-b-9>`).\n\n----",
        ".. [#f1] **let another straight line be inflected**, $\\text{κεκλάσθω δὴ πάλιν}$ (without $\\text{εὐθεῖα}$). The verb $\\text{κλάω}$ (to *break off*) was the regular technical term for drawing from a point a (broken) straight line which first meets another straight line or curve and is then *bent back* from it to another point, or (in other words) for drawing straight lines from two points meeting at a point on a curve or another straight line. $\\text{κεκλάσθαι}$ is one of the geometrical terms the definition of which must according to :person:`Aristotle <aristotle>` be assumed (:cite:`*Anal. Post.* I. 10, 76 b 9 <aristotle:anal-post:i-10-76-b-9>`).",
    ),
    # 12. Book III Prop. 23 (0058.rst & 0059.rst)
    (
        "book_iii/propositions/0058.rst",
        "   On the same straight line there cannot be constructed two similar and unequal segments of circles on the same side.",
        r"   On the same straight line there cannot be constructed\ [#f1]_ two similar and unequal segments of circles on the same side.",
    ),
    (
        "book_iii/propositions/0059.rst",
        "**1. cannot be constructed**, $\\text{οὐ συσταθήσεται}$, the same phrase as in I. 7.\n\n----",
        ".. [#f1] **cannot be constructed**, $\\text{οὐ συσταθήσεται}$, the same phrase as in I. 7.",
    ),
    # 13 & 14. Book III Props. 24 & 25 (0060.rst & 0062.rst)
    (
        "book_iii/propositions/0060.rst",
        "or it will fall awry, as :g:`$CGD$ <0060.g1:( C G D )>`, and a circle cuts a circle at more",
        r"or it will fall awry,\ [#f1]_ as :g:`$CGD$ <0060.g1:( C G D )>`, and a circle cuts a circle at more",
    ),
    (
        "book_iii/propositions/0060.rst",
        "**15. fall awry**, $\\text{παραλλάξει}$, the same word as used in the like case in I. 8. The word implies that the applied figure will partly fall short of, and partly overlap, the figure to which it is applied.\n\n----",
        ".. [#f1] **fall awry**, $\\text{παραλλάξει}$, the same word as used in the like case in I. 8. The word implies that the applied figure will partly fall short of, and partly overlap, the figure to which it is applied.",
    ),
    (
        "book_iii/propositions/0060.rst",
        "   Given a segment of a circle, to describe the complete circle of which it is a segment.",
        r"   Given a segment of a circle, to describe the complete circle\ [#f1]_ of which it is a segment.",
    ),
    (
        "book_iii/propositions/0062.rst",
        "**1. to describe the complete circle**, $\\text{προσαναγράψαι τὸν κύκλον}$, literally “to describe the circle *on to it*.”\n\n----",
        ".. [#f1] **to describe the complete circle**, $\\text{προσαναγράψαι τὸν κύκλον}$, literally “to describe the circle *on to it*.”",
    ),
    # 15. Book IV Prop. 3 (0089.rst & 0090.rst)
    (
        "book_iv/propositions/0089.rst",
        "the straight line :g:`$KB$ <0089.g1:/ K B />` be drawn across at random;",
        r"the straight line :g:`$KB$ <0089.g1:/ K B />` be drawn across at random;\ [#f1]_",
    ),
    (
        "book_iv/propositions/0090.rst",
        "are equal to four right angles, inasmuch as :g:`$AMBK$ <0089.g1:< A M B K >>` is in fact\ndivisible into two triangles,",
        "are equal to four right angles, inasmuch as :g:`$AMBK$ <0089.g1:< A M B K >>` is in fact\n" + r"divisible\ [#f2]_ into two triangles,",
    ),
    (
        "book_iv/propositions/0090.rst",
        "**10. at random**, literally \"as it may chance,\" ὡς ἔτυχεν. The same expression is used in III. 1 and commonly.\n\n**22. is in fact divisible**, καὶ διαιρεῖται, literally \"is actually divided.\"\n\n----",
        ".. [#f1] **at random**, literally \"as it may chance,\" ὡς ἔτυχεν. The same expression is used in III. 1 and commonly.\n\n.. [#f2] **is in fact divisible**, καὶ διαιρεῖται, literally \"is actually divided.\"",
    ),
    # 16. Book IV Prop. 4 (0091.rst & 0092.rst)
    (
        "book_iv/propositions/0091.rst",
        "one of the straight lines :g:`$DE$ <0091.g1:/ D E />`, :g:`$DF$ <0091.g1:/ D F />`, :g:`$DG$ <0091.g1:/ D G />` will pass also",
        r"one of the straight lines :g:`$DE$ <0091.g1:/ D E />`, :g:`$DF$ <0091.g1:/ D F />`, :g:`$DG$ <0091.g1:/ D G />`\ [#f1]_ will pass also",
    ),
    (
        "book_iv/propositions/0092.rst",
        "one of the straight lines :g:`$DE$ <0091.g1:/ D E />`, :g:`$DF$ <0091.g1:/ D F />`, :g:`$DG$ <0091.g1:/ D G />` will not cut the",
        r"one of the straight lines :g:`$DE$ <0091.g1:/ D E />`, :g:`$DF$ <0091.g1:/ D F />`, :g:`$DG$ <0091.g1:/ D G />`\ [#f1]_ will not cut the",
    ),
    (
        "book_iv/propositions/0092.rst",
        "**26, 34. and distance one of the (straight lines D)E, (D)F, (D**) :g:`$G$ <0091.g1:G>`. The words and letters here shown in brackets are put in to fill out the rather careless language of the Greek. Here and in several other places in Book IV. Euclid says literally \"and with distance one of the (points) $E$, $F$, $G$\" ($\\kappa\\alpha\\grave{\\iota}\\ \\delta\\iota\\alpha\\sigma\\tau\\acute{\\eta}\\mu\\alpha\\tau\\iota\\ \\dot{\\varepsilon}\\nu\\grave{\\iota}\\ \\tau\\tilde{\\omega}\\nu\\ \\text{E, Z, H}$) and the like. In one case (IV. 13) he actually has \"with distance one of the *points* $G$, $H$, $K$, $L$, $M$\" ($\\delta\\iota\\alpha\\sigma\\tau\\acute{\\eta}\\mu\\alpha\\tau\\iota\\ \\dot{\\varepsilon}\\nu\\grave{\\iota}\\ \\tau\\tilde{\\omega}\\nu\\ \\text{H, }\\Theta\\text{, K, }\\Lambda\\text{, M }\\sigma\\eta\\mu\\varepsilon\\acute{\\iota}\\omega\\nu$). :person:`Heiberg <heiberg>` notes \"Graecam locutionem satis miram et negligentem,\" but, in view of its frequent occurrence in good MSS., does not venture to correct it.\n\n----",
        ".. [#f1] **and distance one of the (straight lines D)E, (D)F, (D** :g:`$G$ <0091.g1:G>` **)**. The words and letters here shown in brackets are put in to fill out the rather careless language of the Greek. Here and in several other places in Book IV. Euclid says literally \"and with distance one of the (points) $E$, $F$, $G$\" ($\\kappa\\alpha\\grave{\\iota}\\ \\delta\\iota\\alpha\\sigma\\tau\\acute{\\eta}\\mu\\alpha\\tau\\iota\\ \\dot{\\varepsilon}\\nu\\grave{\\iota}\\ \\tau\\tilde{\\omega}\\nu\\ \\text{E, Z, H}$) and the like. In one case (IV. 13) he actually has \"with distance one of the *points* $G$, $H$, $K$, $L$, $M$\" ($\\delta\\iota\\alpha\\sigma\\tau\\acute{\\eta}\\mu\\alpha\\tau\\iota\\ \\dot{\\varepsilon}\\nu\\grave{\\iota}\\ \\tau\\tilde{\\omega}\\nu\\ \\text{H, }\\Theta\\text{, K, }\\Lambda\\text{, M }\\sigma\\eta\\mu\\varepsilon\\acute{\\iota}\\omega\\nu$). :person:`Heiberg <heiberg>` notes \"Graecam locutionem satis miram et negligentem,\" but, in view of its frequent occurrence in good MSS., does not venture to correct it.",
    ),
    # 17. Book V Prop. 5 (0151.rst & 0152.rst)
    (
        "book_v/propositions/0151.rst",
        "For, whatever multiple :g:`$AE$ <0151.g1:/ A E />` is of :g:`$CF$ <0151.g1:/ C F />`, let :g:`$EB$ <0151.g1:/ E B />` be made that multiple of :g:`$CG$ <0151.g1:/ C G />`.",
        r"For, whatever multiple :g:`$AE$ <0151.g1:/ A E />` is of :g:`$CF$ <0151.g1:/ C F />`, let :g:`$EB$ <0151.g1:/ E B />` be made that multiple of :g:`$CG$ <0151.g1:/ C G />`.\ [#f1]_",
    ),
    (
        "book_v/propositions/0152.rst",
        "**10. let EB be made that multiple of** :g:`$CG$ <0151.g1:/ C G />`,",
        ".. [#f1] **let EB be made that multiple of** :g:`$CG$ <0151.g1:/ C G />`,",
    ),
    # 18. Book V Prop. 16 (0170.rst & 0171.rst)
    (
        "book_v/propositions/0170.rst",
        "Let :g:`$A$ <0170.g1:A>`, :g:`$B$ <0170.g1:B>`, :g:`$C$ <0170.g1:C>`, :g:`$D$ <0170.g1:D>` be four proportional magnitudes, so that, as :g:`$A$ <0170.g1:A>` is to :g:`$B$ <0170.g1:B>`, so is :g:`$C$ <0170.g1:C>` to :g:`$D$ <0170.g1:D>` ;",
        r"Let :g:`$A$ <0170.g1:A>`, :g:`$B$ <0170.g1:B>`, :g:`$C$ <0170.g1:C>`, :g:`$D$ <0170.g1:D>` be four proportional magnitudes, so that, as :g:`$A$ <0170.g1:A>` is to :g:`$B$ <0170.g1:B>`, so is :g:`$C$ <0170.g1:C>` to :g:`$D$ <0170.g1:D>` ;\ [#f1]_",
    ),
    (
        "book_v/propositions/0171.rst",
        "3. \"**Let** :g:`$A$ <0170.g1:A>`, :g:`$B$ <0170.g1:B>`, :g:`$C$ <0170.g1:C>`, :g:`$D$ <0170.g1:D>` **be four proportional magnitudes,",
        ".. [#f1] \"**Let** :g:`$A$ <0170.g1:A>`, :g:`$B$ <0170.g1:B>`, :g:`$C$ <0170.g1:C>`, :g:`$D$ <0170.g1:D>` **be four proportional magnitudes,",
    ),
    # 19. Book VI Prop. 1 (0197.rst & 0198.rst)
    (
        "book_vi/propositions/0197.rst",
        "Let :g:`$ABC$ <0197.g1:< A B C >>`, :g:`$ACD$ <0197.g1:< A C D >>` be triangles and :g:`$EC$ <0197.g1:< E C >>`, :g:`$CF$ <0197.g1:< C F >>` parallelograms under the same height;",
        r"Let :g:`$ABC$ <0197.g1:< A B C >>`, :g:`$ACD$ <0197.g1:< A C D >>` be triangles and :g:`$EC$ <0197.g1:< E C >>`, :g:`$CF$ <0197.g1:< C F >>` parallelograms under the same height;\ [#f1]_",
    ),
    (
        "book_vi/propositions/0197.rst",
        "   the triangles :g:`$ABC$ <0197.g1:< A B C >>`, :g:`$AGB$ <0197.g1:< A G B >>`, :g:`$AHG$ <0197.g1:< A H G >>` are also equal to one another. :just:`[I. 38] <I.38>`",
        r"   the triangles :g:`$ABC$ <0197.g1:< A B C >>`, :g:`$AGB$ <0197.g1:< A G B >>`, :g:`$AHG$ <0197.g1:< A H G >>`\ [#f2]_ are also equal to one another. :just:`[I. 38] <I.38>`",
    ),
    (
        "book_vi/propositions/0198.rst",
        "Since, then, it was proved that, as the base :g:`$BC$ <0197.g1:/ B C />` is to :g:`$CD$ <0197.g1:/ C D />`, so is the triangle :g:`$ABC$ <0197.g1:< A B C >>` to the triangle :g:`$ACD$ <0197.g1:< A C D >>`, and, as the triangle :g:`$ABC$ <0197.g1:< A B C >>` is to the triangle :g:`$ACD$ <0197.g1:< A C D >>`, so is the parallelogram :g:`$EC$ <0197.g1:< E C >>` to the parallelogram :g:`$CF$ <0197.g1:< C F >>`,",
        r"Since, then, it was proved that, as the base :g:`$BC$ <0197.g1:/ B C />` is to :g:`$CD$ <0197.g1:/ C D />`, so is the triangle :g:`$ABC$ <0197.g1:< A B C >>` to the triangle :g:`$ACD$ <0197.g1:< A C D >>`,\ [#f3]_ and, as the triangle :g:`$ABC$ <0197.g1:< A B C >>` is to the triangle :g:`$ACD$ <0197.g1:< A C D >>`, so is the parallelogram :g:`$EC$ <0197.g1:< E C >>` to the parallelogram :g:`$CF$ <0197.g1:< C F >>`,",
    ),
    (
        "book_vi/propositions/0198.rst",
        "**4. Under the same height.**",
        ".. [#f1] **Under the same height.**",
    ),
    (
        "book_vi/propositions/0198.rst",
        "**14. ABC, AGB**, :g:`$AHG$ <0197.g1:< A H G >>`.",
        ".. [#f2] **ABC, AGB**, :g:`$AHG$ <0197.g1:< A H G >>`.",
    ),
    (
        "book_vi/propositions/0198.rst",
        "**46. Since then it was proved that, as the base**",
        ".. [#f3] **Since then it was proved that, as the base**",
    ),
    # 20. Book VI Prop. 9 (0218.rst)
    (
        "book_vi/propositions/0218.rst",
        "Let a straight line :g:`$AC$ <0218.g1:/ A C />` be drawn through from :g:`$A$ <0218.g1:A>` containing with :g:`$AB$ <0218.g1:/ A B />` any angle;",
        r"Let a straight line :g:`$AC$ <0218.g1:/ A C />` be drawn through from :g:`$A$ <0218.g1:A>` containing with :g:`$AB$ <0218.g1:/ A B />` any angle;\ [#f1]_",
    ),
    (
        "book_vi/propositions/0218.rst",
        "**6. any angle.**",
        ".. [#f1] **any angle.**",
    ),
    # 21. Book VI Prop. 11 (0220.rst)
    (
        "book_vi/propositions/0220.rst",
        "   To two given straight lines to find a third proportional.",
        r"   To two given straight lines to find\ [#f1]_ a third proportional.",
    ),
    (
        "book_vi/propositions/0220.rst",
        "**1. to find.**",
        ".. [#f1] **to find.**",
    ),
    # 22. Book VI Prop. 19 (0238.rst & 0239.rst)
    (
        "book_vi/propositions/0238.rst",
        "and such that, as :g:`$AB$ <0238.g2:/ A B />` is to :g:`$BC$ <0238.g2:/ B C />`, so is :g:`$DE$ <0238.g2:/ D E />` to :g:`$EF$ <0238.g2:/ E F />`, so that :g:`$BC$ <0238.g2:/ B C />` corresponds to :g:`$EF$ <0238.g2:/ E F />`;",
        r"and such that, as :g:`$AB$ <0238.g2:/ A B />` is to :g:`$BC$ <0238.g2:/ B C />`, so is :g:`$DE$ <0238.g2:/ D E />` to :g:`$EF$ <0238.g2:/ E F />`,\ [#f1]_ so that :g:`$BC$ <0238.g2:/ B C />` corresponds to :g:`$EF$ <0238.g2:/ E F />`;",
    ),
    (
        "book_vi/propositions/0239.rst",
        "**4. and such that, as**",
        ".. [#f1] **and such that, as**",
    ),
    # 23. Book VI Prop. 20 (0241.rst, 0242.rst, 0244.rst)
    (
        "book_vi/propositions/0241.rst",
        "   Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon",
        r"   Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes,\ [#f1]_ and the polygon",
    ),
    (
        "book_vi/propositions/0242.rst",
        "while :g:`$FGL$ <0241.g1:< F G L >>`, :g:`$LGH$ <0241.g1:< L G H >>`, :g:`$LHK$ <0241.g1:< L H K >>` are their consequents, and that the polygon",
        r"while :g:`$FGL$ <0241.g1:< F G L >>`, :g:`$LGH$ <0241.g1:< L G H >>`, :g:`$LHK$ <0241.g1:< L H K >>` are their consequents,\ [#f2]_ and that the polygon",
    ),
    (
        "book_vi/propositions/0244.rst",
        "**2.** **in the same ratio as the wholes.**",
        ".. [#f1] **in the same ratio as the wholes.**",
    ),
    (
        "book_vi/propositions/0244.rst",
        "**49.** **ἑπόμενα αὐτῶν, \"their consequents,\"**",
        ".. [#f2] **ἑπόμενα αὐτῶν, \"their consequents,\"**",
    ),
    # 24. Book VI Prop. 23 (0253.rst & 0254.rst)
    (
        "book_vi/propositions/0253.rst",
        "   Equiangular parallelograms have to one another the ratio compounded of the ratios of their sides.",
        r"   Equiangular parallelograms have to one another the ratio compounded of the ratios of their sides.\ [#f1]_",
    ),
    (
        "book_vi/propositions/0253.rst",
        "I say that the parallelogram :g:`$AC$ <0253.g1:< A C >>` has to the parallelogram :g:`$CF$ <0253.g1:< C F >>` the ratio compounded of the ratios of the sides.",
        r"I say that the parallelogram :g:`$AC$ <0253.g1:< A C >>` has to the parallelogram :g:`$CF$ <0253.g1:< C F >>` the ratio compounded of the ratios of the sides.\ [#f1]_",
    ),
    (
        "book_vi/propositions/0253.rst",
        "Let the parallelogram :g:`$DG$ <0253.g1:< D G >>` be completed; let a straight line :g:`$K$ <0253.g1:K>` be set out, and let it be contrived that,",
        r"Let the parallelogram :g:`$DG$ <0253.g1:< D G >>` be completed; let a straight line :g:`$K$ <0253.g1:K>` be set out, and let it be contrived that,\ [#f2]_",
    ),
    (
        "book_vi/propositions/0254.rst",
        "   so that :g:`$K$ <0253.g1:K>` has also to :g:`$M$ <0253.g1:M>` the ratio compounded of the ratios of the sides.",
        r"   so that :g:`$K$ <0253.g1:K>` has also to :g:`$M$ <0253.g1:M>` the ratio compounded of the ratios of the sides.\ [#f1]_",
    ),
    (
        "book_vi/propositions/0254.rst",
        "1, 6, 19, 36. **the ratio compounded of the ratios of the sides**,",
        ".. [#f1] **the ratio compounded of the ratios of the sides**,",
    ),
    (
        "book_vi/propositions/0254.rst",
        "11. **let it be contrived that, as**",
        ".. [#f2] **let it be contrived that, as**",
    ),
    # 25. Book VI Prop. 25 (0259.rst & 0260.rst)
    (
        "book_vi/propositions/0259.rst",
        "Let :g:`$ABC$ <0259.g1:< A B C >>` be the given rectilineal figure to which the figure to be constructed must be similar, and :g:`$D$ <0259.g1:< D >>` that to which it must be equal ;",
        r"Let :g:`$ABC$ <0259.g1:< A B C >>` be the given rectilineal figure to which the figure to be constructed must be similar,\ [#f1]_ and :g:`$D$ <0259.g1:< D >>` that to which it must be equal ;",
    ),
    (
        "book_vi/propositions/0260.rst",
        "**3. to which the figure to be constructed must be similar,**",
        ".. [#f1] **to which the figure to be constructed must be similar,**",
    ),
    # 26. Book VII Prop. 16 (0322.rst)
    (
        "book_vii/propositions/0322.rst",
        r"the numbers so produced\ [#f316_1]_ will be equal to one another.",
        r"the numbers so produced\ [#f1]_ will be equal to one another.",
    ),
    (
        "book_vii/propositions/0322.rst",
        ".. [#f316_1] **2. The numbers so produced.** The Greek has οἱ γενόμενοι ἐξ αὐτῶν, \"the (numbers) produced *from them*.\" By \"from them\" Euclid means \"from the original numbers,\" though this is not very clear even in the Greek. I think ambiguity is best avoided by leaving out the words.\n\n----",
        "----\n\n.. [#f1] **The numbers so produced.** The Greek has οἱ γενόμενοι ἐξ αὐτῶν, \"the (numbers) produced *from them*.\" By \"from them\" Euclid means \"from the original numbers,\" though this is not very clear even in the Greek. I think ambiguity is best avoided by leaving out the words.",
    ),
    # 27. Book VII Props. 24 & 25 (0331.rst, 0332.rst, 0333.rst)
    (
        "book_vii/propositions/0331.rst",
        "   If two numbers be prime to any number, their product also will be prime to the same.",
        r"   If two numbers be prime to any number, their product\ [#f1]_ also will be prime to the same.",
    ),
    (
        "book_vii/propositions/0332.rst",
        ".. [#f326_1] **their product.**",
        ".. [#f1] **their product.**",
    ),
    (
        "book_vii/propositions/0332.rst",
        "   If two numbers be prime to one another, the product of one of them into itself will be prime to the remaining one.",
        r"   If two numbers be prime to one another, the product of one of them into itself\ [#f1]_ will be prime to the remaining one.",
    ),
    (
        "book_vii/propositions/0333.rst",
        ".. [#f327_1] **the product of one of them into itself.**",
        ".. [#f1] **the product of one of them into itself.**",
    ),
    # 28. Book VII Prop. 31 (0338.rst & 0339.rst)
    (
        "book_vii/propositions/0338.rst",
        "   Now, if :g:`$B$ <0338.g1:B>` is prime, what was enjoined will have been done.",
        r"   Now, if :g:`$B$ <0338.g1:B>` is prime, what was enjoined will have been done.\ [#f1]_",
    ),
    (
        "book_vii/propositions/0338.rst",
        "   Thus, if the investigation be continued in this way, some prime number will be found which will measure the number before it, which will also measure :g:`$A$ <0338.g1:A>`.",
        r"   Thus, if the investigation be continued in this way, some prime number will be found which will measure\ [#f2]_ the number before it, which will also measure :g:`$A$ <0338.g1:A>`.",
    ),
    (
        "book_vii/propositions/0339.rst",
        "**8. if** :g:`$B$ <0338.g1:B>` **is prime, what was enjoined will have been done**, *i.e.* the implied *problem* of finding a prime number which measures :g:`$A$ <0338.g1:A>`.\n\n**18. some prime number will be found which will measure.**",
        "----\n\n.. [#f1] **if** :g:`$B$ <0338.g1:B>` **is prime, what was enjoined will have been done**, *i.e.* the implied *problem* of finding a prime number which measures :g:`$A$ <0338.g1:A>`.\n\n.. [#f2] **some prime number will be found which will measure.**",
    ),
    # 29. Book VII Prop. 33 (0340.rst & 0341.rst)
    (
        "book_vii/propositions/0340.rst",
        "   Therefore the numbers :g:`$E$ <0339.g2:E>`, :g:`$F$ <0339.g2:F>`, :g:`$G$ <0339.g2:G>` measure the numbers :g:`$A$ <0339.g2:A>`, :g:`$B$ <0339.g2:B>`, :g:`$C$ <0339.g2:C>` respectively according to the units in :g:`$D$ <0339.g2:D>`. :just:`[VII. 16] <VII.16>`",
        r"   Therefore the numbers :g:`$E$ <0339.g2:E>`, :g:`$F$ <0339.g2:F>`, :g:`$G$ <0339.g2:G>` measure the numbers :g:`$A$ <0339.g2:A>`, :g:`$B$ <0339.g2:B>`, :g:`$C$ <0339.g2:C>` respectively\ [#f1]_ according to the units in :g:`$D$ <0339.g2:D>`. :just:`[VII. 16] <VII.16>`",
    ),
    (
        "book_vii/propositions/0341.rst",
        "**17. the numbers** :g:`$E$ <0339.g2:E>`, :g:`$F$ <0339.g2:F>`, :g:`$G$ <0339.g2:G>` **measure the numbers**",
        ".. [#f1] **the numbers** :g:`$E$ <0339.g2:E>`, :g:`$F$ <0339.g2:F>`, :g:`$G$ <0339.g2:G>` **measure the numbers**",
    ),
    # 30. Book VIII Prop. 4 (0358.rst & 0359.rst)
    (
        "book_viii/propositions/0358.rst",
        "I say next that they are also the least that are in the ratios :g:`$A$ <0357.g1:A>` : :g:`$B$ <0357.g1:B>`, :g:`$C$ <0357.g1:C>` : :g:`$D$ <0357.g1:D>`, :g:`$E$ <0357.g1:E>` : :g:`$F$ <0357.g1:F>`.",
        r"I say next that they are also the least that are in the ratios :g:`$A$ <0357.g1:A>` : :g:`$B$ <0357.g1:B>`, :g:`$C$ <0357.g1:C>` : :g:`$D$ <0357.g1:D>`, :g:`$E$ <0357.g1:E>` : :g:`$F$ <0357.g1:F>`.\ [#f1]_",
    ),
    (
        "book_viii/propositions/0359.rst",
        "   therefore :g:`$N$ <0357.g1:N>`, :g:`$O$ <0357.g1:O>`, :g:`$M$ <0357.g1:M>`, :g:`$P$ <0357.g1:P>` are the least numbers continuously proportional in the ratios :g:`$A$ <0357.g1:A>` : :g:`$B$ <0357.g1:B>`, :g:`$C$ <0357.g1:C>` : :g:`$D$ <0357.g1:D>`, :g:`$E$ <0357.g1:E>` : :g:`$F$ <0357.g1:F>`.",
        r"   therefore :g:`$N$ <0357.g1:N>`, :g:`$O$ <0357.g1:O>`, :g:`$M$ <0357.g1:M>`, :g:`$P$ <0357.g1:P>` are the least numbers continuously proportional in the ratios :g:`$A$ <0357.g1:A>` : :g:`$B$ <0357.g1:B>`, :g:`$C$ <0357.g1:C>` : :g:`$D$ <0357.g1:D>`, :g:`$E$ <0357.g1:E>` : :g:`$F$ <0357.g1:F>`.\ [#f1]_",
    ),
    (
        "book_viii/propositions/0359.rst",
        "**69, 71, 99. the ratios** :g:`$A$ <0357.g1:A>` : :g:`$B$ <0357.g1:B>`, :g:`$C$ <0357.g1:C>` : :g:`$D$ <0357.g1:D>`, :g:`$E$ <0357.g1:E>` : :g:`$F$ <0357.g1:F>`.",
        ".. [#f1] **the ratios** :g:`$A$ <0357.g1:A>` : :g:`$B$ <0357.g1:B>`, :g:`$C$ <0357.g1:C>` : :g:`$D$ <0357.g1:D>`, :g:`$E$ <0357.g1:E>` : :g:`$F$ <0357.g1:F>`.",
    ),
    # 31. Book VIII Prop. 5 (0360.rst)
    (
        "book_viii/propositions/0360.rst",
        "   Plane numbers have to one another the ratio compounded of the ratios of their sides.",
        r"   Plane numbers have to one another the ratio compounded of the ratios of their sides.\ [#f1]_",
    ),
    (
        "book_viii/propositions/0360.rst",
        "**1, 5, 29, 31. compounded of the ratios of their sides.**",
        ".. [#f1] **compounded of the ratios of their sides.**",
    ),
    # 32. Book VIII Prop. 8 (0363.rst & 0364.rst)
    (
        "book_viii/propositions/0363.rst",
        "   If between two numbers there fall numbers in continued proportion with them,",
        r"   If between two numbers there fall\ [#f1]_ numbers in continued proportion with them,",
    ),
    (
        "book_viii/propositions/0364.rst",
        "**1. fall.** The Greek word is ἐμπίπτω, \"fall in\" = \"can be interpolated.\"",
        ".. [#f1] **fall.** The Greek word is ἐμπίπτω, \"fall in\" = \"can be interpolated.\"",
    ),
    # 33. Book VIII Prop. 20 (0382.rst)
    (
        "book_viii/propositions/0382.rst",
        r"   For, †\ [#f376_1]_since :g:`$F$ <0382.g1:F>`",
        r"   For, †\ [#f1]_since :g:`$F$ <0382.g1:F>`",
    ),
    (
        "book_viii/propositions/0382.rst",
        ".. [#f376_1] **25. For, †since** :g:`$F$ <0382.g1:F>`......**27**. :g:`$C$ <0382.g1:C>` **to** :g:`$B$ <0382.g1:B>`. The text has clearly suffered corruption here. It  is not necessary to infer from other facts that, as :g:`$D$ <0382.g1:D>` is to :g:`$E$ <0382.g1:E>`, so is :g:`$A$ <0382.g1:A>` to :g:`$C$ <0382.g1:C>`; for this is part of  the hypotheses (ll. 6, 7). Again, there is no explanation of the statement (l. 25) that :g:`$F$ <0382.g1:F>` by  multiplying :g:`$E$ <0382.g1:E>` has made :g:`$C$ <0382.g1:C>`. It is the statement and explanation of this latter fact which are  alone wanted; after which the proof proceeds in l. 28. We might therefore substitute for  ll. 25—28 the following.  “For, since :g:`$E$ <0382.g1:E>` measures :g:`$C$ <0382.g1:C>` the same number of times that :g:`$D$ <0382.g1:D>` measures :g:`$A$ <0382.g1:A>` [l. 8], that is,  according to the units in :g:`$F$ <0382.g1:F>` [l. 10], therefore :g:`$F$ <0382.g1:F>` by multiplying :g:`$E$ <0382.g1:E>` has made :g:`$C$ <0382.g1:C>`.  And, since :g:`$E$ <0382.g1:E>` by multiplying :g:`$F$ <0382.g1:F>`, :g:`$G$ <0382.g1:G>`,” etc. etc.\n\n----",
        ".. [#f1] **For, †since** :g:`$F$ <0382.g1:F>`......**27**. :g:`$C$ <0382.g1:C>` **to** :g:`$B$ <0382.g1:B>`. The text has clearly suffered corruption here. It is not necessary to infer from other facts that, as :g:`$D$ <0382.g1:D>` is to :g:`$E$ <0382.g1:E>`, so is :g:`$A$ <0382.g1:A>` to :g:`$C$ <0382.g1:C>`; for this is part of the hypotheses (ll. 6, 7). Again, there is no explanation of the statement (l. 25) that :g:`$F$ <0382.g1:F>` by multiplying :g:`$E$ <0382.g1:E>` has made :g:`$C$ <0382.g1:C>`. It is the statement and explanation of this latter fact which are alone wanted; after which the proof proceeds in l. 28. We might therefore substitute for ll. 25—28 the following. “For, since :g:`$E$ <0382.g1:E>` measures :g:`$C$ <0382.g1:C>` the same number of times that :g:`$D$ <0382.g1:D>` measures :g:`$A$ <0382.g1:A>` [l. 8], that is, according to the units in :g:`$F$ <0382.g1:F>` [l. 10], therefore :g:`$F$ <0382.g1:F>` by multiplying :g:`$E$ <0382.g1:E>` has made :g:`$C$ <0382.g1:C>`. And, since :g:`$E$ <0382.g1:E>` by multiplying :g:`$F$ <0382.g1:F>`, :g:`$G$ <0382.g1:G>`,” etc. etc.",
    ),
    # 34. Book IX Prop. 23 (0420.rst)
    (
        "book_ix/propositions/0420.rst",
        r"the multitude of which is odd,\ [#f414_1]_ be added together ;",
        r"the multitude of which is odd,\ [#f1]_ be added together ;",
    ),
    (
        "book_ix/propositions/0420.rst",
        ".. [#f414_1] 3. Literally “let there be as many numbers as we please, of which *let the multitude be odd*.” This form, natural in Greek, is awkward in English.",
        "----\n\n.. [#f1] Literally “let there be as many numbers as we please, of which *let the multitude be odd*.” This form, natural in Greek, is awkward in English.",
    ),
]


def main() -> None:
    applied = 0
    for rel_path, old_s, new_s in _REPLACEMENTS:
        f = _VOL2_DIR / rel_path
        text = f.read_text(encoding="utf-8")
        if old_s not in text:
            if new_s in text:
                continue
            raise RuntimeError(f"Could not find target substring in {rel_path}:\n{old_s!r}")
        text = text.replace(old_s, new_s, 1)
        f.write_text(text, encoding="utf-8")
        applied += 1
    print(f"Applied {applied} footnote replacements across Volume II.")


if __name__ == "__main__":
    main()
