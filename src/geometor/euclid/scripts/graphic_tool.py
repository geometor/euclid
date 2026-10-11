"""Command-line utility for graphic detection, cropping, zooming, and XML reference validation."""

import argparse
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageOps

from geometor.euclid.ingest.cleanup import clean_image
from geometor.euclid.ingest.detect_graphics_cv import detect_graphic_cv


def cmd_detect(args: argparse.Namespace) -> None:
    """Detect graphic bounding box on an image."""
    img_path = Path(args.image)
    if not img_path.exists():
        print(f"Error: image not found at {img_path}", file=sys.stderr)
        sys.exit(1)

    result = detect_graphic_cv(img_path, debug=args.debug)
    print(json.dumps(result, indent=2))


def cmd_crop(args: argparse.Namespace) -> None:
    """Crop, clean, and optionally invert a graphic from a page image."""
    src_path = Path(args.image)
    out_path = Path(args.output)

    if not src_path.exists():
        print(f"Error: image not found at {src_path}", file=sys.stderr)
        sys.exit(1)

    img = Image.open(src_path)

    # Determine bounding box
    if args.bbox:
        x, y, w, h = args.bbox
    elif args.offsets:
        # Heath index format: x_offset, y_offset, w, h
        x, y, w, h = args.offsets
    else:
        # Auto-detect
        res = detect_graphic_cv(src_path)
        if "error" in res:
            print(f"Error auto-detecting graphic: {res['error']}", file=sys.stderr)
            sys.exit(1)
        x = res["x_offset"]
        y = res["y_offset"]
        w, h = res["crop_box"]
        print(f"Auto-detected bbox: x={x}, y={y}, w={w}, h={h}")

    # Crop
    crop_box = (x, y, x + w, y + h)
    cropped = img.crop(crop_box)

    # Clean (levels adjustment to remove paper bleed-through)
    if not args.no_clean:
        cropped = clean_image(cropped, white_point=args.white_point)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(out_path)
    print(f"Saved cropped graphic to: {out_path}")

    # Invert / Dark background
    inverted_name = None
    if args.invert:
        inverted = ImageOps.invert(cropped.convert("RGB"))
        inverted_path = out_path.with_name(f"{out_path.stem}.inverted{out_path.suffix}")
        inverted.save(inverted_path)
        inverted_name = inverted_path.name
        print(f"Saved inverted graphic to: {inverted_path}")

    # Markdown tag helper
    caption = args.caption or out_path.stem.replace("_", " ").title()

    # Save crop info metadata JSON (<folio>.json)
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
    if not isinstance(metadata, dict):
        metadata = {}

    graphics_list = metadata.get("graphics", [])
    entry = {
        "id": graphic_subid,
        "file": out_path.name,
        "inverted_file": inverted_name,
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

    # Build target query
    target = args.ref.strip().lower()
    # Normalize query: e.g. "1", "prop.1", "elem.1.1", "def.4", "post.1", "cn.1"
    matched_elements = []

    # If user passed just a number e.g. "1", assume proposition: "elem.B.N"
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
        description="Euclid Graphic & XML Transcription Helper Tools"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # detect
    p_detect = subparsers.add_parser("detect", help="Auto-detect graphic bounding box")
    p_detect.add_argument("image", help="Scan PNG to process")
    p_detect.add_argument("--debug", action="store_true", help="Save debug visualization")
    p_detect.set_defaults(func=cmd_detect)

    # crop
    p_crop = subparsers.add_parser("crop", help="Crop graphic with cleanup and dark mode")
    p_crop.add_argument("image", help="Source page scan PNG")
    p_crop.add_argument("output", help="Output PNG file path")
    p_crop.add_argument(
        "--bbox", nargs=4, type=int, metavar=("X", "Y", "W", "H"), help="Exact bounding box [x y w h]"
    )
    p_crop.add_argument(
        "--offsets", nargs=4, type=int, metavar=("X", "Y", "W", "H"), help="Offsets from index.json"
    )
    p_crop.add_argument(
        "--white-point", type=int, default=226, help="Linear levels white point threshold (default 226)"
    )
    p_crop.add_argument("--no-clean", action="store_true", help="Skip bleed-through level adjustment")
    p_crop.add_argument("--invert", action="store_true", help="Generate negative (inverted) image for dark mode")
    p_crop.add_argument("--caption", type=str, help="Caption for markdown embed tag")
    p_crop.set_defaults(func=cmd_crop)

    # zoom
    p_zoom = subparsers.add_parser("zoom", help="Crop hard-to-read area to isolate and magnify")
    p_zoom.add_argument("image", help="Source page scan PNG")
    p_zoom.add_argument("output", help="Output scratch PNG path")
    p_zoom.add_argument(
        "--bbox", nargs=4, type=int, required=True, metavar=("X", "Y", "W", "H"), help="Bounding box [x y w h]"
    )
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
