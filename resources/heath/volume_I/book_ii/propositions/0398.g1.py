"""Programmatic construction for Book II, Proposition 5 Simson Quadratic Solution (0398.g1).

Constructs Simson's geometrical solution of ax - x^2 = b^2 based on II. 5:
CO perpendicular to AB and equal to b, OC produced to N with ON = CB, and a
circle with centre O and radius ON cutting CB at D and AC at (E).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0398_g1() -> Model:
    """Construct Simson's quadratic equation figure on folio 0398."""
    model = Model("0398.g1")

    # Line AB bisected at C, with circle intersections D on CB and E on AC
    A = model.set_point(18.5, -39.5, classes=["given"], label="A")
    E = model.set_point(70.5, -39.5, label="E")
    C = model.set_point(115.5, -39.5, classes=["given"], label="C")
    D = model.set_point(160.5, -39.5, label="D")
    B = model.set_point(212.5, -39.5, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(C, D)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(E, C)
    model.set_segment(E, D)

    # Perpendicular CO to AB, produced to N above C so ON = CB, and circle (O, N)
    O = model.set_point(115.5, -125.0, label="O")
    N = model.set_point(115.5, -28.0, label="N")
    model.construct_line(N, O)
    model.set_segment(N, O)
    model.set_segment(N, C)
    model.set_segment(C, O)

    model.construct_circle(O, N)
    model.set_segment(O, D)
    model.set_polygon([O, C, D])

    # Square on CB (C, P, Q, B) and rectangle AH (A, D, H, K)
    K = model.set_point(18.5, -91.5, label="K")
    L = model.set_point(115.5, -91.5, label="L")
    H = model.set_point(160.5, -91.5, label="H")
    M = model.set_point(212.5, -91.5, label="M")
    P = model.set_point(115.5, -136.5, label="P")
    G = model.set_point(160.5, -136.5, label="G")
    Q = model.set_point(212.5, -136.5, label="Q")

    model.set_segment(A, K)
    model.set_segment(K, M)
    model.set_segment(K, H)
    model.set_segment(C, P)
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(B, Q)
    model.set_segment(P, Q)
    model.set_segment(B, P)

    model.set_polygon([A, D, H, K])
    model.set_polygon([C, P, Q, B])
    model.set_polygon([D, B, M, H])
    model.set_polygon([L, H, G, P])

    return model


if __name__ == "__main__":
    construct_0398_g1()
