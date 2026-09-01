[CmdletBinding()] param([string]$OutputPath)
. (Join-Path $PSScriptRoot '..\scripts\common.ps1')
if(-not $OutputPath){$OutputPath=Join-Path $script:RepoRoot 'student-work\week-01-git-lab'}
$python=Join-Path $script:RepoRoot '.venv\Scripts\python.exe'; if(-not(Test-Path $python)){throw 'Run training-platform\scripts\setup.ps1 first.'}
& $python (Join-Path $script:PlatformRoot 'python\build_week01_git_lab.py') --output $OutputPath
if($LASTEXITCODE -ne 0){throw 'Week 1 lab creation failed. The script never overwrites an existing lab.'}
Write-Host "Week 1 lab created at $OutputPath" -ForegroundColor Green
