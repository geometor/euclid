"""Programmatic construction for Book VI, Proposition 22 Clavius Diagram (0250.g1).

Clavius's proof of the ex aequali inequality of ratios for three magnitudes A, B, C
and three magnitudes D, E, F, with auxiliary fourth proportionals G and H.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0250_g1() -> Model:
    """Construct the figure for 0250.g1 (VI.22 Clavius) using geometor.model."""
    model = Model("0250.g1")

    # Left column magnitudes: A, B, C, G, H
    A1 = model.set_point(24.0, -19.0, classes=["given"], label="A1")
    A2 = model.set_point(154.0, -19.0, classes=["given"], label="A2")
    model.set_segment(A1, A2)

    B1 = model.set_point(24.0, -40.0, classes=["given"], label="B1")
    B2 = model.set_point(105.0, -40.0, classes=["given"], label="B2")
    model.set_segment(B1, B2)

    C1 = model.set_point(24.0, -63.0, classes=["given"], label="C1")
    C2 = model.set_point(77.0, -63.0, classes=["given"], label="C2")
    model.set_segment(C1, C2)

    G1 = model.set_point(24.0, -86.0, label="G1")
    G2 = model.set_point(99.0, -86.0, label="G2")
    model.set_segment(G1, G2)

    H1 = model.set_point(24.0, -106.0, label="H1")
    H2 = model.set_point(121.0, -106.0, label="H2")
    model.set_segment(H1, H2)

    # Right column magnitudes: D, E, F
    D1 = model.set_point(233.0, -19.0, classes=["given"], label="D1")
    D2 = model.set_point(377.0, -19.0, classes=["given"], label="D2")
    model.set_segment(D1, D2)

    E1 = model.set_point(233.0, -40.0, classes=["given"], label="E1")
    E2 = model.set_point(336.0, -40.0, classes=["given"], label="E2")
    model.set_segment(E1, E2)

    F1 = model.set_point(233.0, -63.0, classes=["given"], label="F1")
    F2 = model.set_point(308.0, -63.0, classes=["given"], label="F2")
    model.set_segment(F1, F2)

    return model


if __name__ == "__main__":
    construct_0250_g1()
