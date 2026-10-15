"""Programmatic construction for Book XI, Proposition 30 Commentary (0340.g2).

Transformation of an oblique parallelepiped ABCD-EFGH into an equivalent
parallelepiped A'B'C'D'-E'F'G'H' by right sections perpendicular to AB, and
then into a rectangular parallelepiped A''B''C''D''-E''F''G''H'' by right
sections perpendicular to B'C'.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0340_g2() -> Model:
    """Construct the three-step parallelepiped reduction figure (0340.g2)."""
    model = Model("0340.g2")

    # Original oblique parallelepiped ABCD-EFGH
    A = model.set_point(sp.Rational(26, 100), sp.Rational(166, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(118, 100), sp.Rational(166, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(168, 100), sp.Rational(212, 100), classes=["given"], label="C")
    D = model.set_point(sp.Rational(76, 100), sp.Rational(212, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(66, 100), sp.Rational(244, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(158, 100), sp.Rational(244, 100), classes=["given"], label="F")
    G = model.set_point(sp.Rational(208, 100), sp.Rational(290, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(116, 100), sp.Rational(290, 100), classes=["given"], label="H")

    # Intermediate parallelepiped A'B'C'D'-E'F'G'H'
    Ap = model.set_point(sp.Rational(351, 100), sp.Rational(166, 100), label="A'")
    Bp = model.set_point(sp.Rational(443, 100), sp.Rational(166, 100), label="B'")
    Cp = model.set_point(sp.Rational(460, 100), sp.Rational(212, 100), label="C'")
    Dp = model.set_point(sp.Rational(368, 100), sp.Rational(212, 100), label="D'")
    Ep = model.set_point(sp.Rational(355, 100), sp.Rational(244, 100), label="E'")
    Fp = model.set_point(sp.Rational(447, 100), sp.Rational(244, 100), label="F'")
    Gp = model.set_point(sp.Rational(464, 100), sp.Rational(290, 100), label="G'")
    Hp = model.set_point(sp.Rational(372, 100), sp.Rational(290, 100), label="H'")

    # Final rectangular parallelepiped A''B''C''D''-E''F''G''H''
    App = model.set_point(sp.Rational(296, 100), sp.Rational(28, 100), label="A''")
    Bpp = model.set_point(sp.Rational(388, 100), sp.Rational(28, 100), label="B''")
    Cpp = model.set_point(sp.Rational(407, 100), sp.Rational(76, 100), label="C''")
    Dpp = model.set_point(sp.Rational(315, 100), sp.Rational(76, 100), label="D''")
    Epp = model.set_point(sp.Rational(293, 100), sp.Rational(88, 100), label="E''")
    Fpp = model.set_point(sp.Rational(385, 100), sp.Rational(88, 100), label="F''")
    Gpp = model.set_point(sp.Rational(404, 100), sp.Rational(136, 100), label="G''")
    Hpp = model.set_point(sp.Rational(312, 100), sp.Rational(136, 100), label="H''")

    for p, q in [
        (A, B), (D, C), (E, F), (H, G),
        (Ap, Bp), (Dp, Cp), (Ep, Fp), (Hp, Gp),
        (Dp, Ap), (Cp, Bp), (Gp, Fp), (Hp, Ep),
        (Bpp, Cpp),
    ]:
        model.set_segment(p, q)

    model.set_polygon([Ap, Dp, Hp, Ep])
    model.set_polygon([Bp, Cp, Gp, Fp])

    return model


if __name__ == "__main__":
    construct_0340_g2()
