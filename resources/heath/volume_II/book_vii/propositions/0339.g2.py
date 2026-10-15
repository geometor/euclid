"""Programmatic construction for Book VII, Proposition 33 (0339.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0339_g2() -> Model:
    """Construct the figure 0339.g2 using geometor.model."""
    model = Model("0339.g2")

    # Given numbers A, B, C and greatest common measure D
    A_t = model.set_point(58.0, -12.0, classes=["given"], label="A")
    A_b = model.set_point(58.0, -83.0, label="A_b")

    B_t = model.set_point(87.0, -15.0, classes=["given"], label="B")
    B_b = model.set_point(87.0, -119.0, label="B_b")

    C_t = model.set_point(118.0, -12.0, classes=["given"], label="C")
    C_b = model.set_point(118.0, -150.0, label="C_b")

    D_t = model.set_point(144.0, -14.0, classes=["given"], label="D")
    D_b = model.set_point(144.0, -50.0, label="D_b")

    # Numbers H, K, L and unit-count M
    H_t = model.set_point(22.0, -115.0, classes=["given"], label="H")
    H_b = model.set_point(22.0, -145.0, label="H_b")

    K_t = model.set_point(44.0, -116.0, classes=["given"], label="K")
    K_b = model.set_point(44.0, -153.0, label="K_b")

    L_t = model.set_point(64.0, -113.0, classes=["given"], label="L")
    L_b = model.set_point(64.0, -162.0, label="L_b")

    M_t = model.set_point(87.0, -137.0, classes=["given"], label="M")
    M_b = model.set_point(87.0, -163.0, label="M_b")

    # Least numbers in the same ratio E, F, G
    E_t = model.set_point(144.0, -87.0, classes=["given"], label="E")
    E_b = model.set_point(144.0, -133.0, label="E_b")

    F_t = model.set_point(170.0, -86.0, classes=["given"], label="F")
    F_b = model.set_point(170.0, -157.0, label="F_b")

    G_t = model.set_point(198.0, -85.0, classes=["given"], label="G")
    G_b = model.set_point(198.0, -173.0, label="G_b")

    # Segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(H_t, H_b)
    model.set_segment(K_t, K_b)
    model.set_segment(L_t, L_b)
    model.set_segment(M_t, M_b)
    model.set_segment(E_t, E_b)
    model.set_segment(F_t, F_b)
    model.set_segment(G_t, G_b)

    return model


if __name__ == "__main__":
    construct_0339_g2()
