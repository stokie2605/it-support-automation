# IT Support Automation
> **The 1-Line Mission:** Python-based CLI workstation audit tool automating hardware diagnostics, partition metrics collection, and scoped temporary file cleaning for IT support teams.

### ⚡ Engineering Breakdown
* **The Problem:** Tier-1 support technicians waste manual labor running identical workstation diagnostics and clearing temporary user caches, resulting in non-standardized ticket notes and zero auditable evidence of completed maintenance.
* **The Solution:** A modular Python CLI utility using native platform and storage library calls (`platform`, `shutil`) to inspect OS variables, compute disk allocation, run scoped temporary directory purge loops, and output timestamped, parser-friendly text reports.
* **The Tech Stack:** `Python` `Pytest` `GitHub Actions`
