"""Programmatic construction for Book VI, Proposition 28 Commentary (0270.g1).

Alternative solution (second root of the quadratic equation) by placing GOQP in the vertically opposite angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0270_g1() -> Model:
    """Construct the figure for 0270.g1 (VI.28 commentary) using geometor.model."""
    model = Model("0270.g1")

    # 1. Points
    Bp = model.set_point(18, -31, label="B'")
    Q1 = model.set_point(160, -31, label="Q1")
    Ap = model.set_point(180, -31, label="A'")

    B1 = model.set_point(22, -51, label="B1")
    Qp = model.set_point(43, -51, label="Q'")
    Op = model.set_point(104, -51, label="O'")
    Q2 = model.set_point(164, -51, label="Q2")
    A1 = model.set_point(184, -51, label="A1")

    G1 = model.set_point(32, -108, label="G1")
    Pp = model.set_point(53, -108, label="P'")
    G = model.set_point(114, -108, label="G")
    P = model.set_point(173, -108, label="P")
    F = model.set_point(194, -108, label="F")

    T = model.set_point(42, -165, label="T")
    Pp1 = model.set_point(64, -165, label="Pp1")
    O = model.set_point(124, -165, label="O")
    Q = model.set_point(183, -165, label="Q")
    R = model.set_point(204, -165, label="R")

    A = model.set_point(46, -185, classes=["given"], label="A")
    Sp = model.set_point(68, -185, label="Sp")
    E = model.set_point(128, -185, label="E")
    S = model.set_point(187, -185, label="S")
    B = model.set_point(208, -185, classes=["given"], label="B")

    # 2. Construction Lines
    model.construct_line(A, B)
    model.construct_line(B, G)
    model.construct_line(A, T)

    # 3. Segments
    model.set_segment(Bp, Q1)
    model.set_segment(Q1, Ap)
    model.set_segment(Bp, Ap)

    model.set_segment(B1, Qp)
    model.set_segment(Qp, Op)
    model.set_segment(Op, A1)
    model.set_segment(B1, Op)
    model.set_segment(Qp, A1)
    model.set_segment(B1, A1)

    model.set_segment(G1, Pp)
    model.set_segment(Pp, G)
    model.set_segment(G, P)
    model.set_segment(P, F)
    model.set_segment(G1, G)
    model.set_segment(Pp, F)
    model.set_segment(G, F)
    model.set_segment(G1, F)

    model.set_segment(T, O)
    model.set_segment(O, Q)
    model.set_segment(Q, R)
    model.set_segment(T, Q)
    model.set_segment(O, R)
    model.set_segment(T, R)

    model.set_segment(A, Sp)
    model.set_segment(Sp, E)
    model.set_segment(E, S)
    model.set_segment(S, B)
    model.set_segment(A, E)
    model.set_segment(A, S)
    model.set_segment(E, B)
    model.set_segment(A, B)

    model.set_segment(Bp, B1)
    model.set_segment(B1, G1)
    model.set_segment(G1, T)
    model.set_segment(T, A)
    model.set_segment(B1, A)
    model.set_segment(Bp, A)

    model.set_segment(Qp, Pp)
    model.set_segment(Pp, Sp)
    model.set_segment(Qp, Sp)

    model.set_segment(Op, G)
    model.set_segment(G, O)
    model.set_segment(O, E)
    model.set_segment(G, E)
    model.set_segment(Op, O)
    model.set_segment(Op, E)

    model.set_segment(Q1, P)
    model.set_segment(P, Q)
    model.set_segment(Q, S)
    model.set_segment(P, S)
    model.set_segment(Q1, S)

    model.set_segment(Ap, A1)
    model.set_segment(A1, F)
    model.set_segment(F, R)
    model.set_segment(R, B)
    model.set_segment(F, B)
    model.set_segment(A1, B)
    model.set_segment(Ap, B)

    model.set_segment(Bp, Qp)
    model.set_segment(Qp, G)
    model.set_segment(G, Q)
    model.set_segment(Q, B)
    model.set_segment(G, B)
    model.set_segment(Qp, B)
    model.set_segment(Bp, B)

    # 4. Collinear Sections
    model.set_section([A, E, B])
    model.set_section([A, S, B])
    model.set_section([Op, G, O])
    model.set_section([G, O, E])
    model.set_section([Bp, Qp, G])
    model.set_section([Qp, G, B])
    model.set_section([G, Q, B])

    # 5. Polygons (Parallelograms)
    model.set_polygon([G, E, B, F])  # GB
    model.set_polygon([G, O, Q, P])  # GOQP / GQ
    model.set_polygon([G, Op, Qp, Pp])  # GO'Q'P' / GQ'
    model.set_polygon([A, Sp, Qp, B1])  # AQ'
    model.set_polygon([Bp, A, B, Ap])  # B'ABA'
    model.set_polygon([Q1, Q, R, Ap])  # QA'
    model.set_polygon([T, A, S, Q])  # AQ

    # 6. Angles (Wedges)
    model.set_wedge(G, F, F, E)  # FGE
    model.set_wedge(G, Pp, Pp, Op)  # P'GO' (vertically opposite to FGE)

    return model


if __name__ == "__main__":
    construct_0270_g1()
