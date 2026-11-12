"""Concordance loader, validator, and functional DAG query helpers for Euclid's *Data*.

Provides stdlib-only typed structures and validation utilities over the static
JSON apparatus in ``resources/data/`` (``concordance.json``, ``citations.json``,
``persons.json``, ``glossary.json``, and ``enunciations.json``).
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class DataDefinitionEntry:
    """Structured record for one of the 15 Definitions of Euclid's *Data*.

    Attributes:
        id: Canonical identifier (``D.def.1`` through ``D.def.15``).
        number: Sequential integer index (1 through 15).
        greek_numeral: Milesian Greek numeral header in Menge (1896).
        menge_page: Page number in Menge's 1896 Teubner edition.
        simson_id: Corresponding definition identifier in Simson (1762/1806).
        authentic: Whether Menge prints the definition outside editorial brackets.
        category: Epistemic/geometric category of givenness.
        greek_text: Polytonic Greek text from Menge (1896).
        english_text: Public-domain / literal English translation.
        functional_form: Algebraic or constructive predicate specification.
    """

    id: str
    number: int
    greek_numeral: str
    menge_page: int
    simson_id: str
    authentic: bool
    category: str
    greek_text: str
    english_text: str
    functional_form: str


@dataclass(frozen=True)
class DataPropositionEntry:
    """Structured record for one of the 94 Propositions of Euclid's *Data*.

    Attributes:
        id: Canonical identifier (``D.1`` through ``D.94``).
        number: Sequential integer index in Menge (1896) (1 through 94).
        greek_numeral: Milesian Greek numeral header in Menge (1896).
        unit: Thematic unit number (1 through 6).
        unit_slug: Directory slug in ``docsrc/data/``.
        menge_page: Starting page in Menge's 1896 Teubner edition.
        simson_id: Corresponding proposition identifier in Simson (1762/1806).
        greek_enunciation: Polytonic Greek enunciation from Menge (1896).
        english_enunciation: Public-domain / literal English enunciation.
        given: Tuple of typed input hypotheses.
        determined: Tuple of typed output determinations.
        functional_signature: Compact ``Given(...) -> Determined(...)`` signature.
        data_deps: Tuple of internal *Data* dependencies (``D.def.*``, ``D.*``).
        elements_deps: Tuple of *Elements* dependencies (``I.1``–``VI.33``, etc.).
        g_index_deps: Tuple of ``geometor/elements`` G-Index identifiers.
        pappus_refs: Tuple of cross-references to Pappus's *Synagoge* Book VII.
        petersen_methods: Tuple of Julius Petersen locus/transformation tags.
        altshiller_court_refs: Tuple of Nathan Altshiller-Court *College Geometry* loci.
        computational_primitive: Modern ``geometor.model`` / solver interpretation.
    """

    id: str
    number: int
    greek_numeral: str
    unit: int
    unit_slug: str
    menge_page: int
    simson_id: str
    greek_enunciation: str
    english_enunciation: str
    given: tuple[str, ...]
    determined: tuple[str, ...]
    functional_signature: str
    data_deps: tuple[str, ...]
    elements_deps: tuple[str, ...]
    g_index_deps: tuple[str, ...]
    pappus_refs: tuple[str, ...]
    petersen_methods: tuple[str, ...]
    altshiller_court_refs: tuple[str, ...]
    computational_primitive: str


@dataclass(frozen=True)
class DataConcordance:
    """Complete parsed concordance for Euclid's *Data* (*Δεδομένα*).

    Attributes:
        title: English title of the codex.
        greek_title: Polytonic Greek title of the treatise.
        edition_greek: Bibliographic description of the Greek base text.
        edition_english: Bibliographic description of the English translation track.
        units: Tuple of unit metadata dictionaries (Units 0 through 6).
        definitions: Tuple of all 15 ``DataDefinitionEntry`` records.
        propositions: Tuple of all 94 ``DataPropositionEntry`` records.
    """

    title: str
    greek_title: str
    edition_greek: str
    edition_english: str
    units: tuple[dict[str, Any], ...]
    definitions: tuple[DataDefinitionEntry, ...]
    propositions: tuple[DataPropositionEntry, ...]


def default_data_resources_dir() -> Path:
    """Return the canonical ``resources/data`` directory inside ``geometor.euclid``.

    Returns:
        Absolute ``Path`` to ``<repo_root>/resources/data``.
    """
    return Path(__file__).resolve().parents[3] / "resources" / "data"


def load_data_concordance(resources_dir: Path | None = None) -> DataConcordance:
    """Load and parse ``concordance.json`` into typed ``DataConcordance`` records.

    Args:
        resources_dir: Optional override directory containing ``concordance.json``.

    Returns:
        Parsed ``DataConcordance`` instance.
    """
    base = resources_dir if resources_dir is not None else default_data_resources_dir()
    raw: dict[str, Any] = json.loads((base / "concordance.json").read_text(encoding="utf-8"))

    defs = tuple(
        DataDefinitionEntry(
            id=str(d["id"]),
            number=int(d["number"]),
            greek_numeral=str(d["greek_numeral"]),
            menge_page=int(d["menge_page"]),
            simson_id=str(d["simson_id"]),
            authentic=bool(d["authentic"]),
            category=str(d["category"]),
            greek_text=str(d["greek_text"]),
            english_text=str(d["english_text"]),
            functional_form=str(d["functional_form"]),
        )
        for d in raw["definitions"]
    )

    props = tuple(
        DataPropositionEntry(
            id=str(p["id"]),
            number=int(p["number"]),
            greek_numeral=str(p["greek_numeral"]),
            unit=int(p["unit"]),
            unit_slug=str(p["unit_slug"]),
            menge_page=int(p["menge_page"]),
            simson_id=str(p["simson_id"]),
            greek_enunciation=str(p["greek_enunciation"]),
            english_enunciation=str(p["english_enunciation"]),
            given=tuple(str(x) for x in p["given"]),
            determined=tuple(str(x) for x in p["determined"]),
            functional_signature=str(p["functional_signature"]),
            data_deps=tuple(str(x) for x in p["data_deps"]),
            elements_deps=tuple(str(x) for x in p["elements_deps"]),
            g_index_deps=tuple(str(x) for x in p["g_index_deps"]),
            pappus_refs=tuple(str(x) for x in p["pappus_refs"]),
            petersen_methods=tuple(str(x) for x in p["petersen_methods"]),
            altshiller_court_refs=tuple(str(x) for x in p["altshiller_court_refs"]),
            computational_primitive=str(p["computational_primitive"]),
        )
        for p in raw["propositions"]
    )

    return DataConcordance(
        title=str(raw["title"]),
        greek_title=str(raw["greek_title"]),
        edition_greek=str(raw["edition_greek"]),
        edition_english=str(raw["edition_english"]),
        units=tuple(dict(u) for u in raw["units"]),
        definitions=defs,
        propositions=props,
    )


def load_data_apparatus(resources_dir: Path | None = None) -> dict[str, dict[str, Any]]:
    """Load the four scholarly apparatus JSON registries for ``docsrc/data/``.

    Args:
        resources_dir: Optional override directory containing the JSON registries.

    Returns:
        Mapping with keys ``citations``, ``persons``, ``glossary``, and ``enunciations``.
    """
    base = resources_dir if resources_dir is not None else default_data_resources_dir()
    result: dict[str, dict[str, Any]] = {}
    for name in ("citations", "persons", "glossary", "enunciations"):
        result[name] = json.loads((base / f"{name}.json").read_text(encoding="utf-8"))
    return result


def validate_data_concordance(concordance: DataConcordance) -> list[str]:
    """Validate completeness, sequential numbering, and internal DAG acyclicity.

    Args:
        concordance: Parsed ``DataConcordance`` object to inspect.

    Returns:
        List of validation error messages (empty list when 100% valid).
    """
    errors: list[str] = []

    if len(concordance.units) != 7:
        errors.append(f"Expected 7 thematic units (0..6), got {len(concordance.units)}")

    if len(concordance.definitions) != 15:
        errors.append(f"Expected 15 definitions, got {len(concordance.definitions)}")

    for idx, d in enumerate(concordance.definitions, start=1):
        expected_id = f"D.def.{idx}"
        if d.id != expected_id or d.number != idx:
            errors.append(f"Definition index mismatch at {idx}: got {d.id} (#{d.number})")
        if not d.greek_text.strip() or not d.english_text.strip():
            errors.append(f"Empty Greek or English text on {d.id}")
        if not d.functional_form.strip():
            errors.append(f"Empty functional_form on {d.id}")

    if len(concordance.propositions) != 94:
        errors.append(f"Expected 94 propositions, got {len(concordance.propositions)}")

    known_def_ids = {d.id for d in concordance.definitions}
    known_prop_ids = {p.id for p in concordance.propositions}

    for idx, p in enumerate(concordance.propositions, start=1):
        expected_id = f"D.{idx}"
        if p.id != expected_id or p.number != idx:
            errors.append(f"Proposition index mismatch at {idx}: got {p.id} (#{p.number})")
        if p.unit not in {1, 2, 3, 4, 5, 6}:
            errors.append(f"Invalid unit {p.unit} on {p.id}")
        if not p.greek_enunciation.strip() or not p.english_enunciation.strip():
            errors.append(f"Empty Greek or English enunciation on {p.id}")
        if not p.simson_id.strip():
            errors.append(f"Missing Simson cross-reference on {p.id}")
        if not p.given or not p.determined or not p.functional_signature.strip():
            errors.append(f"Incomplete functional type signature on {p.id}")
        for dep in p.data_deps:
            if dep in known_def_ids:
                continue
            if dep not in known_prop_ids:
                errors.append(f"Unknown Data dependency {dep!r} on {p.id}")
                continue
            dep_num = int(dep.split(".")[1])
            if dep_num >= p.number:
                errors.append(
                    f"Non-causal forward dependency {dep} cited by {p.id} in Menge order"
                )

    return errors


def propositions_by_unit(
    concordance: DataConcordance,
    unit: int,
) -> list[DataPropositionEntry]:
    """Return all propositions belonging to a given thematic unit (1 through 6).

    Args:
        concordance: Parsed ``DataConcordance`` instance.
        unit: Thematic unit index (1 through 6).

    Returns:
        Ordered list of ``DataPropositionEntry`` records in ``unit``.
    """
    return [p for p in concordance.propositions if p.unit == unit]


def propositions_citing_elements(
    concordance: DataConcordance,
    element_id: str,
) -> list[DataPropositionEntry]:
    """Find all *Data* propositions whose synthetic proof invokes ``element_id``.

    Args:
        concordance: Parsed ``DataConcordance`` instance.
        element_id: Canonical *Elements* target such as ``"I.4"`` or ``"VI.28"``.

    Returns:
        Ordered list of matching ``DataPropositionEntry`` records.
    """
    needle = element_id.strip()
    return [p for p in concordance.propositions if needle in p.elements_deps]


def build_data_dependency_dag(
    concordance: DataConcordance,
) -> dict[str, tuple[str, ...]]:
    """Build an adjacency mapping from each *Data* node to its internal *Data* prerequisites.

    Args:
        concordance: Parsed ``DataConcordance`` instance.

    Returns:
        Dictionary mapping ``D.def.1``..``D.def.15`` and ``D.1``..``D.94`` to
        their direct *Data* prerequisite identifiers.
    """
    dag: dict[str, tuple[str, ...]] = {d.id: () for d in concordance.definitions}
    for p in concordance.propositions:
        dag[p.id] = p.data_deps
    return dag
