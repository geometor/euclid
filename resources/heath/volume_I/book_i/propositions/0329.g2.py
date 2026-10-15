"""GEOMETOR construction for Book I, Proposition 30 Note (Folio 0329, Graphic 2).

De Morgan's note: angles with perpendicular sides (Case 2).
ED is perpendicular to AB, and GEF is perpendicular to BC;
ED' is drawn perpendicular to ED, and EG' perpendicular to EF.
"""

from geometor.model import Model


def build_0329_g2() -> Model:
    model = Model("0329.g2")

    A = model.set_point(-0.6, 1.4, classes=["given"], label="A")
    B = model.set_point(-1.2, 0, classes=["given"], label="B")
    C = model.set_point(1.2, 0, classes=["given"], label="C")
    D = model.set_point(-0.81, 0.91, classes=["given"], label="D")
    E = model.set_point(0.1, 0.55, classes=["given"], label="E")
    F = model.set_point(0.1, 0, classes=["given"], label="F")
    G = model.set_point(0.1, 1.15, classes=["given"], label="G")
    D_prime = model.set_point(0.42, 1.35, classes=["given"], label="D'")
    G_prime = model.set_point(0.9, 0.55, classes=["given"], label="G'")

    model.construct_line(A, B)
    model.construct_line(B, C)
    model.construct_line(D, E)
    model.construct_line(G, F)
    model.construct_line(E, D_prime)
    model.construct_line(E, G_prime)

    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(B, C)
    model.set_segment(B, F)
    model.set_segment(F, C)
    model.set_segment(E, D)
    model.set_segment(G, E)
    model.set_segment(E, F)
    model.set_segment(G, F)
    model.set_segment(E, D_prime)
    model.set_segment(E, G_prime)

    model.set_section([G, E, F])

    model.set_wedge(B, A, A, C)
    model.set_wedge(E, D, D, G)
    model.set_wedge(E, D, D, F)
    model.set_wedge(D, B, B, E)
    model.set_wedge(E, D, D, D_prime)
    model.set_wedge(E, D_prime, D_prime, G_prime)
    model.set_wedge(E, G, G, G_prime)
    model.set_wedge(E, G, G, D_prime)

    return model


if __name__ == "__main__":
    m = build_0329_g2()
    print(f"Constructed {m.name} with {len(m)} elements.")
