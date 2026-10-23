# GodotDocs

A directory of [Godot](https://godotengine.org/) documentation in `.md` format, suitable for RAG (Retrieval-Augmented Generation) applications. This project replaces the standard RST files with Markdown for easier parsing and integration with LLM-based tools.

## Prerequisites

- Python 3.x
- A virtual environment (venv)

## Setup

1. Navigate to the project directory:

   ```bash
   cd GodotDocs
   ```

2. Create and activate the virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies (includes rst-to-myst):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The easiest way to run the full conversion pipeline is with the provided script:

```bash
python run_conversion.py
```

Or manually:

1. Clone (or pull updates to) the Godot docs repository into `input-rst/`:

   ```bash
   cd input-rst
   git clone https://github.com/godotengine/godot-docs.git
   # or `git pull` later to update the repository
   ```

2. Copy the source into the output directory (working copy):

   ```bash
   cp -r input-rst/godot-docs/ output-md/godot-docs/
   ```

3. Convert RST files to MyST Markdown **in the output directory**:

   ```bash
   rst2myst convert output-md/godot-docs/**/*.rst
   ```

   This creates a `.md` file alongside each `.rst` (e.g., `guides/basic.rst` → `guides/basic.md`). The original `.rst` files are untouched.

4. Remove `.rst` files from the output directory (keep only converted `.md`):

   ```bash
   find output-md/godot-docs/ -type f -name "*.rst" -delete
   ```

   After conversion, each directory contains both `.rst` and `.md`. This step removes the `.rst` files, leaving only the final converted `.md` output.

The Markdown output is directly compatible with most RAG pipelines (e.g., LangChain, ChromaDB, FAISS).

## Project Structure

```
GodotDocs/
├── README.md
├── .venv/               # Virtual environment (gitignored)
├── input-rst/           # Source RST files from Godot docs repo
│   └── godot-docs/      # Cloned Godot documentation
│       └── *.rst        # Original source files
├── output-md/           # Final converted Markdown output for RAG
│   └── godot-docs/      # Clean copy of Godot documentation
|       └── *.md         # Converted markdown files
├── output-md-backup/    # Backup of previously converted documentation
└── requirements.txt     # Dependencies including rst-to-myst
```

