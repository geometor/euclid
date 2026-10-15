"""Programmatic construction for Book XI, Proposition 37 (0362.g1).

Four proportional straight lines AB, CD, EF, GH and the similar and similarly
situated parallelepipedal solids KA, LC, ME, NG described on them.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def _add_box(
    model: Model,
    x1: int, y1: int,
    x2: int, y2: int,
    dx: int, dy: int,
    lbl_bl: str, lbl_br: str, lbl_tr: str,
) -> None:
    """Add a parallelepiped box to the model."""
    p_tl1 = model.set_point(sp.Rational(x1, 100), sp.Rational(191 - y1, 100), label=f"{lbl_bl}_tl1")
    p_tr1 = model.set_point(sp.Rational(x2, 100), sp.Rational(191 - y1, 100), classes=["given"], label=lbl_tr)
    p_br1 = model.set_point(sp.Rational(x2 - 3, 100), sp.Rational(191 - y2, 100), label=f"{lbl_bl}_br1")
    p_bl1 = model.set_point(sp.Rational(x1 - 3, 100), sp.Rational(191 - y2, 100), label=f"{lbl_bl}_bl1")

    p_tl2 = model.set_point(sp.Rational(x1 + dx, 100), sp.Rational(191 - (y1 + dy), 100), label=f"{lbl_bl}_tl2")
    p_tr2 = model.set_point(sp.Rational(x2 + dx, 100), sp.Rational(191 - (y1 + dy), 100), label=f"{lbl_bl}_tr2")
    p_br2 = model.set_point(sp.Rational(x2 - 3 + dx, 100), sp.Rational(191 - (y2 + dy), 100), classes=["given"], label=lbl_br)
    p_bl2 = model.set_point(sp.Rational(x1 - 3 + dx, 100), sp.Rational(191 - (y2 + dy), 100), classes=["given"], label=lbl_bl)

    for p1, p2 in [
        (p_tl1, p_tr1), (p_tr1, p_br1), (p_br1, p_bl1), (p_bl1, p_tl1),
        (p_tl2, p_tr2), (p_tr2, p_br2), (p_br2, p_bl2), (p_bl2, p_tl2),
        (p_tl1, p_tl2), (p_tr1, p_tr2), (p_br1, p_br2), (p_bl1, p_bl2),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([p_bl1, p_br1, p_br2, p_bl2])
    model.set_polygon([p_tl2, p_tr2, p_br2, p_bl2])


def construct_0362_g1() -> Model:
    """Construct the four similar parallelepipeds KA, LC, ME, NG for XI.37."""
    model = Model("0362.g1")

    _add_box(model, 30, 92, 98, 134, 16, 23, "A", "B", "K")
    _add_box(model, 168, 77, 256, 131, 20, 27, "C", "D", "L")
    _add_box(model, 338, 65, 442, 129, 24, 31, "E", "F", "M")
    _add_box(model, 482, 36, 616, 122, 30, 36, "G", "H", "N")

    return model


if __name__ == "__main__":
    construct_0362_g1()
