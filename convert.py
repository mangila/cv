import subprocess
import sys
from pathlib import Path


def convert_markdown_to_pdf(input_file: str, output_file: str) -> None:
    input_path = Path(input_file)

    if not input_path.is_file():
        print(f"Error: Input file {input_file} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Converting {input_file} to {output_file}...")

    cmd = [
        "pandoc",

        # --- Input & Output ---
        input_file, "-o", output_file,

        # --- Engine ---
        "--pdf-engine=xelatex",

        # --- Layout & Typography ---
        "-V", "geometry:margin=1in",
        "-V", "fontsize=11pt",
        "-V", "mainfont=DejaVu Sans",
        "-V", "monofont=DejaVu Sans Mono",
        "-V", "linestretch=1.2",

        # --- Link Styling ---
        "-V", "colorlinks=true",
        "-V", "linkcolor=blue",
        "-V", "urlcolor=MidnightBlue",
        "-V", "urlstyle=same",
    ]

    result = subprocess.run(cmd)

    if result.returncode != 0:
        print("Error: pandoc failed", file=sys.stderr)
        sys.exit(1)

    if Path(output_file).is_file():
        print("Conversion completed successfully!")
    else:
        print("Error: Failed to create output file", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    convert_markdown_to_pdf("README.md", "CV.pdf")
    convert_markdown_to_pdf("SV.md", "SV_CV.pdf")
