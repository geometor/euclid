"""Programmatic construction for Book III, Proposition 10 (0029.g1).

A circle ABC does not cut a circle DEF at more points than two (reductio ad
absurdum assuming four common points B, G, F, H and constructing the
perpendicular bisectors AC of BH and NO of BG intersecting at the common
centre P).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0029_g1() -> Model:
    """Construct the figure 0029.g1 for Book III, Proposition 10."""
    model = Model("0029.g1")

    # Circle ABC with centre P at origin and horizontal diameter NO
    P = model.set_point(0, 0, classes=["given"], label="P")
    O = model.set_point(1, 0, label="O")
    N = model.set_point(-1, 0, label="N")
    model.construct_line(N, O)
    model.construct_circle(P, O)

    # Outer endpoints M, E of the second circle DEF along the horizontal bisector
    M = model.set_point(sp.Rational(-53, 44), 0, label="M")
    E = model.set_point(sp.Rational(29, 22), 0, label="E")

    # Vertical chord BG bisected at right angles at L by NO
    L = model.set_point(sp.Rational(21, 25), 0, label="L")
    B = model.set_point(sp.Rational(21, 25), sp.Rational(2, 5) * sp.sqrt(6), classes=["given"], label="B")
    G = model.set_point(sp.Rational(21, 25), sp.Rational(-2, 5) * sp.sqrt(6), classes=["given"], label="G")
    model.construct_line(B, G)

    # Points H and F on the left side of circle ABC
    H = model.set_point(sp.Rational(-22, 25), sp.Rational(3, 25) * sp.sqrt(21), classes=["given"], label="H")
    F = model.set_point(sp.Rational(-22, 25), sp.Rational(-3, 25) * sp.sqrt(21), classes=["given"], label="F")
    model.construct_line(H, B)

    # Midpoint K of chord HB and perpendicular bisector AC through K and P
    K = model.set_point((H.x + B.x) / 2, (H.y + B.y) / 2, label="K")
    model.construct_line(K, P)
    len_KP = sp.sqrt(K.x**2 + K.y**2)
    ux, uy = K.x / len_KP, K.y / len_KP
    A = model.set_point(ux, uy, label="A")
    C = model.set_point(-ux, -uy, label="C")
    D = model.set_point(sp.Rational(7, 10) * ux, sp.Rational(7, 10) * uy, label="D")

    # Chords BH and BG and their sub-segments
    model.set_segment(B, K)
    model.set_segment(K, H)
    model.set_segment(B, H)
    model.set_section([B, K, H])

    model.set_segment(B, L)
    model.set_segment(L, G)
    model.set_segment(B, G)
    model.set_section([B, L, G])

    # Perpendicular bisector A-D-K-P-C segments
    model.set_segment(A, D)
    model.set_segment(D, K)
    model.set_segment(K, P)
    model.set_segment(P, C)
    model.set_segment(K, C)
    model.set_segment(A, C)

    # Perpendicular bisector M-N-P-L-O-E segments
    model.set_segment(M, N)
    model.set_segment(N, P)
    model.set_segment(P, L)
    model.set_segment(L, O)
    model.set_segment(O, E)
    model.set_segment(L, M)
    model.set_segment(N, O)
    model.set_segment(M, E)

    return model


if __name__ == "__main__":
    construct_0029_g1()
