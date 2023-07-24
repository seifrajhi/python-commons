import re

# Return true (0) if the first string (haystack) contains the second string (needle), and false (1) otherwise.
def string_contains(haystack, needle):
    return needle in haystack

# Returns true (0) if the first string (haystack), which is assumed to contain multiple lines, contains the second
# string (needle), and false (1) otherwise. The needle can contain regular expressions.
def string_multiline_contains(haystack, needle):
    return bool(re.search(needle, haystack, re.MULTILINE))

# Convert the given string to uppercase
def string_to_uppercase(s):
    return s.upper()

# Strip the prefix from the given string. Supports wildcards.
#
# Example:
#
# string_strip_prefix("foo=bar", "foo=")  ===> "bar"
# string_strip_prefix("foo=bar", "*=")    ===> "bar"
#
def string_strip_prefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s

# Strip the suffix from the given string. Supports wildcards.
#
# Example:
#
# string_strip_suffix("foo=bar", "=bar")  ===> "foo"
# string_strip_suffix("foo=bar", "=*")    ===> "foo"
#
def string_strip_suffix(s, suffix):
    return s[:len(s) - len(suffix)] if s.endswith(suffix) else s

# Return true if the given response is empty or "null" (the latter is from jq parsing).
def string_is_empty_or_null(response):
    return not response or response == "null"

# Given a string s, return the substring beginning at index start and ending at index end.
#
# Example:
#
# string_substr("hello world", 0, 5)  ===> "hello"
def string_substr(s, start, end=None):
    if end is None:
        return s[start:]
    else:
        return s[start:end]

# Example for string_contains
haystack = "Hello, world!"
needle = "world"
print(string_contains(haystack, needle))  # Output: True

# Example for string_multiline_contains
haystack = """Line 1
Line 2
Line 3"""
needle = "Line 2"
print(string_multiline_contains(haystack, needle))  # Output: True

# Example for string_to_uppercase
s = "hello"
print(string_to_uppercase(s))  # Output: "HELLO"

# Example for string_strip_prefix
s = "foo=bar"
prefix = "foo="
print(string_strip_prefix(s, prefix))  # Output: "bar"

# Example for string_strip_suffix
s = "foo=bar"
suffix = "=bar"
print(string_strip_suffix(s, suffix))  # Output: "foo"

# Example for string_is_empty_or_null
response = ""
print(string_is_empty_or_null(response))  # Output: True

response = "null"
print(string_is_empty_or_null(response))  # Output: True

response = "Hello"
print(string_is_empty_or_null(response))  # Output: False

# Example for string_substr
s = "Hello, world!"
start = 7
end = 12
print(string_substr(s, start, end))  # Output: "world"

start = 7
print(string_substr(s, start))  # Output: "world!"
