"""Programmatic construction for Book X, Proposition 114 (0256.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0256_g1() -> Model:
    """Construct the figure 0256.g1 using geometor.model."""
    model = Model("0256.g1")

    # Line AF divided at B
    A = model.set_point(55.0, -19.0, classes=["given"], label="A")
    B = model.set_point(128.0, -19.0, classes=["given"], label="B")
    F = model.set_point(168.0, -19.0, classes=["given"], label="F")

    # Line CD divided at E
    C = model.set_point(17.0, -49.5, classes=["given"], label="C")
    E = model.set_point(164.0, -49.5, classes=["given"], label="E")
    D = model.set_point(217.0, -49.5, classes=["given"], label="D")

    # Single-letter magnitude segments G and H
    G_l = model.set_point(49.0, -81.0, classes=["given"], label="G")
    G_r = model.set_point(171.0, -81.0, label="G_r")

    H_l = model.set_point(38.0, -111.5, classes=["given"], label="H")
    H_r = model.set_point(182.0, -111.5, label="H_r")

    # Line KM divided at L
    K = model.set_point(35.0, -143.5, label="K")
    L = model.set_point(133.0, -143.5, label="L")
    M = model.set_point(185.0, -143.5, label="M")

    # Base lines
    model.construct_line(A, F)
    model.construct_line(C, D)
    model.construct_line(G_l, G_r)
    model.construct_line(H_l, H_r)
    model.construct_line(K, M)

    # Segments
    model.set_segment(A, F)
    model.set_segment(A, B)
    model.set_segment(B, F)
    model.set_segment(C, D)
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K, M)
    model.set_segment(K, L)
    model.set_segment(L, M)

    # Sections
    model.set_section([A, B, F])
    model.set_section([C, E, D])
    model.set_section([K, L, M])

    return model


if __name__ == "__main__":
    construct_0256_g1()
