"""Programmatic construction for Book X, Proposition 14 (0041.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0041_g1() -> Model:
    """Construct the figure 0041.g1 using geometor.model."""
    model = Model("0041.g1")

    # Vertical straight lines A, B, E, C, D, F
    A_t = model.set_point(19.5, -12.0, classes=["given"], label="A")
    A_b = model.set_point(19.5, -175.0, label="A_b")

    B_t = model.set_point(44.5, -33.0, classes=["given"], label="B")
    B_b = model.set_point(44.5, -175.0, label="B_b")

    E_t = model.set_point(78.5, -16.0, label="E")
    E_b = model.set_point(78.5, -98.0, label="E_b")

    C_t = model.set_point(103.5, -34.0, classes=["given"], label="C")
    C_b = model.set_point(103.5, -172.0, label="C_b")

    D_t = model.set_point(130.5, -58.0, classes=["given"], label="D")
    D_b = model.set_point(130.5, -178.0, label="D_b")

    F_t = model.set_point(153.5, -18.0, label="F")
    F_b = model.set_point(153.5, -91.0, label="F_b")

    for p_t, p_b in [
        (A_t, A_b),
        (B_t, B_b),
        (E_t, E_b),
        (C_t, C_b),
        (D_t, D_b),
        (F_t, F_b),
    ]:
        model.construct_line(p_t, p_b)
        model.set_segment(p_t, p_b)

    return model


if __name__ == "__main__":
    construct_0041_g1()
