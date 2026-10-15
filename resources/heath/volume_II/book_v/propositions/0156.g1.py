"""Programmatic construction for Book V, Proposition 8 Case 1 (0156.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0156_g1() -> Model:
    """Construct the figure 0156.g1 for Book V, Proposition 8 (Case 1) using geometor.model."""
    model = Model("0156.g1")

    # Magnitude AB subdivided at E
    A = model.set_point(28.0, -28.0, classes=["given"], label="A")
    E = model.set_point(67.0, -28.0, label="E")
    B = model.set_point(145.0, -28.0, classes=["given"], label="B")

    # Standalone magnitude C
    C_1 = model.set_point(28.0, -52.0, classes=["given"], label="C_1")
    C_2 = model.set_point(106.0, -52.0, classes=["given"], label="C_2")

    # Magnitude FH subdivided at G (with intermediate multiple marks F_1, G_1)
    F = model.set_point(28.0, -76.0, label="F")
    F_1 = model.set_point(69.0, -76.0, label="F_1")
    G = model.set_point(109.0, -76.0, label="G")
    G_1 = model.set_point(188.0, -76.0, label="G_1")
    H = model.set_point(267.0, -76.0, label="H")

    # Standalone magnitudes K, D, L, M, N
    K_1 = model.set_point(28.0, -100.0, label="K_1")
    K_2 = model.set_point(186.0, -100.0, label="K_2")
    D_1 = model.set_point(28.0, -127.0, classes=["given"], label="D_1")
    D_2 = model.set_point(75.0, -127.0, classes=["given"], label="D_2")
    L_1 = model.set_point(28.0, -153.0, label="L_1")
    L_2 = model.set_point(122.0, -153.0, label="L_2")
    M_1 = model.set_point(28.0, -176.0, label="M_1")
    M_2 = model.set_point(170.0, -176.0, label="M_2")
    N_1 = model.set_point(28.0, -200.0, label="N_1")
    N_2 = model.set_point(218.0, -200.0, label="N_2")

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
    construct_0156_g1()
