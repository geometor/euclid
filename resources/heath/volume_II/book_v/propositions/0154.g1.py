"""Programmatic construction for Book V, Proposition 7 (0154.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0154_g1() -> Model:
    """Construct the figure 0154.g1 for Book V, Proposition 7 using geometor.model."""
    model = Model("0154.g1")

    # Left column magnitudes: A, B, C
    A_1 = model.set_point(28.0, -18.0, classes=["given"], label="A_1")
    A_2 = model.set_point(72.0, -18.0, classes=["given"], label="A_2")
    B_1 = model.set_point(28.0, -45.0, classes=["given"], label="B_1")
    B_2 = model.set_point(72.0, -45.0, classes=["given"], label="B_2")
    C_1 = model.set_point(28.0, -74.0, classes=["given"], label="C_1")
    C_2 = model.set_point(84.0, -74.0, classes=["given"], label="C_2")

    # Right column multiples: D, E, F
    D_1 = model.set_point(127.0, -18.0, label="D_1")
    D_2 = model.set_point(169.0, -18.0, label="D_2")
    D_3 = model.set_point(211.0, -18.0, label="D_3")
    D_4 = model.set_point(254.0, -18.0, label="D_4")
    D_5 = model.set_point(296.0, -18.0, label="D_5")

    E_1 = model.set_point(127.0, -45.0, label="E_1")
    E_2 = model.set_point(169.0, -45.0, label="E_2")
    E_3 = model.set_point(211.0, -45.0, label="E_3")
    E_4 = model.set_point(254.0, -45.0, label="E_4")
    E_5 = model.set_point(296.0, -45.0, label="E_5")

    F_1 = model.set_point(127.0, -74.0, label="F_1")
    F_2 = model.set_point(183.0, -74.0, label="F_2")
    F_3 = model.set_point(238.0, -74.0, label="F_3")
    F_4 = model.set_point(294.0, -74.0, label="F_4")

    # Segments for standalone magnitudes A, B, C, D, E, F
    model.set_segment(A_1, A_2)
    model.set_segment(B_1, B_2)
    model.set_segment(C_1, C_2)
    model.set_segment(D_1, D_5)
    model.set_segment(E_1, E_5)
    model.set_segment(F_1, F_4)

    return model


if __name__ == "__main__":
    construct_0154_g1()
