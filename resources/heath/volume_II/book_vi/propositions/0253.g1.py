"""Programmatic construction for Book VI, Proposition 23 (0253.g1).

Equiangular parallelograms have to one another the ratio compounded of the ratios
of their sides.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0253_g1() -> Model:
    """Construct the figure for 0253.g1 (VI.23) using geometor.model."""
    model = Model("0253.g1")

    # 1. Equiangular parallelograms AC (ABCD), CF (CEFG), and completed DG (DCGH)
    A = model.set_point(161.0, -28.0, classes=["given"], label="A")
    D = model.set_point(253.0, -28.0, classes=["given"], label="D")
    H = model.set_point(366.0, -28.0, label="H")

    B = model.set_point(156.0, -59.0, classes=["given"], label="B")
    C = model.set_point(248.0, -59.0, classes=["given"], label="C")
    G = model.set_point(361.0, -59.0, classes=["given"], label="G")

    E = model.set_point(240.0, -109.0, classes=["given"], label="E")
    F = model.set_point(353.0, -109.0, classes=["given"], label="F")

    # 2. Auxiliary straight lines K, L, M
    K1 = model.set_point(30.0, -65.0, label="K1")
    K2 = model.set_point(92.0, -65.0, label="K2")
    model.set_segment(K1, K2)

    L1 = model.set_point(30.0, -87.0, label="L1")
    L2 = model.set_point(105.0, -87.0, label="L2")
    model.set_segment(L1, L2)

    M1 = model.set_point(30.0, -109.0, label="M1")
    M2 = model.set_point(135.0, -109.0, label="M2")
    model.set_segment(M1, M2)

    # 3. Construction lines
    model.construct_line(B, G)
    model.construct_line(D, E)

    # 4. Segments and sub-segments
    model.set_segment(A, D)
    model.set_segment(D, H)
    model.set_segment(A, H)

    model.set_segment(B, C)
    model.set_segment(C, G)
    model.set_segment(B, G)

    model.set_segment(E, F)

    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_segment(D, E)
    model.set_segment(H, G)
    model.set_segment(G, F)
    model.set_segment(H, F)

    # 5. Collinear sections
    model.set_section([A, D, H])
    model.set_section([B, C, G])
    model.set_section([D, C, E])
    model.set_section([H, G, F])

    # 6. Parallelograms AC, CF, DG (CH)
    model.set_polygon([A, B, C, D])
    model.set_polygon([C, E, F, G])
    model.set_polygon([D, C, G, H])

    # 7. Equal vertical angles BCD and ECG
    model.set_wedge(C, B, B, D)  # < B C D )
    model.set_wedge(C, E, E, G)  # < E C G )

    return model


if __name__ == "__main__":
    construct_0253_g1()
