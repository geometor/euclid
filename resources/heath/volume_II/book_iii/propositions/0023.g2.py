"""Programmatic construction for Book III, Proposition 7 Note (0023.g2).

Heron's third case: both perpendiculars DG and DH from the centre D to EA and
FA fall on the lines produced beyond A (chords EAGK and FAHL intersecting at A).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0023_g2() -> Model:
    """Construct the figure 0023.g2 using geometor.model."""
    model = Model("0023.g2")

    # Circle centre D and diameter endpoints C, B
    D = model.set_point(0, 0, classes=["given"], label="D")
    B = model.set_point(1, 0, classes=["given"], label="B")
    C = model.set_point(-1, 0, label="C")

    model.construct_line(C, B)
    model.construct_circle(D, B)

    # Internal point A on segment CD
    A = model.set_point(sp.Rational(-23, 35), 0, classes=["given"], label="A")

    # Line EAGK through A with direction (11, -5) in math coordinates
    # Foot G of perpendicular from D(0,0) to line EAGK
    dx1, dy1 = sp.Integer(11), sp.Integer(-5)
    t_G = (sp.Rational(23, 35) * dx1) / (dx1**2 + dy1**2)
    x_G = sp.Rational(-23, 35) + t_G * dx1
    y_G = t_G * dy1
    G = model.set_point(x_G, y_G, label="G")

    # Chord endpoints E and K on unit circle
    half_EK = sp.sqrt((1 - (x_G**2 + y_G**2)) / (dx1**2 + dy1**2))
    E = model.set_point(x_G - half_EK * dx1, y_G - half_EK * dy1, label="E")
    K = model.set_point(x_G + half_EK * dx1, y_G + half_EK * dy1, label="K")
    model.construct_line(E, K)

    # Line FAHL through A with direction (3, 4) in math coordinates
    # Foot H of perpendicular from D(0,0) to line FAHL
    dx2, dy2 = sp.Integer(3), sp.Integer(4)
    t_H = (sp.Rational(23, 35) * dx2) / (dx2**2 + dy2**2)
    x_H = sp.Rational(-23, 35) + t_H * dx2
    y_H = t_H * dy2
    H = model.set_point(x_H, y_H, label="H")

    # Chord endpoints F and L on unit circle
    half_FL = sp.sqrt((1 - (x_H**2 + y_H**2)) / (dx2**2 + dy2**2))
    F = model.set_point(x_H - half_FL * dx2, y_H - half_FL * dy2, label="F")
    L = model.set_point(x_H + half_FL * dx2, y_H + half_FL * dy2, label="L")
    model.construct_line(F, L)

    # Diameter segments
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(C, D)
    model.set_segment(A, B)
    model.set_segment(C, B)
    model.set_section([C, A, D])
    model.set_section([A, D, B])

    # Sub-segments along chord EAGK
    model.set_segment(E, A)
    model.set_segment(A, G)
    model.set_segment(G, K)
    model.set_segment(E, G)
    model.set_segment(A, K)
    model.set_segment(E, K)
    model.set_section([E, A, G])
    model.set_section([A, G, K])
    model.set_section([E, A, K])

    # Sub-segments along chord FAHL
    model.set_segment(F, A)
    model.set_segment(A, H)
    model.set_segment(H, L)
    model.set_segment(F, H)
    model.set_segment(A, L)
    model.set_segment(F, L)
    model.set_section([F, A, H])
    model.set_section([A, H, L])
    model.set_section([F, A, L])

    # Radii and perpendiculars from D
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(D, E)
    model.set_segment(D, F)

    # Right-angled triangles
    model.set_polygon([D, G, E])
    model.set_polygon([D, G, A])
    model.set_polygon([D, H, F])
    model.set_polygon([D, H, A])

    return model


if __name__ == "__main__":
    construct_0023_g2()
