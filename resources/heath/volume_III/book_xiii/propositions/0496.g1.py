"""Programmatic construction for Book XIII, Proposition 16 Commentary (0496.g1).

H. M. Taylor's construction of a regular icosahedron inscribed in a cube
ABCDEFGH of centre O, with face centres L, M, N and twelve vertices
P, P', Q, Q', R, R', p, p', q, q', r, r'.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0496_g1() -> Model:
    """Construct the figure 0496.g1 using geometor.model."""
    model = Model("0496.g1")

    # Cube vertices A, B, C, D, E, F, G, H and centre O
    A = model.set_point(19.5, -111.5, classes=["given"], label="A")
    B = model.set_point(100.0, -23.5, classes=["given"], label="B")
    C = model.set_point(401.5, -23.5, classes=["given"], label="C")
    D = model.set_point(318.5, -111.5, classes=["given"], label="D")
    E = model.set_point(19.5, -411.5, classes=["given"], label="E")
    F = model.set_point(100.0, -324.0, classes=["given"], label="F")
    G = model.set_point(401.5, -324.0, classes=["given"], label="G")
    H = model.set_point(318.5, -411.5, classes=["given"], label="H")
    O = model.set_point(210.5, -217.5, classes=["constructed"], label="O")

    # Face centres L, M, N
    L = model.set_point(210.5, -67.5, classes=["constructed"], label="L")
    M = model.set_point(169.0, -260.0, classes=["constructed"], label="M")
    N = model.set_point(61.0, -217.5, classes=["constructed"], label="N")

    # Twelve icosahedron vertices on the six faces of the cube
    P = model.set_point(183.5, -96.5, classes=["constructed"], label="P")
    P_prime = model.set_point(237.5, -38.5, classes=["constructed"], label="P'")
    p_prime = model.set_point(183.5, -396.5, classes=["constructed"], label="p'")
    p = model.set_point(237.5, -338.5, classes=["constructed"], label="p")

    Q = model.set_point(79.0, -260.0, classes=["constructed"], label="Q")
    Q_prime = model.set_point(261.0, -260.0, classes=["constructed"], label="Q'")
    q_prime = model.set_point(159.0, -172.0, classes=["constructed"], label="q'")
    q = model.set_point(341.0, -172.0, classes=["constructed"], label="q")

    R = model.set_point(61.0, -124.0, classes=["constructed"], label="R")
    R_prime = model.set_point(61.0, -311.0, classes=["constructed"], label="R'")
    r_prime = model.set_point(359.0, -124.0, classes=["constructed"], label="r'")
    r = model.set_point(359.0, -311.0, classes=["constructed"], label="r")

    # Polygons (Cube faces and Icosahedron faces)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, D, H, E])
    model.set_polygon([A, B, F, E])
    model.set_polygon([P, Q, Q_prime])
    model.set_polygon([P, R, Q])
    model.set_polygon([P, P_prime, R])
    model.set_polygon([P, P_prime, r_prime])
    model.set_polygon([P, Q_prime, r_prime])

    # Cube edges, perpendiculars OL, OM, ON, and icosahedron edges
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (E, F), (F, G), (G, H), (H, E),
        (A, E), (B, F), (C, G), (D, H),
        (O, L), (O, M), (O, N), (O, P),
        (P, P_prime), (L, P), (L, P_prime),
        (Q, Q_prime), (M, Q), (M, Q_prime),
        (R, R_prime), (N, R), (N, R_prime),
        (p, p_prime), (q, q_prime), (r, r_prime),
        (P, Q), (P, Q_prime), (P, R), (P, r_prime),
        (P_prime, R), (P_prime, r_prime), (P_prime, q_prime), (P_prime, q),
        (Q, R), (Q, R_prime), (Q, p_prime),
        (Q_prime, r_prime), (Q_prime, r), (Q_prime, p_prime),
        (R, q_prime), (R_prime, q_prime), (R_prime, p_prime), (R_prime, p),
        (r_prime, q), (r, q), (r, p_prime), (r, p),
        (p, q_prime), (p, q),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0496_g1()
