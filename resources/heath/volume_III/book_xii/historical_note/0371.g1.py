"""Programmatic construction for Book XII, Historical Note (0371.g1).

Archimedes' mechanical method for the quadrature of a parabolic segment CBA.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0371_g1() -> Model:
    """Construct the figure 0371.g1 using geometor.model."""
    model = Model("0371.g1")

    # Main vertices of triangle CFA
    C = model.set_point(318.0, -22.0, classes=["given"], label="C")
    A = model.set_point(246.0, -126.0, classes=["given"], label="A")
    F = model.set_point(96.0, -126.0, classes=["given"], label="F")

    # Midpoint D of CA, midpoint E of CF, and vertex B of parabolic segment on ED
    D = model.set_point(282.0, -74.0, label="D")
    E = model.set_point(207.0, -74.0, label="E")
    B = model.set_point(244.5, -74.0, label="B")

    # Lever CH through C, B, K (midpoint of FA) to H (with CK = KH)
    K = model.set_point(171.0, -126.0, label="K")
    H = model.set_point(24.0, -230.0, label="H")

    # Centre of gravity X of triangle CFA on CK (CK = 3 XK)
    X = model.set_point(220.0, -91.33, label="X")

    # Parallel diameter MNPO at t = 0.78 along C -> FA
    M = model.set_point(144.84, -103.12, label="M")
    N = model.set_point(203.34, -103.12, label="N")
    P = model.set_point(234.52, -103.12, label="P")
    O = model.set_point(261.84, -103.12, label="O")

    # Balanced segment TG with midpoint H and length equal to PO
    T = model.set_point(10.0, -230.0, label="T")
    G = model.set_point(38.0, -230.0, label="G")

    # Construction lines
    model.construct_line(C, F)
    model.construct_line(C, A)
    model.construct_line(F, A)
    model.construct_line(E, D)
    model.construct_line(C, H)
    model.construct_line(M, O)

    # Segments along CF
    for p1, p2 in [(C, F), (C, E), (E, M), (M, F), (C, M), (E, F)]:
        model.set_segment(p1, p2)

    # Segments along CA
    for p1, p2 in [(C, A), (C, D), (D, O), (O, A), (C, O), (D, A)]:
        model.set_segment(p1, p2)

    # Segments along ED
    for p1, p2 in [(E, D), (E, B), (B, D)]:
        model.set_segment(p1, p2)

    # Segments along MO
    for p1, p2 in [(M, O), (M, N), (N, P), (P, O), (M, P), (N, O)]:
        model.set_segment(p1, p2)

    # Segments along FA
    for p1, p2 in [(F, A), (F, K), (K, A)]:
        model.set_segment(p1, p2)

    # Segments along lever CH
    for p1, p2 in [
        (C, H), (C, B), (B, X), (X, N), (N, K), (K, H),
        (C, K), (X, K), (B, K), (C, N),
    ]:
        model.set_segment(p1, p2)

    # Segments along TG and triangle ABC
    for p1, p2 in [(T, G), (T, H), (H, G), (A, B)]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([E, B, D])
    model.set_section([C, K, H])
    model.set_section([M, N, O])

    # Polygons
    model.set_polygon([C, F, A])
    model.set_polygon([A, B, C])

    return model


if __name__ == "__main__":
    construct_0371_g1()
