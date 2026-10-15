"""Programmatic construction for Book X, Proposition 12 (0038.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0038_g1() -> Model:
    """Construct the figure 0038.g1 using geometor.model."""
    model = Model("0038.g1")

    # Magnitudes A, C, B
    A_l = model.set_point(27.0, -20.5, classes=["given"], label="A")
    A_r = model.set_point(99.0, -20.5, label="A_r")

    C_l = model.set_point(136.0, -21.5, classes=["given"], label="C")
    C_r = model.set_point(231.0, -21.5, label="C_r")

    B_l = model.set_point(267.0, -22.5, classes=["given"], label="B")
    B_r = model.set_point(381.0, -22.5, label="B_r")

    # Numbers D, E, F, G
    D_l = model.set_point(82.0, -42.5, label="D")
    D_r = model.set_point(135.0, -42.5, label="D_r")

    E_l = model.set_point(82.0, -63.0, label="E")
    E_r = model.set_point(148.0, -63.0, label="E_r")

    F_l = model.set_point(80.0, -84.5, label="F")
    F_r = model.set_point(117.0, -84.5, label="F_r")

    G_l = model.set_point(80.0, -103.0, label="G")
    G_r = model.set_point(125.0, -103.0, label="G_r")

    # Numbers H, K, L
    H_l = model.set_point(271.0, -64.5, label="H")
    H_r = model.set_point(319.0, -64.5, label="H_r")

    K_l = model.set_point(270.0, -85.5, label="K")
    K_r = model.set_point(335.0, -85.5, label="K_r")

    L_l = model.set_point(271.0, -103.5, label="L")
    L_r = model.set_point(349.0, -103.5, label="L_r")

    for p_l, p_r in [
        (A_l, A_r),
        (C_l, C_r),
        (B_l, B_r),
        (D_l, D_r),
        (E_l, E_r),
        (F_l, F_r),
        (G_l, G_r),
        (H_l, H_r),
        (K_l, K_r),
        (L_l, L_r),
    ]:
        model.construct_line(p_l, p_r)
        model.set_segment(p_l, p_r)

    return model


if __name__ == "__main__":
    construct_0038_g1()
