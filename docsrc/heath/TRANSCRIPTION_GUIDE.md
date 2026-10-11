# Heath Euclid Transcription & Reconstruction Guide

## Overview

This guide establishes the architecture, standards, and procedures for transcribing and reconstructing Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements* (Volumes I–III, covering Books I through XIII).

Our methodology is **Zero-OCR**: all text is visually verified directly from the high-resolution page scans (`XXXX.png`), ensuring complete accuracy for polytonic Greek, Arabic transliterations, mathematical symbols, footnotes, and geometric diagrams.

---

## 1. Directory Structure & Co-location Standard

### Atomic Page Files in `resources/`
All atomic markdown page transcriptions must reside **directly alongside the original scan images**:

```
resources/heath/volume_I/
├── book_i/
│   ├── definitions/
│   │   ├── 0167.png
│   │   └── 0167.md          <-- Markdown alongside scan
│   ├── postulates/
│   │   ├── 0168.png
│   │   └── 0168.md
│   ├── common_notions/
│   │   ├── 0174.png
│   │   ├── 0174.md
│   │   ├── 0174.json        <-- Crop info metadata
│   │   ├── 0174.g1.png      <-- Clustered graphic 1
│   │   └── 0174.g1.inverted.png
│   └── propositions/
│       ├── 0255.png
│       ├── 0255.md
│       ├── 0255.json        <-- Crop info metadata
│       ├── 0255.g1.png      <-- Clustered graphic 1
│       └── 0255.g1.inverted.png
```

### Demonstration Graphics Naming Standard
All assets for a given page follow the folio number as their base:
1. **Source Scan**: `0021.png`
2. **Markdown Transcription**: `0021.md`
3. **Crop Info Metadata**: `0021.json` (stores bounding boxes, crop parameters, label info, offsets)
4. **Graphic 1**: `0021.g1.png`
5. **Inverted Graphic 1 (Dark Mode)**: `0021.g1.inverted.png`
6. **Subsequent Graphics** (if multiple exist on a page): `0021.g2.png`, `0021.g2.inverted.png`, etc.

This naming guarantees that all related files for a page cluster together alphabetically in file managers, editors, and CLI listings.

Inside the local `.md` file, reference the graphic relatively:
```markdown
![Proposition 1 figure](0255.g1.png)
```

> [!NOTE]
> **No Mirroring Yet**: Do not mirror graphics to `docsrc/heath/_static/graphics/` at this stage. Our current priority is exclusively collecting and perfecting all transcription data and assets inside `resources/`. Publishing and documentation generation will occur in a later phase.

---

## 2. Granularity & Few-Shot Subagent Protocol

### Granular Work Units
Subagents maintain significantly higher accuracy and speed when constrained to small batches:
- **First Principles / Commentaries**: 1 to 2 folios per task.
- **Propositions**: 1 proposition and its immediate commentary (typically 1 to 3 folios).

### Few-Shot Context Pattern
When dispatching a transcription subagent, always provide:
1. **Preceding Reference Files**: Provide paths to the immediately preceding 1–2 completed `.md` and `.png` files as concrete examples of formatting, tone, and footnote style.
2. **Current Target Folio(s)**: Path to the target `.png` scan(s).
3. **Pre-detected Graphics (if any)**: If a graphic was detected on the page, provide the graphic path `0255.g1.png` so the subagent can insert the image tag at the appropriate place in the text.
4. **Output Target Path**: Specific `resources/.../XXXX.md` path.

---

## 3. Compound Footnote Standard (`[^<page>_<num>]`)

Heath restarts footnote numbering (`1`, `2`, `3`...) on every printed page. To allow seamless concatenation of atomic pages into unified chapter/section documents without identifier collisions, use the **compound footnote format**:

```markdown
<!-- In page 89 (folio 0103.md) -->
...mentioned in the *Fihrist*[^89_1]...
...as noted by Steinschneider[^89_2]...

[^89_1]: *Fihrist*, p. 265.
[^89_2]: *Zeitschrift für Math. u. Phys.* xxxv. (1890).
```

### Key Rules:
- The prefix is the **printed page number** (e.g., `89`), followed by an underscore `_` and the footnote index (`1`, `2`, `3`).
- In commentary and proposition text, footnote definitions appear at the bottom of the atomic `.md` file.

---

## 4. Diagram Detection & Cropping Pipeline

### Upfront Pre-Transcription Detection
We run the detection script **before** launching transcription for a folio. This determines upfront whether a graphic is present, identifies its bounding box, and generates `XXXX.json` and `XXXX.g1.png`. The transcription subagent is then simply instructed to position the image tag at the correct narrative location.

The automated pipeline is in `src/geometor/euclid/ingest/detect_graphics_cv.py` and `src/geometor/euclid/scripts/graphic_tool.py`.

### Running with `uv`:
```bash
/home/phi/.local/bin/uv run python src/geometor/euclid/scripts/graphic_tool.py <command>
```

### Commands:

#### 1. Auto-Detect Graphic Bounding Box
Analyzes connected components, filters horizontal text lines, and finds the core diagram and letter labels:
```bash
/home/phi/.local/bin/uv run python src/geometor/euclid/scripts/graphic_tool.py detect <path/to/scan.png>
```
Output:
```json
{
  "x_offset": 343,
  "y_offset": 158,
  "crop_box": [287, 189]
}
```

#### 2. Crop, Clean, Invert, and Save Metadata JSON
Crops the specified bounding box, performs linear levels adjustment (`white_point=226`) to eliminate paper bleed-through, creates `<folio>.g1.inverted.png`, and saves crop info to `<folio>.json`:
```bash
/home/phi/.local/bin/uv run python src/geometor/euclid/scripts/graphic_tool.py crop \
  resources/heath/volume_I/book_i/propositions/0255.png \
  resources/heath/volume_I/book_i/propositions/0255.g1.png \
  --bbox 343 158 287 189 \
  --invert
```

#### 3. Precomputed Proposition Catalog
All 48 propositions of Book I (and books throughout Volumes I–III) have precomputed baseline offsets in:
`resources/heath/volume_I/book_i/propositions/index.json`
You can pass these offsets directly or tweak them slightly to tighten the crop box.

---

## 5. Zoom Inspection for Hard-to-Read Text

When encountering tiny polytonic Greek characters, faint breathings (rough ῾ vs smooth ᾿), iota subscripts (ᾳ, ῃ, ῳ), or dense critical apparatus, use the `zoom` tool to crop a high-resolution region of interest into `scratch/`:

```bash
/home/phi/.local/bin/uv run python src/geometor/euclid/scripts/graphic_tool.py zoom \
  resources/heath/volume_I/book_i/common_notions/0175.png \
  scratch/zoom_p175_greek.png \
  --bbox 150 420 500 180
```
Then use `view_file` on `scratch/zoom_p175_greek.png` to inspect the text in isolation without surrounding page clutter.

---

## 6. Perseus TEI XML Ground-Truth Cross-Validation

The repository contains digitized Perseus TEI XML for all 13 books in:
`resources/xml/books/01.xml` through `13.xml`.

The XML contains:
- English enunciation and proof text for every definition, postulate, common notion, and proposition.
- Heath's translation footnotes and critical notes (including Greek citations).
- Page numbers (`<pb n="241" />`).

### Querying XML:
```bash
# Query Proposition 1 in Book 1:
/home/phi/.local/bin/uv run python src/geometor/euclid/scripts/graphic_tool.py xml 1 prop.1

# Query Definition 4:
/home/phi/.local/bin/uv run python src/geometor/euclid/scripts/graphic_tool.py xml 1 def.4

# Query Postulate 1:
/home/phi/.local/bin/uv run python src/geometor/euclid/scripts/graphic_tool.py xml 1 post.1
```

> [!NOTE]
> The TEI XML contains only the core mathematical enunciations, proofs, and translation notes. Heath's extensive historical and mathematical commentary that follows each proposition is **not in the XML** and must be visually transcribed from the scan.

---

## 7. Proposition Anatomy & Formatting Standards

Each proposition in Heath is structured into classical components:
1. **Header**: `# PROPOSITION N.`
2. **Enunciation**: The general statement of the theorem or problem.
3. **Setting-out (*ekthesis*)**: "Let *AB* be the given finite straight line..."
4. **Specification (*diorismos*)**: "Thus it is required to construct..."
5. **Construction (*kataskeue*)**: "With centre *A* and distance *AB*..."
6. **Proof (*apodeixis*)**: "Now, since the point *A* is the centre..."
7. **Conclusion (*sumperasma*)**: "Therefore the triangle *ABC* is equilateral..."
8. **Q.E.D. / Q.E.F.**: "Being what it was required to do." (Q.E.F. / ὅπερ ἔδει ποιῆσαι) or "Being what it was required to prove." (Q.E.D. / ὅπερ ἔδει δεῖξαι).

### Marginal Line Numbers
When Heath provides marginal line numbers in the proofs, preserve them using span tags:
```markdown
Thus it is required to construct<span class="lineno">5</span> an equilateral triangle on the straight line *AB*.
```

### Frontmatter Standard
Every atomic page `.md` begins with YAML frontmatter:
```yaml
---
folio: "0255"
page: "241"
volume: "I"
book: "I"
section: "propositions"
title: "Proposition 1"
---
```

---

## 8. Specialized Subagent Roles

1. **`heath_transcriber`**:
   Responsible for granular visual transcription of page folios, maintaining full polytonic Greek and footnote fidelity, cross-checking with XML, and linking local graphics.

2. **`graphic_extractor`**:
   Specialized subagent responsible for scanning proposition pages, detecting figures with `graphic_tool.py detect` or `index.json`, fine-tuning bounding boxes, applying levels cleaning, generating dark-mode negatives, and saving both assets to `resources/` and `docsrc/heath/_static/graphics/`.

---

## 9. Git Workflow & Commits

- Commit completed chapters and major milestones atomically.
- Use conventional commit messages:
  - `feat(heath): transcribe Volume I Front Matter (folios 0001-0014)`
  - `feat(heath): transcribe Volume I Introduction Chapters I-IX (folios 0015-0166)`
  - `feat(heath): transcribe Book I First Principles pp. 153-172 (folios 0167-0186)`
  - `feat(heath): transcribe Book I Propositions 1-4 (folios 0255-0262)`
