"""Programmatic construction for Book V, Definition 5 note (0133.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0133_g1() -> Model:
    """Construct the figure 0133.g1 using geometor.model."""
    model = Model("0133.g1")

    # Left column magnitudes: A, B, C, D
    A_l = model.set_point(26.0, -22.0, classes=["given"], label="A")
    A_r = model.set_point(152.0, -22.0, label="A_r")
    B_l = model.set_point(26.0, -45.0, classes=["given"], label="B")
    B_r = model.set_point(68.0, -45.0, label="B_r")
    C_l = model.set_point(26.0, -68.0, classes=["given"], label="C")
    C_r = model.set_point(111.0, -68.0, label="C_r")
    D_l = model.set_point(26.0, -90.0, classes=["given"], label="D")
    D_r = model.set_point(56.0, -90.0, label="D_r")

    # Right column magnitudes: E, G, F, H
    E_l = model.set_point(232.0, -22.0, classes=["given"], label="E")
    E_r = model.set_point(478.0, -22.0, label="E_r")
    G_l = model.set_point(232.0, -45.0, classes=["given"], label="G")
    G_r = model.set_point(316.0, -45.0, label="G_r")
    F_l = model.set_point(232.0, -68.0, classes=["given"], label="F")
    F_r = model.set_point(401.0, -68.0, label="F_r")
    H_l = model.set_point(232.0, -90.0, classes=["given"], label="H")
    H_r = model.set_point(289.0, -90.0, label="H_r")

    # Magnitude segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(G_l, G_r)
    model.set_segment(F_l, F_r)
    model.set_segment(H_l, H_r)

    return model


if __name__ == "__main__":
    construct_0133_g1()
