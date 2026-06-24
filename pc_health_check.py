import os
import platform
import shutil
from datetime import datetime


def generate_report(disk_free_gb, system_info, cleaned_files_count):
    """Generate a text report of the system health check."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"health_report_{timestamp}.txt"

    with open(report_filename, "w", encoding="utf-8") as report:
        report.write("=========================================\n")
        report.write(f"IT SUPPORT AUTOMATION REPORT - {datetime.now()}\n")
        report.write("=========================================\n\n")
        report.write(f"Operating System: {system_info['os']} {system_info['version']}\n")
        report.write(f"Machine Architecture: {system_info['architecture']}\n")
        report.write(f"Available Disk Space: {disk_free_gb:.2f} GB\n")

        if disk_free_gb < 10:
            report.write("WARNING: Low disk space (under 10 GB available).\n")
        else:
            report.write("Disk Space Status: Healthy\n")

        report.write(f"\nMaintenance: Cleaned {cleaned_files_count} temporary files.\n")
        report.write("\n=========================================\n")

    print(f"[OK] Report successfully generated: {report_filename}")


def check_system_and_clean():
    print("[INFO] Starting system health check and maintenance...")

    sys_info = {
        "os": platform.system(),
        "version": platform.release(),
        "architecture": platform.machine(),
    }

    total, used, free = shutil.disk_usage("/")
    free_gb = free / (2**30)

    cleaned_count = 0
    target_temp_dir = "./mock_temp_clutter"

    if not os.path.exists(target_temp_dir):
        os.makedirs(target_temp_dir)
        for i in range(3):
            with open(
                os.path.join(target_temp_dir, f"temp_log_{i}.txt"),
                "w",
                encoding="utf-8",
            ) as temp_file:
                temp_file.write("Temporary log data.")

    try:
        for filename in os.listdir(target_temp_dir):
            file_path = os.path.join(target_temp_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                cleaned_count += 1
        os.rmdir(target_temp_dir)
    except Exception as exc:
        print(f"[WARN] Error during cleanup: {exc}")

    generate_report(free_gb, sys_info, cleaned_count)


if __name__ == "__main__":
    check_system_and_clean()
