Write-Host "entered"
$ip_address = $args[0]
Write-Host "wait start" $ip_address
Start-Sleep -Seconds $ip_address
Write-Host "end" $ip_address