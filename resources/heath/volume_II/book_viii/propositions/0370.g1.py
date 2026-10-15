"""Programmatic construction for Book VIII, Proposition 12 (0370.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0370_g1() -> Model:
    """Construct the figure 0370.g1 using geometor.model."""
    model = Model("0370.g1")

    # Single-letter horizontal number segments A, B, C, D, H, K, E, F, G
    A_l = model.set_point(23.0, -17.0, classes=["given"], label="A")
    A_r = model.set_point(90.0, -17.0, label="A_r")

    B_l = model.set_point(22.0, -40.0, classes=["given"], label="B")
    B_r = model.set_point(261.0, -40.0, label="B_r")

    C_l = model.set_point(63.0, -66.0, classes=["given"], label="C")
    C_r = model.set_point(86.0, -66.0, label="C_r")

    D_l = model.set_point(61.0, -90.0, classes=["given"], label="D")
    D_r = model.set_point(93.0, -90.0, label="D_r")

    H_l = model.set_point(165.0, -66.0, classes=["given"], label="H")
    H_r = model.set_point(244.0, -66.0, label="H_r")

    K_l = model.set_point(163.0, -90.0, classes=["given"], label="K")
    K_r = model.set_point(304.0, -90.0, label="K_r")

    E_l = model.set_point(327.0, -15.0, classes=["given"], label="E")
    E_r = model.set_point(364.0, -15.0, label="E_r")

    F_l = model.set_point(328.0, -39.0, classes=["given"], label="F")
    F_r = model.set_point(379.0, -39.0, label="F_r")

    G_l = model.set_point(329.0, -66.0, classes=["given"], label="G")
    G_r = model.set_point(387.0, -66.0, label="G_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)

    return model


if __name__ == "__main__":
    construct_0370_g1()
