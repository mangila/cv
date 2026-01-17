### Project Guidelines

#### Build/Configuration Instructions
The project uses [Pandoc](https://pandoc.org/) and [XeLaTeX](https://tug.org/xetex/) to convert Markdown files into PDF format.

- **Dependencies**:
  - `pandoc`
  - `texlive-xetex` (or equivalent package providing `xelatex`)
  - `fonts-dejavu` (the script specifically uses "DejaVu Sans")

- **Build Process**:
  - Execute the `./pandoc.sh` script to generate `CV.pdf` from `README.md` and `SV_CV.pdf` from `SV.md`.
  - Ensure the script has execution permissions: `chmod +x pandoc.sh`.

#### Testing Information
Testing for this project involves verifying that the Markdown to PDF conversion is working correctly.

- **Automated Verification**:
  - You can use a script to verify that `pandoc` is installed and can generate a PDF.
  - Example test script (`test_pandoc.sh`):
    ```bash
    #!/bin/bash
    echo "# Test" > test.md
    pandoc test.md -o test.pdf --pdf-engine=xelatex -V mainfont="DejaVu Sans"
    if [ -f test.pdf ]; then
        echo "Conversion successful"
        rm test.md test.pdf
    else
        echo "Conversion failed"
        exit 1
    fi
    ```

- **Adding New Tests**:
  - When modifying `pandoc.sh`, ensure that any new font or geometry options are available in the build environment.

#### Additional Development Information
- **CV Matcher Workflow**:
  - This repository functions as a "CV Matcher".
  - `README.md` (English) and `SV.md` (Swedish) are the master templates containing all professional experience.
  - When provided with a **job advertisement**, the goal is to create a tailored CV that highlights the most relevant skills and experiences for that specific role.
  - **Process**:
    1. Analyze the job ad for key requirements and keywords.
    2. Extract relevant experiences from the master templates (`README.md` or `SV.md`).
    3. Create a new tailored Markdown file (e.g., `Tailored_CV.md`).
    4. Use `pandoc.sh` (or modify it) to generate a PDF for the tailored CV.
- **Code Style**:
  - Markdown files should follow a clean structure with clear headers.
- **Workflow**:
  - Master edits are made in the base `.md` files.
  - The `pandoc.sh` script is the single point of truth for the conversion parameters.
