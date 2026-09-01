[CmdletBinding()] param([Parameter(Mandatory)][ValidatePattern('^week-(0[1-9]|1[0-3])$')][string]$Preset)
. (Join-Path $PSScriptRoot '..\scripts\common.ps1'); Import-TrainingEnv
$file=Join-Path $PSScriptRoot "incident-presets\$Preset.json"; $preset=Get-Content $file -Raw | ConvertFrom-Json
$body=@{mode=$preset.mode;delay_ms=$preset.delay_ms;failure_rate=$preset.failure_rate}|ConvertTo-Json
Invoke-RestMethod "$(Get-ApiBase)/admin/fault" -Method Post -Headers @{Authorization="Bearer $env:TRAINING_ADMIN_TOKEN"} -ContentType 'application/json' -Body $body | Out-Null
Write-Host "Fault preset $Preset enabled. Do not reveal its JSON to the student." -ForegroundColor Yellow
