"""Programmatic construction for Proposition 47 Commentary (0369.g2).

Zeuthen / Chóu-peï 7x7 unit grid dissection showing the tilted square EFGH of
25 unit squares inside the 7x7 square ABCD.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0369_g2() -> Model:
    """Construct the Chóu-peï 7x7 grid figure (0369.g2) using geometor.model."""
    model = Model("0369.g2")

    # Outer 7x7 square ABCD (unit = 20)
    A = model.set_point(39, -34, classes=["given"], label="A")
    B = model.set_point(179, -34, classes=["given"], label="B")
    C = model.set_point(179, -174, classes=["given"], label="C")
    D = model.set_point(39, -174, classes=["given"], label="D")

    # Tilted square EFGH of side 5
    E = model.set_point(119, -34, label="E")
    F = model.set_point(179, -114, label="F")
    G = model.set_point(99, -174, label="G")
    H = model.set_point(39, -94, label="H")

    # Central unit square PQRS
    P = model.set_point(99, -94, label="P")
    Q = model.set_point(119, -94, label="Q")
    R = model.set_point(119, -114, label="R")
    S = model.set_point(99, -114, label="S")

    model.set_polygon([A, B, C, D])
    model.set_polygon([E, F, G, H])
    model.set_polygon([P, Q, R, S])
    model.set_polygon([A, E, Q, H])
    model.set_polygon([E, B, F, R])
    model.set_polygon([S, F, C, G])
    model.set_polygon([H, P, G, D])
    model.set_polygon([A, E, H])
    model.set_polygon([E, B, F])
    model.set_polygon([F, C, G])
    model.set_polygon([G, D, H])

    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (A, E), (E, B), (B, F), (F, C), (C, G), (G, D), (D, H), (H, A),
        (E, F), (F, G), (G, H), (H, E),
        (H, Q), (E, R), (F, S), (G, P),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0369_g2()
