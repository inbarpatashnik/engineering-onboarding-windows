[CmdletBinding()] param()
. (Join-Path $PSScriptRoot '..\scripts\common.ps1'); Import-TrainingEnv
$body=@{mode='none';delay_ms=0;failure_rate=0}|ConvertTo-Json
Invoke-RestMethod "$(Get-ApiBase)/admin/fault" -Method Post -Headers @{Authorization="Bearer $env:TRAINING_ADMIN_TOKEN"} -ContentType 'application/json' -Body $body | Out-Null
Write-Host 'Faults reset.' -ForegroundColor Green
