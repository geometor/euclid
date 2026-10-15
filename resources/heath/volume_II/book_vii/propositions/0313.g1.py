"""Programmatic construction for Book VII, Proposition 8 (0313.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0313_g1() -> Model:
    """Construct the figure 0313.g1 using geometor.model."""
    model = Model("0313.g1")

    # Top horizontal number segment CD (divided at F)
    C = model.set_point(13.0, -24.0, classes=["given"], label="C")
    F = model.set_point(157.0, -24.0, label="F")
    D = model.set_point(231.0, -24.0, classes=["given"], label="D")

    # Middle horizontal number segment GH (divided at M, K, N)
    G = model.set_point(13.0, -55.0, classes=["given"], label="G")
    M = model.set_point(65.0, -55.0, label="M")
    K = model.set_point(88.0, -55.0, label="K")
    N = model.set_point(140.0, -55.0, label="N")
    H = model.set_point(164.0, -55.0, classes=["given"], label="H")

    # Bottom horizontal number segment AB (divided at L, E)
    A = model.set_point(12.0, -81.0, classes=["given"], label="A")
    L = model.set_point(63.0, -81.0, label="L")
    E = model.set_point(115.0, -81.0, label="E")
    B = model.set_point(162.0, -81.0, classes=["given"], label="B")

    # Base lines
    model.construct_line(C, D)
    model.construct_line(G, H)
    model.construct_line(A, B)

    # Segments on CD
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Segments on GH
    model.set_segment(G, H)
    model.set_segment(G, M)
    model.set_segment(M, K)
    model.set_segment(K, N)
    model.set_segment(N, H)
    model.set_segment(G, K)
    model.set_segment(K, H)
    model.set_segment(G, N)
    model.set_segment(M, N)
    model.set_segment(M, H)

    # Segments on AB
    model.set_segment(A, B)
    model.set_segment(A, L)
    model.set_segment(L, E)
    model.set_segment(E, B)
    model.set_segment(A, E)
    model.set_segment(L, B)

    # Collinear sections
    model.set_section([C, F, D])
    model.set_section([G, K, H])
    model.set_section([G, M, K])
    model.set_section([K, N, H])
    model.set_section([A, L, E])
    model.set_section([A, E, B])

    return model


if __name__ == "__main__":
    construct_0313_g1()
