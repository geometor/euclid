"""Programmatic construction for Book VI, Proposition 33 (0279.g2).

In equal circles ABC, DEF, angles BGC, EHF at the centres G, H and angles BAC, EDF
at the circumferences have the same ratio as the circumferences BC, EF on which
they stand.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0279_g2() -> Model:
    """Construct the figure for 0279.g2 (VI.33) using geometor.model."""
    model = Model("0279.g2")

    # 1. Centres and circumference points of equal circles ABC and DEF (r = 70)
    G = model.set_point(96.0, -115.0, classes=["given"], label="G")
    B = model.set_point(26.0, -115.0, classes=["given"], label="B")
    O = model.set_point(32.56, -144.60, label="O")
    C = model.set_point(51.00, -168.62, classes=["given"], label="C")
    P = model.set_point(76.71, -182.29, label="P")
    K = model.set_point(105.74, -184.32, label="K")
    L = model.set_point(156.02, -151.02, label="L")
    A = model.set_point(155.26, -77.69, classes=["given"], label="A")

    H = model.set_point(271.0, -114.0, classes=["given"], label="H")
    D = model.set_point(310.02, -55.90, classes=["given"], label="D")
    E = model.set_point(212.31, -152.18, classes=["given"], label="E")
    Q = model.set_point(225.50, -167.20, label="Q")
    F = model.set_point(243.00, -178.19, classes=["given"], label="F")
    M = model.set_point(282.00, -183.13, label="M")
    N = model.set_point(320.00, -163.99, label="N")

    # 2. Equal Circles ABC and DEF
    model.construct_circle(G, B)
    model.construct_circle(H, E)

    # 3. Radii and Chords
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(G, B)
    model.set_segment(G, C)
    model.set_segment(G, K)
    model.set_segment(G, L)
    model.set_segment(B, C)
    model.set_segment(C, K)

    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(H, E)
    model.set_segment(H, F)
    model.set_segment(H, M)
    model.set_segment(H, N)

    # 4. Polygons (Triangles GBC, GCK in Theon's sector proof)
    model.set_polygon([G, B, C])
    model.set_polygon([G, C, K])

    # 5. Angles & Sectors (Wedges)
    model.set_wedge(G, B, B, C)  # < B G C )
    model.set_wedge(G, C, C, K)  # < C G K )
    model.set_wedge(G, K, K, L)  # < K G L )
    model.set_wedge(G, B, B, L)  # < B G L )
    model.set_wedge(A, B, B, C)  # < B A C )

    model.set_wedge(H, E, E, F)  # < E H F )
    model.set_wedge(H, F, F, M)  # < F H M )
    model.set_wedge(H, M, M, N)  # < M H N )
    model.set_wedge(H, E, E, N)  # < E H N )
    model.set_wedge(D, E, E, F)  # < E D F )

    return model


if __name__ == "__main__":
    construct_0279_g2()
