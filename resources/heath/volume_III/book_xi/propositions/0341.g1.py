"""Programmatic construction for Book XI, Proposition 31 (0341.g1).

Parallelepipedal solids AE and CF on equal bases AB and CD and of the same height
are equal to one another, proved via auxiliary solids XU, XY, RI, and CI.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0341_g1() -> Model:
    """Construct the parallelepipedal solids for Book XI, Proposition 31."""
    model = Model("0341.g1")

    # Left compound figure: top-back line Q-F-I and top-front line P-D-a
    Q = model.set_point(sp.Rational(60, 100), sp.Rational(224, 100), classes=["given"], label="Q")
    F = model.set_point(sp.Rational(179, 100), sp.Rational(224, 100), classes=["given"], label="F")
    I = model.set_point(sp.Rational(300, 100), sp.Rational(224, 100), label="I")

    P = model.set_point(sp.Rational(28, 100), sp.Rational(186, 100), classes=["given"], label="P")
    D = model.set_point(sp.Rational(147, 100), sp.Rational(186, 100), classes=["given"], label="D")
    a = model.set_point(sp.Rational(268, 100), sp.Rational(186, 100), label="a")

    # Middle-back line O-S-X and middle-front line C-R-T
    O = model.set_point(sp.Rational(47, 100), sp.Rational(146, 100), classes=["given"], label="O")
    S = model.set_point(sp.Rational(166, 100), sp.Rational(146, 100), classes=["given"], label="S")
    X = model.set_point(sp.Rational(287, 100), sp.Rational(146, 100), label="X")

    C = model.set_point(sp.Rational(15, 100), sp.Rational(108, 100), classes=["given"], label="C")
    R = model.set_point(sp.Rational(134, 100), sp.Rational(108, 100), classes=["given"], label="R")
    T = model.set_point(sp.Rational(255, 100), sp.Rational(108, 100), label="T")

    # Bottom-back line e-d-c-V and bottom-front line Y-U-b-W
    e = model.set_point(sp.Rational(152, 100), sp.Rational(64, 100), label="e")
    d = model.set_point(sp.Rational(229, 100), sp.Rational(64, 100), label="d")
    c = model.set_point(sp.Rational(273, 100), sp.Rational(64, 100), label="c")
    V = model.set_point(sp.Rational(350, 100), sp.Rational(64, 100), label="V")

    Y = model.set_point(sp.Rational(120, 100), sp.Rational(26, 100), label="Y")
    U = model.set_point(sp.Rational(197, 100), sp.Rational(26, 100), label="U")
    b = model.set_point(sp.Rational(241, 100), sp.Rational(26, 100), label="b")
    W = model.set_point(sp.Rational(318, 100), sp.Rational(26, 100), label="W")

    # Right figure: solid AE
    K = model.set_point(sp.Rational(444, 100), sp.Rational(143, 100), classes=["given"], label="K")
    E = model.set_point(sp.Rational(565, 100), sp.Rational(143, 100), classes=["given"], label="E")
    H = model.set_point(sp.Rational(412, 100), sp.Rational(105, 100), classes=["given"], label="H")
    B = model.set_point(sp.Rational(533, 100), sp.Rational(105, 100), classes=["given"], label="B")
    G = model.set_point(sp.Rational(504, 100), sp.Rational(64, 100), classes=["given"], label="G")
    M = model.set_point(sp.Rational(625, 100), sp.Rational(64, 100), classes=["given"], label="M")
    A = model.set_point(sp.Rational(472, 100), sp.Rational(26, 100), classes=["given"], label="A")
    L = model.set_point(sp.Rational(593, 100), sp.Rational(26, 100), classes=["given"], label="L")

    # Segments
    for p, q in [
        (P, Q), (D, F), (C, O), (R, S), (a, I), (T, X),
        (H, K), (B, E), (A, G), (L, M),
        (C, R), (R, T), (R, U), (A, L), (L, B),
        (D, R), (R, Y), (D, Y), (W, U), (Y, W), (e, V),
        (a, b), (T, b), (T, W), (S, e), (S, d), (X, c), (X, V), (P, D),
    ]:
        model.set_segment(p, q)

    # Polygons
    model.set_polygon([A, H, B, L])
    model.set_polygon([C, P, D, R])
    model.set_polygon([R, U, W, T])
    model.set_polygon([R, T, X, S])
    model.set_polygon([A, L, M, G])
    model.set_polygon([L, B, E, M])
    model.set_polygon([S, R, U, d])
    model.set_polygon([Y, b, c, e])
    model.set_polygon([U, W, V, d])
    model.set_polygon([Y, b, T, R])
    model.set_polygon([D, a, T, R])
    model.set_polygon([R, D, F, S])

    return model


if __name__ == "__main__":
    construct_0341_g1()
