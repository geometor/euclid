"""Programmatic construction for Book X, Proposition 1 (0018.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0018_g1() -> Model:
    """Construct the magnitude bars AB, C, DE for Book X, Proposition 1 (0018.g1)."""
    model = Model("0018.g1")

    # Subdivided magnitude AB (divided at K and H)
    A = model.set_point(27.0, -24.0, classes=["given"], label="A")
    K = model.set_point(60.0, -24.0, label="K")
    H = model.set_point(95.0, -24.0, label="H")
    B = model.set_point(153.0, -24.0, classes=["given"], label="B")

    # Single-letter magnitude C
    C_l = model.set_point(217.0, -24.5, classes=["given"], label="C")
    C_r = model.set_point(266.0, -24.5, label="C_r")

    # Subdivided magnitude DE (divided at F and G)
    D = model.set_point(65.0, -52.5, classes=["given"], label="D")
    F = model.set_point(118.0, -52.5, label="F")
    G = model.set_point(172.0, -52.5, label="G")
    E = model.set_point(226.0, -52.5, classes=["given"], label="E")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D, E)

    # Segments on AB
    model.set_segment(A, K)
    model.set_segment(K, H)
    model.set_segment(H, B)
    model.set_segment(A, H)
    model.set_segment(K, B)
    model.set_segment(A, B)

    # Magnitude C
    model.set_segment(C_l, C_r)

    # Segments on DE
    model.set_segment(D, F)
    model.set_segment(F, G)
    model.set_segment(G, E)
    model.set_segment(D, G)
    model.set_segment(F, E)
    model.set_segment(D, E)

    # Sections
    model.set_section([A, K, H])
    model.set_section([K, H, B])
    model.set_section([A, H, B])
    model.set_section([D, F, G])
    model.set_section([F, G, E])
    model.set_section([D, G, E])

    return model


if __name__ == "__main__":
    construct_0018_g1()
