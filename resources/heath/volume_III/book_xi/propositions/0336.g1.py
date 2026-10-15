"""Programmatic construction for Book XI, Proposition 28 Commentary (0336.g1).

Two prisms ABCDE-FGHKL and A'B'C'D'E'-F'G'H'K'L' are equal when they have a solid
angle in each contained by three faces equal each to each and similarly arranged.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0336_g1() -> Model:
    """Construct the two equal pentagonal prisms for Book XI, Prop. 28 note."""
    model = Model("0336.g1")

    # Left prism ABCDE-FGHKL
    A = model.set_point(sp.Rational(69, 100), sp.Rational(33, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(132, 100), sp.Rational(33, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(165, 100), sp.Rational(77, 100), classes=["given"], label="C")
    D = model.set_point(sp.Rational(95, 100), sp.Rational(102, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(25, 100), sp.Rational(59, 100), classes=["given"], label="E")

    F = model.set_point(sp.Rational(69, 100), sp.Rational(128, 100), classes=["given"], label="F")
    G = model.set_point(sp.Rational(132, 100), sp.Rational(128, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(165, 100), sp.Rational(172, 100), classes=["given"], label="H")
    K = model.set_point(sp.Rational(95, 100), sp.Rational(197, 100), classes=["given"], label="K")
    L = model.set_point(sp.Rational(25, 100), sp.Rational(154, 100), classes=["given"], label="L")

    # Right prism A'B'C'D'E'-F'G'H'K'L'
    Ap = model.set_point(sp.Rational(237, 100), sp.Rational(33, 100), classes=["given"], label="A'")
    Bp = model.set_point(sp.Rational(300, 100), sp.Rational(33, 100), classes=["given"], label="B'")
    Cp = model.set_point(sp.Rational(333, 100), sp.Rational(77, 100), classes=["given"], label="C'")
    Dp = model.set_point(sp.Rational(263, 100), sp.Rational(102, 100), classes=["given"], label="D'")
    Ep = model.set_point(sp.Rational(193, 100), sp.Rational(59, 100), classes=["given"], label="E'")

    Fp = model.set_point(sp.Rational(237, 100), sp.Rational(128, 100), classes=["given"], label="F'")
    Gp = model.set_point(sp.Rational(300, 100), sp.Rational(128, 100), classes=["given"], label="G'")
    Hp = model.set_point(sp.Rational(333, 100), sp.Rational(172, 100), classes=["given"], label="H'")
    Kp = model.set_point(sp.Rational(263, 100), sp.Rational(197, 100), classes=["given"], label="K'")
    Lp = model.set_point(sp.Rational(193, 100), sp.Rational(154, 100), classes=["given"], label="L'")

    # Base and top polygons
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([F, G, H, K, L])
    model.set_polygon([Ap, Bp, Cp, Dp, Ep])
    model.set_polygon([Fp, Gp, Hp, Kp, Lp])

    # Lateral faces
    model.set_polygon([A, B, G, F])
    model.set_polygon([A, F, L, E])
    model.set_polygon([Ap, Bp, Gp, Fp])
    model.set_polygon([Ap, Fp, Lp, Ep])

    # Lateral segments
    for p, q in [
        (A, F), (B, G), (C, H), (D, K), (E, L),
        (Ap, Fp), (Bp, Gp), (Cp, Hp), (Dp, Kp), (Ep, Lp),
    ]:
        model.set_segment(p, q)

    return model


if __name__ == "__main__":
    construct_0336_g1()
