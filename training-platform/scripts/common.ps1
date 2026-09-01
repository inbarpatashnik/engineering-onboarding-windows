Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$script:PlatformRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$script:RepoRoot = (Resolve-Path (Join-Path $script:PlatformRoot '..')).Path
function Assert-Command([string]$Name) { if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) { throw "Required command '$Name' was not found. See WINDOWS-SETUP.md." } }
function Assert-Week([int]$Week) { if ($Week -lt 1 -or $Week -gt 13) { throw 'Week must be between 1 and 13.' } }
function Get-WeekConfig([int]$Week) { Assert-Week $Week; Get-Content (Join-Path $script:PlatformRoot ("environments\week-{0:D2}.json" -f $Week)) -Raw | ConvertFrom-Json }
function Get-ComposeArgs([int]$Week) { $cfg=Get-WeekConfig $Week; $composeArgs=@('--project-directory',$script:PlatformRoot,'-f',(Join-Path $script:PlatformRoot 'compose.yaml')); foreach($p in $cfg.profiles){$composeArgs += @('--profile',[string]$p)}; return $composeArgs }
function Get-ApiBase { $port = if ($env:TRAINING_API_PORT) {$env:TRAINING_API_PORT} else {'8080'}; return "http://localhost:$port" }
function Import-TrainingEnv { $file=Join-Path $script:PlatformRoot '.env'; if(Test-Path $file){ foreach($line in Get-Content $file){ if($line -match '^([^#=]+)=(.*)$'){ [Environment]::SetEnvironmentVariable($Matches[1].Trim(),$Matches[2].Trim(),'Process') } } } }
