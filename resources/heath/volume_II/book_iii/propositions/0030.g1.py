"""Programmatic construction for Book III, Proposition 10 Alternative Proof (0030.g1).

Alternative proof (Heron/Simson) of Book III, Proposition 10: if circle ABC
with centre K cuts circle DEF at more than two points B, G, F, H, then KB, KG,
KF are three equal straight lines falling from K on circle DEF.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0030_g1() -> Model:
    """Construct the figure 0030.g1 using geometor.model."""
    model = Model("0030.g1")

    # Circle ABC with centre K at origin
    K = model.set_point(0, 0, classes=["given"], label="K")
    A = model.set_point(0, 1, label="A")
    C = model.set_point(0, -1, label="C")
    model.construct_circle(K, A)

    # Points B, G, F, H common to both circles
    B = model.set_point(sp.Rational(18, 25), sp.Rational(7, 25) * sp.sqrt(7), classes=["given"], label="B")
    G = model.set_point(sp.Rational(18, 25), sp.Rational(-7, 25) * sp.sqrt(7), classes=["given"], label="G")
    H = model.set_point(sp.Rational(-9, 10), sp.sqrt(19) / 10, classes=["given"], label="H")
    F = model.set_point(sp.Rational(-9, 10), -sp.sqrt(19) / 10, classes=["given"], label="F")

    # Auxiliary points D, E on circle DEF
    D = model.set_point(sp.Rational(-1, 5), sp.Rational(3, 5), label="D")
    E = model.set_point(sp.Rational(29, 25), sp.Rational(1, 5), label="E")

    # Equal straight lines KB, KG, KF from centre K
    model.set_segment(K, B)
    model.set_segment(K, G)
    model.set_segment(K, F)

    return model


if __name__ == "__main__":
    construct_0030_g1()
