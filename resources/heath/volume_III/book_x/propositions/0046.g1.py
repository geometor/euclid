"""Programmatic construction for Book X, Proposition 17 (0046.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0046_g1() -> Model:
    """Construct the figure 0046.g1 using geometor.model."""
    model = Model("0046.g1")

    # Straight line A (lesser given line, with midpoint tick)
    A_l = model.set_point(23.0, -23.0, classes=["given"], label="A")
    A_m = model.set_point(85.0, -23.0, label="A_m")
    A_r = model.set_point(147.0, -23.0, label="A_r")

    # Straight line BC (greater given line) with points B, F, E, D, C
    B = model.set_point(17.0, -103.0, classes=["given"], label="B")
    F = model.set_point(59.0, -103.0, label="F")
    E = model.set_point(99.0, -103.0, label="E")
    D = model.set_point(138.0, -103.0, label="D")
    C = model.set_point(184.0, -103.0, classes=["given"], label="C")

    # Dashed applied parallelogram corners above B and D
    B_t = model.set_point(17.0, -63.0, label="B_t")
    D_t = model.set_point(138.0, -63.0, label="D_t")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B, C)

    # Segment A
    model.set_segment(A_l, A_r)

    # Whole and all sub-segments on BC
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(B, F)
    model.set_segment(F, E)
    model.set_segment(E, D)
    model.set_segment(E, C)
    model.set_segment(D, F)
    model.set_segment(B, E)
    model.set_segment(F, C)

    # Collinear sections on BC
    model.set_section([B, D, C])
    model.set_section([B, E, C])
    model.set_section([F, E, D])

    # Applied parallelogram on BD
    model.set_polygon([B, D, D_t, B_t])

    return model


if __name__ == "__main__":
    construct_0046_g1()
