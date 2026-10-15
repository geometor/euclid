"""Programmatic construction for Book II, Definition 2 Parallelogram Gnomon (0385.g2).

Constructs a parallelogram ABCD with diameter AC and point K on AC, divided by
parallels EF (horizontal) and GH (parallel to AD) through K into two
parallelograms about the diameter (AEKG, KCFH) and two complements (EBfk, GKHD),
where the shaded L-shaped gnomon consists of KCFH with the two complements.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0385_g2() -> Model:
    """Construct the parallelogram gnomon figure on folio 0385."""
    model = Model("0385.g2")

    # Outer parallelogram ABCD
    A = model.set_point(39.0, -16.0, classes=["given"], label="A")
    B = model.set_point(153.0, -16.0, classes=["given"], label="B")
    C = model.set_point(186.0, -114.0, classes=["given"], label="C")
    D = model.set_point(72.0, -114.0, label="D")

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_polygon([A, B, C, D])

    # Diameter AC and point K on AC
    K = model.set_point(148.5, -89.0, label="K")
    model.construct_line(A, C)
    model.set_segment(A, C)
    model.set_segment(A, K)
    model.set_segment(K, C)

    # Parallels through K: GKH horizontal (meeting AD at G, BC at H)
    # and EKF parallel to AD/BC (meeting AB at E, CD at F)
    E = model.set_point(124.0, -16.0, label="E")
    F = model.set_point(157.0, -114.0, label="F")
    G = model.set_point(63.6, -89.0, label="G")
    H = model.set_point(177.6, -89.0, label="H")

    model.construct_line(E, F)
    model.set_segment(E, F)
    model.set_segment(E, K)
    model.set_segment(K, F)

    model.construct_line(G, H)
    model.set_segment(G, H)
    model.set_segment(G, K)
    model.set_segment(K, H)

    # Sub-segments along outer sides
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(D, G)
    model.set_segment(G, A)

    # Parallelograms about the diameter and complements
    model.set_polygon([A, E, K, G])
    model.set_polygon([K, H, C, F])
    model.set_polygon([E, B, H, K])
    model.set_polygon([G, K, F, D])

    # L-shaped gnomon E B C D G K
    model.set_polygon([E, B, C, D, G, K])

    return model


if __name__ == "__main__":
    construct_0385_g2()
