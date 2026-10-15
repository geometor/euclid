"""Programmatic construction for Book V, Definition 5 note (0130.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0130_g1() -> Model:
    """Construct the figure 0130.g1 using geometor.model."""
    model = Model("0130.g1")

    # Origin and ray endpoints
    O = model.set_point(20.0, -113.0, classes=["given"], label="O")
    X_end = model.set_point(403.0, -113.0, label="X_end")
    Y_end = model.set_point(398.0, -22.0, label="Y_end")

    # Points on OA produced: a, A, a_2, A_2, a_3, A_3, a_4, A_4
    a = model.set_point(94.0, -113.0, classes=["given"], label="a")
    A = model.set_point(106.0, -113.0, classes=["given"], label="A")
    a_2 = model.set_point(172.0, -113.0, label="a_2")
    A_2 = model.set_point(196.0, -113.0, label="A_2")
    a_3 = model.set_point(253.0, -113.0, label="a_3")
    A_3 = model.set_point(286.0, -113.0, label="A_3")
    a_4 = model.set_point(332.0, -113.0, label="a_4")
    A_4 = model.set_point(374.0, -113.0, label="A_4")

    # Points on OB produced: b, B, b_2, B_2, b_3, B_3, b_4, B_4
    b = model.set_point(94.0, -95.19, classes=["given"], label="b")
    B = model.set_point(106.0, -92.30, classes=["given"], label="B")
    b_2 = model.set_point(172.0, -76.41, label="b_2")
    B_2 = model.set_point(196.0, -70.63, label="B_2")
    b_3 = model.set_point(253.0, -56.91, label="b_3")
    B_3 = model.set_point(286.0, -48.96, label="B_3")
    b_4 = model.set_point(332.0, -37.89, label="b_4")
    B_4 = model.set_point(374.0, -27.78, label="B_4")

    # Base lines (OA produced, OB produced)
    model.construct_line(O, A)
    model.construct_line(O, B)

    # Polygons
    model.set_polygon([O, A, B])
    model.set_polygon([O, a, b])

    # Vertical parallel segments
    model.set_segment(a, b)
    model.set_segment(A, B)
    model.set_segment(a_2, b_2)
    model.set_segment(A_2, B_2)
    model.set_segment(a_3, b_3)
    model.set_segment(A_3, B_3)
    model.set_segment(a_4, b_4)
    model.set_segment(A_4, B_4)

    # Segments along OA produced
    model.set_segment(O, X_end)
    model.set_segment(O, a)
    model.set_segment(O, A)
    model.set_segment(a, a_2)
    model.set_segment(a_2, a_3)
    model.set_segment(a_3, a_4)
    model.set_segment(A, A_2)
    model.set_segment(A_2, A_3)
    model.set_segment(A_3, A_4)

    # Segments along OB produced
    model.set_segment(O, Y_end)
    model.set_segment(O, b)
    model.set_segment(O, B)
    model.set_segment(b, b_2)
    model.set_segment(b_2, b_3)
    model.set_segment(b_3, b_4)
    model.set_segment(B, B_2)
    model.set_segment(B_2, B_3)
    model.set_segment(B_3, B_4)

    return model


if __name__ == "__main__":
    construct_0130_g1()
