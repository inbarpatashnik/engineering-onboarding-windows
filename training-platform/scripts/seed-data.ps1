[CmdletBinding()] param([Parameter(Mandatory)][ValidateRange(1,13)][int]$Week)
. (Join-Path $PSScriptRoot 'common.ps1'); Import-TrainingEnv
$python=Join-Path $script:RepoRoot '.venv\Scripts\python.exe'; if(-not(Test-Path $python)){throw 'Run setup.ps1 first.'}
$out=Join-Path $script:PlatformRoot ("data\generated\week-{0:D2}.json" -f $Week)
& $python (Join-Path $script:PlatformRoot 'python\generate_training_data.py') --week $Week --output $out
$payload=Get-Content $out -Raw; $headers=@{Authorization="Bearer $env:TRAINING_ADMIN_TOKEN"}
$base=Get-ApiBase; $deadline=(Get-Date).AddSeconds(60); do { try {$null=Invoke-RestMethod "$base/health" -TimeoutSec 2; break} catch {Start-Sleep -Seconds 2} } while((Get-Date)-lt$deadline)
Invoke-RestMethod "$base/admin/seed" -Method Post -Headers $headers -ContentType 'application/json' -Body $payload | Out-Null
Write-Host "Seeded deterministic data for week $Week." -ForegroundColor Green
