"""Programmatic construction for Book III, Proposition 31 Commentary — Liber Assumptorum (0071.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0071_g1() -> Model:
    """Construct the figure 0071.g1 using geometor.model."""
    model = Model("0071.g1")

    # Case 1 (Left circle: center (82, -84), radius 68)
    M1 = model.set_point(82.0, -84.0, label="M1")
    A = model.set_point(29.33, -41.0, classes=["given"], label="A")
    B = model.set_point(134.67, -41.0, classes=["given"], label="B")
    C = model.set_point(63.0, -18.71, classes=["given"], label="C")
    D = model.set_point(63.0, -149.29, classes=["given"], label="D")
    O = model.set_point(63.0, -41.0, label="O")
    E = model.set_point(101.0, -149.29, label="E")

    model.construct_circle(M1, A)

    # Segments (Case 1)
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, O)
    model.set_segment(B, O)
    model.set_segment(C, O)
    model.set_segment(D, O)
    model.set_segment(C, E)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, D)
    model.set_segment(B, E)

    # Sections (Case 1)
    model.set_section([A, O, B])
    model.set_section([C, O, D])

    # Polygons (Case 1)
    model.set_polygon([A, O, C])
    model.set_polygon([E, B, C])
    model.set_polygon([A, O, D])
    model.set_polygon([B, O, C])

    # Angles (Case 1)
    model.set_wedge(A, C, C, O)
    model.set_wedge(E, C, C, B)
    model.set_wedge(O, C, C, A)
    model.set_wedge(B, C, C, E)
    model.set_wedge(C, A, A, O)
    model.set_wedge(C, E, E, B)

    return model


if __name__ == "__main__":
    construct_0071_g1()
