"""Scanner and indexer for the Euclid folio resources.

Scans the resources/heath/ folder for volume_I, volume_II, volume_III folio scans,
markdown transcriptions, transcription notes, and graphics extraction metadata.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import time
from typing import Any, Dict, List, Optional, Tuple
import yaml
import markdown


def fix_relative_media_urls(html: str, volume: str, section_path: str) -> str:
    """Rewrite relative image paths (e.g. src="0225.g1.png") to /media/{volume}/{section_path}/{filename}."""
    if not html:
        return ""
    media_base = f"/media/{volume}/{section_path}"

    def _replace_src(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        if url.startswith(("http://", "https://", "/", "data:", "#", "mailto:")):
            return match.group(0)
        clean_url = url
        if clean_url.startswith("./"):
            clean_url = clean_url[2:]
        return f"{prefix}{media_base}/{clean_url}{suffix}"

    html = re.sub(r'(src=["\'])([^"\']+)(["\'])', _replace_src, html, flags=re.IGNORECASE)

    def _replace_href(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        if url.startswith(("http://", "https://", "/", "data:", "#", "mailto:")):
            return match.group(0)
        if any(url.lower().endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"]):
            clean_url = url
            if clean_url.startswith("./"):
                clean_url = clean_url[2:]
            return f"{prefix}{media_base}/{clean_url}{suffix}"
        return match.group(0)

    html = re.sub(r'(href=["\'])([^"\']+)(["\'])', _replace_href, html, flags=re.IGNORECASE)
    return html


class FolioScanner:
    """Scans and indexes folios from resources/heath/."""

    def __init__(self, root_dir: Optional[Path] = None):
        if root_dir is None:
            # Default to repo resources/heath
            workspace_root = Path(__file__).resolve().parents[4]
            self.root_dir = workspace_root / "resources" / "heath"
        else:
            self.root_dir = Path(root_dir)

        self._cache: Dict[str, Any] = {}
        self._last_scan_time: float = 0
        self._scan_ttl: float = 2.0  # seconds between auto-refreshes

    def refresh(self, force: bool = False) -> None:
        """Refresh index from disk if TTL expired or forced."""
        now = time.time()
        if not force and self._cache and (now - self._last_scan_time) < self._scan_ttl:
            return

        folios_list: List[Dict[str, Any]] = []
        folios_map: Dict[Tuple[str, str], Dict[str, Any]] = {}
        volume_stats: Dict[str, Dict[str, Any]] = {}

        if not self.root_dir.exists():
            self._cache = {
                "folios": [],
                "map": {},
                "volume_stats": {},
                "sections": [],
            }
            self._last_scan_time = now
            return

        vol_dirs = sorted(
            [d for d in self.root_dir.iterdir() if d.is_dir() and d.name.startswith("volume_")]
        )

        for vol_dir in vol_dirs:
            vol_name = vol_dir.name
            volume_stats[vol_name] = {
                "name": vol_name,
                "label": vol_name.replace("_", " ").title().replace("Volume Iii", "Volume III").replace("Volume Ii", "Volume II"),
                "total_folios": 0,
                "transcribed_count": 0,
                "notes_count": 0,
                "graphics_count": 0,
                "svg_count": 0,
                "folios_with_graphics": 0,
                "missing_crops_count": 0,
                "folios_with_svg": 0,
                "sections": set(),
            }

            for png_path in sorted(vol_dir.rglob("*.png")):
                stem = png_path.stem
                # Check for 4-digit folio stem (e.g. 0167)
                if not (len(stem) == 4 and stem.isdigit()):
                    continue

                parent_dir = png_path.parent
                rel_sec = str(parent_dir.relative_to(vol_dir))
                volume_stats[vol_name]["sections"].add(rel_sec)

                folio_id = stem
                folio_num = int(stem)

                md_path = parent_dir / f"{stem}.md"
                notes_path = parent_dir / f"{stem}.notes.md"
                json_path = parent_dir / f"{stem}.json"

                has_md = md_path.exists()
                has_notes = notes_path.exists()
                has_json = json_path.exists()

                # Parse frontmatter if md exists
                frontmatter: Dict[str, Any] = {}
                page_str = ""
                title_str = ""
                book_str = ""
                section_str = rel_sec

                md_raw_text = ""
                if has_md:
                    try:
                        md_raw_text = md_path.read_text(encoding="utf-8")
                        if md_raw_text.startswith("---"):
                            parts = md_raw_text.split("---", 2)
                            if len(parts) >= 3:
                                parsed = yaml.safe_load(parts[1])
                                if isinstance(parsed, dict):
                                    frontmatter = parsed
                                    page_str = str(parsed.get("page", ""))
                                    title_str = str(parsed.get("title", ""))
                                    book_str = str(parsed.get("book", ""))
                                    if parsed.get("section"):
                                        section_str = str(parsed.get("section"))
                    except Exception:
                        pass

                # Parse graphics if json exists
                graphics_list: List[Dict[str, Any]] = []
                missing_crops = 0
                folio_svg_count = 0
                if has_json:
                    try:
                        with open(json_path, "r", encoding="utf-8") as jf:
                            jdata = json.load(jf)
                            raw_graphics = jdata.get("graphics", [])
                            for g in raw_graphics:
                                gid = g.get("id", "g1")
                                g_file = g.get("file", f"{stem}.{gid}.png")
                                inv_file = g.get("inverted_file", f"{stem}.{gid}.inverted.png")
                                svg_file = g.get("svg_file", f"{stem}.{gid}.svg")
                                
                                file_exists = (parent_dir / g_file).exists()
                                inv_exists = (parent_dir / inv_file).exists()
                                svg_exists = (parent_dir / svg_file).exists()

                                if not file_exists:
                                    missing_crops += 1
                                if svg_exists:
                                    folio_svg_count += 1

                                in_md_format = None
                                if md_raw_text:
                                    if svg_file in md_raw_text:
                                        in_md_format = "svg"
                                    elif g_file in md_raw_text:
                                        in_md_format = "png"

                                graphics_list.append({
                                    "id": gid,
                                    "file": g_file,
                                    "file_exists": file_exists,
                                    "inverted_file": inv_file,
                                    "inverted_exists": inv_exists,
                                    "svg_file": svg_file,
                                    "svg_exists": svg_exists,
                                    "in_md_format": in_md_format,
                                    "bbox": g.get("bbox", []),
                                    "white_point": g.get("white_point", 226),
                                    "caption": g.get("caption", f"Folio {stem} Figure {gid}"),
                                    "geometry": g.get("geometry"),
                                })
                    except Exception:
                        pass

                # Section label
                clean_sec_label = rel_sec.replace("_", " ").title()

                folio_item = {
                    "volume": vol_name,
                    "volume_label": volume_stats[vol_name]["label"],
                    "folio": folio_id,
                    "folio_num": folio_num,
                    "section_path": rel_sec,
                    "section_label": clean_sec_label,
                    "page": page_str or str(folio_num),
                    "title": title_str or clean_sec_label,
                    "book": book_str or rel_sec.split("/")[0],
                    "frontmatter": frontmatter,
                    "scan_file": png_path.name,
                    "scan_rel_path": str(png_path.relative_to(self.root_dir)),
                    "md_rel_path": str(md_path.relative_to(self.root_dir)) if has_md else None,
                    "notes_rel_path": str(notes_path.relative_to(self.root_dir)) if has_notes else None,
                    "json_rel_path": str(json_path.relative_to(self.root_dir)) if has_json else None,
                    "has_scan": True,
                    "has_md": has_md,
                    "has_notes": has_notes,
                    "has_json": has_json,
                    "graphics": graphics_list,
                    "graphics_count": len(graphics_list),
                    "has_graphics": len(graphics_list) > 0,
                    "svg_count": folio_svg_count,
                    "has_svg": folio_svg_count > 0,
                    "missing_crops_count": missing_crops,
                }

                folios_list.append(folio_item)
                folios_map[(vol_name, folio_id)] = folio_item

                # Update stats
                volume_stats[vol_name]["total_folios"] += 1
                if has_md:
                    volume_stats[vol_name]["transcribed_count"] += 1
                if has_notes:
                    volume_stats[vol_name]["notes_count"] += 1
                if graphics_list:
                    volume_stats[vol_name]["folios_with_graphics"] += 1
                    volume_stats[vol_name]["graphics_count"] += len(graphics_list)
                    volume_stats[vol_name]["svg_count"] += folio_svg_count
                volume_stats[vol_name]["missing_crops_count"] += missing_crops
                if folio_svg_count > 0:
                    volume_stats[vol_name]["folios_with_svg"] += 1

        # Sort folios by volume and folio_num
        folios_list.sort(key=lambda x: (x["volume"], x["folio_num"]))

        # Convert sections to sorted lists in volume_stats
        for v in volume_stats.values():
            v["sections"] = sorted(list(v["sections"]))

        # Unique list of sections across all volumes
        all_sections = sorted(list({f["section_path"] for f in folios_list}))

        self._cache = {
            "folios": folios_list,
            "map": folios_map,
            "volume_stats": volume_stats,
            "sections": all_sections,
        }
        self._last_scan_time = now

    def get_stats(self) -> Dict[str, Any]:
        """Return aggregate statistics across all volumes."""
        self.refresh()
        vol_stats = self._cache.get("volume_stats", {})
        total_folios = sum(v["total_folios"] for v in vol_stats.values())
        total_transcribed = sum(v["transcribed_count"] for v in vol_stats.values())
        total_notes = sum(v["notes_count"] for v in vol_stats.values())
        total_graphics = sum(v["graphics_count"] for v in vol_stats.values())
        total_svgs = sum(v.get("svg_count", 0) for v in vol_stats.values())
        total_folios_with_graphics = sum(v["folios_with_graphics"] for v in vol_stats.values())
        total_missing_crops = sum(v["missing_crops_count"] for v in vol_stats.values())
        total_folios_with_svg = sum(v.get("folios_with_svg", 0) for v in vol_stats.values())

        return {
            "total_folios": total_folios,
            "total_transcribed": total_transcribed,
            "transcribed_pct": round((total_transcribed / total_folios * 100), 1) if total_folios else 0,
            "total_notes": total_notes,
            "notes_pct": round((total_notes / total_folios * 100), 1) if total_folios else 0,
            "total_graphics": total_graphics,
            "total_svgs": total_svgs,
            "svg_pct": round((total_svgs / total_graphics * 100), 1) if total_graphics else 0,
            "total_folios_with_graphics": total_folios_with_graphics,
            "total_missing_crops": total_missing_crops,
            "total_folios_with_svg": total_folios_with_svg,
            "volumes": vol_stats,
        }

    def get_volumes(self) -> List[Dict[str, Any]]:
        """Return list of volumes."""
        self.refresh()
        return list(self._cache.get("volume_stats", {}).values())

    def get_sections(self, volume_id: Optional[str] = None) -> List[str]:
        """Return list of section relative paths."""
        self.refresh()
        if volume_id and volume_id in self._cache.get("volume_stats", {}):
            return self._cache["volume_stats"][volume_id]["sections"]
        return self._cache.get("sections", [])

    def get_folios(
        self,
        volume_id: Optional[str] = None,
        section: Optional[str] = None,
        filter_status: Optional[str] = None,
        search_query: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Filter folios by volume, section, status, or search query."""
        self.refresh()
        results = self._cache.get("folios", [])

        if volume_id:
            results = [f for f in results if f["volume"] == volume_id]

        if section:
            results = [f for f in results if f["section_path"] == section or f["section_path"].startswith(section)]

        if filter_status == "transcribed":
            results = [f for f in results if f["has_md"]]
        elif filter_status == "missing_transcription":
            results = [f for f in results if not f["has_md"]]
        elif filter_status == "has_notes":
            results = [f for f in results if f["has_notes"]]
        elif filter_status == "missing_notes":
            results = [f for f in results if not f["has_notes"]]
        elif filter_status == "has_graphics":
            results = [f for f in results if f["has_graphics"]]
        elif filter_status == "has_svg":
            results = [f for f in results if f.get("has_svg")]
        elif filter_status == "missing_crops":
            results = [f for f in results if f["missing_crops_count"] > 0]
        elif filter_status == "missing_svg":
            results = [f for f in results if f.get("has_graphics") and not f.get("has_svg")]

        if search_query:
            q = search_query.strip().lower()
            results = [
                f for f in results
                if q in f["folio"].lower()
                or q in f["page"].lower()
                or q in f["title"].lower()
                or q in f["section_path"].lower()
                or q in f["section_label"].lower()
            ]

        return results

    def get_folio(self, volume_id: str, folio_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve full details of a specific folio."""
        self.refresh()
        # Normalise folio_id (e.g. 167 -> 0167)
        if folio_id.isdigit():
            folio_id = f"{int(folio_id):04d}"

        key = (volume_id, folio_id)
        item = self._cache.get("map", {}).get(key)
        if not item:
            return None

        # Return a copy with fresh content read from disk
        res = dict(item)
        full_parent = self.root_dir / res["volume"] / res["section_path"]

        # Read Markdown transcription content
        md_file = full_parent / f"{folio_id}.md"
        if md_file.exists():
            try:
                res["md_content"] = md_file.read_text(encoding="utf-8")
                clean_text = res["md_content"]
                if clean_text.startswith("---"):
                    parts = clean_text.split("---", 2)
                    if len(parts) >= 3:
                        clean_text = parts[2].strip()
                rendered_md = markdown.markdown(
                    clean_text, extensions=["tables", "fenced_code", "footnotes"]
                )
                res["md_html"] = fix_relative_media_urls(
                    rendered_md, res["volume"], res["section_path"]
                )
            except Exception as e:
                res["md_content"] = f"Error reading markdown: {e}"
                res["md_html"] = f"<p>Error rendering markdown: {e}</p>"
        else:
            res["md_content"] = None
            res["md_html"] = ""

        # Read Notes content
        notes_file = full_parent / f"{folio_id}.notes.md"
        if notes_file.exists():
            try:
                res["notes_content"] = notes_file.read_text(encoding="utf-8")
                rendered_notes = markdown.markdown(
                    res["notes_content"], extensions=["tables", "fenced_code", "footnotes"]
                )
                res["notes_html"] = fix_relative_media_urls(
                    rendered_notes, res["volume"], res["section_path"]
                )
            except Exception as e:
                res["notes_content"] = f"Error reading notes: {e}"
                res["notes_html"] = f"<p>Error rendering notes: {e}</p>"
        else:
            res["notes_content"] = None
            res["notes_html"] = ""

        # Read JSON metadata
        json_file = full_parent / f"{folio_id}.json"
        if json_file.exists():
            try:
                with open(json_file, "r", encoding="utf-8") as jf:
                    res["raw_json"] = json.load(jf)
            except Exception as e:
                res["raw_json"] = {"error": str(e)}
        else:
            res["raw_json"] = None

        # Load SVG content for any graphics that exist
        graphics_with_content = []
        for g in res.get("graphics", []):
            g_copy = dict(g)
            if g_copy.get("svg_exists"):
                svg_p = full_parent / g_copy["svg_file"]
                if svg_p.exists():
                    try:
                        g_copy["svg_content"] = svg_p.read_text(encoding="utf-8")
                    except Exception:
                        g_copy["svg_content"] = None
                else:
                    g_copy["svg_content"] = None
            else:
                g_copy["svg_content"] = None
            graphics_with_content.append(g_copy)
        res["graphics"] = graphics_with_content

        return res

    def get_adjacent_folios(
        self,
        volume_id: str,
        folio_id: str,
        section: Optional[str] = None
    ) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
        """Return (previous_folio, next_folio) within volume or section."""
        self.refresh()
        folios = self.get_folios(volume_id=volume_id, section=section)

        if folio_id.isdigit():
            folio_id = f"{int(folio_id):04d}"

        curr_idx = -1
        for i, f in enumerate(folios):
            if f["folio"] == folio_id:
                curr_idx = i
                break

        if curr_idx == -1:
            return None, None

        prev_folio = folios[curr_idx - 1] if curr_idx > 0 else None
        next_folio = folios[curr_idx + 1] if curr_idx < len(folios) - 1 else None

        return prev_folio, next_folio
