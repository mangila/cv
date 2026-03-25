### Project Guidelines

#### Build/Configuration Instructions

The project uses [Pandoc](https://pandoc.org/) and [XeLaTeX](https://tug.org/xetex/) to convert Markdown files into PDF
format and python scripts to automate the conversion process.

- **Dependencies**:
    - `pandoc`
    - `texlive-xetex` (or equivalent package providing `xelatex`)
    - `fonts-dejavu` (the script specifically uses "DejaVu Sans")
    - `python3`

- **Build Process**:
    - Execute the `python convert.py` script to generate `CV.pdf` from `README.md` and `SV_CV.pdf` from `SV.md`.

#### Additional Development Information

- **CV Matcher Workflow**:
    - This repository functions as a "CV Matcher."
    - `README.md` (English) and `SV.md` (Swedish) are the master templates containing all professional experience.
    - When provided with a **job advertisement**, the goal is to create a tailored CV that highlights the most relevant
      skills and experiences for that specific role.
    - **Process**:
        1. Analyze the job ad for key requirements and keywords.
        2. Extract relevant experiences from the master templates (`README.md` or `SV.md`).
        3. Create a new tailored Markdown file (e.g., `(Company Name)_CV.md`).
        4. Create a small Markdown file for the hiring team (e.g., `(Company Name)_MESSAGE.md`).
        5. Use `convert.py` (or modify it) to generate a PDF for the tailored CV.
- **Code Style**:
    - Markdown files should follow a clean structure with clear headers.
- **Workflow**:
    - Master edits are made in the base `.md` files.
    - The `convert.py` script is the single point of truth for the conversion parameters.
