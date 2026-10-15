"""Programmatic construction for Book V, Proposition 18 Commentary (0179.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0179_g1() -> Model:
    """Construct the figure 0179.g1 (Austin's proof of V.18 with vertical subdivided lines AB and CD)."""
    model = Model("0179.g1")

    # Left vertical line AB subdivided at E
    A = model.set_point(22.00, -12.00, classes=["given"], label="A")
    E = model.set_point(22.00, -71.00, classes=["given"], label="E")
    B = model.set_point(22.00, -190.00, classes=["given"], label="B")
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_section([A, E, B])

    # Right vertical line CD subdivided at F
    C = model.set_point(52.00, -48.00, classes=["given"], label="C")
    F = model.set_point(52.00, -95.00, classes=["given"], label="F")
    D = model.set_point(52.00, -190.00, classes=["given"], label="D")
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_0179_g1()
