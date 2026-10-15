"""Programmatic construction for Book XI, Proposition 3 Commentary Diagram 2 (0281.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0281_g2() -> Model:
    """Construct the figure 0281.g2 using geometor.model."""
    model = Model("0281.g2")

    # Left subfigure (convergent lines of intersection meeting at O)
    O = model.set_point(4.0, -18.0, label="O")
    B = model.set_point(56.0, -18.0, classes=["given"], label="B")
    A = model.set_point(199.0, -18.0, classes=["given"], label="A")
    D = model.set_point(41.0, -58.0, classes=["given"], label="D")
    C = model.set_point(162.0, -100.0, classes=["given"], label="C")
    F = model.set_point(56.0, -99.0, classes=["given"], label="F")
    E = model.set_point(199.0, -189.0, classes=["given"], label="E")

    # Right subfigure (parallel lines of intersection)
    B2 = model.set_point(322.0, -47.0, classes=["given"], label="B'")
    A2 = model.set_point(466.0, -47.0, classes=["given"], label="A'")
    D2 = model.set_point(353.0, -83.0, classes=["given"], label="D'")
    C2 = model.set_point(496.0, -83.0, classes=["given"], label="C'")
    F2 = model.set_point(322.0, -155.0, classes=["given"], label="F'")
    E2 = model.set_point(466.0, -155.0, classes=["given"], label="E'")

    # Segments (Left subfigure)
    model.set_segment(A, B)
    model.set_segment(B, O)
    model.set_segment(C, D)
    model.set_segment(D, O)
    model.set_segment(E, F)
    model.set_segment(F, O)
    model.set_segment(B, D)
    model.set_segment(D, F)
    model.set_segment(B, F)
    model.set_segment(A, C)
    model.set_segment(C, E)
    model.set_segment(A, E)

    # Segments (Right subfigure)
    model.set_segment(A2, B2)
    model.set_segment(C2, D2)
    model.set_segment(E2, F2)
    model.set_segment(B2, D2)
    model.set_segment(D2, F2)
    model.set_segment(B2, F2)
    model.set_segment(A2, C2)
    model.set_segment(C2, E2)
    model.set_segment(A2, E2)

    # Planes (Polygons)
    model.set_polygon([A, B, D, C])
    model.set_polygon([C, D, F, E])
    model.set_polygon([A, B, F, E])
    model.set_polygon([A2, B2, D2, C2])
    model.set_polygon([C2, D2, F2, E2])
    model.set_polygon([A2, B2, F2, E2])

    return model


if __name__ == "__main__":
    construct_0281_g2()
