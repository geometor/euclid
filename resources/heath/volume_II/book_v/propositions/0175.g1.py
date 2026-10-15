"""Programmatic construction for Book V, Proposition 18 (0175.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0175_g1() -> Model:
    """Construct the figure 0175.g1 (Book V, Prop. 18 subdivided magnitudes AB and CD)."""
    model = Model("0175.g1")

    # Top magnitude AB subdivided at E
    A = model.set_point(17.00, -26.00, classes=["given"], label="A")
    E = model.set_point(94.00, -26.00, classes=["given"], label="E")
    B = model.set_point(138.00, -26.00, classes=["given"], label="B")
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_section([A, E, B])

    # Bottom magnitude CD subdivided at F and G
    C = model.set_point(17.00, -54.00, classes=["given"], label="C")
    F = model.set_point(170.00, -54.00, classes=["given"], label="F")
    G = model.set_point(191.00, -54.00, label="G")
    D = model.set_point(260.00, -54.00, classes=["given"], label="D")
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(C, G)
    model.set_segment(F, D)
    model.set_segment(G, D)
    model.set_segment(F, G)
    model.set_section([C, F, D])
    model.set_section([C, G, D])

    return model


if __name__ == "__main__":
    construct_0175_g1()
