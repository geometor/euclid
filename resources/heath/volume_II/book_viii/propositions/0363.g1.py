"""Programmatic construction for Book VIII, Proposition 8 (0363.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0363_g1() -> Model:
    """Construct the figure 0363.g1 using geometor.model."""
    model = Model("0363.g1")

    # Left column: single-letter horizontal number segments A, C, D, B, G, H, K, L
    A_l = model.set_point(26.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(79.0, -14.0, label="A_r")

    C_l = model.set_point(27.0, -38.0, classes=["given"], label="C")
    C_r = model.set_point(96.0, -38.0, label="C_r")

    D_l = model.set_point(28.0, -64.0, classes=["given"], label="D")
    D_r = model.set_point(119.0, -64.0, label="D_r")

    B_l = model.set_point(28.0, -88.0, classes=["given"], label="B")
    B_r = model.set_point(153.0, -88.0, label="B_r")

    G_l = model.set_point(27.0, -105.0, classes=["given"], label="G")
    G_r = model.set_point(55.0, -105.0, label="G_r")

    H_l = model.set_point(27.0, -120.0, classes=["given"], label="H")
    H_r = model.set_point(63.0, -120.0, label="H_r")

    K_l = model.set_point(29.0, -138.0, classes=["given"], label="K")
    K_r = model.set_point(75.0, -138.0, label="K_r")

    L_l = model.set_point(28.0, -158.0, classes=["given"], label="L")
    L_r = model.set_point(93.0, -158.0, label="L_r")

    # Right column: single-letter horizontal number segments E, M, N, F
    E_l = model.set_point(207.0, -14.0, classes=["given"], label="E")
    E_r = model.set_point(278.0, -14.0, label="E_r")

    M_l = model.set_point(210.0, -39.0, classes=["given"], label="M")
    M_r = model.set_point(299.0, -39.0, label="M_r")

    N_l = model.set_point(208.0, -64.0, classes=["given"], label="N")
    N_r = model.set_point(333.0, -64.0, label="N_r")

    F_l = model.set_point(206.0, -88.0, classes=["given"], label="F")
    F_r = model.set_point(377.0, -88.0, label="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(B_l, B_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)
    model.set_segment(L_l, L_r)
    model.set_segment(E_l, E_r)
    model.set_segment(M_l, M_r)
    model.set_segment(N_l, N_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0363_g1()
