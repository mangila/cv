# Project Guidelines

## Build/Configuration Instructions

The project uses [Pandoc](https://pandoc.org/) and [XeLaTeX](https://tug.org/xetex/) to convert Markdown files into PDF
format and python scripts to automate the conversion process.

- **Dependencies**:
  - `pandoc`
  - `texlive-xetex` (or equivalent package providing `xelatex`)
  - `fonts-dejavu` (the script specifically uses "DejaVu Sans")
  - `python3`

- **Build Process**:
  - Execute the `mise convert` script to generate `CV.pdf` from `README.md`

### Additional Development Information

- **CV Matcher Workflow**:
  - This repository functions as a "CV Matcher."
  - `README.md` (English) is the master templates containing all professional experience.
  - If the job advertisement is in Swedish, create a tailored CV in Swedish using the same process instead.
  - When provided with a **job advertisement**, the goal is to create a tailored CV that highlights the most relevant
    skills and experiences for that specific role.
  - **Process**:
        1. Analyze the job ad for key requirements and keywords.
        2. Extract relevant experiences from the master templates (`README.md`).
        3. Create a new tailored Markdown file (e.g., `(Company Name)_CV.md`).
        4. Create a small Markdown file for the hiring team (e.g., `(Company Name)_MESSAGE.md`).
        5. Use `convert.py` with the params like `python convert.py (Company Name)_CV.md (Company Name)_CV.pdf` to generate a PDF for the tailored CV.
- **Code Style**:
  - Markdown files should follow a clean structure with clear headers.
  - Run `mise format` to format the Markdown files.
  - Run `mise lint` to lint with vale and rumdl
- **Workflow**:
  - Master edits are made in the base `.md` files.
  - The `convert.py` script is the single point of truth for the conversion parameters.
