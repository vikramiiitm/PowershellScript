$BaseDir = Get-Location

$url = "https://psiphon.ca/psiphon3.exe"
$filename = "Psiphon3.exe"

$output = Join-Path -Path $BaseDir -ChildPath "\Download\$filename"

Write-Host $output
# Using BitsTransfer module to downlaod
Import-Module BitsTransfer

Write-Host "Starting to download the file ..."
Start-BitsTransfer -Source $url -Destination $output


Write-Host "Starting to install the software"
Start-Process "$output" -ArgumentList "/S /v/qn"
