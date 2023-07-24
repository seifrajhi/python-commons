import os
import re
import subprocess

# Function to run commands with sudo
def run_sudo_command(command):
    return subprocess.check_output(["sudo", "sh", "-c", command], universal_newlines=True)

# Returns true (0) if the given file exists and is a file and false (1) otherwise
def file_exists(file):
    return os.path.isfile(file)

# Returns true (0) if the given file exists contains the given text and false (1) otherwise.
# The given text is a regular expression.
def file_contains_text(text, file):
    try:
        output = subprocess.check_output(["grep", "-q", text, file], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

# Append the given text to the given file using sudo
def file_append_text(text, file):
    run_sudo_command(f"echo -e '{text}' | tee -a '{file}' > /dev/null")

# Replace a line of text that matches the given regular expression in a file with the given replacement. Only works for
# single-line replacements.
def file_replace_text(original_text_regex, replacement_text, file):
    run_sudo_command(f"sed -i'' -e 's|{original_text_regex}|{replacement_text}|' '{file}'")

# Call file_replace_text for each of the files listed in files
def file_replace_text_in_files(original_text_regex, replacement_text, *files):
    for file in files:
        file_replace_text(original_text_regex, replacement_text, file)

# If the given file already contains the original text (which is a regex), replace it with the given replacement.
# If it doesn't contain that text, simply append the replacement text at the end of the file.
def file_replace_or_append_text(original_text_regex, replacement_text, file):
    if file_exists(file) and file_contains_text(original_text_regex, file):
        file_replace_text(original_text_regex, replacement_text, file)
    else:
        file_append_text(replacement_text, file)

# Replace a specific template string in a file with a value. Provided as an array of TEMPLATE-STRING=VALUE
def file_fill_template(file, *auto_fill):
    if not auto_fill:
        print("No auto-fill params specified.")
        return

    for param in auto_fill:
        name, _, value = param.partition("=")
        file_replace_text(name, value, file)
# Function to read the contents of a file
def read_file(file):
    with open(file, "r") as f:
        return f.read()

# Function to write contents to a file
def write_file(file, contents):
    with open(file, "w") as f:
        f.write(contents)

# Function to append contents to a file
def append_file(file, contents):
    with open(file, "a") as f:
        f.write(contents)

# Function to replace a line in a file matching a given regular expression with new contents
def replace_line_in_file(original_text_regex, new_contents, file):
    contents = read_file(file)
    new_contents = re.sub(original_text_regex, new_contents, contents)
    write_file(file, new_contents)

# Function to remove a line from a file that matches a given regular expression
def remove_line_from_file(line_regex, file):
    contents = read_file(file)
    new_contents = re.sub(line_regex, "", contents)
    write_file(file, new_contents)

# Function to get the size of a file in bytes
def file_size(file):
    return os.path.getsize(file)

# Function to get the file permissions in octal format
def file_permissions(file):
    return oct(os.stat(file).st_mode & 0o777)

# Function to change the file permissions using chmod
def change_file_permissions(file, mode):
    run_sudo_command(f"chmod {mode} {file}")

# Function to change the owner and group of a file using chown
def change_file_owner_and_group(file, owner, group):
    run_sudo_command(f"chown {owner}:{group} {file}")

# Function to get the last modified time of a file
def file_last_modified(file):
    return os.path.getmtime(file)

# Function to get the creation time of a file (Note: This may not be available on all systems)
def file_creation_time(file):
    return os.path.getctime(file)

# Function to get the access time of a file
def file_last_accessed(file):
    return os.path.getatime(file)
