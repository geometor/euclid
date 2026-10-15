"""Programmatic construction for Book V, Proposition 1 (0144.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0144_g1() -> Model:
    """Construct the figure 0144.g1 using geometor.model."""
    model = Model("0144.g1")

    # Points on AB (divided at G) and CD (divided at H)
    A = model.set_point(30.0, -29.0, classes=["given"], label="A")
    G = model.set_point(68.0, -29.0, label="G")
    B = model.set_point(106.0, -29.0, classes=["given"], label="B")

    C = model.set_point(196.0, -29.0, classes=["given"], label="C")
    H = model.set_point(251.0, -29.0, label="H")
    D = model.set_point(306.0, -29.0, classes=["given"], label="D")

    # Single-letter magnitudes E and F
    E_l = model.set_point(26.0, -63.0, classes=["given"], label="E")
    E_r = model.set_point(66.0, -63.0, label="E_r")
    F_l = model.set_point(194.0, -63.0, classes=["given"], label="F")
    F_r = model.set_point(249.0, -63.0, label="F_r")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_segment(C, D)
    model.set_segment(C, H)
    model.set_segment(H, D)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    # Collinear sections
    model.set_section([A, G, B])
    model.set_section([C, H, D])

    return model


if __name__ == "__main__":
    construct_0144_g1()
