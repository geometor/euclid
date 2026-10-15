"""Programmatic construction for Book V, Proposition 8 Case 2 (0157.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0157_g1() -> Model:
    """Construct the figure 0157.g1 for Book V, Proposition 8 (Case 2) using geometor.model."""
    model = Model("0157.g1")

    # Magnitude AB subdivided at E
    A = model.set_point(28.0, -27.0, classes=["given"], label="A")
    E = model.set_point(109.0, -27.0, label="E")
    B = model.set_point(148.0, -27.0, classes=["given"], label="B")

    # Standalone magnitude C
    C_1 = model.set_point(28.0, -52.0, classes=["given"], label="C_1")
    C_2 = model.set_point(69.0, -52.0, classes=["given"], label="C_2")

    # Magnitude FH subdivided at G (with intermediate multiple marks F_1, G_1)
    F = model.set_point(28.0, -75.0, label="F")
    F_1 = model.set_point(109.0, -75.0, label="F_1")
    G = model.set_point(192.0, -75.0, label="G")
    G_1 = model.set_point(233.0, -75.0, label="G_1")
    H = model.set_point(274.0, -75.0, label="H")

    # Standalone magnitudes K, D, L, M, N
    K_1 = model.set_point(28.0, -99.0, label="K_1")
    K_2 = model.set_point(110.0, -99.0, label="K_2")
    D_1 = model.set_point(28.0, -122.0, classes=["given"], label="D_1")
    D_2 = model.set_point(79.0, -122.0, classes=["given"], label="D_2")
    L_1 = model.set_point(28.0, -149.0, label="L_1")
    L_2 = model.set_point(128.0, -149.0, label="L_2")
    M_1 = model.set_point(28.0, -174.0, label="M_1")
    M_2 = model.set_point(180.0, -174.0, label="M_2")
    N_1 = model.set_point(28.0, -198.0, label="N_1")
    N_2 = model.set_point(228.0, -198.0, label="N_2")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(F, H)

    # Segments along AB
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    # Segments along FH
    model.set_segment(F, H)
    model.set_segment(F, G)
    model.set_segment(G, H)

    # Standalone magnitudes C, K, D, L, M, N
    model.set_segment(C_1, C_2)
    model.set_segment(K_1, K_2)
    model.set_segment(D_1, D_2)
    model.set_segment(L_1, L_2)
    model.set_segment(M_1, M_2)
    model.set_segment(N_1, N_2)

    return model


if __name__ == "__main__":
    construct_0157_g1()
