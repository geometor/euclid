"""Programmatic construction for Book II, Proposition 10 (0409.g1).

If a straight line be bisected, and a straight line be added to it in a
straight line, the square on the whole with the added straight line and the
square on the added straight line both together are double of the square on
the half and of the square described on the straight line made up of the half
and the added straight line as on one straight line.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0409_g1() -> Model:
    """Construct the figure for Book II, Proposition 10 using geometor.model."""
    model = Model("0409.g1")

    # 1. Let a straight line AB be bisected at C, and BD added to it in a straight line.
    A = model.set_point(0, 0, classes=["given"], label="A")
    C = model.set_point(1, 0, classes=["given"], label="C")
    B = model.set_point(2, 0, classes=["given"], label="B")
    D = model.set_point(sp.Rational(5, 2), 0, classes=["given"], label="D")

    model.construct_line(A, D)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(B, D)
    model.set_segment(C, D)
    model.set_segment(A, D)

    # 2. Let CE be drawn from C at right angles to AB, made equal to AC or CB.
    E = model.set_point(1, 1, label="E")
    model.set_segment(C, E)

    # 3. Let EA, EB be joined.
    model.set_segment(E, A)
    model.set_segment(E, B)

    # 4. Through E let EF be drawn parallel to AD, and through D let FD be drawn parallel to CE.
    F = model.set_point(sp.Rational(5, 2), 1, label="F")
    model.set_segment(E, F)
    model.set_segment(F, D)

    # 5. Let EB, FD be produced in the direction B, D and meet at G; let AG be joined.
    model.construct_line(E, B)
    model.construct_line(F, D)
    G = model.set_point(sp.Rational(5, 2), sp.Rational(-1, 2), label="G")
    model.set_segment(E, G)
    model.set_segment(B, G)
    model.set_segment(F, G)
    model.set_segment(D, G)
    model.set_segment(A, G)

    # 6. Triangles referenced in the proof
    model.set_polygon([A, C, E])
    model.set_polygon([E, C, B])
    model.set_polygon([A, E, B])
    model.set_polygon([B, D, G])
    model.set_polygon([E, F, G])
    model.set_polygon([A, E, G])
    model.set_polygon([A, D, G])

    # 7. Angles (wedges) referenced in the proof
    model.set_wedge(E, C, C, F)  # < C E F )
    model.set_wedge(F, E, E, D)  # < E F D )
    model.set_wedge(E, F, F, B)  # < F E B )
    model.set_wedge(A, E, E, C)  # < E A C )
    model.set_wedge(E, A, A, C)  # < A E C )
    model.set_wedge(C, A, A, E)  # < A C E )
    model.set_wedge(C, E, E, D)  # < E C D )
    model.set_wedge(E, C, C, B)  # < C E B )
    model.set_wedge(B, E, E, C)  # < E B C )
    model.set_wedge(E, A, A, B)  # < A E B )
    model.set_wedge(B, D, D, G)  # < D B G )
    model.set_wedge(D, B, B, G)  # < B D G )
    model.set_wedge(G, D, D, B)  # < D G B )
    model.set_wedge(G, E, E, F)  # < E G F )
    model.set_wedge(E, F, F, G)  # < F E G )

    return model


if __name__ == "__main__":
    construct_0409_g1()
