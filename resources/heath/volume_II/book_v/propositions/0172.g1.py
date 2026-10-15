"""Programmatic construction for Book V, Proposition 16 Commentary (0172.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0172_g1() -> Model:
    """Construct the figure 0172.g1 (Smith & Bryant rectangle area proof of V.16)."""
    model = Model("0172.g1")

    # Top row: d (21, 23), c (128, 23), e (189, 23)
    d = model.set_point(21.00, -23.00, classes=["given"], label="d")
    c = model.set_point(128.00, -23.00, classes=["given"], label="c")
    e = model.set_point(189.00, -23.00, classes=["given"], label="e")

    # Middle row: a (21, 98), b (128, 98), f (189, 98)
    a = model.set_point(21.00, -98.00, classes=["given"], label="a")
    b = model.set_point(128.00, -98.00, classes=["given"], label="b")
    f = model.set_point(189.00, -98.00, classes=["given"], label="f")

    # Bottom row: h (21, 160), g (128, 160), k (189, 160)
    h = model.set_point(21.00, -160.00, classes=["given"], label="h")
    g = model.set_point(128.00, -160.00, classes=["given"], label="g")
    k = model.set_point(189.00, -160.00, classes=["given"], label="k")

    # Polygons (rectangles)
    model.set_polygon([d, e, k, h])
    model.set_polygon([a, b, c, d])
    model.set_polygon([b, c, e, f])
    model.set_polygon([a, b, g, h])
    model.set_polygon([b, f, k, g])

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
    construct_0172_g1()
