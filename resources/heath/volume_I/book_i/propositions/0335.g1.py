"""GEOMETOR construction for Book I, Proposition 32 Note (Folio 0335, Graphic 1).

Thibaut's method of rotation for the angle-sum of a triangle ABC with sides produced.
"""

from geometor.model import Model


def build_0335_g1() -> Model:
    model = Model("0335.g1")

    B = model.set_point(0, 0, classes=["given"], label="B")
    C = model.set_point(1.4, 0, classes=["given"], label="C")
    D = model.set_point(-0.5, 0, classes=["given"], label="D")
    A = model.set_point(0.78, 0.62, classes=["given"], label="A")

    model.construct_line(D, C)
    model.construct_line(B, A)
    model.construct_line(A, C)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(C, D)

    model.set_polygon([A, B, C])
    model.set_section([D, B, C])

    return model


if __name__ == "__main__":
    m = build_0335_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
