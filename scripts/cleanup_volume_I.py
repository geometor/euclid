#!/usr/bin/env python3
"""Structural cleanup and footnote-wiring pass across Volume I (resources/heath/volume_I/).

Tasks:
1. Remove all :line:`N` marginal line number tags and clean up whitespace artifacts.
2. Wire all line-keyed proposition notes in Book I and Book II to proper RST footnotes ([#fN]_ and .. [#fN]).
3. Reflow forced `| ` line-blocks in propositions and commentary, and fix mid-sentence `.. subclause::` splits.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

_REPO_ROOT = Path(__file__).resolve().parents[1]
_LOCAL_SRC = _REPO_ROOT / "src"
_PROJECTS_ROOT = _REPO_ROOT.parents[1]
_PUBLISH_SRC = _PROJECTS_ROOT / "photon-platform" / "publish" / "src"

for _p in (_PUBLISH_SRC, _LOCAL_SRC):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

for _ws_venv in (
    _REPO_ROOT / ".venv",
    _PROJECTS_ROOT / "photon-platform" / "publish" / ".venv",
    _PROJECTS_ROOT / "geometor" / "elements" / ".venv",
    _PROJECTS_ROOT / "geometor" / "hoenen" / ".venv",
    _PROJECTS_ROOT / "geometor" / "pacioli" / ".venv",
    _PROJECTS_ROOT / "geometor" / "model" / ".venv",
):
    for _sp in sorted(_ws_venv.glob("lib/python*/site-packages")):
        if _sp.exists() and str(_sp) not in sys.path:
            sys.path.append(str(_sp))

from photon_platform.publish.rst_renderer import render_rst_html


# ---------------------------------------------------------------------------
# Files where `| ` line-blocks are intentional (title pages, verse, tables)
# ---------------------------------------------------------------------------
_KEEP_PIPE_FILES = {
    "euclids_elements/0005.rst",
    "euclids_elements/0006.rst",
    "excursus_ii/0429.rst",
    "excursus_ii/0430.rst",
    "excursus_ii/0432.rst",
    "introduction/chapter_iv/0058.rst",
    "introduction/chapter_viii/0109.rst",
    "introduction/chapter_viii/0114.rst",
    "introduction/chapter_viii/0123.rst",
    "introduction/chapter_viii/0127.rst",
    "book_i/common_notions/0169.rst",
    "book_i/common_notions/0172.rst",
    "book_i/common_notions/0179.rst",
    "book_i/common_notions/0183.rst",
    "book_i/common_notions/0185.rst",
    "book_i/common_notions/0189.rst",
    "book_i/common_notions/0203.rst",
}


# ---------------------------------------------------------------------------
# Task 2: Exact Footnote Reference Insertions & Note Definition Conversions
# ---------------------------------------------------------------------------
# List of (rel_path, old_substring, new_substring)
_FOOTNOTE_PATCHES: List[Tuple[str, str, str]] = [
    # Prop I.2 (0258, 0259)
    (
        "book_i/propositions/0258.rst",
        "To place at a given point (as an extremity) a straight line equal to a given straight line.",
        r"To place at a given point (as an extremity)\ [#f1]_ a straight line equal to a given straight line.",
    ),
    (
        "book_i/propositions/0258.rst",
        "Let the straight lines :g:`$AE$ <0258.g1:/ A E />`, :g:`$BF$ <0258.g1:/ B F />` be produced in a straight line",
        r"Let the straight lines :g:`$AE$ <0258.g1:/ A E />`, :g:`$BF$ <0258.g1:/ B F />` be produced\ [#f2]_ in a straight line",
    ),
    (
        "book_i/propositions/0258.rst",
        "therefore the remainder :g:`$AL$ <0258.g1:/ A L />` is equal to the remainder :g:`$BG$ <0258.g1:/ B G />`. :just:`[C.N. 3] <I.cn.3>`",
        r"therefore the remainder :g:`$AL$ <0258.g1:/ A L />` is equal to the remainder :g:`$BG$ <0258.g1:/ B G />`.\ [#f3]_ :just:`[C.N. 3] <I.cn.3>`",
    ),
    (
        "book_i/propositions/0258.rst",
        "**1. (as an extremity).**",
        ".. [#f1] **(as an extremity).**",
    ),
    (
        "book_i/propositions/0258.rst",
        "**11. Let the straight lines AE, BF be produced....**",
        ".. [#f2] **Let the straight lines AE, BF be produced....**",
    ),
    (
        "book_i/propositions/0259.rst",
        "**23. the remainder AL...the remainder BG.**",
        ".. [#f3] **the remainder AL...the remainder BG.**",
    ),
    # Prop I.4 (0261, 0262, 0263)
    (
        "book_i/propositions/0261.rst",
        "If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base, the triangle will be equal to the triangle, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend.",
        r"If two triangles have the two sides equal to two sides respectively,\ [#f2]_ and have the angles contained by the equal straight lines equal,\ [#f1]_ they will also have the base\ [#f3]_ equal to the base, the triangle will be equal to the triangle, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend.\ [#f4]_",
    ),
    (
        "book_i/propositions/0261.rst",
        "and the angle :g:`$BAC$ <0261.g1:< B A C )>` equal to the angle :g:`$EDF$ <0261.g1:< E D F )>`.",
        r"and the angle :g:`$BAC$ <0261.g1:< B A C )>`\ [#f5]_ equal to the angle :g:`$EDF$ <0261.g1:< E D F )>`.",
    ),
    (
        "book_i/propositions/0261.rst",
        "For, if the triangle :g:`$ABC$ <0261.g1:< A B C >>` be applied to the triangle :g:`$DEF$ <0261.g1:< D E F >>`,",
        r"For, if the triangle :g:`$ABC$ <0261.g1:< A B C >>` be applied\ [#f6]_ to the triangle :g:`$DEF$ <0261.g1:< D E F >>`,",
    ),
    (
        "book_i/propositions/0262.rst",
        ":g:`$EF$ <0261.g1:/ E F />`] and will be equal to it.",
        r":g:`$EF$ <0261.g1:/ E F />`]\ [#f7]_ and will be equal to it.",
    ),
    (
        "book_i/propositions/0262.rst",
        "Therefore etc.",
        r"Therefore etc.\ [#f8]_",
    ),
    (
        "book_i/propositions/0262.rst",
        "**1—3.** It is a fact",
        ".. [#f1] It is a fact",
    ),
    (
        "book_i/propositions/0262.rst",
        "**2. respectively.**",
        ".. [#f2] **respectively.**",
    ),
    (
        "book_i/propositions/0262.rst",
        "**3. the base.**",
        ".. [#f3] **the base.**",
    ),
    (
        "book_i/propositions/0263.rst",
        "**6. subtend.**",
        ".. [#f4] **subtend.**",
    ),
    (
        "book_i/propositions/0263.rst",
        "**9. the angle BAC.**",
        ".. [#f5] **the angle BAC.**",
    ),
    (
        "book_i/propositions/0263.rst",
        "**17. if the triangle be applied to..., 23. coincide.**",
        ".. [#f6] **if the triangle be applied to..., coincide.**",
    ),
    (
        "book_i/propositions/0263.rst",
        "**32. [For if, when B coincides... 36. coincide with EF].**",
        ".. [#f7] **[For if, when B coincides... coincide with EF].**",
    ),
    (
        "book_i/propositions/0263.rst",
        "**44. Therefore etc.**",
        ".. [#f8] **Therefore etc.**",
    ),
    # Prop I.5 (0265, 0266)
    (
        "book_i/propositions/0265.rst",
        "if the equal straight lines be produced further,",
        r"if the equal straight lines\ [#f1]_ be produced further,",
    ),
    (
        "book_i/propositions/0265.rst",
        "Let a point :g:`$F$ <0265.g1:F>` be taken at random on :g:`$BD$ <0265.g1:/ B D />`;",
        r"Let a point :g:`$F$ <0265.g1:F>` be taken at random on :g:`$BD$ <0265.g1:/ B D />`;\ [#f2]_",
    ),
    (
        "book_i/propositions/0265.rst",
        "the two sides :g:`$FA$ <0265.g1:/ F A />`, :g:`$AC$ <0265.g1:/ A C />` are equal to the two sides :g:`$GA$ <0265.g1:/ G A />`, :g:`$AB$ <0265.g1:/ A B />`, respectively;",
        r"the two sides :g:`$FA$ <0265.g1:/ F A />`, :g:`$AC$ <0265.g1:/ A C />` are equal to the two sides :g:`$GA$ <0265.g1:/ G A />`, :g:`$AB$ <0265.g1:/ A B />`, respectively;\ [#f3]_",
    ),
    (
        "book_i/propositions/0265.rst",
        "while the base :g:`$BC$ <0265.g1:/ B C />` is common to them;",
        r"while the base :g:`$BC$ <0265.g1:/ B C />` is common to them;\ [#f4]_",
    ),
    (
        "book_i/propositions/0266.rst",
        "Therefore etc. :just:`Q. E. D.`",
        r"Therefore etc.\ [#f5]_ :just:`Q. E. D.`",
    ),
    (
        "book_i/propositions/0266.rst",
        "**2. the equal straight lines**",
        ".. [#f1] **the equal straight lines**",
    ),
    (
        "book_i/propositions/0266.rst",
        "**10. Let a point F be taken at random on BD,**",
        ".. [#f2] **Let a point F be taken at random on BD,**",
    ),
    (
        "book_i/propositions/0266.rst",
        "**17. the two sides FA, AC are equal to the two sides GA, AB respectively,**",
        ".. [#f3] **the two sides FA, AC are equal to the two sides GA, AB respectively,**",
    ),
    (
        "book_i/propositions/0266.rst",
        "**33. the base BC is common to them,**",
        ".. [#f4] **the base BC is common to them,**",
    ),
    (
        "book_i/propositions/0266.rst",
        "**48.** As “(Being) what it was required to prove”",
        ".. [#f5] As “(Being) what it was required to prove”",
    ),
    # Prop I.7 (0272, 0273, 0274)
    (
        "book_i/propositions/0272.rst",
        "namely each to that which has the same extremity with it.",
        r"namely each to that which has the same extremity with it.\ [#f1]_",
    ),
    (
        "book_i/propositions/0273.rst",
        "therefore the angle :g:`$ADC$ <0272.g2:< A D C )>` is greater than the angle :g:`$DCB$ <0272.g2:< D C B )>`;",
        r"therefore the angle :g:`$ADC$ <0272.g2:< A D C )>` is greater than the angle :g:`$DCB$ <0272.g2:< D C B )>`;\ [#f2]_",
    ),
    (
        "book_i/propositions/0273.rst",
        "therefore the angle :g:`$CDB$ <0272.g2:< C D B )>` is much greater than the angle :g:`$DCB$ <0272.g2:< D C B )>`.",
        r"therefore the angle :g:`$CDB$ <0272.g2:< C D B )>` is much greater\ [#f3]_ than the angle :g:`$DCB$ <0272.g2:< D C B )>`.",
    ),
    (
        "book_i/propositions/0273.rst",
        "**1—6.** In an English translation",
        ".. [#f1] In an English translation",
    ),
    (
        "book_i/propositions/0274.rst",
        "**20.** It would be natural",
        ".. [#f2] It would be natural",
    ),
    (
        "book_i/propositions/0274.rst",
        "**21. much greater,**",
        ".. [#f3] **much greater,**",
    ),
    # Prop I.8 (0276)
    (
        "book_i/propositions/0276.rst",
        ":g:`$BA$ <0275.g1:/ B A />`, :g:`$AC$ <0275.g1:/ A C />` will also coincide with :g:`$ED$ <0275.g1:/ E D />`, :g:`$DF$ <0275.g1:/ D F />`;",
        r":g:`$BA$ <0275.g1:/ B A />`, :g:`$AC$ <0275.g1:/ A C />`\ [#f1]_ will also coincide with :g:`$ED$ <0275.g1:/ E D />`, :g:`$DF$ <0275.g1:/ D F />`;",
    ),
    (
        "book_i/propositions/0276.rst",
        "but fall beside them as :g:`$EG$ <0275.g1:/ E G />`, :g:`$GF$ <0275.g1:/ G F />`,",
        r"but fall beside them\ [#f2]_ as :g:`$EG$ <0275.g1:/ E G />`, :g:`$GF$ <0275.g1:/ G F />`,",
    ),
    (
        "book_i/propositions/0276.rst",
        "**19. BA, AC.**",
        ".. [#f1] **BA, AC.**",
    ),
    (
        "book_i/propositions/0276.rst",
        "**21. fall beside them.**",
        ".. [#f2] **fall beside them.**",
    ),
    # Prop I.11 (0283)
    (
        "book_i/propositions/0283.rst",
        "let :g:`$CE$ <0283.g1:/ C E />` be made equal to :g:`$CD$ <0283.g1:/ C D />`; :just:`[I. 3] <I.3>`",
        r"let :g:`$CE$ <0283.g1:/ C E />` be made equal to :g:`$CD$ <0283.g1:/ C D />`;\ [#f1]_ :just:`[I. 3] <I.3>`",
    ),
    (
        "book_i/propositions/0283.rst",
        "**10. let** :g:`$CE$ <0283.g1:/ C E />` **be made equal to** :g:`$CD$ <0283.g1:/ C D />`.",
        ".. [#f1] **let** :g:`$CE$ <0283.g1:/ C E />` **be made equal to** :g:`$CD$ <0283.g1:/ C D />`.",
    ),
    # Prop I.12 (0284, 0285)
    (
        "book_i/propositions/0284.rst",
        "To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.",
        r"To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.\ [#f1]_",
    ),
    (
        "book_i/propositions/0285.rst",
        "at random on the other side of the straight line :g:`$AB$ <0285.g1:[ A B ]>`, and with centre",
        r"at random on the other side of the straight line :g:`$AB$ <0285.g1:[ A B ]>`,\ [#f2]_ and with centre",
    ),
    (
        "book_i/propositions/0285.rst",
        "**2. a perpendicular straight line**,",
        ".. [#f1] **a perpendicular straight line**,",
    ),
    (
        "book_i/propositions/0285.rst",
        "**10. on the other side of the straight line** :g:`$AB$ <0285.g1:[ A B ]>`,",
        ".. [#f2] **on the other side of the straight line** :g:`$AB$ <0285.g1:[ A B ]>`,",
    ),
    # Prop I.13 (0289, 0290)
    (
        "book_i/propositions/0289.rst",
        "let the angle :g:`$EBD$ <0289.g1:< E B D )>` be added to each;",
        r"let the angle :g:`$EBD$ <0289.g1:< E B D )>` be added to each;\ [#f1]_",
    ),
    (
        "book_i/propositions/0290.rst",
        "**17. let the angle** :g:`$EBD$ <0289.g1:< E B D )>` **be added to each**,",
        ".. [#f1] **let the angle** :g:`$EBD$ <0289.g1:< E B D )>` **be added to each**,",
    ),
    # Prop I.14 (0290, 0291)
    (
        "book_i/propositions/0290.rst",
        "If with any straight line, and at a point on it,",
        r"If with any straight line,\ [#f1]_ and at a point on it,",
    ),
    (
        "book_i/propositions/0290.rst",
        "therefore the angles :g:`$CBA$ <0290.g1:< C B A )>`, :g:`$ABE$ <0290.g1:< A B E )>` are equal to the angles :g:`$CBA$ <0290.g1:< C B A )>`, :g:`$ABD$ <0290.g1:< A B D )>`.",
        r"therefore the angles :g:`$CBA$ <0290.g1:< C B A )>`, :g:`$ABE$ <0290.g1:< A B E )>` are equal to the angles :g:`$CBA$ <0290.g1:< C B A )>`, :g:`$ABD$ <0290.g1:< A B D )>`.\ [#f2]_",
    ),
    (
        "book_i/propositions/0290.rst",
        "Similarly we can prove that neither is any other straight",
        r"Similarly we can prove\ [#f3]_ that neither is any other straight",
    ),
    (
        "book_i/propositions/0291.rst",
        "**1. If with any straight line....**",
        ".. [#f1] **If with any straight line....**",
    ),
    (
        "book_i/propositions/0291.rst",
        "**17.** :person:`Todhunter <todhunter>` points out",
        ".. [#f2] :person:`Todhunter <todhunter>` points out",
    ),
    (
        "book_i/propositions/0291.rst",
        "**24. we can prove.**",
        ".. [#f3] **we can prove.**",
    ),
    # Prop I.15 (0291, 0292)
    (
        "book_i/propositions/0291.rst",
        "If two straight lines cut one another, they make the vertical angles equal to one another.",
        r"If two straight lines cut one another, they make the vertical angles\ [#f1]_ equal to one another.",
    ),
    (
        "book_i/propositions/0292.rst",
        "they will make the angles at the point of section equal to four right angles.]",
        r"they will make the angles at the point of section\ [#f2]_ equal to four right angles.]",
    ),
    (
        "book_i/propositions/0292.rst",
        "**1. the vertical angles.**",
        ".. [#f1] **the vertical angles.**",
    ),
    (
        "book_i/propositions/0292.rst",
        "**26. at the point of section,**",
        ".. [#f2] **at the point of section,**",
    ),
    # Prop I.16 (0293, 0294)
    (
        "book_i/propositions/0293.rst",
        "In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.",
        r"In any triangle, if one of the sides be produced, the exterior angle\ [#f1]_ is greater than either of the interior and opposite angles.\ [#f2]_",
    ),
    (
        "book_i/propositions/0293.rst",
        "and let :g:`$AC$ <0293.g1:/ A C />` be drawn through to :g:`$G$ <0293.g1:G>`. :just:`[Post. 2] <I.post.2>`",
        r"and let :g:`$AC$ <0293.g1:/ A C />` be drawn through to :g:`$G$ <0293.g1:G>`.\ [#f3]_ :just:`[Post. 2] <I.post.2>`",
    ),
    (
        "book_i/propositions/0293.rst",
        "and the triangle :g:`$ABE$ <0293.g1:< A B E >>` is equal to the triangle :g:`$CFE$ <0293.g1:< C F E >>`,",
        r"and the triangle :g:`$ABE$ <0293.g1:< A B E >>` is equal to the triangle :g:`$CFE$ <0293.g1:< C F E >>`,\ [#f4]_",
    ),
    (
        "book_i/propositions/0294.rst",
        "**1. the exterior angle,**",
        ".. [#f1] **the exterior angle,**",
    ),
    (
        "book_i/propositions/0294.rst",
        "**2. the interior and opposite angles,**",
        ".. [#f2] **the interior and opposite angles,**",
    ),
    (
        "book_i/propositions/0294.rst",
        "**12. let** :g:`$AC$ <0293.g1:/ A C />` **be drawn through to** :g:`$G$ <0293.g1:G>`.",
        ".. [#f3] **let** :g:`$AC$ <0293.g1:/ A C />` **be drawn through to** :g:`$G$ <0293.g1:G>`.",
    ),
    (
        "book_i/propositions/0294.rst",
        "**21**. :g:`$CFE$ <0293.g1:< C F E >>`,",
        ".. [#f4] :g:`$CFE$ <0293.g1:< C F E >>`,",
    ),
    # Prop I.17 (0295, 0296)
    (
        "book_i/propositions/0295.rst",
        "In any triangle two angles taken together in any manner are less than two right angles.",
        r"In any triangle two angles taken together in any manner\ [#f1]_ are less than two right angles.",
    ),
    (
        "book_i/propositions/0296.rst",
        "**1. taken together in any manner,**",
        ".. [#f1] **taken together in any manner,**",
    ),
    # Prop I.21 (0303)
    (
        "book_i/propositions/0303.rst",
        "If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle,",
        r"If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle,\ [#f1]_ the straight lines so constructed\ [#f2]_ will be less than the remaining two sides of the triangle,",
    ),
    (
        "book_i/propositions/0303.rst",
        "**2. be constructed...meeting within the triangle.**",
        ".. [#f1] **be constructed...meeting within the triangle.**",
    ),
    (
        "book_i/propositions/0303.rst",
        "**3. the straight lines so constructed.**",
        ".. [#f2] **the straight lines so constructed.**",
    ),
    # Prop I.22 (0306, 0307)
    (
        "book_i/propositions/0306.rst",
        "Out of three straight lines, which are equal to three given straight lines, to construct a triangle : thus it is necessary that two of the straight lines taken together in any manner should be greater than the remaining one. :just:`[I. 20] <I.20>`",
        r"Out of three straight lines, which are equal to three given straight lines, to construct a triangle:\ [#f1]_ thus it is necessary\ [#f2]_ that two of the straight lines taken together in any manner should be greater than the remaining one.\ [#f3]_ :just:`[I. 20] <I.20>`",
    ),
    (
        "book_i/propositions/0307.rst",
        "**2–4.** This is the first case",
        ".. [#f1] This is the first case",
    ),
    (
        "book_i/propositions/0307.rst",
        "**2. thus it is necessary.**",
        ".. [#f2] **thus it is necessary.**",
    ),
    (
        "book_i/propositions/0307.rst",
        "**4.** To this enunciation",
        ".. [#f3] To this enunciation",
    ),
    # Prop I.24 (0310, 0311)
    (
        "book_i/propositions/0310.rst",
        "For, since the angle :g:`$BAC$ <0310.g2:< B A C )>` is greater than the angle :g:`$EDF$ <0310.g2:< E D F )>`,",
        r"For, since the angle :g:`$BAC$ <0310.g2:< B A C )>` is greater than the angle :g:`$EDF$ <0310.g2:< E D F )>`,\ [#f1]_",
    ),
    (
        "book_i/propositions/0311.rst",
        "**10.** I have naturally left out",
        ".. [#f1] I have naturally left out",
    ),
    # Prop I.26 (0315, 0316, 0317)
    (
        "book_i/propositions/0315.rst",
        "either the side adjoining the equal angles,",
        r"either the side adjoining the equal angles,\ [#f1]_",
    ),
    (
        "book_i/propositions/0316.rst",
        "But the angle :g:`$DFE$ <0316.g1:< D F E )>` is by hypothesis equal to the angle :g:`$BCA$ <0316.g1:< B C A )>`;",
        r"But the angle :g:`$DFE$ <0316.g1:< D F E )>` is by hypothesis equal\ [#f2]_ to the angle :g:`$BCA$ <0316.g1:< B C A )>`;",
    ),
    (
        "book_i/propositions/0317.rst",
        "**2—3. the side adjoining the equal angles,**",
        ".. [#f1] **the side adjoining the equal angles,**",
    ),
    (
        "book_i/propositions/0317.rst",
        "**29. is by hypothesis equal.**",
        ".. [#f2] **is by hypothesis equal.**",
    ),
    # Prop I.27 (0321, 0322)
    (
        "book_i/propositions/0321.rst",
        "If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.",
        r"If a straight line falling on two straight lines\ [#f1]_ make the alternate angles\ [#f2]_ equal to one another, the straight lines will be parallel to one another.",
    ),
    (
        "book_i/propositions/0321.rst",
        "of :g:`$B$ <0321.g1:B>`, :g:`$D$ <0321.g1:D>` or towards :g:`$A$ <0321.g1:A>`, :g:`$C$ <0321.g1:C>`.",
        r"of :g:`$B$ <0321.g1:B>`, :g:`$D$ <0321.g1:D>` or towards :g:`$A$ <0321.g1:A>`, :g:`$C$ <0321.g1:C>`.\ [#f3]_",
    ),
    (
        "book_i/propositions/0322.rst",
        "**1. falling on two straight lines,**",
        ".. [#f1] **falling on two straight lines,**",
    ),
    (
        "book_i/propositions/0322.rst",
        "**2. the alternate angles,**",
        ".. [#f2] **the alternate angles,**",
    ),
    (
        "book_i/propositions/0322.rst",
        "**9. in the direction of B, D or towards A, C,**",
        ".. [#f3] **in the direction of B, D or towards A, C,**",
    ),
    # Prop I.29 (0326)
    (
        "book_i/propositions/0326.rst",
        "But straight lines produced indefinitely from angles less than two right angles meet; :just:`[Post. 5] <I.post.5>`",
        r"But straight lines produced indefinitely from angles less than two right angles\ [#f1]_ meet; :just:`[Post. 5] <I.post.5>`",
    ),
    (
        "book_i/propositions/0326.rst",
        "but they do not meet, because they are by hypothesis parallel.",
        r"but they do not meet, because they are by hypothesis parallel.\ [#f2]_",
    ),
    (
        "book_i/propositions/0326.rst",
        "**23. straight lines produced indefinitely from angles less than two right angles,**",
        ".. [#f1] **straight lines produced indefinitely from angles less than two right angles,**",
    ),
    (
        "book_i/propositions/0326.rst",
        "**26. because they are by hypothesis parallel,**",
        ".. [#f2] **because they are by hypothesis parallel,**",
    ),
    # Prop I.30 (0328)
    (
        "book_i/propositions/0328.rst",
        "Therefore :g:`$AB$ <0328.g1:/ A B />` is parallel to :g:`$CD$ <0328.g1:/ C D />`.",
        r"Therefore :g:`$AB$ <0328.g1:/ A B />` is parallel to :g:`$CD$ <0328.g1:/ C D />`.\ [#f1]_",
    ),
    (
        "book_i/propositions/0328.rst",
        "**20.** The usual conclusion",
        ".. [#f1] The usual conclusion",
    ),
    # Prop I.33 (0336, 0337)
    (
        "book_i/propositions/0336.rst",
        "The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.",
        r"The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively)\ [#f1]_ are themselves also equal and parallel.",
    ),
    (
        "book_i/propositions/0337.rst",
        "the two sides :g:`$AB$ <0337.g1:/ A B />`, :g:`$BC$ <0337.g1:/ B C />` are equal to the two sides :g:`$DC$ <0337.g1:/ D C />`, :g:`$CB$ <0337.g1:/ C B />`;",
        r"the two sides :g:`$AB$ <0337.g1:/ A B />`, :g:`$BC$ <0337.g1:/ B C />` are equal to the two sides :g:`$DC$ <0337.g1:/ D C />`, :g:`$CB$ <0337.g1:/ C B />`;\ [#f2]_",
    ),
    (
        "book_i/propositions/0337.rst",
        "**1. joining...(at the extremities which are) in the same directions (respectively).**",
        ".. [#f1] **joining...(at the extremities which are) in the same directions (respectively).**",
    ),
    (
        "book_i/propositions/0337.rst",
        "**15. DC, CB and 18. DCB.**",
        ".. [#f2] **DC, CB and DCB.**",
    ),
    # Prop I.34 (0337, 0338, 0339)
    (
        "book_i/propositions/0337.rst",
        "In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.",
        r"In parallelogrammic areas\ [#f1]_ the opposite sides and angles are equal to one another, and the diameter bisects the areas.",
    ),
    (
        "book_i/propositions/0338.rst",
        "Therefore :g:`$ABC$ <0338.g1:< A B C >>`, :g:`$DCB$ <0338.g1:< D C B >>` are two triangles",
        r"Therefore :g:`$ABC$ <0338.g1:< A B C >>`, :g:`$DCB$ <0338.g1:< D C B >>`\ [#f2]_ are two triangles",
    ),
    (
        "book_i/propositions/0339.rst",
        "**1.** It is to be observed",
        ".. [#f1] It is to be observed",
    ),
    (
        "book_i/propositions/0339.rst",
        "**17, 18, 40. DCB and 36. DC, CB.**",
        ".. [#f2] **DCB and DC, CB.**",
    ),
    # Prop I.35 (0341)
    (
        "book_i/propositions/0341.rst",
        "and the triangle :g:`$EAB$ <0341.g1:< E A B >>` will be equal to the triangle :g:`$FDC$ <0341.g1:< F D C >>`.",
        r"and the triangle :g:`$EAB$ <0341.g1:< E A B >>` will be equal to the triangle :g:`$FDC$ <0341.g1:< F D C >>`.\ [#f1]_",
    ),
    (
        "book_i/propositions/0341.rst",
        "Let :g:`$DGE$ <0341.g1:< D G E >>` be subtracted from each;",
        r"Let :g:`$DGE$ <0341.g1:< D G E >>` be subtracted\ [#f2]_ from each;",
    ),
    (
        "book_i/propositions/0341.rst",
        "**21. FDC.**",
        ".. [#f1] **FDC.**",
    ),
    (
        "book_i/propositions/0341.rst",
        "**22. Let DGE be subtracted.**",
        ".. [#f2] **Let DGE be subtracted.**",
    ),
    # Prop I.37 (0346)
    (
        "book_i/propositions/0346.rst",
        "[But the halves of equal things are equal to one another.]",
        r"[But the halves of equal things are equal to one another.]\ [#f1]_",
    ),
    (
        "book_i/propositions/0346.rst",
        "**21.** Here and in the next proposition",
        ".. [#f1] Here and in the next proposition",
    ),
    # Prop I.39 (0350, 0351)
    (
        "book_i/propositions/0350.rst",
        "[I say that they are also in the same parallels.]",
        r"[I say that they are also in the same parallels.]\ [#f1]_",
    ),
    (
        "book_i/propositions/0351.rst",
        "**5. [I say that they are also in the same parallels.]**",
        ".. [#f1] **[I say that they are also in the same parallels.]**",
    ),
    # Prop I.43 (0354, 0355)
    (
        "book_i/propositions/0354.rst",
        "In any parallelogram the complements of the parallelograms about the diameter are equal to one another.",
        r"In any parallelogram the complements\ [#f1]_ of the parallelograms about the diameter are equal to one another.",
    ),
    (
        "book_i/propositions/0354.rst",
        "and about :g:`$AC$ <0354.g1:/ A C />` let :g:`$EH$ <0354.g1:< A E K H >>`, :g:`$FG$ <0354.g1:< K F C G >>` be parallelograms,",
        r"and about :g:`$AC$ <0354.g1:/ A C />`\ [#f2]_ let :g:`$EH$ <0354.g1:< A E K H >>`, :g:`$FG$ <0354.g1:< K F C G >>` be parallelograms,",
    ),
    (
        "book_i/propositions/0355.rst",
        "**1. complements**,",
        ".. [#f1] **complements**,",
    ),
    (
        "book_i/propositions/0355.rst",
        "**4. and about** :g:`$AC$ <0354.g1:/ A C />`....",
        ".. [#f2] **and about** :g:`$AC$ <0354.g1:/ A C />`....",
    ),
    # Prop I.44 (0356)
    (
        "book_i/propositions/0356.rst",
        "Then, since the straight line :g:`$HF$ <0356.g1:/ H F />` falls upon the parallels",
        r"Then, since the straight line :g:`$HF$ <0356.g1:/ H F />` falls\ [#f1]_ upon the parallels",
    ),
    (
        "book_i/propositions/0356.rst",
        "**14. since the straight line** :g:`$HF$ <0356.g1:/ H F />` **falls**....",
        ".. [#f1] **since the straight line** :g:`$HF$ <0356.g1:/ H F />` **falls**....",
    ),
    # Prop I.45 (0359, 0360)
    (
        "book_i/propositions/0359.rst",
        "To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.",
        r"To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.\ [#f1]_",
    ),
    (
        "book_i/propositions/0360.rst",
        "**2, 3, 6, 45, 48. rectilineal figure**,",
        ".. [#f1] **rectilineal figure**,",
    ),
    # Prop I.46 (0361, 0362)
    (
        "book_i/propositions/0361.rst",
        "On a given straight line to describe a square.",
        r"On a given straight line to describe\ [#f1]_ a square.",
    ),
    (
        "book_i/propositions/0362.rst",
        "**1, 3, 30.** :person:`Proclus <proclus>`",
        ".. [#f1] :person:`Proclus <proclus>`",
    ),
    # Prop I.47 (0363, 0364)
    (
        "book_i/propositions/0363.rst",
        "In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.",
        r"In right-angled triangles the square on\ [#f1]_ the side subtending the right angle\ [#f2]_ is equal to the squares on the sides containing the right angle.",
    ),
    (
        "book_i/propositions/0364.rst",
        "the two sides :g:`$AB$ <0363.g1:/ A B />`, :g:`$BD$ <0363.g1:/ B D />` are equal to the two sides :g:`$FB$ <0363.g1:/ F B />`, :g:`$BC$ <0363.g1:/ B C />`",
        r"the two sides :g:`$AB$ <0363.g1:/ A B />`, :g:`$BD$ <0363.g1:/ B D />`\ [#f3]_ are equal to the two sides :g:`$FB$ <0363.g1:/ F B />`, :g:`$BC$ <0363.g1:/ B C />`",
    ),
    (
        "book_i/propositions/0364.rst",
        "[But the doubles of equals are equal to one another.]",
        r"[But the doubles of equals are equal to one another.]\ [#f4]_",
    ),
    (
        "book_i/propositions/0364.rst",
        "**1. the square on**,",
        ".. [#f1] **the square on**,",
    ),
    (
        "book_i/propositions/0364.rst",
        "**subtending the right angle.**",
        ".. [#f2] **subtending the right angle.**",
    ),
    (
        "book_i/propositions/0364.rst",
        "**33. the two sides AB, BD....**",
        ".. [#f3] **the two sides AB, BD....**",
    ),
    (
        "book_i/propositions/0364.rst",
        "**44. [But the doubles of equals are equal to one another.]**",
        ".. [#f4] **[But the doubles of equals are equal to one another.]**",
    ),
    # Prop II.1 (0389, 0390)
    (
        "book_i" if False else "book_ii/propositions/0389.rst",
        "Now :g:`$BH$ <0389.g1:< B H >>` is the rectangle :g:`$A$ <0389.g1:A>`, :g:`$BC$ <0389.g1:/ B C />`, for it is contained",
        r"Now :g:`$BH$ <0389.g1:< B H >>` is the rectangle :g:`$A$ <0389.g1:A>`, :g:`$BC$ <0389.g1:/ B C />`,\ [#f1]_ for it is contained",
    ),
    (
        "book_ii/propositions/0390.rst",
        "**20. the rectangle** :g:`$A$ <0389.g1:A>`, :g:`$BC$ <0389.g1:/ B C />`.",
        ".. [#f1] **the rectangle** :g:`$A$ <0389.g1:A>`, :g:`$BC$ <0389.g1:/ B C />`.",
    ),
    # Prop II.4 (0393, 0394)
    (
        "book_ii/propositions/0393.rst",
        "If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.",
        r"If a straight line be cut at random, the square on the whole is equal to the squares on the segments and twice the rectangle contained by the segments.\ [#f1]_",
    ),
    (
        "book_ii/propositions/0394.rst",
        "and it is described on :g:`$CB$ <0393.g1:/ B C />`.",
        r"and it is described\ [#f2]_ on :g:`$CB$ <0393.g1:/ B C />`.",
    ),
    (
        "book_ii/propositions/0394.rst",
        "therefore the four areas :g:`$HF$ <0393.g1:< H F >>`, :g:`$CK$ <0393.g1:< C K >>`, :g:`$AG$ <0393.g1:< A G >>`, :g:`$GE$ <0393.g1:< G E >>` are equal",
        r"therefore the four areas\ [#f3]_ :g:`$HF$ <0393.g1:< H F >>`, :g:`$CK$ <0393.g1:< C K >>`, :g:`$AG$ <0393.g1:< A G >>`, :g:`$GE$ <0393.g1:< G E >>` are equal",
    ),
    (
        "book_ii/propositions/0394.rst",
        "**2. twice the rectangle contained by the segments.**",
        ".. [#f1] **twice the rectangle contained by the segments.**",
    ),
    (
        "book_ii/propositions/0394.rst",
        "**35, 38. described. 39, 45. the squares**",
        ".. [#f2] **described; the squares**",
    ),
    (
        "book_ii/propositions/0394.rst",
        "**46. areas.**",
        ".. [#f3] **areas.**",
    ),
    # Prop II.5 (0396, 0397)
    (
        "book_ii/propositions/0396.rst",
        "together with the square on the straight line between the points of section is equal to the square on the half.",
        r"together with the square on the straight line between the points of section\ [#f1]_ is equal to the square on the half.",
    ),
    (
        "book_ii/propositions/0397.rst",
        "**3. between the points of section,**",
        ".. [#f1] **between the points of section,**",
    ),
    # Prop II.14 (0423, 0424)
    (
        "book_ii/propositions/0423.rst",
        "Then, if :g:`$BE$ <0423.g1:/ B E />` is equal to :g:`$ED$ <0423.g1:/ E D />`, that which was enjoined will have been done;",
        r"Then, if :g:`$BE$ <0423.g1:/ B E />` is equal to :g:`$ED$ <0423.g1:/ E D />`, that which was enjoined will have been done;\ [#f1]_",
    ),
    (
        "book_ii/propositions/0424.rst",
        "Therefore the rectilineal figure :g:`$A$ <0423.g1:A>` is also equal to the square :line:`35` which can be described on :g:`$EH$ <0423.g1:/ E H />`.",
        r"Therefore the rectilineal figure :g:`$A$ <0423.g1:A>` is also equal to the square which can be described\ [#f2]_ on :g:`$EH$ <0423.g1:/ E H />`.",
    ),
    (
        "book_ii/propositions/0424.rst",
        "**7. that which was enjoined will have been done,**",
        ".. [#f1] **that which was enjoined will have been done,**",
    ),
    (
        "book_ii/propositions/0424.rst",
        "**35, 36. which can be described,**",
        ".. [#f2] **which can be described,**",
    ),
]


# ---------------------------------------------------------------------------
# Mid-sentence `.. subclause::` / `.. assertion::` structural fixes
# ---------------------------------------------------------------------------
_STRUCTURAL_BLOCK_PATCHES: List[Tuple[str, str, str]] = [
    # 0261.rst lines 45-58: mid-sentence split across two `.. subclause::` blocks
    (
        "book_i/propositions/0261.rst",
        """| For, if the triangle :g:`$ABC$ <0261.g1:< A B C >>` be applied\\ [#f6]_ to the triangle :g:`$DEF$ <0261.g1:< D E F >>`,
| and if the point :g:`$A$ <0261.g1:A>` be placed

.. subclause::

   on the point :g:`$D$ <0261.g1:D>`

and the straight line :g:`$AB$ <0261.g1:/ A B />`

.. subclause::

   on :g:`$DE$ <0261.g1:/ D E />`,

then the point :g:`$B$ <0261.g1:B>` will also coincide with :g:`$E$ <0261.g1:E>`, because :g:`$AB$ <0261.g1:/ A B />` is equal to :g:`$DE$ <0261.g1:/ D E />`.""",
        """For, if the triangle :g:`$ABC$ <0261.g1:< A B C >>` be applied\\ [#f6]_ to the triangle :g:`$DEF$ <0261.g1:< D E F >>`, and if the point :g:`$A$ <0261.g1:A>` be placed on the point :g:`$D$ <0261.g1:D>` and the straight line :g:`$AB$ <0261.g1:/ A B />` on :g:`$DE$ <0261.g1:/ D E />`, then the point :g:`$B$ <0261.g1:B>` will also coincide with :g:`$E$ <0261.g1:E>`, because :g:`$AB$ <0261.g1:/ A B />` is equal to :g:`$DE$ <0261.g1:/ D E />`.""",
    ),
    # 0262.rst lines 12-20: mid-bracket split across `.. subclause::`
    (
        "book_i/propositions/0262.rst",
        """| But :g:`$B$ <0261.g1:B>` also coincided with :g:`$E$ <0261.g1:E>`;
| hence the base :g:`$BC$ <0261.g1:/ B C />` will coincide with the base :g:`$EF$ <0261.g1:/ E F />`.
| [For if, when :g:`$B$ <0261.g1:B>` coincides with :g:`$E$ <0261.g1:E>` and :g:`$C$ <0261.g1:C>` with :g:`$F$ <0261.g1:F>`, the base :g:`$BC$ <0261.g1:/ B C />` does not coincide with the base :g:`$EF$ <0261.g1:/ E F />`, two straight lines will enclose a space: which is impossible.

Therefore the base :g:`$BC$ <0261.g1:/ B C />` will coincide with

.. subclause:: [C.N. 4] <I.cn.4>

   :g:`$EF$ <0261.g1:/ E F />`]\\ [#f7]_ and will be equal to it.""",
        """But :g:`$B$ <0261.g1:B>` also coincided with :g:`$E$ <0261.g1:E>`; hence the base :g:`$BC$ <0261.g1:/ B C />` will coincide with the base :g:`$EF$ <0261.g1:/ E F />` [For if, when :g:`$B$ <0261.g1:B>` coincides with :g:`$E$ <0261.g1:E>` and :g:`$C$ <0261.g1:C>` with :g:`$F$ <0261.g1:F>`, the base :g:`$BC$ <0261.g1:/ B C />` does not coincide with the base :g:`$EF$ <0261.g1:/ E F />`, two straight lines will enclose a space: which is impossible. Therefore the base :g:`$BC$ <0261.g1:/ B C />` will coincide with :g:`$EF$ <0261.g1:/ E F />`]\\ [#f7]_ and will be equal to it. :just:`[C.N. 4] <I.cn.4>`""",
    ),
    # 0270.rst lines 16-20: "the less to the greater: / which is absurd."
    (
        "book_i/propositions/0270.rst",
        """.. assertion::

   the less to the greater:

which is absurd.""",
        """.. assertion::

   the less to the greater: which is absurd.""",
    ),
    # 0306.rst lines 23-36: "| Let the three given straight lines... | namely / .. subclause::"
    (
        "book_i/propositions/0306.rst",
        """| Let the three given straight lines be :g:`$A$ <0306.g1:A>`, :g:`$B$ <0306.g1:B>`, :g:`$C$ <0306.g1:C>`, and of these let two taken together in any manner be greater than the remaining one,
| namely""",
        """Let the three given straight lines be :g:`$A$ <0306.g1:A>`, :g:`$B$ <0306.g1:B>`, :g:`$C$ <0306.g1:C>`, and of these let two taken together in any manner be greater than the remaining one, namely,""",
    ),
    # 0394.rst lines 37-41: "For the same reason / .. assertion:: / :g:`$HF$ <0393.g1:< H F >>` is also a square;"
    (
        "book_ii/propositions/0394.rst",
        """For the same reason

.. assertion::

   :g:`$HF$ <0393.g1:< H F >>` is also a square;""",
        """.. assertion::

   For the same reason :g:`$HF$ <0393.g1:< H F >>` is also a square;""",
    ),
    # 0404.rst lines 17-21: "For the same reason / .. assertion:: / :g:`$QR$ <0404.g1:/ Q R />` is also equal to :g:`$RP$ <0404.g1:/ R P />`."
    (
        "book_ii/propositions/0404.rst",
        """For the same reason

.. assertion::

   :g:`$QR$ <0404.g1:/ Q R />` is also equal to :g:`$RP$ <0404.g1:/ R P />`.""",
        """.. assertion::

   For the same reason :g:`$QR$ <0404.g1:/ Q R />` is also equal to :g:`$RP$ <0404.g1:/ R P />`.""",
    ),
]


def strip_line_roles(lines: List[str]) -> Tuple[List[str], int]:
    """Remove all :line:`N` tags and clean up resulting whitespace or empty pipe lines."""
    out: List[str] = []
    removed_count = 0
    line_role_re = re.compile(r":line:`\d+`")

    for line in lines:
        # Normalize any 1-space or 4-space indent left from an earlier pass where :line:`N` was at the start of the line
        if re.match(r"^ \S", line):
            line = line[1:]
        elif re.match(r"^    (?!- )\S", line):
            line = "   " + line[4:]

        matches = line_role_re.findall(line)
        if not matches:
            out.append(line)
            continue

        removed_count += len(matches)
        # Preserve original leading indentation before removing :line:`N`
        indent_len = len(line) - len(line.lstrip(" "))
        indent = line[:indent_len]
        cleaned = line_role_re.sub("", line[indent_len:])
        body = cleaned.lstrip(" ")
        # Clean spaces after `| ` if it's a pipe line
        if body.startswith("|"):
            rest = body[1:].strip()
            if not rest:
                # Line was just `| :line:`25`` -> drop empty pipe line
                continue
            body = "| " + re.sub(r"  +", " ", rest)
        else:
            body = re.sub(r"  +", " ", body).strip()
            if not body:
                continue
        out.append(indent + body)

    return out, removed_count


def reflow_pipe_block(
    pipe_lines: List[str],
    rel_path: str,
    is_prop_body: bool,
) -> List[str]:
    """Reflow a contiguous group of `| ...` lines into clean paragraphs."""
    if not pipe_lines:
        return []

    # Check if this is the 2-line equation inside .. assertion:: in 0397.rst
    if rel_path == "book_ii/propositions/0397.rst" and any("$ax - x^2 =$" in l for l in pipe_lines):
        return pipe_lines

    first = pipe_lines[0]
    indent_len = len(first) - len(first.lstrip(" "))
    indent = first[:indent_len]

    # Extract text after `| `
    texts: List[str] = []
    for l in pipe_lines:
        s = l.strip()
        if s.startswith("|"):
            t = s[1:].strip()
            if t:
                texts.append(t)

    if not texts:
        return []

    # Inside directives (`.. assertion::`, `.. subclause::`, `.. qed::`, `.. porism::`), indent is 3+ spaces
    if indent_len >= 3 and "propositions/" in rel_path:
        return [indent + " ".join(texts)]

    # Group texts into paragraphs
    paragraphs: List[List[str]] = [[texts[0]]]
    for prev_t, curr_t in zip(texts, texts[1:]):
        start_new_para = False

        if is_prop_body:
            # 1. Previous line ended with a :just:`...` citation -> separate step!
            if re.search(r":just:`[^`]+`\s*$", prev_t):
                start_new_para = True
            # 2. Previous line ended with `;` or `.` and current line starts a distinct statement/construction step
            elif prev_t.endswith((";", ".")):
                if re.match(
                    r"^(?:I say\b|thus it is required\b|\[For if\b|Let\b|for let\b|again,\s*with centre\b|with centre\b|and from the point\b|and let\b|from\s+:g:|on\s+:g:|through\s+)",
                    curr_t,
                ):
                    start_new_para = True
        else:
            # Commentary or Introduction / Common Notions prose:
            # Start a new paragraph before numbered/lettered items or distinct steps
            if re.match(
                r"^(?:\(\d+\)|\(\$[a-z\\]+\$\)|>\s*\*\*[IVX]+\.|>\s*etc\.|All\s+\$[A-Z]\$|All\s+not-\$[A-Z]\$|and it follows logically that\b)",
                curr_t,
            ):
                start_new_para = True
            elif prev_t.endswith(".") and re.match(r"^\([1-9a-z]\)", curr_t):
                start_new_para = True

        if start_new_para:
            paragraphs.append([curr_t])
        else:
            paragraphs[-1].append(curr_t)

    out_lines: List[str] = []
    for idx, para in enumerate(paragraphs):
        if idx > 0:
            out_lines.append("")
        out_lines.append(indent + " ".join(para))
    return out_lines


def reflow_folio_pipes(lines: List[str], rel_path: str) -> Tuple[List[str], int]:
    """Unwrap and reflow `| ` blocks in a folio unless the folio is in _KEEP_PIPE_FILES."""
    if rel_path in _KEEP_PIPE_FILES:
        return lines, 0

    out: List[str] = []
    i = 0
    n = len(lines)
    unwrapped_count = 0

    # Track whether we are inside a proposition body (between `PROPOSITION N.` / top of continuation prop and `----`)
    # Note: some folios start with commentary from Prop N-1, then `PROPOSITION N.`, then prop body.
    # And some folios start directly with the continuation of Prop N's body, then `----`, then commentary.
    in_prop_body = False
    if "propositions/" in rel_path:
        # Check if the file starts inside a proposition body (before the first `----` or `PROPOSITION`)
        for l in lines:
            s = l.strip()
            if s.startswith("PROPOSITION "):
                in_prop_body = False
                break
            if s == "----":
                # If we hit `----` before `PROPOSITION`, check if there were proposition directives/lines before `----`
                break
        # More accurately: scan top-to-bottom and maintain `in_prop_body`:
        # At file start, we are in_prop_body if before the first `----` or `PROPOSITION` there is `.. assertion::`, `.. subclause::`, `.. qed::`, or `:just:`.
        for l in lines:
            s = l.strip()
            if s.startswith("PROPOSITION "):
                break
            if s.startswith((".. assertion::", ".. subclause::", ".. qed::", ".. enunciation::")) or ":just:`" in s:
                in_prop_body = True
                break
            if s == "----":
                break

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("PROPOSITION "):
            in_prop_body = True
        elif stripped == "----":
            in_prop_body = False

        if line.lstrip().startswith("| ") or stripped == "|":
            # Collect contiguous `| ` lines
            block: List[str] = []
            while i < n and (lines[i].lstrip().startswith("| ") or lines[i].strip() == "|"):
                block.append(lines[i])
                i += 1
            reflowed = reflow_pipe_block(block, rel_path, in_prop_body)
            if reflowed != block:
                unwrapped_count += len(block)
            out.extend(reflowed)
        else:
            out.append(line)
            i += 1

    return out, unwrapped_count


def main() -> None:
    vol1_dir = _REPO_ROOT / "resources" / "heath" / "volume_I"

    # 1. Apply exact footnote patches and structural block patches first
    fn_applied = 0
    for rel_path, old_s, new_s in _FOOTNOTE_PATCHES:
        p = vol1_dir / rel_path
        txt = p.read_text(encoding="utf-8")
        if new_s in txt:
            fn_applied += 1
            continue
        if old_s not in txt:
            raise RuntimeError(f"Footnote patch target not found in {rel_path}: {old_s!r}")
        txt = txt.replace(old_s, new_s, 1)
        p.write_text(txt, encoding="utf-8")
        fn_applied += 1

    struct_applied = 0
    for rel_path, old_b, new_b in _STRUCTURAL_BLOCK_PATCHES:
        p = vol1_dir / rel_path
        txt = p.read_text(encoding="utf-8")
        if new_b in txt:
            struct_applied += 1
            continue
        if old_b not in txt:
            raise RuntimeError(f"Structural patch target not found in {rel_path}: {old_b!r}")
        txt = txt.replace(old_b, new_b, 1)
        p.write_text(txt, encoding="utf-8")
        struct_applied += 1

    # 2. Process all 446 folios: remove :line:`N` tags and reflow `| ` blocks
    rst_files = sorted(
        p for p in vol1_dir.rglob("*.rst") if not p.name.endswith(".notes.rst")
    )

    total_line_roles_removed = 0
    total_pipes_unwrapped = 0
    files_modified = 0

    for rst_p in rst_files:
        rel_path = str(rst_p.relative_to(vol1_dir))
        orig_txt = rst_p.read_text(encoding="utf-8")
        lines = orig_txt.splitlines()

        lines, n_line_removed = strip_line_roles(lines)
        total_line_roles_removed += n_line_removed

        lines, n_pipes = reflow_folio_pipes(lines, rel_path)
        total_pipes_unwrapped += n_pipes

        new_txt = "\n".join(lines) + "\n"
        if new_txt != orig_txt:
            rst_p.write_text(new_txt, encoding="utf-8")
            files_modified += 1

    # 3. Verify across all 446 folios
    remaining_line_roles = 0
    remaining_pipes = 0
    total_fn_refs = 0
    total_fn_defs = 0
    render_errors: List[Tuple[str, str]] = []

    for rst_p in rst_files:
        rel_path = str(rst_p.relative_to(vol1_dir))
        txt = rst_p.read_text(encoding="utf-8")
        remaining_line_roles += len(re.findall(r":line:`\d+`", txt))
        remaining_pipes += sum(1 for l in txt.splitlines() if l.lstrip().startswith("| "))
        total_fn_refs += len(re.findall(r"\[#f\d+\]_", txt))
        total_fn_defs += len(re.findall(r"^\.\.\s+\[#f\d+\]", txt, flags=re.M))

        try:
            html = render_rst_html(txt)
            if not html and txt.strip():
                render_errors.append((rel_path, "Empty HTML output"))
        except Exception as exc:
            render_errors.append((rel_path, str(exc)))

    print(f"Footnote patches applied/verified: {fn_applied} / {len(_FOOTNOTE_PATCHES)}")
    print(f"Structural patches applied/verified: {struct_applied} / {len(_STRUCTURAL_BLOCK_PATCHES)}")
    print(f"Total :line: tags removed: {total_line_roles_removed} (remaining: {remaining_line_roles})")
    print(f"Total | lines unwrapped: {total_pipes_unwrapped} (remaining intentional | lines: {remaining_pipes})")
    print(f"Total [#fN]_ references in Volume I: {total_fn_refs}")
    print(f"Total .. [#fN] definitions in Volume I: {total_fn_defs}")
    print(f"Render errors across {len(rst_files)} folios: {len(render_errors)}")
    for rel, err in render_errors[:20]:
        print(f"  {rel}: {err}")


if __name__ == "__main__":
    main()
