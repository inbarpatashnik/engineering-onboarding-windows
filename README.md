# Engineering Onboarding — Windows-first package

This repository is a complete 13-week engineering onboarding program for one student and one mentor. The required student path assumes **Windows 10/11**, **PowerShell 7+**, **Git**, **Python 3.11+**, and **Docker Desktop using Linux containers**. No required workflow depends on Bash, Make, `chmod`, Unix sockets, symbolic links, or `/tmp` paths.

## Start here

1. Read [WINDOWS-SETUP.md](WINDOWS-SETUP.md).
2. Open PowerShell 7 in this folder (not Command Prompt).
3. Run `Set-ExecutionPolicy -Scope Process Bypass` if local policy blocks scripts.
4. Run `.\training-platform\scripts\setup.ps1`.
5. Run `.\training-platform\scripts\start-week.ps1 -Week 1`.
6. Run `.\training-platform\scripts\smoke-test.ps1 -Week 1`.
7. Student: open `student\week-01\assignment.md`. Mentor: open `mentor\week-01\guide.md`.

## Package index

| Location | Audience | Purpose |
|---|---|---|
| `curriculum/` | Both | Syllabus, 13-week map, assessment rubric |
| `student/` | Student | Weekly briefs, exercises, deliverables, definitions of done |
| `mentor/` | Mentor only | Review guidance, hints, red flags, incident keys |
| `training-platform/` | Both, controls mentor-only | Docker environment, simulator, scripts, seed data, fault presets |
| `WINDOWS-SETUP.md` | Both | Installation and troubleshooting instructions |

## Weekly command loop

```powershell
.\training-platform\scripts\start-week.ps1 -Week 4
.\training-platform\scripts\seed-data.ps1 -Week 4
.\training-platform\scripts\smoke-test.ps1 -Week 4
# complete the assignment
.\training-platform\scripts\stop-week.ps1 -Week 4
```

Use `reset-week.ps1` when you need a clean deterministic state. Reset removes the week's Docker volumes and reseeds them; do not store personal work inside containers.

## Privacy boundary

The `mentor/` directory and `training-platform/mentor/` directory contain solutions, fault controls, and incident answers. Keep them outside the student's working copy when assessment integrity matters.

## Offline behavior

The first setup needs internet access to pull container images and install Python packages. After images and packages are cached, the simulator and curriculum can run locally. All training data is synthetic.
