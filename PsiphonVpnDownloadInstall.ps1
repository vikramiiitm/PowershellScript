$BaseDir = Get-Location
$filename = $args[0]
$url = $args[1]

Write-Host $file_name $url

$output = Join-Path -Path $BaseDir -ChildPath "\Download\$filename"

Write-Host $output

# Using BitsTransfer module to downlaod
Import-Module BitsTransfer

Write-Host "Starting to download the file ..."
Start-BitsTransfer -Source $url -Destination $output

Write-Host "Starting to install the software"
Start-Process "$output" -ArgumentList "/S /v/qn"
