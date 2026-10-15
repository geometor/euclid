"""Programmatic construction for Book I, Postulate 1 Note — Saccheri's Proof (0210.g2).

Saccheri's diagram of two lines enclosing a space between common extremities A and X,
revolved about the fixed axis AX.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0210_g2() -> Model:
    """Construct the figure for 0210.g2 using geometor.model."""
    model = Model("0210.g2")

    # Common extremities A (bottom) and X (top)
    A = model.set_point(45.0, -140.0, classes=["given"], label="A")
    X = model.set_point(45.0, -24.0, classes=["given"], label="X")
    model.set_segment(A, X)

    # Intermediate points on the revolved curves and axis
    B = model.set_point(35.5, -62.0, label="B")
    D = model.set_point(45.0, -62.0, label="D")
    C = model.set_point(54.5, -62.0, label="C")

    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(B, C)

    return model


if __name__ == "__main__":
    construct_0210_g2()
