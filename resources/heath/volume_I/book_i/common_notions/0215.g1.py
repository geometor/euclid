"""Programmatic construction for Book I, Postulate 4 Note — Saccheri's Proof (0215.g1).

Saccheri's proof of the equality of all rectilineal right angles: DA standing on BAC
and LH standing on FHM, with FHM laid upon BAC so that H falls on A and L on D.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0215_g1() -> Model:
    """Construct the figure for 0215.g1 using geometor.model."""
    model = Model("0215.g1")

    # Left figure: DA standing on BAC, and applied line FAM cutting BC at A
    B = model.set_point(14.0, -102.0, classes=["given"], label="B")
    A = model.set_point(72.0, -102.0, classes=["given"], label="A")
    C = model.set_point(132.0, -102.0, classes=["given"], label="C")
    D = model.set_point(72.0, -22.0, classes=["given"], label="D")
    F_applied = model.set_point(25.0, -82.0, label="F")
    M_applied = model.set_point(125.0, -124.5, label="M")

    model.set_segment(B, A)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(D, A)
    model.set_segment(F_applied, A)
    model.set_segment(A, M_applied)
    model.set_section([B, A, C])
    model.set_section([F_applied, A, M_applied])

    # Right figure: LH standing on FHM
    F = model.set_point(165.0, -102.0, classes=["given"], label="F_2")
    H = model.set_point(220.0, -102.0, classes=["given"], label="H")
    M = model.set_point(276.0, -102.0, classes=["given"], label="M_2")
    L = model.set_point(220.0, -22.0, classes=["given"], label="L")

    model.set_segment(F, H)
    model.set_segment(H, M)
    model.set_segment(F, M)
    model.set_segment(L, H)
    model.set_section([F, H, M])

    return model


if __name__ == "__main__":
    construct_0215_g1()
