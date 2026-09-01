[CmdletBinding()] param()
. (Join-Path $PSScriptRoot 'common.ps1')
Assert-Command docker; Assert-Command py
docker version | Out-Null
$envFile=Join-Path $script:PlatformRoot '.env'; if(-not(Test-Path $envFile)){Copy-Item (Join-Path $script:PlatformRoot '.env.example') $envFile}
$venv=Join-Path $script:RepoRoot '.venv'; if(-not(Test-Path $venv)){& py -3 -m venv $venv}
$python=Join-Path $venv 'Scripts\python.exe'; & $python -m pip install --upgrade pip; & $python -m pip install -r (Join-Path $script:PlatformRoot 'requirements.txt')
Write-Host 'Setup complete. Start week 1 with .\training-platform\scripts\start-week.ps1 -Week 1' -ForegroundColor Green
