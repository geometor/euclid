"""Programmatic construction for Book VI, Proposition 27 Commentary (0266.g1).

Second case of Proposition 27 (F on BD produced beyond D) and symmetry reduction.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0266_g1() -> Model:
    """Construct the figure for 0266.g1 (VI.27 commentary) using geometor.model."""
    model = Model("0266.g1")

    # 1. Points
    P = model.set_point(24, -25, label="P")
    Fp1 = model.set_point(131, -25, label="Fp1")
    Q = model.set_point(187, -25, label="Q")

    G = model.set_point(35, -78, label="G")
    F = model.set_point(91, -78, label="F")
    D1 = model.set_point(117, -78, label="D1")
    Fp2 = model.set_point(142, -78, label="Fp2")
    H = model.set_point(198, -78, label="H")

    O = model.set_point(40, -101, label="O")
    F1 = model.set_point(96, -101, label="F1")
    D = model.set_point(122, -101, label="D")
    Fp3 = model.set_point(147, -101, label="Fp3")
    E = model.set_point(203, -101, label="E")

    O1 = model.set_point(45, -125, label="O1")
    F2 = model.set_point(101, -125, label="F2")
    D2 = model.set_point(127, -125, label="D2")
    Fp = model.set_point(152, -125, label="F'")
    E1 = model.set_point(208, -125, label="E1")

    A = model.set_point(56, -179, classes=["given"], label="A")
    K = model.set_point(113, -179, label="K")
    C = model.set_point(138, -179, label="C")
    Kp = model.set_point(163, -179, label="Kp")
    B = model.set_point(219, -179, classes=["given"], label="B")

    # 2. Construction Lines
    model.construct_line(A, B)
    model.construct_line(B, D)
    model.construct_line(E, D)
    model.construct_line(A, G)

    # 3. Segments
    model.set_segment(P, Fp1)
    model.set_segment(Fp1, Q)
    model.set_segment(P, Q)

    model.set_segment(G, F)
    model.set_segment(F, D1)
    model.set_segment(D1, Fp2)
    model.set_segment(Fp2, H)
    model.set_segment(G, D1)
    model.set_segment(F, H)
    model.set_segment(D1, H)
    model.set_segment(G, H)

    model.set_segment(O, F1)
    model.set_segment(F1, D)
    model.set_segment(D, Fp3)
    model.set_segment(Fp3, E)
    model.set_segment(O, D)
    model.set_segment(F1, E)
    model.set_segment(D, E)
    model.set_segment(O, E)

    model.set_segment(O1, Fp)
    model.set_segment(Fp, E1)
    model.set_segment(O1, E1)

    model.set_segment(A, K)
    model.set_segment(K, C)
    model.set_segment(C, Kp)
    model.set_segment(Kp, B)
    model.set_segment(A, C)
    model.set_segment(A, Kp)
    model.set_segment(K, B)
    model.set_segment(C, B)
    model.set_segment(A, B)

    model.set_segment(P, G)
    model.set_segment(G, O)
    model.set_segment(O, O1)
    model.set_segment(O1, A)
    model.set_segment(O, A)
    model.set_segment(G, A)
    model.set_segment(P, A)

    model.set_segment(F, F1)
    model.set_segment(F1, K)
    model.set_segment(F, K)

    model.set_segment(D1, D)
    model.set_segment(D, C)
    model.set_segment(D1, C)

    model.set_segment(Fp1, Fp)
    model.set_segment(Fp, Kp)
    model.set_segment(Fp1, Kp)

    model.set_segment(Q, H)
    model.set_segment(H, E)
    model.set_segment(E, E1)
    model.set_segment(E1, B)
    model.set_segment(E, B)
    model.set_segment(H, B)
    model.set_segment(Q, B)

    model.set_segment(P, F)
    model.set_segment(F, D)
    model.set_segment(D, Fp)
    model.set_segment(Fp, B)
    model.set_segment(F, Fp)
    model.set_segment(D, B)
    model.set_segment(F, B)
    model.set_segment(P, B)

    # 4. Collinear Sections
    model.set_section([A, K, C])
    model.set_section([A, C, B])
    model.set_section([O, D, E])
    model.set_section([P, G, A])
    model.set_section([P, F, B])
    model.set_section([F, D, B])
    model.set_section([F, D, Fp])

    # 5. Polygons (Parallelograms)
    model.set_polygon([F, K, B, H])  # FKBH / KH / FB
    model.set_polygon([G, A, K, F])  # GAKF / AF
    model.set_polygon([C, B, E, D])  # CE
    model.set_polygon([A, C, D, O])  # AD
    model.set_polygon([F1, K, C, D])  # KD
    model.set_polygon([D1, D, E, H])  # DH
    model.set_polygon([O, D, D1, G])  # DG
    model.set_polygon([G, O, F1, F])  # OF
    model.set_polygon([O, A, K, F1])  # OK
    model.set_polygon([F, F1, D, D1])  # DF
    model.set_polygon([B, A, P, Q])  # BAPQ
    model.set_polygon([Fp1, Fp, E1, Q])  # F'Q
    model.set_polygon([O1, A, Kp, Fp])  # AF'

    return model


if __name__ == "__main__":
    construct_0266_g1()
