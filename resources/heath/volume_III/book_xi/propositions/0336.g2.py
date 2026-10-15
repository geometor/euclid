"""Programmatic construction for Book XI, Proposition 28 Commentary (0336.g2).

An oblique prism AD' is equivalent to a right prism GL' whose base GL is a right
section of the oblique prism and whose height is equal to a lateral edge of AD'.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0336_g2() -> Model:
    """Construct the oblique prism and right prism equivalence figure (0336.g2)."""
    model = Model("0336.g2")

    # Top right-section G'H'K'L'M'
    Mp = model.set_point(sp.Rational(21, 100), sp.Rational(246, 100), classes=["given"], label="M'")
    Gp = model.set_point(sp.Rational(52, 100), sp.Rational(244, 100), classes=["given"], label="G'")
    Hp = model.set_point(sp.Rational(116, 100), sp.Rational(271, 100), classes=["given"], label="H'")
    Kp = model.set_point(sp.Rational(165, 100), sp.Rational(296, 100), classes=["given"], label="K'")
    Lp = model.set_point(sp.Rational(85, 100), sp.Rational(283, 100), classes=["given"], label="L'")

    # Upper oblique base A'B'C'D'E'
    Ep = model.set_point(sp.Rational(46, 100), sp.Rational(186, 100), classes=["given"], label="E'")
    Ap = model.set_point(sp.Rational(84, 100), sp.Rational(166, 100), classes=["given"], label="A'")
    Bp = model.set_point(sp.Rational(157, 100), sp.Rational(166, 100), classes=["given"], label="B'")
    Cp = model.set_point(sp.Rational(203, 100), sp.Rational(202, 100), classes=["given"], label="C'")
    Dp = model.set_point(sp.Rational(115, 100), sp.Rational(210, 100), classes=["given"], label="D'")

    # Lower right-section GHKLM
    M = model.set_point(sp.Rational(80, 100), sp.Rational(102, 100), classes=["given"], label="M")
    G = model.set_point(sp.Rational(110, 100), sp.Rational(101, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(174, 100), sp.Rational(125, 100), classes=["given"], label="H")
    K = model.set_point(sp.Rational(224, 100), sp.Rational(151, 100), classes=["given"], label="K")
    L = model.set_point(sp.Rational(142, 100), sp.Rational(144, 100), classes=["given"], label="L")

    # Lower oblique base ABCDE
    E = model.set_point(sp.Rational(100, 100), sp.Rational(52, 100), classes=["given"], label="E")
    A = model.set_point(sp.Rational(137, 100), sp.Rational(33, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(209, 100), sp.Rational(34, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(255, 100), sp.Rational(74, 100), classes=["given"], label="C")
    D = model.set_point(sp.Rational(167, 100), sp.Rational(84, 100), classes=["given"], label="D")

    # Cross-section polygons
    model.set_polygon([G, H, K, L, M])
    model.set_polygon([Gp, Hp, Kp, Lp, Mp])
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([Ap, Bp, Cp, Dp, Ep])

    # Lateral segments
    for p, q in [
        (A, G), (Ap, Gp), (B, H), (Bp, Hp), (C, K), (Cp, Kp),
        (D, L), (Dp, Lp), (E, M), (Ep, Mp),
    ]:
        model.set_segment(p, q)

    # Truncated prism faces
    model.set_polygon([A, B, H, G])
    model.set_polygon([B, C, K, H])
    model.set_polygon([C, D, L, K])
    model.set_polygon([Ap, Bp, Hp, Gp])
    model.set_polygon([Bp, Cp, Kp, Hp])
    model.set_polygon([Cp, Dp, Lp, Kp])

    return model


if __name__ == "__main__":
    construct_0336_g2()
