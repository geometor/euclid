"""Programmatic construction for Book I, Proposition 47 (0363.g1).

In right-angled triangles the square on the side subtending the right angle is
equal to the squares on the sides containing the right angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0363_g1() -> Model:
    """Construct the windmill figure for Book I, Proposition 47 using geometor.model."""
    model = Model("0363.g1")

    # 1. Right-angled triangle ABC with right angle BAC
    A = model.set_point(118, -133, classes=["given"], label="A")
    B = model.set_point(91, -186, classes=["given"], label="B")
    C = model.set_point(222, -186, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_polygon([A, B, C])

    # 2. Square BDEC described on BC [I. 46]
    D = model.set_point(91, -319, label="D")
    E = model.set_point(222, -319, label="E")
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(C, E)
    model.set_polygon([B, D, E, C])

    # 3. Square BAGF (GB) described on BA [I. 46]
    F = model.set_point(38, -159, label="F")
    G = model.set_point(65, -106, label="G")
    model.set_segment(B, F)
    model.set_segment(F, G)
    model.set_segment(G, A)
    model.set_polygon([B, A, G, F])

    # 4. Square ACKH (HC) described on AC [I. 46]
    H = model.set_point(171, -29, label="H")
    K = model.set_point(275, -82, label="K")
    model.set_segment(A, H)
    model.set_segment(H, K)
    model.set_segment(C, K)
    model.set_polygon([A, C, K, H])

    # 5. Parallel AL through A to BD or CE, meeting BC at M and DE at L [I. 31]
    M = model.set_point(118, -186, label="M")
    L = model.set_point(118, -319, label="L")
    model.construct_line(A, L)
    model.set_segment(A, L)
    model.set_segment(A, M)
    model.set_segment(M, L)
    model.set_segment(B, M)
    model.set_segment(M, C)
    model.set_segment(D, L)
    model.set_segment(L, E)

    # Split rectangles BL (BDLM) and CL (CELM)
    model.set_polygon([B, D, L, M])
    model.set_polygon([C, E, L, M])

    # Collinear extensions CA-AG and BA-AH [I. 14]
    model.construct_line(C, A)
    model.construct_line(B, A)
    model.set_segment(G, C)
    model.set_segment(B, H)

    # 6. Auxiliary transversals AD, FC, AE, BK and triangles ABD, FBC, ACE, KCB
    model.set_segment(A, D)
    model.set_segment(F, C)
    model.set_segment(A, E)
    model.set_segment(B, K)
    model.set_polygon([A, B, D])
    model.set_polygon([F, B, C])
    model.set_polygon([A, C, E])
    model.set_polygon([K, C, B])

    # 7. Referenced angles (wedges)
    model.set_wedge(A, B, B, C)  # < B A C )
    model.set_wedge(A, B, B, G)  # < B A G )
    model.set_wedge(B, D, D, C)  # < D B C )
    model.set_wedge(B, F, F, A)  # < F B A )
    model.set_wedge(B, A, A, C)  # < A B C )
    model.set_wedge(B, D, D, A)  # < D B A ) / < A B D )
    model.set_wedge(B, F, F, C)  # < F B C )

    return model


if __name__ == "__main__":
    construct_0363_g1()
