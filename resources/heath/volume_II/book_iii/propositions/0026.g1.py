"""Programmatic construction for Book III, Proposition 8 Note (0026.g1).

De Morgan's note on Book III, Proposition 8: from external point D, secants
D-K-Z-Y-E and D-L-F are drawn to the circle with centre M, meeting the radii
LM and FM at Z and Y respectively.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0026_g1() -> Model:
    """Construct the figure 0026.g1 using geometor.model."""
    model = Model("0026.g1")

    # Circle centre M at origin and radius 1
    M = model.set_point(0, 0, classes=["given"], label="M")
    E = model.set_point(-1, 0, label="E")
    model.construct_circle(M, E)

    # External point D in the first quadrant
    D = model.set_point(sp.Rational(68, 67), sp.Rational(87, 67), classes=["given"], label="D")
    model.construct_line(D, M)

    # Line DE through D and E(-1, 0) meeting the circle again at K
    model.construct_line(D, E)
    vx1, vy1 = -1 - D.x, -D.y
    a1 = vx1**2 + vy1**2
    b1 = 2 * (D.x * vx1 + D.y * vy1)
    c1 = D.x**2 + D.y**2 - 1
    t_K = (-b1 - sp.sqrt(b1**2 - 4 * a1 * c1)) / (2 * a1)
    K = model.set_point(D.x + t_K * vx1, D.y + t_K * vy1, label="K")

    # Line DLF through D with slope 9/25 meeting circle at L and F
    vx2, vy2 = sp.Integer(-25), sp.Integer(-9)
    a2 = vx2**2 + vy2**2
    b2 = 2 * (D.x * vx2 + D.y * vy2)
    c2 = D.x**2 + D.y**2 - 1
    disc2 = sp.sqrt(b2**2 - 4 * a2 * c2)
    t_L = (-b2 - disc2) / (2 * a2)
    t_F = (-b2 + disc2) / (2 * a2)
    L = model.set_point(D.x + t_L * vx2, D.y + t_L * vy2, label="L")
    F = model.set_point(D.x + t_F * vx2, D.y + t_F * vy2, label="F")
    model.construct_line(D, F)

    # Intersections Z = DE cap LM and Y = DE cap FM
    model.construct_line(L, M)
    model.construct_line(F, M)

    # Line DE has equation y = m_DE * (x + 1) where m_DE = D.y / (D.x + 1)
    m_DE = D.y / (D.x + 1)
    x_Z = m_DE * L.x / (L.y - m_DE * L.x)
    Z = model.set_point(x_Z, m_DE * (x_Z + 1), label="Z")

    x_Y = m_DE * F.x / (F.y - m_DE * F.x)
    Y = model.set_point(x_Y, m_DE * (x_Y + 1), label="Y")

    # Segments along secant D-K-Z-Y-E
    model.set_segment(D, K)
    model.set_segment(K, Z)
    model.set_segment(Z, Y)
    model.set_segment(Y, E)
    model.set_segment(D, E)

    # Segments along secant D-L-F
    model.set_segment(D, L)
    model.set_segment(L, F)
    model.set_segment(D, F)

    # Radii and sub-segments from M
    model.set_segment(M, Z)
    model.set_segment(Z, L)
    model.set_segment(M, L)
    model.set_segment(M, Y)
    model.set_segment(Y, F)
    model.set_segment(M, F)
    model.set_segment(M, K)
    model.set_segment(M, E)
    model.set_segment(D, M)

    # Triangles DLM and DFM
    model.set_polygon([D, L, M])
    model.set_polygon([D, F, M])

    return model


if __name__ == "__main__":
    construct_0026_g1()
