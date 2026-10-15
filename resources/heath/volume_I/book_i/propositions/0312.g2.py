"""Programmatic construction for Book I, Proposition 24 (0312.g2).

Modern Alternative Proof of Book I, Proposition 24 (Both Cases).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0312_g2() -> Model:
    """Construct the figure for 0312.g2 (I.24) using geometor.model."""
    model = Model("0312.g2")

    # Points
    pt_A1 = model.set_point(37, -25, classes=["given"], label="A")
    pt_B1 = model.set_point(11, -120, classes=["given"], label="B")
    pt_C1 = model.set_point(124, -120, classes=["given"], label="C")
    pt_D1 = model.set_point(182, -22, classes=["given"], label="D")
    pt_E1 = model.set_point(150, -119, classes=["given"], label="E")
    pt_G1 = model.set_point(278, -119, classes=["given"], label="G")
    pt_H1 = model.set_point(242, -119, classes=["given"], label="H")
    pt_F1 = model.set_point(223.5, -149, classes=["given"], label="F")
    pt_A2 = model.set_point(412, -23, classes=["given"], label="A")
    pt_B2 = model.set_point(318, -120, classes=["given"], label="B")
    pt_C2 = model.set_point(435, -120, classes=["given"], label="C")
    pt_D2 = model.set_point(573, -25, classes=["given"], label="D")
    pt_E2 = model.set_point(483, -120, classes=["given"], label="E")
    pt_G2 = model.set_point(595, -120, classes=["given"], label="G")
    pt_H2 = model.set_point(561, -120, classes=["given"], label="H")
    pt_F2 = model.set_point(522, -102, classes=["given"], label="F")

    # Segments
    model.set_segment(pt_A1, pt_B1)
    model.set_segment(pt_A1, pt_C1)
    model.set_segment(pt_B1, pt_C1)
    model.set_segment(pt_D1, pt_E1)
    model.set_segment(pt_D1, pt_G1)
    model.set_segment(pt_E1, pt_G1)
    model.set_segment(pt_E1, pt_H1)
    model.set_segment(pt_H1, pt_G1)
    model.set_segment(pt_D1, pt_F1)
    model.set_segment(pt_E1, pt_F1)
    model.set_segment(pt_D1, pt_H1)
    model.set_segment(pt_H1, pt_F1)
    model.set_segment(pt_A2, pt_B2)
    model.set_segment(pt_A2, pt_C2)
    model.set_segment(pt_B2, pt_C2)
    model.set_segment(pt_D2, pt_E2)
    model.set_segment(pt_D2, pt_G2)
    model.set_segment(pt_E2, pt_G2)
    model.set_segment(pt_E2, pt_H2)
    model.set_segment(pt_H2, pt_G2)
    model.set_segment(pt_D2, pt_F2)
    model.set_segment(pt_E2, pt_F2)
    model.set_segment(pt_D2, pt_H2)
    model.set_segment(pt_H2, pt_F2)

    # Polygons
    model.set_polygon([pt_A1, pt_B1, pt_C1])
    model.set_polygon([pt_D1, pt_E1, pt_G1])
    model.set_polygon([pt_D1, pt_E1, pt_F1])
    model.set_polygon([pt_F1, pt_D1, pt_H1])
    model.set_polygon([pt_G1, pt_D1, pt_H1])
    model.set_polygon([pt_A2, pt_B2, pt_C2])
    model.set_polygon([pt_D2, pt_E2, pt_G2])
    model.set_polygon([pt_D2, pt_E2, pt_F2])
    model.set_polygon([pt_F2, pt_D2, pt_H2])
    model.set_polygon([pt_G2, pt_D2, pt_H2])

    # Angles (Wedges)
    model.set_wedge(pt_A1, pt_B1, pt_B1, pt_C1)
    model.set_wedge(pt_D1, pt_F1, pt_F1, pt_G1)
    model.set_wedge(pt_D1, pt_F1, pt_F1, pt_H1)
    model.set_wedge(pt_D1, pt_G1, pt_G1, pt_H1)
    model.set_wedge(pt_A2, pt_B2, pt_B2, pt_C2)
    model.set_wedge(pt_D2, pt_F2, pt_F2, pt_G2)
    model.set_wedge(pt_D2, pt_F2, pt_F2, pt_H2)
    model.set_wedge(pt_D2, pt_G2, pt_G2, pt_H2)

    return model


if __name__ == "__main__":
    construct_0312_g2()
