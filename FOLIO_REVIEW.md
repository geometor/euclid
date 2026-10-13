# Euclid Folio Review Application (`folio_review`)

A dedicated, lightweight web application for quality-assuring, proofreading, and vetting the digital reconstruction of Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements* (1,438 folios across Volumes I, II, and III).

---

## Table of Contents

1. [Overview & Purpose](#overview--purpose)
2. [Quick Start](#quick-start)
3. [Architecture & Data Sources](#architecture--data-sources)
4. [Dashboard (`/`)](#dashboard-)
5. [Folio Review Workspace (`/folio/<volume>/<folio>`)](#folio-review-workspace-foliovolumefolio)
   - [Scan Viewer (Left Pane)](#scan-viewer-left-pane)
   - [Transcription Previewer (Right Pane)](#transcription-previewer-right-pane)
   - [Scholarly Notes](#scholarly-notes)
   - [Graphics Calibration & Re-Extraction](#graphics-calibration--re-extraction)
   - [Vetting & Verification Checklist](#vetting--verification-checklist)
6. [Keyboard Shortcuts (`hjkl`)](#keyboard-shortcuts-hjkl)
7. [Recommended Vetting Workflow](#recommended-vetting-workflow)
8. [Persistence & Review Records](#persistence--review-records)

---

## Overview & Purpose

The `folio_review` application was built to solve the tedious challenge of manually proofreading and validating over 1,400 reconstructed folio scans:

- **100% Transcription Verification**: Comparing Heath's original scan directly against the markdown transcription (`.md`).
- **Mathematical Validation**: Inspecting KaTeX equations, inline Greek mathematical symbols, and formatting.
- **Graphic Alignment & Calibration**: Reviewing diagram bounding boxes (`.json`) overlaid directly onto the scan, with real-time recalculation and crop re-extraction.
- **Scholarly Notes Review**: Ensuring that philological notes, textual apparatus references, and cross-folio continuity comments (`.notes.md`) are accurate.
- **Persistent Vetting Records**: Tracking review statuses (`verified`, `needs_fix`, `flagged`) and reviewer checklists in a version-controlled JSON store (`resources/heath/folio_reviews.json`).

---

## Quick Start

### Launching the Review App

Run using `uv`:

```bash
# Launch on default interface (http://127.0.0.1:5000)
uv run folio_review

# Launch accessible across local network (e.g. tablet / secondary monitor)
uv run folio_review --host 0.0.0.0 --port 5000
```

Alternatively, invoke via Python script:

```bash
uv run python scripts/run_folio_review.py --port 5000
```

Open your browser to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## Architecture & Data Sources

The review app is completely file-system backed. It requires no external database:

```
resources/heath/
├── folio_reviews.json               # Persistent vetting statuses & reviewer notes
├── volume_I/
│   └── book_i/
│       └── propositions/
│           ├── 0314.png             # Full folio scan (original Heath edition)
│           ├── 0314.md              # Markdown transcription with YAML frontmatter
│           ├── 0314.notes.md        # Scholarly commentary & textual observations
│           ├── 0314.json            # Graphics bounding box metadata
│           ├── 0314.g1.png          # Normal extracted crop
│           └── 0314.g1.inverted.png # Dark-mode inverted crop
├── volume_II/
└── volume_III/
```

### Core Python Components (`src/geometor/euclid/folio_review/`)

- **`scanner.py` (`FolioScanner`)**:
  - Auto-discovers and indexes all 1,438 folios across all volumes and section directories.
  - Automatically parses frontmatter and pre-renders Markdown and Notes into HTML.
  - Features dynamic URL rewriting (`fix_relative_media_urls`) so relative image links like `![caption](0314.g1.png)` resolve directly.
  - Employs a low-TTL live cache so concurrent transcription edits on disk appear automatically.
- **`reviews.py` (`ReviewManager`)**:
  - Thread-safe persistence of vetting records to `resources/heath/folio_reviews.json`.
- **`app.py` (`create_app`)**:
  - Flask application with REST API endpoints, image streaming routes, and inline text saving.

---

## Dashboard (`/`)

The Dashboard provides a top-level progress summary and table of all folios:

- **Metrics Cards**:
  - Overall transcription completion percentage.
  - Scholarly notes coverage.
  - Folios with extracted graphics vs. text-only folios.
  - Vetting progress: *Verified*, *Needs Fix*, *Flagged*, and *Unreviewed*.
- **Volume & Section Filtering**: Filter by Volume (I, II, III), section path, review status, or free-text search (searching folio numbers, proposition numbers, or titles).
- **Vim Navigation**: Use `j` and `k` to navigate rows in the table; press `Enter` or `l` to jump straight into the folio workspace.

---

## Folio Review Workspace (`/folio/<volume>/<folio>`)

The review workspace features a split-pane interface designed specifically for side-by-side comparison.

### Scan Viewer (Left Pane)

- **Pan & Zoom Engine**:
  - Click and drag to pan freely across the high-resolution page scan.
  - Zoom in (`+`) or out (`-`) via toolbar buttons or mouse wheel.
  - **Fit Page (`f`)**: Fits the entire scan into the current viewport.
  - **Fit Figure (`z`)**: Instantly focuses and centers the first graphic bounding box at optimal reading zoom.
  - **1:1 (`100%`)**: Resets to native pixel resolution.
- **SVG Bounding Box Overlay**:
  - Green interactive rectangles highlight calibrated figure locations (`[x, y, w, h]`).
  - Hovering a rectangle displays figure ID and highlights the graphic. Clicking it jumps directly to the calibration card in the Graphics tab.
  - Press `b` to toggle overlays on/off.
- **Mouse Coordinate HUD**:
  - Moving the mouse over the scan displays the exact real-pixel coordinates (`X: ..., Y: ...`), making it trivial to find coordinates for new or misplaced figures.
- **Color Inversion (`i`)**:
  - Inverts the scan (white text on dark background) to reduce eye fatigue during night work.

### Transcription Previewer (Right Pane)

- **Classical Heath Book Simulation**:
  - Typeset in **EB Garamond** serif with true book typography.
  - Pure white background (`#ffffff`) with deep black ink (`#000000`) matching the high contrast of the physical printed page.
  - Paragraphs formatted with classic book first-line indents (`1.75em`) and justified text.
- **Typographic Tuning Controls**:
  - **Font Size (`A-` / `A+`)**: Adjust preview font size on the fly to match the physical scan line-for-line.
  - **Column Width Selector**: Switch between *Book (540px)*, *Narrow (480px)*, *Medium (600px)*, or *Full Width*.
  - **Indent Toggle**: Toggle between book indent style and block paragraph style.
- **Right-Floating Graphics**:
  - Proposition diagrams float on the right margin with proof text wrapping naturally along the left, mirroring Heath's original layout.
- **Three View Modes**:
  - **Rendered**: Full book page simulation with formatted KaTeX mathematical expressions and embedded diagrams.
  - **Raw**: Monospaced view of the raw markdown file with YAML frontmatter.
  - **Edit**: In-browser markdown editor. Make corrections directly and click **Save Markdown to Disk** to update the `.md` file immediately.

### Scholarly Notes

Click the **Notes** tab to review the corresponding `<folio>.notes.md` file:

- Inspect summaries, preceding/following folio continuity, mathematical commentary, and translation footnotes.
- Like the transcription tab, Notes can be viewed rendered, viewed raw, or edited and saved directly to disk.

### Graphics Calibration & Re-Extraction

Click the **Graphics** tab to manage figures defined in `<folio>.json`:

- **Side-by-Side Crop Comparison**: Inspect both the standard crop (`.png`) and dark-mode inverted crop (`.inverted.png`).
- **Bounding Box Recalibration**:
  - Edit `X`, `Y`, `Width`, and `Height` coordinates.
  - Click **Recalibrate**: The app writes the updated coordinates to `<folio>.json` and runs `graphic_tool` to regenerate the crops on disk.
- **Re-Extract Crops Button**: Re-runs extraction across all figures on the page if crop files are missing or updated.

### Vetting & Verification Checklist

Click the **Vetting** tab (or use the status dropdown in the header):

- **Status Selection**:
  - `Verified`: Transcription, math, notes, and figures are 100% vetted.
  - `Needs Fix`: Errors found (e.g. typos, missing math formatting, misaligned crop).
  - `Flagged`: Scholarly ambiguity or question requiring architectural discussion.
  - `Unreviewed`: Default pending review status.
- **Quality Checklist**:
  - [x] Transcription verified against scan
  - [x] Mathematical notation & KaTeX checked
  - [x] Scholarly notes verified
  - [x] Figures & bounding box crops aligned
- **Review Notes**: Enter notes explaining what was fixed or what needs attention, then click **Save Vetting Record**.

---

## Keyboard Shortcuts (`hjkl`)

The review app is built for rapid, keyboard-first navigation:

| Key | Context | Action |
| :--- | :--- | :--- |
| **`l`** or **`j`** | Workspace | Navigate to **Next Folio** |
| **`h`** or **`k`** | Workspace | Navigate to **Previous Folio** |
| **`j`** / **`k`** | Dashboard | Select next / previous table row |
| **`Enter`** / **`l`** | Dashboard | Open selected folio |
| **`f`** | Workspace | **Fit Page** (fit scan to viewport) |
| **`z`** | Workspace | **Fit Figure** (zoom to first bounding box) |
| **`b`** | Workspace | Toggle **Bounding Box Overlays** |
| **`i`** | Workspace | Toggle **Invert Scan** (dark/light) |
| **`+`** / **`=`** | Workspace | Zoom in scan |
| **`-`** | Workspace | Zoom out scan |
| **`0`** | Workspace | Reset scan zoom to 100% |
| **`1`** | Workspace | Switch to **Transcription** tab |
| **`2`** | Workspace | Switch to **Notes** tab |
| **`3`** | Workspace | Switch to **Graphics** tab |
| **`4`** | Workspace | Switch to **Vetting** tab |
| **`v`** | Workspace | Mark folio as **Verified** |
| **`n`** | Workspace | Mark folio as **Needs Fix** |
| **`?`** | Anywhere | Open **Keyboard Shortcuts Help Modal** |
| **`Esc`** | Anywhere | Close active modal |

*(Note: Single-key shortcuts are automatically ignored when typing in text inputs or textareas).*

---

## Recommended Vetting Workflow

For reviewers proofreading folios:

1. **Open Folio**: Open a folio from the Dashboard or navigate using `h`/`l`.
2. **Scan Alignment**:
   - Press `f` to see the full page scan.
   - Adjust the previewer font size (`A-`/`A+`) until line lengths roughly align with the scan.
3. **Verify Text & Math**:
   - Read through the rendered markdown alongside the scan.
   - Check that proposition numbers, enunciations, proofs, and KaTeX math formulas match Heath's text.
   - If a typo is found: switch to **Edit** mode, fix the error, and click **Save Markdown to Disk**.
4. **Check Figures**:
   - Press `b` to verify that bounding box overlays tightly surround the diagrams without cutting off letters ($A, B, C...$).
   - If a crop is shifted: check coordinates using the Coordinate HUD, enter adjusted `X, Y, W, H` in the Graphics tab, and click **Recalibrate**.
5. **Verify Notes**:
   - Switch to the **Notes** tab (`2`). Ensure continuity across preceding and following folios is maintained.
6. **Set Status**:
   - Switch to the **Vetting** tab (`4`) or press `v` to mark **Verified**.
   - Check off the verification checklist and add any relevant notes.
7. **Advance**:
   - Press `l` to move to the next folio.

---

## Persistence & Review Records

All review decisions and notes are saved directly to:

```
resources/heath/folio_reviews.json
```

Example review record:

```json
{
  "volume_I:0314": {
    "volume": "volume_I",
    "folio": "0314",
    "status": "verified",
    "checklist": {
      "transcription_verified": true,
      "math_verified": true,
      "notes_verified": true,
      "graphics_verified": true
    },
    "notes": "Menelaus alternative proof and figure verified. KaTeX alignment matches scan.",
    "reviewer": "phi",
    "updated_at": "2026-10-13T10:15:00Z"
  }
}
```

Because this file is tracked in Git, review progress can be committed and shared across team members.
