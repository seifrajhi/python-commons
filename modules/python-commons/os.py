import os
import pwd
import subprocess

# Return the available memory on the current OS in MB
def os_get_available_memory_mb():
    total_memory_kb = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    return total_memory_kb / 1024

# Returns true (0) if this is an Amazon Linux server at the given version or false (1) otherwise. The version number
# can use regex. If you don't care about the version, leave it unspecified.
def os_is_amazon_linux(version=None):
    release_info = read_release_info()
    return is_matching_version("Amazon Linux", version, release_info)

# Returns true (0) if this is an Ubuntu server at the given version or false (1) otherwise. The version number
# can use regex. If you don't care about the version, leave it unspecified.
def os_is_ubuntu(version=None):
    release_info = read_release_info()
    return is_matching_version("Ubuntu", version, release_info)

# Returns true (0) if this is a CentOS server at the given version or false (1) otherwise. The version number
# can use regex. If you don't care about the version, leave it unspecified.
def os_is_centos(version=None):
    release_info = read_release_info()
    return is_matching_version("CentOS Linux", version, release_info)

# Returns true (0) if this is a RedHat server at the given version or false (1) otherwise. The version number
# can use regex. If you don't care about the version, leave it unspecified.
def os_is_redhat(version=None):
    release_info = read_release_info()
    return is_matching_version("Red Hat Enterprise Linux Server", version, release_info)

# Returns true (0) if this is an OS X server or false (1) otherwise.
def os_is_darwin():
    return sys.platform == "darwin"

# Validate that the given file has the given checksum of the given checksum type, where type is one of "md5" or
# "sha256".
def os_validate_checksum(filepath, checksum, checksum_type):
    command = None
    if checksum_type == "sha256":
        command = ["shasum", "-a", "256", "-c", "-"]
    elif checksum_type == "md5":
        command = ["md5sum", "-c", "-"]
    else:
        raise ValueError("Unsupported checksum type: " + checksum_type)

    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, text=True, universal_newlines=True)
        process.communicate(input=f"{checksum} {filepath}\n")
        if process.returncode != 0:
            raise ValueError("Checksum validation failed.")
    except FileNotFoundError:
        raise FileNotFoundError("Checksum command not found. Make sure the command is installed on your system.")

# Returns true (0) if this the given command/app is installed and on the PATH or false (1) otherwise.
def os_command_is_installed(name):
    try:
        subprocess.run(["which", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Get the username of the current OS user
def os_get_current_users_name():
    return pwd.getpwuid(os.getuid()).pw_name

# Get the name of the primary group for the current OS user
def os_get_current_users_group():
    return pwd.getpwuid(os.getuid()).pw_name

# Returns true (0) if the current user is root or sudo and false (1) otherwise.
def os_user_is_root_or_sudo():
    return os.geteuid() == 0

# Returns a zero exit code if the given $username exists
def os_user_exists(username):
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

# Create an OS user whose name is $username. If true is passed in as the second arg, run the commands with sudo.
def os_create_user(username, with_sudo=False):
    if os_user_exists(username):
        log_info(f"User {username} already exists. Will not create again.")
    else:
        log_info(f"Creating user named {username}")
        command = ["useradd", username]
        if with_sudo:
            command.insert(0, "sudo")
        subprocess.run(command, check=True)

# Change the owner of $dir to $username. If true is passed in as the last arg, run the command with sudo.
def os_change_dir_owner(dir, username, with_sudo=False):
    log_info(f"Changing ownership of {dir} to {username}")
    command = ["chown", "-R", f"{username}:{username}", dir]
    if with_sudo:
        command.insert(0, "sudo")
    subprocess.run(command, check=True)

# Helper function to read release information from /etc/*release files
def read_release_info():
    release_info = {}
    release_files = ["/etc/os-release", "/usr/lib/os-release", "/etc/centos-release"]
    for file in release_files:
        if os.path.isfile(file):
            with open(file) as f:
                for line in f:
                    key, _, value = line.strip().partition("=")
                    if key and value:
                        release_info[key] = value.strip('"')
    return release_info

# Helper function to check if the given OS version matches the provided pattern
def is_matching_version(os_name, version, release_info):
    if "NAME" in release_info and release_info["NAME"] == os_name:
        if not version:
            return True
        if "VERSION_ID" in release_info and re.match(version, release_info["VERSION_ID"]):
            return True
    return False
