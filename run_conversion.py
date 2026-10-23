#!/usr/bin/env python3
"""Convert cloned Godot RST docs to MyST Markdown and clean up."""

import os
import subprocess
import shutil
import sys


def run(cmd, check=True):
    """Run a shell command and print output."""
    print(f"$ {cmd}")
    result = subprocess.run(
        cmd, shell=True, text=True, capture_output=False
    )
    if result.returncode != 0:
        if check:
            raise RuntimeError(f"Command failed: {cmd}")
        return False
    return True


def main():
    project_root = os.path.dirname(os.path.abspath(__file__)) or "."

    # Paths
    rst_dir = os.path.join(project_root, "input-rst", "godot-docs")
    output_dir = os.path.join(project_root, "output-md")

    print("=== Step 1: Clone (or pull) Godot docs ===")
    if not os.path.isdir(rst_dir):
        run(f"git clone https://github.com/godotengine/godot-docs.git {rst_dir}")
    else:
        run("git -C input-rst/godot-docs pull")

    print("=== Step 2: Backup existing output, then clear ===")

    # Check if there's anything in the output directory yet
    if os.path.isdir(output_dir) and os.listdir(output_dir):
        backup_dir = os.path.join(project_root, "output-md-backup")
        run(f"mkdir -p '{backup_dir}'")

        # Copy existing files to a backup location (preserving structure)
        for root, dirs, files in os.walk(output_dir):
            rel_path = os.path.relpath(root, output_dir)
            if rel_path == ".":
                dest = backup_dir
            else:
                dest = os.path.join(backup_dir, rel_path)
            shutil.copytree(root, dest, dirs_exist_ok=True)

        print(f"  → Backed up existing content to output-md-backup/")

    # Clear the output directory for a clean state
    run(f"rm -rf '{output_dir}' && mkdir -p '{output_dir}'")

    print("  → Output directory cleared and ready.")
    print("\n=== Step 3: Copy only .rst files to output (working copy) ===")
    for root, dirs, files in os.walk(rst_dir):
        for name in files:
            if name.endswith(".rst"):
                src = os.path.join(root, name)
                rel = os.path.relpath(src, rst_dir)
                dst = os.path.join(output_dir, rel)
                parent = os.path.dirname(dst)
                if parent != ".":
                    os.makedirs(parent, exist_ok=True)
                shutil.copy2(src, dst)

    print("\n=== Step 4: Convert RST to MyST Markdown ===")
    # Use rst2myst's glob pattern to convert all .rst files in the working copy.
    # It creates a .md file alongside each .rst, without overwriting the original.
    run(f"rst2myst convert {output_dir}/**/*.rst")

    print("\n=== Step 5: Remove .rst files from output (keep only converted .md) ===")
    # After conversion, each directory has both .rst and .md. Remove the .rst files
    # so that only the converted .md files remain in the output directory.
    for root, _, files in os.walk(output_dir):
        for f in files:
            if f.endswith(".rst"):
                os.remove(os.path.join(root, f))

    print("\n=== Conversion complete! ===")


if __name__ == "__main__":
    main()
