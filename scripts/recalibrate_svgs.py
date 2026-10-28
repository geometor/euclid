#!/usr/bin/env python3
"""Recalibrate SVG bounding boxes (viewBox, width, height) and normalize styles
for light/dark mode and global CSS control across resources/heath/.
"""

from __future__ import annotations

import argparse
import math
import pathlib
import re
import xml.etree.ElementTree as ET
from typing import Iterable, Tuple

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)

STANDALONE_STYLE = """
    :root {
      --geom-fg: #18181b;
      --geom-bg: #ffffff;
      --geom-point-stroke: #ffffff;
      --geom-poly-fill: #000000;
      --geom-accent: #ef4444;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --geom-fg: #d6cfc5;
        --geom-bg: #1e1e20;
        --geom-point-stroke: #1e1e20;
        --geom-poly-fill: #d6cfc5;
        --geom-accent: #ef4444;
      }
    }
    .euclid-graphic {
      font-family: 'EB Garamond', 'Times New Roman', 'Georgia', serif;
      font-style: italic;
      background-color: var(--geom-bg);
    }
    .geom-line {
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-bold {
      stroke: var(--geom-fg);
      stroke-width: 2.2;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-circle, .geom-curve, .geom-ellipse {
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-arc {
      stroke: var(--geom-fg);
      stroke-width: 1.6;
      stroke-linecap: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-dashed, .geom-line-dashed, .geom-arc-dashed, .geom-aux, .geom-Auxiliary, .geom-construction {
      stroke: var(--geom-fg);
      stroke-width: 1.5;
      stroke-dasharray: 4, 3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-arc-dotted {
      stroke: var(--geom-fg);
      stroke-width: 1.5;
      stroke-dasharray: 2.5, 2.5;
      stroke-linecap: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-ray {
      stroke: var(--geom-fg);
      stroke-width: 1.3;
      stroke-linecap: round;
      fill: none;
      opacity: 0.85;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-tick {
      stroke: var(--geom-fg);
      stroke-width: 1.5;
      stroke-linecap: round;
      fill: none;
    }
    .grid-line {
      stroke: var(--geom-fg);
      stroke-width: 0.9;
      stroke-linecap: round;
      fill: none;
      opacity: 0.65;
    }
    .geom-polygon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.04;
      stroke: none;
      transition: fill-opacity 0.15s, stroke 0.15s;
    }
    .geom-polygon-bordered, .geom-polygon-stroked, .geom-space {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.04;
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: fill-opacity 0.15s, stroke 0.15s, stroke-width 0.15s;
    }
    .geom-polygon-gnomon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.14;
      stroke: none;
      transition: fill-opacity 0.15s, stroke 0.15s;
    }
    .wedge, .angle {
      fill: var(--geom-accent);
      fill-opacity: 0.24;
      stroke: var(--geom-accent);
      stroke-width: 2;
      stroke-linejoin: round;
      transition: opacity 0.12s ease, fill-opacity 0.12s ease;
    }
    .geom-point {
      fill: var(--geom-fg);
      stroke: var(--geom-point-stroke);
      stroke-width: 1;
      transition: fill 0.15s, r 0.15s;
    }
    .geom-dot {
      fill: var(--geom-fg);
      stroke: none;
      transition: fill 0.15s, r 0.15s;
    }
    .geom-label {
      font-size: 14.5px;
      font-weight: bold;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-label-roman {
      font-size: 14.5px;
      font-weight: bold;
      font-style: normal;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-label-sm {
      font-size: 11px;
      font-weight: bold;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-label-sub {
      font-size: 11px;
      font-style: normal;
      font-weight: bold;
    }
    .geom-overlay {
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.12s ease;
    }
    [data-ref]:hover, .highlight, .geom-highlight-active {
      opacity: 1 !important;
      stroke: var(--geom-accent) !important;
      cursor: pointer;
    }
    text[data-ref]:hover, text.highlight, text.geom-highlight-active, text.geom-highlight-secondary, text.geom-highlight-active *, text.geom-highlight-secondary * {
      opacity: 1 !important;
      fill: var(--geom-accent) !important;
      stroke: none !important;
    }
    .geom-polygon:hover, .geom-polygon.highlight, .geom-polygon-bordered:hover, .geom-polygon-bordered.highlight, .geom-polygon-stroked:hover, .geom-polygon-stroked.highlight, .geom-polygon-gnomon:hover, .geom-polygon-gnomon.highlight, .geom-space:hover, .geom-space.highlight, polygon.geom-highlight-active, path.geom-polygon.geom-highlight-active, .wedge:hover, .wedge.highlight, .wedge.angle:hover, .wedge.angle.highlight, .wedge.angle.geom-highlight-active, path.wedge.geom-highlight-active, path.angle.geom-highlight-active {
      opacity: 1 !important;
      fill-opacity: 0.24 !important;
      fill: var(--geom-accent) !important;
      stroke: var(--geom-accent) !important;
    }
    .geom-point:hover, .geom-point.highlight, circle.geom-point.geom-highlight-active, .geom-dot:hover, .geom-dot.highlight, circle.geom-highlight-active {
      opacity: 1 !important;
      fill: var(--geom-accent) !important;
      stroke: none !important;
    }
""".strip("\n")


class BBox:
    """Mutable 2D axis-aligned bounding box."""

    def __init__(self) -> None:
        self.min_x = float("inf")
        self.min_y = float("inf")
        self.max_x = float("-inf")
        self.max_y = float("-inf")

    @property
    def is_valid(self) -> bool:
        return self.min_x <= self.max_x and self.min_y <= self.max_y

    def add_point(self, x: float, y: float) -> None:
        if math.isnan(x) or math.isnan(y) or math.isinf(x) or math.isinf(y):
            return
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y

    def add_box(self, x0: float, y0: float, x1: float, y1: float) -> None:
        self.add_point(x0, y0)
        self.add_point(x1, y1)


def _local_tag(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


def _sample_cubic(
    p0: Tuple[float, float],
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    p3: Tuple[float, float],
    bbox: BBox,
    steps: int = 32,
) -> None:
    for i in range(steps + 1):
        t = i / steps
        mt = 1.0 - t
        x = (
            mt * mt * mt * p0[0]
            + 3 * mt * mt * t * p1[0]
            + 3 * mt * t * t * p2[0]
            + t * t * t * p3[0]
        )
        y = (
            mt * mt * mt * p0[1]
            + 3 * mt * mt * t * p1[1]
            + 3 * mt * t * t * p2[1]
            + t * t * t * p3[1]
        )
        bbox.add_point(x, y)


def _sample_quad(
    p0: Tuple[float, float],
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    bbox: BBox,
    steps: int = 24,
) -> None:
    for i in range(steps + 1):
        t = i / steps
        mt = 1.0 - t
        x = mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0]
        y = mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]
        bbox.add_point(x, y)


def _sample_arc(
    x1: float,
    y1: float,
    rx: float,
    ry: float,
    phi_deg: float,
    fa: int,
    fs: int,
    x2: float,
    y2: float,
    bbox: BBox,
    steps: int = 64,
) -> None:
    """Convert SVG endpoint arc to center parameterization (SVG 1.1 F.6.5) and sample points."""
    bbox.add_point(x1, y1)
    bbox.add_point(x2, y2)
    rx = abs(rx)
    ry = abs(ry)
    if rx == 0.0 or ry == 0.0 or (x1 == x2 and y1 == y2):
        return

    phi = math.radians(phi_deg % 360.0)
    cos_phi = math.cos(phi)
    sin_phi = math.sin(phi)

    dx2 = (x1 - x2) / 2.0
    dy2 = (y1 - y2) / 2.0
    x1p = cos_phi * dx2 + sin_phi * dy2
    y1p = -sin_phi * dx2 + cos_phi * dy2

    lam = (x1p * x1p) / (rx * rx) + (y1p * y1p) / (ry * ry)
    if lam > 1.0:
        scale = math.sqrt(lam)
        rx *= scale
        ry *= scale

    rx2 = rx * rx
    ry2 = ry * ry
    x1p2 = x1p * x1p
    y1p2 = y1p * y1p

    denom = rx2 * y1p2 + ry2 * x1p2
    if denom == 0.0:
        return
    num = max(0.0, rx2 * ry2 - denom)
    factor = math.sqrt(num / denom)
    if fa == fs:
        factor = -factor

    cxp = factor * (rx * y1p / ry)
    cyp = factor * (-ry * x1p / rx)

    cx = cos_phi * cxp - sin_phi * cyp + (x1 + x2) / 2.0
    cy = sin_phi * cxp + cos_phi * cyp + (y1 + y2) / 2.0

    def vec_angle(ux: float, uy: float, vx: float, vy: float) -> float:
        dot = ux * vx + uy * vy
        mag = math.hypot(ux, uy) * math.hypot(vx, vy)
        if mag == 0.0:
            return 0.0
        cos_a = max(-1.0, min(1.0, dot / mag))
        ang = math.acos(cos_a)
        if ux * vy - uy * vx < 0.0:
            ang = -ang
        return ang

    ux = (x1p - cxp) / rx
    uy = (y1p - cyp) / ry
    vx = (-x1p - cxp) / rx
    vy = (-y1p - cyp) / ry

    theta1 = vec_angle(1.0, 0.0, ux, uy)
    dtheta = vec_angle(ux, uy, vx, vy)

    if fs == 0 and dtheta > 0.0:
        dtheta -= 2.0 * math.pi
    elif fs == 1 and dtheta < 0.0:
        dtheta += 2.0 * math.pi

    for i in range(steps + 1):
        theta = theta1 + dtheta * (i / steps)
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        px = cos_phi * rx * cos_t - sin_phi * ry * sin_t + cx
        py = sin_phi * rx * cos_t + cos_phi * ry * sin_t + cy
        bbox.add_point(px, py)


_PATH_TOKEN_RE = re.compile(
    r"([MmLlHhVvCcSsQqTtAaZz])|([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)"
)


def _add_path_bbox(d: str, bbox: BBox) -> None:
    tokens = _PATH_TOKEN_RE.findall(d)
    cmd = ""
    nums: list[float] = []

    items: list[str | float] = []
    for c, n in tokens:
        if c:
            items.append(c)
        else:
            items.append(float(n))

    idx = 0
    cur_x, cur_y = 0.0, 0.0
    start_x, start_y = 0.0, 0.0
    last_ctrl: Tuple[float, float] | None = None
    last_cmd = ""

    while idx < len(items):
        if isinstance(items[idx], str):
            cmd = str(items[idx])
            idx += 1
        if cmd in ("Z", "z"):
            cur_x, cur_y = start_x, start_y
            last_ctrl = None
            last_cmd = cmd
            continue

        if cmd in ("M", "m"):
            x = float(items[idx])
            y = float(items[idx + 1])
            idx += 2
            if cmd == "m":
                cur_x += x
                cur_y += y
            else:
                cur_x, cur_y = x, y
            start_x, start_y = cur_x, cur_y
            bbox.add_point(cur_x, cur_y)
            cmd = "l" if cmd == "m" else "L"
            last_ctrl = None
            last_cmd = cmd
        elif cmd in ("L", "l"):
            x = float(items[idx])
            y = float(items[idx + 1])
            idx += 2
            if cmd == "l":
                cur_x += x
                cur_y += y
            else:
                cur_x, cur_y = x, y
            bbox.add_point(cur_x, cur_y)
            last_ctrl = None
            last_cmd = cmd
        elif cmd in ("H", "h"):
            x = float(items[idx])
            idx += 1
            cur_x = cur_x + x if cmd == "h" else x
            bbox.add_point(cur_x, cur_y)
            last_ctrl = None
            last_cmd = cmd
        elif cmd in ("V", "v"):
            y = float(items[idx])
            idx += 1
            cur_y = cur_y + y if cmd == "v" else y
            bbox.add_point(cur_x, cur_y)
            last_ctrl = None
            last_cmd = cmd
        elif cmd in ("C", "c"):
            x1, y1, x2, y2, x, y = [float(items[idx + k]) for k in range(6)]
            idx += 6
            if cmd == "c":
                x1 += cur_x
                y1 += cur_y
                x2 += cur_x
                y2 += cur_y
                x += cur_x
                y += cur_y
            _sample_cubic((cur_x, cur_y), (x1, y1), (x2, y2), (x, y), bbox)
            cur_x, cur_y = x, y
            last_ctrl = (x2, y2)
            last_cmd = cmd
        elif cmd in ("S", "s"):
            x2, y2, x, y = [float(items[idx + k]) for k in range(4)]
            idx += 4
            if cmd == "s":
                x2 += cur_x
                y2 += cur_y
                x += cur_x
                y += cur_y
            if last_cmd in ("C", "c", "S", "s") and last_ctrl is not None:
                x1 = 2 * cur_x - last_ctrl[0]
                y1 = 2 * cur_y - last_ctrl[1]
            else:
                x1, y1 = cur_x, cur_y
            _sample_cubic((cur_x, cur_y), (x1, y1), (x2, y2), (x, y), bbox)
            cur_x, cur_y = x, y
            last_ctrl = (x2, y2)
            last_cmd = cmd
        elif cmd in ("Q", "q"):
            x1, y1, x, y = [float(items[idx + k]) for k in range(4)]
            idx += 4
            if cmd == "q":
                x1 += cur_x
                y1 += cur_y
                x += cur_x
                y += cur_y
            _sample_quad((cur_x, cur_y), (x1, y1), (x, y), bbox)
            cur_x, cur_y = x, y
            last_ctrl = (x1, y1)
            last_cmd = cmd
        elif cmd in ("T", "t"):
            x, y = float(items[idx]), float(items[idx + 1])
            idx += 2
            if cmd == "t":
                x += cur_x
                y += cur_y
            if last_cmd in ("Q", "q", "T", "t") and last_ctrl is not None:
                x1 = 2 * cur_x - last_ctrl[0]
                y1 = 2 * cur_y - last_ctrl[1]
            else:
                x1, y1 = cur_x, cur_y
            _sample_quad((cur_x, cur_y), (x1, y1), (x, y), bbox)
            cur_x, cur_y = x, y
            last_ctrl = (x1, y1)
            last_cmd = cmd
        elif cmd in ("A", "a"):
            rx, ry, rot, fa, fs, x, y = [float(items[idx + k]) for k in range(7)]
            idx += 7
            if cmd == "a":
                x += cur_x
                y += cur_y
            _sample_arc(cur_x, cur_y, rx, ry, rot, int(fa), int(fs), x, y, bbox)
            cur_x, cur_y = x, y
            last_ctrl = None
            last_cmd = cmd
        else:
            break


def compute_svg_bbox(root: ET.Element) -> BBox:
    """Compute tight bounding box of all geometric and text elements in root."""
    bbox = BBox()

    for el in root.iter():
        tag = _local_tag(el.tag)
        classes = set(el.get("class", "").split())

        if tag in ("svg", "g", "style", "defs", "title", "desc", "image"):
            continue

        if tag == "rect":
            w_str = el.get("width", "")
            h_str = el.get("height", "")
            if (
                "%" in w_str
                or "%" in h_str
                or "bg" in classes
                or "facsimile-bg" in classes
            ):
                continue
            x = float(el.get("x", "0"))
            y = float(el.get("y", "0"))
            w = float(w_str or "0")
            h = float(h_str or "0")
            bbox.add_box(x, y, x + w, y + h)

        elif tag == "circle":
            cx = float(el.get("cx", "0"))
            cy = float(el.get("cy", "0"))
            r = float(el.get("r", "0"))
            if r > 0:
                bbox.add_box(cx - r, cy - r, cx + r, cy + r)

        elif tag == "ellipse":
            cx = float(el.get("cx", "0"))
            cy = float(el.get("cy", "0"))
            rx = float(el.get("rx", "0"))
            ry = float(el.get("ry", "0"))
            if rx > 0 and ry > 0:
                bbox.add_box(cx - rx, cy - ry, cx + rx, cy + ry)

        elif tag == "line":
            x1 = float(el.get("x1", "0"))
            y1 = float(el.get("y1", "0"))
            x2 = float(el.get("x2", "0"))
            y2 = float(el.get("y2", "0"))
            bbox.add_box(x1, y1, x2, y2)

        elif tag in ("polygon", "polyline"):
            pts_str = el.get("points", "").strip()
            nums = [
                float(v)
                for v in re.findall(r"[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?", pts_str)
            ]
            for i in range(0, len(nums) - 1, 2):
                bbox.add_point(nums[i], nums[i + 1])

        elif tag == "path":
            d = el.get("d", "").strip()
            if d:
                _add_path_bbox(d, bbox)

        elif tag == "text":
            x = float(el.get("x", "0")) + float(el.get("dx", "0"))
            y = float(el.get("y", "0")) + float(el.get("dy", "0"))
            text_content = "".join(el.itertext()).strip()
            if not text_content:
                continue

            font_size = 11.0 if "geom-label-sm" in classes else 15.0
            char_count = max(1, len(text_content))
            w = max(0.75 * font_size, char_count * 0.68 * font_size)

            anchor = el.get("text-anchor", "start").strip()
            if anchor == "middle":
                x0, x1 = x - w / 2.0, x + w / 2.0
            elif anchor == "end":
                x0, x1 = x - w, x + 2.0
            else:
                x0, x1 = x - 2.0, x + w

            baseline = el.get("dominant-baseline", "").strip()
            has_sub = any(_local_tag(c.tag) == "tspan" for c in el)
            if baseline in ("central", "middle"):
                y0, y1 = y - 0.55 * font_size, y + (0.65 if has_sub else 0.55) * font_size
            else:
                y0, y1 = y - 0.85 * font_size, y + (0.45 if has_sub else 0.28) * font_size

            bbox.add_box(x0, y0, x1, y1)

    return bbox


def normalize_and_recalibrate_svg(
    svg_path: pathlib.Path, pad: float = 12.0, write: bool = False
) -> Tuple[bool, Tuple[float, float, float, float], Tuple[int, int, int, int]]:
    """Normalize classes/attributes, recalibrate viewBox/width/height, and update standalone <style>."""
    raw = svg_path.read_text(encoding="utf-8")
    tree = ET.ElementTree(ET.fromstring(raw))
    root = tree.getroot()

    # Skip manuscript facsimile with <image> (0003.g1.svg)
    if any(_local_tag(el.tag) == "image" for el in root.iter()):
        return False, (0, 0, 0, 0), (0, 0, 0, 0)

    old_vb_str = root.get("viewBox", "0 0 100 100")
    old_vb = tuple(float(v) for v in old_vb_str.split())  # type: ignore[assignment]

    # Inspect original <style> for per-file property overrides
    style_text = ""
    for el in root:
        if _local_tag(el.tag) == "style" and el.text:
            style_text += el.text

    clean_css = re.sub(r"/\*.*?\*/", "", style_text, flags=re.S)
    label_anchor_middle = False
    label_baseline_central = False
    label_font_11 = False
    label_font_normal = False
    label_hidden = False
    point_hidden = False
    poly_stroked = False
    aux_solid = False
    arc_dashed = False

    for rule in re.finditer(r"([^{]+)\{([^}]+)\}", clean_css):
        sel = " ".join(rule.group(1).strip().split())
        body = " ".join(rule.group(2).strip().split())
        if "hover" in sel or "highlight" in sel or "active" in sel:
            continue
        if sel in (".geom-label", ".label", ".lbl"):
            if "text-anchor: middle" in body:
                label_anchor_middle = True
            if "dominant-baseline: central" in body:
                label_baseline_central = True
            if "font-size: 11px" in body:
                label_font_11 = True
            if "font-style: normal" in body:
                label_font_normal = True
            if "opacity: 0" in body:
                label_hidden = True
        elif sel == ".geom-point":
            if "opacity: 0;" in body or body.endswith("opacity: 0"):
                point_hidden = True
        elif sel == ".geom-polygon":
            if "stroke: #000000" in body:
                poly_stroked = True
        elif sel == ".geom-aux":
            if "stroke-dasharray" not in body:
                aux_solid = True
        elif sel == ".geom-arc":
            if "stroke-dasharray" in body:
                arc_dashed = True

    # Remove full-bleed background <rect> children from root
    for child in list(root):
        if _local_tag(child.tag) == "rect":
            w_str = child.get("width", "")
            h_str = child.get("height", "")
            c_set = set(child.get("class", "").split())
            if (
                "%" in w_str
                or "%" in h_str
                or "bg" in c_set
                or "facsimile-bg" in c_set
                or (
                    len(old_vb) == 4
                    and w_str == str(int(old_vb[2]))
                    and h_str == str(int(old_vb[3]))
                )
            ):
                root.remove(child)

    # Normalize classes and attributes on all elements
    for parent in root.iter():
        parent_id = parent.get("id", "")
        in_highlights = parent_id == "highlights"
        for el in parent:
            tag = _local_tag(el.tag)
            cls_list = el.get("class", "").split()

            # Legacy class mapping (0132.g1, 0507.g1, 0512.g1)
            new_cls: list[str] = []
            for c in cls_list:
                if c in ("line", "graphic-seg"):
                    new_cls.append("geom-line")
                elif c == "element":
                    if tag == "circle":
                        new_cls.append("geom-circle")
                    elif tag == "path":
                        new_cls.append("geom-arc")
                    else:
                        new_cls.append("geom-line")
                elif c in ("poly", "graphic-poly"):
                    new_cls.append("geom-polygon")
                elif c == "graphic-wedge":
                    new_cls.extend(["wedge", "angle", "geom-overlay"])
                elif c == "point":
                    new_cls.append("geom-point")
                elif c in ("label", "lbl"):
                    new_cls.append("geom-label")
                elif c in ("highlight", "highlight-line", "highlight-poly", "highlight-point"):
                    if tag == "circle":
                        if "r" in el.attrib and float(el.get("r", "0")) <= 6:
                            new_cls.extend(["geom-point", "geom-overlay"])
                        else:
                            new_cls.extend(["geom-circle", "geom-overlay"])
                    elif tag == "polygon":
                        new_cls.extend(["geom-polygon", "geom-overlay"])
                    elif tag == "path":
                        if "Z" in el.get("d", "") or "z" in el.get("d", ""):
                            new_cls.extend(["wedge", "angle", "geom-overlay"])
                        else:
                            new_cls.extend(["geom-arc", "geom-overlay"])
                    else:
                        new_cls.extend(["geom-line", "geom-overlay"])
                elif c == "geom-aux" and aux_solid:
                    new_cls.append("geom-line")
                else:
                    new_cls.append(c)

            cls_list = list(dict.fromkeys(new_cls))

            if in_highlights and "geom-overlay" not in cls_list:
                cls_list.append("geom-overlay")

            if tag == "polygon":
                inline_style = el.get("style", "")
                if "stroke:" in inline_style:
                    del el.attrib["style"]
                    if "geom-polygon-stroked" not in cls_list:
                        cls_list.append("geom-polygon-stroked")
                if (
                    poly_stroked
                    and "geom-polygon" in cls_list
                    and "geom-overlay" not in cls_list
                    and "geom-polygon-stroked" not in cls_list
                ):
                    cls_list.append("geom-polygon-stroked")

            if arc_dashed and "geom-arc" in cls_list and "geom-arc-dashed" not in cls_list:
                cls_list.append("geom-arc-dashed")

            if tag == "circle" and point_hidden and "geom-point" in cls_list:
                if "geom-overlay" not in cls_list:
                    cls_list.append("geom-overlay")

            if tag == "text" and "geom-label" in cls_list:
                if label_anchor_middle and "text-anchor" not in el.attrib:
                    el.set("text-anchor", "middle")
                if label_baseline_central and "dominant-baseline" not in el.attrib:
                    el.set("dominant-baseline", "central")
                if label_font_11 and "geom-label-sm" not in cls_list:
                    cls_list.append("geom-label-sm")
                elif label_font_normal and "geom-label-roman" not in cls_list:
                    cls_list.append("geom-label-roman")
                if label_hidden and "geom-overlay" not in cls_list:
                    cls_list.append("geom-overlay")

            if cls_list:
                el.set("class", " ".join(cls_list))

    # Compute tight bounding box
    bbox = compute_svg_bbox(root)
    if not bbox.is_valid:
        return False, old_vb, (0, 0, 0, 0)

    vx = int(math.floor(bbox.min_x - pad))
    vy = int(math.floor(bbox.min_y - pad))
    vw = int(math.ceil(bbox.max_x + pad)) - vx
    vh = int(math.ceil(bbox.max_y + pad)) - vy
    new_vb = (vx, vy, vw, vh)

    root.set("viewBox", f"{vx} {vy} {vw} {vh}")
    root.set("width", str(vw))
    root.set("height", str(vh))
    if "euclid-graphic" not in root.get("class", ""):
        root.set("class", "euclid-graphic")
    if "data-graphic-id" not in root.attrib:
        root.set("data-graphic-id", svg_path.stem)

    # Update standalone <style> block
    style_el = None
    for child in root:
        if _local_tag(child.tag) == "style":
            style_el = child
            break
    if style_el is None:
        style_el = ET.Element(f"{{{SVG_NS}}}style")
        root.insert(0, style_el)
    style_el.text = "\n" + STANDALONE_STYLE + "\n  "

    if write:
        ET.indent(tree, space="  ")
        xml_str = ET.tostring(root, encoding="unicode")
        svg_path.write_text(xml_str + "\n", encoding="utf-8")

    return True, old_vb, new_vb


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=pathlib.Path,
        default=pathlib.Path("resources/heath"),
        help="Root directory containing Heath SVGs.",
    )
    parser.add_argument(
        "--pad",
        type=float,
        default=12.0,
        help="Uniform padding (in SVG user units) around the tight bounding box.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write recalibrated SVGs back to disk.",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    svg_files = sorted(args.root.rglob("*.svg"))
    updated = 0
    area_reductions: list[ Tuple[float, str, Tuple[float, ...], Tuple[int, ...]] ] = []

    for p in svg_files:
        ok, old_vb, new_vb = normalize_and_recalibrate_svg(
            p, pad=args.pad, write=args.write
        )
        if not ok:
            continue
        updated += 1
        if len(old_vb) == 4 and old_vb[2] > 0 and old_vb[3] > 0:
            old_area = old_vb[2] * old_vb[3]
            new_area = new_vb[2] * new_vb[3]
            ratio = new_area / old_area
            area_reductions.append((ratio, str(p), old_vb, new_vb))

    area_reductions.sort(key=lambda x: x[0])
    print(f"Processed {updated} geometric SVGs (write={args.write}, pad={args.pad}).")
    print("Top 15 SVGs with largest dead-space reduction:")
    for ratio, path_str, old_vb, new_vb in area_reductions[:15]:
        print(
            f"  {path_str}: {old_vb[0]:g} {old_vb[1]:g} {old_vb[2]:g} {old_vb[3]:g} -> "
            f"{new_vb[0]} {new_vb[1]} {new_vb[2]} {new_vb[3]} ({ratio:.1%} of original area)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
