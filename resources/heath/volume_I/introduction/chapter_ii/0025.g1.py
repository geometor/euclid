"""Programmatic construction for Archimedes On Spirals, Prop. 5 (0025.g1).

DBF is a tangent to a circle with centre K. KHF meets the circumference in H
and the tangent in F; KG is parallel to DF, and BHG meets the circle in H and
KG in G.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0025_g1() -> Model:
    """Construct the Archimedes On Spirals figure on folio 0025."""
    model = Model("0025.g1")

    # Circle with centre K and point B at top, C at right
    K = model.set_point(61.5, -69.5, classes=["given"], label="K")
    B = model.set_point(61.5, -16.5, classes=["given"], label="B")
    C = model.set_point(114.5, -69.5, label="C")
    model.construct_circle(K, B)

    # Tangent line DBF at B
    D = model.set_point(22.0, -16.5, label="D")
    F = model.set_point(114.5, -16.5, label="F")
    model.construct_line(D, F)
    model.set_segment(D, F)
    model.set_segment(D, B)
    model.set_segment(B, F)

    # Parallel KG to DF through K, with C on circle
    G = model.set_point(190.0, -69.5, label="G")
    model.construct_line(K, G)
    model.set_segment(K, G)
    model.set_segment(K, C)
    model.set_segment(C, G)

    # Secant KHF and verging line BHG meeting on the circle at H
    H = model.set_point(99.0, -32.0, label="H")
    model.construct_line(K, F)
    model.set_segment(K, F)
    model.set_segment(K, H)
    model.set_segment(H, F)

    model.construct_line(B, G)
    model.set_segment(B, G)
    model.set_segment(B, H)
    model.set_segment(H, G)

    # Circular arc BH
    model.set_wedge(K, B, B, H)

    return model


if __name__ == "__main__":
    construct_0025_g1()
