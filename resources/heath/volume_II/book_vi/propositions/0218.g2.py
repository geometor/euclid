"""Programmatic construction for Book VI, Proposition 9, Simson's Alternative (0218.g2).

Simson's general proof of Proposition 9.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0218_g2() -> Model:
    """Construct the figure for 0218.g2 (VI.9 Simson) using geometor.model."""
    model = Model("0218.g2")

    # 1. Points
    A = model.set_point(95.0, -29.0, classes=["given"], label="A")
    B = model.set_point(49.0, -173.0, classes=["given"], label="B")
    C = model.set_point(226.0, -173.0, label="C")
    D = model.set_point(138.23, -76.52, label="D")
    E = model.set_point(79.82, -76.52, label="E")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(B, C)
    model.set_segment(D, E)

    # 3. Collinear Sections
    model.set_section([A, E, B])
    model.set_section([A, D, C])

    # 4. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, E, D])

    return model


if __name__ == "__main__":
    construct_0218_g2()
