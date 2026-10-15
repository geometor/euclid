"""Programmatic construction for Book V, Proposition 12 (0165.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0165_g1() -> Model:
    """Construct the figure 0165.g1 for Book V, Proposition 12 using geometor.model."""
    model = Model("0165.g1")

    # Top rows: A, D; B, E; C, F
    A_1 = model.set_point(31.0, -23.0, classes=["given"], label="A_1")
    A_2 = model.set_point(92.0, -23.0, classes=["given"], label="A_2")
    D_1 = model.set_point(31.0, -48.0, classes=["given"], label="D_1")
    D_2 = model.set_point(75.0, -48.0, classes=["given"], label="D_2")

    B_1 = model.set_point(158.0, -23.0, classes=["given"], label="B_1")
    B_2 = model.set_point(208.0, -23.0, classes=["given"], label="B_2")
    E_1 = model.set_point(158.0, -48.0, classes=["given"], label="E_1")
    E_2 = model.set_point(195.0, -48.0, classes=["given"], label="E_2")

    C_1 = model.set_point(274.0, -23.0, classes=["given"], label="C_1")
    C_2 = model.set_point(306.0, -23.0, classes=["given"], label="C_2")
    F_1 = model.set_point(274.0, -48.0, classes=["given"], label="F_1")
    F_2 = model.set_point(298.0, -48.0, classes=["given"], label="F_2")

    # Bottom left multiples: G, H, K
    G_1 = model.set_point(30.0, -76.0, label="G_1")
    G_2 = model.set_point(156.0, -76.0, label="G_2")
    H_1 = model.set_point(30.0, -101.0, label="H_1")
    H_2 = model.set_point(135.0, -101.0, label="H_2")
    K_1 = model.set_point(30.0, -125.0, label="K_1")
    K_2 = model.set_point(92.0, -125.0, label="K_2")

    # Bottom right multiples: L, M, N
    L_1 = model.set_point(234.0, -76.0, label="L_1")
    L_2 = model.set_point(372.0, -76.0, label="L_2")
    M_1 = model.set_point(234.0, -101.0, label="M_1")
    M_2 = model.set_point(350.0, -101.0, label="M_2")
    N_1 = model.set_point(234.0, -125.0, label="N_1")
    N_2 = model.set_point(311.0, -125.0, label="N_2")

    for p1, p2 in [
        (A_1, A_2), (D_1, D_2), (B_1, B_2), (E_1, E_2),
        (C_1, C_2), (F_1, F_2), (G_1, G_2), (H_1, H_2),
        (K_1, K_2), (L_1, L_2), (M_1, M_2), (N_1, N_2),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0165_g1()
