Markdown
# IT Support Automation Script

A practical Python command-line utility designed for IT support operations to automate routine workstation maintenance and system auditing.

## Key Features
* **System Auditing:** Automatically detects OS type, release version, and machine architecture.
* **Storage Monitoring:** Checks available storage capacity on the root drive and flags a warning if disk space drops below 10 GB.
* **Automated Maintenance:** Targets and clears localized temporary log clutter safely.
* **Reporting:** Generates a time-stamped text report (`health_report_YYYY-MM-DD.txt`) summarizing findings and actions taken.

## How to Run
1. Ensure you have Python 3.x installed.
2. Clone the repository.
3. Run the script via the terminal:
   ```bash
   python pc_health_check.py
🛠️ Troubleshooting & Core Resolutions
During development and deployment, several standard environment and OS-level issues were encountered and successfully resolved:

1. Windows Python Alias Conflict
Problem: Running python pc_health_check.py initially failed, with Windows intercepting the command and attempting to redirect to the Microsoft Store.

Resolution: Diagnosed as a standard Windows App Execution Alias conflict. Resolved by navigating to Windows Settings > App Execution Aliases and disabling the default App Installer shortcuts for python.exe and python3.exe, allowing the system to use the verified manual installation path.

2. Missing File / Path Execution Errors ([Errno 2])
Problem: The interpreter threw a No such file or directory error when attempting to run the script from the terminal.

Resolution: Identified that the command-line terminal path context did not match the actual file storage location. Resolved by utilizing directory mapping commands (dir) to verify the file placement, ensuring the terminal environment was correctly focused inside the target repository directory (\it-support-automation\).

3. Git Identity Configuration
Problem: Initial deployment to GitHub failed with a fatal error because the local Git environment lacked a verified author identity.

Resolution: Configured global system variables manually using git config --global user.email and git config --global user.name to establish proper cryptographic commit signatures before successfully pushing the code to production.
