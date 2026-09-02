[CmdletBinding()] param()
. (Join-Path $PSScriptRoot '..\scripts\common.ps1'); Assert-Command docker; Import-TrainingEnv
$args=Get-ComposeArgs 6
Write-Host 'Docker version:'; docker version
Write-Host 'Compose service status:'; docker compose @args ps
Write-Host 'Recent Kafka logs:'; docker compose @args logs --no-color --tail 120 kafka
Write-Host 'Save this output with the time and failing command. Continue with fallback-client-lab.py after the timebox.' -ForegroundColor Yellow
