"""Programmatic construction for Book XIII, Proposition 11 (0466.g1).

Regular pentagon ABCDE inscribed in circle ABCDE with rational diameter AG,
centre F, diameter BH meeting AC at M, AG meeting CD at L, FK = 1/4 AF,
and auxiliary line N.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0466_g1() -> Model:
    """Construct the figure 0466.g1 using geometor.model."""
    model = Model("0466.g1")

    cx, cy, r = 204.0, -152.0, 122.0
    F = model.set_point(cx, cy, classes=["given"], label="F")

    # Regular pentagon vertices A (top), B (left), C (bottom-left), D (bottom-right), E (right)
    angles_deg = [90.0, 162.0, -126.0, -54.0, 18.0]
    labels = ["A", "B", "C", "D", "E"]
    pts = {}
    for lbl, deg in zip(labels, angles_deg):
        rad = math.radians(deg)
        pts[lbl] = model.set_point(
            round(cx + r * math.cos(rad), 1),
            round(cy + r * math.sin(rad), 1),
            classes=["given"],
            label=lbl,
        )

    A, B, C, D, E = pts["A"], pts["B"], pts["C"], pts["D"], pts["E"]

    # Circle ABCDE
    model.construct_circle(F, A)

    # Diameter endpoints G (-90 deg) and H (-18 deg)
    G = model.set_point(204.0, -274.0, classes=["constructed"], label="G")
    H = model.set_point(320.0, -189.7, classes=["constructed"], label="H")

    # L (intersection of AG and CD) and M (intersection of BH and AC)
    L = model.set_point(204.0, -250.7, classes=["constructed"], label="L")
    M = model.set_point(168.1, -140.4, classes=["constructed"], label="M")

    # K on FH with FK = 1/4 AF
    K = model.set_point(233.0, -161.4, classes=["constructed"], label="K")

    # Auxiliary line N on the left
    N1 = model.set_point(24.0, -76.0, classes=["auxiliary"], label="N1")
    N2 = model.set_point(24.0, -216.0, classes=["auxiliary"], label="N2")
    model.set_segment(N1, N2)

    # Polygons and triangles
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([A, C, L])
    model.set_polygon([A, M, F])
    model.set_polygon([A, B, H])
    model.set_polygon([A, B, M])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, E), (E, A),
        (C, L), (L, D),
        (A, C), (A, M), (M, C),
        (A, G), (A, F), (F, L), (L, G), (F, G), (A, L),
        (B, H), (B, M), (M, F), (F, K), (K, H), (B, F), (B, K), (M, K), (F, H),
        (A, D), (A, H),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([A, F, G])
    model.set_section([B, F, H])
    model.set_section([A, M, C])
    model.set_section([C, L, D])

    # Angles (wedges)
    model.set_wedge(L, A, A, C)
    model.set_wedge(M, A, A, F)
    model.set_wedge(A, L, L, C)
    model.set_wedge(C, A, A, L)
    model.set_wedge(F, M, M, A)

    return model


if __name__ == "__main__":
    construct_0466_g1()
