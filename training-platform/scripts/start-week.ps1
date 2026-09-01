[CmdletBinding()] param([Parameter(Mandatory)][ValidateRange(1,13)][int]$Week,[switch]$NoBuild)
. (Join-Path $PSScriptRoot 'common.ps1'); Assert-Command docker; Import-TrainingEnv
$composeArgs=Get-ComposeArgs $Week; $composeArgs += @('up','-d'); if(-not $NoBuild){$composeArgs += '--build'}
& docker compose @composeArgs; if($LASTEXITCODE -ne 0){throw 'Docker Compose failed.'}
& (Join-Path $PSScriptRoot 'seed-data.ps1') -Week $Week
Write-Host "Week $Week is running at $(Get-ApiBase)" -ForegroundColor Green
