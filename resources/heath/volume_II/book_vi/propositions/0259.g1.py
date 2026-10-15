"""Programmatic construction for Book VI, Proposition 25 (0259.g1).

To construct one and the same figure similar to a given rectilineal figure ABC
and equal to another given rectilineal figure D.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0259_g1() -> Model:
    """Construct the figure for 0259.g1 (VI.25) using geometor.model."""
    model = Model("0259.g1")

    # 1. Given triangle ABC and applied parallelograms BE (BLEC) and CM/EF (CEMF)
    A = model.set_point(26.0, -51.0, classes=["given"], label="A")
    B = model.set_point(47.0, -125.0, classes=["given"], label="B")
    C = model.set_point(119.0, -125.0, classes=["given"], label="C")
    F = model.set_point(199.0, -125.0, label="F")

    L = model.set_point(36.0, -164.0, label="L")
    E = model.set_point(108.0, -164.0, label="E")
    M = model.set_point(188.0, -164.0, label="M")

    model.construct_line(B, F)
    model.construct_line(L, M)

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, F)
    model.set_segment(B, F)

    model.set_segment(L, E)
    model.set_segment(E, M)
    model.set_segment(L, M)

    model.set_segment(B, L)
    model.set_segment(C, E)
    model.set_segment(F, M)

    model.set_section([B, C, F])
    model.set_section([L, E, M])

    model.set_polygon([A, B, C])
    model.set_polygon([B, L, E, C])
    model.set_polygon([C, E, M, F])
    model.set_polygon([B, L, M, F])

    # 2. Given rectilineal figure D
    D1 = model.set_point(156.0, -84.0, classes=["given"], label="D1")
    D2 = model.set_point(252.0, -48.0, classes=["given"], label="D2")
    D3 = model.set_point(296.0, -94.0, classes=["given"], label="D3")
    D4 = model.set_point(221.0, -110.0, classes=["given"], label="D4")
    model.set_segment(D1, D2)
    model.set_segment(D2, D3)
    model.set_segment(D3, D4)
    model.set_segment(D4, D1)
    model.set_polygon([D1, D2, D3, D4])

    # 3. Constructed similar triangle KGH on mean proportional GH
    K = model.set_point(356.0, -56.0, label="K")
    G = model.set_point(385.0, -162.0, label="G")
    H = model.set_point(490.0, -162.0, label="H")
    model.set_segment(K, G)
    model.set_segment(K, H)
    model.set_segment(G, H)
    model.set_polygon([K, G, H])

    # 4. Angles FCE and CBL
    model.set_wedge(C, F, F, E)  # < F C E )
    model.set_wedge(B, C, C, L)  # < C B L )

    return model


if __name__ == "__main__":
    construct_0259_g1()
