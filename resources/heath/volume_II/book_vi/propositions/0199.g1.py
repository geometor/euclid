"""Programmatic construction for Book VI, Proposition 1 Commentary (0199.g1).

Legendre's proof of the extension of VI.1 to incommensurable rectangles and bases.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0199_g1() -> Model:
    """Construct the figure for 0199.g1 (VI.1 commentary) using geometor.model."""
    model = Model("0199.g1")

    # 1. Points
    A = model.set_point(18, -118, classes=["given"], label="A")
    B = model.set_point(185, -118, classes=["given"], label="B")
    C = model.set_point(185, -29, classes=["given"], label="C")
    D = model.set_point(18, -29, classes=["given"], label="D")
    E = model.set_point(114, -118, classes=["given"], label="E")
    F = model.set_point(114, -29, classes=["given"], label="F")
    I = model.set_point(122, -118, label="I")
    K = model.set_point(122, -29, label="K")
    O = model.set_point(137, -118, label="O")

    # 3. Segments
    # Top segments
    model.set_segment(D, F)
    model.set_segment(F, K)
    model.set_segment(K, C)
    model.set_segment(D, K)
    model.set_segment(D, C)

    # Bottom segments
    model.set_segment(A, E)
    model.set_segment(E, I)
    model.set_segment(I, O)
    model.set_segment(O, B)
    model.set_segment(E, O)
    model.set_segment(A, I)
    model.set_segment(A, O)
    model.set_segment(A, B)
    model.set_segment(E, B)
    model.set_segment(I, B)

    # Vertical segments
    model.set_segment(A, D)
    model.set_segment(E, F)
    model.set_segment(I, K)
    model.set_segment(B, C)

    # 4. Collinear Sections
    model.set_section([D, F, K])
    model.set_section([F, K, C])
    model.set_section([A, E, I])
    model.set_section([E, I, O])
    model.set_section([I, O, B])

    # 5. Polygons (Rectangles)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, E, F, D])
    model.set_polygon([A, I, K, D])
    model.set_polygon([E, I, K, F])
    model.set_polygon([E, B, C, F])
    model.set_polygon([I, B, C, K])

    return model


if __name__ == "__main__":
    construct_0199_g1()
