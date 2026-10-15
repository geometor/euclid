"""Programmatic construction for Book II, Proposition 9 commentary (0408.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0408_g1() -> Model:
    """Construct the figure for 0408.g1 (II.9 & II.10 line diagram) using geometor.model."""
    model = Model("0408.g1")

    # 1. Points (Top Line: Prop. 9)
    A = model.set_point(15.0, -24.0, classes=["given"], label="A")
    C = model.set_point(120.0, -24.0, classes=["given"], label="C")
    D = model.set_point(160.0, -24.0, classes=["given"], label="D")
    B = model.set_point(225.0, -24.0, classes=["given"], label="B")

    # Bottom Line: Prop. 10
    A2 = model.set_point(80.0, -64.0, classes=["given"], label="A'")
    C2 = model.set_point(120.0, -64.0, classes=["given"], label="C'")
    B2 = model.set_point(160.0, -64.0, classes=["given"], label="B'")
    D2 = model.set_point(225.0, -64.0, classes=["given"], label="D'")

    # 2. Segments
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, B)
    model.set_segment(A, D)
    model.set_segment(C, B)
    model.set_segment(A, B)

    model.set_segment(A2, C2)
    model.set_segment(C2, B2)
    model.set_segment(B2, D2)
    model.set_segment(A2, B2)
    model.set_segment(C2, D2)
    model.set_segment(A2, D2)

    # 3. Collinear Sections
    model.set_section([A, C, D])
    model.set_section([C, D, B])
    model.set_section([A, D, B])
    model.set_section([A, C, B])

    model.set_section([A2, C2, B2])
    model.set_section([C2, B2, D2])
    model.set_section([A2, B2, D2])

    return model


if __name__ == "__main__":
    construct_0408_g1()
