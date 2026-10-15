"""Programmatic construction for Book VII, Proposition 34, Case 2 (0343.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0343_g1() -> Model:
    """Construct the figure 0343.g1 using geometor.model."""
    model = Model("0343.g1")

    # Given numbers A, B (not prime to one another)
    A_l = model.set_point(22.0, -23.0, classes=["given"], label="A")
    A_r = model.set_point(90.0, -23.0, label="A_r")

    B_l = model.set_point(124.0, -23.0, classes=["given"], label="B")
    B_r = model.set_point(227.0, -23.0, label="B_r")

    # Least numbers F, E in the same ratio with A, B
    F_l = model.set_point(23.0, -49.0, classes=["given"], label="F")
    F_r = model.set_point(69.0, -49.0, label="F_r")

    E_l = model.set_point(116.0, -49.0, classes=["given"], label="E")
    E_r = model.set_point(184.0, -49.0, label="E_r")

    # Product C and lesser number D
    C_l = model.set_point(23.0, -76.0, classes=["given"], label="C")
    C_r = model.set_point(165.0, -76.0, label="C_r")

    D_l = model.set_point(27.0, -99.0, classes=["given"], label="D")
    D_r = model.set_point(132.0, -99.0, label="D_r")

    # Unit counts G, H
    G_l = model.set_point(40.0, -126.0, classes=["given"], label="G")
    G_r = model.set_point(75.0, -126.0, label="G_r")

    H_l = model.set_point(123.0, -126.0, classes=["given"], label="H")
    H_r = model.set_point(147.0, -126.0, label="H_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(F_l, F_r)
    model.set_segment(E_l, E_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)

    return model


if __name__ == "__main__":
    construct_0343_g1()
