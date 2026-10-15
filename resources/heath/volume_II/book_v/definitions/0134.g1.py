"""Programmatic construction for Book V, Definition 5 note (0134.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0134_g1() -> Model:
    """Construct the figure 0134.g1 using geometor.model."""
    model = Model("0134.g1")

    # Points on AB and CD (subdivided at K)
    A = model.set_point(30.0, -22.0, classes=["given"], label="A")
    B = model.set_point(146.0, -22.0, classes=["given"], label="B")
    C = model.set_point(30.0, -50.0, classes=["given"], label="C")
    K = model.set_point(60.0, -50.0, label="K")
    D = model.set_point(115.0, -50.0, classes=["given"], label="D")

    # Points on EF and GH (subdivided at L)
    E = model.set_point(240.0, -22.0, classes=["given"], label="E")
    F = model.set_point(402.0, -22.0, classes=["given"], label="F")
    G = model.set_point(240.0, -50.0, classes=["given"], label="G")
    L = model.set_point(279.0, -50.0, label="L")
    H = model.set_point(362.0, -50.0, classes=["given"], label="H")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(E, F)
    model.construct_line(G, H)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(C, K)
    model.set_segment(K, D)
    model.set_segment(E, F)
    model.set_segment(G, H)
    model.set_segment(G, L)
    model.set_segment(L, H)

    # Collinear sections
    model.set_section([C, K, D])
    model.set_section([G, L, H])

    return model


if __name__ == "__main__":
    construct_0134_g1()
