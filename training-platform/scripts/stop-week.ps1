[CmdletBinding()] param([Parameter(Mandatory)][ValidateRange(1,13)][int]$Week,[switch]$RemoveVolumes)
. (Join-Path $PSScriptRoot 'common.ps1'); Assert-Command docker; Import-TrainingEnv
$composeArgs=Get-ComposeArgs $Week; $composeArgs += 'down'; if($RemoveVolumes){$composeArgs += '--volumes'}
& docker compose @composeArgs; if($LASTEXITCODE -ne 0){throw 'Docker Compose stop failed.'}
