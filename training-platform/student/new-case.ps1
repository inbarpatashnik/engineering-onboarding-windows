[CmdletBinding()] param(
  [Parameter(Mandatory)][ValidatePattern('^[a-z0-9][a-z0-9-]*$')][string]$Name,
  [Parameter(Mandatory)][ValidateSet('delay','unavailable','malformed')][string]$Mode,
  [ValidateRange(0,10000)][int]$DelayMs=0,
  [ValidateRange(0.0,1.0)][double]$FailureRate=0.0,
  [string]$LearningGoal='Explain the observed failure and safe recovery.',
  [string]$ExpectedSignal='Record status, latency, request ID, logs, and recovery behavior.'
)
$root=(Resolve-Path (Join-Path $PSScriptRoot 'cases\custom')).Path; $path=Join-Path $root "$Name.json"
if(Test-Path $path){throw "Case '$Name' already exists. Choose a new name or edit it deliberately."}
@{name=$Name;mode=$Mode;delay_ms=$DelayMs;failure_rate=$FailureRate;learning_goal=$LearningGoal;expected_signal=$ExpectedSignal} |
  ConvertTo-Json | Set-Content -Path $path -Encoding utf8
Write-Host "Created $path" -ForegroundColor Green
