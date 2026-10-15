"""Programmatic construction for Book V, Proposition 18 Commentary (0179.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0179_g2() -> Model:
    """Construct the figure 0179.g2 (Smith & Bryant rectangle area proof of V.18)."""
    model = Model("0179.g2")

    # Top row: d (21, 22), c (146, 22), e (200, 22)
    d = model.set_point(21.00, -22.00, classes=["given"], label="d")
    c = model.set_point(146.00, -22.00, classes=["given"], label="c")
    e = model.set_point(200.00, -22.00, classes=["given"], label="e")

    # Middle row: a (21, 56), b (146, 56), f (200, 56)
    a = model.set_point(21.00, -56.00, classes=["given"], label="a")
    b = model.set_point(146.00, -56.00, classes=["given"], label="b")
    f = model.set_point(200.00, -56.00, classes=["given"], label="f")

    # Bottom row: h (21, 113), g (146, 113), k (200, 113)
    h = model.set_point(21.00, -113.00, classes=["given"], label="h")
    g = model.set_point(146.00, -113.00, classes=["given"], label="g")
    k = model.set_point(200.00, -113.00, classes=["given"], label="k")

    # Polygons (rectangles)
    model.set_polygon([d, e, k, h])
    model.set_polygon([a, b, c, d])
    model.set_polygon([b, c, e, f])
    model.set_polygon([a, b, g, h])
    model.set_polygon([b, f, k, g])
    model.set_polygon([a, f, e, d])
    model.set_polygon([a, f, k, h])

    # Horizontal segments
    model.set_segment(d, e)
    model.set_segment(d, c)
    model.set_segment(c, e)
    model.set_segment(a, f)
    model.set_segment(a, b)
    model.set_segment(b, f)
    model.set_segment(h, k)
    model.set_segment(h, g)
    model.set_segment(g, k)

    # Vertical segments
    model.set_segment(d, h)
    model.set_segment(d, a)
    model.set_segment(a, h)
    model.set_segment(c, g)
    model.set_segment(c, b)
    model.set_segment(b, g)
    model.set_segment(e, k)
    model.set_segment(e, f)
    model.set_segment(f, k)

    return model


if __name__ == "__main__":
    construct_0179_g2()
