"""Programmatic construction for Book V, Proposition 23 (0187.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0187_g1() -> Model:
    """Construct the figure 0187.g1 for Book V, Proposition 23 using geometor.model."""
    model = Model("0187.g1")

    # Left group: A, D, G (triple of A), K (triple of D)
    A_1 = model.set_point(96.00, -16.00, classes=["given"], label="A_1")
    A_2 = model.set_point(161.00, -16.00, classes=["given"], label="A_2")
    D_1 = model.set_point(96.00, -36.00, classes=["given"], label="D_1")
    D_2 = model.set_point(134.00, -36.00, classes=["given"], label="D_2")
    G_1 = model.set_point(40.00, -58.00, classes=["given"], label="G_1")
    G_2 = model.set_point(232.00, -58.00, classes=["given"], label="G_2")
    K_1 = model.set_point(74.00, -86.00, classes=["given"], label="K_1")
    K_2 = model.set_point(194.00, -86.00, classes=["given"], label="K_2")

    # Middle group: B, E, H (triple of B), M (double of E)
    B_1 = model.set_point(298.00, -16.00, classes=["given"], label="B_1")
    B_2 = model.set_point(326.00, -16.00, classes=["given"], label="B_2")
    E_1 = model.set_point(298.00, -36.00, classes=["given"], label="E_1")
    E_2 = model.set_point(372.00, -36.00, classes=["given"], label="E_2")
    H_1 = model.set_point(298.00, -58.00, classes=["given"], label="H_1")
    H_2 = model.set_point(381.00, -58.00, classes=["given"], label="H_2")
    M_1 = model.set_point(262.00, -86.00, classes=["given"], label="M_1")
    M_2 = model.set_point(410.00, -86.00, classes=["given"], label="M_2")

    # Right group: C, F, L (double of C), N (double of F)
    C_1 = model.set_point(443.00, -16.00, classes=["given"], label="C_1")
    C_2 = model.set_point(496.00, -16.00, classes=["given"], label="C_2")
    F_1 = model.set_point(439.00, -36.00, classes=["given"], label="F_1")
    F_2 = model.set_point(474.00, -36.00, classes=["given"], label="F_2")
    L_1 = model.set_point(442.00, -58.00, classes=["given"], label="L_1")
    L_2 = model.set_point(550.00, -58.00, classes=["given"], label="L_2")
    N_1 = model.set_point(458.00, -86.00, classes=["given"], label="N_1")
    N_2 = model.set_point(530.00, -86.00, classes=["given"], label="N_2")

    for p1, p2 in [
        (A_1, A_2),
        (D_1, D_2),
        (G_1, G_2),
        (K_1, K_2),
        (B_1, B_2),
        (E_1, E_2),
        (H_1, H_2),
        (M_1, M_2),
        (C_1, C_2),
        (F_1, F_2),
        (L_1, L_2),
        (N_1, N_2),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0187_g1()
