"""GEOMETOR construction for Book I, Proposition 32 Note (Folio 0333, Graphic 1).

Hankel/Cantor historical reconstruction: general scalene triangle ABC resolved into two
right-angled triangles ABD, ADC by altitude AD inside bounding rectangle EBCF.
"""

from geometor.model import Model


def build_0333_g1() -> Model:
    model = Model("0333.g1")

    B = model.set_point(-1, 0, classes=["given"], label="B")
    D = model.set_point(0, 0, classes=["given"], label="D")
    C = model.set_point(1.25, 0, classes=["given"], label="C")
    A = model.set_point(0, 0.85, classes=["given"], label="A")
    E = model.set_point(-1, 0.85, classes=["given"], label="E")
    F = model.set_point(1.25, 0.85, classes=["given"], label="F")

    model.construct_line(B, C)
    model.construct_line(E, F)
    model.construct_line(B, E)
    model.construct_line(A, D)
    model.construct_line(C, F)
    model.construct_line(A, B)
    model.construct_line(A, C)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(E, A)
    model.set_segment(A, F)
    model.set_segment(E, F)
    model.set_segment(C, F)

    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([E, B, C, F])

    return model


if __name__ == "__main__":
    m = build_0333_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
