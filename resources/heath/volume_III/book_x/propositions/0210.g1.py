"""Programmatic construction for Book X, Proposition 95 (0210.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0210_g1() -> Model:
    """Construct the figure 0210.g1 using geometor.model."""
    model = Model("0210.g1")

    # Top rectangle AGKC divided by vertical segments DB, EH, FI
    A = model.set_point(20.5, -19.5, classes=["given"], label="A")
    D = model.set_point(123.5, -19.5, classes=["given"], label="D")
    E = model.set_point(213.5, -19.5, label="E")
    F = model.set_point(268.5, -19.5, label="F")
    G = model.set_point(304.5, -19.5, classes=["given"], label="G")

    C = model.set_point(20.5, -100.5, classes=["given"], label="C")
    B = model.set_point(123.5, -100.5, classes=["given"], label="B")
    H = model.set_point(213.5, -100.5, label="H")
    I = model.set_point(268.5, -100.5, label="I")
    K = model.set_point(304.5, -100.5, label="K")

    # Bottom square LPMR with internal lines SO, NT, and diameter PR intersecting at Q
    L = model.set_point(97.0, -127.0, label="L")
    N = model.set_point(184.5, -127.0, label="N")
    P = model.set_point(238.5, -127.0, label="P")

    S = model.set_point(97.0, -179.0, label="S")
    Q = model.set_point(184.5, -179.0, label="Q")
    O = model.set_point(238.5, -179.0, label="O")

    R = model.set_point(97.0, -266.5, label="R")
    T = model.set_point(184.5, -266.5, label="T")
    M = model.set_point(238.5, -266.5, label="M")

    # Base lines
    for p1, p2 in [
        (A, G), (C, K), (A, C), (D, B), (E, H), (F, I), (G, K),
        (L, P), (S, O), (R, M), (L, R), (N, T), (P, M), (P, R),
    ]:
        model.construct_line(p1, p2)

    # Top and bottom collinear segments on AGKC
    for pts in ([A, D, E, F, G], [C, B, H, I, K]):
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                model.set_segment(pts[i], pts[j])

    # Vertical segments on AGKC
    for p1, p2 in [(A, C), (D, B), (E, H), (F, I), (G, K)]:
        model.set_segment(p1, p2)

    # Segments on square LPMR
    for pts in (
        [L, N, P],
        [S, Q, O],
        [R, T, M],
        [L, S, R],
        [N, Q, T],
        [P, O, M],
        [P, Q, R],
    ):
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                model.set_segment(pts[i], pts[j])

    # Collinear sections
    model.set_section([A, D, G])
    model.set_section([D, E, G])
    model.set_section([A, F, G])
    model.set_section([L, N, P])
    model.set_section([S, Q, O])
    model.set_section([R, T, M])
    model.set_section([L, S, R])
    model.set_section([N, Q, T])
    model.set_section([P, O, M])
    model.set_section([P, Q, R])

    # Polygons in AGKC
    model.set_polygon([A, G, K, C])  # AK
    model.set_polygon([A, D, B, C])  # AB
    model.set_polygon([D, G, K, B])  # DK
    model.set_polygon([A, F, I, C])  # AI
    model.set_polygon([F, G, K, I])  # FK / KF
    model.set_polygon([D, E, H, B])  # DH
    model.set_polygon([E, G, K, H])  # EK
    model.set_polygon([E, F, I, H])  # EI
    model.set_polygon([A, E, H, C])  # AH
    model.set_polygon([D, F, I, B])  # DI

    # Polygons and Gnomon in LPMR
    model.set_polygon([L, P, M, R])  # LM
    model.set_polygon([N, P, O, Q])  # NO
    model.set_polygon([S, Q, T, R])  # ST / TS
    model.set_polygon([L, P, O, S])  # LO
    model.set_polygon([N, P, M, T])  # MN
    model.set_polygon([L, N, Q, S])  # LQ
    model.set_polygon([Q, O, M, T])  # QM
    model.set_polygon([L, N, T, R])  # LT
    model.set_polygon([S, O, M, R])  # SM
    model.set_polygon([L, N, Q, O, M, R])  # Gnomon UVW

    # Common angle LPM
    model.set_wedge(P, L, L, M)

    return model


if __name__ == "__main__":
    construct_0210_g1()
