import sys
from datetime import datetime

# Echo to stderr. Useful for printing script usage information.
def echo_stderr(*args):
    print(*args, file=sys.stderr)

# Log the given message at the given level. All logs are written to stderr with a timestamp.
def log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    script_name = sys.argv[0]
    echo_stderr(f"{timestamp} [{level}] [{script_name}] {message}")

# Log the given message at INFO level. All logs are written to stderr with a timestamp.
def log_info(message):
    log("INFO", message)

# Log the given message at WARN level. All logs are written to stderr with a timestamp.
def log_warn(message):
    log("WARN", message)

# Log the given message at ERROR level. All logs are written to stderr with a timestamp.
def log_error(message):
    log("ERROR", message)


# Echo to stderr. Useful for printing script usage information.
def echo_stderr(*args):
    print(*args, file=sys.stderr)

# Log the given message at the given level. All logs are written to stderr with a timestamp.
def log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    script_name = sys.argv[0]
    echo_stderr(f"{timestamp} [{level}] [{script_name}] {message}")

# Log the given message at INFO level. All logs are written to stderr with a timestamp.
def log_info(message):
    log("INFO", message)

# Log the given message at WARN level. All logs are written to stderr with a timestamp.
def log_warn(message):
    log("WARN", message)

# Log the given message at ERROR level. All logs are written to stderr with a timestamp.
def log_error(message):
    log("ERROR", message)

# Log the given message at DEBUG level. All logs are written to stderr with a timestamp.
def log_debug(message):
    log("DEBUG", message)

# Set the logging level for the script. Messages below this level will not be logged.
def set_logging_level(level):
    levels = ["DEBUG", "INFO", "WARN", "ERROR"]
    if level not in levels:
        raise ValueError(f"Invalid logging level. Expected one of: {', '.join(levels)}")
    setattr(sys.modules['__main__'], '_logging_level', level)

# Log the given message at the specified level if it is enabled by the current logging level.
def conditional_log(level, message):
    current_level = getattr(sys.modules['__main__'], '_logging_level', "INFO")
    if level == "DEBUG" and current_level == "DEBUG":
        log(level, message)
    elif level == "INFO" and current_level in ["DEBUG", "INFO"]:
        log(level, message)
    elif level == "WARN" and current_level in ["DEBUG", "INFO", "WARN"]:
        log(level, message)
    elif level == "ERROR" and current_level in ["DEBUG", "INFO", "WARN", "ERROR"]:
        log(level, message)

# Function to enable verbose logging (equivalent to setting logging level to "DEBUG").
def enable_verbose_logging():
    set_logging_level("DEBUG")

# Function to enable quiet logging (equivalent to setting logging level to "WARN").
def enable_quiet_logging():
    set_logging_level("WARN")
