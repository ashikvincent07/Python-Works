system_log_path = "file-operations\\system_log\\system_log.txt"

error_log_path = "file-operations\\system_log\\error_log.txt"

info_log_path = "file-operations\\system_log\\info_log.txt"

warning_log_path = "file-operations\\system_log\\warning_log.txt"

fr_system_log = open(system_log_path, "r")

fw_error_log = open(error_log_path, "w")

fw_info_log = open(info_log_path, "w")

fw_warning_log = open(warning_log_path, "w")

for line in fr_system_log:
    log = line.rstrip("\n")

    if "INFO" in log:
        fw_info_log.write(log + "\n")
    
    elif "ERROR" in log:
        fw_error_log.write(log + "\n")

    elif "WARNING" in log:
        fw_warning_log.write(log + "\n")

print("program end")

