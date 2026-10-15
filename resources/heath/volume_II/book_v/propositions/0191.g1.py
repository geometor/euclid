"""Programmatic construction for Book V, Proposition 25 (0191.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0191_g1() -> Model:
    """Construct the figure 0191.g1 for Book V, Proposition 25 using geometor.model."""
    model = Model("0191.g1")

    # First subdivided magnitude AB divided at G
    A = model.set_point(20.00, -18.00, classes=["given"], label="A")
    G = model.set_point(125.00, -18.00, classes=["given"], label="G")
    B = model.set_point(179.00, -18.00, classes=["given"], label="B")

    # Standalone magnitude E
    E_1 = model.set_point(20.00, -44.00, classes=["given"], label="E_1")
    E_2 = model.set_point(124.00, -44.00, classes=["given"], label="E_2")

    # Second subdivided magnitude CD divided at H
    C = model.set_point(20.00, -70.00, classes=["given"], label="C")
    H = model.set_point(106.00, -70.00, classes=["given"], label="H")
    D = model.set_point(148.00, -70.00, classes=["given"], label="D")

    # Standalone magnitude F
    F_1 = model.set_point(20.00, -95.00, classes=["given"], label="F_1")
    F_2 = model.set_point(106.00, -95.00, classes=["given"], label="F_2")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, B)

    model.set_segment(E_1, E_2)

    model.set_segment(C, D)
    model.set_segment(C, H)
    model.set_segment(H, D)

    model.set_segment(F_1, F_2)

    # Collinear sections
    model.set_section([A, G, B])
    model.set_section([C, H, D])

    return model


if __name__ == "__main__":
    construct_0191_g1()
