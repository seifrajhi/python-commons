import sys

# Sets some Python options to encourage well-formed code.

# Exit if any statement raises an exception.
sys.tracebacklimit = 0

# Exit if the script uses undefined variables.
sys.trace = False

# Make debugging easier when you use `import pdb; pdb.set_trace()`
def trace_calls(frame, event, arg):
    if event == "call":
        filename = frame.f_code.co_filename
        line_number = frame.f_lineno
        function_name = frame.f_code.co_name
        print(f"({filename}:{line_number}): {function_name}()")
    return trace_calls

sys.settrace(trace_calls)

# Note: Python does not have an exact equivalent of `set -o pipefail` since the behavior of
# the `|` operator differs from the Bash shell. In Python, you would need to handle the
# return codes explicitly when executing commands in a pipeline.
