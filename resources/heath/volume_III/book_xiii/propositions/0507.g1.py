"""Programmatic construction for Book XIII, Proposition 18 (0507.g1).

Comparison of the sides of the five regular solids inscribed in a given sphere
with diameter AB and semicircle AEB.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0507_g1() -> Model:
    """Construct the figure 0507.g1 using geometor.model."""
    model = Model("0507.g1")

    # Given diameter AB with center C
    A = model.set_point(-1, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    C = model.set_point(0, 0, classes=["given"], label="C")

    # D divides AB such that AD = 2 DB -> D is at x = 1/3
    D = model.set_point(sp.Rational(1, 3), 0, classes=["constructed"], label="D")

    # Semicircle AEB on diameter AB with center C
    model.construct_circle(C, A)

    # CE perpendicular to AB at C -> E = (0, 1)
    E = model.set_point(0, 1, classes=["constructed"], label="E")

    # DF perpendicular to AB at D -> F = (1/3, sqrt(8)/3)
    F = model.set_point(sp.Rational(1, 3), sp.sqrt(8) / 3, classes=["constructed"], label="F")

    # AG perpendicular to AB at A, AG = AB = 2 -> G = (-1, 2)
    G = model.set_point(-1, 2, classes=["constructed"], label="G")

    # GC meets semicircle at H = (-1/sqrt(5), 2/sqrt(5))
    H = model.set_point(-1 / sp.sqrt(5), 2 / sp.sqrt(5), classes=["constructed"], label="H")

    # HK perpendicular to AB at K = (-1/sqrt(5), 0)
    K = model.set_point(-1 / sp.sqrt(5), 0, classes=["constructed"], label="K")

    # CL = CK -> L = (1/sqrt(5), 0)
    L = model.set_point(1 / sp.sqrt(5), 0, classes=["constructed"], label="L")

    # LM perpendicular to AB at L -> M = (1/sqrt(5), 2/sqrt(5))
    M = model.set_point(1 / sp.sqrt(5), 2 / sp.sqrt(5), classes=["constructed"], label="M")

    # N divides FB in extreme and mean ratio with NB as the greater segment
    phi_inv = (sp.sqrt(5) - 1) / 2
    N = model.set_point(
        B.x + phi_inv * (F.x - B.x),
        B.y + phi_inv * (F.y - B.y),
        classes=["constructed"],
        label="N",
    )

    # Base lines
    model.construct_line(A, B)
    model.construct_line(A, G)
    model.construct_line(G, C)

    # Polygons (triangles)
    model.set_polygon([A, F, B])
    model.set_polygon([A, F, D])
    model.set_polygon([F, D, B])

    # Segments along diameter AB
    for p1, p2 in [
        (A, B), (A, C), (C, B), (A, D), (D, B),
        (C, D), (C, K), (C, L), (K, L), (A, K), (L, B), (A, L),
    ]:
        model.set_segment(p1, p2)

    # Vertical and oblique segments
    for p1, p2 in [
        (C, E), (D, F), (A, G), (H, K), (L, M),
        (A, E), (E, B), (A, F), (F, B), (F, N), (N, B),
        (A, M), (M, B), (G, C), (G, H), (H, C),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0507_g1()
