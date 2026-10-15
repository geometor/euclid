"""GEOMETOR construction for Book I, Proposition 32 (Folio 0331, Graphic 1).

In any triangle ABC, if one of the sides BC be produced to D, the exterior angle ACD is equal
to the two interior and opposite angles CAB, ABC, and the three interior angles ABC, BCA, CAB
are equal to two right angles.
"""

from geometor.model import Model


def build_0331_g1() -> Model:
    model = Model("0331.g1")

    B = model.set_point(-1, 0, classes=["given"], label="B")
    C = model.set_point(0, 0, classes=["given"], label="C")
    D = model.set_point(0.9, 0, classes=["given"], label="D")
    A = model.set_point(-0.4, 1.0, classes=["given"], label="A")
    E = model.set_point(0.6, 1.0, classes=["given"], label="E")

    model.construct_line(B, D)
    model.construct_line(A, B)
    model.construct_line(A, C)
    model.construct_line(C, E)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(B, D)
    model.set_segment(A, C)
    model.set_segment(C, E)

    model.set_polygon([A, B, C])
    model.set_section([B, C, D])

    model.set_wedge(C, A, A, D)
    model.set_wedge(A, C, C, B)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, B, B, A)
    model.set_wedge(C, A, A, E)
    model.set_wedge(C, E, E, D)

    return model


if __name__ == "__main__":
    m = build_0331_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
