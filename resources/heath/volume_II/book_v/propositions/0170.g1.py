"""Programmatic construction for Book V, Proposition 16 (0170.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0170_g1() -> Model:
    """Construct the figure 0170.g1 (Book V, Prop. 16 magnitudes A, B, C, D and equimultiples E, F, G, H)."""
    model = Model("0170.g1")

    # Left column magnitudes: A, B, E (3A), F (3B)
    A1 = model.set_point(27.00, -18.00, classes=["given"], label="A")
    A2 = model.set_point(104.00, -18.00, classes=["given"], label="A2")
    model.set_segment(A1, A2)

    B1 = model.set_point(27.00, -45.00, classes=["given"], label="B")
    B2 = model.set_point(71.00, -45.00, classes=["given"], label="B2")
    model.set_segment(B1, B2)

    E1 = model.set_point(27.00, -72.00, classes=["given"], label="E")
    E2 = model.set_point(103.00, -72.00, label="E2")
    E3 = model.set_point(180.00, -72.00, label="E3")
    E4 = model.set_point(256.00, -72.00, classes=["given"], label="E4")
    model.set_segment(E1, E4)

    F1 = model.set_point(27.00, -99.00, classes=["given"], label="F")
    F2 = model.set_point(71.00, -99.00, label="F2")
    F3 = model.set_point(114.00, -99.00, label="F3")
    F4 = model.set_point(158.00, -99.00, classes=["given"], label="F4")
    model.set_segment(F1, F4)

    # Right column magnitudes: C, D, G (2C), H (2D)
    C1 = model.set_point(316.00, -18.00, classes=["given"], label="C")
    C2 = model.set_point(364.00, -18.00, classes=["given"], label="C2")
    model.set_segment(C1, C2)

    D1 = model.set_point(316.00, -45.00, classes=["given"], label="D")
    D2 = model.set_point(348.00, -45.00, classes=["given"], label="D2")
    model.set_segment(D1, D2)

    G1 = model.set_point(318.00, -72.00, classes=["given"], label="G")
    G2 = model.set_point(365.00, -72.00, label="G2")
    G3 = model.set_point(411.00, -72.00, classes=["given"], label="G3")
    model.set_segment(G1, G3)

    H1 = model.set_point(318.00, -99.00, classes=["given"], label="H")
    H2 = model.set_point(348.00, -99.00, label="H2")
    H3 = model.set_point(378.00, -99.00, classes=["given"], label="H3")
    model.set_segment(H1, H3)

    return model


if __name__ == "__main__":
    construct_0170_g1()
