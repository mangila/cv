#!/bin/bash

inputFile="cv.md"
outputFile="CV.pdf"

if [ ! -f "$inputFile" ]; then
    echo "Error: Input file $inputFile not found" >&2
    exit 1
fi

echo "Converting $inputFile to $outputFile..."

pandoc "$inputFile" -o "$outputFile" --pdf-engine=xelatex -V geometry:"margin=1cm" -V mainfont="DejaVu Sans" -V papersize=legal

if [ -f "$outputFile" ]; then
    echo "Conversion completed successfully!"
else
    echo "Error: Failed to create output file" >&2
    exit 1
fi