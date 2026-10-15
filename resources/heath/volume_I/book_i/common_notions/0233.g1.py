"""Programmatic construction for Postulate 5 Commentary, Legendre (0233.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0233_g1() -> Model:
    """Construct the figure 0233.g1 (Lemma to Proposition VII) using geometor.model."""
    model = Model("0233.g1")

    # Points (y negated for Cartesian coordinates)
    P = model.set_point(67, -29, classes=["given"], label="P")
    Q = model.set_point(67, -101, label="Q")
    R = model.set_point(139, -101, label="R")
    R_prime = model.set_point(241, -101, label="R'")
    S = model.set_point(241, -29, label="S")

    # Construction lines
    model.construct_line(Q, R_prime)
    model.construct_line(P, S)
    model.construct_line(P, Q)
    model.construct_line(P, R)
    model.construct_line(P, R_prime)

    # Segments (including collinear sub-segments)
    model.set_segment(P, Q)
    model.set_segment(Q, R)
    model.set_segment(R, R_prime)
    model.set_segment(Q, R_prime)
    model.set_segment(P, R)
    model.set_segment(P, R_prime)

    # Collinear section
    model.set_section([Q, R, R_prime])

    # Polygons
    model.set_polygon([P, Q, R])
    model.set_polygon([P, R, R_prime])
    model.set_polygon([P, Q, R_prime])

    # Angles (wedges)
    model.set_wedge(P, Q, Q, R)
    model.set_wedge(R, P, P, Q)
    model.set_wedge(P, R, R, R_prime)
    model.set_wedge(R_prime, P, P, R)
    model.set_wedge(Q, R, R, P)

    return model


if __name__ == "__main__":
    construct_0233_g1()
