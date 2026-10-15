"""Programmatic construction for Book I, Proposition 48 (0382.g2).

Converse of the Pythagorean Theorem: if the square on BC equals the sum of the
squares on BA and AC, then angle BAC is right.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0382_g2() -> Model:
    """Construct Book I, Proposition 48 figure (0382.g2) using geometor.model."""
    model = Model("0382.g2")

    A = model.set_point(71.5, -147, classes=["given"], label="A")
    B = model.set_point(123, -147, classes=["given"], label="B")
    C = model.set_point(71.5, -23, classes=["given"], label="C")
    D = model.set_point(20, -147, label="D")

    # Classical construction: line AD perpendicular to AC at A, circle (A, B) giving D, join DC
    L_AC = model.construct_line(A, C)
    model.construct_perpendicular(L_AC, A)
    model.construct_circle(A, B)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, C])

    # Segments
    for p1, p2 in [(A, B), (A, C), (B, C), (A, D), (D, C)]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(A, B, B, C)  # < B A C )
    model.set_wedge(A, D, D, C)  # < D A C )

    return model


if __name__ == "__main__":
    construct_0382_g2()
