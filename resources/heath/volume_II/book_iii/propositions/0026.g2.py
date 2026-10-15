"""Programmatic construction for Book III, Proposition 8 Note (0026.g2).

Heron's note on Book III, Proposition 8: from external point A on the diameter
CB produced, secants A-K-G-E and A-L-H-F are drawn on opposite sides of the
diameter through the centre D, with perpendiculars DG and DH from D.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0026_g2() -> Model:
    """Construct the figure 0026.g2 using geometor.model."""
    model = Model("0026.g2")

    # Circle centre D at origin, vertical diameter BC, external point A above B
    D = model.set_point(0, 0, classes=["given"], label="D")
    B = model.set_point(0, 1, classes=["given"], label="B")
    C = model.set_point(0, -1, label="C")
    A = model.set_point(0, sp.Rational(68, 35), classes=["given"], label="A")

    model.construct_line(A, C)
    model.construct_circle(D, B)

    def secant_and_foot(vx: sp.Expr, vy: sp.Expr):
        """Return (near_pt, foot_pt, far_pt) on ray from A in direction (vx, vy)."""
        a = vx**2 + vy**2
        b = 2 * A.y * vy
        c = A.y**2 - 1
        disc = sp.sqrt(b**2 - 4 * a * c)
        t_near = (-b - disc) / (2 * a)
        t_far = (-b + disc) / (2 * a)
        t_foot = -b / (2 * a)
        return (
            (t_near * vx, A.y + t_near * vy),
            (t_foot * vx, A.y + t_foot * vy),
            (t_far * vx, A.y + t_far * vy),
        )

    # Right secant A-K-G-E (nearer to centre D)
    (kx, ky), (gx, gy), (ex, ey) = secant_and_foot(sp.Integer(6), sp.Integer(-25))
    K = model.set_point(kx, ky, label="K")
    G = model.set_point(gx, gy, label="G")
    E = model.set_point(ex, ey, label="E")
    model.construct_line(A, E)

    # Left secant A-L-H-F (more remote from centre D)
    (lx, ly), (hx, hy), (fx, fy) = secant_and_foot(sp.Integer(-3), sp.Integer(-10))
    L = model.set_point(lx, ly, label="L")
    H = model.set_point(hx, hy, label="H")
    F = model.set_point(fx, fy, label="F")
    model.construct_line(A, F)

    # Collinear segments along A-B-D-C
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)
    model.set_segment(B, C)
    model.set_segment(A, C)

    # Collinear segments along A-K-G-E
    model.set_segment(A, K)
    model.set_segment(K, G)
    model.set_segment(G, E)
    model.set_segment(A, G)
    model.set_segment(K, E)
    model.set_segment(A, E)

    # Collinear segments along A-L-H-F
    model.set_segment(A, L)
    model.set_segment(L, H)
    model.set_segment(H, F)
    model.set_segment(A, H)
    model.set_segment(L, F)
    model.set_segment(A, F)

    # Perpendiculars and radii from D
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(D, K)
    model.set_segment(D, L)
    model.set_segment(D, E)
    model.set_segment(D, F)

    # Obtuse triangles AKD and ALD
    model.set_polygon([A, K, D])
    model.set_polygon([A, L, D])

    return model


if __name__ == "__main__":
    construct_0026_g2()
