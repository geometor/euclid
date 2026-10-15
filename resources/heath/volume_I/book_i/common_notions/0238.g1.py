"""Programmatic construction for Book I, Common Notions 2-3 commentary (0238.g1).

Simplicius's proof of Pappus's axiom (e): If unequals be added to equals,
the difference between the wholes is equal to the difference between the added parts.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0238_g1() -> Model:
    """Construct the figure for 0238.g1 using geometor.model."""
    model = Model("0238.g1")

    # Left magnitude line A-B-G-E (collinear vertical points)
    A = model.set_point(27, -130, classes=["given"], label="A")
    B = model.set_point(27, -75, classes=["given"], label="B")
    G = model.set_point(27, -40, classes=["given"], label="G")
    E = model.set_point(27, -20, classes=["given"], label="E")

    # Right magnitude line C-D-F (collinear vertical points)
    C = model.set_point(60, -130, classes=["given"], label="C")
    D = model.set_point(60, -75, classes=["given"], label="D")
    F = model.set_point(60, -40, classes=["given"], label="F")

    # Base extended lines
    model.construct_line(A, E)
    model.construct_line(C, F)

    # Left line sub-segments
    model.set_segment(A, B)
    model.set_segment(B, G)
    model.set_segment(G, E)
    model.set_segment(A, G)
    model.set_segment(B, E)
    model.set_segment(A, E)

    # Left line sections
    model.set_section([A, B, G])
    model.set_section([B, G, E])
    model.set_section([A, B, E])
    model.set_section([A, G, E])

    # Right line sub-segments
    model.set_segment(C, D)
    model.set_segment(D, F)
    model.set_segment(C, F)

    # Right line section
    model.set_section([C, D, F])

    return model


if __name__ == "__main__":
    construct_0238_g1()
