"""Programmatic construction for Book III, Proposition 8 (0024.g1).

From an external point D, straight lines DA (through the centre M, meeting the
convex circumference at G), DE (through K), DF (through L), DC (through H) are
drawn to the circle ABC, together with DB (such that angle DMB = angle KMD)
and DN on the other side of DG.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0024_g1() -> Model:
    """Construct the figure 0024.g1 for Book III, Proposition 8."""
    model = Model("0024.g1")

    # Circle ABC with centre M at origin and radius 1
    M = model.set_point(0, 0, classes=["given"], label="M")
    P_unit = model.set_point(1, 0)
    model.construct_circle(M, P_unit)

    # External point D along rational unit vector (7/25, 24/25) from M
    ux, uy = sp.Rational(7, 25), sp.Rational(24, 25)
    d_dist = sp.Rational(32, 15)
    D = model.set_point(d_dist * ux, d_dist * uy, classes=["given"], label="D")
    G = model.set_point(ux, uy, label="G")
    A = model.set_point(-ux, -uy, label="A")
    model.construct_line(D, A)

    # Points on concave circumference: E, F, C
    # Points on convex circumference: K, L, H (collinear with D-E, D-F, D-C)
    def secant_points(vx: sp.Expr, vy: sp.Expr):
        """Intersect ray from D in direction (vx, vy) with unit circle at M."""
        a = vx**2 + vy**2
        b = 2 * (D.x * vx + D.y * vy)
        c = D.x**2 + D.y**2 - 1
        disc = sp.sqrt(b**2 - 4 * a * c)
        t_near = (-b - disc) / (2 * a)
        t_far = (-b + disc) / (2 * a)
        return (
            D.x + t_near * vx,
            D.y + t_near * vy,
            D.x + t_far * vx,
            D.y + t_far * vy,
        )

    # Secant D-K-E
    kx, ky, ex, ey = secant_points(sp.Rational(-2, 5), sp.Integer(-1))
    K = model.set_point(kx, ky, label="K")
    E = model.set_point(ex, ey, label="E")
    model.construct_line(D, E)

    # Secant D-L-F
    lx, ly, fx, fy = secant_points(sp.Rational(-14, 25), sp.Integer(-1))
    L = model.set_point(lx, ly, label="L")
    F = model.set_point(fx, fy, label="F")
    model.construct_line(D, F)

    # Secant D-H-C
    hx, hy, cx, cy = secant_points(sp.Rational(-21, 25), sp.Integer(-1))
    H = model.set_point(hx, hy, label="H")
    C = model.set_point(cx, cy, label="C")
    model.construct_line(D, C)

    # Point B on convex circumference such that angle DMB = angle KMD
    # Reflection of K across line MG (unit vector ux, uy)
    dot_K = K.x * ux + K.y * uy
    bx = 2 * dot_K * ux - K.x
    by = 2 * dot_K * uy - K.y
    B = model.set_point(bx, by, label="B")

    # Point N further along the convex circumference on the side of B
    N = model.set_point(sp.Rational(3, 5), sp.Rational(4, 5), label="N")

    # Collinear segments along D-G-M-A
    model.set_segment(D, G)
    model.set_segment(G, M)
    model.set_segment(M, A)
    model.set_segment(D, M)
    model.set_segment(G, A)
    model.set_segment(D, A)
    model.set_section([D, G, M])
    model.set_section([G, M, A])
    model.set_section([D, M, A])

    # Collinear segments along D-K-E, D-L-F, D-H-C
    for P_near, P_far in [(K, E), (L, F), (H, C)]:
        model.set_segment(D, P_near)
        model.set_segment(P_near, P_far)
        model.set_segment(D, P_far)
        model.set_section([D, P_near, P_far])

    # Segments DB and DN
    model.set_segment(D, B)
    model.set_segment(D, N)

    # Radii from centre M
    for P_circ in [E, F, C, K, L, H, B, N]:
        model.set_segment(M, P_circ)

    # Triangles compared in the proof
    for P_circ in [E, F, C, K, L, H, B, N]:
        model.set_polygon([D, M, P_circ])

    return model


if __name__ == "__main__":
    construct_0024_g1()
