"""Programmatic construction for Book X, Proposition 22 (0055.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0055_g1() -> Model:
    """Construct the figure 0055.g1 using geometor.model."""
    model = Model("0055.g1")

    # Medial straight line A
    A_t = model.set_point(21.5, -58.0, classes=["given"], label="A")
    A_b = model.set_point(21.5, -133.0, classes=["given"], label="A_b")

    # Rectangle BD on rational line BC with breadth CD
    B = model.set_point(72.0, -18.5, classes=["given"], label="B")
    C = model.set_point(72.0, -171.5, classes=["given"], label="C")
    D = model.set_point(109.5, -171.5, label="D")
    B_r = model.set_point(109.5, -18.5, label="B_r")

    # Rectangle GF contained by rational straight lines EG, EF
    G = model.set_point(173.5, -68.5, classes=["given"], label="G")
    E = model.set_point(173.5, -171.0, classes=["given"], label="E")
    F = model.set_point(228.5, -171.0, classes=["given"], label="F")
    G_r = model.set_point(228.5, -68.5, label="G_r")

    # Base lines
    model.construct_line(A_t, A_b)
    model.construct_line(B, C)
    model.construct_line(C, D)
    model.construct_line(D, B_r)
    model.construct_line(B, B_r)
    model.construct_line(G, E)
    model.construct_line(E, F)
    model.construct_line(F, G_r)
    model.construct_line(G, G_r)

    # Segments
    model.set_segment(A_t, A_b)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, B_r)
    model.set_segment(B, B_r)
    model.set_segment(G, E)
    model.set_segment(E, F)
    model.set_segment(F, G_r)
    model.set_segment(G, G_r)

    # Polygons: rectangles BD and GF
    model.set_polygon([B, C, D, B_r])
    model.set_polygon([G, E, F, G_r])

    return model


if __name__ == "__main__":
    construct_0055_g1()
