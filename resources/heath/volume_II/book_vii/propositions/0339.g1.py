"""Programmatic construction for Book VII, Proposition 32 (0339.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0339_g1() -> Model:
    """Construct the figure 0339.g1 using geometor.model."""
    model = Model("0339.g1")

    # Single-letter horizontal number segment A
    A_l = model.set_point(23.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(162.0, -14.0, label="A_r")

    model.set_segment(A_l, A_r)

    return model


if __name__ == "__main__":
    construct_0339_g1()
