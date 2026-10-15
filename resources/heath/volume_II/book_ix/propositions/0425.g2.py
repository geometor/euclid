"""Programmatic construction for Book IX, Proposition 34 (0425.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0425_g2() -> Model:
    """Construct the figure 0425.g2 using geometor.model."""
    model = Model("0425.g2")

    # Single-letter horizontal number segment A
    A_l = model.set_point(10.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(160.0, -14.0, label="A_r")

    # Number segment
    model.set_segment(A_l, A_r)

    return model


if __name__ == "__main__":
    construct_0425_g2()
