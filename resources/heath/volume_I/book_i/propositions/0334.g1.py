"""GEOMETOR construction for Book I, Proposition 32 Note (Folio 0334, Graphic 1).

The Pythagorean proof of Proposition 32 (handed down by Eudemus):
Through vertex A of triangle ABC draw DE parallel to BC.
"""

from geometor.model import Model


def build_0334_g1() -> Model:
    model = Model("0334.g1")

    B = model.set_point(-1, 0, classes=["given"], label="B")
    C = model.set_point(1, 0, classes=["given"], label="C")
    A = model.set_point(0.22, 1.0, classes=["given"], label="A")
    D = model.set_point(-0.8, 1.0, classes=["given"], label="D")
    E = model.set_point(1.18, 1.0, classes=["given"], label="E")

    model.construct_line(B, C)
    model.construct_line(D, E)
    model.construct_line(A, B)
    model.construct_line(A, C)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(D, A)
    model.set_segment(A, E)
    model.set_segment(D, E)

    model.set_polygon([A, B, C])
    model.set_section([D, A, E])

    model.set_wedge(A, D, D, B)
    model.set_wedge(B, A, A, C)
    model.set_wedge(A, E, E, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    m = build_0334_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
