"""Programmatic construction for Book I, Postulate 5 Commentary: Nasiraddin (0222.g2).

Nasiraddin at-Tusi's first lemma: perpendiculars EF, GH, KL between AB and CD.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0222_g2() -> Model:
    """Construct the figure for 0222.g2 using geometor.model."""
    model = Model("0222.g2")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_B = model.set_point(20.0, -49.5, classes=["given"], label="B")
    pt_K = model.set_point(54.0, -43.4, classes=["given"], label="K")
    pt_G = model.set_point(78.0, -39.1, classes=["given"], label="G")
    pt_E = model.set_point(102.0, -34.8, classes=["given"], label="E")
    pt_A = model.set_point(162.0, -24.0, classes=["given"], label="A")

    pt_D = model.set_point(20.0, -96.0, classes=["given"], label="D")
    pt_L = model.set_point(54.0, -96.0, classes=["given"], label="L")
    pt_H = model.set_point(78.0, -96.0, classes=["given"], label="H")
    pt_F = model.set_point(102.0, -96.0, classes=["given"], label="F")
    pt_C = model.set_point(164.0, -96.0, classes=["given"], label="C")

    # Base Construction Lines
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_C, pt_D)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_G, pt_K)
    model.set_segment(pt_K, pt_B)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_C, pt_F)
    model.set_segment(pt_F, pt_H)
    model.set_segment(pt_H, pt_L)
    model.set_segment(pt_L, pt_D)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_G, pt_H)
    model.set_segment(pt_K, pt_L)

    return model


if __name__ == "__main__":
    construct_0222_g2()
