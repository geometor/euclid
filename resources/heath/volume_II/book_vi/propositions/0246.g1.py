"""Programmatic construction for Book VI, Proposition 21 (0246.g1).

Figures which are similar to the same rectilineal figure are also similar to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0246_g1() -> Model:
    """Construct the figure for 0246.g1 (VI.21) using geometor.model."""
    model = Model("0246.g1")

    # 1. Similar rectilineal figure A
    A1 = model.set_point(16.0, -48.0, classes=["given"], label="A1")
    A2 = model.set_point(166.0, -86.0, classes=["given"], label="A2")
    A3 = model.set_point(179.0, -153.0, classes=["given"], label="A3")
    A4 = model.set_point(52.0, -153.0, classes=["given"], label="A4")
    model.set_segment(A1, A2)
    model.set_segment(A2, A3)
    model.set_segment(A3, A4)
    model.set_segment(A4, A1)
    model.set_polygon([A1, A2, A3, A4])

    # 2. Similar rectilineal figure B
    B1 = model.set_point(231.0, -86.0, classes=["given"], label="B1")
    B2 = model.set_point(328.0, -112.0, classes=["given"], label="B2")
    B3 = model.set_point(336.0, -154.0, classes=["given"], label="B3")
    B4 = model.set_point(254.0, -154.0, classes=["given"], label="B4")
    model.set_segment(B1, B2)
    model.set_segment(B2, B3)
    model.set_segment(B3, B4)
    model.set_segment(B4, B1)
    model.set_polygon([B1, B2, B3, B4])

    # 3. Similar rectilineal figure C
    C1 = model.set_point(397.0, -102.0, classes=["given"], label="C1")
    C2 = model.set_point(468.0, -121.0, classes=["given"], label="C2")
    C3 = model.set_point(474.0, -154.0, classes=["given"], label="C3")
    C4 = model.set_point(415.0, -154.0, classes=["given"], label="C4")
    model.set_segment(C1, C2)
    model.set_segment(C2, C3)
    model.set_segment(C3, C4)
    model.set_segment(C4, C1)
    model.set_polygon([C1, C2, C3, C4])

    return model


if __name__ == "__main__":
    construct_0246_g1()
