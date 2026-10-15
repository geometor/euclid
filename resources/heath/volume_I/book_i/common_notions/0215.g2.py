"""Programmatic construction for Book I, Postulate 4 Note — Pappus' Lunular Angle (0215.g2).

Pappus' construction (quoted by Proclus) of a lunular angle EBD equal to the
rectilineal right angle ABC, formed by semi-circles AEB and BDC on equal
perpendicular segments BA and BC.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0215_g2() -> Model:
    """Construct the figure for 0215.g2 using geometor.model."""
    model = Model("0215.g2")

    # Equal perpendicular segments BA and BC
    A = model.set_point(81.0, -25.0, classes=["given"], label="A")
    B = model.set_point(81.0, -140.0, classes=["given"], label="B")
    C = model.set_point(196.0, -140.0, classes=["given"], label="C")

    model.set_segment(B, A)
    model.set_segment(B, C)

    # Centres and midpoint points E, D of semi-circles AEB and BDC
    O_AB = model.set_point(81.0, -82.5, label="O1")
    O_BC = model.set_point(138.5, -140.0, label="O2")
    E = model.set_point(23.5, -82.5, label="E")
    D = model.set_point(138.5, -82.5, label="D")

    model.construct_circle(O_AB, A)
    model.construct_circle(O_BC, B)

    return model


if __name__ == "__main__":
    construct_0215_g2()
