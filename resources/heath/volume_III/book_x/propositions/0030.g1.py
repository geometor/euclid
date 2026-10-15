"""Programmatic construction for Book X, Proposition 6 (0030.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0030_g1() -> Model:
    """Construct the magnitude/number bars A, B, C, D, E, F for Book X, Proposition 6 (0030.g1)."""
    model = Model("0030.g1")

    # Single-letter magnitudes A, B, C, F and numbers D, E
    A_l = model.set_point(14.0, -19.0, classes=["given"], label="A")
    A_1 = model.set_point(56.0, -19.0, label="A_1")
    A_2 = model.set_point(98.0, -19.0, label="A_2")
    A_r = model.set_point(140.0, -19.0, label="A_r")

    B_l = model.set_point(193.0, -18.5, classes=["given"], label="B")
    B_r = model.set_point(270.0, -18.5, label="B_r")

    C_l = model.set_point(326.0, -18.0, label="C")
    C_r = model.set_point(370.0, -18.0, label="C_r")

    D_l = model.set_point(104.0, -43.0, classes=["given"], label="D")
    D_r = model.set_point(172.0, -43.0, label="D_r")

    E_l = model.set_point(104.0, -65.5, classes=["given"], label="E")
    E_r = model.set_point(149.0, -65.5, label="E_r")

    F_l = model.set_point(249.0, -64.5, label="F")
    F_r = model.set_point(321.0, -64.5, label="F_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    # Subdivisions of A
    model.set_section([A_l, A_1, A_2])
    model.set_section([A_1, A_2, A_r])

    return model


if __name__ == "__main__":
    construct_0030_g1()
