[CmdletBinding()] param([Parameter(Mandatory)][ValidatePattern('^[a-z0-9][a-z0-9-]*$')][string]$Case)
. (Join-Path $PSScriptRoot '..\scripts\common.ps1'); Import-TrainingEnv
$builtIn=Join-Path $PSScriptRoot "cases\$Case.json"; $custom=Join-Path $PSScriptRoot "cases\custom\$Case.json"
$file=if(Test-Path $builtIn){$builtIn}elseif(Test-Path $custom){$custom}else{throw "Case '$Case' was not found."}
$scenario=Get-Content $file -Raw | ConvertFrom-Json
$body=@{mode=$scenario.mode;delay_ms=$scenario.delay_ms;failure_rate=$scenario.failure_rate}|ConvertTo-Json
Invoke-RestMethod "$(Get-ApiBase)/admin/fault" -Method Post -Headers @{Authorization="Bearer $env:TRAINING_ADMIN_TOKEN"} -ContentType 'application/json' -Body $body | Out-Null
Write-Host "Case '$Case' is active. Learning goal: $($scenario.learning_goal)" -ForegroundColor Yellow
Write-Host "Expected signal: $($scenario.expected_signal)"
