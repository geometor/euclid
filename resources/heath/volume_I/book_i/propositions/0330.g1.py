"""GEOMETOR construction for Book I, Proposition 31 (Folio 0330, Graphic 1).

Through a given point A to draw a straight line EAF parallel to a given straight line BC.
"""

from geometor.model import Model


def build_0330_g1() -> Model:
    model = Model("0330.g1")

    B = model.set_point(-1, 0, classes=["given"], label="B")
    C = model.set_point(1.5, 0, classes=["given"], label="C")
    D = model.set_point(0, 0, classes=["given"], label="D")
    A = model.set_point(0.35, 0.75, classes=["given"], label="A")
    E = model.set_point(-0.85, 0.75, classes=["given"], label="E")
    F = model.set_point(1.35, 0.75, classes=["given"], label="F")

    model.construct_line(B, C)
    model.construct_line(E, F)
    model.construct_line(A, D)

    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(E, F)
    model.set_segment(E, A)
    model.set_segment(A, F)
    model.set_segment(A, D)

    model.set_section([E, A, F])
    model.set_section([B, D, C])

    model.set_wedge(A, D, D, E)
    model.set_wedge(D, A, A, C)

    return model


if __name__ == "__main__":
    m = build_0330_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
