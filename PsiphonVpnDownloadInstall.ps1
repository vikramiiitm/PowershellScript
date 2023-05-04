$url = "https://psiphon.ca/psiphon3.exe"
$output = "C:\Users\Vikram Chowdhury\Desktop\PowershellScript\Download\psiphon3.exe"

# Using BitsTransfer module to downlaod
Import-Module BitsTransfer

Write-Host "Starting to download the file ..."
Start-BitsTransfer -Source $url -Destination $output


Write-Host "Starting to install the software"
Start-Process "C:\Users\Vikram Chowdhury\Desktop\PowershellScript\Download\psiphon3.exe" -ArgumentList "/S /v/qn"
