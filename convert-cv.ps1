$inputFile = "cv.md"
$outputFile = "CV.pdf"

if (!(Test-Path $inputFile))
{
    Write-Error "Input file $inputFile not found"
    exit 1
}

try
{
    Write-Host "Converting $inputFile to $outputFile..."
    pandoc $inputFile `
        -f gfm `
        -o $outputFile `
        --pdf-engine=xelatex `
        -V geometry:"margin=1cm" `
        -V papersize=legal `
        -V mainfont:"Calibri" `
        --standalone

    if (Test-Path $outputFile)
    {
        Write-Host "Conversion completed successfully!"
    }
    else
    {
        Write-Error "Failed to create output file"
    }
}
catch
{
    Write-Error "An error occurred during conversion: $_"
}