"""Programmatic construction for Book XI, Proposition 4 Legendre's Construction (0284.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0284_g2() -> Model:
    """Construct the figure 0284.g2 using geometor.model."""
    model = Model("0284.g2")

    # Points of angle CBD and bisected segment CD
    B = model.set_point(79.0, -32.0, classes=["given"], label="B")
    D = model.set_point(179.0, -32.0, label="D")
    D_ext = model.set_point(219.0, -32.0, classes=["ray_end"])
    K = model.set_point(57.0, -66.0, label="K")
    C = model.set_point(35.0, -100.0, label="C")
    C_ext = model.set_point(21.0, -121.64, classes=["ray_end"])
    E = model.set_point(107.0, -66.0, classes=["given"], label="E")

    # Construction lines
    model.construct_line(B, D)
    model.construct_line(B, C)
    model.construct_line(C, D)

    # Segments
    model.set_segment(B, D)
    model.set_segment(B, D_ext)
    model.set_segment(B, K)
    model.set_segment(K, C)
    model.set_segment(B, C)
    model.set_segment(B, C_ext)
    model.set_segment(E, K)
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(C, D)

    # Polygons
    model.set_polygon([B, C, D])
    model.set_polygon([C, K, E])

    # Angle CBD
    model.set_wedge(B, C, C, D)

    return model


if __name__ == "__main__":
    construct_0284_g2()
