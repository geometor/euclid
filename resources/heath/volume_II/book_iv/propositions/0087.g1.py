"""Programmatic construction for Book IV, Proposition 1 Commentary — Apollonius's neusis (0087.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0087_g1() -> Model:
    """Construct the figure 0087.g1 using geometor.model."""
    model = Model("0087.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(94.0, -92.0, classes=["given"], label="O")
    H = model.set_point(18.81, -80.93, classes=["given"], label="H")
    K = model.set_point(129.24, -24.66, classes=["given"], label="K")
    L = model.set_point(74.02, -52.80, label="L")
    A = model.set_point(25.33, -124.57, label="A")
    B = model.set_point(147.39, -146.09, label="B")
    T = model.set_point(86.36, -135.33, label="T")
    C = model.set_point(55.85, -129.95, classes=["given"], label="C")

    # Concentric circles
    model.construct_circle(O, H)
    model.construct_circle(O, L)

    # Construction lines
    model.construct_line(H, K)
    model.construct_line(A, B)

    # Segments
    model.set_segment(H, K)
    model.set_segment(H, L)
    model.set_segment(L, K)
    model.set_segment(O, L)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Collinear sections
    model.set_section([H, L, K])
    model.set_section([A, C, B])

    return model


if __name__ == "__main__":
    construct_0087_g1()
