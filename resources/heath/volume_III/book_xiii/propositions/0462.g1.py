"""Programmatic construction for Book XIII, Proposition 10 (0462.g1).

Regular pentagon ABCDE inscribed in circle ABCDE with centre F, diameter AG,
perpendiculars FHK to AB and FLM to AK, and chord KN.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0462_g1() -> Model:
    """Construct the figure 0462.g1 using geometor.model."""
    model = Model("0462.g1")

    cx, cy, r = 151.0, -154.0, 120.0
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

    # Diameter point G at bottom (-90 deg)
    G = model.set_point(151.0, -274.0, classes=["constructed"], label="G")

    # K bisects arc AB (126 deg), H is midpoint of AB
    K = model.set_point(80.5, -56.9, classes=["constructed"], label="K")
    H = model.set_point(93.9, -75.5, classes=["constructed"], label="H")

    # M bisects arc AK (108 deg), L is midpoint of AK, N is intersection of FM and AB
    M = model.set_point(113.9, -39.9, classes=["constructed"], label="M")
    L = model.set_point(115.7, -45.5, classes=["constructed"], label="L")
    N = model.set_point(119.5, -56.9, classes=["constructed"], label="N")

    # Polygons and triangles
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([A, B, F])
    model.set_polygon([B, F, N])
    model.set_polygon([A, K, B])
    model.set_polygon([A, K, N])

    # Segments and sub-segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, E), (E, A),
        (A, H), (H, B), (A, N), (B, N), (H, N),
        (A, G), (A, F), (F, G),
        (F, B),
        (F, K), (F, H), (H, K),
        (A, K), (K, B), (A, L), (L, K),
        (F, M), (F, L), (L, M), (F, N), (L, N),
        (K, N),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([A, F, G])
    model.set_section([A, N, B])
    model.set_section([F, H, K])
    model.set_section([A, L, K])
    model.set_section([F, N, M])

    # Angles (wedges)
    model.set_wedge(F, A, A, K)
    model.set_wedge(F, K, K, B)
    model.set_wedge(F, G, G, B)
    model.set_wedge(F, B, B, M)
    model.set_wedge(A, F, F, B)
    model.set_wedge(B, A, A, F)
    model.set_wedge(F, A, A, B)
    model.set_wedge(N, B, B, F)
    model.set_wedge(K, L, L, N)
    model.set_wedge(A, L, L, N)
    model.set_wedge(B, K, K, N)
    model.set_wedge(K, A, A, B)
    model.set_wedge(N, K, K, A)

    return model


if __name__ == "__main__":
    construct_0462_g1()
