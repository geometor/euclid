"""Programmatic construction for Book VI, Proposition 32 (0277.g1).

If two triangles ABC, DCE having two sides proportional to two sides be placed
together at one angle C so that their corresponding sides are also parallel,
the remaining sides BC, CE will be in a straight line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0277_g1() -> Model:
    """Construct the figure for 0277.g1 (VI.32) using geometor.model."""
    model = Model("0277.g1")

    # 1. Points
    A = model.set_point(105.0, -90.0, classes=["given"], label="A")
    B = model.set_point(21.0, -154.0, classes=["given"], label="B")
    C = model.set_point(91.0, -154.0, classes=["given"], label="C")
    D = model.set_point(255.0, -25.0, classes=["given"], label="D")
    E = model.set_point(228.0, -154.0, classes=["given"], label="E")

    # 2. Construction Line along BCE
    model.construct_line(B, E)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(C, E)
    model.set_segment(B, E)

    # 4. Collinear Section
    model.set_section([B, C, E])

    # 5. Polygons (Triangles ABC and DCE)
    model.set_polygon([A, B, C])
    model.set_polygon([D, C, E])

    # 6. Angles (Wedges)
    model.set_wedge(A, C, C, B)  # < B A C )
    model.set_wedge(C, A, A, D)  # < A C D )
    model.set_wedge(D, E, E, C)  # < C D E )
    model.set_wedge(B, A, A, C)  # < A B C )
    model.set_wedge(C, D, D, E)  # < D C E )
    model.set_wedge(C, A, A, E)  # < A C E )
    model.set_wedge(C, B, B, A)  # < A C B )

    return model


if __name__ == "__main__":
    construct_0277_g1()
