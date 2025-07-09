import argparse
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


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown files to PDF. Pandoc is required.")
    # nargs="?" makes these arguments optional
    parser.add_argument("input", nargs="?", help="Path to the input markdown file (e.g., README.md)")
    parser.add_argument("output", nargs="?", help="Path to the output PDF file (e.g., CV.pdf)")

    args = parser.parse_args()

    # If both input and output are provided via CLI, use them
    if args.input and args.output:
        convert_markdown_to_pdf(args.input, args.output)

    # If only one is provided, catch the user error or show usage
    elif args.input or args.output:
        print("Error: Please provide both an input file and an output file, or neither to run defaults.")
        parser.print_help()
    else:
        raise ValueError("Need input and output")

if __name__ == "__main__":
    main()