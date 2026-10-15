"""GEOMETOR construction for Book I, Proposition 32 Note (Folio 0336, Graphic 1).

Extension of Proposition 32 to a convex polygon ABCDEFG divided into triangles
from angular point A.
"""

from geometor.model import Model


def build_0336_g1() -> Model:
    model = Model("0336.g1")

    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(-0.4, 0.28, classes=["given"], label="B")
    C = model.set_point(-0.44, 0.87, classes=["given"], label="C")
    D = model.set_point(0.27, 1.11, classes=["given"], label="D")
    E = model.set_point(0.67, 0.83, classes=["given"], label="E")
    F = model.set_point(1.07, 0.11, classes=["given"], label="F")
    G = model.set_point(0.79, 0, classes=["given"], label="G")

    model.construct_line(A, B)
    model.construct_line(B, C)
    model.construct_line(C, D)
    model.construct_line(D, E)
    model.construct_line(E, F)
    model.construct_line(F, G)
    model.construct_line(G, A)
    model.construct_line(A, C)
    model.construct_line(A, D)
    model.construct_line(A, E)
    model.construct_line(A, F)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(G, A)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(A, F)
    model.set_segment(B, D)

    model.set_polygon([A, B, C, D, E, F, G])
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])
    model.set_polygon([A, D, E])
    model.set_polygon([A, E, F])
    model.set_polygon([A, F, G])

    return model


if __name__ == "__main__":
    m = build_0336_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
