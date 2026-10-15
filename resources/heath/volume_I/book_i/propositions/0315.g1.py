"""Programmatic construction for Book I, Proposition 25 - Heron's Proof (0315.g1).

Heron's direct proof of Book I, Proposition 25.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0315_g1() -> Model:
    """Construct the figure for Heron's proof of I.25 (0315.g1) using geometor.model."""
    model = Model("0315.g1")

    # 1. Left triangle ABC
    A = model.set_point(74, -141, classes=["given"], label="A")
    B = model.set_point(35, -211.5, classes=["given"], label="B")
    C = model.set_point(164.5, -211.5, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # 2. Right triangle DEF and produced points G, H, K
    D = model.set_point(219, -131, classes=["given"], label="D")
    E = model.set_point(206.5, -211.5, classes=["given"], label="E")
    F = model.set_point(299, -211.5, classes=["given"], label="F")
    G = model.set_point(336.5, -211.5, label="G")
    H = model.set_point(236.3, -19.5, label="H")
    K = model.set_point(327.3, -163.4, label="K")

    # Extended lines [ E F ] and [ E D ]
    model.construct_line(E, F)
    model.construct_line(E, D)

    # Circles ( D F ) [alias ( F K H )] and ( E G ) [alias ( K G )]
    model.construct_circle(D, F)
    model.construct_circle(E, G)

    # Segments and collinear sub-segments
    model.set_segment(D, E)
    model.set_segment(D, H)
    model.set_segment(E, H)
    model.set_section([E, D, H])

    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(E, G)
    model.set_section([E, F, G])

    model.set_segment(D, F)
    model.set_segment(D, K)
    model.set_segment(E, K)

    # Triangles on the right
    model.set_polygon([D, E, F])
    model.set_polygon([D, E, K])
    model.set_polygon([D, F, K])

    # Angles (wedges): < B A C ), < E D K ), < E D F )
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, E, E, K)
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_0315_g1()
