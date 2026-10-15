"""Programmatic construction for Proposition 47 Commentary (0382.g1).

Heron's proof of the concurrency of the altitude AKL and the lines BM, MG
(and EC) in Book I, Proposition 47.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0382_g1() -> Model:
    """Construct Heron's concurrency figure (0382.g1) using geometor.model."""
    model = Model("0382.g1")

    A = model.set_point(101, -138, classes=["given"], label="A")
    B = model.set_point(65, -192, classes=["given"], label="B")
    C = model.set_point(182, -192, classes=["given"], label="C")
    K = model.set_point(101, -192, label="K")

    # Square on AB: ABEF
    F = model.set_point(47, -102, label="F")
    E = model.set_point(11, -156, label="E")

    # Square on AC: ACHG
    H = model.set_point(155, -57, label="H")
    G = model.set_point(236, -111, label="G")

    # Top rectangle FAHO and center Y
    O = model.set_point(101, -21, label="O")
    Y = model.set_point(101, -79.5, label="Y")

    # Concurrency point M (intersection of AKL, EC, and BG)
    M = model.set_point(101, -174.95, label="M")

    # Completed parallelogram FENC and auxiliary grid points S, Q, P, R, X1, X2
    N = model.set_point(146, -246, label="N")
    X1 = model.set_point(83.95, -163.58, label="X1")
    X2 = model.set_point(118.05, -149.37, label="X2")
    S = model.set_point(29.95, -127.58, label="S")
    R = model.set_point(164.95, -217.58, label="R")
    Q = model.set_point(172.05, -68.37, label="Q")
    P = model.set_point(82.05, -203.37, label="P")

    # Square on BC: BDEC' and L
    D = model.set_point(65, -309, label="D")
    L = model.set_point(101, -309, label="L")
    Cp = model.set_point(182, -309, label="C'")

    # Triangles and Parallelograms
    model.set_polygon([B, A, C])
    model.set_polygon([F, A, H])
    model.set_polygon([F, A, H, O])      # FH
    model.set_polygon([O, S, M, Q])      # SQ
    model.set_polygon([F, S, X1, A])     # AS
    model.set_polygon([A, X2, Q, H])     # AQ
    model.set_polygon([A, X1, M, X2])    # AM
    model.set_polygon([F, S, M, X2])     # FM
    model.set_polygon([X1, M, Q, H])     # MH
    model.set_polygon([F, E, N, C])      # FN
    model.set_polygon([M, P, N, R])      # MN
    model.set_polygon([B, D, Cp, C])

    # Segments
    for p1, p2 in [
        (O, L), (O, A), (A, K), (O, M),
        (F, H), (F, Y), (Y, A),
        (O, E), (O, G), (F, C), (H, B),
        (S, R), (Q, P), (E, N), (G, N),
        (E, C), (B, G), (B, M), (M, G),
        (B, C), (B, D), (C, Cp), (D, Cp),
    ]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(F, H, H, A)  # < H F A )
    model.set_wedge(B, A, A, C)  # < A B C )
    model.set_wedge(A, C, C, K)  # < C A K )
    model.set_wedge(A, O, O, F)  # < O A F )

    return model


if __name__ == "__main__":
    construct_0382_g1()
