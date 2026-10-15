"""GEOMETOR construction for Book I, Proposition 32 Note (Folio 0332, Graphic 1).

Hankel/Cantor historical reconstruction: equilateral triangle ABC with altitude AD
and completed rectangle ADCE.
"""

from geometor.model import Model


def build_0332_g1() -> Model:
    model = Model("0332.g1")

    B = model.set_point(-1, 0, classes=["given"], label="B")
    D = model.set_point(0, 0, classes=["given"], label="D")
    C = model.set_point(1, 0, classes=["given"], label="C")
    A = model.set_point(0, 1.732, classes=["given"], label="A")
    E = model.set_point(1, 1.732, classes=["given"], label="E")

    model.construct_line(B, C)
    model.construct_line(A, B)
    model.construct_line(A, C)
    model.construct_line(A, D)
    model.construct_line(A, E)
    model.construct_line(C, E)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(C, E)

    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, E, C])
    model.set_polygon([A, D, C, E])

    return model


if __name__ == "__main__":
    m = build_0332_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
