"""Programmatic construction for Book X, Proposition 31 (0073.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0073_g1() -> Model:
    """Construct the figure 0073.g1 using geometor.model."""
    model = Model("0073.g1")

    # Vertical straight line segments A, B, C, D
    A_t = model.set_point(24.0, -13.0, classes=["given"], label="A")
    A_b = model.set_point(24.0, -142.0, label="A_b")

    B_t = model.set_point(54.5, -54.0, classes=["given"], label="B")
    B_b = model.set_point(54.5, -142.0, label="B_b")

    C_t = model.set_point(81.5, -33.0, label="C")
    C_b = model.set_point(81.5, -139.0, label="C_b")

    D_t = model.set_point(111.0, -74.0, label="D")
    D_b = model.set_point(111.0, -141.0, label="D_b")

    for p_t, p_b in [(A_t, A_b), (B_t, B_b), (C_t, C_b), (D_t, D_b)]:
        model.construct_line(p_t, p_b)
        model.set_segment(p_t, p_b)

    return model


if __name__ == "__main__":
    construct_0073_g1()
