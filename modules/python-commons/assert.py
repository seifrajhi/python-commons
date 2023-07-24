import sys
import subprocess
from os import geteuid
from os.path import abspath, dirname, join

# Source the required modules (Python files)
sys.path.append(abspath(join(dirname(__file__), "modules", "bash-commons", "src")))
from log import log_error
from array import array_contains
from string import string_is_empty_or_null
from os import geteuid as os_user_is_root_or_sudo

def assert_is_installed(name):
    """
    Check that the given binary is available on the PATH. If it's not, raise an exception.
    """
    try:
        subprocess.run(["which", name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        log_error(f"The command '{name}' is required by this script but is not installed or in the system's PATH.")
        raise

def assert_not_empty(arg_name, arg_value, reason=""):
    """
    Check that the value of the given arg is not empty. If it is, raise an exception.
    """
    if not arg_value:
        log_error(f"The value for '{arg_name}' cannot be empty. {reason}")
        raise ValueError(f"The value for '{arg_name}' cannot be empty. {reason}")

def assert_empty(arg_name, arg_value, reason=""):
    """
    Check that the value of the given arg is empty. If it isn't, raise an exception.
    """
    if arg_value:
        log_error(f"The value for '{arg_name}' must be empty. {reason}")
        raise ValueError(f"The value for '{arg_name}' must be empty. {reason}")

def assert_not_empty_or_null(response, description=""):
    """
    Check that the given response from AWS is not empty or null. If it is, raise an exception.
    """
    if string_is_empty_or_null(response):
        log_error(f"Got empty response for {description}")
        raise ValueError(f"Got empty response for {description}")

def assert_value_in_list(arg_name, arg_value, *lst):
    """
    Check that the given value is one of the values from the given list. If not, raise an exception.
    """
    if arg_value not in lst:
        log_error(f"'{arg_value}' is not a valid value for {arg_name}. Must be one of: {', '.join(map(repr, lst))}.")
        raise ValueError(f"'{arg_value}' is not a valid value for {arg_name}. Must be one of: {', '.join(map(repr, lst))}.")

def assert_exactly_one_of(*args):
    """
    Reads in a list of keys and values and asserts that one and only one of the values is set.
    This is useful for command line options that are mutually exclusive.
    """
    num_args = len(args)
    if num_args % 2 != 0:
        log_error(f"This script expects an even number of arguments but received {num_args} instead.")
        raise ValueError("This script expects an even number of arguments but received an odd number.")

    num_non_empty = 0
    arg_names = []

    # Determine how many arg_vals are non-empty
    for i in range(0, num_args, 2):
        arg_names.append(args[i])
        if args[i + 1]:
            num_non_empty += 1

    if num_non_empty != 1:
        log_error(f"Exactly one of {', '.join(arg_names)} must be set.")
        raise ValueError(f"Exactly one of {', '.join(arg_names)} must be set.")

def assert_uid_is_root_or_sudo():
    """
    Check that this script is running as root or sudo and raise an exception if it's not.
    """
    if geteuid() != 0:
        log_error("This script should be run using sudo or as the root user.")
        raise PermissionError("This script should be run using sudo or as the root user.")

def assert_user_has_sudo_perms():
    """
    Assert that the user running this script has permissions to run sudo.
    """
    try:
        subprocess.run(["sudo", "-n", "true"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        log_error("This script should be run using sudo, as the root user, or as a user with sudo permissions.")
        raise PermissionError("This script should be run using sudo, as the root user, or as a user with sudo permissions.")
def assert_file_exists(file_path):
    """
    Check that the given file exists. If it doesn't, raise an exception.

    Examples:
    assert_file_exists("/path/to/file.txt")
    """
    if not os.path.exists(file_path):
        log_error(f"The file '{file_path}' does not exist.")
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

def assert_directory_exists(dir_path):
    """
    Check that the given directory exists. If it doesn't, raise an exception.

    Examples:
    assert_directory_exists("/path/to/directory")
    """
    if not os.path.isdir(dir_path):
        log_error(f"The directory '{dir_path}' does not exist.")
        raise NotADirectoryError(f"The directory '{dir_path}' does not exist.")

def assert_file_readable(file_path):
    """
    Check that the given file is readable. If it's not, raise an exception.

    Examples:
    assert_file_readable("/path/to/file.txt")
    """
    if not os.access(file_path, os.R_OK):
        log_error(f"The file '{file_path}' is not readable.")
        raise PermissionError(f"The file '{file_path}' is not readable.")

def assert_file_writable(file_path):
    """
    Check that the given file is writable. If it's not, raise an exception.

    Examples:
    assert_file_writable("/path/to/file.txt")
    """
    if not os.access(file_path, os.W_OK):
        log_error(f"The file '{file_path}' is not writable.")
        raise PermissionError(f"The file '{file_path}' is not writable.")

def assert_value_not_none(value, name):
    """
    Check that the given value is not None. If it is, raise an exception.

    Examples:
    assert_value_not_none(some_variable, "some_variable")
    """
    if value is None:
        log_error(f"The value for '{name}' cannot be None.")
        raise ValueError(f"The value for '{name}' cannot be None.")

def assert_list_not_empty(lst, name):
    """
    Check that the given list is not empty. If it is, raise an exception.

    Examples:
    assert_list_not_empty(some_list, "some_list")
    """
    if not lst:
        log_error(f"The list '{name}' cannot be empty.")
        raise ValueError(f"The list '{name}' cannot be empty.")

def assert_dict_not_empty(dct, name):
    """
    Check that the given dictionary is not empty. If it is, raise an exception.

    Examples:
    assert_dict_not_empty(some_dict, "some_dict")
    """
    if not dct:
        log_error(f"The dictionary '{name}' cannot be empty.")
        raise ValueError(f"The dictionary '{name}' cannot be empty.")
