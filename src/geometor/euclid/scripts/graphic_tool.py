"""Command-line utility for graphic detection, cropping, zooming, and XML reference validation."""

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageOps

from geometor.euclid.ingest.cleanup import clean_image
from geometor.euclid.ingest.detect_graphics_cv import detect_graphics_cv


def detect_single_image(img_path: Path, save: bool = False, force: bool = False, debug: bool = False) -> None:
    """Detect graphic bounding box(es) on a single folio scan and optionally save <folio>.json."""
    if not img_path.exists():
        print(f"Error: image not found at {img_path}", file=sys.stderr)
        return

    folio_stem = img_path.stem
    json_path = img_path.with_name(f"{folio_stem}.json")
    md_path = img_path.with_name(f"{folio_stem}.md")
    if save and json_path.exists() and not force:
        print(f"Skipping {json_path} (already exists). Use --force to overwrite.")
        return
    if save and md_path.exists() and not json_path.exists() and not force:
        metadata = {"folio": folio_stem, "graphics": []}
        with open(json_path, "w") as f:
            f.write(json.dumps(metadata, indent=2) + "\n")
        print(f"Saved empty graphics {json_path} (transcribed text-only folio).")
        return

    results = detect_graphics_cv(img_path, debug=debug)

    graphics: List[Dict[str, Any]] = []
    for idx, result in enumerate(results, start=1):
        gid = f"g{idx}"
        x = result["x_offset"]
        y = result["y_offset"]
        w, h = result["crop_box"]
        graphics.append({
            "id": gid,
            "file": f"{folio_stem}.{gid}.png",
            "bbox": [x, y, w, h],
            "white_point": 226,
            "caption": f"Folio {folio_stem} Figure {idx}"
        })

    metadata = {
        "folio": folio_stem,
        "graphics": graphics
    }

    output_json = json.dumps(metadata, indent=2)
    if not save:
        print(output_json)
    else:
        with open(json_path, "w") as f:
            f.write(output_json + "\n")
        print(f"Saved {json_path} ({len(graphics)} graphic(s))")


def cmd_detect(args: argparse.Namespace) -> None:
    """Detect graphic bounding box on one or more images or directories."""
    for target_str in args.targets:
        target = Path(target_str)
        if target.is_dir():
            png_files = sorted(
                p for p in target.rglob("*.png")
                if "." not in p.stem and p.stem.isdigit()
            )
            for pf in png_files:
                detect_single_image(pf, save=args.save, force=args.force, debug=args.debug)
        elif target.suffix == ".png":
            detect_single_image(target, save=args.save, force=args.force, debug=args.debug)
        else:
            print(f"Error: Unknown target format: {target}", file=sys.stderr)


def extract_from_json(json_path: Path, no_clean: bool = False) -> None:
    """Extract all graphics defined in a <folio>.json file from the corresponding folio scan."""
    if not json_path.exists():
        print(f"Error: JSON file not found at {json_path}", file=sys.stderr)
        return

    with open(json_path, "r") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"Error parsing JSON {json_path}: {e}", file=sys.stderr)
            return

    if isinstance(data, list):
        if not json_path.stem.isdigit():
            return
        folio = json_path.stem
        graphics = data
    elif isinstance(data, dict):
        folio = data.get("folio", json_path.stem)
        graphics = data.get("graphics", [])
    else:
        return

    normalized_changed = isinstance(data, list)
    for idx, g in enumerate(graphics, start=1):
        gid = str(g.get("id", f"g{idx}"))
        if not gid.startswith("g"):
            gid = f"g{gid}"
            normalized_changed = True
        g["id"] = gid
        if "bbox" not in g and "box" in g:
            g["bbox"] = g.pop("box")
            normalized_changed = True
    if normalized_changed:
        with open(json_path, "w") as f:
            json.dump({"folio": folio, "graphics": graphics}, f, indent=2)
            f.write("\n")

    # Remove any stale extracted .g*.png files for this folio that are no longer in graphics
    expected_files = set()
    for g in graphics:
        gid = g.get("id", "g1")
        expected_files.add(g.get("file", f"{folio}.{gid}.png"))
    for existing in json_path.parent.glob(f"{folio}.g*.png"):
        if existing.name not in expected_files:
            existing.unlink()
            print(f"  Removed stale graphic: {existing}")

    img_path = json_path.with_name(f"{folio}.png")
    if not img_path.exists():
        print(f"Error: Source image not found at {img_path}", file=sys.stderr)
        return

    if not graphics:
        print(f"Folio {folio}: No graphics defined in {json_path.name}")
        return

    print(f"\n=== Extracting {len(graphics)} graphic(s) for folio {folio} ===")
    img = Image.open(img_path)
    img_w, img_h = img.size

    for g in graphics:
        gid = g.get("id", "g1")
        bbox = g.get("bbox")
        if not bbox or len(bbox) != 4:
            print(f"Error: invalid bbox {bbox} for graphic {gid}", file=sys.stderr)
            continue

        x, y, w, h = bbox
        if x < 0 or y < 0 or x + w > img_w or y + h > img_h or w <= 0 or h <= 0:
            print(f"Warning: bbox {bbox} exceeds image boundaries {img_w}x{img_h}", file=sys.stderr)

        crop_box = (max(0, x), max(0, y), min(img_w, x + w), min(img_h, y + h))
        cropped = img.crop(crop_box)

        # Levels cleanup
        white_point = g.get("white_point", 226)
        if not no_clean and white_point is not None:
            cropped = clean_image(cropped, white_point=white_point)

        out_name = g.get("file", f"{folio}.{gid}.png")
        out_path = json_path.parent / out_name
        cropped.save(out_path)
        print(f"  Saved: {out_path} (bbox: [{x}, {y}, {w}, {h}])")

        caption = g.get("caption", f"Folio {folio} {gid}")
        print(f"  Markdown: ![{caption}]({out_name})")


def cmd_extract(args: argparse.Namespace) -> None:
    """Extract graphics from one or more <folio>.json or <folio>.png targets."""
    for target_str in args.targets:
        target = Path(target_str)
        if target.is_dir():
            json_files = sorted(
                jf for jf in target.rglob("*.json")
                if "." not in jf.stem and jf.stem.isdigit()
            )
            for jf in json_files:
                extract_from_json(jf, no_clean=args.no_clean)
        elif target.suffix == ".json":
            extract_from_json(target, no_clean=args.no_clean)
        elif target.suffix == ".png":
            json_path = target.with_suffix(".json")
            if json_path.exists():
                extract_from_json(json_path, no_clean=args.no_clean)
            else:
                print(f"Error: No matching JSON file found at {json_path}. Run 'detect --save' or create it first.", file=sys.stderr)
        else:
            print(f"Error: Unknown target format: {target}", file=sys.stderr)


def cmd_set(args: argparse.Namespace) -> None:
    """Set or update graphic metadata in <folio>.json."""
    target = Path(args.target)
    if target.suffix == ".png":
        json_path = target.with_suffix(".json")
        folio = target.stem
    elif target.suffix == ".json":
        json_path = target
        folio = target.stem
    else:
        json_path = Path(f"{args.target}.json")
        folio = Path(args.target).stem

    metadata: Dict[str, Any] = {}
    if json_path.exists():
        try:
            with open(json_path, "r") as f:
                metadata = json.load(f)
        except Exception:
            metadata = {}

    metadata["folio"] = folio
    graphics = metadata.get("graphics", [])
    gid = args.id

    existing_entry = next((g for g in graphics if g.get("id") == gid), {})
    existing_entry.pop("inverted_file", None)
    entry = {
        **existing_entry,
        "id": gid,
        "file": f"{folio}.{gid}.png",
        "bbox": list(args.bbox),
        "white_point": args.white_point,
        "caption": args.caption or existing_entry.get("caption") or f"Folio {folio} Figure {gid.replace('g', '')}",
    }

    # Replace or add
    graphics = [g for g in graphics if g.get("id") != gid]
    graphics.append(entry)
    metadata["graphics"] = graphics

    with open(json_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Updated {json_path} with graphic {gid}: bbox={args.bbox}")

    if args.extract:
        extract_from_json(json_path)


def cmd_crop(args: argparse.Namespace) -> None:
    """Crop and clean a graphic from a page image (legacy command)."""
    src_path = Path(args.image)
    out_path = Path(args.output)

    if not src_path.exists():
        print(f"Error: image not found at {src_path}", file=sys.stderr)
        sys.exit(1)

    img = Image.open(src_path)

    if args.bbox:
        x, y, w, h = args.bbox
    elif args.offsets:
        x, y, w, h = args.offsets
    else:
        res = detect_graphic_cv(src_path)
        if "error" in res:
            print(f"Error auto-detecting graphic: {res['error']}", file=sys.stderr)
            sys.exit(1)
        x = res["x_offset"]
        y = res["y_offset"]
        w, h = res["crop_box"]

    crop_box = (x, y, x + w, y + h)
    cropped = img.crop(crop_box)

    if not args.no_clean:
        cropped = clean_image(cropped, white_point=args.white_point)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(out_path)
    print(f"Saved cropped graphic to: {out_path}")

    caption = args.caption or out_path.stem.replace("_", " ").title()

    folio_stem = out_path.name.split(".")[0]
    graphic_subid = out_path.name.split(".")[1] if out_path.name.count(".") >= 2 else "g1"
    json_path = out_path.parent / f"{folio_stem}.json"
    metadata: Dict[str, Any] = {}
    if json_path.exists():
        try:
            with open(json_path, "r") as jf:
                metadata = json.load(jf)
        except Exception:
            metadata = {}

    graphics_list = metadata.get("graphics", [])
    entry = {
        "id": graphic_subid,
        "file": out_path.name,
        "bbox": [x, y, w, h],
        "white_point": args.white_point if not args.no_clean else None,
        "caption": caption,
    }
    graphics_list = [g for g in graphics_list if g.get("id") != graphic_subid]
    graphics_list.append(entry)
    metadata["folio"] = folio_stem
    metadata["graphics"] = graphics_list

    with open(json_path, "w") as jf:
        json.dump(metadata, jf, indent=2)
    print(f"Updated crop metadata in: {json_path}")
    print(f"\nMarkdown snippet:\n![{caption}]({out_path.name})")


def cmd_zoom(args: argparse.Namespace) -> None:
    """Crop an arbitrary region of interest to eliminate distraction for reading difficult text/symbols."""
    src_path = Path(args.image)
    out_path = Path(args.output)

    if not src_path.exists():
        print(f"Error: image not found at {src_path}", file=sys.stderr)
        sys.exit(1)

    img = Image.open(src_path)
    x, y, w, h = args.bbox
    crop_box = (x, y, x + w, y + h)
    cropped = img.crop(crop_box)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(out_path)
    print(f"Saved zoomed region ({w}x{h} at [{x}, {y}]) to: {out_path}")


def cmd_xml(args: argparse.Namespace) -> None:
    """Extract reference translation and Greek critical notes from TEI XML."""
    book_num = int(args.book)
    xml_filename = f"{book_num:02d}.xml"
    xml_path = Path("resources/xml/books") / xml_filename

    if not xml_path.exists():
        print(f"Error: XML file {xml_path} not found", file=sys.stderr)
        sys.exit(1)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    def get_text(elem: ET.Element) -> str:
        return " ".join("".join(elem.itertext()).split())

    target = args.ref.strip().lower()
    matched_elements = []

    candidate_ids = [target]
    if target.isdigit():
        candidate_ids.extend([f"elem.{book_num}.{target}", f"elem.{book_num}.prop.{target}"])
    elif target.startswith("prop."):
        num = target.split("prop.")[1]
        candidate_ids.append(f"elem.{book_num}.{num}")
    elif target.startswith("def."):
        num = target.split("def.")[1]
        candidate_ids.append(f"elem.{book_num}.def.{num}")
    elif target.startswith("post."):
        num = target.split("post.")[1]
        candidate_ids.append(f"elem.{book_num}.post.{num}")
    elif target.startswith("cn."):
        num = target.split("cn.")[1]
        candidate_ids.extend([f"elem.{book_num}.c.n.{num}", f"elem.{book_num}.cn.{num}"])

    for div3 in root.iter("div3"):
        div_id = div3.get("id", "").lower()
        if div_id in candidate_ids:
            matched_elements.append(div3)

    if not matched_elements:
        print(f"No element matching '{args.ref}' found in Book {book_num}.", file=sys.stderr)
        sys.exit(1)

    for elem in matched_elements:
        print("=" * 60)
        print(f"ID: {elem.get('id')}  (n={elem.get('n')})")
        head = elem.find("head")
        if head is not None:
            print(f"Heading: {get_text(head)}")

        for child in elem:
            if child.tag == "div4":
                t = child.get("type", "")
                print(f"\n[{t.upper()}]:\n{get_text(child)}")
            elif child.tag == "p":
                print(f"\n[TEXT]:\n{get_text(child)}")
            elif child.tag == "note":
                note_n = child.get("n", "")
                print(f"\n[NOTE {note_n}]:\n{get_text(child)}")
        print("=" * 60)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Euclid Graphic & XML Helper Tools (Two-Step JSON-Driven Extraction)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # detect
    p_detect = subparsers.add_parser("detect", help="Auto-detect graphic and output/save <folio>.json")
    p_detect.add_argument("targets", nargs="+", help="Path(s) to scan PNG(s) or directory")
    p_detect.add_argument("--save", action="store_true", help="Save detected metadata to <folio>.json next to image")
    p_detect.add_argument("--force", action="store_true", help="Overwrite existing <folio>.json")
    p_detect.add_argument("--debug", action="store_true", help="Save debug visualization")
    p_detect.set_defaults(func=cmd_detect)

    # extract
    p_extract = subparsers.add_parser("extract", help="Extract graphics from scan based on <folio>.json")
    p_extract.add_argument("targets", nargs="+", help="Path(s) to <folio>.json, <folio>.png, or directory")
    p_extract.add_argument("--no-clean", action="store_true", help="Skip bleed-through levels adjustment")
    p_extract.add_argument("--no-invert", action="store_true", help="Skip generating inverted dark mode image")
    p_extract.set_defaults(func=cmd_extract)

    # set
    p_set = subparsers.add_parser("set", help="Set or update graphic metadata in <folio>.json")
    p_set.add_argument("target", help="Path to <folio>.png, <folio>.json, or folio stem")
    p_set.add_argument("--id", default="g1", help="Graphic ID (default: g1)")
    p_set.add_argument("--bbox", nargs=4, type=int, required=True, metavar=("X", "Y", "W", "H"), help="Bounding box [x y w h]")
    p_set.add_argument("--caption", type=str, help="Caption for markdown embed tag")
    p_set.add_argument("--white-point", type=int, default=226, help="White point threshold (default: 226)")
    p_set.add_argument("--extract", action="store_true", help="Immediately run extraction after updating JSON")
    p_set.set_defaults(func=cmd_set)

    # crop (legacy)
    p_crop = subparsers.add_parser("crop", help="Crop graphic directly (legacy)")
    p_crop.add_argument("image", help="Source page scan PNG")
    p_crop.add_argument("output", help="Output PNG file path")
    p_crop.add_argument("--bbox", nargs=4, type=int, metavar=("X", "Y", "W", "H"), help="Exact bounding box [x y w h]")
    p_crop.add_argument("--offsets", nargs=4, type=int, metavar=("X", "Y", "W", "H"), help="Offsets [x y w h]")
    p_crop.add_argument("--white-point", type=int, default=226, help="White point threshold")
    p_crop.add_argument("--no-clean", action="store_true", help="Skip bleed-through adjustment")
    p_crop.add_argument("--invert", action="store_true", help="Generate inverted image")
    p_crop.add_argument("--caption", type=str, help="Caption")
    p_crop.set_defaults(func=cmd_crop)

    # zoom
    p_zoom = subparsers.add_parser("zoom", help="Crop hard-to-read area to isolate and magnify")
    p_zoom.add_argument("image", help="Source page scan PNG")
    p_zoom.add_argument("output", help="Output scratch PNG path")
    p_zoom.add_argument("--bbox", nargs=4, type=int, required=True, metavar=("X", "Y", "W", "H"), help="Bounding box [x y w h]")
    p_zoom.set_defaults(func=cmd_zoom)

    # xml
    p_xml = subparsers.add_parser("xml", help="Query Perseus TEI XML for core text and notes")
    p_xml.add_argument("book", type=int, help="Book number (1-13)")
    p_xml.add_argument("ref", help="Reference ID (e.g. '1', 'prop.1', 'def.4', 'post.1')")
    p_xml.set_defaults(func=cmd_xml)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
