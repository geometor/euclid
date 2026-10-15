"""Programmatic construction for Book XII, Proposition 5 commentary (0393.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0393_g1() -> Model:
    """Construct the figure 0393.g1 using geometor.model."""
    model = Model("0393.g1")

    # Common vertex V
    V = model.set_point(85.0, -21.0, classes=["given"], label="V")

    # Base ABCDE and altitude foot O of first pyramid
    A = model.set_point(22.0, -177.0, classes=["given"], label="A")
    B = model.set_point(89.0, -226.0, classes=["given"], label="B")
    C = model.set_point(174.0, -159.0, classes=["given"], label="C")
    D = model.set_point(126.0, -126.0, classes=["given"], label="D")
    E = model.set_point(62.0, -126.0, classes=["given"], label="E")
    O = model.set_point(78.0, -165.0, label="O")

    # Parallel section abcde and altitude foot o (t = 0.45 from V)
    a = model.set_point(56.65, -91.2, label="a")
    b = model.set_point(86.8, -113.25, label="b")
    c = model.set_point(125.05, -83.1, label="c")
    d = model.set_point(103.45, -68.25, label="d")
    e = model.set_point(74.65, -68.25, label="e")
    o = model.set_point(81.85, -85.8, label="o")

    # Second pyramid base XYZ and parallel section xyz (t = 0.45 from V)
    X = model.set_point(224.0, -171.0, classes=["given"], label="X")
    Y = model.set_point(285.0, -207.0, classes=["given"], label="Y")
    Z = model.set_point(348.0, -171.0, classes=["given"], label="Z")
    x = model.set_point(147.55, -88.5, label="x")
    y = model.set_point(175.0, -104.7, label="y")
    z = model.set_point(203.35, -88.5, label="z")

    # Lateral edges and altitude segments of first pyramid
    for pt_sec, pt_base in [(a, A), (b, B), (c, C), (d, D), (e, E), (o, O)]:
        model.set_segment(V, pt_sec)
        model.set_segment(pt_sec, pt_base)
        model.set_segment(V, pt_base)

    # Base and section edges of first pyramid
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)
    model.set_segment(B, O)

    model.set_segment(a, b)
    model.set_segment(b, c)
    model.set_segment(c, d)
    model.set_segment(d, e)
    model.set_segment(e, a)
    model.set_segment(b, o)

    # Lateral edges and base/section edges of second pyramid
    for pt_sec, pt_base in [(x, X), (y, Y), (z, Z)]:
        model.set_segment(V, pt_sec)
        model.set_segment(pt_sec, pt_base)
        model.set_segment(V, pt_base)

    model.set_segment(X, Y)
    model.set_segment(Y, Z)
    model.set_segment(Z, X)
    model.set_segment(x, y)
    model.set_segment(y, z)
    model.set_segment(z, x)

    # Polygons and faces
    model.set_polygon([V, A, B])
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([a, b, c, d, e])
    model.set_polygon([X, Y, Z])
    model.set_polygon([x, y, z])

    return model


if __name__ == "__main__":
    construct_0393_g1()
