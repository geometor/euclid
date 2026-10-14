"""Flask application for reviewing Euclid folios, transcriptions, notes, and graphics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Optional

from flask import (
    Flask,
    abort,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from geometor.euclid.folio_review.reviews import ReviewManager
from geometor.euclid.folio_review.scanner import FolioScanner
from geometor.euclid.scripts.graphic_tool import extract_from_json


def create_app(heath_dir: Optional[Path] = None, reviews_path: Optional[Path] = None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    scanner = FolioScanner(root_dir=heath_dir)
    review_mgr = ReviewManager(storage_path=reviews_path)

    @app.route("/")
    def index():
        """Dashboard overview and folio browser."""
        stats = scanner.get_stats()
        rev_stats = review_mgr.get_review_stats()
        volumes = scanner.get_volumes()
        return render_template(
            "dashboard.html",
            stats=stats,
            rev_stats=rev_stats,
            volumes=volumes,
        )

    def _serve_media_file(volume_id: str, filename: str):
        actual_name = Path(filename).name
        # 1. Try to find via folio stem (e.g. 0314.g1.png -> folio 0314)
        stem = actual_name.split(".")[0]
        if stem.isdigit():
            target_folio = f"{int(stem):04d}"
            f_data = scanner.get_folio(volume_id, target_folio)
            if f_data:
                p_dir = scanner.root_dir / f_data["volume"] / f_data["section_path"]
                candidate = p_dir / actual_name
                if candidate.exists():
                    return send_from_directory(p_dir, actual_name)

        # 2. Search anywhere within the volume directory
        vol_dir = scanner.root_dir / volume_id
        if vol_dir.exists():
            found = list(vol_dir.rglob(actual_name))
            if found:
                return send_from_directory(found[0].parent, found[0].name)

        # 3. Search anywhere inside root_dir
        found = list(scanner.root_dir.rglob(actual_name))
        if found:
            return send_from_directory(found[0].parent, found[0].name)

        abort(404)

    @app.route("/folio/<volume_id>/<folio_id>")
    def review_folio(volume_id: str, folio_id: str):
        """Side-by-side interactive review workspace for a folio."""
        # Handle relative image requests that resolved to /folio/<vol>/<img_file>
        ext = Path(folio_id).suffix.lower()
        if ext in [".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"]:
            return _serve_media_file(volume_id, folio_id)

        folio_data = scanner.get_folio(volume_id, folio_id)
        if not folio_data:
            abort(404, description=f"Folio {folio_id} in {volume_id} not found")

        review_data = review_mgr.get_review(volume_id, folio_id)
        prev_folio, next_folio = scanner.get_adjacent_folios(volume_id, folio_id)

        return render_template(
            "folio.html",
            folio=folio_data,
            review=review_data,
            prev_folio=prev_folio,
            next_folio=next_folio,
        )

    @app.route("/folio/<volume_id>/<folio_id>/<path:filename>")
    def serve_nested_relative_media(volume_id: str, folio_id: str, filename: str):
        """Handle relative image requests that resolved to /folio/<vol>/<fol>/<img_file>."""
        ext = Path(filename).suffix.lower()
        if ext in [".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"]:
            return _serve_media_file(volume_id, filename)
        abort(404)

    @app.route("/media/<path:rel_path>")
    def serve_media(rel_path: str):
        """Serve folio scans and extracted crop images securely from resources/heath/."""
        safe_path = Path(rel_path)
        # Prevent path traversal
        try:
            full_path = (scanner.root_dir / safe_path).resolve()
            if not str(full_path).startswith(str(scanner.root_dir.resolve())):
                abort(403)
            if not full_path.exists():
                abort(404)
            return send_from_directory(full_path.parent, full_path.name)
        except Exception:
            abort(404)

    # --- JSON APIs ---

    @app.route("/api/stats")
    def api_stats():
        """Return aggregated statistics."""
        stats = scanner.get_stats()
        stats["review"] = review_mgr.get_review_stats()
        return jsonify(stats)

    @app.route("/api/folios")
    def api_folios():
        """Return list of folios with optional filtering."""
        volume_id = request.args.get("volume")
        section = request.args.get("section")
        filter_status = request.args.get("status")
        review_status = request.args.get("review_status")
        search = request.args.get("q")

        folios = scanner.get_folios(
            volume_id=volume_id,
            section=section,
            filter_status=filter_status,
            search_query=search,
        )

        all_reviews = review_mgr.get_all_reviews()

        # Attach review status to each folio item
        enriched = []
        for f in folios:
            key = f"{f['volume']}:{f['folio']}"
            rev = all_reviews.get(key, {"status": "unreviewed"})
            f_copy = dict(f)
            f_copy["review_status"] = rev.get("status", "unreviewed")
            f_copy["review_notes"] = rev.get("notes", "")

            # Filter by review status if requested
            if review_status and review_status != "all" and f_copy["review_status"] != review_status:
                continue

            enriched.append(f_copy)

        return jsonify({"count": len(enriched), "folios": enriched})

    @app.route("/api/folio/<volume_id>/<folio_id>")
    def api_get_folio(volume_id: str, folio_id: str):
        """Return full data for a single folio."""
        folio_data = scanner.get_folio(volume_id, folio_id)
        if not folio_data:
            return jsonify({"error": "Folio not found"}), 404

        folio_data["review"] = review_mgr.get_review(volume_id, folio_id)
        prev_f, next_f = scanner.get_adjacent_folios(volume_id, folio_id)
        folio_data["prev_folio"] = prev_f
        folio_data["next_folio"] = next_f
        return jsonify(folio_data)

    @app.route("/api/folio/<volume_id>/<folio_id>/review", methods=["POST"])
    def api_update_review(volume_id: str, folio_id: str):
        """Update review status, checklist, and notes."""
        payload = request.get_json(force=True) or {}
        status = payload.get("status", "unreviewed")
        checklist = payload.get("checklist", {})
        notes = payload.get("notes", "")
        reviewer = payload.get("reviewer", "phi")

        record = review_mgr.set_review(
            volume=volume_id,
            folio=folio_id,
            status=status,
            checklist=checklist,
            notes=notes,
            reviewer=reviewer,
        )
        return jsonify({"success": True, "review": record})

    @app.route("/api/folio/<volume_id>/<folio_id>/save_text", methods=["POST"])
    def api_save_text(volume_id: str, folio_id: str):
        """Save edited markdown or notes text to disk."""
        payload = request.get_json(force=True) or {}
        target = payload.get("target")  # "md" or "notes"
        content = payload.get("content", "")

        folio_data = scanner.get_folio(volume_id, folio_id)
        if not folio_data:
            return jsonify({"error": "Folio not found"}), 404

        parent_dir = scanner.root_dir / folio_data["volume"] / folio_data["section_path"]

        if target == "md":
            file_path = parent_dir / f"{folio_data['folio']}.md"
        elif target == "notes":
            file_path = parent_dir / f"{folio_data['folio']}.notes.md"
        else:
            return jsonify({"error": "Invalid target type (must be 'md' or 'notes')"}), 400

        try:
            file_path.write_text(content, encoding="utf-8")
            # Invalidate scanner cache
            scanner.refresh(force=True)
            return jsonify({"success": True, "file": str(file_path.name)})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/api/folio/<volume_id>/<folio_id>/extract_graphics", methods=["POST"])
    def api_extract_graphics(volume_id: str, folio_id: str):
        """Trigger crop extraction for a folio using graphic_tool."""
        folio_data = scanner.get_folio(volume_id, folio_id)
        if not folio_data:
            return jsonify({"error": "Folio not found"}), 404

        parent_dir = scanner.root_dir / folio_data["volume"] / folio_data["section_path"]
        json_path = parent_dir / f"{folio_data['folio']}.json"

        if not json_path.exists():
            return jsonify({"error": f"JSON definition {json_path.name} does not exist"}), 400

        try:
            extract_from_json(json_path)
            scanner.refresh(force=True)
            updated_folio = scanner.get_folio(volume_id, folio_id)
            return jsonify({
                "success": True,
                "graphics": updated_folio.get("graphics", []) if updated_folio else [],
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/api/folio/<volume_id>/<folio_id>/update_graphic_bbox", methods=["POST"])
    def api_update_graphic_bbox(volume_id: str, folio_id: str):
        """Update or add a graphic bbox in <folio>.json and optionally re-extract."""
        payload = request.get_json(force=True) or {}
        gid = payload.get("id", "g1")
        bbox = payload.get("bbox")  # [x, y, w, h]
        white_point = payload.get("white_point", 226)
        caption = payload.get("caption")
        trigger_extract = payload.get("extract", True)

        if not bbox or len(bbox) != 4:
            return jsonify({"error": "bbox must be [x, y, w, h]"}), 400

        folio_data = scanner.get_folio(volume_id, folio_id)
        if not folio_data:
            return jsonify({"error": "Folio not found"}), 404

        parent_dir = scanner.root_dir / folio_data["volume"] / folio_data["section_path"]
        json_path = parent_dir / f"{folio_data['folio']}.json"

        metadata = {}
        if json_path.exists():
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
            except Exception:
                metadata = {}

        metadata["folio"] = folio_data["folio"]
        graphics = metadata.get("graphics", [])

        existing_entry = next((g for g in graphics if g.get("id") == gid), {})
        entry = dict(existing_entry)
        entry.update({
            "id": gid,
            "file": existing_entry.get("file", f"{folio_data['folio']}.{gid}.png"),
            "inverted_file": existing_entry.get("inverted_file", f"{folio_data['folio']}.{gid}.inverted.png"),
            "svg_file": existing_entry.get("svg_file", f"{folio_data['folio']}.{gid}.svg"),
            "bbox": [int(v) for v in bbox],
            "white_point": int(white_point) if white_point is not None else existing_entry.get("white_point", 226),
            "caption": caption or existing_entry.get("caption", f"Folio {folio_data['folio']} Figure {gid.replace('g', '')}"),
        })

        # Replace or add
        graphics = [g for g in graphics if g.get("id") != gid]
        graphics.append(entry)
        graphics.sort(key=lambda x: x.get("id", ""))
        metadata["graphics"] = graphics

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        if trigger_extract:
            try:
                extract_from_json(json_path)
            except Exception as e:
                return jsonify({"error": f"JSON saved but extraction failed: {e}"}), 500

        scanner.refresh(force=True)
        updated_folio = scanner.get_folio(volume_id, folio_id)
        return jsonify({
            "success": True,
            "graphics": updated_folio.get("graphics", []) if updated_folio else [],
        })

    @app.route("/api/folio/<volume_id>/<folio_id>/graphic/<gid>/save_svg", methods=["POST"])
    def api_save_graphic_svg(volume_id: str, folio_id: str, gid: str):
        """Save or update SVG markup for a graphic on disk."""
        payload = request.get_json(force=True) or {}
        svg_content = payload.get("svg", "").strip()

        if not svg_content:
            return jsonify({"error": "Empty SVG content"}), 400

        folio_data = scanner.get_folio(volume_id, folio_id)
        if not folio_data:
            return jsonify({"error": "Folio not found"}), 404

        parent_dir = scanner.root_dir / folio_data["volume"] / folio_data["section_path"]
        svg_filename = f"{folio_data['folio']}.{gid}.svg"
        svg_path = parent_dir / svg_filename

        try:
            svg_path.write_text(svg_content, encoding="utf-8")

            # Also ensure svg_file is set in <folio>.json
            json_path = parent_dir / f"{folio_data['folio']}.json"
            if json_path.exists():
                with open(json_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                updated = False
                for g in meta.get("graphics", []):
                    if g.get("id") == gid:
                        g["svg_file"] = svg_filename
                        updated = True
                        break
                if updated:
                    with open(json_path, "w", encoding="utf-8") as f:
                        json.dump(meta, f, indent=2)

            scanner.refresh(force=True)
            updated_folio = scanner.get_folio(volume_id, folio_id)
            return jsonify({
                "success": True,
                "svg_file": svg_filename,
                "graphics": updated_folio.get("graphics", []) if updated_folio else [],
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/api/folio/<volume_id>/<folio_id>/set_graphic_format", methods=["POST"])
    def api_set_graphic_format(volume_id: str, folio_id: str):
        """Switch markdown reference between PNG and SVG for a graphic."""
        payload = request.get_json(force=True) or {}
        gid = payload.get("id", "g1")
        target_format = payload.get("format", "svg").lower()  # "svg" or "png"

        folio_data = scanner.get_folio(volume_id, folio_id)
        if not folio_data:
            return jsonify({"error": "Folio not found"}), 404

        parent_dir = scanner.root_dir / folio_data["volume"] / folio_data["section_path"]
        md_path = parent_dir / f"{folio_data['folio']}.md"
        if not md_path.exists():
            return jsonify({"error": "Markdown transcription file does not exist"}), 400

        png_name = f"{folio_data['folio']}.{gid}.png"
        svg_name = f"{folio_data['folio']}.{gid}.svg"

        try:
            md_text = md_path.read_text(encoding="utf-8")
            if target_format == "svg":
                if png_name in md_text:
                    md_text = md_text.replace(png_name, svg_name)
                    md_path.write_text(md_text, encoding="utf-8")
            elif target_format == "png":
                if svg_name in md_text:
                    md_text = md_text.replace(svg_name, png_name)
                    md_path.write_text(md_text, encoding="utf-8")

            scanner.refresh(force=True)
            updated_folio = scanner.get_folio(volume_id, folio_id)
            return jsonify({
                "success": True,
                "format": target_format,
                "graphics": updated_folio.get("graphics", []) if updated_folio else [],
                "md_html": updated_folio.get("md_html", "") if updated_folio else "",
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app


def main():
    """Run review application CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Euclid Folio Review Application")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5000, help="Port to listen on (default: 5000)")
    parser.add_argument("--debug", action="store_true", default=True, help="Run in debug mode")
    args = parser.parse_args()

    app = create_app()
    print(f"\n* Starting Euclid Folio Review App on http://{args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
