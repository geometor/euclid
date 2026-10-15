"""GEOMETOR construction for Book I, Proposition 30 Note (Folio 0329, Graphic 1).

De Morgan's note: angles with parallel sides (Case 1).
DE is parallel to AB, and GEF is parallel to BC; DE produced meets BC in H.
"""

from geometor.model import Model


def build_0329_g1() -> Model:
    model = Model("0329.g1")

    A = model.set_point(0, 1.5, classes=["given"], label="A")
    B = model.set_point(-0.6, 0, classes=["given"], label="B")
    C = model.set_point(1.2, 0, classes=["given"], label="C")
    D = model.set_point(0.6, 1.6, classes=["given"], label="D")
    E = model.set_point(0.29, 0.825, classes=["given"], label="E")
    F = model.set_point(1.0, 0.825, classes=["given"], label="F")
    G = model.set_point(0.0, 0.825, classes=["given"], label="G")
    H = model.set_point(-0.1, 0, classes=["given"], label="H")

    model.construct_line(A, B)
    model.construct_line(B, C)
    model.construct_line(D, H)
    model.construct_line(G, F)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_segment(D, E)
    model.set_segment(E, H)
    model.set_segment(D, H)
    model.set_segment(G, E)
    model.set_segment(E, F)
    model.set_segment(G, F)

    model.set_section([G, E, F])
    model.set_section([D, E, H])
    model.set_section([B, H, C])

    model.set_wedge(B, A, A, C)
    model.set_wedge(E, D, D, G)
    model.set_wedge(E, D, D, F)
    model.set_wedge(H, D, D, C)

    return model


if __name__ == "__main__":
    m = build_0329_g1()
    print(f"Constructed {m.name} with {len(m)} elements.")
