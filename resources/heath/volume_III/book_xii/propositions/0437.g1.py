"""Programmatic construction for Book XII, Proposition 17 Lemma (0437.g1).

Two circles with centers O and O' circumscribing isosceles trapezoids ABCD and
A'B'C'D' (with inner homothetic trapezoid XYZW and perpendicular bisectors MO,
NO, M'P).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0437_g1() -> Model:
    """Construct the figure 0437.g1 using geometor.model."""
    model = Model("0437.g1")

    # Left circle and quadrilateral ABCD
    O = model.set_point(90.0, -87.8, classes=["given"], label="O")
    A = model.set_point(42.8, -133.5, classes=["given"], label="A")
    B = model.set_point(137.2, -133.5, classes=["given"], label="B")
    C = model.set_point(123.9, -31.5, classes=["given"], label="C")
    D = model.set_point(56.1, -31.5, classes=["given"], label="D")
    N = model.set_point(90.0, -31.5, classes=["given"], label="N")
    M = model.set_point(49.5, -82.5, classes=["given"], label="M")
    L = model.set_point(79.0, -129.0, classes=["given"], label="L")
    Mp = model.set_point(67.5, -80.2, classes=["given"], label="M'")
    P = model.set_point(90.0, -74.9, classes=["given"], label="P")

    # Right circle and quadrilaterals A'B'C'D' and XYZW
    Op = model.set_point(238.0, -89.5, classes=["given"], label="O'")
    Ap = model.set_point(196.9, -131.5, classes=["given"], label="A'")
    Bp = model.set_point(279.1, -131.5, classes=["given"], label="B'")
    Cp = model.set_point(258.8, -34.5, classes=["given"], label="C'")
    Dp = model.set_point(217.2, -34.5, classes=["given"], label="D'")

    X = model.set_point(205.1, -123.1, classes=["given"], label="X")
    Y = model.set_point(270.9, -123.1, classes=["given"], label="Y")
    Z = model.set_point(254.6, -45.5, classes=["given"], label="Z")
    W = model.set_point(221.4, -45.5, classes=["given"], label="W")

    # Circumscribed circles
    model.construct_circle(O, A)
    model.construct_circle(Op, Ap)

    # Segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (O, A), (O, B), (O, C), (O, D),
        (M, O), (N, O), (D, L), (Mp, P), (D, P),
        (Ap, Bp), (Bp, Cp), (Cp, Dp), (Dp, Ap),
        (Op, Ap), (Op, Bp), (Op, Cp), (Op, Dp),
        (X, Y), (Y, Z), (Z, W), (W, X),
    ]:
        model.set_segment(p1, p2)

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([Ap, Bp, Cp, Dp])
    model.set_polygon([X, Y, Z, W])

    # Angles about O and O'
    model.set_wedge(O, A, A, D)
    model.set_wedge(O, B, B, C)
    model.set_wedge(O, A, A, B)
    model.set_wedge(O, C, C, D)
    model.set_wedge(Op, Ap, Ap, Dp)
    model.set_wedge(Op, Bp, Bp, Cp)
    model.set_wedge(Op, Ap, Ap, Bp)
    model.set_wedge(Op, Cp, Cp, Dp)

    return model


if __name__ == "__main__":
    construct_0437_g1()
