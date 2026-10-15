"""Programmatic construction for Book VI, Proposition 16 / Simson Prop. B (0229.g3).

Particular cases (a) internal bisector ADE and (b) external bisector EAD.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0229_g3() -> Model:
    """Construct the figure for 0229.g3 using geometor.model."""
    model = Model("0229.g3")

    # 1. Left figure: Case (a) internal bisector ADE
    O = model.set_point(95.0, -120.0, label="O")
    A = model.set_point(143.85, -65.75, classes=["given"], label="A")
    B = model.set_point(26.40, -95.03, classes=["given"], label="B")
    C = model.set_point(163.60, -95.03, classes=["given"], label="C")
    D = model.set_point(132.61, -95.03, classes=["given"], label="D")
    E = model.set_point(95.00, -193.00, classes=["given"], label="E")

    model.construct_circle(O, A)

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(A, E)
    model.set_segment(C, E)

    model.set_section([B, D, C])
    model.set_section([A, D, E])

    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, E, C])

    model.set_wedge(A, C, C, B)

    # 2. Right figure: Case (b) external bisector EAD
    O2 = model.set_point(320.0, -126.0, label="O'")
    A2 = model.set_point(374.25, -77.15, classes=["given"], label="A'")
    B2 = model.set_point(247.54, -134.90, classes=["given"], label="B'")
    C2 = model.set_point(392.46, -134.90, classes=["given"], label="C'")
    D2 = model.set_point(503.94, -134.90, classes=["given"], label="D'")
    E2 = model.set_point(320.00, -53.00, classes=["given"], label="E'")
    F2 = model.set_point(412.26, -59.83, label="F'")

    model.construct_circle(O2, A2)

    model.set_segment(B2, D2)
    model.set_segment(B2, C2)
    model.set_segment(C2, D2)
    model.set_segment(B2, F2)
    model.set_segment(B2, A2)
    model.set_segment(A2, F2)
    model.set_segment(A2, C2)
    model.set_segment(E2, D2)
    model.set_segment(E2, A2)
    model.set_segment(A2, D2)
    model.set_segment(E2, C2)

    model.set_section([B2, C2, D2])
    model.set_section([E2, A2, D2])

    model.set_polygon([A2, B2, C2])
    model.set_polygon([A2, B2, D2])
    model.set_polygon([A2, E2, C2])

    return model


if __name__ == "__main__":
    construct_0229_g3()
