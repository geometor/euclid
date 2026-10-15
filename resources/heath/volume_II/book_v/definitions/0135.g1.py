"""Programmatic construction for Book V, Definition 5 note (0135.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0135_g1() -> Model:
    """Construct the figure 0135.g1 using geometor.model."""
    model = Model("0135.g1")

    # Points on AB and CD (subdivided at K)
    A = model.set_point(30.0, -34.0, classes=["given"], label="A")
    B = model.set_point(132.0, -34.0, classes=["given"], label="B")
    C = model.set_point(30.0, -60.0, classes=["given"], label="C")
    K = model.set_point(52.0, -60.0, label="K")
    D = model.set_point(108.0, -60.0, classes=["given"], label="D")

    # Points on EF and GH (subdivided at L)
    E = model.set_point(236.0, -27.0, classes=["given"], label="E")
    F = model.set_point(390.0, -27.0, classes=["given"], label="F")
    G = model.set_point(236.0, -60.0, classes=["given"], label="G")
    L = model.set_point(275.0, -60.0, label="L")
    H = model.set_point(350.0, -60.0, classes=["given"], label="H")

    # Single-letter magnitude M
    M_l = model.set_point(422.0, -58.0, classes=["given"], label="M")
    M_r = model.set_point(575.0, -58.0, label="M_r")

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
    model.set_segment(M_l, M_r)

    # Collinear sections
    model.set_section([C, K, D])
    model.set_section([G, L, H])

    return model


if __name__ == "__main__":
    construct_0135_g1()
