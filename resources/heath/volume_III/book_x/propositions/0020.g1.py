"""Programmatic construction for Book X, Proposition 1 commentary (0020.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0020_g1() -> Model:
    """Construct the Dedekind Postulate line AC for 0020.g1."""
    model = Model("0020.g1")

    # Collinear points A, H, X, M, Y, K, B, C along AC
    A = model.set_point(19.0, -25.0, classes=["given"], label="A")
    H = model.set_point(32.0, -25.0, label="H")
    X = model.set_point(61.0, -25.0, label="X")
    M = model.set_point(75.0, -25.0, label="M")
    Y = model.set_point(96.0, -25.0, label="Y")
    K = model.set_point(122.0, -25.0, label="K")
    B = model.set_point(146.0, -25.0, classes=["given"], label="B")
    C = model.set_point(299.0, -25.0, classes=["given"], label="C")

    # Base line AC
    model.construct_line(A, C)

    # Referenced and elementary segments
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(A, H)
    model.set_segment(A, K)
    model.set_segment(A, M)
    model.set_segment(M, C)
    model.set_segment(M, Y)
    model.set_segment(A, Y)
    model.set_segment(A, X)
    model.set_segment(X, Y)
    model.set_segment(X, M)
    model.set_segment(B, C)

    # Collinear sections
    model.set_section([A, M, C])
    model.set_section([A, X, Y])
    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_0020_g1()
