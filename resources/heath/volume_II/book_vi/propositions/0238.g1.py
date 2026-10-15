"""Programmatic construction for Book VI, Proposition 18 note (0238.g1).

General homothetic construction of polygons C'D'E'F'G' and C1D1E1F1G1
similar and similarly situated to CDEFG with respect to centre O.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0238_g1() -> Model:
    """Construct the figure for 0238.g1 using geometor.model."""
    model = Model("0238.g1")

    # 1. Centre of homothety O
    O = model.set_point(272.0, -99.0, classes=["given"], label="O")

    # 2. Given pentagon CDEFG
    C = model.set_point(53.0, -157.0, classes=["given"], label="C")
    D = model.set_point(54.0, -68.0, classes=["given"], label="D")
    E = model.set_point(92.0, -43.0, classes=["given"], label="E")
    F = model.set_point(147.0, -112.0, classes=["given"], label="F")
    G = model.set_point(110.0, -166.0, classes=["given"], label="G")

    # 3. Direct homothetic pentagon C'D'E'F'G'
    Cp = model.set_point(169.0, -126.0, classes=["given"], label="C'")
    Dp = model.set_point(170.0, -80.0, classes=["given"], label="D'")
    Ep = model.set_point(188.0, -68.0, classes=["given"], label="E'")
    Fp = model.set_point(215.0, -103.0, classes=["given"], label="F'")
    Gp = model.set_point(197.0, -130.0, classes=["given"], label="G'")

    # 4. Inverse homothetic pentagon C1D1E1F1G1
    C1 = model.set_point(421.0, -59.0, classes=["given"], label="C1")
    D1 = model.set_point(420.0, -120.0, classes=["given"], label="D1")
    E1 = model.set_point(397.0, -137.0, classes=["given"], label="E1")
    F1 = model.set_point(361.0, -90.0, classes=["given"], label="F1")
    G1 = model.set_point(383.0, -55.0, classes=["given"], label="G1")

    # 5. Construction Lines through O
    model.construct_line(C, C1)
    model.construct_line(D, D1)
    model.construct_line(E, E1)
    model.construct_line(F, F1)
    model.construct_line(G, G1)

    # 6. Segments
    for P, Q in [(C, D), (D, E), (E, F), (F, G), (G, C)]:
        model.set_segment(P, Q)
    for P, Q in [(Cp, Dp), (Dp, Ep), (Ep, Fp), (Fp, Gp), (Gp, Cp)]:
        model.set_segment(P, Q)
    for P, Q in [(C1, D1), (D1, E1), (E1, F1), (F1, G1), (G1, C1)]:
        model.set_segment(P, Q)

    for P in [C, D, E, F, G, Cp, Dp, Ep, Fp, Gp, C1, D1, E1, F1, G1]:
        model.set_segment(O, P)

    # 7. Polygons
    model.set_polygon([C, D, E, F, G])
    model.set_polygon([Cp, Dp, Ep, Fp, Gp])
    model.set_polygon([C1, D1, E1, F1, G1])

    return model


if __name__ == "__main__":
    construct_0238_g1()
