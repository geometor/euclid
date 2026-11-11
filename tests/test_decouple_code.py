"""Regression tests enforcing code decoupling and asset integrity in ``geometor.euclid``."""

from __future__ import annotations

import importlib
import importlib.util
import json
from pathlib import Path
import tomllib
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[1]
HEATH_RESOURCES = REPO_ROOT / "resources" / "heath"
HEATH_DOCSRC = REPO_ROOT / "docsrc" / "heath"


def test_zero_python_files_in_heath_trees() -> None:
    """Ensure no Python construction scripts exist anywhere in resources/heath or docsrc/heath."""
    resource_py = sorted(HEATH_RESOURCES.rglob("*.py"))
    docsrc_py = sorted(HEATH_DOCSRC.rglob("*.py")) if HEATH_DOCSRC.exists() else []
    assert resource_py == [], f"Unexpected .py files in resources/heath: {resource_py}"
    assert docsrc_py == [], f"Unexpected .py files in docsrc/heath: {docsrc_py}"


def test_folio_jsons_valid_and_free_of_py_file() -> None:
    """Verify all JSON files in resources/heath parse cleanly, have zero py_file keys, and keep geometry."""
    json_files = sorted(HEATH_RESOURCES.rglob("*.json"))
    assert len(json_files) > 1400, "Expected full 3-volume Heath JSON corpus."

    geometry_count = 0
    svg_ref_count = 0
    bbox_count = 0

    for jf in json_files:
        raw = jf.read_text(encoding="utf-8")
        assert '"py_file"' not in raw, f"Legacy py_file key still present in {jf}"
        data = json.loads(raw)

        if isinstance(data, dict) and "graphics" in data:
            graphics = data["graphics"]
            assert isinstance(graphics, list), f"graphics must be a list in {jf}"
            for g in graphics:
                assert "py_file" not in g, f"py_file key found in graphic of {jf}"
                assert "id" in g, f"Missing id in {jf}"
                assert any(
                    k in g for k in ("file", "svg_file", "bbox", "size", "box")
                ), f"Missing graphic asset/bounds metadata in {jf}"
                if "bbox" in g:
                    bbox_count += 1
                if "svg_file" in g:
                    svg_ref_count += 1
                    svg_path = jf.parent / g["svg_file"]
                    assert svg_path.is_file(), f"Missing referenced SVG {svg_path} from {jf}"
                if "geometry" in g:
                    geometry_count += 1
                    geom = g["geometry"]
                    assert isinstance(geom, dict) and len(geom) > 0, f"Empty geometry in {jf}"

    assert bbox_count >= 800, f"Expected >=800 preserved bbox entries, got {bbox_count}"
    assert svg_ref_count >= 800, f"Expected >=800 calibrated SVG references, got {svg_ref_count}"
    assert geometry_count >= 650, f"Expected >=650 preserved geometry blocks, got {geometry_count}"


def test_heath_svgs_are_well_formed_xml() -> None:
    """Verify every calibrated SVG in resources/heath parses cleanly and carries a viewBox."""
    svg_files = sorted(HEATH_RESOURCES.rglob("*.svg"))
    assert len(svg_files) >= 830, f"Expected >=830 SVGs in resources/heath, got {len(svg_files)}"

    for svg_path in svg_files:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        view_box = root.attrib.get("viewBox", "").strip()
        assert view_box, f"Missing viewBox attribute on {svg_path}"


def test_legacy_code_vestiges_removed() -> None:
    """Ensure legacy modeling dependencies, empty demos, and duplicate folio templates stay removed."""
    pyproject_data = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    deps = {
        d.split(">")[0].split("=")[0].split("<")[0].strip().lower()
        for d in pyproject_data["project"]["dependencies"]
    }
    forbidden = {"sympy", "matplotlib", "mplcursors", "geometor-model", "geometor-explorer"}
    assert deps.isdisjoint(forbidden), f"Forbidden modeling dependencies present: {deps & forbidden}"

    assert not (REPO_ROOT / "demos").exists(), "Legacy empty demos/ directory should not exist"
    assert not (REPO_ROOT / "docsrc" / "demos").exists(), "Legacy docsrc/demos/ directory should not exist"
    assert not (
        REPO_ROOT / "src" / "geometor" / "euclid" / "folio_review" / "templates"
    ).exists(), "Dead duplicate folio_review/templates directory should not exist"
    assert not (
        REPO_ROOT / "src" / "geometor" / "euclid" / "ingest" / "compare_models.py"
    ).exists(), "Obsolete compare_models.py prototype should not exist"


def test_active_package_entrypoints_importable() -> None:
    """Ensure active edition compilation, graph, transform, and graphic_tool modules import cleanly."""
    mod = importlib.import_module("geometor.euclid")
    assert mod is not None

    if importlib.util.find_spec("networkx") is not None:
        assert importlib.import_module("geometor.euclid.graph") is not None
        assert importlib.import_module("geometor.euclid.transform") is not None

    if importlib.util.find_spec("cv2") is not None:
        assert importlib.import_module("geometor.euclid.scripts.graphic_tool") is not None

    if importlib.util.find_spec("photon_platform") is not None:
        for mod_name in (
            "geometor.euclid.compile_edition",
            "geometor.euclid.folio_review",
            "geometor.euclid.folio_review.rst_utils",
        ):
            assert importlib.import_module(mod_name) is not None
