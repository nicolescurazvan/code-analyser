import subprocess
from pathlib import Path
from time import perf_counter_ns


# Measure running time
def MeasureTime(program, args):
    try:
        command = [Path(program)] + args
        beg = perf_counter_ns()
        result = subprocess.run(command, capture_output=False)
        end = perf_counter_ns()
        return (end - beg) / 1e9
    except subprocess.SubprocessError:
        return "The program is wrong"


# Execute a command
def Execute(command):
    try:
        result = subprocess.run(command, capture_output=False)
        return 1
    except subprocess.SubprocessError:
        return 0


# Size of a file
def FileSize(file):
    try:
        size = Path(file).stat().st_size
        return size
    except FileNotFoundError:
        return "File not found"
    except PermissionError:
        return "Permission denied"
