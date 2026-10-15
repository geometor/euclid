"""Programmatic construction for Book V, Definition 5 note (0128.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0128_g1() -> Model:
    """Construct the figure 0128.g1 (De Morgan's colonnade and railings) using geometor.model."""
    model = Model("0128.g1")

    # Wall vertices
    W_tl = model.set_point(26.0, -10.0, classes=["given"], label="W_tl")
    W_bl = model.set_point(26.0, -56.0, classes=["given"], label="W_bl")
    W_fl = model.set_point(13.0, -72.0, classes=["given"], label="W_fl")
    W_ft = model.set_point(13.0, -26.0, classes=["given"], label="W_ft")

    # Right ends of horizontal lines
    H_top = model.set_point(460.0, -10.0, label="H_top")
    H_mid = model.set_point(459.0, -43.0, label="H_mid")
    H_col = model.set_point(428.0, -56.0, label="H_col")
    H_rail = model.set_point(436.0, -72.0, label="H_rail")
    W_mid = model.set_point(26.0, -43.0, label="W_mid")

    model.construct_line(W_bl, H_col)
    model.construct_line(W_fl, H_rail)
    model.set_polygon([W_ft, W_tl, W_bl, W_fl])
    model.set_segment(W_tl, H_top)
    model.set_segment(W_mid, H_mid)
    model.set_segment(W_bl, H_col)
    model.set_segment(W_fl, H_rail)

    # Columns 1 to 9 (spacing 41.5 from x=26.0)
    col_x = [67.5, 109.0, 150.5, 192.0, 233.5, 275.0, 316.5, 358.0, 399.5]
    col_base_pts = []
    for i, x in enumerate(col_x, start=1):
        pt_b = model.set_point(x, -56.0, label=f"C_{i}")
        pt_t = model.set_point(x, -10.0, label=f"Ct_{i}")
        model.set_segment(pt_t, pt_b)
        col_base_pts.append(pt_b)

    # Column distance segments C, 4C, 5C
    model.set_segment(W_bl, col_base_pts[0])  # C
    model.set_segment(W_bl, col_base_pts[3])  # 4C
    model.set_segment(W_bl, col_base_pts[4])  # 5C

    # Railings 1 to 19 (spacing 20.0 from x=14.0, first at 34.0)
    rail_base_pts = []
    for i in range(1, 20):
        x = 14.0 + 20.0 * i
        pt_b = model.set_point(x, -72.0, label=f"R_{i}")
        pt_t = model.set_point(x, -43.0, label=f"Rt_{i}")
        model.set_segment(pt_t, pt_b)
        rail_base_pts.append(pt_b)

    # Railing distance segments R, 10R
    model.set_segment(W_fl, rail_base_pts[0])  # R
    model.set_segment(W_fl, rail_base_pts[9])  # 10R

    return model


if __name__ == "__main__":
    construct_0128_g1()
