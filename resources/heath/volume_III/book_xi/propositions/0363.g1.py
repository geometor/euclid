"""Programmatic construction for Book XI, Proposition 37 Alternative Proof (0363.g1).

Four similar parallelepipeds KA, LC, ME, NG on AB, CD, EF, GH together with
continuous proportionals O, P and Q, R and fifth similar parallelepiped SV on ST.
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
    p_tl1 = model.set_point(sp.Rational(x1, 100), sp.Rational(340 - y1, 100), label=f"{lbl_bl}_tl1")
    p_tr1 = model.set_point(sp.Rational(x2, 100), sp.Rational(340 - y1, 100), classes=["given"], label=lbl_tr)
    p_br1 = model.set_point(sp.Rational(x2 - 4, 100), sp.Rational(340 - y2, 100), label=f"{lbl_bl}_br1")
    p_bl1 = model.set_point(sp.Rational(x1 - 4, 100), sp.Rational(340 - y2, 100), label=f"{lbl_bl}_bl1")

    p_tl2 = model.set_point(sp.Rational(x1 + dx, 100), sp.Rational(340 - (y1 + dy), 100), label=f"{lbl_bl}_tl2")
    p_tr2 = model.set_point(sp.Rational(x2 + dx, 100), sp.Rational(340 - (y1 + dy), 100), label=f"{lbl_bl}_tr2")
    p_br2 = model.set_point(sp.Rational(x2 - 4 + dx, 100), sp.Rational(340 - (y2 + dy), 100), classes=["given"], label=lbl_br)
    p_bl2 = model.set_point(sp.Rational(x1 - 4 + dx, 100), sp.Rational(340 - (y2 + dy), 100), classes=["given"], label=lbl_bl)

    for p1, p2 in [
        (p_tl1, p_tr1), (p_tr1, p_br1), (p_br1, p_bl1), (p_bl1, p_tl1),
        (p_tl2, p_tr2), (p_tr2, p_br2), (p_br2, p_bl2), (p_bl2, p_tl2),
        (p_tl1, p_tl2), (p_tr1, p_tr2), (p_br1, p_br2), (p_bl1, p_bl2),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([p_bl1, p_br1, p_br2, p_bl2])
    model.set_polygon([p_tl2, p_tr2, p_br2, p_bl2])


def construct_0363_g1() -> Model:
    """Construct the alternative proof figure for XI.37 using geometor.model."""
    model = Model("0363.g1")

    _add_box(model, 55, 64, 115, 106, 13, 18, "A", "B", "K")
    _add_box(model, 166, 54, 242, 104, 16, 22, "C", "D", "L")
    _add_box(model, 282, 42, 375, 102, 20, 26, "E", "F", "M")
    _add_box(model, 402, 20, 518, 96, 24, 32, "G", "H", "N")
    _add_box(model, 440, 206, 546, 276, 22, 26, "S", "T", "V")

    # Continuous proportional lines O, P, Q, R
    O1 = model.set_point(sp.Rational(52, 100), sp.Rational(172, 100), classes=["given"], label="O")
    O2 = model.set_point(sp.Rational(142, 100), sp.Rational(172, 100), label="O2")
    P1 = model.set_point(sp.Rational(176, 100), sp.Rational(172, 100), classes=["given"], label="P")
    P2 = model.set_point(sp.Rational(308, 100), sp.Rational(172, 100), label="P2")
    Q1 = model.set_point(sp.Rational(232, 100), sp.Rational(188, 100), classes=["given"], label="Q")
    Q2 = model.set_point(sp.Rational(345, 100), sp.Rational(188, 100), label="Q2")
    R1 = model.set_point(sp.Rational(396, 100), sp.Rational(188, 100), classes=["given"], label="R")
    R2 = model.set_point(sp.Rational(542, 100), sp.Rational(188, 100), label="R2")

    for p1, p2 in [(O1, O2), (P1, P2), (Q1, Q2), (R1, R2)]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0363_g1()
