# Windows setup and running guide

This is a one-time operational guide, not a Windows curriculum. Students may copy the commands exactly. Assessment focuses on understanding the services, state, cases, signals, and recovery—not on PowerShell or Windows administration.

## Required software

- Windows 10 or 11 (64-bit)
- PowerShell 7 or newer (`pwsh --version`)
- Git for Windows (`git --version`)
- Python 3.11 or newer (`py -3 --version`)
- Docker Desktop with the WSL 2 engine and Linux containers (`docker version`)

In Docker Desktop, wait until the engine reports **Running**. Allocate at least 4 GB memory and 2 CPUs; 8 GB memory is more comfortable for weeks that enable databases.

## Clone or unzip safely

Use a short path such as `C:\training\engineering-onboarding-windows`. Avoid OneDrive-synchronized folders for Docker database volumes. Open the folder in PowerShell 7:

```powershell
Set-Location C:\training\engineering-onboarding-windows
Set-ExecutionPolicy -Scope Process Bypass
.\training-platform\scripts\setup.ps1
```

The execution-policy change lasts only for the current PowerShell process. If your organization blocks it, run commands individually or ask IT to allow signed/local scripts.

## Python virtual environment

The setup script creates `.venv` in the repository root. To do it manually:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\training-platform\requirements.txt
```

Deactivate with `deactivate`. Never use `source .venv/bin/activate` on Windows.

## Normal operations

```powershell
.\training-platform\scripts\start-week.ps1 -Week 2
.\training-platform\scripts\smoke-test.ps1 -Week 2
.\training-platform\scripts\stop-week.ps1 -Week 2
.\training-platform\scripts\reset-week.ps1 -Week 2
.\training-platform\student\run-case.ps1 -Case week-02-practice
.\training-platform\student\reset-case.ps1
```

Pass `-NoBuild` to `start-week.ps1` to reuse the current simulator image. Use `-RemoveVolumes` with `stop-week.ps1` only when you intentionally want to discard environment data.

## Windows-specific troubleshooting

- **`docker` is not recognized:** restart PowerShell after installing Docker Desktop.
- **Engine connection error:** start Docker Desktop and confirm Linux containers mode.
- **Script execution is disabled:** use `Set-ExecutionPolicy -Scope Process Bypass` in the same window.
- **Port 8080 is busy:** set `$env:TRAINING_API_PORT='8088'` before starting, then use that port for smoke tests.
- **Path too long:** move the repository closer to the drive root and enable long paths through organizational policy if permitted.
- **File sharing prompt:** allow Docker Desktop access to the drive containing the repository.
- **Virtualenv activation blocked:** call `.\.venv\Scripts\python.exe` directly.
- **CRLF/LF warnings:** expected for text files; `.gitattributes` preserves scripts and configuration consistently.

## Clean-up

Stopping a week preserves volumes by default. Reset is destructive to training data only. Student source files remain on the host.
