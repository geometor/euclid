#!/usr/bin/env python3
"""
Programmatic construction for Book XI, Proposition 39 (0367.g1)
using geometor.model.
"""
from geometor.model import Model


def build_model() -> Model:
    m = Model("0367.g1")

    # Left prism ABCDEF and completed solid AO
    B = m.set_point(26, 26, classes=["given"], label="B")
    D = m.set_point(138, 26, classes=["given"], label="D")
    O = m.set_point(154, 42, classes=["constructed"], label="O")
    B2 = m.set_point(42, 42, classes=["auxiliary"])
    A = m.set_point(26, 97, classes=["given"], label="A")
    C = m.set_point(138, 97, classes=["given"], label="C")
    F = m.set_point(154, 113, classes=["given"], label="F")
    E = m.set_point(42, 113, classes=["given"], label="E")

    # Right prism GHKLMN and completed solid GP
    M = m.set_point(275, 32, classes=["given"], label="M")
    P = m.set_point(345, 32, classes=["constructed"], label="P")
    N = m.set_point(378, 60, classes=["given"], label="N")
    L = m.set_point(308, 60, classes=["given"], label="L")
    H = m.set_point(275, 102, classes=["given"], label="H")
    H2 = m.set_point(345, 102, classes=["auxiliary"])
    K = m.set_point(378, 130, classes=["given"], label="K")
    G = m.set_point(308, 130, classes=["given"], label="G")

    # Polygons (solids, prisms, parallelograms, triangles)
    m.set_polygon([B, D, O, F, E, A])  # Solid < A O >
    m.set_polygon([B, D, F, E, A])     # Prism < A B C D E F >
    m.set_polygon([A, C, F, E])        # Parallelogram < A F >
    m.set_polygon([M, P, N, K, G, H])  # Solid < G P >
    m.set_polygon([M, N, K, G, H])     # Prism < G H K L M N >
    m.set_polygon([H, H2, K, G])       # Parallelogram < H K >
    m.set_polygon([G, H, K])           # Triangle < G H K >

    # Segments
    for p1, p2 in [
        (B, D), (D, O), (O, B2), (B2, B),
        (A, C), (C, F), (F, E), (E, A),
        (B, A), (D, C), (O, F), (B2, E),
        (B, E), (D, F),
        (M, P), (P, N), (N, L), (L, M),
        (H, H2), (H2, K), (K, G), (G, H),
        (M, H), (P, H2), (N, K), (L, G),
        (M, N), (H, K),
    ]:
        m.set_segment(p1, p2)

    return m


if __name__ == "__main__":
    model = build_model()
    print(f"Constructed {model.name} with {len(model)} elements.")
