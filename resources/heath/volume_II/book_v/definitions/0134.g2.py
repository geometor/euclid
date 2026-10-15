"""Programmatic construction for Book V, Definition 5 note (0134.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0134_g2() -> Model:
    """Construct the figure 0134.g2 using geometor.model."""
    model = Model("0134.g2")

    # Left column magnitudes: A, B, E
    A_l = model.set_point(26.0, -22.0, classes=["given"], label="A")
    A_r = model.set_point(188.0, -22.0, label="A_r")
    B_l = model.set_point(26.0, -49.0, classes=["given"], label="B")
    B_r = model.set_point(110.0, -49.0, label="B_r")
    E_l = model.set_point(26.0, -76.0, classes=["given"], label="E")
    E_r = model.set_point(194.0, -76.0, label="E_r")

    # Right column magnitudes: C, D, F
    C_l = model.set_point(328.0, -22.0, classes=["given"], label="C")
    C_r = model.set_point(439.0, -22.0, label="C_r")
    D_l = model.set_point(328.0, -49.0, classes=["given"], label="D")
    D_r = model.set_point(384.0, -49.0, label="D_r")
    F_l = model.set_point(328.0, -76.0, classes=["given"], label="F")
    F_r = model.set_point(440.0, -76.0, label="F_r")

    # Magnitude segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(E_l, E_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0134_g2()
