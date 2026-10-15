"""Programmatic construction for Book II, Proposition 6 commentary (0401.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0401_g1() -> Model:
    """Construct the figure for 0401.g1 (II.6 Hippocrates commentary) using geometor.model."""
    model = Model("0401.g1")

    # 1. Points
    A = model.set_point(68.0, -134.0, classes=["given"], label="A")
    O = model.set_point(160.0, -134.0, classes=["given"], label="O")
    C = model.set_point(206.0, -134.0, classes=["given"], label="C")
    B = model.set_point(252.0, -134.0, classes=["given"], label="B")
    D = model.set_point(206.0, -54.3, label="D")
    F = model.set_point(206.0, -107.4, label="F")
    E = model.set_point(114.0, -54.3, label="E")

    # 2. Circle / Semicircle
    model.construct_circle(O, A)

    # 3. Segments
    model.set_segment(A, O)
    model.set_segment(O, C)
    model.set_segment(C, B)
    model.set_segment(O, B)
    model.set_segment(A, C)
    model.set_segment(A, B)

    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(C, D)

    model.set_segment(B, F)
    model.set_segment(F, E)
    model.set_segment(B, E)

    model.set_segment(A, E)

    # 4. Collinear Sections
    model.set_section([A, O, B])
    model.set_section([O, C, B])
    model.set_section([A, C, B])
    model.set_section([C, F, D])
    model.set_section([B, F, E])

    # 5. Polygons (Right-angled triangles)
    model.set_polygon([B, F, C])
    model.set_polygon([B, A, E])

    return model


if __name__ == "__main__":
    construct_0401_g1()
