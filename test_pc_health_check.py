import os
import glob
from unittest.mock import patch
import pc_health_check

def test_generate_report():
    sys_info = {
        "os": "Windows",
        "version": "10",
        "architecture": "AMD64"
    }
    
    # Run the function
    pc_health_check.generate_report(15.5, sys_info, 3)
    
    # Find the generated file (most recent)
    report_files = glob.glob("health_report_*.txt")
    assert len(report_files) > 0
    report_path = max(report_files, key=os.path.getmtime)
    
    try:
        # Read file and verify contents
        with open(report_path, "r", encoding="utf-8") as f:
            content = f.read()
            assert "Operating System: Windows 10" in content
            assert "Available Disk Space: 15.50 GB" in content
            assert "Cleaned 3 temporary files" in content
            assert "Disk Space Status: Healthy" in content
    finally:
        # Clean up
        if os.path.exists(report_path) and "2026-06-09" not in report_path and "2026-06-24" not in report_path:
            os.remove(report_path)

def test_check_system_and_clean():
    # Mock disk usage and platform to return predictable values
    with patch("shutil.disk_usage", return_value=(100*(2**30), 85*(2**30), 15*(2**30))):
        with patch("platform.system", return_value="Linux"):
            with patch("platform.release", return_value="5.15"):
                with patch("platform.machine", return_value="x86_64"):
                    pc_health_check.check_system_and_clean()
                    
                    # Find and verify report (most recent)
                    report_files = glob.glob("health_report_*.txt")
                    assert len(report_files) > 0
                    report_path = max(report_files, key=os.path.getmtime)
                    try:
                        with open(report_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            assert "Operating System: Linux 5.15" in content
                            assert "Available Disk Space: 15.00 GB" in content
                    finally:
                        if os.path.exists(report_path) and "2026-06-09" not in report_path and "2026-06-24" not in report_path:
                            os.remove(report_path)
