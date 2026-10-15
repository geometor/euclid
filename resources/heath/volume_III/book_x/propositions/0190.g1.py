"""Programmatic construction for Book X, Proposition 89 (0190.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0190_g1() -> Model:
    """Construct the figure 0190.g1 using geometor.model."""
    model = Model("0190.g1")

    # Vertical single-letter magnitude segments A and H
    A_t = model.set_point(27.0, -19.0, classes=["given"], label="A")
    A_b = model.set_point(27.0, -154.0, label="A_b")

    H_t = model.set_point(60.0, -57.0, classes=["given"], label="H")
    H_b = model.set_point(60.0, -169.0, label="H_b")

    # Vertical line BG divided at C
    B = model.set_point(104.0, -20.0, classes=["given"], label="B")
    C = model.set_point(104.0, -88.0, classes=["given"], label="C")
    G = model.set_point(104.0, -147.0, classes=["given"], label="G")

    # Vertical number line DE divided at F
    D = model.set_point(130.0, -14.0, classes=["given"], label="D")
    F = model.set_point(130.0, -146.0, classes=["given"], label="F")
    E = model.set_point(130.0, -199.0, classes=["given"], label="E")

    # Base lines
    model.construct_line(A_t, A_b)
    model.construct_line(H_t, H_b)
    model.construct_line(B, G)
    model.construct_line(D, E)

    # Segments
    model.set_segment(A_t, A_b)
    model.set_segment(H_t, H_b)
    model.set_segment(B, G)
    model.set_segment(B, C)
    model.set_segment(C, G)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(F, E)

    # Collinear sections
    model.set_section([B, C, G])
    model.set_section([D, F, E])

    return model


if __name__ == "__main__":
    construct_0190_g1()
