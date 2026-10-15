"""Programmatic construction for Book V, Proposition 17 (0173.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0173_g1() -> Model:
    """Construct the figure 0173.g1 (Book V, Prop. 17 subdivided magnitudes AB, CD, GO, LP)."""
    model = Model("0173.g1")

    # Top-left magnitude AB subdivided at E
    A = model.set_point(99.00, -19.00, classes=["given"], label="A")
    E = model.set_point(179.00, -19.00, classes=["given"], label="E")
    B = model.set_point(223.00, -19.00, classes=["given"], label="B")
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_section([A, E, B])

    # Top-right magnitude CD subdivided at F
    C = model.set_point(312.00, -19.00, classes=["given"], label="C")
    F = model.set_point(358.00, -19.00, classes=["given"], label="F")
    D = model.set_point(383.00, -19.00, classes=["given"], label="D")
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_section([C, F, D])

    # Middle magnitude GO subdivided at H and K
    G = model.set_point(16.00, -76.00, label="G")
    H = model.set_point(168.00, -76.00, label="H")
    K = model.set_point(258.00, -76.00, label="K")
    O = model.set_point(393.00, -76.00, label="O")
    model.set_segment(G, O)
    model.set_segment(G, K)
    model.set_segment(H, O)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, O)
    model.set_section([G, H, K])
    model.set_section([H, K, O])

    # Bottom magnitude LP subdivided at M and N
    L = model.set_point(18.00, -105.00, label="L")
    M = model.set_point(108.00, -105.00, label="M")
    N = model.set_point(164.00, -105.00, label="N")
    P = model.set_point(254.00, -105.00, label="P")
    model.set_segment(L, P)
    model.set_segment(L, N)
    model.set_segment(M, P)
    model.set_segment(L, M)
    model.set_segment(M, N)
    model.set_segment(N, P)
    model.set_section([L, M, N])
    model.set_section([M, N, P])

    return model


if __name__ == "__main__":
    construct_0173_g1()
