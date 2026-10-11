"""Module for standalone OpenCV graphic detection testing."""

try:
    import cv2
except ImportError:
    cv2 = None
import json
import argparse
import numpy as np
from pathlib import Path
import os
from typing import Any, Dict
from PIL import Image
try:
    import scipy.ndimage
except ImportError:
    scipy = None

# Configuration
HEATH_DIR = Path("resources/heath")
PROPOSITIONS_DIR = HEATH_DIR / "propositions"
INDEX_PATH = HEATH_DIR / "volume_I/book_i/propositions/index.json"


def load_json(path: Path) -> Any:  # noqa: ANN401
    """Loads JSON data from a file."""
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return []


def detect_graphic_scipy(image_path: Path, debug: bool = False) -> Dict[str, Any]:
    """Detects graphics using pure NumPy and SciPy algorithms."""
    try:
        pil_img = Image.open(str(image_path)).convert("L")
    except Exception as e:
        return {"error": f"Could not load image: {e}"}

    gray = np.array(pil_img)

    # 1. Otsu thresholding
    hist, _ = np.histogram(gray, bins=256, range=(0, 256))
    total = gray.size
    sum_total = np.dot(np.arange(256), hist)
    curr_max, thresh = 0, 0
    wb, sb = 0, 0
    for i in range(256):
        wb += hist[i]
        if wb == 0:
            continue
        wf = total - wb
        if wf == 0:
            break
        sb += i * hist[i]
        mb = sb / wb
        mf = (sum_total - sb) / wf
        var_b = wb * wf * (mb - mf) ** 2
        if var_b > curr_max:
            curr_max = var_b
            thresh = i

    binary = (gray < thresh)

    # 2. Connected components
    labels, num_labels = scipy.ndimage.label(binary, structure=np.ones((3, 3)))
    slices = scipy.ndimage.find_objects(labels)

    MIN_GRAPHIC_DIM = 60
    MAX_TEXT_HEIGHT = 40
    MIN_TEXT_WIDTH = 100

    large_components = []
    core_mask = np.zeros_like(binary, dtype=bool)

    for idx, sl in enumerate(slices):
        if sl is None:
            continue
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start

        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue

        if w > MIN_GRAPHIC_DIM or h > MIN_GRAPHIC_DIM:
            large_components.append(idx + 1)
            core_mask[labels == (idx + 1)] = True

    if not large_components:
        return {"error": "No large graphic components found"}

    pts_y, pts_x = np.where(core_mask)
    gx, gy = pts_x.min(), pts_y.min()
    gw, gh = pts_x.max() - gx + 1, pts_y.max() - gy + 1

    LABEL_SEARCH_MARGIN = 20
    sx = max(0, gx - LABEL_SEARCH_MARGIN)
    sy = max(0, gy - LABEL_SEARCH_MARGIN)
    sw = gw + 2 * LABEL_SEARCH_MARGIN
    sh = gh + 2 * LABEL_SEARCH_MARGIN

    final_mask = core_mask.copy()
    for idx, sl in enumerate(slices):
        label_id = idx + 1
        if label_id in large_components:
            continue
        if sl is None:
            continue
        h = sl[0].stop - sl[0].start
        w = sl[1].stop - sl[1].start

        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue

        cx = sl[1].start + w / 2
        cy = sl[0].start + h / 2

        if (sx <= cx <= sx + sw) and (sy <= cy <= sy + sh):
            final_mask[labels == label_id] = True

    pts_y, pts_x = np.where(final_mask)
    gx, gy = pts_x.min(), pts_y.min()
    gw, gh = pts_x.max() - gx + 1, pts_y.max() - gy + 1

    PADDING = 10
    height, width = gray.shape

    gx = max(0, gx - PADDING)
    gy = max(0, gy - PADDING)
    gw = min(width - gx, gw + 2 * PADDING)
    gh = min(height - gy, gh + 2 * PADDING)

    return {"x_offset": int(gx), "y_offset": int(gy), "crop_box": [int(gw), int(gh)]}


def detect_graphic_cv(image_path: Path, debug: bool = False) -> Dict[str, Any]:
    """Detects graphics in an image using OpenCV or SciPy fallback."""
    if cv2 is None:
        return detect_graphic_scipy(image_path, debug=debug)

    # Load image
    img = cv2.imread(str(image_path))
    if img is None:
        return {"error": "Could not load image"}

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1. Binarize (Invert so ink is white, paper is black)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 2. Connected Components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binary, connectivity=8
    )

    graphics_mask = np.zeros_like(binary)

    large_components = []

    # Thresholds
    MIN_GRAPHIC_DIM = 60
    MAX_TEXT_HEIGHT = 40
    MIN_TEXT_WIDTH = 100

    # Step A: Find the "Core" (the actual drawing)
    for i in range(1, num_labels):
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue

        if w > MIN_GRAPHIC_DIM or h > MIN_GRAPHIC_DIM:
            large_components.append(i)
            graphics_mask[labels == i] = 255

    if not large_components:
        return {"error": "No large graphic components found"}

    # Step B: Bounding box of the core
    points = cv2.findNonZero(graphics_mask)
    if points is None:
        return {"error": "Mask empty"}

    gx, gy, gw, gh = cv2.boundingRect(points)

    # Step C: Add nearby labels
    LABEL_SEARCH_MARGIN = 20

    search_x = max(0, gx - LABEL_SEARCH_MARGIN)
    search_y = max(0, gy - LABEL_SEARCH_MARGIN)
    search_w = gw + 2 * LABEL_SEARCH_MARGIN
    search_h = gh + 2 * LABEL_SEARCH_MARGIN

    final_mask = graphics_mask.copy()

    for i in range(1, num_labels):
        if i in large_components:
            continue

        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        if w > MIN_TEXT_WIDTH and h < MAX_TEXT_HEIGHT:
            continue

        cx = x + w / 2
        cy = y + h / 2

        if (search_x <= cx <= search_x + search_w) and (
            search_y <= cy <= search_y + search_h
        ):
            final_mask[labels == i] = 255

    points = cv2.findNonZero(final_mask)
    gx, gy, gw, gh = cv2.boundingRect(points)

    PADDING = 10
    height, width = img.shape[:2]

    gx = max(0, gx - PADDING)
    gy = max(0, gy - PADDING)
    gw = min(width - gx, gw + 2 * PADDING)
    gh = min(height - gy, gh + 2 * PADDING)

    if debug:
        debug_img = img.copy()
        cv2.rectangle(debug_img, (gx, gy), (gx + gw, gy + gh), (0, 0, 255), 2)
        debug_path = f"debug_{Path(image_path).name}"
        cv2.imwrite(debug_path, debug_img)
        print(f"Saved debug image to {debug_path}")

    return {"x_offset": int(gx), "y_offset": int(gy), "crop_box": [int(gw), int(gh)]}


def run_test() -> None:
    """Runs a test of the graphic detection against known ground truth."""
    print("Running Graphic Detection Test")
    propositions = load_json(INDEX_PATH)
    prop_map = {p["id"]: p for p in propositions}

    target_props = ["I.1", "I.2", "I.3"]

    for prop_id in target_props:
        print(f"\nProcessing {prop_id}...")
        prop_data = prop_map.get(prop_id)

        gt_graphics = prop_data.get("graphics", [{}])[0]
        print(f"  Ground Truth: {gt_graphics}")

        image_path = PROPOSITIONS_DIR / f"{prop_id}.png"
        if not image_path.exists():
            print("  Image not found")
            continue

        result = detect_graphic_cv(image_path, debug=False)
        print(f"  Detected:     {result}")

        if "error" not in result:
            gt_x = gt_graphics.get("x_offset", 0)
            gt_y = gt_graphics.get("y_offset", 0)
            gt_w, gt_h = gt_graphics.get("crop_box", [0, 0])

            d_x = result["x_offset"] - gt_x
            d_y = result["y_offset"] - gt_y
            d_w = result["crop_box"][0] - gt_w
            d_h = result["crop_box"][1] - gt_h

            print(f"  Diff: x={d_x:+d}, y={d_y:+d}, w={d_w:+d}, h={d_h:+d}")


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Detect graphic coordinates in an image.")
    parser.add_argument("image", nargs="?", type=str, help="Path to image file to scan")
    parser.add_argument("--test", action="store_true", help="Run ground truth test")
    args = parser.parse_args()

    if args.image:
        res = detect_graphic_cv(Path(args.image))
        print(json.dumps(res, indent=2))
    else:
        run_test()


if __name__ == "__main__":
    main()
