[CmdletBinding()] param([Parameter(Mandatory)][ValidateRange(1,13)][int]$Week)
. (Join-Path $PSScriptRoot 'common.ps1'); Import-TrainingEnv
$base=Get-ApiBase; $health=Invoke-RestMethod "$base/health" -TimeoutSec 5; if($health.status -ne 'ok'){throw 'Health check failed.'}
$resources=Invoke-RestMethod "$base/api/resources" -TimeoutSec 5; if($resources.items.Count -lt 1){throw 'Seeded resources are missing.'}
$state=Invoke-RestMethod "$base/api/state" -TimeoutSec 5
Write-Host "PASS week $Week: health=$($health.status), resources=$($resources.items.Count), fault=$($state.fault_mode)" -ForegroundColor Green
