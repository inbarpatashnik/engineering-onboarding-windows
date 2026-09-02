[CmdletBinding()] param()
. (Join-Path $PSScriptRoot '..\scripts\common.ps1')
$python=Join-Path $script:RepoRoot '.venv\Scripts\python.exe'
if(-not(Test-Path $python)){throw 'Run training-platform\scripts\setup.ps1 first.'}
& $python -m pip install --timeout 30 --retries 1 -r (Join-Path $PSScriptRoot 'requirements.txt')
if($LASTEXITCODE -ne 0){throw 'Week 10 dependency installation failed. Preserve the error; do not weaken TLS or download unofficial binaries.'}
& $python (Join-Path $PSScriptRoot 'auth-token-lab.py') self-test
if($LASTEXITCODE -ne 0){throw 'Week 10 token self-test failed.'}
Write-Host 'Week 10 asymmetric-token lab is ready.' -ForegroundColor Green
