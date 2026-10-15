"""Programmatic construction for Book XII, Proposition 5 commentary (0394.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0394_g1() -> Model:
    """Construct the figure 0394.g1 using geometor.model."""
    model = Model("0394.g1")

    # Common altitude TA with point X
    T = model.set_point(66.0, -22.0, classes=["given"], label="T")
    X = model.set_point(68.0, -174.0, label="X")
    A = model.set_point(69.0, -220.0, classes=["given"], label="A")

    # First pyramid VABC
    V = model.set_point(196.0, -22.0, classes=["given"], label="V")
    B = model.set_point(169.0, -304.0, classes=["given"], label="B")
    C = model.set_point(248.0, -212.0, classes=["given"], label="C")

    # Sections of VABC at s = 0.2, 0.4, 0.6, 0.8 from ABC to V
    D = model.set_point(94.4, -180.4, label="D")
    E = model.set_point(174.4, -247.6, label="E")
    F = model.set_point(237.6, -174.0, label="F")

    G = model.set_point(119.8, -140.8, label="G")
    H = model.set_point(179.8, -191.2, label="H")
    I = model.set_point(227.2, -136.0, label="I")

    K = model.set_point(145.2, -101.2, label="K")
    L = model.set_point(185.2, -134.8, label="L")
    M = model.set_point(216.8, -98.0, label="M")

    N = model.set_point(170.6, -61.6, label="N")
    O = model.set_point(190.6, -78.4, label="O")
    P = model.set_point(206.4, -60.0, label="P")

    # Second pyramid vabc
    v = model.set_point(401.0, -26.0, classes=["given"], label="v")
    a = model.set_point(344.0, -220.0, classes=["given"], label="a")
    b = model.set_point(480.0, -294.0, classes=["given"], label="b")
    c = model.set_point(541.0, -220.0, classes=["given"], label="c")

    # Sections of vabc at s = 0.2, 0.4, 0.6, 0.8 from abc to v
    d = model.set_point(355.4, -181.2, label="d")
    e = model.set_point(464.2, -240.4, label="e")
    f = model.set_point(513.0, -181.2, label="f")

    g = model.set_point(366.8, -142.4, label="g")
    h = model.set_point(448.4, -186.8, label="h")
    i = model.set_point(485.0, -142.4, label="i")

    k = model.set_point(378.2, -103.6, label="k")
    l = model.set_point(432.6, -133.2, label="l")
    m = model.set_point(457.0, -103.6, label="m")

    n = model.set_point(389.6, -64.8, label="n")
    o = model.set_point(416.8, -79.6, label="o")
    p = model.set_point(429.0, -64.8, label="p")

    # Altitude segments
    model.set_segment(T, A)
    model.set_segment(A, X)
    model.set_segment(X, T)

    # First pyramid edges and sub-segments
    model.set_segment(A, V)
    model.set_segment(B, V)
    model.set_segment(C, V)
    for p1, p2 in [(A, D), (D, G), (G, K), (K, N), (N, V)]:
        model.set_segment(p1, p2)

    for tri in [(A, B, C), (D, E, F), (G, H, I), (K, L, M), (N, O, P)]:
        model.set_segment(tri[0], tri[1])
        model.set_segment(tri[1], tri[2])
        model.set_segment(tri[2], tri[0])
        model.set_polygon(list(tri))

    # Second pyramid edges and sub-segments
    model.set_segment(a, v)
    model.set_segment(b, v)
    model.set_segment(c, v)
    for p1, p2 in [(a, d), (d, g), (g, k), (k, n), (n, v)]:
        model.set_segment(p1, p2)

    for tri in [(a, b, c), (d, e, f), (g, h, i), (k, l, m), (n, o, p)]:
        model.set_segment(tri[0], tri[1])
        model.set_segment(tri[1], tri[2])
        model.set_segment(tri[2], tri[0])
        model.set_polygon(list(tri))

    return model


if __name__ == "__main__":
    construct_0394_g1()
