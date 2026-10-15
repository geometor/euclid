"""Programmatic construction for Book X, Lemma after Prop. 21 (0054.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0054_g2() -> Model:
    """Construct the figure 0054.g2 using geometor.model."""
    model = Model("0054.g2")

    # Vertices of square DF (F, E, D, F_b) and rectangle GD (E, G, G_b, D)
    F = model.set_point(18.0, -22.5, classes=["given"], label="F")
    E = model.set_point(72.5, -22.5, classes=["given"], label="E")
    G = model.set_point(212.0, -22.5, classes=["given"], label="G")
    D = model.set_point(72.5, -76.0, label="D")
    F_b = model.set_point(18.0, -76.0, label="F_b")
    G_b = model.set_point(212.0, -76.0, label="G_b")

    # Base lines
    model.construct_line(F, G)
    model.construct_line(F_b, G_b)
    model.construct_line(F, F_b)
    model.construct_line(E, D)
    model.construct_line(G, G_b)

    # Segments
    model.set_segment(F, E)
    model.set_segment(E, G)
    model.set_segment(F, G)
    model.set_segment(E, D)
    model.set_segment(F, F_b)
    model.set_segment(G, G_b)
    model.set_segment(F_b, D)
    model.set_segment(D, G_b)
    model.set_segment(F_b, G_b)

    # Collinear section on FG
    model.set_section([F, E, G])

    # Polygons: square DF and rectangle GD
    model.set_polygon([F, E, D, F_b])
    model.set_polygon([E, G, G_b, D])
    model.set_polygon([F, G, G_b, F_b])

    return model


if __name__ == "__main__":
    construct_0054_g2()
