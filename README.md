# IT Support Automation

IT Admin Toolset for repeatable Windows workstation health checks, safe maintenance cleanup, and technician-ready support reporting.

## Overview

IT Support Automation is a lightweight Python command-line utility designed for first-line support and workstation maintenance workflows. It checks local system health, verifies available storage, performs a safe cleanup against scoped temporary clutter, and writes a timestamped report that can be attached to tickets or retained for audit evidence.

The current implementation centers on `pc_health_check.py`, a local execution script that demonstrates a repeatable support automation pattern without touching high-risk system directories.

## 📋 The Administrative Burden

Support teams lose time to manual, repetitive checks that are necessary but low-value when performed by hand. Technicians often need to confirm operating system details, disk capacity, machine architecture, and cleanup status before escalating or closing common desktop support tickets.

The manual burden includes:

- Repeating the same workstation checks across multiple devices.
- Losing time gathering basic OS and hardware context.
- Missing low-disk warnings during rushed ticket triage.
- Performing inconsistent temporary-file cleanup between technicians.
- Writing support notes manually instead of generating structured evidence.
- Struggling to prove what maintenance action was completed and when.

## 🛠️ The Automation Framework

The framework is intentionally simple: one local script, clear terminal output, and a generated health report. This makes it suitable for junior technicians, training environments, and repeatable workstation checks.

Design principles:

- **Safe local execution:** The cleanup routine uses a scoped mock temporary directory instead of broad system paths.
- **Repeatable results:** Each run follows the same health-check sequence.
- **Technician-readable output:** Reports summarize system information, disk status, and maintenance actions.
- **Evidence generation:** Each report is timestamped and saved as a text file.
- **Portable runtime:** Python keeps the workflow lightweight across Windows support machines.

## 📂 Automated Modules

### 1. System Audit Module

Implemented in `pc_health_check.py`.

Collects:

- Operating system family.
- OS release version.
- Machine architecture.

Administrative value:

- Gives technicians quick environmental context.
- Helps standardize ticket notes before escalation.

### 2. Storage Monitoring Module

Implemented in `pc_health_check.py`.

Checks:

- Root drive usage.
- Available disk space in GB.
- Low-storage threshold warning under 10 GB.

Administrative value:

- Identifies devices at risk of update, profile, or application failures.
- Creates a repeatable storage health signal.

### 3. Safe Cleanup Module

Implemented in `pc_health_check.py`.

Actions:

- Creates a local `mock_temp_clutter` directory if needed.
- Removes generated temporary files within that controlled directory.
- Tracks the number of files cleaned.

Administrative value:

- Demonstrates maintenance automation without risking real user or system data.
- Provides a safe base pattern for future cleanup expansion.

### 4. Reporting Module

Implemented in `pc_health_check.py`.

Generates:

- `health_report_YYYY-MM-DD_HH-MM-SS.txt`
- OS and architecture summary.
- Available disk space.
- Disk health status.
- Count of cleaned temporary files.

Administrative value:

- Produces evidence suitable for service desk notes.
- Makes routine maintenance auditable.

## Example Report Output

```text
=========================================
IT SUPPORT AUTOMATION REPORT - 2026-06-09 14:35:18.091579
=========================================

Operating System: Windows 11
Machine Architecture: AMD64
Available Disk Space: 386.43 GB
Disk Space Status: Healthy

Maintenance: Cleaned 3 temporary files.

=========================================
```

## Safety and Permissions

This script is designed for safe local execution and does not require administrator privileges in its current form.

Recommended practices:

- Run the script from the repository root so report files are generated in a predictable location.
- Review any future cleanup path changes before using the script on live endpoints.
- Avoid modifying the script to delete broad locations such as `C:\Windows\Temp` or user profile folders without explicit guardrails.
- Keep generated reports out of public repositories if they contain real device or user data.
- Use a dedicated Python installation and verify the `python` command points to the expected runtime.

Windows Python alias troubleshooting:

- If `python pc_health_check.py` opens the Microsoft Store, disable Python App Execution Aliases in Windows Settings.
- Confirm Python with:

```bash
python --version
```

## Local Execution Setup

### Prerequisites

- Windows 10 or Windows 11
- Python 3.x
- Command Prompt or PowerShell

### Run the Health Check

```bash
python pc_health_check.py
```

### Review Generated Reports

```bash
dir health_report_*.txt
```

## Production Readiness Notes

- Add command-line flags for dry-run, cleanup mode, and output directory selection.
- Use JSON or CSV output if reports need to feed an RMM, SIEM, or ticketing platform.
- Add unit tests around disk threshold logic and report generation.
- Introduce explicit allowlists before expanding cleanup to real system paths.
- Consider packaging the script as an internal support utility with versioned releases.
